"""Independent identities, boundaries and sampling checks for chapter 12."""

from decimal import Decimal, localcontext

import numpy as np
import pytest
from scipy.integrate import quad
from scipy.stats import pareto

from xmath.incerto.forecasting import (
    bounded_to_dual, dual_to_bounded, pareto_forecast_scores,
    quantile_loss, stable_average_scale,
)


@pytest.mark.parametrize("alpha", [.5, .8, 1., 1.5, 2.])
def test_stable_average_characteristic_function(alpha):
    n, sigma = 17, 1.7
    t = np.array([.1, .5, 1.])
    average_cf = np.exp(-abs(sigma*t/n)**alpha)**n
    s = stable_average_scale(alpha, n, scale=sigma)
    np.testing.assert_allclose(np.exp(-abs(s*t)**alpha), average_cf, rtol=2e-14)
    assert stable_average_scale(alpha, 1, scale=sigma) == sigma
    if alpha == 2:
        assert s == pytest.approx(sigma/np.sqrt(n))


@pytest.mark.parametrize("alpha,n", [(0, 2), (2.1, 2), (np.nan, 2), (1.5, True),
                                        (1.5, 0), (1.5, 2.0), (True, 3)])
def test_scale_validation(alpha, n):
    with pytest.raises(ValueError):
        stable_average_scale(alpha, n)


def test_scale_extremes():
    assert stable_average_scale(1e-320, 1, scale=1e-300) == 1e-300
    assert stable_average_scale(1, 2**53, scale=1e300) == 1e300
    with pytest.raises(FloatingPointError):
        stable_average_scale(.01, 100000, scale=1e100)
    with pytest.raises(FloatingPointError):
        stable_average_scale(2, 2**53, scale=np.nextafter(0., 1.))


def test_quantile_asymmetry_and_broadcast():
    np.testing.assert_allclose(quantile_loss([1, 3, 20], 3, tau=.9), [.2, 0, 15.3])
    x = np.array([[1.], [3.]])
    np.testing.assert_allclose(quantile_loss(x, [1., 2.]), .5*abs(x-[1., 2.]))


@pytest.mark.parametrize("alpha", [.8, 1.5, 3.])
def test_paired_quantile_integral_even_without_mean(alpha):
    # Integrate a bounded difference against the density, independently of
    # the expected-risk formula; both individual risks diverge at alpha=.8.
    tau, d1, d2 = .8, 2., 7.
    def difference(x):
        return float(quantile_loss(x, d2, tau=tau)-quantile_loss(x, d1, tau=tau))
    actual = sum(quad(lambda x: difference(x)*pareto.pdf(x, alpha), lo, hi,
                      epsabs=1e-10)[0] for lo, hi in ((1, d1), (d1, d2), (d2, np.inf)))
    expected = quad(lambda t: pareto.cdf(t, alpha)-tau, d1, d2)[0]
    assert actual == pytest.approx(expected, abs=2e-10)
    grid = np.geomspace(1, 1e10, 100)
    assert np.max(abs(quantile_loss(grid, d2, tau=tau)
                      - quantile_loss(grid, d1, tau=tau))) <= d2-d1


def test_quantile_large_finite_and_overflow():
    assert quantile_loss(1e308, -1e308) == pytest.approx(1e308)
    with pytest.raises(OverflowError):
        quantile_loss(1.7e308, -1.7e308, tau=.9)


def test_quantile_opposite_subnormals_preserve_representable_loss():
    tiny = np.nextafter(0., 1.)
    # Half the exact distance 2*tiny is representable; halving each input
    # first rounds both to zero.
    np.testing.assert_array_equal(quantile_loss([tiny, -tiny], [-tiny, tiny]),
                                  [tiny, tiny])


@pytest.mark.parametrize("tau", [0, 1, -.1, np.inf, np.nan, True, 1j])
def test_quantile_validation(tau):
    with pytest.raises(ValueError):
        quantile_loss([1, 2], 1, tau=tau)


@pytest.mark.parametrize("value", [np.nan, np.inf, 1j])
def test_quantile_invalid_values(value):
    with pytest.raises(ValueError):
        quantile_loss([value], 1)


@pytest.mark.parametrize("h", [1e-200, 1., 1e200])
def test_dual_high_precision_and_quantile_transport(h):
    x = h*np.array([0, 1e-12, .1, .5, .99, 1-1e-12])
    z = bounded_to_dual(x, upper=h)
    with localcontext() as ctx:
        ctx.prec = 80
        hd = Decimal.from_float(h)
        expected = [float(-hd*(1-Decimal.from_float(float(v))/hd).ln()) for v in x]
    np.testing.assert_allclose(z, expected, rtol=8e-14, atol=0)
    np.testing.assert_allclose(dual_to_bounded(z, upper=h), x, rtol=8e-14, atol=0)
    assert np.all(np.diff(z) > 0)
    # Uniform physical X has P(Z>z)=exp(-z/H); check quantile transport.
    p = np.array([.1, .5, .9])
    np.testing.assert_allclose(bounded_to_dual(h*p, upper=h)/h, -np.log(1-p))


def test_dual_endpoints_and_lost_resolution():
    assert bounded_to_dual(0, upper=100) == 0
    assert bounded_to_dual(100, upper=100) == np.inf
    assert dual_to_bounded(np.inf, upper=100) == 100
    assert dual_to_bounded(1e300, upper=100) == 100
    # An interior value must not become infinity just because of division rounding.
    h = 1e300
    assert np.isfinite(bounded_to_dual(np.nextafter(h, 0), upper=h))
    tiny = np.nextafter(0., 1.)
    assert bounded_to_dual(tiny, upper=1e300) == tiny
    assert dual_to_bounded(tiny, upper=1e300) == tiny
    with pytest.raises(FloatingPointError):
        bounded_to_dual(np.nextafter(1e308, 0), upper=1e308)


@pytest.mark.parametrize("transform", [bounded_to_dual, dual_to_bounded])
def test_dual_subnormal_ratio_preserves_normal_coordinate(transform):
    # The correction to the identity is far below one ulp, while dividing
    # first rounds these nonzero ratios to very few subnormal bits.
    values = np.array([3e-16, 4e-16, 6e-16, 1e-15])
    np.testing.assert_array_equal(transform(values, upper=1e308), values)


@pytest.mark.parametrize("value", [-1, 101, np.nan, np.inf, -np.inf, 1j])
def test_forward_invalid(value):
    with pytest.raises(ValueError):
        bounded_to_dual(value, upper=100)


@pytest.mark.parametrize("value", [-1, np.nan, -np.inf, 1j])
def test_inverse_invalid(value):
    with pytest.raises(ValueError):
        dual_to_bounded(value, upper=100)


@pytest.mark.parametrize("upper", [0, -1, np.inf, np.nan, True])
def test_transform_bound_validation(upper):
    for transform in (bounded_to_dual, dual_to_bounded):
        with pytest.raises(ValueError):
            transform(0, upper=upper)


def test_pareto_score_population_checks():
    # Forecast 0: absolute loss equals X, squared loss equals X**2,
    # sMAPE is exactly 2. Alpha 6 gives finite variance for every tested score.
    n, reps, alpha = 100, 2000, 6.
    result = pareto_forecast_scores(alpha, n, 0, repetitions=reps, seed=12001)
    np.testing.assert_array_equal(result["absolute"], result["mean"])
    np.testing.assert_array_equal(result["smape"], np.full(reps, 2.))
    for key, order in (("mean", 1), ("squared", 2)):
        moment = alpha/(alpha-order)
        variance = alpha/(alpha-2*order)-moment**2
        assert abs(result[key].mean()-moment) < 6*np.sqrt(variance/(n*reps))
    again = pareto_forecast_scores(alpha, n, 0, repetitions=reps, seed=12001)
    for key in result:
        np.testing.assert_array_equal(result[key], again[key])


def test_pareto_scores_scaling_and_batch_remainder():
    a = pareto_forecast_scores(1.5, 20, 2, repetitions=35, seed=12002)
    b = pareto_forecast_scores(1.5, 20, 6, xm=3, repetitions=35, seed=12002)
    for key, factor in (("mean", 3), ("absolute", 3), ("squared", 9), ("smape", 1)):
        assert a[key].shape == (35,)
        np.testing.assert_allclose(b[key], factor*a[key], rtol=2e-14)


@pytest.mark.parametrize("kwargs", [{"alpha": 0}, {"n": 0}, {"n": True},
    {"n": 1000001}, {"n": 1000000, "repetitions": 51}, {"repetitions": 0},
    {"xm": -1}, {"forecast": np.nan}])
def test_pareto_experiment_validation(kwargs):
    args = dict(alpha=1.5, n=10, forecast=2)
    args.update(kwargs)
    with pytest.raises(ValueError):
        pareto_forecast_scores(**args)


def test_pareto_experiment_does_not_filter_overflow():
    with pytest.raises((FloatingPointError, OverflowError)):
        pareto_forecast_scores(.001, 100, 1, repetitions=2, seed=12)
