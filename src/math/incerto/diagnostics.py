"""Finite-sample return diagnostics; no data acquisition or tail-law verdicts.

All observations must be real, finite, nonempty vectors. Arithmetic that
overflows raises FloatingPointError. NaN denotes a specified undefined sample
statistic, never an inferred infinite population moment.
"""

from __future__ import annotations

import numpy as np
from scipy.stats import norm

from xmath.incerto.concentration import kappa_from_mads
from xmath.incerto.estimators import hill_alpha_estimator, mean_excess


def _sample(x):
    if np.iscomplexobj(x):
        raise ValueError("sample must be real")
    values = np.asarray(x, dtype=float)
    if values.ndim != 1 or not values.size or not np.all(np.isfinite(values)):
        raise ValueError("sample must be a nonempty finite vector")
    return values


def _integer(n, *, minimum=1):
    if isinstance(n, (bool, np.bool_)) or not isinstance(n, (int, np.integer)) or n < minimum:
        raise ValueError(f"count must be an integer >= {minimum}")
    return int(n)


def aggregate_returns(returns, horizon, *, overlap=False):
    """Sum successive returns; disjoint blocks by default, dropping the suffix.

    Require integer 1 <= horizon <= sample size. With overlap=True, return
    every consecutive window (stride one). No calendar resampling or padding.
    The input is in time order; overlapping outputs are not independent.
    """
    x, h = _sample(returns), _integer(horizon)
    if h > x.size or not isinstance(overlap, (bool, np.bool_)):
        raise ValueError("horizon must fit the sample and overlap must be boolean")
    blocks = (np.lib.stride_tricks.sliding_window_view(x, h) if overlap
              else x[:x.size // h * h].reshape(-1, h))
    with np.errstate(over="raise", invalid="raise"):
        return blocks.sum(axis=1)


def sample_excess_kurtosis(sample):
    """Central m4/m2**2 - 3 with divisor n; no bias correction.

    Constant samples, including singletons, return nan. Translation and scaling
    avoid forming unscaled fourth powers. This is a sample descriptor only.
    """
    x = _sample(sample)
    if np.all(x == x[0]):
        return float("nan")
    with np.errstate(over="ignore"):
        shifted = x - x[0]
    if not np.all(np.isfinite(shifted)):
        shifted = x / np.max(np.abs(x)) - x[0] / np.max(np.abs(x))
    scaled = shifted / np.max(np.abs(shifted))
    centered = scaled - scaled.mean()
    second = np.mean(centered**2)
    return float(np.mean(centered**4) / second**2 - 3)


def maximum_drawdown(prices):
    """Largest peak-to-later-trough fractional decline in positive prices.

    Includes the first price in the running peak; a singleton or nondecreasing
    sequence gives zero. Returns a number in [0,1], possibly rounded to 1.
    This is neither a log drawdown nor a drawdown of a sign-filtered series.
    """
    p = _sample(prices)
    if np.any(p <= 0):
        raise ValueError("prices must be strictly positive")
    return float(np.max(1 - p / np.maximum.accumulate(p)))


def moment_share_path(sample, p=4.0):
    """Prefix max |x|**p / sum |x|**p; raw absolute powers, no recentering.

    Require finite real scalar p > 0. All-zero prefixes return nan. Keep the
    sum scaled by the running maximum, using log ratios for power rescaling.
    Extreme p whose log rescalings overflow raises FloatingPointError.
    """
    x = _sample(sample)
    if (np.ndim(p) != 0 or np.iscomplexobj(p) or isinstance(p, (bool, np.bool_))
            or not np.isfinite(p) or p <= 0):
        raise ValueError("p must be a positive finite real scalar")
    result = np.full(x.shape, np.nan)
    peak, total = 0.0, 0.0
    with np.errstate(over="raise", invalid="raise", under="ignore"):
        for i, value in enumerate(np.abs(x)):
            if value > 0:
                if peak == 0:
                    peak, total = value, 1.0
                else:
                    low, high = min(value, peak), max(value, peak)
                    gap = high - low
                    log_ratio = (-np.log1p(gap / low) if gap <= low
                                 else np.log(low) - np.log(high))
                    weight = np.exp(float(p) * log_ratio)
                    total = total * weight + 1 if value > peak else total + weight
                    peak = high
            if total:
                result[i] = 1 / total
    return result


def record_counts(sample):
    """Cumulative strict upper/lower records, extrema, and iid-continuous null.

    The first observation counts on both sides; ties do not set records.
    iid_mean=H_n and iid_variance=H_n-sum(1/j**2) are reference sequences for
    EACH side, valid under iid continuous sampling, not for arbitrary ties or
    dependence. No p-value or independence decision is returned.
    """
    x = _sample(sample)
    maxima, minima = np.maximum.accumulate(x), np.minimum.accumulate(x)
    reciprocal = 1.0 / np.arange(1, x.size + 1)
    return {"upper": np.cumsum(np.r_[True, x[1:] > maxima[:-1]]),
            "lower": np.cumsum(np.r_[True, x[1:] < minima[:-1]]),
            "maximum": maxima, "minimum": minima,
            "iid_mean": np.cumsum(reciprocal),
            "iid_variance": np.cumsum(reciprocal * (1 - reciprocal))}


def conditional_tail_ratio(sample, thresholds, *, min_exceedances=1):
    """Strict empirical E[X | X>u]/u = 1 + mean_excess/u for positive u.

    Returns threshold, mean_excess, exceedances and ratio arrays. Retain nan
    when fewer than min_exceedances remain. Negative observations are allowed;
    apply separately to r and -r for gain/loss tails. Reuses mean_excess.
    """
    x, u = _sample(sample), _sample(thresholds)
    if np.any(u <= 0):
        raise ValueError("thresholds must be strictly positive")
    count = _integer(min_exceedances)
    with np.errstate(over="raise", invalid="raise", divide="raise"):
        result = mean_excess(x, u, min_exceedances=count)
        result["ratio"] = 1 + result["mean_excess"] / u
    return result


def aggregation_diagnostics(returns, horizons=(1, 5, 21), *, overlap=False):
    """Counts, dropped suffix, excess kurtosis, raw mean AD and plug-in kappa.

    Each horizon's sums are centered at their OWN sample mean. The base MAD
    uses all daily observations. Kappa is relative to horizon 1; at horizon 1,
    at zero MAD, or when aggregated MAD decreases below daily MAD, return nan.
    Equal positive MADs give -inf via kappa_from_mads; no clipping to [0,1].
    This comparison is descriptive, not an iid resampling experiment.
    """
    x = _sample(returns)
    hs = [_integer(h) for h in horizons]
    if not hs:
        raise ValueError("at least one horizon is required")
    with np.errstate(over="raise", invalid="raise"):
        base = float(np.mean(np.abs(x - x.mean())))
        result = []
        for h in hs:
            sums = aggregate_returns(x, h, overlap=overlap)
            mad = float(np.mean(np.abs(sums - sums.mean())))
            kappa = (float("nan") if h == 1 or mad < base
                     else kappa_from_mads(base, mad, h))
            result.append({"horizon": h, "blocks": len(sums),
                           "dropped": 0 if overlap else len(x) % h,
                           "excess_kurtosis": sample_excess_kurtosis(sums),
                           "mad": mad, "kappa": kappa})
    return result


def chronological_tail_check(returns, *, train_size=None, probability=0.95):
    """Freeze Gaussian and empirical loss quantiles on an initial training set.

    Loss is minus log return. Default split is floor(n/2), at least two training
    and one test observation. Gaussian fit uses sample mean and ddof=0 std;
    empirical quantile uses method='higher'. Count strict held-out exceedances
    and report their mean loss (nan when none). No refitting, shuffling,
    confidence interval, annualization, or implied calibration guarantee.
    """
    x = _sample(returns)
    split = _integer(len(x) // 2 if train_size is None else train_size, minimum=2)
    if split >= len(x):
        raise ValueError("at least one held-out observation is required")
    if (np.ndim(probability) != 0 or np.iscomplexobj(probability)
            or not np.isfinite(probability) or not 0 < probability < 1):
        raise ValueError("probability must be a finite scalar in (0,1)")
    train, test = -x[:split], -x[split:]
    with np.errstate(over="raise", invalid="raise"):
        cutoffs = {"gaussian": train.mean() + train.std() * norm.ppf(probability),
                   "empirical": np.quantile(train, probability, method="higher")}
        result = {"train_size": split, "test_size": len(test),
                  "probability": float(probability)}
        for name, threshold in cutoffs.items():
            exceeded = test[test > threshold]
            result[name] = {"threshold": float(threshold), "exceedances": len(exceeded),
                            "frequency": len(exceeded) / len(test),
                            "mean_exceedance_loss": (float(exceeded.mean())
                                                     if len(exceeded) else float("nan"))}
    return result


def sp500_diagnostics(prices):
    """Describe a local PriceSeries using all chronological close-to-close returns.

    Validate positive finite closes and strictly increasing nonmissing dates;
    require at least 44 closes. No interpolation, gap removal or fetch. Report
    full/first-half/second-half diagnostics, overlapping sensitivity, and a
    frozen chronological quantile comparison. Tail thresholds are positive-side
    sample quantiles (.8,.9,.95); Hill counts are floor(.05n), floor(.1n),
    floor(.2n), bounded below by 1 and below n. These are descriptive choices,
    never selected by apparent goodness of fit. Days with zero return remain
    in aggregation/record diagnostics and leave both conditional tail samples.
    """
    p = _sample(prices.close)
    dates = np.asarray(prices.date, dtype="datetime64[D]")
    if (len(p) < 44 or np.any(p <= 0) or dates.shape != p.shape
            or np.any(np.isnat(dates)) or np.any(np.diff(dates).astype(int) <= 0)):
        raise ValueError("need >=44 positive closes with strictly increasing dates")
    _, r = prices.log_returns()
    result = {"start": str(dates[0]), "end": str(dates[-1]), "returns": len(r),
              "zero_returns": int(np.count_nonzero(r == 0)),
              "max_calendar_gap_days": int(np.max(np.diff(dates).astype(int))),
              "windows": {}, "holdout": chronological_tail_check(r)}
    split = len(r) // 2
    for label, start, stop in (("full", 0, len(r)), ("first_half", 0, split),
                              ("second_half", split, len(r))):
        sample = r[start:stop]
        records = record_counts(sample)
        window = {"start": str(dates[start]), "end": str(dates[stop]),
                  "n": len(sample), "drawdown": maximum_drawdown(p[start:stop+1]),
                  "aggregation": aggregation_diagnostics(sample),
                  "overlapping": aggregation_diagnostics(sample, overlap=True),
                  "records": {k: float(v[-1]) for k, v in records.items()},
                  "moment_shares": {str(power): float(moment_share_path(sample, power)[-1])
                                    for power in (1, 2, 3, 4)}, "tails": {}}
        for side, signed in (("gain", sample), ("loss", -sample)):
            positive = signed[signed > 0]
            tail = {"n": len(positive), "hill": [], "conditional": []}
            if len(positive) >= 2:
                ks = np.unique(np.maximum(1, (len(positive)*np.array([.05,.1,.2])).astype(int)))
                tail["hill"] = [{"k": int(k), "alpha": hill_alpha_estimator(positive, int(k))}
                                for k in ks if k < len(positive)]
                values = conditional_tail_ratio(signed, np.quantile(positive, [.8,.9,.95]),
                                                min_exceedances=5)
                tail["conditional"] = [{key: float(value[i]) for key, value in values.items()}
                                       for i in range(3)]
            window["tails"][side] = tail
        result["windows"][label] = window
    return result


def hinge_payoff(x, knots, slopes, *, value_at_first=0.0):
    """Continuous piecewise-linear function from ordered knots and segment slopes.

    For m>=1 strictly increasing finite knots, require m+1 finite slopes;
    value_at_first fixes the value at the first knot. Extrapolate with the first
    and last slopes. x may be any finite real scalar/array; output has its shape.
    Coefficients of (x-knot)_+ are successive slope differences, not angles.
    """
    k, s = _sample(knots), _sample(slopes)
    if len(s) != len(k)+1 or np.any(np.diff(k) <= 0):
        raise ValueError("need increasing knots and one more slope than knots")
    if (np.iscomplexobj(x) or np.iscomplexobj(value_at_first)
            or np.ndim(value_at_first) != 0 or not np.isfinite(value_at_first)):
        raise ValueError("x and anchor value must be finite and real")
    points = np.asarray(x, dtype=float)
    if not np.all(np.isfinite(points)):
        raise ValueError("x must be finite")
    with np.errstate(over="raise", invalid="raise"):
        # Evaluate the active segment to avoid cancellation of large hinges.
        at_knots = value_at_first + np.r_[0.0, np.cumsum(s[1:-1] * np.diff(k))]
        segment = np.searchsorted(k, points, side="right")
        anchor = np.maximum(segment - 1, 0)
        y = at_knots[anchor] + s[segment] * (points - k[anchor])
    return float(y) if y.ndim == 0 else y
