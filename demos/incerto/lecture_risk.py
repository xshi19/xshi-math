"""Exact worked models for SCoFT v4 chapter 3, with no data or RNG.

Run: uv run python demos/incerto/lecture_risk.py
Dimensionless fixed grids: 3 x 161 contamination probabilities, 121 spreads,
401/201 time points, 3 x 161 Pareto thresholds, and 40 block counts.
The grids bound runtime (normally a few seconds), not the laws' supports.
Three deterministic SVGs and console tables are the complete outputs.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from xmath.incerto.figures import COLORS, savefig, set_theme
from xmath.incerto.lecture_risk import (
    absorbing_resource_path,
    block_failure_summary,
    finite_payoff_mean,
    repeated_event_probability,
    split_power_damage_logsf,
    survival_from_hazards,
)


def _save(fig: plt.Figure, output: Path, name: str) -> None:
    for ax in fig.axes:
        for line in ax.lines:
            if not np.all(np.isfinite(line.get_ydata())):
                raise ValueError(f"nonfinite plotted values in {name}")
    path = output / name
    savefig(fig, path, metadata={"Date": None, "Creator": "xshi-math lecture_risk.py"})
    plt.close(fig)
    path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines()) + "\n")


def main() -> None:
    output = Path(__file__).resolve().parents[2] / "assets/figures/incerto"
    output.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)

    fig, axes = plt.subplots(2, 1, figsize=(5.0, 7.4), layout="constrained")
    epsilon = np.geomspace(1e-6, 1e-2, 161)
    for n, style in zip((100, 1000, 10000), ("-", "--", "-.")):
        detected = [repeated_event_probability(float(e), n) for e in epsilon]
        axes[0].semilogx(epsilon, detected, linestyle=style, label=f"n = {n:,}")
    axes[0].set(xlabel=r"Contamination probability $\varepsilon$",
                ylabel="Detection probability", ylim=(0, 1.03),
                title="Finite-sample detection")
    axes[0].legend(handlelength=3.5)
    spread = np.linspace(0, 3, 121)
    gap = np.array([finite_payoff_mean([0.5, 0.5], [(4-s)**2, (4+s)**2])-16 for s in spread])
    axes[1].plot(spread, gap, label=r"Convex: $g(x)=x^2$")
    axes[1].plot(spread, -gap, "--", label=r"Concave: $g(x)=-x^2$")
    axes[1].axhline(0, color=COLORS["muted"], linewidth=0.8)
    axes[1].set(xlabel=r"Symmetric spread $s$ around mean 4",
                ylabel=r"$\mathbb{E}g(X)-g(4)$", title="Same mean input,\ndifferent payoff")
    axes[1].legend()
    _save(fig, output, "lecture-inference-payoffs.svg")

    contamination, tail_minimum, tail_alpha = 1e-4, 1e6, 1.5
    contaminated_mean = finite_payoff_mean(
        [1-contamination, contamination],
        [0.5, tail_alpha * tail_minimum / (tail_alpha-1)],
    )
    print("Rare contamination: epsilon=0.0001, b=1000000, alpha=1.5")
    print(f"Baseline mean=0.5; contaminated mean={contaminated_mean:.5f}; second moment=infinity")
    for n in (10, 1000, 10000, 100000):
        detected = repeated_event_probability(contamination, n)
        print(f"n={n:6d}: detection={detected:.9f}; no contamination={1-detected:.9f}")
    print("Payoff means A, B:", finite_payoff_mean([0.98, 0.02], [1, -80]),
          finite_payoff_mean([0.98, 0.02], [-1, 80]))
    print("Equal-variance laws: mean, second moment, absolute moment, fourth moment")
    for probabilities, values in [([0.5, 0.5], np.array([-1, 1])),
                                   ([0.125, 0.75, 0.125], np.array([-2, 0, 2]))]:
        print([finite_payoff_mean(probabilities, v) for v in
               (values, values**2, np.abs(values), values**4)])

    fig, axes = plt.subplots(2, 1, figsize=(5.0, 7.4), layout="constrained")
    horizon = np.arange(401)
    constant = survival_from_hazards(np.full(400, 0.02))
    summable = survival_from_hazards(1 / np.arange(2, 402, dtype=float)**2)
    common = survival_from_hazards(np.r_[0.02, np.zeros(399)])
    axes[0].plot(horizon, constant, label="Constant hazard 0.02")
    axes[0].plot(horizon, summable, "--", label=r"Hazard $1/(k+1)^2$")
    axes[0].plot(horizon, common, "-.", label="One shared failure indicator")
    axes[0].set(xlabel="Horizon N", ylabel="Survival probability", ylim=(0, 1.04),
                title="Which hazard is repeated?")
    axes[0].legend(fontsize=10, handlelength=3.5)
    time = np.arange(201)
    expectation = np.exp(time * (np.log1p(0.04) + np.log1p(-0.02)))
    axes[1].semilogy(time, expectation, label="Ensemble expectation")
    axes[1].semilogy(time, constant[:201], "--", label="Survival probability")
    axes[1].set(xlabel="Step k", ylabel="Dimensionless value (log scale)",
                title="Growth among rare survivors")
    axes[1].legend(fontsize=10)
    _save(fig, output, "lecture-ruin.svg")
    print("Constant hazard q=0.02: ruin probabilities")
    for n in (10, 100, 1000):
        print(f"N={n:4d}: {repeated_event_probability(0.02, n):.10f}")
    print(f"Summable-hazard survival at N=400: {summable[-1]:.9f}; limit=0.5")
    print("Ensemble per-step growth factor:", 1.04 * 0.98)
    for increments in ([-4, 4], [4, -4]):
        print(f"Increments {increments}: resources {absorbing_resource_path(3, increments)}")

    fig, axes = plt.subplots(3, 1, figsize=(5.0, 10.2), layout="constrained")
    threshold = np.geomspace(0.01, 100, 161)
    for m, style in zip((1, 4, 16), ("-", "--", "-.")):
        survival = np.exp(split_power_damage_logsf(threshold, alpha=1.5, power=2, modules=m))
        axes[0].loglog(threshold, survival, linestyle=style, label=f"m = {m}")
    axes[0].set(xlabel="Damage threshold u", ylabel="Survival probability",
                title="Same tail exponent, different scale")
    axes[0].legend(handlelength=3.5)
    blocks = np.arange(1, 41)
    summaries = [block_failure_summary(0.02, int(k)) for k in blocks]
    axes[1].plot(blocks, [s["any_failure"] for s in summaries], marker="o", markevery=5,
                 label="Any loss: independent blocks")
    axes[2].semilogy(blocks, [s["total_failure"] for s in summaries], "--", marker="s", markevery=5,
                     label="Total loss: independent blocks")
    for ax in axes[1:]:
        ax.axhline(0.02, color=COLORS["umber"], linestyle="-.", label="Common shock")
    axes[1].set(xlabel="Independent equal-exposure blocks k", ylabel="Probability",
                ylim=(0, .6), title="At least one block fails: q = 0.02")
    axes[2].set(xlabel="Independent equal-exposure blocks k", ylabel="Probability (log scale)",
                ylim=(1e-70, 1), title="Every block fails: q = 0.02")
    axes[1].legend(fontsize=10, loc="upper left", handlelength=3.5)
    axes[2].legend(fontsize=10, loc="lower left", handlelength=3.5)
    _save(fig, output, "lecture-scale-dependence.svg")
    print("Split quadratic damage, alpha=1.5: m=16 pathwise ratio=1/16; tail ratio=1/8 above u=1")
    for k in (1, 10):
        print(f"Failure summary, independent blocks={k}:", block_failure_summary(0.02, k))
    print("All plotted values finite; no omitted points, stochastic estimates or external data.")
    print(f"Figures: {output}")


if __name__ == "__main__":
    main()
