"""Finite-sum mean absolute deviations and Taleb's kappa (chapter 8).

All deviations are about a specified population mean, never a fitted center.
The stable benchmark is 2-alpha; 1/alpha is the sum's growth exponent.
"""

import numpy as np
from scipy.special import erf, gammaincc, gammaln, ndtr
from scipy.stats import binom

from xmath.incerto.limits import _count, _scalar, repeated_centered_sums


def _n(value):
    value = _count(value, "n")
    if value > 10_000_000:
        raise ValueError("n must not exceed 10 million")
    return value


def _exp(log_value):
    with np.errstate(over="raise", invalid="raise", under="ignore"):
        result = float(np.exp(log_value))
    if result == 0 or not np.isfinite(result):
        raise FloatingPointError("positive finite result is not representable")
    return result


def _stirling_remainder(a):
    # log Gamma(a) - [(a-.5) log(a) - a + .5 log(2 pi)].
    # At a >= 10000, the first omitted term is below 6e-31.
    return 1/(12*a) - 1/(360*a**3) + 1/(1260*a**5)


def kappa_from_mads(mad_n0, mad_n, n, *, n0=1):
    """2-log(n/n0)/log(M(n)/M(n0)); scalar population MAD inputs.

Require integer 1 <= n0 < n <= 10 million and 0 <= M(n0) <= M(n).
Zeros or positive infinities return nan (undefined metric). Equal positive
MADs return -inf, the extended limit as the growth ratio decreases to one.
NaN/negative inputs raise ValueError. No clipping to [0,1] is performed.
An empirical ratio is only a plug-in estimate, not a population guarantee.
"""
    n, n0 = _n(n), _n(n0)
    if n <= n0:
        raise ValueError("require n > n0")
    values = []
    for v in (mad_n0, mad_n):
        if (isinstance(v, (bool, np.bool_)) or np.iscomplexobj(v)
                or np.ndim(v) != 0):
            raise ValueError("MADs must be nonnegative real scalars")
        try:
            v = float(v)
        except (ValueError, TypeError, OverflowError) as error:
            raise ValueError("MADs must be nonnegative real scalars") from error
        if np.isnan(v) or v < 0:
            raise ValueError("MADs must be nonnegative real scalars")
        values.append(v)
    m0, m = values
    if not m0 or not m or not np.isfinite(m0) or not np.isfinite(m):
        return float("nan")
    if m < m0:
        raise ValueError("population sum MAD must not decrease")
    if m == m0:
        return float("-inf")
    difference = m - m0
    log_ratio = np.log1p(difference/m0) if difference <= m0 else np.log(m)-np.log(m0)
    return float(2 - np.log1p((n-n0)/n0)/log_ratio)


def stable_kappa(alpha):
    """Exact kappa for an alpha-stable law; nan at alpha <= 1.

alpha is a finite scalar in (0,2]. The Gaussian endpoint returns zero.
For alpha <= 1 the required finite absolute first moment does not exist.
"""
    alpha = _scalar(alpha, "alpha", positive=True)
    if alpha > 2:
        raise ValueError("alpha must not exceed 2")
    return 2-alpha if alpha > 1 else float("nan")


def gaussian_sum_mad(n, *, sigma=1.0):
    """E|S_n-n*mu| for iid N(mu,sigma**2), sigma > 0."""
    n, sigma = _n(n), _scalar(sigma, "sigma", positive=True)
    # Direct scaling preserves relative accuracy at extreme units; a log/exp
    # round trip can shift an exact Gaussian sample-size crossing by one.
    with np.errstate(over="raise", invalid="raise", under="ignore"):
        result = float(sigma*np.sqrt(2*n/np.pi))
    if result == 0 or not np.isfinite(result):
        raise FloatingPointError("positive finite result is not representable")
    return result


def gamma_sum_mad(n, *, shape=1.0, scale=1.0):
    """Exact gamma-sum MAD: 2*scale*(n*shape)**(n*shape)*exp(-n*shape)/Gamma(n*shape).

Each summand has Gamma(shape, scale) law; shape=1 is exponential.
shape is in [1e-6,1e6], scale > 0. A Stirling remainder avoids cancellation
at large total shape, with omitted log term below 6e-31 at the switch.
Finite overflow/underflow raises FloatingPointError, not mathematical inf/0.
"""
    n = _n(n)
    shape, scale = _scalar(shape, "shape", positive=True), _scalar(scale, "scale", positive=True)
    if not 1e-6 <= shape <= 1e6:
        raise ValueError("shape must be in [1e-6,1e6]")
    a = n*shape
    if a < 10000:
        log_factor = a*np.log(a)-a-gammaln(a)
    else:
        log_factor = .5*np.log(a/(2*np.pi)) - _stirling_remainder(a)
    return _exp(np.log(2) + np.log(scale) + log_factor)


def student_sum_mad(n, *, nu=3.0, scale=1.0):
    """MAD of independent Student-t(nu, location=0, scale=scale) sums.

Closed forms for n=1, n=2 (any nu in [.5,1000]), and all n for nu=3.
Returns inf for nu <= 1; unsupported n>2, nu!=3 raises ValueError.
Uses a regularized upper gamma expression for the cubic Student, avoiding
the subtraction of nearly equal terms in the unregularized formula.
"""
    n = _n(n)
    nu, scale = _scalar(nu, "nu", positive=True), _scalar(scale, "scale", positive=True)
    if not .5 <= nu <= 1000:
        raise ValueError("nu must be in [.5,1000]")
    if nu <= 1:
        return float("inf")
    log_m1 = np.log(scale) + .5*np.log(nu/np.pi) + gammaln((nu-1)/2)-gammaln(nu/2)
    if n == 1:
        return _exp(log_m1)
    if n == 2:
        log_ratio = .5*np.log(np.pi) + (2-nu)*np.log(2) + gammaln(nu-.5)-2*gammaln(nu/2)
    elif nu == 3:
        if n < 10000:
            log_ratio = np.log(n) + n - n*np.log(n) + gammaln(n)
        else:
            log_ratio = .5*np.log(2*np.pi*n) + _stirling_remainder(n)
        log_ratio += np.log(gammaincc(n, n))
    else:
        raise ValueError("closed form requires n <= 2 or nu=3")
    return _exp(log_m1 + log_ratio)


def estimate_sum_mad(rv, n, *, mean, repetitions=20000, random_state=0):
    """Monte Carlo MAD and its estimated standard error about a known mean.

Return dict(mad, mc_se). Require >=2 repetitions; inherited draw budget is
50 million and n<=1 million. All draws are retained. Nonfinite draws or
results raise. mc_se is a finite-variance diagnostic, not a confidence
guarantee; it is not justified when the absolute centered sum has infinite
variance. The law must have the stated finite population mean.
"""
    n, repetitions = _n(n), _count(repetitions, "repetitions")
    if repetitions < 2:
        raise ValueError("at least two repetitions required")
    sums = repeated_centered_sums(rv, [n], center=mean, repetitions=repetitions,
                                 random_state=random_state)[0]
    absolute = np.abs(sums)
    maximum = float(absolute.max())
    if maximum == 0:
        return {"mad": 0.0, "mc_se": 0.0}
    scaled = absolute/maximum
    return {"mad": float(maximum*np.mean(scaled)),
            "mc_se": float(maximum*(np.std(scaled, ddof=1)/np.sqrt(repetitions)))}


def lognormal_sum_mad(n, sigma, *, mu=0.0, repetitions=20000, random_state=0):
    """Lognormal(exp(mu+sigma*Z)) sum MAD using a bounded conditional payoff.

Return dict(mad, mc_se). n=1 is exact (mc_se=0); n>1 is Monte Carlo with
PCG64, conditioning on the last summand. Uses 2 E[(n E[X]-S_n)_+], so
upper-tail samples are never needed to estimate an unbounded payoff.
sigma in [1e-4,10], finite mu; n<=1 million and (n-1)*repetitions<=50 million.
No observations are clipped or removed. Overflow/nonrepresentable positive
results raise. The reported SE describes Monte Carlo integration only.
"""
    n = _n(n)
    sigma, mu = _scalar(sigma, "sigma", positive=True), _scalar(mu, "mu")
    repetitions = _count(repetitions, "repetitions")
    if not 1e-4 <= sigma <= 10:
        raise ValueError("sigma must be in [1e-4,10]")
    if repetitions < 2:
        raise ValueError("at least two repetitions required")
    log_mean = mu + sigma*sigma/2
    if n == 1:
        return {"mad": _exp(np.log(2) + log_mean + np.log(erf(sigma/(2*np.sqrt(2))))),
                "mc_se": 0.0}
    if n > 1_000_000 or (n-1)*repetitions > 50_000_000:
        raise ValueError("experiment exceeds draw budget or size limit")
    rng = np.random.default_rng(random_state)
    payoff = np.empty(repetitions)
    for start in range(0, repetitions, 32):
        count = min(32, repetitions-start)
        z = rng.standard_normal((count, n-1))
        with np.errstate(over="raise", invalid="raise"):
            total = np.exp(sigma*z-sigma*sigma/2).sum(axis=1)
        a = n-total
        positive = a > 0
        p = np.zeros(count)
        d = np.log(a[positive])/sigma + sigma/2
        p[positive] = a[positive]*ndtr(d)-ndtr(d-sigma)
        if np.any(p < 0) or np.any(p > n) or np.any(~np.isfinite(p)):
            raise FloatingPointError("conditional payoff lost its bounds")
        payoff[start:start+count] = p/n
    mean_payoff = float(np.mean(payoff))
    if mean_payoff <= 0:
        raise FloatingPointError("sampled payoff is zero; increase repetitions")
    factor = np.log(2*n) + log_mean
    se = float(np.std(payoff, ddof=1)/np.sqrt(repetitions))
    return {"mad": _exp(factor + np.log(mean_payoff)),
            "mc_se": _exp(factor + np.log(se)) if se > 0 else 0.0}


def normal_location_mixture_sum_mad(n, separation, *, sigma=1.0):
    """Exact binomial mixture for X = separation*R + sigma*Z.

R takes +/-1 equally, Z is independent standard normal; iid summands.
separation>=0, sigma>0, n<=10000. There are n+1 conditional normal laws.
"""
    n = _n(n)
    a, sigma = _scalar(separation, "separation"), _scalar(sigma, "sigma", positive=True)
    if a < 0 or n > 10000:
        raise ValueError("require separation>=0 and n<=10000")
    # Normalize before evaluating absolute-normal moments to avoid squaring
    # dimensional scales or overflowing means of representable mixtures.
    unit = max(a, sigma)
    k = np.arange(n+1)
    location = (a/unit)*np.abs(2*k-n)
    sd = (sigma/unit)*np.sqrt(n)
    # When tiny sigma/unit underflows, use the limiting point masses.
    if sd == 0:
        values = location
    else:
        with np.errstate(over="ignore", under="ignore", divide="ignore"):
            ratio = location/sd
            values = sd*np.sqrt(2/np.pi)*np.exp(-ratio*ratio/2) + location*erf(ratio/np.sqrt(2))
    total = float(np.dot(binom.pmf(k, n, .5), values))
    return _exp(np.log(unit) + np.log(total))


def gaussian_equivalent_n(sum_mad, n_g, *, max_n=1_000_000):
    """Smallest integer n with M(n)/(n*M(1)) <= 1/sqrt(n_g), or None.

sum_mad is a deterministic population-MAD callable for iid integrable sums,
with finite positive M(1). Average MAD is nonincreasing (leave-one-out
Jensen), permitting doubling and binary search. Do not supply noisy estimates.
None means the search cap was insufficient, not an infinite required size.
    n_g and max_n are integers in [1,10 million]. Matching is in relative mean
    absolute error, not variance, confidence coverage, or tail probability.
    Comparisons allow 8 machine epsilons times max(1,abs(log target)) to
    absorb rounding at exact equalities. Nearer crossings are indistinguishable.
"""
    n_g, max_n = _n(n_g), _n(max_n)
    m1 = _scalar(sum_mad(1), "M(1)", positive=True)
    if n_g == 1:
        return 1
    target = -.5*np.log(n_g)

    def qualifies(n):
        m = _scalar(sum_mad(n), "M(n)", positive=True)
        tolerance = 8*np.finfo(float).eps*max(1, abs(target))
        # For the required iid population curve, 1 <= M(n)/M(1) <= n.
        # Divide before taking logs to avoid cancellation from physical units.
        return np.log(m/m1)-np.log(n) <= target + tolerance

    lo, hi = 1, min(2, max_n)
    while not qualifies(hi):
        if hi == max_n:
            return None
        lo, hi = hi, min(2*hi, max_n)
    while hi-lo > 1:
        mid = (lo+hi)//2
        if qualifies(mid):
            hi = mid
        else:
            lo = mid
    return hi


__all__ = ["kappa_from_mads", "stable_kappa", "gaussian_sum_mad", "gamma_sum_mad",
           "student_sum_mad", "estimate_sum_mad", "lognormal_sum_mad",
           "normal_location_mixture_sum_mad", "gaussian_equivalent_n"]
