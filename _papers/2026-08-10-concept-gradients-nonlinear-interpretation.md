---
layout: post
title: "Concept Gradients: Concept-Based Interpretation Without Linear Assumption"
date: 2026-08-10 12:00:00 +0900
venue: "ICLR 2023"
authors: "Andrew Bai, Chih-Kuan Yeh, Neil Y. C. Lin, Pradeep Ravikumar, Cho-Jui Hsieh (2023)"
description: "TCAV assumes a concept occupies a linear direction in activation space. Concept Gradients drops that assumption and, in a medical case study, tracks concept importance scores against mortality-risk descriptions already published in the clinical literature."
related_posts: false
---

**Paper.** *Concept Gradients: Concept-Based Interpretation Without Linear Assumption* — [ICLR 2023](https://github.com/jybai/concept-gradients)

## Why I read it

TCAV's Concept Activation Vectors, which I reviewed earlier in this collection, rest on an assumption I had absorbed without questioning: that a concept corresponds to a linear direction in some layer's activation space. This paper is the first I have found that names that assumption explicitly and asks what happens when it does not hold.

## What the paper claims

Concept Activation Vectors work by fitting a linear classifier that separates activations of concept-present examples from concept-absent examples, then using that classifier's normal vector as the concept's direction. The authors argue meaningful concepts do not generally lie in a linear subspace, and propose Concept Gradients (CG), which extends the idea to a general, potentially non-linear concept function: rather than a fixed direction, CG computes how a small change in the concept's value would affect the model's prediction, via the gradient of the prediction with respect to the concept function itself. In a case study on a medical dataset predicting mortality from 112 clinical input fields, CG concept-importance scores for individual complications were compared against mortality-risk descriptions drawn from the existing medical literature.

## What convinced me

The medical case study is structured as an external check rather than a self-report: the paper does not just show CG producing plausible-looking scores, it compares those scores against an independent source, published mortality-risk language for each complication, and reports that CG's ranking aligns with the literature description more closely than TCAV's does for the highest-risk complications. That is the same "does the model's stated evidence match what the literature already says" logic I want to apply to my own audits, applied here to validate an explanation method rather than a diagnostic model.

## What it leaves open

Comparing concept-importance scores against qualitative risk descriptions in the literature is itself an approximate benchmark. It does not establish that CG scores are causally faithful to the model's actual computation, only that they are more consistent with external clinical knowledge than the linear alternative on this one dataset and this one set of complications. Non-linear concept functions also require more modeling choices (how the concept function itself is fit) than a linear CAV does, which is a new source of assumptions this paper does not fully audit.

## What I take from it

This paper sharpened a question I now ask of every concept-based explanation method I encounter: what geometric assumption is being made about how the concept lives in activation space, and is that assumption ever tested against an independent source rather than just visual plausibility? A concept score that has been checked against outside clinical knowledge, the way CG's mortality-risk comparison is checked here, carries meaningfully more weight than one that has not.
