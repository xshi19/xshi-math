"""P1 Hill, mean-excess and coordinated threshold diagnostics.

Run: uv run python demos/incerto/tail_estimation.py
PCG64 seeds 20261020..20261023, n=30000 per law. One mixture sample is reused
for Hill, the two threshold figures and PP checks. Body U[1,3] (82%),
tail Pareto(alpha=1.7, minimum=3) (18%). No clipping or external data. At most
40 GPD fits, each capped at 2000 iterations / 4000 evaluations. Finite-sample
plots are diagnostics, not threshold-selection rules. Runtime: seconds.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import numpy as np

from xmath.incerto.distributions import generalized_pareto, pareto_type1
from xmath.incerto.estimators import gpd_threshold_fit, hill_stability, mean_excess
from xmath.incerto.figures import COLORS, savefig, set_theme, vertical_figure
from xmath.incerto.stats import empirical_survival_function

N, ALPHA, MIN_COUNT = 30_000, 1.7, 50


def synthetic_samples():
    """Fixed independent exact-Pareto and body/tail samples shared by the plots."""
    exact = pareto_type1.rvs(ALPHA, size=N, random_state=np.random.default_rng(20261020))
    rng = np.random.default_rng(20261021)
    tail = rng.random(N) < .18
    mixture = rng.uniform(1, 3, N)
    mixture[tail] = pareto_type1.rvs(ALPHA, scale=3, size=tail.sum(), random_state=rng)
    return exact, mixture


def mixture_survival(u):
    """The page's specified population survival, evaluated without fitting."""
    u = np.asarray(u, dtype=float)
    result = np.ones_like(u)
    body, tail = (u >= 1) & (u < 3), u >= 3
    result[body] = .82 * (3-u[body])/2 + .18
    result[tail] = .18 * (3/u[tail])**ALPHA
    return result


def finish(fig, output, name):
    for ax in fig.axes:
        if ax.get_legend_handles_labels()[1]:
            ax.legend(loc="upper center", bbox_to_anchor=(.5, -.27), handlelength=3)
    savefig(fig, output / name)
    plt.close(fig)


def main(output=None):
    output = Path(output) if output is not None else Path(__file__).resolve().parents[2] / "assets/figures/incerto"
    output.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)
    exact, mixture = synthetic_samples()
    ks = np.unique(np.geomspace(5, 24000, 170).astype(int))
    fig, axes = vertical_figure(3)
    for ax, sample, title in zip(axes[:2], (exact, mixture), ("Exact Pareto · minimum 1", "Uniform body + Pareto tail")):
        h = hill_stability(sample, ks)
        ax.plot(ks, h["xi"], label="Hill estimate")
        ax.axhline(1/ALPHA, color=COLORS["umber"], linestyle="--", label="Known ξ = 1/1.7")
        ax.set(xscale="log", xlabel="Retained order-statistic count k", ylabel="Extreme-value index ξ",
               title=title)
    tail_count = int(np.count_nonzero(mixture > 3))
    axes[1].axvline(tail_count, color=COLORS["muted"], linestyle=":", label=f"Above known join: {tail_count}")
    for sample, label, style in ((exact, "Exact Pareto", "-"), (mixture, "Body + tail", "--")):
        thresholds = np.sort(sample)[::-1][ks]
        axes[2].plot(ks, thresholds, style, label=label)
        # Continuous synthetic draws have no ties: strict counts equal k.
        assert np.array_equal([np.count_nonzero(sample > u) for u in thresholds], ks)
    axes[2].axhline(3, color=COLORS["muted"], linestyle=":", label="Mixture join u = 3")
    axes[2].set(xscale="log", yscale="log", xlabel="Retained order-statistic count k",
                ylabel="Observed threshold u", title="Thresholds corresponding to k")
    finish(fig, output, "hill-stability.svg")

    exponential = np.random.default_rng(20261022).exponential(size=N)
    uniform = np.random.default_rng(20261023).uniform(0, 5, N)
    cases = [
        (exact, np.geomspace(1, 90, 150), lambda u: u/(ALPHA-1), "Pareto α = 1.7", COLORS["accent"]),
        (exponential, np.linspace(0, 9, 150), lambda u: np.ones_like(u), "Exponential · mean 1", COLORS["green"]),
        (uniform, np.linspace(0, 5, 150), lambda u: (5-u)/2, "Uniform on [0, 5]", COLORS["umber"]),
    ]
    fig, axes = vertical_figure(6, panel_height=3.2)
    for index, (sample, u, population, title, color) in enumerate(cases):
        stats = mean_excess(sample, u, min_exceedances=MIN_COUNT)
        ax, count_ax = axes[2*index:2*index+2]
        valid_population = u < 5 if index == 2 else np.ones(u.size, dtype=bool)
        ax.plot(u[valid_population], population(u[valid_population]), "--", color=COLORS["ink"], label="Population")
        ax.plot(u, stats["mean_excess"], color=color, label="Sample · count ≥ 50")
        ax.set(title=title, xlabel="Threshold u", ylabel="Mean excess")
        count_ax.plot(u, stats["exceedances"], color=color, label="Strict exceedances")
        count_ax.axhline(MIN_COUNT, color=COLORS["ink"], linestyle="--", label="Mask below 50")
        count_ax.fill_between(u, 0, 1, where=stats["exceedances"] < MIN_COUNT,
                              transform=count_ax.get_xaxis_transform(), color=COLORS["sand"], alpha=.7)
        count_ax.set(xlabel="Threshold u", ylabel="Count", yscale="symlog", ylim=(0, N*1.1),
                     title="Counts retained even when estimates stop")
        if index == 0:
            ax.set_title("Pareto α = 1.7\nFor α ≤ 1: population e(u) = ∞ (not drawn)")
        if index == 2:
            for target in (ax, count_ax):
                target.axvline(5, color=COLORS["muted"], linestyle=":")
    finish(fig, output, "mean-excess.svg")

    # Use observed thresholds, so Hill's baseline and strict counts coincide.
    ordered = np.sort(mixture)
    targets = np.unique(np.r_[np.geomspace(1.5, 70, 32), 3, 6, 12])
    u = ordered[np.searchsorted(ordered, targets)]
    counts = N - np.searchsorted(ordered, u, side="right")
    hill = hill_stability(mixture, counts)["xi"]
    means = mean_excess(mixture, u, min_exceedances=MIN_COUNT)
    fits = [gpd_threshold_fit(mixture, t, min_exceedances=MIN_COUNT) for t in u]
    valid = counts >= MIN_COUNT
    shape = np.array([f["xi"] for f in fits])
    modified = np.array([f["modified_scale"] for f in fits])
    first, top = vertical_figure(3, panel_height=3.0)
    second, bottom = vertical_figure(3, panel_height=3.0)
    axes = np.r_[top, bottom]
    support, survival = empirical_survival_function(mixture)
    positive = survival > 0  # the sample maximum's strict survival is exactly zero
    axes[0].step(support[positive], survival[positive], where="post", label="Strict empirical survival")
    grid = np.geomspace(u[0], u[-1], 401)
    axes[0].plot(grid, mixture_survival(grid), "--", color=COLORS["ink"], label="Known mixture survival")
    axes[0].set(yscale="log", ylabel="Survival", title="One body/tail sample · n = 30,000")
    axes[1].plot(u, np.where(valid, hill, np.nan), label="Hill estimate")
    axes[1].plot(u[u >= 3], np.full(np.count_nonzero(u >= 3), 1/ALPHA), "--",
                 color=COLORS["ink"], label="Tail target 1/1.7 (u ≥ 3)")
    axes[1].set(ylabel="Hill ξ", title="Order-statistic thresholds")
    axes[2].plot(u, means["mean_excess"], label="Empirical mean excess")
    axes[2].plot(u[u >= 3], u[u >= 3]/(ALPHA-1), "--", color=COLORS["ink"], label="Tail target u/0.7 (u ≥ 3)")
    axes[2].set(ylabel="Mean excess", title="A mean sensitive to extreme draws")
    axes[3].plot(u, shape, "o-", label="Fitted GPD shape")
    axes[3].plot(u[u >= 3], np.full(np.count_nonzero(u >= 3), 1/ALPHA), "--", color=COLORS["ink"], label="Tail target 1/1.7 (u ≥ 3)")
    axes[3].set(ylabel="GPD ξ", title="Zero-location excess fits")
    axes[4].plot(u, modified, "o-", label="Fitted β(u) − ξu")
    axes[4].plot(u[u >= 3], np.zeros(np.count_nonzero(u >= 3)), "--", color=COLORS["ink"], label="Tail target 0 (u ≥ 3)")
    axes[4].set(ylabel="Modified scale", title="Inspect scale together with shape")
    axes[5].plot(u, counts, "o-", label="Strict exceedance count")
    axes[5].axhline(MIN_COUNT, color=COLORS["ink"], linestyle="--", label="Mask below 50")
    failed = np.array([not f["success"] and f["count"] >= MIN_COUNT for f in fits])
    if np.any(failed):
        axes[5].scatter(u[failed], counts[failed], marker="x", color=COLORS["brick"], label="Failed GPD fit")
    status = (f"{int(failed.sum())} eligible GPD fits failed" if failed.any()
              else "All eligible GPD fits succeeded")
    axes[5].set(ylabel="Count", yscale="log", title="Exceedance counts\n" + status)
    for ax in axes:
        ax.axvline(3, color=COLORS["muted"], linestyle=":")
        ax.set(xscale="log", xlim=(u[0], u[-1]), xlabel="Observed threshold u (log scale)")
        ax.set_xticks([2, 3, 6, 12, 24, 48], labels=["2", "3", "6", "12", "24", "48"])
        ax.xaxis.set_minor_formatter(NullFormatter())
        ax.fill_between(u, 0, 1, where=~valid, transform=ax.get_xaxis_transform(), color=COLORS["sand"], alpha=.5)
    finish(first, output, "threshold-diagnostics.svg")
    finish(second, output, "threshold-gpd.svg")

    fig, axes = vertical_figure(3, panel_height=3.6)
    for ax, threshold in zip(axes, (2, 3, 12)):
        fit = gpd_threshold_fit(mixture, threshold, min_exceedances=MIN_COUNT)
        excesses = np.sort(mixture[mixture > threshold]-threshold)
        count = len(excesses)
        ax.plot([0, 1], [0, 1], "--", color=COLORS["ink"], label="Identity")
        if fit["success"]:
            p = generalized_pareto(fit["xi"], fit["beta"]).cdf(excesses)
            # All observations retained; i/(m+1) are plotting positions, not strict survival.
            ax.plot(p, np.arange(1, count+1)/(count+1), label="Fitted excesses")
        else:
            ax.text(.05, .6, fit["status"], transform=ax.transAxes, wrap=True)
        ax.set(title=f"Threshold u = {threshold} · {count:,} excesses",
               xlabel="Fitted GPD CDF", ylabel="Empirical plotting position",
               xlim=(0, 1), ylim=(0, 1))
        print(f"PP u={threshold}: count={count}, status={fit['status']}, xi={fit['xi']:.4g}, beta={fit['beta']:.4g}")
    finish(fig, output, "threshold-pp.svg")
    print(f"Mixture seed 20261021: {tail_count} draws above 3; {sum(not f['success'] for f in fits)} masked/failed fits.")


if __name__ == "__main__":
    main()
