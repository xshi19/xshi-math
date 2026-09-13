# Information Geometry entry outline

Status: outline established; first batch implemented as original notes.
Updated: 2026-09-13.

## Purpose and scope

The course starts with familiar calculations in Euclidean geometry and
probability, develops the geometry of statistical models, and then prepares a
separate research sequence on observable marginals of latent-variable models.
The eventual application is GH/Normix theory. The entry notes should be useful
without knowledge of that application or its software.

The [owner briefing](ig-entry-curriculum-draft.md) supplies the intended arc.
The [conversation extract](ig-chatgpt-share-extract.md) records questions and
candidate formulas for later investigation. It is a research prompt, not a
mathematical reference. Definitions and claims in public notes need their own
derivations or identifiable sources.

The first batch consists of the hub and six notes listed below. It ends at
elementary Fisher and dual geometry. Marginal metrics, geometric EM, EM rates,
and GH specialization are planned here but are not implemented in this batch.
The successful pinned foundation build under `/math/` satisfies the prerequisite
for beginning these pages; Incerto migration is independent of this work.

## Reader and notation

Assume multivariable calculus, matrix multiplication and positive definite
quadratic forms, basic probability densities, and expectation. Introduce
manifolds and Hilbert-space projection where needed. Readers should be able to
follow each finite-dimensional example without prior differential geometry.

Use $p_\theta(x)$ for a statistical model, $\ell_\theta=\log p_\theta$ for its
log density, and $s_\theta=\nabla_\theta\ell_\theta$ for its score. In an
exponential family, $\theta$ denotes natural coordinates, $\psi$ the
log-partition function, and $\eta=\nabla\psi$ expectation coordinates. For
latent models, use $P_\theta(x,z)$ for the joint, $p_\theta(x)$ for the marginal,
and $r_\theta(z\mid x)$ for the posterior. A later GH page may specialize the
latent variable to a positive mixing variable $Y$ after defining the convention.

Use natural logarithms and the orientation
$D_{\mathrm{KL}}(p\|q)=\mathbb E_p[\log(p/q)]$. If Hellinger distance is used,
fix $H^2(p,q)=1-\int\sqrt{pq}$ explicitly. Keep the raw Euclidean parameter
norm, $L^2(P)$ on random variables, and $L^2(\nu)$ on densities distinct.
Regularity assumptions belong beside the calculation that needs them.

## First batch: Basics

All paths below are relative to `content/`. These are implemented pages.

| Order | Page | Mathematical task | Worked anchor |
| --- | --- | --- | --- |
| Hub | [information-geometry.md](../../content/ig/index.md) | Give prerequisites, notation, reading routes, and the boundary of the present material | The same probability law in different coordinates |
| 1 | [information-geometry-euclidean-to-manifold.md](../../content/information-geometry-euclidean-to-manifold.md) | Explain charts, tangent vectors, metrics, and connections from coordinate changes | Polar coordinates and the interior probability simplex |
| 2 | [information-geometry-exponential-families.md](../../content/information-geometry-exponential-families.md) | Motivate exponential form through sufficient statistics; derive moments, covariance, and moment matching | Bernoulli counts and the normal location-scale family |
| 3 | [information-geometry-latent-variables-em.md](../../content/information-geometry-latent-variables-em.md) | Separate joint, marginal, and posterior; derive ordinary EM and its likelihood inequality | Estimating one mixing weight with fixed component densities |
| 4 | [information-geometry-conditional-expectation.md](../../content/information-geometry-conditional-expectation.md) | Prove conditional expectation is an orthogonal projection onto all square-integrable functions of the observation | A nonlinear conditional mean and total covariance |

The geometry page should establish why coordinates cannot determine a geometry
by themselves. A variable metric matrix in a chart does not establish intrinsic
curvature. A smooth parameter domain also does not, by itself, establish a
regular identifiable statistical model.

The exponential-family page should explain the direction of each implication.
Exponential form gives sufficient statistics by factorization. Sufficiency
alone is not an unrestricted converse. State the open-domain and minimality
conditions needed for an invertible covariance metric; distinguish full families
from constrained or curved subfamilies. An interior likelihood optimum matches
moments, but it need not exist for every sample.

The EM page should hold the old posterior fixed during the M-step. Derive the
lower-bound identity using the actual observations, so continuous empirical
data do not require a false finite KL from an atomic measure to a density.
Explain why a posterior expectation of a complete log likelihood usually needs
more than substitution of a latent mean. Monotonicity is not a theorem of global
convergence.

The conditional-expectation page supplies the linear projection theorem before
the later statistical application. Its hypotheses require square integrability
of the projected quantity, which need not be the observation itself. The
conditional covariance identity prepares the missing-information calculation
without asserting it for an unspecified model.

Information theory is optional as a separate introductory course. KL and its
nonnegativity are introduced in the EM note; local KL and Hellinger expansions
appear with Fisher geometry. Entropy appears only where it explains a lower
bound or a convex dual. A later optional
`information-geometry-entropy-and-divergences.md` can collect entropy, differential
entropy, chain rules, and data processing if cross-page repetition warrants it.
It is not a prerequisite and has no page in the current TOC.

## First batch: Early IG core

| Order | Page | Mathematical task | Worked anchor |
| --- | --- | --- | --- |
| 5 | [information-geometry-fisher-vs-l2.md](../../content/information-geometry-fisher-vs-l2.md) | Derive Fisher information from scores and local KL; verify the coordinate transformation law; distinguish the three uses of $L^2$ | Bernoulli probability versus log odds; square-root densities |
| 6 | [information-geometry-duality.md](../../content/information-geometry-duality.md) | Introduce dual affine coordinates, Bregman/KL orientation, Fisher orthogonality, a Pythagorean identity, and the $\alpha$-connections | Two independent Bernoulli variables and a constrained fit |

These notes should make the statistical interpretation of the metric explicit:
it measures the mean square first-order change in log density. A Euclidean
parameter metric can be an intentional modeling choice, but resetting its matrix
to the identity after every nonlinear reparameterization changes that choice.
Fisher information is already an $L^2$ construction on scores.

The duality page should derive its Pythagorean identity algebraically with KL
arguments in a fixed order. State the affine-set and interior-optimum conditions
for projection equalities. Explain that an expectation-coordinate line inside
an exponential family need not be the literal mixture of its endpoint densities.
Introduce $\alpha=1$ as exponential, $\alpha=-1$ as mixture, and $\alpha=0$ as
Levi-Civita. Dual flatness concerns the first two connections; Riemannian
curvature concerns the third. Detailed curvature calculations come later.

After this batch, a reader should be able to derive a Bernoulli Fisher metric
in two charts, write one exact EM update, prove the conditional projection
identity, and check a KL Pythagorean identity without confusing these different
notions of projection.

## Later IG core: Marginalization and inference

These are proposed stems, not existing files or links. Write them in dependency
order after reviewing the first batch.

| Proposed stem | Prerequisites | Required result and boundary |
| --- | --- | --- |
| `information-geometry-marginalization.md` | EM, conditional expectation, Fisher | Derive the KL chain rule and the Hellinger loss identity; differentiate marginalization to obtain $s_o=\mathbb E[s_c\mid X]$ under stated domination assumptions |
| `information-geometry-missing-information.md` | Marginalization | Prove $I_c=I_o+I_{\mathrm{miss}}$ as a score covariance decomposition; distinguish expected information from a sample observed Hessian; handle singular directions before taking inverses |
| `information-geometry-em-as-projection.md` | EM, duality, marginalization | Define the entire fixed-observable-marginal fiber, prove its KL minimizer is posterior completion, and derive alternating minimization with KL orientation explicit |
| `information-geometry-two-e-steps.md` | Geometric EM | Compare ordinary posterior completion with projection onto a finite-dimensional moment manifold; verify Amari's assumptions and counterexample in the original paper before quoting them |
| `information-geometry-em-local-rate.md` | Missing information, geometric EM | Differentiate a smooth population EM map at an interior correctly specified fixed point; interpret $I_o v=\lambda I_c v$ and the factor $1-\lambda$; state what changes for finite samples or misspecification |
| `information-geometry-curvature.md` | Duality, Fisher | Define connection curvature, distinguish it from the shape of an embedding, and compute a two-dimensional example with its metric and curvature normalization fixed |

The central connection to develop is that posterior conditional expectation
retains the observable part of a joint score. The resulting covariance loss
also appears in EM's local derivative. This is a program of derivations, not a
claim that every latent model has a full exponential-family parameterization or
that every quotient is a smooth manifold.

## Later GH/Normix research

Start only after the general identities above have been checked. Keep theoretical
notes here and the JAX implementation, public API, package tests, and releases
in [Normix](https://github.com/xshi19/normix), following the
[repository boundary](consolidation.md#repository-boundaries).

| Proposed stem | Research question | Evidence required before a substantive page |
| --- | --- | --- |
| `information-geometry-gh-identifiability.md` | Which joint parameter changes preserve the observable law? | Define the precise GIG and normal-mixture convention; derive the scale action; check a local quotient or gauge and its exceptional cases |
| `information-geometry-gh-marginal-metric.md` | How much joint Fisher information survives observation? | Derive the joint sufficient statistics and their posterior expectations; verify the covariance decomposition; distinguish a pullback of the marginal metric from restriction of the joint metric |
| `information-geometry-gh-em-spectrum.md` | Which observable directions explain slow EM? | Compare generalized information eigenvalues with a specified EM map; report quadrature or Monte Carlo uncertainty and separate population predictions from finite-sample results |
| `information-geometry-gh-curvature.md` | What changes on low-dimensional identifiable subfamilies? | Check the metric, cubic tensor, coordinate derivatives, and connection convention against analytic limiting cases before numerical curvature claims |

No general GH curvature formula, package implementation, or numerical experiment
is part of the first batch. Student and Cauchy mixtures are candidates for later
checks because they permit independent calculations; they do not establish
claims about the whole GH family.

## Sources and checks on the briefing

The public pages contain original explanations and derivations. References
provide definitions and further reading; they are not sources for copied book
chapters or inherited conversational prose.

- Michael I. Jordan, [The Exponential Family: Basics](https://people.eecs.berkeley.edu/~jordan/courses/260-spring10/other-readings/chapter8.pdf),
  especially §§8.3–8.7: background on moment derivatives, sufficiency, and
  likelihood. Its natural-parameter notation differs from ours.
- Radford M. Neal and Geoffrey E. Hinton,
  [A view of the EM algorithm that justifies incremental, sparse, and other variants](https://www.cs.utoronto.ca/~hinton/csc2535_06/readings/emk.pdf)
  (1998): the free-energy formulation of ordinary EM.
- Frank Nielsen, [An elementary introduction to information geometry](https://arxiv.org/abs/1808.08271)
  (2020 revision), §§2–3: geometry, dual connections, and divergence conventions.
- Frank Nielsen, [On Voronoi diagrams and dual Delaunay complexes on the information-geometric Cauchy manifolds](https://arxiv.org/abs/2006.07020),
  §2.1, equation (14): in location-scale coordinates the Cauchy Fisher metric is
  $(d\mu^2+d\sigma^2)/(2\sigma^2)$. The extract's scale coefficient differs;
  do not propagate that displayed metric. Any later curvature statement must
  also distinguish Gaussian curvature from scalar curvature.

Other references named in the extract remain leads for the later pages. Check
their titles, relevant statements, parameter conventions, and hypotheses before
using their formulas. In particular, the two-E-step counterexample and the GH
scale action require source-level verification in their own implementation batch.

## Authoring and completion

Use unique Markdown stems flat under `content/`. MyST CLI 1.10.1 derives these
routes from filenames and ignores `slug:`; repeated nested `index.md` files
produce `index-N/` paths. The earlier draft's nested-directory suggestion is
superseded. Add the six pages as children of the IG hub in `myst.yml`, and use
relative source links among existing pages. Do not create links to proposed
stems. Preserve `BASE_URL=/math` in the build script.

Each batch requires mathematical and citation review, a pinned strict HTML
build, local route/asset/fragment and rendered-math checks, and desktop/mobile
inspection under `/math/`. Record results and limitations in the
[verification record](../records/ig-entry-verification.md). Future research pages
also need derivations or reproducible numerical evidence appropriate to each
claim. A local site build establishes neither mathematical correctness nor a
public deployment.
