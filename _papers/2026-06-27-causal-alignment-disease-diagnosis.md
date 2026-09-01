---
layout: post
title: "Learning Causal Alignment for Reliable Disease Diagnosis"
date: 2026-06-27 12:00:00 +0900
venue: "ICLR 2025"
authors: "Mingzhou Liu, Ching-Wen Lee, Xinwei Sun, Xueqing Yu, Qiao Yu, Yizhou Wang (2025)"
description: "A causal framing of the shortcut-learning problem in disease diagnosis — trying to explicitly align a model's learned representation with the causal structure of disease, not just penalize known spurious features after the fact."
related_posts: false
---

**Paper.** *Learning Causal Alignment for Reliable Disease Diagnosis* — [ICLR 2025](https://arxiv.org/abs/2310.01766)

## Why I read it

Most shortcut-mitigation methods I've read work by identifying a specific known confound and suppressing the model's reliance on it. A causal-alignment framing promises something more general — training the model to respect the causal structure connecting disease to imaging evidence, rather than reacting to shortcuts one at a time. I wanted to see how that generality is actually achieved.

## What the paper claims

The authors frame reliable disease diagnosis as a problem of aligning a model's learned representation with the underlying causal graph relating disease state to observed imaging evidence, rather than only the statistical correlation a standard classifier fits. The approach is meant to produce diagnoses that remain reliable even when spurious, non-causal correlations in the training distribution shift or disappear at deployment.

## What convinced me

Framing the problem causally rather than correlationally is the right level of abstraction for shortcut learning generally — a shortcut is, definitionally, a correlation that isn't causal, so a method that directly targets causal structure is attacking the actual source of the problem rather than a specific symptom of it (one particular confound) at a time.

## What it leaves open

Causal alignment methods generally require some assumption about the causal graph's structure, or interventional/multi-environment data, to be identifiable — and how well those assumptions hold for real clinical imaging, where the true causal graph relating pathology to image formation is only partially known, is the hard, unresolved part of applying this framework in practice rather than in a controlled benchmark.

## What I take from it

This paper represents the more ambitious end of the shortcut-mitigation spectrum I've been reading across — where RRR-style methods correct one known shortcut at a time, causal alignment aims to make the whole training objective respect causal structure by design. Neither fully solves the problem: one needs the shortcut to already be named, the other needs (partial) knowledge of the causal graph. Knowing where a given mitigation method sits on that spectrum, and what assumption it's quietly relying on, is now a standard part of how I read this literature.
