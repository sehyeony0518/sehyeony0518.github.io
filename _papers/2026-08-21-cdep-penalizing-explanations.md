---
layout: post
title: "Interpretations Are Useful: Penalizing Explanations to Align Neural Networks with Prior Knowledge"
date: 2026-08-21 12:00:00 +0900
venue: "ICML 2020"
authors: "Laura Rieger, Chandan Singh, W. James Murdoch, Bin Yu (2020)"
description: "CDEP — penalizing a model's contextual-decomposition-based explanation directly during training, so an explanation isn't just a diagnostic afterward but an actionable lever to fix the model."
related_posts: false
---

**Paper.** *Interpretations are Useful: Penalizing Explanations to Align Neural Networks with Prior Knowledge* — [ICML 2020](https://arxiv.org/abs/1909.13584)

## Why I read it

This paper's opening framing — that most explainable-AI methods stop after providing insight, without offering a way to act on that insight to actually improve the model — is a criticism I've come to share after reading a lot of interpretability papers. I wanted to see the specific mechanism CDEP proposes for closing that loop.

## What the paper claims

The authors introduce Contextual Decomposition Explanation Penalization (CDEP), which uses contextual decomposition (a way of attributing a prediction to groups of input features) not just to generate an explanation, but as a differentiable penalty term added directly to the training loss — explicitly discouraging the model from basing its prediction on feature groups a domain expert has flagged as irrelevant or spurious, while training.

## What convinced me

Making the explanation method itself part of the loss function, rather than a separate diagnostic run after training, is the structural choice that actually closes the detect-then-fix loop this paper is arguing for. It sits in the same family as Right for the Right Reasons (constraining input gradients), but works at the level of feature *groups* via contextual decomposition rather than individual input gradients, which is a more natural fit for cases where the spurious signal is a region or group of correlated features rather than a single input dimension.

## What it leaves open

Like RRR, CDEP needs a human to already know and annotate which feature groups are irrelevant or spurious — it corrects a named problem rather than discovering an unknown one. The paper also doesn't fully characterize how the penalty trades off against raw predictive accuracy when the "irrelevant" feature group actually carries some genuine, if weaker, signal.

## What I take from it

CDEP and RRR are converging evidence that training-time explanation penalties are a viable, general strategy once a shortcut is identified — the harder unsolved problem across this whole line of work remains discovery, not correction. For my own research, that keeps sharpening the same question: the tools for fixing a known shortcut are increasingly mature; the tools for finding shortcuts nobody thought to name in advance are where the real gap still is.
