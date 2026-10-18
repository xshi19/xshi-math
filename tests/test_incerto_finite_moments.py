"""Independent integrals, exact examples and boundaries for chapter 4."""

import numpy as np
import pytest
from scipy.integrate import quad
from scipy.stats import norm, pareto

from xmath.incerto.finite_moments import (
    normal_mixture_absolute_moment,
    normal_mixture_log_abs_survival,
    normal_mixture_log_density,
    pareto_moment_estimator_summary,
    power_mean,
)
from xmath.incerto.stats import (
    dispersion_ratios, normal_peak_shoulder_tail,
    normal_variance_peak_shoulder_tail, t_peak_shoulder_tail,
)


@pytest.mark.parametrize('q', [0.5, 1, 2, 4, 6])
def test_mixture_moment_against_density_quadrature(q):
    v, w = [0.4, 1.6], [0.5, 0.5]
    expected = quad(lambda x: x**q * (norm.pdf(x, scale=np.sqrt(.4))
                                    + norm.pdf(x, scale=np.sqrt(1.6))), 0, np.inf)[0]
    assert normal_mixture_absolute_moment(q, v, w) == pytest.approx(expected, rel=1e-10)


def test_rare_variance_mixture_exact_moments_and_zero_weights():
    assert normal_mixture_absolute_moment(2, [.5, 50.5], [.99, .01]) == pytest.approx(1)
    assert normal_mixture_absolute_moment(4, [.5, 50.5], [.99, .01]) == pytest.approx(77.25)
    assert normal_mixture_absolute_moment(4, [1, 100], [1, 0]) == pytest.approx(3)


def test_log_density_normalization_symmetry_and_tail_integration():
    v, w = [.5, 50.5], [.99, .01]
    f = lambda x: np.exp(normal_mixture_log_density(x, v, w))
    assert quad(f, -np.inf, np.inf)[0] == pytest.approx(1, rel=1e-9)
    np.testing.assert_allclose(normal_mixture_log_density([-3, -1, 0], v, w),
                               normal_mixture_log_density([3, 1, 0], v, w))
    for u in (0, .5, 3, 10):
        assert np.exp(normal_mixture_log_abs_survival(u, v, w)) == pytest.approx(
            2*quad(f, u, np.inf)[0], rel=1e-8)
    assert normal_mixture_log_abs_survival(0, v, w) == 0
    assert np.isfinite(normal_mixture_log_abs_survival(1000, [1], [1]))


@pytest.mark.parametrize('v,w', [([], []), ([0], [1]), ([-1], [1]), ([np.inf], [1]),
                                 ([1, 2], [1]), ([1], [.9]), ([1, 2], [-1, 2])])
def test_invalid_mixtures(v, w):
    with pytest.raises(ValueError):
        normal_mixture_log_density(0, v, w)


@pytest.mark.parametrize('u', [-1, np.nan, np.inf])
def test_invalid_thresholds(u):
    with pytest.raises(ValueError):
        normal_mixture_log_abs_survival(u, [1], [1])


def test_overflow_does_not_impersonate_population_infinity():
    with pytest.raises(FloatingPointError):
        normal_mixture_absolute_moment(1000, [1e300], [1])
    with pytest.raises(FloatingPointError):
        normal_mixture_log_density(1e308, [1], [1])
    with pytest.raises(FloatingPointError):
        pareto_moment_estimator_summary(6, 2, 1, 1e200)


@pytest.mark.parametrize('x', [1.5e154, 1.8e154])
def test_representable_log_density_survives_intermediate_square_overflow(x):
    # At this magnitude the bounded log-normalizing constant is below one ulp.
    expected = -(x/2)*x
    assert normal_mixture_log_density(x, [1], [1]) == pytest.approx(expected, rel=3e-15)


@pytest.mark.parametrize('alpha,q,n', [(6, 2, 20), (3, 1, 7), (2, .5, 1)])
def test_pareto_variance_against_independent_scipy_moments(alpha, q, n):
    row = pareto_moment_estimator_summary(alpha, q, n, x_m=2)
    m = pareto.expect(lambda x: x**q, args=(alpha,), scale=2)
    m2 = pareto.expect(lambda x: x**(2*q), args=(alpha,), scale=2)
    assert row['moment'] == pytest.approx(m)
    assert row['estimator_variance'] == pytest.approx((m2-m*m)/n)


@pytest.mark.parametrize('alpha', [3, 4])
def test_finite_moment_infinite_estimator_variance_including_boundary(alpha):
    row = pareto_moment_estimator_summary(alpha, 2, 100)
    assert np.isfinite(row['moment'])
    assert np.isposinf(row['estimator_variance'])


def test_nonexistent_moment_has_no_variance_about_finite_mean():
    row = pareto_moment_estimator_summary(2, 2, 100)
    assert np.isposinf(row['moment']) and np.isnan(row['estimator_variance'])


def test_subnormal_pareto_parameters_keep_the_strict_variance_gate():
    # X**q has Pareto exponent alpha/q = 5/2, regardless of the tiny exponents.
    tiny = np.nextafter(0., 1.)
    row = pareto_moment_estimator_summary(5*tiny, 2*tiny, 1)
    assert row['moment'] == pytest.approx(5/3, rel=1e-12)
    assert row['estimator_variance'] == pytest.approx(20/9, rel=1e-12)


@pytest.mark.parametrize('n', [0, 1.5, True, 2**53+1])
def test_invalid_sample_sizes(n):
    with pytest.raises(ValueError):
        pareto_moment_estimator_summary(3, 1, n)


@pytest.mark.parametrize('alpha,q,x_m', [(0, 1, 1), (3, 0, 1), (3, 1, -1), (np.inf, 1, 1)])
def test_invalid_pareto_parameters(alpha, q, x_m):
    with pytest.raises(ValueError):
        pareto_moment_estimator_summary(alpha, q, 10, x_m)


def test_normalized_power_mean_examples_and_extreme_scale():
    assert power_mean([0, 0, 0, 4], 1) == 1
    assert power_mean([0, 0, 0, 4], 2) == 2
    assert power_mean([0, 0, 0, 4], 4) == pytest.approx(2*np.sqrt(2))
    assert power_mean([0, 0, 0, 4], np.inf) == 4
    for q in (1, 2, 4, 100, np.inf):
        assert power_mean([-1e300, 1e300], q) == 1e300
        assert power_mean([0, 0], q) == 0


def test_positive_power_mean_underflow_is_reported():
    with pytest.raises(FloatingPointError):
        power_mean([np.nextafter(0., 1.), 0, 0], 1)


@pytest.mark.parametrize('x,q', [([], 2), ([np.nan], 2), ([[1]], 2), ([1], .5), ([1], np.nan)])
def test_invalid_power_mean(x, q):
    with pytest.raises(ValueError):
        power_mean(x, q)


@pytest.mark.parametrize('sample', [[0], [2, 2, 2], [1e300]*10])
def test_constant_dispersion_ratios_are_both_undefined(sample):
    with np.errstate(all='raise'):
        assert all(np.isnan(r) for r in dispersion_ratios(sample))


def test_nonconstant_tied_dispersion_is_positive_over_zero():
    mean_ratio, median_ratio = dispersion_ratios([0, 0, 0, 4])
    assert mean_ratio == pytest.approx(np.sqrt(3)/(1.5*np.sqrt(np.pi/2)))
    assert np.isposinf(median_ratio)


def test_dispersion_regular_case_and_scale_invariance():
    x = np.array([-2., -1., 0., 1., 2.])
    expected = (np.sqrt(2)/(1.2*np.sqrt(np.pi/2)), np.sqrt(2)*norm.ppf(.75))
    np.testing.assert_allclose(dispersion_ratios(x), expected)
    np.testing.assert_allclose(dispersion_ratios(x*1e300), expected)


@pytest.mark.parametrize('sample', [
    [1e300, np.nextafter(1e300, np.inf)],
    [-1e300, np.nextafter(-1e300, 0)],
    [-1e308, 1e308],
])
def test_two_point_dispersion_is_independent_of_offset_and_spacing(sample):
    # Any two distinct observations have Std = raw MeanAD = raw MedianAD.
    np.testing.assert_allclose(dispersion_ratios(sample),
                               [np.sqrt(2/np.pi), norm.ppf(.75)], rtol=3e-15)


@pytest.mark.parametrize('sign', [-1, 1])
def test_dispersion_retains_small_central_spacings_beside_a_large_outlier(sign):
    # The raw median deviation is 1; the outlier dominates Std and MeanAD.
    sample = sign*np.array([1e308, 0., 1., 2.])
    expected = [2/np.sqrt(3)*np.sqrt(2/np.pi),
                (np.sqrt(3)/4)*1e308*norm.ppf(.75)]
    np.testing.assert_allclose(dispersion_ratios(sample), expected, rtol=3e-15)


@pytest.mark.parametrize('spacing', [1e-10, np.nextafter(0., 1.)])
def test_unrepresentable_finite_dispersion_does_not_impersonate_zero_median_deviation(spacing):
    with pytest.raises(FloatingPointError):
        dispersion_ratios([1e308, 0., spacing, 2*spacing])


@pytest.mark.parametrize('sample', [[], [1, np.inf], [[1, 2]]])
def test_invalid_dispersion_samples(sample):
    with pytest.raises(ValueError):
        dispersion_ratios(sample)


def test_curvature_roots_against_numerical_differentiation():
    from scipy.stats import t
    h = 1e-4
    for roots, density in [
        (normal_peak_shoulder_tail(), lambda x, s: norm.pdf(x, scale=s)),
        (normal_variance_peak_shoulder_tail(), lambda x, v: norm.pdf(x, scale=np.sqrt(v))),
        (t_peak_shoulder_tail(3), lambda x, s: t.pdf(x, 3, scale=s)),
    ]:
        for x in roots:
            d2 = (density(x, 1+h)-2*density(x, 1)+density(x, 1-h))/h**2
            assert abs(d2) < 2e-8


def test_student_curvature_near_cauchy_and_gaussian_limits():
    df = np.nextafter(1., 2.)
    roots = t_peak_shoulder_tail(df)
    # At df=1 the remaining numerator is 2-6*z**2; the outer pair escapes.
    assert roots[2] == pytest.approx(1/np.sqrt(3), rel=3e-15)
    assert roots[3] == pytest.approx(np.sqrt(6/(df-1)), rel=3e-15)
    np.testing.assert_allclose(t_peak_shoulder_tail(1e308),
                               normal_peak_shoulder_tail(), rtol=3e-15)
