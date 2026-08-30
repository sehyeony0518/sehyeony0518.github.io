---
layout: post
title: "Assessing the Trustworthiness of Saliency Maps for Localizing Abnormalities in Medical Imaging"
date: 2026-05-09 12:00:00 +0900
venue: "Radiology: Artificial Intelligence"
authors: "Arun, Gaw, Singh, Chang, Aggarwal, Chen, Hoebel, Gupta, Patel, Gidwani, Adebayo, Li, Kalpathy-Cramer (2021)"
description: "Radiology-specific saliency evaluation: sanity checks and human-alignment tests applied directly to chest radiograph localization tasks."
related_posts: false
---

**Paper.** *Assessing the Trustworthiness of Saliency Maps for Localizing Abnormalities in Medical Imaging* — [Radiology: Artificial Intelligence 2021](https://pubs.rsna.org/doi/10.1148/ryai.2021200267)

## Why I read it

Adebayo et al.'s sanity checks were run on natural-image benchmarks. I wanted to know whether the same failure modes appear when the task is medical — localizing abnormalities on chest radiographs — where the clinical stakes of a misleading heatmap are much more concrete.

## What they did

The authors evaluated several common saliency methods against two criteria: **repeatability/reproducibility** (does the map stay stable under retraining and minor perturbation?) and **the same randomization sanity checks** from Adebayo et al., now applied to chest-radiograph abnormality localization instead of natural-image classification, alongside comparison to radiologist-annotated ground-truth regions.

The results echo the general-domain finding but ground it clinically: performance on standard localization metrics did not reliably predict whether a method passed the sanity checks, and methods varied substantially in how much they degraded under model randomization. Some methods that produced visually convincing, anatomically plausible heatmaps still showed limited sensitivity to whether the model had actually learned anything.

## Why the medical framing matters

This is the paper that convinced me the general machine-learning literature on explanation reliability doesn't automatically transfer its conclusions to medical imaging — but its *methodology* does. The specific ranking of which saliency method is most trustworthy can differ by task and modality, so the sanity-check protocol itself, not any single method's reputation, is the reusable contribution.

It also reframes localization evaluation: agreement with radiologist annotations is necessary but not sufficient, for the same reason internal test accuracy is not sufficient — a shortcut correlated with lesion location would also pass a localization-overlap check.

## What I take from it

Any saliency-based auditing tool I build for ultrasound needs its own version of this evaluation — modality-specific sanity checks, not an assumption that a method validated on chest X-rays or natural images carries its trustworthiness with it into a new domain.
