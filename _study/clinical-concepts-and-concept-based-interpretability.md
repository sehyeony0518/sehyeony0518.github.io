---
layout: study_note
title: "Clinical Concepts and Concept-Based Interpretability"
description: "Concept bottlenecks and concept activation vectors as attempts to make a model speak in clinical terms."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "alignment"
category_title: "Clinical Alignment & Interpretability"
order: 2
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-11-29-concept-bottleneck-models"
  - "2025-09-19-tcav-concept-activation-vectors"
---

Concept-based interpretability connects model behavior to named properties such as lesion size, attachment morphology, or echogenicity. The central difficulty is ensuring that a quantity given a clinical name actually measures that concept and has the claimed role in prediction.

## Why it matters here

Clinical concepts can make a model easier to question than an unexplained feature vector. A reader can ask whether the lesion was judged sessile or whether its boundary was visible. A familiar term can nevertheless conceal uncertainty in annotation, representation, or the concept's connection to the output.

For my research, concepts offer potential reference points for clinical faithfulness auditing. I want to compare model readouts with independently assessed clinical properties and, where the architecture permits it, examine the effect of changing a concept value. I still need to distinguish a readable interface from validated clinical evidence use.

## The core ideas

### A clinical concept needs an operational definition

A concept must specify what is assessed, on which image or examination, and how uncertainty is represented. Size requires a measurement convention; echogenicity requires a reference for comparison. Some properties may be unassessable in a saved view. I would separate “absent” from “not visible” and retain reader disagreement where possible. Without these distinctions, a concept label can combine biological variation with acquisition and annotation differences while appearing to describe one coherent clinical property.

### Concept bottlenecks put named variables on the prediction path

In a strict concept bottleneck model, the image first produces concept predictions, and the diagnostic predictor receives only those concept values. [Koh and colleagues](https://proceedings.mlr.press/v119/koh20a.html) develop this architecture and examine interventions on its concepts. The design provides an explicit route for questioning intermediate predictions. It also depends on the concept set: omitted clinical information cannot reach the downstream predictor through a genuinely restricted bottleneck. Adding a direct image-feature route changes that restriction and the interpretation it supports.

### Concept activation vectors probe an existing representation

A concept activation vector is a direction derived by separating concept examples from comparison examples in a chosen representation layer. [TCAV](https://proceedings.mlr.press/v80/kim18d.html) examines directional derivatives of a target score along that direction, often summarizing how frequently sensitivity is positive across a class. This is a model sensitivity measurement, not the proportion of a diagnosis explained by the concept. If the concept examples also share a device or acquisition style, the direction may capture those differences. Comparison sets and stability checks are therefore part of the interpretation.

### A named representation can carry unintended information

Concept accuracy does not guarantee that the intermediate representation contains only the intended concepts. Continuous concept scores can preserve information beyond their named labels, and a downstream predictor may use it. This problem is examined in [Promises and Pitfalls of Black-Box Concept Learning Models](https://arxiv.org/abs/2106.13314). The concern also applies when an auxiliary concept prediction task merely encourages a representation: successful concept prediction does not establish that the diagnostic head relies on those concepts rather than other available features.

### Concept interventions test a defined computational route

Replacing a predicted concept with a clinician-supplied value tests how the downstream model responds to that replacement. It does not establish what would happen if the patient's lesion changed. Correlated concepts introduce another difficulty: editing one value while holding others fixed can create an implausible combination. A corrected value may also differ from the noisy concept predictions encountered during training. I would evaluate intervention behavior explicitly, including cases where apparently helpful corrections worsen the diagnostic output.

## Where it touches my work

For gallbladder ultrasound, I would start with a small, clinically reviewed concept set whose definitions and visibility can be assessed reliably. I would examine concept errors by device and view before interpreting their relationship with diagnosis. In a post-hoc audit, concept associations and activation directions could identify hypotheses about evidence use. In a bottleneck model, I could additionally test downstream responses to corrections. Neither approach removes the need for independent clinical reference information or scrutiny of information outside the intended concepts.

## What I have not resolved

- Which gallbladder concepts are sufficiently reproducible and informative to justify restricting a diagnostic model to them?
- How can I detect unintended information in continuous concept scores without discarding useful uncertainty?
- What should a concept intervention do when the requested correction conflicts with other predicted concepts?
- How can I evaluate a clinically meaningful feature that experts recognize but cannot annotate consistently?
