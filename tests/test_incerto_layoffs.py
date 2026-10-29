"""Synthetic fixtures only: no real layoffs data or downloads required."""
import csv
import json
from pathlib import Path
import warnings

import numpy as np
import pytest
from numpy.testing import assert_allclose, assert_array_equal

from xmath.incerto import (
    DatasetNotAvailable, clean_layoffs, load_layoffs, workforce_log_loss,
    hill_alpha_estimator, hill_stability_bootstrap,
)


def row(company='A', date='2020-03-11', n='10', frac='0.2'):
    return dict(company=company, date=date, n=n, frac=frac)


def test_grouping_preserves_missing_values_and_reporting_rule():
    data = clean_layoffs([
        row(' B ', n='', frac=''), row('A', n=10, frac=.2),
        row('A ', date='03/11/2020', n=20, frac=.1),
        row('A', date='2020-03-12', n='', frac=1),
        row('Zero', n=0, frac=0),
    ], source='synthetic')
    assert data.input_rows == 5
    assert data.source == 'synthetic'
    assert_array_equal(data.company, ['A', 'A', 'B', 'Zero'])
    assert_allclose(data.count, [30, np.nan, np.nan, 0], equal_nan=True)
    assert_allclose(data.fraction, [.2, 1, np.nan, 0], equal_nan=True)
    assert data.date.dtype == np.dtype('datetime64[D]')


def test_exact_duplicates_are_aggregated_not_silently_dropped():
    data = clean_layoffs([row(), row()])
    assert data.input_rows == 2
    assert data.count.tolist() == [20]
    assert data.fraction.tolist() == [.2]


def test_raw_csv_and_clean_csv_have_equivalent_events(tmp_path):
    raw = tmp_path/'raw.csv'
    raw.write_text('company,date,total_laid_off,percentage_laid_off\nA,03/11/2020,10.0,0.2\nA,03/11/2020,,0.3\n')
    cleaned = tmp_path/'clean.csv'
    cleaned.write_text('company,date,n,frac\nA,2020-03-11,10.0,0.2\nA,2020-03-11,,0.3\n')
    a, b = load_layoffs(raw), load_layoffs(cleaned)
    for attr in ('company', 'date', 'count', 'fraction'):
        assert_array_equal(getattr(a, attr), getattr(b, attr))
    assert a.count[0] == 10 and a.fraction[0] == .3


def test_loader_default_cache_and_missing_file(tmp_path, monkeypatch):
    monkeypatch.setenv('INCERTO_DATA_DIR', str(tmp_path))
    with pytest.raises(DatasetNotAvailable):
        load_layoffs()
    cache = tmp_path/'cache/layoffs/layoffs.csv'
    cache.parent.mkdir(parents=True)
    cache.write_text('company,date,n,frac\nA,2020-03-11,10,0.2\n')
    assert load_layoffs().count.tolist() == [10]


@pytest.mark.parametrize('rows', [[], [{}], [row(company=' ')], [row(date='2020-02-30')],
    [row(n=-1)], [row(n='2.5')], [row(n='inf')], [row(n=2**53)],
    [row(n=2**53-1), row(n=2)], [row(frac=-.1)], [row(frac=1.1)],
    [row(frac='inf')], [dict(company='A', date='2020-01-01', n=1)],
])
def test_bad_rows_rejected(rows):
    with pytest.raises(ValueError):
        clean_layoffs(rows)


def test_missing_numbers_are_not_zero():
    data = clean_layoffs([row(n=None, frac=np.nan)])
    assert np.isnan(data.count[0]) and np.isnan(data.fraction[0])


def test_logloss_inverse_zero_and_small_fraction():
    p = np.array([0., 1e-16, .1, .5, .9, .99])
    losses = workforce_log_loss(p)
    assert_allclose(-np.expm1(-losses), p, rtol=1e-14, atol=0)
    assert losses[0] == 0 and losses[1] > 0
    assert_allclose(losses[3:], np.log([2, 10, 100]))


@pytest.mark.parametrize('p', [[1], [-.1], [1.01], [np.nan], [np.inf], [[.1]], [1j]])
def test_logloss_requires_explicit_endpoint_and_missing_policy(p):
    with pytest.raises(ValueError):
        workforce_log_loss(p)


def test_bootstrap_matches_independent_order_statistic_calculation():
    x = np.exp(np.linspace(0, 4, 40))
    ks, b, seed = [4, 12], 60, 17
    result = hill_stability_bootstrap(x, ks, replicates=b, random_state=seed)
    rng = np.random.default_rng(seed)
    values = []
    for _ in range(b):
        ordered = np.sort(rng.choice(x, len(x)))[::-1]
        values.append([1 / np.mean(np.log(ordered[:k]/ordered[k])) for k in ks])
    expected = np.quantile(values, [.025, .975], axis=0)
    assert_allclose(result['lower'], expected[0])
    assert_allclose(result['upper'], expected[1])
    assert_array_equal(result['finite_replicates'], [b, b])
    assert_allclose(result['alpha'], [hill_alpha_estimator(x, k) for k in ks])


def test_bootstrap_reports_tied_infinite_estimates():
    with pytest.warns(RuntimeWarning, match='conditional on a finite estimate') as caught:
        result = hill_stability_bootstrap([1, 2, 2, 2], [1], replicates=100, random_state=3)
    assert len(caught) == 1
    assert caught[0].filename == __file__
    assert 0 < result['finite_replicates'][0] < 100
    assert np.isinf(result['alpha'][0])
    assert_allclose(result['lower'], [1/np.log(2)])
    assert_allclose(result['upper'], [1/np.log(2)])
    with pytest.raises(ValueError, match='no finite'):
        hill_stability_bootstrap([2, 2, 2], [1], replicates=10, random_state=1)


@pytest.mark.parametrize('seed, finite_count', [(7, 20), (12, 19), (0, 18)])
def test_bootstrap_warns_only_above_five_percent_excluded(seed, finite_count):
    # These seeded samples exclude 0%, 5%, and 10% at k=2, and none at k=4.
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        result = hill_stability_bootstrap(
            [1, 2, 4, 8, 16], [4, 2], replicates=20, random_state=seed,
        )
    assert_array_equal(result['finite_replicates'], [20, finite_count])
    if finite_count == 18:
        assert len(caught) == 1
        assert caught[0].category is RuntimeWarning
        message = str(caught[0].message)
        assert 'More than 5%' in message
        assert 'k=[2]' in message
        assert 'excluded [2] of 20' in message
        assert 'conditional on a finite estimate' in message
    else:
        assert not caught


@pytest.mark.parametrize('kwargs', [dict(replicates=1), dict(replicates=True),
    dict(confidence=0), dict(confidence=1), dict(confidence=np.nan)])
def test_bootstrap_invalid_controls(kwargs):
    with pytest.raises(ValueError):
        hill_stability_bootstrap([1, 2, 4], [1], **kwargs)


def test_recorded_summary_matches_generated_report():
    # Aggregate outputs ship without the underlying observations.
    import runpy
    root = Path(__file__).resolve().parents[1]
    demo = runpy.run_path(str(root/'demos/incerto/layoffs_tails.py'))
    outputs = root/'assets/incerto/outputs'
    result = json.loads((outputs/'layoffs-tails.json').read_text())
    assert demo['summary'](result) == (outputs/'layoffs-tails.txt').read_text()
    for sample in result['samples'].values():
        assert all(n == result['replicates'] for n in sample['hill']['finite_replicates'])


def test_download_script_uses_cli_and_retains_archive(tmp_path, monkeypatch):
    import runpy
    import shutil
    import subprocess
    import sys
    import zipfile
    root = Path(__file__).resolve().parents[1]
    script = runpy.run_path(str(root/'scripts/download_layoffs.py'))
    destination = tmp_path/'local/layoffs.csv'
    monkeypatch.setattr(sys, 'argv', ['download_layoffs.py', '--destination',
                                    str(destination), '--version', '3'])
    monkeypatch.setattr(shutil, 'which', lambda name: '/synthetic/kaggle')
    calls = []

    def fake_run(command, *, check):
        calls.append(command)
        assert check and command[:4] == ['kaggle', 'datasets', 'download', 'swaptr/layoffs-2022/3']
        archive = Path(command[-1])/'layoffs-2022.zip'
        with zipfile.ZipFile(archive, 'w') as stream:
            stream.writestr('nested/layoffs.csv', 'company,date,n,frac\nA,2020-03-11,10,0.2\n')

    monkeypatch.setattr(subprocess, 'run', fake_run)
    script['main']()
    assert load_layoffs(destination).count.tolist() == [10]
    assert list(destination.parent.glob('download-*/*.zip'))
    with pytest.raises(SystemExit):
        script['main']()
    assert len(calls) == 1
    assert destination.exists()
