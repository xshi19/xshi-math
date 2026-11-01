"""Three chapter-12 figures; synthetic models, no data or network access.

Run: uv run python demos/incerto/point_forecasts.py
PCG64 integer seeds and 2,000 replications; 17,720,000 total Pareto draws.
All realizations retained. The plotted bands are sampling quantiles, not CIs.
"""

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from xmath.incerto.calibration import pareto_tail_bet
from xmath.incerto.figures import COLORS, savefig, set_theme, vertical_figure
from xmath.incerto.forecasting import (
    bounded_to_dual, pareto_forecast_scores, stable_average_scale,
)
from xmath.incerto.limits import pareto_capped_mean


NAMES = ("point-forecast-scaling", "point-forecast-evaluation", "point-forecast-bounds")
SIZES = np.array([30, 100, 300, 1000, 3000])


def _export(fig, output, name):
    savefig(fig, output/f"{name}.svg")
    plt.close(fig)


def main(output=None):
    output = Path(output or Path(__file__).resolve().parents[2]/"assets/figures/incerto")
    output.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)
    fig, axes = vertical_figure(2, panel_height=3.5)
    ns = np.unique(np.geomspace(1, 10000, 120).astype(int))
    for alpha, style in ((.8, "-"), (1., "--"), (1.5, "-."), (2., ":")):
        axes[0].loglog(ns, [stable_average_scale(alpha, int(n)) for n in ns],
                       ls=style, label=f"α = {alpha:g}")
    axes[0].set(title="Stable averages · exact scales", xlabel="sample size n (log scale)",
                ylabel="scale / initial scale (log)")
    axes[0].legend(loc="lower left", ncol=2, fontsize=9)
    quantiles = []
    for i, n in enumerate(SIZES):
        means = pareto_forecast_scores(1.5, int(n), 3, seed=1200+i)["mean"]
        quantiles.append(np.quantile(n**(1/3)*(means-3), [.1, .5, .9]))
    low, middle, high = np.array(quantiles).T
    axes[1].fill_between(SIZES, low, high, color=COLORS["accent"], alpha=.16,
                         label="10th–90th sampling range")
    axes[1].plot(SIZES, middle, "o-", color=COLORS["accent"], label="sampling median")
    axes[1].axhline(0, color=COLORS["muted"], ls=":", lw=1)
    axes[1].set(xscale="log", title="Pareto α = 1.5 · rescaled mean error",
                xlabel="sample size n (log scale)", ylabel=r"$n^{1/3}(\bar X_n-3)$")
    axes[1].legend(loc="upper right", fontsize=9)
    _export(fig, output, NAMES[0])

    results = [pareto_forecast_scores(1.5, int(n), 2**(2/3), seed=1210+int(n))
               for n in SIZES]
    fig, axes = vertical_figure(3, panel_height=3.2)
    for ax, metric, title, color in zip(axes, ("absolute", "squared", "smape"),
            ("Absolute · finite mean, infinite variance", "Squared · infinite expected score",
             "sMAPE · bounded score"), (COLORS["accent"], COLORS["brick"], COLORS["green"])):
        low, middle, high = np.array([np.quantile(row[metric], [.1, .5, .9])
                                      for row in results]).T
        ax.fill_between(SIZES, low, high, color=color, alpha=.16)
        ax.plot(SIZES, middle, "o-", color=color, label="median; band: 10th–90th")
        ax.set(xscale="log", xlabel="test sample size n (log scale)",
               ylabel="average score", title=title)
        if metric != "smape":
            ax.set(yscale="log", ylabel="average score (log scale)")
        if metric == "absolute":
            d = 2**(2/3)
            exact = d-3+2*pareto_tail_bet(1.5, d)["excess_mean"]
            ax.axhline(exact, color=color, ls="--", label="exact expected score")
        ax.legend(loc="upper right", fontsize=8.5)
    _export(fig, output, NAMES[1])

    fig, axes = vertical_figure(2, panel_height=3.5)
    x = np.linspace(0, .995, 401)
    axes[0].plot(x, bounded_to_dual(x, upper=1), color=COLORS["accent"], label="dual transform")
    axes[0].plot(x, x, color=COLORS["muted"], ls="--", label="identity")
    axes[0].set(title="Removing a finite endpoint", xlabel="fraction of cap X / H",
                ylabel="dual coordinate Z / H", xlim=(0, 1), ylim=(0, 5.5))
    axes[0].legend(loc="upper left")
    caps = np.geomspace(20, 1e5, 200)
    for alpha, style in ((.6, "-"), (.8, "--"), (1.2, "-.")):
        xm = 2*2**(-1/alpha)
        excess = (pareto_capped_mean(caps, alpha, x_m=xm)
                  - pareto_capped_mean(10, alpha, x_m=xm))
        axes[1].loglog(caps, excess, ls=style, label=f"α = {alpha:g}")
    axes[1].set(title="Same median 2 · different tail harm", xlabel="cap H (log scale)",
                ylabel="expected excess above 10 (log)")
    axes[1].legend(loc="upper left")
    _export(fig, output, NAMES[2])
    print(f"Exported {len(NAMES)} synthetic figures; no observations removed.")
    return list(NAMES)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    main(parser.parse_args().output)
