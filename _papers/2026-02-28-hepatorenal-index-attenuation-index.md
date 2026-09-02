---
layout: post
title: "Noninvasive Quantitative Estimation of Hepatic Steatosis by Ultrasound: A Comparison of the Hepato-Renal Index and Ultrasound Attenuation Index"
date: 2026-02-28 12:00:00 +0900
venue: "Medical Ultrasonography"
authors: "Heon-Ju Kwon, Kyoung Won Kim, Jin-Hee Jung, Sang Hyun Choi, Woo Kyoung Jeong, Bohyun Kim, Gi-Won Song, Sung-Gyu Lee (2016)"
description: "A head-to-head comparison of two classical ultrasound-based liver-fat indices in living liver-donor candidates, against biopsy — the pair of legible baselines that any liver-steatosis deep model is implicitly competing with."
related_posts: false
---

**Paper.** *Noninvasive quantitative estimation of hepatic steatosis by ultrasound: a comparison of the hepatorenal index and ultrasound attenuation index* — [Medical Ultrasonography (2016)](https://doi.org/10.11152/mu-868)

## Why I read it

This study compares two transparent ultrasound measurements against biopsy rather than training an opaque classifier. I read it to understand what a strong, clinically legible baseline looks like for hepatic-steatosis assessment and where its validation remains incomplete.

## What the paper claims

In 224 prospective living-liver-donor candidates, the authors compute a hepatorenal index from liver–kidney echogenicity and an ultrasound attenuation index from depth-dependent signal loss. Histologic steatosis from biopsy is the reference standard. The study compares diagnostic accuracy, correlation with fat percentage, and interobserver agreement.

## What convinced me

HRI showed numerically higher AUC than attenuation for both thresholds: 0.856 versus 0.820 for steatosis of at least 5%, and 0.937 versus 0.909 for at least 30%, although the differences were not statistically significant. HRI also correlated more strongly with histology (about 0.853 versus 0.682), and both methods had excellent interobserver agreement, with ICC 0.973 for HRI and 0.931 for attenuation.

## What it leaves open

Living-donor candidates are a selected, comparatively healthy population, so spectrum and prevalence differ from routine NAFLD clinics. The study evaluates measurement between readers but does not fully separate image-acquisition variability from measurement variability. Biopsy itself has sampling error, and thresholds may not transfer across devices or protocols.

## What I take from it

Simple quantitative indices deserve serious consideration as baselines and audit anchors. A learned model should show not only better discrimination but also improved repeatability, robustness across scanners, and incremental clinical value beyond HRI. Interpretability begins with knowing what the model must beat.
