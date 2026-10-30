# Incerto data

The snapshots are copied byte-for-byte from incerto-wiki revision
`9717c9cf83aee18b47f423a14bce2f0d14bb8bcb`. They are external data, not covered
by the repository's MIT grant. No financial index data is included.

| File | Source and terms | Recorded access date | Refresh command |
| --- | --- | --- | --- |
| `snapshots/amazon_bookrank_2001.csv` | Caroline (Yuanmo) Zhu, [Amazon Book Sales VS Rank](https://www.kaggle.com/datasets/yuanmozhu/amazon-book-sales-vs-rank), dataset id `yuanmozhu/amazon-book-sales-vs-rank`; CC0 as recorded in source `data/README.md` and `content/bibliography.bib`; Kaggle dataset metadata re-checked 2026-10-17: license "CC0: Public Domain" | 2026-05-24 | `python scripts/fetch_incerto_data.py amazon-bookrank` |
| `snapshots/nyc_dog_name_frequencies.csv` | NYC DOHMH, [Dog Licensing Dataset](https://data.cityofnewyork.us/Health/NYC-Dog-Licensing-Dataset/nu7n-tubp), id `nu7n-tubp`; NYC Open Data; no use restrictions (NYC Open Data FAQ and Local Law 11 of 2012, NYC Admin. Code § 23-502(d)), re-checked 2026-10-17; attribution to DOHMH retained | 2026-08-11 | `python scripts/fetch_incerto_data.py nyc-dog-names` |

The source README and loader document the NYC transformation: trim and uppercase
`animalname`, exclude empty names, `UNKNOWN`, and `NAME NOT PROVIDED`, then group
by normalized name and count license-period rows. Renewals are not deduplicated
into individual dogs. The copied aggregate has 34,680 names and 789,724 included
license-period rows. It contains names and frequencies only.

The source bibliography records NYC's dataset id and access date, but does not
archive a separate license text. On 2026-10-17 the operator re-checked the terms
outside the offline sandbox: the dataset's portal metadata carries no license
field (attribution: Department of Health and Mental Hygiene), and the
[NYC Open Data FAQ](https://opendata.cityofnewyork.us/faq/) states there are no
restrictions on the use of Open Data, consistent with Local Law 11 of 2012; see
the [terms of use](https://opendata.cityofnewyork.us/overview/#termsofuse). The
dates above are source access dates, not new download claims. Record a new access date and review terms when
refreshing either snapshot. Refreshing is explicit and is never part of a build.

`INCERTO_DATA_DIR` or `--data-dir` selects a data root. Editable checkouts default
to `data/incerto/`; wheel installations use `$XDG_CACHE_HOME/xshi-math/incerto`
(or `~/.cache/xshi-math/incerto`). The fetch script writes snapshots beneath
`snapshots/` and financial inputs beneath `cache/` within that root.

## Excluded financial and legacy inputs

The S&P pages now report derived results from a local Yahoo Finance `^GSPC`
daily Close snapshot fetched 2026-10-30. It is a price index, not total return.
The cache spans 1927-12-30–2026-10-29; the 2026-10-30 intraday row was dropped.
See the [observed-data record](../../docs/records/incerto-sp500-observed.md) for
the checksum, transformations and results. No raw prices are redistributed
under Yahoo's source-use terms; FRED also records redistribution restrictions.

```sh
python scripts/fetch_incerto_data.py sp500 --source /path/to/file.csv --end-date 2026-10-29
# Optional Yahoo fetch; the extra is not needed for local CSVs or tests:
uv sync --extra yahoo
python scripts/fetch_incerto_data.py sp500 --provider yahoo --end-date 2026-10-29
python scripts/fetch_incerto_data.py sp500 --provider fred --end-date 2026-10-29
```

FRED remains the default for compatibility. `--source` overrides `--provider`;
`--end-date` is inclusive for every input. Yahoo uses `period="max"`,
`interval="1d"`, `auto_adjust=False` and `Close`. Writers skip missing,
non-finite and nonpositive closes, sort dates, and keep the last usable row
per date. Fewer than two dates fails before replacing the cache.
`cache/sp500_daily.csv` and `raw/` remain ignored. Site rendering uses recorded
statistics and SVGs and does not read or fetch financial data. The empirical
snippet and observed-figure tests skip explicitly when the local cache is
absent; when present they require exact recorded output.

| Source path | Decision |
| --- | --- |
| `legacy/data/SP500.csv` | Excluded: S&P index redistribution restriction |
| `legacy/data/GBP.csv` | Excluded: source and redistribution license not documented |
| `legacy/data/UI_Weekly_Claims.csv` | Excluded: source and redistribution license not documented |
| `legacy/data/SeasonallyAdjustedInitialClaims.csv` | Excluded: source and redistribution license not documented |
| `legacy/data/new-york-air-quality.csv` | Excluded: source and redistribution license not documented |
| `legacy/data/wls_iq_income.csv` | Excluded: source and redistribution license not documented |
| `legacy/data/AmazonBookRank2001.csv` | Excluded: no provenance chain for this legacy copy; the separately documented cleaned CC0 snapshot is included |
| `legacy/1 - Statistical Consequences of Fat Tails/results*.csv` | Excluded: notebook-derived results without sufficient recorded provenance or reproduction contract |

A recognizable filename is not evidence of a redistribution license.
