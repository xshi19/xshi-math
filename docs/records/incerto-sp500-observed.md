# Observed S&P 500 diagnostics

Date: 2026-10-30. Base: `ce67306`, branch `data/sp500-observed`.
Owner selected GPT-6-Astra xhigh for writing/code and a separate max run
afterwards. No commit, publication, or file deletion is part of this task.
The chapter-11 checkout is outside scope.

## Data and decisions

| Item | Recorded choice |
| --- | --- |
| Provider | Yahoo Finance `^GSPC`, daily `Close`, `period="max"`, `auto_adjust=False`; price index, not dividend-reinvested total return |
| Fetch date | 2026-10-30, as supplied with the local snapshot; this run imports that file rather than claiming a new Yahoo network retrieval |
| Source file | `/workspace/incerto-data/sp500_daily.csv`, read only; 24,826 rows, 1927-12-30–2026-10-30 |
| Reference fetcher | `/workspace/incerto-data/fetch_sp500.py`, read only; reused its Yahoo Close selection and cleaning approach; no automatic provider fallback |
| Local cache | `data/incerto/cache/sp500_daily.csv`, ignored by Git; 24,825 closes, 1927-12-30–2026-10-29 |
| Exclusion | The single 2026-10-30 row is intraday; inclusive `--end-date 2026-10-29` drops it |
| Return window | Full available history from 1928-01-03 through 2026-10-29; the 1927-12-30 close supplies the first return's denominator |
| Window rationale | Include early crises and 1987 instead of a short recent sample; historical coverage and volatility regimes are pooled, not assumed homogeneous |
| Units/cleaning | Natural-log close-to-close returns; no interpolation, trimming, calendar resampling, annualization or volatility standardization. Drop missing/non-finite/nonpositive closes, normalize/sort dates, retain last usable duplicate. The supplied file needed only the cutoff. |
| Rights | Yahoo source-use terms apply. Raw prices and the full return sequence are not redistributed. Only derived statistics and diagnostic curves enter tracked files. FRED remains an alternate with its own restrictions. |

Source SHA256:
`cee64b4d35eb839772fcaa5efa68e6e26880921b984176995198c3abcfda04a3`.
Cleaned cache SHA256:
`835b2072b8e4f4bedee4c8e9fcb509a60ee2f7ffeb8292bd1c52b5295d4d8164`.
Checksums identify the private inputs without publishing price rows.

The source and terms are local bibliography entries `yahoo2026gspc` and
`yahoo2026terms`, alongside existing `fred2026sp500`. Yahoo's history and
terms pages returned HTTP 429/999 during this run; no new legal interpretation
or verified quotation is claimed. The supplied source identification is the
provenance for the calculation. yfinance's official download reference was
checked for the explicit period/adjustment/interval and MultiIndex behavior.

## Fetch and reproduction

```sh
python scripts/fetch_incerto_data.py sp500 --source /workspace/incerto-data/sp500_daily.csv --end-date 2026-10-29
uv run python demos/incerto/sp500_diagnostics.py
uv run python demos/incerto/sp500_tail.py
uv run python scripts/regenerate_incerto_outputs.py --pages incerto-sp500 incerto-sp500-tail
```

This environment has no bare `python`; the import command was executed with
the checkout's `.venv/bin/python`. The numerical runs use `UV_NO_SYNC=1` and
temporary writable uv/Matplotlib caches.

FRED remains the default for compatibility. `--provider yahoo` explicitly
selects the new lazy yfinance writer; `--source` takes precedence. The
inclusive cutoff is available to every writer and to cached loader reads.
Existing caches are not changed by read-time filtering. No writer replaces
the destination unless at least two usable dates remain. The `yahoo` extra
is optional; base tests neither import yfinance nor contact Yahoo.

## Derived results

There are **24,824 returns**: **13,018 gains**, **11,493 losses**, and
**313 zeros**. The largest gap is **12 calendar days**; returns retain the
actual adjacent-close spacing. Both halves contain **12,412 returns**.
The first ends on **1977-08-03**; the second starts on **1977-08-04** with
the prior close as its anchor.

| Window / block rule | Excess kurtosis at 1 / 5 / 21 returns | Kappa at 5 / 21 | Maximum drawdown | Largest fourth-power share |
| --- | --- | --- | --- | --- |
| Full, disjoint | 18.77 / 7.66 / 12.04 | 0.12 / 0.10 | 86.19% | 25.22% |
| First half, disjoint | 14.83 / 7.96 / 11.05 | 0.22 / 0.20 | 86.19% | 9.67% |
| Second half, disjoint | 24.53 / 6.23 / 13.30 | 0.03 / -0.04 | 56.78% | 53.54% |
| Full, overlapping | 18.77 / 9.77 / 9.91 | 0.12 / 0.08 | same path | same returns |

The full disjoint 5- and 21-return samples have **4,964 and 1,182 blocks**,
dropping **4 and 2** final returns. Each half has **2,482 and 591 blocks**,
dropping **2 and 1**. Overlapping full-history counts are **24,820 and
24,804**. Kurtosis has no bias correction; kappa uses each horizon's own
sample MAD. The negative second-half value is retained without clipping.
Aggregation does not yield a monotone fall in sample excess kurtosis.

The full-path fractional drawdown is from **1929-09-16 to 1932-06-01**.
The largest absolute return occurs on **1987-10-19**; deleting it changes
sample daily excess kurtosis from **18.77 to 13.76**. The full sample has
**17 upper and 13 lower strict return records**. The continuous-iid
benchmark for each side has mean **10.70**, variance **9.05**. Log-return
extrema are **-22.90% and 15.37%**, not simple-return percentages.

| Tail calculation | Gain side | Loss side |
| --- | --- | --- |
| Hill, floor 5% / 10% / 20% of positive-side count | 2.58 / 2.41 / 2.11 at k=650 / 1301 / 2603 | 2.59 / 2.26 / 1.94 at k=574 / 1149 / 2298 |
| Positive-side 80% / 90% / 95% quantile threshold (% log change) | 1.11 / 1.60 / 2.18 | 1.18 / 1.76 / 2.49 |
| Strict exceedance count | 2604 / 1302 / 651 | 2299 / 1150 / 575 |
| Conditional mean / threshold | 1.78 / 1.65 / 1.59 | 1.87 / 1.70 / 1.57 |

Loss-only Hill at **k=25, 50, 100, 200, 400** gives **4.50, 3.43, 3.09,
2.88, 2.89**. Loss mean excess at the three quantiles is **1.03%, 1.23%,
1.43%** in log-loss units. The broader-fraction Hill estimates differ
substantially; neither a stable exponent nor a universal gain/loss tail
ordering is selected. No confidence interval, moment-existence conclusion,
or proof of regular variation follows from these finite diagnostics.

The existing chronological pipeline was also run on the observed returns.
The initial **12,412** returns train the cutoffs; the final **12,412** are
held out. Both cutoffs use a nominal 95% probability on the training sample.

| Frozen cutoff | Threshold (% log loss) | Held-out exceedances | Frequency | Mean loss above cutoff (% log loss) |
| --- | --- | --- | --- | --- |
| Gaussian mean/std fit | 2.08 | 358 | 2.88% | 3.20 |
| Empirical higher quantile | 1.77 | 518 | 4.17% | 2.80 |

These are a single chronological comparison across different periods.
There is no refitting, random split, iid calibration test, or claim that
one method is generally superior. The pipeline note's theoretical scope
is unchanged; this record supplies its previously missing local-data run.

## Figures and tests

Two new SVGs under `assets/figures/incerto/` use the existing shared
`src/math/incerto/figures.py` theme and vertical layout:

- `sp500-observed-diagnostics.svg`: aggregation summaries and 300 sampled
  chronological prefixes of fourth-power shares and strict record counts.
  Every prefix statistic uses all returns in that prefix.
- `sp500-observed-tail.svg`: strict sign-conditional survival on 80 fixed
  thresholds; loss Hill curve on 100 integer counts; mean excess on 30
  quantile thresholds, with three retained counts. Zero survival is omitted
  from log axes. It does not use rank plotting positions.

No raw prices or full return sequence appear in either SVG or its metadata.
The page code is reader-visible and links to the local API reference;
long code/output blocks remain collapsible. Recorded outputs come from
`scripts/regenerate_incerto_outputs.py`, not hand transcription.
With no cache, the S&P snippets and observed SVG checks skip with explicit
reasons. The regenerator preserves dated output. Synthetic-data execution,
mocked network/cleaning tests and output-format checks still run offline.

## Verification and remaining work

- `UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/sp500obs-uv
  MPLCONFIGDIR=/tmp/sp500obs-final-mpl OPENBLAS_NUM_THREADS=1
  OMP_NUM_THREADS=1 uv run pytest`: **1,425 passed, 1 skipped in 239.50 s**.
  The skip is the absent local layoffs CSV. Both observed S&P snippets pass
  exact-output checks. After final date-normalization and figure-label edits,
  dataset and figure tests pass again: **62 passed in 25.21 s**.
- Absent-cache check with `INCERTO_DATA_DIR=/tmp/sp500obs-absent-data`:
  **17 passed, 4 skipped** in the financial selection. The skips explicitly
  identify the two empirical snippets and two observed SVG checks. Synthetic
  execution and regenerator preservation still pass.
- Both demos ran on real data. The complete report includes all three
  windows, both aggregation rules, both tails, MS powers 1–4, records,
  drawdowns and frozen holdout. Seven page snippets were regenerated through
  `scripts/regenerate_incerto_outputs.py`; a second regeneration is unchanged.
- The two observed SVGs match independent-process regenerations byte for
  byte. Inspected both at **390 and 900 px** after moving the record legend
  and mean-excess counts away from curves. No price or full-return export.
- All **10 display equations** on the two pages parse with KaTeX 0.16.25.
  Conservative glyph/layout estimates at the site's 17 px base size range
  from **159.2 to 265.8 px**. The existing display formulas are unchanged.
  This is not a browser measurement.
- The documented state validator and **1,182 plan file/fragment links** pass.
  It now checks the computed empirical status and evidence record.
  `next_chunk` is unchanged. Changed-file links, bibliography keys, API
  anchors, figure paths, whitespace and the complete new files were reviewed.
- `uv lock --check --offline` and locked offline export with `--extra yahoo`
  pass. The optional dependency graph was generated in a separate scratch
  project from cached registry metadata and merged with the existing lock.
  All **19 existing third-party package entries are unchanged**; 21 optional
  dependency entries were added, with yfinance locked at 1.1.0.
- A fresh `uv sync --locked --offline` was blocked by an uncached pinned
  NumPy wheel before the code changes. Tests use available chapter-10
  dependency files in a new local environment and a fresh editable install
  of **this** checkout. Matplotlib is a local copy to preserve font paths.
  Python 3.13.5, NumPy 2.4.6, SciPy 1.18.1, Matplotlib 3.11.2, pytest 9.0.3.
  The final locked offline sync dry-run resolves without requesting yfinance
  for the base environment; it is not a successful fresh dependency install.
- Local MyST 1.10.1 HTML build, including a scratch attempt, is **blocked**
  at the npm preflight (`Package Not Found`). No fresh HTML check is claimed.
  Playwright's default browser is absent; installed Chrome fails with
  `setsockopt: Operation not permitted`. Desktop/mobile browser navigation,
  live reader review, and a full rendered-page overflow check remain open.
- No packaging mapping changes or Lean work; wheel/Lean builds were not run.
  No source CSV, raw price row or full return sequence was added to tracked
  files. The cache remains ignored, with the checksum above. No files staged,
  no repository files deleted, and no commit or publication made.

Separate GPT-6-Astra max review of the observed claims and live reader review
remain pending. `next_chunk` stays `#/chunks/scft-v4-ch11`.

## Changed files

| Area | Files |
| --- | --- |
| Pages and sources | `content/incerto-sp500.md`, `content/incerto-sp500-tail.md`, `content/incerto-api-reference.md`, `content/bibliography.bib` |
| Fetching and dependency metadata | `src/math/incerto/datasets.py`, `scripts/fetch_incerto_data.py`, `pyproject.toml`, `uv.lock` |
| Reproduction | `demos/incerto/sp500_diagnostics.py`, `demos/incerto/sp500_tail.py`, `scripts/regenerate_incerto_outputs.py` |
| Tests | `tests/test_incerto_datasets.py`, `tests/test_incerto_page_snippets.py`, `tests/test_incerto_diagnostic_figures.py` |
| New derived figures | `assets/figures/incerto/sp500-observed-diagnostics.svg`, `assets/figures/incerto/sp500-observed-tail.svg` |
| Documentation and state | `README.md`, `data/incerto/README.md`, `docs/plan/incerto-program/state.yaml`, `docs/plan/incerto-program/m0.5-review.md`, `docs/plan/incerto-program/validation.md`, this new record |

## Claims for separate max review

These are empirical/computational claims and their interpretation. Existing
chapter-10 theorem statements and proofs are unchanged. Repeated numerical
output is grouped with its prose claim; the complete tables above also
belong to this review. Locators refer to this working tree.

| ID | Public locator | Claim / key numbers |
| --- | --- | --- |
| SP500-O01 | `content/incerto-sp500.md:31`; `content/incerto-sp500-tail.md:36` | Price-index log returns, 1928-01-03–2026-10-29; 24,825 closes, 24,824 returns; 13,018 gains, 11,493 losses, 313 zeros. No homogeneous iid assumption. |
| SP500-O02 | `content/incerto-sp500.md:156` | Disjoint excess kurtosis 18.77 / 7.66 / 12.04; overlapping 18.77 / 9.77 / 9.91; nonmonotone sample aggregation is not a population-moment test. |
| SP500-O03 | `content/incerto-sp500.md:160`; `content/incerto-sp500.md:471` | Kappa full 0.12 / 0.10, first half 0.22 / 0.20, second 0.03 / -0.04; half-window excess kurtoses 14.83 / 7.96 / 11.05 and 24.53 / 6.23 / 13.30; overlapping kappa 0.12 / 0.08. |
| SP500-O04 | `content/incerto-sp500.md:248` | Fractional maximum drawdown 86.19%, peak/trough 1929-09-16 / 1932-06-01; second half 56.78%. |
| SP500-O05 | `content/incerto-sp500.md:276` | Largest fourth-power shares 25.22%, 9.67%, 53.54%; deletion of 1987-10-19 moves full excess kurtosis 18.77 → 13.76. |
| SP500-O06 | `content/incerto-sp500.md:379` | 17/13 strict return records; continuous-iid mean 10.70, variance 9.05; log extrema -22.90% / 15.37%; reference is not a calibrated test of this history. |
| SP500-O07 | `content/incerto-sp500.md:396`; `content/incerto-sp500.md:490` | Gain/loss fractional Hill estimates, thresholds/counts and conditional ratios; 95% ratios 1.59 / 1.57; no threshold-independent population tail ordering. |
| SP500-O08 | `content/incerto-sp500.md:408`; `content/incerto-sp500.md:518` | Derived prefix curves, 1987 concentration jump, subsequent decline; equal halves at 1977-08-03/04; 12-day largest gap; disjoint block counts and dropped suffixes. |
| SP500-O09 | `content/incerto-sp500-tail.md:116` | Fixed-k Hill exponents 4.50 / 3.43 / 3.09 / 2.88 / 2.89 at k=25 / 50 / 100 / 200 / 400; broader-fraction estimates differ. |
| SP500-O10 | `content/incerto-sp500-tail.md:123` | Log-loss thresholds 1.18% / 1.76% / 2.49%; mean excess 1.03% / 1.23% / 1.43%; 2299 / 1150 / 575 strict exceedances; not an exact Pareto-line claim. |
| SP500-O11 | `content/incerto-sp500-tail.md:136`; `content/incerto-sp500-tail.md:158` | Strict sign-conditional survival, zero omission, fixed diagnostic grid rules; Hill/mean-excess curves do not establish regular variation, iid sampling or moment existence. |
| SP500-O12 | This record, chronological pipeline table | 12,412/12,412 split; Gaussian/empirical cutoffs 2.08%/1.77% log loss; hits 358/518, frequencies 2.88%/4.17%, conditional means 3.20%/2.80%; no general ranking. |

## Max review

Date: 2026-10-30. Xiang's selected model/reasoning: GPT-6-Astra, max.
Scope: the observed-data additions on the two S&P pages, their derived
figures, and this record. This completes the observed-claim review requested
above; it does not complete the separate chapter-10 theorem or live site
reviews. The chapter-11 checkout was not accessed.

Every reported observed number reproduces at its printed precision. One
pre-existing explanation of the helper's minimum input size was wrong and
is corrected below. No empirical value, estimator, window, or figure changed.

The independent calculation is `/tmp/sp500_max_review.py`, with aggregate
results in `/tmp/sp500-max-review-summary.json`; these are local review
artifacts, not repository dependencies. Audit-script SHA256:
`9cd6c5513b6677fbc470aea39e434cef47be89a5bce6278b07f7bd0752379a00`.
It imports pandas 3.0.6, NumPy 2.4.6 and SciPy 1.18.1, with no `xmath`, demo,
loader, estimator, or snippet-harness imports. Python is 3.13.5.

- Read the CSV directly with round-trip float parsing. All dates are unique,
  ordered and nonmissing; all closes are positive and finite. Both input
  checksums above match. Independently comparing the supplied source with
  the cache confirms 24,826 source rows, 24,825 retained rows, and exact
  agreement after excluding only 2026-10-30. No price rows were exported.
- Compute log differences and check them against log price ratios; the
  largest absolute discrepancy is below `2e-15`. Form disjoint sums with
  pandas groups and overlapping sums by convolution, then check every sum
  against its telescoping price ratio. All return counts include zeros.
- Check central-moment kurtosis against SciPy's Fisher excess kurtosis with
  `bias=True`. Center each horizon at its own sample mean for MAD; evaluate
  kappa directly as `2 - log(h) / log(MAD_h / MAD_1)` for horizons above one.
  Use all daily returns in each window's baseline MAD.
- Scan prices for drawdowns and returns for strict records. Compute harmonic
  reference moments directly. Delete the largest absolute **return**, not
  its price row, when recomputing centered kurtosis.
- Sort positive magnitudes independently for Hill, using the next order
  statistic below the retained top k as the threshold. Interpolate the
  80%, 90%, and 95% quantiles linearly and count strict exceedances before
  rounding. Holdout uses all signed losses, training standard deviation
  with divisor n, and the `higher` empirical quantile.
- Reconstruct and exactly match all **51 dated output lines** on the two
  pages without executing their snippets. Separately compare every curve
  and annotation in all six observed figure panels with independent arrays;
  numerical coordinates agree within relative tolerance `1e-12`.

Verdicts apply to the dated cache and stated conventions. **Correct** means
the numerical and descriptive claim is supported. **Correct-with-caveat**
retains the stated limitation or records a provenance/interpretation limit;
it is not a request to replace an already qualified page claim.

| ID | File:line | Verdict | Independent finding |
| --- | --- | --- | --- |
| SP500-O01 | `content/incerto-sp500.md:31`; `content/incerto-sp500-tail.md:36` | correct-with-caveat | 24,825 closes, 24,824 returns, 13,018 gains, 11,493 losses, 313 zeros; anchor and return window match. Both pages explicitly say price index, not total return. Yahoo identity, fetch settings/date and intraday status are supplied provenance, not facts encoded by the date/close CSV. |
| SP500-O02 | `content/incerto-sp500.md:156`; `content/incerto-sp500.md:467` | correct | Disjoint excess kurtoses 18.77 / 7.66 / 12.04 and overlapping 18.77 / 9.77 / 9.91 reproduce. Both are nonmonotone across these horizons; neither identifies a population fourth moment. |
| SP500-O03 | `content/incerto-sp500.md:160`; `content/incerto-sp500.md:471` | correct | Full, first-half and second-half disjoint kappas are 0.12 / 0.10, 0.22 / 0.20, and 0.03 / -0.04. Half-window kurtoses are 14.83 / 7.96 / 11.05 and 24.53 / 6.23 / 13.30. Full overlapping kappas are 0.12 / 0.08. The negative value is a valid sample plug-in result. |
| SP500-O04 | `content/incerto-sp500.md:248`; `content/incerto-sp500.md:489` | correct | Full drawdown is 86.189579%, from 1929-09-16 to 1932-06-01 in this supplied history. Second-half drawdown is 56.775388%, from 2007-10-09 to 2009-03-09. These are ordered fractional price declines with the documented anchors. |
| SP500-O05 | `content/incerto-sp500.md:276`; `content/incerto-sp500.md:488` | correct | Raw fourth-power shares are 25.218686%, 9.666204%, 53.535571%. Removing the 1987-10-19 return gives excess kurtosis 13.759592 after recentering. The first-half maximum is the 1933-03-15 gain; the full and second-half maxima are the 1987 loss. These shares are not additive contributions to centered kurtosis. |
| SP500-O06 | `content/incerto-sp500.md:379`; `content/incerto-sp500.md:486` | correct-with-caveat | Strict records are 17 / 13, counting the first return on both sides. The continuous-iid mean and variance are 10.696802 and 9.051908 **per side**, not a joint calibration. Log extrema are -22.899729% / 15.366129%. The positive extreme spans the 12-day gap described below. |
| SP500-O07 | `content/incerto-sp500.md:396`; `content/incerto-sp500.md:490`; `docs/records/incerto-sp500-observed.md:85` | correct-with-caveat | All six fractional-k Hill estimates, six thresholds/counts and six conditional ratios match. The gain/loss fitted ordering reverses between 5% and broader fractions; the 95% ratios are 1.588337 / 1.574201. Different side-specific thresholds and finite-sample fits do not establish population tail ordering. |
| SP500-O08 | `content/incerto-sp500.md:408`; `content/incerto-sp500.md:518`; `docs/records/incerto-sp500-observed.md:71` | correct | Both halves have 12,412 returns and share the 1977-08-03 price anchor; second-half returns start 1977-08-04. Full disjoint block counts/suffixes are 4,964/4 and 1,182/2; each half gives 2,482/2 and 591/1. Overlapping full counts are 24,820 and 24,804. All 300 displayed prefixes use every earlier return. |
| SP500-O09 | `content/incerto-sp500-tail.md:105`; `content/incerto-sp500-tail.md:116` | correct-with-caveat | Fixed-k Hill estimates are 4.497362, 3.426931, 3.094712, 2.875474, 2.893772. The last step is a small increase, so the endpoint fall is not a claim of monotonicity. Neither the two close estimates nor crossings of two/four establish a stable exponent or moment boundary. |
| SP500-O10 | `content/incerto-sp500-tail.md:110`; `content/incerto-sp500-tail.md:123` | correct | Thresholds are 1.181885%, 1.758863%, 2.486712% log loss; mean excesses are 1.032513%, 1.229283%, 1.427874%; strict counts are 2,299 / 1,150 / 575. The increase at these three quantiles does not establish an exactly linear Pareto mean-excess function. |
| SP500-O11 | `content/incerto-sp500-tail.md:136`; `content/incerto-sp500-tail.md:158` | correct | The figure uses 80 strict-survival thresholds from 0.1% to 30% log magnitude, 100 distinct integer Hill counts from 25 to 2,298, and 30 mean-excess quantiles from 80% to 98%. Positive-survival points number 70 for gains and 76 for losses; zeros are omitted. Quantile levels and grid rules are fixed in code; numerical quantile thresholds depend on the sample. The stated limits on regular variation, iid sampling and moment existence are sound. |
| SP500-O12 | `docs/records/incerto-sp500-observed.md:99` | correct-with-caveat | The 12,412/12,412 chronological split, both cutoffs, hits, frequencies and conditional means reproduce. The fitted 95% level is nominal, and the reported severity is mean **loss above the cutoff**, not mean excess. A single retrospective split supplies no general method ranking or calibration guarantee. |

Additional precision checks:

| Window / rule | Excess kurtosis at 1 / 5 / 21 | Kappa at 5 / 21 |
| --- | --- | --- |
| Full, disjoint | 18.768431 / 7.657575 / 12.038630 | 0.115431 / 0.104877 |
| First half, disjoint | 14.834813 / 7.961901 / 11.052106 | 0.216011 / 0.201149 |
| Second half, disjoint | 24.529008 / 6.232915 / 13.298307 | 0.031114 / -0.044447 |
| Full, overlapping | 18.768431 / 9.774042 / 9.910968 | 0.120953 / 0.080955 |

| Frozen cutoff | Threshold (% log loss) | Hits / 12,412 | Frequency | Mean loss above cutoff (% log loss) | Mean excess (% log loss) |
| --- | --- | --- | --- | --- | --- |
| Gaussian | 2.076019 | 358 | 2.884306% | 3.199914 | 1.123895 |
| Empirical higher quantile | 1.769961 | 518 | 4.173381% | 2.798923 | 1.028962 |

The maximum calendar gap is **1933-03-03 to 1933-03-15**. Consequently,
the +15.37% extremum is a change between available closes spanning twelve
calendar days. The pages already explain this clock. No missing-session
diagnosis follows from the date gap alone. The fourth-power share jumps
from 9.533990% to 31.984824% on 1987-10-19, then is nonincreasing to
25.218686%; the figure's concentration interpretation is accurate.

One correction, outside the newly added empirical claims:

| File:line | Verdict before fix | Minimal fix |
| --- | --- | --- |
| `content/incerto-sp500.md:514` | wrong | Replaced “At least 44 closes are required to form a 21-return block in each half” with “The helper requires at least 44 closes.” Mathematically, 43 closes yield 42 returns, hence 21 in each half. A direct synthetic check confirms this, while the existing helper rejects fewer than 44 closes. Its input guard and all numerical outputs are unchanged. |

Decisions for Xiang: retain the documented full window, half split,
threshold rules and printed precision. No observed-claim correction or
statistical redesign is needed. An optional editorial addition could name
the twelve-day interval beside the positive extremum; the existing
available-close caveat already prevents a one-calendar-day interpretation.
Keep population tail/moment conclusions and calibrated iid error bars out
of these exploratory results. No new owner decision blocks this review.

The supplied fetch provenance was not independently reauthenticated:
Yahoo's historical endpoint returned HTTP 429 during this review. The
[FRED series notes](https://fred.stlouisfed.org/series/SP500) do confirm the
alternate provider's ten-year daily window and exclusion of dividends.
No new download, source substitution, or interpretation of redistribution
permission was made.

Verification for this review:

```sh
UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/sp500-max-review-uv \
  MPLCONFIGDIR=/tmp/sp500-max-review-mpl OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
  uv run python scripts/regenerate_incerto_outputs.py --pages incerto-sp500 incerto-sp500-tail
UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/sp500-max-review-uv \
  MPLCONFIGDIR=/tmp/sp500-max-review-mpl OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
  uv run pytest tests/test_incerto_datasets.py tests/test_incerto_diagnostics.py \
  tests/test_incerto_estimators.py tests/test_incerto_concentration.py \
  tests/test_incerto_diagnostic_figures.py tests/test_incerto_page_snippets.py
git diff --check
```

- Regenerated **7 snippet outputs; 0 pages changed** by regeneration.
- Affected tests: **647 passed, 1 skipped in 159.91 s**. The skip is the
  absent local layoffs CSV. Both S&P empirical snippets and both observed
  SVG reproduction tests ran and passed. The SVG tests compare independent
  process regenerations byte for byte with the working-tree artifacts.
- Parsed both complete SVG documents and checked their plotting inputs and
  metadata; no CSV payload, full price/return series, or embedded bitmap.
- Reviewed the complete appended section and the review-only page diff.
  `git diff --check` passes; the untracked record was checked separately
  for trailing whitespace and final newline. Existing page links,
  citations and equations are unchanged.
- No fresh HTML build, browser/live review, dependency installation,
  packaging or Lean check was attempted. The earlier site-build limitations
  remain; passing Python and SVG checks does not close those gates.
- Only `content/incerto-sp500.md` and this already-untracked record changed
  during this review. Hash comparisons preserve every other initially
  modified/untracked artifact. The cache remains ignored and unchanged.
  Nothing was staged, committed, published or deleted.
