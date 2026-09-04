---
layout: post
title: "Assessing the Trustworthiness of Saliency Maps for Localizing Abnormalities in Medical Imaging"
date: 2026-05-09 12:00:00 +0900
venue: "Radiology: Artificial Intelligence"
authors: "Arun, Gaw, Singh, Chang, Aggarwal, Chen, Hoebel, Gupta, Patel, Gidwani, Adebayo, Li, Kalpathy-Cramer (2021)"
description: "Radiology-specific saliency evaluation: sanity checks and human-alignment tests applied directly to chest radiograph localization tasks."
related_posts: false
---

**Paper.** *Assessing the Trustworthiness of Saliency Maps for Localizing Abnormalities in Medical Imaging*. [Radiology: Artificial Intelligence 2021](https://pubs.rsna.org/doi/10.1148/ryai.2021200267)

## Why I read it

Medical papers frequently interpret a saliency map as if it were a lesion detector. I read this study because it evaluates that assumption against explicit localization ground truth and against several basic reliability tests, rather than judging heatmaps by visual appeal.

## What the paper claims

Eight commonly used saliency methods are assessed on pneumothorax segmentation and pneumonia detection. The tests cover localization utility, sensitivity to weight randomization, repeatability across repeated runs, and reproducibility across models. Dedicated U-Net and RetinaNet localization models provide task-appropriate reference points.

## What convinced me

Every saliency method failed at least one criterion. For pneumothorax, saliency-map AUPRC ranged from 0.024 to 0.224, while the U-Net reached 0.404. For pneumonia, saliency AUPRC ranged from 0.160 to 0.519, below the RetinaNet value of 0.596. Several methods also changed little after model weights were randomized, showing that a plausible image overlay can be weakly tied to the learned predictor.

## What it leaves open

The paper tests particular methods, backbones, and localization tasks; it does not imply that every attribution method is useless for every scientific question. A saliency map may still help generate a hypothesis or identify a gross artifact. What it cannot provide without further validation is a reliable lesion boundary or a stand-alone certificate of causal evidence use.

## What I take from it

The explanation target must match the validation target. If the claim is localization, compare with localization annotations and a trained localization model. If the claim is faithfulness, use model-sensitive perturbations or interventions. Visual plausibility should be treated as the beginning of an audit, not its result.
