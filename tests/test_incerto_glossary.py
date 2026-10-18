"""Independent checks for chapter-2 identities and numerical boundaries."""

import math
from decimal import Decimal, localcontext

import numpy as np
import pytest
from scipy.integrate import quad
from scipy.stats import binom, genpareto, pareto

from xmath import exceedance_fraction
from xmath.incerto.glossary import (
    pareto_normalized_maximum_cdf,
    pareto_tail_quantities,
)
from xmath.incerto.stats import empirical_survival_function


def test_tied_sample_cdf_partition_and_monotonicity():
    sample = np.array([1, 2, 2, 4])
    support, survival = empirical_survival_function(sample)
    np.testing.assert_array_equal(support, [1, 2, 4])
    np.testing.assert_array_equal(survival, [.75, .25, 0])
    grid = np.array([0, 1, np.nextafter(2., -np.inf), 2, 3, 4, 5])
    strict = np.array([exceedance_fraction(sample, u) for u in grid])
    np.testing.assert_array_equal(strict + [(sample <= u).mean() for u in grid], 1)
    assert np.all(np.diff(strict) <= 0)
    assert np.all((0 <= strict) & (strict <= 1))
    assert (sample >= 2).mean() - exceedance_fraction(sample, 2) == .5


@pytest.mark.parametrize("q", [0, .125, .5, 1])
def test_indicator_mean_and_variance_by_binomial_enumeration(q):
    n = 8
    fractions = np.arange(n + 1) / n
    mass = binom.pmf(np.arange(n + 1), n, q)
    mean = np.dot(mass, fractions)
    variance = np.dot(mass, (fractions - mean) ** 2)
    assert mean == pytest.approx(q)
    assert variance == pytest.approx(q * (1 - q) / n)


@pytest.mark.parametrize("alpha,x_m,u", [(1.5, 1, 4), (2.5, 2, 2), (3, .5, 8)])
def test_pareto_tail_quantities_against_integrals(alpha, x_m, u):
    row = pareto_tail_quantities(alpha, x_m, u)
    model = pareto(alpha, scale=x_m)
    probability = model.sf(u)
    # Density quadrature is independent of the implemented closed formulas.
    moment, _ = quad(lambda x: x * model.pdf(x), u, np.inf, epsabs=1e-10)
    excess, _ = quad(lambda y: genpareto.sf(y, c=1 / alpha, scale=u / alpha),
                     0, np.inf, epsabs=1e-10)
    assert row["log_survival"] == pytest.approx(model.logsf(u))
    assert row["tail_first_moment"] == pytest.approx(moment, rel=1e-9)
    assert row["conditional_mean"] == pytest.approx(moment / probability, rel=1e-9)
    assert row["mean_excess"] == pytest.approx(excess, rel=1e-9)
    assert row["tail_first_moment"] > u * probability


@pytest.mark.parametrize("alpha", [.2, .8, 1.0])
def test_pareto_mathematical_infinity(alpha):
    row = pareto_tail_quantities(alpha, 1, 4)
    assert math.isfinite(row["log_survival"])
    assert all(row[name] == math.inf for name in
               ("mean_excess", "conditional_mean", "tail_first_moment"))


def test_pareto_underflow_and_units():
    row = pareto_tail_quantities(2, 1, 1e200)
    assert math.exp(row["log_survival"]) == 0  # probability underflows
    assert row["tail_first_moment"] == pytest.approx(2e-200, rel=1e-12, abs=0)
    base = pareto_tail_quantities(1.5, 1, 4)
    scaled = pareto_tail_quantities(1.5, 10, 40)
    assert scaled["log_survival"] == pytest.approx(base["log_survival"])
    for name in ("mean_excess", "conditional_mean", "tail_first_moment"):
        assert scaled[name] == pytest.approx(10 * base[name])


@pytest.mark.parametrize("args", [(0, 1, 2), (2, 0, 2), (2, 1, .5),
                                  (np.nan, 1, 2), (2, np.inf, 2), (2, 1, np.inf)])
def test_pareto_invalid_inputs(args):
    with pytest.raises(ValueError):
        pareto_tail_quantities(*args)


def test_pareto_unrepresentable_finite_quantities():
    with pytest.raises(OverflowError):
        pareto_tail_quantities(1.00001, 1, 1e308)
    with pytest.raises(OverflowError):
        pareto_tail_quantities(1e308, 1, 1e308)


@pytest.mark.parametrize("alpha,n", [(.8, 1), (1.5, 4), (3, 64)])
def test_normalized_maximum_against_scipy_distribution(alpha, n):
    y = np.geomspace(.1, 10, 101)
    actual = pareto_normalized_maximum_cdf(y, alpha=alpha, n=n)
    expected = pareto.cdf(y * n ** (1 / alpha), b=alpha) ** n
    np.testing.assert_allclose(actual, expected, atol=2e-14, rtol=2e-13)
    assert np.all(np.diff(actual) >= 0)
    assert np.all((0 <= actual) & (actual <= 1))


def test_maximum_support_and_large_n_limit():
    np.testing.assert_array_equal(
        pareto_normalized_maximum_cdf([.25, .5], alpha=2, n=4), [0, 0])
    # A naive (1 - 1/n)**n loses this value at sufficiently large n.
    actual = pareto_normalized_maximum_cdf([1], alpha=1.5, n=2**53)[0]
    assert actual == pytest.approx(math.exp(-1), rel=1e-14)
    y = np.geomspace(.25, 4, 301)
    target = np.exp(-y**-1.5)
    errors = [np.max(np.abs(pareto_normalized_maximum_cdf(y, alpha=1.5, n=n)
                            - target)) for n in [1, 4, 16, 64]]
    assert np.all(np.diff(errors) < 0)
    assert errors[-1] < .005


@pytest.mark.parametrize("alpha,n", [(.1, 1), (.01, 1), (1., 8), (1., 16)])
def test_maximum_one_float_above_support(alpha, n):
    boundary = 1. / n  # exact dyadic endpoint in these cases (n=1 or alpha=1)
    y = np.nextafter(boundary, np.inf)
    with localcontext() as context:
        context.prec = 100
        expected = float((1 - Decimal.from_float(float(y))
                          ** -Decimal.from_float(alpha) / n) ** n)
    actual = pareto_normalized_maximum_cdf([boundary, y], alpha=alpha, n=n)
    assert actual[0] == 0
    assert actual[1] > 0
    np.testing.assert_allclose(actual[1], expected, rtol=1e-12, atol=0)


@pytest.mark.parametrize("n", [0, -1, 2.5, True, np.bool_(True), 2**53 + 1])
def test_invalid_maximum_count(n):
    with pytest.raises(ValueError):
        pareto_normalized_maximum_cdf([1], alpha=2, n=n)


@pytest.mark.parametrize("y,alpha", [([], 2), ([[1]], 2), ([0], 2),
                                     ([np.inf], 2), ([1], 0), ([1], np.nan)])
def test_invalid_maximum_grid(y, alpha):
    with pytest.raises(ValueError):
        pareto_normalized_maximum_cdf(y, alpha=alpha, n=4)


def test_maximum_log_overflow():
    with pytest.raises(OverflowError):
        pareto_normalized_maximum_cdf([1e300], alpha=1e308, n=4)
