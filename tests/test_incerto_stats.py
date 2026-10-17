"""Tests for statistical helper functions."""

import numpy as np
import pytest
from scipy.stats import norm

from xmath.incerto.stats import (
    mean_absolute_deviation,
    median_absolute_deviation,
    normal_peak_shoulder_tail,
    normal_variance_peak_shoulder_tail,
    t_peak_shoulder_tail,
)


def test_scaled_absolute_deviation_helpers_match_closed_examples() -> None:
    x = np.array([-1.0, 0.0, 1.0])

    assert mean_absolute_deviation(x) == pytest.approx(
        (2.0 / 3.0) * np.sqrt(np.pi / 2.0)
    )

    y = np.array([-norm.ppf(0.75), 0.0, norm.ppf(0.75)])
    assert median_absolute_deviation(y) == pytest.approx(1.0)


def test_absolute_deviation_helpers_support_axis_argument() -> None:
    x = np.array([[-1.0, 0.0, 1.0], [-2.0, 0.0, 2.0]])

    np.testing.assert_allclose(
        mean_absolute_deviation(x, axis=1),
        np.array([1.0, 2.0]) * (2.0 / 3.0) * np.sqrt(np.pi / 2.0),
    )
    np.testing.assert_allclose(
        median_absolute_deviation(x, axis=1),
        np.array([1.0, 2.0]) / norm.ppf(0.75),
    )


def test_peak_shoulder_tail_boundaries_are_symmetric() -> None:
    boundaries = normal_peak_shoulder_tail(mu=1.0, sigma=2.0)
    centered = (boundaries - 1.0) / 2.0

    np.testing.assert_allclose(centered, -centered[::-1])
    np.testing.assert_allclose(
        centered[[0, 3]],
        np.array([-1.0, 1.0]) * np.sqrt((5.0 + np.sqrt(17.0)) / 2.0),
    )
    assert normal_peak_shoulder_tail()[1] < 0 < normal_peak_shoulder_tail()[2]


def test_variance_peak_shoulder_tail_boundaries_are_symmetric() -> None:
    boundaries = normal_variance_peak_shoulder_tail(mu=1.0, variance=4.0)
    centered = (boundaries - 1.0) / 2.0

    np.testing.assert_allclose(centered, -centered[::-1])
    np.testing.assert_allclose(
        centered[[0, 3]],
        np.array([-1.0, 1.0]) * np.sqrt(3.0 + np.sqrt(6.0)),
    )
    np.testing.assert_allclose(
        centered[[1, 2]],
        np.array([-1.0, 1.0]) * np.sqrt(3.0 - np.sqrt(6.0)),
    )


def test_student_t_boundaries_validate_parameters() -> None:
    boundaries = t_peak_shoulder_tail(df=3.0)
    np.testing.assert_allclose(boundaries, -boundaries[::-1])

    with pytest.raises(ValueError, match="df"):
        t_peak_shoulder_tail(df=1.0)
    with pytest.raises(ValueError, match="sigma"):
        normal_peak_shoulder_tail(sigma=0.0)
    with pytest.raises(ValueError, match="variance"):
        normal_variance_peak_shoulder_tail(variance=0.0)


def test_legacy_log_normal_moments_and_strict_survival():
    from scipy.stats import lognorm
    from xmath.incerto.stats import lognorm_params_from_mean_and_variance, empirical_survival_function
    mu, sigma = lognorm_params_from_mean_and_variance(3.0, 7.0)
    rv = lognorm(sigma, scale=np.exp(mu))
    np.testing.assert_allclose([rv.mean(), rv.var()], [3.0, 7.0])
    support, survival = empirical_survival_function([2, 1, 2, 4])
    np.testing.assert_array_equal(support, [1, 2, 4])
    np.testing.assert_allclose(survival, [0.75, 0.25, 0.0])
    assert lognorm_params_from_mean_and_variance(3, 0)[1] == 0
    for mean, variance in ((0, 1), (1, -1), (np.inf, 1)):
        with pytest.raises(ValueError):
            lognorm_params_from_mean_and_variance(mean, variance)
