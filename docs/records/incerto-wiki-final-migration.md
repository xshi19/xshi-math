# Final incerto-wiki migration

Date: 2026-10-17. Owner: Xiang Shi. Selected model: Codex GPT-6-Astra xhigh.
Source: `xshi19/incerto-wiki` at
`9717c9cf83aee18b47f423a14bce2f0d14bb8bcb`. Worktree branch:
`codex/incerto-wiki-remaining-migration`, based on `24dad46`.
Changes are uncommitted. No source Git history, notebook outputs, secrets,
book excerpts, workflows, or restricted financial data were imported.

The owner authorized the remaining migration, superseding prior deferred
SCoFT/example/graph dispositions. `docs/plan/index.md` and
`docs/plan/incerto-program/**` remain untouched for PR #24. Earlier phase
records describe their original scoped gates, not this expanded migration.

## Placement

| Source area | Destination and decision |
| --- | --- |
| SCoFT intro, Chapters 3 and 4 | `content/incerto-scoft-{intro,ch3,ch4}.md`; cited reading maps with explicit planned topics |
| Chapters 5–7 | Planned stubs in manifest and intro; no empty public pages |
| Five examples and index | `content/incerto-{amazon-bookrank,nyc-dog-name-tail,sp500-tail,dispersion-ratio,lln-preasymptotic,empirical-example-concepts}.md` |
| Example computations | `demos/incerto/`; six static SVG figures in `assets/incerto/figures/`; no executed cells at build time |
| Dependency graph | `scripts/build_concept_graph.py`, `assets/{graphs,css,js,data}/concept-*`; 28 frontmatter nodes, 54 prerequisite edges, 43 reference edges; build stages a fresh copy under `/math/incerto/assets/` |
| Glossary | `content/incerto-glossary.md`: Black Swan, Extremistan, Mediocristan are Incerto-local vocabulary, not parallel mathematical notation |
| Shared notation | Extended `content/notation.md` with sample sums/means, scale, and normal CDF; cross-track symbols remain canonical |
| External guides / Chinese entry | `content/incerto-{external-reading,reading-embrechts,chinese-entry}.md`; new internal and cross-track links |
| API page / Python modules | Public `content/incerto-api-reference.md`; installed `xmath.incerto` in `src/math/incerto/`; module docstrings replace old Sphinx machinery |
| Source home / reading navigation | Static entry paths merged into `content/incerto/index.md`; query-state reading-nav JS/JSON excluded because the lists fit MyST and need no runtime hooks |
| Bibliography | `content/bibliography.bib`, 20 unique useful keys, configured in `myst.incerto.yml`; previous notes used ordinary citation links, so no conflicting existing BibTeX keys |
| Normal-mixture / variance-gamma pages | Standalone duplicates excluded; general theory stays in Normix. Scalar fourth moments, largest-variance tail control, VG MGF/density/origin behavior and API parameter mapping are folded into the Chapter 4 guide |
| Releases / Lean blueprint / proof support / review / audit | Historical docs-only files under `docs/records/incerto-wiki/`, with source/date banners and an archive README |
| Lean project | `formalization/incerto-lean/`, independent of Python and site builds; Lean/Mathlib v4.19.0 checked upstream 2026-09-05, **not rechecked here** |
| Old authoring and build machinery | Excluded in favor of specific xshi-math equivalents listed per path in the manifest |

There are now 43 Incerto pages and 67 canonical pages across the four sites.
The static graph uses semantic concept ids and new flat page stems in URLs;
only prerequisites must form a DAG. Proof/reference/generalization edges may
cycle. Normix references remain ordinary cross-subsite links, outside the graph.
The plain graph list works without JavaScript.

## Rights review

The supplied overlap tool was run from the setup directory against the local
`scoft.txt`, with both `N=6` and `N=5`, before adaptation. Its output label is
always `overlap8`; the table below records the actual requested N. The tool's
counts include metadata, code, titles, and references, so these percentages
are screening evidence, not a license determination.

| Source page | 6-gram token coverage | 5-gram token coverage |
| --- | ---: | ---: |
| SCoFT intro | 3.4% | 8.9% |
| SCoFT ch3 | 1.5% | 2.5% |
| SCoFT ch4 | 0.8% | 1.5% |
| Amazon bookrank | 0.0% | 0.0% |
| Dispersion ratio | 0.0% | 0.6% |
| LLN pre-asymptotic | 0.9% | 0.9% |
| NYC dog names | 0.7% | 1.3% |
| S&P | 0.0% | 0.0% |
| Glossary | 0.0% | 0.0% |

All matched spans were inspected against their surrounding book text. Matches
were bibliographic titles/URLs, short conventional probability language, a
formula's token sequence, and brief Chapter 3 phrasing. No long copied passage
was found in these nine pages. Headings and quoted expressions were reviewed
separately. Short factual chapter/section titles and bibliographic titles remain
as citations. The guides are attributed chapter-to-note maps; they do not
present the chapter's claims as newly proved repository results. Empirical
prose is supported by rerun repository computations and retains its caveats.

Every source-adjacent rewrite/drop identified in this review is listed here;
no book text is included in the record:

| Source file / passage | Action |
| --- | --- |
| `content/reading-guides/taleb-scoft/ch3.md`, opening tail-category comparison | Reworded as a reading route connecting geometry, limit theorems, and estimation |
| Same file, consequence 4, variance-based finance metrics | Reworded around the required moments rather than the book-adjacent metric list |
| Same file, §3.5–3.6 transition after catastrophe discussion | Rewrote the common matched transition as an explicit dependence/exposure modeling caveat |
| Same file, final ensemble/time-probability comparison | Rewrote in terms of realizations, a single trajectory, and an absorbing loss barrier |
| `legacy/.../Chapter-3.ipynb`, consequence and regression captions | Entire notebook excluded; existing maintained concepts/demos supply independent treatments |
| `legacy/.../Chapter-4.ipynb`, stochastic-variance mixture captions | Entire notebook excluded; synthetic plots regenerated by committed scripts |
| `legacy/.../Chapter-5.ipynb`, book-adjacent chapter/section wording | Entire notebook excluded; Chapter 5 remains explicitly planned |
| `legacy/.../Chapter-6.ipynb`, random-matrix/eigenvalue caption and heading | Entire notebook excluded; no caption or output imported |
| `legacy/.../Chapter-7.ipynb` and `Untitled.ipynb` | Entire notebooks excluded as output-heavy exploratory artifacts; the supplied 8-gram report found no matching Markdown spans in these two |

A second N=5/N=6 scan of all nine adapted pages found only the retained
bibliographic/heading/formula/common-language matches (maximum 4.2% at N=5
and 1.6% at N=6, both on the short intro including its MIT notice). No
source-adjacent prose match remained from the rewritten Chapter 3 passages.

The supplied notebook report shows Markdown overlap of 14.5%, 9.6%, 3.4%,
and 7.2% for Chapters 3–6 respectively. Notebook outputs were not used as
public assets. Other adaptation changes correct scope or presentation:
Chapter 4's general scale-mixing claim is restricted to the local Gaussian
variance calculation; Gaussian scale calibrations are explicitly justified;
no new universal heavy-tail theorem is inferred from the figures.

Repository-owned material retains copyright (c) 2023 xshi19 and the full MIT
notice, both centrally and on each new public note. The source book and rights
helper files remain outside the worktree.

## Data and numerical results

See [data/incerto/README.md](../../data/incerto/README.md) for each dataset's
source, dataset id, access date, terms, refresh command, and every excluded
legacy CSV. Amazon is the documented CC0 cleaned snapshot (861 rows); NYC is
the recorded aggregate of `nu7n-tubp` (34,680 names; 789,724 license-period rows).
The source records the NYC aggregation and access date. The operator re-checked
terms on 2026-10-17 outside the sandbox: Kaggle metadata lists "CC0: Public
Domain"; NYC Open Data states no use restrictions (Local Law 11 of 2012).
Access dates are inherited, not new fetches.

No S&P, GBP, claims, air-quality, IQ/income, or undocumented legacy Amazon
copy was imported. Notebook-derived results CSVs are also excluded.
Financial data to be provided later via the Portfolio Manager bot.
The S&P public page shows the method, while its demo exits with an availability
message if no local cache exists. Refreshing is explicit, uses urllib, and
writes financial data only to an ignored cache.

The four public figure demos ran from committed snapshots or seeded synthetic
data. Selected results are embedded as static text in the pages. Amazon's
log-log regression has R² 0.801; Hill estimates change with k. NYC's Hill
estimates range from 1.896 at k=50 to 0.783 at k=5000; no single exponent is
claimed. The Pareto running-mean paths and dispersion-ratio experiments retain
their seeds, sample sizes, and distinction between illustration and proof.

## Package and legacy-code decisions

Base `xmath` remains NumPy-only. `xshi-math[incerto]` adds SciPy/Matplotlib;
the development group includes those plus NetworkX/PyYAML. The build now uses
`uv run --locked` to select that environment. The operator must regenerate
`uv.lock` before using it. No requests dependency is needed. An editable checkout
finds `data/incerto`; wheels use a user cache or explicit `INCERTO_DATA_DIR`,
never a write into site-packages. Snapshots are repository assets, not wheel data.

All eight requested package test modules were ported (71 inherited tests),
with additional tests for urllib success/failure, offline cache reads, data-root
precedence, and wheel cache fallback. No network call occurs in those tests.

Useful legacy code was reconciled rather than copied wholesale:

- Distribution classes and calibrated deviations/curvature helpers were already
  maintained in `incerto/` and are now under `xmath.incerto`.
- Lognormal moment conversion and empirical survival were ported to `stats`.
  The latter now respects strict exceedance and ties; the old rank convention
  did not. Moment reconstruction and tied samples are tested.
- A deterministic multivariate mixture demo preserves the useful construction
  using public SciPy functions. The obsolete private-SciPy subclass is excluded.
- Unseeded histogram/PDF/CDF wrappers are superseded by maintained plotting
  helpers and demos. No pandas, seaborn, or scikit-learn dependency was added.
- The legacy FFT inverter has an unvalidated sign/grid convention; the
  efficiency helper does not implement a justified estimator-efficiency
  comparison; Sn/Qn use simplified median/percentile conventions without the
  required finite-sample definition/correction. These unsupported prototypes
  are excluded, as are automatic Huber outlier rejection and the R²-optimized
  log-survival fitting heuristic. Neither is needed by the migrated examples.
- The generic finite-difference region classifier assumes exactly four
  crossings; explicit normal/Student-t curvature helpers and the body/shoulder
  note supersede it. The Lindy Markdown file is empty.

## Routes and legacy mirror

The URL map produces **64 compatibility pages for 65 mapped CSV rows**.
All newly mapped rows say `local build pending operator`. Normal-mixture and
variance-gamma targets are under `/math/normix-theory/`; the existing generator
already accepts any same-origin destination under `/math/`, so no generator
code change was needed. The PR #23 wording lines in it and `check_html.py`
remain untouched.

Chapters 5–7 redirect to the SCoFT guide hub. The glossary/external indexes
use old routes `index-2`/`index-3`. Historical Lean/release routes stay retained:
their docs-only destinations are not equivalent public math pages. The old
home Markdown download also remains retained. These four deliberately blank
target rows are reported by the existing generator, not silently dropped.
API landing, module, index/search, and source-view routes redirect to the
new API overview, which links the maintained module sources. This also
resolves the old missing tail-diagnostics navigation targets. Historical
function fragments are unaudited; incoming fragments remain preserved.
The assembled site also generates 63 compatibility routes for old flat math URLs.

The dependency-DAG asset allowance was removed from the mirror repair script
because that page is now a compatibility path. The hashed historical
concept-list export still lacks its old stylesheet, so its one exact allowance
remains. A copy of the supplied hub mirror under `/tmp` was overlaid with all
64 generated compatibility pages and the repair overlay, then checked:
**70 HTML files scanned, 64 compatibility paths skipped, 3 static-retained
pages verified, 0 repairs needed, exit 0**. Its 8 warnings are unexpanded historical Sphinx
template references and that one stylesheet gap. This is a mirror
repair check, not a fresh MyST build or live deployment check.

## Open PRs and source accounting

Source PR #54 is captured from the owner's supplied offline summary:
the plug-in page landed; next priorities are Moment-Estimation Failure,
then Inference Asymmetry. Shadow Mean remains separately scoped. Entry-path
navigation was completed upstream and is retained here as static reading paths.
These are future content tasks, not unfinished imports in this migration.
Source PR #55's draft AnyIO lock bump is obsolete: xshi-math owns its own lock.
No network fetch of either PR was attempted.

[The pinned tracked-path list](incerto-wiki/source-paths.txt) contains **252
paths**. Every path has exactly one manifest match: **89 imported/adapted,
160 excluded, 3 stay/planned stubs**, zero uncovered or ambiguous paths.
`tests/test_migration_manifest.py` checks coverage from that committed list
without requiring the old checkout. All rows name a target or replacement and
state a reason. No old CI or publisher was imported.

## Verification and operator handoff

Local environment: Python 3.13.5; numpy 2.4.6, scipy 1.18.1, matplotlib 3.11.2, networkx 3.7, PyYAML 6.0.3, pytest 9.0.3.

Local checks performed:

- All inherited package tests: 71 passed before integration additions.
- Isolated `python -I` imports of stdlib `math`, `xmath`, and `xmath.incerto`
  passed in the supplied editable environment; wheel installation remains unverified.
- Graph validation/generation: 28 nodes; prerequisite graph acyclic; reference
  and proof relations checked separately; staged HTML asset links checked.
- Four static figure demos, S&P missing-data path, and multivariate mixture demo.
- Public source links and citation keys: no missing local targets or unknown
  keys; 20 distinct bibliography keys; no executed notebook cells.
- Temporary mirror overlay and repair `--check`: passed, with known warnings
  described above. Neither supplied read-only clone was modified.

The final suite passed **114 tests and 43 subtests**, with no skips.
`git diff --check` passed. New text files were checked separately; CSV/SVG
assets were parsed, and generated SVG continuation whitespace was normalized.
The read-only skill patch passed `git apply --unidiff-zero --check`. Six figure previews
were inspected, and crowded panel labels were corrected. JavaScript syntax
passed `node --check assets/js/concept-graph.js`. No site build, rendered equation/navigation review, live
publication, wheel build, lock resolution, or Lean recheck is claimed here.
The supplied environment lacks setuptools/build/pip/wheel, and network access
for dependency/toolchain installation is unavailable; packaging verification
is therefore on the operator checklist.

The sandbox mounts `.agents/` read-only. The requested skill edits could not be
written; a temporary `readonly-skills.patch` contained the
exact Lean-status, proof-writing, and hub-publish updates for the operator. The root and Incerto
routers were updated in writable files. The operator applied the patch; this
is a filesystem limitation, not an approval request.

Operator checks, in order:

```sh
git apply --unidiff-zero docs/records/incerto-wiki/readonly-skills.patch
uv lock
uv sync --locked --extra incerto
uv run pytest
uv build
UV_PROJECT_ENVIRONMENT=.venv-wheel uv sync --locked --no-editable --extra incerto
.venv-wheel/bin/python -I -c 'import math, xmath, xmath.incerto; print(math.sqrt(9), xmath.incerto.__file__)'
npm ci
npm run build
npm run check:html
```

Then inspect graph interaction/fallback and the iframe, figures, equations,
citations, and desktop/mobile navigation under `/math/`. Record actual build
results and update URL-map verification statuses. Hub publication remains a
separate action after those checks; preserve the retained mirror and `/normix/`.
The old repository can be archived by the owner after merge and publication
verification. The Lean recheck is optional and independent; use its README.

## Operator results (2026-10-17, outside the sandbox)

- Applied `readonly-skills.patch` to `.agents/skills/` (hub-publish,
  lean-formalization, proof-writing); the patch file is removed after applying.
- `uv lock`; `uv sync --locked --extra incerto`; `uv run pytest`: 114 passed,
  43 subtests passed.
- `uv build`: sdist and wheel built; non-editable wheel environment imports
  stdlib `math`, `xmath`, and `xmath.incerto` from site-packages.
- `npm ci`; `npm run build`: passed. `npm run check:html`: passed (67 pages
  across four sites, 63 flat redirects, 64 legacy compatibility pages for 65
  mapped rows, 4 rows retained with recorded reasons).
- Headless Chrome on a local `/math/` preview: the Incerto hub, the 15 new
  Incerto pages and `/math/notation/` loaded with no 4xx subrequests and no
  JavaScript errors; the dependency-DAG iframe and figures resolve.
- Not done: hub publication and live checks; Lean recheck.
