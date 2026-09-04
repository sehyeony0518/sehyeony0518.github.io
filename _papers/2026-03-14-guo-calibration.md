---
layout: post
title: "On Calibration of Modern Neural Networks"
date: 2026-03-14 12:00:00 +0900
venue: "ICML"
authors: "Guo, Pleiss, Sun, Weinberger (2017)"
description: "Modern networks are more accurate and less calibrated than their predecessors, and the fix (temperature scaling) is almost embarrassingly simple."
related_posts: false
---

**Paper.** *On Calibration of Modern Neural Networks*. [ICML 2017](https://arxiv.org/abs/1706.04599)

## Why I read it

Clinical deployment requires more than ranking patients correctly. A probability of 0.9 should correspond to an event rate near 90% in the population where the model is used. This paper is the standard reference for why modern neural networks often fail that requirement and how a simple post hoc correction can help.

## What the paper claims

The authors show that architectural and training choices (including depth, width, batch normalization, and weight decay) can improve accuracy while worsening confidence calibration. They compare several post hoc methods and find that temperature scaling, a single scalar applied to logits on a held-out validation set, is a strong and simple baseline.

## What convinced me

On CIFAR-100 with ResNet-110, expected calibration error fell from 16.53% to 1.26% after temperature scaling, while class predictions and ranking were unchanged. The simplicity of that result is important: calibration is a separable validation target, and a model can be recalibrated without pretending its discrimination improved.

## What it leaves open

Calibration is distribution-specific. A temperature learned at one hospital can fail after prevalence, scanner, or population shift. ECE also depends on binning and can hide class- or subgroup-specific errors. A calibrated shortcut model remains a shortcut model, and calibration does not repair fairness, causal validity, or poor discrimination.

## What I take from it

Every diagnostic model should report calibration alongside AUROC and threshold metrics, with uncertainty and subgroup analysis. Post hoc temperature scaling is a baseline, not the end point. Under external shift, recalibration and evidence auditing need to be evaluated together.
