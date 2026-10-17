"""Focused tests for migrated probability distributions."""

import warnings

import numpy as np
import pytest

from xmath.incerto.distributions import (
    double_pareto,
    hypsecant2,
    pareto_type1,
    simple_normal_mixture,
    univariate_variance_gamma,
)


def test_double_pareto_pdf_cdf_and_sf_match_closed_forms() -> None:
    alpha = 3.0
    x = np.array([-2.0, 0.0, 4.0])

    np.testing.assert_allclose(
        double_pareto.pdf(x, alpha),
        0.5 * alpha * (1.0 + np.abs(x)) ** (-(alpha + 1.0)),
    )
    np.testing.assert_allclose(
        double_pareto.cdf(x, alpha),
        np.array(
            [
                0.5 * (1.0 - x[0]) ** (-alpha),
                0.5,
                1.0 - 0.5 * (1.0 + x[2]) ** (-alpha),
            ]
        ),
    )
    np.testing.assert_allclose(
        double_pareto.sf(4.0, alpha),
        0.5 * (1.0 + 4.0) ** (-alpha),
    )


def test_double_pareto_fractional_alpha_cdf_sf_do_not_warn() -> None:
    alpha = 1.5
    x = np.array([-4.0, 0.0, 4.0])

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        cdf = double_pareto.cdf(x, alpha)
        sf = double_pareto.sf(x, alpha)

    np.testing.assert_allclose(cdf + sf, np.ones_like(x))
    np.testing.assert_allclose(cdf[2], 1.0 - 0.5 * (1.0 + x[2]) ** (-alpha))
    np.testing.assert_allclose(sf[0], 1.0 - 0.5 * (1.0 - x[0]) ** (-alpha))


def test_double_pareto_ppf_roundtrip_and_moments() -> None:
    alpha = 3.0
    q = np.array([0.05, 0.25, 0.5, 0.75, 0.95])

    x = double_pareto.ppf(q, alpha)
    np.testing.assert_allclose(double_pareto.cdf(x, alpha), q)

    mean, variance = double_pareto.stats(alpha, moments="mv")
    assert mean == pytest.approx(0.0)
    assert variance == pytest.approx(1.0)

    assert np.isnan(double_pareto.mean(0.8))
    assert np.isnan(double_pareto.mean(1.0))
    assert double_pareto.mean(1.5) == pytest.approx(0.0)
    assert np.isinf(double_pareto.var(1.5))
    assert np.isnan(double_pareto.pdf(0.0, 0.0))


@pytest.mark.parametrize(
    ("alpha", "expected_mean", "expected_variance"),
    [(0.8, np.nan, np.inf), (1.0, np.nan, np.inf), (1.5, 0.0, np.inf), (3.0, 0.0, 1.0)],
)
def test_double_pareto_mean_and_variance_convention(
    alpha: float, expected_mean: float, expected_variance: float
) -> None:
    mean, variance = double_pareto.stats(alpha, moments="mv")

    np.testing.assert_allclose([mean, double_pareto.mean(alpha)], expected_mean)
    np.testing.assert_allclose([variance, double_pareto.var(alpha)], expected_variance)


def test_pareto_type1_matches_closed_forms() -> None:
    alpha = 3.0
    x = np.array([1.0, 2.0, 4.0])

    np.testing.assert_allclose(
        pareto_type1.pdf(x, alpha),
        alpha * x ** (-(alpha + 1.0)),
    )
    np.testing.assert_allclose(pareto_type1.sf(x, alpha), x**-alpha)
    np.testing.assert_allclose(
        pareto_type1.ppf(np.array([0.0, 0.75]), alpha),
        [1.0, 4 ** (1 / 3)],
    )

    mean, variance = pareto_type1.stats(alpha, moments="mv")
    assert mean == pytest.approx(alpha / (alpha - 1.0))
    assert variance == pytest.approx(alpha / ((alpha - 1.0) ** 2 * (alpha - 2.0)))
    assert np.isinf(pareto_type1.mean(1.0))
    assert np.isinf(pareto_type1.var(2.0))


def test_hypsecant2_basic_identities() -> None:
    assert hypsecant2.pdf(0.0) == pytest.approx(0.5)
    assert hypsecant2.cdf(0.0) == pytest.approx(0.5)
    assert hypsecant2.ppf(0.5) == pytest.approx(0.0)
    assert hypsecant2.var() == pytest.approx(np.pi**2 / 12.0)
    assert hypsecant2.chf(0.0) == pytest.approx(1.0)


def test_simple_normal_mixture_has_unit_variance() -> None:
    a = 0.4
    assert simple_normal_mixture.mean(a) == pytest.approx(0.0)
    assert simple_normal_mixture.var(a) == pytest.approx(1.0)

    x = np.array([-1.0, 0.0, 1.0])
    np.testing.assert_allclose(
        simple_normal_mixture.pdf(x, 0.0),
        simple_normal_mixture.pdf(x, a=0.0),
    )
    assert np.isnan(simple_normal_mixture.pdf(0.0, 1.0))


def test_univariate_variance_gamma_stats_and_symmetry() -> None:
    alpha = 2.0
    beta = 0.0
    lam = 1.5

    mean, variance = univariate_variance_gamma.stats(alpha, beta, lam, moments="mv")
    assert mean == pytest.approx(0.0)
    assert variance == pytest.approx(lam * 2.0 / alpha**2)

    assert univariate_variance_gamma.pdf(-0.7, alpha, beta, lam) == pytest.approx(
        univariate_variance_gamma.pdf(0.7, alpha, beta, lam)
    )
    assert univariate_variance_gamma.pdf(0.0, alpha, beta, lam) == pytest.approx(
        2.0 / np.pi
    )
    assert np.isnan(univariate_variance_gamma.pdf(0.7, 1.0, 2.0, lam))
