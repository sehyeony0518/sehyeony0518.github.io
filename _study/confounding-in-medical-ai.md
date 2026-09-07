---
layout: study_note
title: "Confounding in Medical AI"
description: "A third factor driving both the image and the label, and what it does to a performance estimate."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "causality"
category_title: "Causality, Bias & Shortcuts"
order: 1
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-10-02-zech-variable-generalization"
---

Confounding occurs when an observed relationship mixes the association of interest with a noncausal pathway through other variables. In medical AI, I use it to ask whether apparent diagnostic evidence or performance partly reflects differences in patients, acquisition, or labeling.

## Core question and definition

The question is not simply whether a third variable predicts the label. It is whether that variable creates an alternative explanation for the relationship being interpreted. A confounder must therefore be defined relative to specified variables and a causal question, rather than identified from correlation alone.

I distinguish this from estimating predictive performance within a dataset. A model can genuinely discriminate labels in that population by using hospital-associated information. The estimate may be valid for the sampled mixture while failing to establish that the model recognizes pathology or will perform similarly elsewhere.

## Key concepts

### A common cause creates an alternative path

In the simple graph $$A \leftarrow Z \rightarrow Y$$, Z influences both A and Y, creating an association that need not reflect an effect of A on Y. For medical images, the full graph may include referral, acquisition, and label generation between these variables. I would draw those mechanisms explicitly. Hospital identity can summarize several processes without itself being a sufficient explanation of their causal structure.

### Pooled relationships depend on group composition

For a cue N and grouping variable Z, the identity

$$
P(Y \mid N) = \sum_z P(Y \mid N, Z = z)\,P(Z = z \mid N)
$$

shows how a pooled association combines within-group relationships and group proportions. A device-identifying cue can predict disease when devices serve different patient groups, even if it adds no diagnostic information within those groups. I therefore want both pooled and stratified results before interpreting an evidence score as a marker of clinical severity.

### Adjustment requires assumptions beyond recorded covariates

Adjustment aims to close the relevant noncausal paths. It requires an appropriate variable set, adequate overlap, and suitable estimation; recording many covariates does not guarantee these conditions. [Pearl's causal framework](https://doi.org/10.1214/09-SS057) makes the distinction between observational and interventional quantities explicit. I would not call a covariate-adjusted correlation a causal effect. Measurement error, omitted causes, and incorrectly specified relationships can leave its interpretation unresolved.

### Controlling for a variable can change the question

A mediator lies on a causal pathway, while a collider is a common effect of other variables. Adjusting for the former can remove part of an effect; conditioning on the latter can introduce an association. Similarly, controlling for diagnostic class in an evidence audit asks about variation within classes. That may be useful, but it can remove clinically meaningful between-class variation. I need to justify this choice before comparing adjusted and unadjusted results.

## Worked examples in medical AI

[Zech and colleagues](https://doi.org/10.1371/journal.pmed.1002683) studied pneumonia classification across hospital systems. Their experiments showed that hospital-identifying information, combined with differences in pneumonia prevalence, could support internal performance that did not transfer reliably. I read this as evidence that a pooled diagnostic benchmark can reward recognition of where an image originated.

Consider a hypothetical gallbladder dataset in which suspicious lesions are examined using a different protocol. A model evidence score and clinician-rated lesion irregularity might correlate partly because both vary across protocol groups. Comparing their relationship within protocols would test one explanation, but would remain inconclusive if clinically comparable lesions were absent from one group.

## Evaluation methods and limitations

I would begin with a causal account, inspect joint distributions of clinical and acquisition variables, and report performance and evidence alignment within relevant strata. Matching, weighting, and regression can support specific comparisons when their assumptions are credible. A cue-only predictor can reveal how much predictive opportunity exists in metadata, without proving that the image classifier uses it.

Patient-level uncertainty estimates remain necessary, but narrow intervals cannot repair missing overlap or unmeasured causes. External evaluation can challenge a site-associated relationship; a performance change alone cannot identify which acquisition or clinical mechanism produced it.

## Research connections and open questions

For gallbladder ultrasound clinical faithfulness auditing, I want each alignment claim to include its clinical reference, adjustment rationale, and population. This would make “the readout tracks a clinical factor” a more precise and challengeable statement.

- Which acquisition variables capture the relevant mechanisms, rather than merely naming the device?
- When does controlling for diagnosis clarify evidence alignment, and when does it remove the signal of interest?
- How should I report an association when the available patients provide insufficient overlap for a credible adjusted comparison?

## References

- Pearl, [Causal inference in statistics: An overview](https://doi.org/10.1214/09-SS057), Statistics Surveys 2009.
- Zech et al., [Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs: A cross-sectional study](https://doi.org/10.1371/journal.pmed.1002683), PLOS Medicine 2018.
