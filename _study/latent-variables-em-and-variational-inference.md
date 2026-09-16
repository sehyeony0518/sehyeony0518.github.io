---
layout: study_note
title: "Latent Variables: EM and Variational Inference"
description: "What to do when neither the parameter nor the variable that produced the data was observed, and why the posterior usually has to be approximated rather than computed."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "probability-and-inference"
category_title: "Probability & Statistical Inference"
order: 10
source: "Independent study"
written: true
updated: "2026-09-15"
---

A latent-variable model describes observations through quantities that were not observed. In a mixture, the missing quantity is a component label. In an image model, it might be a clean image or a lower-dimensional representation. The task has two parts: infer those hidden quantities under a model, and estimate whatever model parameters are unknown.

EM and variational inference organise these tasks around the same function: the evidence lower bound, or ELBO. The central distinction is whether the required posterior can be represented and computed exactly. It is not a distinction between fixed and random parameters. Variational inference can approximate latent-variable posteriors while keeping model parameters as point estimates.

## Separate the model, posterior inference, and parameter estimation

Write the model as

$$
p_\theta(x,z)=p_\theta(z)p_\theta(x\mid z).
$$

Here $$x$$ is observed, $$z$$ is latent, and $$\theta$$ denotes model parameters. For now, the parameters are fixed when computing a posterior:

$$
p_\theta(z\mid x)
=
\frac{p_\theta(x,z)}{p_\theta(x)},
\qquad
p_\theta(x)=\sum_zp_\theta(x,z).
$$

For continuous latent variables, replace the sum by an integral. The marginal quantity is often called the evidence. With parameters fixed, this means integrating out the latent variables, not necessarily integrating over parameters.

Parameter estimation is another operation:

$$
\widehat\theta
\in\arg\max_\theta\log p_\theta(x).
$$

A Bayesian treatment adds a parameter prior and targets a larger posterior:

$$
p(\theta,z\mid x)
\propto p_\theta(x,z)p(\theta).
$$

Both models can require approximate inference. Conversely, some Bayesian posteriors are available analytically. The following distinctions keep the roles separate.

| Procedure | Treatment of model parameters | Distribution over latent variables |
|---|---|---|
| Ordinary maximum-likelihood EM | Optimised as a point | Exact conditional posterior in the E step |
| Variational EM | Usually optimised as a point | Optimised within a chosen family |
| Bayesian variational inference | Included among uncertain quantities | Approximation to a joint posterior |
| MAP EM | Optimised with a parameter-prior term | Exact conditional posterior in an ordinary E step |

EM itself does not produce a posterior distribution over the fitted parameters. That does not prevent a separate frequentist uncertainty analysis. Likewise, using a distribution over latent variables does not by itself make parameter estimation Bayesian.

## A latent sum is not automatically intractable

For an ordinary independent-observation mixture, the joint distribution factorises:

$$
p_\theta(X,Z)
=
\prod_{n=1}^N p_\theta(x_n,z_n).
$$

Distributing sums over the product gives

$$
\sum_{z_1,\ldots,z_N}
\prod_n p_\theta(x_n,z_n)
=
\prod_n\sum_{z_n}p_\theta(x_n,z_n).
$$

There may be $$K^N$$ label configurations, but this calculation needs only $$NK$$ component terms, apart from the cost of evaluating their densities. The posterior over labels also factorises at fixed parameters.

The mixture's difficulty is therefore usually optimisation of the log of a sum, not evaluation of an exponential-size sum.

Other models have coupled latent variables or continuous integrals without a useful analytic form. Even then, counting configurations is not a proof of computational difficulty: a chain can admit efficient dynamic programming. What matters is whether the model's dependence structure allows the relevant sums, integrals, or expectations to be simplified.

EM is useful when complete-data expectations and parameter updates are manageable. It does not automatically make an arbitrary posterior tractable.

## First derivation: introduce a distribution and apply Jensen

Fix the observation and parameters. Choose a normalised auxiliary distribution $$q(z)$$. Initially assume it is positive wherever the joint density is positive, and that the expectations below are finite. Insert the cancelling factor:

$$
p_\theta(x)
=
\sum_z q(z)\frac{p_\theta(x,z)}{q(z)}
=
\mathbb E_q\left[
\frac{p_\theta(x,z)}{q(z)}
\right].
$$

The logarithm is concave. To check the direction of Jensen's inequality, take a positive random quantity $$Y$$ with finite positive mean. The scalar inequality

$$
\log u\leq u-1
$$

follows by considering

$$
g(u)=u-1-\log u,
\qquad
g'(u)=1-\frac1u.
$$

The derivative changes from negative to positive at one, where the function is zero. Applying this inequality to the ratio of the random quantity to its mean gives

$$
\mathbb E\left[
\log\frac{Y}{\mathbb E[Y]}
\right]
\leq
\mathbb E\left[
\frac{Y}{\mathbb E[Y]}-1
\right]=0.
$$

Rearranging,

$$
\mathbb E[\log Y]\leq\log\mathbb E[Y].
$$

Use the joint-density ratio as this random quantity:

$$
\log p_\theta(x)
\geq
\mathbb E_q\left[
\log\frac{p_\theta(x,z)}{q(z)}
\right].
$$

Define the right-hand side:

$$
\mathcal L(q,\theta)
=
\mathbb E_q[\log p_\theta(x,z)]
-\mathbb E_q[\log q(z)].
$$

For discrete variables, the second term is the entropy:

$$
H(q)=-\sum_zq(z)\log q(z).
$$

Thus the ELBO is expected complete-data log probability plus entropy. The entropy term is not an optional regulariser attached after the derivation. It appears because inserting the auxiliary distribution requires dividing by it inside the logarithm.

Why does equality matter? Jensen is tight when the ratio inside the expectation is constant:

$$
\frac{p_\theta(x,z)}{q(z)}=c.
$$

Normalisation determines the constant:

$$
1=\sum_zq(z)
=\frac1c\sum_zp_\theta(x,z)
=\frac{p_\theta(x)}c.
$$

Therefore

$$
c=p_\theta(x),
\qquad
q(z)=p_\theta(z\mid x).
$$

The exact posterior is the distribution that makes the lower bound touch the log evidence.

If the auxiliary distribution omits part of the joint support, the initial expectation equals only the joint mass on its support. One first bounds the full evidence below by that partial mass, then applies Jensen. The ELBO remains a lower bound, but a distribution omitting positive posterior mass cannot make it tight.

## Second derivation: expand the posterior KL divergence

Let $$r(z)=p_\theta(z\mid x)$$. The divergence in the direction used here is

$$
\operatorname{KL}(q\Vert r)
=
\mathbb E_q\left[\log\frac{q(z)}{r(z)}\right].
$$

This direction matters because the expectation is under the distribution we can manipulate and sample from.

For completeness, its nonnegativity follows from the same scalar inequality. If the posterior is positive wherever the auxiliary distribution is positive,

$$
\begin{aligned}
-\operatorname{KL}(q\Vert r)
&=
\sum_{z:q(z)>0}q(z)\log\frac{r(z)}{q(z)}\\
&\leq
\sum_{z:q(z)>0}q(z)
\left[\frac{r(z)}{q(z)}-1\right]\\
&=
\sum_{z:q(z)>0}r(z)-1
\leq0.
\end{aligned}
$$

If the auxiliary distribution assigns mass where the posterior is zero, the divergence is infinite. Otherwise equality requires the distributions to agree, including their support.

Now substitute Bayes' rule into the logarithm:

$$
\log p_\theta(z\mid x)
=
\log p_\theta(x,z)-\log p_\theta(x).
$$

Since the log evidence does not depend on the latent state, its expectation is itself:

$$
\begin{aligned}
\operatorname{KL}(q\Vert p_\theta(z\mid x))
&=
\mathbb E_q[\log q(z)]
-\mathbb E_q[\log p_\theta(x,z)]
+\log p_\theta(x)\\
&=
-\mathcal L(q,\theta)+\log p_\theta(x).
\end{aligned}
$$

Rearranging gives the exact decomposition

$$
\boxed{
\log p_\theta(x)
=
\mathcal L(q,\theta)
+
\operatorname{KL}(q\Vert p_\theta(z\mid x))
}.
$$

For continuous variables, these statements use integrals and require the corresponding density and integrability conditions. The identity should not be manipulated as a subtraction of two infinite quantities.

The Jensen and KL routes have produced exactly the same object: expected log joint density minus expected log auxiliary density. Jensen explains the lower bound and its equality condition. The KL decomposition identifies the exact gap.

At fixed parameters, the log evidence is constant with respect to the auxiliary distribution. Maximising the ELBO therefore minimises this divergence. The evidence is not constant when updating model parameters; dropping it from a parameter optimisation would be a different and invalid step.

## A complete numerical check of the two derivations

Construct a binary observation and a two-state latent variable. Let the latent prior be uniform, with

$$
p(x=1\mid z=A)=0.6,
\qquad
p(x=1\mid z=B)=0.2.
$$

The full joint probability table is then

| Observation | Latent state A | Latent state B | Marginal |
|---|---:|---:|---:|
| $$x=1$$ | $$0.3$$ | $$0.1$$ | $$0.4$$ |
| $$x=0$$ | $$0.2$$ | $$0.4$$ | $$0.6$$ |
| Total | $$0.5$$ | $$0.5$$ | $$1$$ |

Observe $$x=1$$. The posterior is

$$
p(z\mid x=1)=(0.75,0.25).
$$

Start with the auxiliary distribution $$q=(0.5,0.5)$$. All logarithms here are natural. Jensen's construction gives

$$
\begin{aligned}
\mathcal L(q)
&=
\frac12\log\frac{0.3}{0.5}
+\frac12\log\frac{0.1}{0.5}\\
&=
\frac12\log0.6+\frac12\log0.2\\
&\approx-1.060132.
\end{aligned}
$$

The exact log evidence is

$$
\log p(x=1)=\log0.4\approx-0.916291.
$$

The KL gap is

$$
\begin{aligned}
\operatorname{KL}(q\Vert p(z\mid x=1))
&=
\frac12\log\frac{0.5}{0.75}
+\frac12\log\frac{0.5}{0.25}\\
&=
\frac12\log\frac43\\
&\approx0.143841.
\end{aligned}
$$

Adding the ELBO and gap recovers the log evidence, up to rounding:

$$
-1.060132+0.143841=-0.916291.
$$

Now perform an exact E step by setting the auxiliary distribution to the posterior. Both joint-density ratios become the same:

$$
\frac{0.3}{0.75}=0.4,
\qquad
\frac{0.1}{0.25}=0.4.
$$

Jensen is tight, the KL gap is zero, and the ELBO equals the log evidence. No parameter changed during this operation. The E step improved the representation of the current model's posterior, not the model's likelihood.

A hard assignment to state A instead gives

$$
q=(1,0),
\qquad
\mathcal L(q)=\log0.3\approx-1.203973.
$$

Its gap is

$$
\log0.4-\log0.3=\log\frac43>0.
$$

Choosing the most probable latent state is consequently not the same operation as the exact E step.

## What the E and M steps do in each view

For a dataset, regard all observations as $$X$$ and all latent variables as $$Z$$. At iteration $$t$$, exact EM sets

$$
q_t(Z)=p_{\theta_t}(Z\mid X).
$$

In the Jensen view, this makes the bound tight at the current parameters. In the KL view, it makes the posterior-approximation gap zero. These are two descriptions of the same operation.

The M step holds this distribution fixed:

$$
\theta_{t+1}
\in\arg\max_\theta\mathcal L(q_t,\theta).
$$

Its entropy no longer depends on the candidate parameters, so the same update maximises

$$
Q(\theta\mid\theta_t)
=
\mathbb E_{q_t}[\log p_\theta(X,Z)].
$$

The expectation is of the complete-data log-likelihood. It is generally not obtained by putting the posterior mean of the latent variable into that likelihood.

For example, if a latent Bernoulli variable has mean $$a$$, then

$$
\mathbb E[Z^2]=a,
\qquad
(\mathbb E[Z])^2=a^2.
$$

Replacing a random variable by its mean gives the wrong answer for a quadratic term unless those quantities happen to coincide. In a mixture's complete-data log-likelihood, replacing one-hot indicators by their expectations works because that expression is linear in the indicators.

After the parameter update, the old posterior need not equal the new posterior. The next E step closes that new gap. The [monotonicity proof](/study/why-em-works/) depends on this sequence: touch the objective, raise the bound, and then retighten.

## Variational inference restricts the possible posterior

If the exact posterior is unavailable, choose a family of distributions and solve, ideally,

$$
q^*
\in\arg\max_{q\in\mathcal Q}\mathcal L(q,\theta).
$$

The best achievable gap is

$$
\inf_{q\in\mathcal Q}
\operatorname{KL}(q\Vert p_\theta(z\mid x)).
$$

It is zero only if the posterior can be matched, or approached sufficiently closely, within the family. Optimisation can introduce an additional gap if it stops at a worse member. Representation limits and optimisation failure are different problems.

A common choice is mean-field factorisation:

$$
q(z)=\prod_{j=1}^M q_j(z_j).
$$

This declares the latent coordinates independent under the approximation. It does not assert that the actual posterior is independent.

To derive a coordinate update, hold all factors except one fixed. Define

$$
a_j(z_j)
=
\mathbb E_{q_{-j}}[\log p_\theta(x,z)].
$$

The part of the ELBO depending on this factor is

$$
\mathcal L
=
\int q_j(z_j)a_j(z_j)\,dz_j
-\int q_j(z_j)\log q_j(z_j)\,dz_j
+\text{constant}.
$$

Introduce a multiplier for the factor's normalisation and differentiate with respect to its value at each latent state:

$$
a_j(z_j)-\log q_j(z_j)-1+\lambda=0.
$$

Therefore

$$
q_j^*(z_j)
=
\frac{\exp[a_j(z_j)]}
{\int\exp[a_j(u)]\,du},
$$

provided the denominator is finite. The expected log joint determines the shape; normalisation determines the remaining constant. This is why the update contains an exponential of an expectation of a logarithm, rather than an expectation of the joint density.

## A Gaussian example of information excluded by factorisation

Suppose a target posterior is a centred bivariate Gaussian with covariance

$$
C=
\begin{pmatrix}
1&\rho\\
\rho&1
\end{pmatrix},
\qquad
|\rho|<1.
$$

Inverting this two-by-two matrix gives

$$
C^{-1}
=
\frac{1}{1-\rho^2}
\begin{pmatrix}
1&-\rho\\
-\rho&1
\end{pmatrix}.
$$

Consequently its log density, apart from a constant, is

$$
-\frac{z_1^2-2\rho z_1z_2+z_2^2}
{2(1-\rho^2)}.
$$

Use a product approximation. Taking the expectation over the second coordinate leaves

$$
\log q_1^*(z_1)
=
-\frac{z_1^2-2\rho z_1m_2}
{2(1-\rho^2)}
+\text{constant},
\qquad
m_2=\mathbb E_{q_2}[z_2].
$$

Completing the square shows that the updated first factor is Gaussian with mean $$\rho m_2$$ and variance $$1-\rho^2$$. The other coordinate has the symmetric update. At a fixed point,

$$
m_1=\rho m_2,
\qquad
m_2=\rho m_1.
$$

Since the correlation magnitude is less than one, both means must be zero.

For a constructed correlation of $$\rho=0.8$$, both approximate marginal variances are

$$
1-0.8^2=0.36,
$$

while both target marginal variances are one. The approximation also sets the cross-covariance to zero. It fits narrower independent distributions because independent draws cannot follow the target's correlated direction.

This example derives a specific uncertainty distortion. It does not prove that every variational family always underestimates every variance. A family containing the full bivariate Gaussian would represent this posterior exactly.

## The same objective in a variational autoencoder

Factor the joint density into a latent prior and observation model:

$$
\begin{aligned}
\mathcal L(q,\theta)
&=
\mathbb E_q[\log p_\theta(x\mid z)]
+\mathbb E_q[\log p_\theta(z)-\log q(z)]\\
&=
\mathbb E_q[\log p_\theta(x\mid z)]
-\operatorname{KL}(q(z)\Vert p_\theta(z)).
\end{aligned}
$$

This is the familiar reconstruction-and-prior form of the ELBO. The first term is a log likelihood, not automatically a squared reconstruction error; its form depends on the observation distribution.

A variational autoencoder uses an encoder to produce an approximate posterior $$q_\phi(z\mid x)$$ and a decoder to specify $$p_\theta(x\mid z)$$. Parameters are commonly point estimates. The probabilistic latent representation therefore does not imply a Bayesian posterior over all network weights.

For a diagonal Gaussian encoder, sampling can be written as

$$
z=m_\phi(x)+s_\phi(x)\odot\epsilon,
\qquad
\epsilon\sim\mathcal N(0,I),
$$

where the scale entries are positive and the product is coordinatewise. Since the noise has zero mean and identity covariance, the resulting latent variable has the encoder's mean and diagonal variance. This separates random sampling from the parameter-dependent transformation, allowing suitable expectations to be differentiated through that transformation.

Sharing one encoder across observations is amortised inference: computation learned across the dataset replaces a separate unrestricted posterior optimisation for each case. The shared map can introduce an additional restriction.

Variational EM and autoencoder training can improve an ELBO without increasing the exact observed likelihood at every update. The KL gap can change with the parameters. The exact EM guarantee requires the bound to touch the old likelihood, not merely to lie somewhere below it.

## Revision checklist

| Can I reconstruct this without looking? | Check |
|---|---|
| Does variational inference require random model parameters? | No; it can approximate a latent posterior at fixed parameters. |
| Why insert an auxiliary distribution? | It rewrites marginalisation as an expectation to which Jensen applies. |
| Which way does Jensen point for a logarithm? | Expected log is at most log expectation. |
| Where does the entropy term come from? | The auxiliary distribution appears in the denominator inside the log. |
| What distribution makes the bound tight? | The exact conditional posterior. |
| What does the posterior KL measure? | The exact gap between log evidence and ELBO. |
| What changes in an E step? | The auxiliary distribution, with model parameters held fixed. |
| Why is posterior-mean substitution generally wrong? | Expectation does not commute with nonlinear functions. |
| How is a mean-field coordinate updated? | Exponentiate the expected log joint and normalise. |
| What did the correlated Gaussian example lose? | Cross-covariance and part of the marginal variance. |
| Why is an improving ELBO insufficient for exact likelihood monotonicity? | The posterior KL gap can also change. |

## Why it matters for my work

A latent explanation of acquisition variation depends on both the generative assumptions and the posterior family. I should distinguish uncertainty excluded by the approximation from uncertainty absent under the model.

## What I have not resolved

Which posterior dependencies would matter for an acquisition audit, and whether a tractable approximation would preserve them well enough to support the intended conclusions?
