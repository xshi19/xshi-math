"""Chapter-10 synthetic figures and optional local S&P report; never fetch data.

Run: uv run python demos/incerto/sp500_diagnostics.py
Synthetic figures are independent of local financial inputs. All normal/t3
draws use PCG64, with separate seeds per experiment. The report uses the
existing cache loader and prints no observed result if the cache is absent.
"""

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from xmath.incerto.datasets import DatasetNotAvailable, load_sp500_prices
from xmath.incerto.diagnostics import (
    aggregate_returns, chronological_tail_check, hinge_payoff, maximum_drawdown,
    moment_share_path, record_counts, sp500_diagnostics,
)
from xmath.incerto.figures import COLORS, savefig, set_theme, style_axes, vertical_figure


def report_lines(result):
    """Plain numeric presentation of the complete local-cache analysis."""
    yield f"Window: {result['start']} to {result['end']}; returns={result['returns']}"
    yield (f"Zero returns={result['zero_returns']}; "
           f"largest calendar gap={result['max_calendar_gap_days']} days")
    for label, window in result["windows"].items():
        yield f"{label}: {window['start']} to {window['end']}; n={window['n']}"
        yield f"  Maximum drawdown: {window['drawdown']:.4f}"
        for kind in ("aggregation", "overlapping"):
            for row in window[kind]:
                yield (f"  {kind} h={row['horizon']}: blocks={row['blocks']}, "
                       f"dropped={row['dropped']}, excess kurtosis={row['excess_kurtosis']:.4g}, "
                       f"MAD={row['mad']:.4g}, kappa={row['kappa']:.4g}")
        rec = window["records"]
        yield (f"  Records upper/lower: {rec['upper']:.0f}/{rec['lower']:.0f}; "
               f"iid mean={rec['iid_mean']:.3f}, variance={rec['iid_variance']:.3f}")
        yield f"  Return extrema: {rec['minimum']:.4g}, {rec['maximum']:.4g}"
        yield "  MS powers 1/2/3/4: " + ", ".join(f"{v:.4f}" for v in window["moment_shares"].values())
        for side, tail in window["tails"].items():
            yield f"  {side}: positive observations={tail['n']}"
            for point in tail["hill"]:
                yield f"    Hill k={point['k']}: alpha={point['alpha']:.4g}"
            for point in tail["conditional"]:
                yield (f"    u={point['threshold']:.4g}: count={point['exceedances']:.0f}, "
                       f"mean excess={point['mean_excess']:.4g}, ratio={point['ratio']:.4g}")
    check = result["holdout"]
    yield f"Frozen holdout: train={check['train_size']}, test={check['test_size']}"
    for method in ("gaussian", "empirical"):
        row = check[method]
        yield (f"  {method}: cutoff={row['threshold']:.4g}, hits={row['exceedances']}, "
               f"frequency={row['frequency']:.4f}, severity={row['mean_exceedance_loss']:.4g}")


def _export(fig, axes, output, name):
    style_axes(axes)
    savefig(fig, output / f"{name}.svg")
    plt.close(fig)


def main(output=None, *, local_report=True):
    output = Path(output or Path(__file__).resolve().parents[2]/"assets/figures/incerto")
    output.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)

    # 128 independent paths per parent, 4096 observations each. Bands describe
    # the distribution of the statistic, not confidence for a population moment.
    rng = np.random.default_rng(1010)
    horizons = np.array([1,4,16,64])
    fig, axes = vertical_figure(2, panel_height=3.3)
    fig.get_layout_engine().set(hspace=.13)
    for ax, title, draws, color in zip(
        axes, ("Normal: finite fourth moment", "Student t(3): infinite fourth moment"),
        (rng.normal(size=(128,4096)), rng.standard_t(3,size=(128,4096))),
        (COLORS["accent"], COLORS["brick"]),
    ):
        quantiles = []
        for h in horizons:
            sums = draws.reshape(128,-1,h).sum(axis=2)
            centered = sums-sums.mean(axis=1,keepdims=True)
            values = np.mean(centered**4,axis=1)/np.mean(centered**2,axis=1)**2-3
            quantiles.append(np.quantile(values,[.1,.5,.9]))
        low, median, high = np.asarray(quantiles).T
        ax.fill_between(horizons,low,high,color=color,alpha=.18,label="10–90% of samples")
        ax.plot(horizons,median,"o-",color=color,label="sample median")
        ax.set(xscale="log",xlabel="returns per disjoint block",ylabel="sample excess kurtosis",title=title)
        ax.set_xticks(horizons,labels=[str(h) for h in horizons])
        ax.legend(loc="upper left",bbox_to_anchor=(0,1.02),fontsize=9.5)
    axes[0].axhline(0,color=COLORS["muted"],ls=":")
    _export(fig,axes,output,"diagnostics-aggregation")

    rng = np.random.default_rng(1011)
    normal, student = rng.normal(size=3000), rng.standard_t(3,size=3000)
    n = np.arange(1,3001)
    fig, axes = vertical_figure(2,panel_height=3.3)
    fig.get_layout_engine().set(hspace=.13)
    for sample,name,color in ((normal,"normal",COLORS["accent"]),(student,"Student t(3)",COLORS["brick"])):
        axes[0].semilogx(n,moment_share_path(sample),color=color,label=name)
    axes[0].set(xlabel="prefix length",ylabel="largest fourth-power share",ylim=(0,1.03),title="One synthetic path per parent")
    axes[0].legend(loc="lower left")
    records=record_counts(student)
    axes[1].semilogx(n,records["upper"],label="upper records")
    axes[1].semilogx(n,records["lower"],label="lower records",ls="--")
    axes[1].semilogx(n,records["iid_mean"],label="iid mean H(n)",ls=":",color=COLORS["muted"])
    axes[1].set(xlabel="prefix length",ylabel="record count",title="Same Student path; continuous iid model")
    axes[1].legend(loc="upper left",bbox_to_anchor=(0,1.02),fontsize=9.5)
    _export(fig,axes,output,"diagnostics-moments-records")

    fig, axes = vertical_figure(2,panel_height=3.3)
    fig.get_layout_engine().set(hspace=.13)
    for p,label in (([100,120,90,140,84,110],"A"),([100,84,90,110,120,140],"B")):
        axes[0].plot(p,"o-",label=f"{label}: max decline {maximum_drawdown(p):.0%}")
    axes[0].set(xlabel="observation order",ylabel="synthetic price",title="Same prices, different drawdowns")
    axes[0].legend(loc="upper left",fontsize=9.5)
    u=np.geomspace(1,30,150)
    axes[1].semilogx(u,np.full_like(u,3),label="Pareto exponent 1.5")
    axes[1].semilogx(u,1+1/u,label="unit exponential",ls="--")
    axes[1].axhline(1,color=COLORS["muted"],ls=":")
    axes[1].set(xlabel="positive threshold u",ylabel="conditional mean / u",title="Population ratios under specified laws")
    axes[1].legend(loc="center right",fontsize=9.5)
    _export(fig,axes,output,"diagnostics-drawdown-ratio")

    # Fixed 255 observations plus one growing loss; use the training side of
    # the same holdout routine. The unused test point is zero and never fitted.
    base=np.random.default_rng(1012).normal(size=255)
    extremes=np.linspace(2,40,120)
    gaussian, empirical, severity=[],[],[]
    for value in extremes:
        losses=np.r_[base,value]
        fit=chronological_tail_check(np.r_[-losses,0],train_size=256)
        gaussian.append(fit["gaussian"]["threshold"])
        empirical.append(fit["empirical"]["threshold"])
        severity.append(losses[losses>fit["empirical"]["threshold"]].mean())
    fig,axes=vertical_figure(2,panel_height=3.1)
    fig.get_layout_engine().set(hspace=.13)
    axes[0].plot(extremes,gaussian,label="Gaussian fit")
    axes[0].plot(extremes,empirical,label="empirical quantile",ls="--")
    axes[0].set(ylabel="95% loss cutoff",title="One changing observation out of 256")
    axes[0].legend()
    axes[1].plot(extremes,severity,color=COLORS["brick"])
    axes[1].set(ylabel="mean above empirical cutoff",title="Tail severity still changes")
    for ax in axes: ax.set_xlabel("replacement loss (normal scale units)")
    _export(fig,axes,output,"pipeline-contamination")

    fig,axes=vertical_figure(2,panel_height=3.1)
    fig.get_layout_engine().set(hspace=.13)
    x=np.linspace(-2,5,300)
    axes[0].plot(x,hinge_payoff(x,[0,2],[.5,1.5,-.5]),color=COLORS["accent"])
    for knot in (0,2): axes[0].axvline(knot,color=COLORS["muted"],ls=":")
    axes[0].text(-1.85,.1,"slope 0.5",fontsize=9)
    axes[0].text(.1,2.5,"slope 1.5",fontsize=9)
    axes[0].text(2.6,2.8,"slope −0.5",fontsize=9)
    axes[0].set(xlabel="input x",ylabel="piecewise-linear response",title="Hinge weights are slope changes: +1, −2")
    axes[1].plot(x,np.maximum(x,0),label="hinge",lw=2.5)
    for a,ls in ((1,"--"),(4,":")):
        axes[1].plot(x,np.logaddexp(0,a*x)/a,label=f"softplus, a={a}",ls=ls)
    axes[1].set(xlabel="input x",ylabel="response",title="Smoothing keeps a linear right tail")
    axes[1].legend()
    _export(fig,axes,output,"hinge-calibration")
    print("Generated five synthetic/model figures; seeds 1010, 1011, 1012.")
    if local_report:
        try:
            prices=load_sp500_prices(fetch=False)
        except DatasetNotAvailable:
            print("No local S&P cache; empirical diagnostics remain uncomputed.")
        else:
            print("\n".join(report_lines(sp500_diagnostics(prices))))


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    main(parser.parse_args().output)
