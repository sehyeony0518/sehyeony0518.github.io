---
layout: post
title: "Evaluating Shortcut Utilization in Deep Learning Disease Classification Through Counterfactual Analysis"
date: 2026-10-09 12:00:00 +0900
venue: "MIDL 2025"
authors: "Vibujithan Vigneshwaran, Emma A.M. Stanley, Raissa Souza, Erik Ohara, Matthias Wilms, Nils D. Forkert (2025)"
description: "A counterfactual-generation approach to quantifying shortcut reliance in disease classifiers, in the same spirit as RoentMod but framed as a general evaluation method rather than a modality-specific tool."
related_posts: false
---

**Paper.** *Evaluating Shortcut Utilization in Deep Learning Disease Classification through Counterfactual Analysis* — MIDL 2025

## Why I read it

Many shortcut studies stop after showing that site or sex can be decoded from a representation. I read this paper because it asks the more consequential question: how much of the diagnostic performance actually depends on that protected attribute?

## What the paper claims

The authors fit a causal generative model to penultimate-layer activations and construct counterfactual activations in which a protected attribute is removed while other modeled factors are retained. The change in disease-classification performance is then interpreted as the amount of shortcut utilization attributable to that factor. Importantly, the intervention is performed in activation space, not by editing the input MRI.

## What convinced me

The Parkinson's disease study includes 835 T1-weighted MRI scans from nine sites. Removing site information reduced AUROC from about 0.74 to 0.65, suggesting substantial dependence on acquisition site. Removing sex changed AUROC by only about 0.004. The contrast is valuable because both variables may be encoded, yet only one materially supports the diagnostic decision.

## What it leaves open

The estimate is only as credible as the assumed causal graph and the generative model used to create the counterfactual activation. An activation that is mathematically valid may not correspond to any plausible image or patient. A performance drop also quantifies dependence without identifying which anatomical evidence should replace the shortcut.

## What I take from it

The paper provides a much stronger test than metadata decodability: intervene, then measure the task consequence. I would still triangulate activation-space counterfactuals with image-level perturbations, cross-site evaluation, and clinically specified evidence tests before making a causal claim.
