# Design verification

Date: 2026-10-16. Baseline: `998a4a11a17b7ae7ba4c306005a4c8e3109f4392`,
branch `plan/incerto-program`.

## Changed artifacts

The new directory contains `README.md`, `inventory.md`, `concepts.md`,
`architecture.md`, `templates.md`, `sources.md`, `state.yaml`, `validation.md`
and this record. `docs/plan/index.md` gains one reading-map link. All tracked
changes are confined to `docs/plan/`. No implementation, configuration, public
page, URL-map row, proof or dataset was changed. No files were deleted and no
commit, push or publication was performed.

## Results

| Check | Result |
| --- | --- |
| Required repository survey | Read the router, README/architecture, rule and design documents, requested plans/configuration/scripts, applicable skills and Incerto guidance; surveyed all existing Incerto bodies and the numerical example. |
| Source metadata | Checked the publisher/catalog edition and contents records and versioned arXiv metadata. Direct source-content review remains explicitly pending; see `sources.md`. |
| State validation | The executable block in `validation.md` passed: unique keys, IDs, role/status/classification references, acyclic concept/chunk/milestone graphs, source mappings, page conventions, existing paths and derived counts. |
| Counts | 7 books; 125 numbered chapters; 187 book source units; 14 papers; 101 unique concepts; 24 existing concept pages; 0 checked Lean concepts. |
| Human-view consistency | Checked every concept ID, home and classification justification against state, and every chapter row against its locator and concept mapping. |
| Local documentation checks | Relative links, explicit concept anchors, new-file whitespace and `git diff --check` passed. Reviewed the new Markdown and parsed all state records; untracked files were included. |
| MyST inclusion | The new plan directory is outside all four explicit TOCs and the track page globs; the design adds no rendered page. Configurations and scripts are unchanged. |
| `npm ci --cache /tmp/xshi-incerto-npm-cache --fetch-retries=0 --fetch-timeout=15000` | Failed with `EAI_AGAIN`: DNS lookup for `registry.npmjs.org` failed while fetching `mystmd-1.10.1.tgz`. This was a network/DNS failure, not `EPERM`. |
| `npm run build` | Attempted; failed with `FileNotFoundError` for `node_modules/.bin/myst` after dependency installation failed. No complete HTML export was produced. |
| `npm run check:html` | Attempted; failed on absent generated pages, configuration, search/sitemap data and redirects. This does not constitute a passing site check. |

## Checks not performed and remaining limits

Python tests, demos and packaging were not rerun: this change affects planning
documents only. Lean setup/build was not run and remains outside this task.
CI, rendered equations, desktop/mobile navigation and live publication were
not verified. No empirical data was downloaded and no source theorem was
certified by this design.

In an environment with working dependency access, run `npm ci`,
`npm run build`, then `npm run check:html`. The strict build may also need
network for MyST theme or DOI retrieval. Do not describe this design's site
build as verified until that run succeeds. No workaround that changes the
site, dependencies or legacy routes was introduced to bypass this sandbox.

Before implementation, reconcile the expanded Procrustes and 2025 Technical
Incerto editions, inspect exact primary-source claim locators, and follow the
selected chunk's scope/owner-confirmation requirements. The design is complete
as a proposal; its mathematical and empirical program remains `todo`.
