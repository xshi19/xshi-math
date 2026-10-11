# Phase 5 cleanup verification

Date: 2026-10-10 (America/New_York).
Owner-selected model: Codex GPT-6-Astra xhigh
Source baseline: `xshi-math` main `3765783`; working branch `codex/phase5-prune`.
Reported deployed hub revision: `2386290`.

Status: **Phase 5 remains incomplete.** Current documentation and the
hub-publish skill are updated, and the machinery audit is complete. The
operator's local build, HTML checks, and redirect tests passed outside the
Codex sandbox. The IG title correction awaits hub republishing. Owner
freeze/archive, two URL-map decisions, and a hub-only asset defect remain open.

## Operator live verification

The operator ran the live checks directly with `curl` on 2026-10-10. These
executed checks supplement the
[Phase 4 live record](phase-4-live-verification.md), whose historical findings
remain unchanged.

| Check | Result |
| --- | --- |
| [Runbook curl script](../plan/phase-4-cutover-runbook.md#verify-the-live-deployment) | Passed: 63 lines of HTTP 200 results covering all mapped legacy URLs, distinct targets, entry pages, and three representative flat math redirects; printed `Live cutover curl checks passed.` |
| `/math/`, `/math/ig/`, `/math/incerto/`, `/math/normix-theory/`, `/math/notation/` | All HTTP 200 |
| `/normix/`, `/incerto-wiki/` | Both HTTP 200 |
| Generated legacy compatibility pages | 28 pages return HTTP 200; root and literal `index.html` share one file (29 mapped CSV rows) |
| Flat math redirects | HTTP 200 for the three sampled by the runbook script, out of 48 generated redirects |
| Live `/math/ig/` title | Still `Information Geometry - Information Geometry` before this PR; the `Introduction` correction is verified locally and requires hub republishing to go live |
| Live legacy hosting | Hub holds the complete old live-site mirror plus 28 compatibility pages; private `incerto-wiki` Pages removed |
| Retained `intro/` and `sp500-tail/` | Both request `/incerto-wiki/build/routes/$-O2KOSX5W.js`, which returns 404; repair belongs in the hub mirror |

All Incerto, IG, and Normix-theory authoring now belongs in `xshi-math`.
Normix package docs at `/normix/` remain upstream. The private Incerto repository
has not been archived; formal freeze/archive is still an owner action.

The no-JS meta-refresh fallback drops incoming query/hash values because its
destination is static. This behavior is **accepted**, not an open implementation
defect. The earlier browser check verified JavaScript forwarding. Live no-JS
testing, the full desktop/mobile and existing-profile cache matrix, upstream
Normix redirects, and every historical automatic fragment remain unverified.

## Changes and retention audit

- Updated [README](../../README.md), [architecture](../../ARCHITECTURE.md),
  [agent router](../../AGENTS.md), [planning index](../plan/index.md),
  [consolidation](../plan/consolidation.md), and the
  [cutover runbook](../plan/phase-4-cutover-runbook.md) to describe the live
  cutover. Historical publication commands remain labeled as completed operator
  reference. Routine publication preserves the full legacy mirror and uses
  generator output for compatibility overlays without `--delete`.
- Changed only the title front matter in [the IG home](../../content/ig/index.md)
  from `Information Geometry` to `Introduction`. The page heading changes too;
  site/project branding, the route, math content, and all other tracks stay the
  same. The built HTML title is `Introduction - Information Geometry`;
  publishing it requires a hub republish.
- The operator applied the prepared patch unchanged with `git apply` to
  [the hub-publish skill](../../.agents/skills/xshi-math-hub-publish/SKILL.md)
  and removed `docs/records/phase-5-hub-publish.patch`. The updated skill
  states the live hosting facts, generator source, legacy retention,
  removed private Pages, and `/normix/` boundary.
- Read all skill definitions/metadata, Cursor adapters, shared rules, scripts,
  and tests. The other skills/rules/adapters contain no pending-cutover claim
  requiring an edit. They remain unchanged.
- Searched `scripts/`, `tests/`, `package.json`, docs, skills, adapters, and root
  guidance for script references and rehearsal machinery. All five scripts
  support the production build or checks: `build_sites.py` calls both redirect
  generators, `site_layout.py` supplies shared routes, and `check_html.py`
  validates the assembled artifacts. The tests still exercise current behavior.
  No production script or test was removed.
- `_build/phase3-rehearsal/` is ignored local staging, still referenced by the
  historical rehearsal record. It was retained; optional disk cleanup should
  follow a check that any needed recovery copies exist elsewhere. Historical
  records and compatibility/rollback artifacts were not pruned.
- `url-map.csv` is byte-for-byte unchanged. `.gitignore` already covers builds,
  Node dependencies, and Python environments; no gap justified an edit.
  `.codex/prompts/` was untracked and not ignored at entry and remains so;
  its files were neither read nor changed.

## Local verification

Toolchain: Node `v20.19.2`, npm `9.2.0`, Python `3.13.5`, installed MyST `1.10.1`.

The operator ran the build, HTML checker, and redirect tests outside the Codex
sandbox on 2026-10-10 and inspected the built IG title.

| Check | Result |
| --- | --- |
| `python3 -m unittest tests/test_legacy_redirects.py` | Passed: all 5 tests, including redirect JavaScript, CSV conflicts/path safety, and checker rejection of corrupt artifacts |
| `npm run build` | Passed: 4 sites assembled, 48 flat redirects, 28 legacy compatibility pages for 29 mapped rows; 2 unresolved rows skipped |
| `npm run check:html` | Passed: 52 pages across four sites, 48 redirects, 28 legacy pages, and 28 distinct targets |
| Built IG title | `_build/html/ig/index.html` contains `<title>Introduction - Information Geometry</title>` |
| Other tracks | All MyST configs and other home sources match `HEAD`; landing, Incerto, and Normix home titles are unchanged |
| URL-map and generator accounting | Unchanged CSV; 29 mapped legacy rows produce 28 pages, with the same 2 unresolved rows; 48 flat math redirects |
| Hub-publish skill | Operator applied the prepared patch unchanged with `git apply`; the skill is updated and the patch file removed |
| Documentation and guidance | Relative paths/anchors, adapter targets, skill names/metadata, stale-status scan, and diff review passed |
| Whitespace | `git diff --check` and a separate check of this untracked record passed |

The fresh assembled HTML and corrected IG title are verified locally. Browser
navigation/equation review was not rerun. The live curl results describe the
deployed baseline, whose IG title still needs the hub republish and a live
recheck. These operator checks were not rerun during this documentation update.
Unchanged numerical code did not require a Python packaging/demo/pytest rerun.

## Gate status and remaining work

| Phase 5 requirement | Status |
| --- | --- |
| Publication evidence recorded | Met by the operator's direct 2026-10-10 curl checks and Phase 4 record |
| Compatibility and rollback artifacts retained | Met within this task: no pruning or hub writes; preservation is explicit in current guidance |
| Remove obsolete/duplicate build paths | Audit complete; no unreferenced rehearsal-only machinery or duplicate production path found |
| Current guidance has canonical owners | Met locally: docs/router corrected, existing thin adapters retained, and hub-publish skill updated by the operator |
| Live URL defects and retained-route disposition settled | Open: two owner decisions and the hub asset 404 below |
| Owner freeze/archive after cutover | Open: Pages removal is complete, but it is not a repository archive or recorded authoring freeze |
| Verify this source change before publication | Met locally: build, HTML checker, all 5 redirect tests, and built IG title passed; browser review limits are recorded above |
| Publish the IG title correction | Open: hub republish and live title recheck required; the deployed title still reads `Information Geometry - Information Geometry` |

To close the remaining work:

1. The owner confirms the private `incerto-wiki` authoring freeze, confirms
   obsolete publishers stay disabled, and archives that repository while
   retaining private provenance and recovery history.
2. The owner resolves `incerto-scoft-intro` (`/incerto-wiki/intro/`, SCoFT
   rights review) and `hub-incerto-home-export`
   (`/incerto-wiki/build/index-995d9205321c1213987db72d01de44bf.md`, download
   treatment/rights). Preserve both retained artifacts until those decisions.
3. Repair `/incerto-wiki/build/routes/$-O2KOSX5W.js` in the hub and recheck the
   retained `intro/` and `sp500-tail/` pages. This repo does not own that asset.
4. Complete the rendered title/navigation review, republish the checked artifact
   through a separately authorized hub publication, and verify the live IG title
   is `Introduction - Information Geometry`.

No commit, push, Git configuration change, sibling-repository edit, Pages
operation, authoring freeze, or archive was performed in this task.
