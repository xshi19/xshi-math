"""Chapter 5 and appendix B: bounded deterministic population calculations.

Run: uv run python demos/incerto/power_laws.py
Four SVGs, fixed grids, no RNG/external data/censoring/fitted parameters.
81 convolution thresholds per law, rtol=1e-9, maxlevel=12; failed quadrature
stops the run. Ordinary runtime is seconds. Finite curves do not prove limits.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.stats import expon, gamma, logistic, norm, pareto, t, weibull_min

from xmath.incerto.distributions import double_pareto
from xmath.incerto.figures import COLORS, savefig, set_theme
from xmath.incerto.power_laws import (
    entropy_log_constraint_example,
    pareto_product_logsf,
    pareto_truncated_moment,
    q_exponential_logsf,
    student_double_pareto_scales,
)
from xmath.incerto.tail_diagnostics import iid_two_sum_tail


def export(fig, output, name):
    for ax in fig.axes:
        for line in ax.lines:
            if not np.all(np.isfinite(line.get_ydata())):
                raise FloatingPointError(f"nonfinite plotted curve: {name}")
        if ax.get_legend() is None:
            ax.legend(fontsize=10, handlelength=3.5, loc="upper center",
                      bbox_to_anchor=(.5, -.24))
    savefig(fig, output / name)
    plt.close(fig)


def main():
    output = Path(__file__).resolve().parents[2] / "assets/figures/incerto"
    output.mkdir(parents=True, exist_ok=True)
    set_theme(scale=1.1)

    fig, axes = plt.subplots(3, 1, figsize=(5, 13), layout="constrained")
    u = np.geomspace(1, 16, 241)
    models = ((pareto(1.5), "Pareto 1.5", "-"),
              (weibull_min(.5), "Weibull 0.5", "--"),
              (expon(), "Exponential", "-."),
              (logistic(), "Logistic", ":"),
              (norm(), "Normal", "-"))
    for rv, label, style in models:
        target = axes[1] if label in {"Exponential", "Logistic"} else axes[0]
        target.plot(u, 2*rv.logsf(u)-rv.logsf(2*u), style, label=label)
    axes[0].set(xlabel="Threshold u", ylabel="Log squared-survival ratio",
                yscale="symlog", title="Two exceedances versus one at 2u")
    axes[0].set_yticks([-4, -2, -1, 0, 1, 2, 10, 100],
                      labels=["-4", "-2", "-1", "0", "1", "2", "10", "100"])
    axes[1].set(xlabel="Threshold u", ylabel="Log squared-survival ratio",
                ylim=(-.55, .05), title="Linear detail: exponential and logistic")
    u = np.geomspace(3, 1e4, 81)
    for rv, label, style in models[:3]:
        result = iid_two_sum_tail(rv, u, rtol=1e-9, maxlevel=12)
        if not np.all(result["success"]) or not np.all(np.isfinite(result["log_ratio"])):
            raise FloatingPointError(f"convolution failed: {label}")
        axes[2].plot(u, result["ratio"], style, label=label)
        print(f"{label} two-sum ratio at 3/1e4: {result['ratio'][0]:.9g}, "
              f"{result['ratio'][-1]:.9g}; max quadrature evaluations {max(result['nfev']):.0f}")
    axes[2].axhline(1, color=COLORS["muted"], linewidth=1, label="Subexponential limit")
    axes[2].set(xscale="log", yscale="log", xlabel="Threshold u", ylabel="Two-sum ratio R(u)",
                title="A separate convolution question")
    export(fig, output, "power-law-diagnostics.svg")

    fig, axes = plt.subplots(3, 1, figsize=(5, 13), layout="constrained")
    u = np.geomspace(1, 1e4, 241)
    for a, b, label, style in ((1, 2, "Independent: 1 and 2", "-"),
                               (1, 1, "Independent: 1 and 1", "--")):
        axes[0].plot(u, np.exp(pareto_product_logsf(np.log(u), a, b)), style, label=label)
    axes[0].plot(u, 1/u, ":", label="Single Pareto 1")
    axes[0].set(xscale="log", yscale="log", xlabel="Product threshold", ylabel="Survival",
                title="Equal exponents add a log factor")
    for p, style in ((1, "-"), (1.5, "--"), (2, "-.")):
        axes[1].plot(u[1:], pareto_truncated_moment(u[1:], 1.5, p), style, label=f"Order {p:g}")
    axes[1].set(xscale="log", yscale="log", xlabel="Upper cutoff b",
                ylabel="Truncated moment", title="Below, at, and above the boundary")
    u = np.geomspace(1.01, 1e4, 241)
    for rho, style in ((0, "-"), (1, "--")):
        v = (rho+1)*np.log(u)
        ratio = 1 + np.expm1(-v)/v
        axes[2].plot(u, ratio, style, label=f"Power rho = {rho}")
    axes[2].axhline(1, color=COLORS["muted"], linewidth=1, label="Karamata limit")
    axes[2].set(xscale="log", xlabel="Upper limit x", ylabel="Integral / leading term",
                title="A slowly varying logarithmic factor")
    export(fig, output, "power-law-integrals.svg")

    scales = student_double_pareto_scales(3)
    print("Student / double-Pareto matching:", scales)
    dp = double_pareto(3)
    student_models = ((t(3, scale=scales["tail_scale"]), "Student: tail matched", "--"),
                      (t(3, scale=scales["variance_scale"]), "Student: variance matched", "-."))
    fig, axes = plt.subplots(3, 1, figsize=(5, 13), layout="constrained")
    x, u = np.linspace(-4, 4, 501), np.geomspace(1, 1e4, 241)
    axes[0].plot(x, dp.pdf(x), label="Double Pareto")
    axes[2].plot(u, np.exp(dp.logsf(2*u)-dp.logsf(u)), label="Double Pareto")
    for rv, label, style in student_models:
        axes[0].plot(x, rv.pdf(x), style, label=label)
        axes[1].plot(u, np.exp(rv.logsf(u)-dp.logsf(u)), style, label=label)
        axes[2].plot(u, np.exp(rv.logsf(2*u)-rv.logsf(u)), style, label=label)
    for target, style in ((1, ":"), (4/(3*np.pi), "-")):
        axes[1].axhline(target, color=COLORS["muted"], linewidth=1, linestyle=style,
                        label=f"Tail target {target:.3f}")
    axes[0].set(xlabel="Outcome x", ylabel="Density", title="Same exponent, different central shapes")
    axes[1].set(xscale="log", xlabel="Threshold u", ylabel="Student / double-Pareto tail",
                title="Tail matching differs from variance matching")
    axes[2].axhline(1/8, color=COLORS["muted"], linewidth=1, label="Limit 1/8")
    axes[2].set(xscale="log", xlabel="Threshold u", ylabel="Survival at 2u / survival at u",
                title="All three approach the same power ratio")
    export(fig, output, "power-law-matching.svg")

    result = entropy_log_constraint_example()
    print("Entropy constraints and KL:", result)
    fig, axes = plt.subplots(2, 1, figsize=(5, 7.5), layout="constrained")
    z = np.linspace(0, 3, 301)
    axes[0].plot(z, gamma.pdf(z, 1, scale=.5), label="Pareto in log coordinate")
    axes[0].plot(z, gamma.pdf(z, 2, scale=.25), "--", label="Log-gamma alternative")
    axes[0].set(xlabel="Log size z = log x", ylabel="Density of z",
                title="Same log-moment, different entropy")
    x = np.linspace(0, 6, 301)
    for q, style in ((.75, "-"), (1, "--"), (1.25, "-."), (1.6, ":")):
        axes[1].plot(x, np.exp(q_exponential_logsf(x, q, 2)), style, label=f"q = {q:g}")
    axes[1].set(xlabel="Threshold x", ylabel="Survival", title="Normalization restricts the q family")
    export(fig, output, "power-law-entropy.svg")

    # Whole-tail boundary moment in z=log(x) coordinates: alpha=2, v_m=1.
    tail_integral, error = quad(lambda z: z**-2, 1, np.inf, epsabs=1e-10)
    if error > 1e-9:
        raise FloatingPointError("boundary integral failed")
    print(f"Finite RV boundary moment: {np.e**2*(1+2*tail_integral):.9f}")
    print("Log-Pareto survivals at log(x)=2,4,8:", 1/np.array([2., 4., 8.])**2)
    print("All four figures exported; no failed quadrature or nonfinite plotted values.")


if __name__ == "__main__":
    main()
