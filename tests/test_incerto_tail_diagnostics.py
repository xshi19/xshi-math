"""Tests for tail-class diagnostic helpers."""

import numpy as np
import pytest
from scipy.stats import expon, gamma as gamma_dist, pareto, uniform, weibull_min

from xmath.incerto.tail_diagnostics import (
    iid_two_sum_tail,
    regular_variation_ratio,
    subexponential_sum_ratio,
)


def test_regular_variation_ratio_matches_power_tail() -> None:
    thresholds = np.array([1.0, 2.0, 4.0])

    result = regular_variation_ratio(
        lambda x: x**-2.0,
        thresholds,
        multiplier=3.0,
    )

    np.testing.assert_allclose(result["threshold"], thresholds)
    np.testing.assert_allclose(result["survival"], thresholds**-2.0)
    np.testing.assert_allclose(result["ratio"], np.full(3, 1.0 / 9.0))


def test_regular_variation_ratio_validates_inputs() -> None:
    with pytest.raises(ValueError, match="thresholds"):
        regular_variation_ratio(lambda x: x, [0.0])
    with pytest.raises(ValueError, match="multiplier"):
        regular_variation_ratio(lambda x: x, [1.0], multiplier=0.0)
    with pytest.raises(ValueError, match="positive"):
        regular_variation_ratio(lambda x: np.zeros_like(x), [1.0])


def test_iid_two_sum_tail_matches_exponential_closed_form() -> None:
    x = np.array([2.01, 4.0, 10.0, 50.0])

    result = iid_two_sum_tail(expon(scale=1.0), x)
    scalar_result = iid_two_sum_tail(expon(scale=1.0), 4.0)

    np.testing.assert_allclose(result["threshold"], x)
    np.testing.assert_allclose(result["x"], x)
    np.testing.assert_allclose(result["ratio"], (1.0 + x) / 2.0, rtol=1e-10)
    np.testing.assert_allclose(scalar_result["ratio"], [2.5], rtol=1e-10)
    np.testing.assert_allclose(
        result["tail"],
        expon(scale=1.0).sf(x) * (1.0 + x),
        rtol=1e-10,
    )
    assert np.all(result["success"])


def test_iid_two_sum_tail_matches_gamma_convolution() -> None:
    x = np.array([2.01, 4.0, 10.0, 50.0])

    result = iid_two_sum_tail(gamma_dist(a=2.0, scale=1.0), x)
    expected = gamma_dist(a=4.0, scale=1.0).sf(x) / (
        2.0 * gamma_dist(a=2.0, scale=1.0).sf(x)
    )

    np.testing.assert_allclose(result["ratio"], expected, rtol=2e-10)
    assert np.all(result["success"])


def test_iid_two_sum_tail_handles_weibull_endpoint_singularity() -> None:
    x = np.geomspace(2.01, 100.0, 8)

    result = iid_two_sum_tail(weibull_min(c=0.5, scale=1.0), x)

    assert np.all(result["success"])
    assert np.all(np.isfinite(result["log_ratio"]))
    assert np.all(result["ratio"] > 0.0)


def test_iid_two_sum_tail_validates_support_and_logsf() -> None:
    with pytest.raises(ValueError, match="right support"):
        iid_two_sum_tail(uniform(loc=0.0, scale=1.0), [2.0])
    with pytest.raises(ValueError, match="twice the lower support"):
        iid_two_sum_tail(pareto(b=1.5, scale=1.0), [1.5])
    with pytest.raises(ValueError, match="positive"):
        iid_two_sum_tail(expon(scale=1.0), [0.0])


def test_subexponential_sum_ratio_uses_sampler_and_survival() -> None:
    thresholds = np.array([4.0, 6.0])

    def sampler(sample_size: int, rng: np.random.Generator) -> np.ndarray:
        assert isinstance(rng, np.random.Generator)
        return np.arange(1.0, sample_size + 1.0)

    result = subexponential_sum_ratio(
        sampler,
        lambda x: np.array([0.25, 0.125]),
        thresholds,
        sample_size=4,
        random_state=123,
    )

    np.testing.assert_allclose(result["sum_exceedances"], [2.0, 1.0])
    np.testing.assert_allclose(result["sum_tail"], [0.5, 0.25])
    np.testing.assert_allclose(result["single_tail"], [0.25, 0.125])
    np.testing.assert_allclose(result["ratio"], [1.0, 1.0])


def test_subexponential_sum_ratio_validates_samples_and_size() -> None:
    def bad_sampler(sample_size: int, rng: np.random.Generator) -> np.ndarray:
        return np.ones(sample_size + 1)

    with pytest.raises(TypeError, match="sample_size"):
        subexponential_sum_ratio(bad_sampler, lambda x: x, [1.0], sample_size=1.5)
    with pytest.raises(ValueError, match="sample_size"):
        subexponential_sum_ratio(bad_sampler, lambda x: x, [1.0], sample_size=0)
    with pytest.raises(ValueError, match="one-dimensional"):
        subexponential_sum_ratio(bad_sampler, lambda x: x, [1.0], sample_size=3)
