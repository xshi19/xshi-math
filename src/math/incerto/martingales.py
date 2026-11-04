"""Binary forecast models and finite-grid revision diagnostics.

The probit model has dZ = sigma**2 * Z / 2 dt + sigma dW and Y = Phi(Z).
Its share and its conditional terminal-event probability are martingales;
the unbounded coordinate is not. Simulations use exact normal transitions.
"""

from __future__ import annotations

import numpy as np
from scipy.special import ndtr, ndtri

from .calibration import brier_score


def _scalar(value, name, *, positive=False):
    value = float(value)
    if not np.isfinite(value) or (value <= 0 if positive else value < 0):
        domain = "positive" if positive else "nonnegative"
        raise ValueError(f"{name} must be finite and {domain}")
    return value


def _threshold(value):
    value = float(value)
    if not np.isfinite(value) or not 0 < value < 1:
        raise ValueError("threshold must be finite and in (0, 1)")
    return value


def _finite_array(value, name):
    value = np.asarray(value, dtype=float)
    if not value.size or not np.all(np.isfinite(value)):
        raise ValueError(f"{name} must be nonempty and finite")
    return value


def _result(value):
    return float(value) if np.ndim(value) == 0 else value


def gaussian_binary_probability(mean, sigma, remaining, *, threshold=.5):
    """P(X_T > threshold) for X_T | X_t ~ N(mean, sigma**2 * remaining).

    ``mean`` is a finite scalar or nonempty array; other inputs are finite
    scalars, with sigma and remaining nonnegative. Threshold can be any
    finite real. Zero scale or horizon gives the strict deterministic event
    (a tie is zero). Returns a float or an array matching mean. Normal-CDF
    tails may round to 0/1; NaN and infinite inputs are rejected.
    """
    mean = _finite_array(mean, "mean")
    sigma = _scalar(sigma, "sigma")
    remaining = _scalar(remaining, "remaining")
    threshold = float(threshold)
    if not np.isfinite(threshold):
        raise ValueError("threshold must be finite")
    if sigma == 0 or remaining == 0:
        return _result((mean > threshold).astype(float))
    # Avoid overflowing a finite margin or underflowing a positive standard
    # deviation before forming their ratio. Infinite z is a valid CDF limit.
    sd = np.longdouble(sigma) * np.sqrt(np.longdouble(remaining))
    z = (mean.astype(np.longdouble) - np.longdouble(threshold)) / sd
    with np.errstate(over="ignore"):
        return _result(ndtr(np.asarray(z, dtype=float)))


def _latent_probability(z, sigma, remaining, k, *, gap=None):
    if sigma == 0 or remaining == 0:
        return (np.asarray(z) > k).astype(float)
    q = np.longdouble(sigma)**2 * np.longdouble(remaining)
    # z - exp(-q/2)*k, keeping the small drift at z == k.
    numerator = (np.asarray(z, dtype=np.longdouble) - np.longdouble(k)
                 if gap is None else gap)
    numerator = numerator - np.longdouble(k) * np.expm1(-q / 2)
    denominator = np.sqrt(-np.expm1(-q))
    with np.errstate(over="ignore"):
        return ndtr(np.asarray(numerator / denominator, dtype=float))


def probit_binary_probability(share, sigma, remaining, *, threshold=.5):
    """P(Y_T > threshold) in the drift-corrected probit martingale model.

    Share is a finite scalar or nonempty array in [0,1]; threshold is in
    (0,1). Sigma is latent-coordinate volatility, not share volatility.
    Finite sigma and remaining are nonnegative. Endpoint shares are the
    absorbing extension. Zero sigma/horizon uses the strict share inequality.
    Positive-variance ties generally differ from this degenerate value.
    Returns a float or matching array. CDF rounding to 0/1 is retained.

    A 400-digit reference audit of 233 evaluations measured maximum absolute
    errors of 1.12e-16 for ordinary inputs and 4.92e-14 for adjacent floats.
    Errors up to about 2.6e-8 were observed only for shares around 1e-16
    just above the 1e-8 latent-gap cutoff, where rounded inverse-normal
    values are subtracted directly. These are observed errors, not global
    bounds; the midpoint-derivative algorithm below the cutoff is retained.
    """
    share = _finite_array(share, "share")
    if np.any((share < 0) | (share > 1)):
        raise ValueError("share must be in [0, 1]")
    sigma = _scalar(sigma, "sigma")
    remaining = _scalar(remaining, "remaining")
    threshold = _threshold(threshold)
    if sigma == 0 or remaining == 0:
        return _result((share > threshold).astype(float))
    z, k = ndtri(share), ndtri(threshold)
    gap = np.asarray(z, dtype=np.longdouble) - np.longdouble(k)
    # Nearby quantiles can coincide after rounding. Integrate the inverse-CDF
    # derivative with its midpoint value only over gaps below 1e-8 in z.
    # Its relative truncation error is O((1+z**2)*gap**2); unlike subtraction,
    # this preserves the sign and size even for adjacent input probabilities.
    nearby = np.isfinite(z) & (share != threshold) & (np.abs(gap) < 1e-8)
    if np.any(nearby):
        midpoint = (share.astype(np.longdouble) + np.longdouble(threshold)) / 2
        mid_z = ndtri(np.asarray(midpoint[nearby], dtype=float)).astype(np.longdouble)
        density = np.exp(-mid_z**2 / 2) / np.sqrt(2*np.longdouble(np.pi))
        gap = np.array(gap, copy=True)
        gap[nearby] = (share[nearby].astype(np.longdouble)-np.longdouble(threshold)) / density
    return _result(_latent_probability(z, sigma, remaining, k, gap=gap))


def _count(value, name, maximum):
    if (isinstance(value, (bool, np.bool_))
            or not isinstance(value, (int, np.integer))
            or not 1 <= value <= maximum):
        raise ValueError(f"{name} must be an integer in [1, {maximum}]")
    return int(value)


def simulate_probit_forecasts(share, sigma, horizon, *, threshold=.5,
                             steps=40, paths=1000, seed=0):
    """Exact finite-grid latent/share/binary paths, with terminal resolution.

    Scalar share and threshold are in (0,1); horizon > 0, sigma >= 0.
    For sigma > 0, require 1e-12 <= sigma**2*horizon <= 50 to bound the
    numerical experiment. Integrated variance within relative tolerance
    8*np.finfo(float).eps (about 1.8e-15) of either endpoint is treated as
    that endpoint by rescaling sigma; there is no absolute tolerance.
    Thus sigma=1e-6 and sigma=sqrt(50) are accepted at horizon 1.
    Steps <= 10000; paths*(steps+1) <= 2000000.
    PCG64 seed is a nonnegative integer. Sigma zero gives constant shares
    and the deterministic strict event. No Euler scheme or path clipping.

    Returns dict: time (steps+1,), latent/share/probability
    (paths, steps+1), outcome (paths,). Retained latent states, rather than
    rounded CDF shares, determine all future transitions and outcomes.
    """
    share = _threshold(share)
    threshold = _threshold(threshold)
    sigma = _scalar(sigma, "sigma")
    horizon = _scalar(horizon, "horizon", positive=True)
    steps = _count(steps, "steps", 10_000)
    paths = _count(paths, "paths", 1_000_000)
    if paths * (steps + 1) > 2_000_000:
        raise ValueError("path grid must have at most 2000000 cells")
    if (isinstance(seed, (bool, np.bool_))
            or not isinstance(seed, (int, np.integer)) or seed < 0):
        raise ValueError("seed must be a nonnegative integer")
    q = np.longdouble(sigma)**2 * np.longdouble(horizon)
    if sigma > 0:
        # Inputs are float64 even when the variance is evaluated in extended
        # precision. Snap rounding-sized deviations on either side of a bound.
        for endpoint in (np.longdouble('1e-12'), np.longdouble(50)):
            if abs(q - endpoint) <= 8 * np.finfo(float).eps * endpoint:
                q = endpoint
                sigma = np.sqrt(endpoint / np.longdouble(horizon))
                break
    if sigma > 0 and not np.longdouble('1e-12') <= q <= 50:
        raise ValueError("positive integrated latent variance must be in [1e-12, 50]")
    times = np.linspace(0, horizon, steps + 1)
    if np.any(np.diff(times) <= 0):
        raise ValueError("time grid must be representable and strictly increasing")
    latent = np.empty((paths, steps + 1))
    latent[:, 0] = ndtri(share)
    probability = np.empty_like(latent)
    k = ndtri(threshold)
    probability[:, 0] = probit_binary_probability(share, sigma, horizon,
                                                 threshold=threshold)
    if sigma == 0:
        latent[:, 1:] = latent[:, :1]
        outcome = np.full(paths, float(share > threshold))
        probability[:] = outcome[:, None]
        return dict(time=times, latent=latent, share=ndtr(latent),
                    probability=probability, outcome=outcome)
    rng = np.random.Generator(np.random.PCG64(int(seed)))
    for i, dt in enumerate(np.diff(times)):
        step_q = float(np.longdouble(sigma)**2 * np.longdouble(dt))
        latent[:, i + 1] = (np.exp(step_q / 2) * latent[:, i]
                            + np.sqrt(np.expm1(step_q)) * rng.standard_normal(paths))
        probability[:, i + 1] = _latent_probability(
            latent[:, i + 1], sigma, horizon - times[i + 1], k)
    if not np.all(np.isfinite(latent)):
        raise FloatingPointError("nonfinite latent path")
    outcome = (latent[:, -1] > k).astype(float)
    probability[:, -1] = outcome
    return dict(time=times, latent=latent, share=ndtr(latent),
                probability=probability, outcome=outcome)


def forecast_revision_summary(probabilities):
    """Necessary martingale diagnostics for complete independent path rows.

    Input is a finite 2-D array in [0,1], with >=1 row and >=2 columns;
    final reports must be 0/1. At most 2000000 cells. No rows are discarded.
    Conditional coherence is assumed only for interpreting the null moments,
    not for computing them. SEs use the usual independent, identically
    distributed row convention, which is not imposed or tested. Independence
    alone does not justify pooling rows with different means. One row gives
    NaN for every SE.

    Returns squared_revision (mean sum of squared increments), initial_budget
    (mean p0*(1-p0)), budget_gap and budget_gap_se, squared_revision_se,
    mean_revision/revision_se and level_moment/level_moment_se (per step),
    brier (per time, against each row's final outcome), and paths.
    Level moments use predictable instrument p_i - .5. The budget comparison
    is an expectation check, not a pathwise bound or an automatic p-value.
    """
    p = _finite_array(probabilities, "probabilities")
    if p.ndim != 2 or p.shape[1] < 2 or p.size > 2_000_000:
        raise ValueError("require a path matrix with >=2 columns and <=2000000 cells")
    if np.any((p < 0) | (p > 1)):
        raise ValueError("probabilities must be in [0, 1]")
    if np.any((p[:, -1] != 0) & (p[:, -1] != 1)):
        raise ValueError("last column must resolve the event to 0 or 1")
    n = p.shape[0]

    def sem(values):
        if n == 1:
            return np.full(np.shape(values)[1:], np.nan)
        return np.std(values, axis=0, ddof=1) / np.sqrt(n)

    delta = np.diff(p, axis=1)
    energy = np.sum(delta**2, axis=1)
    budget = p[:, 0] * (1 - p[:, 0])
    gap = energy - budget
    level = (p[:, :-1] - .5) * delta
    return dict(paths=n, squared_revision=float(energy.mean()),
                squared_revision_se=float(sem(energy)),
                initial_budget=float(budget.mean()), budget_gap=float(gap.mean()),
                budget_gap_se=float(sem(gap)), mean_revision=delta.mean(axis=0),
                revision_se=sem(delta), level_moment=level.mean(axis=0),
                level_moment_se=sem(level),
                brier=np.array([brier_score(column, p[:, -1]) for column in p.T]))


__all__ = ["gaussian_binary_probability", "probit_binary_probability",
           "simulate_probit_forecasts", "forecast_revision_summary"]
