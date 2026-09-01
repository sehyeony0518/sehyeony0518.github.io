---
layout: post
title: "Deep Residual Learning for Image Recognition"
date: 2025-11-15 12:00:00 +0900
venue: "CVPR 2016"
authors: "Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun (2016)"
description: "The residual-connection paper — read as a reminder that the backbone underneath most medical-imaging classifiers was optimized for making very deep networks trainable, not for clinical evidence."
related_posts: false
---

**Paper.** *Deep Residual Learning for Image Recognition* — [CVPR 2016](https://arxiv.org/abs/1512.03385)

## Why I read it

ResNet is the default backbone cited in an enormous share of the medical-imaging AI I read, often without any discussion of why. I wanted to revisit the actual motivating problem it solved, since that motivation shapes what kind of features the architecture is naturally good at extracting.

## What the paper claims

He et al. observed that simply stacking more layers in a plain convolutional network eventually makes training *harder*, not easier — deeper plain networks showed higher training error than shallower ones, a degradation problem distinct from overfitting. Their fix is the residual connection: instead of learning a direct mapping, each block learns a residual (a difference) added to its input via a skip connection, which makes very deep networks (they trained up to 152 layers) tractable to optimize and pushed ImageNet classification accuracy meaningfully forward, winning ILSVRC 2015.

## What convinced me

The paper's evidence is unusually direct: it isolates the degradation problem with controlled experiments (deeper plain nets doing strictly worse than shallower ones on *training* error, ruling out overfitting as the explanation) before proposing the fix, and then shows the residual formulation resolves exactly that failure mode. It's a clean example of a genuine architectural insight rather than a scale-up dressed as one.

## What it leaves open

The paper is entirely about optimization dynamics and ImageNet-style natural-image recognition; it says nothing about which features a residual network prioritizes on out-of-distribution images like radiographs or ultrasound, or about how skip connections interact with a network's tendency to exploit spurious, easy-to-fit correlations — a question later shortcut-learning work had to address separately.

## What I take from it

When a medical-imaging paper reports its architecture as "ResNet-50 backbone" without further justification, I now read that as a statement about training tractability and transfer-learning convenience, not a statement about suitability for the clinical task. The architecture choice and the evidence-faithfulness question are separate axes, and conflating "state-of-the-art backbone" with "clinically sound reasoning" is a mistake worth actively guarding against in my own reviews.
