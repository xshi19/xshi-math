"""Analytic identities, fit boundaries, and diagnostics for gas-speed helpers."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pytest
from scipy import integrate, stats

from xmath.incerto.figures import savefig
from xmath.incerto.gas_speeds import (
    chi_speed,
    fit_speed_models,
    sample_chi_speed,
    speed_fit_figure,
    speed_fit_table,
    speed_qq,
    squared_speed_ks,
)


@pytest.mark.parametrize("dimension", [1, 2, 3, 7])
def test_chi_density_mass_second_moment_and_energy(dimension):
    variance = 2.5
    law = chi_speed(dimension, variance)
    mass = integrate.quad(law.pdf, 0, np.inf)[0]
    second = integrate.quad(lambda v: v*v*law.pdf(v), 0, np.inf)[0]
    assert mass == pytest.approx(1)
    assert second == pytest.approx(dimension * variance)
    q = np.array([0.1, 1, 3, 10])
    np.testing.assert_allclose(law.cdf(np.sqrt(q)),
                               stats.gamma(dimension/2, scale=2*variance).cdf(q))
    assert law.pdf(-1) == law.cdf(-1) == 0


def test_rayleigh_and_maxwell_formulas_and_flux_weighting():
    v = np.array([0, 0.2, 1, 3])
    rayleigh, maxwell = chi_speed(2), chi_speed(3)
    np.testing.assert_allclose(rayleigh.pdf(v), v*np.exp(-v*v/2))
    np.testing.assert_allclose(maxwell.pdf(v), np.sqrt(2/np.pi)*v*v*np.exp(-v*v/2))
    np.testing.assert_allclose(v*rayleigh.pdf(v)/rayleigh.mean(), maxwell.pdf(v))
    assert rayleigh.mean() == pytest.approx(np.sqrt(np.pi/2))
    assert rayleigh.var() == pytest.approx((4-np.pi)/2)
    assert maxwell.var() == pytest.approx(3-8/np.pi)


@pytest.mark.parametrize("dimension", [0, -1, 2.5, True, np.nan])
def test_invalid_dimension(dimension):
    with pytest.raises(ValueError):
        chi_speed(dimension)
    with pytest.raises(ValueError):
        sample_chi_speed(10, dimension=dimension)


@pytest.mark.parametrize("variance", [0, -1, np.inf, np.nan, 1j, [1]])
def test_invalid_thermal_variance(variance):
    with pytest.raises(ValueError):
        chi_speed(2, variance)
    with pytest.raises(ValueError):
        sample_chi_speed(10, thermal_variance=variance)
    with pytest.raises(ValueError):
        squared_speed_ks([1, 2], variance)


@pytest.mark.parametrize("size", [0, -1, 1.5, True])
def test_invalid_sample_size(size):
    with pytest.raises(ValueError):
        sample_chi_speed(size)


def test_sampling_order_seed_scale_and_generator_consumption():
    seed, size = 20261022, 100
    components = np.random.default_rng(seed).normal(0, 1, (2, size))
    expected = np.hypot(*components)
    np.testing.assert_array_equal(sample_chi_speed(size, random_state=seed), expected)
    np.testing.assert_allclose(sample_chi_speed(size, thermal_variance=4, random_state=seed),
                               2*expected)
    rng = np.random.default_rng(seed)
    np.testing.assert_array_equal(sample_chi_speed(size, random_state=rng), expected)
    assert not np.array_equal(sample_chi_speed(size, random_state=rng), expected)


@pytest.fixture(scope="module")
def experiment():
    sample = sample_chi_speed(50_000, random_state=20261022)
    return sample, fit_speed_models(sample)


def test_fits_likelihood_counts_boundary_and_ranking(experiment):
    sample, fits = experiment
    by_name = {fit.name: fit for fit in fits}
    assert [fit.name for fit in fits] == ["Rayleigh", "Weibull", "Gamma", "GIG",
                                        "Gaussian", "inverse Gaussian", "inverse Gamma"]
    for fit in fits:
        assert fit.log_likelihood == pytest.approx(np.sum(fit.law.logpdf(sample)))
        assert fit.aic == pytest.approx(2*fit.parameters - 2*fit.log_likelihood)
    rayleigh = by_name["Rayleigh"]
    assert rayleigh.law.kwds["scale"]**2 == pytest.approx(np.mean(sample**2)/2)
    assert rayleigh.aic == pytest.approx(93781.3, abs=0.05)
    assert rayleigh.ks_pvalue == pytest.approx(0.618, abs=0.0005)
    gig, gamma = by_name["GIG"], by_name["Gamma"]
    assert gig.boundary == "Gamma"
    assert gig.aic == pytest.approx(gamma.aic+2)
    assert gig.ks_pvalue == gamma.ks_pvalue
    shape, scale = gamma.law.args[0], gamma.law.kwds["scale"]
    assert 1/((shape-1)*scale) < np.mean(1/sample)
    # A nearby interior GIG approaches the boundary likelihood from below.
    a = 2/scale
    for b in (0.01, 0.001):
        interior = stats.geninvgauss(shape, np.sqrt(a*b), scale=np.sqrt(b/a))
        assert np.sum(interior.logpdf(sample)) < gamma.log_likelihood
    table = speed_fit_table(reversed(fits))
    assert "93781.3" in table and "5.43e-47" in table
    assert "np.float" not in table


def test_inverse_gamma_boundary_is_recognized():
    # Reciprocating a Rayleigh sample swaps the two GIG boundaries.
    sample = 1/sample_chi_speed(600, random_state=17)
    fits = {fit.name: fit for fit in fit_speed_models(sample)}
    assert fits["GIG"].boundary == "inverse Gamma"
    assert fits["GIG"].log_likelihood == fits["inverse Gamma"].log_likelihood


def test_interior_gig_fit_beats_boundaries():
    sample = stats.geninvgauss(0.5, 1.5).ppf((np.arange(120)+0.5)/120)
    fits = {fit.name: fit for fit in fit_speed_models(sample)}
    gig = fits["GIG"]
    assert gig.boundary == ""
    assert gig.log_likelihood > fits["Gamma"].log_likelihood
    assert gig.log_likelihood > fits["inverse Gamma"].log_likelihood


@pytest.mark.parametrize("sample", [[], [1, 2], [1, 1, 1], [0, 1, 2], [-1, 1, 2],
                                   [1, np.inf, 3], [1, np.nan, 3], [[1, 2, 3]], [1, 2, 3j]])
def test_invalid_fit_samples(sample):
    with pytest.raises(ValueError):
        fit_speed_models(sample)


def test_qq_orientation_and_interpolation():
    theoretical, empirical = speed_qq([1, 2, 4, 8], chi_speed(), [0.25, 0.5, 0.75])
    np.testing.assert_allclose(theoretical, np.sqrt(-2*np.log([0.75, 0.5, 0.25])))
    np.testing.assert_allclose(empirical, [1.75, 3, 5])


@pytest.mark.parametrize("probabilities", [[], [0], [1], [0.5, 0.4], [0.5, 0.5],
                                          [np.nan], [[0.5]], [0.5j]])
def test_invalid_qq_probabilities(probabilities):
    with pytest.raises(ValueError):
        speed_qq([1, 2], chi_speed(), probabilities)


def test_squared_speed_ks_is_fixed_null_and_scale_invariant(experiment):
    sample, _ = experiment
    result = squared_speed_ks(sample)
    reference = stats.kstest(sample**2, stats.expon(scale=2).cdf, method="exact")
    assert result == {"statistic": reference.statistic, "pvalue": reference.pvalue}
    assert result["pvalue"] == pytest.approx(0.0696174, abs=1e-7)
    scaled = squared_speed_ks(3*sample, thermal_variance=9)
    assert scaled == pytest.approx(result)
    with pytest.raises(FloatingPointError):
        squared_speed_ks([1e308])


@pytest.mark.parametrize(("kind", "panels"), [("density", 2), ("qq", 5)])
def test_figures_are_single_column_finite_and_reproducible(experiment, tmp_path, kind, panels):
    sample, fits = experiment
    fig = speed_fit_figure(sample, fits, kind=kind)
    try:
        assert len(fig.axes) == panels
        assert fig.get_figwidth() == 5
        assert matplotlib.rcParams["font.serif"] == ["DejaVu Serif"]
        for ax in fig.axes:
            for line in ax.lines:
                assert np.all(np.isfinite(line.get_xdata()))
                assert np.all(np.isfinite(line.get_ydata()))
        first = savefig(fig, tmp_path / "first.svg").read_bytes()
    finally:
        plt.close(fig)
    regenerated = speed_fit_figure(sample, fits, kind=kind)
    try:
        assert first == savefig(regenerated, tmp_path / "second.svg").read_bytes()
    finally:
        plt.close(regenerated)
