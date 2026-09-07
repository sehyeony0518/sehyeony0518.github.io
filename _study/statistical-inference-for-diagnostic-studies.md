---
layout: study_note
title: "Statistical Inference for Diagnostic Studies"
description: "Hypothesis testing, confidence intervals, effect size, bootstrap, and multiple comparisons, applied to the claims diagnostic AI papers make."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "foundations"
category_title: "Mathematical & Statistical Foundations"
order: 3
source: "Independent study"
written: true
updated: "2026-09-08"
---

Statistical inference asks what observations from a study support about a specified population or process. In diagnostic AI, that includes uncertainty about performance differences, subgroup failures, and the alignment between model evidence and clinical factors.

## Why it matters here

A performance estimate depends on which patients were sampled, how their labels were established, and which analyses were selected. More decimal places do not resolve those dependencies. I need an inferential claim to identify its target population and comparison before deciding whether its statistical method is appropriate.

For my clinical faithfulness work, this matters because an audit can generate many apparently informative results. Readouts, clinical factors, layers, and subgroups create numerous opportunities to find an association. I want uncertainty estimates that reflect the study design and a clear distinction between a planned test and a pattern discovered during exploration.

## The core ideas

### The estimand comes before the test

An estimand is the quantity the study aims to estimate. A difference in patient-level sensitivity at prespecified thresholds is different from a difference in image-level AUROC. Before comparing models, I need to define the outcome, population, aggregation rule, and operating conditions. When both models evaluate the same patients, the comparison is paired. Treating their estimates as independent discards information about which patients each model gets right or wrong.

### A p-value evaluates compatibility under assumptions

A p-value is the probability, under the null hypothesis and the statistical assumptions used, of a test statistic at least as extreme as the observed one. It is not the probability that the null hypothesis is true. The [ASA statement on p-values](https://doi.org/10.1080/00031305.2016.1154108) also separates statistical significance from effect size and importance. Failure to reject a difference does not establish equivalence; that requires a design and margin suited to an equivalence claim.

### Effect sizes and intervals answer complementary questions

An effect size describes the magnitude of a relationship or difference, preferably in units relevant to the question. A confidence interval describes its uncertainty through a repeated-sampling procedure. Under its assumptions, a 95% confidence procedure covers the fixed true parameter in 95% of repetitions; the realized interval is not a posterior probability statement. I would examine whether the interval permits clinically consequential harm or benefit. Narrow sampling uncertainty does not account for an incorrect reference standard or systematic selection bias.

### Bootstrap resampling must preserve the sampling structure

The bootstrap approximates sampling variation by repeatedly resampling observed units with replacement. If multiple ultrasound frames belong to one patient, resampling frames independently can understate uncertainty. I would resample patients and retain their grouped observations, using the same resampled patients for paired model comparisons. A bootstrap of a fixed model's test predictions measures uncertainty from evaluation sampling. It does not include variation from training a new model, and it cannot manufacture missing patient populations or unseen hospitals.

### Multiple comparisons change the interpretation of discoveries

Testing many associations increases opportunities for false discoveries. Family-wise error control concerns the probability of at least one false rejection in a defined family; false discovery rate control concerns the expected proportion of false rejections among all rejections. The procedure and its assumptions should match the goal. I would define primary comparisons before evaluation and label exploratory findings accordingly. Correcting only the final displayed tests cannot account for an undocumented search across many readouts or analysis choices.

## Where it touches my work

In a gallbladder ultrasound audit, I would report an evidence-alignment estimate with a patient-level interval, its clinical reference definition, and the adjustment variables used. For competing audit methods, I would compare them on the same patients and preserve that pairing during resampling. I would also report subgroup sample composition and failed analyses. A wide interval for an uncommon lesion category is part of the finding, rather than a reason to replace it with a more favorable pooled result.

## What I have not resolved

- What magnitude of change in an evidence-alignment metric would be meaningful enough to alter a model assessment?
- How should I represent uncertainty when there are many patients but only a few independent acquisition sites?
- Which parts of the audit should be prespecified, and how can exploratory findings be confirmed without repeatedly reusing the same evaluation patients?
