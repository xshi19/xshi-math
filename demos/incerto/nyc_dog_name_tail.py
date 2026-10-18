"""Reproduce static nyc-dog-name-tail figures; run from the installed repository.

Adapted from incerto-wiki 9717c9cf83aee18b47f423a14bce2f0d14bb8bcb, content/concepts/examples/nyc-dog-name-tail.md.
Copyright (c) 2023 xshi19; MIT (see THIRD_PARTY_NOTICES.md).
No network access or notebook execution is required.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
OUTPUT = Path(__file__).resolve().parents[2] / "assets/incerto/figures"
OUTPUT.mkdir(parents=True, exist_ok=True)


import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, ScalarFormatter, NullFormatter
import numpy as np
from scipy.stats import genpareto, linregress, lognorm

from xmath.incerto.datasets import load_nyc_dog_name_frequencies
from xmath.incerto.estimators import hill_stability
from xmath.incerto.figures import COLORS, FIGURE_SIZES, savefig, set_theme, style_axes

set_theme()

data = load_nyc_dog_name_frequencies()
frequencies = data.frequency.astype(float)
ordered = np.sort(frequencies)
n = ordered.size
empirical_survival = 1 - np.arange(1, n + 1) / (n + 1)

# Rank-frequency view, from the most common name down to the one-offs.
ranked_frequency = ordered[::-1]
name_rank = np.arange(1, n + 1)
slope, intercept, r_value, _, _ = linregress(
    np.log(name_rank), np.log(ranked_frequency)
)

fig, ax = plt.subplots(figsize=FIGURE_SIZES["single"], layout="constrained")
ax.scatter(
    name_rank,
    ranked_frequency,
    rasterized=True,
    s=10,
    alpha=0.35,
    color=COLORS["accent"],
)
rank_grid = np.geomspace(name_rank.min(), name_rank.max(), 200)
ax.plot(
    rank_grid,
    np.exp(intercept) * rank_grid**slope,
    color=COLORS["umber"],
    linestyle="--",
    label=f"log-log slope {slope:.2f}",
)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("name popularity rank")
ax.set_ylabel("license-period frequency")
ax.set_title("Dog-name rank-frequency relation")
ax.legend()
style_axes(ax, grid_axis="both")
savefig(fig, OUTPUT / "nyc-dog-name-tail-1.svg", metadata={"Date": None})
plt.close()

# Descriptive whole-sample baseline: a two-parameter lognormal with location 0.
lognormal_shape, _, lognormal_scale = lognorm.fit(frequencies, floc=0.0)
fitted_survival = lognorm.sf(
    ordered,
    lognormal_shape,
    loc=0.0,
    scale=lognormal_scale,
)

# Hill sensitivity over upper order statistics.
report_ks = np.array([50, 100, 200, 500, 1_000, 2_000, 5_000])
ks = np.unique(
    np.concatenate(
        [np.geomspace(25, min(8_000, n // 3), 100).astype(int), report_ks]
    )
)
hill = hill_stability(frequencies, ks)
hill_k = hill["k"].astype(int)
hill_threshold = ordered[-(hill_k + 1)]
hill_order = np.argsort(hill_threshold)

# GPD shape sensitivity over fixed integer thresholds.
gpd_thresholds = np.unique(np.geomspace(20, 500, 28).round().astype(int))
gpd_xi = []
gpd_exceedances = []
for threshold in gpd_thresholds:
    excesses = frequencies[frequencies > threshold] - threshold
    xi_hat, loc_hat, _ = genpareto.fit(excesses, floc=0.0)
    if abs(loc_hat) > 1e-10:
        raise RuntimeError("GPD fit did not respect the fixed zero location")
    gpd_xi.append(xi_hat)
    gpd_exceedances.append(excesses.size)

gpd_xi = np.array(gpd_xi)
gpd_exceedances = np.array(gpd_exceedances)

fig, ax = plt.subplots(figsize=FIGURE_SIZES["single"], layout="constrained")
ax.loglog(
    ordered,
    empirical_survival,
    color=COLORS["accent"],
    label="empirical",
)
ax.loglog(
    ordered,
    fitted_survival,
    color=COLORS["umber"],
    linestyle="--",
    label="whole-sample lognormal",
)
ax.set_xlabel("license-period frequency")
ax.set_ylabel("survival across names")
ax.set_title("Global frequency fit")
ax.legend()
style_axes(ax, grid_axis="both")
savefig(fig, OUTPUT / "nyc-dog-name-tail-2.svg", metadata={"Date": None})
plt.close()

fig, axes = plt.subplots(1, 2, figsize=FIGURE_SIZES["two_panel"], layout="constrained")

axes[0].semilogx(
    hill_threshold[hill_order],
    hill["alpha"][hill_order],
    color=COLORS["green"],
)
axes[0].set_xlabel("empirical threshold")
axes[0].set_ylabel(r"Hill $\widehat\alpha$")
axes[0].set_title("Pareto-exponent sensitivity")

xi_line = axes[1].semilogx(
    gpd_thresholds,
    gpd_xi,
    marker="o",
    color=COLORS["teal"],
    label=r"GPD $\widehat\xi$",
)
count_axis = axes[1].twinx()
count_line = count_axis.semilogx(
    gpd_thresholds,
    gpd_exceedances,
    color=COLORS["muted"],
    linestyle=":",
    label="exceedances",
)
axes[1].xaxis.set_major_locator(FixedLocator([20, 50, 100, 200, 500]))
axes[1].xaxis.set_major_formatter(ScalarFormatter())
axes[1].xaxis.set_minor_formatter(NullFormatter())
axes[1].set_xlabel("fixed threshold")
axes[1].set_ylabel(r"GPD $\widehat\xi$")
count_axis.set_ylabel("exceedances")
axes[1].set_title("GPD threshold sensitivity")
axes[1].legend(
    xi_line + count_line,
    [line.get_label() for line in xi_line + count_line],
)

style_axes([*axes, count_axis], grid_axis="both")
savefig(fig, OUTPUT / "nyc-dog-name-tail-3.svg", metadata={"Date": None})
plt.close()

print("NYC dog-name frequencies")
print(f"  Normalized names: {data.name.size:,}")
print(f"  Included license-period records: {data.frequency.sum():,}")
print(f"  Largest name frequency: {data.frequency.max():,}")
print(f"  Rank-frequency log-log slope: {slope:.3f} (R^2={r_value**2:.3f})")
print(
    "  Whole-sample lognormal parameters: "
    f"shape={lognormal_shape:.3f}, scale={lognormal_scale:.3f}"
)
print("\nSelected tail-sensitivity points")
for k in report_ks:
    index = np.flatnonzero(hill_k == k)
    if index.size:
        i = index[0]
        print(
            f"  k={k:5,d}; threshold={hill_threshold[i]:6.0f}; "
            f"Hill alpha={hill['alpha'][i]:.3f}"
        )

lookup_name = "Safari"
lookup_frequency = data.frequency_for(lookup_name)
print(
    f"{lookup_name}: {lookup_frequency:,} included license-period "
    f"record{'s' if lookup_frequency != 1 else ''}"
)

# Keep Matplotlib's SVG path continuations clean in source control.
for output in OUTPUT.glob("nyc-dog-name-tail-*.svg"):
    output.write_text("\n".join(line.rstrip() for line in output.read_text().splitlines()) + "\n")
