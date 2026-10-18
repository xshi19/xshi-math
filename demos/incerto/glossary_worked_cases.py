"""Bounded, deterministic SCoFT v4 chapter-2 examples; no RNG or external data.

Run: uv run python demos/incerto/glossary_worked_cases.py
Dimensionless fixed sample and exact model formulas. Two SVG exports; four
301-point maximum CDFs and one 161-point multiplier grid. A few seconds.
Mathematical infinite moments are printed; unexpected non-finite values fail.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from xmath import exceedance_fraction
from xmath.incerto.figures import COLORS, savefig, set_theme
from xmath.incerto.glossary import (
    pareto_normalized_maximum_cdf,
    pareto_tail_quantities,
)
from xmath.incerto.stats import empirical_survival_function
from xmath.incerto.tail_classes import log_survival_multiplier_ratio


def main() -> None:
    output = Path(__file__).resolve().parents[2] / "assets/figures/incerto"
    output.mkdir(parents=True, exist_ok=True)
    set_theme()
    metadata = {"Date": None, "Creator": "xshi-math glossary_worked_cases.py"}

    sample = np.array([1., 2., 2., 4.])
    support, survival = empirical_survival_function(sample)
    print("Fixed sample (1, 2, 2, 4): u, empirical CDF, strict survival, >= fraction")
    for u, strict in zip(support, survival):
        assert strict == exceedance_fraction(sample, u)
        print(f"{u:g}  {np.mean(sample <= u):.2f}  {strict:.2f}  {np.mean(sample >= u):.2f}")
    upper_half_mean = np.sort(sample)[2:].mean()
    strict_tail_mean = sample[sample > 2].mean()
    print(f"Upper-half quantile average: {upper_half_mean:g}; "
          f"conditional mean strictly above 2: {strict_tail_mean:g}")

    print("\nExact Pareto, x_m=1: alpha, u, log survival, mean excess, conditional mean, tail first moment")
    for alpha in (.8, 1., 1.5, 3.):
        for u in (1., 4., 16.):
            row = pareto_tail_quantities(alpha, 1., u)
            print(f"{alpha:g}  {u:g}  " + "  ".join(f"{v:.8g}" for v in row.values()))
    print("Infinity above is a population expectation, not arithmetic overflow.")

    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.0), layout="constrained")
    ax = axes[0]
    ax.step([0, *support, 5], [1, *survival, 0], where="post", color=COLORS["accent"])
    ax.scatter(support, survival, color=COLORS["accent"], zorder=3)
    before = np.array([1., .75, .25])
    ax.scatter(support, before, facecolors=COLORS["surface"],
               edgecolors=COLORS["accent"], zorder=3)
    ax.set(xlabel=r"Threshold $u$", ylabel=r"Strict empirical survival $\widehat S_4(u)$",
           title="Ties contribute one jump", ylim=(-.04, 1.04), xticks=range(6))
    ax = axes[1]
    y = np.linspace(.25, 4, 301)
    limit = np.exp(-y**-1.5)
    print("\nMaximum CDF comparisons, alpha=1.5: n, largest grid error from Frechet limit")
    for n, style in zip((1, 4, 16, 64), (":", "--", "-.", "-")):
        values = pareto_normalized_maximum_cdf(y, alpha=1.5, n=n)
        if not np.all(np.isfinite(values)):
            raise ValueError("non-finite maximum CDF")
        ax.plot(y, values, linestyle=style, label=f"n={n}")
        print(f"{n}  {np.max(np.abs(values - limit)):.8f}")
    ax.plot(y, limit, color=COLORS["ink"], linewidth=1.2, label="Frechet limit")
    ax.set(xlabel=r"Normalized maximum $y$", ylabel="CDF", title="Exact Pareto maxima",
           ylim=(0, 1))
    ax.legend(loc="lower right", fontsize=8)
    savefig(fig, output / "glossary-exceedances-maxima.svg", metadata=metadata)
    plt.close(fig)

    u = np.geomspace(1, 10_000, 161)
    # Valid survival: 1 below 1; u^-2 * (1 + log(u)) on this grid.
    log_sf = lambda x: -2 * np.log(x) + np.log1p(np.log(x))
    ratios = np.exp(log_survival_multiplier_ratio(log_sf, u))
    if not np.all(np.isfinite(ratios)):
        raise ValueError("non-finite multiplier ratio")
    fig, ax = plt.subplots(figsize=(6.6, 3.8), layout="constrained")
    ax.semilogx(u, ratios, color=COLORS["teal"], label="Log-corrected power tail")
    ax.axhline(.25, color=COLORS["brick"], linestyle="--", label="Exact Pareto, alpha=2")
    ax.set(xlabel=r"Threshold $u$", ylabel=r"$\bar F(2u)/\bar F(u)$",
           ylim=(.23, .44))
    ax.legend(loc="upper right")
    savefig(fig, output / "glossary-slow-variation.svg", metadata=metadata)
    plt.close(fig)
    # Matplotlib emits trailing spaces inside SVG paths; keep exports diff-clean.
    for name in ("glossary-exceedances-maxima.svg", "glossary-slow-variation.svg"):
        path = output / name
        path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines()) + "\n")
    print("\nLog-corrected multiplier ratios: u=1, 10, 100, 10000")
    print(np.exp(log_survival_multiplier_ratio(log_sf, [1, 10, 100, 10_000])))
    print("\nCDF-distance counterexample: j, uniform CDF gap, population mean")
    for j in (10, 100, 1000):
        print(f"{j}  {1 / j:g}  {j}")
    print("1204 finite maximum CDFs and 161 finite multiplier ratios; no omitted points.")
    print(f"Figures: {output}")


if __name__ == "__main__":
    main()
