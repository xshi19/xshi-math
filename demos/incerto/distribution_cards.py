"""Six deterministic P1 figures: five distribution cards and Pareto maxima.

Run: uv run python demos/incerto/distribution_cards.py
No sampling/fitting; fixed 601-point linear and 401-point log grids. The
survival viewport is [1e-8, 1.1], with exact zero omitted on log axes. Support
markers identify endpoints, not atoms. Runtime is normally a few seconds.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from xmath.incerto.distributions import (
    double_pareto, frechet, generalized_extreme_value, generalized_pareto, pareto_type1,
)
from xmath.incerto.figures import COLORS, distribution_card, savefig, set_theme, vertical_figure
from xmath.incerto.glossary import pareto_normalized_maximum_cdf


def main(output=None):
    output = Path(output) if output is not None else Path(__file__).resolve().parents[2] / "assets/figures/incerto"
    output.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)
    alphas = (.8, 1.5, 3.)
    cards = [
        ("pareto-card.svg", [(pareto_type1(a), fr"$\alpha={a:g}$") for a in alphas],
         (-.25, 5), (.25, 100), "Pareto · minimum 1", "Support: x ≥ 1 · dotted cutoff at 1", "x", "Survival"),
        ("gpd-card.svg", [(generalized_pareto(s), fr"$\xi={s:g}$") for s in (-.4, 0, .4)],
         (-.25, 5), (.03, 20), "Generalized Pareto · scale 1",
         "Support: y ≥ 0; y ≤ 2.5 if ξ = −0.4", "Excess y", "Survival"),
        ("gev-card.svg", [(generalized_extreme_value(s), fr"$\xi={s:g}$") for s in (-.3, 0, .3)],
         (-4, 6), (.03, 30), "GEV · location 0, scale 1",
         "ξ = 0.3: x ≥ −10/3\nξ = −0.3: x ≤ 10/3; ξ = 0: all real x", "x", "Right-tail survival"),
        ("frechet-card.svg", [(frechet(a), fr"$\alpha={a:g}$") for a in alphas],
         (-.25, 5), (.03, 100), "Fréchet · scale 1", "Support: y > 0 · boundary at 0", "y", "Survival"),
        ("double-pareto-card.svg", [(double_pareto(a), fr"$\alpha={a:g}$") for a in alphas],
         (-5, 5), (.03, 100), "Symmetric shifted double Pareto",
         "X = ±(Y − 1) · unit scale\nSupport: all real x; no finite endpoint", "x", "Right-tail P(X > x)"),
    ]
    for name, models, linear_range, log_range, title, support, coordinate, tail_label in cards:
        # Include exact finite endpoints so markers and continuous extensions agree.
        endpoints = [v for law, _ in models for v in law.support()
                     if np.isfinite(v) and linear_range[0] <= v <= linear_range[1]]
        x = np.unique(np.r_[np.linspace(*linear_range, 601), endpoints])
        fig = distribution_card(models, x, np.geomspace(*log_range, 401), title=title,
                                support_note=support, coordinate=coordinate, tail_label=tail_label)
        savefig(fig, output / name)
        plt.close(fig)

    fig, axes = vertical_figure(2)
    y = np.linspace(.03, 4, 601)
    alpha = 1.5
    limit = frechet(alpha).cdf(y)
    for n, style in zip((1, 4, 16, 64), (":", "--", "-.", "-")):
        values = pareto_normalized_maximum_cdf(y, alpha=alpha, n=n)
        line, = axes[0].plot(y, values, style, label=f"n = {n}")
        axes[1].plot(y, limit-values, style, color=line.get_color(), label=f"n = {n}")
        axes[0].axvline(n**(-1/alpha), color=line.get_color(), linestyle=":", linewidth=.8)
    axes[0].plot(y, limit, color=COLORS["ink"], linewidth=1.3, label="Fréchet limit")
    axes[0].set(title="Exact normalized Pareto maxima\nα = 1.5 · dotted lower endpoints",
                ylabel="CDF", ylim=(0, 1))
    axes[1].set(title="Finite-block correction", ylabel="Limit CDF − finite-n CDF")
    for ax in axes:
        ax.set(xlabel=r"Normalized maximum $y = M_n/(x_m n^{1/\alpha})$")
        ax.legend(loc="upper center", bbox_to_anchor=(.5, -.27), ncol=2, handlelength=3)
    savefig(fig, output / "frechet-maxima.svg")
    plt.close(fig)
    print("Exported 5 distribution cards and 1 exact maxima comparison.")


if __name__ == "__main__":
    main()
