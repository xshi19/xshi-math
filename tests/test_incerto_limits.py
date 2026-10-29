"""Independent analytic checks and failure policies for chapter 7 helpers."""

from decimal import Decimal, localcontext

import numpy as np
from numpy.testing import assert_allclose
import pytest
from scipy.integrate import quad
from scipy.stats import binom, expon, norm, poisson

from xmath.incerto.limits import (
    bernoulli_chernoff_log_bound, pareto_capped_mean,
    pareto_plugin_nonfinite_probability, repeated_centered_sums,
    symmetric_stable_mean_abs,
)


@pytest.mark.parametrize("alpha", [.2, .8, 1-1e-10, 1, 1+1e-10, 1.3, 5])
@pytest.mark.parametrize("cap", [.5, 2, 10, 1000])
def test_capped_pareto_against_survival_integral(alpha, cap):
    x_m = 2
    expected = min(cap, x_m)
    if cap > x_m:
        expected += quad(lambda x: (x_m/x)**alpha, x_m, cap, epsabs=1e-10)[0]
    assert pareto_capped_mean(cap, alpha, x_m=x_m) == pytest.approx(expected)
    assert 0 <= pareto_capped_mean(cap, alpha, x_m=x_m) <= cap*(1+1e-14)


def test_cap_is_not_indicator_truncation_and_preserves_scaling():
    assert pareto_capped_mean(1, 2) == 1  # indicator-truncated moment is zero
    assert_allclose(pareto_capped_mean([0, .5, 1, 10], 1), [0, .5, 1, 1+np.log(10)])
    assert_allclose(pareto_capped_mean([2, 20], 1.3, x_m=2),
                    2*pareto_capped_mean([1, 10], 1.3))
    assert pareto_capped_mean(1e300, .5, x_m=1e-300) == pytest.approx(2)


@pytest.mark.parametrize("alpha", [1.1, 1.5, 2])
def test_stable_mean_deviation_against_cf_integral(alpha):
    scale = 1.7
    # Work in t, independently of the helper's gamma formula.
    val = quad(lambda t: -np.expm1(-(scale*t)**alpha)/t**2, 0, 1,
               epsabs=1e-9)[0] + quad(lambda t: -np.expm1(-(scale*t)**alpha)/t**2,
                                    1, np.inf, epsabs=1e-9)[0]
    assert symmetric_stable_mean_abs(alpha, scale=scale) == pytest.approx(2*val/np.pi, rel=2e-8)


def test_stable_gaussian_scale_boundary_and_averaging():
    for n in (1, 10, 10000):
        assert symmetric_stable_mean_abs(2, scale=3, n=n) == pytest.approx(6/np.sqrt(np.pi*n))
    for a in (.5, 1):
        assert np.isposinf(symmetric_stable_mean_abs(a, n=1000))
    assert symmetric_stable_mean_abs(1.5, n=1000) == pytest.approx(symmetric_stable_mean_abs(1.5)/10)
    with pytest.raises(FloatingPointError):
        symmetric_stable_mean_abs(1.01, scale=1e308)


@pytest.mark.parametrize("alpha", [.8, 1, 1.5, 4])
@pytest.mark.parametrize("n", [1, 3, 30])
def test_plugin_probability_against_poisson_duality(alpha, n):
    # P(Gamma(n,rate alpha) >= n) = P(Poisson(alpha*n) <= n-1).
    assert pareto_plugin_nonfinite_probability(alpha, n) == pytest.approx(poisson.cdf(n-1, alpha*n))


@pytest.mark.parametrize("p,q,n", [(.5, .75, 20), (.2, .7, 17), (.9, .99, 31), (.5, 1, 100)])
def test_bernoulli_bound_covers_exact_tail_and_markov_tilt(p, q, n):
    result = bernoulli_chernoff_log_bound(p, q, n)
    exact = binom.logsf(int(np.ceil(q*n))-1, n, p)
    assert exact <= result + 1e-12
    if q == 1:
        assert result == pytest.approx(n*np.log(p))
    else:
        t = np.log(q*(1-p)/(p*(1-q)))
        assert result == pytest.approx(n*(np.log1p(p*np.expm1(t))-t*q))
        # Any other tilt is at least as loose.
        for alternative in (t/2, t*2):
            assert result <= n*(np.log1p(p*np.expm1(alternative))-alternative*q)+1e-12
    assert bernoulli_chernoff_log_bound(p, p/2, n) == 0


@pytest.mark.parametrize("p,q", [(.35, .350000001), (.5, .50000001), (.2, .200000001)])
def test_bernoulli_near_mean_large_n_against_high_precision(p, q):
    n = 2**53
    with localcontext() as context:
        context.prec = 80
        dp, dq = Decimal.from_float(p), Decimal.from_float(q)
        divergence = dq*(dq/dp).ln() + (1-dq)*((1-dq)/(1-dp)).ln()
        expected = float(-n*divergence)
    result = bernoulli_chernoff_log_bound(p, q, n)
    assert result == pytest.approx(expected, rel=2e-7, abs=1e-10)
    # Berry--Esseen supplies an independent lower bound on the actual tail.
    # The event at the next integer is contained in {S_n >= n*q}.
    z = (np.ceil(n*q)-n*p)/np.sqrt(n*p*(1-p))
    lower = norm.sf(z) - 3*(p*p+(1-p)**2)/np.sqrt(n*p*(1-p))
    assert np.exp(result) >= lower


def test_repeated_sums_constant_center_shift_seed_and_budget():
    class Constant:
        def rvs(self, size, random_state):
            return np.full(size, 3.)
    assert_allclose(repeated_centered_sums(Constant(), [2, 5], center=1, repetitions=3),
                    [[4]*3, [10]*3])
    first = repeated_centered_sums(norm(), [3, 20], repetitions=17, random_state=9)
    second = repeated_centered_sums(norm(), [3, 20], repetitions=17, random_state=9)
    assert_allclose(first, second, rtol=0, atol=0)
    shifted = repeated_centered_sums(norm(), [3, 20], center=2, repetitions=17, random_state=9)
    assert_allclose(shifted, first-np.array([6, 40])[:, None])
    # For the normal generator, batching does not change the stream.
    assert_allclose(first, repeated_centered_sums(norm(), [3, 20], repetitions=17,
                                                  random_state=9, batch=1))
    with pytest.raises(ValueError, match="budget"):
        repeated_centered_sums(norm(), [1000000], repetitions=51)


@pytest.mark.parametrize("value", [np.inf, np.nan, 1j])
def test_nonfinite_draws_are_not_removed(value):
    class Invalid:
        def rvs(self, size, random_state):
            return np.full(size, value)
    with pytest.raises(FloatingPointError):
        repeated_centered_sums(Invalid(), [2], repetitions=1)


@pytest.mark.parametrize("call", [
    lambda: pareto_capped_mean(-1, 1), lambda: pareto_capped_mean(np.inf, 1),
    lambda: pareto_capped_mean([1, 2j], 1), lambda: pareto_capped_mean(1, 0),
    lambda: pareto_capped_mean(1, 1, x_m=0), lambda: symmetric_stable_mean_abs(3),
    lambda: symmetric_stable_mean_abs(0), lambda: symmetric_stable_mean_abs(1.5, n=True),
    lambda: symmetric_stable_mean_abs(1.5, scale=-1),
    lambda: pareto_plugin_nonfinite_probability(np.nan, 2),
    lambda: pareto_plugin_nonfinite_probability(1, 2.5),
    lambda: bernoulli_chernoff_log_bound(0, .5, 1),
    lambda: bernoulli_chernoff_log_bound(.5, 1.1, 1),
    lambda: repeated_centered_sums(expon(), [2.5]),
    lambda: repeated_centered_sums(expon(), [True]),
    lambda: repeated_centered_sums(expon(), []),
    lambda: repeated_centered_sums(expon(), [2], center=np.inf),
    lambda: repeated_centered_sums(expon(), [2], batch=0),
])
def test_invalid_domains(call):
    with pytest.raises(ValueError):
        call()
