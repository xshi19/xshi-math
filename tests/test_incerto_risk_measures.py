"""Independent integrations, discrete laws and numerical domains for chapter 13."""

from decimal import Decimal, localcontext
from fractions import Fraction

import numpy as np
import pytest
from scipy.integrate import quad
from scipy.special import beta
from scipy.stats import pareto

from xmath.incerto.risk_measures import (
    beta_pareto_quantile_moment, discrete_risk, pareto_mixture_risk, pareto_risk,
)


@pytest.mark.parametrize("alpha", [1.25, 1.7, 3, 8])
@pytest.mark.parametrize("p", [.01, .2, .7])
def test_pareto_risk_against_density_integral(alpha, p):
    law = pareto(alpha, scale=2)
    r = pareto_risk(alpha, p, xm=2)
    assert law.sf(r['var']) == pytest.approx(p, rel=2e-14)
    tail = quad(lambda x: x*law.pdf(x), r['var'], np.inf, epsabs=1e-10)[0]
    assert r['es'] == pytest.approx(tail/p, rel=2e-9)


@pytest.mark.parametrize("alpha", [.2, .8, 1.])
def test_infinite_es_finite_quantile(alpha):
    r = pareto_risk(alpha, .1)
    assert np.isfinite(r['var']) and r['es'] == np.inf


def test_pareto_log_domain_and_overflow():
    r = pareto_risk(.5, 1e-200, xm=1e-300)
    assert r['var'] == pytest.approx(1e100, rel=2e-13)
    assert r['es'] == np.inf
    # Smallest probability remains useful without subtracting it from one.
    p = np.nextafter(0., 1.)
    with localcontext() as ctx:
        ctx.prec = 70
        expected = float((1/Decimal.from_float(p)).sqrt())
    assert pareto_risk(2, p)['var'] == pytest.approx(expected, rel=1e-13)
    with pytest.raises(FloatingPointError):
        pareto_risk(.1, 1e-100)


@pytest.mark.parametrize("p", [0, 1, -.1, 1.1, np.nan, np.inf, True, [0.1]])
def test_invalid_tail_probability(p):
    for call in (lambda: pareto_risk(2, p),
                 lambda: discrete_risk([0, 1], [.5, .5], p),
                 lambda: pareto_mixture_risk([1.5, 2.5], [.5, .5], p)):
        with pytest.raises(ValueError):
            call()


@pytest.mark.parametrize("alpha", [0, -1, np.inf, np.nan, True, [2], 1j])
def test_invalid_exponent(alpha):
    with pytest.raises(ValueError):
        pareto_risk(alpha, .1)


def test_quantile_atom_and_strict_conditional_mean():
    r = discrete_risk([0, 5, 20], [.85, .1, .05], .1)
    assert r == pytest.approx(dict(var=5, es=12.5))
    assert r['es'] != 20  # E[X | X > VaR] omits the fractional atom.
    assert discrete_risk([5, 0, 20, 5], [.06, .85, .05, .04], .1) == pytest.approx(r)
    assert discrete_risk([7, 7], [.2, .8], .1) == dict(var=7., es=7.)


def test_discrete_var_subadditivity_counterexample():
    w = [.92, .04, .04]
    x = discrete_risk([0, 10, 0], w, .05)
    y = discrete_risk([0, 0, 10], w, .05)
    both = discrete_risk([0, 10, 10], w, .05)
    assert x == y == pytest.approx(dict(var=0, es=8))
    assert both == pytest.approx(dict(var=10, es=10))


def test_discrete_exact_cdf_boundary_and_tiny_tail():
    assert discrete_risk([0, 10], [.9, .1], .1) == dict(var=0., es=10.)
    assert discrete_risk([0, 10], [.9, .1], np.nextafter(.1, 0))['var'] == 10
    assert discrete_risk([0, 1e308], [1, 1e-200], 1e-210) == dict(var=1e308, es=1e308)
    assert discrete_risk([0, 1e308], [1, 0], .1) == dict(var=0., es=0.)


@pytest.mark.parametrize("x,w", [([], []), ([1], [.5]), ([1, 2], [1]),
                                   ([1, 2], [-.1, 1.1]), ([np.nan], [1]),
                                   ([-1], [1]), ([[1]], [1]), ([1j], [1])])
def test_invalid_discrete_law(x, w):
    with pytest.raises(ValueError):
        discrete_risk(x, w, .1)


@pytest.mark.parametrize("p", [.001, .05, .6])
@pytest.mark.parametrize("alphas,weights", [([1.3, 2.7], [.4, .6]), ([2, 3, 5], [.2, .5, .3])])
def test_mixture_risk_with_independent_density_integral(p, alphas, weights):
    result = pareto_mixture_risk(alphas, weights, p, xm=3)
    q = result['var']
    survival = sum(w*pareto.sf(q, a, scale=3) for a, w in zip(alphas, weights))
    assert survival == pytest.approx(p, rel=2e-13)
    integral = sum(w*quad(lambda x: x*pareto.pdf(x, a, scale=3), q, np.inf,
                         epsabs=1e-9)[0] for a, w in zip(alphas, weights))
    assert result['es'] == pytest.approx(integral/p, rel=2e-8)
    at_mean = pareto_risk(np.dot(alphas, weights), p, xm=3)
    assert result['var'] > at_mean['var'] and result['es'] > at_mean['es']


def test_mixture_is_not_average_quantiles_and_infinite_components():
    components = [pareto_risk(a, .01) for a in (1.2, 2.8)]
    mix = pareto_mixture_risk([1.2, 2.8], [.5, .5], .01)
    assert mix['var'] != pytest.approx(np.mean([r['var'] for r in components]), rel=1e-3)
    assert pareto_mixture_risk([.8, 2], [.1, .9], .01)['es'] == np.inf
    assert pareto_mixture_risk([.8, 2], [0, 1], .01) == pareto_risk(2, .01)
    assert pareto_mixture_risk([2, 2], [.1, .9], .01) == pareto_risk(2, .01)


def test_mixture_tail_probability_near_one():
    # A log-sum roundoff previously made the valid root bracket negative
    # at both endpoints. At this p, the exact quantile rounds to the cutoff.
    p = np.nextafter(1., 0.)
    result = pareto_mixture_risk([2, 3], [.12345, .87655], p)
    assert result['var'] == 1
    assert result['es'] == pytest.approx(.12345*2 + .87655*1.5, rel=2e-14)


@pytest.mark.parametrize("alphas", [[0, 2], [.0001, 2], [2, 1001], [np.nan, 2], [1j, 2]])
def test_mixture_exponent_domain(alphas):
    with pytest.raises(ValueError):
        pareto_mixture_risk(alphas, [.5, .5], .1)


@pytest.mark.parametrize("a,b,alpha,order", [(2, 3, 2, 1), (2, 3, 2, 2),
                                           (.5, .7, 3, 1), (3, 2, 1.1, 2)])
def test_beta_moments_by_endpoint_weighted_quadrature(a, b, alpha, order):
    # QUADPACK integrates algebraic endpoint singularities; no log-beta ratio.
    value = quad(lambda p: 1/beta(a, b), 0, 1, weight='alg',
                 wvar=(a-1-order/alpha, b-1), epsabs=1e-11)[0]
    actual = beta_pareto_quantile_moment(a, b, alpha, order, xm=2)
    assert actual == pytest.approx(2**order*value, rel=1e-11)


def test_beta_integer_moments_exact_rational_reference():
    # P~Beta(2,3) has polynomial density 12*p*(1-p)^2.
    expected = 12*(Fraction(1) - Fraction(2, 2) + Fraction(1, 3))
    assert beta_pareto_quantile_moment(2, 3, 1, 1) == pytest.approx(float(expected))
    assert beta_pareto_quantile_moment(2, 3, 1, 2) == np.inf
    assert beta_pareto_quantile_moment(2, 3, .5, 1) == np.inf
    assert beta_pareto_quantile_moment(2, 3, .5, 0) == 1
    assert np.isfinite(beta_pareto_quantile_moment(2, 3, np.nextafter(1., 2.), 2))


@pytest.mark.parametrize("b", [1, 3])
def test_beta_finite_moment_when_boundary_gap_is_below_extended_precision(b):
    # (1+eps)^2 - (1+2*eps) = eps^2 > 0, although the float product
    # and even extended-precision subtraction erase this positive gap.
    eps = np.finfo(float).eps
    a = alpha = 1 + eps
    order = 1 + 2*eps
    with localcontext() as ctx:
        ctx.prec = 100
        a_exact = Decimal.from_float(a)
        delta = a_exact - Decimal.from_float(order)/Decimal.from_float(alpha)
        expected = Decimal(1)
        # For integer b, the beta ratio is a finite product, independent
        # of the implementation's log-beta evaluation and rational arithmetic.
        for j in range(b):
            expected *= (a_exact+j)/(delta+j)
    assert beta_pareto_quantile_moment(a, b, alpha, order) == pytest.approx(
        float(expected), rel=2e-14,
    )
    assert beta_pareto_quantile_moment(a, b, alpha, np.nextafter(order, np.inf)) == np.inf
    assert beta_pareto_quantile_moment(2, b, alpha, 2*alpha) == np.inf


def test_beta_tiny_order_and_finite_range_failures():
    assert beta_pareto_quantile_moment(2, 1, 1, 1e-20) == 1
    assert beta_pareto_quantile_moment(2, 1, 1, 1) == pytest.approx(2)
    for xm in (1e-300, 1e300):
        with pytest.raises(FloatingPointError):
            beta_pareto_quantile_moment(3, 1, 1, 2, xm=xm)


@pytest.mark.parametrize("args", [(0, 1, 2, 1), (2, np.inf, 2, 1),
                                  (2, 3, 0, 1), (2, 3, 2, -1),
                                  (2, 3, 2, np.nan), (.0001, 3, 2, 1)])
def test_invalid_beta_domain(args):
    with pytest.raises(ValueError):
        beta_pareto_quantile_moment(*args)


@pytest.mark.parametrize("xm", [0, -1, np.nan, np.inf, [1]])
def test_invalid_cutoff(xm):
    for call in (lambda: pareto_risk(2, .1, xm=xm),
                 lambda: pareto_mixture_risk([2, 3], [.5, .5], .1, xm=xm),
                 lambda: beta_pareto_quantile_moment(2, 3, 2, 1, xm=xm)):
        with pytest.raises(ValueError):
            call()
