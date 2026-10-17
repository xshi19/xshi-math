"""Tests for tail estimators and finite-sample diagnostics."""

import numpy as np
import pytest

from xmath.incerto.estimators import (
    hill_alpha_estimator,
    hill_estimator,
    hill_stability,
    max_to_sum_ratio,
    mean_excess,
    pareto_mean_plugin,
    running_mean,
)


def test_hill_estimator_matches_order_statistic_formula() -> None:
    sample = np.array([1.0, 2.0, 4.0, 8.0, 16.0])

    expected_xi = (np.log(16.0 / 4.0) + np.log(8.0 / 4.0)) / 2.0

    assert hill_estimator(sample, k=2) == pytest.approx(expected_xi)
    assert hill_alpha_estimator(sample, k=2) == pytest.approx(1.0 / expected_xi)


def test_hill_stability_returns_k_xi_and_alpha_arrays() -> None:
    sample = np.array([1.0, 2.0, 4.0, 8.0, 16.0])

    stability = hill_stability(sample, k_values=[1, 2, 3])

    np.testing.assert_allclose(stability["k"], np.array([1.0, 2.0, 3.0]))
    np.testing.assert_allclose(stability["alpha"], 1.0 / stability["xi"])


@pytest.mark.parametrize("k", [0, 5])
def test_hill_estimator_rejects_invalid_k(k: int) -> None:
    sample = np.array([1.0, 2.0, 4.0, 8.0, 16.0])

    with pytest.raises(ValueError):
        hill_estimator(sample, k=k)


def test_hill_estimator_rejects_nonpositive_values() -> None:
    with pytest.raises(ValueError):
        hill_estimator(np.array([0.0, 1.0, 2.0]), k=1)


def test_running_mean() -> None:
    np.testing.assert_allclose(running_mean([1.0, 3.0, 2.0]), [1.0, 2.0, 2.0])


def test_max_to_sum_ratio_vectorized_over_axis() -> None:
    samples = np.array([[1.0, 1.0, 8.0], [2.0, 3.0, 5.0]])

    np.testing.assert_allclose(max_to_sum_ratio(samples, axis=1), [0.8, 0.5])


def test_max_to_sum_ratio_rejects_negative_values() -> None:
    with pytest.raises(ValueError):
        max_to_sum_ratio([1.0, -1.0, 3.0])


def test_mean_excess_reports_threshold_means_and_counts() -> None:
    result = mean_excess([1.0, 2.0, 4.0, 8.0], [1.0, 2.0, 7.0])

    np.testing.assert_allclose(result["threshold"], [1.0, 2.0, 7.0])
    np.testing.assert_allclose(result["mean_excess"], [11.0 / 3.0, 4.0, 1.0])
    np.testing.assert_allclose(result["exceedances"], [3.0, 2.0, 1.0])


def test_mean_excess_uses_nan_when_exceedance_count_is_too_small() -> None:
    result = mean_excess([1.0, 2.0, 4.0], [3.0], min_exceedances=2)

    assert np.isnan(result["mean_excess"][0])
    assert result["exceedances"][0] == 1.0


def test_pareto_mean_plugin_agrees_with_scipy_fixed_cutoff_fit() -> None:
    from scipy.stats import pareto

    sample = pareto.rvs(1.5, scale=3.0, size=2_000,
                        random_state=np.random.default_rng(20260912))
    alpha, loc, scale = pareto.fit(sample, floc=0.0, fscale=3.0)
    expected = pareto.mean(alpha, loc=loc, scale=scale)

    assert pareto_mean_plugin(sample, x_m=3.0) == pytest.approx(expected, rel=1e-12)


def test_pareto_mean_plugin_vectorizes_and_respects_units() -> None:
    # Two fitted log-excess means: 1/2 and 1/4.
    samples = np.exp([[0.25, 0.75], [0.125, 0.375]])
    np.testing.assert_allclose(pareto_mean_plugin(samples, x_m=1, axis=1),
                               [2.0, 4.0 / 3.0], rtol=1e-14)
    np.testing.assert_allclose(pareto_mean_plugin(7 * samples.T, x_m=7, axis=0),
                               [14.0, 28.0 / 3.0], rtol=1e-14)
    np.testing.assert_allclose(pareto_mean_plugin(samples, x_m=1, axis=-1),
                               [2.0, 4.0 / 3.0], rtol=1e-14)
    assert pareto_mean_plugin(samples, x_m=1) == pytest.approx(1.6)


def test_pareto_mean_plugin_reports_mean_boundary_without_clipping() -> None:
    samples = np.exp([[1.0, 1.0], [0.5, 2.0], [0.5, 0.5]])
    result = pareto_mean_plugin(samples, x_m=1, axis=1)
    assert np.all(np.isinf(result[:2]))
    assert result[2] == pytest.approx(2.0)


def test_pareto_mean_plugin_scalar_and_all_cutoff_limit() -> None:
    assert pareto_mean_plugin(3.0, x_m=3.0) == 3.0
    assert pareto_mean_plugin([3.0, 3.0], x_m=3.0) == 3.0
    assert isinstance(pareto_mean_plugin([3.0], x_m=3.0), float)


def test_pareto_mean_plugin_extreme_scales_and_near_boundary() -> None:
    with np.errstate(all="raise"):
        assert np.isinf(pareto_mean_plugin([1e-300, 1e300], x_m=1e-300))
        # Subtracting logs at this scale would lose the small excess.
        cutoff = 1e300
        observation = cutoff * (1 + 1e-12)
        assert pareto_mean_plugin(observation, x_m=cutoff) == pytest.approx(
            observation, rel=2e-16
        )
        assert pareto_mean_plugin(np.exp(1 - 1e-6), x_m=1) == pytest.approx(
            1e6, rel=1e-9
        )


@pytest.mark.parametrize("x_m", [0, -1, np.nan, np.inf, [1.0]])
def test_pareto_mean_plugin_rejects_invalid_cutoff(x_m) -> None:
    with pytest.raises(ValueError, match="finite positive scalar"):
        pareto_mean_plugin([1.0, 2.0], x_m=x_m)


@pytest.mark.parametrize("sample", [[], np.empty((2, 0)), [1.0, np.nan],
                                    [1.0, np.inf], [0.0, 2.0], [-1.0], [0.9]])
def test_pareto_mean_plugin_rejects_invalid_observations(sample) -> None:
    with pytest.raises(ValueError, match="observation|finite"):
        pareto_mean_plugin(sample, x_m=1.0)
