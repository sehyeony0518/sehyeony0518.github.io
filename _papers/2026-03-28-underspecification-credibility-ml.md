---
layout: post
title: "Underspecification Presents Challenges for Credibility in Modern Machine Learning"
date: 2026-03-28 12:00:00 +0900
venue: "JMLR"
authors: "Alexander D'Amour, Katherine Heller, Dan Moldovan, Ben Adlam, Babak Alipanahi, Alex Beutel, Christina Chen, Jonathan Deaton, et al. (2020)"
description: "Two models with identical training accuracy, identical architecture, and different random seeds can behave completely differently under distribution shift — a Google-scale audit of just how common this is, including in a dermatology model."
related_posts: false
---

**Paper.** *Underspecification Presents Challenges for Credibility in Modern Machine Learning* — [arXiv (2020)](https://arxiv.org/abs/2011.03395)

## Why I read it

This is one of the papers most frequently cited as background for why internal validation accuracy is an unreliable signal of real-world reliability, and I wanted to understand the mechanism directly rather than just the headline claim.

## What the paper claims

An ML pipeline is "underspecified" when many different models — differing only in incidental training choices like random seed — achieve statistically indistinguishable performance on the training and standard test distribution, yet behave very differently once evaluated on a shifted distribution or a stress test targeting a specific failure mode. The authors demonstrate this across a wide range of domains, including a dermatology skin-condition classifier, where models with equivalent standard test accuracy showed materially different, and differently biased, performance across skin-tone subgroups depending only on the random seed used during training.

## What convinced me

The controlled setup is what makes the finding hard to dismiss: same architecture, same training data, same standard-test accuracy, different seed, different real-world behavior — including different fairness properties. That rules out "the models are actually different in some principled way we haven't measured" as an easy explanation; the difference is coming from the underdetermined part of the optimization, not from a meaningful modeling choice.

## What it leaves open

The paper is diagnostic — it demonstrates that standard test accuracy underspecifies a model's behavior on stress tests, but doesn't offer a general recipe for which stress tests to run for an arbitrary new model, or how to specify a training pipeline tightly enough to eliminate the problem. Each domain needs its own targeted stress tests, which the paper illustrates rather than automates.

## What I take from it

This paper is the strongest single argument I've read for never trusting a single trained checkpoint's clinical behavior based on standard-test accuracy alone — even holding architecture and data completely fixed, the specific model you happened to get from one training run may or may not be safe on the subgroup or shift you care about. For any clinical-faithfulness audit, this means testing multiple seeds of "the same" model is not a redundant sanity check; it's often the only way to see whether a faithfulness property is a property of the training setup or an accident of one run.
