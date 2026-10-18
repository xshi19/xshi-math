"""SCoFT v4 chapter 4: fixed model curves and bounded repeated samples.

Run: uv run python demos/incerto/finite_moments.py
PCG64 seed 20261018, four laws x four sizes x 600 independent replications.
Largest sample matrix: 600 x 5000; no clipping, censoring or external data.
Four deterministic SVGs; normal runtime is seconds. Curves do not prove limits.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from scipy.special import gammaln
from scipy.stats import norm

from xmath.incerto.figures import COLORS, savefig, set_theme
from xmath.incerto.finite_moments import (
    normal_mixture_absolute_moment,
    normal_mixture_log_abs_survival,
    normal_mixture_log_density,
    pareto_moment_estimator_summary,
    power_mean,
)
from xmath.incerto.stats import (
    normal_peak_shoulder_tail,
    normal_variance_peak_shoulder_tail,
    t_peak_shoulder_tail,
)


def _save(fig, output, name):
    for ax in fig.axes:
        for line in ax.lines:
            if not np.all(np.isfinite(line.get_ydata())):
                raise ValueError(f"nonfinite curve: {name}")
    savefig(fig, output / name)
    plt.close(fig)


def main():
    output = Path(__file__).resolve().parents[2] / "assets/figures/incerto"
    output.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)
    x = np.linspace(-4, 4, 801)
    u = np.linspace(0, 12, 241)
    models = [([1], [1], "Gaussian", "-"),
              ([.4, 1.6], [.5, .5], "Equal-weight mixture", "--"),
              ([.5, 50.5], [.99, .01], "Rare wide component", "-.")]
    fig, axes = plt.subplots(2, 1, figsize=(5, 7.4), layout="constrained")
    for v, w, label, style in models:
        axes[0].plot(x, np.exp(normal_mixture_log_density(x, v, w)), style, label=label)
        axes[1].plot(u, normal_mixture_log_abs_survival(u, v, w), style, label=label)
        m2 = normal_mixture_absolute_moment(2, v, w)
        m4 = normal_mixture_absolute_moment(4, v, w)
        print(f"{label}: second moment={m2:.8g}, fourth moment={m4:.8g}, kurtosis={m4/m2**2:.8g}")
    axes[0].set(xlabel="Outcome x", ylabel="Density", title="Same variance, different shapes")
    axes[1].set(xlabel="Absolute threshold u", ylabel="Log P(|X| > u)", title="Finite-mixture tails")
    for ax in axes:
        ax.legend(fontsize=10, handlelength=3.5)
    _save(fig, output, "finite-moment-mixtures.svg")

    fig, axes = plt.subplots(2, 1, figsize=(5, 7.4), layout="constrained")
    curvature_half = norm.pdf(x) * (x**4-6*x**2+3) / 8
    axes[0].plot(x, curvature_half, label="Half variance curvature")
    for a, style in ((.1, "--"), (.6, "-.")):
        difference = (np.exp(normal_mixture_log_density(x, [1-a, 1+a], [.5, .5]))-norm.pdf(x))/a**2
        axes[0].plot(x, difference, style, label=f"Exact difference / a², a={a}")
        f = lambda t: normal_mixture_log_density(t, [1-a, 1+a], [.5, .5])-norm.logpdf(t)
        print(f"a={a}: positive density crossings {brentq(f, .1, 1.3):.9f}, {brentq(f, 1.3, 4):.9f}")
    for boundary in normal_variance_peak_shoulder_tail():
        axes[0].axvline(boundary, color=COLORS["muted"], linewidth=.7, alpha=.6)
    axes[0].set(xlabel="Outcome x", ylabel="Scaled density change", title="Local curvature and finite mixing")
    axes[0].set_ylim(-.13, .34)
    axes[0].legend(fontsize=10, handlelength=3.5)
    boundaries = [normal_variance_peak_shoulder_tail(), normal_peak_shoulder_tail(), t_peak_shoulder_tail(3)]
    labels = ["Normal: variance", "Normal: scale", "Student 3: scale"]
    for j, (points, label) in enumerate(zip(boundaries, labels)):
        axes[1].plot(points, [j]*4, "o-", label=label)
        print(label, points)
    axes[1].set(yticks=range(3), yticklabels=labels, ylim=(-.5, 2.5),
                xlabel="Boundary (scale = 1)", title="The perturbation changes the boundary")
    _save(fig, output, "finite-moment-curvature.svg")

    rng = np.random.Generator(np.random.PCG64(20261018))
    sizes, reps = (50, 200, 1000, 5000), 600
    results = {}
    for law in ("Gaussian", "Rare mixture", "Pareto 3", "Pareto 6"):
        target = 1 if law in ("Gaussian", "Rare mixture") else pareto_moment_estimator_summary(int(law[-1]), 2, 1)["moment"]
        quantiles = []
        for n in sizes:
            if law == "Gaussian":
                sample = rng.normal(size=(reps, n))
            elif law == "Rare mixture":
                variance = np.where(rng.random((reps, n)) < .01, 50.5, .5)
                sample = rng.normal(size=(reps, n)) * np.sqrt(variance)
                del variance
            else:
                sample = 1 + rng.pareto(int(law[-1]), size=(reps, n))
            estimates = np.mean(sample**2, axis=1) / target
            if not np.all(np.isfinite(estimates)):
                raise FloatingPointError("nonfinite sample moment; no values discarded")
            qs = np.quantile(estimates, [.1, .5, .9])
            quantiles.append(qs)
            print(f"{law}; n={n}; relative second moment q10/50/90=" + "/".join(f"{q:.6f}" for q in qs))
            del sample
        results[law] = np.asarray(quantiles)
    fig, axes = plt.subplots(2, 1, figsize=(5, 7.4), layout="constrained")
    for ax, names in zip(axes, (("Gaussian", "Rare mixture"), ("Pareto 3", "Pareto 6"))):
        for label, style in zip(names, ("-", "--")):
            qs = results[label]
            line, = ax.plot(sizes, qs[:, 1], style, marker="o", label=label)
            ax.fill_between(sizes, qs[:, 0], qs[:, 2], color=line.get_color(), alpha=.15)
        ax.axhline(1, color=COLORS["muted"], linewidth=1)
        ax.set(xscale="log", xlabel="Sample size n", ylabel="Estimate / population moment")
        ax.legend(fontsize=10)
    axes[0].set_title("Every moment finite")
    axes[1].set_title("Finite second moment in both laws")
    _save(fig, output, "finite-moment-estimation.svg")
    print(f"Rare state absent at n=50: {.99**50:.9f}; second-moment estimator variance: 76.25/n")
    for alpha in (3, 4, 6):
        print("Pareto", alpha, pareto_moment_estimator_summary(alpha, 2, 100))
    for n in (10, 100, 1000):
        log_bias_factor = .5*np.log(2/n) + gammaln((n+1)/2)-gammaln(n/2)
        print(f"Gaussian n={n}: RMS MSE/sigma²={-2*np.expm1(log_bias_factor):.9f}; "
              f"calibrated absolute MSE/sigma²={(np.pi/2-1)/n:.9f}")
    print("Power means for (0,0,0,4):", [power_mean([0, 0, 0, 4], p) for p in (1, 2, 4, np.inf)])

    fig, ax = plt.subplots(figsize=(5, 4.8), layout="constrained")
    angle = np.linspace(0, 2*np.pi, 801)
    unit = np.array([np.cos(angle), np.sin(angle)])
    for p, style in ((1, "-"), (2, "--"), (4, "-."), (np.inf, ":")):
        denom = np.max(np.abs(unit), axis=0) if np.isinf(p) else np.sum(np.abs(unit)**p, axis=0)**(1/p)
        curve = unit / denom
        ax.plot(*curve, style, label="p = infinity" if np.isinf(p) else f"p = {p}")
    ax.set(xlabel="First coordinate", ylabel="Second coordinate", aspect="equal", title="Unnormalized norm: expanding unit balls")
    ax.legend(fontsize=10, loc="center", handlelength=3.5)
    _save(fig, output, "finite-moment-norms.svg")
    print("All plotted values finite; no clipped or omitted observations.")


if __name__ == "__main__":
    main()
