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

Grad-CAM appears in nearly every medical-imaging paper that claims interpretability, usually as a single figure: heatmap over the lesion, caption implying the model "looked at the right place." I wanted to go back to the original definition and be precise about what that figure licenses me to conclude.

## What it actually computes

Grad-CAM weights the final convolutional feature maps by the gradient of the target class with respect to each channel, then combines and upsamples them into a coarse localization map. It is architecture-general — no retraining, no modified network — which is exactly why it became the default choice for auditing an existing classifier.

The important detail is in the name: it is a **localization** method. It answers *which spatial regions most influenced the gradient of this class score*, at the resolution of the last convolutional layer, upsampled and smoothed. It was validated against human-annotated bounding boxes and weakly supervised segmentation — spatial correspondence tasks — not against clinical evidence correspondence.

## Why I'm careful with it

A heatmap that overlaps the lesion is compatible with at least three different explanations: the model used the lesion's texture appropriately; the model used a shortcut feature that happens to be co-located with the lesion (a marker, a boundary artifact); or the map itself is imprecise at that resolution and the overlap is partly coincidental. Later work (Adebayo et al.'s sanity checks, among others) showed some saliency methods are largely insensitive to model or label randomization — a caution I now read as directly relevant to how Grad-CAM claims should be qualified, even where Grad-CAM itself has held up comparatively well.

None of this makes Grad-CAM useless. It makes "the heatmap overlapped the lesion" a much weaker claim than the papers that cite it usually treat it as.

## What I take from it

Localization overlap is a necessary check, not a sufficient one. If I use Grad-CAM in my own auditing pipeline, I want to pair it with something that tests *whether* the highlighted region is causally load-bearing — ablation, counterfactual perturbation, or a metric that changes when that region is removed — rather than reporting the heatmap as the endpoint of the audit.
