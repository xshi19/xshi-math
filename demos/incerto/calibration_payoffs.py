"""Chapter 11 model figures; no data access or network.

Run: uv run python demos/incerto/calibration_payoffs.py
All stochastic draws use local PCG64 streams; all replicates are retained.
"""

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from xmath.incerto.calibration import (
    beta_brier_cdf, beta_brier_moments, brier_score_distribution,
    calibration_curve, pareto_tail_bet, point_forecast_loss,
    simulate_brier_scores, tail_bet_payoffs,
)
from xmath.incerto.figures import COLORS, savefig, set_theme, vertical_figure


NAMES = ("calibration-tail-payoffs", "calibration-curves",
         "calibration-score-laws", "point-forecast-losses")


def _export(fig, output, name):
    savefig(fig, output / f"{name}.svg")
    plt.close(fig)


def main(output=None):
    output = Path(output or Path(__file__).resolve().parents[2]/"assets/figures/incerto")
    output.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)

    fig, axes = vertical_figure(2, panel_height=3.4)
    x = np.linspace(0, 10, 301)
    payoff = tail_bet_payoffs(x, 4)
    axes[0].plot(x, payoff["excess"], label="excess (x − 4)+", color=COLORS["green"])
    axes[0].plot([0, 4], [0, 0], color=COLORS["accent"], label="binary 1{x > 4}")
    axes[0].plot([4, 10], [1, 1], color=COLORS["accent"])
    axes[0].plot(4, 1, "o", mfc=COLORS["surface"], mec=COLORS["accent"], zorder=5)
    axes[0].plot(4, 0, "o", color=COLORS["accent"], zorder=5)
    axes[0].set(title="Same threshold, different payoff", xlabel="loss amount x",
                ylabel="payoff units", ylim=(-.2, 6.3))
    axes[0].legend(loc="upper left")
    alphas = np.linspace(1.05, 4, 220)
    means = [pareto_tail_bet(a, 10, xm=10*.02**(1/a))["excess_mean"] for a in alphas]
    axes[1].plot(alphas, means, color=COLORS["green"])
    axes[1].set(title="Same event probability: 2%", xlabel="Pareto exponent α",
                ylabel="expected excess (loss units)", ylim=(0, 4.3))
    axes[1].text(.97, .85, "u = 10; minimum adjusted\nExact finite means for α > 1",
                 transform=axes[1].transAxes, ha="right", va="top", fontsize=10)
    _export(fig, output, NAMES[0])

    fig, axes = vertical_figure(2, panel_height=3.5)
    grid = np.linspace(0, 1, 201)
    for power, seed, label, color, marker in (
        (1, 1103, "calibrated: P(D=1|Q)=Q", COLORS["accent"], "o"),
        (2, 1104, "overforecast: P(D=1|Q)=Q²", COLORS["brick"], "s"),
    ):
        rng = np.random.default_rng(seed)
        q = rng.uniform(size=4000)
        d = rng.random(4000) < q**power
        c = calibration_curve(q, d, bins=10)
        freq = c["event_frequency"]
        error = 2*np.sqrt(freq*(1-freq)/c["count"])
        axes[0].plot(grid, grid**power, color=color, ls="--", lw=1.2)
        axes[0].errorbar(c["forecast_mean"], freq, yerr=error, color=color,
                        fmt=marker, ms=4, capsize=2, label=label)
        axes[1].plot(c["forecast_mean"], c["count"], marker+"-", color=color,
                     label="calibrated" if power == 1 else "overforecast")
    axes[0].set(title="Synthetic reliability curves", xlabel="mean announced probability",
                ylabel="event frequency in bin", xlim=(0, 1), ylim=(-.03, 1.04))
    axes[0].legend(loc="upper left", fontsize=9)
    axes[1].set(title="Every forecast retained", xlabel="mean announced probability",
                ylabel="observations in bin", xlim=(0, 1), ylim=(0, 500))
    axes[1].legend(loc="lower left")
    _export(fig, output, NAMES[1])

    fig, axes = vertical_figure(3, panel_height=3.3)
    values, masses = brier_score_distribution(20, .2, .2)
    axes[0].vlines(values, 0, masses, color=COLORS["accent"], lw=1.2)
    axes[0].plot(values, masses, "o", ms=3, label="q = 0.2: exact masses")
    axes[0].axvline(.25, color=COLORS["brick"], ls="--", label="q = 0.5: unit mass at 0.25")
    axes[0].set(title="Constant forecast · n = 20, p = 0.2", xlabel="average Brier score",
                ylabel="probability mass", xlim=(0, .66), ylim=(0, .26))
    axes[0].legend(loc="upper right", fontsize=8.5)
    z = np.linspace(0, 1, 301)
    for p, label, color in ((.5, "independent", COLORS["brick"]),
                            (None, "calibrated", COLORS["accent"])):
        axes[1].plot(z, beta_brier_cdf(z, 1, 1, p=p), color=color, label=label,
                     ls="--" if p is not None else "-")
        sample = simulate_brier_scores(1, 1, 20, p=p, repetitions=20000, seed=1107)
        moments = beta_brier_moments(1, 1, p=p, n=20)
        axes[2].hist(sample, bins=np.linspace(0, .65, 53), density=True,
                     histtype="step", color=color, label=label, lw=1.8)
        axes[2].axvline(moments["mean"], color=color, ls=":", lw=1.2)
        print(f"{label}: mean={sample.mean():.4f}, exact={moments['mean']:.4f}, "
              f"MC SE={np.sqrt(moments['average_variance']/len(sample)):.4f}")
        print("  quantiles: " + ", ".join(f"{v:.3f}" for v in np.quantile(sample, [.1, .5, .9])))
    axes[1].set(title="Uniform forecasts · one score", xlabel="Brier score",
                ylabel="cumulative probability", xlim=(0, 1), ylim=(0, 1.03))
    axes[1].legend(loc="lower right")
    axes[2].set(title="Uniform forecasts · 20-score averages", xlabel="average Brier score",
                ylabel="simulated density", xlim=(0, .65))
    axes[2].legend(loc="upper right")
    _export(fig, output, NAMES[2])

    fig, axes = vertical_figure(2, panel_height=3.5)
    alpha = 1.5
    mean, median = 3., 2**(1/alpha)
    x = np.geomspace(1.01*median, 100, 200)
    for metric, label in (("absolute", "absolute error"), ("squared", "squared error"),
                          ("smape", "sMAPE (0–2)")):
        axes[0].loglog(x, point_forecast_loss(x, median, metric=metric), label=label)
    axes[0].set(title="Same median forecast, three losses", xlabel="loss amount x (log scale)",
                ylabel="score (log scale; units differ)")
    axes[0].legend(loc="upper left")
    points = np.linspace(1, 5, 201)
    risk = [d-mean+2*pareto_tail_bet(alpha, d)["excess_mean"] for d in points]
    axes[1].plot(points, risk, color=COLORS["accent"])
    axes[1].axvline(median, color=COLORS["green"], ls="--", label=f"median = {median:.2f}")
    axes[1].axvline(mean, color=COLORS["brick"], ls=":", label="mean = 3")
    axes[1].set(title="Pareto α = 1.5 · exact absolute risk", xlabel="point forecast d",
                ylabel="expected absolute loss", ylim=(1.6, 4))
    axes[1].legend(loc="lower right")
    _export(fig, output, NAMES[3])
    return list(NAMES)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    main(parser.parse_args().output)
