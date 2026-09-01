---
layout: post
title: "An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale"
date: 2026-04-04 12:00:00 +0900
venue: "ICLR 2021"
authors: "Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, et al. (2021)"
description: "The Vision Transformer paper — patches as tokens, no convolutional inductive bias — read for what it costs in data efficiency, since that cost matters directly for medical-imaging datasets orders of magnitude smaller than the ones ViT was trained on."
related_posts: false
---

**Paper.** *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale* — [ICLR 2021](https://arxiv.org/abs/2010.11929)

## Why I read it

Vision Transformers increasingly appear as backbones in medical-imaging papers, sometimes swapped in for a CNN with little discussion of the tradeoff. I wanted to reread the original paper specifically for its data-scale caveats, since medical datasets rarely approach the scale ViT was designed around.

## What the paper claims

ViT splits an image into fixed-size patches (16×16 pixels), linearly embeds each as a token, and feeds the sequence through a standard Transformer encoder — the same architecture used for text, with no convolutional inductive biases like locality or translation equivariance built in. The headline result is that, given enough pretraining data (hundreds of millions of images), ViT matches or exceeds CNNs on image classification. The paper is explicit, however, that on mid-sized datasets without that scale of pretraining, ViT underperforms comparable CNNs — the lack of built-in inductive bias has to be learned from data instead of assumed, and that requires a lot of data.

## What convinced me

The paper's own ablation is the most useful part for my purposes: it shows the CNN-versus-ViT gap shrinking and then reversing specifically as pretraining data scale increases, which isolates data scale as the actual variable driving ViT's advantage rather than the architecture being unconditionally superior.

## What it leaves open

The paper doesn't examine what specifically a ViT learns to substitute for the missing locality bias when data is abundant, or how that substitution behaves when the input distribution (natural photographs) differs sharply from the deployment distribution (radiographs, ultrasound). Medical-imaging transfer is outside its scope entirely.

## What I take from it

Given how directly the paper ties ViT's advantage to pretraining scale, I now treat "we used a Vision Transformer backbone" in a medical-imaging paper as a flag to check what it was pretrained on and how much data was used to fine-tune it — a ViT fine-tuned on a few thousand medical images, without the hundreds-of-millions-of-image pretraining this paper relies on, may be exactly the underperforming, under-constrained regime the original paper warns about, more prone to picking up spurious global correlations than a CNN with useful built-in locality bias would be.
