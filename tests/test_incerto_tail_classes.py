"""Analytic checks and numerical boundaries for the Prologue model helpers."""

import numpy as np
import pytest
from scipy.stats import expon, lognorm, pareto, rv_discrete

from xmath.incerto.tail_classes import (
    bounded_spike_summary,
    log_survival_multiplier_ratio,
)


@pytest.mark.parametrize("epsilon", [1.0, 0.1, 0.01, 0.001])
def test_bounded_moments_against_discrete_distribution(epsilon):
    row = bounded_spike_summary(epsilon)
    radius = row["support_radius"]
    law = rv_discrete(values=([-radius, 0, radius],
                              [epsilon / 2, 1 - epsilon, epsilon / 2]))
    mean, variance, _, excess = law.stats(moments="mvsk")
    assert row["mean"] == pytest.approx(mean)
    assert row["variance"] == pytest.approx(variance)
    assert row["kurtosis"] == pytest.approx(excess + 3)
    assert law.sf(radius) == 0


@pytest.mark.parametrize("epsilon", [0, -0.1, 1.1, np.nan, np.inf])
def test_bounded_invalid_probability(epsilon):
    with pytest.raises(ValueError):
        bounded_spike_summary(epsilon)


def test_bounded_unrepresentable_kurtosis():
    with pytest.raises(OverflowError):
        bounded_spike_summary(float(np.nextafter(0.0, 1.0)))


def test_pareto_ratio_is_constant_across_scales():
    u = [1, 10, 1e8]
    result = log_survival_multiplier_ratio(pareto(2.5).logsf, u, multiplier=3)
    np.testing.assert_allclose(result, -2.5 * np.log(3), rtol=1e-13)


def test_exponential_ratio_survives_ordinary_probability_underflow():
    u = np.array([1_000.0, 10_000.0])
    assert np.all(expon.sf(u) == 0)
    np.testing.assert_allclose(log_survival_multiplier_ratio(expon.logsf, u), -u)


def test_lognormal_ratio_agrees_with_direct_probabilities_on_moderate_grid():
    u = np.array([1.0, 4.0, 20.0])
    law = lognorm(1)
    expected = np.log(law.sf(2 * u) / law.sf(u))
    np.testing.assert_allclose(log_survival_multiplier_ratio(law.logsf, u), expected)


@pytest.mark.parametrize("u", [[], [0], [-1], [np.nan], [np.inf], [[1, 2]]])
def test_invalid_thresholds(u):
    with pytest.raises(ValueError):
        log_survival_multiplier_ratio(expon.logsf, u)


@pytest.mark.parametrize("multiplier", [0, 1, -2, np.inf, np.nan])
def test_invalid_multiplier(multiplier):
    with pytest.raises(ValueError):
        log_survival_multiplier_ratio(expon.logsf, [1], multiplier=multiplier)


@pytest.mark.parametrize("value", [np.nan, np.inf, -np.inf, 0.1])
def test_invalid_log_probabilities(value):
    with pytest.raises(ValueError):
        log_survival_multiplier_ratio(lambda u: np.full_like(u, value), [1, 2])


def test_shape_mismatch_and_threshold_overflow():
    with pytest.raises(ValueError, match="one value per threshold"):
        log_survival_multiplier_ratio(lambda u: np.zeros(3), [1, 2])
    with pytest.raises(ValueError, match="multiplied thresholds"):
        log_survival_multiplier_ratio(expon.logsf, [np.finfo(float).max])


def test_zero_numerator_is_reported_as_nonfinite_not_silently_dropped():
    def bounded_logsf(u):
        return np.where(u < 3, -1.0, -np.inf)

    with pytest.raises(ValueError, match="finite and nonpositive"):
        log_survival_multiplier_ratio(bounded_logsf, [1, 2])
