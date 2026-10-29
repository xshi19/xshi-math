"""Analytic cases, time-order contracts, ties and numerical boundaries."""

from itertools import permutations

import numpy as np
import pytest
from scipy.stats import kurtosis

from xmath.incerto.datasets import PriceSeries
from xmath.incerto.diagnostics import (
    aggregate_returns, aggregation_diagnostics, chronological_tail_check,
    conditional_tail_ratio, hinge_payoff, maximum_drawdown, moment_share_path,
    record_counts, sample_excess_kurtosis, sp500_diagnostics,
)
from xmath.incerto.estimators import max_to_sum_path


def test_aggregation_keeps_time_and_drops_only_suffix():
    x = [1, -2, 4, -8, 16]
    assert aggregate_returns(x, 2).tolist() == [-1, -4]
    assert aggregate_returns(x, 2, overlap=True).tolist() == [-1, 2, -4, 8]
    assert aggregate_returns(x, 5).tolist() == [11]
    assert aggregate_returns(x, 1).tolist() == x


@pytest.mark.parametrize("h", [0, -1, True, 1.5, 6])
def test_bad_horizons(h):
    with pytest.raises(ValueError):
        aggregate_returns([1,2,3,4,5], h)


@pytest.mark.parametrize("x", [[], [[1,2]], [np.nan], [np.inf], [1j]])
@pytest.mark.parametrize("fn", [aggregate_returns, sample_excess_kurtosis,
                                maximum_drawdown, moment_share_path, record_counts])
def test_invalid_samples(fn, x):
    with pytest.raises(ValueError):
        fn(x, 1) if fn is aggregate_returns else fn(x)


def test_kurtosis_against_independent_library_and_invariances():
    x = np.array([-3., -1., 0., 2., 8.])
    expected = kurtosis(x, fisher=True, bias=True)
    for sample in (x, 3*x+200, -x, 1e250*x, 1e-250*x):
        assert sample_excess_kurtosis(sample) == pytest.approx(expected)
    assert np.isnan(sample_excess_kurtosis([4,4]))
    assert np.isnan(sample_excess_kurtosis([4]))
    assert sample_excess_kurtosis([-1e308,1e308]) == pytest.approx(-2)


def test_drawdown_matches_all_ordered_pairs():
    p = np.array([100, 120, 90, 140, 84, 110])
    brute = max(1-p[j]/p[i] for i in range(len(p)) for j in range(i,len(p)))
    assert maximum_drawdown(p) == pytest.approx(brute)
    assert maximum_drawdown(p*17) == pytest.approx(.4)
    assert maximum_drawdown([10,11,12]) == 0
    assert maximum_drawdown([10]) == 0
    assert maximum_drawdown([1e308,1e-308]) == 1
    with pytest.raises(ValueError):
        maximum_drawdown([1,0])


def test_moment_shares_reuse_max_to_sum_contract():
    x = np.array([0., -2, 1, 3, 0, -4])
    for power in (.5,1,2,4):
        np.testing.assert_allclose(moment_share_path(x,power), max_to_sum_path(abs(x)**power),
                                   equal_nan=True)
        np.testing.assert_allclose(moment_share_path(x*1e200,power), moment_share_path(x,power),
                                   equal_nan=True, rtol=1e-12)
    np.testing.assert_allclose(moment_share_path([1e-300,1e300],4), [1,1])
    assert np.all(np.isnan(moment_share_path([0,0])))


@pytest.mark.parametrize("scale", [0.5, 2.0, 1e300])
def test_moment_shares_preserve_equal_weights_at_large_powers(scale):
    # Equal nonzero magnitudes have share 1/n at every positive power.
    np.testing.assert_allclose(moment_share_path([0, scale, -scale, scale], 1e18),
                               [np.nan, 1, .5, 1/3], equal_nan=True, rtol=1e-14)


def test_moment_shares_resolve_close_magnitudes_at_large_powers():
    # 80-digit evaluation of 1/(1 + (1/(1 + 2**-52))**(2**52)).
    expected = 0.7310585786300049
    result = moment_share_path([1, np.nextafter(1.0, 2.0)], 2**52)
    np.testing.assert_allclose(result, [1, expected], rtol=1e-14)
    np.testing.assert_allclose(moment_share_path([1e-300, 1e-300, 1e300, 1e300]),
                               [1, .5, 1, .5], rtol=1e-14)


@pytest.mark.parametrize("p", [0,-1,np.nan,np.inf,True,[2],1j])
def test_invalid_power(p):
    with pytest.raises(ValueError):
        moment_share_path([1,2],p)


def test_record_null_by_exhausting_all_rank_orders():
    rows = [record_counts(order) for order in permutations(range(5))]
    for side in ("upper","lower"):
        counts = np.array([row[side] for row in rows])
        np.testing.assert_allclose(counts.mean(axis=0), rows[0]["iid_mean"])
        np.testing.assert_allclose(counts.var(axis=0), rows[0]["iid_variance"], atol=1e-14)
    tied = record_counts([2,2,1,3,3,0])
    assert tied["upper"].tolist() == [1,1,1,2,2,2]
    assert tied["lower"].tolist() == [1,1,2,2,2,3]
    assert tied["maximum"].tolist() == [2,2,2,3,3,3]


def test_tail_ratio_uses_strict_exceedances():
    result = conditional_tail_ratio([-4,0,2,2,4,8], [2,4,8], min_exceedances=2)
    np.testing.assert_allclose(result["ratio"], [3,np.nan,np.nan], equal_nan=True)
    assert result["exceedances"].tolist() == [2,1,0]
    assert result["mean_excess"][0] == 4
    with pytest.raises(ValueError):
        conditional_tail_ratio([1,2], [0])


def test_aggregation_kappa_and_degenerate_samples():
    rows = aggregation_diagnostics([1,1,-1,-1,0], (1,2))
    assert np.isnan(rows[0]["kappa"])
    assert rows[1]["blocks"] == 2 and rows[1]["dropped"] == 1
    exact = aggregation_diagnostics([1,1,-1,-1], (2,))[0]
    assert exact["kappa"] == pytest.approx(1)
    assert exact["excess_kurtosis"] == pytest.approx(-2)
    assert np.isnan(aggregation_diagnostics([1,-1,1,-1], (2,))[0]["kappa"])
    assert np.isnan(aggregation_diagnostics([0,0,0,0], (2,))[0]["kappa"])
    with pytest.raises(ValueError):
        aggregation_diagnostics([1,2], ())


def test_chronological_check_has_no_test_leakage():
    r = np.array([-.03,-.01,0,.01,.03, 0,-.01,.01,-.02,.02])
    original = chronological_tail_check(r)
    contaminated = chronological_tail_check(np.r_[r[:5], -np.ones(5)])
    for method in ("gaussian","empirical"):
        assert original[method]["threshold"] == contaminated[method]["threshold"]
        assert original[method]["exceedances"] == 0
        assert np.isnan(original[method]["mean_exceedance_loss"])
        assert contaminated[method]["frequency"] == 1
    assert original["empirical"]["threshold"] == .03


@pytest.mark.parametrize("kwargs", [{"train_size":1},{"train_size":4},{"probability":0},
                                    {"probability":1},{"probability":np.nan}])
def test_invalid_holdout_configuration(kwargs):
    with pytest.raises(ValueError):
        chronological_tail_check([0,1,2,3], **kwargs)


def test_hinges_match_piecewise_values_and_slopes():
    # Slopes 1,-2,0.5 with value 3 at knot 0.
    x = np.array([-2,-1,0,1,2,3,4])
    np.testing.assert_allclose(hinge_payoff(x,[0,2],[1,-2,.5],value_at_first=3),
                               [1,2,3,1,-1,-.5,0])
    for point,slope in ((-1,1),(1,-2),(3,.5)):
        derivative = (hinge_payoff(point+.001,[0,2],[1,-2,.5])
                      -hinge_payoff(point-.001,[0,2],[1,-2,.5]))/.002
        assert derivative == pytest.approx(slope)
    assert hinge_payoff(0,[0],[0,1]) == 0
    assert hinge_payoff(2,[0],[0,1]) == 2


def test_hinges_preserve_a_bounded_payoff_in_the_far_tail():
    # (x)_+ - (x-1)_+ is exactly one for x >= 1.
    x = np.array([[-1e18, 0, .5], [1, 1e16, 1e18]])
    np.testing.assert_array_equal(hinge_payoff(x, [0, 1], [0, 1, 0]),
                                  [[0, 0, .5], [1, 1, 1]])
    assert hinge_payoff(1e18, [0, 1], [0, 1, 0], value_at_first=3) == 4


@pytest.mark.parametrize("knots,slopes", [([1,1],[0,1,2]),([2,1],[0,1,2]),([1],[0]),([],[])])
def test_invalid_hinges(knots,slopes):
    with pytest.raises(ValueError):
        hinge_payoff([0,1],knots,slopes)


def synthetic_prices():
    r = .01*np.sin(np.arange(300))+.001
    p = 100*np.exp(np.r_[0,np.cumsum(r)])
    dates = np.datetime64("2020-01-01")+np.arange(len(p))
    return PriceSeries("synthetic", dates, p, "test fixture")


def test_full_pipeline_and_subwindow_boundaries():
    prices = synthetic_prices()
    report = sp500_diagnostics(prices)
    assert report["returns"] == 300
    assert report["max_calendar_gap_days"] == 1
    full = report["windows"]["full"]
    first, second = (report["windows"][k] for k in ("first_half","second_half"))
    assert first["end"] == second["start"]
    assert first["n"]+second["n"] == full["n"]
    assert full["tails"]["loss"]["n"]+full["tails"]["gain"]["n"] == full["n"]
    for tail in full["tails"].values():
        assert len(tail["hill"]) == 3 and len(tail["conditional"]) == 3
        assert all(point["ratio"] >= 1 for point in tail["conditional"])
    assert report["holdout"]["train_size"] == 150
    broken = PriceSeries("synthetic", prices.date[::-1], prices.close, "test")
    with pytest.raises(ValueError):
        sp500_diagnostics(broken)


def test_overflow_is_not_an_infinite_population_claim():
    with pytest.raises(FloatingPointError):
        aggregate_returns([1e308,1e308],2)
    with pytest.raises(FloatingPointError):
        hinge_payoff(1e308,[0],[0,10])
