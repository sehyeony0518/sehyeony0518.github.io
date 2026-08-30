---
layout: post
title: "Sanity Checks for Saliency Maps"
date: 2026-04-11 12:00:00 +0900
venue: "NeurIPS"
authors: "Adebayo, Gilmer, Muelly, Goodfellow, Hardt, Kim (2018)"
description: "Randomize the model's weights or the labels — some popular saliency methods produce almost the same heatmap anyway."
related_posts: false
---

**Paper.** *Sanity Checks for Saliency Maps* — [NeurIPS 2018](https://arxiv.org/abs/1810.03292)

## Why I read it

Before trusting any attribution method as evidence in an audit, I wanted to know whether the field has actually tested that these methods respond to the thing they claim to explain — the trained model's learned parameters.

## The test

Two simple randomization tests: **model parameter randomization** (progressively randomize the weights, layer by layer, from output to input, and check whether the saliency map changes) and **data randomization** (train the same architecture on randomly shuffled labels, then compare the resulting saliency maps to the original). A saliency method that is actually explaining the trained model's learned function should produce visibly different, degrading maps under both tests.

Several widely used methods — including Guided Backprop and Guided Grad-CAM in their tested form — failed to change meaningfully even when most of the network's weights were randomized. The maps looked almost like edge detectors, sensitive to the input image and architecture but largely insensitive to what the model had actually learned.

## Why this changed how I read attribution figures

The uncomfortable implication is that a saliency map can look plausible — sharp, focused on anatomically sensible structure — for reasons that have little to do with the specific weights learned during training. A visually convincing heatmap is not, by itself, evidence that the method is measuring the model rather than the input.

Gradient-based methods that do incorporate the model's actual gradient (their tested variant of Grad-CAM, and gradient × input) fared better under these specific tests, which is part of why I read Grad-CAM's localization claims as more defensible than some alternatives — while still keeping in mind that passing this test establishes model-sensitivity, not clinical validity.

## What I take from it

Any attribution method I use in an audit needs to pass some version of this sanity check before I treat its output as evidence about the model. "The heatmap looks reasonable" and "the heatmap is sensitive to the model's learned weights" are different claims, and only the second one is falsifiable in the way this paper demonstrates.
