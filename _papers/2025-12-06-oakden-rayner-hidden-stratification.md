---
layout: post
title: "Hidden Stratification Causes Clinically Meaningful Failures in Machine Learning for Medical Imaging"
date: 2025-12-06 12:00:00 +0900
venue: "ACM CHIL"
authors: "Oakden-Rayner, Dunnmon, Carneiro, Ré (2020)"
description: "Within a labeled class there are clinically distinct subsets, and a model can fail on the dangerous ones while the headline number stays high."
related_posts: false
---

**Paper.** *Hidden Stratification Causes Clinically Meaningful Failures in Machine Learning for Medical Imaging* — [ACM CHIL 2020](https://dl.acm.org/doi/10.1145/3368555.3384468)

## Why I read it

Because "the model is 92% accurate" has never told me what I actually need to know, and this paper explains precisely why in clinical terms.

## The argument

A label like "abnormal" or "pneumothorax" is not one thing. It contains subsets that differ in prevalence, appearance, difficulty, and clinical urgency. A model can learn the common, easy, low-risk subset and fail on the rare, subtle, high-risk one — and the aggregate metric will not move, because the dangerous subset is rare by definition.

Their pneumothorax example is the one I remember: models performed far worse on cases *without* a chest drain. Drains are visually obvious and correlate with the label, so the model learns the treatment rather than the pathology — and treated cases are exactly the ones already diagnosed. The clinically useful case is the one it fails on.

## Why it matters for auditing

This reframes what a subgroup is. Fairness work usually stratifies by demographic attributes, which are recorded. Hidden stratification concerns subsets that are **clinically meaningful but not labeled** — severity, lesion morphology, presence of treatment artifacts, acquisition conditions. You cannot report performance on a subgroup you never defined.

The paper's proposed approaches — schema completion, error auditing, algorithmic measurement — all require someone to hypothesize where the strata might be. That is clinical work, not statistical work.

## What I take from it

The most dangerous errors are structurally invisible to the metrics we publish. Any audit that only reports overall performance plus demographic breakdowns will miss them.
