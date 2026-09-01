---
layout: post
title: "BI-RADS for Sonography: Positive and Negative Predictive Values of Sonographic Features"
date: 2025-12-13 12:00:00 +0900
venue: "AJR"
authors: "Hong et al. (2005)"
description: "An empirical look at how well individual BI-RADS sonographic descriptors actually predict malignancy — the kind of per-feature grounding that a BI-RADS-based concept bottleneck for breast ultrasound is implicitly relying on."
related_posts: false
---

**Paper.** *BI-RADS for Sonography: Positive and Negative Predictive Values of Sonographic Features* — American Journal of Roentgenology (2005)

## Why I read it

Several of the breast-ultrasound papers I've reviewed use BI-RADS descriptors — shape, margin, orientation — as an interpretable concept layer, implicitly assuming each descriptor carries real predictive weight toward malignancy. This paper is one of the empirical studies behind that assumption, so I read it to check how strong that per-feature signal actually is.

## What the paper claims

The authors evaluate individual BI-RADS sonographic features against biopsy outcomes, reporting the positive and negative predictive value of each descriptor category (shape, margin, orientation, echo pattern, posterior features, and others) rather than treating BI-RADS only as a single aggregate assessment category. This decomposes the lexicon into its component parts and asks how much malignancy risk each one carries on its own.

## What convinced me

Treating BI-RADS features individually, rather than only as inputs folded into a single final category, is exactly the granularity a concept-bottleneck or explainable CAD system needs to be built on. If a downstream model's "margin" concept prediction is meant to carry diagnostic weight, this kind of study is what tells you how much weight that concept can legitimately bear.

## What it leaves open

Predictive values computed on one institution's case mix don't transfer directly to a population with a different malignancy prevalence — PPV and NPV are prevalence-dependent by construction, unlike sensitivity and specificity. A concept's predictive value at this site, in this era of equipment, is not automatically the same concept's predictive value elsewhere.

## What I take from it

When I evaluate a BI-RADS-based concept bottleneck, I now check whether its concept-level predictive weights are plausible against studies like this one — and whether the model is implicitly relearning that "irregular margin" matters more than "orientation" in a way that's consistent with the clinical literature, or diverging from it in ways that would need explaining. A concept bottleneck's concepts are only as trustworthy as the empirical grounding behind each one.
