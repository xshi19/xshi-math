"""Dataset loaders and refresh helpers for Incerto examples.

Committed snapshots live under ``data/incerto/snapshots`` when the dataset is small and
redistributable.  Larger, private, or license-restricted data should live in a
local or shared cache selected by ``INCERTO_DATA_DIR``.
"""

from __future__ import annotations

import csv
import io
import json
import os
import zipfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import numpy as np
from numpy.typing import NDArray
from urllib.error import URLError

FRED_SP500_CSV_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500"
KAGGLE_AMAZON_BOOKRANK_METADATA_URL = (
    "https://www.kaggle.com/api/v1/datasets/view/"
    "yuanmozhu/amazon-book-sales-vs-rank"
)
KAGGLE_AMAZON_BOOKRANK_DOWNLOAD_URL = (
    "https://www.kaggle.com/api/v1/datasets/download/"
    "yuanmozhu/amazon-book-sales-vs-rank"
)
NYC_DOG_LICENSE_DATASET_URL = (
    "https://data.cityofnewyork.us/Health/NYC-Dog-Licensing-Dataset/nu7n-tubp"
)
NYC_DOG_NAME_FREQUENCY_API_URL = (
    "https://data.cityofnewyork.us/resource/nu7n-tubp.json?"
    + urlencode(
        {
            "$select": "upper(trim(animalname)) as name,count(*) as frequency",
            "$where": (
                "trim(animalname) != '' and upper(trim(animalname)) "
                "not in ('UNKNOWN','NAME NOT PROVIDED')"
            ),
            "$group": "upper(trim(animalname))",
            "$order": "frequency desc,name",
            "$limit": "50000",
        }
    )
)


class DatasetNotAvailable(FileNotFoundError):
    """Raised when a dataset snapshot/cache is missing and fetching is disabled."""


@dataclass(frozen=True)
class PriceSeries:
    """Daily close-price series used by empirical examples."""

    name: str
    date: NDArray[np.datetime64]
    close: NDArray[np.float64]
    source: str

    def log_returns(self) -> tuple[NDArray[np.datetime64], NDArray[np.float64]]:
        """Return close-to-close log returns and their ending dates."""

        if self.close.size < 2:
            raise ValueError("at least two close prices are required")
        return self.date[1:], np.diff(np.log(self.close))

    def negative_log_returns(self) -> tuple[NDArray[np.datetime64], NDArray[np.float64]]:
        """Return positive losses, defined as negative close-to-close log returns."""

        dates, returns = self.log_returns()
        mask = returns < 0.0
        return dates[mask], -returns[mask]


@dataclass(frozen=True)
class BookRankData:
    """Amazon book sales-rank observations."""

    date: NDArray[np.datetime64]
    isbn: NDArray[np.str_]
    title: NDArray[np.str_]
    weekly_sales: NDArray[np.float64]
    weekly_average_rank: NDArray[np.float64]
    source: str


@dataclass(frozen=True)
class DogNameFrequencyData:
    """Normalized NYC dog-name frequencies from license-period records."""

    name: NDArray[np.str_]
    frequency: NDArray[np.int64]
    source: str

    def frequency_for(self, name: str) -> int:
        """Return the license-period frequency for a case-insensitive name.

        Parameters
        ----------
        name
            Dog name to normalize by trimming whitespace and converting to
            uppercase.

        Returns
        -------
        int
            Frequency in the snapshot, or zero when the name is absent.

        Raises
        ------
        ValueError
            If ``name`` is blank after trimming whitespace.
        """

        normalized = name.strip().upper()
        if not normalized:
            raise ValueError("name must contain at least one non-whitespace character")
        matches = self.frequency[self.name == normalized]
        return int(matches[0]) if matches.size else 0


def data_root(data_dir: str | os.PathLike[str] | None = None) -> Path:
    """Return the configured data directory.

    ``data_dir`` wins first, then the ``INCERTO_DATA_DIR`` environment
    variable, then ``data/incerto`` in an editable checkout or a user cache
    in an ordinary wheel installation.
    """

    if data_dir is not None:
        return Path(data_dir).expanduser().resolve()
    env_dir = os.environ.get("INCERTO_DATA_DIR")
    if env_dir:
        return Path(env_dir).expanduser().resolve()
    # An editable checkout can locate its redistributable snapshots. A wheel
    # uses a user cache instead of attempting to write inside site-packages.
    checkout = Path(__file__).resolve().parents[3]
    if (checkout / "pyproject.toml").is_file() and (checkout / "data/incerto").is_dir():
        return checkout / "data/incerto"
    return Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "xshi-math/incerto"


def snapshot_path(filename: str, data_dir: str | os.PathLike[str] | None = None) -> Path:
    """Return the path to a committed or externally synchronized snapshot."""

    return data_root(data_dir) / "snapshots" / filename


def cache_path(filename: str, data_dir: str | os.PathLike[str] | None = None) -> Path:
    """Return the path to an untracked local cache file."""

    return data_root(data_dir) / "cache" / filename


def load_sp500_prices(
    *,
    data_dir: str | os.PathLike[str] | None = None,
    fetch: bool = False,
) -> PriceSeries:
    """Load S&P 500 daily closes from the local cache, optionally fetching FRED.

    The S&P 500 series on FRED is copyright-restricted by S&P Dow Jones
    Indices, so the project keeps this file out of git and fetches it into
    ``data/incerto/cache`` or the configured ``INCERTO_DATA_DIR`` instead.
    """

    path = cache_path("sp500_daily.csv", data_dir)
    if not path.exists():
        if not fetch:
            raise DatasetNotAvailable(
                f"{path} is missing; run `python scripts/fetch_incerto_data.py sp500` "
                "or call load_sp500_prices(fetch=True)"
            )
        try:
            write_sp500_fred_cache(path)
        except (URLError, TimeoutError) as exc:
            raise DatasetNotAvailable(
                f"{path} is missing and automatic FRED fetch failed; "
                "run `python scripts/fetch_incerto_data.py sp500` when network access "
                "is available or provide a local source with "
                "`python scripts/fetch_incerto_data.py sp500 --source path/to/local.csv`"
            ) from exc

    return _read_sp500_price_csv(path)


def load_amazon_bookrank(
    *,
    data_dir: str | os.PathLike[str] | None = None,
) -> BookRankData:
    """Load the CC0 Amazon book sales-rank snapshot."""

    path = snapshot_path("amazon_bookrank_2001.csv", data_dir)
    if not path.exists():
        raise DatasetNotAvailable(
            f"{path} is missing; run `python scripts/fetch_incerto_data.py amazon-bookrank`"
        )
    return _read_amazon_bookrank_csv(path)


def load_nyc_dog_name_frequencies(
    *,
    data_dir: str | os.PathLike[str] | None = None,
) -> DogNameFrequencyData:
    """Load the NYC Open Data dog-name frequency snapshot."""

    path = snapshot_path("nyc_dog_name_frequencies.csv", data_dir)
    if not path.exists():
        raise DatasetNotAvailable(
            f"{path} is missing; run `python scripts/fetch_incerto_data.py nyc-dog-names`"
        )
    return _read_nyc_dog_name_frequency_csv(path)


def write_sp500_fred_cache(
    destination: str | os.PathLike[str],
    *,
    url: str = FRED_SP500_CSV_URL,
) -> Path:
    """Fetch and clean the public FRED S&P 500 CSV into an untracked cache."""

    text = _download_text(url)
    rows = _clean_fred_sp500_rows(text)
    destination_path = Path(destination)
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    with destination_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "close"])
        writer.writerows(rows)
    return destination_path


def write_sp500_cache_from_csv(
    source: str | os.PathLike[str],
    destination: str | os.PathLike[str],
) -> Path:
    """Clean a local S&P 500-like CSV into the standard untracked cache."""

    rows = _clean_sp500_price_rows(Path(source))
    destination_path = Path(destination)
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    with destination_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "close"])
        writer.writerows(rows)
    return destination_path


def write_amazon_bookrank_snapshot(
    destination: str | os.PathLike[str],
    *,
    url: str = KAGGLE_AMAZON_BOOKRANK_DOWNLOAD_URL,
) -> Path:
    """Fetch and clean the CC0 Kaggle Amazon bookrank dataset."""

    payload = _download_bytes(url)
    rows = _extract_amazon_bookrank_rows(payload)
    destination_path = Path(destination)
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    with destination_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["date", "isbn", "title", "weekly_sales", "weekly_average_rank"]
        )
        writer.writerows(rows)
    return destination_path


def write_nyc_dog_name_frequency_snapshot(
    destination: str | os.PathLike[str],
    *,
    url: str = NYC_DOG_NAME_FREQUENCY_API_URL,
) -> Path:
    """Fetch the server-aggregated NYC dog-name frequencies into a snapshot."""

    rows = _extract_nyc_dog_name_frequency_rows(_download_text(url))
    destination_path = Path(destination)
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    with destination_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "frequency"])
        writer.writerows(rows)
    return destination_path


def _read_sp500_price_csv(path: Path) -> PriceSeries:
    dates: list[str] = []
    closes: list[float] = []
    with path.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            close = row.get("close") or row.get("SP500") or row.get("Close")
            date = row.get("date") or row.get("observation_date") or row.get("Date")
            if not date or not close:
                continue
            dates.append(date)
            closes.append(float(close))

    if len(closes) < 2:
        raise ValueError(f"{path} must contain at least two valid close prices")

    return PriceSeries(
        name="S&P 500",
        date=np.array(dates, dtype="datetime64[D]"),
        close=np.array(closes, dtype=float),
        source=str(path),
    )


def _read_amazon_bookrank_csv(path: Path) -> BookRankData:
    dates: list[str] = []
    isbn: list[str] = []
    title: list[str] = []
    sales: list[float] = []
    ranks: list[float] = []
    with path.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            dates.append(row["date"])
            isbn.append(row["isbn"])
            title.append(row["title"])
            sales.append(float(row["weekly_sales"]))
            ranks.append(float(row["weekly_average_rank"]))

    if not sales:
        raise ValueError(f"{path} must contain at least one sales observation")

    return BookRankData(
        date=np.array(dates, dtype="datetime64[D]"),
        isbn=np.array(isbn, dtype=str),
        title=np.array(title, dtype=str),
        weekly_sales=np.array(sales, dtype=float),
        weekly_average_rank=np.array(ranks, dtype=float),
        source=str(path),
    )


def _read_nyc_dog_name_frequency_csv(path: Path) -> DogNameFrequencyData:
    names: list[str] = []
    frequencies: list[int] = []
    with path.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            name = row["name"].strip().upper()
            frequency = int(row["frequency"])
            if not name or frequency <= 0:
                raise ValueError(f"{path} contains an invalid name-frequency row")
            names.append(name)
            frequencies.append(frequency)

    if not names:
        raise ValueError(f"{path} must contain at least one name frequency")

    return DogNameFrequencyData(
        name=np.array(names, dtype=str),
        frequency=np.array(frequencies, dtype=np.int64),
        source=str(path),
    )


def _clean_fred_sp500_rows(text: str) -> list[tuple[str, str]]:
    reader = csv.DictReader(io.StringIO(text))
    rows: list[tuple[str, str]] = []
    for row in reader:
        date = row.get("observation_date", "").strip()
        close = row.get("SP500", "").strip()
        if not date or not close:
            continue
        float(close)
        datetime.strptime(date, "%Y-%m-%d")
        rows.append((date, close))
    if len(rows) < 2:
        raise ValueError("FRED S&P 500 payload did not contain enough prices")
    return rows


def _clean_sp500_price_rows(path: Path) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = (
                row.get("date")
                or row.get("Date")
                or row.get("observation_date")
                or ""
            ).strip()
            close = (
                row.get("close")
                or row.get("Adj Close")
                or row.get("Close")
                or row.get("SP500")
                or ""
            ).strip()
            if not date or not close:
                continue
            float(close)
            datetime.strptime(date, "%Y-%m-%d")
            rows.append((date, close))

    if len(rows) < 2:
        raise ValueError(f"{path} did not contain enough valid prices")
    return rows


def _extract_amazon_bookrank_rows(payload: bytes) -> list[tuple[str, str, str, int, int]]:
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        candidates = [
            name
            for name in archive.namelist()
            if name.lower().endswith(".csv") and "bookrank" in name.lower()
        ]
        if not candidates:
            raise ValueError("Kaggle archive did not contain the bookrank CSV")
        with archive.open(candidates[0]) as raw:
            text = io.TextIOWrapper(raw, encoding="utf-8-sig", newline="")
            reader = csv.DictReader(text)
            rows = []
            last_date = ""
            for row in reader:
                raw_date = row.get("DATE", "").strip()
                if raw_date:
                    last_date = raw_date
                elif not last_date:
                    continue
                row["DATE"] = last_date
                rows.append(_clean_amazon_bookrank_row(row))

    if not rows:
        raise ValueError("Amazon bookrank payload did not contain observations")
    return rows


def _clean_amazon_bookrank_row(row: dict[str, str]) -> tuple[str, str, str, int, int]:
    raw_date = row["DATE"].strip()
    date = datetime.strptime(raw_date, "%m/%d/%y").strftime("%Y-%m-%d")
    isbn = row["ISBN"].strip().lstrip("'")
    title = row["Title"].strip()
    weekly_sales = int(row["Weekly Sales"])
    weekly_average_rank = int(row["Weekly Average Rank"])
    if weekly_sales < 0 or weekly_average_rank <= 0:
        raise ValueError("bookrank rows must have nonnegative sales and positive ranks")
    return date, isbn, title, weekly_sales, weekly_average_rank


def _extract_nyc_dog_name_frequency_rows(text: str) -> list[tuple[str, int]]:
    payload = json.loads(text)
    if not isinstance(payload, list):
        raise ValueError("NYC dog-name API payload must be a JSON array")

    counts: dict[str, int] = {}
    excluded = {"UNKNOWN", "NAME NOT PROVIDED"}
    for row in payload:
        if not isinstance(row, dict):
            raise ValueError("NYC dog-name API payload contains a non-object row")
        name = str(row.get("name", "")).strip().upper()
        if not name or name in excluded:
            continue
        frequency = int(row.get("frequency", 0))
        if frequency <= 0:
            raise ValueError("NYC dog-name frequencies must be positive integers")
        counts[name] = counts.get(name, 0) + frequency

    if not counts:
        raise ValueError("NYC dog-name API payload did not contain usable names")
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))


def _download_text(url: str) -> str:
    return _download_bytes(url).decode("utf-8")


def _download_bytes(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": "xshi-math-incerto-data/0.1"})
    with urlopen(request, timeout=120) as response:
        return response.read()


__all__ = [
    "BookRankData",
    "DatasetNotAvailable",
    "DogNameFrequencyData",
    "FRED_SP500_CSV_URL",
    "KAGGLE_AMAZON_BOOKRANK_DOWNLOAD_URL",
    "KAGGLE_AMAZON_BOOKRANK_METADATA_URL",
    "NYC_DOG_LICENSE_DATASET_URL",
    "NYC_DOG_NAME_FREQUENCY_API_URL",
    "PriceSeries",
    "cache_path",
    "data_root",
    "load_amazon_bookrank",
    "load_nyc_dog_name_frequencies",
    "load_sp500_prices",
    "snapshot_path",
    "write_amazon_bookrank_snapshot",
    "write_nyc_dog_name_frequency_snapshot",
    "write_sp500_cache_from_csv",
    "write_sp500_fred_cache",
]
