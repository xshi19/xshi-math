"""Finite forecast scores and explicitly specified tail-payoff models.

No fitted law or data acquisition is implicit. ``p=None`` in the beta helpers
means a calibrated experiment, D | Q ~ Bernoulli(Q); a numeric p means that
D ~ Bernoulli(p) is independent of Q. Replications are independent.
"""

from __future__ import annotations

import numpy as np
from scipy.special import ndtr
from scipy.stats import beta, binom


def _probability(value, name):
    value = float(value)
    if not np.isfinite(value) or not 0 <= value <= 1:
        raise ValueError(f"{name} must be finite and in [0, 1]")
    return value


def _count(value, name, maximum=100_000):
    if (isinstance(value, (bool, np.bool_))
            or not isinstance(value, (int, np.integer))
            or not 1 <= value <= maximum):
        raise ValueError(f"{name} must be an integer in [1, {maximum}]")
    return int(value)


def _finite(values, name):
    values = np.asarray(values, dtype=float)
    if not np.all(np.isfinite(values)):
        raise ValueError(f"{name} must be finite")
    return values


def _forecast_pairs(forecasts, outcomes):
    q, d = _finite(forecasts, "forecasts"), _finite(outcomes, "outcomes")
    if q.ndim != 1 or q.size == 0 or d.shape != q.shape:
        raise ValueError("forecasts and outcomes must be equal nonempty vectors")
    if np.any((q < 0) | (q > 1)) or np.any((d != 0) & (d != 1)):
        raise ValueError("forecasts must be in [0, 1] and outcomes binary")
    return q, d


def tail_bet_payoffs(values, threshold):
    """Strict binary, excess (vanilla), and tail-level payoffs, same shape.

    Inputs are finite real numbers; threshold is scalar. Arithmetic overflow
    raises OverflowError. At the threshold all three payoffs are zero.
    """
    x = _finite(values, "values")
    u = float(_finite(threshold, "threshold"))
    event = x > u
    with np.errstate(over="ignore"):
        excess = np.where(event, x - u, 0.0)
    if not np.all(np.isfinite(excess)):
        raise OverflowError("excess payoff exceeds floating-point range")
    return {"binary": event.astype(float), "excess": excess,
            "tail_level": np.where(event, x, 0.0)}


def pareto_tail_bet(alpha, threshold, *, xm=1.0):
    """Exact Type-I Pareto probability and unconditional payoff means.

    alpha>0, threshold>=xm>0, all finite. For alpha<=1 both payoff means
    are +inf. Evaluate finite means in logs, independently of probability
    underflow. Representational overflow raises OverflowError.
    """
    a, u, m = map(float, (alpha, threshold, xm))
    if not np.all(np.isfinite([a, u, m])) or a <= 0 or not u >= m > 0:
        raise ValueError("require finite alpha>0 and threshold>=xm>0")
    # log(m/u), with precision near equality and no ratio underflow far away.
    log_ratio = (np.log1p((m-u)/u) if m >= u/2
                 else np.log(m)-np.log(u))
    with np.errstate(over="ignore", under="ignore"):
        log_p = a * log_ratio
        probability = float(np.exp(log_p))
        log_call = np.log(u) + log_p - np.log(a-1) if a > 1 else np.inf
        call = float(np.exp(log_call))
        tail = float(np.exp(log_call + np.log(a))) if a > 1 else np.inf
    if a > 1 and not np.all(np.isfinite([call, tail])):
        raise OverflowError("finite payoff mean exceeds floating-point range")
    return {"probability": probability, "excess_mean": call, "tail_mean": tail}


def lognormal_tail_bet(sigma, *, mean=1.0):
    """Mean-matched lognormal, struck at its mean, strict event X>mean.

    X=mean*exp(sigma*Z-sigma**2/2) for sigma>0 and Z standard normal.
    sigma=0 is deterministic: all three results are zero. Finite mean>0
    and finite sigma>=0 are required. No simulation or pricing measure.
    """
    s, m = float(sigma), float(mean)
    if not np.all(np.isfinite([s, m])) or s < 0 or m <= 0:
        raise ValueError("require finite sigma>=0 and mean>0")
    if s == 0:
        return dict(probability=0.0, excess_mean=0.0, tail_mean=0.0)
    # erf avoids cancellation in 2*Phi(s/2)-1 for small s.
    from scipy.special import erf
    # Below the normal float range, scale before dividing so a representable
    # payoff is not lost in the erf argument. The cubic term is negligible.
    excess = (m*s/np.sqrt(2*np.pi) if s < np.finfo(float).tiny
              else m*erf(s/(2*np.sqrt(2))))
    return {"probability": float(ndtr(-s/2)),
            "excess_mean": float(excess),
            "tail_mean": float(m * ndtr(s/2))}


def binary_tally_distribution(n, p):
    """(fractions, masses) for the mean of n iid Bernoulli(p) outcomes.

    n is an integer from 1 through 100,000; 0<=p<=1. Endpoint laws retain
    the full grid with zero masses. PMFs are floating-point evaluations.
    """
    n, p = _count(n, "n"), _probability(p, "p")
    k = np.arange(n + 1)
    return k / n, binom.pmf(k, n, p)


def brier_score(forecasts, outcomes):
    """Mean squared binary error, on the [0,1] (not doubled) convention."""
    q, d = _forecast_pairs(forecasts, outcomes)
    return float(np.mean((q-d)**2))


def brier_score_distribution(n, p, q):
    """Exact finite law (sorted support, masses) for a constant forecast q.

    Outcomes are iid Bernoulli(p). At q=1/2 the score is identically 1/4.
    Zero-mass atoms and any coincident floating-point support values are
    merged/removed. n has the binary_tally_distribution bound.
    """
    q = _probability(q, "q")
    fraction, mass = binary_tally_distribution(n, p)
    if q == .5:
        return np.array([.25]), np.array([1.0])
    # Convex combination avoids a negative score through cancellation at q=1.
    support = (1-fraction)*q*q + fraction*(1-q)**2
    values, inverse = np.unique(support, return_inverse=True)
    weights = np.bincount(inverse, weights=mass, minlength=values.size)
    keep = weights > 0
    return values[keep], weights[keep]


def _beta_model(a, b, p):
    a, b = float(a), float(b)
    if not np.all(np.isfinite([a, b])) or not (1e-3 <= a <= 1e4 and 1e-3 <= b <= 1e4):
        raise ValueError("beta shapes must lie in [0.001, 10000]")
    return a, b, None if p is None else _probability(p, "p")


def beta_brier_moments(a, b, *, p=None, n=1):
    """Mean/single-score variance/variance of an iid n-score average.

    Q~Beta(a,b); p=None: D|Q~Bernoulli(Q); otherwise D is independent
    Bernoulli(p). Shapes restricted to [0.001,10000], n to [1,100000].
    Conditional squared-beta moments avoid subtracting nearly equal raw
    moments. Evaluation is numerical, without a uniform error guarantee.
    """
    a, b, p = _beta_model(a, b, p)
    n = _count(n, "n")
    def squared_beta_moments(c, d):
        t = c+d
        mean = c*(c+1)/(t*(t+1))
        variance = (c*(c+1)*d*((4*c+6)*t+6*(c+1))
                    / (t*t*(t+1)**2*(t+2)*(t+3)))
        return mean, variance
    if p is None:
        # Q|D=0 ~ Beta(a,b+1); (1-Q)|D=1 ~ Beta(b,a+1).
        p0, p1 = b/(a+b), a/(a+b)
        mean0, var0 = squared_beta_moments(a, b+1)
        mean1, var1 = squared_beta_moments(b, a+1)
    else:
        p0, p1 = 1-p, p
        mean0, var0 = squared_beta_moments(a, b)
        mean1, var1 = squared_beta_moments(b, a)
    mean = p0*mean0+p1*mean1
    variance = p0*var0+p1*var1+p0*p1*(mean0-mean1)**2
    if variance < 0 or not np.all(np.isfinite([mean, variance])):
        raise ArithmeticError("beta moment evaluation lost precision")
    return {"mean": mean, "score_variance": variance, "average_variance": variance/n}


def beta_brier_cdf(z, a, b, *, p=None):
    """Exact one-score CDF evaluated using incomplete beta functions.

    Same joint-law/shape contract as beta_brier_moments. Returns an array
    matching z (0-D for scalar); +/-inf map to 0/1, NaN is rejected.
    This does not evaluate the distribution of an average with n>1.
    """
    a, b, p = _beta_model(a, b, p)
    z = np.asarray(z, dtype=float)
    if np.any(np.isnan(z)):
        raise ValueError("z must not contain NaN")
    clipped = np.clip(z, 0, 1)
    s = np.sqrt(clipped)
    # Preserve 1-sqrt(z) near one, where small beta shapes amplify rounding.
    complement = (1-clipped)/(1+s)
    def at_root(c, d):
        return np.where(clipped <= .25, beta.cdf(s, c, d),
                        beta.sf(complement, d, c))
    if p is None:
        values = (b/(a+b)*at_root(a, b+1)
                  + a/(a+b)*at_root(b, a+1))
    else:
        values = (1-p)*at_root(a, b) + p*at_root(b, a)
    return np.asarray(np.where(z <= 0, 0.0, np.where(z >= 1, 1.0, values)))


def simulate_brier_scores(a, b, n, *, p=None, repetitions=10_000, seed=1107):
    """Batched iid beta/Bernoulli score averages, retaining every replicate.

    Uses a local NumPy PCG64 generator. At most 20 million (Q,D) pairs;
    n<=100000 and repetitions<=1000000. Same beta/joint-law restrictions as
    beta_brier_moments. Returned vector is numerical simulation, not exact.
    """
    a, b, p = _beta_model(a, b, p)
    n, repetitions = _count(n, "n"), _count(repetitions, "repetitions", 1_000_000)
    if n*repetitions > 20_000_000:
        raise ValueError("at most 20000000 forecast/outcome pairs are allowed")
    if isinstance(seed, (bool, np.bool_)) or not isinstance(seed, (int, np.integer)) or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    rng = np.random.Generator(np.random.PCG64(seed))
    result = np.empty(repetitions)
    batch = max(1, 100_000//n)
    for start in range(0, repetitions, batch):
        size = (min(batch, repetitions-start), n)
        q = rng.beta(a, b, size=size)
        d = rng.random(size) < (q if p is None else p)
        result[start:start+size[0]] = np.mean((q-d)**2, axis=1)
    return result


def calibration_curve(forecasts, outcomes, *, bins=10):
    """Equal-width forecast bins with counts, forecast means and frequencies.

    Bins are [left,right), except the last includes 1. Empty bins have count
    zero and NaN means; no smoothing, confidence intervals or inferred law.
    """
    q, d = _forecast_pairs(forecasts, outcomes)
    bins = _count(bins, "bins", 10_000)
    edges = np.linspace(0, 1, bins+1)
    groups = np.minimum(np.searchsorted(edges, q, side="right")-1, bins-1)
    count = np.bincount(groups, minlength=bins)
    result = {"edges": edges, "count": count}
    for key, values in (("forecast_mean", q), ("event_frequency", d)):
        total = np.bincount(groups, weights=values, minlength=bins)
        result[key] = np.divide(total, count, out=np.full(bins, np.nan), where=count > 0)
    return result


def point_forecast_loss(actual, forecast, *, metric="absolute", scale=None):
    """Elementwise broadcast losses: absolute, squared, smape or mase.

    Inputs must be finite. sMAPE is 2|x-d|/(|x|+|d|), in [0,2], with
    zero assigned at (0,0). MASE needs an externally supplied positive finite
    scalar training scale. Other metrics reject scale. Overflow raises.
    """
    x, d = np.broadcast_arrays(_finite(actual, "actual"), _finite(forecast, "forecast"))
    if metric not in {"absolute", "squared", "smape", "mase"}:
        raise ValueError("unknown loss metric")
    if metric == "mase":
        if scale is None or np.ndim(scale) != 0 or not np.isfinite(scale) or scale <= 0:
            raise ValueError("MASE requires a positive finite training scale")
        scale = float(scale)
    elif scale is not None:
        raise ValueError("scale is used only for MASE")
    with np.errstate(over="ignore", invalid="ignore"):
        if metric == "smape":
            m = np.maximum(np.abs(x), np.abs(d))
            xs = np.divide(x, m, out=np.zeros_like(x), where=m > 0)
            ds = np.divide(d, m, out=np.zeros_like(d), where=m > 0)
            den = np.abs(xs)+np.abs(ds)
            loss = np.divide(2*np.abs(xs-ds), den, out=np.zeros_like(x), where=den > 0)
        elif metric == "mase":
            # Divide first when opposite signs would overflow the difference.
            same_sign = np.signbit(x) == np.signbit(d)
            loss = np.where(same_sign, np.abs(x-d)/scale, np.abs(x/scale-d/scale))
        else:
            loss = np.abs(x-d)
            if metric == "squared":
                loss = loss*loss
    if not np.all(np.isfinite(loss)):
        raise OverflowError("loss exceeds floating-point range")
    return np.asarray(loss)
