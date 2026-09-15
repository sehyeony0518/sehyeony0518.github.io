---
layout: study_note
title: "Choosing the Loss: Squared Error, Absolute Error, and What Each One Believes"
description: "The loss is where you state what counts as a good answer. Squaring makes one bad point outvote nine good ones — and the arithmetic of how badly is worth seeing."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "algebra-and-optimisation"
category_title: "Linear Algebra & Optimisation"
order: 10
source: "Independent study"
written: true
updated: "2026-09-15"
---

Every supervised learning setup is three decisions, and it is worth being able to point at each one in a training script:

$$
\hat\theta = \arg\min_\theta \sum_{i=1}^{N} D\big(f_\theta(x_i),\, y_i\big)
$$

$$f$$ is the architecture. $$D$$ is what counts as a good answer. The minimisation is the optimiser. Architecture and optimiser can plausibly be searched automatically — that is what neural architecture search and hyperparameter tuning are. **$$D$$ cannot**, because it encodes what you want, and there is nobody to ask but you.

## Core question and definition

Linear regression fixes $$f_\theta(x) = w^{\mathsf T}x + b$$, which is best written by appending a constant 1 to $$x$$ so the intercept folds into $$w$$ and the model is a plain inner product. That leaves $$D$$ as the only open choice, which is why linear regression is the right place to look at the choice in isolation.

The default is **squared error**, $$D(\hat y, y) = (\hat y - y)^2$$ — sum of squared residuals, geometrically the total area of squares erected on the vertical gaps. It has three real advantages: it is convex, so any local minimum is global; it is differentiable everywhere; and it has a closed-form solution $$\hat w = (X^{\mathsf T}X)^{-1}X^{\mathsf T}y$$, so for a small problem no iteration is needed at all.

Then there is the reason nobody mentions, which is that it is what everyone else uses.

## Key concepts

### One bad point is enough

Take ten points on the exact line $$y = 2x+1$$. Least squares recovers slope 2 and intercept 1, as it must. Now move a single point up by 50 — a transcription error, a mislabelled case, a sensor glitch:

| | slope | intercept | slope error |
|---|---|---|---|
| truth | 2.000 | 1.000 | — |
| least squares, one outlier | 2.303 | 4.333 | **15.2%** |
| least absolute deviation, one outlier | 2.000 | 1.000 | **0.0%** |

One point in ten moved the least-squares slope by 15% and the intercept by a factor of four. The $$L_1$$ fit returned the exact clean line.

The mechanism is visible in one derivative. The pull a residual exerts on the fit is $$\partial D/\partial r$$: for squared error that is $$2r$$, so at $$r=50$$ the point pulls with strength **100**; for absolute error it is $$\operatorname{sign}(r)$$, strength **1**, the same as every other point. Squared error lets a residual buy influence in proportion to how wrong it is, which is precisely backwards from what you want when large residuals are the ones most likely to be errors.

Squaring is not a neutral technical convenience. **It is the assertion that a point ten times further away matters a hundred times more** — reasonable if residuals are Gaussian noise, wrong if they are contamination.

### What the robust choice costs

$$\sum_i \lvert y_i - w^{\mathsf T}x_i\rvert$$ is still convex, so the global-optimum guarantee survives. Two things do not.

The closed form is gone — absolute value is not differentiable at zero, so setting the derivative to zero does not yield a linear system, and the problem must be solved iteratively (or as a linear program). Second-order methods are also gone: the second derivative of a piecewise-linear function is zero wherever it exists, so Newton's method has nothing to work with. Gradient descent remains, and the loss surface is a collection of planes meeting at creases rather than a smooth bowl.

Pushing further does not help. Raising the exponent above 2 concentrates influence on outliers even harder; lowering it below 1 breaks convexity and the global guarantee with it. **Squared error and absolute error bracket the usable range**, and Huber's loss — quadratic near zero, linear in the tails — is the deliberate compromise: differentiable everywhere like $$L_2$$, bounded-influence like $$L_1$$.[^huber]

### The sample weights are part of the loss too

The same slot in $$D$$ takes per-sample weights:

$$
\sum_i c_i\, D\big(f_\theta(x_i), y_i\big).
$$

This is the standard response to class imbalance — upweight the rare class so the optimiser cannot buy a low loss by predicting the majority everywhere. It is also how "this case must not be missed" gets expressed, because there is nowhere else to express it.

Worth being clear about what it is, though: **reweighting is an attempt, and whether it worked is an evaluation question, not a training one.** Multiplying the positive class by 100 changes what the optimiser chases; it does not guarantee that precision and recall come out where you need them. That is measured afterward, on held-out data, and the two steps should not be confused.

## Why it matters for my work

Medical datasets have outliers, and almost none of them are interesting. Mistyped measurements, mislabelled studies, a scan from the wrong patient, a segmentation where the annotator's cursor slipped. Squared error hands each of these influence proportional to how wrong it is, which means **the single worst record in a dataset has more say in the fit than dozens of good ones**. On a dataset of a few hundred cases — normal in clinical work — a handful of bad records is not a rounding error.

The asymmetry is what makes this actionable: a robust loss costs a closed form and some optimisation convenience, while a non-robust loss costs correctness in a way that does not announce itself. A fit skewed by contamination looks like a fit. It has a residual, an $$R^2$$, a plot. Nothing in the output says a tenth of the data did most of the work.

This connects to [label quality](/study/label-quality-and-interobserver-variability/) more directly than I had appreciated. Interobserver variability is not merely noise to be averaged away — under a squared loss, the most discordant annotations are the most influential ones. A model trained with $$L_2$$ on labels with high interobserver variability is disproportionately fitting the outlier readers. Robust losses are one of the few places where a modelling choice, rather than a data-collection change, does something about that.

## What I have not resolved

Where the crossover actually sits. Robust losses trade efficiency for resistance, and if residuals really are Gaussian, least squares is optimal and $$L_1$$ wastes data — which matters when you have 200 cases, not 200,000. I do not have a principled way to decide, for a given clinical dataset, whether the contamination rate justifies the efficiency loss, and I suspect the honest answer is to fit both and treat a large discrepancy as a finding about the data rather than as a model-selection problem.

---

[^huber]: Huber, P. J. (1964). Robust estimation of a location parameter. *The Annals of Mathematical Statistics*, 35(1), 73–101. [10.1214/aoms/1177703732](https://doi.org/10.1214/aoms/1177703732)
