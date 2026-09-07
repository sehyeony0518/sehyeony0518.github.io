---
layout: study_note
title: "Attribution, Attention, and Counterfactual Explanations"
description: "The main families of post-hoc explanation for medical images, and what each actually measures."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "alignment"
category_title: "Clinical Alignment & Interpretability"
order: 3
source: "Independent study"
written: true
updated: "2026-09-08"
---

A saliency map, an attention matrix, and an edited image answer different questions about a model. I treat each explanation as the result of a specified computation, whose meaning depends on its target, reference, and assumptions.

## Why it matters here

Medical image explanations are often presented in a similar visual form even when their underlying quantities differ. A colored overlay might summarize gradients, feature activations, or a response to masking. Without the method and target, the display does not tell me which claim about the prediction it can support.

For clinical faithfulness auditing, this determines which explanation I would use and how I would evaluate it. In gallbladder ultrasound, identifying an anatomical region, measuring sensitivity to a clinical feature, and constructing a prediction-changing edit are distinct tasks. I need to choose the task before choosing the visualization.

## The core ideas

### Gradient attribution describes sensitivity to inputs

An input gradient measures how a selected output changes locally with the input. Small gradients can occur in saturated regions even when a feature matters over a larger change. [Integrated Gradients](https://proceedings.mlr.press/v70/sundararajan17a.html) accumulates gradients along a path from a reference input, assigning contributions relative to that reference. The baseline and path therefore help define the explanation. A mathematically convenient dark image is not automatically a clinically meaningful absence of ultrasound evidence, and attribution values do not become tissue measurements.

### Perturbation methods depend on what replaces a feature

Occlusion measures prediction changes when a patch is replaced. Local surrogate methods fit a simpler approximation to model behavior around perturbed samples. SHAP-style methods allocate prediction differences across feature coalitions under a specified treatment of missing features. Each approach depends on how the comparison inputs are generated. Masking can destroy anatomy, while realistic replacement can insert new evidence. I would interpret the result as behavior under the stated perturbations, with special attention to correlated regions and the quality of a surrogate's local fit.

### Class activation maps provide a spatial summary

[Grad-CAM](https://arxiv.org/abs/1610.02391) uses gradients of a selected score to weight feature maps and produce a coarse spatial map. The selected layer determines its resolution and representation, while subsequent resizing makes it convenient to overlay on the image. That overlay is not a segmentation boundary or a complete decomposition of the prediction. Highlighting the gallbladder can locate a relevant region without distinguishing whether the contributing pattern is lesion morphology, surrounding tissue, or an acquisition characteristic within the same region.

### Attention weights describe part of the computation

Attention combines value representations using learned, input-dependent weights. Inspecting those weights is a post-hoc use of an internal mechanism, not a separate explanation guarantee. The contribution to the final output also depends on the values, other heads, residual paths, and later computation. [Jain and Wallace](https://aclanthology.org/N19-1357/) demonstrated in NLP models that very different attention distributions could yield equivalent predictions. I take this as a reason to test the explanatory claim in the relevant architecture, rather than transfer a universal conclusion to ultrasound.

### Counterfactual explanations search for a changed answer

A counterfactual explanation typically seeks an alternative input that changes the prediction while satisfying constraints on similarity or plausibility. What counts as a small change depends on the distance and constraints, and several different edits may succeed. A generated image can also exploit the classifier's vulnerabilities. I would separately check whether the output changed, whether the intended feature changed, and whether other clinical properties were preserved. A successful label flip establishes none of those additional properties by itself.

## Where it touches my work

For a gallbladder ultrasound audit, I would define the output being explained, including whether it is a class score or a probability, and record the layer, baseline, masking rule, or editing constraints. I would then compare the explanation with independent clinical descriptors and with measured responses to defensible changes. Agreement between several methods could strengthen a hypothesis, but shared assumptions could also produce shared errors. I would retain disagreements and failed edits as part of the evidence about what remains uncertain.

## What I have not resolved

- What reference input represents absence of a finding without removing the acquisition context needed to interpret ultrasound?
- Which perturbations preserve enough image realism to test reliance on a local feature?
- When explanation methods disagree, how can I determine whether they measure different properties or whether one fails its intended claim?
- How should I assess generated edits that appear plausible but may change subtle clinical evidence?
