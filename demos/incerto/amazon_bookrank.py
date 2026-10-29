"""Reproduce static amazon-bookrank figures; run from the installed repository.

Adapted from incerto-wiki 9717c9cf83aee18b47f423a14bce2f0d14bb8bcb, content/concepts/examples/amazon-bookrank.md.
Copyright (c) 2023 xshi19; MIT (see THIRD_PARTY_NOTICES.md).
No network access or notebook execution is required.
"""
from pathlib import Path
import os
import matplotlib
matplotlib.use("Agg")
OUTPUT = Path(os.environ.get("INCERTO_FIGURE_DIR",
    Path(__file__).resolve().parents[2] / "assets/incerto/figures"))
OUTPUT.mkdir(parents=True, exist_ok=True)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

from xmath.incerto.datasets import load_amazon_bookrank
from xmath.incerto.estimators import hill_alpha_estimator, hill_stability
from xmath.incerto.figures import COLORS, savefig, set_theme, style_axes, vertical_figure

set_theme(scale=1.1)

data = load_amazon_bookrank()
sales = data.weekly_sales
ranks = data.weekly_average_rank

mask = (sales > 0) & (ranks > 0)
log_rank = np.log(ranks[mask])
log_sales = np.log(sales[mask])
slope, intercept, r_value, _, _ = linregress(log_rank, log_sales)

positive_sales = np.sort(sales[sales > 0])
sales_positions = 1 - np.arange(1, positive_sales.size + 1) / (positive_sales.size + 1)

tail_sample = sales[sales > 10]
k_max = max(6, min(140, tail_sample.size - 1))
ks = np.unique(np.geomspace(5, k_max, 60).astype(int))
stability = hill_stability(tail_sample, ks)

fig, axes = vertical_figure(3, panel_height=3.2)
fig.get_layout_engine().set(hspace=.13)

axes[0].scatter(ranks, sales, s=14, alpha=0.65, color=COLORS["accent"])
rank_grid = np.geomspace(ranks.min(), ranks.max(), 150)
axes[0].plot(
    rank_grid,
    np.exp(intercept) * rank_grid**slope,
    color=COLORS["umber"],
    ls="--",
    label=f"log-log slope {slope:.2f}",
)
axes[0].set_xscale("log")
axes[0].set_yscale("log")
axes[0].set_xlabel("weekly average rank")
axes[0].set_ylabel("weekly sales")
axes[0].set_title("Sales-rank relation")
axes[0].legend()

axes[1].loglog(positive_sales, sales_positions, color=COLORS["teal"])
axes[1].set_xlabel("weekly sales")
axes[1].set_ylabel("rank plotting position")
axes[1].set_title("Sales tail: rank positions")

axes[2].semilogx(stability["k"], stability["alpha"], color=COLORS["green"])
axes[2].set_xlabel("upper order statistics k")
axes[2].set_ylabel(r"Hill $\widehat\alpha$")
axes[2].set_title("Tail sensitivity")

style_axes(axes, grid_axis="both")
savefig(fig, OUTPUT / "amazon-bookrank-1.svg", metadata={"Date": None})
plt.close()

print(f"Rows: {sales.size}; titles dated from {data.date.min()} to {data.date.max()}")
print(f"Log-log rank/sales R^2: {r_value**2:.3f}")
for k in [10, 20, 40, 80, 120]:
    if k < tail_sample.size:
        print(f"Hill alpha on sales > 10 for k={k:3d}: {hill_alpha_estimator(tail_sample, k):.2f}")

# Keep Matplotlib's SVG path continuations clean in source control.
for output in OUTPUT.glob("amazon-bookrank-*.svg"):
    output.write_text("\n".join(line.rstrip() for line in output.read_text().splitlines()) + "\n")
