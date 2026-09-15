---
layout: study_note
title: "Curvature Without the Hessian: Power Iteration, Trace Estimation, and Quantization"
description: "Second-order information about a network that is too large to form, estimated by matrix-vector products, and what it is used to decide."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "algebra-and-optimisation"
category_title: "Linear Algebra & Optimisation"
order: 6
source: "Independent study"
written: true
updated: "2026-09-15"
---

Second-order information says how sharply a loss responds to a change in weights. For a trained network the matrix that carries it cannot be formed, let alone stored — and yet the quantities actually needed from it can be estimated with nothing but matrix-vector products.

## Core question and definition

Expanding the loss around trained weights to second order gives

$$
L(w + \Delta) \approx L(w) + g^\top \Delta + \tfrac{1}{2}\,\Delta^\top H \Delta,
$$

with $$g$$ the gradient and $$H$$ the Hessian. If $$w$$ sits at a converged minimum then $$g \approx 0$$, and the quadratic term is what remains: curvature, not slope, describes what a perturbation costs.

The obstacle is size. A model with $$10^6$$ parameters has a Hessian with $$10^{12}$$ entries. It is not a matrix anyone forms, and the Newton step $$\Delta = -H^{-1}g$$ that second-order optimisation would want is doubly out of reach.

The useful move is to stop asking for $$H$$ and ask only for scalars derived from it.

## Key concepts

### Power iteration finds the largest eigenvalue from products alone

Start from a random vector, multiply by the matrix, normalise, repeat:

$$
v \leftarrow \frac{Hv}{\lVert Hv \rVert}.
$$

Writing $$v$$ in the eigenbasis makes the reason plain: each multiplication scales every component by its eigenvalue, so the largest one grows fastest in relative terms and the rest fade. After enough iterations $$v$$ points along the dominant eigenvector and $$v^\top H v$$ gives its eigenvalue.

Nothing here requires $$H$$ itself, only the ability to compute $$Hv$$ — and that is available: $$Hv$$ is the gradient of $$g^\top v$$, so one extra backward pass through an autodiff graph produces it.

### Hutchinson's estimator gets the trace the same way

For a random vector $$z$$ with zero mean and identity covariance,

$$
\mathbb{E}\!\left[z^\top H z\right] = \operatorname{tr}(H).
$$

Averaging $$z^\top H z$$ over sampled $$z$$ therefore estimates the trace — the sum of all eigenvalues — again through matrix-vector products only. [Hutchinson](https://doi.org/10.1080/03610918908812806) (1989) introduced it for influence matrices.

Trace and top eigenvalue answer different questions. The top eigenvalue reports the single sharpest direction; the trace reports total curvature across all of them. Which is the better summary is an empirical question, and the two quantization papers below disagree about it.

### Curvature as a sensitivity ranking for mixed-precision quantization

Mixed precision assigns different bit-widths to different parts of a network, and the search space is hopeless by brute force — thirty blocks with four candidate widths is $$4^{30}$$, each option requiring training to evaluate. A proxy for sensitivity is needed.

Gradient magnitude is the obvious candidate and is a poor one: at a converged minimum the gradient is near zero everywhere by construction, so it separates nothing. Curvature does not have that defect. A block whose loss responds sharply to perturbation should keep more bits; a flat one can be compressed harder.

[HAWQ](https://doi.org/10.1109/iccv.2019.00038) (Dong and colleagues, ICCV 2019) ranks blocks by the top Hessian eigenvalue, obtained by power iteration. Its successor argues the trace is the better measure, on the grounds that one direction is a thin summary of a whole block's curvature.

### Synthesising data from what the network already recorded

Quantization calibration normally needs data. [ZeroQ](https://doi.org/10.1109/cvpr42600.2020.01318) (Cai and colleagues, CVPR 2020) constructs it instead, by exploiting the fact that batch normalisation layers store the mean and variance their inputs had during training. Optimising a synthetic input so that its intermediate activations match those stored statistics produces data that is, in a narrow statistical sense, what the network was trained on.

This depends entirely on those layers existing. A network without batch normalisation, or one where it has been folded into the preceding weights, does not carry the same record.

It also invites a caution that the lecture makes better than the papers do: deploying a model with no evaluation data at all is a strange premise for a clinical setting. If a handful of cases are available, a few is not a test set either, and the honest number is nearer thousands.

## Where this touches my work

Curvature as a sensitivity measure is the same shape of argument as an evidence audit — perturb something, see how much the output moves, rank by that — with one difference worth keeping in view. Here the perturbation is to weights and the ranking is of computational components. An evidence claim needs perturbation of the input and a ranking of clinical structures, and the two do not substitute for each other.

The ZeroQ observation is the part I did not expect to find useful. Batch normalisation statistics are a record of the training distribution carried inside the shipped weights. Anything that leaks the training distribution is a route to asking whether a deployment population resembles it — and if that record can be recovered from the model alone, it is worth knowing both as a tool and as a disclosure risk for models released without their data.

## What I have not resolved

Whether the gradient-is-zero-at-convergence argument holds for the models I work with, which are rarely trained to the point where that is true, and whether a small but non-zero gradient makes first-order sensitivity usable after all.

## References

- Hutchinson (1989). [A Stochastic Estimator of the Trace of the Influence Matrix](https://doi.org/10.1080/03610918908812806). *Communications in Statistics*.
- Dong et al. (2019). [HAWQ: Hessian AWare Quantization of Neural Networks with Mixed-Precision](https://doi.org/10.1109/iccv.2019.00038). ICCV.
