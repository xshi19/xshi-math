"""Reproduce static dispersion-ratio figures; run from the installed repository.

Adapted from incerto-wiki 9717c9cf83aee18b47f423a14bce2f0d14bb8bcb, content/concepts/examples/dispersion-ratio.md.
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
from xmath.incerto.figures import FIGURE_SIZES, set_theme, style_axes
from xmath.incerto.stats import mean_absolute_deviation, median_absolute_deviation

set_theme()


def dispersion_ratios(sample):
    std = np.std(sample)
    mean_ad = mean_absolute_deviation(sample)
    median_ad = median_absolute_deviation(sample)
    median_ratio = np.inf if median_ad == 0 else std / median_ad
    return std / mean_ad, median_ratio


def ratio_quantiles(draw, n, reps=240, seed=20260617):
    rng = np.random.default_rng(seed)
    ratios = np.empty((reps, 2))
    for i in range(reps):
        ratios[i] = dispersion_ratios(draw(rng, n))
    return np.quantile(ratios, [0.5, 0.9], axis=0)


draws = {
    "normal": lambda rng, n: rng.normal(size=n),
    "student-t(3)": lambda rng, n: rng.standard_t(df=3, size=n),
    "Pareto(1.5)": lambda rng, n: pareto_type1.rvs(1.5, size=n, random_state=rng),
}

n_values = np.array([200, 1_000, 5_000, 20_000])
results = {
    name: np.array(
        [ratio_quantiles(draw, n, seed=20260617 + i * 100 + n) for i, n in enumerate(n_values)]
    )
    for name, draw in draws.items()
}

fig, axes = plt.subplots(1, 2, figsize=FIGURE_SIZES["two_panel"], layout="constrained")

for name, qs in results.items():
    axes[0].plot(n_values, qs[:, 0, 0], marker="o", label=name)
    axes[1].plot(n_values, qs[:, 0, 1], marker="o", label=name)

axes[0].axhline(1.0, color="black", linestyle="--", linewidth=1.1)
axes[0].set_xscale("log")
axes[0].set_xlabel("sample size n")
axes[0].set_ylabel("median Std/MeanAD")
axes[0].set_title("Mean absolute deviation ratio")
axes[0].legend()

axes[1].axhline(1.0, color="black", linestyle="--", linewidth=1.1)
axes[1].set_xscale("log")
axes[1].set_xlabel("sample size n")
axes[1].set_ylabel("median Std/MedianAD")
axes[1].set_title("Median absolute deviation ratio")
axes[1].legend()

style_axes(axes, grid_axis="both")
plt.savefig(OUTPUT / "dispersion-ratio-1.svg", metadata={"Date": None})
plt.close()
for name, qs in results.items():
    for n, q in zip(n_values, qs):
        print(f"{name}; n={n}; median Std/MeanAD={q[0,0]:.3f}; median Std/MedianAD={q[0,1]:.3f}")


# Keep Matplotlib's SVG path continuations clean in source control.
for output in OUTPUT.glob("dispersion-ratio-*.svg"):
    output.write_text("\n".join(line.rstrip() for line in output.read_text().splitlines()) + "\n")
