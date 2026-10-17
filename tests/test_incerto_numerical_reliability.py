import numpy as np
import pytest
from scipy.stats import norm, laplace_asymmetric
from xmath.incerto.distributions import (simple_normal_mixture, pareto_type1,
                                   univariate_variance_gamma)
from xmath.incerto.estimators import max_to_sum_ratio, hill_estimator, hill_stability


def test_mixture_extreme_survival():
    expected = 0.5 * (norm.sf(10 / np.sqrt(1.5)) + norm.sf(10 / np.sqrt(.5)))
    assert simple_normal_mixture.sf(10, .5) == pytest.approx(expected, rel=1e-13, abs=0)
    x = np.array([-100., 0., 10., 100.])
    np.testing.assert_allclose(simple_normal_mixture.logsf(x, 0), norm.logsf(x))
    assert np.isfinite(simple_normal_mixture.logsf(100, .5))


def test_pareto_log_survival_support_and_scale():
    assert pareto_type1.logsf(1e200, 2) == pytest.approx(-400 * np.log(10))
    np.testing.assert_allclose(pareto_type1.logsf([0, 2, 20], 2, scale=2),
                               [0, 0, -2*np.log(10)])


@pytest.mark.parametrize('beta', [-1.9, 0., 1.9])
def test_variance_gamma_asymmetric_laplace(beta):
    alpha = 2.
    delta = alpha**2 - beta**2
    reference = laplace_asymmetric(kappa=np.sqrt((alpha-beta)/(alpha+beta)),
                                   scale=1/np.sqrt(delta))
    x = np.array([-1000., -10., 0., 10., 1000.])
    np.testing.assert_allclose(univariate_variance_gamma.logpdf(x, alpha, beta, 1),
                               reference.logpdf(x), rtol=1e-12, atol=1e-12)
    np.testing.assert_allclose(univariate_variance_gamma.pdf(x, alpha, beta, 1),
                               reference.pdf(x), rtol=1e-12, atol=0)


def test_variance_gamma_origin_and_broadcast():
    assert np.isinf(univariate_variance_gamma.pdf(0, 2, 0, .5))
    assert np.isinf(univariate_variance_gamma.logpdf(0, 2, 0, .25))
    values = univariate_variance_gamma.logpdf([0., 1000.], 2, [0., 1.9], [1., 1.])
    assert np.all(np.isfinite(values))


def test_mixture_sampler_broadcast_and_moments():
    a = np.array([0., .5, .9])
    sample = simple_normal_mixture.rvs(a, size=(100000, 3), random_state=123)
    assert sample.shape == (100000, 3)
    np.testing.assert_allclose(sample.mean(axis=0), 0, atol=.02)
    np.testing.assert_allclose(sample.var(axis=0), 1, atol=.03)
    # The fourth moment distinguishes mixtures that all have unit variance.
    np.testing.assert_allclose(np.mean(sample**4, axis=0), 3*(1+a*a), rtol=.06)
    assert simple_normal_mixture.rvs(a, random_state=123).shape == (3,)


@pytest.mark.parametrize('scale', [1e-300, 1., 1e308])
def test_max_to_sum_scaling_and_axes(scale):
    x = np.array([[1., 1.], [.5, 1.]]) * scale
    np.testing.assert_allclose(max_to_sum_ratio(x, axis=1), [.5, 2/3])
    np.testing.assert_allclose(max_to_sum_ratio(x, axis=0), [2/3, .5])
    assert max_to_sum_ratio(x) == pytest.approx(1/3.5)


def test_hill_scalar_vector_consistency():
    x = np.exp(np.linspace(0, 10, 50))
    ks = [1, 3, 10, 30]
    np.testing.assert_allclose(hill_stability(x, ks)['xi'],
                               [hill_estimator(x, k) for k in ks], rtol=1e-12)
