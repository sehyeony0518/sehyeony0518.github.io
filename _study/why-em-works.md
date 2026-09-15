---
layout: study_note
title: "Why EM Works: Responsibilities, the Q Function, and the Monotonicity Guarantee"
description: "The latent-variable construction of a mixture, the update equations that fall out of it, and the argument that each iteration cannot make the likelihood worse."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "math-foundations"
category_title: "Mathematical & Statistical Foundations"
order: 17
source: "Independent study"
written: true
updated: "2026-09-15"
---

The [mixture likelihood is a log of a sum](/study/clustering-and-mixture-models/) and cannot be differentiated into a solution. EM gets around this, and the way it does so is worth following in full, because the guarantee it provides is narrower than it is usually described as being.

## Core question and definition

Introduce a latent one-hot variable $$\mathbf{z}$$ naming which component produced each point. Then

$$
p(\mathbf{z}) = \prod_k \pi_k^{z_k}, \qquad
p(\mathbf{x}\mid\mathbf{z}) = \prod_k \mathcal{N}(\mathbf{x}\mid\mu_k,\Sigma_k)^{z_k},
$$

which look elaborate but are just compact ways of writing "if $$z_k=1$$ then this component, otherwise nothing". Summing the joint over every value of $$\mathbf{z}$$ returns the mixture, so nothing has been changed about the model — only about how it is described.

The point of the description is that the **complete-data** log-likelihood, where $$\mathbf{z}$$ is known, has the logarithm meeting the exponentials directly, with no sum in between. It would be easy. The trouble is that $$\mathbf{z}$$ is not observed.

## Key concepts

### Responsibilities are a posterior over the latent variable

Given a point and the current parameters, Bayes gives the probability it came from component $$k$$:

$$
\gamma(z_{nk}) = \frac{\pi_k\,\mathcal{N}(x_n\mid\mu_k,\Sigma_k)}{\sum_j \pi_j\,\mathcal{N}(x_n\mid\mu_j,\Sigma_j)}.
$$

This is the **responsibility** component $$k$$ takes for point $$n$$ — a soft membership. If these were known, the problem would be over: each component's mean and covariance would be the weighted mean and covariance of the points it is responsible for.

### The update equations, derived by ignoring a dependence

Differentiating the log-likelihood with respect to $$\mu_k$$ produces exactly the responsibility expression, and then the derivation does something indefensible: it treats $$\gamma$$ as a constant, though it plainly depends on the parameters being solved for. Under that pretence the equations rearrange into

$$
\mu_k = \frac{1}{N_k}\sum_n \gamma(z_{nk})\,x_n,
\qquad
N_k = \sum_n \gamma(z_{nk}),
$$

and the covariance follows the same weighted form. The mixing weights need a Lagrange multiplier to enforce $$\sum_k \pi_k = 1$$, and give $$\pi_k = N_k/N$$.

All three read naturally: $$N_k$$ is the effective number of points component $$k$$ is responsible for, and each parameter is that component's weighted statistic. The lecture is candid that the derivation is not valid as reasoning — it is a way of arriving at the right answer, which a separate argument then justifies.

### The Q function states what is actually being maximised

Since $$\mathbf{z}$$ is unavailable, average the complete-data log-likelihood over the posterior implied by the current parameters:

$$
Q(\theta, \theta^{\text{old}}) = \mathbb{E}_{\mathbf{z}\mid\mathbf{x},\theta^{\text{old}}}\!\left[\log p(\mathbf{x},\mathbf{z}\mid\theta)\right].
$$

The **E-step** computes this expectation; the **M-step** maximises it over $$\theta$$. That is the whole algorithm, and it raises the obvious objection: the thing being maximised is not the thing that was wanted.

### The guarantee, and the size of it

The answer is that improving $$Q$$ cannot worsen the actual log-likelihood. The argument rests on one inequality — that for distributions $$p$$ and $$q$$,

$$
\sum p \log p \;\ge\; \sum p \log q,
$$

which follows from $$\log x \le x - 1$$ and is the non-negativity of the KL divergence. Applying it to the posterior over $$\mathbf{z}$$ under the old and new parameters, the difference in log-likelihood decomposes into the change in $$Q$$, which the M-step made non-negative, plus a KL term, which is non-negative by the inequality. So the likelihood does not decrease.

What that buys is precisely: monotonic non-decrease, hence convergence to a **local** optimum. It is not a global guarantee, and no practical method offers one here. [Wu](https://doi.org/10.1214/aos/1176346060) (1983) examined the convergence properties carefully, since the original statement was stronger than what holds.

### The combinatorial argument for why nothing simpler works

It is fair to ask why the latent variable is not simply summed away. With $$K$$ components and $$N$$ points the sum runs over $$K^N$$ configurations. Eighty binary latent variables give $$2^{80}$$ terms; at a hundred billion additions per second that is millions of years. A thousand-by-thousand binary image has $$2^{10^6}$$.

So the intractability is not a matter of cleverness. Any workable method has to avoid that sum, and introducing the latent variable explicitly is how EM does it.

## Where this touches my work

The local-optimum result is the part that matters to me. A mixture fitted to a clinical cohort depends on its initialisation, so the components it recovers are one of many possible answers and not a discovered structure. Reporting them as though they were subpopulations found in the data overstates what the procedure can deliver.

The responsibilities are the more useful object. A soft membership says how ambiguous a point is between components, and a point split near-evenly is one the model cannot place. If those components corresponded to something real — acquisition setting, say — that ambiguity would be worth examining directly, and it is a quantity the fitting procedure produces for free.

## What I have not resolved

Whether the sensitivity to initialisation can be characterised well enough to report — running many restarts and describing the spread of solutions — or whether the spread would simply be too large for any of it to mean anything.

## References

- Dempster, Laird & Rubin (1977). [Maximum Likelihood from Incomplete Data via the EM Algorithm](https://doi.org/10.1111/j.2517-6161.1977.tb01600.x). *JRSS B*.
- Wu (1983). [On the Convergence Properties of the EM Algorithm](https://doi.org/10.1214/aos/1176346060). *Annals of Statistics*.
