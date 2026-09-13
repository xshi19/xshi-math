"""Small educational helpers, installed as ``xmath`` (never ``math``)."""

import numpy as np
from numpy.typing import ArrayLike

__all__ = ["exceedance_fraction"]


def exceedance_fraction(samples: ArrayLike, threshold: float) -> float:
    """Return the fraction of finite observations strictly above a threshold.

    ``samples`` must be a nonempty one-dimensional array; ``threshold`` must
    be finite. This describes the observations, not a fitted tail model.
    """
    values = np.asarray(samples, dtype=float)
    if values.ndim != 1 or values.size == 0:
        raise ValueError("samples must be a nonempty one-dimensional array")
    if not np.all(np.isfinite(values)) or not np.isfinite(threshold):
        raise ValueError("samples and threshold must be finite")
    return float(np.count_nonzero(values > threshold) / values.size)
