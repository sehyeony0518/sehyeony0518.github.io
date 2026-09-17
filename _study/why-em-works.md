---
layout: study_note
title: "Why EM Works: Responsibilities, the Q Function, and the Monotonicity Guarantee"
description: "The latent-variable construction of a mixture, the update equations that fall out of it, and the argument that each iteration cannot make the likelihood worse."
og_image: "https://sehyeony0518.github.io/assets/img/og/why-em-works.png"
tab: "ai-foundations"
tab_title: "AI Theory"
category: "probability-and-inference"
category_title: "Probability & Statistical Inference"
subgroup: "Latent Variables & Approximate Inference"
order: 11
source: "Independent study"
written: true
updated: "2026-09-15"
---

EM maximizes an auxiliary function built from an unobserved part of the data. Why should that improve the likelihood of the observations we actually have? The answer is an exact identity: the likelihood improvement equals the auxiliary-function improvement plus a nonnegative divergence between two latent posteriors.

The guarantee needs careful boundaries. Exact EM cannot decrease the observed likelihood when its E step is exact and its M step improves the stated auxiliary objective. If the likelihood is also bounded above, its values converge. Neither statement establishes convergence of the parameters, convergence to a local maximum, or global optimality. Unconstrained Gaussian mixtures need particular care because their likelihood can be unbounded.

## Set up the complete-data model

Let $$X=(x_1,\ldots,x_N)$$ be observed and $$Z$$ contain latent component indicators. Each indicator vector is one-hot:

$$
z_{nk}\in\{0,1\},
\qquad
\sum_kz_{nk}=1.
$$

For a Gaussian mixture,

$$
p_\theta(X,Z)
=
\prod_{n,k}
\left[
\pi_k\mathcal N(x_n\mid\mu_k,\Sigma_k)
\right]^{z_{nk}}.
$$

The exponent selects one component for each observation. Taking logs now produces a sum:

$$
\log p_\theta(X,Z)
=
\sum_{n,k}z_{nk}
\left[
\log\pi_k+
\log\mathcal N(x_n\mid\mu_k,\Sigma_k)
\right].
$$

Marginalizing the indicators recovers the original mixture likelihood. The latent construction has changed the representation, not the observed probability model.

At iteration $$t$$, define

$$
q_t(Z)=p_{\theta_t}(Z\mid X)
$$

and

$$
Q(\theta\mid\theta_t)
=
\mathbb E_{q_t}[\log p_\theta(X,Z)].
$$

The first argument contains candidate parameters. The second specifies the distribution used to take the expectation. Confusing these two roles is the source of the claim that EM somehow ignores a parameter dependence illegitimately.

For the proof below, assume the relevant log-likelihoods, expectations, and divergences are finite, and that the posteriors have compatible support. Positive mixing weights and nonsingular Gaussian covariances provide a convenient setting for the worked example.

## Why freezing responsibilities is legitimate

Bayes' rule gives the responsibilities under the old parameters:

$$
\gamma_{nk}^{(t)}
=
\frac{
\pi_k^{(t)}
\mathcal N(x_n\mid\mu_k^{(t)},\Sigma_k^{(t)})
}{
\sum_j\pi_j^{(t)}
\mathcal N(x_n\mid\mu_j^{(t)},\Sigma_j^{(t)})
}.
$$

They enter the auxiliary function as fixed coefficients:

$$
Q(\theta\mid\theta_t)
=
\sum_{n,k}\gamma_{nk}^{(t)}
\left[
\log\pi_k+
\log\mathcal N(x_n\mid\mu_k,\Sigma_k)
\right].
$$

This is a definition, not an approximation to a derivative.

There is also a valid direct derivative identity. If differentiation can pass through the latent sum,

$$
\begin{aligned}
\nabla_\theta\log p_\theta(X)
&=
\frac{\sum_Z\nabla_\theta p_\theta(X,Z)}
{p_\theta(X)}\\
&=
\sum_Zp_\theta(Z\mid X)
\nabla_\theta\log p_\theta(X,Z).
\end{aligned}
$$

The posterior weights appear after differentiating the likelihood. Setting this gradient to zero gives self-consistency equations because those weights still depend on the unknown parameters. Rearranging those equations is valid; interpreting them as an explicit solution is not.

EM chooses an iterative update by evaluating the posterior at the old parameters and maximizing the resulting expected complete-data log-likelihood. The separate monotonicity proof justifies this choice. It does not justify every possible fixed-point iteration built from the likelihood equations.

## The bound touches the likelihood at the old parameters

Introduce the entropy of the old posterior and its associated bound:

$$
H(q_t)=-\mathbb E_{q_t}[\log q_t(Z)],
\qquad
F_t(\theta)=Q(\theta\mid\theta_t)+H(q_t).
$$

Bayes' rule, applied at any candidate parameters, gives

$$
\log p_\theta(X,Z)
=
\log p_\theta(X)+\log p_\theta(Z\mid X).
$$

Take expectations under the old posterior:

$$
Q(\theta\mid\theta_t)
=
\ell(\theta)
+
\mathbb E_{q_t}[\log p_\theta(Z\mid X)],
$$

where

$$
\ell(\theta)=\log p_\theta(X).
$$

Subtracting the expected log old posterior from both sides gives

$$
F_t(\theta)
=
\ell(\theta)
-
\operatorname{KL}
\left(q_t\Vert p_\theta(Z\mid X)\right).
$$

At the old parameters, both posterior distributions are identical:

$$
F_t(\theta_t)=\ell(\theta_t).
$$

At other parameters, the divergence is nonnegative, so

$$
F_t(\theta)\leq\ell(\theta).
$$

The E step has therefore constructed a lower bound that meets the likelihood exactly where the iteration starts. Raising an arbitrary loose lower bound would not provide the same guarantee.

## Prove monotonicity and identify equality conditions

First verify the sign of the divergence. For positive numbers,

$$
\log u\leq u-1.
$$

One way to prove this is to differentiate the difference:

$$
g(u)=u-1-\log u,
\qquad
g'(u)=1-\frac1u.
$$

The derivative is negative below one and positive above one, so the minimum is at one, where the difference is zero.

For normalized distributions with common positive support,

$$
\begin{aligned}
-\operatorname{KL}(q\Vert r)
&=\sum_Zq(Z)\log\frac{r(Z)}{q(Z)}\\
&\leq\sum_Zq(Z)
\left[\frac{r(Z)}{q(Z)}-1\right]\\
&=\sum_Zr(Z)-\sum_Zq(Z)=0.
\end{aligned}
$$

Thus the divergence is nonnegative, with equality only when the distributions agree.

Let the M step produce parameters satisfying

$$
Q(\theta_{t+1}\mid\theta_t)
\geq Q(\theta_t\mid\theta_t).
$$

The entropy is unchanged during this step. Therefore

$$
\begin{aligned}
\ell(\theta_{t+1})
&\geq F_t(\theta_{t+1})\\
&\geq F_t(\theta_t)\\
&=\ell(\theta_t).
\end{aligned}
$$

The first inequality is the lower-bound property, the second is the M-step improvement, and the equality is exact posterior matching in the E step.

An equivalent proof subtracts the two exact decompositions:

$$
\boxed{
\ell(\theta_{t+1})-\ell(\theta_t)
=
Q(\theta_{t+1}\mid\theta_t)
-Q(\theta_t\mid\theta_t)
+
\operatorname{KL}(q_t\Vert q_{t+1})
}.
$$

Both terms on the right are nonnegative under the stated update. The direction of the divergence is old posterior to new posterior.

Likelihood equality requires both no improvement in the auxiliary objective and no change in the posterior. Conversely, strictly increasing the auxiliary objective guarantees a strict likelihood increase. Full maximization is sufficient but unnecessary: any step that increases the same auxiliary objective has the monotonicity property. This is the basis of generalized EM.

## Derive the Gaussian-mixture M step

Define the effective counts

$$
N_k=\sum_n\gamma_{nk}^{(t)},
\qquad
\sum_kN_k=N.
$$

The mixing-weight part of the auxiliary objective is

$$
\sum_kN_k\log\pi_k.
$$

With a multiplier for the sum constraint,

$$
\mathcal J
=
\sum_kN_k\log\pi_k
-\lambda\left(\sum_k\pi_k-1\right).
$$

Differentiation gives

$$
\frac{N_k}{\pi_k}-\lambda=0.
$$

Summing the implied equations yields the multiplier and update:

$$
\lambda=N,
\qquad
\pi_k^{(t+1)}=\frac{N_k}{N}.
$$

For the mean, the relevant derivative is

$$
\nabla_{\mu_k}Q
=
\Sigma_k^{-1}
\sum_n\gamma_{nk}^{(t)}(x_n-\mu_k).
$$

Assuming a positive effective count and invertible covariance,

$$
\mu_k^{(t+1)}
=
\frac1{N_k}\sum_n\gamma_{nk}^{(t)}x_n.
$$

To derive the covariance, centre the residuals at this new mean and define

$$
S_k
=
\sum_n\gamma_{nk}^{(t)}
(x_n-\mu_k^{(t+1)})
(x_n-\mu_k^{(t+1)})^\top.
$$

Using precision $$\Lambda_k=\Sigma_k^{-1}$$, the remaining component objective is

$$
Q_k
=
\frac{N_k}{2}\log|\Lambda_k|
-\frac12\operatorname{tr}(\Lambda_kS_k)
+\text{constant}.
$$

The differential is

$$
dQ_k
=
\frac12\operatorname{tr}
\left[
(N_k\Lambda_k^{-1}-S_k)d\Lambda_k
\right].
$$

It vanishes when

$$
\Sigma_k^{(t+1)}=\frac{S_k}{N_k}.
$$

The log-determinant differential used here is derived in [Clustering and mixture models](/study/clustering-and-mixture-models/).

The responsibilities stay fixed throughout all these updates, while the residuals in the covariance use the new mean. A zero effective count makes the mean formula undefined. A singular weighted scatter places the covariance outside the nonsingular model. These cases require a stated constraint, prior, or component-handling rule rather than silent division or matrix inversion.

## Work through one complete numerical iteration

Construct a one-dimensional dataset:

$$
x=(-2,0,2).
$$

Use two components with old parameters

$$
\pi_1=\pi_2=\frac12,
\qquad
\mu_1=-1,\quad\mu_2=1,
\qquad
\sigma_1^2=\sigma_2^2=1.
$$

All numbers below are calculated from this construction. Decimal displays are rounded; the updates use the underlying unrounded values.

### E step

The common normalization and mixing weights cancel in the posterior odds:

$$
\begin{aligned}
\log\frac{\gamma_1(x)}{\gamma_2(x)}
&=
-\frac12\left[(x+1)^2-(x-1)^2\right]\\
&=-2x.
\end{aligned}
$$

Therefore

$$
\gamma_1(x)=\frac1{1+\exp(2x)},
\qquad
\gamma_2(x)=1-\gamma_1(x).
$$

| Observation | First responsibility | Second responsibility |
|---|---:|---:|
| $$-2$$ | $$0.982013790$$ | $$0.017986210$$ |
| $$0$$ | $$0.500000000$$ | $$0.500000000$$ |
| $$2$$ | $$0.017986210$$ | $$0.982013790$$ |

Each row sums to one. By symmetry, both effective counts are

$$
N_1=N_2=1.5.
$$

### M step

Let

$$
a=\frac1{1+e^{-4}},
\qquad
b=1-a.
$$

The new first mean is

$$
\mu_1^{\mathrm{new}}
=
\frac{(-2)a+0(1/2)+2b}{1.5}
\approx-1.285370107.
$$

The other mean is its negative. Both new mixing weights remain one half.

For a transparent variance calculation, expand weighted squared residuals around the weighted mean:

$$
\frac1{N_k}\sum_n\gamma_{nk}(x_n-\mu_k)^2
=
\frac1{N_k}\sum_n\gamma_{nk}x_n^2-\mu_k^2.
$$

The cross term simplifies because the weighted observations sum to the effective count times the new mean. For the first component,

$$
\frac{4a+0+4b}{1.5}=\frac83.
$$

Thus

$$
(\sigma_1^2)^{\mathrm{new}}
=
\frac83-(1.285370107\ldots)^2
\approx1.014490355.
$$

Symmetry gives the same variance for the second component. This completes one full update of weights, means, and variances.

### Evaluate the observed likelihood

For means of equal magnitude, common variance, and equal weights, each observation has density

$$
p(x)
=
\frac{
\exp[-(x+m)^2/(2v)]
+
\exp[-(x-m)^2/(2v)]
}{
2\sqrt{2\pi v}
}.
$$

Use the old pair $$m=1,\ v=1$$ and the new values just computed.

| Observation | Old density | New density |
|---|---:|---:|
| $$-2$$ | $$0.123201286$$ | $$0.154941971$$ |
| $$0$$ | $$0.241970725$$ | $$0.175446603$$ |
| $$2$$ | $$0.123201286$$ | $$0.154941971$$ |

Taking logarithms and adding,

$$
\begin{aligned}
\ell_{\mathrm{old}}
&=
2\log(0.123201286\ldots)
+\log(0.241970725\ldots)\\
&\approx-5.606810105,\\
\ell_{\mathrm{new}}
&=
2\log(0.154941971\ldots)
+\log(0.175446603\ldots)\\
&\approx-5.469829761.
\end{aligned}
$$

The increase is

$$
\Delta\ell\approx0.136980343.
$$

The centre observation became less likely. EM guarantees improvement of the total likelihood, not the density of each observation separately.

### Check the exact improvement identity

For this example, evaluate the auxiliary objective directly:

$$
Q(\theta\mid\theta_{\mathrm{old}})
=
\sum_{n,k}\gamma_{nk}^{\mathrm{old}}
\left[
\log\pi_k
-\frac12\log(2\pi\sigma_k^2)
-\frac{(x_n-\mu_k)^2}{2\sigma_k^2}
\right].
$$

Substitution gives

$$
Q_{\mathrm{old}}\approx-6.480146821,
\qquad
Q_{\mathrm{new}}\approx-6.357836701.
$$

The new first-component responsibility at the left endpoint is

$$
\frac1{1+\exp[-4m/v]}
\approx0.993744647.
$$

The middle responsibility remains one half; the right endpoint is symmetric. If

$$
c=0.993744647\ldots,
$$

the posterior divergence over the whole dataset is

$$
\operatorname{KL}(q_{\mathrm{old}}\Vert q_{\mathrm{new}})
=
2\left[
a\log\frac ac+b\log\frac b{1-c}
\right]
\approx0.014670224.
$$

The factor two accounts for the two endpoints; the middle point contributes zero. Consequently,

$$
\Delta Q+\operatorname{KL}
\approx
0.122310120+0.014670224
=
0.136980344.
$$

This agrees with the observed likelihood increase to rounding precision. The example checks the sign and magnitude of every term in the proof.

## What convergence of the objective actually means

Suppose the nondecreasing likelihood sequence is bounded above. Let its supremum be $$L$$. For every positive tolerance, some iteration lies within that tolerance of the supremum. Every later iterate is at least as large and cannot exceed it. This proves

$$
\ell(\theta_t)\longrightarrow L.
$$

That is convergence of a sequence of numbers. It does not prove convergence of the parameter vectors. Different parameters can represent the same density, and flat or nonidentifiable directions need not settle.

Even if the parameters do converge, the limit need not be a local maximum. Under additional smoothness and interior-limit conditions, an exact EM fixed point satisfies

$$
\nabla_\theta Q(\theta\mid\theta_*)\big|_{\theta=\theta_*}=0.
$$

The likelihood-gradient identity then implies

$$
\nabla_\theta\ell(\theta_*)=0.
$$

A zero gradient identifies a stationary point, not its type. Boundary points require their own constrained analysis. More general convergence claims require regularity conditions beyond the monotonicity argument.

### An exact EM fixed point that is not a good solution

Take observations at $$-3$$ and $$3$$. Fix both component variances to one and both mixing weights to one half. Initialize both means at zero.

The components are identical, so every responsibility is one half. Each weighted mean update returns zero. Exact EM stays there.

At these parameters,

$$
\ell_0=-\log(2\pi)-9.
$$

Instead put the means at the two observations. Each observation then has density

$$
\frac{1+e^{-18}}{2\sqrt{2\pi}},
$$

giving

$$
\ell_{\mathrm{split}}
=
-\log(2\pi)-2\log2+2\log(1+e^{-18}).
$$

The difference is

$$
\ell_{\mathrm{split}}-\ell_0
=
9-2\log2+2\log(1+e^{-18})>0.
$$

To inspect the stationary point locally, place the means at $$-m$$ and $$m$$. The likelihood along this path is

$$
\ell(m)
=
-\log(2\pi)-9-m^2+2\log\cosh(3m).
$$

This follows by factoring the Gaussian exponential and using

$$
\cosh u=\frac{e^u+e^{-u}}2.
$$

The second derivative at zero is

$$
\ell''(0)=-2+18=16>0.
$$

So the fixed point is locally uphill in the splitting direction. It is not a local maximum. Symmetric initialization can keep exact EM at such a point without violating monotonicity.

## Why unrestricted mixtures may have no finite likelihood limit

A Gaussian density is not bounded above by one. In particular, a component centred exactly at an observed point has density

$$
\mathcal N(x_1\mid x_1,\delta^2I)
=
(2\pi\delta^2)^{-d/2}.
$$

Give this component a fixed positive weight and let its variance approach zero. Its contribution to the density at that observation diverges. Keep another nonsingular component with positive weight fixed, so all remaining observations retain positive density.

The total log-likelihood can then approach positive infinity. Monotonicity alone cannot promise a finite objective limit for this unconstrained model.

A positive covariance lower bound removes this particular collapse. A prior or penalty can change the optimization problem so that concentrating on a single point is unattractive. These choices must be reflected in the M step and the monitored objective. Adding arbitrary covariance jitter after an unconstrained update is not automatically an exact maximization of the original auxiliary function.

## Which algorithm changes preserve the proof?

Generalized EM preserves the proof if it uses the exact old posterior and increases the same auxiliary objective. A numerical optimizer does not need to reach the global M-step maximum to achieve this.

A variational E step may leave a positive gap at the old parameters. Raising that loose bound need not raise the observed likelihood. A hard assignment generally has the same problem. Monte Carlo estimates can introduce sampling error into the expected objective, so an estimated improvement is not automatically a true one.

MAP EM adds a parameter-prior term to the M-step objective. The analogous proof then concerns the observed log posterior, including that prior. It need not make the unpenalized likelihood monotone.

For implementation, compute densities in log space. If component log scores are $$a_k$$ and their maximum is $$a_*$$, then

$$
\log\sum_ke^{a_k}
=
a_*+\log\sum_ke^{a_k-a_*}.
$$

This is an exact algebraic rearrangement that avoids exponentiating large positive scores. Responsibilities use the normalized exponentials. Monitor the observed log-likelihood with the same model and constraints after each iteration; do not confuse it with the auxiliary objective, whose posterior weights change between iterations.

A small likelihood increment is a stopping criterion, not a bound on distance to an optimum. The objective can change little along a weakly identified direction while parameters or responsibilities still move. Record the stopping rule and inspect effective counts and covariance behaviour alongside the objective. If a likelihood decrease appears, first distinguish floating-point error from an update that no longer maximizes the stated auxiliary function.

Multiple initializations can reveal different solutions. They provide a comparison among the runs performed, not a certificate that the global optimum has been found.

## Revision checklist

| Can I reconstruct this without looking? | Check |
|---|---|
| Which parameters determine the E-step distribution? | The old parameters only. |
| Why is holding responsibilities fixed valid? | They define the expectation in the auxiliary objective. |
| Where does the bound meet the likelihood? | At the old parameters after an exact E step. |
| What is the exact likelihood-improvement identity? | Auxiliary improvement plus KL from old to new posterior. |
| Is full M-step maximization necessary? | No; increasing the same auxiliary objective suffices. |
| Which mean belongs in the covariance update? | The newly updated weighted mean. |
| Does every observation become more likely? | No; the constructed middle observation became less likely. |
| When do monotone objective values have a finite limit? | When they are bounded above. |
| Can an EM fixed point fail to be a local maximum? | Yes; identical means in the symmetric construction do so. |
| Why can Gaussian-mixture likelihood diverge? | A component covariance can collapse onto one observation. |
| Does variational EM inherit exact likelihood monotonicity? | Not from ELBO improvement alone. |

## Why it matters for my work

A monotone fitting trace verifies an optimization property under stated assumptions. It does not validate recovered subpopulations. I should report sensitivity to initialization and covariance constraints alongside any interpretation of mixture components.

## What I have not resolved

Which comparisons across restarts would distinguish interchangeable labels, near-equivalent densities, and materially different explanations of acquisition variation?
