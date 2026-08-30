---
layout: post
title: "Underdiagnosis Bias: When the Error Falls on Those Already Underserved"
date: 2026-01-10 12:00:00 +0900
venue: "Nature Medicine"
authors: "Seyyed-Kalantari, Zhang, McDermott, Chen, Ghassemi (2021)"
description: "Chest X-ray classifiers assigned 'no finding' disproportionately to underserved patients — the error mode that silently denies care."
related_posts: false
---

**Paper.** *Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations* — [Nature Medicine 2021](https://www.nature.com/articles/s41591-021-01595-0)

## Why I read it

Fairness papers often report differences in accuracy or AUROC. This one asks a sharper question: *which direction* does the error go, and who absorbs it?

## What they found

Across large public chest radiograph datasets, classifiers showed higher false-negative rates — labeling patients "no finding" when disease was present — for female patients, younger patients, Black patients, Hispanic patients, and those with Medicaid insurance. The disparities compounded at intersections. Larger, more diverse training data did not eliminate them.

## Why the direction matters

A false positive triggers further workup. A false negative triggers nothing. Underdiagnosis is the failure mode that is invisible in deployment: the patient is sent home, no alert fires, no correction loop closes. If that error concentrates in populations that already face barriers to care, an ostensibly neutral model widens the gap while reporting excellent aggregate performance.

This is why I think "equal AUROC across groups" is a weak fairness criterion. Two groups can share an AUROC while differing in operating-point behavior, and it is the operating point that determines who gets sent home.

## What it leaves open

The paper documents the disparity clearly but does not fully resolve the mechanism — how much comes from label noise (were the reports themselves biased?), from prevalence and presentation differences, from representation, or from the model. Those require different fixes, and distinguishing them empirically remains hard.

## What I take from it

Report error rates by direction and by subgroup, at the operating point that will actually be deployed. An audit that stops at discrimination metrics has not yet looked at the harm.
