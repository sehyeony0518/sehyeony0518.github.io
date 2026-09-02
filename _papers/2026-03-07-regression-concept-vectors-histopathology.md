---
layout: post
title: "Regression Concept Vectors for Bidirectional Explanations in Histopathology"
date: 2026-03-07 12:00:00 +0900
venue: "MICCAI 2018 Workshop"
authors: "Mara Graziani, Vincent Andrearczyk, Henning Müller (2018)"
description: "An extension of TCAV to continuous, graded concepts — used to show that nuclei texture, not just its presence, is a directional driver of tumor-grade predictions in lymph-node histopathology."
featured: true
related_posts: false
---

**Paper.** *Regression Concept Vectors for Bidirectional Explanations in Histopathology* — [MICCAI 2018 Interpretability Workshop](https://arxiv.org/abs/1904.04520)

## Why I read it

Many clinical concepts are continuous: lesion irregularity, tissue density, fibrosis burden, or steatosis severity. I read this paper because it extends concept-vector explanations beyond binary "present versus absent" concepts to measured quantities that can vary along a clinically meaningful scale.

## What the paper claims

Regression Concept Vectors fit a direction in a layer's activation space that predicts a continuous concept measurement. The directional derivative of the class score along that vector estimates sensitivity to increasing values of the concept, and a relevance measure links the concept value and its influence. The method is applied to breast-cancer histopathology using nuclear texture measurements.

## What convinced me

The analysis uses 300 image patches derived from a larger set of annotated nuclei and identifies contrast and correlation texture measures as relevant to tumor-tissue detection. For nuclear contrast, the raw output–concept association was around Spearman ρ = 0.41, and the proposed sensitivity analysis adds information about direction and magnitude that a binary TCAV score would discard. The paper also evaluates robustness across resampling and layers rather than presenting a single concept direction.

## What it leaves open

The study is a small proof of concept. The regression direction is linear, the concept measurements themselves may be noisy, and directional sensitivity is still a local derivative rather than a causal intervention. Correlated concepts can share a direction, making the clinical interpretation ambiguous.

## What I take from it

Continuous concept tests are a natural fit for clinical severity and quantitative imaging. I would pair them with covariate-adjusted association, out-of-sample concept prediction, and interventions that move the concept while preserving other factors. A continuous score deserves a continuous faithfulness test.
