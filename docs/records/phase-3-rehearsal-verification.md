# Phase 3 local publication rehearsal verification

Date: 2026-10-02 (America/New_York).
Base: `origin/main` at `b1a1a319bfabe99dcdc15086c394b6abfb547edc`;
branch `docs/phase2-closeout-phase3-rehearsal`.
Owner-selected model: Codex GPT-6-Astra xhigh (Codex did Phase 2 docs and the
first rehearsal attempt; babysitter completed the fresh build after restoring
registry access and the book-theme template).

Status: Phase 2 eligible preparation is accounted for. Phase 3 **local** exit
gate is met: fresh `npm ci`, strict multi-subsite `npm run build`, and
`npm run check:html` pass; `_build/phase3-rehearsal/` mirrors hub layout with
`math/` beside copied `normix/` and `incerto-wiki/`; mapped flat `/math/`
redirects and representative track URLs resolve under a local HTTP server.
Live Pages, full desktop/mobile browser matrix, and combined hub publication
rollback were **not** run. Phase 4 public cutover still requires Xiang's
explicit go-ahead. The hub clone was left untouched (no commit/push).

## Phase 2 closeout

The [migration manifest](../plan/migration-manifest.csv) now contains 55 rows:
41 `imported`, six `stay`, three `exclude`, and five `deferred`. No disposition
remains `adapt`; every row has a reason.

- `incerto-home` is accounted as imported by the original adapted foundation
  entry at `content/incerto/index.md`. No wiki-home body was copied.
- `incerto-notation` is accounted as imported by the existing shared canon at
  `content/notation.md`, published at `/math/notation/`. No second table was added.
- `incerto-scoft-intro` is deferred for rights review, with no target path.
  No SCoFT chapter or book content was imported.
- Residual rows record empirical examples and their index (deferred),
  dependency-DAG navigation and graph assets (deferred), the two excluded
  Incerto mixture/VG duplicates (point to existing Normix imports), and five
  named finance-theory pages staying upstream.
- `normix-api` remains `stay`; `hub-incerto-home-export` remains `exclude`.

The residual scope comes from [Incerto Batch 3](../plan/phase-2-incerto-batch-3.md)
and [Normix Theory Batch 2](../plan/phase-2-normix-theory-batch-2.md). No new
mathematical pages were invented or imported in this change. Third-party
rights are not treated as cleared by the owner's MIT decision.

## Commands and results (fresh local gate)

Environment: Node.js 20.19.2, npm 9.2.0, Python 3.13.5. Lockfile pins MyST CLI
1.10.1. Dependency manifests and lockfile were not changed.

| Check | Result |
| --- | --- |
| First `npm ci` (Codex attempt) | Failed with `EAI_AGAIN` resolving `registry.npmjs.org` |
| Retry `npm ci` | Passed (MyST 1.10.1 available) |
| Book-theme template | Incomplete nested extract blocked the first retry build (`build/**/*` missing). Restored by flattening `incerto-wiki/_build/templates/site/myst/book-theme/template.zip` into `_build/templates/site/myst/book-theme/` and running `npm ci --ignore-scripts` in that directory. Theme files remain local build cache (gitignored), not committed |
| `npm run build` | Passed: landing, Incerto, IG, and Normix theory with `--html --strict --ci`; assembled `_build/html/` and wrote 48 flat redirects |
| `npm run check:html` | Passed: 52 pages, 48 redirects, 45 pages with display math; branding/TOCs/search/sitemaps/nested prefixes/shared CSS |
| Local staging | `rm -rf` + `cp -r` of `_build/html` → `_build/phase3-rehearsal/math/`, plus hub working-tree `normix/` and `incerto-wiki/` beside it (no rsync; no hub write) |
| Flat `/math/` redirects | All 48 redirects from `scripts/site_layout.py` present with expected destinations |
| URL-map math destinations | 100 representative old/new `/math/` paths from `url-map.csv` resolve to staged HTML (including homes, notation, track notes, and flat legacy paths) |
| Local HTTP preview | `python3 -m http.server` on staging root returned 200 for `/math/`, `/math/incerto/`, `/math/ig/`, `/math/normix-theory/`, `/math/notation/`, `/math/incerto-pareto/`, `/normix/`, `/incerto-wiki/` |
| Sibling preservation | `normix/` and `incerto-wiki/` remain as separate staging prefixes; math copy did not overwrite them |
| Hub repository | HEAD unchanged at `d15dfbc`. Clone was already dirty (~5,982 unstaged deletions under `incerto-wiki/` and `math/`); no hub files were written, staged, committed, or pushed |

Audit artifacts under ignored `_build/phase3-audit/` include earlier failure
logs and `staging-results-retry.json` from the successful pass.

## Staging layout

```sh
rm -rf _build/phase3-rehearsal
mkdir -p _build/phase3-rehearsal
cp -r _build/html _build/phase3-rehearsal/math
cp -r /workspace/xshi19.github.io/normix _build/phase3-rehearsal/normix
cp -r /workspace/xshi19.github.io/incerto-wiki _build/phase3-rehearsal/incerto-wiki
```

Staging root: `/workspace/xshi-math/_build/phase3-rehearsal/`.
As the [subsite split record](subsite-split-verification.md#compatibility-routes)
states, the math build does **not** implement `/incerto-wiki/` → `/math/...`
compatibility cutover redirects. This local rehearsal covers the math artifact,
flat `/math/` routes, and sibling preservation only.

Representative fragments verified earlier on destination HTML (CSV fragment
cells are empty; these are content-id spot checks):

| Destination path | Verified fragment |
| --- | --- |
| `/math/incerto/incerto-pareto/` | `#pareto-definition` |
| `/math/incerto/incerto-regular-variation/` | `#regular-variation-definition` |
| `/math/ig/information-geometry-fisher-vs-l2/` | `#ig-fisher-information` |
| `/math/ig/information-geometry-latent-variables-em/` | `#ig-em-monotonicity` |
| `/math/normix-theory/normix-varentropy/` | `#ve-r` |
| `/math/normix-theory/normix-factor-analysis/` | `#fa-mstep` |
| `/math/notation/` | `#probability-and-expectation` |

## Checks not run and remaining gates

Not run in this rehearsal:

- Live GitHub Pages fetch or deployment
- Full desktop/mobile Playwright browser matrix (historical coverage remains in
  the [subsite split record](subsite-split-verification.md); not rerun here)
- Combined hub publication rollback (discarding local staging only)
- `/incerto-wiki/` → `/math/...` cutover compatibility pages
- Python package tests/demos (docs-only change)

Rollback for this attempt is discarding
`/workspace/xshi-math/_build/phase3-rehearsal/`; no hub deployment needs
reverting. Phase 4 still needs Xiang's explicit go-ahead after any remaining
cutover-route and browser checks he wants. Phase 5 live verification remains
pending. No secrets, SCoFT dumps, force-push, merge, or hub push were performed.
