"""Independent integrals, finite algebra and edge cases for chapter 6."""

import numpy as np
import pytest
from numpy.testing import assert_allclose
from scipy.integrate import quad
from scipy.stats import t, multivariate_t, norm

from xmath.incerto.multivariate import (
    student_entropy, student_mutual_information, bivariate_student,
    sample_correlation, symmetric_spectrum, regression_population_r2,
    normal_location_mixture_kurtosis,
)


@pytest.mark.parametrize("nu", [0.5, 1, 1.5, 3, 10])
def test_entropy_independent_integrals(nu):
    h1, err = quad(lambda x: -2*t.pdf(x, nu)*t.logpdf(x, nu), 0, np.inf,
                   epsabs=2e-9, limit=250)
    assert err < 2e-8
    assert_allclose(student_entropy(nu, 1), h1, atol=2e-8)
    # Independent polar quadrature of SciPy's normalized joint density.
    rv = multivariate_t(df=nu, shape=np.eye(2))
    h2, err = quad(lambda r: -2*np.pi*r*np.exp(rv.logpdf([r, 0]))*rv.logpdf([r, 0]),
                   0, np.inf, epsabs=2e-9, limit=250)
    assert err < 2e-8
    assert_allclose(student_entropy(nu, 2), h2, atol=2e-8)


def test_information_exact_cauchy_and_scale():
    assert_allclose(student_mutual_information(1), np.log(8*np.pi)-3, atol=2e-15)
    assert_allclose(student_entropy(3, 1, np.log(9))-student_entropy(3, 1), np.log(3))
    for nu in [.5, 1, 3, 10, 1000]:
        assert student_mutual_information(nu) > 0
        assert_allclose(student_mutual_information(nu, .6)-student_mutual_information(nu),
                        -np.log(.8), atol=1e-14)
    assert student_mutual_information(1000) < 1e-6


@pytest.mark.parametrize("nu", [0, .49, 1001, np.inf, np.nan])
def test_student_domain(nu):
    with pytest.raises(ValueError):
        student_entropy(nu, 2)


@pytest.mark.parametrize("rho", [-1, 1, np.nan, np.inf])
def test_scatter_domain(rho):
    with pytest.raises(ValueError):
        student_mutual_information(3, rho)


@pytest.mark.parametrize("dimension,logdet", [(0, 0), (3, 0), (True, 0), (1.0, 0), (1, np.nan)])
def test_entropy_dimensions(dimension, logdet):
    with pytest.raises(ValueError):
        student_entropy(3, dimension, logdet)


def test_sampler_reproducible_and_marginal_probabilities():
    sample = bivariate_student(np.random.default_rng(42), 3, .6, 50000)
    assert_allclose(sample, bivariate_student(np.random.default_rng(42), 3, .6, 50000))
    # Bounded indicators have standard error <= 1/(2 sqrt(n)), even with fat tails.
    se_bound = .5/np.sqrt(len(sample))
    for coordinate in sample.T:
        assert abs(np.mean(coordinate <= 1)-t.cdf(1, 3)) < 6*se_bound
    projection = (sample[:, 0]+sample[:, 1])/np.sqrt(3.2)
    assert abs(np.mean(projection <= 1)-t.cdf(1, 3)) < 6*se_bound


@pytest.mark.parametrize("size", [0, -1, 2.5, True])
def test_sampler_size(size):
    with pytest.raises(ValueError):
        bivariate_student(np.random.default_rng(1), 3, 0, size)


def test_correlations_centering_rescaling_and_degenerate():
    x, y = np.array([1., 2, 5, -1]), np.array([4., 0, 2, 3])
    expected = np.corrcoef(x, y)[0, 1]
    assert_allclose(sample_correlation(x, y), expected)
    assert_allclose(sample_correlation(x, y, centered=False), x@y/(np.linalg.norm(x)*np.linalg.norm(y)))
    assert_allclose(sample_correlation(x*1e300, y*1e-300), expected)
    assert_allclose(sample_correlation(np.stack([x, x]), np.stack([y, -y])), [expected, -expected])
    assert np.isnan(sample_correlation([2, 2], [1, 2]))
    assert np.isnan(sample_correlation([0, 0], [1, 2], centered=False))
    assert sample_correlation([1, 1], [2, 2], centered=False) == pytest.approx(1)


@pytest.mark.parametrize("x,y", [([], []), ([1], [2]), ([1, 2], [1, 2, 3]),
                                 ([1, np.inf], [2, 3]), ([1, np.nan], [2, 3])])
def test_correlation_invalid(x, y):
    with pytest.raises(ValueError):
        sample_correlation(x, y)


def test_fixed_sample_contamination_and_ols_identity():
    x, y = np.array([1., -2, 4, 7, 1e8]), np.array([3., 1, -3, 2, -2e8])
    assert sample_correlation(x, y) == pytest.approx(-1, abs=1e-12)
    assert sample_correlation(x, y, centered=False) == pytest.approx(-1, abs=1e-12)
    x, y = np.array([-2., -1, 0, 1, 2]), np.array([-1., 2, 1, 3, 0])
    design = np.column_stack([np.ones(len(x)), x])
    residual = y-design@np.linalg.lstsq(design, y, rcond=None)[0]
    r2 = 1-residual@residual/np.sum((y-y.mean())**2)
    assert_allclose(sample_correlation(x, y)**2, r2, atol=1e-15)


def test_spectrum_identities_and_extreme_scales():
    matrix = np.array([[1., 2, 0], [2, -1, 3], [0, 3, 4]])
    spectrum = symmetric_spectrum(matrix)
    assert_allclose(spectrum.sum(), np.trace(matrix))
    assert_allclose(np.sum(spectrum**2), np.sum(matrix**2))
    assert np.max(np.abs(spectrum)) >= np.max(np.abs(matrix))
    assert_allclose(symmetric_spectrum(matrix*1e200)/1e200, spectrum)
    assert_allclose(symmetric_spectrum([[0, 0], [0, 0]]), [0, 0])
    assert_allclose(symmetric_spectrum([[0, 7], [7, 0]]), [-7, 7])
    with pytest.raises(FloatingPointError):
        symmetric_spectrum(np.full((2, 2), 1.7e308))


@pytest.mark.parametrize("matrix", [[], [[1, 2]], [[1, 2], [3, 4]],
                                   [[np.inf]], [[1j]]])
def test_spectrum_domain(matrix):
    with pytest.raises(ValueError):
        symmetric_spectrum(matrix)


def test_population_r2_and_limit_distinction():
    assert regression_population_r2(1, 3) == pytest.approx(.25)
    assert regression_population_r2(-2, 4) == pytest.approx(.5)
    assert regression_population_r2(0, 3) == 0
    assert regression_population_r2(1e200, 1e300) == pytest.approx(1)
    assert regression_population_r2(1e-200, 1e-300) == pytest.approx(1e-100, rel=1e-12, abs=0)
    for variance in [0, -1, np.inf, np.nan]:
        with pytest.raises(ValueError):
            regression_population_r2(1, variance)


@pytest.mark.parametrize("m,sigma", [(0, 1), (2, 1), (1, 2), (5, .5)])
def test_location_mixture_by_integrating_density(m, sigma):
    def density(x):
        return (norm.pdf(x, m, sigma)+norm.pdf(x, -m, sigma))/2
    m2 = quad(lambda x: x*x*density(x), -np.inf, np.inf)[0]
    m4 = quad(lambda x: x**4*density(x), -np.inf, np.inf)[0]
    assert_allclose(normal_location_mixture_kurtosis(m, sigma), m4/m2**2, rtol=1e-10)
    assert_allclose(normal_location_mixture_kurtosis(m*1e200, sigma*1e200), m4/m2**2)


@pytest.mark.parametrize("m,sigma", [(-1, 1), (1, 0), (1, -1), (np.inf, 1), (1, np.nan)])
def test_location_mixture_domain(m, sigma):
    with pytest.raises(ValueError):
        normal_location_mixture_kurtosis(m, sigma)


def test_correlation_large_offset_retains_represented_differences():
    baseline = 1e300
    step = np.spacing(baseline)
    x = baseline+step*np.arange(5)
    y = np.array([0., 1, -1, 2, 1])
    expected = np.corrcoef(np.arange(5), y)[0, 1]
    assert_allclose(sample_correlation(x, y), expected, atol=2e-15)
    assert_allclose(sample_correlation(-x, y), -expected, atol=2e-15)
    with pytest.raises(ValueError):
        sample_correlation([1j, 2j], [1, 2])


@pytest.mark.parametrize("nu", [1, 3])
def test_joint_exceedance_two_conditioning_routes(nu):
    from scipy.stats import gamma
    u = 1.25
    precision_value = quad(lambda g: (2*norm.sf(u*np.sqrt(g)))**2
                          * gamma.pdf(g, nu/2, scale=2/nu), 0, np.inf,
                          epsabs=1e-9, limit=200)[0]
    coordinate_value = quad(lambda x: 4*t.pdf(x, nu)
                           * t.sf(u/np.sqrt((nu+x*x)/(nu+1)), nu+1),
                           u, np.inf, epsabs=1e-9, limit=200)[0]
    assert_allclose(precision_value, coordinate_value, atol=2e-9)
    assert precision_value > (2*t.sf(u, nu))**2


@pytest.mark.parametrize("function,args", [
    (student_entropy, (np.complex128(3+2j), 2)),
    (student_entropy, (3, 2, np.complex128(1+2j))),
    (student_mutual_information, (3, np.complex128(.6+.2j))),
    (bivariate_student, (np.random.default_rng(1), np.complex128(3+2j), 0, 2)),
    (bivariate_student, (np.random.default_rng(1), 3, np.complex128(.6+.2j), 2)),
    (regression_population_r2, (np.complex128(1+2j), 3)),
    (regression_population_r2, (1, np.complex128(3+2j))),
    (normal_location_mixture_kurtosis, (np.array([2+3j]), 1)),
    (normal_location_mixture_kurtosis, (2, np.array([1+3j]))),
])
def test_complex_parameters_are_rejected_before_real_conversion(function, args):
    # NumPy complex scalars/arrays can otherwise cast with only a warning,
    # returning a plausible result for a different, real-valued model.
    with pytest.raises(ValueError, match="real"):
        function(*args)
