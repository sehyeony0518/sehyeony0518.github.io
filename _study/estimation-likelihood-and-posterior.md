---
layout: study_note
title: "Estimation: Likelihood, Posterior, and What Few Observations Permit"
description: "What maximum likelihood actually claims, what a prior adds, and why five observations and five hundred do not license the same statement."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "probability-and-inference"
category_title: "Probability & Statistical Inference"
subgroup: "Conditioning, Estimation & Decisions"
order: 2
source: "Independent study"
written: true
updated: "2026-09-15"
---

A sensor produces observations; something underneath produced them. Estimation is the step between, and the uncertainty in it comes from noise and from the limits of the model assumed. Which estimator is used decides what the resulting number is entitled to claim.

## Core question and definition

Three situations differ, and confusing them is the usual source of trouble.

The parameter is unknown and the random variable is observed. The realisations $$x_1,\dots,x_N$$ are in hand and $$\theta$$ is wanted: **maximum likelihood**.

The parameter is known and the realisation is not. A quantity was generated but never observed directly: **estimation of the latent value**.

Neither is known. Both the parameter and the variable it generated are hidden: the case the [next note](/study/latent-variables-em-and-variational-inference/) takes up.

## Key concepts

### Maximum likelihood answers one question, not every question

Given observations $$D$$ and a model with parameter $$\theta$$, maximum likelihood takes

$$
\hat\theta_{\mathrm{ML}} = \arg\max_\theta \; p(D \mid \theta),
$$

and when the observations are assumed independent the product factorises, so the log is maximised instead:

$$
\log p(D\mid\theta) = \sum_{i=1}^{N} \log p(x_i \mid \theta).
$$

For a die rolled five times, with $$n_i$$ the count of face $$i$$ and $$\sum_i \theta_i = 1$$ as a constraint handled by a Lagrange multiplier, the answer is the obvious one: $$\hat\theta_i = n_i / N$$. Each face gets the fraction of rolls it won.

That is also its problem. Five rolls showing 6, 5, 3, 4, 4 give $$\hat\theta_1 = 0$$: the estimate says face 1 is impossible. Maximum likelihood is not wrong here; it is answering exactly the question asked, which was what parameter best explains *these* observations and nothing else.

### A prior is the belief the data must overcome

Treating $$\theta$$ as a random variable rather than a fixed unknown changes the object being sought. Bayes gives

$$
p(\theta \mid D) = \frac{p(D \mid \theta)\,p(\theta)}{p(D)},
$$

and the answer is now a distribution, not a point. A point can be extracted afterwards, the mode, the mean, but that extraction is a separate decision.

The denominator is where this becomes hard. It requires integrating over $$\theta$$, which for anything beyond a toy model is rarely available in closed form.

### Conjugate priors buy tractability with expressiveness

If the likelihood is binomial, a Beta prior $$\mathrm{Beta}(\alpha,\beta)$$ returns a Beta posterior. The integral still exists; it just does not have to be performed, because the update is a change of parameters.

This makes the small-sample question concrete. Three products: 10 reviews all positive, 50 reviews with 48 positive, 200 reviews with 186 positive. Maximum likelihood ranks them 1.00, 0.96, 0.93 and declares the first best. Under a prior that mildly doubts extremes, the 200-review estimate barely moves, the 50-review estimate moves a little, and the 10-review estimate moves a lot, and the second product wins.

The objection "too few reviews" is really a statement that a prior is being held and the data has not been sufficient to shift it.

### Which estimator is chosen is a claim about what is known

The contrast is sharpest in the joke where a detector reports the sun has exploded after passing a test that lies with probability $$1/36$$. From the likelihood alone the report is far more probable under explosion than not. The refusal to accept it is a prior about suns, and it is worth being explicit that this is what is happening rather than pretending the data decided.

The historical version is less comfortable. Observations that the sun moves across the sky were taken as evidence for a geocentric model, and the prior that overturned it was not the obvious one. A prior is not automatically the reasonable party in the dispute.

## Where this touches my work

A diagnostic model that outputs a probability is an estimator, and the number it reports carries the same dependence on sample size. A subgroup represented by a handful of cases produces an estimate with the structure of the ten-review product: extreme, confident-looking, and not entitled to the confidence. When I report subgroup performance, the count belongs next to the estimate, not in an appendix.

The conjugate-prior example is also the cleanest statement I know of why an audit needs to say how many cases stand behind each claim. An estimate and an estimate-with-its-sample-size are different objects, and only the second can be argued with.

## What I have not resolved

Where a defensible prior comes from in a clinical setting. Prevalence from the literature is one source, but literature prevalence is itself estimated from a population that may not be the deployment population, which pushes the problem back a level rather than solving it.

## References

- Dempster, Laird & Rubin (1977). [Maximum Likelihood from Incomplete Data via the EM Algorithm](https://doi.org/10.1111/j.2517-6161.1977.tb01600.x). *JRSS B*.
