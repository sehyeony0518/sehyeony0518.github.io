---
layout: post
title: "Multi-Resolution Tone Mapping for High Dynamic Range Medical Ultrasound Images"
date: 2026-10-16 12:00:00 +0900
venue: "PLOS ONE"
authors: "Thi Lan Nhi Vu, Vimal Chandran, Christina Haberl, Otmar Scherzer, Julia Binder (2026)"
description: "A tone-mapping method that expands ultrasound's usable dynamic range before a model — or a clinician — ever sees the image, quantified with real, measurable image-quality gains."
related_posts: false
---

**Paper.** *Multi-resolution tone mapping for high dynamic range medical ultrasound images* — [PLOS ONE (2026)](https://doi.org/10.1371/journal.pone.0340777)

## Why I read it

I've read enough liver-ultrasound papers using attenuation and echogenicity features to want to understand a step upstream of all of them: how the raw ultrasound signal gets tone-mapped into the image a radiologist (or a downstream model) actually sees. A preprocessing choice at this stage can shape everything built on top of it, including any AI system reading the same output image.

## What the paper claims

Ultrasound diagnostics is a standard tool in obstetrics and beyond, but the raw signal has a dynamic range that standard image displays compress in ways that can obscure diagnostically relevant detail. The authors propose a multi-resolution tone-mapping method for high-dynamic-range ultrasound images, reporting quantitative image-quality improvements: a 5.4% mean increase in entropy (more preserved information) and generalized contrast-to-noise ratio (gCNR) improvements of 15.79%, 8.93%, and 17.39% across their evaluated conditions.

## What convinced me

Reporting entropy and gCNR — established, objective image-quality metrics — rather than only qualitative visual comparisons gives the claimed improvement something concrete to stand on. A tone-mapping method that measurably preserves more information and improves contrast-to-noise is directly relevant to any downstream task, human or automated, that depends on distinguishing subtle tissue differences.

## What it leaves open

Better entropy and gCNR are general image-quality improvements, not evidence specific to any particular diagnostic task — the paper doesn't test whether these gains translate into measurably better downstream classification or grading performance on a task like liver steatosis or breast lesion classification, which would be the more direct clinical validation.

## What I take from it

This is a reminder that a model's apparent sensitivity to a clinical feature can be partly an artifact of how the raw signal was tone-mapped before the model ever saw it — two ultrasound machines or preprocessing pipelines producing "the same" image can differ enough in dynamic-range handling to shift what's easy or hard for a model to detect. When auditing an ultrasound-based model for clinical faithfulness, I now treat the tone-mapping/preprocessing pipeline as part of what needs auditing, not just the model downstream of it.
