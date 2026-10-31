"""Refresh external datasets used by Incerto examples."""

from __future__ import annotations

import argparse

from xmath.incerto.datasets import (
    cache_path,
    load_nyc_dog_name_frequencies,
    snapshot_path,
    write_amazon_bookrank_snapshot,
    write_nyc_dog_name_frequency_snapshot,
    write_sp500_cache_from_csv,
    write_sp500_fred_cache,
    write_sp500_yahoo_cache,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "dataset",
        choices=["amazon-bookrank", "nyc-dog-names", "sp500", "all"],
        help="Dataset to refresh.",
    )
    parser.add_argument(
        "--data-dir",
        default=None,
        help="Data root. Defaults to INCERTO_DATA_DIR or repo-local data/incerto/ (wheel: user cache).",
    )
    parser.add_argument(
        "--source",
        default=None,
        help="Optional local CSV source for S&P 500 cache cleaning.",
    )
    parser.add_argument(
        "--provider", choices=["fred", "yahoo"], default="fred",
        help="S&P provider (default: fred); --source overrides the provider.",
    )
    parser.add_argument(
        "--end-date", default=None, metavar="YYYY-MM-DD",
        help="Keep S&P closes on or before this date (exclude later intraday rows).",
    )
    args = parser.parse_args()

    if args.dataset in {"amazon-bookrank", "all"}:
        amazon_path = snapshot_path("amazon_bookrank_2001.csv", args.data_dir)
        write_amazon_bookrank_snapshot(amazon_path)
        print(f"Wrote CC0 Amazon bookrank snapshot: {amazon_path}")

    if args.dataset in {"nyc-dog-names", "all"}:
        dog_name_path = snapshot_path("nyc_dog_name_frequencies.csv", args.data_dir)
        write_nyc_dog_name_frequency_snapshot(dog_name_path)
        dog_names = load_nyc_dog_name_frequencies(data_dir=args.data_dir)
        print(
            "Wrote NYC Open Data dog-name aggregate: "
            f"{dog_name_path} ({dog_names.name.size:,} names, "
            f"{dog_names.frequency.sum():,} license-period records)"
        )

    if args.dataset in {"sp500", "all"}:
        sp500_path = cache_path("sp500_daily.csv", args.data_dir)
        if args.source:
            write_sp500_cache_from_csv(args.source, sp500_path, end_date=args.end_date)
        else:
            writer = write_sp500_yahoo_cache if args.provider == "yahoo" else write_sp500_fred_cache
            writer(sp500_path, end_date=args.end_date)
        print(f"Wrote untracked S&P 500 cache: {sp500_path}")


if __name__ == "__main__":
    main()
