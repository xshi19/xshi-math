"""Regenerate the Rayleigh comparison: uv run python demos/incerto/rayleigh_speed.py.

50,000 iid 2D canonical speeds; seed 20261022; kT/m=1. No data downloads.
Writes two single-column SVGs and prints the same fit diagnostics as the note.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from xmath.incerto.figures import savefig
from xmath.incerto.gas_speeds import (
    fit_speed_models,
    sample_chi_speed,
    speed_fit_figure,
    speed_fit_table,
    squared_speed_ks,
)


def main():
    speeds = sample_chi_speed(50_000, random_state=20261022)
    fits = fit_speed_models(speeds)
    print(speed_fit_table(fits))
    energy = squared_speed_ks(speeds)
    print(f"V^2 vs Exp(mean 2): D={energy['statistic']:.4f}, p={energy['pvalue']:.4f}")
    output = Path(__file__).resolve().parents[2] / "assets/figures/incerto"
    output.mkdir(parents=True, exist_ok=True)
    for kind, name in (("density", "fits"), ("qq", "qq")):
        fig = speed_fit_figure(speeds, fits, kind=kind)
        path = savefig(fig, output / f"rayleigh-speed-{name}.svg")
        plt.close(fig)
        print(f"Wrote {path.name}")


if __name__ == "__main__":
    main()
