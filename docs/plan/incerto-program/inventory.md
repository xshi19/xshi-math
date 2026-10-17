# Book and chapter inventory

This concept map uses editorial topic labels, not copied chapter summaries.
`state.yaml` owns the records; [sources.md](sources.md) records locator evidence.
An asterisk marks an existing concept body, not Lean verification.

Completion covers **2 technical books, 48 numbered chapters, 64 mapped book
source units, 14 paper records and 72 concepts**. The required 2025 Technical
Incerto additions await exact reconciliation and may expand these counts.
All **101 concept IDs** remain: **72 in scope, 29 out of scope**. The historical
inventory also retains 5 excluded books, 77 numbered chapters and 123 units,
for totals of 7 books, 125 numbered chapters and 187 units.

Statistical Consequences of Fat Tails / Technical Incerto is first and highest
priority. Dynamic Hedging includes continuous-time teaching and numerics.
Every active concept follows website math → Python → optional Lean. A Lean
skip cannot remove mathematical source coverage.

In technical rows, a concept marked `out-of-scope` is a retained association,
not a required deliverable. `required_concept_ids` in state defines the active
mapping. Non-technical book tables are retained history only; those books may
supply a cited origin reference, with no interpretive or prose-only coverage.


## Statistical Consequences of Fat Tails / Technical Incerto, volume 1

Book ID: `scft`. Status: **in-scope**. Baseline: 2020 print spine, ISBN 9781544508054; compare arXiv:2001.10488v2; v4 expansion not yet reconciled.

2020 locator namespace retained; 2025 additions are required completion scope and await direct reconciliation. Statistical Consequences of Fat Tails is the first and highest-priority book.

| Unit ID | Source locator | Editorial topic | Concepts | Status |
| --- | --- | --- | --- | --- |
| `scft-ch01` | ch. 1 | Program and limits | [`c-tail-catalog`](concepts.md#c-tail-catalog) *, [`c-induction`](concepts.md#c-induction) (out-of-scope) | in-scope |
| `scft-ch02` | ch. 2 | Definitions and conventions | [`c-exceedances`](concepts.md#c-exceedances) *, [`c-pareto`](concepts.md#c-pareto) *, [`c-evi`](concepts.md#c-evi) *, [`c-tail-catalog`](concepts.md#c-tail-catalog) * | in-scope |
| `scft-ch03` | ch. 3 | Inference and exposure | [`c-inference-asymmetry`](concepts.md#c-inference-asymmetry), [`c-asymmetric-payoffs`](concepts.md#c-asymmetric-payoffs), [`c-ruin`](concepts.md#c-ruin) | in-scope |
| `scft-ch04` | ch. 4 | Finite-moment heavy tails | [`c-mixture-uncertainty`](concepts.md#c-mixture-uncertainty), [`c-body-shoulder`](concepts.md#c-body-shoulder) *, [`c-moment-estimation`](concepts.md#c-moment-estimation) | in-scope |
| `scft-ch05` | ch. 5 | Power-law and sum-tail classes | [`c-pareto`](concepts.md#c-pareto) *, [`c-regular-variation`](concepts.md#c-regular-variation) *, [`c-subexponential`](concepts.md#c-subexponential) *, [`c-double-pareto`](concepts.md#c-double-pareto) *, [`c-tail-ratio`](concepts.md#c-tail-ratio) *, [`c-karamata`](concepts.md#c-karamata) *, [`c-pareto-moments`](concepts.md#c-pareto-moments) * | in-scope |
| `scft-ch06` | ch. 6 | Dependence in several dimensions | [`c-tail-geometry`](concepts.md#c-tail-geometry) *, [`c-multivariate-tails`](concepts.md#c-multivariate-tails) | in-scope |
| `scft-ch07` | ch. 7 | Averaging and limiting laws | [`c-lln-failure`](concepts.md#c-lln-failure) *, [`c-stable-clt`](concepts.md#c-stable-clt) *, [`c-max-sum`](concepts.md#c-max-sum) *, [`c-cauchy-running`](concepts.md#c-cauchy-running) | in-scope |
| `scft-ch08` | ch. 8 | Finite-sum concentration | [`c-kappa`](concepts.md#c-kappa) | in-scope |
| `scft-ch09` | ch. 9 | Extremes and unobserved tails | [`c-gev`](concepts.md#c-gev) *, [`c-frechet`](concepts.md#c-frechet) *, [`c-pbdh`](concepts.md#c-pbdh) *, [`c-gpd`](concepts.md#c-gpd) *, [`c-evi`](concepts.md#c-evi) *, [`c-hill`](concepts.md#c-hill) *, [`c-mean-excess`](concepts.md#c-mean-excess) *, [`c-threshold`](concepts.md#c-threshold) * | in-scope |
| `scft-ch10` | ch. 10 | Equity-return evidence | [`c-sp500`](concepts.md#c-sp500) | in-scope |
| `scft-ch11` | ch. 11 | Probabilities and magnitudes | [`c-calibration-payoff`](concepts.md#c-calibration-payoff), [`c-point-forecast`](concepts.md#c-point-forecast) | in-scope |
| `scft-ch12` | ch. 12 | Coherent forecast updating | [`c-forecast-martingale`](concepts.md#c-forecast-martingale) | in-scope |
| `scft-ch13` | ch. 13 | Heavy-tailed inequality estimation | [`c-gini`](concepts.md#c-gini) | in-scope |
| `scft-ch14` | ch. 14 | Contributions above quantiles | [`c-quantile-share`](concepts.md#c-quantile-share) | in-scope |
| `scft-ch15` | ch. 15 | Finite bounds and tail transforms | [`c-shadow-mean`](concepts.md#c-shadow-mean) | in-scope |
| `scft-ch16` | ch. 16 | Conflict-severity evidence | [`c-conflict-study`](concepts.md#c-conflict-study) | in-scope |
| `scft-ch17` | ch. 17 | Uncertainty about parameters | [`c-mixture-uncertainty`](concepts.md#c-mixture-uncertainty) | in-scope |
| `scft-ch18` | ch. 18 | Uncertain power-law exponents | [`c-random-alpha`](concepts.md#c-random-alpha) | in-scope |
| `scft-ch19` | ch. 19 | Testing and selective inference | [`c-pvalues`](concepts.md#c-pvalues), [`c-multiple-testing`](concepts.md#c-multiple-testing) | in-scope |
| `scft-ch20` | ch. 20 | Option-model assumptions | [`c-model-risk`](concepts.md#c-model-risk), [`c-stochastic-pricing`](concepts.md#c-stochastic-pricing) | in-scope |
| `scft-ch21` | ch. 21 | Pricing under limited constraints | [`c-pricing-measures`](concepts.md#c-pricing-measures) | in-scope |
| `scft-ch22` | ch. 22 | Trading practice and pricing narratives | [`c-tacit-knowledge`](concepts.md#c-tacit-knowledge) (out-of-scope), [`c-model-risk`](concepts.md#c-model-risk), [`c-hedging-error`](concepts.md#c-hedging-error) | in-scope |
| `scft-ch23` | ch. 23 | Power-law option tails | [`c-power-option`](concepts.md#c-power-option) | in-scope |
| `scft-ch24` | ch. 24 | Finance calculations under tail risk | [`c-moment-estimation`](concepts.md#c-moment-estimation), [`c-jensen`](concepts.md#c-jensen), [`c-numeraire`](concepts.md#c-numeraire), [`c-risk-measures`](concepts.md#c-risk-measures) | in-scope |
| `scft-ch25` | ch. 25 | Entropy under tail constraints | [`c-maximum-entropy`](concepts.md#c-maximum-entropy) | in-scope |
| `scft-appa` | appendix A | Additional tail models | [`c-tail-catalog`](concepts.md#c-tail-catalog) *, [`c-pareto`](concepts.md#c-pareto) * | in-scope |
| `scft-appb` | appendix B | Growth transformations | [`c-ergodicity`](concepts.md#c-ergodicity), [`c-mixture-uncertainty`](concepts.md#c-mixture-uncertainty) | in-scope |
| `scft-appc` | appendix C | Large-deviation conditions | [`c-cramer`](concepts.md#c-cramer) * | in-scope |
| `scft-appd` | appendix D | Calibration with power-law tails | [`c-plugin`](concepts.md#c-plugin) *, [`c-hill`](concepts.md#c-hill) *, [`c-threshold`](concepts.md#c-threshold) * | in-scope |
| `scft-appe` | appendix E | Econometric assumptions | [`c-ml-econometrics`](concepts.md#c-ml-econometrics) | in-scope |
| `scft-appf` | appendix F | Learning algorithms and tails | [`c-ml-econometrics`](concepts.md#c-ml-econometrics) | in-scope |
| `scft-appg` | appendix G | Conflict risk interpretation | [`c-conflict-study`](concepts.md#c-conflict-study) | in-scope |
| `scft-apph` | appendix H | Behavioral evidence and tails | [`c-biases`](concepts.md#c-biases) (out-of-scope), [`c-ml-econometrics`](concepts.md#c-ml-econometrics) | in-scope |

## Dynamic Hedging

Book ID: `dh`. Status: **in-scope**. Baseline: 1997 Wiley, ISBN 9780471152804.

Includes continuous-time mathematics as teaching and numerics; optional Lean feasibility cannot reduce book scope.

| Unit ID | Source locator | Editorial topic | Concepts | Status |
| --- | --- | --- | --- | --- |
| `dh-ch01` | ch. 1 | Instrument payoff definitions | [`c-payoff-algebra`](concepts.md#c-payoff-algebra) | in-scope |
| `dh-ch02` | ch. 2 | Generalized payoff representations | [`c-payoff-algebra`](concepts.md#c-payoff-algebra) | in-scope |
| `dh-ch03` | ch. 3 | Quoting and inventory | [`c-market-making`](concepts.md#c-market-making) | in-scope |
| `dh-ch04` | ch. 4 | Discontinuous liquidity | [`c-liquidity`](concepts.md#c-liquidity) | in-scope |
| `dh-ch05` | ch. 5 | Arbitrage constraints | [`c-arbitrage`](concepts.md#c-arbitrage) | in-scope |
| `dh-ch06` | ch. 6 | Volatility and dependence | [`c-volatility-surface`](concepts.md#c-volatility-surface), [`c-correlation-constraints`](concepts.md#c-correlation-constraints) | in-scope |
| `dh-ch07` | ch. 7 | First price sensitivity | [`c-greeks`](concepts.md#c-greeks) | in-scope |
| `dh-ch08` | ch. 8 | Second price sensitivity | [`c-greeks`](concepts.md#c-greeks) | in-scope |
| `dh-ch09` | ch. 9 | Volatility sensitivity | [`c-greeks`](concepts.md#c-greeks), [`c-volatility-surface`](concepts.md#c-volatility-surface) | in-scope |
| `dh-ch10` | ch. 10 | Time and mixed sensitivities | [`c-greeks`](concepts.md#c-greeks) | in-scope |
| `dh-ch11` | ch. 11 | Joint sensitivity behavior | [`c-hedging-error`](concepts.md#c-hedging-error), [`c-greeks`](concepts.md#c-greeks) | in-scope |
| `dh-ch12` | ch. 12 | Exposure matching | [`c-basis-buckets`](concepts.md#c-basis-buckets) | in-scope |
| `dh-ch13` | ch. 13 | Execution details | [`c-liquidity`](concepts.md#c-liquidity), [`c-market-making`](concepts.md#c-market-making) | in-scope |
| `dh-ch14` | ch. 14 | Risk decomposition | [`c-basis-buckets`](concepts.md#c-basis-buckets) | in-scope |
| `dh-ch15` | ch. 15 | Distribution and model choice | [`c-model-risk`](concepts.md#c-model-risk) | in-scope |
| `dh-ch16` | ch. 16 | Trading and model use | [`c-model-risk`](concepts.md#c-model-risk), [`c-hedging-error`](concepts.md#c-hedging-error) | in-scope |
| `dh-ch17` | ch. 17 | Terminal digital claims | [`c-digitals`](concepts.md#c-digitals) | in-scope |
| `dh-ch18` | ch. 18 | First-passage digital claims | [`c-digitals`](concepts.md#c-digitals) | in-scope |
| `dh-ch19` | ch. 19 | Barrier structure | [`c-barriers`](concepts.md#c-barriers) | in-scope |
| `dh-ch20` | ch. 20 | Barrier hedging | [`c-barriers`](concepts.md#c-barriers), [`c-hedging-error`](concepts.md#c-hedging-error) | in-scope |
| `dh-ch21` | ch. 21 | Nested options | [`c-compound-options`](concepts.md#c-compound-options) | in-scope |
| `dh-ch22` | ch. 22 | Joint-asset claims | [`c-multiasset-options`](concepts.md#c-multiasset-options) | in-scope |
| `dh-ch23` | ch. 23 | Path-dependent claims | [`c-path-options`](concepts.md#c-path-options) | in-scope |
| `dh-moda` | module A | Simulated diffusion paths | [`c-brownian`](concepts.md#c-brownian) | in-scope |
| `dh-modb` | module B | Pricing probabilities | [`c-pricing-measures`](concepts.md#c-pricing-measures) | in-scope |
| `dh-modc` | module C | Relative price units | [`c-numeraire`](concepts.md#c-numeraire) | in-scope |
| `dh-modd` | module D | Correlation feasibility | [`c-correlation-constraints`](concepts.md#c-correlation-constraints) | in-scope |
| `dh-mode` | module E | Loss quantiles | [`c-risk-measures`](concepts.md#c-risk-measures) | in-scope |
| `dh-modf` | module F | Payoff ordering | [`c-arbitrage`](concepts.md#c-arbitrage), [`c-payoff-algebra`](concepts.md#c-payoff-algebra) | in-scope |
| `dh-modg` | module G | Continuous-time pricing | [`c-stochastic-pricing`](concepts.md#c-stochastic-pricing), [`c-barriers`](concepts.md#c-barriers) | in-scope |
| `dh-opening` | preface and introductory material | Scope and trading conventions | [`c-model-risk`](concepts.md#c-model-risk) | in-scope |

## Selected technical papers

On-demand inclusion is approved: add a versioned paper when a concrete mathematical claim needs it. These 14 records include one critical response. Metadata was checked at the baseline; exact sections, hypotheses and claims still require reading. Only mathematical models and statistical studies enter completion; interpretive, clinical and policy coverage is excluded.

| Paper ID and source | Concepts |
| --- | --- |
| `paper-fragility` — [Mathematical Definition, Mapping, and Detection of (Anti)Fragility](https://arxiv.org/abs/1208.1189v1) | [`c-fragility`](concepts.md#c-fragility), [`c-jensen`](concepts.md#c-jensen) |
| `paper-precaution` — [The Precautionary Principle (with Application to the Genetic Modification of Organisms)](https://arxiv.org/abs/1410.5787v1) | [`c-ruin`](concepts.md#c-ruin), [`c-decentralization`](concepts.md#c-decentralization), [`c-ethics`](concepts.md#c-ethics) (out-of-scope) |
| `paper-kappa` — [How Much Data Do You Need? An Operational, Pre-Asymptotic Metric for Fat-tailedness](https://arxiv.org/abs/1802.05495v3) | [`c-kappa`](concepts.md#c-kappa), [`c-moment-estimation`](concepts.md#c-moment-estimation) |
| `paper-conflicts` — [On the statistical properties and tail risk of violent conflicts](https://arxiv.org/abs/1505.04722v2) | [`c-shadow-mean`](concepts.md#c-shadow-mean), [`c-conflict-study`](concepts.md#c-conflict-study) |
| `paper-diseases` — [Tail Risk of Contagious Diseases](https://arxiv.org/abs/2004.08658v1) | [`c-shadow-mean`](concepts.md#c-shadow-mean), [`c-disease-study`](concepts.md#c-disease-study) |
| `paper-diseases-comment` — [Scientific comment on Tail risk of contagious diseases](https://arxiv.org/abs/2007.06876v1) | [`c-disease-study`](concepts.md#c-disease-study) |
| `paper-gini` — [Gini estimation under infinite variance](https://arxiv.org/abs/1707.01370v4) | [`c-gini`](concepts.md#c-gini) |
| `paper-quantile` — [On the Super-Additivity and Estimation Biases of Quantile Contributions](https://arxiv.org/abs/1405.1791v3) | [`c-quantile-share`](concepts.md#c-quantile-share) |
| `paper-alpha` — [Stochastic Tail Exponent For Asymmetric Power Laws](https://arxiv.org/abs/1609.02369v3) | [`c-random-alpha`](concepts.md#c-random-alpha) |
| `paper-option-tail` — [Tail Option Pricing Under Power Laws](https://arxiv.org/abs/1908.02347v3) | [`c-power-option`](concepts.md#c-power-option) |
| `paper-pricing` — [Risk Neutral Option Pricing With Neither Dynamic Hedging nor Complete Markets](https://arxiv.org/abs/1405.2609v2) | [`c-pricing-measures`](concepts.md#c-pricing-measures) |
| `paper-entropy` — [Tail Risk Constraints and Maximum Entropy](https://arxiv.org/abs/1412.7647v1) | [`c-maximum-entropy`](concepts.md#c-maximum-entropy) |
| `paper-convex-response` — [Working With Convex Responses: Antifragility From Finance to Oncology](https://arxiv.org/abs/2209.14631v2) | [`c-jensen`](concepts.md#c-jensen), [`c-hormesis`](concepts.md#c-hormesis) |
| `paper-point-forecast` — [On Single Point Forecasts for Fat-Tailed Variables](https://arxiv.org/abs/2007.16096v1) | [`c-point-forecast`](concepts.md#c-point-forecast) |

## Retained books outside completion

Every unit below is **out-of-scope** because its book is non-technical Incerto. The mappings preserve prior references; they schedule no page, chapter review or edition work. An active technical concept appearing here is in scope only through its technical source mapping above.

### Fooled by Randomness

Book ID: `fbr`. Status: **out-of-scope**. Baseline: Updated second edition, 2008 hardcover, ISBN 9781400067930.

Retained historical locator map only. No chapter review, prose coverage or edition reconciliation is scheduled.

| Unit ID | Source locator | Editorial topic | Concepts | Status |
| --- | --- | --- | --- | --- |
| `fbr-ch01` | ch. 1 | Performance attribution | [`c-luck-skill`](concepts.md#c-luck-skill) (out-of-scope), [`c-counterfactuals`](concepts.md#c-counterfactuals) (out-of-scope) | out-of-scope |
| `fbr-ch02` | ch. 2 | Outcome and exposure | [`c-counterfactuals`](concepts.md#c-counterfactuals) (out-of-scope), [`c-asymmetric-payoffs`](concepts.md#c-asymmetric-payoffs) | out-of-scope |
| `fbr-ch03` | ch. 3 | Simulation and observation | [`c-counterfactuals`](concepts.md#c-counterfactuals) (out-of-scope), [`c-noise-monitoring`](concepts.md#c-noise-monitoring) (out-of-scope) | out-of-scope |
| `fbr-ch04` | ch. 4 | Expertise and explanation | [`c-causal-narrative`](concepts.md#c-causal-narrative) (out-of-scope), [`c-skepticism`](concepts.md#c-skepticism) (out-of-scope) | out-of-scope |
| `fbr-ch05` | ch. 5 | Selection on success | [`c-survivorship`](concepts.md#c-survivorship) (out-of-scope), [`c-luck-skill`](concepts.md#c-luck-skill) (out-of-scope) | out-of-scope |
| `fbr-ch06` | ch. 6 | Payoff imbalance | [`c-asymmetric-payoffs`](concepts.md#c-asymmetric-payoffs), [`c-pareto-moments`](concepts.md#c-pareto-moments) * | out-of-scope |
| `fbr-ch07` | ch. 7 | Generalizing from observations | [`c-induction`](concepts.md#c-induction) (out-of-scope), [`c-inference-asymmetry`](concepts.md#c-inference-asymmetry) | out-of-scope |
| `fbr-ch08` | ch. 8 | Comparison populations | [`c-survivorship`](concepts.md#c-survivorship) (out-of-scope), [`c-inequality-mobility`](concepts.md#c-inequality-mobility) (out-of-scope) | out-of-scope |
| `fbr-ch09` | ch. 9 | Searching for patterns | [`c-multiple-testing`](concepts.md#c-multiple-testing) | out-of-scope |
| `fbr-ch10` | ch. 10 | Feedback and concentration | [`c-path-dependence`](concepts.md#c-path-dependence) (out-of-scope), [`c-scalability`](concepts.md#c-scalability) (out-of-scope) | out-of-scope |
| `fbr-ch11` | ch. 11 | Judgments about chance | [`c-biases`](concepts.md#c-biases) (out-of-scope) | out-of-scope |
| `fbr-ch12` | ch. 12 | Learned causal stories | [`c-causal-narrative`](concepts.md#c-causal-narrative) (out-of-scope), [`c-biases`](concepts.md#c-biases) (out-of-scope) | out-of-scope |
| `fbr-ch13` | ch. 13 | Belief revision | [`c-skepticism`](concepts.md#c-skepticism) (out-of-scope), [`c-epistemic-uncertainty`](concepts.md#c-epistemic-uncertainty) (out-of-scope) | out-of-scope |
| `fbr-ch14` | ch. 14 | Responding to chance | [`c-stoicism`](concepts.md#c-stoicism) (out-of-scope) | out-of-scope |
| `fbr-opening` | prologue and prefatory material | Evidence and interpretation | [`c-luck-skill`](concepts.md#c-luck-skill) (out-of-scope), [`c-skepticism`](concepts.md#c-skepticism) (out-of-scope) | out-of-scope |
| `fbr-closing` | epilogue and postscript | Reflection and remaining limits | [`c-stoicism`](concepts.md#c-stoicism) (out-of-scope), [`c-induction`](concepts.md#c-induction) (out-of-scope), [`c-ludic`](concepts.md#c-ludic) (out-of-scope) | out-of-scope |

### The Black Swan

Book ID: `tbs`. Status: **out-of-scope**. Baseline: Second edition, 2010, ISBN 9780812973815.

Retained historical locator map only. No chapter review, prose coverage or edition reconciliation is scheduled.

| Unit ID | Source locator | Editorial topic | Concepts | Status |
| --- | --- | --- | --- | --- |
| `tbs-ch01` | ch. 1 | Unexpected historical events | [`c-black-swan`](concepts.md#c-black-swan) (out-of-scope), [`c-skepticism`](concepts.md#c-skepticism) (out-of-scope) | out-of-scope |
| `tbs-ch02` | ch. 2 | Success with scalable rewards | [`c-scalability`](concepts.md#c-scalability) (out-of-scope), [`c-luck-skill`](concepts.md#c-luck-skill) (out-of-scope) | out-of-scope |
| `tbs-ch03` | ch. 3 | Aggregation regimes | [`c-scalability`](concepts.md#c-scalability) (out-of-scope), [`c-pareto-moments`](concepts.md#c-pareto-moments) * | out-of-scope |
| `tbs-ch04` | ch. 4 | Induction from a finite record | [`c-induction`](concepts.md#c-induction) (out-of-scope), [`c-inference-asymmetry`](concepts.md#c-inference-asymmetry) | out-of-scope |
| `tbs-ch05` | ch. 5 | Selective confirmation | [`c-biases`](concepts.md#c-biases) (out-of-scope), [`c-multiple-testing`](concepts.md#c-multiple-testing) | out-of-scope |
| `tbs-ch06` | ch. 6 | Retrospective explanation | [`c-causal-narrative`](concepts.md#c-causal-narrative) (out-of-scope) | out-of-scope |
| `tbs-ch07` | ch. 7 | Delayed and concentrated rewards | [`c-asymmetric-payoffs`](concepts.md#c-asymmetric-payoffs), [`c-optionality`](concepts.md#c-optionality) (out-of-scope) | out-of-scope |
| `tbs-ch08` | ch. 8 | Missing unsuccessful cases | [`c-survivorship`](concepts.md#c-survivorship) (out-of-scope) | out-of-scope |
| `tbs-ch09` | ch. 9 | Closed-world uncertainty | [`c-ludic`](concepts.md#c-ludic) (out-of-scope) | out-of-scope |
| `tbs-ch10` | ch. 10 | Prediction and expertise | [`c-forecasting`](concepts.md#c-forecasting) (out-of-scope) | out-of-scope |
| `tbs-ch11` | ch. 11 | Unplanned discovery | [`c-optionality`](concepts.md#c-optionality) (out-of-scope), [`c-tacit-knowledge`](concepts.md#c-tacit-knowledge) (out-of-scope) | out-of-scope |
| `tbs-ch12` | ch. 12 | Admitting limited knowledge | [`c-epistemic-uncertainty`](concepts.md#c-epistemic-uncertainty) (out-of-scope), [`c-skepticism`](concepts.md#c-skepticism) (out-of-scope) | out-of-scope |
| `tbs-ch13` | ch. 13 | Decisions with weak forecasts | [`c-barbell`](concepts.md#c-barbell) (out-of-scope), [`c-ruin`](concepts.md#c-ruin) | out-of-scope |
| `tbs-ch14` | ch. 14 | Concentration and feedback | [`c-path-dependence`](concepts.md#c-path-dependence) (out-of-scope), [`c-inequality-mobility`](concepts.md#c-inequality-mobility) (out-of-scope) | out-of-scope |
| `tbs-ch15` | ch. 15 | Gaussian extrapolation | [`c-tail-catalog`](concepts.md#c-tail-catalog) *, [`c-cramer`](concepts.md#c-cramer) * | out-of-scope |
| `tbs-ch16` | ch. 16 | Scale-free tails | [`c-regular-variation`](concepts.md#c-regular-variation) *, [`c-pareto`](concepts.md#c-pareto) *, [`c-stable-clt`](concepts.md#c-stable-clt) * | out-of-scope |
| `tbs-ch17` | ch. 17 | Distributional model misuse | [`c-model-risk`](concepts.md#c-model-risk), [`c-moment-estimation`](concepts.md#c-moment-estimation) | out-of-scope |
| `tbs-ch18` | ch. 18 | Irreducible limits of description | [`c-epistemic-uncertainty`](concepts.md#c-epistemic-uncertainty) (out-of-scope), [`c-ludic`](concepts.md#c-ludic) (out-of-scope) | out-of-scope |
| `tbs-ch19` | ch. 19 | Personal exposure and restraint | [`c-stoicism`](concepts.md#c-stoicism) (out-of-scope), [`c-barbell`](concepts.md#c-barbell) (out-of-scope) | out-of-scope |
| `tbs-opening` | prologue | Observer-relative surprise | [`c-black-swan`](concepts.md#c-black-swan) (out-of-scope) | out-of-scope |
| `tbs-es01` | robustness essay, section 1 | Redundancy | [`c-decentralization`](concepts.md#c-decentralization) | out-of-scope |
| `tbs-es02` | robustness essay, section 2 | System exposure | [`c-fragility`](concepts.md#c-fragility), [`c-ruin`](concepts.md#c-ruin) | out-of-scope |
| `tbs-es03` | robustness essay, section 3 | Claims and responses | [`c-skepticism`](concepts.md#c-skepticism) (out-of-scope) | out-of-scope |
| `tbs-es04` | robustness essay, section 4 | Kinds of uncertainty | [`c-epistemic-uncertainty`](concepts.md#c-epistemic-uncertainty) (out-of-scope) | out-of-scope |
| `tbs-es05` | robustness essay, section 5 | Statistical induction | [`c-inference-asymmetry`](concepts.md#c-inference-asymmetry) | out-of-scope |
| `tbs-es06` | robustness essay, section 6 | Tail and payoff domains | [`c-asymmetric-payoffs`](concepts.md#c-asymmetric-payoffs), [`c-tail-catalog`](concepts.md#c-tail-catalog) * | out-of-scope |
| `tbs-es07` | robustness essay, section 7 | Decisions under tail uncertainty | [`c-barbell`](concepts.md#c-barbell) (out-of-scope), [`c-optionality`](concepts.md#c-optionality) (out-of-scope) | out-of-scope |
| `tbs-es08` | robustness essay, section 8 | Institutional exposure | [`c-agency`](concepts.md#c-agency) (out-of-scope), [`c-decentralization`](concepts.md#c-decentralization) | out-of-scope |
| `tbs-es09` | robustness essay, section 9 | Personal stance | [`c-stoicism`](concepts.md#c-stoicism) (out-of-scope) | out-of-scope |

### The Bed of Procrustes

Book ID: `bop`. Status: **out-of-scope**. Baseline: 2010 historical locator baseline, ISBN 9781400069972; out of completion scope.

Retained historical locator map only. No chapter review, prose coverage or edition reconciliation is scheduled.

| Unit ID | Source locator | Editorial topic | Concepts | Status |
| --- | --- | --- | --- | --- |
| `bop-s01` | unnumbered thematic section 1 (planner ordinal) | Opening observations | [`c-procrustean`](concepts.md#c-procrustean) (out-of-scope), [`c-skepticism`](concepts.md#c-skepticism) (out-of-scope) | out-of-scope |
| `bop-s02` | unnumbered thematic section 2 (planner ordinal) | Competing explanations | [`c-causal-narrative`](concepts.md#c-causal-narrative) (out-of-scope) | out-of-scope |
| `bop-s03` | unnumbered thematic section 3 (planner ordinal) | Existence and categories | [`c-procrustean`](concepts.md#c-procrustean) (out-of-scope), [`c-epistemic-uncertainty`](concepts.md#c-epistemic-uncertainty) (out-of-scope) | out-of-scope |
| `bop-s04` | unnumbered thematic section 4 (planner ordinal) | Sacred values | [`c-ethics`](concepts.md#c-ethics) (out-of-scope) | out-of-scope |
| `bop-s05` | unnumbered thematic section 5 (planner ordinal) | Chance and composure | [`c-luck-skill`](concepts.md#c-luck-skill) (out-of-scope), [`c-stoicism`](concepts.md#c-stoicism) (out-of-scope) | out-of-scope |
| `bop-s06` | unnumbered thematic section 6 (planner ordinal) | Exposure to persuasion | [`c-agency`](concepts.md#c-agency) (out-of-scope), [`c-biases`](concepts.md#c-biases) (out-of-scope) | out-of-scope |
| `bop-s07` | unnumbered thematic section 7 (planner ordinal) | Continuity and adaptation | [`c-procrustean`](concepts.md#c-procrustean) (out-of-scope), [`c-hormesis`](concepts.md#c-hormesis) | out-of-scope |
| `bop-s08` | unnumbered thematic section 8 (planner ordinal) | Intellectual institutions | [`c-tacit-knowledge`](concepts.md#c-tacit-knowledge) (out-of-scope), [`c-agency`](concepts.md#c-agency) (out-of-scope) | out-of-scope |
| `bop-s09` | unnumbered thematic section 9 (planner ordinal) | General and particular claims | [`c-induction`](concepts.md#c-induction) (out-of-scope), [`c-procrustean`](concepts.md#c-procrustean) (out-of-scope) | out-of-scope |
| `bop-s10` | unnumbered thematic section 10 (planner ordinal) | Judging randomness | [`c-luck-skill`](concepts.md#c-luck-skill) (out-of-scope), [`c-biases`](concepts.md#c-biases) (out-of-scope) | out-of-scope |
| `bop-s11` | unnumbered thematic section 11 (planner ordinal) | Taste and form | [`c-aesthetics`](concepts.md#c-aesthetics) (out-of-scope) | out-of-scope |
| `bop-s12` | unnumbered thematic section 12 (planner ordinal) | Responsibility | [`c-ethics`](concepts.md#c-ethics) (out-of-scope) | out-of-scope |
| `bop-s13` | unnumbered thematic section 13 (planner ordinal) | Response to shocks | [`c-fragility`](concepts.md#c-fragility) | out-of-scope |
| `bop-s14` | unnumbered thematic section 14 (planner ordinal) | Transfer between domains | [`c-ludic`](concepts.md#c-ludic) (out-of-scope) | out-of-scope |
| `bop-s15` | unnumbered thematic section 15 (planner ordinal) | Knowing by exclusion | [`c-skepticism`](concepts.md#c-skepticism) (out-of-scope), [`c-iatrogenics`](concepts.md#c-iatrogenics) (out-of-scope) | out-of-scope |
| `bop-s16` | unnumbered thematic section 16 (planner ordinal) | Predictive pretensions | [`c-forecasting`](concepts.md#c-forecasting) (out-of-scope) | out-of-scope |
| `bop-s17` | unnumbered thematic section 17 (planner ordinal) | Philosophical practice | [`c-stoicism`](concepts.md#c-stoicism) (out-of-scope), [`c-tacit-knowledge`](concepts.md#c-tacit-knowledge) (out-of-scope) | out-of-scope |
| `bop-s18` | unnumbered thematic section 18 (planner ordinal) | Economic incentives | [`c-agency`](concepts.md#c-agency) (out-of-scope) | out-of-scope |
| `bop-s19` | unnumbered thematic section 19 (planner ordinal) | Power and restraint | [`c-ethics`](concepts.md#c-ethics) (out-of-scope), [`c-stoicism`](concepts.md#c-stoicism) (out-of-scope) | out-of-scope |
| `bop-s20` | unnumbered thematic section 20 (planner ordinal) | Unspoken knowledge | [`c-tacit-knowledge`](concepts.md#c-tacit-knowledge) (out-of-scope) | out-of-scope |
| `bop-s21` | unnumbered thematic section 21 (planner ordinal) | Attachment and judgment | [`c-procrustean`](concepts.md#c-procrustean) (out-of-scope), [`c-ethics`](concepts.md#c-ethics) (out-of-scope) | out-of-scope |
| `bop-s22` | unnumbered thematic section 22 (planner ordinal) | Closing observations | [`c-skepticism`](concepts.md#c-skepticism) (out-of-scope) | out-of-scope |
| `bop-opening` | opening myth and notice | The costs of forced fit | [`c-procrustean`](concepts.md#c-procrustean) (out-of-scope) | out-of-scope |
| `bop-postface` | postface | Reading compressed arguments | [`c-procrustean`](concepts.md#c-procrustean) (out-of-scope), [`c-ludic`](concepts.md#c-ludic) (out-of-scope) | out-of-scope |

### Antifragile

Book ID: `af`. Status: **out-of-scope**. Baseline: 2014 paperback, ISBN 9780812979688; first published 2012.

Retained historical locator map only. No chapter review, prose coverage or edition reconciliation is scheduled.

| Unit ID | Source locator | Editorial topic | Concepts | Status |
| --- | --- | --- | --- | --- |
| `af-ch01` | ch. 1 | Response to variability | [`c-fragility`](concepts.md#c-fragility) | out-of-scope |
| `af-ch02` | ch. 2 | Adaptation to stress | [`c-hormesis`](concepts.md#c-hormesis) | out-of-scope |
| `af-ch03` | ch. 3 | Living and engineered systems | [`c-hormesis`](concepts.md#c-hormesis), [`c-decentralization`](concepts.md#c-decentralization) | out-of-scope |
| `af-ch04` | ch. 4 | Selection at different levels | [`c-selection-levels`](concepts.md#c-selection-levels) (out-of-scope) | out-of-scope |
| `af-ch05` | ch. 5 | Central control and variation | [`c-decentralization`](concepts.md#c-decentralization) | out-of-scope |
| `af-ch06` | ch. 6 | Suppressed volatility | [`c-fragility`](concepts.md#c-fragility), [`c-ruin`](concepts.md#c-ruin) | out-of-scope |
| `af-ch07` | ch. 7 | Intervention costs | [`c-iatrogenics`](concepts.md#c-iatrogenics) (out-of-scope) | out-of-scope |
| `af-ch08` | ch. 8 | Forecast dependence | [`c-forecasting`](concepts.md#c-forecasting) (out-of-scope), [`c-fragility`](concepts.md#c-fragility) | out-of-scope |
| `af-ch09` | ch. 9 | Exposure and judgment | [`c-agency`](concepts.md#c-agency) (out-of-scope), [`c-tacit-knowledge`](concepts.md#c-tacit-knowledge) (out-of-scope) | out-of-scope |
| `af-ch10` | ch. 10 | Controlling downside | [`c-barbell`](concepts.md#c-barbell) (out-of-scope), [`c-stoicism`](concepts.md#c-stoicism) (out-of-scope) | out-of-scope |
| `af-ch11` | ch. 11 | Separated risk allocations | [`c-barbell`](concepts.md#c-barbell) (out-of-scope) | out-of-scope |
| `af-ch12` | ch. 12 | Options and experimentation | [`c-optionality`](concepts.md#c-optionality) (out-of-scope) | out-of-scope |
| `af-ch13` | ch. 13 | Practice before explanation | [`c-tacit-knowledge`](concepts.md#c-tacit-knowledge) (out-of-scope) | out-of-scope |
| `af-ch14` | ch. 14 | Causal accounts of discovery | [`c-causal-narrative`](concepts.md#c-causal-narrative) (out-of-scope), [`c-tacit-knowledge`](concepts.md#c-tacit-knowledge) (out-of-scope) | out-of-scope |
| `af-ch15` | ch. 15 | Evidence from technological history | [`c-survivorship`](concepts.md#c-survivorship) (out-of-scope), [`c-tacit-knowledge`](concepts.md#c-tacit-knowledge) (out-of-scope) | out-of-scope |
| `af-ch16` | ch. 16 | Learning through trials | [`c-optionality`](concepts.md#c-optionality) (out-of-scope) | out-of-scope |
| `af-ch17` | ch. 17 | Limits of explicit rules | [`c-tacit-knowledge`](concepts.md#c-tacit-knowledge) (out-of-scope), [`c-ludic`](concepts.md#c-ludic) (out-of-scope) | out-of-scope |
| `af-ch18` | ch. 18 | Size and nonlinear response | [`c-jensen`](concepts.md#c-jensen), [`c-fragility`](concepts.md#c-fragility) | out-of-scope |
| `af-ch19` | ch. 19 | Curvature and estimation error | [`c-jensen`](concepts.md#c-jensen), [`c-fragility`](concepts.md#c-fragility) | out-of-scope |
| `af-ch20` | ch. 20 | Time and survival selection | [`c-lindy`](concepts.md#c-lindy) (out-of-scope) | out-of-scope |
| `af-ch21` | ch. 21 | Uneven medical response | [`c-hormesis`](concepts.md#c-hormesis), [`c-iatrogenics`](concepts.md#c-iatrogenics) (out-of-scope) | out-of-scope |
| `af-ch22` | ch. 22 | Subtractive choices | [`c-iatrogenics`](concepts.md#c-iatrogenics) (out-of-scope) | out-of-scope |
| `af-ch23` | ch. 23 | Incentives and transferred losses | [`c-agency`](concepts.md#c-agency) (out-of-scope), [`c-ethics`](concepts.md#c-ethics) (out-of-scope) | out-of-scope |
| `af-ch24` | ch. 24 | Professional responsibility | [`c-ethics`](concepts.md#c-ethics) (out-of-scope) | out-of-scope |
| `af-ch25` | ch. 25 | Closing argument | [`c-fragility`](concepts.md#c-fragility), [`c-ruin`](concepts.md#c-ruin) | out-of-scope |
| `af-prologue` | prologue | The response spectrum | [`c-fragility`](concepts.md#c-fragility) | out-of-scope |
| `af-app1` | appendix I | Concept relationships | [`c-fragility`](concepts.md#c-fragility), [`c-optionality`](concepts.md#c-optionality) (out-of-scope) | out-of-scope |
| `af-app2` | appendix II | Mathematical supplement | [`c-jensen`](concepts.md#c-jensen), [`c-fragility`](concepts.md#c-fragility) | out-of-scope |
| `af-glossary` | glossary | Terminology alignment | [`c-fragility`](concepts.md#c-fragility), [`c-tail-catalog`](concepts.md#c-tail-catalog) * | out-of-scope |

### Skin in the Game

Book ID: `sitg`. Status: **out-of-scope**. Baseline: 2018 ebook, ISBN 9780425284636.

Retained historical locator map only. No chapter review, prose coverage or edition reconciliation is scheduled.

| Unit ID | Source locator | Editorial topic | Concepts | Status |
| --- | --- | --- | --- | --- |
| `sitg-ch01` | ch. 1 | Information and transaction symmetry | [`c-agency`](concepts.md#c-agency) (out-of-scope), [`c-ethics`](concepts.md#c-ethics) (out-of-scope) | out-of-scope |
| `sitg-ch02` | ch. 2 | Collective preference thresholds | [`c-minority-rule`](concepts.md#c-minority-rule) (out-of-scope) | out-of-scope |
| `sitg-ch03` | ch. 3 | Employment and dependence | [`c-agency`](concepts.md#c-agency) (out-of-scope) | out-of-scope |
| `sitg-ch04` | ch. 4 | Delegating consequences | [`c-agency`](concepts.md#c-agency) (out-of-scope) | out-of-scope |
| `sitg-ch05` | ch. 5 | Commitment and simulation | [`c-costly-signals`](concepts.md#c-costly-signals) (out-of-scope), [`c-ethics`](concepts.md#c-ethics) (out-of-scope) | out-of-scope |
| `sitg-ch06` | ch. 6 | Credentials and decision authority | [`c-tacit-knowledge`](concepts.md#c-tacit-knowledge) (out-of-scope), [`c-agency`](concepts.md#c-agency) (out-of-scope) | out-of-scope |
| `sitg-ch07` | ch. 7 | Inequality over time | [`c-inequality-mobility`](concepts.md#c-inequality-mobility) (out-of-scope), [`c-gini`](concepts.md#c-gini) | out-of-scope |
| `sitg-ch08` | ch. 8 | Age and survival | [`c-lindy`](concepts.md#c-lindy) (out-of-scope) | out-of-scope |
| `sitg-ch09` | ch. 9 | Competence and appearance | [`c-costly-signals`](concepts.md#c-costly-signals) (out-of-scope), [`c-tacit-knowledge`](concepts.md#c-tacit-knowledge) (out-of-scope) | out-of-scope |
| `sitg-ch10` | ch. 10 | Imposed preferences | [`c-procrustean`](concepts.md#c-procrustean) (out-of-scope), [`c-agency`](concepts.md#c-agency) (out-of-scope) | out-of-scope |
| `sitg-ch11` | ch. 11 | Action as evidence | [`c-costly-signals`](concepts.md#c-costly-signals) (out-of-scope) | out-of-scope |
| `sitg-ch12` | ch. 12 | Selection in public narratives | [`c-causal-narrative`](concepts.md#c-causal-narrative) (out-of-scope), [`c-survivorship`](concepts.md#c-survivorship) (out-of-scope) | out-of-scope |
| `sitg-ch13` | ch. 13 | Visible virtue and incentives | [`c-costly-signals`](concepts.md#c-costly-signals) (out-of-scope), [`c-ethics`](concepts.md#c-ethics) (out-of-scope) | out-of-scope |
| `sitg-ch14` | ch. 14 | Scale and institutions | [`c-decentralization`](concepts.md#c-decentralization), [`c-minority-rule`](concepts.md#c-minority-rule) (out-of-scope) | out-of-scope |
| `sitg-ch15` | ch. 15 | Belief categories | [`c-procrustean`](concepts.md#c-procrustean) (out-of-scope), [`c-ethics`](concepts.md#c-ethics) (out-of-scope) | out-of-scope |
| `sitg-ch16` | ch. 16 | Costly commitments | [`c-costly-signals`](concepts.md#c-costly-signals) (out-of-scope) | out-of-scope |
| `sitg-ch17` | ch. 17 | Stated and revealed belief | [`c-costly-signals`](concepts.md#c-costly-signals) (out-of-scope), [`c-rationality`](concepts.md#c-rationality) (out-of-scope) | out-of-scope |
| `sitg-ch18` | ch. 18 | Survival as a criterion | [`c-rationality`](concepts.md#c-rationality) (out-of-scope), [`c-ergodicity`](concepts.md#c-ergodicity) | out-of-scope |
| `sitg-ch19` | ch. 19 | Repeated exposure and ruin | [`c-ruin`](concepts.md#c-ruin), [`c-ergodicity`](concepts.md#c-ergodicity) | out-of-scope |
| `sitg-pro1` | prologue, part 1 | Risk sharing and reciprocity | [`c-agency`](concepts.md#c-agency) (out-of-scope), [`c-ethics`](concepts.md#c-ethics) (out-of-scope) | out-of-scope |
| `sitg-pro2` | prologue, part 2 | Risk sharing and reciprocity | [`c-ethics`](concepts.md#c-ethics) (out-of-scope), [`c-rationality`](concepts.md#c-rationality) (out-of-scope) | out-of-scope |
| `sitg-pro3` | prologue, part 3 | Risk sharing and reciprocity | [`c-agency`](concepts.md#c-agency) (out-of-scope), [`c-costly-signals`](concepts.md#c-costly-signals) (out-of-scope) | out-of-scope |
| `sitg-app-intro` | appendix following introduction | Asymmetric exposure | [`c-agency`](concepts.md#c-agency) (out-of-scope), [`c-asymmetric-payoffs`](concepts.md#c-asymmetric-payoffs) | out-of-scope |
| `sitg-app-book3` | appendix to book III | Collective dynamics | [`c-minority-rule`](concepts.md#c-minority-rule) (out-of-scope) | out-of-scope |
| `sitg-epilogue` | epilogue | Conduct and consequences | [`c-ethics`](concepts.md#c-ethics) (out-of-scope), [`c-stoicism`](concepts.md#c-stoicism) (out-of-scope) | out-of-scope |

All retained units have a mapping, but completion concerns only the two technical books and selected mathematical paper claims. Closing a unit requires review of its mathematical scope and required concepts; it does not require excluded contextual associations. The required 2025 additions cannot disappear behind the current mapped counts.
