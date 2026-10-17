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

Financial data to be provided later via the Portfolio Manager bot.
S&P Dow Jones Indices/FRED S&P 500 data have redistribution restrictions recorded
by the source. Supply an authorized local file with
`python scripts/fetch_incerto_data.py sp500 --source /path/to/file.csv`, or fetch
for permitted local use with `python scripts/fetch_incerto_data.py sp500`.
The resulting `cache/sp500_daily.csv` is ignored; no values are needed to build
the public method page. `raw/` is ignored as well.

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
