---
layout: study_note
title: "Optimising the Input: Visualisation, Style, and Adversarial Examples"
description: "What happens when the weights are frozen and the image becomes the free variable, and why the same procedure produces both a picture of a concept and a picture that fools the model."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "learning-principles"
category_title: "Learning Paradigms & Representations"
order: 3
source: "Independent study"
written: true
updated: "2026-09-15"
---

Training computes the gradient of a loss with respect to the weights and leaves the input alone. Nothing in backpropagation requires that arrangement. Freeze the weights, treat the image as the variable, and the same machinery runs — which is where a surprising amount of what is known about trained networks comes from.

## Core question and definition

Ordinary training solves

$$
\min_\theta \; L\big(f_\theta(x),\, y\big)
$$

over $$\theta$$ with $$x$$ fixed. Swapping which symbol is free gives

$$
\min_x \; L\big(f_\theta(x),\, y^\*\big)
$$

with $$\theta$$ fixed and $$y^\*$$ a chosen target. Both are gradient descent; the backward pass simply continues past the first layer instead of stopping there. Frameworks expose it directly, because computing $$\partial L/\partial x$$ is no different in kind from computing $$\partial L/\partial w$$.

What separates the applications below is only the choice of objective and of starting point. My [notes on attribution](/study/attribution-attention-and-counterfactual-explanations/) cover reading a single gradient; this is about optimising against one.

## Key concepts

### Class visualisation, and why a regulariser is needed

Start from noise, maximise the score of one class, and the result should be the network's picture of that concept. What actually appears first is high-frequency structure that no person would recognise.

Adding a penalty on the image — commonly the squared norm — changes the result into something interpretable. The lecture's observation about this is the one worth keeping: the same $$\lVert\cdot\rVert^2$$ term appears in ordinary training as weight decay, and in both places it means *do not use extreme values*. Only the variable it applies to has changed. A regulariser is not a fixed technique but a statement about which solutions are admissible, and here it is what makes the output legible to a person at all.

The honest caveat is that legibility to a person is not evidence about the network. A recognisable dumbbell image is consistent with the model having learned dumbbells; it is also consistent with a great deal else.

### Style transfer separates two losses over the same image

Content and style are made into two objectives and summed. Content similarity is the squared difference of activations at a middle layer — not raw pixels, which would forbid any restyling, and not the top layer, which retains too little of the arrangement. Style is the difference of **Gram matrices**: the correlations between feature channels at a layer, which discard where things are and keep what co-occurs.

[Gatys, Ecker and Bethge](https://doi.org/10.1109/CVPR.2016.265) (CVPR 2016) set this out. The part worth carrying is the pattern: a property that resists direct description was captured by choosing a statistic that is invariant to what it should ignore. Texture has been studied for decades precisely because it does not survive a pointwise comparison.

### Adversarial examples are the same optimisation with a small budget

Maximise the score of a chosen wrong class, and constrain the perturbation to stay within a small bound per pixel. After a few iterations the network is confident about the wrong label while the image is unchanged to a person.

Two things about this are worth more than the demonstration. First, the perturbations often transfer: an example built against one network fools another with different architecture and training data. That is not what one expects of an arbitrary exploit, and it suggests the vulnerability belongs to something shared rather than to one model's idiosyncrasies. Second, nobody has a satisfying explanation. [Biggio and Roli](https://doi.org/10.1016/j.patcog.2018.07.023) (2018) survey a decade of the field and the question remains open.

### The forward-and-backward symmetry is what makes all of this cheap

Because [the backward pass is the same kind of operation as the forward pass](/study/backpropagation/), obtaining $$\partial L/\partial x$$ costs about one extra pass. Occlusion-style methods, which hide part of the image and re-run the model, cost one forward pass per region tested. That difference in cost is why gradient-based methods became the default, and it is a computational fact rather than a claim that they answer the question better.

## Where this touches my work

Both halves of this bear on auditing, and they cut in opposite directions.

The encouraging half is that a trained model can be interrogated with nothing but its own gradients, which is the situation an external reviewer is usually in: weights, no training data, no ability to retrain.

The discouraging half is the adversarial result. A perturbation invisible to a clinician can move a prediction across a decision boundary, which means agreement between a model and a reader on an image says nothing about what would happen to a slightly different image. Transferability makes it worse, because it suggests the exposure is not specific to one model that could simply be replaced.

I also take a caution about visualisation from this. Class visualisation and style transfer both produce output that looks like understanding, and in both cases what is actually established is that an objective was minimised. The gap between "this optimisation converged" and "the model represents this concept" is the same gap I care about between a plausible explanation and a faithful one.

## What I have not resolved

Whether adversarial robustness and evidence validity are the same property seen from two sides, or genuinely different things. A model could plausibly rely on correct clinical evidence and still be fragile to imperceptible perturbation, and I do not know whether that combination actually occurs.

## References

- Gatys, Ecker & Bethge (2016). [Image Style Transfer Using Convolutional Neural Networks](https://doi.org/10.1109/CVPR.2016.265). CVPR.
- Biggio & Roli (2018). [Wild patterns: Ten years after the rise of adversarial machine learning](https://doi.org/10.1016/j.patcog.2018.07.023). *Pattern Recognition*.
