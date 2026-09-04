---
layout: post
title: "Ultrasonographic Fatty Liver Indicator, a Novel Score Which Rules Out NASH and Is Correlated with Metabolic Parameters in NAFLD"
date: 2025-09-27 12:00:00 +0900
venue: "Liver International"
authors: "Stefano Ballestri, Amedeo Lonardo, Dante Romagnoli, Lucia Carulli, Luisa Losi, Christopher P. Day, Paola Loria (2012)"
description: "A hand-crafted, semi-quantitative ultrasound score (US-FLI) built from four visual features, the kind of clinically legible scoring system that a learned model in the same space should be able to match or explain, not just outperform."
related_posts: false
---

**Paper.** *Ultrasonographic fatty liver indicator, a novel score which rules out NASH and is correlated with metabolic parameters in NAFLD*. [Liver International (2012)](https://doi.org/10.1111/j.1478-3231.2012.02804.x)

## Why I read it

US-FLI is a compact example of clinically structured ultrasound reasoning. Instead of learning an unrestricted image representation, it combines a small set of interpretable signs: liver–kidney contrast, attenuation, vessel blurring, diaphragm and gallbladder-wall visibility, and focal sparing.

## What the paper claims

The score ranges from 2 to 8 and was evaluated in 53 biopsy-confirmed NAFLD patients. The authors test associations with steatosis, metabolic markers, and histologic NASH, and assess interobserver agreement in an additional subset of 31 patients. US-FLI is proposed as a noninvasive tool to better select patients for biopsy.

## What convinced me

US-FLI was an independent predictor of NASH, with odds ratio 2.236 per score increase in the reported model. A score below 4 had a 94% negative predictive value for ruling out severe NASH by the specified criterion. AUROC was approximately 0.76–0.80 depending on the histologic definition, and pairwise interobserver agreement was high, around 0.81–0.88. The score also correlated with histologic steatosis and several metabolic measures.

## What it leaves open

The cohort is small, nonconsecutive, and entirely composed of patients with NAFLD. Negative predictive value is prevalence-dependent, and the score did not correlate with fibrosis. Several components remain qualitative and operator-dependent, so high reader agreement in a small expert subset does not guarantee cross-device reproducibility.

## What I take from it

US-FLI is valuable as a clinical anchor and transparent baseline, not as a perfect ground truth. A learned model should show what it adds beyond these six signs and whether its evidence remains stable across operators, scanners, body habitus, and fibrosis status.
