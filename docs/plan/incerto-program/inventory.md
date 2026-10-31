# Book and chapter inventory

Chapter 11 is implemented at the scope in the
[chapter-11 checkpoint](../../records/incerto-scft-v4-ch11.md). Separate max
review and site/live verification remain; chapter 12 is next. Earlier empirical
and source-locator limitations remain recorded in their own checkpoints.

`state.yaml` owns the records. Technical rows reproduce **titles and locators
only**, with original editorial concept associations. Those associations do
not certify a mathematical claim. An asterisk marks an existing concept body.

Active scope: **two books, 53 numbered chapters, 70 book source units,
16 papers and 75 concepts**. SCoFT v4 contributes 30 chapters and nine appendices;
Dynamic Hedging contributes 23 chapters, seven modules and introductory
material. The register retains **103 concept IDs: 75 active and 28 excluded**.
Five excluded books retain 77 chapters and 123 units. Totals: seven books,
130 chapters and 193 book units. All active concepts follow teaching → Python
→ optional Lean; excluded associations schedule no deliverables.

## Statistical Consequences of Fat Tails / Technical Incerto, volume 1

Book ID: `scft`. Baseline: **2025 third edition, arXiv:2001.10488v4**.
Chapter and appendix titles/printed starting pages were checked against both
the supplied TOC extract and direct PDF extraction (PDF pages 7–14).
Typesetting markers are omitted and capitalization normalized. Active unit
IDs include `v4`; legacy IDs are confined to the correspondence table below.

| Unit ID | V4 locator / printed page | Title | Concepts | Chapter chunk |
| --- | --- | --- | --- | --- |
| <a id="scft-v4-ch01"></a>`scft-v4-ch01` | ch. 1, p. 3 | Prologue | [`c-tail-catalog`](concepts.md#c-tail-catalog) *, [`c-induction`](concepts.md#c-induction) (out-of-scope) | `scft-v4-ch01` |
| <a id="scft-v4-ch02"></a>`scft-v4-ch02` | ch. 2, p. 7 | Glossary, definitions, and notations | [`c-exceedances`](concepts.md#c-exceedances) *, [`c-pareto`](concepts.md#c-pareto) *, [`c-evi`](concepts.md#c-evi) *, [`c-tail-catalog`](concepts.md#c-tail-catalog) * | `scft-v4-ch02` |
| <a id="scft-v4-ch03"></a>`scft-v4-ch03` | ch. 3, p. 25 | A non-technical overview - the Darwin College lecture | [`c-inference-asymmetry`](concepts.md#c-inference-asymmetry), [`c-asymmetric-payoffs`](concepts.md#c-asymmetric-payoffs), [`c-ruin`](concepts.md#c-ruin) | `scft-v4-ch03` |
| <a id="scft-v4-ch04"></a>`scft-v4-ch04` | ch. 4, p. 69 | Univariate fat tails, level 1, finite moments | [`c-mixture-uncertainty`](concepts.md#c-mixture-uncertainty), [`c-body-shoulder`](concepts.md#c-body-shoulder) *, [`c-moment-estimation`](concepts.md#c-moment-estimation) | `scft-v4-ch04` |
| <a id="scft-v4-ch05"></a>`scft-v4-ch05` | ch. 5, p. 91 | Level 2: subexponentials and power laws | [`c-pareto`](concepts.md#c-pareto) *, [`c-regular-variation`](concepts.md#c-regular-variation) *, [`c-subexponential`](concepts.md#c-subexponential) *, [`c-double-pareto`](concepts.md#c-double-pareto) *, [`c-tail-ratio`](concepts.md#c-tail-ratio) *, [`c-karamata`](concepts.md#c-karamata) *, [`c-pareto-moments`](concepts.md#c-pareto-moments) * | `scft-v4-ch05` |
| <a id="scft-v4-ch06"></a>`scft-v4-ch06` | ch. 6, p. 107 | Thick tails in higher dimensions | [`c-tail-geometry`](concepts.md#c-tail-geometry) *, [`c-multivariate-tails`](concepts.md#c-multivariate-tails) | `scft-v4-ch06` |
| <a id="scft-v4-ch07"></a>`scft-v4-ch07` | ch. 7, p. 137 | Limit distributions, a consolidation | [`c-lln-failure`](concepts.md#c-lln-failure) *, [`c-stable-clt`](concepts.md#c-stable-clt) *, [`c-max-sum`](concepts.md#c-max-sum) *, [`c-cauchy-running`](concepts.md#c-cauchy-running) | `scft-v4-ch07` |
| <a id="scft-v4-ch08"></a>`scft-v4-ch08` | ch. 8, p. 153 | How much data do you need? | [`c-kappa`](concepts.md#c-kappa) * | `scft-v4-ch08` |
| <a id="scft-v4-ch09"></a>`scft-v4-ch09` | ch. 9, p. 171 | Extreme values and hidden tails | [`c-gev`](concepts.md#c-gev) *, [`c-frechet`](concepts.md#c-frechet) *, [`c-pbdh`](concepts.md#c-pbdh) *, [`c-gpd`](concepts.md#c-gpd) *, [`c-evi`](concepts.md#c-evi) *, [`c-hill`](concepts.md#c-hill) *, [`c-mean-excess`](concepts.md#c-mean-excess) *, [`c-threshold`](concepts.md#c-threshold) * | `scft-v4-ch09` |
| <a id="scft-v4-ch10"></a>`scft-v4-ch10` | ch. 10, p. 193 | "it is what it is": diagnosing the SP500 | [`c-sp500`](concepts.md#c-sp500) | `scft-v4-ch10` |
| <a id="scft-v4-ch11"></a>`scft-v4-ch11` | ch. 11, p. 219 | Probability calibration under fat tails | [`c-calibration-payoff`](concepts.md#c-calibration-payoff), [`c-point-forecast`](concepts.md#c-point-forecast) | `scft-v4-ch11` |
| <a id="scft-v4-ch12"></a>`scft-v4-ch12` | ch. 12, p. 241 | On single point forecasts for fat-tailed variables | [`c-point-forecast`](concepts.md#c-point-forecast) | `scft-v4-ch12` |
| <a id="scft-v4-ch13"></a>`scft-v4-ch13` | ch. 13, p. 253 | The probability conflation | [`c-probability-conflation`](concepts.md#c-probability-conflation), [`c-calibration-payoff`](concepts.md#c-calibration-payoff), [`c-risk-measures`](concepts.md#c-risk-measures) | `scft-v4-ch13` |
| <a id="scft-v4-ch14"></a>`scft-v4-ch14` | ch. 14, p. 261 | Election predictions as martingales: an arbitrage approach | [`c-forecast-martingale`](concepts.md#c-forecast-martingale) | `scft-v4-ch14` |
| <a id="scft-v4-ch15"></a>`scft-v4-ch15` | ch. 15, p. 277 | Gini estimation under infinite variance | [`c-gini`](concepts.md#c-gini) | `scft-v4-ch15` |
| <a id="scft-v4-ch16"></a>`scft-v4-ch16` | ch. 16, p. 297 | Biases of quantile contribution | [`c-quantile-share`](concepts.md#c-quantile-share) | `scft-v4-ch16` |
| <a id="scft-v4-ch17"></a>`scft-v4-ch17` | ch. 17, p. 313 | Shadow moments of apparently infinite-mean phenomena | [`c-shadow-mean`](concepts.md#c-shadow-mean) | `scft-v4-ch17` |
| <a id="scft-v4-ch18"></a>`scft-v4-ch18` | ch. 18, p. 323 | On the tail risk of violent conflict (with P. Cirillo) | [`c-conflict-study`](concepts.md#c-conflict-study) | `scft-v4-ch18` |
| <a id="scft-v4-ch19"></a>`scft-v4-ch19` | ch. 19, p. 347 | Tail risk of contagious diseases | [`c-disease-study`](concepts.md#c-disease-study), [`c-shadow-mean`](concepts.md#c-shadow-mean) | `scft-v4-ch19` |
| <a id="scft-v4-ch20"></a>`scft-v4-ch20` | ch. 20, p. 367 | How thick tails emerge from recursive epistemic uncertainty | [`c-mixture-uncertainty`](concepts.md#c-mixture-uncertainty) | `scft-v4-ch20` |
| <a id="scft-v4-ch21"></a>`scft-v4-ch21` | ch. 21, p. 379 | Stochastic tail exponent for asymmetric power laws | [`c-random-alpha`](concepts.md#c-random-alpha) | `scft-v4-ch21` |
| <a id="scft-v4-ch22"></a>`scft-v4-ch22` | ch. 22, p. 389 | Meta-distribution of p-values and p-hacking | [`c-pvalues`](concepts.md#c-pvalues), [`c-multiple-testing`](concepts.md#c-multiple-testing) | `scft-v4-ch22` |
| <a id="scft-v4-ch23"></a>`scft-v4-ch23` | ch. 23, p. 405 | Lindy as distance from an absorbing barrier | [`c-lindy`](concepts.md#c-lindy) | `scft-v4-ch23` |
| <a id="scft-v4-ch24"></a>`scft-v4-ch24` | ch. 24, p. 417 | Financial theory’s failures with option pricing | [`c-model-risk`](concepts.md#c-model-risk), [`c-stochastic-pricing`](concepts.md#c-stochastic-pricing) | `scft-v4-ch24` |
| <a id="scft-v4-ch25"></a>`scft-v4-ch25` | ch. 25, p. 421 | Option pricing w/o dynamic hedging | [`c-pricing-measures`](concepts.md#c-pricing-measures) | `scft-v4-ch25` |
| <a id="scft-v4-ch26"></a>`scft-v4-ch26` | ch. 26, p. 429 | Option traders never use the Black-Scholes formula | [`c-tacit-knowledge`](concepts.md#c-tacit-knowledge) (out-of-scope), [`c-model-risk`](concepts.md#c-model-risk), [`c-hedging-error`](concepts.md#c-hedging-error) | `scft-v4-ch26` |
| <a id="scft-v4-ch27"></a>`scft-v4-ch27` | ch. 27, p. 445 | Option pricing under power laws: a robust heuristic | [`c-power-option`](concepts.md#c-power-option) | `scft-v4-ch27` |
| <a id="scft-v4-ch28"></a>`scft-v4-ch28` | ch. 28, p. 453 | Four mistakes in quantitative finance | [`c-moment-estimation`](concepts.md#c-moment-estimation), [`c-jensen`](concepts.md#c-jensen), [`c-numeraire`](concepts.md#c-numeraire), [`c-risk-measures`](concepts.md#c-risk-measures) | `scft-v4-ch28` |
| <a id="scft-v4-ch29"></a>`scft-v4-ch29` | ch. 29, p. 459 | Portfolios should never rely on correlation | [`c-portfolio-tail-dependence`](concepts.md#c-portfolio-tail-dependence), [`c-multivariate-tails`](concepts.md#c-multivariate-tails), [`c-correlation-constraints`](concepts.md#c-correlation-constraints), [`c-risk-measures`](concepts.md#c-risk-measures) | `scft-v4-ch29` |
| <a id="scft-v4-ch30"></a>`scft-v4-ch30` | ch. 30, p. 469 | Tail risk constraints and maximum entropy (w. D.& H. Geman) | [`c-maximum-entropy`](concepts.md#c-maximum-entropy) | `scft-v4-ch30` |
| <a id="scft-v4-appa"></a>`scft-v4-appa` | appendix A, p. 121 | Special cases of thick tails | [`c-tail-catalog`](concepts.md#c-tail-catalog) *, [`c-pareto`](concepts.md#c-pareto) * | `scft-v4-ch06` |
| <a id="scft-v4-appb"></a>`scft-v4-appb` | appendix B, p. 127 | Fat tails from maximum entropy | [`c-maximum-entropy`](concepts.md#c-maximum-entropy), [`c-tail-catalog`](concepts.md#c-tail-catalog) * | `scft-v4-ch05` |
| <a id="scft-v4-appc"></a>`scft-v4-appc` | appendix C, p. 183 | Growth rate & outcome: not in the same distribution class | [`c-ergodicity`](concepts.md#c-ergodicity), [`c-mixture-uncertainty`](concepts.md#c-mixture-uncertainty) | `scft-v4-ch07` |
| <a id="scft-v4-appd"></a>`scft-v4-appd` | appendix D, p. 187 | The large deviation principle, in brief | [`c-cramer`](concepts.md#c-cramer) * | `scft-v4-ch07` |
| <a id="scft-v4-appe"></a>`scft-v4-appe` | appendix E, p. 189 | Calibrating under Paretianity | [`c-plugin`](concepts.md#c-plugin) *, [`c-hill`](concepts.md#c-hill) *, [`c-threshold`](concepts.md#c-threshold) * | `scft-v4-ch09` |
| <a id="scft-v4-appf"></a>`scft-v4-appf` | appendix F, p. 207 | The problem with econometrics | [`c-ml-econometrics`](concepts.md#c-ml-econometrics) | `scft-v4-ch10` |
| <a id="scft-v4-appg"></a>`scft-v4-appg` | appendix G, p. 213 | Machine learning considerations | [`c-ml-econometrics`](concepts.md#c-ml-econometrics) | `scft-v4-ch10` |
| <a id="scft-v4-apph"></a>`scft-v4-apph` | appendix H, p. 343 | What are the chances of a third world war? | [`c-conflict-study`](concepts.md#c-conflict-study) | `scft-v4-ch18` |
| <a id="scft-v4-appi"></a>`scft-v4-appi` | appendix I, p. 399 | Some confusions in behavioral economics | [`c-biases`](concepts.md#c-biases) (out-of-scope), [`c-ml-econometrics`](concepts.md#c-ml-econometrics) | `scft-v4-ch22` |

## V2 to v4 correspondence

Verified directly from both PDF TOCs, not inferred from the third-edition
description. Numbering follows the expected insertions with **no numbering
deviation**: 1–11 unchanged; 12–16 +2; 17–19 +3; 20–24 +4; 25 +5.
Appendix A stays A; B–H become C–I. Section numbering, titles and pagination
must not be carried forward by a blanket offset. The table records every
old unit ID so existing references can be migrated without rebinding an ID.

| Previous unit ID / v2 locator | V2 title | V4 unit / locator | V4 title | Title changed |
| --- | --- | --- | --- | --- |
| `scft-ch01` / ch. 1 | Prologue | [`scft-v4-ch01`](#scft-v4-ch01) / ch. 1 | Prologue | no |
| `scft-ch02` / ch. 2 | Glossary, definitions, and notations | [`scft-v4-ch02`](#scft-v4-ch02) / ch. 2 | Glossary, definitions, and notations | no |
| `scft-ch03` / ch. 3 | A non-technical overview - the Darwin College lecture | [`scft-v4-ch03`](#scft-v4-ch03) / ch. 3 | A non-technical overview - the Darwin College lecture | no |
| `scft-ch04` / ch. 4 | Univariate fat tails, level 1, finite moments | [`scft-v4-ch04`](#scft-v4-ch04) / ch. 4 | Univariate fat tails, level 1, finite moments | no |
| `scft-ch05` / ch. 5 | Level 2: subexponentials and power laws | [`scft-v4-ch05`](#scft-v4-ch05) / ch. 5 | Level 2: subexponentials and power laws | no |
| `scft-ch06` / ch. 6 | Thick tails in higher dimensions | [`scft-v4-ch06`](#scft-v4-ch06) / ch. 6 | Thick tails in higher dimensions | no |
| `scft-ch07` / ch. 7 | Limit distributions, a consolidation | [`scft-v4-ch07`](#scft-v4-ch07) / ch. 7 | Limit distributions, a consolidation | no |
| `scft-ch08` / ch. 8 | How much data do you need? an operational metric for fat-tailedness | [`scft-v4-ch08`](#scft-v4-ch08) / ch. 8 | How much data do you need? | yes |
| `scft-ch09` / ch. 9 | Extreme values and hidden tails | [`scft-v4-ch09`](#scft-v4-ch09) / ch. 9 | Extreme values and hidden tails | no |
| `scft-ch10` / ch. 10 | "it is what it is": diagnosing the SP500 | [`scft-v4-ch10`](#scft-v4-ch10) / ch. 10 | "it is what it is": diagnosing the SP500 | no |
| `scft-ch11` / ch. 11 | Probability calibration under fat tails | [`scft-v4-ch11`](#scft-v4-ch11) / ch. 11 | Probability calibration under fat tails | no |
| `scft-ch12` / ch. 12 | Election predictions as martingales: an arbitrage approach | [`scft-v4-ch14`](#scft-v4-ch14) / ch. 14 | Election predictions as martingales: an arbitrage approach | no |
| `scft-ch13` / ch. 13 | Gini estimation under infinite variance | [`scft-v4-ch15`](#scft-v4-ch15) / ch. 15 | Gini estimation under infinite variance | no |
| `scft-ch14` / ch. 14 | On the super-additivity and estimation biases of quantile contributions | [`scft-v4-ch16`](#scft-v4-ch16) / ch. 16 | Biases of quantile contribution | yes |
| `scft-ch15` / ch. 15 | Shadow moments of apparently infinite-mean phenomena | [`scft-v4-ch17`](#scft-v4-ch17) / ch. 17 | Shadow moments of apparently infinite-mean phenomena | no |
| `scft-ch16` / ch. 16 | On the tail risk of violent conflict (with P. Cirillo) | [`scft-v4-ch18`](#scft-v4-ch18) / ch. 18 | On the tail risk of violent conflict (with P. Cirillo) | no |
| `scft-ch17` / ch. 17 | How thick tails emerge from recursive epistemic uncertainty | [`scft-v4-ch20`](#scft-v4-ch20) / ch. 20 | How thick tails emerge from recursive epistemic uncertainty | no |
| `scft-ch18` / ch. 18 | Stochastic tail exponent for asymmetric power laws | [`scft-v4-ch21`](#scft-v4-ch21) / ch. 21 | Stochastic tail exponent for asymmetric power laws | no |
| `scft-ch19` / ch. 19 | Meta-distribution of p-values and p-hacking | [`scft-v4-ch22`](#scft-v4-ch22) / ch. 22 | Meta-distribution of p-values and p-hacking | no |
| `scft-ch20` / ch. 20 | Financial theory’s failures with option pricing | [`scft-v4-ch24`](#scft-v4-ch24) / ch. 24 | Financial theory’s failures with option pricing | no |
| `scft-ch21` / ch. 21 | Unique option pricing measure (no dynamic hedging/complete markets) | [`scft-v4-ch25`](#scft-v4-ch25) / ch. 25 | Option pricing w/o dynamic hedging | yes |
| `scft-ch22` / ch. 22 | Option traders never use the Black-Scholes-Merton formula | [`scft-v4-ch26`](#scft-v4-ch26) / ch. 26 | Option traders never use the Black-Scholes formula | yes |
| `scft-ch23` / ch. 23 | Option pricing under power laws: a robust heuristic | [`scft-v4-ch27`](#scft-v4-ch27) / ch. 27 | Option pricing under power laws: a robust heuristic | no |
| `scft-ch24` / ch. 24 | Four mistakes in quantitative finance | [`scft-v4-ch28`](#scft-v4-ch28) / ch. 28 | Four mistakes in quantitative finance | no |
| `scft-ch25` / ch. 25 | Tail risk constraints and maximum entropy (w. D.& H. Geman) | [`scft-v4-ch30`](#scft-v4-ch30) / ch. 30 | Tail risk constraints and maximum entropy (w. D.& H. Geman) | no |
| `scft-appa` / appendix A | Special cases of thick tails | [`scft-v4-appa`](#scft-v4-appa) / appendix A | Special cases of thick tails | no |
| `scft-appb` / appendix B | Growth rate and outcome are not in the same distribution class | [`scft-v4-appc`](#scft-v4-appc) / appendix C | Growth rate & outcome: not in the same distribution class | yes |
| `scft-appc` / appendix C | The large deviation principle, in brief | [`scft-v4-appd`](#scft-v4-appd) / appendix D | The large deviation principle, in brief | no |
| `scft-appd` / appendix D | Calibrating under Paretianity | [`scft-v4-appe`](#scft-v4-appe) / appendix E | Calibrating under Paretianity | no |
| `scft-appe` / appendix E | The problem with econometrics | [`scft-v4-appf`](#scft-v4-appf) / appendix F | The problem with econometrics | no |
| `scft-appf` / appendix F | Machine learning considerations | [`scft-v4-appg`](#scft-v4-appg) / appendix G | Machine learning considerations | no |
| `scft-appg` / appendix G | What are the chances of a third world war? | [`scft-v4-apph`](#scft-v4-apph) / appendix H | What are the chances of a third world war? | no |
| `scft-apph` / appendix H | Some confusions in behavioral economics | [`scft-v4-appi`](#scft-v4-appi) / appendix I | Some confusions in behavioral economics | no |

Added relative to v2: chapters **12, 13, 19, 23, 29** and appendix **B**.
The earlier plan's “three added chapters” metadata was not the complete
v2-to-v4 difference. Title changes occur at v2 chapters 8, 14, 21, 22 and
appendix B; their v4 destinations are 8, 16, 25, 26 and C. The chapter 29 /
journal-paper title difference is recorded under [sources](sources.md#papers).

## Supporting unit attachments

Every appendix/module has one host chunk. The choices below preserve numbered
chapter order while putting supporting material beside its use. Chapter
checkpoints must cover the attached units; no appendix is dropped from scope.

| Supporting unit | Host chapter | Reason |
| --- | --- | --- |
| SCoFT v4 A | 6 | Additional tail models alongside the higher-dimensional model comparison. |
| SCoFT v4 B | 5 | Maximum-entropy constructions support the introduction to tail classes; chapter 30 returns to constrained portfolio models. |
| SCoFT v4 C | 7 | Growth transformations help distinguish time aggregation from outcome distributions. |
| SCoFT v4 D | 7 | The exponential-moment gate distinguishes the limit and deviation regimes. |
| SCoFT v4 E | 9 | Calibration and threshold diagnostics accompany extreme-value models. |
| SCoFT v4 F, G | 10 | Estimator and pipeline checks accompany the equity-return example. |
| SCoFT v4 H | 18 | Review only the mathematical conflict-risk scope; no policy conclusions. |
| SCoFT v4 I | 22 | Mathematical testing and model-assumption checks; excluded behavioral claims stay outside scope. |
| DH introductory material | 1 | Establish instrument and model conventions. |
| DH module A | 7 | Brownian basics support the delta examples. |
| DH modules B, F | 5 | Pricing probabilities and finite-state arbitrage checks. |
| DH module D | 6 | Correlation feasibility accompanies volatility and correlation. |
| DH module E | 15 | Risk measures accompany distribution/model choices. |
| DH modules C, G | 16 | Numeraire and pricing basics support option trading examples. |

## Dynamic Hedging

Book ID: `dh`. Baseline: Wiley, 1997, ISBN 9780471152804. Execute chapters
1–23 after SCoFT chapter 30. Titles use the [catalog contents locator](https://www.yes24.com/product/goods/80530);
exact claim/page locators still require the selected copy. Stochastic calculus
is limited to basics needed for the hedging concepts.

| Unit ID | Source locator | Title | Concepts | Chapter chunk |
| --- | --- | --- | --- | --- |
| <a id="dh-ch01"></a>`dh-ch01` | ch. 1 | Introduction to the Instruments | [`c-payoff-algebra`](concepts.md#c-payoff-algebra) | `dh-ch01` |
| <a id="dh-ch02"></a>`dh-ch02` | ch. 2 | The Generalized Option | [`c-payoff-algebra`](concepts.md#c-payoff-algebra) | `dh-ch02` |
| <a id="dh-ch03"></a>`dh-ch03` | ch. 3 | Market Making and Market Using | [`c-market-making`](concepts.md#c-market-making) | `dh-ch03` |
| <a id="dh-ch04"></a>`dh-ch04` | ch. 4 | Liquidity and Liquidity Holes | [`c-liquidity`](concepts.md#c-liquidity) | `dh-ch04` |
| <a id="dh-ch05"></a>`dh-ch05` | ch. 5 | Arbitrage and the Arbitrageurs | [`c-arbitrage`](concepts.md#c-arbitrage) | `dh-ch05` |
| <a id="dh-ch06"></a>`dh-ch06` | ch. 6 | Volatility and Correlation | [`c-volatility-surface`](concepts.md#c-volatility-surface), [`c-correlation-constraints`](concepts.md#c-correlation-constraints) | `dh-ch06` |
| <a id="dh-ch07"></a>`dh-ch07` | ch. 7 | Adapting Black-Scholes-Merton: The Delta | [`c-greeks`](concepts.md#c-greeks) | `dh-ch07` |
| <a id="dh-ch08"></a>`dh-ch08` | ch. 8 | Gamma and Shadow Gamma | [`c-greeks`](concepts.md#c-greeks) | `dh-ch08` |
| <a id="dh-ch09"></a>`dh-ch09` | ch. 9 | Vega and the Volatility Surface | [`c-greeks`](concepts.md#c-greeks), [`c-volatility-surface`](concepts.md#c-volatility-surface) | `dh-ch09` |
| <a id="dh-ch10"></a>`dh-ch10` | ch. 10 | Theta and Minor Greeks | [`c-greeks`](concepts.md#c-greeks) | `dh-ch10` |
| <a id="dh-ch11"></a>`dh-ch11` | ch. 11 | The Greeks and Their Behavior | [`c-hedging-error`](concepts.md#c-hedging-error), [`c-greeks`](concepts.md#c-greeks) | `dh-ch11` |
| <a id="dh-ch12"></a>`dh-ch12` | ch. 12 | Fungibility, Convergence, and Stacking | [`c-basis-buckets`](concepts.md#c-basis-buckets) | `dh-ch12` |
| <a id="dh-ch13"></a>`dh-ch13` | ch. 13 | Some Wrinkles of Option Markets | [`c-liquidity`](concepts.md#c-liquidity), [`c-market-making`](concepts.md#c-market-making) | `dh-ch13` |
| <a id="dh-ch14"></a>`dh-ch14` | ch. 14 | Bucketing and Topography | [`c-basis-buckets`](concepts.md#c-basis-buckets) | `dh-ch14` |
| <a id="dh-ch15"></a>`dh-ch15` | ch. 15 | Beware the Distribution | [`c-model-risk`](concepts.md#c-model-risk) | `dh-ch15` |
| <a id="dh-ch16"></a>`dh-ch16` | ch. 16 | Option Trading Concepts | [`c-model-risk`](concepts.md#c-model-risk), [`c-hedging-error`](concepts.md#c-hedging-error) | `dh-ch16` |
| <a id="dh-ch17"></a>`dh-ch17` | ch. 17 | Binary Options: European Style | [`c-digitals`](concepts.md#c-digitals) | `dh-ch17` |
| <a id="dh-ch18"></a>`dh-ch18` | ch. 18 | Binary Options: American Style | [`c-digitals`](concepts.md#c-digitals) | `dh-ch18` |
| <a id="dh-ch19"></a>`dh-ch19` | ch. 19 | Barrier Options (I) | [`c-barriers`](concepts.md#c-barriers) | `dh-ch19` |
| <a id="dh-ch20"></a>`dh-ch20` | ch. 20 | Barrier Options (II) | [`c-barriers`](concepts.md#c-barriers), [`c-hedging-error`](concepts.md#c-hedging-error) | `dh-ch20` |
| <a id="dh-ch21"></a>`dh-ch21` | ch. 21 | Compound, Choosers, and Higher Order Options | [`c-compound-options`](concepts.md#c-compound-options) | `dh-ch21` |
| <a id="dh-ch22"></a>`dh-ch22` | ch. 22 | Multiasset Options | [`c-multiasset-options`](concepts.md#c-multiasset-options) | `dh-ch22` |
| <a id="dh-ch23"></a>`dh-ch23` | ch. 23 | Minor Exotics: Lookback and Asian Options | [`c-path-options`](concepts.md#c-path-options) | `dh-ch23` |
| <a id="dh-moda"></a>`dh-moda` | module A | Brownian Motion on a Spreadsheet, a Tutorial | [`c-brownian`](concepts.md#c-brownian) | `dh-ch07` |
| <a id="dh-modb"></a>`dh-modb` | module B | Risk Neutrality Explained | [`c-pricing-measures`](concepts.md#c-pricing-measures) | `dh-ch05` |
| <a id="dh-modc"></a>`dh-modc` | module C | Numeraire Relativity and the Two-Country Paradox | [`c-numeraire`](concepts.md#c-numeraire) | `dh-ch16` |
| <a id="dh-modd"></a>`dh-modd` | module D | Correlation Triangles: A Graphical Case Study | [`c-correlation-constraints`](concepts.md#c-correlation-constraints) | `dh-ch06` |
| <a id="dh-mode"></a>`dh-mode` | module E | The Value-at-Risk | [`c-risk-measures`](concepts.md#c-risk-measures) | `dh-ch15` |
| <a id="dh-modf"></a>`dh-modf` | module F | Probabilistic Rankings in Arbitrage | [`c-arbitrage`](concepts.md#c-arbitrage), [`c-payoff-algebra`](concepts.md#c-payoff-algebra) | `dh-ch05` |
| <a id="dh-modg"></a>`dh-modg` | module G | Option Pricing | [`c-stochastic-pricing`](concepts.md#c-stochastic-pricing), [`c-barriers`](concepts.md#c-barriers) | `dh-ch16` |
| <a id="dh-opening"></a>`dh-opening` | preface and introductory material | Introduction: Dynamic Hedging | [`c-model-risk`](concepts.md#c-model-risk) | `dh-ch01` |

## Selected technical papers

There are **16 records**: the previous 14 plus the probability-conflation reply
and the portfolio-correlation paper. Attach each to its host chapter; future
on-demand papers follow the same rule. A chapter version is a bibliographic
correspondence, not a claim that every theorem or equation is unchanged.
Exact claim locators and full-text comparison remain pending. Narrative,
clinical and policy coverage is excluded.

| Paper ID and source | Concepts | V4 chapter / relationship |
| --- | --- | --- |
| <a id="paper-fragility"></a>`paper-fragility` — [Mathematical Definition, Mapping, and Detection of (Anti)Fragility](https://arxiv.org/abs/1208.1189v1) | [`c-fragility`](concepts.md#c-fragility), [`c-jensen`](concepts.md#c-jensen) | [ch. 28](#scft-v4-ch28); supporting reading |
| <a id="paper-precaution"></a>`paper-precaution` — [The Precautionary Principle (with Application to the Genetic Modification of Organisms)](https://arxiv.org/abs/1410.5787v1) | [`c-ruin`](concepts.md#c-ruin), [`c-decentralization`](concepts.md#c-decentralization), [`c-ethics`](concepts.md#c-ethics) (out-of-scope) | [ch. 3](#scft-v4-ch03); supporting reading |
| <a id="paper-kappa"></a>`paper-kappa` — [How Much Data Do You Need? An Operational, Pre-Asymptotic Metric for Fat-tailedness](https://arxiv.org/abs/1802.05495v3) | [`c-kappa`](concepts.md#c-kappa), [`c-moment-estimation`](concepts.md#c-moment-estimation) | [ch. 8](#scft-v4-ch08); chapter version |
| <a id="paper-conflicts"></a>`paper-conflicts` — [On the statistical properties and tail risk of violent conflicts](https://arxiv.org/abs/1505.04722v2) | [`c-shadow-mean`](concepts.md#c-shadow-mean), [`c-conflict-study`](concepts.md#c-conflict-study) | [ch. 18](#scft-v4-ch18); chapter version |
| <a id="paper-diseases"></a>`paper-diseases` — [Tail Risk of Contagious Diseases](https://arxiv.org/abs/2004.08658v1) | [`c-shadow-mean`](concepts.md#c-shadow-mean), [`c-disease-study`](concepts.md#c-disease-study) | [ch. 19](#scft-v4-ch19); chapter version |
| <a id="paper-diseases-comment"></a>`paper-diseases-comment` — [Scientific comment on Tail risk of contagious diseases](https://arxiv.org/abs/2007.06876v1) | [`c-disease-study`](concepts.md#c-disease-study) | [ch. 19](#scft-v4-ch19); supporting reading |
| <a id="paper-gini"></a>`paper-gini` — [Gini estimation under infinite variance](https://arxiv.org/abs/1707.01370v4) | [`c-gini`](concepts.md#c-gini) | [ch. 15](#scft-v4-ch15); chapter version |
| <a id="paper-quantile"></a>`paper-quantile` — [On the Super-Additivity and Estimation Biases of Quantile Contributions](https://arxiv.org/abs/1405.1791v3) | [`c-quantile-share`](concepts.md#c-quantile-share) | [ch. 16](#scft-v4-ch16); chapter version |
| <a id="paper-alpha"></a>`paper-alpha` — [Stochastic Tail Exponent For Asymmetric Power Laws](https://arxiv.org/abs/1609.02369v3) | [`c-random-alpha`](concepts.md#c-random-alpha) | [ch. 21](#scft-v4-ch21); chapter version |
| <a id="paper-option-tail"></a>`paper-option-tail` — [Tail Option Pricing Under Power Laws](https://arxiv.org/abs/1908.02347v3) | [`c-power-option`](concepts.md#c-power-option) | [ch. 27](#scft-v4-ch27); chapter version |
| <a id="paper-pricing"></a>`paper-pricing` — [Risk Neutral Option Pricing With Neither Dynamic Hedging nor Complete Markets](https://arxiv.org/abs/1405.2609v2) | [`c-pricing-measures`](concepts.md#c-pricing-measures) | [ch. 25](#scft-v4-ch25); chapter version |
| <a id="paper-entropy"></a>`paper-entropy` — [Tail Risk Constraints and Maximum Entropy](https://arxiv.org/abs/1412.7647v1) | [`c-maximum-entropy`](concepts.md#c-maximum-entropy) | [ch. 30](#scft-v4-ch30); chapter version |
| <a id="paper-convex-response"></a>`paper-convex-response` — [Working With Convex Responses: Antifragility From Finance to Oncology](https://arxiv.org/abs/2209.14631v2) | [`c-jensen`](concepts.md#c-jensen), [`c-hormesis`](concepts.md#c-hormesis) | [ch. 28](#scft-v4-ch28); supporting reading |
| <a id="paper-point-forecast"></a>`paper-point-forecast` — [On Single Point Forecasts for Fat-Tailed Variables](https://arxiv.org/abs/2007.16096v1) | [`c-point-forecast`](concepts.md#c-point-forecast) | [ch. 12](#scft-v4-ch12); chapter version |
| <a id="paper-probability-conflation"></a>`paper-probability-conflation` — [The Probability Conflation: A Reply](https://arxiv.org/abs/2301.10985v1) | [`c-probability-conflation`](concepts.md#c-probability-conflation) | [ch. 13](#scft-v4-ch13); chapter version |
| <a id="paper-portfolio-correlation"></a>`paper-portfolio-correlation` — [Pension Funds Should Never Rely on Correlation](https://doi.org/10.3905/jai.2022.1.157) | [`c-portfolio-tail-dependence`](concepts.md#c-portfolio-tail-dependence) | [ch. 29](#scft-v4-ch29); chapter version |

Chapter 12 corresponds to the IJF 2022 single-point-forecast paper; chapter 13
to the IJF 2023 reply to Tetlock et al. Chapter 29 is titled *Portfolios should
never rely on correlation*, whereas its JAI 2022 paper is *Pension Funds Should
Never Rely on Correlation*. See [bibliographic evidence](sources.md#papers).

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
| `af-ch20` | ch. 20 | Time and survival selection | [`c-lindy`](concepts.md#c-lindy) | out-of-scope |
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
| `sitg-ch08` | ch. 8 | Age and survival | [`c-lindy`](concepts.md#c-lindy) | out-of-scope |
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

All retained units have a mapping, but completion concerns only the two technical books and selected mathematical paper claims. Closing a unit requires review of its mathematical scope and required concepts; it does not require excluded contextual associations. All six v4 additions are included above; exact mathematical scope closes within the chapter checkpoints.
