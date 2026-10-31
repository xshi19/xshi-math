# Concept register

The register retains all 101 previous IDs and appends two: **103 stable IDs,
75 in scope and 28 out of scope**. SCoFT uses the **2025 third edition,
arXiv:2001.10488v4** throughout. `c-lindy` is reactivated for the technical
absorbing-barrier treatment in chapter 23; its former non-technical scope is
retained in state as history. New IDs are `c-probability-conflation` and
`c-portfolio-tail-dependence`. Appendix B reuses `c-maximum-entropy`.

The remaining exclusions comprise 24 concepts mapped only to non-technical
books and four contextual concepts (induction, cognitive biases, tacit
knowledge and ethics). An origin citation does not create a coverage task.

Every active concept requires website math teaching first and Python demos,
visualizations or worked cases second. Lean is optional and last.
`lean-verifiable` identifies a declaration candidate, not checked evidence.
`numeric-demo` uses synthetic/fixed inputs; `empirical` needs observed data.
Lean skips preserve teaching/numerical obligations. M0.5 reviewed its fixed
24-body inventory. Chapters 1–5 now have scoped implementation checkpoints
and completed separate max reviews. State is the completion authority;
the chapter-5 entries below reflect its new evidence and later scopes.

Chapter 9 and Appendix E extend nine existing registered concepts. The
[hidden-tail note](../../../content/incerto-hidden-tail.md) is a supplementary
treatment of their moment/extrapolation scope, not a new program concept ID.

Source links below use v4 chapter/appendix locators. Chunk lists identify
chapter-scoped reuse or extension; the first chunk does not promise completion
of every later claim. Concept prerequisites do not reorder the chapter queue.
Proposed paths remain reservations, not public pages.

<a id="c-exceedances"></a>

## Finite-sample exceedance counts (`c-exceedances`)

Home: [content/incerto-counting-exceedances.md](../../../content/incerto-counting-exceedances.md). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

For n >= 1 and real observations, prove fraction bounds and antitonicity in u; no population inference.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional-approved-pilot`).

- **numeric-demo:** The existing fixed sample checks the strict threshold convention.
- **lean-verifiable:** Finite-set counting gives exact bounds and threshold monotonicity.

Coverage: Original page and xmath.exceedance_fraction; fixed synthetic demo exists. Neither implementation nor population inference is formally verified.

Prerequisites: none within this inventory.

Technical source mappings: [SCoFT v4 ch. 2](inventory.md#scft-v4-ch02).

Chapter chunks: `scft-v4-ch02`.

<a id="c-pareto"></a>

## Pareto distribution (`c-pareto`)

Home: [content/incerto-pareto.md](../../../content/incerto-pareto.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Positive scale x_m and alpha; distinguish normalized distribution from a tail approximation.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`). Chapter-6 teaching/Python done; Lean skipped for toolchain/network limits.

- **numeric-demo:** Compare simulated exceedances with the stated survival law.
- **lean-verifiable:** Density, survival, and support identities admit exact analysis.

Coverage: Chapter-6 teaching and bounded Python implemented; separate max review complete with numerical-domain and caption fixes; no checked Lean. See [chapter-6 evidence](../../records/incerto-scft-v4-ch06.md).

Prerequisites: none within this inventory.

Technical source mappings: [SCoFT v4 ch. 2](inventory.md#scft-v4-ch02), [SCoFT v4 ch. 5](inventory.md#scft-v4-ch05), [SCoFT v4 appendix A](inventory.md#scft-v4-appa).

Chapter chunks: `scft-v4-ch02`, `scft-v4-ch05`, `scft-v4-ch06`.

<a id="c-regular-variation"></a>

## Regular variation (`c-regular-variation`)

Home: [content/incerto-regular-variation.md](../../../content/incerto-regular-variation.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Pointwise ratio limits at positive dilation; do not infer regular variation from a finite plot.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`). Chapter-5 teaching/Python done; Lean skipped for toolchain/network limits.

- **numeric-demo:** Ratios illustrate convergence and slowly varying corrections.
- **lean-verifiable:** Definitions and individual limit statements can be formalized.

Coverage: Chapter-5 teaching and deterministic worked cases implemented; separate max review complete with fixes; no checked Lean. See [chapter-5 evidence](../../records/incerto-scft-v4-ch05.md).

Prerequisites: [c-pareto](#c-pareto).

Technical source mappings: [SCoFT v4 ch. 5](inventory.md#scft-v4-ch05).

Chapter chunks: `scft-v4-ch05`.

<a id="c-karamata"></a>

## Karamata tail integrals (`c-karamata`)

Home: [content/incerto-karamata.md](../../../content/incerto-karamata.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

General theorem requires a library feasibility audit; p = alpha depends on the slowly varying factor.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`). Chapter-5 teaching/Python done; Lean skipped for toolchain/network limits.

- **numeric-demo:** Compare exact and truncated tail integrals in admissible regimes and at the boundary.
- **lean-verifiable:** The integral theorem needs explicit measurable and asymptotic hypotheses.

Coverage: Chapter-5 teaching and deterministic worked cases implemented; separate max review complete with fixes; no checked Lean. See [chapter-5 evidence](../../records/incerto-scft-v4-ch05.md).

Prerequisites: [c-regular-variation](#c-regular-variation).

Technical source mappings: [SCoFT v4 ch. 5](inventory.md#scft-v4-ch05).

Chapter chunks: `scft-v4-ch05`.

<a id="c-pareto-moments"></a>

## Pareto moment boundary (`c-pareto-moments`)

Home: [content/incerto-pareto-moment-existence.md](../../../content/incerto-pareto-moment-existence.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

For p > 0, the pth Pareto moment is finite exactly when p < alpha; handle equality separately.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`). Chapter-5 teaching/Python done; Lean skipped for toolchain/network limits.

- **numeric-demo:** Truncation plots distinguish finite estimates from finite population moments.
- **lean-verifiable:** Integrability and the exact positive-power integral have a small analytic scope.

Coverage: Chapter-5 teaching and deterministic worked cases implemented; separate max review complete with fixes; no checked Lean. See [chapter-5 evidence](../../records/incerto-scft-v4-ch05.md).

Prerequisites: [c-pareto](#c-pareto).

Technical source mappings: [SCoFT v4 ch. 5](inventory.md#scft-v4-ch05).

Chapter chunks: `scft-v4-ch05`.

<a id="c-mean-excess"></a>

## Mean excess (`c-mean-excess`)

Home: [content/incerto-mean-excess-function.md](../../../content/incerto-mean-excess-function.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Separate a population conditional mean from its sample diagnostic.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now` at chapter-9 scope).

- **numeric-demo:** Threshold curves compare exact models with finite samples.
- **lean-verifiable:** Conditional expectation formulas require positive exceedance probability and integrability.

Coverage: Chapter-9 teaching and Python complete; separate max review pending; no checked Lean.

Prerequisites: [c-pareto-moments](#c-pareto-moments).

Technical source mappings: [SCoFT v4 ch. 9](inventory.md#scft-v4-ch09).

Chapter chunks: `scft-v4-ch09`.

Chapter-9 teaching/Python complete; [checkpoint](../../records/incerto-scft-v4-ch09.md).
Separate max review and general theorem-source follow-ups remain pending.
Lean skipped at this scope.

<a id="c-hill"></a>

## Hill tail-index estimation (`c-hill`)

Home: [content/incerto-hill-estimator.md](../../../content/incerto-hill-estimator.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Do not claim general consistency without intermediate-sequence and tail conditions.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now` at chapter-9 scope).

- **numeric-demo:** Vary the number of upper order statistics to expose bias and noise.
- **lean-verifiable:** Exact Pareto log-transform identities can precede asymptotic theory.

Coverage: Chapter-9 teaching and Python complete; separate max review pending; no checked Lean.

Prerequisites: [c-regular-variation](#c-regular-variation).

Technical source mappings: [SCoFT v4 ch. 9](inventory.md#scft-v4-ch09), [SCoFT v4 appendix E](inventory.md#scft-v4-appe).

Chapter chunks: `scft-v4-ch09`.

Chapter-9 teaching/Python complete; [checkpoint](../../records/incerto-scft-v4-ch09.md).
Separate max review and general theorem-source follow-ups remain pending.
Lean skipped at this scope.

<a id="c-evi"></a>

## Extreme-value index (`c-evi`)

Home: [content/incerto-extreme-value-index.md](../../../content/incerto-extreme-value-index.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

xi = 1/alpha only in the positive regularly varying regime; other signs need separate domains.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now` at chapter-9 scope).

- **numeric-demo:** Work through positive, zero and negative index examples with explicit support.
- **lean-verifiable:** Domain-specific parameter relations are precise statements.

Coverage: Chapter-9 teaching and Python complete; separate max review pending; no checked Lean.

Prerequisites: none within this inventory.

Technical source mappings: [SCoFT v4 ch. 2](inventory.md#scft-v4-ch02), [SCoFT v4 ch. 9](inventory.md#scft-v4-ch09).

Chapter chunks: `scft-v4-ch02`, `scft-v4-ch09`.

Chapter-9 teaching/Python complete; [checkpoint](../../records/incerto-scft-v4-ch09.md).
Separate max review and general theorem-source follow-ups remain pending.
Lean skipped at this scope.

<a id="c-gpd"></a>

## Generalized Pareto excess models (`c-gpd`)

Home: [content/incerto-generalized-pareto.md](../../../content/incerto-generalized-pareto.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Distinguish xi = 0, xi > 0, and finite-endpoint xi < 0.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now` at chapter-9 scope).

- **numeric-demo:** Check support and exponential limit numerically.
- **lean-verifiable:** Support, survival, and exact threshold stability have explicit parameter cases.

Coverage: Chapter-9 teaching and Python complete; separate max review pending; no checked Lean.

Prerequisites: [c-evi](#c-evi).

Technical source mappings: [SCoFT v4 ch. 9](inventory.md#scft-v4-ch09).

Chapter chunks: `scft-v4-ch09`.

Chapter-9 teaching/Python complete; [checkpoint](../../records/incerto-scft-v4-ch09.md).
Separate max review and general theorem-source follow-ups remain pending.
Lean skipped at this scope.

<a id="c-plugin"></a>

## Plug-in tail estimation (`c-plugin`)

Home: [content/incerto-plug-in-tail-estimation.md](../../../content/incerto-plug-in-tail-estimation.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

The unregularized mean estimator has a pole at estimated xi = 1; no uniform MSE superiority.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now` at chapter-9 scope).

- **numeric-demo:** Compare sample and plug-in estimators on identical simulated samples.
- **lean-verifiable:** A specified Pareto estimator permits exact transforms and singularity analysis.

Coverage: Chapter-9 teaching and Python complete; separate max review pending; no checked Lean.

Prerequisites: [c-pareto-moments](#c-pareto-moments), [c-hill](#c-hill).

Technical source mappings: [SCoFT v4 appendix E](inventory.md#scft-v4-appe).

Chapter chunks: `scft-v4-ch09`.

Chapter-9 teaching/Python complete; [checkpoint](../../records/incerto-scft-v4-ch09.md).
Separate max review and general theorem-source follow-ups remain pending.
Lean skipped at this scope.

<a id="c-pbdh"></a>

## Threshold-limit theorem (`c-pbdh`)

Home: [content/incerto-pickands-balkema-de-haan.md](../../../content/incerto-pickands-balkema-de-haan.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Record the existing general result as cited; formalizing one excess identity does not certify the theorem.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now` at chapter-9 scope).

- **numeric-demo:** Illustrate threshold excess convergence and finite-threshold discrepancies in specified models.
- **lean-verifiable:** The general theorem is a substantial probability formalization; the exact Pareto case is smaller.

Coverage: Chapter-9 teaching and Python complete; separate max review pending; no checked Lean.

Prerequisites: [c-gpd](#c-gpd), [c-regular-variation](#c-regular-variation).

Technical source mappings: [SCoFT v4 ch. 9](inventory.md#scft-v4-ch09).

Chapter chunks: `scft-v4-ch09`.

Chapter-9 teaching/Python complete; [checkpoint](../../records/incerto-scft-v4-ch09.md).
Separate max review and general theorem-source follow-ups remain pending.
Lean skipped at this scope.

<a id="c-gev"></a>

## Generalized extreme-value laws (`c-gev`)

Home: [content/incerto-generalized-extreme-value.md](../../../content/incerto-generalized-extreme-value.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Specify the domain of attraction, centering, scaling, and convergence mode.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now` at chapter-9 scope).

- **numeric-demo:** Block-maxima experiments illustrate normalization sensitivity.
- **lean-verifiable:** Distribution formulas and maxima limits have separate proof obligations.

Coverage: Chapter-9 teaching and Python complete; separate max review pending; no checked Lean.

Prerequisites: [c-evi](#c-evi).

Technical source mappings: [SCoFT v4 ch. 9](inventory.md#scft-v4-ch09).

Chapter chunks: `scft-v4-ch09`.

Chapter-9 teaching/Python complete; [checkpoint](../../records/incerto-scft-v4-ch09.md).
Separate max review and general theorem-source follow-ups remain pending.
Lean skipped at this scope.

<a id="c-frechet"></a>

## Frechet maxima (`c-frechet`)

Home: [content/incerto-frechet.md](../../../content/incerto-frechet.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Positive tail exponent and explicit normalization; finite-n errors remain numerical.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now` at chapter-9 scope).

- **numeric-demo:** Compare normalized maxima with the limiting distribution.
- **lean-verifiable:** The Pareto maximum limit provides a bounded first EVT target.

Coverage: Chapter-9 teaching and Python complete; separate max review pending; no checked Lean.

Prerequisites: [c-pareto](#c-pareto), [c-gev](#c-gev).

Technical source mappings: [SCoFT v4 ch. 9](inventory.md#scft-v4-ch09).

Chapter chunks: `scft-v4-ch09`.

Chapter-9 teaching/Python complete; [checkpoint](../../records/incerto-scft-v4-ch09.md).
Separate max review and general theorem-source follow-ups remain pending.
Lean skipped at this scope.

<a id="c-subexponential"></a>

## Subexponential sums (`c-subexponential`)

Home: [content/incerto-subexponentiality.md](../../../content/incerto-subexponentiality.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Fixed n iid nonnegative variables; no automatic extension to growing n.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`). Chapter-5 teaching/Python done; Lean skipped for toolchain/network limits.

- **numeric-demo:** Compare the sum tail with a single-large-observation approximation.
- **lean-verifiable:** Convolution-tail statements need nonnegative support and fixed-sum hypotheses.

Coverage: Chapter-5 teaching and deterministic worked cases implemented; separate max review complete with fixes; no checked Lean. See [chapter-5 evidence](../../records/incerto-scft-v4-ch05.md).

Prerequisites: [c-regular-variation](#c-regular-variation).

Technical source mappings: [SCoFT v4 ch. 5](inventory.md#scft-v4-ch05).

Chapter chunks: `scft-v4-ch05`.

<a id="c-tail-ratio"></a>

## Survival-tail ratio diagnostic (`c-tail-ratio`)

Home: [content/incerto-survival-tail-ratio.md](../../../content/incerto-survival-tail-ratio.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Independence is required for a joint-exceedance interpretation.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`). Chapter-5 teaching/Python done; Lean skipped for toolchain/network limits.

- **numeric-demo:** Plot the diagnostic across models without treating it as a convolution proof.
- **lean-verifiable:** Specified survival-function ratios allow exact limit calculations.

Coverage: Chapter-5 teaching and deterministic worked cases implemented; separate max review complete with fixes; no checked Lean. See [chapter-5 evidence](../../records/incerto-scft-v4-ch05.md).

Prerequisites: [c-pareto](#c-pareto).

Technical source mappings: [SCoFT v4 ch. 5](inventory.md#scft-v4-ch05).

Chapter chunks: `scft-v4-ch05`.

<a id="c-max-sum"></a>

## Maximum-to-sum ratio (`c-max-sum`)

Home: [content/incerto-max-to-sum-ratio.md](../../../content/incerto-max-to-sum-ratio.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

A nondegenerate heavy-tail limit need not equal one; define zero-sum behavior.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`: no toolchain).

- **numeric-demo:** Compare finite-mean, alpha = 1, and alpha < 1 regimes.
- **lean-verifiable:** Finite positive-sum bounds are elementary; limit regimes need probability theory.

Coverage: Chapter-7 teaching and bounded Python implemented; separate max review pending; no checked Lean. See [chapter-7 evidence](../../records/incerto-scft-v4-ch07.md).

Prerequisites: [c-pareto-moments](#c-pareto-moments).

Technical source mappings: [SCoFT v4 ch. 7](inventory.md#scft-v4-ch07).

Chapter chunks: `scft-v4-ch07`.

<a id="c-double-pareto"></a>

## Symmetric shifted Pareto construction (`c-double-pareto`)

Home: [content/incerto-double-pareto.md](../../../content/incerto-double-pareto.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Preserve the existing shifted construction; symmetry alone does not imply an existing mean.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`). Chapter-5 teaching/Python done; Lean skipped for toolchain/network limits.

- **numeric-demo:** Symmetry and unstable averages can be illustrated independently.
- **lean-verifiable:** The stated sign-mixture construction has exact distribution and moment properties.

Coverage: Chapter-5 teaching and deterministic worked cases implemented; separate max review complete with fixes; no checked Lean. See [chapter-5 evidence](../../records/incerto-scft-v4-ch05.md).

Prerequisites: [c-pareto-moments](#c-pareto-moments).

Technical source mappings: [SCoFT v4 ch. 5](inventory.md#scft-v4-ch05).

Chapter chunks: `scft-v4-ch05`.

<a id="c-threshold"></a>

## Tail-threshold selection (`c-threshold`)

Home: [content/incerto-tail-threshold-selection.md](../../../content/incerto-tail-threshold-selection.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

No universal optimal threshold from a visually straight tail plot.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now` at chapter-9 scope).

- **numeric-demo:** Sensitivity curves show the bias and variance tradeoff.
- **empirical:** Real-data threshold choice requires dependence and model-fit diagnostics.
- **lean-verifiable:** The stated body-plus-tail example and threshold-stability identities have exact model-specific claims.

Coverage: Chapter-9 teaching and Python complete; separate max review pending; no checked Lean.

Prerequisites: [c-hill](#c-hill), [c-mean-excess](#c-mean-excess).

Technical source mappings: [SCoFT v4 ch. 9](inventory.md#scft-v4-ch09), [SCoFT v4 appendix E](inventory.md#scft-v4-appe).

Chapter chunks: `scft-v4-ch09`.

Chapter-9 teaching/Python complete; [checkpoint](../../records/incerto-scft-v4-ch09.md).
Separate max review and general theorem-source follow-ups remain pending.
Lean skipped at this scope.

<a id="c-body-shoulder"></a>

## Body, shoulder, and tail under perturbation (`c-body-shoulder`)

Home: [content/incerto-body-shoulder-tail.md](../../../content/incerto-body-shoulder-tail.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

The existing normal variance perturbation is not a universal tail-threshold rule.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Chapter-4 Lean: `skipped-for-now`. No Lean toolchain is installed and sandbox network is unavailable; no new checked declaration.

- **numeric-demo:** Original curves can display the signed effects.
- **lean-verifiable:** Density derivatives locate sign changes for a specified perturbation.

Coverage: Chapter-4 original teaching, numerical cases and separate max review done. See [chapter 4 evidence](../../records/incerto-scft-v4-ch04.md).

Prerequisites: none within this inventory.

Technical source mappings: [SCoFT v4 ch. 4](inventory.md#scft-v4-ch04).

Chapter chunks: `scft-v4-ch04`.

<a id="c-tail-geometry"></a>

## Multivariate tail geometry (`c-tail-geometry`)

Home: [content/incerto-iso-density-tail-geometry.md](../../../content/incerto-iso-density-tail-geometry.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Point density and probability mass must remain distinct.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`). Chapter-6 teaching/Python done; Lean skipped for toolchain/network limits.

- **numeric-demo:** Compare contours and integrated regional probabilities.
- **lean-verifiable:** Product-density comparisons are exact under their independence assumptions.

Coverage: Chapter-6 teaching and bounded Python implemented; separate max review complete with numerical-domain and caption fixes; no checked Lean. See [chapter-6 evidence](../../records/incerto-scft-v4-ch06.md).

Prerequisites: [c-pareto](#c-pareto).

Technical source mappings: [SCoFT v4 ch. 6](inventory.md#scft-v4-ch06).

Chapter chunks: `scft-v4-ch06`.

<a id="c-cramer"></a>

## Exponential-moment gate (`c-cramer`)

Home: [content/incerto-cramer-condition.md](../../../content/incerto-cramer-condition.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

An exponential-moment condition and a Chernoff bound do not prove a full large-deviation principle.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`: no toolchain).

- **numeric-demo:** Compare exponential and power-law tail bounds.
- **lean-verifiable:** Markov/Chernoff bounds are formalizable with finite exponential moments.

Coverage: Chapter-7 teaching and bounded Python implemented; separate max review pending; no checked Lean. See [chapter-7 evidence](../../records/incerto-scft-v4-ch07.md).

Prerequisites: none within this inventory.

Technical source mappings: [SCoFT v4 appendix D](inventory.md#scft-v4-appd).

Chapter chunks: `scft-v4-ch07`.

<a id="c-stable-clt"></a>

## Stable limits for sums (`c-stable-clt`)

Home: [content/incerto-generalized-central-limit-theorem.md](../../../content/incerto-generalized-central-limit-theorem.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Handle alpha = 1 centering and slowly varying factors explicitly.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`: no toolchain).

- **numeric-demo:** Simulations compare Gaussian and stable scaling.
- **lean-verifiable:** Stable attraction is an advanced formalization with explicit centering and scaling.

Coverage: Chapter-7 teaching and bounded Python implemented; separate max review pending; no checked Lean. See [chapter-7 evidence](../../records/incerto-scft-v4-ch07.md).

Prerequisites: [c-regular-variation](#c-regular-variation).

Technical source mappings: [SCoFT v4 ch. 7](inventory.md#scft-v4-ch07).

Chapter chunks: `scft-v4-ch07`.

<a id="c-lln-failure"></a>

## Failure of finite-mean averaging assumptions (`c-lln-failure`)

Home: [content/incerto-lln-failure.md](../../../content/incerto-lln-failure.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

The existing nonnegative divergence result does not apply to symmetric Cauchy sums.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`: no toolchain).

- **numeric-demo:** Compare with a two-sided Cauchy example without conflating the arguments.
- **lean-verifiable:** Nonnegative iid infinite-mean divergence has a precise theorem statement.

Coverage: Chapter-7 teaching and bounded Python implemented; separate max review pending; no checked Lean. See [chapter-7 evidence](../../records/incerto-scft-v4-ch07.md).

Prerequisites: none within this inventory.

Technical source mappings: [SCoFT v4 ch. 7](inventory.md#scft-v4-ch07).

Chapter chunks: `scft-v4-ch07`.

<a id="c-tail-catalog"></a>

## Tail classes and implication boundaries (`c-tail-catalog`)

Home: [content/incerto-tail-class-catalog.md](../../../content/incerto-tail-class-catalog.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Keep cited class memberships separate from the elementary convolution derivation and exact ratio checks.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`). Chapter-6 teaching/Python done; Lean skipped for toolchain/network limits.

- **numeric-demo:** Population tail-ratio curves illustrate distinct asymptotic classes.
- **lean-verifiable:** The convolution decomposition and exact light-tail ratios are precise proof targets.

Coverage: Chapter-6 teaching and bounded Python implemented; separate max review complete with numerical-domain and caption fixes; no checked Lean. See [chapter-6 evidence](../../records/incerto-scft-v4-ch06.md).

Prerequisites: [c-regular-variation](#c-regular-variation), [c-subexponential](#c-subexponential), [c-cramer](#c-cramer).

Technical source mappings: [SCoFT v4 ch. 1](inventory.md#scft-v4-ch01), [SCoFT v4 ch. 2](inventory.md#scft-v4-ch02), [SCoFT v4 appendix A](inventory.md#scft-v4-appa), [SCoFT v4 appendix B](inventory.md#scft-v4-appb).

Chapter chunks: `scft-v4-ch01`, `scft-v4-ch02`, `scft-v4-ch05`, `scft-v4-ch06`.

<a id="c-luck-skill"></a>

## Luck, skill, and performance selection (`c-luck-skill`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-luck-skill.md`; no page is scheduled.

Former scope (inactive): Separate ex ante ability, realized payoff, and selection on realized payoff.

Former evidence candidates (inactive):

- **numeric-demo:** A controlled population exposes selection effects.
- **empirical:** Observed performance needs a specified null and selection process.
- **prose-only:** Attributing success involves causal assumptions beyond the simulation.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): none within this inventory.

<a id="c-counterfactuals"></a>

## Alternative histories and decision quality (`c-counterfactuals`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-counterfactuals.md`; no page is scheduled.

Former scope (inactive): State the generative assumptions and the chosen loss or utility.

Former evidence candidates (inactive):

- **numeric-demo:** Repeated simulated paths compare decisions under the same model.
- **prose-only:** A single realized history cannot identify every counterfactual.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): none within this inventory.

<a id="c-noise-monitoring"></a>

## Observation frequency and noise (`c-noise-monitoring`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-max`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-noise-monitoring.md`; no page is scheduled.

Former scope (inactive): No universal claim that frequent observation is harmful.

Former evidence candidates (inactive):

- **numeric-demo:** Change monitoring frequency while holding the path model fixed.
- **lean-verifiable:** Signal/noise scaling can be proved for a specified independent-increment model.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): [c-counterfactuals](#c-counterfactuals).

<a id="c-survivorship"></a>

## Survivorship and silent evidence (`c-survivorship`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-max`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-survivorship.md`; no page is scheduled.

Former scope (inactive): Distinguish truncation, censoring, selection, and unobserved failures.

Former evidence candidates (inactive):

- **numeric-demo:** Simulate observed survivors and the full cohort.
- **empirical:** Historical missingness requires a documented observation model.
- **lean-verifiable:** Finite conditional-probability examples can establish selection bias.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): [c-luck-skill](#c-luck-skill).

<a id="c-asymmetric-payoffs"></a>

## Asymmetric payoffs and exposure (`c-asymmetric-payoffs`)

Home: `content/incerto-asymmetric-payoffs.md` (existing). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Expected payoff statements require integrability; a high hit rate is insufficient.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: No Lean toolchain is installed and sandbox network is unavailable; teaching and numerical evidence take priority. No new checked declaration.

- **numeric-demo:** Use original examples with visible rare-loss exposure.
- **lean-verifiable:** Finite payoff tables separate win probability from expected payoff.

Coverage: Original chapter-3 teaching and exact Python cases complete. Max review is complete; external build and live reader review remain pending; see [chapter 3 evidence](../../records/incerto-scft-v4-ch03.md).

Prerequisites: none within this inventory.

Technical source mappings: [SCoFT v4 ch. 3](inventory.md#scft-v4-ch03).

Chapter chunks: `scft-v4-ch03`.

<a id="c-induction"></a>

## Induction and limits of finite evidence (`c-induction`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Interpretive, ethical or behavioral coverage is outside the mathematical completion scope, including contextual associations in technical sources.

Retained reservation: `content/incerto-induction.md`; no page is scheduled.

Former scope (inactive): Separate logical underdetermination from model-relative confidence statements.

Former evidence candidates (inactive):

- **prose-only:** The philosophical problem cannot be settled by a finite statistical theorem.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): none within this inventory.

Technical source mappings (context only): [SCoFT v4 ch. 1](inventory.md#scft-v4-ch01).

<a id="c-multiple-testing"></a>

## Search, multiple testing, and regression effects (`c-multiple-testing`)

Home: `content/incerto-multiple-testing.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Selection must be included when interpreting a reported winner.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Repeat the full search procedure under a declared null.
- **lean-verifiable:** Finite-family error bounds and a specified regression example are formalizable.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

Technical source mappings: [SCoFT v4 ch. 22](inventory.md#scft-v4-ch22).

Chapter chunks: `scft-v4-ch22`.

<a id="c-path-dependence"></a>

## Reinforcement and path-dependent outcomes (`c-path-dependence`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-path-dependence.md`; no page is scheduled.

Former scope (inactive): A toy process is not a universal explanation of social concentration.

Former evidence candidates (inactive):

- **numeric-demo:** A specified urn or preferential-attachment process demonstrates one mechanism.
- **empirical:** Claims about actual inequality need data and alternative mechanisms.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): none within this inventory.

<a id="c-biases"></a>

## Probability judgments and cognitive biases (`c-biases`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Interpretive, ethical or behavioral coverage is outside the mathematical completion scope, including contextual associations in technical sources.

Retained reservation: `content/incerto-biases.md`; no page is scheduled.

Former scope (inactive): Keep normative probability arithmetic distinct from claims about human behavior.

Former evidence candidates (inactive):

- **empirical:** Psychological generalizations require primary studies and replication review.
- **prose-only:** Explain the reasoning error without asserting its empirical prevalence.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): none within this inventory.

Technical source mappings (context only): [SCoFT v4 appendix I](inventory.md#scft-v4-appi).

<a id="c-causal-narrative"></a>

## Narrative explanations and causal identification (`c-causal-narrative`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-causal-narrative.md`; no page is scheduled.

Former scope (inactive): Do not infer causation from a fitted story or a retrospective sequence.

Former evidence candidates (inactive):

- **numeric-demo:** Observationally similar simulated models can have different interventions.
- **prose-only:** Discuss what observations do and do not distinguish.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): none within this inventory.

<a id="c-skepticism"></a>

## Fallibility and practical skepticism (`c-skepticism`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-skepticism.md`; no page is scheduled.

Former scope (inactive): Distinguish uncertainty about a model from uncertainty within it.

Former evidence candidates (inactive):

- **prose-only:** This is an epistemic stance, not a universal probability theorem.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): none within this inventory.

<a id="c-stoicism"></a>

## Control, dignity, and responses to chance (`c-stoicism`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-stoicism.md`; no page is scheduled.

Former scope (inactive): Use original commentary and cited chapter locators; no aphorism collection.

Former evidence candidates (inactive):

- **prose-only:** These are ethical and interpretive arguments.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): none within this inventory.

<a id="c-scalability"></a>

## Scalable outcomes and concentration (`c-scalability`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-max`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-scalability.md`; no page is scheduled.

Former scope (inactive): Do not treat occupational labels as distributional assumptions.

Former evidence candidates (inactive):

- **numeric-demo:** Compare bounded and unbounded-support model families.
- **lean-verifiable:** Specified finite payoff and aggregation examples can be checked.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): [c-asymmetric-payoffs](#c-asymmetric-payoffs).

<a id="c-black-swan"></a>

## Surprise, impact, and retrospective explanation (`c-black-swan`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-black-swan.md`; no page is scheduled.

Former scope (inactive): A surprising event is not automatically a power-law observation.

Former evidence candidates (inactive):

- **prose-only:** Define the observer-relative concept and its limits.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): [c-induction](#c-induction), [c-causal-narrative](#c-causal-narrative).

<a id="c-ludic"></a>

## Model boundaries and domain transfer (`c-ludic`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-ludic.md`; no page is scheduled.

Former scope (inactive): Do not use a model-boundary critique as evidence for a particular alternative law.

Former evidence candidates (inactive):

- **prose-only:** Assess omitted mechanisms and the limits of closed-world games.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): none within this inventory.

<a id="c-forecasting"></a>

## Prediction limits and forecast evaluation (`c-forecasting`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-forecasting.md`; no page is scheduled.

Former scope (inactive): Score distributions and decisions separately; distinguish impossibility from poor calibration.

Former evidence candidates (inactive):

- **numeric-demo:** Simulate horizon and parameter uncertainty.
- **empirical:** Skill claims need dated forecasts, baselines, and leakage control.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): none within this inventory.

<a id="c-epistemic-uncertainty"></a>

## Model uncertainty and unseen mechanisms (`c-epistemic-uncertainty`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-epistemic-uncertainty.md`; no page is scheduled.

Former scope (inactive): Do not assign an unsupported probability to unknown model classes.

Former evidence candidates (inactive):

- **numeric-demo:** Compare predictions across explicitly declared model families.
- **prose-only:** Classify what the model leaves unspecified.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): [c-skepticism](#c-skepticism).

<a id="c-tacit-knowledge"></a>

## Practice, tacit knowledge, and explicit models (`c-tacit-knowledge`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Interpretive, ethical or behavioral coverage is outside the mathematical completion scope, including contextual associations in technical sources.

Retained reservation: `content/incerto-tacit-knowledge.md`; no page is scheduled.

Former scope (inactive): Distinguish an account of discovery from a mathematical justification.

Former evidence candidates (inactive):

- **prose-only:** Historical and philosophical claims need attribution and counterexamples.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): none within this inventory.

Technical source mappings (context only): [SCoFT v4 ch. 26](inventory.md#scft-v4-ch26).

<a id="c-procrustean"></a>

## Category fit and forced measurement (`c-procrustean`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-procrustean.md`; no page is scheduled.

Former scope (inactive): Discuss the aphoristic themes in original prose; no close paraphrase or reconstructed aphorisms.

Former evidence candidates (inactive):

- **prose-only:** Evaluate the choice of categories and what they erase.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): none within this inventory.

<a id="c-aesthetics"></a>

## Aesthetic judgment and intellectual style (`c-aesthetics`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-aesthetics.md`; no page is scheduled.

Former scope (inactive): Separate taste, rhetoric, and factual historical assertions.

Former evidence candidates (inactive):

- **prose-only:** Interpretive commentary has no theorem-like truth condition.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): none within this inventory.

<a id="c-jensen"></a>

## Convexity and Jensen effects (`c-jensen`)

Home: `content/incerto-jensen.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Distinguish payoff curvature from a full claim about welfare or survival.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Mean-preserving perturbations illustrate expectation changes.
- **lean-verifiable:** Convexity inequalities have exact domain and integrability conditions.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

Technical source mappings: [SCoFT v4 ch. 28](inventory.md#scft-v4-ch28), [`paper-fragility`](inventory.md#paper-fragility), [`paper-convex-response`](inventory.md#paper-convex-response).

Chapter chunks: `scft-v4-ch28`.

<a id="c-fragility"></a>

## Sensitivity-based fragility (`c-fragility`)

Home: `content/incerto-fragility.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Specify response, adverse region, dispersion parameter, and derivative existence.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Finite differences reveal dependence on the perturbation family.
- **lean-verifiable:** A chosen distribution family and response functional give a checkable sensitivity.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-jensen](#c-jensen), [c-asymmetric-payoffs](#c-asymmetric-payoffs).

Technical source mappings: [`paper-fragility`](inventory.md#paper-fragility).

Chapter chunks: `scft-v4-ch28`.

<a id="c-hormesis"></a>

## Dose response and adaptation (`c-hormesis`)

Home: `content/incerto-hormesis.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-xhigh`.

Teach and illustrate the declared dose-response function, curvature and perturbation assumptions; clinical benefit and biological interpretation are outside completion scope.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: No exact declaration selected for this numerical or empirical treatment; teaching and Python evidence take priority.

- **numeric-demo:** A declared response curve separates local convexity from global effects.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-jensen](#c-jensen).

Technical source mappings: [`paper-convex-response`](inventory.md#paper-convex-response).

Chapter chunks: `scft-v4-ch28`.

<a id="c-selection-levels"></a>

## Individual failure and population adaptation (`c-selection-levels`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-selection-levels.md`; no page is scheduled.

Former scope (inactive): Specify whose outcome is improved, at what cost, and on which time scale.

Former evidence candidates (inactive):

- **numeric-demo:** A branching or replacement toy model separates levels of aggregation.
- **prose-only:** Ethical consequences do not follow from aggregate fitness.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): [c-survivorship](#c-survivorship).

<a id="c-decentralization"></a>

## Redundancy, size, and decentralized exposure (`c-decentralization`)

Home: `content/incerto-decentralization.md` (existing). Status: **done**. Milestone: **M1**. Lead: `astra-xhigh`.

Teach finite aggregation and dependence models from the technical paper; numerical stress cases do not establish institutional or normative conclusions.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: No Lean toolchain is installed and sandbox network is unavailable; teaching and numerical evidence take priority. No new checked declaration.

- **numeric-demo:** Network and concentration models permit controlled stress experiments.

Coverage: Original chapter-3 teaching and exact Python cases complete. Max review is complete; external build and live reader review remain pending; see [chapter 3 evidence](../../records/incerto-scft-v4-ch03.md).

Prerequisites: none within this inventory.

Technical source mappings: [`paper-precaution`](inventory.md#paper-precaution).

Chapter chunks: `scft-v4-ch03`.

<a id="c-iatrogenics"></a>

## Intervention error and subtractive decisions (`c-iatrogenics`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-iatrogenics.md`; no page is scheduled.

Former scope (inactive): Do not convert a medical illustration into treatment advice.

Former evidence candidates (inactive):

- **numeric-demo:** Compare actions under explicit error costs and uncertain treatment effects.
- **empirical:** Claims of harm require suitable causal evidence.
- **prose-only:** A preference for restraint remains a decision rule with assumptions.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): [c-epistemic-uncertainty](#c-epistemic-uncertainty).

<a id="c-barbell"></a>

## Bounded downside and barbell allocations (`c-barbell`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-max`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-barbell.md`; no page is scheduled.

Former scope (inactive): Specify default, leverage, funding, and admissible losses; no investment prescription.

Former evidence candidates (inactive):

- **numeric-demo:** Compare payoff distributions with the same budget constraints.
- **lean-verifiable:** A specified finite allocation gives exact payoff bounds.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): [c-asymmetric-payoffs](#c-asymmetric-payoffs), [c-ruin](#c-ruin).

<a id="c-optionality"></a>

## Optionality and asymmetric experimentation (`c-optionality`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-max`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-optionality.md`; no page is scheduled.

Former scope (inactive): An option with costs or constraints need not be beneficial in every model.

Former evidence candidates (inactive):

- **numeric-demo:** Simulate exploration under explicit costs and stopping rules.
- **lean-verifiable:** Taking a maximum over available actions gives precise order inequalities.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): [c-asymmetric-payoffs](#c-asymmetric-payoffs).

<a id="c-lindy"></a>

## Conditional lifetime and Lindy models (`c-lindy`)

Home: `content/incerto-lindy.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Explain the specified absorbing-barrier model, survival conditioning and drift assumptions in v4 chapter 23. Distinguish this process from a Pareto lifetime formula; no universal age law or historical longevity claim.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

Lean `skipped-for-now` for continuous-time absorption and drift-change claims: Pinned stochastic-calculus library support has not been established; this does not block teaching or simulations.

- **numeric-demo:** Bounded repeated paths compare survival, distance from absorption and drift, with censoring and grid effects explicit.
- **lean-verifiable:** Exact finite-state absorption or scoped conditional-survival identities are candidates; continuous-time passage results require a separate feasibility audit.

Coverage: Reactivated at a technical scope from v4 chapter 23; no existing page, simulation or checked Lean.

Prerequisites: [c-ruin](#c-ruin), [c-pareto-moments](#c-pareto-moments).

Technical source mappings: [SCoFT v4 ch. 23](inventory.md#scft-v4-ch23).

Chapter chunks: `scft-v4-ch23`.

<a id="c-agency"></a>

## Agency, incentives, and risk transfer (`c-agency`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-max`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-agency.md`; no page is scheduled.

Former scope (inactive): State who bears losses, observes actions, and can leave.

Former evidence candidates (inactive):

- **numeric-demo:** Compare reward rules on identical outcome paths.
- **lean-verifiable:** A finite principal-agent model can check incentive inequalities.
- **prose-only:** Fairness and responsibility remain normative questions.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): [c-asymmetric-payoffs](#c-asymmetric-payoffs).

<a id="c-minority-rule"></a>

## Threshold preferences and collective outcomes (`c-minority-rule`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-minority-rule.md`; no page is scheduled.

Former scope (inactive): Do not infer a universal sociological law from a threshold toy model.

Former evidence candidates (inactive):

- **numeric-demo:** A finite mixing model illustrates parameter-dependent collective effects.
- **empirical:** Applications need actual network and preference data.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): [c-path-dependence](#c-path-dependence).

<a id="c-costly-signals"></a>

## Commitment, signals, and revealed preferences (`c-costly-signals`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-max`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-costly-signals.md`; no page is scheduled.

Former scope (inactive): Separate an equilibrium calculation from claims about real motives.

Former evidence candidates (inactive):

- **lean-verifiable:** Specified signaling games admit finite incentive checks.
- **prose-only:** Actions need not uniquely reveal beliefs or values.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): [c-agency](#c-agency).

<a id="c-inequality-mobility"></a>

## Inequality, mobility, and population definitions (`c-inequality-mobility`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-inequality-mobility.md`; no page is scheduled.

Former scope (inactive): Fix units, population entry/exit, and observation windows.

Former evidence candidates (inactive):

- **numeric-demo:** Simulate equal marginals with different mobility.
- **empirical:** Cross-sectional concentration and transitions require different data.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): [c-path-dependence](#c-path-dependence).

<a id="c-ethics"></a>

## Reciprocity, responsibility, and professional ethics (`c-ethics`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Interpretive, ethical or behavioral coverage is outside the mathematical completion scope, including contextual associations in technical sources.

Retained reservation: `content/incerto-ethics.md`; no page is scheduled.

Former scope (inactive): A formal payoff model cannot verify a moral conclusion.

Former evidence candidates (inactive):

- **prose-only:** These are ethical arguments and institutional judgments.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): [c-agency](#c-agency).

Technical source mappings (context only): [`paper-precaution`](inventory.md#paper-precaution).

<a id="c-rationality"></a>

## Rationality as an explicit decision criterion (`c-rationality`)

Status: **out-of-scope**. No milestone or deliverables. Former lead: `astra-xhigh`.

Exclusion reason: Mapped only to the five excluded non-technical books; no technical-source mathematical deliverable is currently selected.

Retained reservation: `content/incerto-rationality.md`; no page is scheduled.

Former scope (inactive): State the criterion and information set before calling an action rational.

Former evidence candidates (inactive):

- **numeric-demo:** Counterexamples expose differences between decision criteria.
- **prose-only:** Compare consistency, survival, and welfare criteria without equating them.

Coverage: No existing page; the reserved path is retained only for stable references. No deliverable is scheduled.

Historical prerequisites (inactive): none within this inventory.

<a id="c-ruin"></a>

## Ruin and repeated exposure (`c-ruin`)

Home: `content/incerto-ruin.md` (existing). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

No almost-sure ruin claim from unspecified dependence or a merely positive time-varying hazard.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: No Lean toolchain is installed and sandbox network is unavailable; teaching and numerical evidence take priority. No new checked declaration.

- **numeric-demo:** Compare finite-horizon outcomes and dependence assumptions.
- **lean-verifiable:** Independent repeated trials with fixed positive ruin probability give an exact finite-horizon formula and limit.

Coverage: Original chapter-3 teaching and exact Python cases complete. Max review is complete; external build and live reader review remain pending; see [chapter 3 evidence](../../records/incerto-scft-v4-ch03.md).

Prerequisites: none within this inventory.

Technical source mappings: [SCoFT v4 ch. 3](inventory.md#scft-v4-ch03), [`paper-precaution`](inventory.md#paper-precaution).

Chapter chunks: `scft-v4-ch03`.

<a id="c-ergodicity"></a>

## Time averages and ensemble averages (`c-ergodicity`)

Home: [content/incerto-ergodicity.md](../../../content/incerto-ergodicity.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Separate ergodic theorems, absorbing ruin, and a chosen growth objective.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`: no toolchain).

- **numeric-demo:** Compare cross-sectional wealth with one path through time.
- **lean-verifiable:** Finite multiplicative examples and scoped log-growth results are formalizable.

Coverage: Chapter-7 teaching and bounded Python implemented; separate max review pending; no checked Lean. See [chapter-7 evidence](../../records/incerto-scft-v4-ch07.md).

Prerequisites: [c-ruin](#c-ruin).

Technical source mappings: [SCoFT v4 appendix C](inventory.md#scft-v4-appc).

Chapter chunks: `scft-v4-ch07`.

<a id="c-moment-estimation"></a>

## Moment-estimation failure (`c-moment-estimation`)

Home: [content/incerto-moment-estimation.md](../../../content/incerto-moment-estimation.md) (existing). Status: **in-progress**. Milestone: **M1**. Lead: `astra-max`.

Start with Pareto regimes and the existing plug-in singularity; no universal estimator ranking.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

Chapter-4 Lean: `skipped-for-now`. No Lean toolchain is installed and sandbox network is unavailable; no new checked declaration.

- **numeric-demo:** Run bounded, reproducible repeated-sample comparisons.
- **lean-verifiable:** Separate moment existence from estimator integrability and consistency.

Coverage: Chapters 4 and 8 implemented; chapter-4 max review complete,
chapter-8 max review pending. Chapter 28 remains. See
[chapter 4 evidence](../../records/incerto-scft-v4-ch04.md) and
[chapter 8 evidence](../../records/incerto-scft-v4-ch08.md).
Chapter-8 Lean is `skipped-for-now` as requested; no new checked declaration.

Prerequisites: [c-pareto-moments](#c-pareto-moments), [c-plugin](#c-plugin).

Technical source mappings: [SCoFT v4 ch. 4](inventory.md#scft-v4-ch04), [SCoFT v4 ch. 28](inventory.md#scft-v4-ch28), [`paper-kappa`](inventory.md#paper-kappa).

Chapter chunks: `scft-v4-ch04`, `scft-v4-ch08`, `scft-v4-ch28`.

<a id="c-inference-asymmetry"></a>

## Finite-sample evidence and tail non-identification (`c-inference-asymmetry`)

Home: `content/incerto-inference-asymmetry.md` (existing). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Quantify sample size, contamination probability, distance, and the moment that differs.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: No Lean toolchain is installed and sandbox network is unavailable; teaching and numerical evidence take priority. No new checked declaration.

- **numeric-demo:** Compare models indistinguishable in most finite samples.
- **lean-verifiable:** Construct a specified rare-contamination counterexample with controlled sample discrepancy.

Coverage: Original chapter-3 teaching and exact Python cases complete. Max review is complete; external build and live reader review remain pending; see [chapter 3 evidence](../../records/incerto-scft-v4-ch03.md).

Prerequisites: [c-exceedances](#c-exceedances), [c-moment-estimation](#c-moment-estimation).

Technical source mappings: [SCoFT v4 ch. 3](inventory.md#scft-v4-ch03).

Chapter chunks: `scft-v4-ch03`.

<a id="c-cauchy-running"></a>

## Cauchy running statistics (`c-cauchy-running`)

Home: [content/incerto-cauchy-running.md](../../../content/incerto-cauchy-running.md). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Bounded-runtime synthetic experiment with repeated Cauchy paths; attach to v4 chapter 7 (sections 7.2.1 and 7.6). The legacy Chapter 4 label was incorrect; no population-moment inference from finite machine outputs.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`: no toolchain).

- **numeric-demo:** Fixed-seed repeated paths expose unstable averages and Monte Carlo uncertainty.
- **lean-verifiable:** Distributional stability is a separate later theorem candidate.

Coverage: Chapter-7 teaching and bounded Python implemented; separate max review pending; no checked Lean. See [chapter-7 evidence](../../records/incerto-scft-v4-ch07.md).

Prerequisites: [c-stable-clt](#c-stable-clt), [c-lln-failure](#c-lln-failure).

Technical source mappings: [SCoFT v4 ch. 7](inventory.md#scft-v4-ch07).

Chapter chunks: `scft-v4-ch07`.

<a id="c-mixture-uncertainty"></a>

## Parameter mixtures and recursive uncertainty (`c-mixture-uncertainty`)

Home: [content/incerto-mixture-uncertainty.md](../../../content/incerto-mixture-uncertainty.md). Status: **in-progress**. Milestone: **M1**. Lead: `astra-max`.

Reuse Normix mixture definitions; a recursive construction needs an explicit limiting model.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

Chapter-4 Lean: `skipped-for-now`. No Lean toolchain is installed and sandbox network is unavailable; no new checked declaration.

- **numeric-demo:** Simulate a declared finite hierarchy of parameter uncertainty.
- **lean-verifiable:** Specified mixtures permit moment and tail calculations.

Coverage: Chapter-7 teaching and bounded Python implemented; separate max review pending; no checked Lean. Chapter-20 extension remains. See [chapter-7 evidence](../../records/incerto-scft-v4-ch07.md).

Prerequisites: [c-pareto-moments](#c-pareto-moments).

Technical source mappings: [SCoFT v4 ch. 4](inventory.md#scft-v4-ch04), [SCoFT v4 ch. 20](inventory.md#scft-v4-ch20), [SCoFT v4 appendix C](inventory.md#scft-v4-appc).

Chapter chunks: `scft-v4-ch04`, `scft-v4-ch07`, `scft-v4-ch20`.

<a id="c-multivariate-tails"></a>

## Multivariate tails and dependence summaries (`c-multivariate-tails`)

Home: [content/incerto-multivariate-tails.md](../../../content/incerto-multivariate-tails.md). Status: **in-progress**. Milestone: **M1**. Lead: `astra-max`.

PCA and covariance interpretations require moments; mutual information needs its own existence checks.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`). Chapter-6 teaching/Python done; Lean skipped for toolchain/network limits.

- **numeric-demo:** Contrast correlation, tail dependence, and geometric diagnostics.
- **lean-verifiable:** A specified model can test existence of covariance and validity of dependence formulas.

Coverage: Chapter-6 teaching and bounded Python implemented; separate max review complete with numerical-domain and caption fixes; no checked Lean. Chapter-29 extension remains. See [chapter-6 evidence](../../records/incerto-scft-v4-ch06.md).

Prerequisites: [c-tail-geometry](#c-tail-geometry), [c-mixture-uncertainty](#c-mixture-uncertainty).

Technical source mappings: [SCoFT v4 ch. 6](inventory.md#scft-v4-ch06), [SCoFT v4 ch. 29](inventory.md#scft-v4-ch29).

Chapter chunks: `scft-v4-ch06`, `scft-v4-ch29`.

<a id="c-kappa"></a>

## Finite-sum concentration metric (`c-kappa`)

Home: [content/incerto-kappa.md](../../../content/incerto-kappa.md) (existing). Status: **done**. Milestone: **M1**. Lead: `astra-max`.

Do not extend the metric to undefined moments or claim a universal sample-size guarantee.

Deliverables: website math (required, done) → Python (required, done) → Lean
(optional; `skipped-for-now` as requested, no new checked declaration).

- **numeric-demo:** Estimate it over declared finite aggregation sizes.
- **lean-verifiable:** Re-derive the selected paper metric under its finite-first-moment assumptions.

Coverage: Chapter-8 teaching, exact formulas and bounded numerical examples
implemented; separate max review pending; no checked Lean. See
[chapter 8 evidence](../../records/incerto-scft-v4-ch08.md).

Prerequisites: [c-pareto-moments](#c-pareto-moments), [c-stable-clt](#c-stable-clt).

Technical source mappings: [SCoFT v4 ch. 8](inventory.md#scft-v4-ch08), [`paper-kappa`](inventory.md#paper-kappa).

Chapter chunks: `scft-v4-ch08`.

<a id="c-sp500"></a>

## Equity-return tail study (`c-sp500`)

Home: [content/incerto-sp500.md](../../../content/incerto-sp500.md). Status: **in-progress**. Milestone: **M1**. Lead: `astra-xhigh`.

Record price adjustments, sampling interval, nonstationarity, dependence, and data rights.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: No exact declaration selected for this numerical or empirical treatment; teaching and Python evidence take priority.

- **empirical:** An actual return series permits a reproducible, dated model comparison.

Coverage: Chapter-10 teaching and Python implemented; empirical evaluation awaits an authorized S&P cache. Separate max review remains pending.

[Chapter-10 checkpoint](../../records/incerto-scft-v4-ch10.md).

Prerequisites: [c-threshold](#c-threshold), [c-moment-estimation](#c-moment-estimation).

Technical source mappings: [SCoFT v4 ch. 10](inventory.md#scft-v4-ch10).

Chapter chunks: `scft-v4-ch10`.

<a id="c-calibration-payoff"></a>

## Probability calibration versus payoff accuracy (`c-calibration-payoff`)

Home: `content/incerto-calibration-payoff.md` (existing). Status: **in-progress**. Milestone: **M1**. Lead: `astra-xhigh`.

A calibrated event forecast need not estimate an unbounded payoff well.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Compare scoring rules and payoff errors under the same forecasts.
- **lean-verifiable:** Finite examples separate event probabilities from magnitude-sensitive expectations.

Coverage: Chapter-11 teaching and deterministic model examples implemented; later scft-v4-ch13 scope and separate max review remain. No checked Lean.

Prerequisites: [c-asymmetric-payoffs](#c-asymmetric-payoffs), [c-moment-estimation](#c-moment-estimation).

Technical source mappings: [SCoFT v4 ch. 11](inventory.md#scft-v4-ch11), [SCoFT v4 ch. 13](inventory.md#scft-v4-ch13).

Chapter chunks: `scft-v4-ch11`, `scft-v4-ch13`.

Chapter-11 scope: teaching and Python **done**; Lean **skipped-for-now**.
Separate max review and later chapter scope remain; see the
[chapter-11 checkpoint](../../records/incerto-scft-v4-ch11.md).

<a id="c-forecast-martingale"></a>

## Forecast updating and martingale constraints (`c-forecast-martingale`)

Home: `content/incerto-forecast-martingale.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Changing information sets or forecasting systems can break a naive empirical comparison.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Simulate conditional forecast updates under an explicit filtration before empirical comparison.
- **empirical:** Timestamped forecasts allow model-dependent diagnostics.
- **lean-verifiable:** Conditional probabilities under one filtration satisfy scoped martingale identities.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-calibration-payoff](#c-calibration-payoff).

Technical source mappings: [SCoFT v4 ch. 14](inventory.md#scft-v4-ch14).

Chapter chunks: `scft-v4-ch14`.

<a id="c-gini"></a>

## Gini estimation with heavy tails (`c-gini`)

Home: `content/incerto-gini.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Infinite variance and infinite mean are different regimes. Define the measured population and nonnegative observations locally; no mobility or social-interpretation note is required.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Compare finite-sample bias under stated Pareto regimes.
- **empirical:** Application needs population and measurement definitions.
- **lean-verifiable:** Population and estimator properties require nonnegative values and a finite positive mean.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pareto-moments](#c-pareto-moments).

Technical source mappings: [SCoFT v4 ch. 15](inventory.md#scft-v4-ch15), [`paper-gini`](inventory.md#paper-gini).

Chapter chunks: `scft-v4-ch15`.

<a id="c-quantile-share"></a>

## Quantile contributions and aggregation bias (`c-quantile-share`)

Home: `content/incerto-quantile-share.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Check the assumptions behind any super-additivity claim.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Compare aggregation and estimation orders.
- **lean-verifiable:** A specified tail-share functional permits exact distribution calculations.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pareto-moments](#c-pareto-moments).

Technical source mappings: [SCoFT v4 ch. 16](inventory.md#scft-v4-ch16), [`paper-quantile`](inventory.md#paper-quantile).

Chapter chunks: `scft-v4-ch16`.

<a id="c-shadow-mean"></a>

## Bounded-tail transformations and shadow moments (`c-shadow-mean`)

Home: `content/incerto-shadow-mean.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Approved first scope: bounded invertible transform, physical upper bound and assumptions; show sensitivity to endpoint, threshold and fitted parameters. Historical conflict estimates belong to the separate chapter 18 study.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Vary endpoint, threshold, and fitted tail parameters.
- **lean-verifiable:** A declared invertible transformation and support bound permit exact integrals.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-gpd](#c-gpd), [c-mean-excess](#c-mean-excess).

Technical source mappings: [SCoFT v4 ch. 17](inventory.md#scft-v4-ch17), [SCoFT v4 ch. 19](inventory.md#scft-v4-ch19), [`paper-conflicts`](inventory.md#paper-conflicts), [`paper-diseases`](inventory.md#paper-diseases).

Chapter chunks: `scft-v4-ch17`, `scft-v4-ch18`, `scft-v4-ch19`.

<a id="c-conflict-study"></a>

## Historical conflict severity study (`c-conflict-study`)

Home: `content/incerto-conflict-study.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-xhigh`.

Do not treat uncertain historical counts as iid measurements or equate tail fit with a trend conclusion.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: No exact declaration selected for this numerical or empirical treatment; teaching and Python evidence take priority.

- **empirical:** Reanalysis requires event definitions, reporting ranges, exposure adjustments, and licensed data.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-shadow-mean](#c-shadow-mean), [c-threshold](#c-threshold).

Technical source mappings: [SCoFT v4 ch. 18](inventory.md#scft-v4-ch18), [SCoFT v4 appendix H](inventory.md#scft-v4-apph), [`paper-conflicts`](inventory.md#paper-conflicts).

Chapter chunks: `scft-v4-ch18`.

<a id="c-disease-study"></a>

## Historical epidemic severity study (`c-disease-study`)

Home: `content/incerto-disease-study.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-xhigh`.

Study historical severity distributions; no clinical or public-health policy claim follows from the tail fit alone.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: No exact declaration selected for this numerical or empirical treatment; teaching and Python evidence take priority.

- **empirical:** Compare competing analyses with explicit selection, censoring, and finite-population bounds.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-shadow-mean](#c-shadow-mean), [c-threshold](#c-threshold).

Technical source mappings: [SCoFT v4 ch. 19](inventory.md#scft-v4-ch19), [`paper-diseases`](inventory.md#paper-diseases), [`paper-diseases-comment`](inventory.md#paper-diseases-comment).

Chapter chunks: `scft-v4-ch19`.

<a id="c-random-alpha"></a>

## Random tail exponents (`c-random-alpha`)

Home: `content/incerto-random-alpha.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

The mixing law and its support near zero control the result.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Compare finite-range apparent exponents with asymptotic behavior.
- **lean-verifiable:** A specified mixing law over alpha permits survival and integrability analysis.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-regular-variation](#c-regular-variation), [c-mixture-uncertainty](#c-mixture-uncertainty).

Technical source mappings: [SCoFT v4 ch. 21](inventory.md#scft-v4-ch21), [`paper-alpha`](inventory.md#paper-alpha).

Chapter chunks: `scft-v4-ch21`.

<a id="c-pvalues"></a>

## P-value variability and selection (`c-pvalues`)

Home: `content/incerto-pvalues.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

A p-value is not a posterior probability; distinguish variability from invalid calibration.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Repeat tests and selection under one declared model.
- **lean-verifiable:** Distribution statements need a fully specified null, alternative, and testing rule.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-multiple-testing](#c-multiple-testing).

Technical source mappings: [SCoFT v4 ch. 22](inventory.md#scft-v4-ch22).

Chapter chunks: `scft-v4-ch22`.

<a id="c-maximum-entropy"></a>

## Tail constraints and maximum entropy (`c-maximum-entropy`)

Home: [content/incerto-maximum-entropy.md](../../../content/incerto-maximum-entropy.md). Status: **in-progress**. Milestone: **M1**. Lead: `astra-max`.

Use IG exponential-family definitions; a formal optimum does not validate chosen constraints.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`). Chapter-5 teaching/Python done; Lean skipped for toolchain/network limits.

- **numeric-demo:** Numerical solutions can be checked against constraints.
- **lean-verifiable:** A constrained optimization problem needs feasibility, normalization, and uniqueness checks.

Coverage: Chapter-5 teaching and deterministic worked cases implemented; separate max review complete with fixes; no checked Lean. Later chapter extensions remain. See [chapter-5 evidence](../../records/incerto-scft-v4-ch05.md).

Prerequisites: none within this inventory.

Technical source mappings: [SCoFT v4 ch. 30](inventory.md#scft-v4-ch30), [SCoFT v4 appendix B](inventory.md#scft-v4-appb), [`paper-entropy`](inventory.md#paper-entropy).

Chapter chunks: `scft-v4-ch05`, `scft-v4-ch30`.

<a id="c-point-forecast"></a>

## Point forecasts under heavy-tailed losses (`c-point-forecast`)

Home: `content/incerto-point-forecast.md` (existing). Status: **in-progress**. Milestone: **M1**. Lead: `astra-xhigh`.

Specify median/mean/quantile targets and what happens when expected loss is infinite.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Compare losses on identical simulated draws.
- **lean-verifiable:** The optimal point summary depends on the loss and existence of its expectation.

Coverage: Chapter-11 teaching and deterministic model examples implemented; later scft-v4-ch12 scope and separate max review remain. No checked Lean.

Prerequisites: [c-pareto-moments](#c-pareto-moments), [c-calibration-payoff](#c-calibration-payoff).

Technical source mappings: [SCoFT v4 ch. 11](inventory.md#scft-v4-ch11), [SCoFT v4 ch. 12](inventory.md#scft-v4-ch12), [`paper-point-forecast`](inventory.md#paper-point-forecast).

Chapter chunks: `scft-v4-ch11`, `scft-v4-ch12`.

Chapter-11 scope: teaching and Python **done**; Lean **skipped-for-now**.
Separate max review and later chapter scope remain; see the
[chapter-11 checkpoint](../../records/incerto-scft-v4-ch11.md).

<a id="c-ml-econometrics"></a>

## Tail assumptions in statistical pipelines (`c-ml-econometrics`)

Home: [content/incerto-ml-econometrics.md](../../../content/incerto-ml-econometrics.md). Status: **in-progress**. Milestone: **M1**. Lead: `astra-xhigh`.

No blanket rejection of econometrics, machine learning, or behavioral economics.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: No exact declaration selected for this numerical or empirical treatment; teaching and Python evidence take priority.

- **numeric-demo:** Stress a specified estimator under controlled contamination.
- **empirical:** Evaluate one documented pipeline on data with leakage and dependence checks.

Coverage: Chapter-10 teaching and Python implemented; empirical evaluation awaits an authorized S&P cache. Separate max review remains pending.

[Chapter-10 checkpoint](../../records/incerto-scft-v4-ch10.md). Appendix I remains chapter-22 work.

Prerequisites: [c-moment-estimation](#c-moment-estimation), [c-multiple-testing](#c-multiple-testing).

Technical source mappings: [SCoFT v4 appendix F](inventory.md#scft-v4-appf), [SCoFT v4 appendix G](inventory.md#scft-v4-appg), [SCoFT v4 appendix I](inventory.md#scft-v4-appi).

Chapter chunks: `scft-v4-ch10`, `scft-v4-ch22`.

<a id="c-payoff-algebra"></a>

## Option and forward payoff algebra (`c-payoff-algebra`)

Home: `content/incerto-payoff-algebra.md` (proposed). Status: **todo**. Milestone: **M2**. Lead: `astra-max`.

Start with European terminal payoffs and explicit financing conventions.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Original payoff diagrams illustrate cases and boundaries.
- **lean-verifiable:** Piecewise real functions support exact parity and order identities.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-asymmetric-payoffs](#c-asymmetric-payoffs).

Technical source mappings: [DH ch. 1](inventory.md#dh-ch01), [DH ch. 2](inventory.md#dh-ch02), [DH module F](inventory.md#dh-modf).

Chapter chunks: `dh-ch01`, `dh-ch02`, `dh-ch05`.

<a id="c-arbitrage"></a>

## Finite-state arbitrage and price bounds (`c-arbitrage`)

Home: `content/incerto-arbitrage.md` (proposed). Status: **todo**. Milestone: **M2**. Lead: `astra-max`.

Separate terminal payoff identities from trading admissibility and market completeness.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Compute finite-state payoff bounds and transaction-cost cases.
- **lean-verifiable:** Finite portfolio inequalities and specified transaction costs are checkable.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra).

Technical source mappings: [DH ch. 5](inventory.md#dh-ch05), [DH module F](inventory.md#dh-modf).

Chapter chunks: `dh-ch05`.

<a id="c-market-making"></a>

## Market making and inventory exposure (`c-market-making`)

Home: `content/incerto-market-making.md` (proposed). Status: **todo**. Milestone: **M2**. Lead: `astra-xhigh`.

Account for adverse selection and fill assumptions.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: No exact declaration selected for this numerical or empirical treatment; teaching and Python evidence take priority.

- **numeric-demo:** An explicit quote/inventory model illustrates risk and execution.
- **empirical:** Market claims require timestamped, licensed quote and trade data.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra).

Technical source mappings: [DH ch. 3](inventory.md#dh-ch03), [DH ch. 13](inventory.md#dh-ch13).

Chapter chunks: `dh-ch03`, `dh-ch13`.

<a id="c-liquidity"></a>

## Liquidity gaps and hedge execution (`c-liquidity`)

Home: `content/incerto-liquidity.md` (proposed). Status: **todo**. Milestone: **M2**. Lead: `astra-xhigh`.

A continuous-path replication theorem does not cover discontinuous execution.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: No exact declaration selected for this numerical or empirical treatment; teaching and Python evidence take priority.

- **numeric-demo:** Discrete jumps and transaction costs expose replication error.
- **empirical:** Empirical execution costs depend on venue, size, and timestamp.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-market-making](#c-market-making).

Technical source mappings: [DH ch. 4](inventory.md#dh-ch04), [DH ch. 13](inventory.md#dh-ch13).

Chapter chunks: `dh-ch04`, `dh-ch13`.

<a id="c-volatility-surface"></a>

## Volatility, correlation, and surface conventions (`c-volatility-surface`)

Home: `content/incerto-volatility-surface.md` (proposed). Status: **todo**. Milestone: **M2**. Lead: `astra-xhigh`.

Distinguish realized, implied, local, and stochastic volatility.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: No exact declaration selected for this numerical or empirical treatment; teaching and Python evidence take priority.

- **numeric-demo:** Inspect parameter and quotation conventions on synthetic surfaces.
- **empirical:** Market surfaces require licensed observations and cleaning.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra).

Technical source mappings: [DH ch. 6](inventory.md#dh-ch06), [DH ch. 9](inventory.md#dh-ch09).

Chapter chunks: `dh-ch06`, `dh-ch09`.

<a id="c-greeks"></a>

## Delta, gamma, vega, theta, and mixed sensitivities (`c-greeks`)

Home: `content/incerto-greeks.md` (proposed). Status: **todo**. Milestone: **M2**. Lead: `astra-max`.

Keep Greek notation local and distinguish derivative exposure from realized hedge P&L.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Compare derivatives with finite differences and finite shocks.
- **lean-verifiable:** Derivatives of a specified price function are exact local statements.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra), [c-jensen](#c-jensen).

Technical source mappings: [DH ch. 7](inventory.md#dh-ch07), [DH ch. 8](inventory.md#dh-ch08), [DH ch. 9](inventory.md#dh-ch09), [DH ch. 10](inventory.md#dh-ch10), [DH ch. 11](inventory.md#dh-ch11).

Chapter chunks: `dh-ch07`, `dh-ch08`, `dh-ch09`, `dh-ch10`, `dh-ch11`.

<a id="c-hedging-error"></a>

## Discrete hedging and joint Greek exposure (`c-hedging-error`)

Home: `content/incerto-hedging-error.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Specify self-financing, funding, rebalancing, and transaction conventions.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

Lean `skipped-for-now` for continuous-time replication and convergence claims: Stochastic-calculus and measure-theoretic library support has not been established in a pinned Mathlib revision; finite-state candidates are separate declarations.

- **numeric-demo:** Measure discretization, jump, cost, and model errors separately.
- **lean-verifiable:** Finite rebalancing cash-flow identities can be formalized before continuous limits.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-greeks](#c-greeks), [c-liquidity](#c-liquidity).

Technical source mappings: [SCoFT v4 ch. 26](inventory.md#scft-v4-ch26), [DH ch. 11](inventory.md#dh-ch11), [DH ch. 16](inventory.md#dh-ch16), [DH ch. 20](inventory.md#dh-ch20).

Chapter chunks: `scft-v4-ch26`, `dh-ch11`, `dh-ch16`, `dh-ch20`.

<a id="c-basis-buckets"></a>

## Basis, fungibility, and risk buckets (`c-basis-buckets`)

Home: `content/incerto-basis-buckets.md` (proposed). Status: **todo**. Milestone: **M2**. Lead: `astra-max`.

Netting exposures across mismatched maturities or instruments leaves basis risk.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Compare bucketed approximations with full repricing.
- **lean-verifiable:** Finite aggregation and cancellation identities have explicit matching conditions.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-greeks](#c-greeks).

Technical source mappings: [DH ch. 12](inventory.md#dh-ch12), [DH ch. 14](inventory.md#dh-ch14).

Chapter chunks: `dh-ch12`, `dh-ch14`.

<a id="c-model-risk"></a>

## Pricing-model and distribution risk (`c-model-risk`)

Home: `content/incerto-model-risk.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-xhigh`.

Agreement on several prices need not determine the full terminal distribution. Specify the compared model families locally; no interpretive model-uncertainty note is required.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: No exact declaration selected for this numerical or empirical treatment; teaching and Python evidence take priority.

- **numeric-demo:** Hold payoff fixed while changing calibrated model families.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-volatility-surface](#c-volatility-surface).

Technical source mappings: [SCoFT v4 ch. 24](inventory.md#scft-v4-ch24), [SCoFT v4 ch. 26](inventory.md#scft-v4-ch26), [DH ch. 15](inventory.md#dh-ch15), [DH ch. 16](inventory.md#dh-ch16), [DH preface and introductory material](inventory.md#dh-opening).

Chapter chunks: `scft-v4-ch24`, `scft-v4-ch26`, `dh-ch01`, `dh-ch15`, `dh-ch16`.

<a id="c-digitals"></a>

## European and American digital options (`c-digitals`)

Home: `content/incerto-digitals.md` (proposed). Status: **todo**. Milestone: **M2**. Lead: `astra-max`.

Separate terminal indicators from first-passage events.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

Lean `skipped-for-now` for continuous-time first-passage claims: Stochastic-calculus and measure-theoretic library support has not been established in a pinned Mathlib revision; finite-state candidates are separate declarations.

- **numeric-demo:** Resolution and path monitoring materially affect estimates.
- **lean-verifiable:** Terminal digital payoff limits and bounds are tractable; hitting-time results are separate.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra).

Technical source mappings: [DH ch. 17](inventory.md#dh-ch17), [DH ch. 18](inventory.md#dh-ch18).

Chapter chunks: `dh-ch17`, `dh-ch18`.

<a id="c-barriers"></a>

## Barrier contracts and monitoring (`c-barriers`)

Home: `content/incerto-barriers.md` (proposed). Status: **todo**. Milestone: **M2**. Lead: `astra-max`.

Specify inclusive boundaries, rebate timing, and continuous versus discrete monitoring.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

Lean `skipped-for-now` for continuous monitoring and stopping-time pricing claims: Stochastic-calculus and measure-theoretic library support has not been established in a pinned Mathlib revision; finite-state candidates are separate declarations.

- **numeric-demo:** Discrete monitoring and bridge corrections expose numerical assumptions.
- **lean-verifiable:** Pathwise payoff decompositions can be proved with compatible conventions.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-digitals](#c-digitals), [c-hedging-error](#c-hedging-error).

Technical source mappings: [DH ch. 19](inventory.md#dh-ch19), [DH ch. 20](inventory.md#dh-ch20), [DH module G](inventory.md#dh-modg).

Chapter chunks: `dh-ch16`, `dh-ch19`, `dh-ch20`.

<a id="c-compound-options"></a>

## Compound and chooser options (`c-compound-options`)

Home: `content/incerto-compound-options.md` (proposed). Status: **todo**. Milestone: **M2**. Lead: `astra-max`.

Exercise timing and information sets determine the payoff.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Use small trees with explicit exercise conventions.
- **lean-verifiable:** Nested payoff identities admit exact finite-state statements.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra).

Technical source mappings: [DH ch. 21](inventory.md#dh-ch21).

Chapter chunks: `dh-ch21`.

<a id="c-multiasset-options"></a>

## Multi-asset payoff dependence (`c-multiasset-options`)

Home: `content/incerto-multiasset-options.md` (proposed). Status: **todo**. Milestone: **M2**. Lead: `astra-max`.

A scalar correlation does not determine all nonlinear joint payoffs.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Change dependence while preserving marginal distributions.
- **lean-verifiable:** Pathwise bounds and finite-state prices can be formalized.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra), [c-multivariate-tails](#c-multivariate-tails).

Technical source mappings: [DH ch. 22](inventory.md#dh-ch22).

Chapter chunks: `dh-ch22`.

<a id="c-path-options"></a>

## Asian and lookback path functionals (`c-path-options`)

Home: `content/incerto-path-options.md` (proposed). Status: **todo**. Milestone: **M2**. Lead: `astra-max`.

Separate a finite average or maximum from a continuous-time functional.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

Lean `skipped-for-now` for continuous-time path-functional pricing claims: Stochastic-calculus and measure-theoretic library support has not been established in a pinned Mathlib revision; finite-state candidates are separate declarations.

- **numeric-demo:** Compare sampling grids under the same stochastic model.
- **lean-verifiable:** Finite monitored-path bounds and identities have a manageable scope.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra).

Technical source mappings: [DH ch. 23](inventory.md#dh-ch23).

Chapter chunks: `dh-ch23`.

<a id="c-brownian"></a>

## Brownian simulation and discretization (`c-brownian`)

Home: `content/incerto-brownian.md` (proposed). Status: **todo**. Milestone: **M2**. Lead: `astra-max`.

Brownian definitions and increment properties only as needed to explain Dynamic Hedging; bounded simulations and grid checks. A finite random walk does not prove a Brownian theorem.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: Required continuous-time probability or stochastic-calculus support has not been established in a pinned Mathlib revision; no Lean development is promised. Teaching and numerics remain required.

- **numeric-demo:** Check sample increment moments and grid-refinement behavior for a declared scheme.
- **lean-verifiable:** Distributional properties need a later probability-library audit.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

Technical source mappings: [DH module A](inventory.md#dh-moda).

Chapter chunks: `dh-ch07`.

<a id="c-pricing-measures"></a>

## Pricing measures and incomplete markets (`c-pricing-measures`)

Home: `content/incerto-pricing-measures.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

A forward-mean constraint alone does not identify a unique risk-neutral distribution.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

Lean `skipped-for-now` for continuous-time pricing-measure construction: Stochastic-calculus and measure-theoretic library support has not been established in a pinned Mathlib revision; finite-state candidates are separate declarations.

- **numeric-demo:** Compute price intervals under explicit constraints.
- **lean-verifiable:** Finite-state examples show when moment constraints leave multiple pricing measures.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-arbitrage](#c-arbitrage).

Technical source mappings: [SCoFT v4 ch. 25](inventory.md#scft-v4-ch25), [DH module B](inventory.md#dh-modb), [`paper-pricing`](inventory.md#paper-pricing).

Chapter chunks: `scft-v4-ch25`, `dh-ch05`.

<a id="c-numeraire"></a>

## Numeraire changes and relative prices (`c-numeraire`)

Home: `content/incerto-numeraire.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Positive numeraires, normalization and finite-state measure-change identities, plus only the continuous-time basics needed for Dynamic Hedging examples. Numerical worked cases remain required; Lean candidates are exact finite-state identities only.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

Lean `skipped-for-now` for continuous-time measure-change identities: Stochastic-calculus and measure-theoretic library support has not been established in a pinned Mathlib revision; finite-state candidates are separate declarations.

- **numeric-demo:** Compute normalized finite-state measure changes before continuous-time numerical cases.
- **lean-verifiable:** Finite-state change-of-measure identities require a positive numeraire and normalization.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pricing-measures](#c-pricing-measures).

Technical source mappings: [SCoFT v4 ch. 28](inventory.md#scft-v4-ch28), [DH module C](inventory.md#dh-modc).

Chapter chunks: `scft-v4-ch28`, `dh-ch16`.

<a id="c-correlation-constraints"></a>

## Feasible correlation matrices (`c-correlation-constraints`)

Home: `content/incerto-correlation-constraints.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Finite second moments and consistent normalization are required.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Show incompatible pairwise inputs and their pricing consequences.
- **lean-verifiable:** Positive semidefiniteness gives exact three-variable feasibility bounds.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

Technical source mappings: [SCoFT v4 ch. 29](inventory.md#scft-v4-ch29), [DH ch. 6](inventory.md#dh-ch06), [DH module D](inventory.md#dh-modd).

Chapter chunks: `scft-v4-ch29`, `dh-ch06`.

<a id="c-risk-measures"></a>

## VaR, expected shortfall, and model limits (`c-risk-measures`)

Home: `content/incerto-risk-measures.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Expected shortfall may be infinite; VaR subadditivity needs conditions.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Show tail sensitivity and estimation uncertainty.
- **lean-verifiable:** Finite-distribution counterexamples and scoped coherence statements are checkable.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pareto-moments](#c-pareto-moments).

Technical source mappings: [SCoFT v4 ch. 13](inventory.md#scft-v4-ch13), [SCoFT v4 ch. 28](inventory.md#scft-v4-ch28), [SCoFT v4 ch. 29](inventory.md#scft-v4-ch29), [DH module E](inventory.md#dh-mode).

Chapter chunks: `scft-v4-ch13`, `scft-v4-ch28`, `scft-v4-ch29`, `dh-ch15`.

<a id="c-stochastic-pricing"></a>

## Ito calculus and continuous-time pricing (`c-stochastic-pricing`)

Home: `content/incerto-stochastic-pricing.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Ito formula, diffusion pricing and hedge-error basics only as needed to explain Dynamic Hedging concepts, with stated assumptions and bounded numerical cases. No standalone advanced stochastic-calculus development; Lean remains optional and skipped pending support.

Deliverables: website math (required) → Python (required) → Lean (optional; `skipped-for-now`).

Lean limit: Required continuous-time probability or stochastic-calculus support has not been established in a pinned Mathlib revision; no Lean development is promised. Teaching and numerics remain required.

- **numeric-demo:** Compare discretizations only after a model and convergence target are fixed.
- **lean-verifiable:** A full development needs stochastic integrals, admissibility, and analytic hypotheses.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-brownian](#c-brownian), [c-pricing-measures](#c-pricing-measures), [c-hedging-error](#c-hedging-error).

Technical source mappings: [SCoFT v4 ch. 24](inventory.md#scft-v4-ch24), [DH module G](inventory.md#dh-modg).

Chapter chunks: `scft-v4-ch24`, `dh-ch16`.

<a id="c-power-option"></a>

## Option tails under power laws (`c-power-option`)

Home: `content/incerto-power-option.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Specify pricing measure, tail regime, and finite call-price condition.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Compare exact power laws with finite-strike approximations.
- **lean-verifiable:** Integrating a stated survival tail gives scoped price relations and moment gates.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pareto-moments](#c-pareto-moments), [c-pricing-measures](#c-pricing-measures).

Technical source mappings: [SCoFT v4 ch. 27](inventory.md#scft-v4-ch27), [`paper-option-tail`](inventory.md#paper-option-tail).

Chapter chunks: `scft-v4-ch27`.

<a id="c-probability-conflation"></a>

## Tail probabilities, expectations and parameter uncertainty (`c-probability-conflation`)

Home: `content/incerto-probability-conflation.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Scope the chapter 13 probability-versus-expectation and error-propagation claims with explicit distributions and integrability. Chapter 11 owns the basic calibration distinction; no assertion about individual forecasters follows from a model example.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Compare probability and tail-expectation sensitivity on identical parameter grids; report moment boundaries.
- **lean-verifiable:** Specified probability and tail-expectation comparisons admit exact declarations after the source hypotheses are checked.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-calibration-payoff](#c-calibration-payoff), [c-point-forecast](#c-point-forecast).

Technical source mappings: [SCoFT v4 ch. 13](inventory.md#scft-v4-ch13), [`paper-probability-conflation`](inventory.md#paper-probability-conflation).

Chapter chunks: `scft-v4-ch13`.

<a id="c-portfolio-tail-dependence"></a>

## Portfolio losses beyond correlation (`c-portfolio-tail-dependence`)

Home: `content/incerto-portfolio-tail-dependence.md` (proposed). Status: **todo**. Milestone: **M1**. Lead: `astra-max`.

Compare specified portfolio loss laws with similar correlation summaries but different joint-tail exposure. Separate finite-moment assumptions, simulation evidence and historical allocation claims; no investment prescription.

Deliverables: website math (required) → Python (required) → Lean (optional; `optional`).

- **numeric-demo:** Stress fixed allocations under declared marginals and dependence models; retain reproducible seeds and uncertainty summaries.
- **lean-verifiable:** Finite joint-distribution examples can separate correlation constraints from nonlinear loss and tail-event probabilities.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-multivariate-tails](#c-multivariate-tails), [c-correlation-constraints](#c-correlation-constraints), [c-risk-measures](#c-risk-measures).

Technical source mappings: [SCoFT v4 ch. 29](inventory.md#scft-v4-ch29), [`paper-portfolio-correlation`](inventory.md#paper-portfolio-correlation).

Chapter chunks: `scft-v4-ch29`.
