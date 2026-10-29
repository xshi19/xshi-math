# Tech layoffs empirical example

2026-10-29. Branch `csn/layoffs-example`, base `0306b19`. Xiang selected
**gpt-6-astra xhigh** for prose/code and a separate **gpt-6-astra max** run
for subsequent mathematical review. No agents were delegated work. Nothing
was staged, committed, pushed, published, or deleted. No ch09 or kappa page,
ch09 record, or program-state field was edited.

## Delivered files and scope

- [Worked page](../../content/incerto-layoffs-tails.md): original English
  empirical exposition; main conclusion for counts is “fat tail, tail index
  about 1,” with explicit rejection of the pure continuous power-law fit.
- Two main figures:
  [count Hill plot](../../assets/incerto/figures/layoffs-counts-hill.svg) and
  [reported-percentage log-loss Hill plot](../../assets/incerto/figures/layoffs-logloss-hill.svg).
  Shading is a nominal 95% pointwise empirical-bootstrap interval, not a
  simultaneous band or a coverage guarantee.
- [Demo](../../demos/incerto/layoffs_tails.py) generates both SVGs and
  [aggregate JSON](../../assets/incerto/outputs/layoffs-tails.json) /
  [readable output](../../assets/incerto/outputs/layoffs-tails.txt).
  The JSON contains summary statistics and plot coordinates, no event rows.
- [Dataset helpers](../../src/math/incerto/datasets.py): `LayoffData`,
  `clean_layoffs`, `load_layoffs`, `workforce_log_loss`.
  [Estimator helper](../../src/math/incerto/estimators.py):
  `hill_stability_bootstrap`. All are re-exported from `xmath.incerto` and
  documented at stable [API anchors](../../content/incerto-api-reference.md).
- [Download script](../../scripts/download_layoffs.py) uses the separately
  installed Kaggle CLI and the user's configured credentials. It retains the
  ZIP, refuses an existing output path, and extracts only the selected CSV
  to a fixed destination. The ignored default is
  `data/incerto/cache/layoffs/layoffs.csv`. No credentials or dataset files
  were added. `.gitignore` also covers `data/incerto/layoffs/`.
- Updated the two power-law pages' future-example notes, Incerto hub,
  empirical-example index, and `myst.incerto.yml`. Regenerated
  `assets/data/concept-graph.json` and `assets/graphs/concept-list.html`:
  **43 nodes, 75 dependency edges, 87 reference edges** (191 total edges
  including the graph's other edge categories).
- [Snippet tests](../../tests/test_incerto_page_snippets.py) skip only the
  data-dependent layoffs block when its local CSV is absent. They still test
  its recorded output against aggregate JSON and execute its data branch
  against synthetic rows. API-link, dropdown, and plain-number checks remain.
  [Output regeneration](../../scripts/regenerate_incerto_outputs.py) now
  accepts `--pages` and preserves the recorded data block if its CSV is absent.
- [Synthetic unit tests](../../tests/test_incerto_layoffs.py) cover grouping,
  raw/clean schema equivalence, missingness, invalid values, log-loss
  inversion/endpoints, bootstrap percentiles/ties, and mocked CLI download.

The only additional statistical comparison is a compact CSN cutoff/MLE/KS
fit and 1,000-replicate refitted GOF check for each observable. These separate
an empirical exponent estimate from a model claim. No LR/Vuong table, implied
company-size analysis, imputed percentage analysis, or extra visualization was
added. The reference's nominal exponential-comparison p-values are especially
awkward to interpret with an apparent count index near one; the existing GOF
note explains the likelihood-contrast moment conditions. The two requested
observables do not need that additional inference.

## Data and cleaning agreement

Source: layoffs.fyi via Kaggle mirror `swaptr/layoffs-2022`, retrieved
**2026-10-26**, event dates **2020-03-11 through 2026-10-22**. Local inputs were
read from `/workspace/layoffs-research/data/`; none was modified or copied
into this repository. No Grok Bot Page was consulted, copied, or linked.

The raw and research-clean CSVs give identical event arrays. There are
**4,644 rows**, **4,621 company-date events**, **3,014 observed positive
counts**, and **1,607 missing counts**. Company names are trimmed but not
case-folded. Within company/date, available counts are summed and fractions
maximized; all-missing groups stay missing. Exact duplicate rows are included
in that aggregation, matching `common.events(load(), 0)` in the reference.
There is no multi-day wave merge or additional deduplication.

There are **2,891 reported fractions**: **2,513 in (0,1)**, **377 equal to 1**,
and **one zero**; **1,730** events lack a fraction. The included fraction
vector matches exactly the sorted `pct_source == reported` subset of
`pct_with_imputed.csv` used in `19_final_numbers.py`. No imputed rows enter.
The largest finite included fraction is 0.98, mapping to log loss 3.91.

The helper computes `-log1p(-p)`, retaining zero and rejecting 1, missing,
nonfinite, or out-of-range inputs. The caller explicitly filters the positive
finite-loss sample. The page counts full cuts separately and never clips
100% to 99% or to `1-epsilon`. Its `L` is explicitly local log loss, distinct
from the shared canon's slowly varying function.

Input SHA-256:

- Raw `kaggle_swaptr_layoffs.csv`:
  `3e2df7c77ec8a2e0818587709ce1a088178cd866d288cdf0bc3b0826a6757add`.
- Clean `layoffs_clean.csv`:
  `b4bbf5a04e8341f9b1e48928817ebcead0587cacf42ed660bf48d024836406b6`.

A later Kaggle download can differ. The downloader accepts an optional
`--version`; the historical Kaggle version number is not supplied by the
reference, so exact snapshot provenance is recorded by date and hashes.
The demo's optional `--retrieved` records the actual input retrieval date;
it does not label every future download as the historical snapshot.

## Comparison with FINAL_NUMBERS

Compared directly with `/workspace/layoffs-research/out/FINAL_NUMBERS.md`,
`final_numbers.json`, and `src/19_final_numbers.py`.

| Quantity | Reference | This implementation |
| --- | --- | --- |
| Counts n / cutoff / inclusive tail n | 3014 / 230 / 681 | identical |
| Counts CSN alpha / SE / KS | 1.036770 / 0.039729 / 0.052828 | same to shown precision |
| Counts Hill k=301 / k=603 | 1.036464 / 1.006639 | same to shown precision |
| Counts GOF hits / replicates | 0 / 1000 | 0 / 1000 |
| Log-loss n / cutoff / inclusive tail n | 2513 / 0.371064 / 387 | same to shown precision |
| Log-loss CSN alpha / SE / KS | 1.887652 / 0.095955 / 0.113767 | same to shown precision |
| Log-loss Hill k=251 / k=503 | 1.981745 / 2.283022 | same to shown precision |
| Log-loss GOF hits / replicates | 0 / 1000 | 0 / 1000 |

The largest absolute point-estimate difference is below **6e-15**.
It comes from stable `log1p` versus `log(1-p)` and direct versus cumulative
log-sum arithmetic. Both implementations use the continuous likelihood and
both sides of empirical CDF jumps; the candidate rule retains at least 50
observations and refits thresholds in every GOF replicate.

| Pointwise Hill interval | Reference | This page |
| --- | --- | --- |
| Counts, k=301 | [0.94, 1.19] | [0.94, 1.21] |
| Counts, k=603 | [0.96, 1.12] | [0.96, 1.13] |
| Log loss, k=251 | [1.73, 2.42] | [1.73, 2.45] |
| Log loss, k=503 | [1.92, 2.51] | [1.92, 2.50] |

The maximum unrounded endpoint difference is **0.036**. These are new Monte
Carlo intervals with the same percentile method and replicate count. The
reference consumes one RNG across five samples, GOF and separate top-10% /
top-20% bootstraps. This page uses PCG64 seeds **20261029** (counts) and
**20261030** (log loss), resetting the generator to the sample-specific seed
for each method and sharing a whole-sample resample across each Hill curve. The package
GOF sampler also draws a binomial tail count instead of the reference's
per-observation Bernoulli mask. The null mixture is the same, but seeded
realizations differ. This is explained on the page; intervals were not copied
into a differently generated plot. No infinite Hill replicates occurred on
the plotted grids. The helper labels percentiles as conditional on a finite
estimate, reports finite replicate counts, and warns when more than 5% of
replicates are excluded at any k. Synthetic tied cases exercise that warning.

## Reproduction and visual checks

```sh
UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/layoffs-uv MPLCONFIGDIR=/tmp/layoffs-mpl OPENBLAS_NUM_THREADS=1 uv run python demos/incerto/layoffs_tails.py --data /workspace/layoffs-research/data/clean/layoffs_clean.csv --retrieved 2026-10-26
UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/layoffs-uv MPLCONFIGDIR=/tmp/layoffs-mpl uv run python demos/incerto/layoffs_tails.py --recorded assets/incerto/outputs/layoffs-tails.json --figure-dir /tmp/layoffs-figures-repeat
```

Two full-data runs and a fresh-process redraw from aggregate coordinates give
byte-identical SVGs. The final aggregate JSON is from the final helper
implementation, including its direct log-spacing `xi` calculation. No event
identifiers or individual measurements appear in the outputs.

SVG SHA-256:

- Counts: `c26e0e194005b09e2fa25087660165419517d4e4f778e7e42d514f04f49e74c3`.
- Log loss: `abf0f7c12ae2b05db2cb38636898e3ca8de0f23545a99616245b3b41814e6325`.

Rendered all four PNGs with librsvg/Cairo and inspected them at **390×327**
and **900×754** in `/tmp/layoffs-previews`. Labels, markers, shaded intervals,
and legends are legible. The figures use `figures.py`'s fixed fonts, palette,
vertical layout, deterministic SVG IDs, and metadata suppression.

All **six display equations** parse with KaTeX **0.16.25** and errors enabled.
The uniform-fraction calculation now uses three short rows in `aligned`.
The other five displays were reviewed for long rows; none needed another split.
The earlier MathText width estimate did not catch the owner's reported
roughly **435 px** overflow on a **390 px** phone and does not verify browser
fit. The focused check below records the remaining rendering limitation.

## hard_math_claims_for_max_review

| Location | Claim and scope |
| --- | --- |
| `content/incerto-layoffs-tails.md:55`; `src/math/incerto/estimators.py:230` | Hill uses the top k observations with the next order statistic as threshold; alpha is the reciprocal xi estimate and the survival exponent. Pointwise finite-only empirical-bootstrap percentiles have no asserted simultaneous or extreme-value coverage guarantee. |
| `content/incerto-layoffs-tails.md:104` | Counts support the finite-range description “fat tail, tail index about 1”; this is not proof of regular variation or an infinite mean. Assess the strength of that empirical interpretation given ties, pooling, and dependence. |
| `content/incerto-layoffs-tails.md:117`; `src/math/incerto/datasets.py:233` | The explicit local variable L=-log(1-p), its inverse/range, and the uniform-to-exponential counterexample. Endpoint conditioning excludes p=1; the transform alone supplies no tail-class theorem. |
| `content/incerto-layoffs-tails.md:187` | Percentage log-loss estimates describe a different, rounded, conditional sample, not an exponent for raw bounded percentages or full-cut probability. |
| `content/incerto-layoffs-tails.md:196`; `demos/incerto/layoffs_tails.py:25` | Inclusive CSN threshold/MLE/KS agreement with the reference; GOF refits the threshold, reports 0/1000 rather than zero probability, and rejects the specified continuous null while acknowledging rounding/dependence mismatch. |
| `src/math/incerto/datasets.py:146` | The company-date aggregation and missing-value policy reproduce the reference unit; summing rows and maximizing fractions are reporting conventions, not validation of unique job losses. |

This run performed implementation checks and a meaning-preserving prose pass;
it is not the separately requested max mathematical review. No Lean result is
claimed or needed for this empirical deliverable.

## Initial verification and limits

- Requested **`UV_NO_SYNC=1 uv run pytest`**, with writable cache/Matplotlib
  directories and one BLAS thread: **1188 passed, 1 skipped in 165.02 s**.
  The skip is the intentionally absent real-data page snippet. All **35** new
  helper/script cases and synthetic snippet/recorded-output checks pass.
- Explicitly ran both new page snippets with
  `INCERTO_LAYOFFS_PATH=/workspace/layoffs-research/data/clean/layoffs_clean.csv`:
  **two outputs reproduced, zero page changes**.
- Selective output regeneration executed **90** snippets on API/new page,
  preserving the absent-data output. It corrected the new synthetic bootstrap
  example's finite-replicate count to 39. The first targeted test run collected
  the earlier count of 38 before regeneration completed; the final full suite
  passes with the executed output. No pre-existing API output changed.
- Independent raw/clean loader equivalence and reported-percentage agreement
  checked against the local reference inputs. Point estimates, both GOF
  counts, and all four selected intervals compared as above.
- `git diff --check`, new-file whitespace, Python syntax, SVG XML, relative
  paths, API fragments, local bibliography keys, TOC/graph membership, and
  protected-file checks pass. New prose/code files and all aggregate arrays
  were reviewed; the SVGs were visually inspected and byte-compared.
- Python **3.13.5**, NumPy **2.4.6**, SciPy **1.18.1**, Matplotlib **3.11.2**.
  Used locally available dependencies plus an offline editable install. This
  is **not** a locked `uv sync` verification. No dependency/lockfile/package
  mapping changed; no wheel build was run.
- A fresh single-project MyST **1.10.1** build in `/tmp/layoffs-site-check`
  failed at npm preflight: direct npm reports **11.21.1**, but Node's child
  process reports `spawnSync /bin/sh EPERM`. The HTML checker consequently
  fails for absent fresh artifacts. The standard multi-site builder, which
  explicitly deletes intermediate directories, was not used under the
  no-deletion instruction. No HTML/navigation pass is claimed.
- Chrome failed with `setsockopt: Operation not permitted`. PNG figure checks
  succeeded through librsvg; full rendered-page/mobile browser review remains
  unverified. Kaggle live download was not attempted; its CLI integration was
  tested with a synthetic ZIP and mocked subprocess, using no credentials.
- `state.yaml` remains byte-identical to HEAD, SHA-256
  `939070c953ba373672f641e4f4a78dd3f81ede64704bf5b15fd548da21e254a9`.
  No ch09/kappa source, record, or queue state was touched.

## 2026-10-29 focused fixes

Xiang selected **gpt-6-astra xhigh** for this follow-up. Changes are limited to
the estimator, its API documentation and synthetic tests, the worked page,
and this record. Existing worktree changes were preserved.

- `hill_stability_bootstrap` now labels its percentile endpoints as
  **conditional on a finite estimate** in its docstring and
  [API documentation](../../content/incerto-api-reference.md#api-hill-stability-bootstrap).
  It emits one `RuntimeWarning` when more than 5% of replicates are excluded
  at any k, listing affected k values and excluded counts. The warning points
  to the caller; an entirely non-finite column still raises `ValueError`.
- [Regression tests](../../tests/test_incerto_layoffs.py) cover 0%, exactly
  5%, and 10% exclusions, an unaffected k in the same curve, the warning's
  caller location, and both conditional endpoints for tied data.
- The [worked page](../../content/incerto-layoffs-tails.md) now says
  “The Hill estimate and its reciprocal are”. The probability calculation
  puts its left-hand side and each equality on separate `aligned` rows.
  KaTeX parsed all six displays; inspecting the generated MathML found at
  most 25 math characters per row, including scripts and accents. This is
  a source/structure check, not a pixel-width measurement.
- Ran `UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/layoffs-uv
  MPLCONFIGDIR=/tmp/layoffs-mpl OPENBLAS_NUM_THREADS=1 uv run pytest`:
  **1191 passed, 1 skipped in 156.76 s**. The skip remains the real-data page
  snippet without a local CSV. All **38** layoffs helper/script cases pass,
  as do executable API snippets and recorded-output consistency checks.
- Numerical calculations and recorded outputs did not change, so no figure,
  JSON, or text-output regeneration was needed. The displayed API example
  still retains 39 of 40 replicates, below the warning threshold.
- A fresh isolated MyST **1.10.1** build in
  `/tmp/layoffs-fixes-bhzse9my/site` failed at npm preflight
  (`Package Not Found`). A Chromium/Playwright launch failed with
  `setsockopt: Operation not permitted`. Fresh HTML, navigation, and actual
  390 px layout checks remain blocked. The deleting multi-site builder and
  the HTML checker without fresh artifacts were not run.
- `git diff --check`, whitespace checks on the untracked page/test/record,
  and all 21 relative links on the worked page pass. Hashes confirm that only
  the five scoped files changed during this follow-up, no repository files
  were deleted, and ch09/state files and generated outputs are unchanged.
  Nothing was staged, committed, or published. No dependency, wheel, or
  locked-environment build was run.

## Open questions

No owner decision is needed to use the delivered example. Separate max review
remains to be done. A rounding-aware null and employer/period sensitivity
would be useful additional empirical work, but are outside this focused page.
The historical Kaggle version number, a locked-environment rerun, and an
unblocked HTML/mobile-browser check remain verification limitations. No
publication or commit was requested or performed.
