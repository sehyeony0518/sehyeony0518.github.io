---
layout: study_note
title: "Clustering and Mixture Models: k-means, GMM, and the Log of a Sum"
description: "Hard assignment by alternating minimisation, soft assignment by a density, and the structural reason the mixture likelihood cannot be solved by differentiating."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "probability-and-inference"
category_title: "Probability & Statistical Inference"
order: 9
source: "Independent study"
written: true
updated: "2026-09-15"
---

Given points and no labels, the task is to say which belong together. The answer can be a hard assignment or a distribution over assignments, and the difference between those two is also the difference between a procedure that has a closed form and one that does not.

## Core question and definition

**Hard clustering** gives each point one label. **Soft clustering** gives each point a distribution over labels — 0.8 to one cluster, 0.2 to another — which is strictly more information and reduces to the hard version by taking the maximum.

k-means produces the first. A Gaussian mixture produces the second, and produces something else besides: a density, from which new points can be drawn.

## Key concepts

### k-means is alternating minimisation, and each step is a one-liner

With binary indicators $$r_{nk} \in \{0,1\}$$ saying whether point $$n$$ belongs to cluster $$k$$, the objective is total squared distance to the assigned centre:

$$
J = \sum_n \sum_k r_{nk}\,\lVert x_n - \mu_k\rVert^2 .
$$

Two unknowns, and neither is solvable with the other free — the same structure as any latent-variable problem. So fix one and solve for the other, alternately.

Holding the centres fixed, $$J$$ is linear in the indicators, so each point independently takes its nearest centre. Holding the assignments fixed, differentiating and setting to zero gives

$$
\mu_k = \frac{\sum_n r_{nk}x_n}{\sum_n r_{nk}},
$$

the mean of the points assigned to $$k$$ — which is where the name comes from. [Lloyd](https://doi.org/10.1109/TIT.1982.1056489) (1982) gave the standard form.

Each step cannot increase $$J$$, so the procedure converges. It converges to a local optimum, which is why it is run from several initialisations, and it is only as good as squared distance is as a notion of similarity.

### Maximum likelihood for one Gaussian has a closed form

Before mixtures, the single-component case. With $$x_1,\dots,x_N$$ assumed drawn independently from $$\mathcal{N}(\mu,\Sigma)$$, the log-likelihood is a sum, and differentiating with respect to $$\mu$$ gives the sample mean immediately.

The covariance takes more work — it needs the derivatives of $$\log\det$$ and of a quadratic form, and is easier in terms of $$\Sigma^{-1}$$ — but it comes out as

$$
\hat\Sigma = \frac{1}{N}\sum_n (x_n - \hat\mu)(x_n - \hat\mu)^\top .
$$

Note the $$1/N$$. This is the **biased** estimator: its expectation is $$\frac{N-1}{N}\Sigma$$, so it systematically underestimates spread. That is not an error in the derivation. Maximum likelihood optimises a stated criterion and unbiasedness is a different criterion, so getting a biased answer is the method working as specified. The bias vanishes as $$N$$ grows, and matters when it is small.

### The mixture likelihood is a log of a sum, and that is the whole obstacle

A mixture density is a weighted sum of components,

$$
p(x) = \sum_{k=1}^{K} \alpha_k \,\mathcal{N}(x \mid \mu_k, \Sigma_k),
\qquad \alpha_k \ge 0,\ \sum_k \alpha_k = 1,
$$

and the log-likelihood over the dataset is

$$
\sum_n \log \sum_k \alpha_k\, \mathcal{N}(x_n \mid \mu_k, \Sigma_k).
$$

The logarithm no longer meets the exponential of each Gaussian, because a sum sits between them. Differentiating gives equations in which every parameter appears inside every term, and setting them to zero does not separate.

This is the structural reason [EM](/study/latent-variables-em-and-variational-inference/) exists. The single-Gaussian case was tractable because there was no sum to get past; introducing a latent variable saying which component produced each point restores that, at the cost of not knowing its value.

### What a mixture buys beyond clusters

Any distribution a single Gaussian cannot describe — two peaks, a long tail, a mixed population — can be approximated by enough components. The framing worth keeping is not that data *is* a mixture of Gaussians but that a mixture is a flexible approximation to a density that is something else.

Because it is a density, it also generates: sample a component by its weight, then sample from that component. Clustering is one use of the fitted model rather than its definition.

## Where this touches my work

The unmodelled-mixture idea is the one I keep coming back to. A clinical cohort is rarely one population — scanner, operator, referral route, disease severity all partition it, and none of those are recorded as labels. A model fitted to the pooled data fits the mixture, and a subgroup that behaves differently is a component nobody named.

The biased-covariance result is a smaller but sharper caution. Maximum likelihood answers the question posed and not a neighbouring one, and a reported spread estimated this way is systematically too small on a small subgroup — which is exactly where subgroup analyses are thinnest.

## What I have not resolved

Whether fitting a mixture to a clinical dataset would recover components that mean anything, or whether it would recover site labels I already have, in which case the exercise has cost more than it returned.

## References

- Lloyd (1982). [Least squares quantization in PCM](https://doi.org/10.1109/TIT.1982.1056489). *IEEE Trans. Information Theory*.
- Dempster, Laird & Rubin (1977). [Maximum Likelihood from Incomplete Data via the EM Algorithm](https://doi.org/10.1111/j.2517-6161.1977.tb01600.x). *JRSS B*.
