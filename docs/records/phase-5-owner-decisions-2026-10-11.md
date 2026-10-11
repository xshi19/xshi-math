# Phase 5 owner decisions — 2026-10-11

Xiang settled the two legacy URL-map decisions on 2026-10-11. This record
supersedes their pending status in the historical
[Phase 5 verification record](phase-5-verification.md); its other findings and
verification limits remain unchanged.

| URL-map source ID | Owner decision | Recorded treatment |
| --- | --- | --- |
| `hub-incerto-home-export` | Delete the stale `/incerto-wiki/build/index-995d9205321c1213987db72d01de44bf.md` hub build leftover. | Keep the audit row, marked `deleted 2026-10-11 by owner decision`, with an empty target and no compatibility page. The hub deletion is handled separately; this task does not perform or verify it. |
| `incerto-scoft-intro` | Retain `/incerto-wiki/intro/` as is, with no compatibility page. | Set `decided: retain` with the decision date, keep `new_url` empty, and continue skipping the row during generation. |

The [URL map](../plan/url-map.csv) still contains 31 legacy rows: 29 mapped rows
produce 28 compatibility pages pointing to 28 distinct built pages. Two
owner-decided rows are skipped; no legacy URL-map decisions remain unresolved.
The generator and HTML checker now describe those rows as skipped with recorded
reasons. Empty-target handling and redirect generation are unchanged.

Retaining the legacy intro page does not approve a SCoFT source import or settle
its deferred rights review. The [migration manifest](../plan/migration-manifest.csv)
and earlier verification records remain unchanged. The owner freeze/archive,
hub asset repair, and IG title publication follow-ups remain in the
[planning index](../plan/index.md) and
[consolidation plan](../plan/consolidation.md#one-time-consolidation-phases).

## Verification

Toolchain: Node `v20.19.2`, npm `9.2.0`, Python `3.13.5`, MyST `1.10.1`.

| Check | Result |
| --- | --- |
| `npm run build` | Blocked before rendering: the sandbox denies Node's npm-version subprocess with `EPERM`; MyST reports npm as `Package Not Found`, although direct `npm --version` succeeds. |
| `npm run check:html` | Passed against restored reference HTML: 52 pages, 48 flat redirects, 45 pages with display math, 28 legacy compatibility pages and 28 distinct targets. This is not a fresh-build pass. |
| `python3 -m unittest discover -s tests` | Passed: 5 redirect tests in the temporary test environment described below. |
| `python3 -m pytest tests/test_xmath.py` | Passed: 6 numerical/import tests in that temporary environment; unittest discovery does not execute these pytest functions. |
| Redirect-output comparison | All 28 regenerated legacy files match the pre-edit renderings byte-for-byte by SHA-256. Neither skipped route produces a file. |
| CSV and documentation | Both dated dispositions retain empty targets; CSV structure, relative links/anchors, diff review, and tracked/new-file whitespace checks passed. |

The failed build cleared `_build/html/`. For the limited HTML check, it was
restored from the retained `_build/phase3-rehearsal/math/` snapshot and matching
cached book-theme assets, then the current legacy generator was run. The
reference output is identified in `_build/cleanup-reference-verification.txt`;
it is not a fresh export of current source and must not be published. Build and
reference-check logs are `/tmp/xshi-math-cleanup-build.log` and
`/tmp/xshi-math-cleanup-html-reference.log`.

The initial system-Python discovery failed because `pytest` was absent.
`uv sync --locked` then failed on dependency-download DNS resolution. Tests
instead used `/tmp/xshi-math-cleanup-test-env`, with cached pytest `9.1.1` and
NumPy `2.5.3`; its site-packages `xmath` symlink points to this repo's `src/math/`
according to the declared package mapping. No `src/` path was added to
`PYTHONPATH`. Locked-environment setup and package installation were not verified;
dependency manifests and lockfiles remain unchanged.

The requested fresh-build gate remains blocked by the sandbox. Browser and live
URL checks were not run. No hub files, Git history, or publication settings were
changed; the pre-existing untracked `.codex/prompts/` directory was left alone.
