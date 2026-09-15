---
layout: study_note
title: "The Exponential Moving Average: One Recursion Behind Momentum, RMSProp and Adam"
description: "A single line of algebra that replaces a buffer with one number — and once you recognise it, most of the optimiser zoo stops being a zoo."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "algebra-and-optimisation"
category_title: "Linear Algebra & Optimisation"
order: 9
source: "Independent study"
written: true
updated: "2026-09-15"
---

Suppose you want a running average of a quantity arriving one value at a time, inside a network, without storing the history.

The honest approach — accumulate a sum and a count, divide — gives the average over all time, which is usually not what is wanted: a recent average is. The obvious fix is a buffer of the last 100 values, summed and divided. That works and costs 100 floats per quantity averaged, which inside a network with millions of parameters is a hundredfold memory increase for a bookkeeping device.

## Core question and definition

The **exponential moving average** removes the buffer entirely:

$$
v_t = \alpha\,v_{t-1} + (1-\alpha)\,x_t .
$$

One float of state. Unrolling shows what it computes:

$$
v_t = (1-\alpha)\sum_{k=0}^{\infty} \alpha^{k}\,x_{t-k},
$$

a weighted average whose weights decay geometrically into the past. They sum to exactly 1 — I verified this numerically to ten decimal places for $$\alpha = 0.9$$ and $$0.99$$ — so this is a genuine average, not a scaled sum.

The natural reading of $$\alpha$$ is through $$1/(1-\alpha)$$: the effective window. At $$\alpha=0.9$$ that is 10 samples, at $$\alpha=0.99$$ it is 100. The most recent $$1/(1-\alpha)$$ terms carry about 63% of the total weight in both cases — $$0.6513$$ and $$0.6303$$ — which is the same $$1-1/e$$ that governs any first-order decay. The half-life is $$\log(0.5)/\log\alpha$$: 6.6 steps at $$\alpha=0.9$$, 69 steps at $$\alpha=0.99$$.

So the defaults are not arbitrary. **$$\beta_1 = 0.9$$ means "average the last ten gradients" and $$\beta_2 = 0.999$$ means "average the last thousand squared gradients"** — which makes it obvious why the second moment uses a far longer window than the first.

## Key concepts

### Momentum is an EMA of the gradient

Plain gradient descent on an elongated valley oscillates across the narrow direction while creeping along the shallow one, because the steepest direction at each point is across the valley rather than down it.

Momentum averages the direction instead:

$$
v_t = \beta v_{t-1} + (1-\beta)\nabla f(\theta_{t-1}), \qquad \theta_t = \theta_{t-1} - \eta\, v_t .
$$

The oscillating component alternates sign and averages toward zero; the consistent component accumulates. This is exactly the EMA above with $$x_t = \nabla f$$, and the ball-rolling-downhill metaphor is a description of what the recursion does rather than an independent idea.

Nesterov's variant evaluates the gradient at the point momentum is *about to* carry you to, $$\theta_{t-1} - \eta\beta v_{t-1}$$, rather than where you are — which lets it decelerate before overshooting rather than after.[^nesterov]

### Adaptive rates are an EMA of the squared gradient

A separate problem: one global learning rate is wrong for every parameter, because gradients differ wildly in scale across a network. A parameter whose gradient is usually zero and occasionally large should move decisively when it does move; a parameter receiving a gradient every step should move cautiously.

AdaGrad divides the step by $$\sqrt{\sum_\tau g_\tau^2}$$, accumulated over all time.[^adagrad] The accumulator only grows, so the effective rate decays monotonically toward zero — which is provably right for convex problems and, for a long training run, means the optimiser stops before arriving.

RMSProp fixes it with one substitution: **replace the running sum with an EMA.** $$s_t = \beta_2 s_{t-1} + (1-\beta_2)g_t^2$$, step $$\propto g_t/\sqrt{s_t + \epsilon}$$. The window is now finite, so the rate can rise again if gradients shrink.

**Adam is the two combined** — an EMA of the gradient for direction, an EMA of the squared gradient for per-parameter scale.[^adam] That is the whole idea. Once the EMA is recognised, Adam has no third ingredient.

### Bias correction is the startup artifact

Initialising $$v_0 = 0$$ biases the estimate toward zero for the first several steps. With a constant gradient of 1 and $$\beta=0.9$$ the raw EMA reads $$0.1, 0.19, 0.271, 0.3439, 0.4095$$ — still less than half the true value after five steps.

Dividing by $$1-\beta^t$$ fixes it exactly: I checked, and the corrected value is $$1.0000$$ at every one of those steps. That is Adam's $$\hat v_t = v_t/(1-\beta_1^t)$$, and it is not a heuristic — it is the exact normalisation for the weights actually accumulated so far, since $$\sum_{k=0}^{t-1}(1-\beta)\beta^k = 1-\beta^t$$.

### The same recursion, in three other places

Once seen, it is hard to unsee. Batch normalisation's inference-time statistics are an EMA of the training batch statistics, for the same memory reason.[^bn] Weight averaging over a trajectory is an EMA of the parameters. Target networks in deep RL are an EMA of the online network.

Each is described in its own paper as its own mechanism. Each is $$v \leftarrow \alpha v + (1-\alpha)x$$.

And it is also a filter. Written as a difference equation, $$v_t = \alpha v_{t-1} + (1-\alpha)x_t$$ is a one-pole IIR low-pass with a pole at $$z=\alpha$$ — which is why it smooths, why $$\alpha$$ close to 1 smooths harder, and why it costs one state variable where a [moving-average FIR](/study/fir-filter-design/) of comparable smoothing costs a full buffer of taps. The optimiser literature and the signal-processing literature named the same object twice.

## Why it matters for my work

The practical value is that **the optimiser hyperparameters become interpretable rather than incantatory.** "$$\beta_1=0.9$$" is unreadable; "average over roughly the last ten gradients" tells me immediately that a run with 30 steps per epoch is smoothing over a third of an epoch, and whether that is sensible depends on how heterogeneous my batches are. With a class-imbalanced medical dataset where positive cases appear in a minority of batches, a ten-batch gradient window may span no positive example at all.

There is a reporting point too. Optimiser choice and its hyperparameters materially affect final performance, and papers reporting a single run with default Adam settings are reporting one sample from a distribution they did not characterise. That belongs with the other [reproducibility](/study/reproducibility-benchmarks-and-translational-study-design/) concerns rather than being treated as an implementation detail below the threshold of description.

The conceptual point I value more: this is a case where **four named methods collapse into one idea plus a choice of what to average.** I keep meeting literatures that look like a catalogue of tricks and turn out to have a small number of ideas in them. Finding the recursion is a better use of time than memorising the catalogue — and it is the difference between being able to invent the next variant and being able to recite the last one.

## What I have not resolved

Whether Adam's advantage over well-tuned SGD with momentum survives on the small, imbalanced datasets typical of medical imaging, or whether the per-parameter scaling mostly helps in regimes — very large models, sparse gradients — that those datasets do not reach. The comparisons I have seen are on large-scale benchmarks.

---

[^nesterov]: Sutskever, I., Martens, J., Dahl, G., & Hinton, G. (2013). On the importance of initialization and momentum in deep learning. *ICML*, PMLR 28(3), 1139–1147.

[^adagrad]: Duchi, J., Hazan, E., & Singer, Y. (2011). Adaptive subgradient methods for online learning and stochastic optimization. *JMLR*, 12, 2121–2159.

[^adam]: Kingma, D. P., & Ba, J. (2015). Adam: A method for stochastic optimization. *ICLR*. [arXiv:1412.6980](https://arxiv.org/abs/1412.6980)

[^bn]: Ioffe, S., & Szegedy, C. (2015). Batch normalization: Accelerating deep network training by reducing internal covariate shift. *ICML*. [arXiv:1502.03167](https://arxiv.org/abs/1502.03167)
