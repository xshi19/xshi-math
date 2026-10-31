"""Chapter 11: independent integrals, exact enumerations and boundary cases."""

from itertools import product
from fractions import Fraction

import numpy as np
import pytest
from scipy.integrate import quad
from scipy.stats import beta, lognorm, pareto

from xmath.incerto.calibration import (
    beta_brier_cdf, beta_brier_moments, binary_tally_distribution,
    brier_score, brier_score_distribution, calibration_curve,
    lognormal_tail_bet, pareto_tail_bet, point_forecast_loss,
    simulate_brier_scores, tail_bet_payoffs,
)


def test_tail_payoff_ties_and_decomposition():
    x = np.array([-2., 0., 2., 5.])
    result = tail_bet_payoffs(x, 2)
    np.testing.assert_array_equal(result["binary"], [0, 0, 0, 1])
    np.testing.assert_array_equal(result["excess"], [0, 0, 0, 3])
    np.testing.assert_array_equal(result["tail_level"], 2*result["binary"]+result["excess"])
    assert tail_bet_payoffs(2, 2)["binary"] == 0
    with pytest.raises(OverflowError):
        tail_bet_payoffs([1e308], -1e308)


@pytest.mark.parametrize("a", [.8, 1, 1.5, 3, 8])
@pytest.mark.parametrize("u", [2, 7])
def test_pareto_integrals(a, u):
    result = pareto_tail_bet(a, u, xm=2)
    law = pareto(a, scale=2)
    assert result["probability"] == pytest.approx(law.sf(u))
    if a <= 1:
        assert result["excess_mean"] == result["tail_mean"] == np.inf
    else:
        for name, payoff in (("excess_mean", lambda x: x-u), ("tail_mean", lambda x: x)):
            value, error = quad(lambda x: payoff(x)*law.pdf(x), u, np.inf, epsabs=1e-9)
            assert error < 1e-6
            assert result[name] == pytest.approx(value, rel=1e-8)


def test_pareto_log_evaluation_preserves_representable_mean():
    result = pareto_tail_bet(2, 1e200)
    assert result["probability"] == 0
    assert result["excess_mean"] == pytest.approx(1e-200, rel=1e-12, abs=0)
    with pytest.raises(OverflowError):
        pareto_tail_bet(1.01, 1e308, xm=1e308)


@pytest.mark.parametrize("s", [.1, 1, 2])
def test_lognormal_density_integrals(s):
    m = 3
    result = lognormal_tail_bet(s, mean=m)
    law = lognorm(s, scale=m*np.exp(-s*s/2))
    assert result["probability"] == pytest.approx(law.sf(m))
    for name, payoff in (("excess_mean", lambda x: x-m), ("tail_mean", lambda x: x)):
        value, _ = quad(lambda x: payoff(x)*law.pdf(x), m, np.inf)
        assert result[name] == pytest.approx(value, rel=1e-7)
    assert result["tail_mean"] == pytest.approx(m*result["probability"]+result["excess_mean"])


def test_lognormal_degeneracy_and_small_scale():
    assert set(lognormal_tail_bet(0).values()) == {0}
    assert lognormal_tail_bet(1e-20)["excess_mean"] == pytest.approx(1e-20/np.sqrt(2*np.pi), rel=1e-14, abs=0)
    assert lognormal_tail_bet(1e308)["excess_mean"] == 1


def test_lognormal_subnormal_scale_preserves_representable_payoff():
    sigma = np.nextafter(0., 1.)
    # At this scale the relative cubic correction is below 1e-647.
    expected = (1e308*sigma)/np.sqrt(2*np.pi)
    assert lognormal_tail_bet(sigma, mean=1e308)["excess_mean"] == pytest.approx(
        expected, rel=1e-14, abs=0,
    )


@pytest.mark.parametrize("p", [0, .1, .5, 1])
@pytest.mark.parametrize("q", [0, .2, .5, .8, 1])
def test_finite_score_law_by_enumeration(p, q):
    n = 5
    values, weights = brier_score_distribution(n, p, q)
    exact = []
    for outcome in product((0, 1), repeat=n):
        k = sum(outcome)
        exact.append((sum((q-d)**2 for d in outcome)/n, p**k*(1-p)**(n-k)))
    assert weights.sum() == pytest.approx(1)
    assert np.all(np.diff(values) > 0)
    for power in (1, 2, 3, 4):
        assert weights @ values**power == pytest.approx(sum(s**power*w for s, w in exact), abs=1e-14)
    fractions, mass = binary_tally_distribution(n, p)
    assert mass @ fractions == pytest.approx(p)
    assert mass @ (fractions-p)**2 == pytest.approx(p*(1-p)/n)


def test_bounded_score_can_have_large_kurtosis():
    z, mass = brier_score_distribution(1, .01, 0)
    mean = mass @ z
    variance = mass @ (z-mean)**2
    assert mass @ (z-mean)**4/variance**2 > 98


@pytest.mark.parametrize("a,b", [(1, 1), (2, 5), (.4, 1.3)])
@pytest.mark.parametrize("p", [None, 0, .3, 1])
def test_beta_moments_and_cdf_from_joint_density(a, b, p):
    law = beta(a, b)
    chance = (lambda q: q) if p is None else (lambda q: p)
    moments = []
    for r in (1, 2):
        value, _ = quad(lambda q: law.pdf(q)*((1-chance(q))*q**(2*r)
                                            + chance(q)*(1-q)**(2*r)), 0, 1)
        moments.append(value)
    result = beta_brier_moments(a, b, p=p, n=17)
    assert result["mean"] == pytest.approx(moments[0], rel=2e-8)
    assert result["score_variance"] == pytest.approx(moments[1]-moments[0]**2, rel=2e-8)
    assert result["average_variance"]*17 == pytest.approx(result["score_variance"])
    for z in (.01, .25, .81):
        s = np.sqrt(z)
        left = quad(lambda q: (1-chance(q))*law.pdf(q), 0, s)[0]
        right = quad(lambda q: chance(q)*law.pdf(q), 1-s, 1)[0]
        assert float(beta_brier_cdf(z, a, b, p=p)) == pytest.approx(left+right, rel=2e-8)


def test_uniform_beta_closed_forms_and_endpoints():
    z = np.linspace(0, 1, 31)
    np.testing.assert_allclose(beta_brier_cdf(z, 1, 1, p=.2), np.sqrt(z))
    np.testing.assert_allclose(beta_brier_cdf(z, 1, 1), 2*np.sqrt(z)-z)
    np.testing.assert_array_equal(beta_brier_cdf([-np.inf, -1, 0, 1, np.inf], 2, 5), [0, 0, 0, 1, 1])
    assert beta_brier_moments(1, 1, p=.2)["score_variance"] == pytest.approx(4/45)
    assert beta_brier_moments(1, 1)["score_variance"] == pytest.approx(7/180)


def test_beta_cdf_near_one_with_endpoint_singularities():
    # 80-digit mpmath integration at the exact binary float z and shapes.
    expected = .518368261894198
    z = np.nextafter(1., 0.)
    for p in (0, .3, 1):
        assert float(beta_brier_cdf(z, .001, .001, p=p)) == pytest.approx(
            expected, rel=0, abs=2e-15,
        )
    for a, b, p in ((.001, 10000, 1), (10000, .001, 0)):
        assert float(beta_brier_cdf(z, a, b, p=p)) == pytest.approx(
            .027264685119773348, rel=0, abs=2e-15,
        )


@pytest.mark.parametrize("a,b", [(.001, 10000), (10000, .001), (10000, 10000)])
@pytest.mark.parametrize("p", [None, 0, .3, 1])
def test_beta_boundary_variance_against_exact_rational_raw_moments(a, b, p):
    a_exact, b_exact = Fraction(str(a)), Fraction(str(b))
    def rising(x, n):
        result = Fraction(1)
        for k in range(n):
            result *= x+k
        return result
    def moment(r):
        if p is None:
            return (rising(a_exact, 2*r)*b_exact+a_exact*rising(b_exact, 2*r)
                    )/rising(a_exact+b_exact, 2*r+1)
        p_exact = Fraction(str(p))
        return ((1-p_exact)*rising(a_exact, 2*r)+p_exact*rising(b_exact, 2*r)
                )/rising(a_exact+b_exact, 2*r)
    mean = moment(1)
    variance = moment(2)-mean*mean
    result = beta_brier_moments(a, b, p=p, n=100000)
    assert result["mean"] == pytest.approx(float(mean), rel=2e-14, abs=0)
    assert result["score_variance"] == pytest.approx(float(variance), rel=2e-12, abs=0)
    assert result["average_variance"] == pytest.approx(float(variance)/100000, rel=2e-12, abs=0)


@pytest.mark.parametrize("p", [None, .3])
def test_beta_simulation_reproducibility_and_exact_benchmarks(p):
    settings = dict(a=2, b=5, n=20, p=p, repetitions=30_000, seed=311)
    sample = simulate_brier_scores(**settings)
    np.testing.assert_array_equal(sample, simulate_brier_scores(**settings))
    target = beta_brier_moments(2, 5, p=p, n=20)
    assert abs(sample.mean()-target["mean"]) < 5*np.sqrt(target["average_variance"]/len(sample))
    assert sample.var() == pytest.approx(target["average_variance"], rel=.04)
    assert np.all((sample >= 0) & (sample <= 1))


def test_calibration_bins_and_empty_bins():
    curve = calibration_curve([0, .25, .5, 1], [0, 1, 0, 1], bins=4)
    np.testing.assert_array_equal(curve["count"], [1, 1, 1, 1])
    np.testing.assert_array_equal(curve["forecast_mean"], [0, .25, .5, 1])
    curve = calibration_curve([0, 1], [0, 1], bins=3)
    assert np.isnan(curve["event_frequency"][1]) and curve["count"][1] == 0
    assert brier_score([0, 1], [0, 1]) == 0
    assert brier_score([0, 1], [1, 0]) == 1


def test_point_loss_metrics_and_float_range():
    x, d = [0, 2, 5], [0, 1, 1]
    np.testing.assert_array_equal(point_forecast_loss(x, d), [0, 1, 4])
    np.testing.assert_array_equal(point_forecast_loss(x, d, metric="squared"), [0, 1, 16])
    np.testing.assert_allclose(point_forecast_loss(x, d, metric="smape"), [0, 2/3, 4/3])
    np.testing.assert_allclose(point_forecast_loss(x, d, metric="mase", scale=2), [0, .5, 2])
    assert point_forecast_loss(1e308, -1e308, metric="smape") == 2
    assert point_forecast_loss(1e308, -1e308, metric="mase", scale=1e308) == 2
    with pytest.raises(OverflowError):
        point_forecast_loss(1e308, -1e308)
    with pytest.raises(OverflowError):
        point_forecast_loss(1e200, 0, metric="squared")


@pytest.mark.parametrize("call", [
    lambda: tail_bet_payoffs([np.nan], 1),
    lambda: pareto_tail_bet(0, 2), lambda: pareto_tail_bet(2, .5),
    lambda: lognormal_tail_bet(-1), lambda: lognormal_tail_bet(np.inf),
    lambda: binary_tally_distribution(True, .2), lambda: binary_tally_distribution(0, .2),
    lambda: binary_tally_distribution(2, np.nan), lambda: brier_score_distribution(2, .2, 2),
    lambda: brier_score([], []), lambda: brier_score([.1], [2]),
    lambda: brier_score([.1, .2], [1]), lambda: brier_score([np.inf], [1]),
    lambda: beta_brier_moments(0, 2), lambda: beta_brier_moments(2, 1e6),
    lambda: beta_brier_cdf(np.nan, 2, 3), lambda: beta_brier_moments(2, 3, p=-.1),
    lambda: simulate_brier_scores(2, 3, 100_000),
    lambda: simulate_brier_scores(2, 3, 1, seed=-1),
    lambda: calibration_curve([.1], [0], bins=0),
    lambda: point_forecast_loss(1, np.nan),
    lambda: point_forecast_loss(1, 2, metric="mase", scale=0),
    lambda: point_forecast_loss(1, 2, metric="mase", scale=np.array([2.])),
    lambda: point_forecast_loss(1, 2, metric="mase", scale=np.array([[2.]])),
    lambda: point_forecast_loss(1, 2, scale=1),
    lambda: point_forecast_loss(1, 2, metric="other"),
])
def test_invalid_domains(call):
    with pytest.raises(ValueError):
        call()
