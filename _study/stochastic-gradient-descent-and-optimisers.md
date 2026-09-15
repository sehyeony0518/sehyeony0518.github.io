---
layout: study_note
title: "Stochastic Gradient Descent and the Optimisers Built On It"
description: "Why the gradient is estimated from a handful of examples, what momentum and per-parameter rates each fix, and why saddle points replaced local minima as the suspected obstacle."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "math-foundations"
category_title: "Mathematical & Statistical Foundations"
order: 14
source: "Independent study"
written: true
updated: "2026-09-15"
---

Training minimises a sum over every example, so the exact gradient requires a pass over the whole dataset for one step. Almost nothing about modern training survives that literal reading, and the departures from it are not compromises but the thing that makes training work.

## Core question and definition

The objective is a sum, so its gradient is a sum:

$$
\nabla_\theta L = \sum_{i=1}^{N} \nabla_\theta\, \ell\big(f_\theta(x_i),\, y_i\big).
$$

Computing it in full — **batch gradient descent** — needs every example in memory for a single update, and adding one example invalidates the whole calculation.

Using one example instead gives an unbiased but noisy estimate. [Robbins and Monro](https://doi.org/10.1214/aoms/1177729586) (1951) established that such a procedure converges under conditions on the step size, long before anyone applied it here. In practice neither extreme is used: a **mini-batch** of a few dozen examples averages away enough of the noise while suiting hardware that computes a batch faster than the same examples one at a time.

The [existing note on optimisation](/study/optimization-for-machine-learning/) covers what an objective and a regulariser mean. This one is about the procedure.

## Key concepts

### The noise is not only a cost

A noisy gradient makes the path erratic, and that erratic path can leave a basin that a smooth descent would have settled into. This is the stated reason stochastic descent is not merely a cheaper approximation.

It comes at a price that should be named: convergence becomes hard to characterise, and the loss can increase between steps. Watching a training curve rise is not by itself evidence of a bug.

### Momentum averages the direction

Gradients that disagree between steps waste movement. Momentum keeps a running direction,

$$
v \leftarrow \beta v + (1-\beta)\,\nabla_\theta L, \qquad \theta \leftarrow \theta - \eta\, v,
$$

which is an **exponentially weighted moving average**. Unrolling it shows every past gradient present with a weight decaying geometrically — recent ones count most, and nothing has to be stored but the running vector.

The effect in a narrow valley is that oscillation across the walls cancels while movement along the floor accumulates. A refinement evaluates the gradient at the point the momentum is about to reach rather than where it currently is, so the step can be checked before it is taken.

### Per-parameter rates fix a different problem

One global learning rate treats every parameter alike, though some receive large gradients constantly and others receive small ones rarely. Dividing each parameter's step by the accumulated magnitude of its own gradients equalises this — but an accumulating sum only grows, so the rate decays to zero and learning stops.

Replacing the sum with a moving average fixes that, and combining the two ideas — an average of the gradient for direction, an average of its square for scale — is the optimiser in general use. Both are the same exponential average applied to different quantities.

### Saddle points, not local minima

The older explanation for training failure was local minima. The current suspicion is saddle points: places that curve down along one direction and up along another, where the gradient vanishes and descent stalls even though a descending direction exists nearby.

The argument is that in high dimensions a critical point must curve upward in *every* direction to be a minimum, which becomes vanishingly unlikely, whereas mixed curvature does not. This is an inference rather than a direct observation — the surface cannot be seen — and it is worth holding as the current reading rather than a settled fact. It does explain why momentum helps: accumulated velocity carries a parameter through a flat region that an instantaneous gradient would stop in.

## Where this touches my work

Two things here bear on auditing a trained model.

The first is that the optimiser is part of what determined the solution. Two runs differing only in batch order reach different weights, and if one relies on a shortcut more than the other, that difference was produced by the procedure and not by the data. An audit of a single trained model is an audit of one draw.

The second is about training curves as evidence. Because stochastic descent legitimately goes uphill, a loss curve is weak evidence of anything, and a model that converged to a low training loss has demonstrated that a parameter setting exists which fits the training set — a statement about the optimisation, not about what was learned.

## What I have not resolved

Whether the run-to-run variation in shortcut reliance is large enough to matter in practice. If it is, auditing one checkpoint is reporting a sample of size one, and I have not seen this quantified for medical imaging models.

## References

- Robbins & Monro (1951). [A Stochastic Approximation Method](https://doi.org/10.1214/aoms/1177729586). *Annals of Mathematical Statistics*.
- Polyak (1964). [Some methods of speeding up the convergence of iteration methods](https://doi.org/10.1016/0041-5553%2864%2990137-5). *USSR Computational Mathematics*.
