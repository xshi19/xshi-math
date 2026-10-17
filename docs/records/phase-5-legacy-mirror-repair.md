# Retained legacy mirror repair

Date: 2026-10-17. Live verification: **pending hub publish**.

## Cause and owner decision

The frozen hub mirror contains 23 retained MyST route pages built against
`build/manifest-C732C875.js`. Their module preloads and inline module imports
request `/incerto-wiki/build/routes/$-O2KOSX5W.js`, which is absent from the
mirror. The owner also verified its absence in the 2026-10-10 live snapshot.
The server-rendered content and KaTeX markup survive the failed hydration.

The owner chose static retained pages at the same URLs. In particular, `intro/`
remains retained with no compatibility page; this repair adds no mappings or
redirects. The 28 compatibility paths remain owned by
[`write_legacy_incerto.py`](../../scripts/write_legacy_incerto.py).

[`repair_legacy_mirror.py`](../../scripts/repair_legacy_mirror.py) scans the
mirror and stages affected HTML separately. It removes module preloads, module
scripts, the Remix context assignment, and Remix scroll restoration. It inserts
`<meta name="xshi-math-legacy" content="static-retained">` and preserves every
other byte, including visible text, styles, and non-Remix scripts. Marked pages
are rechecked on subsequent runs. Healthy retained pages are not emitted.

Missing navigation targets and the two exact pre-existing graph-asset gaps
below are warnings. Other missing assets that runtime removal cannot fix are
errors: the scan writes no overlay if any page fails. Literal local references
in HTML attributes and inline module imports are checked;
this does not execute scripts or recursively inspect CSS and JS dependencies.
Unexpanded Sphinx template references are reported separately as warnings.

## Operator procedure

Use a fresh hub clone and preserve the rollback artifacts required by the
[cutover runbook](../plan/phase-4-cutover-runbook.md). After generating the
compatibility pages, run from this repository, adjusting the hub checkout path:

```bash
set -e
python3 scripts/repair_legacy_mirror.py --mirror /workspace/xshi19.github.io/incerto-wiki
rsync -a _build/legacy/incerto-wiki/ /workspace/xshi19.github.io/incerto-wiki/
rsync -a _build/legacy/retained-repair/incerto-wiki/ /workspace/xshi19.github.io/incerto-wiki/
python3 scripts/repair_legacy_mirror.py --mirror /workspace/xshi19.github.io/incerto-wiki --check
```

Both overlays copy only generated HTML paths; neither uses `--delete`.
`--out` can select another dedicated output directory. A successful repair run
refreshes its generated output, removing stale repairs; unrelated files and
output paths overlapping the input mirror are rejected. `--check` writes
nothing and exits 1 for needed repairs or asset errors; known gaps alone do not
fail it. Stop on errors and review warnings before a separate hub commit and
publish.

Static pages retain ordinary links and SSR layout. Controls that depended on
Remix hydration, including client search and navigation toggles, are inactive.
No replacement interactive behavior is introduced.

## Local verification

Input: `/workspace/incerto-archive-202610171146/hub/incerto-wiki`, from clean hub
commit `49c6198a6b0dd928d474d580c573ff30842ac6ee`. Authoring checkout started at
`998a4a1` on `codex/legacy-mirror-static-repair`.

| Check | Result |
| --- | --- |
| Mirror scan | 68 HTML files; 28 compatibility paths skipped; 23 pages need repair |
| Normal CLI, default output | Exit 0; 23 repaired pages emitted to `_build/legacy/retained-repair/incerto-wiki/`; two `KNOWN GAP` warnings |
| Original-mirror `--check` | Exit 1 for 23 needed repairs; no asset errors |
| Temporary mirror with full repair overlay | Exactly 23 HTML files changed; `--check` exits 0, verifies all 23, reports zero needed repairs and two known gaps; copy removed afterwards |
| Original mirror preservation | SHA-256 inventory of all 1,860 files unchanged |
| `python3 -m unittest discover -s tests -p 'test_legacy*.py' -v` | 25 pass: 20 synthetic repair tests and 5 existing redirect tests; includes exact-pair matching, unknown-asset rejection, and stale allowances |
| Diff, new-file whitespace, Python syntax, documentation links, proposed skill patch applicability | Passed |
| Browser rendering and live verification | Not run; pending hub publish |

Full Python/site checks were not rerun in this follow-up. Earlier dependency
installs failed on DNS resolution for PyPI and npm; full test discovery lacked
`pytest`, the build lacked MyST, and the HTML checker lacked built artifacts.

The 23 affected routes are `amazon-bookrank/`, `api-reference/`, `ch3/`, `ch4/`,
`ch5/`, `ch6/`, `ch7/`, `chinese-entry/`, `dependency-dag/`, `dispersion-ratio/`,
`embrechts-modelling-extremal-events/`, `empirical-example-concepts/`, `index-2/`,
`index-3/`, `intro/`, `lean-blueprint/`, `lln-preasymptotic/`, `normal-mixture/`,
`nyc-dog-name-tail/`, `releases/`, `sp500-tail/`, `v0-1-0/`, and `variance-gamma/`.

## Known pre-existing gaps

The operator confirmed that these two assets were already absent from the
2026-10-10 live snapshot and return 404 live:

| Referring file | Missing asset, relative to `incerto-wiki/` |
| --- | --- |
| `build/concept-list-7ef20491bebc3cb4a7d50502026374c8.html` | `css/concept-graph.css` |
| `dependency-dag/index.html` (iframe) | `assets/graphs/concept-graph.html` |

The [migration manifest](../plan/migration-manifest.csv) defers the DAG and its
graph assets in rows `incerto-dependency-dag` and `incerto-graph-assets`. The
runbook forbids copying private source into the hub, so neither asset is
restored here. The dependency-dag iframe remains a known 404 pending the
deferred DAG decision; its referring HTML is preserved.

`KNOWN_MISSING_ASSETS` allows only these exact (referring file, asset) pairs and
records the manifest reasons. Missing matches produce `KNOWN GAP` warnings;
an asset that now exists produces a `STALE ALLOWANCE` warning for review.
Other missing non-runtime assets still fail the scan. The successful check
reports 29 warnings: these two gaps, 20 missing API navigation references, and
7 unexpanded Sphinx template references.

The operator will apply `_build/legacy/hub-publish-skill.patch` and commit the
three untracked source/record files. The patch now documents known-gap and
stale-allowance warnings. `.agents/`, `.git/`, and the hub clone were not modified
in this follow-up; no commit, push, or hub publish was attempted.
