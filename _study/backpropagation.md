---
layout: study_note
title: "Backpropagation, in Scalars and in Matrices"
description: "Why a procedure for computing derivatives is the whole of a training algorithm, and what the backward pass turns out to be for a dense layer and for a convolution."
tab: "ai-foundations"
tab_title: "Theory"
category: "neural-networks"
category_title: "Neural Networks & Representation"
order: 2
source: "Independent study"
written: true
updated: "2026-09-15"
---

Nobody tells the middle layers of a network what to represent. Only the output is supervised, and whatever the intermediate layers come to encode is a by-product of solving one optimisation problem. The mathematics that makes that possible is less than it appears: the chain rule, applied carefully.

## Core question and definition

Training is stated in one line. With parameters $$\theta$$ and a loss summed over training examples,

$$
\hat\theta = \arg\min_\theta \sum_i \ell\big(f_\theta(x_i),\, y_i\big).
$$

Setting the derivative to zero and solving is the textbook method and is unavailable here. What remains is to move downhill repeatedly:

$$
\theta \leftarrow \theta - \alpha \,\frac{\partial L}{\partial \theta}.
$$

This is worth stating in its strong form: **a procedure for computing the derivative is a procedure for learning.** Nothing else is required — not a closed-form solution, not an analytic minimum. Once Newton had the derivative, a method for descending followed; the surprise is how far that carries when $$\theta$$ has a hundred million components.

Because the loss is a sum over examples and differentiation is linear, the gradient for one example is the whole problem. The rest is addition.

## Key concepts

### The chain rule, read as a sensitivity

For $$w$$ depending on $$x$$, $$y$$, $$z$$,

$$
\delta w = \frac{\partial w}{\partial x}\delta x + \frac{\partial w}{\partial y}\delta y + \frac{\partial w}{\partial z}\delta z,
$$

which says only this: nudge an input, and the partial derivative is the constant of proportionality by which the output moves. Backpropagation is that statement composed across layers, and the interesting content is bookkeeping rather than insight.

### The matrix forms are compact, and they are all products

For a dense block $$y = Wx + b$$ followed by an element-wise nonlinearity, working with differentials gives the three results that matter. Writing $$g_y = \partial L / \partial y$$:

$$
\frac{\partial L}{\partial x} = W^\top g_y, \qquad
\frac{\partial L}{\partial W} = g_y\, x^\top, \qquad
\frac{\partial L}{\partial b} = g_y .
$$

Three things follow. The gradient flows backward through $$W^\top$$, the same weights transposed. The weight gradient is an **outer product** of what arrived from above with what was passed up from below. And an element-wise nonlinearity contributes a **Hadamard product** with its derivative — for a ReLU, a mask of ones and zeros.

Forward is a matrix product; backward is a matrix product. From a hardware point of view they are the same kind of work, which is why the same accelerator serves training and inference.

### The forward activations have to be kept

The backward pass needs $$x$$ to form $$g_y x^\top$$, and it needs the pre-activation to evaluate the nonlinearity's derivative. Those values came from the forward pass and cannot be conjured later without recomputing it.

This is the practical reason training consumes so much more memory than inference: every intermediate activation, across every channel and every layer, is held until the backward pass consumes it. The alternative — checkpointing a subset and recomputing the rest — trades time for memory and exists precisely because of this.

### A convolution's backward pass is another convolution

Convolution can be written as multiplication by a structured, sparse matrix. The backward pass is then multiplication by that matrix transposed — and transposing it turns out to be another convolution, with the kernel flipped.

So convolution is closed under this operation. Forward is a convolution, the gradient with respect to the input is a convolution, and the gradient with respect to the kernel is a convolution between the input and the incoming gradient — though that last one is not implemented as such, because its effective kernel is the size of the output rather than a few taps.

The practical value of knowing this arrives when autodiff cannot help: a custom layer whose forward pass is not composed of known operations needs a hand-written backward pass, and writing one requires this picture.

## Where this touches my work

Frameworks differentiate automatically, so none of this has to be written out. What it buys is the ability to debug — and debugging a network means having an expectation of what a value should be at a given point, which is exactly what is unavailable to someone who only knows the API. When a model trains to a good loss and behaves wrongly, the question is where the expectation and the observation part company, and that question is unaskable without knowing what the pass computes.

The memory point matters for a smaller reason that has caught me out: the activations retained during training are the same tensors an analysis would want to inspect, and a model shipped as weights alone has none of them. What can be examined after training is a narrower set than what existed during it.

## What I have not resolved

Whether the flipped-kernel picture generalises cleanly to the strided and dilated convolutions I actually use, or whether the correspondence gets complicated enough that the intuition stops paying for itself.

## References

- Rumelhart, Hinton & Williams (1986). [Learning representations by back-propagating errors](https://doi.org/10.1038/323533a0). *Nature*.
- LeCun et al. (1989). [Backpropagation Applied to Handwritten Zip Code Recognition](https://doi.org/10.1162/neco.1989.1.4.541). *Neural Computation*.
