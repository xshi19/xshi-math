"""Chapter 8: exact MAD curves and bounded seeded numerical comparisons.

Run: uv run python demos/incerto/concentration.py
Four SVGs; about 9 million total scalar draws, no clipping or discarded draws.
Monte Carlo bars are +/-2 estimated SEs of MAD transformed to kappa. They
are diagnostic intervals, not confidence guarantees or model uncertainty.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from xmath.incerto.concentration import (
    estimate_sum_mad, gamma_sum_mad, gaussian_equivalent_n, gaussian_sum_mad,
    kappa_from_mads, lognormal_sum_mad, normal_location_mixture_sum_mad,
    student_sum_mad,
)
from xmath.incerto.distributions import pareto_type1
from xmath.incerto.figures import COLORS, savefig, set_theme, vertical_figure


def finish(fig, output, name):
    savefig(fig, output/name)
    plt.close(fig)


def kappa_interval(m1, result, n):
    """Transform the Monte Carlo MAD diagnostic, retaining its asymmetry."""
    value = kappa_from_mads(m1, result["mad"], n)
    lo = kappa_from_mads(m1, result["mad"]-2*result["mc_se"], n)
    hi = kappa_from_mads(m1, result["mad"]+2*result["mc_se"], n)
    return value, value-lo, hi-value


def main(output=None):
    output = Path(output) if output is not None else Path(__file__).resolve().parents[2]/"assets/figures/incerto"
    output.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)
    sizes = np.unique(np.geomspace(2, 1000, 80).astype(int))
    models = [("Gaussian", gaussian_sum_mad, COLORS["muted"], "--"),
              ("Student 3", student_sum_mad, COLORS["accent"], "-"),
              ("Exponential", gamma_sum_mad, COLORS["green"], "-."),
              ("Stable 1.5", lambda n: n**(2/3), COLORS["brick"], ":")]
    fig, axes = vertical_figure(2, panel_height=3.5)
    fig.get_layout_engine().set(hspace=.12)
    for label, mad, color, style in models:
        m1 = mad(1)
        values = np.array([mad(int(n)) for n in sizes])
        axes[0].plot(sizes, values/(sizes*m1), color=color, ls=style, label=label)
        kappas = [kappa_from_mads(m1, value, int(n)) for n, value in zip(sizes, values)]
        axes[1].plot(sizes, kappas, color=color, ls=style, label=label)
    axes[0].set(title="Absolute error after averaging", ylabel="Error / single-observation MAD",
                xscale="log", yscale="log", xlabel="Number of observations n")
    axes[1].set(title="Kappa anchored at one observation", ylabel="Kappa (1, n)",
                xscale="log", xlabel="Number of observations n", ylim=(-.02, .55))
    axes[1].legend(loc="upper center", bbox_to_anchor=(.5, -.25), ncol=2, handlelength=3)
    finish(fig, output, "kappa-aggregation.svg")

    reference = np.unique(np.geomspace(2, 1000, 65).astype(int))
    fig, axes = vertical_figure(1, panel_height=4.1)
    for label, mad, color, style in models:
        # Stable index 1.5 gives exponent 1.5 for the matching size.
        values = ([int(np.ceil(int(n)**1.5)) for n in reference] if label == "Stable 1.5"
                  else [gaussian_equivalent_n(mad, int(n)) for n in reference])
        axes[0].plot(reference, values, color=color, ls=style, label=label)
    axes[0].set(title="Equal absolute error · equal starting MAD",
                xlabel="Gaussian reference size", ylabel="Required observation count",
                xscale="log", yscale="log")
    axes[0].legend(loc="upper center", bbox_to_anchor=(.5, -.25), ncol=2, handlelength=3)
    finish(fig, output, "kappa-sample-size.svg")

    sigmas = np.linspace(.2, 3, 11)
    fig, axes = vertical_figure(1, panel_height=4.1)
    for row, (n, color, marker) in enumerate(((2, COLORS["accent"], "o"), (16, COLORS["green"], "s"))):
        values, errors = [], []
        for j, sigma in enumerate(sigmas):
            m1 = lognormal_sum_mad(1, sigma)["mad"]
            result = lognormal_sum_mad(n, sigma, repetitions=30000, random_state=20261100+11*row+j)
            value, lower, upper = kappa_interval(m1, result, n)
            values.append(value)
            errors.append([lower, upper])
        axes[0].errorbar(sigmas, values, yerr=np.array(errors).T, color=color, marker=marker,
                         capsize=3, label=f"n = {n}")
    axes[0].axhline(0, color=COLORS["muted"], ls="--", lw=1)
    axes[0].axhline(1, color=COLORS["muted"], ls=":", lw=1)
    axes[0].set(title="Lognormal · conditional Monte Carlo", xlabel="Log-scale σ",
                ylabel="Estimated kappa (1, n)", ylim=(-.05, 1.05))
    axes[0].legend(loc="upper center", bbox_to_anchor=(.5, -.25), ncol=2)
    finish(fig, output, "kappa-lognormal.svg")

    fig, axes = vertical_figure(2, panel_height=3.8)
    fig.get_layout_engine().set(hspace=.12)
    axes[0].plot(sizes, [kappa_from_mads(student_sum_mad(1), student_sum_mad(int(n)), int(n))
                         for n in sizes], color=COLORS["accent"], label="Student 3 · exact")
    mc_sizes = [2, 8, 32, 128]
    values, errors = [], []
    for j, n in enumerate(mc_sizes):
        result = estimate_sum_mad(pareto_type1(3), n, mean=1.5,
                                  repetitions=20000, random_state=20261090+j)
        value, lower, upper = kappa_interval(4/9, result, n)
        values.append(value)
        errors.append([lower, upper])
        print(f"Pareto 3, n={n}: MAD={result['mad']:.4f}, MC SE={result['mc_se']:.4f}, kappa={value:.4f}")
    axes[0].errorbar(mc_sizes, values, yerr=np.array(errors).T, color=COLORS["umber"],
                     marker="o", capsize=3, label="Pareto 3 · estimated")
    axes[0].set(title="Same tail exponent, different bodies", xlabel="Number of observations n",
                ylabel="Kappa (1, n)", xscale="log", xlim=(1.8, 150), ylim=(0, .58))
    axes[0].legend(loc="upper right", fontsize=9.5)
    a = np.linspace(0, 5, 151)
    values = [kappa_from_mads(normal_location_mixture_sum_mad(1, v),
                              normal_location_mixture_sum_mad(2, v), 2) for v in a]
    axes[1].plot(a, values, color=COLORS["brick"], label="Normal mixture · σ = 1")
    axes[1].axhline(kappa_from_mads(2/3, 14/15, 2), color=COLORS["green"], ls="--",
                    label="Unimodal triangle: −0.060")
    axes[1].set(title="Negative kappa", xlabel="Mixture half-separation a",
                ylabel="Kappa (1, 2)", ylim=(-4.8, .25))
    axes[1].legend(loc="lower left", fontsize=9.5)
    finish(fig, output, "kappa-shape.svg")

    for label, mad, _, _ in models[:3]:
        print(f"{label}, Gaussian n=30: required n={gaussian_equivalent_n(mad, 30)}")
    print("Exported four chapter-8 figures.")


if __name__ == "__main__":
    main()
