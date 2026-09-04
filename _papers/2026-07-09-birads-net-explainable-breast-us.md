---
layout: post
title: "BI-RADS-Net: An Explainable Multitask Learning Approach for Cancer Diagnosis in Breast Ultrasound Images"
date: 2026-07-09 12:00:00 +0900
venue: "IEEE ISBI 2021"
authors: "Boyu Zhang, Aleksandar Vakanski, Min Xian (2021)"
description: "A multitask model that predicts BI-RADS descriptors alongside malignancy, one of the earlier attempts at the same explainable-by-BI-RADS idea that later concept-bottleneck papers pushed further."
related_posts: false
---

**Paper.** *BI-RADS-Net: An Explainable Multitask Learning Approach for Cancer Diagnosis in Breast Ultrasound Images*, IEEE ISBI (2021)

## Why I read it

I read BI-RADS-Net alongside BUS-CBM to separate two architectures that are often described with the same word, "explainable." Both predict BI-RADS concepts, but only one constrains how those concepts enter the final diagnosis.

## What the paper claims

BI-RADS-Net jointly predicts five BI-RADS descriptors, a benign/malignant class, and a malignancy likelihood from breast ultrasound. Shared features are intended to improve classification while presenting outputs in the vocabulary radiologists already use: shape, orientation, margin, echo pattern, and posterior features.

## What convinced me

The multitask formulation is clinically coherent and performs reasonably on 1,192 images. All five descriptor tasks exceeded 80% accuracy, and tumor classification reached 88.9%. This is more informative than a post hoc heatmap because the auxiliary tasks are trained against explicit clinical labels rather than inferred after training.

## What it leaves open

The malignancy head can still bypass the predicted descriptors through the shared representation. Descriptor agreement therefore shows that the network can recover BI-RADS information, not that its cancer decision actually depends on that information. The paper also did not include the clinician-facing qualitative study that it proposed as future work, and descriptor accuracy alone does not establish explanation usefulness or calibration.

## What I take from it

This paper is a useful architectural baseline. Multitask concept prediction answers "does the representation contain this clinical information?" A strict bottleneck or an intervention test is needed to answer the stronger question, "would changing this concept change the diagnosis?" I now look for that distinction whenever a model claims concept-level explainability.
