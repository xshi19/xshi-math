"""Tests for local dataset loaders and cleaning helpers."""

import json
import runpy
import sys
from datetime import datetime
from io import BytesIO
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

from xmath.incerto.datasets import (
    DatasetNotAvailable,
    load_amazon_bookrank,
    load_nyc_dog_name_frequencies,
    load_sp500_prices,
    write_nyc_dog_name_frequency_snapshot,
    write_sp500_fred_cache,
    write_sp500_yahoo_cache,
    write_sp500_cache_from_csv,
)


@pytest.fixture(params=["writer", "loader", "cli"])
def fetch_sp500(request, tmp_path, monkeypatch):
    """Exercise each fetch entry point with synthetic CSV and no network."""
    from xmath.incerto import datasets

    destination = tmp_path / "cache/sp500_daily.csv"

    def fetch(text):
        monkeypatch.setattr(
            datasets, "urlopen", lambda *args, **kwargs: BytesIO(text.encode("utf-8"))
        )
        if request.param == "writer":
            write_sp500_fred_cache(destination)
        elif request.param == "loader":
            load_sp500_prices(data_dir=tmp_path, fetch=True)
        else:
            script = Path(__file__).resolve().parents[1] / "scripts/fetch_incerto_data.py"
            monkeypatch.setattr(sys, "argv", [str(script), "sp500", "--data-dir", str(tmp_path)])
            runpy.run_path(str(script), run_name="__main__")
        return load_sp500_prices(data_dir=tmp_path)

    return fetch, destination


def test_fred_fetch_skips_missing_and_nonfinite_closes(fetch_sp500):
    fetch, destination = fetch_sp500
    placeholders = [".", "", "  ", " . ", "NaN", "nan", "inf", "-inf", "Infinity", "1e999"]
    gaps = "".join(f"2026-01-{day:02d},{close}\n" for day, close in enumerate(placeholders, 3))
    series = fetch(
        "observation_date,SP500\n2026-01-02,100\n" + gaps + "2026-01-15,110\n"
    )
    assert destination.read_text() == "date,close\n2026-01-02,100\n2026-01-15,110\n"
    np.testing.assert_array_equal(series.close, [100, 110])
    np.testing.assert_array_equal(series.date, np.array(["2026-01-02", "2026-01-15"], dtype="datetime64[D]"))
    np.testing.assert_allclose(series.log_returns()[1], [np.log(1.1)])


@pytest.mark.parametrize("bad_row, line", [
    ("2026-01-03,broken\n", 3),
    ("2026-02-30,101\n", 3),
    (",101\n", 3),
    ("2026-01-03\n", 3),
    ("2026-01-03,101,extra\n", 3),
    ('2026-01-03,"unterminated\n', 4),
])
def test_fred_fetch_rejects_malformed_rows_without_writing_cache(fetch_sp500, bad_row, line):
    fetch, destination = fetch_sp500
    with pytest.raises(DatasetNotAvailable, match=rf"FRED S&P 500.*line {line}"):
        fetch("observation_date,SP500\n2026-01-02,100\n" + bad_row + "2026-01-05,110\n")
    assert not destination.exists()


@pytest.mark.parametrize("payload, message", [
    ("date,close\n2026-01-02,100\n2026-01-05,110\n", "columns"),
    ("observation_date,SP500\n2026-01-02,.\n2026-01-05,NaN\n", "enough prices"),
    ("observation_date,SP500\n2026-01-02,100\n2026-01-05,\n", "enough prices"),
])
def test_fred_fetch_rejects_unusable_payload(fetch_sp500, payload, message):
    fetch, destination = fetch_sp500
    with pytest.raises(DatasetNotAvailable, match=message):
        fetch(payload)
    assert not destination.exists()


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


def yahoo_frame(rows, *, multi=False):
    """Small pandas protocol fake: no optional dependencies in base tests."""
    series = SimpleNamespace(ndim=1, items=lambda: [
        (datetime.strptime(day, "%Y-%m-%d"), value) for day, value in rows])
    class Columns:
        def __getitem__(self, key):
            assert key == (slice(None), 0)
            return series
    return {"Close": SimpleNamespace(ndim=2, shape=(len(rows), 1), iloc=Columns())
            if multi else series,
            "Adj Close": None}  # Never selected.


@pytest.mark.parametrize("multi", [False, True])
@pytest.mark.parametrize("entry", ["writer", "loader", "cli"])
def test_yahoo_fetch_cleaning_cutoff_and_entry_points(tmp_path, monkeypatch, multi, entry):
    calls = []
    rows = [("2026-01-03", 103), ("2026-01-02", 100), ("2026-01-03", 104),
            ("2026-01-04", np.nan), ("2026-01-05", 0), ("2026-01-06", -1),
            ("2026-01-07", np.inf), ("2026-01-08", 108), ("2026-01-03", np.nan)]
    def download(*args, **kwargs):
        calls.append((args, kwargs))
        return yahoo_frame(rows, multi=multi)
    monkeypatch.setitem(sys.modules, "yfinance", SimpleNamespace(download=download))
    destination = tmp_path / "cache/sp500_daily.csv"
    if entry == "writer":
        write_sp500_yahoo_cache(destination, end_date="2026-01-07")
    elif entry == "loader":
        load_sp500_prices(data_dir=tmp_path, fetch=True, provider="yahoo", end_date="2026-01-07")
    else:
        script = Path(__file__).resolve().parents[1] / "scripts/fetch_incerto_data.py"
        monkeypatch.setattr(sys, "argv", [str(script), "sp500", "--provider", "yahoo",
                                          "--end-date", "2026-01-07", "--data-dir", str(tmp_path)])
        runpy.run_path(str(script), run_name="__main__")
    assert calls == [(("^GSPC",), dict(period="max", interval="1d", auto_adjust=False, progress=False))]
    assert destination.read_text() == "date,close\n2026-01-02,100.0\n2026-01-03,104.0\n"
    # A cached read, including a cutoff, must not import the optional dependency.
    monkeypatch.setitem(sys.modules, "yfinance", None)
    assert load_sp500_prices(data_dir=tmp_path, provider="yahoo", end_date="2026-01-03").close.tolist() == [100, 104]


def test_yahoo_optional_import_and_failed_fetch_preserve_cache(tmp_path, monkeypatch):
    destination = tmp_path / "prices.csv"
    destination.write_text("existing cache")
    monkeypatch.setitem(sys.modules, "yfinance", None)
    with pytest.raises(DatasetNotAvailable, match="uv sync --extra yahoo"):
        write_sp500_yahoo_cache(destination)
    def failed(*args, **kwargs):
        raise OSError("mock network unavailable")
    monkeypatch.setitem(sys.modules, "yfinance", SimpleNamespace(download=failed))
    with pytest.raises(DatasetNotAvailable, match="Yahoo.*fetch failed"):
        write_sp500_yahoo_cache(destination)
    assert destination.read_text() == "existing cache"


@pytest.mark.parametrize("frame", [None, {}, yahoo_frame([]),
    yahoo_frame([("2026-01-02", 100), ("2026-01-02", 101)]),
    {"Close": SimpleNamespace(ndim=2, shape=(2, 2))}])
def test_yahoo_rejects_unusable_payload(tmp_path, monkeypatch, frame):
    monkeypatch.setitem(sys.modules, "yfinance", SimpleNamespace(download=lambda *a, **kw: frame))
    destination = tmp_path / "prices.csv"
    with pytest.raises(DatasetNotAvailable):
        write_sp500_yahoo_cache(destination)
    assert not destination.exists()


@pytest.mark.parametrize("provider", ["fred", "csv"])
def test_other_sp500_writers_clean_sort_dedupe_and_cutoff(tmp_path, monkeypatch, provider):
    from xmath.incerto import datasets
    source = tmp_path / "source.csv"
    rows = "2026-01-03,102\n2026-01-02,100\n2026-01-03,103\n2026-01-04,0\n2026-01-05,-1\n2026-01-06,106\n"
    destination = tmp_path / "cache/sp500_daily.csv"
    if provider == "fred":
        monkeypatch.setattr(datasets, "urlopen", lambda *a, **kw:
                            BytesIO(("observation_date,SP500\n" + rows).encode()))
        write_sp500_fred_cache(destination, end_date="2026-01-05")
    else:
        source.write_text("date,close\n" + rows)
        script = Path(__file__).resolve().parents[1] / "scripts/fetch_incerto_data.py"
        # --source takes priority even when Yahoo is unavailable.
        monkeypatch.setitem(sys.modules, "yfinance", None)
        monkeypatch.setattr(sys, "argv", [str(script), "sp500", "--source", str(source),
            "--provider", "yahoo", "--end-date", "2026-01-05", "--data-dir", str(tmp_path)])
        runpy.run_path(str(script), run_name="__main__")
    assert destination.read_text() == "date,close\n2026-01-02,100\n2026-01-03,103\n"


def test_csv_uses_close_not_adjusted_and_skips_bad_values(tmp_path):
    source, destination = tmp_path / "source.csv", tmp_path / "cache/sp500_daily.csv"
    source.write_text("Date,Close,Adj Close\n2026-01-01,100,50\n2026-01-02,NaN,51\n"
                      "2026-01-03,,52\n2026-01-04,.,53\n2026-01-05,inf,54\n2026-01-06,110,55\n")
    write_sp500_cache_from_csv(source, destination)
    assert load_sp500_prices(data_dir=tmp_path).close.tolist() == [100, 110]
    original = destination.read_bytes()
    with pytest.raises(DatasetNotAvailable, match="need two"):
        write_sp500_cache_from_csv(source, destination, end_date="2026-01-01")
    assert destination.read_bytes() == original


def test_sp500_read_cutoff_is_inclusive_and_does_not_rewrite(tmp_path):
    path = tmp_path / "cache/sp500_daily.csv"
    path.parent.mkdir()
    text = "date,close\n2026-01-01,100\n2026-01-02,101\n2026-01-03,102\n"
    path.write_text(text)
    assert len(load_sp500_prices(data_dir=tmp_path, end_date="2026-01-02").close) == 2
    with pytest.raises(DatasetNotAvailable, match="need two"):
        load_sp500_prices(data_dir=tmp_path, end_date="2026-01-01")
    assert path.read_text() == text


@pytest.mark.parametrize("cutoff", ["2026-02-30", "2026-1-2", "not-a-date"])
def test_invalid_cutoff_precedes_any_fetch(tmp_path, monkeypatch, cutoff):
    monkeypatch.setitem(sys.modules, "yfinance", None)
    with pytest.raises(ValueError):
        write_sp500_yahoo_cache(tmp_path / "prices.csv", end_date=cutoff)
