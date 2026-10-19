"""Chapter 6 and appendix A: five figures, bounded models, no external data.

Run: uv run python demos/incerto/multivariate_tails.py
PCG64 seed 20261018; 400 replications per size <=1000; 12 matrices of size
80 per law. Quadrature limit 200, epsabs/epsrel 1e-9; checks errors <=2e-8.
No censoring, clipping, nonfinite removal or data fitting. Runtime: seconds.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import numpy as np
from scipy.integrate import quad
from scipy.stats import gamma, norm, t, semicircular

from xmath.incerto.figures import COLORS, savefig, set_theme
from xmath.incerto.lecture_risk import survival_from_hazards
from xmath.incerto.multivariate import (
    bivariate_student, sample_correlation, student_mutual_information,
    symmetric_spectrum, regression_population_r2, normal_location_mixture_kurtosis,
)

OUTPUT = Path(__file__).resolve().parents[2] / "assets/figures/incerto"


def export(fig, name):
    for ax in fig.axes:
        for line in ax.lines:
            if not np.all(np.isfinite(line.get_ydata())) or not np.all(np.isfinite(line.get_xdata())):
                raise FloatingPointError(f"nonfinite figure values: {name}")
        if ax.get_legend_handles_labels()[1]:
            ax.legend(loc="upper center", bbox_to_anchor=(.5, -.24), fontsize=10,
                      handlelength=3, ncol=1)
    savefig(fig, OUTPUT/name)
    plt.close(fig)


def integral(fn):
    value, error = quad(fn, 0, np.inf, epsabs=1e-9, epsrel=1e-9, limit=200)
    if not np.isfinite(value) or not np.isfinite(error) or error > 2e-8:
        raise FloatingPointError("quadrature failed its error budget")
    return value, error


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)
    rng = np.random.Generator(np.random.PCG64(20261018))

    grid = np.linspace(-4, 4, 241)
    x, y = np.meshgrid(grid, grid)
    r = .8
    density = (
        1/(np.pi**2*(1+x*x)*(1+y*y)),
        1/(2*np.pi)*(1+x*x+y*y)**-1.5,
        (np.exp(-(x*x-2*r*x*y+y*y)/(2*(1-r*r)))
         + np.exp(-(x*x+2*r*x*y+y*y)/(2*(1-r*r))))/(4*np.pi*np.sqrt(1-r*r)),
    )
    titles = ["Independent Cauchy coordinates", "Spherical Cauchy: shared scale",
              "Normal mixture: switching correlation"]
    fig, axes = plt.subplots(3, 1, figsize=(5, 13), layout="constrained")
    for ax, f, title in zip(axes, density, titles):
        if not np.all(np.isfinite(f)):
            raise FloatingPointError("nonfinite density")
        levels = f[120, 120]*np.array([.05, .15, .35, .65])
        ax.contour(x, y, f, levels=levels, colors=[COLORS[c] for c in ["teal", "green", "umber", "accent"]])
        ax.set(xlabel="Coordinate x1", ylabel="Coordinate x2", title=title, aspect="equal")
    export(fig, "multivariate-geometry.svg")
    sector, err = quad(lambda radius: radius*(1+radius*radius)**-1.5/6, 3, np.inf,
                       epsabs=1e-10, epsrel=1e-10)
    if err > 1e-9 or not np.isclose(sector, 1/(6*np.sqrt(10)), rtol=1e-10):
        raise FloatingPointError("sector probability failed")
    print(f"Cauchy sector probability (u=3, angle=pi/3): {sector:.12g}")
    for s in (4., 8., 12.):
        print(f"Axial/equal densities s={s:g}: normal={np.exp(-s*s/4):.9g}, "
              f"independent Cauchy={(1+s*s/4)**2/(1+s*s):.9g}")

    fig, axes = plt.subplots(2, 1, figsize=(5, 9), layout="constrained")
    nus = np.geomspace(.75, 30, 121)
    for rho, style in [(0, "-"), (.6, "--")]:
        axes[0].plot(nus, [student_mutual_information(nu, rho) for nu in nus], style,
                     label=f"Scatter rho = {rho:g}")
    axes[0].set(xscale="log", xlabel="Student degrees of freedom", ylabel="Mutual information (nats)",
                title="Dependence survives diagonal scatter")
    thresholds = np.geomspace(.2, 8, 61)
    joint, errors = [], []
    for u in thresholds:
        value, err = integral(lambda g: (2*norm.sf(u*np.sqrt(g)))**2*gamma.pdf(g, 1.5, scale=2/3))
        joint.append(value)
        errors.append(err)
    marginal = 2*t.sf(thresholds, 3)
    axes[1].plot(thresholds, joint, label="Shared-scale joint probability")
    axes[1].plot(thresholds, marginal**2, "--", label="Independent marginals")
    axes[1].set(xscale="log", yscale="log", xlabel="Absolute threshold u",
                ylabel="P(|X1| > u, |X2| > u)", title="Joint exceedances at nu = 3")
    axes[1].set_xticks([.2, .5, 1, 2, 5], labels=["0.2", "0.5", "1", "2", "5"])
    axes[1].xaxis.set_minor_formatter(NullFormatter())
    export(fig, "multivariate-information.svg")
    print("Student information at rho=0:", {nu: student_mutual_information(nu) for nu in [1, 3, 5, 30]})
    print(f"Joint-tail quadrature maximum error estimate: {max(errors):.3g}")

    fig, axes = plt.subplots(3, 1, figsize=(5, 12), layout="constrained")
    n, repetitions = 80, 12
    upper = np.triu_indices(n)
    for ax, nu, title in zip(axes, [None, 3, 1.5], ["Normal entries: variance one",
                            "Student 3 entries: variance one", "Student 1.5 entries: scale one"]):
        all_values = []
        for rep in range(repetitions):
            entries = rng.standard_normal(len(upper[0])) if nu is None else rng.standard_t(nu, len(upper[0]))
            if nu == 3:
                entries /= np.sqrt(3)
            matrix = np.zeros((n, n))
            matrix[upper] = entries
            matrix[(upper[1], upper[0])] = entries
            matrix /= np.sqrt(n)
            values = symmetric_spectrum(matrix)
            if not np.isclose(values@values, np.sum(matrix*matrix), rtol=1e-12):
                raise FloatingPointError("spectral trace identity failed")
            all_values.extend(values)
            ax.step(values, np.arange(1, n+1)/n, where="post", color=COLORS["accent"],
                    alpha=.45, linewidth=1, label="12 matrix CDFs" if rep == 0 else None)
        if nu is None or nu == 3:
            v = np.linspace(min(-2.2, min(all_values)), max(2.2, max(all_values)), 801)
            ax.plot(v, semicircular.cdf(v, scale=2), "--", color=COLORS["umber"], label="Semicircle limit CDF")
        ax.set(xlabel="Eigenvalue of W / sqrt(80)", ylabel="Fraction at or below", title=title)
        print(f"Spectra {title}: full range [{min(all_values):.9g}, {max(all_values):.9g}]")
    export(fig, "multivariate-spectra.svg")

    sizes = np.array([30, 100, 300, 1000])
    reps = 400
    fig, axes = plt.subplots(2, 1, figsize=(5, 9), layout="constrained")
    for nu, color, style in [(1.5, COLORS["accent"], "-"), (5, COLORS["green"], "--")]:
        quantiles = []
        for size in sizes:
            sample = bivariate_student(rng, nu, .6, int(reps*size)).reshape(reps, size, 2)
            correlations = sample_correlation(sample[:, :, 0], sample[:, :, 1])
            if not np.all(np.isfinite(correlations)):
                raise FloatingPointError("degenerate sample correlation")
            quantiles.append(np.quantile(correlations, [.1, .5, .9]))
        q = np.array(quantiles)
        axes[0].plot(sizes, q[:, 1], style, color=color, label=f"Student {nu:g}: median")
        axes[0].fill_between(sizes, q[:, 0], q[:, 2], color=color, alpha=.15)
        print(f"Sample correlation nu={nu:g}, 10/50/90 percentiles:", q.tolist())
    axes[0].axhline(.6, color=COLORS["umber"], linestyle=":", label="Population rho (nu=5 only)")
    axes[0].set(xscale="log", ylim=(-1, 1), xlabel="Sample size n", ylabel="Centered sample correlation",
                title="A finite coefficient, different moment gates")
    quantiles = []
    for size in sizes:
        predictors = rng.standard_normal((reps, size))
        response = predictors+rng.standard_t(3, (reps, size))
        r2 = sample_correlation(predictors, response)**2
        if not np.all(np.isfinite(r2)):
            raise FloatingPointError("degenerate regression")
        quantiles.append(np.quantile(r2, [.1, .5, .9]))
    q = np.array(quantiles)
    axes[1].plot(sizes, q[:, 1], label="Fitted R squared: median")
    axes[1].fill_between(sizes, q[:, 0], q[:, 2], alpha=.15, color=COLORS["accent"])
    axes[1].axhline(regression_population_r2(1, 3), color=COLORS["umber"], linestyle="--", label="Population target 1/4")
    axes[1].set(xscale="log", ylim=(0, 1), xlabel="Sample size n", ylabel="Fitted R squared",
                title="Independent Student-3 regression error")
    for ax in axes:
        ax.set_xticks(sizes, labels=[str(n) for n in sizes])
        ax.xaxis.set_minor_formatter(NullFormatter())
    export(fig, "multivariate-sampling.svg")
    print("Regression R2 10/50/90 percentiles:", q.tolist())

    fig, axes = plt.subplots(3, 1, figsize=(5, 12), layout="constrained")
    x = np.linspace(-6, 6, 481)
    for m, style in [(0, "--"), (2, "-")]:
        axes[0].plot(x, (norm.pdf(x-m)+norm.pdf(x+m))/2, style, label=f"Separation m = {m}")
    axes[0].set(xlabel="Outcome x", ylabel="Density", title="Moving locations creates a central valley")
    m = np.linspace(0, 5, 241)
    axes[1].plot(m, normal_location_mixture_kurtosis(m), label="Equal location mixture")
    axes[1].axhline(3, color=COLORS["umber"], linestyle="--", label="Gaussian kurtosis")
    axes[1].set(xlabel="Location m (sigma = 1)", ylabel="Pearson kurtosis", title="Low kurtosis can accompany two regimes")
    steps = np.arange(1, 101)
    for hazards, label, style in [(np.full(100, .05), "Constant hazard 0.05", "-"),
                                  (2.**(-steps-1), "Decreasing hazard", "--")]:
        survival = survival_from_hazards(hazards)[1:]
        axes[2].plot(steps, survival, style, label=label)
        print(f"Intact survival after 100 steps ({label}): {survival[-1]:.12g}")
    axes[2].set(xlabel="Step n", ylabel="Intact probability", ylim=(0, 1),
                title="Absorption requires persistent risk")
    export(fig, "multivariate-regimes.svg")
    print("Location mixture m=2 sigma=1 kurtosis:", normal_location_mixture_kurtosis(2))
    print("Rare Pareto regime: survival at 4 =", .02*4**-1.5,
          "; mean =", .98/2+.02*3, "; second moment = infinity")
    print("Five figures exported; no clipped draws or omitted eigenvalues.")


if __name__ == "__main__":
    main()
