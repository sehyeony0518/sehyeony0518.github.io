---
layout: post
title: "On Calibration of Modern Neural Networks"
date: 2026-03-14 12:00:00 +0900
venue: "ICML"
authors: "Guo, Pleiss, Sun, Weinberger (2017)"
description: "Modern networks are more accurate and less calibrated than their predecessors — and the fix (temperature scaling) is almost embarrassingly simple."
related_posts: false
---

**Paper.** *On Calibration of Modern Neural Networks* — [ICML 2017](https://arxiv.org/abs/1706.04599)

## Why I read it

Every clinical faithfulness question I ask eventually runs into a prior question: does the model's confidence mean anything? A model that is accurate but poorly calibrated can still produce a "90% probability" that is wrong 40% of the time. That gap matters more in medicine than almost anywhere else, since confidence is often what determines whether a clinician double-checks a result.

## The finding

Across a range of architectures, the authors show that model capacity, batch normalization, and reduced weight decay — the ingredients responsible for modern accuracy gains — simultaneously **increase miscalibration**, even as accuracy improves. Deeper and wider is not calibration-neutral. It is a trade the field made implicitly, in pursuit of a different number.

Their diagnostic tool, the reliability diagram plotting confidence against observed accuracy, is one of those visualizations I now think should accompany every deployed classifier and rarely does.

## The fix and its limits

Temperature scaling — dividing the logits by a single learned scalar before the softmax — recovers most of the calibration loss with essentially no cost to accuracy, and outperforms more complex alternatives (Platt scaling, isotonic regression, vector/matrix scaling) on their benchmarks. The simplicity is almost suspicious, and that's the point worth sitting with: calibration and accuracy are close to separable problems, at least for i.i.d. test data.

That "at least for i.i.d. test data" is the boundary I care about. Temperature scaling fits one scalar on a held-out set from the *same* distribution. Nothing here guarantees the calibration transfers across sites, scanners, or patient populations — which is precisely the setting shortcut learning shows up in. A model can be shortcut-driven and well-calibrated on its own test set simultaneously.

## What I take from it

Calibration is necessary infrastructure for any auditing claim that touches confidence, uncertainty, or thresholds — but it is orthogonal to whether the model's evidence is clinically valid. Reporting a reliability diagram tells you the number can be trusted as a number. It does not tell you what the number is about.
