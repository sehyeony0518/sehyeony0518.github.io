---
layout: post
title: "Knee-xRAI: An Explainable AI Framework for Automatic Kellgren-Lawrence Grading of Knee Osteoarthritis"
date: 2026-11-27 12:00:00 +0900
venue: "arXiv preprint"
authors: "Azmul A. Irfan, Nur Ahmad Khatim, Alfan Alfian Irfan, Achmad Zaki, Erike A. Suwarsono, Mansur M. Arief (2026)"
description: "A framework built around the fact that a single-grade disagreement on the KL scale can redirect a patient from conservative therapy to a surgical pathway — explainability motivated directly by clinical stakes, not as a generic add-on."
related_posts: false
---

**Paper.** *Knee-xRAI: An Explainable AI Framework for Automatic Kellgren-Lawrence Grading of Knee Osteoarthritis* — arXiv preprint (2026)

## Why I read it

I read Knee-xRAI because it attempts something stronger than attaching a heatmap to a Kellgren-Lawrence classifier. The pipeline first measures the radiographic findings that define the grade — joint-space narrowing, osteophytes, and subchondral sclerosis — and then exposes those measurements as an auditable evidence surface.

## What the paper claims

The framework combines a U-Net++ module for joint-space measurements, a site-specific multitask network for OARSI osteophyte grades, and a texture-based sclerosis detector. These outputs form a 50-dimensional structured vector. The authors evaluate an XGBoost–SHAP audit path using only that vector, and a higher-capacity ConvNeXt hybrid path that also receives unrestricted visual features.

## What convinced me

The most informative result is the intervention study, not the SHAP plot. On 8,260 OAI-derived radiographs, the joint-space module reached a Dice score of 0.8909 and an mJSW ICC of 0.8674. The deployment path achieved QWK 0.8436 and AUC 0.9017. When joint-space evidence was removed, KL4 recall fell from 88% to 0%, while early grades were much less affected — behavior that matches the clinical construction of the KL scale.

## What it leaves open

The explanation and deployment paths are not identical. The fully structured audit path reached QWK 0.6294, substantially below the ConvNeXt hybrid, so SHAP explanations from the former do not completely account for the latter's decision. The feature annotations were also available only for subsets, and their inter-reader agreement was not fully quantified.

## What I take from it

Component-level prediction plus targeted ablation is much more persuasive than visual plausibility alone. At the same time, an auditable surrogate is not enough: the evidence test must apply to the model that will actually be deployed.
