---
layout: study_note
title: "Latent Variables: EM and Variational Inference"
description: "What to do when neither the parameter nor the variable that produced the data was observed, and why the posterior usually has to be approximated rather than computed."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "probability-and-inference"
category_title: "Probability & Statistical Inference"
order: 10
source: "Independent study"
written: true
updated: "2026-09-15"
---

When a parameter is unknown, maximum likelihood applies. When both the parameter and a variable it generated are unknown, neither is identified without the other, and the methods that handle this are the ones underneath mixture models, the variational autoencoder, and most modern generative modelling.

## Core question and definition

A latent variable is one the model posits but the data does not contain. Written out, the observed likelihood requires summing it away:

$$
p(x \mid \theta) = \sum_{z} p(x, z \mid \theta),
$$

and that sum is what makes the problem hard. Maximising a log of a sum has none of the convenience that maximising a sum of logs had.

The distinction from the [previous note](/study/estimation-likelihood-and-posterior/) is whether $$\theta$$ is treated as a fixed unknown or as a random variable. **EM** takes it as fixed and estimates a point. **Variational methods** take it as random and approximate a distribution. That is the whole of the difference, and it decides what the output means.

## Key concepts

### EM alternates between filling in and re-fitting

If the latent values were known, estimating $$\theta$$ would be ordinary maximum likelihood. If $$\theta$$ were known, the latent values would follow from the posterior. Neither is known, so each is held fixed in turn.

The **E-step** fixes $$\theta$$ and computes the posterior over the latent variable — for a Gaussian mixture, the responsibility of each component for each sample, which in practice is a table of soft assignments. The **M-step** treats those as if observed and re-estimates $$\theta$$ by maximum likelihood.

The Gaussian mixture is the case worth writing out by hand, because everything stays in closed form and the table makes the E-step concrete: which component produced this point, expressed as a probability rather than a label. [Dempster, Laird and Rubin](https://doi.org/10.1111/j.2517-6161.1977.tb01600.x) (1977) gave the general treatment.

What EM returns is a point estimate of $$\theta$$ and a distribution over $$z$$. It does not report uncertainty about $$\theta$$, because it never treated $$\theta$$ as uncertain.

### The posterior is intractable for the same reason every time

Taking $$\theta$$ as random requires the posterior, and the posterior requires the normalising constant — the integral over everything unknown. With a handful of binary latent variables this is a sum over $$2^n$$ configurations. A hundred of them is not a large model, and the sum is already out of reach.

So the problem is not that the mathematics is unavailable. It is available and cannot be evaluated.

### Variational inference gives up exactness to keep tractability

Rather than compute $$p(z \mid x)$$, choose a family $$\mathcal{Q}$$ that can be handled — often factorised, often Gaussian — and find the member closest to the true posterior:

$$
q^\star = \arg\min_{q \in \mathcal{Q}} \; \mathrm{KL}\!\left(q(z) \,\|\, p(z \mid x)\right).
$$

This converts an integration problem into an optimisation problem, which is the move worth remembering. [Blei, Kucukelbir and McAuliffe](https://doi.org/10.1080/01621459.2017.1285773) (2017) review it for statisticians.

The cost is stated plainly: the answer is the nearest element of the family chosen, and a posterior outside that family cannot be represented no matter how well the optimisation runs. A factorised $$q$$ cannot express correlation between latent dimensions; that correlation is not lost in the noise, it is excluded by construction.

This is also the machinery under the variational autoencoder, where an encoder maps an input to a distribution over a latent space rather than to a point, and a decoder maps back. Sampling a two-dimensional latent space and decoding each point is the clearest demonstration that the space has structure.

### EM and variational methods are not opposed

EM's E-step needs a posterior over $$z$$. When that posterior is itself intractable, it can be approximated variationally, and the result is variational EM. The two are separated by what they treat as random, not by being alternatives.

## Where this touches my work

The mixture model is the honest version of a suspicion I have about clinical datasets: that a labelled cohort is a mixture of subpopulations that were never recorded — scanner, operator, referral route — and that a model fits the mixture rather than the disease. EM says what it would take to recover those components, and also what it would cost: a model of how many there are, which is exactly the thing nobody knows.

The variational bargain has a direct analogue in auditing. Choosing a tractable family and reporting the nearest member is what any audit does when it enumerates candidate explanations. The failure mode is the same: what lies outside the family is not scored badly, it is not scored at all.

## What I have not resolved

Whether a latent-variable account of acquisition confounding is testable on a real dataset, or whether the components it recovers would just be a restatement of the site labels I already have.

## References

- Dempster, Laird & Rubin (1977). [Maximum Likelihood from Incomplete Data via the EM Algorithm](https://doi.org/10.1111/j.2517-6161.1977.tb01600.x). *JRSS B*.
- Blei, Kucukelbir & McAuliffe (2017). [Variational Inference: A Review for Statisticians](https://doi.org/10.1080/01621459.2017.1285773). *JASA*.
