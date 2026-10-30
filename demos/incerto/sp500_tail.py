"""Run local S&P loss diagnostics and export only derived tail curves.

Adapted from incerto-wiki at 9717c9cf83aee18b47f423a14bce2f0d14bb8bcb.
Copyright (c) 2023 xshi19; MIT (see THIRD_PARTY_NOTICES.md).
"""
import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from xmath.incerto.datasets import DatasetNotAvailable, load_sp500_prices
from xmath.incerto.estimators import hill_alpha_estimator, mean_excess
from xmath.incerto.figures import COLORS, savefig, set_theme, vertical_figure


def observed_figure(prices, output):
    """Fixed-grid tail summaries; no raw prices or full sorted-return export."""
    _, returns = prices.log_returns()
    losses = -returns[returns < 0]
    if len(losses) < 50:
        raise ValueError("at least 50 loss days are required for the tail figure")
    fig, axes = vertical_figure(3, panel_height=3.4)
    fig.get_layout_engine().set(hspace=.13)
    grid = np.geomspace(.001, .30, 80)
    for values, label, color in ((returns[returns > 0], "gains", COLORS["green"]),
                                  (losses, "losses", COLORS["brick"])):
        if not len(values):
            continue
        survival = np.array([np.mean(values > u) for u in grid])
        keep = survival > 0
        axes[0].loglog(100 * grid[keep], survival[keep], label=label, color=color)
    axes[0].set(xlabel="threshold (% log change)", ylabel="fraction above threshold",
                title="Strict survival, conditional on sign")
    axes[0].legend()
    ks = np.unique(np.geomspace(25, max(26, int(.2 * len(losses))), 100).astype(int))
    axes[1].plot(ks, [hill_alpha_estimator(losses, int(k)) for k in ks], color=COLORS["brick"])
    axes[1].set(xlabel="retained loss count k", ylabel="Hill exponent alpha",
                title="Loss-tail threshold sensitivity", xscale="log")
    axes[1].set_xticks([25, 100, 400, 2000], labels=["25", "100", "400", "2000"])
    result = mean_excess(losses, np.quantile(losses, np.linspace(.8, .98, 30)), min_exceedances=5)
    axes[2].plot(100 * result["threshold"], 100 * result["mean_excess"], color=COLORS["brick"])
    selected = mean_excess(losses, np.quantile(losses, [.8, .9, .95]), min_exceedances=5)
    for u, excess, count in zip(selected["threshold"], selected["mean_excess"], selected["exceedances"]):
        axes[2].plot(100 * u, 100 * excess, "o", color=COLORS["brick"])
        axes[2].annotate(f"n={int(count)}", (100 * u, 100 * excess),
                         xytext=(0, 20), textcoords="offset points", fontsize=10)
    axes[2].set(xlabel="threshold (% log loss)", ylabel="mean excess (% log loss)",
                title="Loss mean excess and retained counts")
    axes[2].margins(y=.2)
    savefig(fig, output / "sp500-observed-tail.svg")
    plt.close(fig)


def main(output=None, *, end_date="2026-10-29"):
    try:
        prices = load_sp500_prices(fetch=False, end_date=end_date)
    except DatasetNotAvailable:
        print("No usable local S&P cache; import a dated price CSV with scripts/fetch_incerto_data.py.")
        return
    _, losses = prices.negative_log_returns()
    print(f"Return window: {prices.date[1]} to {prices.date[-1]}; {len(losses)} loss days")
    for k in (25, 50, 100, 200, 400):
        if k < len(losses):
            print(f"k={k}: Hill alpha={hill_alpha_estimator(losses, k):.2f}")
    if len(losses) >= 20:
        result = mean_excess(losses, np.quantile(losses, [0.8, 0.9, 0.95]), min_exceedances=5)
        for u, excess, count in zip(result["threshold"], result["mean_excess"], result["exceedances"]):
            print(f"threshold={100*u:.2f}% log, mean excess={100*excess:.2f}% log, exceedances={count:.0f}")
    if len(losses) >= 50:
        output = Path(output or Path(__file__).resolve().parents[2]/"assets/figures/incerto")
        output.mkdir(parents=True, exist_ok=True)
        set_theme(scale=1.1)
        observed_figure(prices, output)
        print("Generated derived observed tail figure; no raw prices or return series exported.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--end-date", default="2026-10-29")
    args = parser.parse_args()
    main(args.output, end_date=args.end_date)
