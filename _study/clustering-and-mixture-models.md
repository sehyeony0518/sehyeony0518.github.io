---
layout: study_note
title: "Clustering and Mixture Models: k-means, GMM, and the Log of a Sum"
description: "Hard assignment by alternating minimisation, soft assignment by a density, and the structural reason the mixture likelihood cannot be solved by differentiating."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "probability-and-inference"
category_title: "Probability & Statistical Inference"
subgroup: "Latent Variables & Approximate Inference"
order: 9
source: "Independent study"
written: true
updated: "2026-09-15"
---

A clustering algorithm must decide what counts as similarity before it can discover a grouping. A mixture model must specify how observations could have been generated before it can assign probabilities to possible groups. These are related tasks, but neither grouping nor probability removes the assumptions.

The connection becomes precise for Gaussian components with a common spherical covariance. As that covariance shrinks, posterior assignments approach nearest-centre assignments, and a rescaled mixture objective approaches the k-means objective. Deriving this connection also exposes two common mistakes: k-means has simple conditional updates, not a general closed-form joint solution; and a mixture likelihood can be differentiated, even though the resulting equations usually cannot be solved explicitly.

## What is being estimated?

Let the observations be $$x_1,\ldots,x_N\in\mathbb R^d$$, and choose a number of clusters $$K$$. A hard assignment records one cluster for each observation. Write it using indicators:

$$
r_{nk}\in\{0,1\},
\qquad
\sum_{k=1}^K r_{nk}=1.
$$

The sum constraint matters. Without it, setting every indicator to zero would make a distance-based objective zero without assigning anything.

A Gaussian mixture instead introduces a categorical latent variable $$z_n$$ and parameters

$$
\theta=\{\pi_k,\mu_k,\Sigma_k\}_{k=1}^K,
\qquad
\pi_k\geq0,\quad\sum_k\pi_k=1.
$$

Its generative construction is

$$
p(z_n=k)=\pi_k,
\qquad
p(x_n\mid z_n=k,\theta)
=\mathcal N(x_n\mid\mu_k,\Sigma_k).
$$

The component index is unobserved. The observed density is obtained by summing over mutually exclusive possibilities:

$$
p(x_n\mid\theta)
=\sum_k\pi_k\mathcal N(x_n\mid\mu_k,\Sigma_k).
$$

This is a normalised density because integrating each Gaussian gives one and the weights sum to one. To generate a new observation, sample a component index and then sample from its Gaussian.

A component is a term in this construction. It is not automatically a biological subgroup, a separate peak, or a useful cluster. Two overlapping components can describe one broad peak. Permuting their indices changes neither the density nor the likelihood. Component numbers therefore have no intrinsic meaning.

## Deriving both k-means updates

The squared Euclidean objective is

$$
J(r,\mu)
=\sum_{n=1}^N\sum_{k=1}^K
r_{nk}\lVert x_n-\mu_k\rVert^2.
$$

Fix the centres. For observation $$n$$, the contribution to the objective is one of the squared distances, because exactly one indicator must equal one. Choosing the smallest contribution gives

$$
r_{nk}=1
\quad\text{for a chosen }k\in
\arg\min_j\lVert x_n-\mu_j\rVert^2.
$$

A tie requires a convention. It does not supply evidence that one tied cluster is more appropriate.

Now fix the assignments. Define the count

$$
N_k=\sum_n r_{nk}.
$$

Only terms belonging to cluster $$k$$ depend on its centre. Differentiate the squared distance coordinate by coordinate:

$$
\nabla_{\mu_k}J
=2\sum_n r_{nk}(\mu_k-x_n)
=2N_k\mu_k-2\sum_n r_{nk}x_n.
$$

For a nonempty cluster, setting this to zero gives

$$
\mu_k=\frac{\sum_n r_{nk}x_n}{N_k}.
$$

Its Hessian is $$2N_kI$$, which is positive definite when $$N_k>0$$, so this conditional minimiser is unique. If the cluster is empty, the objective does not depend on its centre. The fraction is undefined; an implementation needs an explicit empty-cluster policy.

Alternating these updates cannot increase the objective: each solves one block of variables while holding the other fixed. Since squared distances are nonnegative, the objective values have a finite limit. That reasoning does not prove that the joint solution is globally optimal. The assignment choices make the full problem nonconvex, and different initial centres can lead to different final partitions.

The metric is part of the model. Rescaling a feature changes its squared-distance contribution. If one coordinate is multiplied by ten, its contribution is multiplied by one hundred. Standardising features therefore changes the clustering question; it is not merely a computational convenience.

## A k-means iteration that can be checked by hand

Take four one-dimensional observations and two initial centres:

$$
x=(0,1,4,5),
\qquad
\mu^{\mathrm{old}}=(0,3).
$$

The assignment step is completely determined by the following distances.

| Observation | Squared distance to first centre | Squared distance to second centre | Assigned cluster |
|---|---:|---:|---|
| $$0$$ | $$0$$ | $$9$$ | First |
| $$1$$ | $$1$$ | $$4$$ | First |
| $$4$$ | $$16$$ | $$1$$ | Second |
| $$5$$ | $$25$$ | $$4$$ | Second |

The objective after this assignment is

$$
J_{\mathrm{old}}=0+1+1+4=6.
$$

The centre update gives

$$
\mu_1^{\mathrm{new}}=\frac{0+1}{2}=\frac12,
\qquad
\mu_2^{\mathrm{new}}=\frac{4+5}{2}=\frac92.
$$

Every assigned point is now half a unit from its centre, so

$$
J_{\mathrm{new}}
=4\left(\frac12\right)^2=1.
$$

Reassigning with these centres leaves the same partition. This verifies a fixed point of the alternating procedure for this construction. It does not establish a general theorem that any initialisation finds the best partition.

Notice also that k-means has produced no covariance, mixing probability, or probability for a new observation. Those require additional modelling choices.

## Why one Gaussian has explicit likelihood estimates

For a positive-definite covariance, the Gaussian density is

$$
\mathcal N(x\mid\mu,\Sigma)
=
(2\pi)^{-d/2}|\Sigma|^{-1/2}
\exp\left[
-\frac12(x-\mu)^\top\Sigma^{-1}(x-\mu)
\right].
$$

The inverse covariance measures distance relative to spread. The determinant compensates for the volume occupied by the distribution. Broadening a component makes its density lower near its centre; the exponential term alone would miss this normalisation effect.

For independent observations, the log-likelihood is

$$
\ell(\mu,\Sigma)
=
-\frac{Nd}{2}\log(2\pi)
-\frac N2\log|\Sigma|
-\frac12\sum_n
(x_n-\mu)^\top\Sigma^{-1}(x_n-\mu).
$$

The logarithm has converted a product into a sum and cancelled the exponential. Differentiating with respect to the mean gives

$$
\nabla_\mu\ell
=
\Sigma^{-1}\sum_n(x_n-\mu)=0.
$$

Since the covariance is invertible,

$$
\widehat\mu=\bar x=\frac1N\sum_nx_n.
$$

For the covariance, use the precision matrix and residual scatter:

$$
\Lambda=\Sigma^{-1},
\qquad
S=\sum_n(x_n-\bar x)(x_n-\bar x)^\top.
$$

The identity

$$
v^\top\Lambda v
=\operatorname{tr}(\Lambda vv^\top)
$$

turns the remaining expression into

$$
\ell(\Lambda)
=\frac N2\log|\Lambda|
-\frac12\operatorname{tr}(\Lambda S)+\text{constant}.
$$

To see the derivative of the log determinant, perturb the matrix by a small symmetric matrix $$tE$$:

$$
\log|\Lambda+tE|
=
\log|\Lambda|
+\log|I+t\Lambda^{-1}E|
=
\log|\Lambda|
+t\operatorname{tr}(\Lambda^{-1}E)+o(t).
$$

Thus the differential of the log-likelihood is

$$
d\ell
=
\frac12\operatorname{tr}
\left[(N\Lambda^{-1}-S)d\Lambda\right].
$$

Setting it to zero for every symmetric perturbation gives

$$
\widehat\Sigma=\frac SN.
$$

This is an interior estimate only when the scatter is positive definite. A singular scatter does not define a nonsingular Gaussian maximum by this formula.

Why divide by the sample count rather than one less? Because this is maximum likelihood, not an unbiasedness requirement. The difference can be derived. Let the true mean and covariance be $$m$$ and $$C$$. Expanding around the true mean gives

$$
\sum_n(x_n-\bar x)(x_n-\bar x)^\top
=
\sum_n(x_n-m)(x_n-m)^\top
-N(\bar x-m)(\bar x-m)^\top.
$$

The first term has expectation $$NC$$. Independence gives $$\operatorname{Cov}(\bar x)=C/N$$, so the second has expectation $$C$$. Therefore

$$
\mathbb E[\widehat\Sigma]
=
\frac{N-1}{N}C.
$$

The correction for an ordinary sample covariance follows from this identity. It does not automatically transfer to mixture responsibilities, which are estimated from the same observations and are not fixed integer memberships.

## The log of a sum produces implicit equations

For the mixture, write each observation's density as

$$
s_n(\theta)
=\sum_j\pi_j\mathcal N(x_n\mid\mu_j,\Sigma_j).
$$

The observed log-likelihood is

$$
\ell(\theta)=\sum_n\log s_n(\theta).
$$

The problem is not that this expression is impossible to differentiate. Apply the chain rule and use the Gaussian mean derivative:

$$
\begin{aligned}
\nabla_{\mu_k}\ell
&=
\sum_n\frac{1}{s_n(\theta)}
\pi_k\mathcal N(x_n\mid\mu_k,\Sigma_k)
\Sigma_k^{-1}(x_n-\mu_k)\\
&=
\sum_n\gamma_{nk}(\theta)
\Sigma_k^{-1}(x_n-\mu_k),
\end{aligned}
$$

where

$$
\gamma_{nk}(\theta)
=
\frac{\pi_k\mathcal N(x_n\mid\mu_k,\Sigma_k)}
{\sum_j\pi_j\mathcal N(x_n\mid\mu_j,\Sigma_j)}.
$$

At an interior stationary point, rearranging gives

$$
\mu_k
=
\frac{\sum_n\gamma_{nk}(\theta)x_n}
{\sum_n\gamma_{nk}(\theta)}.
$$

This resembles an explicit weighted mean, but the weights contain the unknown means, covariances, and mixing proportions. The parameter being solved for still appears on the right-hand side. The equation is a self-consistency condition.

In a single Gaussian, every observation has weight one and the coupling disappears. In a general mixture, the logarithm encloses a sum, so it cannot be distributed across components to remove that coupling. Numerical iteration is generally needed. EM is a particularly useful iterative scheme, but direct likelihood optimisation is also possible. The presence of a sum does not make EM the only legitimate algorithm.

## Responsibilities follow from Bayes' rule

The fraction introduced by differentiation has a probabilistic meaning. The joint density is

$$
p(x_n,z_n=k\mid\theta)
=
\pi_k\mathcal N(x_n\mid\mu_k,\Sigma_k).
$$

Dividing by the marginal density gives

$$
p(z_n=k\mid x_n,\theta)=\gamma_{nk}(\theta).
$$

These are called responsibilities because each observation contributes a fractional count to each component. They satisfy

$$
\gamma_{nk}\geq0,
\qquad
\sum_k\gamma_{nk}=1.
$$

The denominator is essential: a high component density does not imply high membership probability if another weighted component density is higher.

For two one-dimensional components with common variance, the posterior log odds are

$$
\log\frac{\gamma_{n1}}{\gamma_{n2}}
=
\log\frac{\pi_1}{\pi_2}
+
\frac{(x_n-\mu_2)^2-(x_n-\mu_1)^2}{2\sigma^2}.
$$

This follows by dividing the two Bayes fractions: their denominators cancel, and the common Gaussian normalisers cancel. It separates the prior preference from the distance evidence.

For a constructed example, take equal weights, means zero and two, variance one, and observation one half. The squared distances are one quarter and nine quarters, so

$$
\log\frac{\gamma_1}{\gamma_2}
=
\frac{9/4-1/4}{2}=1.
$$

Normalising the odds gives

$$
\gamma_1=\frac{e}{1+e}\approx0.731059,
\qquad
\gamma_2=\frac{1}{1+e}\approx0.268941.
$$

If the first weight is changed to one quarter and the second to three quarters, the same observation has

$$
\gamma_1=\frac{e}{e+3}\approx0.475367.
$$

The nearer centre now has less than half the posterior probability. Its distance advantage is outweighed by the prior odds.

With unequal covariances, the log odds also include determinant terms and distinct covariance-weighted distances. Nearest Euclidean centre then need not be the most probable component.

## From posterior memberships to EM updates

Introduce one-hot indicators $$z_{nk}$$. If they were observed, the complete-data log-likelihood would be

$$
\log p(X,Z\mid\theta)
=
\sum_{n,k}z_{nk}
\left[
\log\pi_k+\log\mathcal N(x_n\mid\mu_k,\Sigma_k)
\right].
$$

The E step computes the responsibilities using the old parameters. Taking the conditional expectation replaces each indicator by its posterior expectation:

$$
Q(\theta\mid\theta^{\mathrm{old}})
=
\sum_{n,k}\gamma_{nk}^{\mathrm{old}}
\left[
\log\pi_k+\log\mathcal N(x_n\mid\mu_k,\Sigma_k)
\right].
$$

Now the weights are fixed by the definition of a new objective. Holding them fixed is legitimate; it is not an instruction to ignore a derivative of the original likelihood.

Define the effective component count

$$
N_k=\sum_n\gamma_{nk}^{\mathrm{old}}.
$$

Differentiating the weighted quadratic gives

$$
N_k\mu_k-\sum_n\gamma_{nk}^{\mathrm{old}}x_n=0.
$$

For the weights, a Lagrange multiplier enforcing normalisation gives

$$
\frac{N_k}{\pi_k}-\lambda=0,
\qquad
\lambda=\sum_kN_k=N.
$$

The precision-matrix calculation from the single-Gaussian case applies with weighted scatter. These yield

$$
\begin{aligned}
\pi_k^{\mathrm{new}}&=\frac{N_k}{N},\\
\mu_k^{\mathrm{new}}&=
\frac{1}{N_k}\sum_n\gamma_{nk}^{\mathrm{old}}x_n,\\
\Sigma_k^{\mathrm{new}}&=
\frac{1}{N_k}\sum_n\gamma_{nk}^{\mathrm{old}}
(x_n-\mu_k^{\mathrm{new}})
(x_n-\mu_k^{\mathrm{new}})^\top.
\end{aligned}
$$

These formulas require nonzero effective counts and, for an unconstrained full-covariance update, positive-definite weighted scatter. The reason improving this auxiliary objective also improves the observed likelihood is proved in [Why EM works](/study/why-em-works/).

## Deriving k-means as covariance shrinks

Consider a restricted mixture with fixed equal weights and a common isotropic covariance:

$$
\pi_k=\frac1K,
\qquad
\Sigma_k=\varepsilon I,
\qquad
\varepsilon>0.
$$

Treat the variance as fixed while fitting the centres. We then examine a sequence of these models as the variance approaches zero. This is different from allowing each covariance to collapse independently during unconstrained maximum likelihood.

Let

$$
d_{nk}=\lVert x_n-\mu_k\rVert^2.
$$

The responsibility becomes

$$
\gamma_{nk}
=
\frac{\exp[-d_{nk}/(2\varepsilon)]}
{\sum_j\exp[-d_{nj}/(2\varepsilon)]}.
$$

Hold the centres fixed for this limit. If $$k_*$$ is the unique nearest centre, divide numerator and denominator by its exponential:

$$
\gamma_{nk_*}
=
\frac{1}
{1+\sum_{j\ne k_*}
\exp[-(d_{nj}-d_{nk_*})/(2\varepsilon)]}.
$$

Every distance difference in the sum is positive. Every exponential therefore tends to zero, giving

$$
\gamma_{nk_*}\longrightarrow1,
\qquad
\gamma_{nj}\longrightarrow0
\quad(j\ne k_*).
$$

The weighted mean update consequently approaches the k-means mean update, provided the limiting cluster is nonempty.

For the earlier observation at one half, the distance difference is two. Its responsibility for the nearer centre is

$$
\gamma_1=\frac{1}{1+\exp(-1/\varepsilon)}.
$$

| Common variance | Responsibility for nearer centre |
|---|---:|
| $$1$$ | $$0.731059$$ |
| $$1/4$$ | $$0.982014$$ |
| $$1/16$$ | $$0.999999887$$ |

These numbers follow directly from the displayed exponential. No fitting experiment is involved.

The objective has the same limit. Remove the Gaussian normalisation term, which is independent of the centres for fixed variance, and multiply the negative log-likelihood by $$2\varepsilon$$:

$$
F_\varepsilon(\mu)
=
-2\varepsilon
\sum_n
\log\left[
\frac1K\sum_k
\exp\left(-\frac{d_{nk}}{2\varepsilon}\right)
\right].
$$

Let $$m_n=\min_kd_{nk}$$. Factoring out the largest exponential gives

$$
F_\varepsilon
=
\sum_nm_n
-2\varepsilon\sum_n
\log\left[
\frac1K\sum_k
\exp\left(-\frac{d_{nk}-m_n}{2\varepsilon}\right)
\right].
$$

At least one exponential in each sum equals one, and all are at most one. The bracket is therefore between $$1/K$$ and one. Hence

$$
\sum_nm_n
\leq F_\varepsilon(\mu)
\leq
\sum_nm_n+2\varepsilon N\log K.
$$

The upper and lower bounds approach the same quantity:

$$
F_\varepsilon(\mu)
\longrightarrow
\sum_n\min_k\lVert x_n-\mu_k\rVert^2.
$$

This is exactly k-means after minimising over hard assignments. The rescaling matters: it is the reduced objective that approaches squared distortion, not the unmodified log-likelihood.

There are three qualifications. Tied nearest centres retain shared probability; the limit does not choose a unique label. Fixed positive unequal weights disappear from the leading distance term, but can resolve ties and matter at finite variance. A common shrinking anisotropic covariance produces distance weighted by its inverse shape matrix, not ordinary Euclidean k-means.

Finally, this limiting relationship does not imply that running EM with a very small variance finds a global k-means solution. The optimisation still depends on initialisation.

## Reading a fitted mixture critically

A responsibility is conditional on the chosen model and fitted parameters. A point far from every centre can still have a responsibility near one if one component is less implausible than the others. Membership certainty is therefore different from high data density or a good model fit.

Likewise, a covariance measures spread within a fitted component; it does not quantify uncertainty about the estimated centre. Parameter uncertainty requires a separate analysis. Near-duplicate components and interchangeable labels can make raw parameter comparisons misleading.

Unconstrained Gaussian-mixture likelihoods also have a degeneracy: a component can concentrate around a single observation with vanishing variance. Its density there grows without bound. A large training likelihood is consequently not, by itself, evidence of a useful clustering. Covariance restrictions, an explicitly stated penalty or prior, and evaluation beyond the fitted observations address different parts of this problem.

When comparing fits, first align component labels or compare label-invariant objects such as the fitted density and pairwise co-membership. Then ask whether the grouping survives reasonable choices of feature scaling, initialisation, component count, and covariance structure. Stability is evidence about the procedure; semantic meaning still needs information beyond the clustering objective.

## Revision checklist

| Can I reconstruct this without looking? | Check |
|---|---|
| Why must every hard-assignment row sum to one? | Otherwise all-zero assignments minimise the distance objective. |
| Why is the centre an arithmetic mean? | Differentiate the assigned squared distances. |
| What happens to an empty cluster? | Its mean update is undefined and its centre is unconstrained by the current objective. |
| Why does Gaussian maximum likelihood use the sample count? | Differentiate the precision objective; unbiasedness is a separate criterion. |
| What blocks an explicit mixture solution? | The posterior weights depend on the parameters being solved for. |
| Why do responsibilities sum to one? | They are joint component densities divided by their marginal sum. |
| Why may EM hold responsibilities fixed? | They define an expectation under the old parameters. |
| How does k-means emerge? | Shared shrinking isotropic covariance makes assignments hard and the rescaled objective approach distortion. |
| What survives at a distance tie? | Shared posterior mass unless a separate tie rule is imposed. |
| Does a fitted component prove a real subgroup? | No; component meaning requires external evidence. |

## Why it matters for my work

A mixture can describe variation in acquisition or patient populations, but a component label does not establish its cause. I should examine both membership ambiguity and overall density, then compare recovered groups with acquisition metadata and outcomes.

## What I have not resolved

Which representation and covariance assumptions would separate acquisition variation from clinically relevant variation, and what independent evidence would make a recovered component interpretable?
