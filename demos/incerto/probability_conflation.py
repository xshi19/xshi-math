"""Four chapter-13 figures: exact laws and a bounded synthetic Hill experiment.

Run: uv run python demos/incerto/probability_conflation.py
PCG64 seed 1308; 2,000 iid samples of 500; one million total draws.
Every sample is reused at five fixed k values, with infinite ES fits retained.
"""

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import betainc

from xmath.incerto.calibration import brier_score_distribution, pareto_tail_bet
from xmath.incerto.estimators import hill_alpha_estimator
from xmath.incerto.figures import COLORS, savefig, set_theme, vertical_figure
from xmath.incerto.risk_measures import pareto_mixture_risk, pareto_risk


NAMES = ("conflation-payoff-gap", "conflation-probability-error",
         "risk-exponent-uncertainty", "risk-estimation")


def _export(fig, output, name):
    savefig(fig, output / f"{name}.svg")
    plt.close(fig)


def main(output=None):
    output = Path(output or Path(__file__).resolve().parents[2] / "assets/figures/incerto")
    output.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)

    fig, axes = vertical_figure(2, panel_height=3.3)
    scores, mass = brier_score_distribution(20, .1, .1)
    axes[0].vlines(scores, 0, mass, color=COLORS['accent'])
    axes[0].plot(scores, mass, 'o', color=COLORS['accent'], ms=3,
                 label="same law for all three exponents")
    axes[0].set(title="Binary score · no exponent information",
                xlabel="average Brier score (20 events)", ylabel="probability mass")
    axes[0].legend(loc="upper right", fontsize=8.5)
    grid = np.linspace(1.02, 4, 240)
    payoff = [pareto_tail_bet(a, 5, xm=5*.1**(1/a))['excess_mean'] for a in grid]
    axes[1].plot(grid, payoff, color=COLORS['brick'])
    for a, marker in ((3, 'o'), (1.5, 's'), (1.05, '^')):
        value = pareto_tail_bet(a, 5, xm=5*.1**(1/a))['excess_mean']
        axes[1].plot(a, value, marker, ms=6, label=f"α = {a:g}")
    axes[1].set(title="Same 10% event · unequal severity", xlabel="tail exponent α",
                ylabel="expected excess above 5", yscale="log")
    axes[1].set_ylabel("expected excess above 5 (log)")
    axes[1].legend(loc="upper right")
    _export(fig, output, NAMES[0])

    fig, axes = vertical_figure(2, panel_height=3.3)
    ps, ks = np.geomspace(1e-4, .8, 180), np.geomspace(1.01, 1e4, 200)
    for a, style in ((.5, '-'), (1, '--'), (2, '-.')):
        axes[0].loglog(ps, [pareto_risk(a, p)['var'] for p in ps], ls=style,
                       label=f"α = {a:g}")
        axes[1].loglog(ks, betainc(2, 3, ks**(-a)), ls=style, label=f"α = {a:g}")
    axes[0].set(title="Inverse survival · exact Pareto", xlabel="tail probability p (log)",
                ylabel="threshold K (log)")
    axes[1].set(title="Random report Π ~ Beta(2, 3)", xlabel="threshold k (log)",
                ylabel="P(K > k) (log)")
    axes[0].legend(loc="upper right")
    axes[1].legend(loc="lower left")
    _export(fig, output, NAMES[1])

    fig, axes = vertical_figure(2, panel_height=3.4)
    ds = np.linspace(0, .95, 150)
    average, mixture = [], []
    for d in ds:
        parts = [pareto_risk(a, .01) for a in (2-d, 2+d)]
        average.append([np.mean([r[key] for r in parts]) for key in ('var', 'es')])
        mixture.append(list(pareto_mixture_risk([2-d, 2+d], [.5, .5], .01).values()))
    average, mixture = np.array(average), np.array(mixture)
    for i, (ax, key, title) in enumerate(zip(axes, ('var', 'es'), ('VaR', 'Expected shortfall'))):
        ax.plot(ds, average[:, i], color=COLORS['accent'], label="average model risk")
        ax.plot(ds, mixture[:, i], '--', color=COLORS['brick'], label="predictive mixture risk")
        ax.axhline(pareto_risk(2, .01)[key], color=COLORS['muted'], ls=':',
                   label="risk at mean exponent 2")
        ax.set(title=title + " · fixed tail mass 1%", xlabel="exponent spread d",
               ylabel="loss amount (log)", yscale='log')
        ax.legend(loc='upper left', fontsize=8.5)
    _export(fig, output, NAMES[2])

    rng = np.random.default_rng(1308)
    samples = 1 + rng.pareto(1.2, (2000, 500))
    retained = np.array([20, 50, 100, 200, 400])
    quantiles, infinite = [], []
    for k in retained:
        alphas = [hill_alpha_estimator(sample, int(k)) for sample in samples]
        risks = [pareto_risk(a, .01) for a in alphas]
        quantiles.append(np.quantile([r['var'] for r in risks], [.1, .5, .9]))
        infinite.append(sum(np.isinf(r['es']) for r in risks))
    fig, axes = vertical_figure(2, panel_height=3.3)
    low, middle, high = np.array(quantiles).T
    axes[0].fill_between(retained, low, high, color=COLORS['accent'], alpha=.16,
                         label="10th–90th sampling range")
    axes[0].plot(retained, middle, 'o-', color=COLORS['accent'], label="sampling median")
    axes[0].axhline(pareto_risk(1.2, .01)['var'], ls='--', color=COLORS['brick'],
                   label="population VaR")
    axes[0].set(title="Hill plug-in VaR · true α = 1.2", xlabel="retained tail count k",
                ylabel="VaR at 1% tail mass")
    axes[0].legend(loc='upper right', fontsize=8.5)
    axes[1].plot(retained, np.array(infinite)/2000, 'o-', color=COLORS['brick'])
    axes[1].set(title="Infinite ES fits stay in the record", xlabel="retained tail count k",
                ylabel="fraction with fitted α ≤ 1", ylim=(-.005, .25))
    _export(fig, output, NAMES[3])
    print("Infinite ES fits / 2000: " + ", ".join(f"k={k}: {n}" for k, n in zip(retained, infinite)))
    print(f"Exported {len(NAMES)} synthetic figures; all 1,000,000 draws retained.")
    return list(NAMES)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    main(parser.parse_args().output)
