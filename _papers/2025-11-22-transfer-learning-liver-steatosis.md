---
layout: post
title: "Transfer Learning with Deep Convolutional Neural Network for Liver Steatosis Assessment in Ultrasound Images"
date: 2025-11-22 12:00:00 +0900
venue: "IJCARS"
authors: "Michał Byra, Grzegorz Styczynski, Cezary Szmigielski, Piotr Kalinowski, Łukasz Michałowski, Rafał Paluszkiewicz, Bogna Ziarkiewicz-Wróblewska, Krzysztof Zieniewicz, Piotr Sobieraj, Andrzej Nowicki (2018)"
description: "A transfer-learning pipeline for grading liver steatosis from B-mode ultrasound, benchmarked directly against the hepatorenal index and GLCM texture features, with biopsy as the reference standard."
related_posts: false
---

**Paper.** *Transfer learning with deep convolutional neural network for liver steatosis assessment in ultrasound images*. [International Journal of Computer Assisted Radiology and Surgery (2018)](https://doi.org/10.1007/s11548-018-1843-2)

## Why I read it

This is an early transfer-learning study in liver ultrasound with biopsy reference and a direct comparison against the hepatorenal index. I read it to see where a deep representation truly adds value over a transparent quantitative baseline.

## What the paper claims

ImageNet-pretrained Inception-ResNet-v2 features are extracted from B-mode liver image sequences. An SVM detects steatosis above 5%, and Lasso regression estimates histologic fat percentage. The model is compared with HRI and gray-level co-occurrence-matrix texture features on 550 images from 55 patients.

## What convinced me

For steatosis detection, the CNN features achieved AUC 0.977, above HRI at 0.959 and GLCM at 0.893. The quantification result is more nuanced: Spearman correlation with biopsy fat percentage was 0.78 for the CNN and 0.80 for HRI, while GLCM reached 0.39. The deep model therefore improved binary discrimination but did not outperform the simple clinical index for continuous severity estimation.

## What it leaves open

The cohort is very small, despite the larger image count, and comes from a narrow clinical setting. Repeated frames from the same patient require strict patient-level validation. Transfer learning may also exploit acquisition texture that does not generalize across scanners, and the study provides little insight into which image evidence supports the prediction.

## What I take from it

A black box should be compared against the right clinical baseline for each target. Better AUC does not imply better severity tracking. For liver steatosis, I would report patient-wise evaluation, external scanners, calibration, and incremental value beyond HRI rather than treating feature-learning capacity as sufficient evidence of progress.
