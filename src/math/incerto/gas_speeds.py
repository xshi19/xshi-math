"""Equilibrium chi speeds and likelihood comparisons for the Rayleigh note.

Speeds are sampled from independent Gaussian components, not collision dynamics.
Positive families have location fixed at zero. KS p-values after fitting are
uncorrected diagnostics. GIG fitting includes its normalizable Gamma and inverse
Gamma boundaries; a boundary result is a supremum for the strict interior family.
"""

from __future__ import annotations

from dataclasses import dataclass
from numbers import Integral
from typing import Any

import numpy as np
from numpy.typing import ArrayLike
from scipy import stats
from scipy.optimize import fmin


def _positive_scalar(value, name):
    if np.iscomplexobj(value) or np.ndim(value) != 0:
        raise ValueError(f"{name} must be a finite positive scalar")
    value = float(value)
    if not np.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be a finite positive scalar")
    return value


def _count(value, name):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, Integral) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return int(value)


def _sample(sample, *, fitting=False):
    if np.iscomplexobj(sample):
        raise ValueError("sample must be real")
    x = np.asarray(sample, dtype=float)
    if (x.ndim != 1 or x.size < (3 if fitting else 1)
            or not np.all(np.isfinite(x)) or np.any(x <= 0)):
        raise ValueError("sample must be a finite positive vector of sufficient length")
    if fitting and np.ptp(x) == 0:
        raise ValueError("fitting requires a nonconstant sample")
    return x


def chi_speed(dimension: int = 2, thermal_variance: float = 1.0):
    """Frozen chi law for speed, with component variance kT/m.

    ``dimension`` is a positive integer; ``thermal_variance`` is a finite
    positive scalar. Returns a SciPy law exposing pdf/cdf/sf/ppf/moment/rvs.
    Support is [0, infinity); dimensions 1, 2, 3 give half-normal, Rayleigh,
    Maxwell. Density and CDF are zero at negative speeds.
    """
    d = _count(dimension, "dimension")
    variance = _positive_scalar(thermal_variance, "thermal_variance")
    return stats.chi(d, scale=np.sqrt(variance))


def sample_chi_speed(size: int, *, dimension: int = 2,
                     thermal_variance: float = 1.0, random_state=None):
    """Draw iid speeds from Gaussian components; return a length-size array.

    Counts are positive integers; thermal_variance is kT/m > 0. random_state
    is a NumPy Generator, integer seed, or None. Draw order is (dimension,
    size), so all first components precede all second components. Hypot
    reduction avoids unnecessary overflow of squared components. Nonfinite
    or zero floating-point draws raise; none are clipped or resampled.
    """
    size, d = _count(size, "size"), _count(dimension, "dimension")
    variance = _positive_scalar(thermal_variance, "thermal_variance")
    rng = np.random.default_rng(random_state)
    with np.errstate(over="ignore"):
        components = rng.normal(0, np.sqrt(variance), (d, size))
        speeds = np.hypot.reduce(components, axis=0)
    if not np.all(np.isfinite(speeds)) or np.any(speeds <= 0):
        raise FloatingPointError("sampled speed is not representable")
    return speeds


@dataclass(frozen=True)
class SpeedFit:
    """One fitted law and its diagnostics; p-values are not fit-corrected.

    ``law`` is a frozen SciPy distribution in the input speed units.
    ``parameters`` counts estimated parameters, excluding fixed locations.
    ``boundary`` is empty for an interior fit, otherwise names the GIG limit.
    AIC uses 2*parameters - 2*log_likelihood, including a nominal count of
    three for GIG even on a boundary where ordinary AIC theory is irregular.
    """

    name: str
    law: Any
    parameters: int
    log_likelihood: float
    aic: float
    ks_statistic: float
    ks_pvalue: float
    boundary: str = ""


def _optimizer(function, start, args=(), disp=0):
    result, _, _, _, flag = fmin(function, start, args=args, disp=False,
                                 full_output=True, maxiter=4000, maxfun=8000,
                                 xtol=1e-8, ftol=1e-8)
    if flag:
        raise RuntimeError("maximum-likelihood optimizer did not converge")
    return result


def _gig_fit(x, gamma_law, inverse_gamma_law):
    # In natural coordinates (p-1, -a/2, -b/2) the log likelihood is concave.
    # At the Gamma MLE only the b-direction remains; a nonpositive inward
    # derivative certifies the global boundary maximum. Likewise for a at
    # the inverse Gamma boundary. No tiny positive b is misreported as zero.
    shape = gamma_law.args[0]
    if shape > 1 and 1 / ((shape - 1) * gamma_law.kwds["scale"]) <= np.mean(1 / x):
        return gamma_law, "Gamma"
    shape = inverse_gamma_law.args[0]
    if shape > 1 and inverse_gamma_law.mean() <= np.mean(x):
        return inverse_gamma_law, "inverse Gamma"
    p, b, loc, scale = stats.geninvgauss.fit(x, floc=0, optimizer=_optimizer)
    if not np.all(np.isfinite([p, b, loc, scale])) or b <= 0 or scale <= 0:
        raise RuntimeError("invalid interior GIG fit")
    law = stats.geninvgauss(p, b, loc=0, scale=scale)
    ll = np.sum(law.logpdf(x))
    boundary_ll = max(np.sum(gamma_law.logpdf(x)), np.sum(inverse_gamma_law.logpdf(x)))
    if not np.isfinite(ll) or ll < boundary_ll - 1e-7:
        raise RuntimeError("interior GIG fit is worse than an available boundary")
    return law, ""


def fit_speed_models(sample: ArrayLike) -> tuple[SpeedFit, ...]:
    """Fit seven candidate families by maximum likelihood; sort by AIC.

    Require at least three finite, positive, nonconstant observations.
    Gaussian estimates mean/standard deviation. Rayleigh estimates one
    scale. Gamma, inverse Gamma, inverse Gaussian and Weibull estimate shape
    and scale with location zero; GIG estimates three parameters. The inverse
    Gamma MLE is obtained by a Gamma fit to reciprocal observations.

    GIG boundary optima are certified by the inward likelihood derivative;
    otherwise SciPy's numerical interior fit must converge and beat both
    boundary likelihoods. Numerical interior convergence is not a global
    optimization certificate. Nonfinite calculations or failed fits raise.
    Ordinary underflow of extremely small KS p-values to zero is retained.
    Interior GIG CDF quadrature can be slow for large samples.
    """
    x = _sample(sample, fitting=True)
    with np.errstate(over="raise", divide="raise", invalid="raise"):
        mu, sigma = stats.norm.fit(x)
        rayleigh_scale = np.sqrt(np.mean(x**2) / 2)
        shape, _, scale = stats.gamma.fit(x, floc=0)
        gamma_law = stats.gamma(shape, scale=scale)
        shape, _, scale = stats.gamma.fit(1 / x, floc=0)
        inverse_gamma_law = stats.invgamma(shape, scale=1 / scale)
        shape, _, scale = stats.invgauss.fit(x, floc=0)
        inverse_gaussian_law = stats.invgauss(shape, scale=scale)
        shape, _, scale = stats.weibull_min.fit(x, floc=0, optimizer=_optimizer)
        weibull_law = stats.weibull_min(shape, scale=scale)
        gig_law, boundary = _gig_fit(x, gamma_law, inverse_gamma_law)
    candidates = (
        ("Gaussian", stats.norm(mu, sigma), 2, ""),
        ("Rayleigh", stats.rayleigh(scale=rayleigh_scale), 1, ""),
        ("Gamma", gamma_law, 2, ""),
        ("inverse Gamma", inverse_gamma_law, 2, ""),
        ("inverse Gaussian", inverse_gaussian_law, 2, ""),
        ("GIG", gig_law, 3, boundary),
        ("Weibull", weibull_law, 2, ""),
    )
    fits = []
    for name, law, count, boundary in candidates:
        ll = float(np.sum(law.logpdf(x)))
        ks = stats.kstest(x, law.cdf, method="exact")
        aic = 2 * count - 2 * ll
        if not np.all(np.isfinite([ll, aic, ks.statistic, ks.pvalue])):
            raise FloatingPointError(f"nonfinite fit diagnostic: {name}")
        fits.append(SpeedFit(name, law, count, ll, aic,
                             float(ks.statistic), float(ks.pvalue), boundary))
    return tuple(sorted(fits, key=lambda fit: fit.aic))


def speed_fit_table(fits) -> str:
    """Format SpeedFit records as an AIC-sorted text table, without printing.

    AIC has one decimal, KS distance four, and uncorrected p-values three
    significant digits. A p-value rounded to floating-point zero prints 0.
    """
    lines = [f"{'Model':<18} {'K':>1} {'AIC':>10} {'KS D':>8} {'KS p (raw)':>12}"]
    for fit in sorted(fits, key=lambda fit: fit.aic):
        lines.append(f"{fit.name:<18} {fit.parameters:1d} {fit.aic:10.1f} "
                     f"{fit.ks_statistic:8.4f} {fit.ks_pvalue:12.3g}")
    return "\n".join(lines)


def speed_qq(sample: ArrayLike, law, probabilities=None):
    """Return theoretical and empirical quantiles for a positive sample.

    ``law`` exposes ppf. Default: 199 equally spaced probabilities from
    0.005 to 0.995. An explicit grid must be finite, increasing, nonempty,
    one-dimensional, and strictly inside (0, 1). Empirical quantiles use
    NumPy's linear interpolation; theoretical quantiles must be finite.
    """
    x = _sample(sample)
    if probabilities is None:
        probabilities = np.linspace(0.005, 0.995, 199)
    if np.iscomplexobj(probabilities):
        raise ValueError("probabilities must be real")
    q = np.asarray(probabilities, dtype=float)
    if (q.ndim != 1 or q.size == 0 or not np.all(np.isfinite(q))
            or np.any(q <= 0) or np.any(q >= 1) or np.any(np.diff(q) <= 0)):
        raise ValueError("probabilities must increase strictly inside (0, 1)")
    theoretical = np.asarray(law.ppf(q), dtype=float)
    if theoretical.shape != q.shape or not np.all(np.isfinite(theoretical)):
        raise FloatingPointError("theoretical quantiles must be finite and match the grid")
    return theoretical, np.quantile(x, q, method="linear")


def squared_speed_ks(sample: ArrayLike, thermal_variance: float = 1.0):
    """Two-sided KS of squared 2D speeds vs Exp(mean=2*kT/m).

    thermal_variance must be specified independently of this sample for the
    usual simple-null calibration. No parameter is estimated. Returns a dict
    with float ``statistic`` and ``pvalue``; overflow on squaring raises.
    """
    x = _sample(sample)
    variance = _positive_scalar(thermal_variance, "thermal_variance")
    with np.errstate(over="raise", invalid="raise"):
        squared = (x / np.sqrt(variance))**2
    ks = stats.kstest(squared, stats.expon(scale=2).cdf, method="exact")
    return {"statistic": float(ks.statistic), "pvalue": float(ks.pvalue)}


def speed_fit_figure(sample: ArrayLike, fits, *, kind="density", thermal_variance=1.0):
    """Return a single-column density or QQ figure with two panels.

    Use the same positive sample that generated the supplied SpeedFit records.
    Density: 80-bin histogram and 401-point fitted curves on linear/log axes.
    QQ: 199 probabilities in [0.005, 0.995]; qq shows five central fits and
    squared speed against the specified Exp(mean=2*kT/m) null; qq-tail shows
    the inverse Gaussian and inverse Gamma on their own ranges. Every panel
    retains its full plotted quantile range. This helper applies the shared
    DejaVu Serif theme and draws, but neither saves nor closes the figure.
    """
    from xmath.incerto.figures import COLORS, COLOR_CYCLE, set_theme, vertical_figure

    x = _sample(sample)
    variance = _positive_scalar(thermal_variance, "thermal_variance")
    if kind not in {"density", "qq", "qq-tail"}:
        raise ValueError("kind must be density, qq, or qq-tail")
    fits = tuple(fits)
    by_name = {fit.name: fit for fit in fits}
    required = {"Rayleigh", "Weibull", "Gamma", "GIG", "Gaussian", "inverse Gaussian", "inverse Gamma"}
    if set(by_name) != required or len(fits) != len(required):
        raise ValueError("one fit for each of the seven candidate families is required")
    set_theme(scale=1.1)
    fig, axes = vertical_figure(2, panel_height=3.5)
    styles = ("-", "--", "-.", ":", "-", "--", "-.")
    appearance = {fit.name: (COLOR_CYCLE[i], styles[i]) for i, fit in enumerate(fits)}
    if kind == "density":
        grid = np.linspace(-0.5 * np.sqrt(variance), max(x), 401)
        for ax in axes:
            ax.hist(x, bins=80, density=True, color=COLORS["sand"], label="Sample")
            for fit in fits:
                color, style = appearance[fit.name]
                ax.plot(grid, fit.law.pdf(grid), color=color, ls=style, label=fit.name)
            ax.set(xlabel="Speed v", ylabel="Density")
            ax.legend(ncol=2, loc="upper center", bbox_to_anchor=(0.5, -0.23))
        axes[0].set_title("Chamber speeds and fitted densities")
        axes[1].set(yscale="log", ylim=(1e-5 / np.sqrt(variance), 2 / np.sqrt(variance)),
                    title="The same densities on a log scale")
    else:
        groups = ((("Rayleigh", "Weibull", "Gaussian", "Gamma", "GIG"),) if kind == "qq"
                  else (("inverse Gaussian",), ("inverse Gamma",)))
        for ax, names in zip(axes, groups):
            limits = [0.0]
            for name in names:
                theoretical, empirical = speed_qq(x, by_name[name].law)
                color, style = appearance[name]
                ax.plot(theoretical, empirical, color=color, ls=style, label=name)
                limits.extend([min(theoretical), max(theoretical), max(empirical)])
            ax.plot([min(limits), max(limits)], [min(limits), max(limits)],
                    color=COLORS["muted"], ls=":", lw=1, label="Equality")
            ax.set(xlabel="Fitted speed quantile", ylabel="Sample speed quantile",
                   ylim=(0, max(empirical) * 1.05))
            ax.legend(ncol=2, loc="upper center", bbox_to_anchor=(0.5, -0.23))
        if kind == "qq":
            with np.errstate(over="raise"):
                theoretical, empirical = speed_qq(x**2, stats.expon(scale=2 * variance))
            axes[-1].plot(theoretical, empirical, color=COLORS["accent"], label="Squared speed")
            axes[-1].plot([0, max(theoretical)], [0, max(theoretical)],
                           color=COLORS["muted"], ls=":", label="Equality")
            axes[-1].set(xlabel="Exp(mean 2 kT/m) quantile", ylabel="Sample squared-speed quantile")
            axes[-1].legend(loc="upper left")
        axes[0].set_title("Quantile comparisons" if kind == "qq" else "Inverse-family quantiles")
    return fig
