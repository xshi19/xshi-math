"""Bounded numerical examples for averaging and limit laws.

No sampler truncates a parent law or silently removes nonfinite observations.
Analytic functions distinguish infinite moments from floating-point overflow.
"""

from numbers import Integral

import numpy as np
from scipy.special import gammaincc, gammaln, xlogy


def _scalar(value, name, *, positive=False):
    if isinstance(value, (bool, np.bool_)) or np.iscomplexobj(value) or np.ndim(value) != 0:
        raise ValueError(f"{name} must be a finite real scalar")
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError(f"{name} must be a finite real scalar") from error
    if not np.isfinite(result) or (positive and result <= 0):
        raise ValueError(f"{name} must be finite" + (" and positive" if positive else ""))
    return result


def _count(value, name):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, Integral) or not 1 <= value <= 2**53:
        raise ValueError(f"{name} must be an integer in [1, 2**53]")
    return int(value)


def pareto_capped_mean(cap, alpha, *, x_m=1.0):
    """E[min(X, cap)] for exact Pareto(alpha, x_m); finite nonnegative caps.

    Scalar or array caps are accepted. For cap <= x_m the answer is cap.
    The alpha=1 logarithmic boundary uses a continuous expm1 expression.
    This is not E[X 1{X <= cap}]. Overflow raises, not mathematical infinity.
    """
    alpha, x_m = _scalar(alpha, "alpha", positive=True), _scalar(x_m, "x_m", positive=True)
    if np.iscomplexobj(cap):
        raise ValueError("caps must be finite nonnegative reals")
    try:
        cap = np.asarray(cap, dtype=float)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("caps must be finite nonnegative reals") from error
    if np.any(~np.isfinite(cap)) or np.any(cap < 0):
        raise ValueError("caps must be finite nonnegative reals")
    result = cap.copy()
    mask = cap > x_m
    # Logarithms separately avoid overflowing cap/x_m.
    log_ratio = np.log(cap[mask]) - np.log(x_m)
    with np.errstate(over="ignore"):
        z = (1-alpha)*log_ratio  # -inf is a valid expm1 saturation for huge alpha.
    # cap * exp(-alpha*log_ratio) avoids an overflowing power before scaling.
    if alpha < 1:
        growth = cap[mask]*np.exp(-alpha*log_ratio)
        # Near alpha=1 cancellation matters more than extreme-scale overflow.
        factor = np.empty_like(z)
        near = np.abs(z) < .5
        factor[near] = x_m*np.expm1(z[near])/(1-alpha)
        factor[~near] = (growth[~near]-x_m)/(1-alpha)
    elif alpha == 1:
        factor = x_m*log_ratio
    else:
        factor = x_m*(-np.expm1(z))/(alpha-1)
    with np.errstate(over="raise", invalid="raise"):
        result[mask] = x_m + factor
    if np.any(~np.isfinite(result)):
        raise FloatingPointError("capped mean not representable")
    return float(result) if result.ndim == 0 else result


def symmetric_stable_mean_abs(alpha, *, scale=1.0, n=1):
    """E[|sample mean - location|], CF exp(i*mu*t - |scale*t|**alpha).

    alpha in (0,2], scale > 0, integer n >= 1. Returns inf for alpha <= 1.
    At alpha=2 the parent variance is 2*scale**2. Finite-result overflow raises.
    """
    alpha = _scalar(alpha, "alpha", positive=True)
    scale = _scalar(scale, "scale", positive=True)
    n = _count(n, "n")
    if alpha > 2:
        raise ValueError("alpha must be at most 2")
    if alpha <= 1:
        return float("inf")
    log_value = np.log(2/np.pi) + np.log(scale) + gammaln(1-1/alpha) + (1/alpha-1)*np.log(n)
    with np.errstate(over="raise", invalid="raise"):
        return float(np.exp(log_value))


def repeated_centered_sums(rv, sizes, *, center=0.0, repetitions=600,
                           random_state=0, batch=32):
    """Independent samples at each size; return (len(sizes), repetitions) sums.

    rv is a frozen law with rvs(size=..., random_state=Generator). center is a
    specified per-observation centering, not an estimated mean. Each call draws
    rows in batches, using one PCG64 stream (or the passed Generator). Rejects
    nonfinite draws/results. Experiment limit: 50 million total draws and at
    most 1 million observations per sample; sampling memory is O(batch*max(sizes)).
    """
    center = _scalar(center, "center")
    repetitions, batch = _count(repetitions, "repetitions"), _count(batch, "batch")
    values = np.asarray(sizes)
    if values.ndim != 1 or not values.size or values.dtype.kind not in "iu":
        raise ValueError("sizes must be a nonempty integer vector")
    ns = [_count(v, "size") for v in values]
    if max(ns) > 1_000_000 or sum(ns)*repetitions > 50_000_000:
        raise ValueError("experiment exceeds the 50-million-draw budget or size limit")
    rng = np.random.default_rng(random_state)
    result = np.empty((len(ns), repetitions))
    for index, n in enumerate(ns):
        for start in range(0, repetitions, batch):
            stop = min(start+batch, repetitions)
            sample = np.asarray(rv.rvs(size=(stop-start, n), random_state=rng))
            if sample.shape != (stop-start, n) or np.iscomplexobj(sample) or not np.all(np.isfinite(sample)):
                raise FloatingPointError("sampler returned invalid or nonfinite observations")
            with np.errstate(over="raise", invalid="raise"):
                result[index, start:stop] = np.sum(sample-center, axis=1)
    if not np.all(np.isfinite(result)):
        raise FloatingPointError("nonfinite centered sum; no observations removed")
    return result


def pareto_plugin_nonfinite_probability(alpha, n):
    """P(known-cutoff Pareto mean fit is infinite), for true alpha > 0.

    The log-excess sum has Gamma(shape=n, rate=alpha) law. Returns its survival
    at n; exact continuous-model probability, not a Monte Carlo estimate.
    The cutoff cancels. Tiny representable probabilities can underflow to zero.
    """
    alpha = _scalar(alpha, "alpha", positive=True)
    n = _count(n, "n")
    return float(gammaincc(n, alpha*n))


def bernoulli_chernoff_log_bound(p, q, n):
    """Log Chernoff upper bound on P(S_n >= n*q), iid Bernoulli(p).

    0 < p < 1, 0 <= q <= 1; returns 0 (bound one) when q <= p.
    At q=1 the all-success bound n*log(p) is exact. This is not a log-tail
    approximation. n is a positive integer no greater than 2**53.
    """
    p, q, n = _scalar(p, "p"), _scalar(q, "q"), _count(n, "n")
    if not 0 < p < 1 or not 0 <= q <= 1:
        raise ValueError("require 0 < p < 1 and 0 <= q <= 1")
    if q <= p:
        return 0.0
    delta = q-p
    if delta < .5*min(p, 1-p):
        # Avoid cancelling four order-one terms when q is close to p.
        divergence = q*np.log1p(delta/p) + (1-q)*np.log1p(-delta/(1-p))
    else:
        divergence = xlogy(q, q) - q*np.log(p) + xlogy(1-q, 1-q) - (1-q)*np.log1p(-p)
    return float(-n*max(0.0, divergence))


__all__ = ["pareto_capped_mean", "symmetric_stable_mean_abs", "repeated_centered_sums",
           "pareto_plugin_nonfinite_probability", "bernoulli_chernoff_log_bound"]
