---
layout: post
title: "Hidden Stratification Causes Clinically Meaningful Failures in Machine Learning for Medical Imaging"
date: 2025-11-10 12:00:00 +0900
venue: "ACM CHIL"
authors: "Oakden-Rayner, Dunnmon, Carneiro, Ré (2020)"
description: "Within a labeled class there are clinically distinct subsets, and a model can fail on the dangerous ones while the headline number stays high."
related_posts: false
---

**Paper.** *Hidden Stratification Causes Clinically Meaningful Failures in Machine Learning for Medical Imaging*. [ACM CHIL 2020](https://dl.acm.org/doi/10.1145/3368555.3384468)

## Why I read it

A high aggregate score can conceal failure on the exact subgroup for which the model would be most useful. I read this paper because it shows that medically meaningful subtypes often exist inside a broad benchmark label even when the dataset does not name them.

## What the paper claims

Hidden stratification occurs when a coarse target contains clinically distinct subclasses with different prevalence, difficulty, or shortcut opportunities. The authors demonstrate the problem in chest radiographs, musculoskeletal radiographs, and fracture detection, then discuss schema completion, error auditing, and algorithmic subgroup discovery as partial remedies.

## What convinced me

The examples show how reassuring averages can reverse clinical interpretation. A pneumothorax model achieved AUC 0.87 overall and 0.94 in cases with a chest drain, but only 0.77 in cases without one, the untreated cases where detection matters most. In MURA, abnormality AUC was 0.98 for hardware but 0.76 for degenerative disease. Fracture sensitivity was also lower for subtle and cervical fractures than the overall result suggested.

## What it leaves open

Subgroup labels may be unavailable, expensive, or themselves incomplete. Error auditing can discover known patterns but cannot guarantee that all clinically important strata have been found. Reporting more subgroups also creates multiplicity and small-sample uncertainty, which requires prespecified priorities and confidence intervals.

## What I take from it

Evaluation should follow a clinical failure taxonomy, not only the dataset schema. I would ask which subtypes are untreated, rare, subtle, or disproportionately harmful, then report performance and evidence use within them. Aggregate AUROC is a summary, not a safety argument.
