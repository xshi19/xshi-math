"""Exact model comparisons for SCoFT v4 ch. 1, with no external data or RNG.

Run: uv run python demos/incerto/prologue_tail_classes.py
Dimensionless inputs; three bounded laws and five unbounded laws, evaluated
on 241 thresholds in [1, 10000]. No distribution is truncated or fitted.
Outputs: two deterministic SVGs in assets/figures/incerto and console tables.
Runtime is normally a few seconds. Non-finite diagnostic values are errors.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon, gamma, lognorm, pareto, weibull_min

from xmath.incerto.figures import COLORS, savefig, set_theme
from xmath.incerto.tail_classes import (
    bounded_spike_summary,
    log_survival_multiplier_ratio,
)


def main() -> None:
    output = Path(__file__).resolve().parents[2] / "assets/figures/incerto"
    output.mkdir(parents=True, exist_ok=True)
    set_theme()
    # Stable SVG IDs and no timestamp, so a rerun produces identical assets.
    matplotlib.rcParams["svg.hashsalt"] = "scft-v4-ch01"
    metadata = {"Date": None, "Creator": "xshi-math prologue_tail_classes.py"}

    epsilon = np.array([0.1, 0.01, 0.001])
    summaries = [bounded_spike_summary(float(p)) for p in epsilon]
    print("Bounded three-point laws (population quantities; dimensionless)")
    print("epsilon  support_radius  mean  variance  Pearson_kurtosis")
    for p, row in zip(epsilon, summaries):
        print(f"{p:g}  {row['support_radius']:.6f}  {row['mean']:g}  "
              f"{row['variance']:g}  {row['kurtosis']:g}")
    fig, ax = plt.subplots(figsize=(6.4, 3.8), layout="constrained")
    ax.loglog(epsilon, [row["kurtosis"] for row in summaries], "o", label="Bounded laws")
    for p, row in zip(epsilon, summaries):
        ax.annotate(f"radius {row['support_radius']:.2f}",
                    (p, row["kurtosis"]), xytext=(0, 10),
                    textcoords="offset points", ha="center", fontsize=9)
    ax.axhline(3, linestyle="--", color=COLORS["muted"], label="Gaussian reference: 3")
    ax.set(xlabel=r"Nonzero probability $\varepsilon$", ylabel="Pearson kurtosis",
           xlim=(0.0005, 0.2), ylim=(2, 3000))
    ax.legend(loc="center right")
    savefig(fig, output / "prologue-kurtosis.svg", metadata=metadata)
    plt.close(fig)

    # Gamma(shape=2, rate=1) has log survival -u + log(1+u).
    # scipy.stats.gamma.logsf can underflow internally at this grid's far end.
    models = [
        ("Pareto (alpha=2.5)", pareto(2.5).logsf, "-"),
        ("Lognormal (log mean=0, log sd=1)", lognorm(1).logsf, "--"),
        ("Weibull (shape=0.5)", weibull_min(0.5).logsf, "-."),
        ("Exponential (rate=1)", expon().logsf, ":"),
        ("Gamma (shape=2, rate=1)", lambda u: -u + np.log1p(u), (0, (5, 2, 1, 2))),
    ]
    u = np.geomspace(1, 10_000, 241)
    fig, ax = plt.subplots(figsize=(6.8, 4.4), layout="constrained")
    print("\nLog multiplier ratios at u = 2, 10, 100, 10000; t = 2")
    for name, log_sf, style in models:
        log_ratio = log_survival_multiplier_ratio(log_sf, u)
        if np.any(log_ratio >= 0):
            raise ValueError(f"expected strictly negative log ratios for {name}")
        ax.loglog(u, -log_ratio, linestyle=style, label=name)
        table = log_survival_multiplier_ratio(log_sf, [2, 10, 100, 10_000])
        print(name, np.array2string(table, precision=6))
    ax.set(xlabel=r"Threshold $u$", ylabel=r"$-\log[\bar F(2u)/\bar F(u)]$")
    ax.legend(loc="upper left", fontsize=8)
    savefig(fig, output / "prologue-tail-ratios.svg", metadata=metadata)
    plt.close(fig)

    # Independent special-function evaluation of the page's exact sum ratios.
    thresholds = np.array([2.0, 10.0, 100.0])
    print("\nTwo-sum ratios R(u), u = 2, 10, 100")
    for shape in (1, 2):
        ratios = np.exp(gamma(2 * shape).logsf(thresholds)
                        - gamma(shape).logsf(thresholds) - np.log(2))
        if not np.all(np.isfinite(ratios)):
            raise ValueError("non-finite two-sum check")
        print(f"Gamma shape={shape}, rate=1:", np.array2string(ratios, precision=6))
    print("All 1205 grid log ratios finite; no omitted points, sampling or external data.")
    print(f"Figures: {output}")


if __name__ == "__main__":
    main()
