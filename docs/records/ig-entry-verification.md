# Information Geometry entry verification

Date: 2026-09-13.
Scope: the original IG outline, hub, and six Basics / early IG notes; local site
validation under `/math/`. No content migration or deployment.

## Result

The twelve-page artifact builds with MyST CLI 1.10.1 and
`BASE_URL=/math`. `npm run check:html` passes for all twelve routes, including
local links, assets, fragments, shared CSS, rendered display math, and KaTeX
error checks. The Phase 1 local HTML prerequisite is complete, and the
[IG outline](../plan/ig-entry-outline.md) and first entry batch are implemented.

Desktop and mobile browser checks pass on the locally served static artifact.
Later marginalization, geometric EM, and GH/Normix research pages remain
proposals in the outline.

## Files in this change

The [IG hub](../../content/ig/index.md) now links these six new
pages, all flat under `content/`:

| Source | Route below `/math/` |
| --- | --- |
| [information-geometry-euclidean-to-manifold.md](../../content/information-geometry-euclidean-to-manifold.md) | `information-geometry-euclidean-to-manifold/` |
| [information-geometry-exponential-families.md](../../content/information-geometry-exponential-families.md) | `information-geometry-exponential-families/` |
| [information-geometry-latent-variables-em.md](../../content/information-geometry-latent-variables-em.md) | `information-geometry-latent-variables-em/` |
| [information-geometry-conditional-expectation.md](../../content/information-geometry-conditional-expectation.md) | `information-geometry-conditional-expectation/` |
| [information-geometry-fisher-vs-l2.md](../../content/information-geometry-fisher-vs-l2.md) | `information-geometry-fisher-vs-l2/` |
| [information-geometry-duality.md](../../content/information-geometry-duality.md) | `information-geometry-duality/` |

Supporting changes:

- [content/index.md](../../content/index.md) and [myst.yml](../../myst.yml):
  entry links and six TOC children beneath the IG hub.
- [scripts/check_html.py](../../scripts/check_html.py): the twelve expected
  pages, actual KaTeX element detection, error markers, and local fragment checks.
- [assets/styles/math.css](../../assets/styles/math.css): mobile heading
  permalinks occupy layout space, fixing a 9–12 px viewport overflow found in
  two IG notes and the existing exceedance example.
- [ig-entry-outline.md](../plan/ig-entry-outline.md): the new curriculum and
  explicit boundary between this batch and later research.
- [Planning index](../plan/index.md), [curriculum draft](../plan/ig-entry-curriculum-draft.md),
  and [consolidation plan](../plan/consolidation.md): completed prerequisites,
  supplied owner input, and unique flat filenames.
- [README](../../README.md), [architecture](../../ARCHITECTURE.md),
  [agent router](../../AGENTS.md), [framework](../design/AGENT_FRAMEWORK.md),
  and [foundation record](phase-0-1-verification.md): current status and pointers
  to this record, preserving the original foundation results.
- This verification record is new. `package.json` already supplies the required
  base path and build flags; the npm manifest and lockfile are unchanged.

## Executed checks

Environment: Node.js 20.19.2, npm 9.2.0, Python 3.13.5, MyST CLI 1.10.1.
Browser inspection used Chrome 151.0.7922.169 and a temporary Playwright Core
1.63.0 installation outside the repository.

| Check | Observed result |
| --- | --- |
| `npm ci` | Passed using the committed npm lockfile |
| Foundation build and checker before adding pages | Passed for the original six routes under `/math/` |
| `npm run build` after the content and CSS changes | Passed; `BASE_URL=/math myst build --html --strict --ci` exported twelve pages |
| `npm run check:html` on the final build | Passed for twelve pages, local links/assets/fragments, prefix, shared CSS, and rendered math |
| TOC and output route audit | Twelve existing flat sources with unique stems match `PAGES` in order; twelve HTML routes, with no `index-N/` routes |
| Desktop browser, 1440 × 1000 | All twelve pages load; IG navigation, equations, and representative screenshots reviewed |
| Mobile browser, 390 × 844 | All twelve pages load with no page-wide horizontal overflow after the permalink fix; IG drawer shows all six children |
| Navigation at both widths | Clicking an IG TOC child and the EM-to-exponential-family equation link reaches the expected page and fragment |
| Browser runtime and resources | No JavaScript page errors, failed HTTP responses, or KaTeX error elements during the checks |
| Long equations | Contained horizontal scrolling remains available on narrow screens; a Fisher equation was explicitly scrolled to its right edge |
| Source review | New files read in full; mathematical assumptions, KL orientation, notation, references, relative links, and planned-versus-implemented scope reviewed |
| Whitespace | `git diff --check` and a separate scan of new files pass |

The preview served `_build/html/` beneath a local `math/` directory. This tests
the real prefix without writing to the publishing hub. Reproduce the preview
using the commands in [README](../../README.md#build-the-sites).

The downloaded theme identifies itself as `@myst-theme/book` 1.3.1. Its local
`template.zip` SHA-256 is
`9ce315ec6cfe3d96f99f2c2d96e07ee4bd076b896da97178c10e32f883077bea`.
This records the tested archive; the `book-theme` alias is still not pinned to
an upstream source revision.

## Checks not run and remaining limits

Python package tests, demos, packaging, and import-isolation checks were not
rerun because this batch changes site material and its HTML checker. The
[foundation record](phase-0-1-verification.md) retains the earlier Python results.
No numerical GH experiment, formal proof check, CI run, public-host browser
review, hub assembly, legacy-route rehearsal, or deployment was performed.
The local browser check covers Chrome at the two stated viewport sizes; it
does not establish cross-browser or assistive-technology conformance.

The prose and examples are original. No Incerto wiki bodies, private history,
or Normix JAX implementation were imported. The supplied conversation remains
a planning input; the outline records a Cauchy metric correction and defers
unverified later formulas to their own source review.

All changes are working-tree edits. No commit, branch, Git configuration change,
push, or PR was created. The pre-existing migration-manifest and Phase 2 planning
work are outside this batch.
