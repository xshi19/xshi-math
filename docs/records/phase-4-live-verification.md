# Phase 4 live cutover verification

Date: 2026-10-10 (America/New_York).
Revisions: `xshi-math` `fd9406d` + docs #20 `49481f7`; hub `2386290`.
Owner-selected model: Codex GPT-6-Astra xhigh.

Status: Phase 4 cutover is live. The `incerto-wiki` repository's own Pages was
removed. The hub serves `/incerto-wiki/` as a full mirror of the old live site
plus 28 compatibility pages. See the
[preparation record](phase-4-cutover-prep-verification.md) for the build gate and
the [planning index](../plan/index.md) for Phase 5 follow-ups.

## Live findings

These are the operator-reported checks from 2026-10-10. Curl covered 26
`/incerto-wiki/` routes, with targets returning HTTP 200, plus a browser check.
This is batch coverage, not a separate curl result for every URL-map row.

| Check | Result |
| --- | --- |
| Compatibility pages | 28 live; root and literal `index.html` share one file |
| JavaScript redirect | Query string and hash preserved in the browser test |
| Meta-refresh fallback | Drops query/hash; clients without JavaScript were not tested live |
| Kept `intro/` and `sp500-tail/` pages | Render fine; both request `/incerto-wiki/build/routes/$-O2KOSX5W.js`, which returns 404 |
| Service worker | No service worker registered in the browser check |
| Cache header | `Cache-Control: max-age=600` observed |
| `/math/ig/information-geometry-euclidean-to-manifold/` | 448 formulas, 0 errors |

## Remaining work

The `incerto-wiki` authoring freeze/archive remains an owner action. Phase 5
remains unchecked; candidates include the kept-page asset 404 and the no-JS
fallback. The URL-map rows `incerto-scoft-intro` and `hub-incerto-home-export`
remain unresolved. These checks do not verify upstream Normix redirects or
every historical fragment.

## Docs-only validation

`python3 -m unittest tests/test_legacy_redirects.py` passed all five tests.
The pytest invocation could not run because `pytest` is unavailable. CSV checks
confirmed that only `verification_status` changed and both unresolved rows are
unchanged; local documentation links and whitespace checks passed. Live
curl/browser checks and a site build were not rerun for this closeout.
