"""Tests for local dataset loaders and cleaning helpers."""

import json
from pathlib import Path

import numpy as np
import pytest

from xmath.incerto.datasets import (
    DatasetNotAvailable,
    load_amazon_bookrank,
    load_nyc_dog_name_frequencies,
    load_sp500_prices,
    write_nyc_dog_name_frequency_snapshot,
    write_sp500_fred_cache,
)


def test_sp500_loader_reads_cache_and_computes_losses(tmp_path: Path) -> None:
    cache = tmp_path / "cache"
    cache.mkdir()
    (cache / "sp500_daily.csv").write_text(
        "date,close\n2026-01-02,100\n2026-01-05,110\n2026-01-06,99\n",
        encoding="utf-8",
    )

    series = load_sp500_prices(data_dir=tmp_path)
    dates, losses = series.negative_log_returns()

    assert series.name == "S&P 500"
    np.testing.assert_array_equal(dates, np.array(["2026-01-06"], dtype="datetime64[D]"))
    np.testing.assert_allclose(losses, [-np.log(99.0 / 110.0)])


def test_sp500_loader_raises_when_cache_is_missing(tmp_path: Path) -> None:
    with pytest.raises(DatasetNotAvailable):
        load_sp500_prices(data_dir=tmp_path)


def test_write_sp500_fred_cache_from_file_url(tmp_path: Path) -> None:
    source = tmp_path / "fred.csv"
    source.write_text(
        "observation_date,SP500\n2026-01-02,100\n2026-01-03,\n2026-01-05,101\n",
        encoding="utf-8",
    )

    destination = tmp_path / "cache" / "sp500_daily.csv"
    write_sp500_fred_cache(destination, url=source.as_uri())

    assert destination.read_text(encoding="utf-8") == (
        "date,close\n2026-01-02,100\n2026-01-05,101\n"
    )


def test_amazon_bookrank_loader_reads_snapshot(tmp_path: Path) -> None:
    snapshots = tmp_path / "snapshots"
    snapshots.mkdir()
    (snapshots / "amazon_bookrank_2001.csv").write_text(
        (
            "date,isbn,title,weekly_sales,weekly_average_rank\n"
            "2001-04-21,0596000405,Java Servlet Programming,227,238\n"
        ),
        encoding="utf-8",
    )

    data = load_amazon_bookrank(data_dir=tmp_path)

    np.testing.assert_array_equal(
        data.date, np.array(["2001-04-21"], dtype="datetime64[D]")
    )
    assert data.isbn[0] == "0596000405"
    assert data.title[0] == "Java Servlet Programming"
    np.testing.assert_allclose(data.weekly_sales, [227.0])
    np.testing.assert_allclose(data.weekly_average_rank, [238.0])


def test_nyc_dog_name_frequency_loader_normalizes_lookup(tmp_path: Path) -> None:
    snapshots = tmp_path / "snapshots"
    snapshots.mkdir()
    (snapshots / "nyc_dog_name_frequencies.csv").write_text(
        "name,frequency\nBELLA,12\nSAFARI,3\n",
        encoding="utf-8",
    )

    data = load_nyc_dog_name_frequencies(data_dir=tmp_path)

    np.testing.assert_array_equal(data.name, ["BELLA", "SAFARI"])
    np.testing.assert_array_equal(data.frequency, [12, 3])
    assert data.frequency_for(" safari ") == 3
    assert data.frequency_for("missing") == 0
    with pytest.raises(ValueError):
        data.frequency_for("   ")


def test_write_nyc_dog_name_frequency_snapshot_from_file_url(tmp_path: Path) -> None:
    source = tmp_path / "dog_names.json"
    source.write_text(
        json.dumps(
            [
                {"name": "Safari", "frequency": "1"},
                {"name": "SAFARI", "frequency": "2"},
                {"name": "Bella", "frequency": "12"},
                {"name": "UNKNOWN", "frequency": "20"},
            ]
        ),
        encoding="utf-8",
    )
    destination = tmp_path / "snapshots" / "nyc_dog_name_frequencies.csv"

    write_nyc_dog_name_frequency_snapshot(destination, url=source.as_uri())
    data = load_nyc_dog_name_frequencies(data_dir=tmp_path)

    np.testing.assert_array_equal(data.name, ["BELLA", "SAFARI"])
    np.testing.assert_array_equal(data.frequency, [12, 3])


def test_http_download_is_mocked_and_failure_is_actionable(tmp_path, monkeypatch):
    from io import BytesIO
    from urllib.error import URLError
    from xmath.incerto import datasets
    calls = []

    def response(request, timeout):
        calls.append((request.full_url, timeout))
        return BytesIO(b"observation_date,SP500\n2026-01-01,100\n2026-01-02,99\n")

    monkeypatch.setattr(datasets, "urlopen", response)
    series = load_sp500_prices(data_dir=tmp_path, fetch=True)
    assert calls == [(datasets.FRED_SP500_CSV_URL, 120)]
    assert series.close.tolist() == [100, 99]
    # A local read must never make a request.
    def offline(*args, **kwargs):
        raise URLError("offline test")
    monkeypatch.setattr(datasets, "urlopen", offline)
    assert load_sp500_prices(data_dir=tmp_path).close.tolist() == [100, 99]
    with pytest.raises(DatasetNotAvailable, match="fetch failed"):
        load_sp500_prices(data_dir=tmp_path / "empty", fetch=True)


def test_data_root_precedence_and_wheel_fallback(tmp_path, monkeypatch):
    from xmath.incerto import datasets
    monkeypatch.setenv("INCERTO_DATA_DIR", str(tmp_path / "external"))
    assert datasets.data_root() == tmp_path / "external"
    assert datasets.data_root(tmp_path / "explicit") == tmp_path / "explicit"
    monkeypatch.delenv("INCERTO_DATA_DIR")
    monkeypatch.setattr(datasets, "__file__", str(tmp_path / "lib/python/site-packages/xmath/incerto/datasets.py"))
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path / "user-cache"))
    assert datasets.data_root() == tmp_path / "user-cache/xshi-math/incerto"
