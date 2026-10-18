"""Finite exposure models for the chapter 3 notes, without sampling or data.

Probabilities use log1p/expm1 where subtraction would lose rare-event mass.
Ordinary floating-point rounding and underflow remain possible. Functions
reject nonfinite inputs; overflow of a reported finite quantity raises.
"""

from __future__ import annotations

from decimal import Decimal, localcontext
import math
import operator

import numpy as np
from numpy.typing import ArrayLike, NDArray


def _count(value: int, *, minimum: int = 0) -> int:
    if isinstance(value, (bool, np.bool_)):
        raise ValueError("count must be an integer, not a boolean")
    try:
        count = operator.index(value)
    except TypeError as exc:
        raise ValueError("count must be an integer") from exc
    if not minimum <= count <= 2**53:
        raise ValueError(f"count must lie in [{minimum}, 2**53]")
    return count


def _probability(value: float) -> float:
    q = float(value)
    if not math.isfinite(q) or not 0 <= q <= 1:
        raise ValueError("probability must be finite and lie in [0, 1]")
    return q


def _vector(values: ArrayLike, name: str) -> NDArray[np.float64]:
    result = np.asarray(values, dtype=float)
    if result.ndim != 1 or not np.all(np.isfinite(result)):
        raise ValueError(f"{name} must be a finite one-dimensional array")
    return result


def repeated_event_probability(probability: float, trials: int) -> float:
    """Chance of at least one event in independent equal-probability trials.

    ``trials`` is an integer in [0, 2**53]. Zero trials give zero, including
    probability one. Small positive probabilities are preserved by expm1.
    Also gives exact sample total variation for the disjoint contamination
    model in the notes, not for arbitrary overlapping mixtures.
    """
    q = _probability(probability)
    n = _count(trials)
    if n == 0 or q == 0:
        return 0.0
    if n == 1:
        return q
    if q == 1:
        return 1.0
    return -math.expm1(n * math.log1p(-q))


def survival_from_hazards(hazards: ArrayLike) -> NDArray[np.float64]:
    """Survival at horizons 0..N from N conditional hazards in [0, 1].

    Hazards condition on survival, so independence is not required. After a
    hazard of one, later entries cannot change survival from zero and have
    no conditional-probability interpretation on the unreachable branch.
    An empty list returns [1]. Very small survival may underflow to zero.
    """
    h = _vector(hazards, "hazards")
    if np.any((h < 0) | (h > 1)):
        raise ValueError("hazards must lie in [0, 1]")
    with np.errstate(divide="ignore"):
        log_survival = np.cumsum(np.log1p(-h))
    return np.concatenate(([1.0], np.exp(log_survival)))


def finite_payoff_mean(probabilities: ArrayLike, payoffs: ArrayLike) -> float:
    """Expected payoff of a finite law; no implicit normalization.

    Inputs are equally sized nonempty finite vectors. Probabilities must
    lie in [0, 1] and sum to one within an absolute tolerance of 1e-12.
    This helper says nothing about integrability of an unbounded model.
    """
    p = _vector(probabilities, "probabilities")
    x = _vector(payoffs, "payoffs")
    if p.size == 0 or p.shape != x.shape:
        raise ValueError("probabilities and payoffs must have equal nonzero length")
    if np.any((p < 0) | (p > 1)) or not math.isclose(
        math.fsum(p), 1.0, rel_tol=0, abs_tol=1e-12
    ):
        raise ValueError("probabilities must sum to one and lie in [0, 1]")
    return math.fsum(float(pi) * float(xi) for pi, xi in zip(p, x))


def absorbing_resource_path(initial: float, increments: ArrayLike) -> NDArray[np.float64]:
    """Resources including the initial value, stopped at a nonpositive total.

    ``initial`` is finite and nonnegative; increments form a finite vector.
    After first reaching a nonpositive total the path is zero forever, even
    if later increments are positive. Overflow before ruin raises.
    """
    resource = float(initial)
    if not math.isfinite(resource) or resource < 0:
        raise ValueError("initial resources must be finite and nonnegative")
    changes = _vector(increments, "increments")
    path = np.empty(changes.size + 1)
    path[0] = resource
    for k, change in enumerate(changes, start=1):
        if resource > 0:
            resource += float(change)
            if not math.isfinite(resource):
                raise OverflowError("resource update is not representable")
            resource = max(0.0, resource)
        path[k] = resource
    return path


def split_power_damage_logsf(
    threshold: ArrayLike, *, alpha: float, power: float, modules: int,
    exposure: float = 1.0, x_m: float = 1.0,
) -> NDArray[np.float64]:
    """Log survival of D_m = exposure**power * m**(1-power) * X**power.

    X is exact Pareto(alpha, x_m). Parameters are positive and finite,
    modules is in [1, 2**53], and thresholds are finite and nonnegative.
    Scalars yield a zero-dimensional array. The calculation uses log space
    with Decimal refinement near cancellation or the support boundary; it
    does not simulate or truncate X. Unrepresentable transformed parameters
    raise OverflowError. Splitting reduces damage only when power > 1.
    """
    m = _count(modules, minimum=1)
    alpha, power, exposure, x_m = map(float, (alpha, power, exposure, x_m))
    if not all(math.isfinite(v) and v > 0 for v in (alpha, power, exposure, x_m)):
        raise ValueError("alpha, power, exposure and x_m must be positive and finite")
    u = np.asarray(threshold, dtype=float)
    if not np.all(np.isfinite(u)) or np.any(u < 0):
        raise ValueError("thresholds must be finite and nonnegative")
    log_exposure, log_x_m, log_m = math.log(exposure), math.log(x_m), math.log(m)
    log_scale = math.fsum((log_exposure, log_x_m, -log_m))
    log_minimum = log_m + power * log_scale
    if abs(log_scale) <= 1e-8 * (abs(log_exposure) + abs(log_x_m) + abs(log_m)):
        # Near exposure*x_m/m = 1, rounded logs can erase the scale or
        # amplify its error by a large power. Form the ratio before its log.
        with localcontext() as context:
            context.prec = 80
            scale = Decimal.from_float(exposure) * Decimal.from_float(x_m) / Decimal(m)
            log_minimum = float(Decimal(m).ln() + Decimal.from_float(power) * scale.ln())
    exponent = alpha / power
    if not math.isfinite(log_minimum) or not math.isfinite(exponent) or exponent == 0:
        raise OverflowError("transformed parameters are not representable")
    with np.errstate(divide="ignore"):
        log_u = np.log(u)
    with np.errstate(over="raise", invalid="raise"):
        # Clipping before multiplication keeps below-support values at zero.
        result = np.asarray(-exponent * np.maximum(log_u - log_minimum, 0))
    near_support = (u > 0) & (
        np.abs(log_u - log_minimum) <= 1e-8 * (np.abs(log_u) + abs(log_minimum))
    )
    if np.any(near_support):
        # Two rounded logs may coincide just above the cutoff. A large
        # exponent can turn that lost difference into a large log-tail error.
        with localcontext() as context:
            decimal_power = Decimal.from_float(power)
            context.prec = max(80, 80 - decimal_power.adjusted())
            scale = Decimal.from_float(exposure) * Decimal.from_float(x_m) / Decimal(m)
            minimum = Decimal(m) * scale ** decimal_power
            for index in np.ndindex(u.shape):
                if near_support[index]:
                    log_ratio = (Decimal.from_float(float(u[index])) / minimum).ln()
                    result[index] = float(
                        -(Decimal.from_float(alpha) / decimal_power) * max(log_ratio, Decimal(0))
                    )
    return result


def block_failure_summary(probability: float, blocks: int, exposure: float = 1.0) -> dict[str, float]:
    """Exact summary of equal independent all-or-nothing exposure blocks.

    Each block fails with the same probability; total exposure is positive
    and finite. One block represents a common shock to all nominal modules.
    All-failure probability can underflow for large block counts. Counts
    are integers in [1, 2**53]. No claim about network dynamics is made.
    """
    q = _probability(probability)
    k = _count(blocks, minimum=1)
    a = float(exposure)
    if not math.isfinite(a) or a <= 0:
        raise ValueError("exposure must be positive and finite")
    # Keep both the large scale and small Bernoulli factor in log space.
    # Multiplying or dividing those factors first can overflow/underflow.
    variance = 0.0 if q in (0, 1) else math.exp(
        2 * math.log(a) + math.log(q) + math.log1p(-q) - math.log(k)
    )
    return {
        "mean": a * q,
        "variance": variance,
        "any_failure": repeated_event_probability(q, k),
        "total_failure": q**k,
    }
