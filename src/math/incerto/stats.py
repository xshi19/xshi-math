"""Statistical helper functions used by Incerto examples."""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.stats import norm


def mean_absolute_deviation(
    x: ArrayLike,
    axis: int | None = None,
) -> float | NDArray[np.float64]:
    """Return mean absolute deviation scaled to match normal standard deviation.

    The raw mean absolute deviation is centered at the arithmetic mean.  The
    multiplier ``sqrt(pi / 2)`` makes the value equal to ``sigma`` for a
    Gaussian ``N(mu, sigma**2)`` distribution.

    Parameters
    ----------
    x:
        Input observations.
    axis:
        Axis along which to compute the statistic.  When ``None``, compute over
        the flattened input.

    Returns
    -------
    float or numpy.ndarray
        Scaled mean absolute deviation.
    """

    x_array = np.asarray(x, dtype=float)
    center = np.mean(x_array, axis=axis, keepdims=True)
    result = np.mean(np.abs(x_array - center), axis=axis) * np.sqrt(np.pi / 2.0)
    return float(result) if np.ndim(result) == 0 else result


def median_absolute_deviation(
    x: ArrayLike,
    axis: int | None = None,
) -> float | NDArray[np.float64]:
    """Return median absolute deviation scaled to match normal standard deviation.

    The raw median absolute deviation is centered at the median.  Dividing by
    ``Phi^{-1}(0.75)`` makes the value equal to ``sigma`` for a Gaussian
    ``N(mu, sigma**2)`` distribution.

    Parameters
    ----------
    x:
        Input observations.
    axis:
        Axis along which to compute the statistic.  When ``None``, compute over
        the flattened input.

    Returns
    -------
    float or numpy.ndarray
        Scaled median absolute deviation.
    """

    x_array = np.asarray(x, dtype=float)
    center = np.median(x_array, axis=axis, keepdims=True)
    raw = np.median(np.abs(x_array - center), axis=axis)
    result = raw / norm.ppf(0.75)
    return float(result) if np.ndim(result) == 0 else result


def normal_peak_shoulder_tail(
    mu: float = 0.0,
    sigma: float = 1.0,
) -> NDArray[np.float64]:
    """Return normal scale-curvature boundaries for tail diagnostics.

    The four returned points split a symmetric normal density into left tail,
    left shoulder, peak, right shoulder, and right tail regions under the
    scale-perturbation diagnostic used in the Chapter 4 notes.
    """

    if sigma <= 0:
        raise ValueError("sigma must be positive")

    outer = np.sqrt((5.0 + np.sqrt(17.0)) / 2.0)
    inner = np.sqrt((5.0 - np.sqrt(17.0)) / 2.0)
    return np.array(
        [
            mu - outer * sigma,
            mu - inner * sigma,
            mu + inner * sigma,
            mu + outer * sigma,
        ]
    )


def normal_variance_peak_shoulder_tail(
    mu: float = 0.0,
    variance: float = 1.0,
) -> NDArray[np.float64]:
    """Return normal variance-curvature boundaries for tail diagnostics.

    The four returned points split a symmetric normal density into left tail,
    left shoulder, peak, right shoulder, and right tail regions under a local,
    mean-preserving perturbation of the variance parameter.
    """

    if variance <= 0:
        raise ValueError("variance must be positive")

    sigma = np.sqrt(variance)
    outer = np.sqrt(3.0 + np.sqrt(6.0))
    inner = np.sqrt(3.0 - np.sqrt(6.0))
    return np.array(
        [
            mu - outer * sigma,
            mu - inner * sigma,
            mu + inner * sigma,
            mu + outer * sigma,
        ]
    )


def t_peak_shoulder_tail(
    df: float,
    mu: float = 0.0,
    sigma: float = 1.0,
) -> NDArray[np.float64]:
    """Return Student-t scale-curvature boundaries for tail diagnostics.

    Parameters
    ----------
    df:
        Degrees of freedom.  Must be greater than 1 for these boundaries.
    mu:
        Location parameter.
    sigma:
        Positive scale parameter.

    Returns
    -------
    numpy.ndarray
        Four ordered boundary points.
    """

    if df <= 1:
        raise ValueError("df must be greater than 1")
    if sigma <= 0:
        raise ValueError("sigma must be positive")

    discriminant = np.sqrt((df + 1.0) * (17.0 * df + 1.0))
    outer = np.sqrt(0.5 * (5.0 * df + discriminant + 1.0) / (df - 1.0))
    inner = np.sqrt(0.5 * (5.0 * df - discriminant + 1.0) / (df - 1.0))
    return np.array(
        [
            mu - outer * sigma,
            mu - inner * sigma,
            mu + inner * sigma,
            mu + outer * sigma,
        ]
    )


def lognorm_params_from_mean_and_variance(mean: float, variance: float) -> tuple[float, float]:
    """Return log-location and log-scale matching positive mean and variance.

    Adapted from legacy/src/stats.py. Zero variance returns a degenerate
    log-scale of zero, not a nondegenerate SciPy lognormal density.
    """
    if not np.isfinite(mean) or mean <= 0 or not np.isfinite(variance) or variance < 0:
        raise ValueError("mean must be positive and variance nonnegative, both finite")
    if variance == 0:
        return float(np.log(mean)), 0.0
    log_mean = np.log(mean)
    sigma_squared = np.logaddexp(0.0, np.log(variance) - 2 * log_mean)
    return float(log_mean - sigma_squared / 2), float(np.sqrt(sigma_squared))


def empirical_survival_function(x: ArrayLike) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """Return unique sorted values and strict empirical P(X > x).

    This corrects the legacy rank-based implementation at tied observations.
    The last value is zero; use an explicit plotting-position convention if
    nonzero endpoints are needed on logarithmic axes.
    """
    values = np.asarray(x, dtype=float)
    if values.ndim != 1 or values.size == 0 or not np.all(np.isfinite(values)):
        raise ValueError("x must be a nonempty finite one-dimensional sample")
    support, counts = np.unique(values, return_counts=True)
    return support, (values.size - np.cumsum(counts)) / values.size
