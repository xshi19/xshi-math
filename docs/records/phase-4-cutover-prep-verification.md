# Phase 4 cutover preparation verification

Date: 2026-10-07 (America/New_York).
Branch: `codex/phase4-cutover`; base/unchanged HEAD:
`5db7eb78bf9b09a902f8c8bbd12f4a6eedd9fb6e`.
Owner-selected model: Codex GPT-6-Astra xhigh.

Status: compatibility code, checks, and runbook prepared for review. **The fresh
build and `check:html` gate passed on 2026-10-07.** The operator ran both commands
outside the sandbox at approximately 18:50 EDT on this exact working tree.
Phase 4 remains unchecked; the owner publication gates in the
[runbook](../plan/phase-4-cutover-runbook.md) remain open.

## Scope and counts

| Item | Result |
| --- | --- |
| Legacy CSV rows | 31 under the public `/incerto-wiki/` prefix |
| Mapped rows | 29, producing 28 compatibility files; root and literal `index.html` share one file |
| Destinations checked | 28 distinct built pages; includes normalized `/math/notation/` for `index-1/` |
| Skipped/unresolved rows | 2, printed with reasons by both generation and checking |
| Fragment columns | All empty in current legacy rows; translation and default-fragment behavior tested with synthetic CSV rows |
| Committed hub inventory | 1,755 files, including 55 HTML files; 37 HTML files absent from the CSV, listed in the runbook |
| Proposed overlay at inspected hub revision | Replace 17 existing HTML files, add 11, retain 38 (37 gaps plus `intro/`); preserve all other legacy files |

The skipped rows are `intro/` (reading-guide rights review deferred; the old
proposed target was never built) and
`build/index-995d9205321c1213987db72d01de44bf.md` (empty target; unresolved
download treatment). The CSV clears only the stale intro destination; it creates
no replacement target and leaves the migration manifest's dispositions intact.

The checker now requires every mapped legacy file, noindex, agreement among
refresh/canonical/visible links, the correct JavaScript mapping, and a real
destination page with any explicitly mapped fragment. Missing targets,
conflicting aliases, unsupported fragment-only mappings, and unexpected
compatibility HTML fail. Query and unknown-hash preservation are tested by
executing the emitted JavaScript in Node.

## Commands and results

Preparation environment: Node.js 20.19.2, npm 9.2.0, Python 3.13.5; pinned MyST
CLI 1.10.1. Dependency manifests and lockfiles are unchanged. The operator's
successful rerun used Node.js v20.19.2; logs are `/tmp/phase4-build.log` and
`/tmp/phase4-check.log`. Earlier sandbox logs and artifact provenance remain
in the local, ignored `_build/phase4-audit/` directory.

| Command/check | Result |
| --- | --- |
| Earlier sandbox `npm ci` | Failed: `EAI_AGAIN` resolving `registry.npmjs.org` |
| `npm ci --offline --cache _build/npm-cache` | Passed: installed the pinned CLI from the retained rehearsal cache |
| `npm run build` (operator, 2026-10-07) | Passed, exit 0: fresh MyST render of all four sites; 48 flat redirects; 28 legacy compatibility pages for 29 mapped rows, with 2 unresolved rows skipped |
| `UV_CACHE_DIR=.../_build/uv-cache uv run pytest` | Blocked: dependency download DNS failure at `files.pythonhosted.org` (`pygments`); the full Python suite did not execute |
| `python3 -m unittest tests/test_legacy_redirects.py` (operator, 2026-10-07) | Passed: 5 focused tests, including Node execution of redirect JS, fallback/fragment handling, escaping, conflicting aliases, path safety, stale output removal, and checker rejection of damaged/missing files and destinations |
| `npm run check:html` (operator, 2026-10-07) | Passed, exit 0: 52 pages across four sites, 48 flat redirects, 45 pages with display math, independent branding/TOCs/search/sitemaps/local links/assets/fragments/shared CSS; 28 legacy pages and 28 distinct targets |
| Diff, new-file whitespace, local documentation links, and runbook syntax | Passed; generated output remains ignored |

Earlier sandbox build attempts failed before rendering with child-process
`EPERM`, an environment limitation. A temporary check used restored Phase 3
HTML and cached theme assets; the operator's fresh build and check above
supersede that result. The pre-existing `tests/test_xmath.py` still needs pytest,
unavailable offline; this is unrelated to the fresh HTML gate.

## Read-only evidence and remaining gates

The hub audit used `git -C /workspace/xshi19.github.io ls-tree -r --name-only HEAD
incerto-wiki/` at `1511d5e358cc8040327e5a4df33d30ac3983fcef`. It did not inspect
deleted working-tree files as route evidence. The private source plan was read
at `0bb63beb029947bae3aa39e8ff067da8866a9ef7`; its PR #54 priorities are recorded
as future `xshi-math` work in the consolidation plan. Neither neighboring
repository was modified. Mathematical sources under `content/` and untracked
`.codex/prompts/` were left untouched.

Not run: live curl checks, full browser/mobile review, hub transfer, live
rollback, source authoring freeze, or private-repo
archive. No source commit, push, PR, merge, or deployment was performed. Phase 4
remains unchecked, with Xiang's 2026-10-07 preparation approval recorded.

Xiang still needs to confirm merge, the effective Pages publisher and
serialization, and the proposed retention of the two unresolved rows and 37
unmapped HTML files. Archive remains an owner action after live verification
and the Incerto authoring freeze; Phase 5 follows.
