# Phase 0–1 Verification

Date: 2026-09-13 (updated after HTML gate).
Scope: representative inventory and original minimal foundation; no migration,
hub write, or deployment.

## Result

Phase 0 light inventory and Phase 1 foundation (Python package + six-page MyST
site under `BASE_URL=/math`) are **complete locally**. `npm run check:html`
passed against the built artifact. No hub cutover and no CI workflow yet.

## Checks performed

Environment: Python 3.13.5, uv 0.12.5, Node.js 20.19.2, npm 9.2.0, mystmd 1.10.1.

| Check | Observed result |
| --- | --- |
| `uv sync` / `uv run pytest` / demo / wheel / `xmath` import isolation | Passed earlier in Phase 1 scaffold |
| `npm install` (mystmd 1.10.1) | Passed |
| `BASE_URL=/math myst build --html --strict --ci` | Passed; six pages under `_build/html/` |
| Stable page paths (unique Markdown stems; MyST ignores `slug:`) | `index`, `incerto`, `incerto-counting-exceedances`, `information-geometry`, `normix-theory`, `normix-conditioning-a-mixture` |
| `npm run check:html` | Passed: six pages, local links, `/math` prefix, sample KaTeX, shared `math.css` |

Build command:

```sh
BASE_URL=/math myst build --html --strict --ci
```

(`package.json` `npm run build` uses the same flags.) Multiple nested `index.md`
files previously collapsed to `index-N/` URLs; content is flattened to unique
filenames so routes match the checker and planned `/math/` map.

## Still open (later phases)

- Public-host browser review under `/math/`; local desktop/mobile review of the
  expanded site is recorded with the [IG entry batch](ig-entry-verification.md).
- Pin / record book-theme revision used at publish time.
- Hub assembly into `xshi19.github.io/math/` and cutover.
- Incerto / Normix theory migration and later IG marginalization / GH research
  pages beyond the implemented first entry batch.
- Lean and CI workflows.

## Information Geometry note

Owner curriculum draft and ChatGPT share extract live under `docs/plan/`.
The [polished outline](../plan/ig-entry-outline.md) and six original `content/`
entry notes are now implemented following the owner's authorization. This
record retains the original six-page foundation results; the expanded twelve-page
artifact has its own [verification record](ig-entry-verification.md).
