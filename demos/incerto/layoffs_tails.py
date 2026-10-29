"""Regenerate the layoffs figures and aggregate outputs from a local CSV.

UV_NO_SYNC=1 uv run python demos/incerto/layoffs_tails.py --data /path/to/layoffs.csv
Use --recorded assets/incerto/outputs/layoffs-tails.json to redraw without data.
No event rows or company identifiers are written; no network calls are made.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from xmath.incerto.datasets import load_layoffs, workforce_log_loss
from xmath.incerto.estimators import hill_stability_bootstrap
from xmath.incerto.figures import COLORS, savefig, set_theme, vertical_figure
from xmath.incerto.powerlaw import powerlaw_gof_bootstrap, powerlaw_standard_error

ROOT = Path(__file__).resolve().parents[2]


def calculate(path, replicates=1000, retrieved=None):
    data = load_layoffs(path)
    samples = {
        "counts": data.count[data.count > 0],
        "pct_logloss_reported": workforce_log_loss(
            data.fraction[(data.fraction > 0) & (data.fraction < 1)]),
    }
    result = {
        "source": "layoffs.fyi via Kaggle mirror swaptr/layoffs-2022",
        "retrieved": retrieved,
        "input_sha256": hashlib.sha256(Path(path).read_bytes()).hexdigest(),
        "input_rows": data.input_rows, "events": int(data.count.size),
        "first_date": str(min(data.date)), "last_date": str(max(data.date)),
        "missing_counts": int(np.isnan(data.count).sum()),
        "missing_fractions": int(np.isnan(data.fraction).sum()),
        "full_workforce_cuts": int((data.fraction == 1).sum()),
        "zero_fractions": int((data.fraction == 0).sum()),
        "replicates": replicates, "confidence": .95, "min_tail": 50,
        "samples": {},
    }
    for offset, (name, x) in enumerate(samples.items()):
        seed = 20261029 + offset
        ks = np.unique(np.r_[np.arange(25, len(x)//3 + 1, 5),
                             round(.1*len(x)), round(.2*len(x))])
        curve = hill_stability_bootstrap(x, ks, replicates=replicates, random_state=seed)
        print(f"{name}: Hill curve complete; refitting {replicates} GOF samples", flush=True)
        gof = powerlaw_gof_bootstrap(x, replicates=replicates, random_state=seed,
                                    min_tail=50)
        fitted = gof["fit"]
        csn = {key: fitted[key] for key in ("xmin", "alpha", "n_tail", "ks")}
        csn.update(standard_error=powerlaw_standard_error(fitted["alpha"], fitted["n_tail"]),
                   gof_p=gof["p_value"],
                   gof_hits=int(np.sum(gof["ks_samples"] >= fitted["ks"])))
        result["samples"][name] = {
            "n": int(x.size), "seed": seed, "csn": csn,
            "hill": {key: values.tolist() for key, values in curve.items()},
        }
        print(f"{name}: xmin={csn['xmin']:.3f}, alpha={csn['alpha']:.3f}, "
              f"GOF={csn['gof_hits']}/{replicates}", flush=True)
    return result


def summary(result):
    lines = [f"Events: {result['events']}; source rows: {result['input_rows']}",
             f"Dates: {result['first_date']} to {result['last_date']}",
             f"Excluded fractions: {result['full_workforce_cuts']} at 1, "
             f"{result['zero_fractions']} at 0, {result['missing_fractions']} missing"]
    for name, sample in result["samples"].items():
        lines.append(f"{name}: n={sample['n']}")
        curve = sample["hill"]
        for fraction in (.1, .2):
            k = round(fraction*sample['n'])
            i = curve['k'].index(k)
            lines.append(f"  Hill k={k}: {curve['alpha'][i]:.2f} "
                         f"[{curve['lower'][i]:.2f}, {curve['upper'][i]:.2f}]")
        fit = sample['csn']
        lines.append(f"  CSN xmin={fit['xmin']:.3f}, tail n={fit['n_tail']}, "
                     f"alpha={fit['alpha']:.2f}, SE={fit['standard_error']:.2f}, "
                     f"KS={fit['ks']:.3f}")
        lines.append(f"  GOF: {fit['gof_hits']}/{result['replicates']}")
    return '\n'.join(lines) + '\n'


def render(result, destination):
    set_theme(scale=1.15)
    destination.mkdir(parents=True, exist_ok=True)
    for name, sample in result['samples'].items():
        counts = name == 'counts'
        curve = sample['hill']
        fig, (ax,) = vertical_figure(1, panel_height=4.1)
        ax.fill_between(curve['k'], curve['lower'], curve['upper'],
                        color=COLORS['accent_light'], alpha=.2,
                        label='95% pointwise bootstrap interval')
        ax.plot(curve['k'], curve['alpha'], color=COLORS['accent'], label='Hill estimate')
        ax.axhline(1, color=COLORS['umber'], linestyle='--', linewidth=1.2,
                   label=r'Reference $\alpha=1$')
        for fraction, marker in ((.1, 'o'), (.2, 's')):
            k = round(fraction*sample['n']); i = curve['k'].index(k)
            ax.scatter([k], [curve['alpha'][i]], marker=marker, s=34,
                       facecolor=COLORS['surface'], edgecolor=COLORS['accent'], zorder=4)
            ax.axvline(k, color=COLORS['muted'], linestyle=':', linewidth=.8)
            ax.text(k, 1.02, f'{int(100*fraction)}%', transform=ax.get_xaxis_transform(),
                    ha='center', fontsize=10, color=COLORS['muted'])
        ax.set(xlabel=r'Upper observations used, $k$', ylabel=r'Tail index $\widehat{\alpha}$',
               xlim=(0, max(curve['k'])+10),
               title=('People laid off per event' if counts else 'Reported percentage log loss')
                     + f"\n{sample['n']} events",
               ylim=(0, max(curve['upper'])*1.07))
        ax.set_title(ax.get_title(), pad=27)
        ax.legend(loc='upper center', bbox_to_anchor=(.5, -.23), ncol=1)
        name = 'layoffs-counts-hill.svg' if counts else 'layoffs-logloss-hill.svg'
        savefig(fig, destination/name)
        plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument('--data', type=Path)
    inputs.add_argument('--recorded', type=Path)
    parser.add_argument('--replicates', type=int, default=1000)
    parser.add_argument('--retrieved', help='Actual input retrieval date (YYYY-MM-DD), if known')
    parser.add_argument('--figure-dir', type=Path, default=ROOT/'assets/incerto/figures')
    parser.add_argument('--output-dir', type=Path, default=ROOT/'assets/incerto/outputs')
    args = parser.parse_args()
    if args.data:
        result = calculate(args.data, args.replicates, args.retrieved)
        args.output_dir.mkdir(parents=True, exist_ok=True)
        (args.output_dir/'layoffs-tails.json').write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
        (args.output_dir/'layoffs-tails.txt').write_text(summary(result))
    else:
        result = json.loads(args.recorded.read_text())
    render(result, args.figure_dir)
    print(summary(result))


if __name__ == '__main__':
    main()
