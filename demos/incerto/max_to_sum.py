"""P1 running max/sum and pointwise repeated-sample quantiles.

Run: uv run python demos/incerto/max_to_sum.py
Exact iid Pareto, minimum 1, alpha=.8/1/1.3. PCG64 independent path streams
20261030..32 and ensemble streams 20261040..42. Three paths per law (all
30000 prefixes); 400 independent replication paths summarized at 100 fixed
checkpoints. One path at a time bounds memory. No truncation or censoring.
Bands are 10th/90th sampling percentiles, not confidence or simultaneous
bands. Finite simulations do not prove the cited limits. Runtime: seconds.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from xmath.incerto.distributions import pareto_type1
from xmath.incerto.estimators import max_to_sum_path
from xmath.incerto.figures import COLORS, savefig, set_theme, vertical_figure


def main(output=None):
    output = Path(output) if output is not None else Path(__file__).resolve().parents[2] / "assets/figures/incerto"
    output.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)
    size, reps = 30000, 400
    n = np.arange(1, size+1)
    checkpoints = np.unique(np.geomspace(1, size, 100).astype(int))
    fig, axes = vertical_figure(6, panel_height=3.1)
    for i, (alpha, color, regime) in enumerate(zip((.8, 1., 1.3),
            (COLORS["brick"], COLORS["umber"], COLORS["green"]),
            ("infinite mean", "infinite-mean boundary", "finite mean"))):
        ax, band = axes[2*i:2*i+2]
        rng = np.random.default_rng(20261030+i)
        for path in range(3):
            sample = pareto_type1.rvs(alpha, size=size, random_state=rng)
            ax.plot(n, max_to_sum_path(sample), ("-", "--", "-.")[path],
                    color=color, alpha=1-.2*path, linewidth=1.1, label=f"Path {path+1}")
        ax.set_title(f"Pareto α = {alpha:g} · {regime}\nThree independent paths")
        rng = np.random.default_rng(20261040+i)
        results = np.empty((reps, len(checkpoints)))
        for rep in range(reps):
            sample = pareto_type1.rvs(alpha, size=size, random_state=rng)
            results[rep] = max_to_sum_path(sample)[checkpoints-1]
        lower, median, upper = np.quantile(results, [.1, .5, .9], axis=0)
        band.fill_between(checkpoints, lower, upper, color=color, alpha=.2, label="10th–90th percentiles")
        band.plot(checkpoints, median, color=color, label="Median · 400 replications")
        band.set_title(f"α = {alpha:g} · pointwise sampling quantiles")
        for target in (ax, band):
            target.set(xscale="log", xlim=(1, size), ylim=(0, 1.02),
                       xlabel="Prefix size n (log scale)", ylabel="Maximum / sum")
            target.legend(loc="upper center", bbox_to_anchor=(.5, -.26), handlelength=3,
                           ncol=3 if target is ax else 1)
        print(f"alpha={alpha:g}, n={size}, 10/50/90 percentiles: "
              + ", ".join(f"{v:.4g}" for v in (lower[-1], median[-1], upper[-1])))
    savefig(fig, output / "max-to-sum.svg")
    plt.close(fig)


if __name__ == "__main__":
    main()
