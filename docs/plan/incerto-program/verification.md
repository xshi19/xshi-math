# Design verification

Baseline: 2026-10-16, revision `998a4a11a17b7ae7ba4c306005a4c8e3109f4392`.
Owner revision: 2026-10-17, branch `plan/incerto-program`, PR #24.

## Changed artifacts

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

## This revision: local checks

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

Counts now distinguish completion scope from retained references:

| Record | In scope | Out of scope | Total retained |
| --- | --- | --- | --- |
| Books | 2 | 5 | 7 |
| Numbered chapters | 48 | 77 | 125 |
| Book source units | 64 | 123 | 187 |
| Concepts | 72 | 29 | 101 |

There are 14 starting paper records, 24 existing concept bodies and zero
checked Lean concepts. Required 2025 Technical Incerto additions await exact
reconciliation and are not counted as mapped units yet.

## Operator record: outside-sandbox rerun for this revision

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

## Checks not performed and remaining limits

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
