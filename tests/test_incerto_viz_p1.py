"""P1 distribution conventions, diagnostic edge cases and reproducible exports."""

from pathlib import Path
import os
import runpy
import subprocess
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from numpy.testing import assert_allclose
import pytest
from scipy.integrate import quad

from xmath.incerto.distributions import frechet, generalized_extreme_value, generalized_pareto, pareto_type1
from xmath.incerto.estimators import gpd_threshold_fit, max_to_sum_path, max_to_sum_ratio, mean_excess
from xmath.incerto.figures import distribution_card, vertical_figure

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("xi", [-.4, 0, .4])
def test_gpd_formulas_support_and_density_mass(xi):
    beta = 2
    law = generalized_pareto(xi, beta)
    y = np.array([0., .2, 1, 4])
    survival = np.exp(-y/beta) if xi == 0 else (1+xi*y/beta)**(-1/xi)
    density = survival/beta if xi == 0 else survival/(beta+xi*y)
    assert_allclose(law.sf(y), survival)
    assert_allclose(law.cdf(y), 1-survival, atol=1e-16)
    assert_allclose(law.pdf(y), density)
    assert_allclose([law.pdf(-1), law.cdf(-1), law.sf(-1)], [0, 0, 1])
    if xi < 0:
        endpoint = -beta/xi
        assert law.support() == (0, endpoint)
        assert_allclose(law.cdf([endpoint, endpoint+1]), 1)
        assert_allclose(law.sf([endpoint, endpoint+1]), 0)
        assert_allclose(law.pdf([endpoint, endpoint+1]), 0)
        assert law.sf(np.nextafter(endpoint, 0)) > 0
    else:
        assert law.support() == (0, np.inf)
    mass, _ = quad(law.pdf, *law.support())
    assert mass == pytest.approx(1, abs=1e-8)


@pytest.mark.parametrize("xi,endpoint_pdf", [(-2., np.inf), (-1., .5), (-.5, 0.)])
def test_gpd_finite_endpoint_density_regimes(xi, endpoint_pdf):
    beta = 2.
    law = generalized_pareto(xi, beta)
    endpoint = -beta/xi
    y = endpoint - np.array([1e-3, 1e-6])
    base = -xi*(endpoint-y)/beta
    survival = base**(-1/xi)
    assert_allclose(law.sf(y), survival, rtol=1e-9)
    assert_allclose(law.cdf(y), 1-survival)
    assert_allclose(law.pdf(y), survival/(beta*base), rtol=1e-9)
    assert law.pdf(endpoint) == endpoint_pdf
    assert_allclose(law.pdf([endpoint+1]), 0)
    assert_allclose(law.cdf([endpoint, endpoint+1]), 1)
    assert_allclose(law.sf([endpoint, endpoint+1]), 0)


@pytest.mark.parametrize("xi", [-.3, 0, .3])
def test_gev_uses_page_shape_sign_location_scale_and_endpoints(xi):
    mu, sigma = 2, 3
    law = generalized_extreme_value(xi, mu, sigma)
    x = np.array([-1., 2, 5])
    z = (x-mu)/sigma
    t = np.exp(-z) if xi == 0 else (1+xi*z)**(-1/xi)
    cdf = np.exp(-t)
    pdf = cdf*t/sigma if xi == 0 else cdf*t/(sigma*(1+xi*z))
    assert_allclose(law.cdf(x), cdf)
    assert_allclose(law.sf(x), -np.expm1(-t))
    assert_allclose(law.pdf(x), pdf)
    assert law.cdf(mu) == pytest.approx(np.exp(-1))
    if xi != 0:
        endpoint = mu-sigma/xi
        assert law.support() == ((endpoint, np.inf) if xi > 0 else (-np.inf, endpoint))
        outside = endpoint + (-1 if xi > 0 else 1)
        assert law.cdf(outside) == (0 if xi > 0 else 1)
        assert law.sf(outside) == (1 if xi > 0 else 0)
        assert law.pdf(outside) == 0
        assert law.cdf(endpoint) == (0 if xi > 0 else 1)
        assert law.sf(endpoint) == (1 if xi > 0 else 0)
    else:
        assert law.support() == (-np.inf, np.inf)
    # Gumbel's far-left exp(-exp(-z)) evaluates to zero when the inner
    # exponential overflows; this is harmless in this normalization integral.
    with np.errstate(over="ignore"):
        mass, _ = quad(law.pdf, *law.support())
    assert mass == pytest.approx(1, abs=1e-8)


@pytest.mark.parametrize("xi,endpoint_pdf", [(-2., 0.), (-1., .25), (-.5, 0.)])
def test_gev_right_endpoint_limit_and_scipy_point_convention(xi, endpoint_pdf):
    mu, sigma = 2., 4.
    law = generalized_extreme_value(xi, mu, sigma)
    endpoint = mu-sigma/xi
    x = endpoint - np.array([1e-3, 1e-6])
    base = -xi*(endpoint-x)/sigma
    t = base**(-1/xi)
    assert_allclose(law.cdf(x), np.exp(-t))
    assert_allclose(law.sf(x), -np.expm1(-t), rtol=1e-9)
    assert_allclose(law.pdf(x), np.exp(-t)*t/(sigma*base), rtol=1e-9)
    if xi < -1:
        assert law.pdf(x[1]) > law.pdf(x[0])  # diverges on approach
    # SciPy assigns zero at the singular endpoint; a density is defined a.e.
    assert law.pdf(endpoint) == endpoint_pdf
    assert_allclose(law.cdf([endpoint, endpoint+1]), 1)
    assert_allclose(law.sf([endpoint, endpoint+1]), 0)


@pytest.mark.parametrize("alpha", [.8, 1.5, 3])
def test_frechet_formulas_gev_mapping_and_small_survival(alpha):
    scale = 2
    law = frechet(alpha, scale)
    assert law.support() == (0, np.inf)
    y = np.array([.5, 2., 4., 10.])
    t = (y/scale)**-alpha
    assert_allclose(law.cdf(y), np.exp(-t))
    assert_allclose(law.sf(y), -np.expm1(-t))
    assert_allclose(law.pdf(y), alpha*t/y*np.exp(-t))
    assert_allclose(law.cdf(y), generalized_extreme_value(1/alpha, scale, scale/alpha).cdf(y))
    assert_allclose(law.pdf([-1, 0]), 0)
    assert_allclose(law.cdf([-1, 0]), 0)
    assert_allclose(law.sf([-1, 0]), 1)
    assert law.sf(1e30) > 0
    mass, _ = quad(law.pdf, 0, np.inf)
    assert mass == pytest.approx(1, abs=1e-8)


@pytest.mark.parametrize("factory,args", [
    (generalized_pareto, (np.nan,)), (generalized_pareto, (.2, 0)),
    (generalized_pareto, ([.2],)), (generalized_pareto, (.2, np.inf)),
    (generalized_extreme_value, (np.inf,)), (generalized_extreme_value, (.2, np.nan)),
    (generalized_extreme_value, (.2, 0, -1)), (generalized_extreme_value, (.2j,)),
    (frechet, (0,)), (frechet, (-1,)), (frechet, (1, 0)), (frechet, (np.nan,)),
    (generalized_pareto, (None,)), (generalized_extreme_value, (None,)),
    (frechet, (None,)), (frechet, (10**400,)),
])
def test_distribution_invalid_parameters(factory, args):
    with pytest.raises(ValueError):
        factory(*args)


def test_zero_shape_limits_and_tiny_tails():
    y = np.array([.1, 1, 5])
    for xi in [-1e-10, 1e-10]:
        gpd, gev = generalized_pareto(xi), generalized_extreme_value(xi)
        assert_allclose(gpd.sf(y), np.exp(-y), rtol=2e-9)
        assert_allclose(gpd.cdf(y), -np.expm1(-y), rtol=2e-9)
        assert_allclose(gpd.pdf(y), np.exp(-y), rtol=2e-9)
        assert_allclose(gev.cdf(y), np.exp(-np.exp(-y)), rtol=2e-9)
        assert_allclose(gev.sf(y), -np.expm1(-np.exp(-y)), rtol=2e-9)
        assert_allclose(gev.pdf(y), np.exp(-y-np.exp(-y)), rtol=2e-9)
    assert generalized_extreme_value(.3).sf(1e15) > 0
    assert generalized_pareto(.4).sf(1e15) > 0


def test_running_ratio_exact_prefixes_zeros_and_overflow():
    sample = np.array([1., 1, 1, 1, 16, 1, 1, 1, 1])
    assert_allclose(max_to_sum_path(sample), np.maximum.accumulate(sample)/np.cumsum(sample))
    assert_allclose(max_to_sum_path([0, 0, 3, 0, 3]), [np.nan, np.nan, 1, 1, .5])
    assert np.isnan(max_to_sum_path([0, 0])).all()
    assert_allclose(max_to_sum_path([1e308, 1e308, 1e308]), [1, .5, 1/3], rtol=2e-13)
    assert_allclose(max_to_sum_path([1e-300, 1e-300, 1e300]), [1, .5, 1], rtol=2e-13)
    rng = np.random.default_rng(41)
    sample = rng.lognormal(size=100)
    path = max_to_sum_path(sample)
    assert path[-1] == pytest.approx(max_to_sum_ratio(sample))
    assert_allclose(path, max_to_sum_path(sample*1e200), rtol=1e-12)
    assert np.all((path >= 1/np.arange(1, 101)-1e-14) & (path <= 1))


@pytest.mark.parametrize("sample", [[], [[1, 2]], [-1, 2], [np.nan], [np.inf], [1j]])
def test_running_ratio_rejects_invalid_samples(sample):
    with pytest.raises(ValueError):
        max_to_sum_path(sample)


@pytest.mark.parametrize("xi", [-.3, 0, .4])
def test_gpd_fit_recovers_deterministic_quantiles_and_scale(xi):
    # Smooth quantile samples isolate the numerical fit from Monte Carlo luck.
    excess = generalized_pareto(xi, 2).ppf((np.arange(3000)+.5)/3000)
    sample = np.r_[0., 3., 3., 3+excess]
    result = gpd_threshold_fit(sample, 3)
    assert result["success"], result
    assert result["count"] == 3000  # ties at u are excluded
    assert result["xi"] == pytest.approx(xi, abs=.008)
    assert result["beta"] == pytest.approx(2, abs=.02)
    assert result["modified_scale"] == pytest.approx(result["beta"]-3*result["xi"])
    assert np.all(1+result["xi"]*excess/result["beta"] > 0)


def test_gpd_fit_mask_degenerate_invalid_and_failed_support(monkeypatch):
    from xmath.incerto import estimators
    result = gpd_threshold_fit([1, 2, 2, 4], 2, min_exceedances=2)
    assert result["count"] == 1 and not result["success"]
    assert result["status"] == "insufficient count" and np.isnan(result["xi"])
    assert gpd_threshold_fit([1, 2], 2)["count"] == 0
    assert gpd_threshold_fit([4]*30, 2)["status"] == "constant excesses"
    for x, u, minimum in [([], 1, 1), ([1, np.nan], 1, 1), ([1, 2], np.inf, 1),
                          ([1, 2], 1, 0), ([[1, 2]], 1, 1), ([1j, 2], 1, 1)]:
        with pytest.raises(ValueError):
            gpd_threshold_fit(x, u, min_exceedances=minimum)
    with pytest.raises(TypeError):
        gpd_threshold_fit([1, 2], 1, min_exceedances=1.5)
    monkeypatch.setattr(estimators.genpareto, "fit", lambda *a, **k: (-1, 0, .1))
    result = gpd_threshold_fit(np.arange(31), 0)
    assert not result["success"] and "support" in result["status"]
    assert np.isnan(result["beta"]) and result["count"] == 30


def test_gpd_fit_reports_optimizer_nonconvergence(monkeypatch):
    from xmath.incerto import estimators
    monkeypatch.setattr(estimators, "fmin", lambda *a, **k: (np.array([.1, 1]), 0, 2000, 4000, 1))
    result = gpd_threshold_fit(np.arange(31), 0)
    assert not result["success"] and "converge" in result["status"]


def test_gpd_fit_retains_count_when_finite_inputs_overflow_excesses():
    sample = np.linspace(1., 1.7, 30)*1e308
    result = gpd_threshold_fit(sample, -1e308)
    assert result["count"] == 30 and not result["success"]
    assert result["status"].startswith("fit failed:")
    assert "overflow" in result["status"]
    assert all(np.isnan(result[key]) for key in ("xi", "beta", "modified_scale"))
    insufficient = gpd_threshold_fit(sample, -1e308, min_exceedances=31)
    assert insufficient["count"] == 30
    assert insufficient["status"] == "insufficient count"


@pytest.mark.parametrize("parameters", [(.2, 1., 2.), (.2, 0., 0.),
                                        (.2, 0., np.nan), (np.inf, 0., 2.)])
def test_gpd_fit_rejects_invalid_optimizer_results(parameters, monkeypatch):
    from xmath.incerto import estimators
    monkeypatch.setattr(estimators.genpareto, "fit", lambda *a, **k: parameters)
    result = gpd_threshold_fit(np.arange(31.), 0)
    assert result["count"] == 30 and not result["success"]
    assert all(np.isnan(result[key]) for key in ("xi", "beta", "modified_scale"))


def test_shared_sample_population_and_mean_excess_mask():
    demo = runpy.run_path(str(ROOT / "demos/incerto/tail_estimation.py"))
    exact, mixture = demo["synthetic_samples"]()
    again = demo["synthetic_samples"]()
    assert np.array_equal(exact, again[0]) and np.array_equal(mixture, again[1])
    assert len(mixture) == 30000 and np.all(mixture >= 1)
    assert_allclose(demo["mixture_survival"]([0, 1, 2, 3, 6]), [1, 1, .59, .18, .18*2**-1.7])
    result = mean_excess([1, 2, 2, 4], [1, 2, 4], min_exceedances=2)
    assert_allclose(result["exceedances"], [3, 1, 0])
    assert_allclose(result["mean_excess"], [5/3, np.nan, np.nan])


def test_card_layout_support_markers_and_no_log_zero():
    fig = distribution_card([(generalized_pareto(-.4), "bounded")],
                             np.linspace(-1, 4, 51), np.geomspace(.1, 4, 41),
                             title="GPD", support_note="Endpoint 2.5")
    assert len(fig.axes) == 3
    assert fig.axes[2].get_xscale() == fig.axes[2].get_yscale() == "log"
    values = fig.axes[2].lines[0].get_ydata()
    assert np.isnan(values).any() and np.all(values[np.isfinite(values)] > 0)
    assert any(np.array_equal(line.get_xdata(), [2.5, 2.5]) for line in fig.axes[2].lines[1:])
    assert fig.axes[0].get_position().y0 > fig.axes[1].get_position().y0 > fig.axes[2].get_position().y0
    plt.close(fig)
    fig, axes = vertical_figure(1)
    assert axes.shape == (1,)
    plt.close(fig)
    for panels in (0, 1.5, True):
        with pytest.raises(ValueError):
            vertical_figure(panels)
    with pytest.raises(ValueError):
        vertical_figure(1, panel_height=-1)
    with pytest.raises(ValueError):
        distribution_card([(pareto_type1(2), "Pareto")], [0, 1], [0, 2], title="", support_note="")


@pytest.mark.parametrize("producer,names", [
    ("distribution_cards", ["pareto-card", "gpd-card", "gev-card", "frechet-card", "double-pareto-card", "frechet-maxima"]),
    ("tail_estimation", ["hill-stability", "mean-excess", "threshold-diagnostics", "threshold-gpd", "threshold-pp"]),
    ("max_to_sum", ["max-to-sum"]),
    ("glossary_worked_cases", ["glossary-slow-variation"]),
])
def test_p1_svg_reproducibility(producer, names, tmp_path):
    # Two fresh interpreter runs and comparison with the checked-in assets:
    # catches RNG/metadata/hash instability and stale exports together.
    script = ROOT / f"demos/incerto/{producer}.py"
    for run in ("a", "b"):
        output = tmp_path / run
        code = f"import runpy; runpy.run_path({str(script)!r})['main']({str(output)!r})"
        env = {**os.environ, "MPLBACKEND": "Agg", "MPLCONFIGDIR": str(tmp_path / "mpl"),
               "OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1"}
        result = subprocess.run([sys.executable, "-c", code], env=env, cwd=tmp_path,
                                capture_output=True, text=True, timeout=90)
        assert result.returncode == 0, result.stdout + result.stderr
    for name in names:
        first = (tmp_path / "a" / f"{name}.svg").read_bytes()
        assert first == (tmp_path / "b" / f"{name}.svg").read_bytes(), name
        assert first == (ROOT / f"assets/figures/incerto/{name}.svg").read_bytes(), name
        assert b"<dc:date>" not in first and b"Bold" not in first
