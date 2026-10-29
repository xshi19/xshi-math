"""Chapter 7 and P2 ranks 12/15: bounded, untruncated sampling experiments.

Run: uv run python demos/incerto/limit_distributions.py
PCG64 streams 20261071..74, 20261080..82 and 20261180..82; no external data. At most
10,000 observations per path; repeated sums in batches of 32. All nonfinite
draws/results raise. Bands are pointwise sampling percentiles, not CIs.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import cauchy

from xmath.incerto.distributions import pareto_type1
from xmath.incerto.estimators import running_mean
from xmath.incerto.figures import COLORS, savefig, set_theme, vertical_figure
from xmath.incerto.limits import pareto_capped_mean, repeated_centered_sums


def finish(fig, output, name):
    for ax in fig.axes:
        if ax.get_legend_handles_labels()[1]:
            ax.legend(loc="upper center", bbox_to_anchor=(.5, -.24), ncol=2,
                      handlelength=2.8, columnspacing=1)
    savefig(fig, output / name)
    plt.close(fig)


def band(ax, n, samples, label, color):
    low, median, high = np.quantile(samples, [.1, .5, .9], axis=1)
    ax.fill_between(n, low, high, color=color, alpha=.16)
    ax.plot(n, median, "o-", color=color, label=label)
    return low, median, high


def main(output=None):
    output = Path(output) if output is not None else Path(__file__).resolve().parents[2] / "assets/figures/incerto"
    output.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)

    fig, axes = vertical_figure(2, panel_height=3.7)
    rng = np.random.default_rng(20261071)
    for index in range(3):
        sample = rng.standard_cauchy(10_000)
        means = running_mean(sample)
        if not np.all(np.isfinite(means)):
            raise FloatingPointError("nonfinite Cauchy path")
        axes[0].plot(np.arange(1, len(sample)+1), means, lw=1, label=f"Path {index+1}")
    axes[0].set(xscale="log", yscale="symlog", xlabel="Prefix length n", ylabel="Running mean",
                title="Cauchy means keep jumping")
    n = np.array([10, 30, 100, 1000, 10_000])
    rng = np.random.default_rng(20261072)
    means, medians = [], []
    for size in n:
        # 600 repetitions, <= 32 by 10,000 values held per batch.
        mean_row, median_row = [], []
        for start in range(0, 600, 32):
            x = rng.standard_cauchy((min(32, 600-start), size))
            mean_row.extend(x.mean(axis=1))
            median_row.extend(np.median(x, axis=1))
        means.append(mean_row)
        medians.append(median_row)
    if not np.all(np.isfinite([means, medians])):
        raise FloatingPointError("nonfinite Cauchy statistics")
    band(axes[1], n, means, "Mean: 10–90%", COLORS["accent"])
    band(axes[1], n, medians, "Median: 10–90%", COLORS["green"])
    for i, p in enumerate((.1, .9)):
        axes[1].axhline(cauchy.ppf(p), color=COLORS["muted"], ls="--", lw=1,
                        label="Exact mean quantiles" if i == 0 else None)
    axes[1].set(xscale="log", xlabel="Sample size n", ylabel="Sampling quantiles",
                title="A median can concentrate")
    finish(fig, output, "cauchy-running.svg")

    fig, axes = vertical_figure(2, panel_height=3.7)
    n = np.array([30, 100, 300, 1000, 3000])
    for alpha, seed, color in ((.8, 20261080, COLORS["brick"]),
                                (1., 20261081, COLORS["umber"]),
                                (1.3, 20261082, COLORS["green"])):
        law = pareto_type1(alpha)
        sample = law.rvs(size=10_000, random_state=np.random.default_rng(seed))
        axes[0].plot(np.arange(1, 10_001), running_mean(sample), color=color, lw=1,
                     label=f"α = {alpha:g}")
        sums = repeated_centered_sums(law, n, repetitions=600, random_state=seed+100)
        band(axes[1], n, sums/n[:, None], f"α = {alpha:g}", color)
    for ax in axes:
        ax.axhline(13/3, color=COLORS["green"], ls="--", lw=1, label="Mean for α = 1.3")
        ax.set(xscale="log", yscale="log", xlabel="Sample size n", ylabel="Mean (log scale)")
    axes[0].set_title("Pareto means · all 10,000 prefixes")
    axes[1].set_title("600 samples per size · 10–90%")
    finish(fig, output, "lln-failure-paths.svg")

    fig, axes = vertical_figure(1, panel_height=3.8)
    caps = np.geomspace(1, 1e7, 301)
    for alpha, color, style in ((.8, COLORS["brick"], "-"), (1, COLORS["umber"], "--"),
                                 (1.3, COLORS["green"], "-.")):
        axes[0].plot(caps, pareto_capped_mean(caps, alpha), style, color=color, label=f"α = {alpha:g}")
    axes[0].axhline(13/3, color=COLORS["green"], ls=":", lw=1, label="Finite limit for α = 1.3")
    axes[0].set(xscale="log", yscale="log", xlabel="Cap c", ylabel="E[min(X, c)]",
                title="Population capped means · minimum 1")
    finish(fig, output, "lln-capped-means.svg")

    n = np.array([30, 100, 300, 1000, 3000])
    sums = repeated_centered_sums(pareto_type1(1.5), n, center=3, repetitions=800,
                                  random_state=20261074)
    fig, axes = vertical_figure(2, panel_height=3.4)
    for ax, power, title, color in zip(axes, (2/3, .5),
            ("Pareto 1.5 · stable normalization", "The same sums · square-root normalization"),
            (COLORS["accent"], COLORS["brick"])):
        normalized = sums/n[:, None]**power
        band(ax, n, normalized, "Median and 10–90%", color)
        ax.set(xscale="log", xlabel="Sample size n", ylabel="Centered, normalized sum", title=title)
    finish(fig, output, "generalized-clt.svg")
    stable_iqr = np.diff(np.quantile(sums/n[:, None]**(2/3), [.25, .75], axis=1), axis=0)[0]
    print("Stable-scale IQR: " + ", ".join(f"{v:.4g}" for v in stable_iqr))

    rng = np.random.default_rng(20261073)
    increments = np.log(rng.choice([1.5, .6], size=(800, 200)))
    log_wealth = np.column_stack([np.zeros(800), np.cumsum(increments, axis=1)])
    n = np.arange(201)
    fig, axes = vertical_figure(1, panel_height=4.3)
    ax = axes[0]
    for i in range(4):
        ax.plot(n, log_wealth[i], color=COLORS["muted"], lw=.7, alpha=.6,
                 label="Four paths" if i == 0 else None)
    band(ax, n, log_wealth.T, "Median and 10–90%", COLORS["accent"])
    ax.plot(n, n*np.log(1.05), "--", color=COLORS["green"], label="log E[wealth]")
    ax.plot(n, n*.5*np.log(.9), "-.", color=COLORS["brick"], label="E[log wealth]")
    ax.set(xlabel="Number of steps n", ylabel="Log wealth", title="Two population targets · 1.5 or 0.6")
    finish(fig, output, "ergodicity-growth.svg")
    print("Exported 5 figures; no draws clipped or removed.")


if __name__ == "__main__":
    main()
