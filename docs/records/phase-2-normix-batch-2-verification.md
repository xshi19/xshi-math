# Phase 2 — Normix Theory Batch 2 verification

Date: 2026-09-13 (UTC).
Status: five-page import executed locally; standard strict HTML build and
extended 51-page checker pass. Changes remain uncommitted for the parent to
branch/commit/PR. Further imports and public cutover remain separate work.

## Source and scope

The source is public `xshi19/normix`, pinned to
`763bb3608920661a012cf089888d349fbf680aad`. The sibling checkout's HEAD equals
that pin and its working tree is clean. The five selected Markdown files,
root MIT license, and source bibliography were read and compared byte-for-byte
with their pinned Git blobs. All writes were confined to `xshi-math`; the
source checkout was not modified. The destination working tree started clean.

The [executed plan](../plan/phase-2-normix-theory-batch-2.md) retains the exact
source paths, stems, dispositions, and exclusions. Batch 2 follows the eight
Batch 1 notes beneath the [Normix hub](../../content/normix-theory/index.md):

| Adapted file / route stem below `/math/` | Disposition | Explicit source labels retained | Rendered display equations |
| --- | --- | --- | --- |
| [normix-online-em](../../content/normix-online-em.md) | Adapt | 3 | 13 |
| [normix-factor-analysis](../../content/normix-factor-analysis.md) | Adapt | 3 | 13 |
| [normix-shrinkage](../../content/normix-shrinkage.md) | Adapt | 0 | 11 |
| [normix-varentropy](../../content/normix-varentropy.md) | Adapt | 12 | 20 |
| [normix-em-framework](../../content/normix-em-framework.md) | Mathematical rewrite | 0 | 11 |

**Five-page decision:** the EM-framework extract stands alone; it was not
folded into online EM or shrinkage. Its aggregation and recovery maps, general
and affine rules, scalar Bregman penalty, composition algebra, and blockwise
limitations form about 200 source lines before provenance, with eleven display
equations. This comfortably exceeds the plan's roughly 1.5–2-screen fallback
threshold without API tables, product modes, or fitting recipes.

No Batch 1 body was re-imported. No finance theory, tutorials, API body, solver
design, research note, PDF, package code, CI, ASV, or release machinery was
imported. Incerto pages and IG pages were not changed. The existing conditioning
note is unchanged, and no unimplemented IG/GH stem is linked.

## Adaptation decisions

- **Static content and notation:** title-only frontmatter; ordinary relative
  links among imported notes and absolute links for deferred package/design/
  tutorial material. All GH statistic orders begin with
  $(\log Y,Y^{-1},Y)$, followed by $(X,X/Y,XX^\top/Y)$. The factor note's
  ten blocks use this same first-six order. $Y$ maps to $W$ in the conditioning
  note; $Z$ is standard normal. Classical parameter tuples are distinguished
  from natural $\theta$ and expectation $\eta$. The factor regression matrix
  is called $A$, avoiding confusion with the conditioning note's skew $\beta$.
- **Online EM:** the learning rate is $\rho_t=1/(\tau_0+t)$, rather than
  calling its reciprocal the step size. The Bregman regret decomposition is
  retained with a proof and finite/interior assumptions; it is an identity,
  not a sublinear regret guarantee. No blanket equivalence of online and batch
  convergence rates or per-observation likelihood ascent is claimed.
  The source's exclusion of curved families is corrected: a model-specific
  constrained maximizing map can be used, while unrestricted ambient moment
  inversion can leave the family. Cappé–Moulines explicitly allow curved
  families under their maximizing-map assumptions; see
  [their author manuscript, Section 2.3 and Assumption 1](https://arxiv.org/pdf/0712.4273).
- **Factor analysis:** the source's $s_7^\top s_{10}^{-1}s_8$ and
  $s_7^\top s_{10}^{-1}s_9$ in `fa-aux` are dimensionally invalid for
  $s_7\in\mathbb R^{d\times r}$. The transpose is removed in both products.
  The normal updates are checked against an independent weighted least-squares
  solve. The likelihood expression omits only parameter-independent terms;
  positive diagonal residuals and nonsingular moment matrices are required.
  The GIG update remains numerical. Conditional dispersion is distinguished
  from marginal covariance; rotations and scale nonidentifiability are stated
  without importing research-gauge results.
- **Shrinkage:** determinant rescaling does not repair singularity or improve
  the condition number. The penalty compares joint laws on a fixed latent
  coordinate, while the likelihood is marginal. The penalized EM identity
  establishes ascent of that objective under an improving M-step. Scalar
  shrinkage blends complete statistic vectors; it is not generally a direct
  convex blend of fitted covariance matrices. A compatible sixth-block-only
  example explains when that simpler covariance formula and an eigenvalue
  lower bound do hold.
- **Framework rewrite:** general and affine statistic rules are kept as
  mathematics, with no class API, JAX/eqx detail, fitter loops, or product-mode
  tables. Scalar KL/Bregman shrinkage is distinguished from arbitrary
  blockwise rules, which need not correspond to the same penalty or preserve
  feasible moments. Shrinking a whole running average and updating toward
  newly shrunk statistics have different reference weights; the first can
  dominate a vanishing data step. The source's Euclidean-distance description
  of a model-based Bregman target is not carried over.
- **Varentropy:** the density-power derivative formulas require a fixed
  reference measure, integrability, and justified differentiation. The simple
  Fisher quadratic form uses a constant carrier; nonconstant carriers add
  covariance terms. GIG escort derivatives are evaluated at order one and
  retain the variable-coefficient operator correction. Proper inverse-gamma
  boundaries require their own argument, not an interior Bessel substitution.
  Joint entropy/varentropy are distinguished from marginal quantities; joint
  entropy does not depend on normal location/skew. A general joint density-power
  integral and the affine-coordinate limitation make these distinctions explicit.
- **References:** bibliography roles became attributed years and links.
  Cappé–Moulines metadata and the curved-family statement were checked against
  the publisher/author manuscript; Tortora–McNicholas–Browne's
  [2013 factor-analyzer preprint](https://arxiv.org/abs/1311.6530), Rényi's
  [1961 Berkeley contribution](https://digicoll.lib.berkeley.edu/record/112906),
  [NIST DLMF's Bessel integral](https://dlmf.nist.gov/10.32.E10), and the
  [Stankyavichyus preprint](https://anatolyvitold.com/preprints/varentropy_decomposition.pdf)
  provide the retained external references. Shi (2016) remains an attributed
  thesis citation from the pinned source bibliography; its incomplete metadata
  was not independently resolved. No shared bibliography or scholarly PDF was
  copied, and no substantial scholarly quotations were included.
- **Notices:** the new [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md)
  section lists all five source/target pairs and repeats the complete pinned
  MIT notice, including `Copyright (c) 2020 xshi19`. Each page carries the same
  full notice in its source, rendered dropdown, and Markdown download.

Supporting edits update the site index, Normix hub, two small Batch 1 link passages
(`normix-em-algorithm` and `normix-mixture-architecture`), [myst.yml](../../myst.yml),
[HTML checker](../../scripts/check_html.py), [migration manifest](../plan/migration-manifest.csv),
and [URL map](../plan/url-map.csv). The manifest adds five unique `imported`
rows at the required pin; unrelated rows are preserved. README, architecture,
the planning index, consolidation summary, and the Batch 2 plan reflect
thirteen imported Normix notes and the 51-page site. The earlier Batch 3
sandbox limitation remains historical in its own record.

## Executed verification

Environment: Node.js 20.19.2, npm 9.2.0, Python 3.13.5, NumPy 2.4.6,
MyST CLI 1.10.1. Browser checks used Chrome 151.0.7922.169 and the existing
ignored Playwright Core installation; no browser dependency was added.

| Check | Result |
| --- | --- |
| Source pin and scope | HEAD matches the pin; five sources, license, and bibliography match pinned blobs; Normix working tree clean before and after |
| `npm ci` | Passed with unchanged package manifests/lockfile and npm cache under ignored `_build/` |
| `npm run build` | Passed with the standard `BASE_URL=/math myst build --html --strict --ci`; no warnings or errors; rerun after the final content/link edits |
| `npm run check:html` | Passed for all 51 pages, local links/assets/fragments, `/math/` prefix, shared CSS, and rendered math |
| TOC / routes / checker | Same ordered set of 51 unique sources and HTML routes; Batch 1 order preserved, then the five Batch 2 stems in the plan's order; 14 Normix children |
| Math and labels | 68 display equations across the five imports; all 18 source equation labels retained in Markdown; all 29 explicit source/new labels resolve in rendered HTML after MyST case normalization |
| Notices and downloads | Complete pinned MIT text verified in all five source pages, rendered dropdowns, and JSON-linked Markdown exports; generated content license is MIT |
| Artifact scan | Generated HTML, JSON, and Markdown contain no source-checkout paths, private Incerto source links, or executable Normix/JAX imports |
| Numerical spot checks | 75 comparisons passed; largest scaled error about `1.98e-10`; algebra tolerance `2e-9`, finite-difference derivative tolerance `5e-7`; covariance eigenvalue bound also checked |
| Desktop, 1440 × 1000 | All 51 pages loaded without page-wide overflow; representative new-note equation screenshots reviewed |
| Mobile, 390 × 844 | All 51 pages loaded without page-wide overflow; representative screenshots reviewed; wide equations scroll horizontally |
| Navigation at both widths | All 14 Normix children present; TOC-to-framework, hub-to-online-to-factor, mixture-to-factor, varentropy equation, and Batch 1 peer/fragment navigation passed |
| Browser runtime | No page errors, failed resources, HTTP errors, or KaTeX error elements; pages with final prose/link edits and navigation were rechecked |
| Source/diff review | Full new files and supporting diffs reviewed for equations, assumptions, notation, citations, scope, source notices, and current/proposed status |
| Links and whitespace | Changed/new Markdown relative paths checked; `git diff --check` and a separate untracked-file whitespace check passed |

Numerical checks used NumPy trapezoidal integration on a log-mixing-variable
mesh from -16 to 16 with 32,001 points for four moderate interior GIG triples.
They compare density-power integrals, entropy, Fisher varentropy, and joint
operator/density-power formulas for dimensions one and three. Fourth-order
finite differences use step `0.002`. Factor checks compare the corrected
normal-block update with a direct least-squares solve on fixed seeded synthetic
complete-data arrays, and compare aggregated factor E-step blocks with
per-observation conditional quadrature. A finite two-by-two latent model checks
the online aggregation and regret identity with a nonzero posterior-KL sum.
These are numerical illustrations, not formal proofs, a boundary survey,
Normix package tests, or GH/FA fitting-convergence experiments.

The standard build runs its normal localhost renderer in this environment;
no theme-only workaround was used. Browser review served the static artifact
under `/math/`. Local audit scripts, logs, numerical results, and screenshots
remain under ignored `_build/normix-batch2-review/` and are not dependencies
of the content or package. The tested theme is `@myst-theme/book` 1.3.1;
its `template.zip` SHA-256 is
`9ce315ec6cfe3d96f99f2c2d96e07ee4bd076b896da97178c10e32f883077bea`.
The `book-theme` alias is still not pinned to a theme source revision.

## Fragment audit and publication limits

The source labels retained are `regret-def`, `online-em-update`,
`regret-decomp`; `fa-joint`, `fa-aux`, `fa-mstep`; and all twelve `ve-*`
labels from the varentropy source. Shrinkage and the design framework have no
explicit upstream equation labels. MyST lowercases these four rendered IDs:

| Source label | Local HTML fragment |
| --- | --- |
| `ve-R` | `#ve-r` |
| `ve-R-ef` | `#ve-r-ef` |
| `ve-gig-R` | `#ve-gig-r` |
| `ve-L` | `#ve-l` |

All internal references resolve to the generated fragments. This is not full
historic-fragment compatibility: Sphinx `equation-*` prefixes, automatic heading
anchors, and headings removed from the API-heavy design page require cutover
review. The five URL-map rows retain proposed publication/compatibility status;
legacy upstream routes are unchanged. No redirect, hub assembly, public
hosting, or exhaustive live upstream URL audit was performed.

## Checks not run and remaining limits

No local build blocker remains. Python sync/pytest, the exceedance demo, wheel
builds, and import isolation were not rerun because no helper, package mapping,
Python dependency, or demo changed. No Normix fitting code, tutorial execution,
benchmark, upstream package test, stochastic convergence experiment, Lean, or
formal-proof verification was run. Reference checks do not mean that every
cited thesis or article was independently reviewed in full.

The browser checks cover Chrome at the two stated sizes, not cross-browser or
assistive-technology conformance. A hermetic/offline build was not tested.
Finance theory, full implementation design, Bessel solvers, tutorials, research
notes, API, and package surfaces remain upstream/deferred as specified in the
plan. No new IG/GH research result is claimed.

No commit, branch change, Git configuration change, push, PR, Cursor CloudAgent,
source-repository write, or deployment was made. The 14 modified files and six
new untracked files remain uncommitted; ignored review artifacts stay local to
`xshi-math`.
