---
title: Pickands-Balkema-de Haan Theorem
options:
  concept:
    id: pickands-balkema-de-haan
    type: theorem
    depends_on:
      - regular-variation
      - extreme-value-index
      - generalized-pareto
      - generalized-extreme-value
    tags:
      - extreme-value-theory
      - peaks-over-threshold
---

## Statement

Let $F$ be a distribution function with finite or infinite right endpoint
$x_F=\sup\{x:F(x)<1\}$.  For a high threshold $u<x_F$, define the conditional
excess distribution

$$
\begin{gathered}
F_u(y)=P(X-u\le y\mid X>u)\\
=\frac{F(u+y)-F(u)}{1-F(u)},\\
0\le y<x_F-u.
\end{gathered}
$$

If $F$ is in the maximum domain of attraction of an extreme-value law with
extreme-value index $\xi$, then there is a positive scale function $\beta(u)$
such that

$$
\begin{gathered}
\sup_{0\le y<x_F-u}
\left|F_u(y)-G_{\xi,\beta(u)}(y)\right|\to0,\\
u\uparrow x_F.
\end{gathered}
$$

The comparison is over the excess support, using the full GPD CDF: for
$\xi<0$, set $G_{\xi,\beta}(y)=1$ at and beyond $-\beta/\xi$.  The generalized Pareto term
has scale $\beta>0$ and is

$$
\begin{gathered}
G_{\xi,\beta}(y)
=1-\left(1+\frac{\xi y}{\beta}\right)^{-1/\xi},\\
\xi\ne0,
\end{gathered}
$$

on the support where $1+\xi y/\beta>0$, and

$$
G_{0,\beta}(y)=1-e^{-y/\beta}
$$

for $\xi=0$.  The theorem is the asymptotic justification for the
peaks-over-threshold model: sufficiently high threshold exceedances are modeled
by a [generalized Pareto distribution](./incerto-generalized-pareto.md).

$X$ denotes a draw from $F$, $u$ the threshold, $x_F$ its right endpoint,
$\xi$ the extreme-value index, and $\beta(u)>0$ the excess scale.
The maximum-domain-of-attraction assumption means that for iid draws,
some $a_n>0$ and $b_n$ give $(M_n-b_n)/a_n\Rightarrow H_{\xi,0,1}$.
Here $M_n$ is the sample maximum and $\Rightarrow$ is convergence in
distribution. The GEV page defines $H$. See [Shared notation](https://xshi19.github.io/math/notation/).

## Threshold intuition

Block-maxima theory says that properly normalized maxima have only a small
number of possible limiting shapes, collected in the
[Generalized Extreme-Value Distribution](./incerto-generalized-extreme-value.md).
The Pickands-Balkema-de Haan theorem says the matching threshold view has the
same discipline: once we condition on being far enough into the tail, the
remaining excess has an approximately
[Generalized Pareto Distribution](./incerto-generalized-pareto.md).

For fat-tail work, the case $\xi>0$ is the main bridge.  It corresponds to a
[regularly varying](./incerto-regular-variation.md) right tail with exponent
$\alpha=1/\xi$.  The theorem does not say every high observation is generated
by a clean [Pareto law](./incerto-pareto.md).  It says the excess
distribution over moving high thresholds has a universal limit shape under the
same domain-of-attraction assumptions used in extreme-value theory.

## Exact Pareto excess special case

The full Pickands-Balkema-de Haan theorem is cited here, not proved.  The
calculation below proves the exact Pareto special case: once the threshold is
above the lower cutoff, the excess distribution is already generalized Pareto,
not merely asymptotically close to it.

The full theorem is a classical result of Balkema and de Haan and,
independently, Pickands.  Its proof uses the equivalence between convergence of
normalized maxima and convergence of normalized threshold excesses.  We
record the statement and use exact Pareto algebra as a checkable special
case.

If $X$ is Pareto Type I with lower cutoff $x_m$ and tail exponent $\alpha$,
then for $u\ge x_m$,

$$
\begin{gathered}
P(X-u>y\mid X>u)\\
=\frac{P(X>u+y)}{P(X>u)}\\
=\left(1+\frac{y}{u}\right)^{-\alpha}.
\end{gathered}
$$

This is exactly a generalized Pareto survival function with

$$
\xi=\frac1\alpha,
\qquad
\beta(u)=\frac{u}{\alpha}.
$$

Thus exact Pareto tails do not merely approach the generalized Pareto form;
they have it at every threshold above $x_m$.

## Exact threshold calibration

(pbdh-threshold-excess-fit)=
For $\alpha=1.7=17/10$, the population excess parameters are
$\xi=10/17$ and $\beta(u)=10u/17$. The scaled excess
$Z=(X-u)/u$, conditional on $X>u$, has survival $(1+z)^{-1.7}$.

| Threshold $u\ge x_m$ | Shape $\xi$ | Scale $\beta(u)$ | $\mathbb P(Z>1\mid X>u)$ |
| --- | --- | --- | --- |
| $x_m$ | $10/17$ | $10x_m/17$ | $2^{-1.7}$ |
| $2x_m$ | $10/17$ | $20x_m/17$ | $2^{-1.7}$ |
| $4x_m$ | $10/17$ | $40x_m/17$ | $2^{-1.7}$ |

These are exact population identities, not fitted estimates. In finite data,
estimated shape and scale fluctuate, and real tails may approach the GPD
family slowly. [Threshold selection](./incerto-tail-threshold-selection.md)
examines that modeling choice; the theorem supplies no finite-sample cutoff.

(pbdh-chapter-nine)=
## What the limit permits

SCoFT v4 §9.1.3, pp. 176–177, introduces conditional excesses
[@taleb2025scoftv4]. In the theorem above, membership in a maximum domain
of attraction and an **absolute** CDF difference are essential. Approaching
the endpoint of an arbitrary CDF does not by itself establish a GPD limit.
The full theorem is cited from @balkema1974residual and
@pickands1975statistical; this page proves only special cases and consequences.

For a standard normal parent, excesses also have a limit, but on a shrinking
scale. For $u\to\infty$ and fixed $y\ge0$, the normal-tail bounds in the
[Gaussian maxima proof](incerto-generalized-extreme-value.md#gev-gaussian-maxima)
give

$$
\begin{gathered}
P(u(X-u)>y\mid X>u)\\
=\frac{\bar\Phi(u+y/u)}{\bar\Phi(u)}\longrightarrow e^{-y}.
\end{gathered}
$$

Thus $\xi=0$ with asymptotic excess scale $1/u$, whereas exact Pareto
has $\xi=1/\alpha$ and scale $u/\alpha$. A bounded example is uniform
on $[0,b]$: above $0\le u<b$ its excess is exactly uniform on $[0,b-u]$,
a GPD with $\xi=-1$ and $\beta(u)=b-u$.

These three cases can be compared with
[`generalized_pareto`](incerto-api-reference.md#api-generalized-pareto).
The normal row is a limit comparison; the other two are exact.

```python
from scipy.stats import norm
from xmath.incerto.distributions import generalized_pareto

for u in (2, 4, 8):
    probability = norm.sf(u+1/u)/norm.sf(u)
    print(f"normal u={u}: scaled excess survival={probability:.4g}")
for xi, scale in ((0, 1), (.5, .5), (-1, 1)):
    print(f"GPD xi={xi:g}: sf(1)={generalized_pareto(xi, beta=scale).sf(1):.4g}")
```

**Output**

```text
normal u=2: scaled excess survival=0.273
normal u=4: scaled excess survival=0.3375
normal u=8: scaled excess survival=0.3596
GPD xi=0: sf(1)=0.3679
GPD xi=0.5: sf(1)=0.25
GPD xi=-1: sf(1)=0
```

Uniform closeness of CDFs does not control unbounded moments: the
[contamination counterexample](incerto-hidden-tail.md#hidden-tail-empirical)
shows why. Computing a fitted mean from $\xi<1$ is a statement about that
GPD model. Transferring a moment limit to the true excess distribution
requires additional tail-integrability conditions. The theorem alone gives
no finite-sample threshold, rate, or mean-error bound.

## Caveats

- The theorem is asymptotic in the threshold.  It does not choose the threshold
  for a finite dataset.
- Dependence, seasonality, volatility clustering, rounding, truncation, and
  mixtures can all distort threshold exceedances.
- A generalized Pareto fit is a tail model, not a proof that the full
  distribution is Pareto.
- When $\xi\ge1$, the fitted generalized Pareto model has no finite mean.  When
  $\xi\ge1/2$, it has no finite variance.  These moment boundaries are often
  the practical reason the shape estimate matters.
- Raising the threshold can reduce tail-approximation bias but leaves fewer
  exceedances; it does not guarantee a monotone improvement in a fitted model.

## References

- Balkema and de Haan, "Residual Life Time at Great Age"
  @balkema1974residual.
- Pickands, "Statistical Inference Using Extreme Order Statistics"
  @pickands1975statistical.
- Embrechts, Klueppelberg, and Mikosch, *Modelling Extremal Events*
  @embrechts1997modelling.
- Coles, *An Introduction to Statistical Modeling of Extreme Values*
  @coles2001introduction.

## Backlinks

- Depends on: [Regular Variation](./incerto-regular-variation.md),
  [Extreme-Value Index](./incerto-extreme-value-index.md),
  [Generalized Pareto Distribution](./incerto-generalized-pareto.md),
  [Generalized Extreme-Value Distribution](./incerto-generalized-extreme-value.md),
  and [Shared notation](https://xshi19.github.io/math/notation/).
- Used by: [Mean Excess Function](./incerto-mean-excess-function.md) and
  [S&P 500 Tail Diagnostics](./incerto-sp500-tail.md).
