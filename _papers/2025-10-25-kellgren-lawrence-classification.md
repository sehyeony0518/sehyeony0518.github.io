---
layout: post
title: "Classifications in Brief: Kellgren-Lawrence Classification of Osteoarthritis"
date: 2025-10-25 12:00:00 +0900
venue: "Clinical Orthopaedics and Related Research"
authors: "Mark D. Kohn, Adam A. Sassoon, Navin D. Fernando (2016)"
description: "A short clinical primer on the KL grading scale — the single most common label target for knee-OA deep learning papers, and a reminder of how much subjectivity that five-point scale is quietly absorbing."
related_posts: false
---

**Paper.** *Classifications in Brief: Kellgren-Lawrence Classification of Osteoarthritis* — [Clinical Orthopaedics and Related Research (2016)](https://doi.org/10.1007/s11999-016-4732-4)

## Why I read it

I've now read several deep-learning papers that report their model's KL-grade accuracy or agreement with a radiologist as if the scale were a fixed, objective ruler. This clinical-orthopaedics "in brief" piece is the kind of source that explains where the scale actually came from and what it's meant — and not meant — to capture.

## What the paper claims

Kohn, Sassoon, and Fernando give a short history and clinical explanation of the Kellgren-Lawrence (KL) system: a five-grade (0–4) radiographic severity scale for knee osteoarthritis, originally developed in 1957 and still the most widely used classification in both clinical practice and research, based primarily on osteophyte formation and joint space narrowing observed on a plain radiograph.

## What convinced me

The piece is upfront that KL grading is an ordinal, holistic judgment rather than a measurement — two radiographs that would earn the same grade can look meaningfully different, and the boundary between adjacent grades (especially grade 1 versus grade 2) is a known source of disagreement between readers, not a bright line.

## What it leaves open

As a short clinical-education piece, it doesn't quantify inter-rater reliability numerically or compare KL to more granular alternatives like the OARSI atlas or automated joint-space-width measurement — it's a primer, not a validation study. It also doesn't address how KL grading correlates (or fails to correlate) with patient-reported pain and function, a well-known clinical mismatch.

## What I take from it

Whenever a paper reports a model achieving high agreement with "ground truth KL grade," I now read that claim as agreement with one or more readers' holistic five-point judgment call, not agreement with an objectively measured quantity. That reframing changes how I weigh reported accuracy numbers — a model matching KL grade near-perfectly on an internal test set may be matching the labeling habits of the specific radiologists in that dataset rather than a stable, transferable notion of severity.
