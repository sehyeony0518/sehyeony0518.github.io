---
layout: study_note
title: "Choosing an Estimator: MMSE, MAP, and Maximum Likelihood"
description: "Three answers to the same question, what each one optimises, and which of them needs an integral nobody can evaluate."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "probability-and-inference"
category_title: "Probability & Statistical Inference"
order: 3
source: "Independent study"
written: true
updated: "2026-09-15"
---

Something is observed and something else is wanted. Several estimators answer that, they do not agree, and the disagreement is not a technicality: it is a disagreement about what question was being asked.

## Core question and definition

With $$y$$ observed and $$x$$ unknown, three criteria:

$$
\hat{x}_{\mathrm{MMSE}} = \arg\min_{\hat{x}(\cdot)} \mathbb{E}\!\left[\lVert x - \hat{x}(y)\rVert^2\right],
\qquad
\hat{x}_{\mathrm{MAP}} = \arg\max_x p(x \mid y),
\qquad
\hat{x}_{\mathrm{ML}} = \arg\max_x p(y \mid x).
$$

The first minimises expected squared error over all estimators, without restricting their form: the restriction to affine estimators is what produces [the Wiener filter](/study/linear-mmse-and-the-wiener-filter/) instead. The second takes the most probable value of the unknown given what was seen. The third takes the value under which the observation was most probable, which is not the same thing.

## Key concepts

### The MMSE estimator is the conditional mean

Conditioning on $$y$$ and minimising pointwise gives a clean answer:

$$
\hat{x}_{\mathrm{MMSE}}(y) = \mathbb{E}[x \mid y].
$$

The best guess under squared error is the average of what $$x$$ could be, given what was seen. This sounds unavoidable and is specific to the criterion: under absolute error the answer is the conditional median, and under a zero-one criterion it is the mode, which is MAP.

So "best" was never a property of an estimator. It is a property of an estimator together with a loss.

### Likelihood and posterior point in opposite directions

Maximum likelihood asks which $$x$$ makes the observation most probable. MAP asks which $$x$$ is most probable given the observation. Mistaking one for the other is the base-rate error.

A seismic sensor reports vibration. Given an earthquake, the alarm fires essentially always, so under maximum likelihood an earthquake is the answer. But alarms also fire when a mouse runs past the sensor, and mice are far commoner than earthquakes. What is wanted is $$p(\text{earthquake} \mid \text{alarm})$$, and getting it requires the prior that maximum likelihood has no place for.

The general point is that $$p(A \mid B)$$ and $$p(B \mid A)$$ are different quantities, and that the one easier to write down is usually not the one wanted.

### MAP is cheap because a constant can be ignored

By Bayes,

$$
p(x \mid y) = \frac{p(y \mid x)\,p(x)}{p(y)},
$$

and the denominator does not involve $$x$$. Maximising the posterior therefore only needs $$p(y\mid x)p(x)$$, and the evidence term can be dropped entirely.

MMSE has no such luck. A conditional mean is an integral against the posterior, and the posterior needs its normalising constant. This is the practical reason MAP appears far more often than MMSE, not that it answers a better question, but that it avoids the integral.

### In the Gaussian case they all coincide, and the answer is shrinkage

Take $$y = x + w$$ with $$x \sim \mathcal{N}(0, \sigma_x^2)$$, $$w \sim \mathcal{N}(0, \sigma_w^2)$$, independent. The posterior is Gaussian, so its mean and its mode are the same point, and

$$
\hat{x} = \frac{\sigma_x^2}{\sigma_x^2 + \sigma_w^2}\, y .
$$

MMSE, MAP and the Wiener filter all return this. Maximum likelihood does not: with no prior it returns $$\hat{x} = y$$, keeping the noise.

The coefficient is the signal's share of the total variance, so the estimate is pulled toward the prior mean by exactly how noisy the observation is. That this simplest possible case is already this much work is itself the lesson: estimation is rarely a one-line calculation, and closed forms are the exception.

## Where this touches my work

The base-rate confusion is the failure I most expect to meet in clinical machine learning, because the quantity a model reports and the quantity a clinician needs differ in precisely this way. A model trained on a cohort enriched for disease has learned something closer to $$p(\text{finding} \mid \text{disease})$$ than to the $$p(\text{disease} \mid \text{finding})$$ that a screening population requires, and its outputs will be confidently wrong in the direction the mouse-and-earthquake example predicts.

The second transfer concerns what a reported probability is. If it came from a MAP-style argument, it is a mode and says nothing about the spread around it. Two models can report the same number with completely different posteriors behind them, and only one of those is a basis for abstaining.

## What I have not resolved

Whether the prior a deployment site needs can be supplied post hoc, rescaling outputs by a known prevalence ratio, or whether a model trained on the wrong base rate has learned features that no reweighting fixes.

## References

- Wiener (1949). [Extrapolation, Interpolation, and Smoothing of Stationary Time Series](https://doi.org/10.7551/mitpress/2946.001.0001). MIT Press.
