---
layout: post
title: "Transfer Learning with Deep Convolutional Neural Network for Liver Steatosis Assessment in Ultrasound Images"
date: 2025-11-22 12:00:00 +0900
venue: "IJCARS"
authors: "Michał Byra, Grzegorz Styczynski, Cezary Szmigielski, Piotr Kalinowski, Łukasz Michałowski, Rafał Paluszkiewicz, Bogna Ziarkiewicz-Wróblewska, Krzysztof Zieniewicz, Piotr Sobieraj, Andrzej Nowicki (2018)"
description: "A transfer-learning pipeline for grading liver steatosis from B-mode ultrasound, benchmarked directly against the hepatorenal index and GLCM texture features — with biopsy as the reference standard."
related_posts: false
---

**Paper.** *Transfer learning with deep convolutional neural network for liver steatosis assessment in ultrasound images* — [International Journal of Computer Assisted Radiology and Surgery (2018)](https://doi.org/10.1007/s11548-018-1843-2)

## Why I read it

This is one of the earlier papers applying ImageNet-pretrained CNN features to liver ultrasound, and it directly benchmarks against two classical approaches — the hepatorenal index and gray-level co-occurrence matrix (GLCM) texture — that I'd already encountered as comparators elsewhere. I wanted to see the head-to-head numbers and understand what the deep features were actually adding.

## What the paper claims

Using Inception-ResNet-v2 pretrained on ImageNet as a fixed feature extractor on B-mode liver ultrasound, followed by an SVM classifier, the authors grade steatosis against wedge-biopsy ground truth. The proposed approach reaches AUC 0.977, compared with 0.959 for the hepatorenal index (HRI) and 0.893 for GLCM texture features; on Spearman correlation with biopsy-graded steatosis, HRI actually edges out the proposed method (0.80 vs. 0.78), while GLCM lags well behind at 0.39.

## What convinced me

The fact that HRI — a simple, fully legible ratio of liver-to-kidney echogenicity — comes within a hair of the deep-feature approach on AUC, and slightly beats it on correlation, is the most informative part of the paper, even though it's not the headline result. It suggests the deep features are capturing much of the same signal HRI already captures, plus a smaller increment, rather than a qualitatively different kind of evidence.

## What it leaves open

Because the CNN is used purely as a frozen feature extractor pretrained on natural images, the paper can't tell us which visual patterns in the ultrasound the SVM is actually keying on — there's no concept-level or saliency analysis connecting the deep features back to hepatorenal contrast, attenuation, or something else entirely. Sample size and single-center biopsy grading also limit how far the AUC comparison generalizes.

## What I take from it

A deep model narrowly beating a simple, interpretable index on AUC while losing to it on correlation is a genuinely useful negative-ish result — it argues against treating "the deep model achieved higher AUC" as automatic evidence of a richer or more clinically meaningful signal. This is exactly the kind of comparison I want to see more of in medical-AI papers: not just "did the black box win," but "by how much, and against what specific legible baseline."
