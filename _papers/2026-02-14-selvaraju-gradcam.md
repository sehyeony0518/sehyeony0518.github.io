---
layout: post
title: "Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization"
date: 2026-02-14 12:00:00 +0900
venue: "ICCV"
authors: "Selvaraju, Cogswell, Das, Vedantam, Parikh, Batra (2017)"
description: "The saliency method almost every medical-imaging paper cites — and a good place to be precise about what its heatmap actually certifies."
related_posts: false
---

**Paper.** *Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization* — [ICCV 2017](https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html)

## Why I read it

Grad-CAM is the default explanation in much of medical imaging, so it is important to understand exactly what it computes before using a heatmap as evidence of clinical reasoning. I read the original paper to separate its intended claim from the stronger claims later attached to it.

## What the paper claims

Grad-CAM averages the gradient of a target score with respect to each channel of the final convolutional feature map, then uses those weights to form a coarse, class-discriminative localization map. It requires no architectural change or retraining and can be applied to classification, captioning, and visual-question-answering models.

## What convinced me

The method is simple, model-conditioned, and broadly applicable. The original work evaluates weakly supervised localization, identifies dataset biases, and includes human studies showing that visualizations can help users distinguish stronger from weaker models. Those experiments support Grad-CAM as an accessible diagnostic interface, especially for generating hypotheses about gross spatial focus.

## What it leaves open

A Grad-CAM region is not a lesion segmentation and does not prove that the highlighted pixels were causally necessary. Its resolution is limited by the final feature map, and later sanity-check studies show that visually plausible maps can be insensitive to parameters or unstable across models. The choice of layer and target also changes the result.

## What I take from it

I use Grad-CAM as a screening tool, not a faithfulness endpoint. A clinical claim requires a matching test: lesion overlap for localization, parameter randomization for model dependence, and targeted perturbation or intervention for causal reliance. The heatmap suggests where to investigate; it does not finish the investigation.
