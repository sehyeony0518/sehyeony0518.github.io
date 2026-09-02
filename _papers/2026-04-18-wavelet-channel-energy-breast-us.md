---
layout: post
title: "Breast Tumor Classification of Ultrasound Images Using Wavelet-Based Channel Energy and ImageJ"
date: 2026-04-18 12:00:00 +0900
venue: "IEEE JSTSP"
authors: "Hsieh-Wei Lee, Bin-Da Liu, King-Chu Hung, Sheau-Fang Lei, Po-Chin Wang, Tsung-Lung Yang (2009)"
description: "A pre-deep-learning approach to breast-ultrasound CAD: hand-engineered wavelet channel-energy features meant to capture how infiltrative a lesion's margin looks — a useful reminder of what feature engineering used to make explicit."
related_posts: false
---

**Paper.** *Breast Tumor Classification of Ultrasound Images Using Wavelet-Based Channel Energy and ImageJ* — [IEEE Journal of Selected Topics in Signal Processing (2009)](https://doi.org/10.1109/JSTSP.2008.2011160)

## Why I read it

Before CNNs, breast-ultrasound CAD relied on hand-engineered features meant to capture specific radiological signs. This paper's target — the "infiltrative nature" of a lesion's margin, a classic malignancy cue — is exactly the kind of feature a modern deep model is implicitly expected to rediscover on its own, so I wanted to see how it was made explicit here.

## What the paper claims

The authors treat the irregularity of a lesion's boundary as a kind of energy signal that produces local variance along a one-dimensional contour representation, and use a wavelet transform to extract "channel energy" features that quantify that irregularity, feeding them into a classifier to distinguish malignant from benign masses. The motivation is grounded directly in known clinical practice: breast ultrasound as an adjunct to mammography measurably improves sensitivity, and reducing unnecessary biopsies (most biopsied masses turn out to be benign) is the explicit clinical goal.

## What convinced me

The feature is designed around a specific, named, clinically established sign (infiltrative/irregular margin as a malignancy indicator) rather than an arbitrary texture statistic, which makes the resulting classifier's reasoning traceable back to something a radiologist already looks for. That traceability is exactly what gets harder to verify once a CNN takes over the same task end-to-end.

## What it leaves open

Hand-engineered features like this one are, by construction, incomplete — they capture one clinically meaningful signal (margin irregularity) and will miss any other pattern predictive of malignancy that a radiologist or a learned model might pick up on. The paper doesn't report on a large or multi-institution cohort, so how well this specific feature generalizes across scanner and population is untested.

## What I take from it

Reading a hand-engineered-feature paper after a run of deep-learning breast-ultrasound papers is clarifying: it shows exactly what a black-box CNN is implicitly being asked to reinvent, and it's a useful sanity check for concept-bottleneck-style designs — margin irregularity is precisely the kind of concept that a modern bottleneck should be able to name explicitly, the same way this 2009 paper did with an explicit wavelet feature.
