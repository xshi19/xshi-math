"""Point-forecast experiments and endpoint transforms (SCoFT chapter 12).

Model assumptions are explicit; no data access or forecast fitting occurs here.
Floating-point checks distinguish an endpoint infinity from arithmetic overflow.
"""

import numpy as np

from xmath.incerto.calibration import point_forecast_loss
from xmath.incerto.limits import _count, _scalar


def _real_array(value, name, *, allow_inf=False):
    if np.iscomplexobj(value):
        raise ValueError(f"{name} must contain real values")
    try:
        result = np.asarray(value, dtype=float)
    except (ValueError, TypeError, OverflowError) as error:
        raise ValueError(f"{name} must contain real values") from error
    if np.any(np.isnan(result)) or (not allow_inf and np.any(~np.isfinite(result))):
        raise ValueError(f"{name} must contain " + ("non-NaN" if allow_inf else "finite") + " values")
    return result


def _scalar_or_array(value):
    return float(value) if value.ndim == 0 else value


def stable_average_scale(alpha, n, *, scale=1.0):
    """Scale of an iid symmetric stable average: scale*n**(1/alpha-1).

    CF convention exp(i*location*t - abs(scale*t)**alpha); 0<alpha<=2.
    This is a distributional scale, not a standard deviation or an expected
    error. n is an integer in [1,2**53]. Positive-result overflow/underflow
    raises FloatingPointError. n=1 preserves scale exactly.
    """
    alpha = _scalar(alpha, "alpha", positive=True)
    scale = _scalar(scale, "scale", positive=True)
    n = _count(n, "n")
    if alpha > 2:
        raise ValueError("alpha must not exceed 2")
    if n == 1 or alpha == 1:
        return scale
    with np.errstate(over="raise", invalid="raise", under="ignore"):
        value = np.exp(np.log(scale) + (1/alpha-1)*np.log(n))
    if not np.isfinite(value) or value <= 0:
        raise FloatingPointError("positive stable scale is not representable")
    return float(value)


def quantile_loss(actual, forecast, *, tau=0.5):
    """Broadcast pinball loss at finite real inputs and scalar 0<tau<1.

    Underprediction costs tau per unit, overprediction costs 1-tau.
    Returns a NumPy array, including a zero-dimensional array for scalars.
    Scale before subtracting only when the residual overflows, to retain
    representable losses. Unrepresentable positive losses raise OverflowError.
    """
    tau = _scalar(tau, "tau")
    if not 0 < tau < 1:
        raise ValueError("tau must lie strictly between zero and one")
    x, d = np.broadcast_arrays(_real_array(actual, "actual"),
                               _real_array(forecast, "forecast"))
    weight = np.where(x >= d, tau, 1-tau)
    with np.errstate(over="ignore", invalid="ignore", under="ignore"):
        residual = np.abs(x-d)
        result = np.where(np.isfinite(residual), weight*residual,
                          np.abs(weight*x-weight*d))
    if np.any(~np.isfinite(result)):
        raise OverflowError("quantile loss exceeds floating-point range")
    return np.asarray(result)


def bounded_to_dual(values, *, upper):
    """Map [0,H] to [0,inf] by -H*log(1-x/H), H=upper>0.

    Endpoint H maps to mathematical +inf; NaN, infinity, or out-of-support
    inputs raise ValueError. Finite-result overflow raises FloatingPointError.
    Near zero use log1p; near H use the positive gap before taking logs.
    A fraction that underflows uses the leading term x (correction is below
    floating-point resolution). No clipping or fitted tail law is implied.
    """
    h = _scalar(upper, "upper", positive=True)
    x = _real_array(values, "values")
    if np.any(x < 0) or np.any(x > h):
        raise ValueError("values must lie in [0, upper]")
    result = np.full_like(x, np.inf)
    small = x <= h/2
    with np.errstate(over="raise", invalid="raise", under="ignore"):
        ratio = x[small]/h
        result[small] = -h*np.log1p(-ratio)
        # Subnormal x/H loses relative precision even when it stays nonzero.
        result[small] = np.where(ratio < np.finfo(float).tiny, x[small], result[small])
        near = (x > h/2) & (x < h)
        result[near] = h*(np.log(h)-np.log(h-x[near]))
    if np.any(~np.isfinite(result[x < h])):
        raise FloatingPointError("finite dual coordinate is not representable")
    return _scalar_or_array(result)


def dual_to_bounded(values, *, upper):
    """Map [0,inf] to [0,H] by H*(1-exp(-z/H)), H=upper>0.

    +inf maps to H; NaN, negatives and -inf raise ValueError. Finite large
    coordinates may also round to H, so endpoint round trips can lose
    information. expm1 preserves small values; ratio underflow uses z.
    """
    h = _scalar(upper, "upper", positive=True)
    z = _real_array(values, "values", allow_inf=True)
    if np.any(z < 0):
        raise ValueError("dual values must be nonnegative")
    with np.errstate(over="ignore", under="ignore"):
        ratio = z/h
        result = -h*np.expm1(-ratio)
    result = np.where(ratio < np.finfo(float).tiny, z, result)
    return _scalar_or_array(result)


def pareto_forecast_scores(alpha, n, forecast, *, xm=1.0, repetitions=2000, seed=0):
    """Repeated iid exact-Pareto test sets scored against one fixed forecast.

    Return arrays of length repetitions in a dict with keys mean, absolute,
    squared, smape. All scores use the same draws within a replication;
    replications are independent. Uses default_rng(seed), PCG64 for integer
    seeds, in batches of 32 rows. n<=1e6 and n*repetitions<=50e6.
    No truncation, fitting, filtering or Monte Carlo standard-error claim.
    Nonfinite draws/averages raise FloatingPointError; score overflow raises
    OverflowError through point_forecast_loss. Population risks can be infinite
    while every returned realization is finite.
    """
    alpha = _scalar(alpha, "alpha", positive=True)
    xm = _scalar(xm, "xm", positive=True)
    forecast = _scalar(forecast, "forecast")
    n, repetitions = _count(n, "n"), _count(repetitions, "repetitions")
    if n > 1_000_000 or n*repetitions > 50_000_000:
        raise ValueError("experiment exceeds draw budget or size limit")
    rng = np.random.default_rng(seed)
    result = {name: np.empty(repetitions)
              for name in ("mean", "absolute", "squared", "smape")}
    for start in range(0, repetitions, 32):
        stop = min(start+32, repetitions)
        with np.errstate(over="raise", invalid="raise"):
            x = xm*(1+rng.pareto(alpha, (stop-start, n)))
            if np.any(~np.isfinite(x)):
                raise FloatingPointError("nonfinite Pareto draw; no observations removed")
            result["mean"][start:stop] = np.mean(x, axis=1)
            for metric in ("absolute", "squared", "smape"):
                result[metric][start:stop] = np.mean(
                    point_forecast_loss(x, forecast, metric=metric), axis=1)
    if any(np.any(~np.isfinite(values)) for values in result.values()):
        raise FloatingPointError("nonfinite average; no replications removed")
    return result


__all__ = ["stable_average_scale", "quantile_loss", "bounded_to_dual",
           "dual_to_bounded", "pareto_forecast_scores"]
