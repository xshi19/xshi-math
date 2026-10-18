"""Finite model calculations for the SCoFT Prologue teaching examples."""

from collections.abc import Callable
import math

import numpy as np
from numpy.typing import ArrayLike, NDArray


def bounded_spike_summary(epsilon: float) -> dict[str, float]:
    """Moments of masses epsilon/2 at +/-1/sqrt(epsilon), and 1-epsilon at 0.

    Return the support radius, mean, variance and Pearson (not excess)
    kurtosis. This is a population calculation, not a sample estimator.
    Require finite 0 < epsilon <= 1 and a representable kurtosis.
    """
    if not math.isfinite(epsilon) or not 0 < epsilon <= 1:
        raise ValueError("epsilon must be finite and in (0, 1]")
    kurtosis = 1.0 / epsilon
    if not math.isfinite(kurtosis):
        raise OverflowError("kurtosis is not representable; increase epsilon")
    return {
        "support_radius": math.sqrt(kurtosis),
        "mean": 0.0,
        "variance": 1.0,
        "kurtosis": kurtosis,
    }


def log_survival_multiplier_ratio(
    log_survival: Callable[[NDArray[np.float64]], ArrayLike],
    thresholds: ArrayLike,
    *,
    multiplier: float = 2.0,
) -> NDArray[np.float64]:
    """Return log(P(X > t*u) / P(X > u)) for finite positive thresholds u.

    ``log_survival`` must accept a one-dimensional array and return finite,
    nonpositive log probabilities with the same shape. It must evaluate log
    survival directly; taking log of an underflowed ordinary survival does
    not recover the probability. Require t > 1 and positive survival at both
    grids. Reject NaN/infinity (including a zero survival's -infinity), shape
    mismatches and threshold overflow rather than silently omitting points.

    No exponentiation is performed. Finite evaluations are diagnostics of a
    specified law and cannot certify a limiting tail class.
    """
    u = np.atleast_1d(np.asarray(thresholds, dtype=float))
    if u.ndim != 1 or u.size == 0 or not np.all(np.isfinite(u)) or np.any(u <= 0):
        raise ValueError("thresholds must be a nonempty vector of finite positive values")
    if not math.isfinite(multiplier) or multiplier <= 1:
        raise ValueError("multiplier must be finite and greater than one")
    with np.errstate(over="ignore"):
        scaled = multiplier * u
    if not np.all(np.isfinite(scaled)):
        raise ValueError("multiplied thresholds must be finite")
    values = []
    for grid in (u, scaled):
        log_sf = np.asarray(log_survival(grid), dtype=float)
        if log_sf.shape != u.shape:
            raise ValueError("log_survival must return one value per threshold")
        if not np.all(np.isfinite(log_sf)) or np.any(log_sf > 0):
            raise ValueError("log_survival values must be finite and nonpositive")
        values.append(log_sf)
    return values[1] - values[0]
