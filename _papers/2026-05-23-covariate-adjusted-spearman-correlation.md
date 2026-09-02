---
layout: post
title: "Covariate-Adjusted Spearman's Rank Correlation with Probability-Scale Residuals"
date: 2026-05-23 12:00:00 +0900
venue: "Biometrics"
authors: "Qi Liu, Chun Li, Valentine Wanga, Bryan E. Shepherd (2018)"
description: "A statistics paper on adjusting rank correlation for confounding covariates — read because so many AI-versus-classical-index comparisons in medical imaging report raw Spearman correlation without asking whether a shared confound is inflating it."
related_posts: false
---

**Paper.** *Covariate-Adjusted Spearman's Rank Correlation with Probability-Scale Residuals* — [Biometrics (2018)](https://doi.org/10.1111/biom.12812)

## Why I read it

Clinical alignment is often measured by correlating a model score with an ordinal biomarker or severity grade. That correlation can be inflated, attenuated, or reversed by age, label, site, or other covariates. I read this paper for a principled rank-based adjustment rather than an ad hoc residualization step.

## What the paper claims

The authors define population parameters for partial and conditional Spearman correlation through concordance–discordance probabilities. The practical estimator is the correlation between probability-scale residuals from models of each variable conditional on the covariates. This preserves a rank interpretation and accommodates continuous, ordinal, and other orderable outcomes.

## What convinced me

The applications show that adjustment can change the scientific conclusion. The unadjusted correlation between IL-6 and sCD14 was 0.03, but the adjusted estimate was 0.19 with a 95% confidence interval of 0.04–0.33. The leptin–sCD14 association changed sign, from –0.20 unadjusted to +0.13 after adjustment. Simulations also showed better type-I-error behavior than several traditional partial-rank alternatives in the examined settings.

## What it leaves open

The method is not automatically causal. Its validity depends on choosing the relevant covariates and adequately modeling each conditional distribution. Conditioning on a collider or adjusting away part of the clinical construct can create a different bias. The resulting coefficient also needs uncertainty estimates and sensitivity analysis.

## What I take from it

For evidence-alignment metrics, I would report the raw rank correlation, the covariate-adjusted estimate, its confidence interval, and the exact adjustment set. A label-controlled correlation can isolate within-class ordering, but only if the conditioning choice is clinically and causally defensible.
