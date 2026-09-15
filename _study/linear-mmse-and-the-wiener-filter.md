---
layout: study_note
title: "Linear MMSE Estimation and the Wiener Filter"
description: "The best linear estimate of one quantity from another, and why it needs only means and covariances rather than a distribution."
tab: "ai-foundations"
tab_title: "Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
order: 8
source: "Independent study"
written: true
updated: "2026-09-15"
---

Something is observed and something else is wanted. Restricting the estimator to an affine function of the observation turns that into a problem with a closed-form answer, and the answer needs far less about the underlying randomness than one might expect.

## Core question and definition

Given an observation $$y$$, estimate $$x$$ with

$$
\hat{x} = Ay + b,
$$

choosing $$A$$ and $$b$$ to minimise the expected squared error $$\mathbb{E}\!\left[\lVert x - (Ay+b) \rVert^2\right]$$.

Two restrictions are being accepted at once. The estimator must be affine — a richer function of $$y$$ might do better. And the criterion is squared error, which weights a large mistake far more than several small ones, a choice that is conventional rather than inevitable.

What is bought in return is stated below, and it is the reason this remains practical.

## Key concepts

### Setting the derivative to zero, in two steps

Differentiating with respect to $$b$$ gives the easier half. The optimum satisfies

$$
b = \mu_x - A\mu_y,
$$

which says the estimator passes through the means: feed it the average observation and it returns the average target. The problem can therefore be re-centred, and from here both variables are taken as zero-mean.

Differentiating with respect to $$A$$ needs matrix calculus and yields the normal equations, whose solution is

$$
A = C_{xy} C_{y}^{-1},
$$

with $$C_{xy} = \mathbb{E}[xy^\top]$$ the cross-covariance and $$C_y$$ the covariance of the observation. When $$C_y$$ is singular a pseudo-inverse stands in.

In one dimension this collapses to something familiar, $$a = \sigma_{xy}/\sigma_y^2$$ — the regression slope. The matrix result is that statement generalised, not a different idea.

### Only second-order statistics are required

The solution contains means and covariances and nothing else. No density, no distributional family, no independence assumption beyond what the covariances already encode.

That is the property worth carrying away. Means, variances and correlations can be estimated from data far more reliably than a joint distribution over high-dimensional variables can, so an estimator that asks only for them is buildable when a fully Bayesian one is not. It is optimal among affine estimators; the conditional mean $$\mathbb{E}[x \mid y]$$ may do better and generally requires the distribution the affine estimator avoided needing.

### The denoising case makes the structure visible

Take $$y = x + w$$ with signal and noise uncorrelated and the noise zero-mean. Then

$$
C_y = C_x + C_w, \qquad C_{xy} = C_x,
$$

so

$$
A = C_x (C_x + C_w)^{-1}.
$$

This is the Wiener filter, and it reads as a ratio. Where the signal dominates, $$A$$ approaches the identity and the observation passes through. Where noise dominates, $$A$$ shrinks toward zero and the estimate falls back on the mean. The filter is doing nothing more clever than weighting each component by how much of it is signal — which is also why it cannot recover what the noise buried.

## Where this touches my work

Shrinkage toward the mean is the behaviour I would want to notice in a preprocessing step. Any denoising or enhancement applied before a diagnostic model is an estimator with a prior in it, and this one's prior is a covariance structure. A small, low-contrast finding is exactly the component such a filter attenuates, because attenuating low-power components is what it was derived to do.

The second-order-statistics point cuts the other way and is more encouraging. When I want to describe how two measurements co-vary — a finding and an acquisition setting, say — covariance is estimable from the data I actually have, whereas their joint distribution is not. Knowing what a covariance can and cannot support is part of knowing when a claim is within reach.

## What I have not resolved

Whether the affine restriction is a real limitation for the quantities I care about, or whether the interesting dependence between an image feature and an acquisition variable is linear enough that it does not matter. I suspect the former and have not tested it.

## References

- Wiener (1949). [Extrapolation, Interpolation, and Smoothing of Stationary Time Series](https://doi.org/10.7551/mitpress/2946.001.0001). MIT Press.
