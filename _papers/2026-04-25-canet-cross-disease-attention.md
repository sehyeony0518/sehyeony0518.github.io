---
layout: post
title: "CANet: Cross-Disease Attention Network for Joint Diabetic Retinopathy and Diabetic Macular Edema Grading"
date: 2026-04-25 12:00:00 +0900
venue: "IEEE TMI"
authors: "Xiaomeng Li, Xiaowei Hu, Lequan Yu, Lei Zhu, Chi-Wing Fu, Pheng-Ann Heng (2020)"
description: "Joint grading of two correlated diabetic-eye diseases via cross-disease attention — a structural bet that shared retinal evidence should inform both diagnoses at once, rather than training two separate classifiers that never talk to each other."
related_posts: false
---

**Paper.** *CANet: Cross-disease Attention Network for Joint Diabetic Retinopathy and Diabetic Macular Edema Grading* — [IEEE Transactions on Medical Imaging (2020)](https://arxiv.org/abs/1911.01376)

## Why I read it

Diabetic retinopathy (DR) and diabetic macular edema (DME) are graded from the same retinal photograph and share underlying pathophysiology, yet most grading models I'd read treat them as two independent classification tasks. CANet's premise — that jointly modeling the two diseases should help both — is a structural claim about how the tasks relate, and I wanted to see how that claim was operationalized.

## What the paper claims

CANet introduces a cross-disease attention mechanism that lets features relevant to DR grading inform DME grading and vice versa, alongside a disease-specific attention module for each task individually, jointly training both graders on the same retinal image inputs rather than treating them as separate pipelines. The paper reports this joint, attention-coupled approach outperforming single-disease baselines on standard DR/DME benchmarks.

## What convinced me

Grounding the architecture in a real clinical relationship — DR and DME frequently co-occur and share retinal vascular pathology — gives the cross-disease attention module a principled justification beyond "attention improves things." It's testing a specific hypothesis (shared evidence helps both gradings) rather than just adding capacity.

## What it leaves open

The paper doesn't decompose *which* shared visual evidence the cross-disease attention is actually routing between tasks — whether it's genuinely shared pathological signal (microaneurysms, exudates near the macula) or a more diffuse statistical correlation between the two disease labels in the training set that happens to help accuracy without being clinically traceable.

## What I take from it

Joint modeling of correlated clinical labels is a reasonable structural prior, but the same faithfulness question I ask of single-task models applies here with an extra layer: does the cross-disease attention improve accuracy because it surfaces genuinely shared clinical evidence, or because DR and DME labels are correlated in ways a model can exploit without engaging the underlying pathology at all? A joint model earning higher accuracy isn't automatically evidence that it reasons more like a clinician connecting the two diagnoses.
