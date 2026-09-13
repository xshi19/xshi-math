# Information Geometry of Marginals — extract from shared ChatGPT conversation

Source: https://chatgpt.com/share/6aa5f5d6-1060-83ea-a30b-6c71f42b8768
Title: **Information Geometry of Marginals**
Access: public read-only share; content rendered without login.

## Xiang's goals/questions

- For Normix's generalized hyperbolic (GH) / normal-mixture distributions, understand the information geometry of the observable marginal p(x), given that the joint p(x,y)=p(x|y)p(y) is an exponential family with a simple dual-flat structure and Fisher metric.
- Determine whether the marginal family has a useful information-geometric framework, despite generally not being exponential/dually flat.
- Relate KL and Hellinger bounds computed on the joint to the marginal, and understand what is lost by marginalization.
- Understand Amari's EM-as-projection picture: what the E-step and M-step are, how the formulas are derived, whether Amari's two E-steps are related, and why conditional expectation is an orthogonal projection.

## Main recommendation / conceptual thesis

Study the **marginal Fisher geometry on the identifiable parameter space**, using conditional expectation to relate it to the joint exponential-family geometry. The same missing-information object links:

1. joint-vs-marginal divergence bounds,
2. latent-scale/gauge redundancy,
3. the marginal Fisher metric and curvature, and
4. EM's local convergence speed.

Marginalization preserves a natural Riemannian/Fisher geometry and Amari's alpha-connections, but generally does **not** preserve the joint family's dual flatness.

## Divergences and information loss

Write P_theta(x,y) = p_theta(x) r_theta(y|x), with r the latent posterior. The KL chain rule is

D_KL(P_theta || P_phi) = D_KL(p_theta || p_phi)
  + E_{X~p_theta} D_KL(r_theta(.|X) || r_phi(.|X)).

Thus the excess joint KL is exactly the difference in latent explanations after observing X. Joint and marginal KL agree when the relevant posteriors agree; a large joint divergence can coexist with close observable marginals.

For H^2(p,q)=1 - integral sqrt(pq), the shared answer states

H^2(P_theta,P_phi) - H^2(p_theta,p_phi)
 = integral sqrt(p_theta(x)p_phi(x)) H^2(r_theta(.|x),r_phi(.|x)) dx.

(Here the displayed convention is the conversation's convention.) For GH mixtures the posteriors are GIG, making these decompositions tractable.

## Marginal Fisher metric / central formulas

Complete and observed scores:

s_c = grad_theta log P_theta(X,Y),
 s_o = grad_theta log p_theta(X).

Differentiation under the integral gives the key identity

s_o(X) = E_theta[s_c(X,Y) | X].

Therefore

I_o = E[s_o s_o^T]
    = I_c - I_miss,
I_miss = E[ Cov(s_c | X) ].

This is a Pythagorean decomposition in L^2_0(P): observing X retains the score component predictable from X and discards the conditional (latent) component. Locally,

D_KL(p_theta || p_{theta+dtheta}) = 1/2 dtheta^T I_o dtheta + o(||dtheta||^2),
H^2(p_theta,p_{theta+dtheta}) = 1/8 dtheta^T I_o dtheta + o(||dtheta||^2).

Both divergences therefore recover the same marginal Riemannian metric locally (up to normalization).

For an exponential-family joint
P_theta(x,y)=h(x,y) exp(theta^T T(x,y)-psi(theta)),
let eta=grad psi and m_theta(x)=E[T(X,Y)|X=x]. Then

s_o(x)=m_theta(x)-eta(theta),
I_o = Cov_X(m_theta(X))
    = grad^2 psi(theta) - E[Cov(T|X)].

This is the central Normix formula: **joint metric = covariance of sufficient statistics; marginal metric = covariance of posterior expected sufficient statistics.** The marginal log-density Hessian also has the x-dependent term Cov(T|X=x), so the joint potential psi alone does not generate the marginal metric.

## Identifiability / GH scale quotient

With Normix's convention Y~GIG(lambda,a,b), the transformation

(mu,gamma,Sigma,lambda,a,b) -> (mu,gamma/c,Sigma/c,lambda,a/c,c b), c>0

leaves the law of X unchanged. Hence the marginal Fisher metric has a null/gauge direction even when joint Fisher information is positive definite. Use the quotient Theta/~ where p_theta=p_phi, with a gauge such as |Sigma|=1 or E[Y]=1 (when defined).

A gauge removes scale redundancy but does not restore dual flatness; restricting the joint metric to a gauge is generally larger than the true marginal metric. Minimizing joint lengths over scale changes cannot remove all marginally invisible latent changes.

## Marginal information geometry and curvature

On an identifiable regular model, define

g_ij=E[s_{o,i}s_{o,j}], C_ijk=E[s_{o,i}s_{o,j}s_{o,k}].

The canonical alpha-connections are

nabla^(alpha) = nabla^LC - (alpha/2) C-sharp,

with exponential and mixture connections at alpha=1 and -1. They exist without a finite-dimensional exponential-family representation, and can be curved. Dual flatness is distinct from zero Levi-Civita curvature.

Example cited: the Cauchy location-scale family is a normal inverse-gamma mixture with

ds^2 = (dmu^2)/(2 sigma^2) + (dsigma^2)/(sigma^2),
K = -2 (as rendered in the shared conversation; exact metric normalization should be checked against the linked paper).
Its cubic tensor is said to vanish, so canonical alpha-connections coincide with Levi-Civita; Nielsen's Cauchy-manifold paper is cited as a reference. The example shows marginalization can produce curved canonical geometry, not the curvature of the full GH family.

## EM as KL projection (population and finite sample)

For population data density q(x), define the fixed-marginal fiber
F_q={R(x,y)=q(x)s(y|x): s any conditional density}.
It is mixture-affine and preserves the entire observable distribution. KL decomposition gives

D_KL(R||P_theta)=D_KL(q||p_theta)
 + E_q D_KL(s(.|X)||r_theta(.|X)).

The minimizer over F_q is R_theta^*(x,y)=q(x)r_theta(y|x), and

D_KL(q||p_theta)= inf_{R in F_q} D_KL(R||P_theta).

EM alternates:

R_t = argmin_{R in F_q} D_KL(R||P_{theta_t}),
P_{theta_{t+1}} = argmin_{P_theta} D_KL(R_t||P_theta).

There is an exact E-step Pythagorean identity:
D_KL(R||P_theta)=D_KL(R||R_theta^*)+D_KL(R_theta^*||P_theta), R in F_q.

For continuous empirical data, use the ordinary averaged log-likelihood/posterior identities rather than literal KL from an atomic empirical measure to a continuous model.

### Ordinary EM derivation

For observations x_i, the objective is
ell(theta)=(1/n) sum_i log p_theta(x_i)=(1/n) sum_i log integral P_theta(x_i,y)dy.

E-step:
Q(theta|theta_t)=(1/n) sum_i E_{theta_t}[log P_theta(x_i,Y_i)|X_i=x_i].

M-step: theta_{t+1} in argmax_theta Q(theta|theta_t).

The posterior in the expectation is held fixed at theta_t during the M-step; the E-step does not simply substitute a posterior mean for Y. In Normix, Y, Y^{-1}, and log Y need separate posterior expectations.

Using P_theta=p_theta r_theta and r_{t,i}=r_{theta_t}(.|x_i),

ell(theta)=Q(theta|theta_t)+H_t
 +(1/n) sum_i D_KL(r_{t,i}||r_theta(.|x_i)),

where H_t is theta-independent. This proves monotonicity and the proximal form

theta_{t+1} in argmax_theta {ell(theta) - (1/n) sum_i D_KL(r_{t,i}||r_theta(.|x_i))}.

For an exponential-family joint, with m_theta(x)=E_theta[T|X=x],
Q(theta|theta_t)=theta^T mbar_t - psi(theta)+const,
mbar_t=(1/n) sum_i m_{theta_t}(x_i),
so the unconstrained M-step satisfies

grad psi(theta_{t+1}) = mbar_t.

That is: posterior expectations -> new expectation coordinates eta_{t+1} -> theta_{t+1}.

## Amari's two E-steps: what differs

The statistical E-step uses pointwise conditional expectations and then averages over actual observations. Amari's geometric lowercase e-step minimizes KL over a specified finite-dimensional data/moment manifold. They coincide for the full fixed-marginal fiber, but need not coincide for a finite-dimensional moment manifold.

If sufficient statistics split as (U,V), and D_u={P_{a,b}: E[U]=u}, geometric e-projection keeps hidden natural parameter b fixed and changes a to enforce E[U]=u. Its completed moment is (u,E_e[V]), whereas the statistical E-step gives (u,E_theta[V|U=u]). They agree when these match; an affine conditional mean E[V|U]=A U+c is a useful sufficient condition.

The cited Gaussian counterexample (from Amari's Appendix 1) uses Z_1,Z_2 iid N(u,u^2), observed U=2Z_1+Z_2=c, hidden V=2Z_1^2+Z_2^2. The statistical conditional second moment is c^2+2u^2; geometric e-projection gives c^2+u^2. The observed-data MLE is u_MLE=(sqrt(3)-1)c, while the geometric alternating scheme intersects at u=c.

For Normix, retain the exact pointwise posterior E-step; replacing it with a few observed moments needs extra justification.

## Conditional expectation as orthogonal projection

In L^2(P), H_X={g(X): E[g(X)^2]<infinity} is a closed linear subspace. For m(X)=E[A|X],

<A-m(X),g(X)>=0 for every g(X) in H_X.

Thus Pi_X A=E[A|X], and

E[(A-g(X))^2]=E[(A-E[A|X])^2]+E[(E[A|X]-g(X))^2].

The subspace contains all square-integrable functions of X, not only linear functions of X. For a joint path P_epsilon=P(1+epsilon a)+o(epsilon), marginalization sends its score to E[a|X]. Hence conditional expectation is literally the differential of marginalization in score coordinates.

The fixed-marginal fiber tangent is {a in L^2_0(P): E[a|X]=0}; every joint tangent splits into observable and fiber components. Applying this to scores gives s_r=s_c-s_o, E[s_r|X]=0, and

I_c = I_o + I_miss,
I_miss=E[s_r s_r^T].

At the E-step, log(R_t/P_{theta_t}) depends only on X and is orthogonal to fiber tangents. At the M-step optimum, the mixture-geodesic direction is orthogonal to the joint-model tangent space. Global KL projections therefore have infinitesimal Fisher-orthogonality interpretations.

## EM local rate / concrete claims

At a correctly specified fixed point q=p_{theta*}, for a full exponential-family joint,

DM(theta*) = I_c^{-1} I_miss = I - I_c^{-1} I_o.

If I_o v=lambda I_c v, the local EM error factor in that direction is 1-lambda:

- lambda near 1: most information is observable; fast EM.
- lambda near 0: motion mostly changes the latent explanation; slow EM.
- lambda=0: infinitesimally unidentifiable/gauge direction; neutral unreduced EM.

For fixed-nu Student mixtures, Y~InvGamma(nu/2,nu/2), X|Y~N(mu,sigma^2 Y), in coordinates (mu, log sigma), the conversation gives diagonal complete/marginal information and EM-factor table:

- mu: I_c=sigma^{-2}; I_o=((nu+1)/(nu+3)) sigma^{-2}; factor 2/(nu+3).
- log sigma: I_c=2; I_o=(2nu/(nu+3)); factor 3/(nu+3).

For Cauchy (nu=1), it says the marginal retains half the complete location information and one quarter of complete log-scale information; EM factors are 1/2 and 3/4. These claims hold for all nu>0 even when ordinary observation variance does not exist.

## GH / Normix implementation route

The GH posterior is
Y|X=x ~ GIG(lambda-d/2, a+gamma^T Sigma^{-1} gamma,
              b+(x-mu)^T Sigma^{-1}(x-mu)).

Order joint sufficient statistics as
T(x,y)=(log y, y^{-1}, y, x, x/y, xx^T/y),
using independent entries for the symmetric block. Then

m_theta(x)=(E[log Y|x], E[Y^{-1}|x], E[Y|x],
            x, x E[Y^{-1}|x], xx^T E[Y^{-1}|x]).

Compute
I_o=Cov_{p_theta}(m_theta(X));
for identifiable coordinates phi with joint natural parameters theta(phi),
g_phi=J^T I_o J, J=partial theta/partial phi.

Latent integration is analytic through GIG moments; the remaining X expectation can use quadrature or Monte Carlo.

## Proposed learning path / curriculum

1. Probability and measure basics for latent-variable models: conditional densities, regularity, differentiation under integrals, KL/Hellinger.
2. Ordinary EM first: observed likelihood, complete likelihood, posterior E-step, Q-function, M-step, monotonicity/proximal identity.
3. Exponential families: natural/expectation coordinates, log-partition psi, sufficient statistics, moment matching.
4. Fisher geometry: scores, Fisher metric, local divergence expansions, information matrices.
5. Conditional expectation in L^2: Hilbert-space projection, Pythagoras, score decomposition.
6. Marginalization as a map of statistical models: observable tangent = conditional expectation; fixed-marginal fibers and quotient/identifiability.
7. Missing information: I_o=I_c-I_miss; generalized eigenproblem I_o v=lambda I_c v; interpretation as observable information and EM rate.
8. KL geometry of EM: mixture-affine fixed-marginal fiber, e-projection, m-projection, Pythagorean identity.
9. Amari's uppercase EM vs lowercase geometric em: full marginal fiber versus finite-dimensional moment/data manifold; study the equivalence condition and Gaussian counterexample.
10. Amari alpha-connections and curvature: cubic tensor, Levi-Civita connection, dual flatness versus curvature; work first on 1D/2D subfamilies such as Cauchy.
11. GH/Normix specialization: GIG posterior moments, posterior sufficient-statistic map m_theta(x), quotient gauge, numerical covariance/quadrature/Monte Carlo.
12. Research priorities: marginal metric/null directions; generalized spectrum and slow EM; marginal cubic tensor and curvature on low-dimensional GH subfamilies.

## Concrete references/page titles cited in the chat

- Ay–Jost–Lê–Schwachhöfer, linked as arXiv:1207.6736 (information loss/statistical information geometry).
- Hino–Akaho–Murata, §4, linked as arXiv:2209.01301v2 (EM/KL projection construction).
- Neal and Hinton, “A view of the EM algorithm that justifies incremental, sparse, and other variants,” linked from cs.toronto.edu (lower-bound/alternating-optimization treatment).
- Amari's 1995 note, linked PDF at bsi-ni.brain.riken.jp/database/file/148/151.pdf (theorem, appendices, two E-step distinction).
- Noll, discussion of Amari's condition, §8, linked as arXiv:2601.02252.
- Nielsen's Cauchy-manifold paper, linked as arXiv:2006.07020.

## Final distilled research advice

Start with the interior GH family after fixing the scale quotient. Implement m_theta(x) from the existing GIG posterior code, estimate Cov(m_theta(X)) and E[Cov(T|X)], and compare the generalized spectrum I_o v=lambda I_c v with observed EM convergence. Only then study the marginal cubic tensor/curvature on low-dimensional subfamilies. The same posterior moments already computed by Normix's E-step support all three viewpoints: marginal geometry, missing information, and EM speed.
