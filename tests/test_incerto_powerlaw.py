"""Independent distribution identities, fitting checks, and failure contracts."""
from pathlib import Path
import os
import subprocess
import sys

import numpy as np
from numpy.testing import assert_allclose
import pytest
from scipy.integrate import quad
from scipy.special import exp1, gammaincc, gammaln, zeta
from scipy.stats import chi2, kstest, lognorm, norm, pareto, weibull_min

from xmath.incerto import powerlaw as pl
from xmath.incerto.estimators import hill_estimator

ROOT = Path(__file__).resolve().parents[1]


def test_continuous_mle_hill_and_scale():
    x = np.array([2., 3., 5., 9.])
    expected = 4/np.log(x/2).sum()
    assert pl.powerlaw_mle_continuous(x, 2) == pytest.approx(expected)
    # Hill excludes the order-statistic baseline; the inclusive fit counts it.
    assert expected == pytest.approx(4/3/hill_estimator(x, 3))
    assert pl.powerlaw_mle_continuous(x*1e150, 2e150) == pytest.approx(expected)
    assert pl.powerlaw_standard_error(2, 400) == .1


@pytest.mark.parametrize("alpha,xmin,discrete", [(1.6, 2, False), (3.1, 1, False),
                                                   (1.8, 1, True), (1.3, 8, True)])
def test_recover_known_exponent(alpha, xmin, discrete):
    # Independent SciPy generator for continuous; inverse zeta tested below.
    x = (pl.sample_powerlaw(alpha, xmin, 25000, discrete=True, random_state=271)
         if discrete else pareto.rvs(alpha, scale=xmin, size=25000,
                                    random_state=np.random.default_rng(271)))
    mle = pl.powerlaw_mle_discrete if discrete else pl.powerlaw_mle_continuous
    assert abs(mle(x, xmin)-alpha) < .07
    assert pl.ks_distance_powerlaw(x, alpha, xmin, discrete=discrete) < .015


def test_exact_discrete_draw_inverts_cdf_and_retains_large_minimum():
    rng = np.random.default_rng(19)
    uniforms = rng.random(300)
    for u in (1, 7, 10000):
        x = pl.sample_powerlaw(1.4, u, 300, discrete=True, random_state=19)
        left = 1-zeta(2.4, x)/zeta(2.4, u)
        right = 1-zeta(2.4, x+1)/zeta(2.4, u)
        assert np.all(left <= uniforms) and np.all(uniforms <= right)
        assert np.issubdtype(x.dtype, np.integer) and x.min() >= u
    x = pl.sample_powerlaw(2, 3, 5000, random_state=1)
    assert kstest(x, pareto(2, scale=3).cdf).statistic < .025


def test_discrete_likelihood_and_fisher_information():
    x = np.array([1, 1, 1, 2, 2, 3, 5, 9, 12])
    alpha = pl.powerlaw_mle_discrete(x, 1)
    def ell(a):
        return -len(x)*np.log(zeta(a+1, 1))-(a+1)*np.log(x).sum()
    assert ell(alpha) > ell(alpha-.02)
    assert ell(alpha) > ell(alpha+.02)
    # Independent long finite series; omitted log-weighted tail is negligible.
    k = np.arange(1., 200001.)
    mass = k**-4/zeta(4, 1)
    fisher = np.dot(mass, np.log(k)**2)-np.dot(mass, np.log(k))**2
    se = pl.powerlaw_standard_error(3, 400, discrete=True)
    assert se == pytest.approx(1/np.sqrt(400*fisher), rel=1e-6)


@pytest.mark.parametrize('alpha,xmin', [(3., 1), (40., 1), (80., 1), (10., 7), (40., 10000)])
def test_discrete_fisher_information_resolves_small_log_moments(alpha, xmin):
    # Independent direct series: its omitted tail is negligible for these
    # exponents. Relative weights also cover zeta underflow at large xmin.
    k = np.arange(float(xmin), xmin+200000.)
    logs = np.log(k/xmin)
    mass = (k/xmin)**(-(alpha+1))
    mass /= mass.sum()
    mean = np.dot(mass, logs)
    information = np.dot(mass, (logs-mean)**2)
    expected = 1/np.sqrt(100*information)
    assert pl.powerlaw_standard_error(alpha, 100, xmin=xmin, discrete=True) == pytest.approx(
        expected, rel=1e-9)


@pytest.mark.parametrize('alpha', [.01, .2, 1., 40.])
def test_discrete_fisher_large_cutoff_continuous_limit(alpha):
    assert pl.powerlaw_standard_error(alpha, 100, xmin=10**10, discrete=True) == pytest.approx(
        alpha/10, rel=1e-9)


@pytest.mark.parametrize('alpha', [1060, 1100])
def test_discrete_fisher_rejects_underflowed_information(alpha):
    with pytest.raises(FloatingPointError, match='not resolved'):
        pl.powerlaw_standard_error(alpha, 100, discrete=True)


def test_half_integer_approximation_is_not_exact_at_small_cutoff():
    # Zeta generator from SciPy supplies independent integer samples.
    x = np.random.default_rng(42).zipf(3, size=20000)
    exact = pl.powerlaw_mle_discrete(x, 1)
    approx = pl.powerlaw_mle_discrete(x, 1, approximate=True)
    assert abs(exact-2) < .08
    assert abs(approx-2) > .5


def test_ks_continuous_jump_sides_and_discrete_empty_gaps():
    x = np.array([1., 1., 2., 5.])
    assert pl.ks_distance_powerlaw(x, 2, 1) == pytest.approx(kstest(x, pareto(2).cdf).statistic)
    grid = np.arange(0, 25)
    empirical = np.mean(x[:, None] <= grid, axis=0)
    model = np.where(grid < 1, 0, 1-zeta(3, grid+1)/zeta(3, 1))
    assert pl.ks_distance_powerlaw(x, 2, 1, discrete=True) == pytest.approx(max(abs(empirical-model)))


def test_ks_selects_known_break_in_seeded_mixture():
    rng = np.random.default_rng(982)
    x = rng.uniform(1, 4, 6000)
    tail = rng.random(x.size) < .3
    x[tail] = pareto.rvs(1.8, scale=4, size=tail.sum(), random_state=rng)
    fit = pl.select_xmin(x, candidates=np.arange(1, 6.01, .25), min_tail=200)
    assert 3.75 <= fit['xmin'] <= 4.5
    assert abs(fit['alpha']-1.8) < .15
    assert fit['ks'] == np.nanmin(fit['distances'])
    assert fit['n_tail'] == np.count_nonzero(x >= fit['xmin'])
    assert fit['ks'] < fit['distances'][0]/4


def test_candidate_policy_and_ties():
    fit = pl.select_xmin([1, 1, 2, 3, 6], min_tail=2)
    assert_allclose(fit['xmins'], [1, 2, 3, 6])
    assert_allclose(fit['counts'], [5, 3, 2, 1])
    assert np.isnan(fit['distances'][-1])
    fixed = pl.select_xmin([1, 1, 2, 3, 6], candidates=[1], min_tail=2, discrete=True)
    assert fixed['n_tail'] == 5


def test_bootstrap_refits_body_tail_and_joint_uncertainty():
    x = np.r_[np.linspace(1, 2, 50), pl.sample_powerlaw(2, 3, 80, random_state=8)]
    result = pl.powerlaw_gof_bootstrap(x, replicates=16, min_tail=25, random_state=90)
    assert result['p_value'] == np.mean(result['ks_samples'] >= result['fit']['ks'])
    assert np.unique(result['xmins']).size > 1
    assert np.unique(result['generated_tail_counts']).size > 1
    assert result['generated_tail_counts'].max() < len(x)
    again = pl.powerlaw_gof_bootstrap(x, replicates=16, min_tail=25, random_state=90)
    assert_allclose(result['ks_samples'], again['ks_samples'])
    empirical = pl.powerlaw_bootstrap_se(x, replicates=16, min_tail=25, random_state=91)
    assert empirical['alpha_se'] == pytest.approx(np.std(empirical['alphas'], ddof=1))
    assert empirical['xmin_se'] > 0
    assert_allclose(empirical['covariance'], np.cov([empirical['alphas'], empirical['xmins']], ddof=1))


def test_bootstrap_single_candidate_is_reused_and_discrete_works():
    x = pl.sample_powerlaw(1.4, 2, 120, discrete=True, random_state=10)
    result = pl.powerlaw_gof_bootstrap(x, discrete=True, candidates=[2],
                                      min_tail=20, replicates=8, random_state=8)
    assert_allclose(result['xmins'], 2)
    assert_allclose(result['generated_tail_counts'], len(x))
    assert result['worst_case_mc_se'] == pytest.approx(.5/np.sqrt(8))


def test_bootstrap_failure_is_not_silently_discarded():
    with pytest.raises(RuntimeError, match='no replicates discarded'):
        pl.powerlaw_bootstrap_se([1, 2], min_tail=2, replicates=30, random_state=1)


@pytest.mark.parametrize('generator,sign', [('pareto', 1), ('exponential', -1)])
def test_lr_sign_for_known_generators(generator, sign):
    rng = np.random.default_rng(17)
    x = pareto.rvs(3, size=5000, random_state=rng) if generator == 'pareto' else 1+rng.exponential(size=5000)
    first = pl.fit_tail_model(x, 1)
    second = pl.fit_tail_model(x, 1, 'exponential')
    result = pl.likelihood_ratio_test(first['loglik'], second['loglik'])
    assert sign*result['R'] > 10
    assert sign*result['normalized_R'] > 2
    assert result['p_value'] < .05


def test_alternative_lognormal_conditional_fit_and_lr():
    rng = np.random.default_rng(20)
    x = rng.lognormal(1, .6, 5000)
    u = 1.
    fit = pl.fit_tail_model(x, u, 'lognormal')
    assert fit['success']
    p = fit['parameters']
    assert abs(p['mu']-1) < .05 and abs(p['sigma']-.6) < .05
    law = lognorm(p['sigma'], scale=np.exp(p['mu']))
    assert_allclose(fit['loglik'], law.logpdf(x[x >= u])-law.logsf(u), atol=1e-12)
    power = pl.fit_tail_model(x, u)
    assert pl.likelihood_ratio_test(power['loglik'], fit['loglik'])['R'] < -100


def test_weibull_conditional_fit_normalization_and_exponential_special_case():
    rng = np.random.default_rng(99)
    x = 3*rng.weibull(.7, 6000)
    fit = pl.fit_tail_model(x, 1, 'stretched_exponential')
    assert fit['success']
    p = fit['parameters']
    assert abs(p['shape']-.7) < .07
    law = weibull_min(p['shape'], scale=p['scale'])
    assert_allclose(fit['loglik'], law.logpdf(x[x >= 1])-law.logsf(1), atol=1e-12)
    exp = pl.fit_tail_model(x, 1, 'exponential')
    assert fit['loglikelihood'] >= exp['loglikelihood']-1e-8


def test_exponential_constant_sample_above_threshold():
    fit = pl.fit_tail_model([.5, 2, 2], 1, 'exponential')
    assert fit['success'] and not fit['boundary']
    assert fit['n_tail'] == 2
    assert fit['parameters'] == {'rate': 1.}
    assert_allclose(fit['loglik'], [-1., -1.])
    assert fit['loglikelihood'] == -2.
    with pytest.raises(ValueError, match='degenerate'):
        pl.fit_tail_model([1, 1], 1, 'exponential')


@pytest.mark.parametrize('a,log_beta', [(-9., -10.), (-9., -100.), (-.5, -40.),
                                      (-99., -10.), (.5, -10.), (-9., 4.),
                                      (-9999., -100.)])
def test_cutoff_normalizer_remote_mode_against_gamma_and_integral(a, log_beta):
    beta = np.exp(log_beta)
    actual = pl._cutoff_log_normalizer(a-1, beta)
    expected = beta + (a-1)*log_beta + gammaln(1-a) + np.log(gammaincc(1-a, beta))
    assert actual == pytest.approx(expected, rel=3e-13, abs=2e-10)
    # Independently integrate the claimed density in r=beta*x/xmin,
    # where its mass stays visible even for tiny beta and negative a.
    def density(r):
        return np.exp(-a*np.log(r)-r + beta + (a-1)*log_beta - actual)
    split = max(beta, 1., -a)
    total = quad(density, beta, split, epsabs=1e-10)[0]
    total += quad(density, split, np.inf, epsabs=1e-10)[0]
    assert total == pytest.approx(1., abs=2e-9)


def test_cutoff_normalizer_preserves_tail_beyond_exponential_overflow():
    beta = np.exp(-700.)
    # At a=1, substitution r=beta*x/xmin gives exp(beta)*E1(beta).
    expected = beta + np.log(exp1(beta))
    assert pl._cutoff_log_normalizer(0., beta) == pytest.approx(expected, abs=1e-10, rel=0)


@pytest.mark.parametrize('xmin', [1., 1e-90, 1e90])
def test_cutoff_search_finds_small_rate_on_wide_sample(xmin):
    x = xmin*np.geomspace(1., 1e9, 1000)
    pure = pl.fit_tail_model(x, xmin)
    fit = pl.fit_tail_model(x, xmin, 'truncated_powerlaw')
    assert fit['success'] and not fit['boundary']
    assert 0 < fit['parameters']['rate']*xmin < np.exp(-18)
    # The review's fixed feasible point already improves log L by 107.06193.
    lr = pl.likelihood_ratio_test(pure['loglik'], fit['loglik'], nested=True)
    assert lr['statistic'] >= 214.12386


def test_cutoff_boundary_requires_nonpositive_inward_score():
    x = np.r_[np.ones(99), 10.]
    pure = pl.fit_tail_model(x, 1)
    alpha = pure['parameters']['alpha']
    assert alpha > 1 and 1/(alpha-1) < np.mean(x-1)
    fit = pl.fit_tail_model(x, 1, 'truncated_powerlaw')
    assert fit['success'] and fit['boundary']
    assert fit['parameters'] == {'a': alpha+1, 'rate': 0.}
    assert_allclose(fit['loglik'], pure['loglik'])


def test_cutoff_search_expands_exponent_bounds():
    x = np.linspace(1.8, 2.2, 41)
    fit = pl.fit_tail_model(x, 1, 'truncated_powerlaw')
    assert fit['success'] and not fit['boundary']
    assert fit['parameters']['a'] < -19
    assert fit['loglikelihood'] > pl.fit_tail_model(x, 1, 'exponential')['loglikelihood']


@pytest.mark.parametrize('optimizer_success', [False, True])
def test_cutoff_inferior_search_does_not_certify_boundary(monkeypatch, optimizer_success):
    from scipy.optimize import OptimizeResult

    def stuck(objective, start, **kwargs):
        point = np.array([1., -4.])
        return OptimizeResult(x=point, fun=objective(point), success=optimizer_success)

    monkeypatch.setattr(pl, 'minimize', stuck)
    fit = pl.fit_tail_model(np.geomspace(1., 1e9, 1000), 1, 'truncated_powerlaw')
    assert not fit['success']
    assert 'not certified' in fit['status']


def test_cutoff_optimizer_failure_remains_unsuccessful(monkeypatch):
    original = pl.minimize

    def failed(*args, **kwargs):
        result = original(*args, **kwargs)
        result.success = False
        return result

    monkeypatch.setattr(pl, 'minimize', failed)
    fit = pl.fit_tail_model(np.geomspace(1., 1e9, 1000), 1, 'truncated_powerlaw')
    assert not fit['success'] and not fit['boundary']
    assert 'failed' in fit['status']


def test_cutoff_failure_after_expansion_is_not_masked_by_previous_success(monkeypatch):
    from scipy.optimize import OptimizeResult

    calls = 0

    def stuck(objective, start, **kwargs):
        nonlocal calls
        calls += 1
        # The initial box has a constrained optimum at alpha=-20. After
        # expansion, the optimizer fails to leave that same feasible point.
        point = np.array([-20., np.log(10.)])
        return OptimizeResult(x=point, fun=objective(point), success=calls <= 3)

    monkeypatch.setattr(pl, 'minimize', stuck)
    fit = pl.fit_tail_model(np.linspace(1.8, 2.2, 41), 1, 'truncated_powerlaw')
    assert calls > 3
    assert not fit['success'] and not fit['boundary']
    assert 'failed' in fit['status']


def test_cutoff_normalization_and_nested_boundary_contract():
    x = 2+np.random.default_rng(41).exponential(size=1000)
    fit = pl.fit_tail_model(x, 2, 'truncated_powerlaw')
    pure = pl.fit_tail_model(x, 2)
    assert fit['success']
    p = fit['parameters']
    # Independent integration in x coordinates; exported per-observation scores.
    a, rate = p['a'], p['rate']
    z = quad(lambda t: (t/2)**(-a)*np.exp(-rate*(t-2)), 2, np.inf)[0]
    expected = -a*np.log(x/2)-rate*(x-2)-np.log(z)
    assert_allclose(fit['loglik'], expected, atol=1e-8)
    result = pl.likelihood_ratio_test(pure['loglik'], fit['loglik'], nested=True)
    assert result['statistic'] > 0 and np.isnan(result['p_value'])
    assert 'calibration' in result['status']


def test_vuong_and_explicit_nested_reference_formulas():
    a, b = [1., 2., 5., 1.], [2., 1., 1., 0.]
    d = np.subtract(a, b)
    z = d.sum()/(np.sqrt(4)*np.std(d))
    result = pl.likelihood_ratio_test(a, b)
    assert result['normalized_R'] == pytest.approx(z)
    assert result['p_value'] == pytest.approx(2*norm.sf(abs(z)))
    reverse = pl.likelihood_ratio_test(b, a)
    assert reverse['R'] == -result['R'] and reverse['p_value'] == result['p_value']
    interior = pl.likelihood_ratio_test([0, 0], [1, 1], nested=True, calibration='chi2')
    boundary = pl.likelihood_ratio_test([0, 0], [1, 1], nested=True, calibration='boundary')
    assert interior['p_value'] == pytest.approx(chi2.sf(4, 1))
    assert boundary['p_value'] == interior['p_value']/2
    assert pl.likelihood_ratio_test([0, 0], [0, 0], nested=True, calibration='boundary')['p_value'] == 1
    assert np.isnan(pl.likelihood_ratio_test([1, 1], [0, 0])['p_value'])


@pytest.mark.parametrize('x', [[], [1], [1, np.nan], [1, np.inf], [0, 2], [-1, 2], [[1, 2]], [1+1j, 2]])
@pytest.mark.parametrize('function', [pl.powerlaw_mle_continuous, pl.powerlaw_mle_discrete,
                                      pl.fit_tail_model])
def test_invalid_samples(x, function):
    with pytest.raises(ValueError):
        function(x, 1)


@pytest.mark.parametrize('xmin', [0, -1, np.nan, np.inf, [1], 1+1j])
def test_invalid_cutoffs(xmin):
    with pytest.raises(ValueError):
        pl.powerlaw_mle_continuous([1, 2], xmin)


@pytest.mark.parametrize('call', [
    lambda: pl.powerlaw_mle_continuous([1, 1], 1),
    lambda: pl.powerlaw_mle_discrete([1, 1], 1),
    lambda: pl.powerlaw_mle_discrete([1, 2.5], 1),
    lambda: pl.powerlaw_mle_discrete([1, 2], 1.5),
    lambda: pl.powerlaw_mle_continuous([1, 2], 3),
    lambda: pl.select_xmin([1, 1], min_tail=2),
    lambda: pl.select_xmin([1, 2], candidates=[]),
    lambda: pl.select_xmin([1, 2], candidates=[np.nan]),
    lambda: pl.select_xmin([1, 2], min_tail=1),
    lambda: pl.powerlaw_standard_error(np.nan, 2),
    lambda: pl.sample_powerlaw(0, 1, 2),
    lambda: pl.sample_powerlaw(1, 1, 0),
    lambda: pl.fit_tail_model([1, 2], 1, 'unknown'),
    lambda: pl.fit_tail_model([1, 2], 1, 'lognormal', discrete=True),
    lambda: pl.likelihood_ratio_test([0, 1], [0]),
    lambda: pl.likelihood_ratio_test([0, np.nan], [0, 1]),
    lambda: pl.likelihood_ratio_test([1, 1], [0, 0], nested=True),
    lambda: pl.likelihood_ratio_test([0, 0], [1, 1], calibration='chi2'),
    lambda: pl.likelihood_ratio_test([0, 0], [1, 1], nested=True, calibration='boundary', df=2),
    lambda: pl.powerlaw_gof_bootstrap([1, 2], replicates=1),
])
def test_invalid_domains(call):
    with pytest.raises(ValueError):
        call()


def test_reexports():
    import xmath.incerto as incerto
    for name in pl.__all__:
        assert getattr(incerto, name) is getattr(pl, name)


def test_powerlaw_figures_match_fresh_processes_and_assets(tmp_path):
    script = ROOT/'demos/incerto/powerlaw_fitting.py'
    for run in ('a', 'b'):
        code = f"import runpy; runpy.run_path({str(script)!r})['main']({str(tmp_path/run)!r})"
        env = {**os.environ, 'MPLBACKEND': 'Agg', 'MPLCONFIGDIR': str(tmp_path/'mpl'),
               'OPENBLAS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1'}
        result = subprocess.run([sys.executable, '-c', code], env=env, cwd=tmp_path,
                                capture_output=True, text=True, timeout=60)
        assert result.returncode == 0, result.stdout+result.stderr
    for name in ('powerlaw-fitted-tail', 'powerlaw-ks-threshold'):
        first = (tmp_path/'a'/f'{name}.svg').read_bytes()
        assert first == (tmp_path/'b'/f'{name}.svg').read_bytes()
        assert first == (ROOT/f'assets/figures/incerto/{name}.svg').read_bytes()
        assert b'<dc:date>' not in first
