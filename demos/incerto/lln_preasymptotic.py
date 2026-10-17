"""Reproduce static lln-preasymptotic figures; run from the installed repository.

Adapted from incerto-wiki 9717c9cf83aee18b47f423a14bce2f0d14bb8bcb, content/concepts/examples/lln-preasymptotic.md.
Copyright (c) 2023 xshi19; MIT (see THIRD_PARTY_NOTICES.md).
No network access or notebook execution is required.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "xshi-math-incerto"
OUTPUT = Path(__file__).resolve().parents[2] / "assets/incerto/figures"
OUTPUT.mkdir(parents=True, exist_ok=True)

import numpy as np
import matplotlib.pyplot as plt

from xmath.incerto.distributions import pareto_type1
from xmath.incerto.estimators import max_to_sum_ratio, running_mean
from xmath.incerto.figures import COLORS, FIGURE_SIZES, set_theme, style_axes

set_theme()

path_n = 300_000
checkpoints = np.unique(np.geomspace(10, path_n, 90).astype(int))
path_specs = [
    (0.8, 20260617, COLORS["brick"]),
    (1.0, 20260618, COLORS["umber"]),
    (1.3, 20260619, COLORS["green"]),
]

n_values = np.array([300, 1_000, 3_000, 10_000, 30_000])


def final_mean_quantiles(alpha, n, reps=300, batch=50, seed=20260617):
    rng = np.random.default_rng(seed)
    means = np.empty(reps)
    for start in range(0, reps, batch):
        stop = min(start + batch, reps)
        sample = pareto_type1.rvs(
            alpha,
            size=(stop - start, n),
            random_state=rng,
        )
        means[start:stop] = sample.mean(axis=1)
    return np.quantile(means, [0.10, 0.50, 0.90])


fig, axes = plt.subplots(1, 2, figsize=FIGURE_SIZES["two_panel"], layout="constrained")

for alpha, seed, color in path_specs:
    rng = np.random.default_rng(seed)
    sample = pareto_type1.rvs(alpha, size=path_n, random_state=rng)
    means = running_mean(sample)

    axes[0].loglog(
        checkpoints,
        means[checkpoints - 1],
        color=color,
        label=fr"$\alpha={alpha}$",
    )

    if alpha > 1:
        axes[0].axhline(alpha / (alpha - 1), color=color, ls="--", alpha=0.8)

    print(f"Pareto alpha={alpha}:")
    print(f"  final running mean after {path_n:,} draws: {float(means[-1]):.3f}")
    print(f"  largest observation's share of total: {float(max_to_sum_ratio(sample)):.3f}")
    if alpha > 1:
        print(f"  finite theoretical mean: {alpha / (alpha - 1):.3f}")
    else:
        print("  finite theoretical mean: none")

axes[0].set_xlabel("sample size n")
axes[0].set_ylabel("running mean")
axes[0].set_title("Single running-mean paths")
axes[0].legend()

for alpha, color in [(0.8, COLORS["brick"]), (1.3, COLORS["green"])]:
    qs = np.array(
        [
            final_mean_quantiles(alpha, n, seed=20260617 + int(100 * alpha) + n)
            for n in n_values
        ]
    )
    axes[1].fill_between(n_values, qs[:, 0], qs[:, 2], color=color, alpha=0.18)
    axes[1].plot(n_values, qs[:, 1], color=color, marker="o", label=fr"$\alpha={alpha}$ median")

axes[1].axhline(1.3 / (1.3 - 1), color=COLORS["green"], ls="--", alpha=0.8)
axes[1].set_xscale("log")
axes[1].set_yscale("log")
axes[1].set_xlabel("sample size n")
axes[1].set_ylabel("sample-mean quantiles")
axes[1].set_title("Repeated-simulation bands")
axes[1].legend()

style_axes(axes, grid_axis="both")
plt.savefig(OUTPUT / "lln-preasymptotic-1.svg", metadata={"Date": None})
plt.close()

# Keep Matplotlib's SVG path continuations clean in source control.
for output in OUTPUT.glob("lln-preasymptotic-*.svg"):
    output.write_text("\n".join(line.rstrip() for line in output.read_text().splitlines()) + "\n")
