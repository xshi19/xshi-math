"""Exact enumeration, boundary and independent model checks for chapter 3."""

from fractions import Fraction
from itertools import product
import math

import numpy as np
import pytest
from scipy.integrate import quad
from scipy.stats import pareto

from xmath.incerto.lecture_risk import (
    absorbing_resource_path,
    block_failure_summary,
    finite_payoff_mean,
    repeated_event_probability,
    split_power_damage_logsf,
    survival_from_hazards,
)


@pytest.mark.parametrize("n", [1, 2, 3, 5])
def test_contamination_distance_and_block_moments_by_enumeration(n):
    # P is a point mass at 0, R at 2. Enumerate every Q sample exactly;
    # this checks both product-law TV and the finite aggregate-failure law.
    q = Fraction(1, 4)
    tv = mean = second = any_failure = total_failure = Fraction(0)
    for bits in product((0, 1), repeat=n):
        failures = sum(bits)
        mass = q**failures * (1-q)**(n-failures)
        baseline = Fraction(int(failures == 0))
        tv += abs(mass-baseline) / 2
        damage = Fraction(3*failures, n)
        mean += mass*damage
        second += mass*damage**2
        any_failure += mass*int(failures > 0)
        total_failure += mass*int(failures == n)
    assert repeated_event_probability(float(q), n) == pytest.approx(float(tv))
    actual = block_failure_summary(float(q), n, exposure=3)
    assert actual == pytest.approx(dict(mean=float(mean), variance=float(second-mean**2),
                                      any_failure=float(any_failure), total_failure=float(total_failure)))


@pytest.mark.parametrize("q,n,expected", [(0, 20, 0), (1, 0, 0), (1, 20, 1), (0.25, 1, 0.25)])
def test_repeated_probability_endpoints(q, n, expected):
    assert repeated_event_probability(q, n) == expected


def test_rare_probability_survives_cancellation():
    # Naive 1-(1-q)**n is zero here, while the first-order value is accurate.
    assert repeated_event_probability(1e-20, 1000) == pytest.approx(1e-17, rel=1e-14, abs=0)
    assert 0 < repeated_event_probability(1e-20, 2**53) < 1


@pytest.mark.parametrize("q,n", [(-0.1, 2), (1.1, 2), (np.nan, 2), (np.inf, 2),
                                (0.1, -1), (0.1, 1.5), (0.1, True), (0.1, 2**53+1)])
def test_invalid_probability_or_count(q, n):
    with pytest.raises(ValueError):
        repeated_event_probability(q, n)


def test_conditional_hazards_from_a_finite_ruin_time_law():
    # P(T=1,2,3,infinity)=(1/8,1/4,1/8,1/2); hazards are conditional.
    actual = survival_from_hazards([1/8, 2/7, 1/5])
    np.testing.assert_allclose(actual, [1, 7/8, 5/8, 1/2])


def test_summable_hazards_exact_telescoping_and_absorption():
    n = np.arange(1, 1001)
    survival = survival_from_hazards(1/(n+1.0)**2)
    np.testing.assert_allclose(survival[1:], (n+2)/(2*(n+1)), rtol=2e-14)
    np.testing.assert_array_equal(survival_from_hazards([]), [1])
    np.testing.assert_array_equal(survival_from_hazards([0, 1, 0.5]), [1, 1, 0, 0])


@pytest.mark.parametrize("h", [[-0.1], [1.1], [np.nan], [np.inf], [[0.1]]])
def test_invalid_hazards(h):
    with pytest.raises(ValueError):
        survival_from_hazards(h)


def test_finite_payoffs_jensen_and_cancellation():
    assert finite_payoff_mean([0.98, 0.02], [1, -80]) == pytest.approx(-0.62)
    assert finite_payoff_mean([0.5, 0.5], [2**2, 6**2]) == 20
    assert finite_payoff_mean([0.5, 0.5], [math.sqrt(2), math.sqrt(6)]) < 2
    assert finite_payoff_mean([0.25]*4, [1e20, 4, -1e20, 4]) == 2


@pytest.mark.parametrize("p,x", [([], []), ([1], [1, 2]), ([0.9], [1]),
                                ([-1, 2], [1, 2]), ([1], [np.inf]), ([[1]], [1])])
def test_invalid_finite_law(p, x):
    with pytest.raises(ValueError):
        finite_payoff_mean(p, x)


def test_absorbing_order_and_zero_barrier():
    np.testing.assert_array_equal(absorbing_resource_path(3, [-4, 4]), [3, 0, 0])
    np.testing.assert_array_equal(absorbing_resource_path(3, [4, -4]), [3, 7, 3])
    np.testing.assert_array_equal(absorbing_resource_path(3, [-3, 100]), [3, 0, 0])
    np.testing.assert_array_equal(absorbing_resource_path(0, [100]), [0, 0])
    np.testing.assert_array_equal(absorbing_resource_path(3, []), [3])
    with pytest.raises(OverflowError):
        absorbing_resource_path(1e308, [1e308])
    with pytest.raises(ValueError):
        absorbing_resource_path(-1, [])


@pytest.mark.parametrize("power", [0.5, 1, 2, 3])
def test_power_damage_distribution_and_exposure_units(power):
    # Compare at thresholds obtained from SciPy's original Pareto quantiles.
    probabilities = np.array([0.1, 0.5, 0.9, 0.999])
    x = pareto.ppf(probabilities, 1.5, scale=2)
    threshold = 4 * (3*x/4)**power
    actual = split_power_damage_logsf(threshold, alpha=1.5, power=power, modules=4, exposure=3, x_m=2)
    np.testing.assert_allclose(actual, np.log1p(-probabilities), rtol=1e-13)
    shifted = split_power_damage_logsf(threshold*5**power, alpha=1.5, power=power, modules=4, exposure=15, x_m=2)
    np.testing.assert_allclose(shifted, actual, rtol=1e-13)


def test_power_damage_support_tail_ratio_and_integrable_mean():
    np.testing.assert_array_equal(split_power_damage_logsf([0, 0.01, 1/16], alpha=1.5, power=2, modules=16), [0, 0, 0])
    original = split_power_damage_logsf([1, 10, 100], alpha=1.5, power=2, modules=1)
    split = split_power_damage_logsf([1, 10, 100], alpha=1.5, power=2, modules=16)
    np.testing.assert_allclose(np.exp(split-original), 1/8)
    # Tail-integral mean versus an independent integral of the original density.
    survival_mean = 0.25 + quad(lambda u: np.exp(split_power_damage_logsf(u, alpha=3, power=2, modules=4)), 0.25, np.inf)[0]
    density_mean = quad(lambda x: x*x/4 * pareto.pdf(x, 3), 1, np.inf)[0]
    assert survival_mean == pytest.approx(density_mean, rel=1e-8)
    assert survival_mean == pytest.approx(0.75)


@pytest.mark.parametrize("power", [1e8, 1e16, 1e308])
@pytest.mark.parametrize("modules,exposure,x_m", [(2, 2, 1), (3, 1.5, 2)])
def test_power_damage_cancelling_scale(power, modules, exposure, x_m):
    # exposure*x_m/modules = 1 and alpha = power, so D has Pareto
    # minimum modules and exponent 1, independently of the large power.
    actual = split_power_damage_logsf(
        [modules / 2, modules, 2 * modules], alpha=power, power=power,
        modules=modules, exposure=exposure, x_m=x_m,
    )
    np.testing.assert_allclose(actual, [0, 0, -math.log(2)], rtol=2e-15, atol=0)


@pytest.mark.parametrize("alpha", [1.5, 1e16, 1e308])
def test_power_damage_immediately_above_support(alpha):
    above = np.nextafter(3.0, np.inf)
    actual = split_power_damage_logsf(
        [np.nextafter(3.0, 0), 3, above], alpha=alpha, power=1e16,
        modules=3, exposure=1.5, x_m=2,
    )
    # The exact minimum is 3; log1p preserves the one-float excess above it.
    expected = -(alpha / 1e16) * math.log1p((above - 3) / 3)
    np.testing.assert_array_equal(actual[:2], [0, 0])
    assert actual[2] == pytest.approx(expected, rel=3e-15, abs=0)


@pytest.mark.parametrize("power", [1e-20, 1e-100, 1e-308])
def test_power_damage_small_power_retains_tail_probability(power):
    # D = 2*(X/2)**power exceeds 2 exactly when X exceeds 2.
    actual = split_power_damage_logsf(2, alpha=1, power=power, modules=2)
    assert actual == pytest.approx(-math.log(2), rel=3e-15)


@pytest.mark.parametrize("changes", [{"alpha": 0}, {"power": -1}, {"modules": 0},
                                     {"exposure": np.inf}, {"x_m": 0}, {"threshold": [-1]}])
def test_invalid_power_damage(changes):
    args = dict(threshold=[1], alpha=1.5, power=2, modules=4)
    args.update(changes)
    with pytest.raises(ValueError):
        split_power_damage_logsf(**args)


def test_log_damage_tail_and_block_extremes():
    log_sf = split_power_damage_logsf(1e300, alpha=4, power=2, modules=1)
    assert np.isfinite(log_sf) and log_sf < -1000  # ordinary survival underflows
    for q in (0, 1):
        assert block_failure_summary(q, 10, exposure=1e300)["variance"] == 0
    with pytest.raises(OverflowError):
        block_failure_summary(0.5, 1, exposure=1e300)
    # Early q/k underflows, but the scaled variance is representable.
    tiny = float.fromhex("0x0.0000000000001p-1022")
    reference = float(Fraction.from_float(1e200)**2 * Fraction.from_float(tiny)
                      * (1-Fraction.from_float(tiny)) / 10**15)
    assert block_failure_summary(tiny, 10**15, exposure=1e200)["variance"] == pytest.approx(reference, rel=2e-13)
