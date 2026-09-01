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

Several liver-ultrasound and imaging papers I've reviewed report Spearman correlation between a model's output and a reference standard as their headline evidence of validity, without adjusting for shared covariates like age, BMI, or disease severity that could inflate the raw correlation. I wanted to understand the statistical machinery for doing that adjustment properly, since I keep flagging its absence.

## What the paper claims

The authors point out that the traditionally defined partial Spearman correlation has real limitations when adjusting for covariates, and propose an alternative based on probability-scale residuals — a way to compute a covariate-adjusted rank correlation that behaves more consistently than the existing partial-correlation approach, applicable to continuous, discrete, or mixed variable types.

## What convinced me

The paper is careful about exactly where the standard partial-Spearman approach breaks down, rather than just asserting a new method is better — that specificity makes it possible to check, for any given reported correlation in a downstream imaging paper, whether the confound structure in question is one this critique actually applies to.

## What it leaves open

Being a statistical methods paper, it doesn't itself audit any medical-imaging validation study — it provides the tool, not the application. Whether a given imaging paper's confounds (age, sex, BMI, disease severity) are large enough in practice to meaningfully inflate an unadjusted correlation is a separate, empirical question this paper doesn't answer.

## What I take from it

This paper gave me a concrete standard to check reported correlations against: if a paper claims a model's continuous output correlates strongly with a reference standard, and that correlation is computed without adjusting for an obvious shared confound (disease severity being the most common offender), I now treat the reported number as an upper bound on the model's real predictive contribution, not a clean estimate of it. It's a small, easy-to-overlook methodological gap that can make a model look more clinically informative than it actually is.
