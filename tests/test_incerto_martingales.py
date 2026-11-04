"""Independent Gaussian integrals, exact finite trees, and forecast boundaries."""

import numpy as np
import pytest
from scipy.integrate import quad
from scipy.special import ndtr, ndtri
from scipy.stats import norm

from xmath.incerto.martingales import (
    gaussian_binary_probability, probit_binary_probability,
    simulate_probit_forecasts, forecast_revision_summary,
)


@pytest.mark.parametrize("mean,sigma,tau,u", [
    (.54, .08, 1, .5), (.42, .2, .3, .6), (-2, 3, 2, -1), (.5, 1, 2, .5),
])
def test_gaussian_against_density_integral(mean, sigma, tau, u):
    law = norm(loc=mean, scale=sigma*np.sqrt(tau))
    expected, error = quad(law.pdf, u, np.inf, epsabs=1e-12, epsrel=1e-12)
    assert error < 1e-9
    assert gaussian_binary_probability(mean, sigma, tau, threshold=u) == pytest.approx(expected)


@pytest.mark.parametrize("function", [gaussian_binary_probability, probit_binary_probability])
def test_strict_degenerate_event_and_shape(function):
    for sigma, tau in ((0, 1), (1, 0), (0, 0)):
        np.testing.assert_array_equal(function([.4, .5, .6], sigma, tau), [0, 0, 1])
    assert isinstance(function(.5, 1, 1), float)
    assert function([[.4, .5], [.6, .8]], .8, 1).shape == (2, 2)
    assert function(.5, 1, 1) == .5


def test_gaussian_extreme_finite_arithmetic():
    # Both the margin and its variance overflow ordinary float intermediates.
    p = gaussian_binary_probability(1e308, 1e308, 1, threshold=-1e308)
    assert p == pytest.approx(ndtr(2), rel=1e-14)
    assert gaussian_binary_probability(1e-300, 1e-300, 1, threshold=0) == pytest.approx(ndtr(1))
    assert gaussian_binary_probability(-1, 1e-300, 1e-300) == 0
    assert gaussian_binary_probability(1, 1e-300, 1e-300) == 1


@pytest.mark.parametrize("y,u,sigma,tau", [
    (.2, .5, .8, 1), (.54, .5, .3, 2), (.7, .35, .9, .4), (.5, .7, .6, 2),
])
def test_probit_value_against_latent_density(y, u, sigma, tau):
    q = sigma*sigma*tau
    mean, sd = np.exp(q/2)*ndtri(y), np.sqrt(np.expm1(q))
    expected, error = quad(norm(loc=mean, scale=sd).pdf, ndtri(u), np.inf, epsabs=1e-12)
    assert error < 1e-8
    assert probit_binary_probability(y, sigma, tau, threshold=u) == pytest.approx(expected, abs=1e-12)


@pytest.mark.parametrize("y,u", [(.2, .35), (.54, .5), (.75, .7)])
def test_bounded_share_and_event_tower_by_quadrature(y, u):
    sigma, earlier, later = .7, .4, .8
    q = sigma*sigma*earlier
    mean, sd = np.exp(q/2)*ndtri(y), np.sqrt(np.expm1(q))
    share_mean = quad(lambda n: ndtr(mean+sd*n)*norm.pdf(n), -10, 10, epsabs=1e-12)[0]
    value_mean = quad(lambda n: probit_binary_probability(
        ndtr(mean+sd*n), sigma, later, threshold=u)*norm.pdf(n), -10, 10, epsabs=1e-12)[0]
    assert share_mean == pytest.approx(y, abs=1e-12)
    assert value_mean == pytest.approx(
        probit_binary_probability(y, sigma, earlier+later, threshold=u), abs=2e-12)


def test_distinct_high_uncertainty_limits_and_absorbing_endpoints():
    for y in (.15, .54, .9):
        assert gaussian_binary_probability(y, 1e12, 1) == pytest.approx(.5, abs=1e-12)
        for u in (.2, .5, .8):
            assert probit_binary_probability(y, 10, 1, threshold=u) == pytest.approx(y, abs=1e-14)
        values = [probit_binary_probability(y, s, 1) for s in (.1, .3, 1, 3)]
        assert all(y <= v <= 1 for v in values) if y > .5 else all(0 <= v <= y for v in values)
        assert all(np.diff(values) <= 0) if y > .5 else all(np.diff(values) >= 0)
    np.testing.assert_array_equal(probit_binary_probability([0, 1], 1, 1), [0, 1])


def test_positive_variance_tie_and_tiny_variance():
    for y in (.2, .5, .8):
        p = probit_binary_probability(y, 1e-200, 1e-200, threshold=y)
        assert p == pytest.approx(.5, abs=1e-15)
        assert probit_binary_probability(y, 0, 1, threshold=y) == 0
    assert probit_binary_probability(.4, 1e-200, 1e-200) == 0
    assert probit_binary_probability(.6, 1e-200, 1e-200) == 1


@pytest.mark.parametrize("u", [1e-300, 1e-100, .01, .2, .8])
def test_adjacent_shares_preserve_strict_order(u):
    y = np.nextafter(u, 1.)
    # ndtri(y) and ndtri(u) can round to the same float; the event is distinct.
    sample = simulate_probit_forecasts(y, 0, 1, threshold=u, steps=3, paths=1)
    np.testing.assert_array_equal(sample["probability"], np.ones((1, 4)))
    assert probit_binary_probability(y, 1e-200, 1, threshold=u) == 1
    assert probit_binary_probability(u, 1e-200, 1, threshold=y) == 0


def test_adjacent_share_quantile_difference_via_inverse_derivative():
    u = .01
    y = np.nextafter(u, 1.)
    delta = (y-u)/norm.pdf(ndtri(u))
    # At this scale higher derivative terms are below double precision.
    sigma = delta / .7
    assert probit_binary_probability(y, sigma, 1, threshold=u) == pytest.approx(ndtr(.7), rel=1e-13)


@pytest.mark.parametrize("function", [gaussian_binary_probability, probit_binary_probability])
@pytest.mark.parametrize("value", [np.nan, np.inf, -np.inf])
def test_nonfinite_inputs_rejected(function, value):
    for args, kwargs in (((value, 1, 1), {}), ((.5, value, 1), {}),
                         ((.5, 1, value), {}), ((.5, 1, 1), {"threshold": value})):
        with pytest.raises(ValueError):
            function(*args, **kwargs)


@pytest.mark.parametrize("function", [gaussian_binary_probability, probit_binary_probability])
@pytest.mark.parametrize("args", [([], 1, 1), (.5, -1, 1), (.5, 1, -1)])
def test_empty_and_negative_domains(function, args):
    with pytest.raises(ValueError):
        function(*args)


@pytest.mark.parametrize("y,u", [(-.1, .5), (1.1, .5), (.5, 0), (.5, 1)])
def test_probit_share_threshold_domains(y, u):
    with pytest.raises(ValueError):
        probit_binary_probability(y, 1, 1, threshold=u)


def test_exact_finite_tree_revision_and_score_identities():
    # Eight equiprobable leaves: the conditional success rates are 1/4, 3/4.
    p = np.array([[.5, .25, 0]]*3 + [[.5, .25, 1]] +
                 [[.5, .75, 0]] + [[.5, .75, 1]]*3)
    result = forecast_revision_summary(p)
    assert result["paths"] == 8
    assert result["squared_revision"] == result["initial_budget"] == .25
    assert result["budget_gap"] == 0
    np.testing.assert_array_equal(result["mean_revision"], [0, 0])
    np.testing.assert_array_equal(result["level_moment"], [0, 0])
    np.testing.assert_array_equal(result["brier"], [.25, .1875, 0])
    np.testing.assert_allclose(-np.diff(result["brier"]), np.mean(np.diff(p)**2, axis=0))
    # Conditional start: each branch separately satisfies the remaining budget.
    for branch in (p[:4, 1:], p[4:, 1:]):
        assert forecast_revision_summary(branch)["budget_gap"] == 0


def test_independent_row_standard_errors_and_one_row_nan():
    p = np.array([[.5, .25, 0], [.5, .25, 1]])
    result = forecast_revision_summary(p)
    assert result["budget_gap_se"] == pytest.approx(.25)
    np.testing.assert_allclose(result["revision_se"], [0, .5])
    np.testing.assert_allclose(result["level_moment_se"], [0, .125])
    one = forecast_revision_summary(p[:1])
    for key in ("budget_gap_se", "squared_revision_se", "revision_se", "level_moment_se"):
        assert np.all(np.isnan(one[key]))


def test_pathwise_trading_identity_is_not_the_expectation_budget():
    p = np.array([[.5, .1, .9, .1, 1], [.5, .9, .1, .9, 0]])
    delta = np.diff(p, axis=1)
    gain = np.sum(2*(p[:, :1]-p[:, :-1])*delta, axis=1)
    energy = np.sum(delta**2, axis=1)
    np.testing.assert_allclose(gain, energy-(p[:, -1]-p[:, 0])**2)
    assert np.all(gain > 0)
    assert forecast_revision_summary(p)["budget_gap"] > 0


def test_predictable_level_moment_detects_constant_mean_failure():
    # Constant marginal mean at every date, but intermediate quotes add noise.
    p = np.array([[.5, .1, 0], [.5, .1, 1], [.5, .9, 0], [.5, .9, 1]])
    result = forecast_revision_summary(p)
    np.testing.assert_allclose(result["mean_revision"], 0, atol=1e-15)
    assert result["level_moment"][-1] == pytest.approx(-.16)
    assert result["budget_gap"] == pytest.approx(.32)


def test_simulator_reproducibility_and_exact_transition_moments():
    sample = simulate_probit_forecasts(.54, .8, 1, steps=4, paths=40000, seed=1410)
    again = simulate_probit_forecasts(.54, .8, 1, steps=4, paths=40000, seed=1410)
    for key in sample:
        np.testing.assert_array_equal(sample[key], again[key])
    latent = sample["latent"]
    expected_mean = np.exp(.8**2/2)*ndtri(.54)
    expected_var = np.expm1(.8**2)
    assert abs(latent[:, -1].mean()-expected_mean) < 6*np.sqrt(expected_var/40000)
    assert abs(latent[:, -1].var()-expected_var) < 6*expected_var*np.sqrt(2/39999)
    np.testing.assert_array_equal(sample["outcome"], (latent[:, -1] > 0).astype(float))
    np.testing.assert_array_equal(sample["probability"][:, -1], sample["outcome"])
    np.testing.assert_allclose(sample["share"], ndtr(latent))
    assert abs(sample["share"][:, -1].mean()-.54) < 6*sample["share"][:, -1].std()/200
    summary = forecast_revision_summary(sample["probability"])
    assert abs(summary["budget_gap"]) < 6*summary["budget_gap_se"]
    assert np.all(abs(summary["mean_revision"]) < 6*summary["revision_se"])
    assert np.all(abs(summary["level_moment"]) <= 6*summary["level_moment_se"] + 1e-16)


def test_simulator_keeps_latent_after_cdf_rounding():
    sample = simulate_probit_forecasts(.54, 5, 1, steps=10, paths=20, seed=1411)
    assert np.any((sample["share"] == 0) | (sample["share"] == 1))
    assert np.all(np.isfinite(sample["latent"]))
    assert np.all(np.isfinite(sample["probability"]))
    np.testing.assert_array_equal(sample["outcome"], (sample["latent"][:, -1] > 0))


def test_deterministic_simulation_and_one_step():
    for share in (.3, .5, .8):
        sample = simulate_probit_forecasts(share, 0, 1, paths=2, steps=1)
        np.testing.assert_allclose(sample["share"], share)
        np.testing.assert_array_equal(sample["probability"], float(share > .5)*np.ones((2, 2)))
    sample = simulate_probit_forecasts(.6, .8, 1, steps=1, paths=100, threshold=.7)
    np.testing.assert_array_equal(sample["outcome"], sample["latent"][:, -1] > ndtri(.7))


@pytest.mark.parametrize("sigma", [1e-6, np.sqrt(50)])
@pytest.mark.parametrize("horizon", [1, .25, 4])
def test_simulator_nominal_endpoints_and_rounding_tolerance(sigma, horizon):
    sigma /= np.sqrt(horizon)
    params = dict(share=.54, horizon=horizon, steps=4, paths=8, seed=1412)
    endpoint = simulate_probit_forecasts(sigma=sigma, **params)
    for key, values in endpoint.items():
        assert np.all(np.isfinite(values)), key
    np.testing.assert_array_equal(endpoint["probability"][:, -1], endpoint["outcome"])

    # Both inward and outward roundoff must give the same endpoint model.
    # Two epsilons in sigma give about four in integrated variance.
    for direction in (-1, 1):
        nearby = simulate_probit_forecasts(
            sigma=sigma * (1 + direction * 2 * np.finfo(float).eps), **params)
        for key in endpoint:
            np.testing.assert_array_equal(nearby[key], endpoint[key])


@pytest.mark.parametrize("sigma,direction", [(1e-6, -1), (np.sqrt(50), 1)])
@pytest.mark.parametrize("horizon", [1, .25, 4])
def test_simulator_rejects_values_beyond_endpoint_rounding_tolerance(sigma, direction, horizon):
    # About sixteen epsilons in variance is outside the eight-epsilon band.
    sigma = sigma / np.sqrt(horizon) * (1 + direction * 8 * np.finfo(float).eps)
    with pytest.raises(ValueError, match="integrated latent variance"):
        simulate_probit_forecasts(.54, sigma, horizon, steps=4, paths=8)


@pytest.mark.parametrize("kwargs", [
    {"steps": 0}, {"steps": True}, {"steps": 1.5}, {"paths": 0}, {"paths": True},
    {"paths": 50000, "steps": 100}, {"seed": -1}, {"seed": True}, {"seed": .5},
    {"sigma": np.nan}, {"sigma": np.inf}, {"sigma": -1}, {"sigma": 8}, {"sigma": 1e-8},
    {"horizon": 0}, {"horizon": np.inf}, {"share": 0}, {"share": 1}, {"threshold": 0},
])
def test_simulator_domains(kwargs):
    params = dict(share=.5, sigma=.8, horizon=1, paths=2)
    params.update(kwargs)
    with pytest.raises(ValueError):
        simulate_probit_forecasts(**params)


@pytest.mark.parametrize("p", [[], [.5, 1], [[.5]], [[.5, .6]], [[np.nan, 1]],
                                   [[np.inf, 1]], [[-.1, 0]], [[1.1, 1]], np.zeros((0, 2))])
def test_summary_domains(p):
    with pytest.raises(ValueError):
        forecast_revision_summary(p)
