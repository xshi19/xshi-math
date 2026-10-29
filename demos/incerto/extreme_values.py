"""Chapter 9: exact curves, numerical normal integrals and fixed-k Hill checks.

Run: uv run python demos/incerto/extreme_values.py
Only the Hill check is simulated: 2 * 4,000 * 200 iid Pareto observations,
PCG64 seeds 2026102905/2026102930. No observation or fit is discarded.
All figures share the deterministic Incerto export path and vertical layout.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gumbel_r, norm

from xmath.incerto.estimators import hill_alpha_estimator
from xmath.incerto.extremes import (
    expected_gaussian_hidden_mean, expected_pareto_hidden_fraction,
    gaussian_maximum_cdf, gaussian_maximum_norming, maximum_missing_mass,
    pareto_exponent_sampling,
)
from xmath.incerto.figures import COLORS, savefig, set_theme, vertical_figure

ROOT = Path(__file__).resolve().parents[2]


def plot_gaussian():
    z = np.linspace(-3, 5, 401)
    fig, axes = vertical_figure(3, panel_height=3.4)
    for n in (10, 100, 10000):
        a, b = gaussian_maximum_norming(n)
        axes[0].plot(z, gaussian_maximum_cdf(b+a*z, n), label=f"n = {n:,}")
    axes[0].plot(z, gumbel_r.cdf(z), '--', color=COLORS['ink'], label='Gumbel')
    axes[0].set(title='Normal maxima · exact CDF', ylabel='Cumulative probability', ylim=(0, 1.03))
    axes[0].legend(loc='upper center', bbox_to_anchor=(.5, -.26), ncol=2)
    for method, style in [('mills', '-'), ('asymptotic', '--')]:
        a, b = gaussian_maximum_norming(100, method=method)
        x = b+a*z
        density = np.exp(np.log(100*a)+norm.logpdf(x)+99*norm.logcdf(x))
        axes[1].plot(z, gaussian_maximum_cdf(x, 100)-gumbel_r.cdf(z), style, label=method)
        axes[2].plot(z, density-gumbel_r.pdf(z), style, label=method)
    for ax, quantity in zip(axes[1:], ['CDF', 'Density']):
        ax.axhline(0, color=COLORS['muted'], linewidth=.8)
        ax.set(title=f'{quantity} difference · n = 100', ylabel=f'Exact − Gumbel {quantity.lower()}')
        ax.legend(loc='upper right')
    for ax in axes:
        ax.set(xlabel='Normalized maximum z', xlim=(-3, 5))
    return fig


def plot_hidden_pareto():
    ns = np.unique(np.geomspace(10, 10**6, 101).astype(int))
    fig, axes = vertical_figure(2, panel_height=3.6)
    for alpha in (1.1, 1.5, 2):
        expected = [expected_pareto_hidden_fraction(int(n), alpha) for n in ns]
        axes[0].plot(ns, expected, label=fr'$\alpha={alpha:g}$')
    axes[0].plot(ns, 1/(ns+1), '--', color=COLORS['ink'], label='Missing probability')
    axes[0].set(title='Pareto · expected hidden fractions', ylabel='Fraction (log scale)')
    axes[0].legend(loc='upper center', bbox_to_anchor=(.5, -.27), ncol=2)
    quantiles = np.array([maximum_missing_mass(int(n)).ppf([.1, .5, .9])**(1/3) for n in ns])
    axes[1].fill_between(ns, quantiles[:, 0], quantiles[:, 2], alpha=.22,
                         color=COLORS['teal'], label='10th–90th quantiles')
    axes[1].plot(ns, quantiles[:, 1], color=COLORS['teal'], label='Median')
    axes[1].plot(ns, [expected_pareto_hidden_fraction(int(n), 1.5) for n in ns],
                 '--', color=COLORS['ink'], label='Expectation')
    axes[1].set(title=r'Hidden mean · $\alpha=1.5$', ylabel='Fraction (log scale)')
    axes[1].legend(loc='lower left')
    for ax in axes:
        ax.set(xscale='log', yscale='log', xlabel='Sample size n (log scale)', xlim=(10, 10**6))
    return fig


def plot_hidden_normal():
    ns = np.unique(np.geomspace(10, 10**5, 41).astype(int))
    results = [expected_gaussian_hidden_mean(int(n)) for n in ns]
    values = np.array([r['value'] for r in results])
    fig, axes = vertical_figure(2, panel_height=3.3)
    axes[0].plot(ns, values)
    axes[0].set(title='Normal · hidden mean contribution', ylabel='Contribution / σ (log scale)')
    axes[1].plot(ns, values*(ns+1))
    axes[1].set(title='Size conditional on a new record', ylabel='Conditional mean / σ (log scale)')
    for ax in axes:
        ax.set(xscale='log', yscale='log', xlabel='Sample size n (log scale)', xlim=(10, 10**5))
    print(f"Normal quadrature: maximum reported absolute error={max(r['abs_error'] for r in results):.2g}")
    return fig


def hill_samples(k, *, repetitions=4000):
    rng = np.random.default_rng(2026102900+k)
    sample = np.exp(rng.exponential(1/1.5, size=(repetitions, 200)))
    return np.array([hill_alpha_estimator(row, k) for row in sample])


def plot_hill():
    grid = np.linspace(.2, 4.5, 401)
    ms = np.arange(3, 101)
    fig, axes = vertical_figure(3, panel_height=3.5)
    for k in (5, 30):
        law = pareto_exponent_sampling(1.5, k)
        axes[0].plot(grid, law.pdf(grid), label=f'm = {k}')
        samples = hill_samples(k)
        empirical = np.searchsorted(np.sort(samples), grid, side='right')/samples.size
        axes[2].plot(grid, empirical-law.cdf(grid), label=f'k = {k}')
        print(f"Hill k={k}: fits={samples.size}, finite={np.isfinite(samples).sum()}, median={np.median(samples):.4g}")
    axes[0].set(title='Exponent estimate · exact density', xlabel='Estimated exponent', ylabel='Density', xlim=(.2, 4.5))
    axes[0].axvline(1.5, color=COLORS['muted'], linestyle=':', label='True exponent')
    axes[0].legend()
    laws = [pareto_exponent_sampling(1.5, int(m)) for m in ms]
    qs = np.array([law.ppf([.1, .5, .9]) for law in laws])
    axes[1].fill_between(ms, qs[:, 0], qs[:, 2], alpha=.22, color=COLORS['teal'], label='10th–90th quantiles')
    axes[1].plot(ms, qs[:, 1], color=COLORS['teal'], label='Median')
    axes[1].plot(ms, [law.mean() for law in laws], '--', color=COLORS['ink'], label='Mean')
    axes[1].axhline(1.5, color=COLORS['muted'], linestyle=':')
    axes[1].set(title='Sampling spread and finite-size bias', xlabel='Log-excess count m', ylabel='Estimated exponent', xlim=(3, 100))
    axes[1].legend()
    axes[2].axhline(0, color=COLORS['muted'], linewidth=.8)
    axes[2].set(title='4,000 Hill fits · sample size 200', xlabel='Estimated exponent',
                ylabel='Empirical CDF − exact CDF', xlim=(.2, 4.5))
    axes[2].legend()
    return fig


def main(output_dir=None):
    set_theme(scale=1.1)
    output = Path(output_dir) if output_dir is not None else ROOT/'assets/figures/incerto'
    output.mkdir(parents=True, exist_ok=True)
    for name, make in [('gaussian-maxima', plot_gaussian), ('hidden-tail-pareto', plot_hidden_pareto),
                       ('hidden-tail-normal', plot_hidden_normal), ('hill-sampling-law', plot_hill)]:
        fig = make()
        savefig(fig, output/f'{name}.svg')
        plt.close(fig)
        print(f'{name}.svg')


if __name__ == '__main__':
    main()
