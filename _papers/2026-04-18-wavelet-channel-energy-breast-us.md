---
layout: post
title: "Breast Tumor Classification of Ultrasound Images Using Wavelet-Based Channel Energy and ImageJ"
date: 2026-04-18 12:00:00 +0900
venue: "IEEE JSTSP"
authors: "Hsieh-Wei Lee, Bin-Da Liu, King-Chu Hung, Sheau-Fang Lei, Po-Chin Wang, Tsung-Lung Yang (2009)"
description: "A pre-deep-learning approach to breast-ultrasound CAD: hand-engineered wavelet channel-energy features meant to capture how infiltrative a lesion's margin looks, a useful reminder of what feature engineering used to make explicit."
related_posts: false
---

**Paper.** *Breast Tumor Classification of Ultrasound Images Using Wavelet-Based Channel Energy and ImageJ*. [IEEE Journal of Selected Topics in Signal Processing (2009)](https://doi.org/10.1109/JSTSP.2008.2011160)

## Why I read it

This paper is relevant to my ultrasound work because it turns a recognizable BI-RADS idea, the infiltrative or irregular contour of a malignant lesion, into an explicit multiscale signal feature. The evidence path is simple enough to inspect from contour to score.

## What the paper claims

A lesion boundary is converted into a one-dimensional signal, and high-octave wavelet channel energies quantify local contour variation. The authors argue that malignant infiltration produces irregular, localized changes that are captured efficiently by low-frequency-adjacent wavelet bands. They evaluate both physician-drawn contours and contours generated with ImageJ.

## What convinced me

With expert contours, the feature achieved AUC 0.991, accuracy 0.951, sensitivity 0.985, and specificity 0.933. Performance fell when automated ImageJ contours were used, with AUC around 0.934 and accuracy 0.844. That drop is scientifically useful: it shows that the classifier's apparent strength is conditional on the quality of the upstream lesion boundary.

## What it leaves open

The study uses a relatively small curated dataset and does not establish patient-level, multi-site, or multi-scanner generalization. Contour delineation is itself operator- and algorithm-dependent, and high performance with manual boundaries can hide the difficulty of automatic lesion extraction. The feature is clinically legible, but it captures only one aspect of BI-RADS reasoning.

## What I take from it

An interpretable pipeline should report error propagation between stages. Here, contour uncertainty is part of the diagnostic uncertainty. Modern models can learn richer features, but this paper remains a useful control for whether they truly improve on a clinically motivated contour descriptor.
