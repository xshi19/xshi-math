# Phase 2 — Normix Theory Batch 2 (proposed)

Status: **proposal only** — not executed. Writes under `/tmp` only; do not
modify `/workspace/xshi-math` from this planning pass.
Date: 2026-09-12 (ET) / 2026-09-13 UTC.
Source: public `https://github.com/xshi19/normix` at
`763bb3608920661a012cf089888d349fbf680aad`, read from `/workspace/normix`.
Normix Theory Batch 1 already imported **8** adapted/rewritten pages (plus
scaffold hubs `normix-theory`, `normix-conditioning-a-mixture`).

## Goal

Second Normix **theory** adaptation into `xshi-math` as flat stems
`content/normix-*.md`, drawing from the deferred theory cluster named in Batch 1:
`online_em`, `factor_analysis`, `shrinkage`, `varentropy`, and a mathematical
extract of design `em_framework` where it is not package API.

Still **NO** finance theory, **NO** API reference, **NO** JAX package / CI /
ASV / release machinery. Package how-tos remain at
[normix docs](https://xshi19.github.io/normix/).

## Batch 1 already imported (do not re-list as work)

| Stem | Source |
| --- | --- |
| `normix-generalized-inverse-gaussian` | `docs/theory/gig.md` |
| `normix-generalized-hyperbolic` | `docs/theory/gh.md` |
| `normix-em-algorithm` | `docs/theory/em_algorithm.md` |
| `normix-exponential-family-core` | `docs/design/exponential_family.md` |
| `normix-mixture-architecture` | `docs/design/mixtures.md` |
| `normix-why-not-gradient-descent` | `docs/design/why_not_gradient_descent.md` |
| `normix-gh-family-tour` | `docs/tutorials/core/02_gh_family_tour.md` |
| `normix-normal-mixtures` | `docs/tutorials/distributions/04_normal_mixtures.md` |

Scaffold (unchanged): `normix-theory`, `normix-conditioning-a-mixture`.

## Source survey residual (`docs/` @ 763bb36)

| Area | Remaining after Batch 1 | Batch 2? |
| --- | --- | --- |
| `docs/theory/` deferred math | online_em, factor_analysis, shrinkage, varentropy | **4 adapt** |
| `docs/design/em_framework.md` | API-heavy; η-update + Shrinkage math reusable | **1 rewrite** (math extract) |
| `docs/design/solvers_and_bessel.md` | Numerics / backends | **defer** (link upstream) |
| Finance theory: enb, generalized_enb, cvar_derivatives, mean_risk_optimization, transaction_costs | — | **NO** |
| `docs/api/*`, `user_guide/*`, `distributions/*` package pages | — | **NO / stay** |
| Tutorials (core Bessel/sampling, em/*, stats/*, finance/*) | — | **defer** |
| `docs/research/*`, `docs/pdfs/*` | — | defer / stay |

## Batch 2 pages (5)

MyST flat stems under `content/<stem>.md`; public slugs `/math/<stem>`.
Cross-links to package behavior remain absolute to
`https://xshi19.github.io/normix/…`. Approximate source size: **~1.19k lines**
(~216+192+131+255+394 before stripping API sections from `em_framework`).

| # | Source path | Stem → `content/<stem>.md` | Upstream URL | Disposition |
| --- | --- | --- | --- | --- |
| 1 | `docs/theory/online_em.md` | `normix-online-em` | https://xshi19.github.io/normix/theory/online_em.html | **adapt** |
| 2 | `docs/theory/factor_analysis.md` | `normix-factor-analysis` | https://xshi19.github.io/normix/theory/factor_analysis.html | **adapt** |
| 3 | `docs/theory/shrinkage.md` | `normix-shrinkage` | https://xshi19.github.io/normix/theory/shrinkage.html | **adapt** |
| 4 | `docs/theory/varentropy.md` | `normix-varentropy` | https://xshi19.github.io/normix/theory/varentropy.html | **adapt** |
| 5 | `docs/design/em_framework.md` | `normix-em-framework` | https://xshi19.github.io/normix/design/em_framework.html | **rewrite** (math only) |

### Why these five

Reading path continuing Batch 1 EM / EF / mixture geometry:

1. **Online EM** — Cappé–Moulines-style online EM for exponential families with
   hidden data; regret / Bregman view and η-space updates applied to GH.
   Extends `normix-em-algorithm` from batch to sequential.
2. **Factor analysis for GH** — Σ = FFᵀ + D structure; joint (X,Y,Z) density as
   a **curved exponential family**; sufficient statistics. Feeds mixture
   architecture / conditioning and later IG / gauge work; strip fitter API.
3. **Shrinkage / penalized likelihood** — KL / Bregman-penalized EM toward a
   prior θ₀; conditioning of Σ. Pairs with Batch 1 M-step and with the
   Shrinkage combinator math extracted from `em_framework`.
4. **Varentropy** — entropy, varentropy, Rényi entropy for EF components and
   joint normal variance–mean mixtures; density-power route. High IG value;
   keep formulas, drop package/`normix` autodoc tone and tutorial execution.
5. **EM framework (math extract)** — Source is design/API-heavy (fitter
   classes, loop dispatch, covariance modes). **Rewrite** to keep only:
   - η-update rule abstraction (two layers / sufficient-stat aggregation);
   - Shrinkage as Bregman-penalized EM (combinator math, not Python class API);
   - brief relation of batch vs incremental updates as algorithmic schemes.
   Cut public API tables, `BatchEMFitter` / `IncrementalEMFitter` recipes,
   eqx/JAX notes, and covariance-regularisation product modes → link upstream
   design page. If after stripping the page is thinner than ~1.5–2 screens of
   math, fold those two sections into `normix-online-em` /
   `normix-shrinkage` instead of a fifth stem (fallback: **4 pages**).

### Per-page notes

#### 1. `normix-online-em` — adapt

- **Source:** `docs/theory/online_em.md` (~216 lines). Theory Markdown; Sphinx
  `{ref}` / `{eq}` / possible `{doc}` to EM / GH.
- **Sphinx → MyST:** Convert math labels; Cappe2009 etc. → attributed
  year/DOI/publisher links (Batch 1 style); `{doc}` → flat stems or upstream.
- **Package:** Strip any fitter / IncrementalEM mentions as API; keep update
  equations.
- **IG / track value:** sequential η-space EM; Bregman regret.

#### 2. `normix-factor-analysis` — adapt

- **Source:** `docs/theory/factor_analysis.md` (~192 lines). Joint density,
  curved EF, ten-component sufficient stats, EM outline.
- **Sphinx → MyST:** Same role conversion; link `normix-generalized-hyperbolic`,
  `normix-em-algorithm`, `normix-mixture-architecture`.
- **Package:** No factor-mixture fitter API paste; Tortora et al. citation stay
  as attributed references.
- **IG value:** curved EF / latent (Y,Z) structure.

#### 3. `normix-shrinkage` — adapt

- **Source:** `docs/theory/shrinkage.md` (~131 lines). Penalized likelihood with
  KL(θ₀∥θ); EM fixed-point.
- **Cross-links:** `normix-em-algorithm`, `normix-exponential-family-core`,
  rewritten `normix-em-framework` (or inline if folded).
- **Package:** Shi2016 citation; no `Shrinkage` class autodoc.

#### 4. `normix-varentropy` — adapt

- **Source:** `docs/theory/varentropy.md` (~255 lines). Definitions, R(α)
  density-power route, EF and mixture formulas.
- **Sphinx → MyST:** Convert `{eq}` / `{ref}` / `{doc}` to stats tutorial →
  **absolute upstream** tutorial URL (do not import `tutorials/stats/*` here).
- **Tone:** “formulas used by the code” → “formulas for the EF / mixture
  models”; no ``normix`` API names required for the math to stand alone.
- **IG value:** varentropy as L² surprisal; fat-tail-friendly vs kurtosis.

#### 5. `normix-em-framework` — rewrite (conditional)

- **Source:** `docs/design/em_framework.md` (~394 lines). Keep §3–§4 math;
  drop §1–§2 API, §5 product modes, §6 loop dispatch, §7 cross-ref tables
  except peer math links.
- **Fallback:** If rewrite is too thin, do **not** add the fifth stem; document
  the η-update / Shrinkage combinator inside `normix-online-em` and
  `normix-shrinkage`, and leave design page upstream-only.

### Source line counts (pre-adaptation reference)

| Page | Lines | Notes |
| --- | ---: | --- |
| online_em | 216 | adapt |
| factor_analysis | 192 | adapt |
| shrinkage | 131 | adapt |
| varentropy | 255 | adapt |
| em_framework | 394 | rewrite → expect ≪394 after API strip |
| **Total (raw)** | **1188** | |

## Explicitly out of Batch 2

| Item | Disposition | Reason |
| --- | --- | --- |
| Finance theory (`enb`, `generalized_enb`, `cvar_derivatives`, `mean_risk_optimization`, `transaction_costs`) | **NO** | Portfolio / risk track |
| `docs/api/*`, JAX package, tests, CI, ASV, release | **NO / stay** | Repository boundary |
| `docs/user_guide/*`, `docs/distributions/*` | **stay** | Package how-to / catalog |
| `docs/design/solvers_and_bessel.md` | **defer** | Numerics / backends; link upstream |
| Tutorials: Bessel, sampling, `em/*`, `stats/*`, `finance/*`, remaining distributions tours | **defer** | Practice / API demos |
| `docs/research/mixture_gauges.md` | **defer** | Study-plan status |
| `docs/pdfs/*` | **stay** / link | Do not vendor binary |
| Incerto `normal-mixture` / `variance-gamma` wiki pages | schedule separately | Overlap already handled by Batch 1 Normix notes |
| Second Normix implementation or GH fitters in `xmath` | **non-goal** | Use pinned upstream when demos needed |

## Explicit non-goals (this batch)

- Do **not** move the JAX package, API reference, CI, ASV, or release machinery.
- Do **not** import finance theory or finance tutorials.
- Do **not** open a PR, push, or perform hub cutover / live redirects.
- Do **not** claim new GH curvature / marginal Fisher formulas beyond what
  adapted pages prove; `information-geometry-gh-*` remains a separate track.

## Proposed adaptation contract

1. Read selected Markdown + MIT license from the pinned checkout; record pin in
   provenance. Source tree read-only.
2. Frontmatter: `title:` only (match scaffold); drop Sphinx-only chrome.
3. Convert Sphinx roles → MyST math labels, relative flat stems, attributed
   citations, or **absolute** https://xshi19.github.io/normix/ links.
4. Strip `{code-cell}` / `import normix` / JAX if any appear; foundation does
   not install Normix by default.
5. Preserve equation `:label:` IDs used in upstream fragments where practical;
   record fragment audit in `url-map.csv`.
6. Cross-link Batch 1 peers + Batch 2 peers + `normix-conditioning-a-mixture`
   + relevant IG hubs; do not invent unimplemented `information-geometry-gh-*`
   stems.
7. Retain full MIT notice `(c) 2020 xshi19` on each page and in
   `THIRD_PARTY_NOTICES.md`.
8. Extend `content/normix-theory.md` TOC (online EM → FA → shrinkage →
   varentropy; optional EM-framework math note); update manifest / URL map /
   checker; run strict MyST HTML build.

## Suggested TOC extension under `normix-theory.md`

After Batch 1 EM / why-not-GD:

- **Sequential and regularized EM** — online EM → shrinkage → (optional)
  EM-framework math note.
- **Structured covariances** — factor analysis (curved EF).
- **Information quantities** — varentropy (entropy / Rényi).

Keep absolute links to upstream design (full EM framework, Bessel solvers) and
API for implementers.

## Non-goals (publication)

- Opening a PR / committing / pushing from this planning workspace.
- Modifying `/workspace/xshi-math` as part of this `/tmp` plan write.
- Importing finance, API, or package code.

## After Batch 2 (residual)

Deferred Normix math of IG-prep interest is largely covered. Remaining
upstream docs are finance theory, solvers/Bessel design, tutorials, research
gauges, and package surfaces — explicitly out of scope for theory batches.
Optional later: thin NumPy demos under `demos/normix/` (separate PR, pinned
`normix` version if executable).

## Survey counts (reference)

- Theory body pages: 12 · Design body: 5 (excl. indexes).
- Batch 1 = **8** pages; Batch 2 proposes **5** (or **4** if `em_framework`
  rewrite is folded).
- Finance theory pages: 5 — still excluded.
- Already present scaffold hubs: **2**.

## Page count & path

- **Pages proposed in Batch 2:** 5 (fallback 4 if EM-framework math is folded)
- **Plan file:** `/tmp/xshi-math-next-batches/phase-2-normix-theory-batch-2.md`
