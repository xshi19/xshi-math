"""Synthetic fixtures only: no real layoffs data or downloads required."""
import csv
import json
from pathlib import Path
import runpy
import sys
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


def assert_summary_only(result):
    # An explicit allowlist prevents accidentally publishing dense curves,
    # thresholds, spacings, resamples, or event-level data through another key.
    assert set(result) == {
        'source', 'retrieved', 'input_sha256', 'input_rows', 'events',
        'first_date', 'last_date', 'missing_counts', 'zero_counts',
        'missing_fractions', 'full_workforce_cuts', 'zero_fractions',
        'replicates', 'confidence', 'min_tail', 'samples',
    }
    assert all(not isinstance(value, (list, dict)) for key, value in result.items() if key != 'samples')
    assert set(result['samples']) == {'counts', 'pct_logloss_reported'}
    for sample in result['samples'].values():
        assert set(sample) == {'n', 'seed', 'csn', 'hill_reported'}
        assert set(sample['csn']) == {
            'xmin', 'alpha', 'n_tail', 'ks', 'standard_error', 'gof_p', 'gof_hits',
        }
        assert all(isinstance(value, (int, float)) for value in sample['csn'].values())
        points = sample['hill_reported']
        assert [point['k'] for point in points] == [round(f*sample['n']) for f in (.1, .2)]
        for point in points:
            assert set(point) == {'k', 'alpha', 'lower', 'upper', 'finite_replicates'}
            assert all(isinstance(value, (int, float)) for value in point.values())
            assert 0 < point['finite_replicates'] <= result['replicates']


def test_recorded_summary_matches_generated_report():
    # Aggregate outputs ship without the underlying observations.
    root = Path(__file__).resolve().parents[1]
    demo = runpy.run_path(str(root/'demos/incerto/layoffs_tails.py'))
    outputs = root/'assets/incerto/outputs'
    result = json.loads((outputs/'layoffs-tails.json').read_text())
    assert_summary_only(result)
    assert demo['summary'](result) == (outputs/'layoffs-tails.txt').read_text()
    for sample in result['samples'].values():
        assert all(p['finite_replicates'] == result['replicates'] for p in sample['hill_reported'])


def test_demo_writes_only_summaries_and_recorded_mode_does_not_render(tmp_path, monkeypatch, capsys):
    root = Path(__file__).resolve().parents[1]
    demo = runpy.run_path(str(root/'demos/incerto/layoffs_tails.py'))
    source = tmp_path/'synthetic.csv'
    source.write_text('company,date,n,frac\n' + ''.join(
        f'Synthetic {i},2020-03-11,{10+i*i},{(i % 80 + 1)/100}\n' for i in range(180))
        + 'Zero,2020-03-11,0,0\nMissing,2020-03-11,,\nFull,2020-03-11,,1\n')
    figures, outputs = tmp_path/'figures', tmp_path/'outputs'
    monkeypatch.setattr(sys, 'argv', ['layoffs_tails.py', '--data', str(source),
                                    '--replicates', '10', '--figure-dir', str(figures),
                                    '--output-dir', str(outputs)])
    demo['main']()
    report_path = outputs/'layoffs-tails.json'
    result = json.loads(report_path.read_text())
    assert_summary_only(result)
    assert result['zero_counts'] == 1 and result['missing_counts'] == 2
    assert result['zero_fractions'] == result['missing_fractions'] == result['full_workforce_cuts'] == 1
    assert result['samples']['counts']['n'] == result['samples']['pct_logloss_reported']['n'] == 180
    data = load_layoffs(source)
    samples = {'counts': data.count[data.count > 0],
               'pct_logloss_reported': workforce_log_loss(data.fraction[(data.fraction > 0)
                                                                       & (data.fraction < 1)])}
    for name, values in samples.items():
        sample = result['samples'][name]
        points = sample['hill_reported']
        # Keeping only selected k must preserve the original bootstrap draws.
        expected = hill_stability_bootstrap(values, [p['k'] for p in points],
                                            replicates=10, random_state=sample['seed'])
        for key in ('alpha', 'lower', 'upper', 'finite_replicates'):
            assert_allclose([p[key] for p in points], expected[key], rtol=0, atol=0)
    assert (outputs/'layoffs-tails.txt').read_text() == demo['summary'](result)
    assert {p.name for p in figures.iterdir()} == {'layoffs-counts-hill.svg', 'layoffs-logloss-hill.svg'}
    before = {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in figures.iterdir()}
    capsys.readouterr()

    def unexpected(*args, **kwargs):
        pytest.fail('--recorded must neither calculate from data nor render figures')

    monkeypatch.setitem(demo['main'].__globals__, 'calculate', unexpected)
    monkeypatch.setitem(demo['main'].__globals__, 'render', unexpected)
    unused_outputs = tmp_path/'unused-outputs'
    monkeypatch.setattr(sys, 'argv', ['layoffs_tails.py', '--recorded', str(report_path),
                                    '--figure-dir', str(figures), '--output-dir', str(unused_outputs)])
    demo['main']()
    assert capsys.readouterr().out.strip() == demo['summary'](result).strip()
    assert not unused_outputs.exists()
    assert before == {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in figures.iterdir()}


def test_output_regenerator_rebuilds_layoffs_from_summary_without_csv(tmp_path, monkeypatch, capsys):
    root = Path(__file__).resolve().parents[1]
    script = runpy.run_path(str(root/'scripts/regenerate_incerto_outputs.py'))
    for relative in ('content/incerto-layoffs-tails.md', 'content/incerto-api-reference.md',
                     'content/incerto/index.md',
                     'tests/test_incerto_page_snippets.py', 'demos/incerto/layoffs_tails.py',
                     'assets/incerto/outputs/layoffs-tails.json'):
        destination = tmp_path/relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes((root/relative).read_bytes())
    page = tmp_path/'content/incerto-layoffs-tails.md'
    original = page.read_text()
    page.write_text(original.replace('Hill k=301: 1.04', 'Hill k=301: 9.99'))
    monkeypatch.setenv('INCERTO_LAYOFFS_PATH', str(tmp_path/'absent.csv'))
    monkeypatch.setitem(script['main'].__globals__, 'ROOT', tmp_path)
    monkeypatch.setattr(sys, 'argv', ['regenerate_incerto_outputs.py', '--pages', 'incerto-layoffs-tails'])
    script['main']()
    assert page.read_text() == original
    output = capsys.readouterr().out
    assert 'Rebuilt from summary JSON' in output
    assert '1 executed snippet outputs, 1 summary-derived outputs' in output
    assert not (tmp_path/'assets/incerto/figures').exists()


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
