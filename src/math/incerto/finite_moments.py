"""Finite-mixture and empirical-moment calculations for SCoFT chapter 4.

These evaluate specified laws, not fitted tail classes. Floating-point
underflow in densities is avoided with log probabilities; an unrepresentable
finite result raises FloatingPointError instead of impersonating a moment gate.
"""

from __future__ import annotations

from numbers import Integral

import numpy as np
from numpy.typing import ArrayLike
from scipy.special import gammaln, logsumexp
from scipy.stats import norm


def _positive(value: float, name: str) -> float:
    value = float(value)
    if not np.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")
    return value


def _mixture(variances: ArrayLike, weights: ArrayLike):
    v, w = np.asarray(variances, dtype=float), np.asarray(weights, dtype=float)
    if (v.ndim != 1 or v.size == 0 or w.shape != v.shape
            or not np.all(np.isfinite(v)) or np.any(v <= 0)
            or not np.all(np.isfinite(w)) or np.any(w < 0)
            or not np.isclose(w.sum(), 1, rtol=0, atol=1e-12)):
        raise ValueError("positive finite variances and nonnegative weights summing to one required")
    active = w > 0
    return v[active], w[active] / w.sum()


def _finite(result):
    if not np.all(np.isfinite(result)):
        raise FloatingPointError("finite model result exceeds floating-point range")
    return float(result) if np.ndim(result) == 0 else result


def normal_mixture_log_density(x: ArrayLike, variances: ArrayLike, weights: ArrayLike):
    """Log density of a finite centered Gaussian variance mixture.

    Supports scalar or array x, finite positive component variances and zero
    weights. At extremely large x even a log density may exceed float range.
    """
    v, w = _mixture(variances, weights)
    x = np.asarray(x, dtype=float)
    if not np.all(np.isfinite(x)):
        raise ValueError("x must be finite")
    with np.errstate(over="ignore", invalid="ignore"):
        z = x[..., None] / np.sqrt(v)
        # Halve before squaring: z**2 can overflow while z**2/2 is finite.
        components = (-0.5 * z) * z - 0.5 * (np.log(2*np.pi) + np.log(v))
    return _finite(logsumexp(components + np.log(w), axis=-1))


def normal_mixture_log_abs_survival(u: ArrayLike, variances: ArrayLike, weights: ArrayLike):
    """Log P(|X| > u) for finite nonnegative thresholds under the mixture."""
    v, w = _mixture(variances, weights)
    u = np.asarray(u, dtype=float)
    if not np.all(np.isfinite(u)) or np.any(u < 0):
        raise ValueError("u must be nonnegative and finite")
    with np.errstate(over="ignore", invalid="ignore"):
        components = np.log(2) + norm.logsf(u[..., None] / np.sqrt(v))
    result = logsumexp(components + np.log(w), axis=-1)
    return _finite(np.where(u == 0, 0.0, np.minimum(result, 0.0)))


def normal_mixture_absolute_moment(q: float, variances: ArrayLike, weights: ArrayLike) -> float:
    """Return E|X|**q for q > 0; all such moments exist for this finite mixture."""
    q = _positive(q, "q")
    v, w = _mixture(variances, weights)
    with np.errstate(over="ignore", invalid="ignore", under="ignore"):
        log_c = q / 2 * np.log(2) + gammaln((q + 1) / 2) - np.log(np.pi) / 2
        result = np.exp(log_c + logsumexp(np.log(w) + q / 2 * np.log(v)))
    if result == 0:
        raise FloatingPointError("positive moment underflows floating-point range")
    return _finite(result)


def pareto_moment_estimator_summary(alpha: float, q: float, n: int, x_m: float = 1.0):
    """Target and variance of n^-1 sum X_i**q for iid exact Pareto draws.

    An infinite target returns variance NaN (no finite centering). A finite
    target with alpha <= 2q returns variance infinity. Counts are positive
    integers <= 2**53, to keep their float conversion exact.
    """
    alpha, q, x_m = (_positive(alpha, "alpha"), _positive(q, "q"), _positive(x_m, "x_m"))
    if isinstance(n, (bool, np.bool_)) or not isinstance(n, Integral) or not 1 <= n <= 2**53:
        raise ValueError("n must be an integer in [1, 2**53]")
    if q >= alpha:
        return {"moment": float("inf"), "estimator_variance": float("nan")}
    log_m = np.log(alpha) + q * np.log(x_m) - np.log(alpha-q)
    with np.errstate(over="ignore", under="ignore"):
        moment = _finite(np.exp(log_m))
    if moment == 0:
        raise FloatingPointError("positive moment underflows floating-point range")
    # Doubling is exact unless it overflows (which also puts us above alpha).
    # Halving a subnormal alpha can round down onto q and misclassify the gate.
    if 2*q >= alpha:
        variance = float("inf")
    else:
        # Algebraically reduced positive formula avoids subtracting close moments.
        log_v = (np.log(alpha) + 2*np.log(q) + 2*q*np.log(x_m)
                 - np.log(alpha-2*q) - 2*np.log(alpha-q) - np.log(n))
        with np.errstate(over="ignore", under="ignore"):
            variance = _finite(np.exp(log_v))
        if variance == 0:
            raise FloatingPointError("positive estimator variance underflows floating-point range")
    return {"moment": moment, "estimator_variance": variance}


def power_mean(sample: ArrayLike, order: float) -> float:
    """Normalized absolute power mean, order >= 1 or +infinity.

    Rescale by the largest magnitude before exponentiation. Zero samples
    return zero, and infinity selects the maximum rather than a finite power.
    """
    x = np.asarray(sample, dtype=float)
    if x.ndim != 1 or x.size == 0 or not np.all(np.isfinite(x)):
        raise ValueError("sample must be nonempty, finite and one-dimensional")
    order = float(order)
    if np.isnan(order) or order < 1:
        raise ValueError("order must be >= 1, possibly infinity")
    maximum = np.max(np.abs(x))
    if maximum == 0 or np.isposinf(order):
        return float(maximum)
    result = float(maximum * np.mean((np.abs(x) / maximum)**order)**(1/order))
    if result == 0:
        raise FloatingPointError("positive power mean underflows floating-point range")
    return result
