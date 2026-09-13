# Phase 2 — Normix Theory Batch 1

Status: **imported / executed locally** (eight static mathematical notes).
Execution date: 2026-09-13 (UTC); original survey date: 2026-09-12 (ET).
Source: public `https://github.com/xshi19/normix` at
`763bb3608920661a012cf089888d349fbf680aad`, read from `/workspace/normix`.
All writes are confined to `/workspace/xshi-math`; changes remain uncommitted.
See the [verification record](../records/phase-2-normix-batch-1-verification.md)
for the strict build, 29-page HTML gate, mathematical corrections, and limits.
The body retains the approved mapping, adaptation rationale, and exclusions;
publication and legacy compatibility remain future work.

## Goal

Completed first Normix **theory** adaptation into `xshi-math` as flat stems `content/normix-*.md`, supporting the later IG → GH/Normix research sequence (`information-geometry-gh-*` in `docs/plan/ig-entry-outline.md`). Prefer foundational GIG / GH / mixture / EM geometry pages. Keep package API, JAX code, CI, and finance tutorials upstream at [normix docs](https://xshi19.github.io/normix/).

Existing scaffold (already in `xshi-math`; do not re-import):

| Stem | Role |
| --- | --- |
| `normix-theory` | Track hub; reading path and TOC expanded |
| `normix-conditioning-a-mixture` | Original conditioning derivation (already MyST) |

## Source survey (`docs/` on master)

| Area | Count (approx) | Batch 1? |
| --- | --- | --- |
| `docs/theory/*.md` (excl. index) | 12 | **3** adapt (GIG, GH, EM); online EM deferred |
| `docs/design/*.md` (excl. index) | 5 | **3** rewrite/adapt (EF core, mixtures, why-not-GD); defer EM framework + Bessel solvers |
| `docs/tutorials/core/*` | 4 | **1** rewrite (GH family tour); defer Bessel/sampling how-tos |
| `docs/tutorials/distributions/*` | 5 | **1** rewrite (normal mixtures); defer univariate/MVN/factor/API tours |
| `docs/tutorials/em/*`, `stats/*`, `finance/*` | many | **defer** (fitting practice / finance) |
| `docs/api/*`, `user_guide/*`, `distributions/*` package pages | — | **stay** in normix |
| `docs/research/*` | 2+ | **defer** (study-plan status; not production theory) |
| `docs/pdfs/*` | 1 PDF | **stay** / link upstream; do not vendor binary |

## Batch 1 pages (8)

MyST needs **unique flat stems** under `content/*.md` (match current scaffold; no nested `index.md`). Proposed public slugs: `/math/<stem>`. Cross-links to package behavior remain absolute to `https://xshi19.github.io/normix/…`.

| # | Source path | Stem → `content/<stem>.md` | Legacy / upstream URL | Disposition |
| --- | --- | --- | --- | --- |
| 1 | `docs/theory/gig.md` | `normix-generalized-inverse-gaussian` | https://xshi19.github.io/normix/theory/gig.html | **adapt** |
| 2 | `docs/theory/gh.md` | `normix-generalized-hyperbolic` | https://xshi19.github.io/normix/theory/gh.html | **adapt** |
| 3 | `docs/theory/em_algorithm.md` | `normix-em-algorithm` | https://xshi19.github.io/normix/theory/em_algorithm.html | **adapt** |
| 4 | `docs/design/exponential_family.md` | `normix-exponential-family-core` | https://xshi19.github.io/normix/design/exponential_family.html | **rewrite** |
| 5 | `docs/design/mixtures.md` | `normix-mixture-architecture` | https://xshi19.github.io/normix/design/mixtures.html | **rewrite** |
| 6 | `docs/design/why_not_gradient_descent.md` | `normix-why-not-gradient-descent` | https://xshi19.github.io/normix/design/why_not_gradient_descent.html | **adapt** |
| 7 | `docs/tutorials/core/02_gh_family_tour.md` | `normix-gh-family-tour` | https://xshi19.github.io/normix/tutorials/core/02_gh_family_tour.html | **rewrite** |
| 8 | `docs/tutorials/distributions/04_normal_mixtures.md` | `normix-normal-mixtures` | https://xshi19.github.io/normix/tutorials/distributions/04_normal_mixtures.html | **rewrite** |

Execution extended the existing hub and TOC, refreshed the two sampled GH/GIG rows, and added the six remaining rows to both CSVs. All eight manifest dispositions are `imported`; the table above retains each page's adaptation method.

### Why these eight

Reading path for IG prep:

1. **GIG** — mixing density, moments, EF form (needed for posterior moments).
2. **GH** — normal variance–mean mixture, joint vs marginal, **model identifiability**, EF form (feeds `information-geometry-gh-identifiability`).
3. **EM for GH** — conditional \(Y\mid X\), posterior expectations of \(Y,Y^{-1},\log Y\), M-step (feeds latent-variable / EM spectrum notes).
4. **EF core (design → math note)** — \(\theta/\eta/\psi\) triad and Bregman view without shipping the package layout.
5. **Mixture architecture (design → math note)** — joint vs marginal classes as mathematical layers; sufficient-statistic order.
6. **Why not GD** — observed-data NLL vs EM / exponential-family MLE geometry (pairs with IG EM page).
7. **GH family tour** — subordinators and nesting (Gamma / InvGamma / IG / GIG) as narrative; strip executable package demos.
8. **Normal mixtures tutorial** — mean/covariance, joint vs marginal face; strip `normix` fitters/API cells.

Approximate source size: ~8 pages, 2,017 lines / about 75 KB Markdown (theory-heavy pages dominate). Smaller than a full theory dump; comparable to Incerto Batch 1 scope.

### Per-page notes (Sphinx → MyST, figures, package links)

#### 1. `normix-generalized-inverse-gaussian` — adapt

- **Source:** `docs/theory/gig.md` (~292 lines). Pure Markdown theory; no figures; no `{code-cell}`.
- **Sphinx → MyST:** Convert `{eq}`labels / `:label:` to MyST ` ```{math} :label:` …`; rewrite `{doc}`../tutorials/distributions/02_gig`` → either Batch-deferred stub or absolute upstream tutorial URL; rewrite `{ref}`CiteKey <key>`` to site bibliography strategy (none in foundation yet — inline citations or add bib in same PR); replace `{class}`/`{meth}` ``~normix…`` with links to https://xshi19.github.io/normix/api/… (or prose “see package API”).
- **Figures:** none in source.
- **Package links:** keep Gamma / InvGamma / IG / GIG API pointers upstream; do not paste autodoc.
- **IG value:** GIG parameterization and moment formulas are prerequisites for posterior maps.

#### 2. `normix-generalized-hyperbolic` — adapt

- **Source:** `docs/theory/gh.md` (~334 lines). Sections include Definition as Normal Mixture, Joint GH, Marginal density, Alternative parameterization, **Model Identifiability**, Moments, Exponential Family Form.
- **Sphinx → MyST:** Same equation/role conversion as GIG; `{doc}`gig`` → relative `./normix-generalized-inverse-gaussian.md`; API roles → upstream `/normix/api/` links (NIG, NIGamma, VG, skewness/kurtosis helpers).
- **Figures:** none.
- **Package links:** density/moments methods stay upstream; math conventions must be stated independently of constructor names (align with `normix-conditioning-a-mixture`).
- **IG value:** identifiability / scale action material is the direct precursor to `information-geometry-gh-identifiability`.

#### 3. `normix-em-algorithm` — adapt

- **Source:** `docs/theory/em_algorithm.md` (~417 lines). Conditional \(Y\mid X\), conditional expectations, EM / MCECM, regularization, special cases.
- **Sphinx → MyST:** Heavy `{class}`/`{func}`/`{meth}`/`{mod}` to `normix.fitting.*`, `JointNormalMixture.conditional_expectations`, `solve_bregman`, etc. → **strip or replace with upstream links**; keep Dempster / Meng–Rubin / Hu citations; `{doc}`gh`` → flat stem.
- **Figures:** none.
- **Package links:** fitting user guide + API remain at https://xshi19.github.io/normix/ (e.g. user guide EM, API fitting); math page must not become a second API reference.
- **IG value:** exact posterior E-step moments underpin missing-information / EM-spectrum research.

#### 4. `normix-exponential-family-core` — rewrite

- **Source:** `docs/design/exponential_family.md` (~176 lines). Design rationale (“why one log-partition”), triad pattern, Bregman solver interface, pre-1.0 decisions.
- **Disposition rewrite:** Keep mathematical triad / dual coordinates; **cut** API layout, class-path recipes, and “decisions recorded here” changelog tone. Point readers to upstream design+API for implementation.
- **Sphinx → MyST:** Few `{doc}` links (to API index, EM theory, GIG, solvers, why-not-GD) → flat stems or `https://xshi19.github.io/normix/…`.
- **Figures:** none.
- **Cross-links:** complement existing IG note `information-geometry-exponential-families.md` (do not duplicate; cite relative link).

#### 5. `normix-mixture-architecture` — rewrite

- **Source:** `docs/design/mixtures.md` (~287 lines). Joint vs Marginal split, `from_expectation`, factor family, sufficient statistics order.
- **Disposition rewrite:** Extract joint/marginal mathematical roles and η→model map; remove public-API facade and class-naming policy. Link factor-analysis **theory** (deferred) and upstream API mixtures pages.
- **Figures:** none.
- **IG value:** joint EF vs observable marginal is the structural hook for marginal Fisher / quotient gauges.

#### 6. `normix-why-not-gradient-descent` — adapt

- **Source:** `docs/design/why_not_gradient_descent.md` (~169 lines). Compares EM / EF MLE vs Adam/L-BFGS on observed NLL; contains illustrative `jax` snippets and `{py:class}` roles.
- **Sphinx → MyST:** Convert roles; either (a) drop executable snippets and summarize findings, or (b) thin non-package NumPy sketch in `demos/` later — **Batch 1 prefer (a)**. Keep Dempster citation and limitations section (“what this does not show”).
- **Figures:** none embedded; no `_static` images referenced.
- **Package links:** BatchEMFitter / GH / GIG → upstream API; user-guide EM fitting stays on normix site.

#### 7. `normix-gh-family-tour` — rewrite

- **Source:** `docs/tutorials/core/02_gh_family_tour.md` (~194 lines). MyST-NB (`file_format: mystnb`) with `{code-cell}` importing `normix`, JAX, matplotlib.
- **Disposition rewrite:** Keep mixing-mechanism + subordinator nesting narrative and citations; **remove or disable code-cells**; replace plots with static captions linking upstream tutorial HTML, or regenerate offline later under `assets/` (not in this plan). Drop kernelspec frontmatter incompatible with foundation MyST without notebook execution.
- **Figures:** tutorial generates plots at build time (no checked-in PNG under `docs/`); Batch 1 omits figures and links upstream — do not vendor notebook outputs from CI.
- **Package links:** “how to construct in normix” → https://xshi19.github.io/normix/tutorials/core/02_gh_family_tour.html.

#### 8. `normix-normal-mixtures` — rewrite

- **Source:** `docs/tutorials/distributions/04_normal_mixtures.md` (~148 lines). MyST-NB with package constructors, EM fitting cells.
- **Disposition rewrite:** Keep mean/covariance identities and joint vs marginal explanation; remove constructor/fitter cells; deepen cross-links to Batch 1 theory stems and to `normix-conditioning-a-mixture`.
- **Figures:** none checked in; same static/omit policy as #7.
- **Package links:** upstream tutorial + API mixtures pages for executable examples.

## Explicitly out of Batch 1

| Item | Disposition | Reason |
| --- | --- | --- |
| `docs/api/*` | **stay** | Package API reference remains on normix site |
| JAX package, tests, CI, release/ASV workflows | **stay** | Repository boundary (`xshi-math → normix`) |
| `docs/user_guide/*`, `docs/distributions/*` | **stay** | Package how-to / distribution catalog |
| Finance theory: `enb`, `generalized_enb`, `cvar_derivatives`, `mean_risk_optimization`, `transaction_costs` | **defer** | Portfolio/risk track; not IG prerequisites |
| `docs/theory/online_em.md`, `factor_analysis.md`, `shrinkage.md`, `varentropy.md` | **defer** | Batch 2+ (online/curved EF, FA, penalties, info quantities) |
| `docs/design/em_framework.md`, `solvers_and_bessel.md` | **defer** | Implementation/design depth; link upstream for now |
| `docs/tutorials/core/01_exponential_family.md`, `03_bessel_*`, `04_random_sampling.md` | **defer** | Mostly API/backends/numerics how-to |
| Other `tutorials/distributions/*`, all `tutorials/em/*`, `stats/*`, `finance/*` | **defer** | Fitting practice / finance / API demos |
| `docs/research/mixture_gauges.md` | **defer** | Marked study plan (2026-08-19); not ready as public theory |
| `docs/pdfs/generalized_hyperbolic_finance.pdf` | **stay** / link | Do not copy binary into math repo in Batch 1 |
| Incerto `normal-mixture` / `variance-gamma` wiki pages | schedule separately | Overlap boundary; reconcile with this batch later |
| Vendoring second Normix implementation or `xmath` GH fitters | **non-goal** | Use pinned upstream package when demos are needed |

## Explicit non-goals (this batch)

- Do **not** move the JAX package, API reference, CI, ASV, or release machinery into `xshi-math`.
- Do **not** import finance tutorials or finance theory wholesale.
- Do **not** open a PR, push, or perform hub cutover / legacy redirects live (Phase 3+).
- Do **not** claim GH curvature / marginal Fisher formulas beyond what adapted pages already prove; later `information-geometry-gh-*` pages remain separate.

## Executed adaptation contract

1. Read selected Markdown and the MIT license from the pinned sibling checkout; compare selected files with their Git blobs; retain the full pin in provenance.
2. Frontmatter: `title:` only (match scaffold); drop Sphinx/MyST-NB kernelspec / `file_format: mystnb` unless notebook execution is deliberately enabled.
3. Convert Sphinx roles: `{eq}`, `{doc}`, `{ref}`, `{class}`/`{func}`/`{meth}`/`{mod}`/`{py:*}` → MyST math labels, relative flat stems, bibliography, or **absolute** https://xshi19.github.io/normix/ links.
4. Strip `{code-cell}` that `import normix` / JAX; foundation does not install Normix by default.
5. Preserve equation `:label:` IDs used in upstream fragments where practical; record fragment audit in `url-map.csv`.
6. Cross-link Batch 1 peers + `normix-conditioning-a-mixture` + relevant IG hubs; do not link unimplemented `information-geometry-gh-*` stems.
7. Retain the full MIT notice `(c) 2020 xshi19` in each page and `THIRD_PARTY_NOTICES.md`; imported pages include no external figures or substantial scholarly quotations.
8. Update `content/normix-theory.md` and `myst.yml`; extend manifest, URL map, and checker; run the strict MyST build and HTML check across all 29 pages.

## Import issues resolved and remaining limits

1. **Sphinx roles:** converted to MyST math blocks, relative peer links, plain
   attributed scholarly citations, or absolute upstream links; no autodoc copied.
2. **Bibliography:** kept inline publisher links and attributed references; no
   shared bibliography added. Source bibliographic years and reported evidence
   are qualified in the adapted pages and verification record.
3. **Notebooks:** executable cells and generated figures omitted; package
   examples and plots remain linked upstream.
4. **Conventions and mathematical review:** standardized normal noise $Z$,
   explicitly mapped $Y=W$, and unified the sufficient-statistic order.
   Corrected GIG scaling/MGF expressions and EM scale equivariance; qualified
   boundary moments, MLE existence, identifiability, and convergence claims.
5. **Legacy URLs:** all eight routes are mapped to proposed `/math/<stem>`
   targets; no upstream route, deployment, or live redirect was changed.
6. **Notices:** full pinned MIT notice carried on all eight pages and in the
   repository notice. No third-party assets, PDFs, or substantial scholarly
   quotations were imported.
7. **Workspace:** source checkout remained read-only; all writes stayed under
   `xshi-math`. The owner explicitly authorized execution of this batch.
8. **Deferred design depth:** EM framework and Bessel/solver implementation
   pages remain upstream and are linked explicitly.

## Completed change shape

1. Provenance notices and URL-map/manifest rows for all eight stems.
2. Adapt/rewrite eight pages + TOC update on `normix-theory.md`.
3. Relative links among Batch 1 and existing IG entries, absolute package links, and local strict build / `check:html` for all 29 pages.
4. No Normix package dependency pin required if cells are stripped; if a later demo PR adds executable cells, pin a tested `normix` version then.

## Survey counts (reference)

- Theory body pages: 12 · Design body: 5 · Core tutorials: 4 · Distributions tutorials: 5.
- Batch 1 = **8** pages (2,017 source lines).
- Already present scaffold hubs: **2** (`normix-theory`, `normix-conditioning-a-mixture`).
- Finance theory + finance tutorials + API + research gauges: explicitly excluded.

## Output path

- This plan: `docs/plan/phase-2-normix-theory-batch-1.md`.
- Verification: [Normix Batch 1 record](../records/phase-2-normix-batch-1-verification.md).
