---
layout: study_note
title: "Recurrent Networks and Gating"
description: "State carried across time, why gradients through it vanish or explode, and what a gate is actually doing about it."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "learning-principles"
category_title: "Learning Paradigms & Representations"
order: 4
source: "Independent study"
written: true
updated: "2026-09-15"
---

A feedforward network maps one input to one output. Much of what needs modelling does not have that shape — a sentence of unknown length, a video, a stream of sensor readings — and the recurrent answer is to carry state.

## Core question and definition

Add a hidden state that persists between steps:

$$
h_t = f(h_{t-1},\, x_t), \qquad y_t = g(h_t),
$$

which in the simplest case is a matrix product and a nonlinearity,

$$
h_t = \tanh\!\left(W_{hh}h_{t-1} + W_{xh}x_t + b\right).
$$

The analogy the lecture draws is a finite state machine: input plus current state determines next state and output. A feedforward network has no state; this does.

The consequence is that the same parameters handle sequences of any length. A network trained on sequences of fifty can run on five, or on five hundred.

## Key concepts

### The shapes this buys

One-to-many produces a variable-length output from a fixed input — an image and a caption whose length is not known in advance. Many-to-one consumes a variable-length input and emits one answer. Many-to-many with a delay is translation: read the whole source before emitting, because word order differs between languages. Many-to-many in step is per-frame classification.

The caution attached is worth repeating: recurrence is one way to handle sequences, not the only one, and being able to handle them does not make it the right choice.

### The gradient is a repeated product, which is the whole problem

Unrolling and backpropagating through time multiplies by the same recurrent weights at every step. A scalar analogy makes the consequence plain: a number slightly above one, raised to the hundredth power, explodes; slightly below one, vanishes.

Exploding gradients are the manageable half — clipping the norm bounds them. Vanishing is worse, because nothing signals it: training proceeds, the loss falls, and the model simply never learns any dependency longer than a few steps. [Bengio and colleagues](https://doi.org/10.1109/72.279181) (1994) showed this is intrinsic to the architecture rather than a tuning failure.

So the failure mode is specific: short-range structure is learned and long-range structure is silently not.

### A gate is multiplication by something between zero and one

The LSTM's response is an additional state that is *added to* rather than multiplied through, giving the gradient a path that does not pass through the repeated weight matrix.

What flows along that path is controlled by gates — sigmoid outputs in $$[0,1]$$ multiplying a signal, so zero erases and one passes unchanged. Three of them: what to forget from the carried state, how much of the newly computed content to write, and how much of the state to expose as output. The content itself comes from a $$\tanh$$, bounded so magnitudes stay controlled.

[Hochreiter and Schmidhuber](https://doi.org/10.1162/neco.1997.9.8.1735) (1997) introduced it. The linguistic example the lecture uses is the clearest: a sentence establishes a subject's gender, that fact is carried forward, and when a new subject appears the forget gate clears it. The gate learns *when* to discard, which is what a fixed decay cannot do.

Variants exist — coupling the forget and input gates so they sum to one, feeding the cell state into the gates, or the simpler GRU. Comparisons find no consistent winner, and the lecture is candid that the specific design choices are not well explained by anything but empirical results.

### Sequential computation is the cost

The state at step $$t$$ requires the state at $$t-1$$, so a sequence cannot be processed in parallel. Hardware that computes a whole batch at once cannot be used along the time axis, and training is slow in a way that no implementation fixes — which is much of why architectures without recurrence displaced these for long sequences.

## Where this touches my work

Ultrasound is acquired as a sweep and stored as frames, so the sequential structure is real and mostly discarded — a still frame is selected and the rest thrown away. What a recurrent model would add is the ability to use what came before a frame, which is also what a sonographer uses.

That creates an auditing question I have not seen asked. If a model reads a sequence, the evidence for its prediction may not be in the frame where the prediction is made, and an audit that examines one frame is looking in the wrong place. The gating mechanism makes this concrete: a value written into the carried state twenty frames earlier can still be driving the output.

The vanishing-gradient failure mode also generalises. A model that quietly learns only short-range structure looks like a model that works, and the shortfall is invisible in aggregate performance. That is the same shape as a shortcut — a model succeeding for reasons narrower than intended, with nothing in the training curve to say so.

## What I have not resolved

Whether frame-sequence context in ultrasound would improve clinical evidence use or simply give a model more opportunity to find acquisition-related shortcuts, since consecutive frames share operator, machine and settings almost perfectly.

## References

- Hochreiter & Schmidhuber (1997). [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735). *Neural Computation*.
- Bengio, Simard & Frasconi (1994). [Learning long-term dependencies with gradient descent is difficult](https://doi.org/10.1109/72.279181). *IEEE Trans. Neural Networks*.
