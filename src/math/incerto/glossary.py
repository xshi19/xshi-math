"""Exact population calculations for the chapter-2 glossary worked cases."""

import math
import operator
from decimal import Decimal, localcontext

import numpy as np
from numpy.typing import ArrayLike, NDArray


def pareto_tail_quantities(
    alpha: float, x_m: float, threshold: float
) -> dict[str, float]:
    """Return log survival, mean excess, conditional mean and tail first moment.

    Use an exact Pareto Type I law, finite alpha > 0 and threshold >= x_m > 0.
    The tail first moment is E[X * 1{X > threshold}], not a conditional mean.
    For alpha <= 1 all three expectations are mathematically +infinity.
    For alpha > 1, overflowing finite expectations raise OverflowError.
    Log survival avoids probability underflow; positive expectations below
    the floating-point range may round to zero. No sampling or fitting.
    """
    if not all(math.isfinite(v) for v in (alpha, x_m, threshold)):
        raise ValueError("alpha, x_m and threshold must be finite")
    if alpha <= 0 or x_m <= 0 or threshold < x_m:
        raise ValueError("require alpha > 0 and threshold >= x_m > 0")
    # Preserve small log excesses near the cutoff without forming a huge ratio.
    if threshold - x_m <= x_m:
        log_ratio = math.log1p((threshold - x_m) / x_m)
    else:
        log_ratio = math.log(threshold) - math.log(x_m)
    log_survival = -alpha * log_ratio
    if not math.isfinite(log_survival):
        raise OverflowError("log survival is outside the floating-point range")
    if alpha <= 1:
        mean_excess = conditional_mean = tail_first_moment = math.inf
    else:
        mean_excess = threshold / (alpha - 1)
        conditional_mean = threshold + mean_excess
        if not math.isfinite(mean_excess) or not math.isfinite(conditional_mean):
            raise OverflowError("finite Pareto expectations are not representable")
        # Forming exp(log_survival) first could erase a representable product.
        tail_first_moment = math.exp(log_survival + math.log(conditional_mean))
    return {
        "log_survival": log_survival,
        "mean_excess": mean_excess,
        "conditional_mean": conditional_mean,
        "tail_first_moment": tail_first_moment,
    }


def pareto_normalized_maximum_cdf(
    y: ArrayLike, *, alpha: float, n: int
) -> NDArray[np.float64]:
    """CDF of M_n / (x_m * n**(1/alpha)) for iid exact Pareto observations.

    The positive scale x_m cancels. Require a finite positive one-dimensional
    y grid, finite alpha > 0, and integer 1 <= n <= 2**53 (exact float count).
    Return zero below the finite-n support; preserve small CDFs and tail
    probabilities with expm1 and log1p, respectively.
    Ordinary CDFs can round to 0 or 1; these endpoints are not support claims.
    Reject non-finite intermediate log probabilities rather than drop points.
    """
    values = np.atleast_1d(np.asarray(y, dtype=float))
    if (values.ndim != 1 or values.size == 0
            or not np.all(np.isfinite(values)) or np.any(values <= 0)):
        raise ValueError("y must be a nonempty vector of finite positive values")
    if not math.isfinite(alpha) or alpha <= 0:
        raise ValueError("alpha must be finite and positive")
    if isinstance(n, (bool, np.bool_)):
        raise ValueError("n must be an integer in [1, 2**53]")
    try:
        count = operator.index(n)
    except TypeError as exc:
        raise ValueError("n must be an integer in [1, 2**53]") from exc
    if not 1 <= count <= 2**53:
        raise ValueError("n must be an integer in [1, 2**53]")
    with np.errstate(over="ignore"):
        log_q = -alpha * np.log(values) - math.log(count)
    if not np.all(np.isfinite(log_q)):
        raise OverflowError("log probabilities are outside the floating-point range")
    # Near the lower endpoint, subtracting the two logs can erase the distance
    # from the support. Recompute just these cases at higher precision. The
    # product also preserves exact endpoints such as n=8, alpha=1, y=1/8.
    if count > 1:
        with localcontext() as context:
            context.prec = 80
            for index in np.flatnonzero(np.abs(log_q) < 1e-8):
                scaled_power = (Decimal.from_float(float(values[index]))
                                ** Decimal.from_float(float(alpha))) * count
                log_q[index] = float(-scaled_power.ln())
    result = np.zeros_like(values)
    inside = log_q < 0
    near_support = inside & (log_q > -math.log(2))
    with np.errstate(divide="ignore", under="ignore"):
        result[near_support] = np.exp(count * np.log(-np.expm1(log_q[near_support])))
        far = inside & ~near_support
        result[far] = np.exp(count * np.log1p(-np.exp(log_q[far])))
    return result
