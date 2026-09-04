---
layout: post
title: "Concept Bottleneck Models"
date: 2025-12-27 12:00:00 +0900
venue: "ICML 2020"
authors: "Pang Wei Koh, Thao Nguyen, Yew Siang Tang, Stephen Mussmann, Emma Pierson, Been Kim, Percy Liang (2020)"
description: "The paper that named and formalized the concept bottleneck: asking, using the paper's own example, whether a model would still predict severe arthritis if it didn't think there was a bone spur."
related_posts: false
---

**Paper.** *Concept Bottleneck Models*. [ICML 2020](https://arxiv.org/abs/2007.04612)

## Why I read it

Concept bottleneck models provide one of the clearest architectural answers to the faithfulness problem: make the final prediction pass through human-interpretable concepts and allow a user to correct those concepts at test time.

## What the paper claims

A concept encoder first predicts supervised attributes, and a downstream model predicts the target from those concept values. The paper evaluates sequential and joint training, with and without additional information paths, on CUB and an OAI knee-radiograph task. Concept intervention tests whether correcting selected concepts improves the final prediction.

## What convinced me

The intervention result is the key evidence. On the OAI task, correcting only two concepts reduced prediction RMSE from above 0.4 to around 0.3 in the reported setting. The models also remained competitive with standard black boxes, showing that an interpretable interface need not require a large performance sacrifice. Unlike an auxiliary concept head, the bottleneck creates a concrete route through which expert corrections can affect the output.

## What it leaves open

The guarantee weakens when information bypasses the concept layer, and a strict bottleneck can fail when the concept vocabulary is incomplete. Concept labels may be costly or subjective, and independently correcting one concept can create combinations that were rare or impossible during training. Interpretability therefore depends on both architectural exclusivity and concept quality.

## What I take from it

A concept model should be judged by more than concept accuracy. I would test bottleneck completeness, leakage around the bottleneck, calibration of each concept, and the gain from realistic expert interventions. The strongest explanation is one that is editable and demonstrably controls the decision.
