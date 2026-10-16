# Concept register

Classification describes the proposed evidence, not evidence already obtained. `lean-verifiable` means a precisely scoped formalization candidate; library support and effort are unverified. `numeric-demo` uses synthetic or fixed inputs. `empirical` requires observed data. `prose-only` identifies an interpretive component; it may coexist with a separately scoped mathematical model. All program concepts start `todo`.

Existing notes are linked below. Proposed paths are code text, not links to nonexistent pages. Each proposed public path follows `/math/incerto/<filename-stem>/`; no new route exists yet. Dependencies are mathematical reading prerequisites. Milestones give the first planned treatment, not a deadline to formalize an entire subject.

<a id="c-exceedances"></a>
## Finite-sample exceedance counts (`c-exceedances`)

Home: [content/incerto-counting-exceedances.md](../../../content/incerto-counting-exceedances.md). Milestone: **M1**. Lead: `astra-max`.

For n >= 1 and real observations, prove fraction bounds and antitonicity in u; no population inference.

- **lean-verifiable:** Finite-set counting gives exact bounds and threshold monotonicity.
- **numeric-demo:** The existing fixed sample checks the strict threshold convention.

Coverage: Original page and xmath.exceedance_fraction; fixed synthetic demo exists. Neither implementation nor population inference is formally verified.

Prerequisites: none within this inventory.

<a id="c-pareto"></a>
## Pareto distribution (`c-pareto`)

Home: [content/incerto-pareto.md](../../../content/incerto-pareto.md). Milestone: **M6**. Lead: `astra-max`.

Positive scale x_m and alpha; distinguish normalized distribution from a tail approximation.

- **lean-verifiable:** Density, survival, and support identities admit exact analysis.
- **numeric-demo:** Compare simulated exceedances with the stated survival law.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: none within this inventory.

<a id="c-regular-variation"></a>
## Regular variation (`c-regular-variation`)

Home: [content/incerto-regular-variation.md](../../../content/incerto-regular-variation.md). Milestone: **M6**. Lead: `astra-max`.

Pointwise ratio limits at positive dilation; do not infer regular variation from a finite plot.

- **lean-verifiable:** Definitions and individual limit statements can be formalized.
- **numeric-demo:** Ratios illustrate convergence and slowly varying corrections.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-pareto](#c-pareto).

<a id="c-karamata"></a>
## Karamata tail integrals (`c-karamata`)

Home: [content/incerto-karamata.md](../../../content/incerto-karamata.md). Milestone: **M6**. Lead: `astra-max`.

General theorem requires a library feasibility audit; p = alpha depends on the slowly varying factor.

- **lean-verifiable:** The integral theorem needs explicit measurable and asymptotic hypotheses.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-regular-variation](#c-regular-variation).

<a id="c-pareto-moments"></a>
## Pareto moment boundary (`c-pareto-moments`)

Home: [content/incerto-pareto-moment-existence.md](../../../content/incerto-pareto-moment-existence.md). Milestone: **M2**. Lead: `astra-max`.

For p > 0, the pth Pareto moment is finite exactly when p < alpha; handle equality separately.

- **lean-verifiable:** Integrability and the exact positive-power integral have a small analytic scope.
- **numeric-demo:** Truncation plots distinguish finite estimates from finite population moments.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-pareto](#c-pareto).

<a id="c-mean-excess"></a>
## Mean excess (`c-mean-excess`)

Home: [content/incerto-mean-excess-function.md](../../../content/incerto-mean-excess-function.md). Milestone: **M6**. Lead: `astra-max`.

Separate a population conditional mean from its sample diagnostic.

- **lean-verifiable:** Conditional expectation formulas require positive exceedance probability and integrability.
- **numeric-demo:** Threshold curves compare exact models with finite samples.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-pareto-moments](#c-pareto-moments).

<a id="c-hill"></a>
## Hill tail-index estimation (`c-hill`)

Home: [content/incerto-hill-estimator.md](../../../content/incerto-hill-estimator.md). Milestone: **M6**. Lead: `astra-max`.

Do not claim general consistency without intermediate-sequence and tail conditions.

- **lean-verifiable:** Exact Pareto log-transform identities can precede asymptotic theory.
- **numeric-demo:** Vary the number of upper order statistics to expose bias and noise.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-regular-variation](#c-regular-variation).

<a id="c-evi"></a>
## Extreme-value index (`c-evi`)

Home: [content/incerto-extreme-value-index.md](../../../content/incerto-extreme-value-index.md). Milestone: **M6**. Lead: `astra-max`.

xi = 1/alpha only in the positive regularly varying regime; other signs need separate domains.

- **lean-verifiable:** Domain-specific parameter relations are precise statements.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: none within this inventory.

<a id="c-gpd"></a>
## Generalized Pareto excess models (`c-gpd`)

Home: [content/incerto-generalized-pareto.md](../../../content/incerto-generalized-pareto.md). Milestone: **M6**. Lead: `astra-max`.

Distinguish xi = 0, xi > 0, and finite-endpoint xi < 0.

- **lean-verifiable:** Support, survival, and exact threshold stability have explicit parameter cases.
- **numeric-demo:** Check support and exponential limit numerically.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-evi](#c-evi).

<a id="c-plugin"></a>
## Plug-in tail estimation (`c-plugin`)

Home: [content/incerto-plug-in-tail-estimation.md](../../../content/incerto-plug-in-tail-estimation.md). Milestone: **M2**. Lead: `astra-max`.

The unregularized mean estimator has a pole at estimated xi = 1; no uniform MSE superiority.

- **lean-verifiable:** A specified Pareto estimator permits exact transforms and singularity analysis.
- **numeric-demo:** Compare sample and plug-in estimators on identical simulated samples.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-pareto-moments](#c-pareto-moments), [c-hill](#c-hill).

<a id="c-pbdh"></a>
## Threshold-limit theorem (`c-pbdh`)

Home: [content/incerto-pickands-balkema-de-haan.md](../../../content/incerto-pickands-balkema-de-haan.md). Milestone: **M6**. Lead: `astra-max`.

Record the existing general result as cited; formalizing one excess identity does not certify the theorem.

- **lean-verifiable:** The general theorem is a substantial probability formalization; the exact Pareto case is smaller.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-gpd](#c-gpd), [c-regular-variation](#c-regular-variation).

<a id="c-gev"></a>
## Generalized extreme-value laws (`c-gev`)

Home: [content/incerto-generalized-extreme-value.md](../../../content/incerto-generalized-extreme-value.md). Milestone: **M6**. Lead: `astra-max`.

Specify the domain of attraction, centering, scaling, and convergence mode.

- **lean-verifiable:** Distribution formulas and maxima limits have separate proof obligations.
- **numeric-demo:** Block-maxima experiments illustrate normalization sensitivity.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-evi](#c-evi).

<a id="c-frechet"></a>
## Frechet maxima (`c-frechet`)

Home: [content/incerto-frechet.md](../../../content/incerto-frechet.md). Milestone: **M6**. Lead: `astra-max`.

Positive tail exponent and explicit normalization; finite-n errors remain numerical.

- **lean-verifiable:** The Pareto maximum limit provides a bounded first EVT target.
- **numeric-demo:** Compare normalized maxima with the limiting distribution.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-pareto](#c-pareto), [c-gev](#c-gev).

<a id="c-subexponential"></a>
## Subexponential sums (`c-subexponential`)

Home: [content/incerto-subexponentiality.md](../../../content/incerto-subexponentiality.md). Milestone: **M6**. Lead: `astra-max`.

Fixed n iid nonnegative variables; no automatic extension to growing n.

- **lean-verifiable:** Convolution-tail statements need nonnegative support and fixed-sum hypotheses.
- **numeric-demo:** Compare the sum tail with a single-large-observation approximation.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-regular-variation](#c-regular-variation).

<a id="c-tail-ratio"></a>
## Survival-tail ratio diagnostic (`c-tail-ratio`)

Home: [content/incerto-survival-tail-ratio.md](../../../content/incerto-survival-tail-ratio.md). Milestone: **M6**. Lead: `astra-max`.

Independence is required for a joint-exceedance interpretation.

- **lean-verifiable:** Specified survival-function ratios allow exact limit calculations.
- **numeric-demo:** Plot the diagnostic across models without treating it as a convolution proof.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-pareto](#c-pareto).

<a id="c-max-sum"></a>
## Maximum-to-sum ratio (`c-max-sum`)

Home: [content/incerto-max-to-sum-ratio.md](../../../content/incerto-max-to-sum-ratio.md). Milestone: **M6**. Lead: `astra-max`.

A nondegenerate heavy-tail limit need not equal one; define zero-sum behavior.

- **lean-verifiable:** Finite positive-sum bounds are elementary; limit regimes need probability theory.
- **numeric-demo:** Compare finite-mean, alpha = 1, and alpha < 1 regimes.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-pareto-moments](#c-pareto-moments).

<a id="c-double-pareto"></a>
## Symmetric shifted Pareto construction (`c-double-pareto`)

Home: [content/incerto-double-pareto.md](../../../content/incerto-double-pareto.md). Milestone: **M6**. Lead: `astra-max`.

Preserve the existing shifted construction; symmetry alone does not imply an existing mean.

- **lean-verifiable:** The stated sign-mixture construction has exact distribution and moment properties.
- **numeric-demo:** Symmetry and unstable averages can be illustrated independently.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-pareto-moments](#c-pareto-moments).

<a id="c-threshold"></a>
## Tail-threshold selection (`c-threshold`)

Home: [content/incerto-tail-threshold-selection.md](../../../content/incerto-tail-threshold-selection.md). Milestone: **M2**. Lead: `astra-max`.

No universal optimal threshold from a visually straight tail plot.

- **lean-verifiable:** The stated body-plus-tail example and threshold-stability identities have exact model-specific claims.
- **numeric-demo:** Sensitivity curves show the bias and variance tradeoff.
- **empirical:** Real-data threshold choice requires dependence and model-fit diagnostics.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-hill](#c-hill), [c-mean-excess](#c-mean-excess).

<a id="c-body-shoulder"></a>
## Body, shoulder, and tail under perturbation (`c-body-shoulder`)

Home: [content/incerto-body-shoulder-tail.md](../../../content/incerto-body-shoulder-tail.md). Milestone: **M6**. Lead: `astra-max`.

The existing normal variance perturbation is not a universal tail-threshold rule.

- **lean-verifiable:** Density derivatives locate sign changes for a specified perturbation.
- **numeric-demo:** Original curves can display the signed effects.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: none within this inventory.

<a id="c-tail-geometry"></a>
## Multivariate tail geometry (`c-tail-geometry`)

Home: [content/incerto-iso-density-tail-geometry.md](../../../content/incerto-iso-density-tail-geometry.md). Milestone: **M6**. Lead: `astra-max`.

Point density and probability mass must remain distinct.

- **lean-verifiable:** Product-density comparisons are exact under their independence assumptions.
- **numeric-demo:** Compare contours and integrated regional probabilities.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-pareto](#c-pareto).

<a id="c-cramer"></a>
## Exponential-moment gate (`c-cramer`)

Home: [content/incerto-cramer-condition.md](../../../content/incerto-cramer-condition.md). Milestone: **M6**. Lead: `astra-max`.

An exponential-moment condition and a Chernoff bound do not prove a full large-deviation principle.

- **lean-verifiable:** Markov/Chernoff bounds are formalizable with finite exponential moments.
- **numeric-demo:** Compare exponential and power-law tail bounds.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: none within this inventory.

<a id="c-stable-clt"></a>
## Stable limits for sums (`c-stable-clt`)

Home: [content/incerto-generalized-central-limit-theorem.md](../../../content/incerto-generalized-central-limit-theorem.md). Milestone: **M6**. Lead: `astra-max`.

Handle alpha = 1 centering and slowly varying factors explicitly.

- **lean-verifiable:** Stable attraction is an advanced formalization with explicit centering and scaling.
- **numeric-demo:** Simulations compare Gaussian and stable scaling.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-regular-variation](#c-regular-variation).

<a id="c-lln-failure"></a>
## Failure of finite-mean averaging assumptions (`c-lln-failure`)

Home: [content/incerto-lln-failure.md](../../../content/incerto-lln-failure.md). Milestone: **M6**. Lead: `astra-max`.

The existing nonnegative divergence result does not apply to symmetric Cauchy sums.

- **lean-verifiable:** Nonnegative iid infinite-mean divergence has a precise theorem statement.
- **numeric-demo:** Compare with a two-sided Cauchy example without conflating the arguments.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: none within this inventory.

<a id="c-tail-catalog"></a>
## Tail classes and implication boundaries (`c-tail-catalog`)

Home: [content/incerto-tail-class-catalog.md](../../../content/incerto-tail-class-catalog.md). Milestone: **M2**. Lead: `astra-max`.

Keep cited class memberships separate from the elementary convolution derivation and exact ratio checks.

- **lean-verifiable:** The convolution decomposition and exact light-tail ratios are precise proof targets.
- **numeric-demo:** Population tail-ratio curves illustrate distinct asymptotic classes.

Coverage: Existing prose needs claim-by-claim review; no checked Lean.

Prerequisites: [c-regular-variation](#c-regular-variation), [c-subexponential](#c-subexponential), [c-cramer](#c-cramer).

<a id="c-luck-skill"></a>
## Luck, skill, and performance selection (`c-luck-skill`)

Home: `content/incerto-luck-skill.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

Separate ex ante ability, realized payoff, and selection on realized payoff.

- **numeric-demo:** A controlled population exposes selection effects.
- **empirical:** Observed performance needs a specified null and selection process.
- **prose-only:** Attributing success involves causal assumptions beyond the simulation.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-counterfactuals"></a>
## Alternative histories and decision quality (`c-counterfactuals`)

Home: `content/incerto-counterfactuals.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

State the generative assumptions and the chosen loss or utility.

- **numeric-demo:** Repeated simulated paths compare decisions under the same model.
- **prose-only:** A single realized history cannot identify every counterfactual.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-noise-monitoring"></a>
## Observation frequency and noise (`c-noise-monitoring`)

Home: `content/incerto-noise-monitoring.md` (proposed). Milestone: **M3**. Lead: `astra-max`.

No universal claim that frequent observation is harmful.

- **lean-verifiable:** Signal/noise scaling can be proved for a specified independent-increment model.
- **numeric-demo:** Change monitoring frequency while holding the path model fixed.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-counterfactuals](#c-counterfactuals).

<a id="c-survivorship"></a>
## Survivorship and silent evidence (`c-survivorship`)

Home: `content/incerto-survivorship.md` (proposed). Milestone: **M3**. Lead: `astra-max`.

Distinguish truncation, censoring, selection, and unobserved failures.

- **lean-verifiable:** Finite conditional-probability examples can establish selection bias.
- **numeric-demo:** Simulate observed survivors and the full cohort.
- **empirical:** Historical missingness requires a documented observation model.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-luck-skill](#c-luck-skill).

<a id="c-asymmetric-payoffs"></a>
## Asymmetric payoffs and exposure (`c-asymmetric-payoffs`)

Home: `content/incerto-asymmetric-payoffs.md` (proposed). Milestone: **M3**. Lead: `astra-max`.

Expected payoff statements require integrability; a high hit rate is insufficient.

- **lean-verifiable:** Finite payoff tables separate win probability from expected payoff.
- **numeric-demo:** Use original examples with visible rare-loss exposure.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-induction"></a>
## Induction and limits of finite evidence (`c-induction`)

Home: `content/incerto-induction.md` (proposed). Milestone: **M2**. Lead: `astra-xhigh`.

Separate logical underdetermination from model-relative confidence statements.

- **prose-only:** The philosophical problem cannot be settled by a finite statistical theorem.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-multiple-testing"></a>
## Search, multiple testing, and regression effects (`c-multiple-testing`)

Home: `content/incerto-multiple-testing.md` (proposed). Milestone: **M3**. Lead: `astra-max`.

Selection must be included when interpreting a reported winner.

- **lean-verifiable:** Finite-family error bounds and a specified regression example are formalizable.
- **numeric-demo:** Repeat the full search procedure under a declared null.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-luck-skill](#c-luck-skill).

<a id="c-path-dependence"></a>
## Reinforcement and path-dependent outcomes (`c-path-dependence`)

Home: `content/incerto-path-dependence.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

A toy process is not a universal explanation of social concentration.

- **numeric-demo:** A specified urn or preferential-attachment process demonstrates one mechanism.
- **empirical:** Claims about actual inequality need data and alternative mechanisms.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-biases"></a>
## Probability judgments and cognitive biases (`c-biases`)

Home: `content/incerto-biases.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

Keep normative probability arithmetic distinct from claims about human behavior.

- **empirical:** Psychological generalizations require primary studies and replication review.
- **prose-only:** Explain the reasoning error without asserting its empirical prevalence.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-causal-narrative"></a>
## Narrative explanations and causal identification (`c-causal-narrative`)

Home: `content/incerto-causal-narrative.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

Do not infer causation from a fitted story or a retrospective sequence.

- **prose-only:** Discuss what observations do and do not distinguish.
- **numeric-demo:** Observationally similar simulated models can have different interventions.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-skepticism"></a>
## Fallibility and practical skepticism (`c-skepticism`)

Home: `content/incerto-skepticism.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

Distinguish uncertainty about a model from uncertainty within it.

- **prose-only:** This is an epistemic stance, not a universal probability theorem.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-stoicism"></a>
## Control, dignity, and responses to chance (`c-stoicism`)

Home: `content/incerto-stoicism.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

Use original commentary and cited chapter locators; no aphorism collection.

- **prose-only:** These are ethical and interpretive arguments.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-scalability"></a>
## Scalable outcomes and concentration (`c-scalability`)

Home: `content/incerto-scalability.md` (proposed). Milestone: **M3**. Lead: `astra-max`.

Do not treat occupational labels as distributional assumptions.

- **lean-verifiable:** Specified finite payoff and aggregation examples can be checked.
- **numeric-demo:** Compare bounded and unbounded-support model families.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-asymmetric-payoffs](#c-asymmetric-payoffs).

<a id="c-black-swan"></a>
## Surprise, impact, and retrospective explanation (`c-black-swan`)

Home: `content/incerto-black-swan.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

A surprising event is not automatically a power-law observation.

- **prose-only:** Define the observer-relative concept and its limits.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-induction](#c-induction), [c-causal-narrative](#c-causal-narrative).

<a id="c-ludic"></a>
## Model boundaries and domain transfer (`c-ludic`)

Home: `content/incerto-ludic.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

Do not use a model-boundary critique as evidence for a particular alternative law.

- **prose-only:** Assess omitted mechanisms and the limits of closed-world games.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-forecasting"></a>
## Prediction limits and forecast evaluation (`c-forecasting`)

Home: `content/incerto-forecasting.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

Score distributions and decisions separately; distinguish impossibility from poor calibration.

- **empirical:** Skill claims need dated forecasts, baselines, and leakage control.
- **numeric-demo:** Simulate horizon and parameter uncertainty.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-epistemic-uncertainty"></a>
## Model uncertainty and unseen mechanisms (`c-epistemic-uncertainty`)

Home: `content/incerto-epistemic-uncertainty.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

Do not assign an unsupported probability to unknown model classes.

- **prose-only:** Classify what the model leaves unspecified.
- **numeric-demo:** Compare predictions across explicitly declared model families.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-skepticism](#c-skepticism).

<a id="c-tacit-knowledge"></a>
## Practice, tacit knowledge, and explicit models (`c-tacit-knowledge`)

Home: `content/incerto-tacit-knowledge.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

Distinguish an account of discovery from a mathematical justification.

- **prose-only:** Historical and philosophical claims need attribution and counterexamples.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-procrustean"></a>
## Category fit and forced measurement (`c-procrustean`)

Home: `content/incerto-procrustean.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

Discuss the aphoristic themes in original prose; no close paraphrase or reconstructed aphorisms.

- **prose-only:** Evaluate the choice of categories and what they erase.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-aesthetics"></a>
## Aesthetic judgment and intellectual style (`c-aesthetics`)

Home: `content/incerto-aesthetics.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

Separate taste, rhetoric, and factual historical assertions.

- **prose-only:** Interpretive commentary has no theorem-like truth condition.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-jensen"></a>
## Convexity and Jensen effects (`c-jensen`)

Home: `content/incerto-jensen.md` (proposed). Milestone: **M3**. Lead: `astra-max`.

Distinguish payoff curvature from a full claim about welfare or survival.

- **lean-verifiable:** Convexity inequalities have exact domain and integrability conditions.
- **numeric-demo:** Mean-preserving perturbations illustrate expectation changes.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-fragility"></a>
## Sensitivity-based fragility (`c-fragility`)

Home: `content/incerto-fragility.md` (proposed). Milestone: **M3**. Lead: `astra-max`.

Specify response, adverse region, dispersion parameter, and derivative existence.

- **lean-verifiable:** A chosen distribution family and response functional give a checkable sensitivity.
- **numeric-demo:** Finite differences reveal dependence on the perturbation family.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-jensen](#c-jensen), [c-asymmetric-payoffs](#c-asymmetric-payoffs).

<a id="c-hormesis"></a>
## Dose response and adaptation (`c-hormesis`)

Home: `content/incerto-hormesis.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

A curve calculation does not establish a clinical or biological benefit.

- **numeric-demo:** A declared response curve separates local convexity from global effects.
- **empirical:** Biological claims need domain-specific evidence and confounding review.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-jensen](#c-jensen).

<a id="c-selection-levels"></a>
## Individual failure and population adaptation (`c-selection-levels`)

Home: `content/incerto-selection-levels.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

Specify whose outcome is improved, at what cost, and on which time scale.

- **numeric-demo:** A branching or replacement toy model separates levels of aggregation.
- **prose-only:** Ethical consequences do not follow from aggregate fitness.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-survivorship](#c-survivorship).

<a id="c-decentralization"></a>
## Redundancy, size, and decentralized exposure (`c-decentralization`)

Home: `content/incerto-decentralization.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

No general theorem that decentralization dominates for every dependency structure.

- **numeric-demo:** Network and concentration models permit controlled stress experiments.
- **empirical:** Institutional claims require comparative evidence.
- **prose-only:** State normative tradeoffs separately.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-iatrogenics"></a>
## Intervention error and subtractive decisions (`c-iatrogenics`)

Home: `content/incerto-iatrogenics.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

Do not convert a medical illustration into treatment advice.

- **numeric-demo:** Compare actions under explicit error costs and uncertain treatment effects.
- **empirical:** Claims of harm require suitable causal evidence.
- **prose-only:** A preference for restraint remains a decision rule with assumptions.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-epistemic-uncertainty](#c-epistemic-uncertainty).

<a id="c-barbell"></a>
## Bounded downside and barbell allocations (`c-barbell`)

Home: `content/incerto-barbell.md` (proposed). Milestone: **M3**. Lead: `astra-max`.

Specify default, leverage, funding, and admissible losses; no investment prescription.

- **lean-verifiable:** A specified finite allocation gives exact payoff bounds.
- **numeric-demo:** Compare payoff distributions with the same budget constraints.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-asymmetric-payoffs](#c-asymmetric-payoffs), [c-ruin](#c-ruin).

<a id="c-optionality"></a>
## Optionality and asymmetric experimentation (`c-optionality`)

Home: `content/incerto-optionality.md` (proposed). Milestone: **M3**. Lead: `astra-max`.

An option with costs or constraints need not be beneficial in every model.

- **lean-verifiable:** Taking a maximum over available actions gives precise order inequalities.
- **numeric-demo:** Simulate exploration under explicit costs and stopping rules.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-asymmetric-payoffs](#c-asymmetric-payoffs).

<a id="c-lindy"></a>
## Conditional lifetime and Lindy models (`c-lindy`)

Home: `content/incerto-lindy.md` (proposed). Milestone: **M3**. Lead: `astra-max`.

A selected lifetime model does not establish a universal age law.

- **lean-verifiable:** Pareto conditional-life formulas have explicit moment conditions.
- **empirical:** Historical longevity claims need censoring and cohort analysis.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pareto-moments](#c-pareto-moments), [c-survivorship](#c-survivorship).

<a id="c-agency"></a>
## Agency, incentives, and risk transfer (`c-agency`)

Home: `content/incerto-agency.md` (proposed). Milestone: **M3**. Lead: `astra-max`.

State who bears losses, observes actions, and can leave.

- **lean-verifiable:** A finite principal-agent model can check incentive inequalities.
- **numeric-demo:** Compare reward rules on identical outcome paths.
- **prose-only:** Fairness and responsibility remain normative questions.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-asymmetric-payoffs](#c-asymmetric-payoffs).

<a id="c-minority-rule"></a>
## Threshold preferences and collective outcomes (`c-minority-rule`)

Home: `content/incerto-minority-rule.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

Do not infer a universal sociological law from a threshold toy model.

- **numeric-demo:** A finite mixing model illustrates parameter-dependent collective effects.
- **empirical:** Applications need actual network and preference data.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-path-dependence](#c-path-dependence).

<a id="c-costly-signals"></a>
## Commitment, signals, and revealed preferences (`c-costly-signals`)

Home: `content/incerto-costly-signals.md` (proposed). Milestone: **M3**. Lead: `astra-max`.

Separate an equilibrium calculation from claims about real motives.

- **lean-verifiable:** Specified signaling games admit finite incentive checks.
- **prose-only:** Actions need not uniquely reveal beliefs or values.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-agency](#c-agency).

<a id="c-inequality-mobility"></a>
## Inequality, mobility, and population definitions (`c-inequality-mobility`)

Home: `content/incerto-inequality-mobility.md` (proposed). Milestone: **M4**. Lead: `astra-xhigh`.

Fix units, population entry/exit, and observation windows.

- **empirical:** Cross-sectional concentration and transitions require different data.
- **numeric-demo:** Simulate equal marginals with different mobility.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-path-dependence](#c-path-dependence).

<a id="c-ethics"></a>
## Reciprocity, responsibility, and professional ethics (`c-ethics`)

Home: `content/incerto-ethics.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

A formal payoff model cannot verify a moral conclusion.

- **prose-only:** These are ethical arguments and institutional judgments.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-agency](#c-agency).

<a id="c-rationality"></a>
## Rationality as an explicit decision criterion (`c-rationality`)

Home: `content/incerto-rationality.md` (proposed). Milestone: **M3**. Lead: `astra-xhigh`.

State the criterion and information set before calling an action rational.

- **prose-only:** Compare consistency, survival, and welfare criteria without equating them.
- **numeric-demo:** Counterexamples expose differences between decision criteria.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-ruin"></a>
## Ruin and repeated exposure (`c-ruin`)

Home: `content/incerto-ruin.md` (proposed). Milestone: **M3**. Lead: `astra-max`.

No almost-sure ruin claim from unspecified dependence or a merely positive time-varying hazard.

- **lean-verifiable:** Independent repeated trials with fixed positive ruin probability give an exact finite-horizon formula and limit.
- **numeric-demo:** Compare finite-horizon outcomes and dependence assumptions.
- **prose-only:** Precaution adds a normative decision premise.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-ergodicity"></a>
## Time averages and ensemble averages (`c-ergodicity`)

Home: `content/incerto-ergodicity.md` (proposed). Milestone: **M3**. Lead: `astra-max`.

Separate ergodic theorems, absorbing ruin, and a chosen growth objective.

- **lean-verifiable:** Finite multiplicative examples and scoped log-growth results are formalizable.
- **numeric-demo:** Compare cross-sectional wealth with one path through time.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-ruin](#c-ruin).

<a id="c-moment-estimation"></a>
## Moment-estimation failure (`c-moment-estimation`)

Home: `content/incerto-moment-estimation.md` (proposed). Milestone: **M2**. Lead: `astra-max`.

Start with Pareto regimes and the existing plug-in singularity; no universal estimator ranking.

- **lean-verifiable:** Separate moment existence from estimator integrability and consistency.
- **numeric-demo:** Run bounded, reproducible repeated-sample comparisons.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pareto-moments](#c-pareto-moments), [c-plugin](#c-plugin).

<a id="c-inference-asymmetry"></a>
## Finite-sample evidence and tail non-identification (`c-inference-asymmetry`)

Home: `content/incerto-inference-asymmetry.md` (proposed). Milestone: **M2**. Lead: `astra-max`.

Quantify sample size, contamination probability, distance, and the moment that differs.

- **lean-verifiable:** Construct a specified rare-contamination counterexample with controlled sample discrepancy.
- **numeric-demo:** Compare models indistinguishable in most finite samples.
- **prose-only:** Explain the limits of the result without claiming a universal undecidability theorem.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-exceedances](#c-exceedances), [c-induction](#c-induction), [c-moment-estimation](#c-moment-estimation).

<a id="c-cauchy-running"></a>
## Cauchy running statistics (`c-cauchy-running`)

Home: `content/incerto-cauchy-running.md` (proposed). Milestone: **M2**. Lead: `astra-max`.

Synthetic experiment only; the legacy Chapter 4 locator needs edition reconciliation.

- **numeric-demo:** Fixed-seed repeated paths expose unstable averages and Monte Carlo uncertainty.
- **lean-verifiable:** Distributional stability is a separate later theorem candidate.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-stable-clt](#c-stable-clt), [c-lln-failure](#c-lln-failure).

<a id="c-mixture-uncertainty"></a>
## Parameter mixtures and recursive uncertainty (`c-mixture-uncertainty`)

Home: `content/incerto-mixture-uncertainty.md` (proposed). Milestone: **M6**. Lead: `astra-max`.

Reuse Normix mixture definitions; a recursive construction needs an explicit limiting model.

- **lean-verifiable:** Specified mixtures permit moment and tail calculations.
- **numeric-demo:** Simulate a declared finite hierarchy of parameter uncertainty.

Existing cross-track foundations (partial prerequisites, not this proposed claim): [content/normix-normal-mixtures.md](../../../content/normix-normal-mixtures.md), [content/normix-generalized-hyperbolic.md](../../../content/normix-generalized-hyperbolic.md).

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pareto-moments](#c-pareto-moments).

<a id="c-multivariate-tails"></a>
## Multivariate tails and dependence summaries (`c-multivariate-tails`)

Home: `content/incerto-multivariate-tails.md` (proposed). Milestone: **M6**. Lead: `astra-max`.

PCA and covariance interpretations require moments; mutual information needs its own existence checks.

- **lean-verifiable:** A specified model can test existence of covariance and validity of dependence formulas.
- **numeric-demo:** Contrast correlation, tail dependence, and geometric diagnostics.

Existing cross-track foundations (partial prerequisites, not this proposed claim): [content/normix-normal-mixtures.md](../../../content/normix-normal-mixtures.md).

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-tail-geometry](#c-tail-geometry), [c-mixture-uncertainty](#c-mixture-uncertainty).

<a id="c-kappa"></a>
## Finite-sum concentration metric (`c-kappa`)

Home: `content/incerto-kappa.md` (proposed). Milestone: **M6**. Lead: `astra-max`.

Do not extend the metric to undefined moments or claim a universal sample-size guarantee.

- **lean-verifiable:** Re-derive the selected paper metric under its finite-first-moment assumptions.
- **numeric-demo:** Estimate it over declared finite aggregation sizes.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pareto-moments](#c-pareto-moments), [c-stable-clt](#c-stable-clt).

<a id="c-sp500"></a>
## Equity-return tail study (`c-sp500`)

Home: `content/incerto-sp500.md` (proposed). Milestone: **M4**. Lead: `astra-xhigh`.

Record price adjustments, sampling interval, nonstationarity, dependence, and data rights.

- **empirical:** An actual return series permits a reproducible, dated model comparison.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-threshold](#c-threshold), [c-moment-estimation](#c-moment-estimation).

<a id="c-calibration-payoff"></a>
## Probability calibration versus payoff accuracy (`c-calibration-payoff`)

Home: `content/incerto-calibration-payoff.md` (proposed). Milestone: **M6**. Lead: `astra-max`.

A calibrated event forecast need not estimate an unbounded payoff well.

- **lean-verifiable:** Finite examples separate event probabilities from magnitude-sensitive expectations.
- **numeric-demo:** Compare scoring rules and payoff errors under the same forecasts.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-asymmetric-payoffs](#c-asymmetric-payoffs), [c-moment-estimation](#c-moment-estimation).

<a id="c-forecast-martingale"></a>
## Forecast updating and martingale constraints (`c-forecast-martingale`)

Home: `content/incerto-forecast-martingale.md` (proposed). Milestone: **M6**. Lead: `astra-max`.

Changing information sets or forecasting systems can break a naive empirical comparison.

- **lean-verifiable:** Conditional probabilities under one filtration satisfy scoped martingale identities.
- **empirical:** Timestamped forecasts allow model-dependent diagnostics.

Existing cross-track foundations (partial prerequisites, not this proposed claim): [content/information-geometry-conditional-expectation.md](../../../content/information-geometry-conditional-expectation.md).

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-calibration-payoff](#c-calibration-payoff).

<a id="c-gini"></a>
## Gini estimation with heavy tails (`c-gini`)

Home: `content/incerto-gini.md` (proposed). Milestone: **M4**. Lead: `astra-max`.

Infinite variance and infinite mean are different regimes.

- **lean-verifiable:** Population and estimator properties require nonnegative values and a finite positive mean.
- **numeric-demo:** Compare finite-sample bias under stated Pareto regimes.
- **empirical:** Application needs population and measurement definitions.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pareto-moments](#c-pareto-moments), [c-inequality-mobility](#c-inequality-mobility).

<a id="c-quantile-share"></a>
## Quantile contributions and aggregation bias (`c-quantile-share`)

Home: `content/incerto-quantile-share.md` (proposed). Milestone: **M4**. Lead: `astra-max`.

Check the assumptions behind any super-additivity claim.

- **lean-verifiable:** A specified tail-share functional permits exact distribution calculations.
- **numeric-demo:** Compare aggregation and estimation orders.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pareto-moments](#c-pareto-moments).

<a id="c-shadow-mean"></a>
## Bounded-tail transformations and shadow moments (`c-shadow-mean`)

Home: `content/incerto-shadow-mean.md` (proposed). Milestone: **M4**. Lead: `astra-max`.

Keep the physical upper bound and model uncertainty explicit; scope remains an owner decision.

- **lean-verifiable:** A declared invertible transformation and support bound permit exact integrals.
- **numeric-demo:** Vary endpoint, threshold, and fitted tail parameters.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-gpd](#c-gpd), [c-mean-excess](#c-mean-excess).

<a id="c-conflict-study"></a>
## Historical conflict severity study (`c-conflict-study`)

Home: `content/incerto-conflict-study.md` (proposed). Milestone: **M4**. Lead: `astra-xhigh`.

Do not treat uncertain historical counts as iid measurements or equate tail fit with a trend conclusion.

- **empirical:** Reanalysis requires event definitions, reporting ranges, exposure adjustments, and licensed data.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-shadow-mean](#c-shadow-mean), [c-threshold](#c-threshold).

<a id="c-disease-study"></a>
## Historical epidemic severity study (`c-disease-study`)

Home: `content/incerto-disease-study.md` (proposed). Milestone: **M4**. Lead: `astra-xhigh`.

Study historical severity distributions; no clinical or public-health policy claim follows from the tail fit alone.

- **empirical:** Compare competing analyses with explicit selection, censoring, and finite-population bounds.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-shadow-mean](#c-shadow-mean), [c-threshold](#c-threshold).

<a id="c-random-alpha"></a>
## Random tail exponents (`c-random-alpha`)

Home: `content/incerto-random-alpha.md` (proposed). Milestone: **M6**. Lead: `astra-max`.

The mixing law and its support near zero control the result.

- **lean-verifiable:** A specified mixing law over alpha permits survival and integrability analysis.
- **numeric-demo:** Compare finite-range apparent exponents with asymptotic behavior.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-regular-variation](#c-regular-variation), [c-mixture-uncertainty](#c-mixture-uncertainty).

<a id="c-pvalues"></a>
## P-value variability and selection (`c-pvalues`)

Home: `content/incerto-pvalues.md` (proposed). Milestone: **M6**. Lead: `astra-max`.

A p-value is not a posterior probability; distinguish variability from invalid calibration.

- **lean-verifiable:** Distribution statements need a fully specified null, alternative, and testing rule.
- **numeric-demo:** Repeat tests and selection under one declared model.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-multiple-testing](#c-multiple-testing).

<a id="c-maximum-entropy"></a>
## Tail constraints and maximum entropy (`c-maximum-entropy`)

Home: `content/incerto-maximum-entropy.md` (proposed). Milestone: **M6**. Lead: `astra-max`.

Use IG exponential-family definitions; a formal optimum does not validate chosen constraints.

- **lean-verifiable:** A constrained optimization problem needs feasibility, normalization, and uniqueness checks.
- **numeric-demo:** Numerical solutions can be checked against constraints.

Existing cross-track foundations (partial prerequisites, not this proposed claim): [content/information-geometry-exponential-families.md](../../../content/information-geometry-exponential-families.md), [content/normix-exponential-family-core.md](../../../content/normix-exponential-family-core.md).

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-point-forecast"></a>
## Point forecasts under heavy-tailed losses (`c-point-forecast`)

Home: `content/incerto-point-forecast.md` (proposed). Milestone: **M6**. Lead: `astra-max`.

Specify median/mean/quantile targets and what happens when expected loss is infinite.

- **lean-verifiable:** The optimal point summary depends on the loss and existence of its expectation.
- **numeric-demo:** Compare losses on identical simulated draws.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pareto-moments](#c-pareto-moments), [c-calibration-payoff](#c-calibration-payoff).

<a id="c-ml-econometrics"></a>
## Tail assumptions in statistical pipelines (`c-ml-econometrics`)

Home: `content/incerto-ml-econometrics.md` (proposed). Milestone: **M4**. Lead: `astra-xhigh`.

No blanket rejection of econometrics, machine learning, or behavioral economics.

- **numeric-demo:** Stress a specified estimator under controlled contamination.
- **empirical:** Evaluate one documented pipeline on data with leakage and dependence checks.
- **prose-only:** Map which assumptions a published method actually requires.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-moment-estimation](#c-moment-estimation), [c-multiple-testing](#c-multiple-testing).

<a id="c-payoff-algebra"></a>
## Option and forward payoff algebra (`c-payoff-algebra`)

Home: `content/incerto-payoff-algebra.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

Start with European terminal payoffs and explicit financing conventions.

- **lean-verifiable:** Piecewise real functions support exact parity and order identities.
- **numeric-demo:** Original payoff diagrams illustrate cases and boundaries.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-asymmetric-payoffs](#c-asymmetric-payoffs).

<a id="c-arbitrage"></a>
## Finite-state arbitrage and price bounds (`c-arbitrage`)

Home: `content/incerto-arbitrage.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

Separate terminal payoff identities from trading admissibility and market completeness.

- **lean-verifiable:** Finite portfolio inequalities and specified transaction costs are checkable.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra).

<a id="c-market-making"></a>
## Market making and inventory exposure (`c-market-making`)

Home: `content/incerto-market-making.md` (proposed). Milestone: **M5**. Lead: `astra-xhigh`.

Account for adverse selection and fill assumptions.

- **numeric-demo:** An explicit quote/inventory model illustrates risk and execution.
- **empirical:** Market claims require timestamped, licensed quote and trade data.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra).

<a id="c-liquidity"></a>
## Liquidity gaps and hedge execution (`c-liquidity`)

Home: `content/incerto-liquidity.md` (proposed). Milestone: **M5**. Lead: `astra-xhigh`.

A continuous-path replication theorem does not cover discontinuous execution.

- **numeric-demo:** Discrete jumps and transaction costs expose replication error.
- **empirical:** Empirical execution costs depend on venue, size, and timestamp.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-market-making](#c-market-making).

<a id="c-volatility-surface"></a>
## Volatility, correlation, and surface conventions (`c-volatility-surface`)

Home: `content/incerto-volatility-surface.md` (proposed). Milestone: **M5**. Lead: `astra-xhigh`.

Distinguish realized, implied, local, and stochastic volatility.

- **numeric-demo:** Inspect parameter and quotation conventions on synthetic surfaces.
- **empirical:** Market surfaces require licensed observations and cleaning.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra).

<a id="c-greeks"></a>
## Delta, gamma, vega, theta, and mixed sensitivities (`c-greeks`)

Home: `content/incerto-greeks.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

Keep Greek notation local and distinguish derivative exposure from realized hedge P&L.

- **lean-verifiable:** Derivatives of a specified price function are exact local statements.
- **numeric-demo:** Compare derivatives with finite differences and finite shocks.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra), [c-jensen](#c-jensen).

<a id="c-hedging-error"></a>
## Discrete hedging and joint Greek exposure (`c-hedging-error`)

Home: `content/incerto-hedging-error.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

Specify self-financing, funding, rebalancing, and transaction conventions.

- **lean-verifiable:** Finite rebalancing cash-flow identities can be formalized before continuous limits.
- **numeric-demo:** Measure discretization, jump, cost, and model errors separately.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-greeks](#c-greeks), [c-liquidity](#c-liquidity).

<a id="c-basis-buckets"></a>
## Basis, fungibility, and risk buckets (`c-basis-buckets`)

Home: `content/incerto-basis-buckets.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

Netting exposures across mismatched maturities or instruments leaves basis risk.

- **lean-verifiable:** Finite aggregation and cancellation identities have explicit matching conditions.
- **numeric-demo:** Compare bucketed approximations with full repricing.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-greeks](#c-greeks).

<a id="c-model-risk"></a>
## Pricing-model and distribution risk (`c-model-risk`)

Home: `content/incerto-model-risk.md` (proposed). Milestone: **M5**. Lead: `astra-xhigh`.

Agreement on several prices need not determine the full terminal distribution.

- **numeric-demo:** Hold payoff fixed while changing calibrated model families.
- **prose-only:** Separate trading practice from model-validity and historical claims.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-volatility-surface](#c-volatility-surface), [c-epistemic-uncertainty](#c-epistemic-uncertainty).

<a id="c-digitals"></a>
## European and American digital options (`c-digitals`)

Home: `content/incerto-digitals.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

Separate terminal indicators from first-passage events.

- **lean-verifiable:** Terminal digital payoff limits and bounds are tractable; hitting-time results are separate.
- **numeric-demo:** Resolution and path monitoring materially affect estimates.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra).

<a id="c-barriers"></a>
## Barrier contracts and monitoring (`c-barriers`)

Home: `content/incerto-barriers.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

Specify inclusive boundaries, rebate timing, and continuous versus discrete monitoring.

- **lean-verifiable:** Pathwise payoff decompositions can be proved with compatible conventions.
- **numeric-demo:** Discrete monitoring and bridge corrections expose numerical assumptions.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-digitals](#c-digitals), [c-hedging-error](#c-hedging-error).

<a id="c-compound-options"></a>
## Compound and chooser options (`c-compound-options`)

Home: `content/incerto-compound-options.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

Exercise timing and information sets determine the payoff.

- **lean-verifiable:** Nested payoff identities admit exact finite-state statements.
- **numeric-demo:** Use small trees with explicit exercise conventions.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra).

<a id="c-multiasset-options"></a>
## Multi-asset payoff dependence (`c-multiasset-options`)

Home: `content/incerto-multiasset-options.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

A scalar correlation does not determine all nonlinear joint payoffs.

- **lean-verifiable:** Pathwise bounds and finite-state prices can be formalized.
- **numeric-demo:** Change dependence while preserving marginal distributions.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra), [c-multivariate-tails](#c-multivariate-tails).

<a id="c-path-options"></a>
## Asian and lookback path functionals (`c-path-options`)

Home: `content/incerto-path-options.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

Separate a finite average or maximum from a continuous-time functional.

- **lean-verifiable:** Finite monitored-path bounds and identities have a manageable scope.
- **numeric-demo:** Compare sampling grids under the same stochastic model.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-payoff-algebra](#c-payoff-algebra).

<a id="c-brownian"></a>
## Brownian simulation and discretization (`c-brownian`)

Home: `content/incerto-brownian.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

A finite random-walk approximation is not a proof of a Brownian theorem.

- **numeric-demo:** Check sample increment moments and grid-refinement behavior for a declared scheme.
- **lean-verifiable:** Distributional properties need a later probability-library audit.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-pricing-measures"></a>
## Pricing measures and incomplete markets (`c-pricing-measures`)

Home: `content/incerto-pricing-measures.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

A forward-mean constraint alone does not identify a unique risk-neutral distribution.

- **lean-verifiable:** Finite-state examples show when moment constraints leave multiple pricing measures.
- **numeric-demo:** Compute price intervals under explicit constraints.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-arbitrage](#c-arbitrage).

<a id="c-numeraire"></a>
## Numeraire changes and relative prices (`c-numeraire`)

Home: `content/incerto-numeraire.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

Keep physical and pricing measures distinct; continuous-time extension is later.

- **lean-verifiable:** Finite-state change-of-measure identities require a positive numeraire and normalization.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pricing-measures](#c-pricing-measures).

<a id="c-correlation-constraints"></a>
## Feasible correlation matrices (`c-correlation-constraints`)

Home: `content/incerto-correlation-constraints.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

Finite second moments and consistent normalization are required.

- **lean-verifiable:** Positive semidefiniteness gives exact three-variable feasibility bounds.
- **numeric-demo:** Show incompatible pairwise inputs and their pricing consequences.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: none within this inventory.

<a id="c-risk-measures"></a>
## VaR, expected shortfall, and model limits (`c-risk-measures`)

Home: `content/incerto-risk-measures.md` (proposed). Milestone: **M5**. Lead: `astra-max`.

Expected shortfall may be infinite; VaR subadditivity needs conditions.

- **lean-verifiable:** Finite-distribution counterexamples and scoped coherence statements are checkable.
- **numeric-demo:** Show tail sensitivity and estimation uncertainty.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pareto-moments](#c-pareto-moments).

<a id="c-stochastic-pricing"></a>
## Ito calculus and continuous-time pricing (`c-stochastic-pricing`)

Home: `content/incerto-stochastic-pricing.md` (proposed). Milestone: **M6**. Lead: `astra-max`.

Library feasibility is unknown; do not promise a full BSM or stochastic-volatility proof in M5.

- **lean-verifiable:** A full development needs stochastic integrals, admissibility, and analytic hypotheses.
- **numeric-demo:** Compare discretizations only after a model and convergence target are fixed.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-brownian](#c-brownian), [c-pricing-measures](#c-pricing-measures), [c-hedging-error](#c-hedging-error).

<a id="c-power-option"></a>
## Option tails under power laws (`c-power-option`)

Home: `content/incerto-power-option.md` (proposed). Milestone: **M6**. Lead: `astra-max`.

Specify pricing measure, tail regime, and finite call-price condition.

- **lean-verifiable:** Integrating a stated survival tail gives scoped price relations and moment gates.
- **numeric-demo:** Compare exact power laws with finite-strike approximations.

Coverage: Proposed original note; path is reserved in this plan only.

Prerequisites: [c-pareto-moments](#c-pareto-moments), [c-pricing-measures](#c-pricing-measures).
