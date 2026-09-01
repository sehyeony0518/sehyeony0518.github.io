---
layout: post
title: "Swin Transformer: Hierarchical Vision Transformer Using Shifted Windows"
date: 2026-06-13 12:00:00 +0900
venue: "ICCV 2021"
authors: "Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng Zhang, Stephen Lin, Baining Guo (2021)"
description: "A hierarchical, windowed Transformer designed to fix ViT's fixed-scale, quadratic-cost weaknesses for dense prediction — the backbone choice behind a growing share of medical image segmentation papers."
related_posts: false
---

**Paper.** *Swin Transformer: Hierarchical Vision Transformer using Shifted Windows* — [ICCV 2021](https://arxiv.org/abs/2103.14030)

## Why I read it

Segmentation-focused medical-imaging papers increasingly use Swin Transformer rather than plain ViT, and I wanted to understand specifically what problem it's solving, since segmentation is a dense, per-pixel task where ViT's original design has real limitations.

## What the paper claims

Plain ViT operates at a single, fixed scale and its global self-attention cost grows quadratically with image size, which is a poor fit for dense prediction tasks like detection and segmentation that need multi-scale feature maps and high-resolution inputs. Swin computes self-attention within local, non-overlapping windows (making cost linear in image size) and shifts the window partition between successive layers so information can still flow across window boundaries, while merging patches at deeper layers to build a hierarchical, multi-scale feature pyramid analogous to a CNN's.

## What convinced me

The shifted-window mechanism is a genuinely clever fix for a real, identified weakness — restricting attention to windows brings back some of the locality bias plain ViT deliberately removed, and the hierarchical merging gives the multi-scale representation that dense prediction tasks need but single-scale ViT lacks. It's architecturally closer to a CNN than plain ViT is, which explains why it transfers more readily to segmentation.

## What it leaves open

The paper's evaluation is on natural-image detection and segmentation benchmarks (COCO, ADE20K); nothing here speaks to how the reintroduced locality bias interacts with medical-image-specific structure, or whether window-based attention has failure modes specific to the kind of diffuse, texture-based findings (like liver steatosis) that don't have clean local boundaries the way object-detection targets do.

## What I take from it

Swin is a reasonable default for medical segmentation specifically because it reintroduces locality and multi-scale structure that plain ViT gave up — which means the ViT data-efficiency caveat I noted in my review of the original ViT paper applies less directly here. But it's still worth checking, for any Swin-based medical segmentation paper, whether its performance advantage is being benchmarked against a well-tuned CNN baseline (like a U-Net) rather than only against plain ViT, since that's the comparison that actually tells you whether the added architectural complexity is earning its keep.
