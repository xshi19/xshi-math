> Historical record from `incerto-wiki` at `9717c9cf83aee18b47f423a14bce2f0d14bb8bcb`.
> Source: `docs/plan/proof-support-and-formalization-notes.md`. Statements and commands below describe that repository
> at the recorded date, not current xshi-math verification. MIT; copyright (c) 2023 xshi19.

# Proof Support and Formalization Notes

Maintainer: Xiang Shi
Last updated: 2026-09-12

This internal note preserves proof-support and Lean-formalization bookkeeping
that should not appear as project-status prose on ordinary public concept
pages.  Public pages should orient readers in natural prose: what is proved,
what is sketched, and what is cited.  This file can carry the project-management
view.

Current formalization state: `formalization/lean/` contains a Lake/Mathlib
project pinned to Lean/Mathlib `v4.19.0`. On 2026-09-05,
`cd formalization/lean && lake build` checked two declarations in
`Incerto/Pareto.lean`:

- `Incerto.moment_exponent_threshold`: the real inequality equivalence
  `p - alpha - 1 < -1` iff `p < alpha`, without an integrability claim.
- `Incerto.pareto_survival_scale`: the piecewise survival expression has
  ratio `t ^ (-alpha)` for positive cutoff, shape, and multiplier when
  both thresholds are at or above the cutoff. No probability measure is
  constructed.

Do not describe any other statement as formalized until `lake build`
checks its corresponding declaration.

## Editorial Decision

- `content/` concept pages should read like mathematical notes or a textbook.
- Use prose such as "We prove..." or "The calculation below shows..." before a
  proof or derivation.
- Keep pending Lean work, implementation plans, and editorial TODOs in `docs/`
  or short Markdown comments.
- The public Lean blueprint page may still discuss formalization status because
  that page is explicitly about the formalization track.

## Moved Concept-Page Notes

| Page | Reader-facing support | Internal formalization note |
| --- | --- | --- |
| `content/concepts/distributions/pareto.md` | The piecewise survival expression and tail scaling are stated and illustrated. | Checked: `Incerto.pareto_survival_scale`, with both thresholds at or above the cutoff. Probability-measure construction remains deferred. |
| `content/concepts/theorems/regular-variation.md` | Algebraic characterization of regular variation is proved; deeper representation theorems are cited through Karamata. | Candidate Lean item: `f in RV_rho` iff `f(x)=x^rho L(x)` with slowly varying `L`, starting with power-survival special cases. |
| `content/concepts/theorems/karamata.md` | Karamata integral asymptotics are cited; moment consequences are derived by integration by parts. | Candidate Lean items: upper-tail moment consequence for `0<p<alpha`; lower-truncated moment consequence for `p>alpha`. |
| `content/concepts/theorems/pareto-moment-existence.md` | Pareto moment criterion, moment formula, and truncated regimes are proved by direct integration. | Checked: `Incerto.moment_exponent_threshold` (algebra only). Blueprint-only: convergent moment formula, logarithmic boundary, divergent cutoff regimes. |
| `content/concepts/theorems/lln-failure.md` | Infinite-mean LLN failure is sketched by truncation and the strong law; Pareto threshold is cited from Pareto moments. | No immediate Lean obligation until the probability framework is chosen. |
| `content/concepts/theorems/generalized-central-limit-theorem.md` | Stable-limit theorem is cited; exact Pareto maximum scaling is proved as the local calculation. | Candidate Lean item: exact Pareto maximum scale or algebraic survival scaling, not stable convergence. |
| `content/concepts/theorems/cramer-condition.md` | Chernoff bound is proved from Markov's inequality; examples are direct checks. | Candidate Lean items: Chernoff upper-tail bound, exact normal/exponential/Pareto mgf comparisons after probability infrastructure exists. |
| `content/concepts/theorems/subexponentiality.md` | Maximum-tail asymptotic is proved; exact Pareto two-summand residual bound is a partial proof; full subexponential theory is cited. | Candidate Lean items: iid maximum-tail asymptotic for fixed `n`; exact Pareto `n=2` residual estimate. |
| `content/concepts/theorems/pickands-balkema-de-haan.md` | Full theorem is cited; exact Pareto excess distribution is derived. | Candidate Lean item: Pareto excess survival is generalized Pareto for thresholds `u>=x_m`. |
| `content/concepts/theorems/mean-excess-function.md` | Pareto mean-excess formula is derived; GPD formula is sketched from threshold stability and the GPD mean. | Candidate Lean item: exact Pareto mean excess for `alpha>1`. |
| `content/concepts/methods/max-to-sum-ratio.md` | Finite-mean vanishing max-to-sum theorem is proved; infinite-mean Pareto regimes are cited or heuristic. | Candidate Lean item: finite-mean max-to-sum ratio using strong law and Borel-Cantelli, after probability support exists. |
| `content/concepts/methods/plug-in-tail-estimation.md` | Known-cutoff Pareto MLE is derived; its mean's normal limit uses cited CLT/delta-method results. The sample-mean stable limit is cited. Body/tail decomposition and the finite-fit moment singularity are derived. Simulations compare error quantiles and probabilities, not MSE. | Candidate Lean items: log-excess exponential law, plug-in derivative and variance algebra, body/tail expectation split, and gamma-density boundary divergence. Probability limits remain cited; no new checked declarations. |
| `content/concepts/methods/body-shoulder-tail.md` | Normal variance-curvature derivatives and sign-change boundaries are derived; Taylor mixture interpretation is sketched. | Candidate Lean items: variance derivative formulas and roots `3 +/- sqrt(6)` for the standard normal density curvature polynomial. |
| `content/concepts/distributions/double-pareto.md` | Tail, density, CDF, and moment-threshold facts are derived from a signed Pareto magnitude. | Candidate Lean items: one-sided/two-sided tail formulas and variance formula where moments exist. |
| `content/concepts/distributions/normal-mixture.md` | Two-component mixture formulas are derived; general mixture identities are sketched by conditioning. | Candidate Lean items: two-component density, mean, variance, fourth moment, and finite-support largest-variance tail control. |
| `content/concepts/distributions/tail-class-catalog.md` | Two-summand convolution formula and iid lower-bounded split are derived in the appendix. | Candidate Lean items: continuous convolution identity and iid split, once measure/integration setup is available. |
| `content/concepts/distributions/variance-gamma.md` | MGF, finiteness interval, moments, and tail rates are derived or sketched from the gamma-normal mixture. | Candidate Lean items: MGF interval and mean/variance formulas; Bessel-density and asymptotic facts should remain cited until special-function support is clear. |

## Follow-Up

- Update this note when a new declaration passes the Lean build.
- Move only checked Lean declarations back into public concept pages.
- Keep public proof introductions human and local even when this internal table
  grows.
