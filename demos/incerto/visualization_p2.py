"""P2 ranks 11/13/14; ranks 12/15 share limit_distributions.py.

Run: uv run python demos/incerto/visualization_p2.py
Fixed event geometry and tied sample; checked convolution quadrature (81
thresholds, rtol=1e-9, maxlevel=12); 600 independent Pareto fits per size/law,
n=10/30/100/300, PCG64 seeds 20261090..92. No clipping or nonfinite removal.
"""

from pathlib import Path
import runpy

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Patch
import numpy as np

from xmath.incerto.distributions import pareto_type1
from xmath.incerto.estimators import pareto_mean_plugin
from xmath.incerto.figures import COLORS, savefig, set_theme, vertical_figure
from xmath.incerto.limits import pareto_plugin_nonfinite_probability
from xmath.incerto.stats import empirical_survival_function


def finish(fig, output, name):
    savefig(fig, output/name)
    plt.close(fig)


def main(output=None):
    output = Path(output) if output is not None else Path(__file__).resolve().parents[2]/"assets/figures/incerto"
    output.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)
    fig, axes = vertical_figure(1, panel_height=4.5)
    ax = axes[0]
    ax.add_patch(Polygon([(0, 1), (0, 1.4), (1.4, 1.4), (1.4, 0), (1, 0), (1, 1)],
                         facecolor=COLORS["green"], alpha=.25))
    ax.add_patch(Polygon([(0, 1), (1, 0), (1, 1)], facecolor=COLORS["gold"], alpha=.45))
    ax.plot([0, 1], [1, 0], "--", color=COLORS["ink"], label="Sum boundary")
    ax.axvline(1, ls=":", color=COLORS["muted"])
    ax.axhline(1, ls=":", color=COLORS["muted"])
    ax.text(.38, .82, "Sum > u\nmax ≤ u", ha="center")
    ax.text(1.16, .55, "Max\n> u", ha="center")
    ax.text(.3, .25, "Sum ≤ u", ha="center")
    ax.set(xlim=(0, 1.4), ylim=(0, 1.4), xlabel="First summand / u", ylabel="Second summand / u",
           title="Two nonnegative summands")
    ax.set_aspect("equal")
    ax.legend(handles=[Patch(facecolor=COLORS["green"], alpha=.25, label="Max exceeds u"),
                       Patch(facecolor=COLORS["gold"], alpha=.45, label="Residual sum event")],
               loc="upper center", bbox_to_anchor=(.5, -.24))
    finish(fig, output, "subexponential-geometry.svg")

    # One shared calculation/plotter also owns the chapter-5 convolution panel.
    producer = runpy.run_path(str(Path(__file__).with_name("power_laws.py")))
    fig, axes = vertical_figure(1, panel_height=3.8)
    producer["plot_convolution_ratio"](axes[0])
    axes[0].legend(loc="upper center", bbox_to_anchor=(.5, -.24), ncol=2, handlelength=3)
    finish(fig, output, "subexponential-convolution.svg")

    fig, axes = vertical_figure(2, panel_height=3.7)
    alpha_grid = np.geomspace(1.01, 4, 401)
    axes[0].plot(alpha_grid, alpha_grid/(alpha_grid-1), color=COLORS["accent"])
    axes[0].axvspan(.6, 1, color=COLORS["sand"])
    axes[0].axvline(1, color=COLORS["brick"], ls="--")
    axes[0].text(.62, 10, "Infinite\nmean", fontsize=10)
    axes[0].set(xlim=(.6, 4), yscale="log", xlabel="Fitted exponent", ylabel="Fitted mean (log scale)",
                title="The Pareto mean singularity · minimum 1")
    sizes = np.array([10, 30, 100, 300])
    for alpha, seed, color in ((.8, 20261090, COLORS["brick"]), (1, 20261091, COLORS["umber"]),
                                (1.5, 20261092, COLORS["green"])):
        rng = np.random.default_rng(seed)
        fractions = []
        for n in sizes:
            estimates = np.array([pareto_mean_plugin(pareto_type1.rvs(alpha, size=n, random_state=rng), x_m=1)
                                  for _ in range(600)])
            if np.any(np.isnan(estimates)) or np.any(np.isneginf(estimates)):
                raise FloatingPointError("unexpected plug-in failure")
            nonfinite = int(np.count_nonzero(np.isposinf(estimates)))
            fractions.append(nonfinite/600)
            print(f"alpha={alpha:g}, n={n}: finite={600-nonfinite}, infinite={nonfinite}")
        exact = [pareto_plugin_nonfinite_probability(alpha, int(n)) for n in sizes]
        axes[1].plot(sizes, exact, color=color, label=f"α = {alpha:g}")
        axes[1].scatter(sizes, fractions, color=color, marker="o", s=25)
    axes[1].set(xscale="log", ylim=(-.03, 1.03), xlabel="Sample size n", ylabel="Fraction of infinite estimates",
                title="Lines: exact · dots: 600 samples")
    axes[1].legend(loc="upper center", bbox_to_anchor=(.5, -.24), ncol=3)
    finish(fig, output, "plugin-mean-singularity.svg")

    fig, axes = vertical_figure(2, panel_height=3.0)
    support, survival = empirical_survival_function([1, 2, 2, 4])
    for ax, levels, start, label in ((axes[0], survival, 1, "Strict survival: fraction > u"),
                                    (axes[1], 1-survival, 0, "CDF: fraction ≤ u")):
        boundaries = np.r_[0, support, 5]
        heights = np.r_[start, levels]
        # Horizontal segments and endpoint markers; no vertical connector can
        # obscure which value is assigned at a tied observation.
        for i, level in enumerate(heights):
            ax.plot(boundaries[i:i+2], [level, level], color=COLORS["accent"])
        ax.scatter(support, np.r_[start, levels[:-1]], facecolors=COLORS["surface"],
                    edgecolors=COLORS["accent"], s=45, zorder=3)
        ax.scatter(support, levels, color=COLORS["accent"], s=24, zorder=4)
        ax.axvline(2, ls=":", color=COLORS["umber"])
        ax.annotate(f"u = 2: {levels[1]:g}", (2, levels[1]), xytext=(2.55, .5),
                     arrowprops={"arrowstyle": "->", "color": COLORS["muted"]})
        ax.set(xlim=(0, 5), ylim=(-.07, 1.07), xlabel="Threshold u", ylabel="Fraction", title=label)
        ax.set_yticks([0, .25, .5, .75, 1])
    finish(fig, output, "exceedances-ties.svg")
    print("Exported 4 figures; finite and infinite fits exhaust every sample.")


if __name__ == "__main__":
    main()
