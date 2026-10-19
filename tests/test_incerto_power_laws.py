"""Analytic references and independent integrals for chapter-5 helpers."""

from decimal import Decimal, localcontext

import numpy as np
import pytest
from scipy.integrate import quad
from scipy.special import digamma
from scipy.stats import expon, gamma, genpareto, pareto, t, weibull_min

from xmath.incerto.distributions import double_pareto, hypsecant2
from xmath.incerto.power_laws import (
    entropy_log_constraint_example,
    pareto_product_logsf,
    pareto_truncated_moment,
    q_exponential_logsf,
    student_double_pareto_scales,
)
from xmath.incerto.tail_diagnostics import iid_two_sum_tail


@pytest.mark.parametrize("a,b", [(1, 2), (2, 1), (.4, 3), (1.5, 1.5), (2, 2+1e-12)])
def test_product_against_conditioning_in_log_coordinate(a, b):
    for z in (0, .2, 1, 5, 15):
        # log(X1),log(X2) are independent exponentials, no product formula used.
        reference = np.exp(-a*z) + quad(
            lambda y: a*np.exp(-a*y)*np.exp(-b*(z-y)), 0, z, epsabs=1e-13)[0]
        assert np.exp(pareto_product_logsf(z, a, b)) == pytest.approx(reference, rel=2e-12)


def test_equal_product_is_gamma_in_log_coordinate_and_extreme_logtail_is_finite():
    z = np.array([0, .001, 1, 20, 100])
    np.testing.assert_allclose(pareto_product_logsf(z, 2, 2),
                               gamma.logsf(z, 2, scale=.5), atol=5e-14)
    assert np.isfinite(pareto_product_logsf(10000, 2, 3))


@pytest.mark.parametrize("a,b", [(1, 1), (2, 3), (1e-3, 7)])
def test_product_near_lower_support_retains_second_order_probability(a, b):
    z = 1e-12
    # CDF of the sum has density slope a*b at zero.
    assert pareto_product_logsf(z, a, b) == pytest.approx(-a*b*z*z/2, rel=1e-10, abs=0)


@pytest.mark.parametrize("alpha,order", [(1.5, 1), (1.5, 1.5), (1.5, 2), (3, .4),
                                         (2, 2+1e-12), (2, 2-1e-12)])
def test_truncated_moment_against_density_integral(alpha, order):
    for xm in (.3, 1, 4):
        b = xm*np.array([1, 1.2, 3, 100])
        values = pareto_truncated_moment(b, alpha, order, x_m=xm)
        for cutoff, value in zip(b, values):
            ref = quad(lambda x: x**order*pareto.pdf(x, alpha, scale=xm),
                       xm, cutoff, epsabs=1e-11, epsrel=1e-11)[0]
            assert value == pytest.approx(ref, rel=2e-11, abs=1e-13)


def test_truncated_moment_support_and_rescaling():
    b = np.nextafter(1., 2.)
    assert pareto_truncated_moment(1., 3, 2) == 0
    assert pareto_truncated_moment(b, 3, 2) == pytest.approx(3*(b-1)/b, rel=1e-14, abs=0)
    # Tiny scale factor and large cutoff cancel in log coordinates.
    assert pareto_truncated_moment(1e100, 1, 2, x_m=1e-100) == pytest.approx(1, rel=1e-12)


@pytest.mark.parametrize("alpha", [2.5, 3., 7., 15.])
def test_student_matching_matches_independent_density_constant_and_variance(alpha):
    result = student_double_pareto_scales(alpha)
    c = result["student_tail_constant"]
    # A high threshold is a numerical check of the density algebra, not a limit proof.
    log_reference = t.logpdf(1e5, alpha)+(alpha+1)*np.log(1e5)-np.log(alpha)
    assert np.log(c) == pytest.approx(log_reference, abs=2e-8)
    assert t.var(alpha, scale=result["variance_scale"]) == pytest.approx(double_pareto.var(alpha))
    assert c*result["tail_scale"]**alpha == pytest.approx(.5)
    assert t.var(alpha, scale=result["tail_scale"]) == pytest.approx(result["tail_matched_variance"])


@pytest.mark.parametrize("q", [.25, .75, 1., 1.25, 1.6, 1.95])
def test_q_survival_against_independent_gpd_parameterization(q):
    x = np.linspace(0, 8, 41)
    # GPD shape=(q-1)/(2-q), scale=1/(beta*(2-q)).
    expected = genpareto.logsf(x, (q-1)/(2-q), scale=1/(2*(2-q)))
    np.testing.assert_allclose(q_exponential_logsf(x, q, 2), expected, atol=1e-12)


def test_q_compact_endpoint_and_exponential_limit():
    endpoint = 2.
    xs = np.array([0, np.nextafter(endpoint, 0), endpoint, 3])
    result = q_exponential_logsf(xs, .75, 2)
    assert result[0] == 0 and np.isfinite(result[1])
    assert np.isneginf(result[2:]).all()
    for q in (np.nextafter(1., 0), np.nextafter(1., 2)):
        np.testing.assert_allclose(q_exponential_logsf([0, .1, 2], q, 2), [0, -.2, -4], atol=2e-14)


def test_q_near_one_does_not_underflow_the_rate_before_scaling_x():
    q, beta, x = np.nextafter(1., 2.), 1e-309, 1e300
    assert q_exponential_logsf(x, q, beta) == pytest.approx(-beta*x, rel=1e-14, abs=0)


@pytest.mark.parametrize("q,beta,x", [
    (np.nextafter(1., 2.), 1e-309, 1.),
    (np.nextafter(1., 0.), 1e-10, 1e-300),
])
def test_q_retains_tiny_log_survival_on_both_sides_of_one(q, beta, x):
    # Integrating the hazard beta*(2-q)/(1+(q-1)*beta*t) over [0,x]
    # differs from beta*(2-q)*x by far less than one output ulp here.
    expected = -(2-q)*(beta*x)
    assert expected < 0
    assert q_exponential_logsf(x, q, beta) == pytest.approx(expected, rel=1e-12, abs=0)


@pytest.mark.parametrize("q,beta", [(.25, 7.), (.1, 3.), (.9, 1.3), (1e-20, 1.)])
def test_q_compact_boundary_against_high_precision_input_parameters(q, beta):
    endpoint = (1/(1-q))/beta
    x = np.array([np.nextafter(endpoint, 0), endpoint, np.nextafter(endpoint, np.inf)])
    result = q_exponential_logsf(x, q, beta)
    with localcontext() as context:
        context.prec = 90
        dq, dbeta = Decimal.from_float(q), Decimal.from_float(beta)
        for value, got in zip(x, result):
            base = 1 + (dq-1)*dbeta*Decimal.from_float(float(value))
            if base <= 0:
                assert np.isneginf(got)
            else:
                expected = float(-(2-dq)/(dq-1)*base.ln())
                assert np.isfinite(got)
                assert got == pytest.approx(expected, rel=2e-14)


def test_q_nonrepresentable_compact_endpoint_raises():
    with pytest.raises(FloatingPointError):
        q_exponential_logsf(1e300, .75, 1e-309)


@pytest.mark.parametrize("q", [.5, 1.25, 1.6])
def test_q_density_normalization_and_escort_mean(q):
    beta = 2
    upper = 1/((1-q)*beta) if q < 1 else np.inf
    density = lambda x: beta*(2-q)*(1+(q-1)*beta*x)**(-1/(q-1))
    mass = quad(density, 0, upper)[0]
    escort_mass = quad(lambda x: density(x)**q, 0, upper)[0]
    escort_first = quad(lambda x: x*density(x)**q, 0, upper)[0]
    assert mass == pytest.approx(1, abs=1e-9)
    assert escort_mass == pytest.approx(beta**(q-1)*(2-q)**q, rel=1e-9)
    assert escort_first/escort_mass == pytest.approx(1/(beta*(2-q)), rel=1e-9)
    if q < 1.5:
        assert quad(lambda x: x*density(x), 0, upper)[0] == pytest.approx(1/(beta*(3-2*q)))


def test_entropy_constraint_and_kl_against_gamma_entropy_identity():
    result = entropy_log_constraint_example()
    for prefix in ("pareto", "log_gamma"):
        assert result[f"{prefix}_mass"] == pytest.approx(1, abs=1e-10)
        assert result[f"{prefix}_log_moment"] == pytest.approx(.5, abs=1e-10)
    assert result["pareto_entropy"] == pytest.approx(1.5-np.log(2), abs=1e-10)
    assert result["log_gamma_entropy"] == pytest.approx(2.5-np.log(4)-digamma(2), abs=1e-10)
    assert result["pareto_entropy"]-result["log_gamma_entropy"] == pytest.approx(result["kl"], abs=1e-10)
    assert result["kl"] > 0


def test_convolution_demo_against_independent_quadrature_and_exact_exponential():
    x = np.array([3., 7., 30., 100.])
    for rv in (pareto(1.5), weibull_min(.5)):
        got = iid_two_sum_tail(rv, x, rtol=1e-9)
        assert got["success"].all()
        # Conditioning in a CDF-uniform coordinate avoids the Weibull origin singularity.
        for u, ratio in zip(x, got["ratio"]):
            ref = rv.sf(u) + quad(lambda v: rv.sf(u-rv.ppf(v)), 0, rv.cdf(u),
                                  epsabs=1e-11, epsrel=1e-11, limit=160)[0]
            assert ratio == pytest.approx(ref/(2*rv.sf(u)), rel=2e-8)
    np.testing.assert_allclose(iid_two_sum_tail(expon(), x)["ratio"], (1+x)/2, rtol=1e-10)


def test_logistic_helper_is_the_normalized_squared_secant_law():
    from scipy.stats import logistic
    x = np.linspace(-5, 5, 31)
    # hypsecant2's SciPy scale=1/k gives logistic scale=1/(2*k).
    np.testing.assert_allclose(hypsecant2.pdf(x, scale=2/3),
                               logistic.pdf(x, scale=1/3), rtol=1e-13)


@pytest.mark.parametrize("call", [
    lambda: pareto_product_logsf(-1, 1, 2),
    lambda: pareto_product_logsf(1, 0, 2),
    lambda: pareto_product_logsf(np.nan, 1, 2),
    lambda: pareto_truncated_moment(.5, 2, 1),
    lambda: pareto_truncated_moment(2, 2, 0),
    lambda: student_double_pareto_scales(2),
    lambda: student_double_pareto_scales(np.inf),
    lambda: q_exponential_logsf(1, 2),
    lambda: q_exponential_logsf(1, 0),
    lambda: q_exponential_logsf(-1, 1),
    lambda: q_exponential_logsf(1, 1, -2),
    lambda: pareto_product_logsf([], 1, 2),
])
def test_invalid_domains(call):
    with pytest.raises(ValueError):
        call()


def test_arithmetic_overflow_is_not_reported_as_a_mathematical_infinite_moment():
    with pytest.raises(FloatingPointError):
        pareto_truncated_moment(1e300, 1, 10)
    with pytest.raises(FloatingPointError):
        pareto_product_logsf(1e300, 1e300, 1e300)
