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

DR and DME are related but not interchangeable clinical targets. I read CANet to see whether modeling their relationship jointly can improve grading without requiring lesion-level annotations, and whether the resulting attention can support a meaningful explanation claim.

## What the paper claims

CANet uses disease-specific attention to learn features for each task and disease-dependent attention to exchange information between the DR and DME branches. It is trained with image-level grades only. The architecture is meant to exploit clinically relevant co-occurrence while retaining task-specific representations.

## What convinced me

The joint formulation improves over the compared single-task and generic multitask baselines. On the IDRiD challenge setting, the reported joint grading accuracy was 65.1%. On Messidor, the model reached AUC 96.3 for DR and 92.4 for DME, with joint accuracy reported at 85.1 in the corresponding evaluation. The ablations indicate that both disease-specific and cross-disease attention contribute rather than one branch simply dominating.

## What it leaves open

Attention weights are not lesion annotations and do not prove that the model localized microaneurysms, exudates, or macular involvement faithfully. Disease correlation can also become a shortcut if prevalence or referral patterns change across populations. Image-level supervision leaves open whether the exchanged information is clinically correct or merely statistically convenient.

## What I take from it

Related diagnoses can provide useful inductive structure, but the relationship itself must be audited. I would test whether DME predictions depend on macula-centered evidence and whether the benefit persists when DR–DME prevalence is shifted. Cross-task attention is a hypothesis about reasoning, not yet proof of it.
