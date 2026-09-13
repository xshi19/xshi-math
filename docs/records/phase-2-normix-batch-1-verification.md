# Phase 2 — Normix Theory Batch 1 verification

Date: 2026-09-13 (UTC).
Status: eight-page import executed locally; strict HTML build and extended
29-page checker pass. Changes remain uncommitted for the parent to commit/PR.
Further Phase 2 imports and public cutover remain planned.

## Source and scope

The source is public `xshi19/normix`, pinned to
`763bb3608920661a012cf089888d349fbf680aad`. The sibling checkout's HEAD equals
that pin and its working tree is clean. Each of the eight selected Markdown
files was read at the pin and compared byte-for-byte with its checked-out file.
The root MIT license and source bibliography were also read at the pin.
All writes were confined to `xshi-math`; the source repository was not modified.

The [executed plan](../plan/phase-2-normix-theory-batch-1.md) retains the exact
source paths, stems, adaptation methods, and exclusions. These files follow
the existing conditioning introduction beneath the
[Normix hub](../../content/normix-theory/index.md):

| Adapted file / route stem below `/math/` | Explicit source labels retained | Rendered display equations |
| --- | --- | --- |
| [normix-generalized-inverse-gaussian](../../content/normix-generalized-inverse-gaussian.md) | 10 | 18 |
| [normix-generalized-hyperbolic](../../content/normix-generalized-hyperbolic.md) | 9 | 17 |
| [normix-em-algorithm](../../content/normix-em-algorithm.md) | 3 | 19 |
| [normix-exponential-family-core](../../content/normix-exponential-family-core.md) | 0 | 12 |
| [normix-mixture-architecture](../../content/normix-mixture-architecture.md) | 0 | 8 |
| [normix-why-not-gradient-descent](../../content/normix-why-not-gradient-descent.md) | 0 | 3 |
| [normix-gh-family-tour](../../content/normix-gh-family-tour.md) | 0 | 7 |
| [normix-normal-mixtures](../../content/normix-normal-mixtures.md) | 0 | 8 |

No finance theory, API bodies, online EM, factor-analysis derivations, EM
framework or solver implementation, research gauges, PDF, notebook image,
Normix/JAX code, or package dependency was imported. Deferred implementation
and tutorial pages remain absolute upstream links. Incerto and IG content
files were not edited. The original conditioning derivation was preserved
and gained symbol mappings and links to the new notes.

## Adaptation decisions

- **Static mathematical notes:** all eight pages have title-only frontmatter.
  Design and tutorial sources were rewritten around probability laws,
  sufficient statistics, moments, and estimation. Constructor recipes, class
  layouts, fitters, executable JAX cells, and generated plots were removed.
  The normal-mixtures note includes an exact rational covariance calculation.
- **Notation:** $Z$ is standard normal; the literature mixing variable $Y$
  corresponds to $W$ in the conditioning note. In one dimension
  $\gamma=\beta$ and $\Sigma=\sigma^2$; multivariate noise is $LZ$ with
  $LL^\top=\Sigma$. GIG scale/concentration uses $(\delta,\omega)$ so that
  $\eta$ consistently denotes expectation coordinates. All six-block joint
  statistics begin with $(\log Y,Y^{-1},Y)$, correcting the source's differing
  slot orders in the GH and EM pages.
- **GIG corrections:** the scale density uses $\delta^{-p}$; the alternative
  MGF argument is $\sqrt{\omega^2-2\omega\delta u}$. The log moment is an
  exact order derivative of $\log K$, even though numerical evaluation is
  required in practice. The likelihood uses the same statistic order as its
  expectation map. Boundary moments and MLE existence are stated separately
  from interior convexity and numerical conditioning.
- **GH and EM corrections:** the scale action is consistently
  $(\gamma,\Sigma,a,b)\mapsto(\gamma/c,\Sigma/c,a/c,bc)$, with posterior
  moments transforming as those of $cY$. The joint law on a fixed latent
  coordinate is distinguished from the invariant marginal law. Determinant
  normalization transforms every coupled parameter and does not control the
  covariance condition number. The source's univariate hyperbolic $p=1$
  designation is qualified by dimension.
- **Optimization qualifications:** EM increases the observed likelihood under
  exact posteriors and improving M-steps; no global-MLE or parameter-convergence
  guarantee is claimed. The MCECM explanation requires actual conditional
  maximizations and does not justify ascent by rescaling the covariance alone.
  Gamma and inverse-gamma shape updates remain scalar numerical solves.
  The optimization comparison is explicitly an upstream report, without local
  timing or upstream-test claims.
- **Geometry and boundaries:** joint exponential-family structure is not
  inferred for arbitrary mixing laws or their marginals. Matrix statistics use
  independent symmetric coordinates for rank/minimality statements. Bessel
  functions alone are not evidence against exponential-family membership.
  Posterior moment requirements at gamma/inverse-gamma boundaries and the
  distinction between a positive mixing variable and a process subordinator
  are explicit. No later IG/GH curvature or research-gauge theory is imported.
- **References:** Sphinx bibliography roles became ordinary attributed
  author/year citations or publisher links. The pinned source bibliography
  supplied the retained references; selected metadata was checked against
  NIST DLMF, Springer's Jørgensen book page (1982; electronic edition 2012),
  and the Oxford publisher records for Dempster–Laird–Rubin (1977) and
  Meng–Rubin (1993). No shared bibliography or scholarly PDF was copied.
- **Notices:** [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md) lists the
  eight source/target pairs and retains `Copyright (c) 2020 xshi19` plus the
  complete pinned MIT notice. Every imported page repeats the notice in its
  source and rendered dropdown. No external figures, datasets, or substantial
  scholarly quotations were included.

Supporting edits update the hub, conditioning note, site index,
[myst.yml](../../myst.yml), [HTML checker](../../scripts/check_html.py),
[migration manifest](../plan/migration-manifest.csv), and
[URL map](../plan/url-map.csv). The existing `normix-gh` and `normix-gig`
manifest IDs are preserved; six rows were added. All eight dispositions are
`imported`, with exact target stems including `normix-exponential-family-core`.
All eight URL mappings retain proposed publication/compatibility status.
README, architecture, the planning index, and consolidation status now reflect
this completed batch and the 29-page site.

## Executed verification

Environment: Node.js 20.19.2, npm 9.2.0, Python 3.13.5, MyST CLI 1.10.1.
Browser review used Chrome 151.0.7922.169 with the existing ignored local
Playwright Core 1.63.0 installation. No browser tooling dependency was added to the
repository manifests.

| Check | Result |
| --- | --- |
| Source pin | HEAD equals the requested pin; source working tree clean; all eight files match their pinned Git blobs |
| `npm ci` | Passed with the unchanged lockfile; npm cache confined to ignored `_build/` |
| `npm run build` | Passed with `BASE_URL=/math myst build --html --strict --ci`; 29 pages, no warnings or errors |
| Clean output rebuild | Site/HTML output cleaned and strict build rerun; final artifact contains only the 29 current Markdown exports |
| `npm run check:html` | Passed on the final artifact for all 29 pages, local links/assets/fragments, `/math/` prefix, shared CSS, and rendered math |
| TOC / routes / checker | Same ordered set of 29 unique sources and routes; conditioning remains the first of nine Normix children; no extra HTML routes |
| Math and labels | 92 display equations across eight imports; all 22 upstream explicit equation labels retained; all 32 new/retained explicit labels present in HTML |
| Notices and exports | Complete pinned MIT notice verified in all eight source pages, rendered pages, and JSON-linked Markdown downloads; generated content license is MIT |
| Artifact scan | HTML, JSON, and Markdown contain no source-checkout paths, private Incerto source links, or executable Normix/JAX imports |
| Numerical spot checks | 221 independent NumPy quadrature/algebra comparisons passed at scaled tolerance `2e-9`; largest observed scaled error about `1.53e-15` |
| Desktop, 1440 × 1000 | All 29 pages loaded without page-wide overflow; representative Normix equations/screenshots reviewed |
| Mobile, 390 × 844 | All 29 pages loaded without page-wide overflow; representative equations/screenshots reviewed; wide equations scroll horizontally |
| Navigation at both widths | All nine Normix children visible; TOC-to-EF-core, hub-to-GIG-to-GH, and EM-to-GIG-equation links worked |
| Browser runtime | No page errors, failed resource requests, HTTP errors, or KaTeX error elements in the final run |
| Source and diff review | All eight new pages and supporting edits reviewed for mathematics, scope, citations, notation, notices, and current/proposed status |
| Relative links and whitespace | Changed/new Markdown targets checked; `git diff --check` and a separate untracked-file whitespace check passed |

The independent numerical checks use NumPy trapezoidal integration on a log
mixing-variable grid from -16 to 16 with 32,001 points. Four moderate interior
GIG triples and dimensions 1–3 exercise density normalization, scale and MGF
formulas, moments, the integrated GH density, posterior closure and scaling,
normal-block moment inversion, and agreement of classical, natural-coordinate,
and integrated joint Hellinger affinities. The rational covariance example
was also checked. This is finite-grid numerical evidence for the adapted
formulas, not an upstream package test, a proof, a boundary survey, or a test of
GIG fitting and full EM convergence.

The browser served static HTML below `/math/` from a local server. Opening GH
and EM equations were split across lines after the initial layout review;
the final clean build and browser checks use that revised source. Audit scripts,
logs, numerical details, and screenshots remain under ignored
`_build/normix-batch1-review/`. No publishing-hub write was made.

The tested theme is `@myst-theme/book` 1.3.1. Its `template.zip` SHA-256 is
`9ce315ec6cfe3d96f99f2c2d96e07ee4bd076b896da97178c10e32f883077bea`.
The `book-theme` alias is still not pinned to an upstream source revision.

## Checks not run and remaining limits

No local Batch 1 build blocker remains. Python sync/pytest, the exceedance demo,
wheel builds, and import-isolation checks were not rerun: no Python helper,
package mapping, dependency, or demo changed. The HTML checker was exercised
by `npm run check:html`; earlier package checks remain in the
[foundation record](phase-0-1-verification.md).

Upstream benchmark scripts, notebook plots, Normix fitters, stochastic
simulations, and package tests were not executed. No Lean or formal-proof
verification was performed. The plain attributions preserved from the source
are not a claim that every cited thesis or article was independently reviewed.

Fresh builds can require theme downloads and citation metadata requests; an
offline or fully hermetic build was not tested. Browser review covers Chrome
at the two stated viewport sizes, not cross-browser or assistive-technology
conformance. No CI, hub assembly, deployment, live legacy redirect, or full
historic-fragment compatibility check was performed. All 22 explicit source
equation labels survive locally, but Sphinx URL fragment prefixes and historic
automatic heading anchors still need cutover review. Upstream legacy routes
remain unchanged and their current availability was not exhaustively checked.

The pre-existing untracked Normix plan was updated in place. Unrelated manifest
and URL-map proposals were preserved. No commit, branch change, Git
configuration change, push, PR, Cursor CloudAgent, or source-repository write
was made. All requested changes are left uncommitted.
