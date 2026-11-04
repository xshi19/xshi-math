# Design verification

Chapter-9 implementation (2026-10-29) is recorded in the
[chapter-9 checkpoint](../../records/incerto-scft-v4-ch09.md): nine extended
concepts, hidden-tail note and guide, seven helpers, the Hill tie fix and four
figures. This record separates executed numerical/source checks from blocked
site checks and the pending separate max review.

Earlier chapter-8 evidence is in the [implementation record](../../records/incerto-scft-v4-ch08.md):
teaching/Python, four new SVGs and two figure repairs, with 390/900 px inspection.
The completed separate chapter-8 max review and numerical fixes are appended
to that record; its original checkpoint retains historical pending flags. Chapter 7's
[max review](../../records/incerto-scft-v4-ch07.md#max-review) is already complete;
its earlier pending flag is reconciled in state. Local tests use available
dependency versions. Locked installation, a fresh MyST build and browser
review remain blocked as recorded in the current checkpoint. No publication
or live reader review is claimed. Historical evidence below retains its scope.

Baseline: 2026-10-16, revision `998a4a11a17b7ae7ba4c306005a4c8e3109f4392`.
Owner revisions: 2026-10-17, branch `plan/incerto-program`, PR #24.
The records below retain their original design scope and results, including
the [v4 chapter-order record](#v4-chapter-order-revision-2026-10-17).
The subsequent review branch records its actual checks and sandbox limits in
[M0.5 verification](m0.5-review.md#verification-and-limits); these historical
passes do not validate that working tree.

Prior chapter-5 and appendix-B implementation and checks are in the
[chapter-5 checkpoint](../../records/incerto-scft-v4-ch05.md#max-review):
separate Astra max review passed with fixes; 392 Python tests passed,
including 54 chapter-5 cases. Four deterministic SVGs use the shared style
and were inspected at 390px and 900px. Lean is skipped.
A fresh HTML build remains blocked by the sandbox's MyST npm preflight;
HTML checks consequently fail on absent output. External build/check and
post-publication live reader review remain pending. The chapter-4 record
retains its completed operator build pass; that pass does not verify this worktree.
The historical results below do not verify this worktree.

## Earlier revision: changed artifacts

Revised `README.md`, `inventory.md`, `concepts.md`, `architecture.md`,
`templates.md`, `sources.md`, `state.yaml`, `validation.md` and this record;
added [m0.5-review.md](m0.5-review.md) as the pending review contract and issues
list. Only the Incerto program row text changed in `docs/plan/index.md`.
All authored changes stay within these authorized planning paths. No concept
page, Lean, Python or site code, configuration, URL-map row or dataset changed.
No files were deleted; no commit, push or publication was performed.

## Previous run: outside-sandbox results

The operator's results supplied in Xiang's review replace the initial sandbox
failure as the previous run's site-verification outcome:

| Check | Result supplied by operator |
| --- | --- |
| `npm ci` | Passed outside the sandbox. |
| `npm run build` | Passed outside the sandbox. |
| `npm run check:html` | Passed: 52 pages across four sites and 48 redirects. |
| Legacy URL map | Two pre-existing unresolved rows were skipped; neither was introduced by PR #24. |

The skipped rows are `incerto-scoft-intro` and `hub-incerto-home-export` in
[the URL map](../url-map.csv). Their existing rights/retention decisions remain
unchanged. The first sandbox's DNS `EAI_AGAIN`, absent MyST executable and
missing-build HTML failures are historical context only; they do not negate
the completed outside-sandbox run. These are operator-reported results, not
checks rerun by this revision's agent.

## Earlier revision: local checks

| Check | Result |
| --- | --- |
| Guidance and scope | Re-read `AGENTS.md`, all `docs/rules/` files, relevant skills and repository/track guidance; honored the explicit Astra max selection. |
| State validation | The executable block in `validation.md` passed with PyYAML 6.0.3: unique keys, IDs, scope/status/role references, acyclic graphs, required source mappings, delivery order, optional Lean/skip reasons, M0.5 gate, resolved decisions, baseline paths and derived counts. |
| Stable records and human views | Preserved all 101 concept IDs and 187 book source-unit IDs; checked human concept fields, chapter mappings, exclusions and the 24-page review matrix against state. |
| Local links and whitespace | Relative links and Markdown/explicit anchors passed; `git diff --check` and separate new-file whitespace checks passed. Reviewed the diff and full new review record. |
| MyST inclusion | Planning files remain outside all four TOCs and page globs; no rendered page is added. |
| `npm ci --cache /tmp/xshi-incerto-revision-npm-cache --fetch-retries=0 --fetch-timeout=15000` | Attempted for this revision; failed with DNS `EAI_AGAIN` fetching `mystmd-1.10.1.tgz` from `registry.npmjs.org`. No `EPERM` was observed. |
| `npm run build` | Attempted; failed because `node_modules/.bin/myst` is absent after dependency installation failed. No fresh complete HTML artifact was produced. |
| `npm run check:html` | Attempted; failed on missing generated pages/assets after the failed build. The two existing unresolved legacy rows were again skipped; they are not the cause of the missing-artifact failures. |

Counts for that earlier revision distinguished completion scope from retained references:

| Record | In scope | Out of scope | Total retained |
| --- | --- | --- | --- |
| Books | 2 | 5 | 7 |
| Numbered chapters | 48 | 77 | 125 |
| Book source units | 64 | 123 | 187 |
| Concepts | 72 | 29 | 101 |

There are 14 starting paper records, 24 existing concept bodies and zero
checked Lean concepts. Required 2025 Technical Incerto additions await exact
reconciliation and are not counted as mapped units yet.

## Operator record: outside-sandbox rerun for the earlier revision

Completed on 2026-10-17 (America/New_York) against the working tree of this
revision (base commit f425a1c plus these docs/plan changes), outside the sandbox.

| Field | Operator entry |
| --- | --- |
| Date and revision | 2026-10-17; f425a1c + this revision's docs/plan changes |
| `npm ci` | pass |
| `npm run build` | pass after deleting the ignored `_build/` cache (the sandboxed attempt had left an incomplete MyST book-theme template; a clean rebuild succeeded) |
| `npm run check:html`, page/site/redirect counts | pass: 52 pages across four sites, 48 redirects, 45 pages with display math |
| Pre-existing legacy skips / new findings | 2 pre-existing unresolved legacy url-map rows skipped (28 compatibility pages for 29 mapped rows); no new findings |
| Log or evidence location | operator shell logs on the agent box (not committed) |

## Earlier revision: limits (historical)

Python tests, demos and packaging were not rerun: only planning documents
changed. Lean setup/build and CI were not run. Live reader review, rendered
equation/navigation review and publication were not performed. The two M0.5
reviews are defined here as the next chunk, not claimed complete. No dataset
was acquired and no source theorem was certified by this revision.

Source metadata checks from the baseline remain historical; this revision did
not recheck external metadata or full-text claims. The open content decisions
are Shadow Mean scope, stochastic-calculus teaching/numerical depth and exact
2025 Technical Incerto reconciliation. The M1 pilot, declaration-level Lean
scope, bot data routing and on-demand paper inclusion are approved in state.

<a id="v4-chapter-order-revision-2026-10-17"></a>

## V4 chapter-order revision — 2026-10-17

Revision base: `e7aaa5ffb786acfdd6a969c4ba780a7c9f4e0fe4`, plus the current
uncommitted planning changes. The historical open questions above are closed
by this revision's owner decisions; their earlier pending status is retained
only as history.

### Changed artifacts

Revised all ten existing files under `docs/plan/incerto-program/`: `README.md`,
`inventory.md`, `concepts.md`, `architecture.md`, `templates.md`, `sources.md`,
`state.yaml`, `validation.md`, `m0.5-review.md` and this record. Outside that
directory, only the Incerto program row text in `docs/plan/index.md` changed.
No source file was added or deleted. No concept page, Lean, Python, site code,
configuration, dataset or URL-map row changed. The PDFs, TOC extracts and
bibliography remain read-only outside the repository. No commit, push, PR
message or publication was performed.

### Source reconciliation and decisions

Direct PDF extraction of TOC pages 7–14 matches both supplied TOC extracts
for all numbered chapters and lettered appendices. The v2 map has 25 chapters
and eight appendices; v4 has **30 chapters and nine appendices**. All 33 old
units have explicit correspondences, and the six additions are mapped.
`pdfinfo` counts and PDF hashes are in [sources](sources.md#local-v2-and-v4-evidence).

No numbering deviation was found: chapters 1–11 keep their numbers; shifts
are +2 for v2 12–16, +3 for 17–19, +4 for 20–24 and +5 for 25. Appendix A
is unchanged; B–H become C–I. There are title changes at v2 chapters 8, 14,
21, 22 and appendix B, recorded in the [mapping table](inventory.md#v2-to-v4-correspondence).
The full v2-to-v4 delta is five chapters plus one appendix, exceeding the
three main additions used by the earlier metadata-only plan. Chapter 29 and
its journal paper also have different titles: *Portfolios* versus *Pension
Funds*. Title/locator reconciliation does not certify theorem equivalence.

All 101 prior concept IDs and their page reservations are preserved.
`c-probability-conflation` and `c-portfolio-tail-dependence` are appended;
`c-lindy` is reactivated at chapter 23's technical scope. All papers have
chapter hosts. M0.5 remains first, followed by `scft-v4-ch01` and
`scft-v4-ch02`; the latter contains the optional exceedance pilot.
Shadow Mean scope, basic calculus depth and edition reconciliation are
approved and removed from `open_questions`.

### Checks performed

| Check | Result |
| --- | --- |
| Guidance and scope | Re-read root guidance, all `docs/rules/`, the current planning set and applicable skills; owner-selected Astra max honored. No subagents were used. |
| State and human views | The executable validator in [validation.md](validation.md) passed with PyYAML 6.0.3: unique keys/no aliases, IDs, graphs, exact chapter order, complete attachment coverage, reciprocal concepts/papers, roles, optional Lean, M0.5, closed decisions, v2 correspondence and derived counts. Human titles/scopes/source links and the 24-page review matrix agree with state. |
| Stable records | Compared with the revision-base Git state: all 101 concept IDs and paths retained; only `c-lindy` changes scope disposition. All 33 old SCoFT unit IDs are preserved in the correspondence map, with an explicit v4 active namespace. |
| Source check | Verified every v2/v4 chapter/appendix TOC record using the local PDFs and extracts; checked the six additions, title changes and bibliography locators. Full-text mathematical review was not performed. |
| Local links and whitespace | Relative file and Markdown/MyST/HTML fragment checks passed; `git diff --check` passed. Reviewed the diff and full changed sections. No new repository files needed a separate whitespace scan. |
| MyST inclusion and change boundary | Planning files remain outside all four TOCs/page globs. Only the ten plan files and one index row changed; no deletions. |
| `npm ci` | Not rerun: an installed MyST 1.10.1 was available and the lockfile was unchanged. |
| `npm run build` | Attempted in an isolated temporary copy of the unchanged site sources and existing build/dependency cache. Failed at MyST preflight: Node 20.19.2 was detected, but npm was reported as `Package Not Found`. Direct `npm --version` returned 11.21.0; the child-process probe returned no version output. No fresh complete HTML export was produced. |
| `npm run check:html` | Attempted against that temporary copy after the failed build; failed on missing generated pages, assets, redirects and subsite configs. Two pre-existing unresolved legacy rows were skipped. This is not a passing fresh HTML check. |

Site checks ran in `/tmp/incerto-v4-site-rtf0akec`, leaving the repository's
existing `_build/` artifact intact. Session logs are
`/tmp/incerto-v4-build.log` and `/tmp/incerto-v4-html-check.log` (not committed).
These results concern this sandbox environment. They do not replace the
successful earlier operator runs or imply an npm package is actually absent.

| Record | In scope | Out of scope | Total retained |
| --- | --- | --- | --- |
| Books | 2 | 5 | 7 |
| Numbered chapters | 53 | 77 | 130 |
| Book source units | 70 | 123 | 193 |
| Concepts | 75 | 28 | 103 |

Additional counts: SCoFT v4 30 chapters / nine appendices; 16 papers;
53 chapter chunks / 55 total chunks; 24 existing concept bodies;
zero checked Lean concepts.

### Operator rerun: v4 chapter-order revision

Completed on 2026-10-17 (America/New_York) outside the sandbox against base
`e7aaa5f` plus this revision's docs/plan changes, after deleting the ignored
`_build/` cache.

| Field | Operator entry |
| --- | --- |
| Date and revision | 2026-10-17; `e7aaa5f` + v4 planning changes |
| `npm ci` | pass |
| `npm run build` | pass |
| `npm run check:html`, page/site/redirect counts | pass: 52 pages across four sites, 48 redirects, 45 pages with display math |
| Pre-existing legacy skips / new findings | 2 pre-existing unresolved legacy url-map rows skipped (28 compatibility pages for 29 mapped rows); no new findings |
| Log or evidence location | operator shell logs on the agent box (not committed) |

### Checks not run and remaining limits

No Python tests, demos, packaging, Lean builds or CI runs: implementation files
were unchanged. No live reader review, browser equation/navigation review,
data acquisition or publication was performed. M0.5 remains unstarted.
Mathematical claim review, precise source hypotheses and empirical provenance
remain chapter work. No program-scope questions remain open; legacy rights,
retention and publishing actions remain with their existing owners.

## Chapter 10 and Appendices F/G (2026-10-29)

[Chapter-10 checkpoint](../../records/incerto-scft-v4-ch10.md) records original
teaching, ten helpers, five new figures and four Amazon/NYC repairs.
`next_chunk` is `scft-v4-ch11`. The chapter chunk is done at teaching/Python
implementation scope; observed S&P evaluation, separate max review and site
gates remain open. The two concepts and attached source units remain
in-progress; synthetic evidence does not close empirical requirements.

- `UV_NO_SYNC=1 uv run pytest`: **1,396 passed, 1 skipped in 216.10 s**.
  Available dependencies; locked installation failed on an uncached wheel.
  The skip is the existing local-data layoffs example. Exact snippet outputs,
  both S&P data branches and fresh-process SVG bytes pass.
- Regenerated 120 snippet outputs and the NYC full demo with the existing
  script. All nine new/changed SVGs inspected as 390/900 px PNGs.
- All 19 affected teaching-page display blocks parse; estimated widths stay
  below 266 px. Browser measurement remains unavailable.
- State/human-view validation and 1,181 plan file/fragment links passed;
  current program bodies 37, frozen M0.5 bodies 24, total concepts 103.
- M05-ISSUE-003 remains resolved. M05-ISSUE-014's rank-position labels and
  captions are fixed and regenerated; two other source-review assignments
  remain open. Snapshot data and third-party source notes are unchanged.
- `npm ci --offline` failed on the uncached MyST archive; scratch build failed
  npm preflight, and the HTML check had no fresh artifact. Chrome launch
  failed on a sandbox socket restriction. No site/browser/live pass claimed.
- No commit, deletion, packaging build, Lean, hub transfer or publication.

## Chapter 11 (2026-10-30)

The [chapter-11 checkpoint](../../records/incerto-scft-v4-ch11.md) records
two new concept pages, the chapter guide, eleven helpers and four original
model figures. Chapter 11 is done at teaching/model/Python scope;
`next_chunk` is `scft-v4-ch12`. Separate max review and publication gates
remain pending. The two concepts retain their later chapter scopes.

- `UV_NO_SYNC=1 uv run pytest`: **1,522 passed, 1 skipped in 239.51 s**.
  This includes exact page outputs, numerical checks, two fresh-process
  exports matching all four SVGs, and graph/integration checks. The skip
  is the existing local-data layoffs example. Tests used available
  dependencies; `uv sync --locked --offline` failed on an uncached wheel.
- Output regeneration executed **128 snippets** across the two concept
  pages, guide and API reference. The snippet tests and regenerator are
  unchanged. Every new package helper has an API anchor and executed example.
- All four figures were rendered to PNG at **390 and 900 px** and inspected.
  All **24** new display blocks parse with KaTeX; the maximum conservative
  width estimate is **287.3 px**. Browser widths remain unverified.
- State/human-view validation and **1,187** plan file/fragment links passed.
  There are **39** existing program concept bodies, 103 retained concepts,
  and zero new checked Lean claims. The generated graph has **48 nodes,
  89 dependency edges and 110 reference edges**.
- M05-ISSUE-006/007 remain open. The new elementary claims are proved at
  their stated scope; this does not close the deferred source audits.
- `npm ci --offline` failed on the uncached MyST archive. A network-blocked
  scratch build with available dependencies failed at MyST's npm preflight;
  the subsequent HTML check found missing artifacts. Chrome failed to launch
  because sandbox socket setup was denied. No fresh HTML/browser/live pass
  is claimed.
- No commit, deletion, packaging build, Lean build, hub transfer or publication.


## Chapter 12 (2026-11-01)

The [chapter-12 checkpoint](../../records/incerto-scft-v4-ch12.md) records
an extension of the point-forecast page, its new guide, five helpers and
three synthetic/model figures. Chapter 12 and the attached selected
mathematical paper scope are done; `next_chunk` is `scft-v4-ch13`.
Separate max review and publication gates remain pending. Lean is skipped.

- `UV_NO_SYNC=1 uv run pytest`: **1,645 passed, 1 skipped in 447.24 s**,
  including exact page outputs, numerical identities and two fresh-process
  exports matching all three SVGs. The skip is the existing local-data
  layoffs example. Available dependencies were used; locked offline Python
  installation failed on an uncached wheel.
- Regenerated **132** snippet outputs with the existing script. Every new
  helper has an API anchor and executed domain/endpoint examples.
- All three figures were inspected as **390/900 px** PNGs. All **25**
  affected display blocks parse with KaTeX 0.19.1; the maximum font-metric
  width estimate is **248.81 px** at 17 px, without browser certification.
- State/human-view validation and **1,195** plan file/fragment links pass;
  530 changed page/record links, citation keys and tracked/new whitespace
  were checked. Program bodies remain 39; concepts 103; new Lean claims zero.
  The graph has **48 nodes, 89 dependency edges, 116 reference edges**.
- M05-ISSUE-006/007 and the frozen review inventory retain their previous
  dispositions. The new source qualifications are recorded for max review.
- Offline scratch `npm ci` passed using the recovered cached MyST archive.
  The fresh scratch build failed MyST's npm version preflight; HTML checks
  found missing artifacts. Chrome launch failed sandbox socket setup.
  No fresh HTML/browser/live pass is claimed.
- No commit, repository file deletion, packaging build, Lean build, hub
  transfer or publication. Chapter-17 fitting and historical pandemic data
  analysis were not started.

## Chapter-13 implementation (2026-11-02)

The [chapter-13 checkpoint](../../records/incerto-scft-v4-ch13.md) records
the final tests, regenerated page outputs, source qualifications and nine
claims for the separate max review. Two new canonical concept bodies and
one guide extend the existing calibration/payoff home. Four risk helpers,
their independent numerical tests and four deterministic figures are added.
The graph has 50 nodes, 92 dependency edges and 123 reference edges.
State records 41 existing program concept bodies and chapter 14 next;
the frozen M0.5 denominator remains 24 and no Lean evidence is added.


Final `UV_NO_SYNC=1 uv run pytest`: **1,757 passed, 5 skipped in 480.37 s**;
the skips need absent local observed-data CSVs. All chapter-13 tests and
page outputs pass. The regenerator executed 151 affected teaching/API
outputs. The focused helper/figure run passed 73 cases after the endpoint
fix. State validation checks 1,204 plan links; the changed-Markdown and
bibliography check passes 1,271 local links. Tracked and new-file whitespace
checks pass. See the checkpoint for environment and command details.

All four figures were inspected as PNGs at 390 and 900 px. KaTeX parsed
41 displays, with a maximum font-metric width estimate of 303.66 px at
17 px; actual browser measurement remains unavailable. The state/human-view
validator passes, including its local file/fragment checks. A normalized
full-book comparison found no matching 8-, 10- or 12-word sequences in
the new pages, calibration extension, helper and producer; manual source
comparison confirms original exposition and explicit qualifications.

Locked offline sync is blocked by an uncached SciPy wheel; Python checks
use the documented available dependencies with `UV_NO_SYNC=1`. Offline npm
installation succeeds, but the fresh MyST build fails its npm preflight.
The HTML checker has no fresh artifacts to inspect, and Chrome launch is
blocked by sandbox socket permissions. These failures leave site/browser
and later live-reader gates open. No commit, deletion, publication, hub
transfer, packaging check or Lean build is part of this chunk.

## Chapter-14 implementation (2026-11-03)

The [chapter-14 checkpoint](../../records/incerto-scft-v4-ch14.md) records
the original forecast-martingale page and guide, four helpers, three
synthetic figures, source qualifications and nine claims for separate
max review. Existing calibration and probability-conflation pages are
linked without duplicating their teaching. State records chapter 14 done
at teaching/Python scope and chapter 15 next, with 42 existing program
concept bodies. The 103 IDs and frozen 24-body M0.5 inventory are unchanged.

The focused numerical/figure suite passes 74 cases after an adjacent-share
rounding fix. The output regenerator executed 142 teaching/API snippets.
The graph has 51 nodes, 93 dependency edges and 124 reference edges.
State/human-view validation, file/fragment links, local citation keys, TOC
membership and tracked/new whitespace checks pass. Final
`UV_NO_SYNC=1 uv run pytest`: **1,855 passed, 5 skipped in 254.66 s**;
the skips need absent local observed-data CSVs.

All three SVGs have visually inspected 390/900 px PNGs and fresh-process
byte comparisons. KaTeX parses 18 new displays; the largest font-metric
estimate is 223.34 px at 17 px, without browser certification. Full-book
8-, 10- and 12-word overlap checks find no matches in the four new authored
teaching/code sources. The chapter citation reuses the existing entry in
the clean `bib/` submodule; no new entry or submodule pointer is needed.

Scratch offline npm installation passes; the MyST build fails its npm
preflight and HTML checks find no fresh artifact. Chromium launch fails
sandbox socket setup. Locked offline Python installation is blocked by
an uncached SciPy wheel; tests use available dependencies with
`UV_NO_SYNC=1`. Separate max review, browser/site and later live reader
review remain open. Lean is skipped-for-now; no commit, repository file
deletion, packaging change, publication or hub transfer.
