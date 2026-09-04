---
layout: post
title: "Underdiagnosis Bias of Artificial Intelligence Algorithms Applied to Chest Radiographs in Under-Served Patient Populations"
date: 2025-12-13 12:00:00 +0900
venue: "Nature Medicine"
authors: "Seyyed-Kalantari, Zhang, McDermott, Chen, Ghassemi (2021)"
description: "Chest X-ray classifiers assigned 'no finding' disproportionately to underserved patients, the error mode that silently denies care."
related_posts: false
---

**Paper.** *Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations*. [Nature Medicine 2021](https://www.nature.com/articles/s41591-021-01595-0)

## Why I read it

Fairness metrics can be abstract unless they are tied to a clinically directional harm. This paper focuses on underdiagnosis, diseased patients incorrectly labeled as having "no finding", and asks which groups bear that error across widely used chest-radiograph datasets.

## What the paper claims

The authors train models on MIMIC-CXR, CheXpert, ChestX-ray14, and pooled data, then compare false "no finding" predictions across sex, age, race or ethnicity, and insurance groups. They also examine intersections of attributes rather than assuming that a single-axis analysis captures the highest-risk patients.

## What convinced me

The disparity appears across datasets and training configurations rather than in one isolated model. Female patients, younger patients, Black and Hispanic patients, and patients with Medicaid were among the groups with higher underdiagnosis rates in the reported analyses; intersections such as Hispanic women could face compounded errors. Results were repeated over five random seeds with confidence intervals, which is important because a fairness conclusion should not rest on one checkpoint.

## What it leaves open

The reference labels are derived from clinical reports and can reproduce unequal diagnostic documentation or care. "No finding" is also a broad target that combines many diseases and severities. Equalizing one error rate may change other clinically relevant operating characteristics, and group categories do not explain the mechanism of disparity.

## What I take from it

Fairness evaluation should start from a harm model: who is missed, for which condition, and with what consequence? I would report subgroup uncertainty, intersectional results, label-quality sensitivity, and shortcut tests. Performance parity without mechanism or clinical context is incomplete.
