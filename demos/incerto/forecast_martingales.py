"""Three chapter-14 figures from exact models and synthetic paths.

Run: uv run python demos/incerto/forecast_martingales.py
PCG64 seeds 1402/1403; 4*100 + 10000*40 = 400400 normal draws.
"""

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from xmath.incerto.figures import COLORS, COLOR_CYCLE, savefig, set_theme, vertical_figure
from xmath.incerto.martingales import (
    gaussian_binary_probability, probit_binary_probability,
    simulate_probit_forecasts, forecast_revision_summary,
)


NAMES = ("forecast-uncertainty", "forecast-dual-paths", "forecast-revision-budget")


def _export(fig, output, name):
    savefig(fig, output / f"{name}.svg")
    plt.close(fig)


def main(output=None):
    output = Path(output or Path(__file__).resolve().parents[2] / "assets/figures/incerto")
    output.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)

    fig, axes = vertical_figure(2, panel_height=3.5)
    normal_scale = np.linspace(.005, .4, 220)
    latent_scale = np.linspace(.03, 3, 220)
    for share, color in ((.46, COLORS["brick"]), (.54, COLORS["accent"])):
        axes[0].plot(normal_scale,
                     [gaussian_binary_probability(share, s, 1) for s in normal_scale],
                     color=color, label=f"current level {share:.2f}")
        axes[1].plot(latent_scale,
                     [probit_binary_probability(share, s, 1) for s in latent_scale],
                     color=color, label=f"current share {share:.2f}")
        axes[1].axhline(share, ls="--", lw=1.1, color=color)
    axes[0].axhline(.5, ls="--", color=COLORS["muted"], lw=1.1)
    axes[0].set(title="Gaussian terminal uncertainty", xlabel="remaining standard deviation s",
                ylabel="event probability", ylim=(-.02, 1.02))
    axes[1].set(title="Bounded probit martingale", xlabel=r"latent noise $\sigma\sqrt{\tau}$",
                ylabel="event probability", ylim=(-.02, 1.02))
    for ax in axes:
        ax.legend(loc="upper right", fontsize=9)
    _export(fig, output, NAMES[0])

    sample = simulate_probit_forecasts(.54, .8, 1, steps=100, paths=4, seed=1402)
    fig, axes = vertical_figure(3, panel_height=3)
    for row in range(4):
        for ax, key in zip(axes, ("latent", "share", "probability")):
            ax.plot(sample["time"], sample[key][row], color=COLOR_CYCLE[row],
                    lw=1.5, label=f"path {row+1}")
    axes[0].set(title="Unbounded coordinate", ylabel="latent Z")
    axes[0].legend(loc="lower left", ncol=2, fontsize=8.5)
    axes[1].set(title="Bounded share · martingale", ylabel="share Y", ylim=(-.03, 1.03))
    axes[2].set(title="Event probability · martingale", ylabel="probability p", ylim=(-.03, 1.03))
    for ax in axes:
        ax.set(xlabel="elapsed time", xlim=(0, 1))
    _export(fig, output, NAMES[1])

    sample = simulate_probit_forecasts(.54, .8, 1, steps=40, paths=10000, seed=1403)
    proper = sample["probability"]
    altered = proper.copy()
    altered[:, 1:-1] = np.clip(altered[:, 1:-1] + .12*(-1.)**np.arange(1, 40), 0, 1)
    fig, axes = vertical_figure(2, panel_height=3.5)
    reports = []
    for paths, label, color, style in ((proper, "conditional probability", COLORS["accent"], "-"),
                                      (altered, "alternating ±0.12", COLORS["brick"], "--")):
        summary = forecast_revision_summary(paths)
        reports.append(summary)
        energy = np.c_[np.zeros(paths.shape[0]), np.cumsum(np.diff(paths, axis=1)**2, axis=1)]
        budget = summary["initial_budget"]
        axes[0].plot(sample["time"], energy.mean(axis=0)/budget, color=color, ls=style, label=label)
        axes[0].errorbar(1, summary["squared_revision"]/budget,
                         yerr=2*summary["squared_revision_se"]/budget,
                         color=color, fmt="o", capsize=4)
        axes[1].plot(sample["time"], summary["brier"], color=color, ls=style, label=label)
    axes[0].axhline(1, color=COLORS["muted"], ls=":", label="expected full budget")
    axes[0].set(title="Accumulated squared revisions", ylabel="mean revisions / initial budget")
    axes[0].legend(loc="upper left", fontsize=8.5)
    axes[1].set(title="Brier score on the same outcomes", ylabel="mean squared forecast error")
    axes[1].legend(loc="upper right", fontsize=8.5)
    for ax in axes:
        ax.set(xlabel="elapsed time", xlim=(0, 1.03), ylim=(0, None))
    _export(fig, output, NAMES[2])
    for label, result in zip(("coherent", "altered"), reports):
        print(f"{label}: revision gap={result['budget_gap']:.4f}, SE={result['budget_gap_se']:.4f}")
    exceeding = np.count_nonzero(np.sum(np.diff(proper)**2, axis=1) > reports[0]["initial_budget"])
    print(f"Coherent paths exceeding expected budget: {exceeding}/10000")
    print(f"Exported {len(NAMES)} figures; 400400 normal draws, all paths retained.")
    return list(NAMES)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    main(parser.parse_args().output)
