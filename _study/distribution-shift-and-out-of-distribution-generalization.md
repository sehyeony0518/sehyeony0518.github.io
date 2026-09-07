---
layout: study_note
title: "Distribution Shift and Out-of-Distribution Generalization"
description: "What breaks when the hospital, scanner, operator, or population changes, and which failures are foreseeable."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
order: 9
source: "Independent study"
written: true
updated: "2026-09-08"
---

Distribution shift means that the joint distribution of inputs and targets differs between development and use. Out-of-distribution generalization asks how well a model works under those differences, with the answer depending on which changes are actually tested.

## Why it matters here

Moving a diagnostic model to another hospital can change patient mix, acquisition, labeling, and workflow simultaneously. A performance decline identifies a transfer problem but does not isolate its cause. Conversely, similar overall performance can conceal a new failure in a small subgroup or a change in how predictions are supported.

For gallbladder ultrasound AI, I need to anticipate changes in device settings, operator choices, available views, and referral populations. Clinical faithfulness auditing adds another target: whether the relationship between a model's readout and independently assessed clinical factors remains credible across those settings, even when headline discrimination appears stable.

## The core ideas

### Shift categories describe assumptions about distributions

Under covariate shift, the input distribution $$P(X)$$ changes while $$P(Y \mid X)$$ remains fixed. Under label shift, $$P(Y)$$ changes while $$P(X \mid Y)$$ remains fixed. Conditional or concept shift refers to a change in $$P(Y \mid X)$$, although terminology varies. These are useful mathematical distinctions, not diagnoses I can assign from the words “new scanner” or “new hospital.” Real transfers can combine several changes. A label-shift correction, for example, needs more than evidence that disease prevalence differs.

### Acquisition and clinical composition can move together

A device change may alter appearance, but it may also coincide with a new service, different patients, or revised examination protocols. Operator-selected views can change which findings are visible to an image-level classifier. Benchmarks such as [WILDS](https://proceedings.mlr.press/v139/koh21a.html) make naturally occurring shifts, including differences across hospitals, explicit evaluation conditions. My takeaway is to name the changing factors and retain their metadata. Without that description, “external validation” gives little indication of what the model has survived.

### Support limits what development data can establish

If the target setting contains patient or image conditions missing from development, the model must extrapolate beyond observed support. Reweighting existing examples cannot create the missing examples. Generalization to such conditions requires additional assumptions, data, or restrictions on intended use. A subgroup may be present only nominally, with too few independent patients or too narrow a range of findings to characterize performance. I would examine coverage of clinical combinations, not only whether each category appears somewhere.

### Evaluation must match the transfer claim

A random patient split tests new patients from the sampled mixture. Holding out a hospital, device family, or later period addresses a different question. The split should follow the intended deployment change, with adaptation and model selection kept separate from final evaluation. I would report discrimination, calibration, and performance at the intended operating point alongside subgroup results. A stable AUROC does not guarantee stable positive predictive value when prevalence changes, nor stable consequences for the clinical workflow.

### Detection, adaptation, and robustness are different tasks

An out-of-distribution detector tries to flag unfamiliar inputs; it does not establish whether their predictions are wrong. A familiar-looking case can still belong to a subgroup with poor performance, and changed labeling may be invisible from images alone. Adaptation uses target-setting information to modify the system, while generalization evaluates transfer without such adjustment. Recalibration may address risk estimates in a particular setting, but it does not by itself repair missing diagnostic features or invalid evidence use.

## Where it touches my work

I would organize gallbladder ultrasound evaluation around plausible changes: a new device, a different operator group, or a different referral service. For each comparison, I would document available clinical factors and assess both prediction quality and evidence alignment. If alignment changes, I would investigate whether the model changed its dependence, the clinical measurements changed, or the patient range became different. Repeating the audit with the same definitions would make those alternatives more inspectable than reporting a single external performance number.

## What I have not resolved

- Which acquisition changes can be simulated credibly, and which require actual examinations from the target setting?
- How can I distinguish a shift in clinical evidence use from a shift in the reliability of the clinical annotations?
- What evaluation is sufficient when a model may encounter combinations of patient characteristics and devices absent from development?
- How should an audit respond when performance stays stable but the supporting evidence becomes less clinically aligned?

## References

- Koh et al., [WILDS: A Benchmark of in-the-Wild Distribution Shifts](https://proceedings.mlr.press/v139/koh21a.html), ICML, 2021.
