"""Independent integrals, exact identities, and numerical failure contracts."""

from math import comb, factorial

import numpy as np
from numpy.testing import assert_allclose
import pytest
from scipy.integrate import quad
from scipy.stats import gamma, norm, t

from xmath.incerto.concentration import (
    estimate_sum_mad, gamma_sum_mad, gaussian_equivalent_n, gaussian_sum_mad,
    kappa_from_mads, lognormal_sum_mad, normal_location_mixture_sum_mad,
    stable_kappa, student_sum_mad,
)


@pytest.mark.parametrize("n", [1, 2, 7, 50])
@pytest.mark.parametrize("shape", [.3, 1, 2.5])
def test_gamma_against_upper_deviation_integral(n, shape):
    law = gamma(n*shape, scale=1.3)
    mean = law.mean()
    integral = 2*quad(lambda x: (x-mean)*law.pdf(x), mean, np.inf, epsabs=1e-9)[0]
    assert gamma_sum_mad(n, shape=shape, scale=1.3) == pytest.approx(integral, rel=1e-8)


@pytest.mark.parametrize("nu", [1.1, 1.5, 2, 3, 5, 30])
def test_student_single_and_pair_against_conditional_integral(nu):
    law = t(nu)
    m1 = 2*quad(lambda x: x*law.pdf(x), 0, np.inf)[0]
    assert student_sum_mad(1, nu=nu) == pytest.approx(m1, rel=1e-8)
    # Different route: E|X+y| = y*(2F(y)-1) + 2*(nu+y*y)/(nu-1)*f(y).
    # Symmetry reduces the outer integral to the positive half-line.
    def integrand(y):
        inner = y*(2*law.cdf(y)-1) + 2*(nu+y*y)/(nu-1)*law.pdf(y)
        return 2*inner*law.pdf(y)
    expected = quad(integrand, 0, np.inf, epsabs=1e-8)[0]
    assert student_sum_mad(2, nu=nu) == pytest.approx(expected, rel=2e-8)


@pytest.mark.parametrize("n", [1, 2, 3, 8, 30, 100])
def test_cubic_student_against_cf_mad_integral(n):
    # Integration by parts of (1-phi(t)**n)/t**2, then u=sqrt(3)*t.
    expected = 2*np.sqrt(3)/np.pi * quad(
        lambda u: n*np.exp((n-1)*np.log1p(u)-n*u), 0, np.inf)[0]
    assert student_sum_mad(n) == pytest.approx(expected, rel=1e-10)


def test_cubic_student_finite_polynomial_and_asymptotic_constants():
    for n in range(1, 12):
        ratio = factorial(n)/n**n * sum(n**k/factorial(k) for k in range(n))
        assert student_sum_mad(n)/student_sum_mad(1) == pytest.approx(ratio)
    n = 10_000_000
    assert student_sum_mad(n)/np.sqrt(n) == pytest.approx(np.sqrt(6/np.pi), rel=.0002)
    # The finite-n log*kappa correction is appreciable; test the exact
    # implied constant 2 log(M(n)^2/(n M(1)^2)), rather than a loose plot.
    constant = 4*np.log(student_sum_mad(n)/(np.sqrt(n)*student_sum_mad(1)))
    assert constant == pytest.approx(2*np.log(np.pi/2), abs=.001)
    assert 4*np.log(gamma_sum_mad(n)/(np.sqrt(n)*gamma_sum_mad(1))) == pytest.approx(
        4-2*np.log(2*np.pi), abs=1e-6)


@pytest.mark.parametrize("n", [9999, 10000, 10001, 1_000_000])
def test_gamma_stirling_switch_against_density_at_mean(n):
    # SciPy uses its independent Gamma log density implementation.
    expected = 2*n*gamma.pdf(n, a=n)
    assert gamma_sum_mad(n) == pytest.approx(expected, rel=1e-8)


def test_gaussian_and_stable_benchmarks_and_scale_invariance():
    for n0, n in [(1, 2), (1, 30), (5, 200)]:
        assert kappa_from_mads(gaussian_sum_mad(n0), gaussian_sum_mad(n), n, n0=n0) == pytest.approx(0, abs=1e-14)
        for alpha in (1.2, 1.5, 2):
            assert kappa_from_mads(n0**(1/alpha), n**(1/alpha), n, n0=n0) == pytest.approx(stable_kappa(alpha))
    for scale in (1e-200, 1, 1e200):
        assert kappa_from_mads(scale, 1.5*scale, 2) == pytest.approx(2-np.log(2)/np.log(1.5))
    assert np.isnan(stable_kappa(.8)) and np.isnan(stable_kappa(1))
    assert stable_kappa(2) == 0


def test_negative_kappa_for_unimodal_triangle():
    # X=U1+U2 with iid uniform[-1,1]; direct Irwin-Hall positive-part integral.
    def uniform_sum_mad(m):
        return 4/factorial(m+1)*sum((-1)**k*comb(m,k)*max(m/2-k, 0)**(m+1)
                                   for k in range(m+1))
    assert uniform_sum_mad(2) == pytest.approx(2/3)
    assert uniform_sum_mad(4) == pytest.approx(14/15)
    assert kappa_from_mads(2/3, 14/15, 2) < 0


@pytest.mark.parametrize("a", [0, .5, 2, 8])
@pytest.mark.parametrize("n", [1, 2, 7])
def test_location_mixture_against_normal_absolute_integral(a, n):
    integral = sum(comb(n,k)/2**n * quad(
        lambda z: abs(a*(2*k-n)+np.sqrt(n)*z)*norm.pdf(z),
        -12, 12, points=[np.clip(-a*(2*k-n)/np.sqrt(n), -12, 12)],
        epsabs=1e-8)[0] for k in range(n+1))
    assert normal_location_mixture_sum_mad(n, a) == pytest.approx(integral, rel=1e-8)


@pytest.mark.parametrize("sigma", [.15, .8, 2, 4])
def test_lognormal_conditional_mc_against_independent_2d_integral(sigma):
    # A direct lower-tail integral for two independent normalized lognormals;
    # condition on Z1 and integrate Z2's put using a different scipy API.
    from scipy.stats import lognorm
    law = lognorm(sigma, scale=np.exp(-sigma*sigma/2))
    cutoff = np.log(2)/sigma+sigma/2
    def integrand(z):
        a = 2-np.exp(sigma*z-sigma*sigma/2)
        if a <= 0:
            return 0
        upper_z = (np.log(a)+sigma*sigma/2)/sigma
        truncated_mean = norm.cdf(upper_z-sigma)
        return 2*(a*law.cdf(a)-truncated_mean)*norm.pdf(z)
    expected = quad(integrand, -12, cutoff, epsabs=1e-10)[0]
    result = lognormal_sum_mad(2, sigma, mu=-sigma*sigma/2, repetitions=40000, random_state=123)
    assert abs(result['mad']-expected) < 6*result['mc_se'] + 1e-8
    exact_single = 2*quad(lambda x: (1-x)*law.pdf(x), 0, 1, epsabs=1e-9)[0]
    assert lognormal_sum_mad(1, sigma, mu=-sigma*sigma/2)['mad'] == pytest.approx(exact_single, rel=1e-8)


def test_estimators_center_seed_and_known_gaussian_target():
    first = estimate_sum_mad(norm(loc=3, scale=2), 10, mean=3, repetitions=20000, random_state=8)
    assert first == estimate_sum_mad(norm(loc=3, scale=2), 10, mean=3, repetitions=20000, random_state=8)
    assert abs(first['mad']-gaussian_sum_mad(10, sigma=2)) < 6*first['mc_se']
    one = lognormal_sum_mad(8, 1, random_state=8)
    two = lognormal_sum_mad(8, 1, mu=np.log(3), random_state=8)
    assert_allclose(list(two.values()), 3*np.array(list(one.values())))
    huge_sigma = lognormal_sum_mad(8, 10, mu=-50, random_state=4)
    assert huge_sigma['mad'] == pytest.approx(16, rel=.001)


@pytest.mark.parametrize("n_g", [1, 2, 30, 1000])
def test_sample_sufficiency_matches_exhaustive_search(n_g):
    for law in (gaussian_sum_mad, gamma_sum_mad, student_sum_mad):
        answer = gaussian_equivalent_n(law, n_g, max_n=10000)
        exhaustive = next(n for n in range(1, 10001) if law(n)/(n*law(1)) <= 1/np.sqrt(n_g)*(1+2e-15))
        assert answer == exhaustive
    assert gaussian_equivalent_n(lambda n: float(n), n_g, max_n=100) == (1 if n_g == 1 else None)


def test_metric_edge_cases():
    assert np.isnan(kappa_from_mads(0, 0, 2))
    assert np.isnan(kappa_from_mads(np.inf, np.inf, 2))
    assert np.isneginf(kappa_from_mads(1, 1, 2))
    assert np.isposinf(student_sum_mad(100, nu=1))
    assert gaussian_equivalent_n(student_sum_mad, 30, max_n=10) is None
    with pytest.raises(FloatingPointError):
        gamma_sum_mad(10, scale=1e308)
    with pytest.raises(FloatingPointError):
        lognormal_sum_mad(1, 1, mu=1000)
    class Bad:
        def rvs(self, size, random_state):
            return np.full(size, np.inf)
    with pytest.raises(FloatingPointError):
        estimate_sum_mad(Bad(), 2, mean=0)


def test_gaussian_search_does_not_step_past_rounded_equalities():
    for n in range(1, 500):
        assert gaussian_equivalent_n(gaussian_sum_mad, n) == n


@pytest.mark.parametrize("scale", [1e-300, 1e-200, 1, 1e200, 1e300])
def test_gaussian_search_is_invariant_to_extreme_units(scale):
    for n in (2, 3, 4, 16, 30, 257, 10000, 10_000_000):
        # Independent Gaussian MAD curve, with single-observation MAD=scale.
        assert gaussian_equivalent_n(lambda k: scale*np.sqrt(k), n,
                                     max_n=n) == n
        assert gaussian_equivalent_n(lambda k: gaussian_sum_mad(k, sigma=scale),
                                     n, max_n=n) == n


def test_gaussian_mad_preserves_finite_overflow_contract():
    assert gaussian_sum_mad(2, sigma=1e308) == pytest.approx(2/np.sqrt(np.pi)*1e308)
    with pytest.raises(FloatingPointError):
        gaussian_sum_mad(10, sigma=1e308)


@pytest.mark.parametrize("call", [
    lambda: gaussian_sum_mad(True), lambda: gaussian_sum_mad(1.5),
    lambda: gaussian_sum_mad(1, sigma=0), lambda: gamma_sum_mad(1, shape=0),
    lambda: gamma_sum_mad(1, shape=1e7), lambda: student_sum_mad(3, nu=5),
    lambda: student_sum_mad(1, nu=1001), lambda: stable_kappa(2.1),
    lambda: stable_kappa(np.nan), lambda: kappa_from_mads(1, .9, 2),
    lambda: kappa_from_mads(1, 2, 1), lambda: kappa_from_mads(np.nan, 2, 2),
    lambda: kappa_from_mads(1j, 2, 2), lambda: kappa_from_mads(-1, 2, 2),
    lambda: lognormal_sum_mad(1, 0), lambda: lognormal_sum_mad(1, 11),
    lambda: lognormal_sum_mad(1000000, 1), lambda: lognormal_sum_mad(2, 1, repetitions=1),
    lambda: estimate_sum_mad(norm(), 1, mean=0, repetitions=1),
    lambda: normal_location_mixture_sum_mad(1, -1),
    lambda: normal_location_mixture_sum_mad(10001, 1),
    lambda: gaussian_equivalent_n(lambda n: 0, 30),
    lambda: gaussian_equivalent_n(gaussian_sum_mad, 0),
])
def test_input_contracts(call):
    with pytest.raises(ValueError):
        call()
