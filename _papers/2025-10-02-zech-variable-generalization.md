---
layout: post
title: "Variable Generalization Performance of a Deep Learning Model to Detect Pneumonia in Chest Radiographs: A Cross-Sectional Study"
date: 2025-10-02 12:00:00 +0900
venue: "PLOS Medicine"
authors: "Zech, Badgeley, Liu, Costa, Titano, Oermann (2018)"
description: "CNNs detected the treating institution from chest radiographs and used it as a proxy for disease prevalence, an early, concrete demonstration of confounding by site."
related_posts: false
---

**Paper.** *Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs*. [PLOS Medicine 2018](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002683)

## Why I read it

This paper is an early and unusually clear demonstration that hospital identity can be easier to learn than disease. I read it to understand how prevalence differences across institutions create a shortcut that internal validation actively rewards.

## What the paper claims

Pneumonia classifiers are trained and tested across NIH, Mount Sinai, and Indiana chest-radiograph data. The authors compare internal and external performance, train models to predict hospital and department, and manipulate pneumonia prevalence by site to test whether source becomes a useful proxy for the label.

## What convinced me

Hospital identity was almost perfectly recoverable: the site classifier correctly identified more than 99.9% of NIH and Mount Sinai test images and about 95.6% of Indiana images. A model trained jointly on Mount Sinai and NIH reached internal AUC 0.931 but only 0.815 at Indiana. When site-specific disease prevalence was artificially imbalanced, internal AUC increased substantially; balancing prevalence reduced the apparent advantage. The model was exploiting a real statistical property of the dataset, not necessarily pneumonia anatomy.

## What it leaves open

The study identifies site confounding but cannot enumerate every image feature carrying site identity. External performance varies by which hospitals happen to share acquisition characteristics, so one external site is not a complete robustness test. Report-derived pneumonia labels and different patient populations also contribute to the observed gap.

## What I take from it

Site should be treated as a candidate predictor and stress-tested explicitly. I would report source-classification accuracy, prevalence by site, leave-one-site-out performance, and evidence use within each site. Pooling hospitals can increase sample size while simultaneously strengthening a hospital–label shortcut.
