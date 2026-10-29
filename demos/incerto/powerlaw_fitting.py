"""Synthetic body/tail fitting; two mobile SVGs, no empirical inputs.

PCG64 seed 982, n=6000, uniform [1,4] body (probability .7), continuous
Pareto tail (minimum 4, survival exponent 1.8). Twenty-one fixed candidate
thresholds, min_tail=200; no bootstrap or unbounded optimization in this demo.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from xmath.incerto.figures import COLORS, savefig, set_theme, vertical_figure
from xmath.incerto.powerlaw import sample_powerlaw, select_xmin
from xmath.incerto.stats import empirical_survival_function

ROOT = Path(__file__).resolve().parents[2]


def experiment():
    rng = np.random.default_rng(982)
    x = rng.uniform(1, 4, 6000)
    tail = rng.random(x.size) < .3
    x[tail] = sample_powerlaw(1.8, 4, int(tail.sum()), random_state=rng)
    return x, select_xmin(x, candidates=np.arange(1, 6.01, .25), min_tail=200)


def main(output=None):
    out = Path(output) if output else ROOT/'assets/figures/incerto'
    out.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)
    x, fit = experiment()
    points, sf = empirical_survival_function(x)
    fig, (ax,) = vertical_figure(1, panel_height=4.2)
    positive = sf > 0
    ax.step(points[positive], sf[positive], where='post', label='Empirical survival', linewidth=1.5)
    grid = np.geomspace(fit['xmin'], x.max(), 300)
    model = fit['n_tail']/len(x)*(grid/fit['xmin'])**(-fit['alpha'])
    ax.plot(grid, model, '--', color=COLORS['green'], label='Fitted tail')
    ax.axvline(4, color=COLORS['muted'], linestyle=':', label='Population join: 4')
    ax.set(xscale='log', yscale='log', xlabel='x (log scale)', ylabel='P(X > x) (log scale)',
           title=f"Body and fitted power tail\nChosen minimum {fit['xmin']:.2f}; tail count {fit['n_tail']}")
    ax.legend(loc='upper right')
    savefig(fig, out/'powerlaw-fitted-tail.svg')
    plt.close(fig)

    fig, axes = vertical_figure(2, panel_height=3.1)
    axes[0].plot(fit['xmins'], fit['distances'], 'o-', markersize=3)
    axes[0].scatter([fit['xmin']], [fit['ks']], color=COLORS['brick'], zorder=5, label='KS minimum')
    axes[0].set(ylabel='KS distance', title='Refit at every candidate')
    axes[0].legend()
    axes[1].plot(fit['xmins'], fit['counts'], 'o-', color=COLORS['green'], markersize=3)
    axes[1].set(ylabel='Retained observations', title='The cost of raising the threshold')
    for ax in axes:
        ax.axvline(4, color=COLORS['muted'], linestyle=':')
        ax.set(xlabel='Candidate minimum', xlim=(1, 6))
    savefig(fig, out/'powerlaw-ks-threshold.svg')
    plt.close(fig)
    print(f"xmin={fit['xmin']:.2f}, alpha={fit['alpha']:.3f}, tail={fit['n_tail']}, KS={fit['ks']:.3f}")


if __name__ == '__main__':
    main()
