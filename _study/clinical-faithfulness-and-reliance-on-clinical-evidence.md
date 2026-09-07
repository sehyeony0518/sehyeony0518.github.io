---
layout: study_note
title: "Clinical Faithfulness and Reliance on Clinical Evidence"
description: "My own research question: whether a model's evidence aligns with independent clinical factors rather than merely looking anatomically reasonable."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "alignment"
category_title: "Clinical Alignment & Interpretability"
order: 5
source: "Independent study"
written: true
updated: "2026-09-08"
---

Clinical faithfulness asks whether a model's prediction depends on evidence that is meaningful for the clinical task. In my work, I approach this through the alignment between interpretable model readouts and independent clinical factors, while keeping that alignment distinct from proof of reliance.

## Why it matters here

A correct prediction leaves its supporting evidence unspecified. A model may use a lesion characteristic, an acquisition cue, or a mixture that works within one dataset. Trustworthy medical AI therefore needs evidence about how predictions are supported, alongside evidence about discrimination, calibration, and performance in other settings.

This is the central question in my research: how can I make a claim about clinical evidence use measurable and auditable? I am interested in evaluating trained medical image classifiers without retraining them or requiring direct annotations of faithfulness. That still requires clinical reference information and explicit assumptions about what each measurement can establish.

## The core ideas

### Clinical relevance, explanation faithfulness, and reliance

Clinical relevance concerns whether a feature is meaningful for the diagnostic task. Explanation faithfulness concerns whether a readout accurately reflects the model's behavior. Reliance concerns whether that feature contributes to the prediction under a specified comparison or intervention. These properties can come apart. An explanation might accurately reveal dependence on an irrelevant marker, while an anatomically plausible heatmap might poorly reflect the predictor. I need to specify which property an audit actually tests.

### Independent clinical factors provide an external reference

A clinical factor might be a separately assessed morphological feature, a severity grade, or a measurement with a documented clinical interpretation. Independence here means that the reference was not manufactured from the model readout being evaluated. It does not mean statistical independence from the diagnosis or freedom from measurement error. Blinded assessment can reduce circularity. Agreement between readers and the provenance of each factor still matter, particularly when the factor and diagnostic label come from the same image.

### Anatomical overlap is an incomplete test

A heatmap overlapping the gallbladder tells me where its displayed attribution falls. It does not identify which property within that region supports the prediction. Texture associated with an acquisition setting could occupy the same pixels as a clinically relevant finding. [Arun and colleagues](https://pubs.rsna.org/doi/10.1148/ryai.2021200267) evaluated localization alongside model sensitivity and reproducibility, illustrating why these require separate checks. I would use anatomical overlap to narrow an audit question, then test the proposed evidence more directly.

### Association can support alignment without establishing dependence

Suppose an evidence score increases with an independently assessed clinical factor. That association supports a specific alignment claim, but both quantities could vary with diagnosis, lesion size, or acquisition conditions. Stratification or covariate adjustment may help examine alternatives. The adjustment set needs a clinical rationale, because controlling for a variable on the relevant pathway can remove the relationship of interest. A pooled association also does not establish faithful evidence use for every patient.

### Interventions strengthen the question but introduce assumptions

A reliance test asks how the prediction changes when specified evidence changes. Removing an annotation while preserving the underlying image could test one suspected shortcut. Editing lesion morphology is harder because the edit must preserve other relevant properties and remain plausible. A confidence drop after masking might reflect an unfamiliar input rather than removal of diagnostic evidence. I would combine interventions with matched observational comparisons, negative controls, and evaluation across acquisition settings, reporting what each test leaves open.

## Where it touches my work

For gallbladder ultrasound, I would define the clinical factor before choosing an explanation method: for example, lesion size or attachment morphology, where relevant to the target diagnosis. I would then examine whether a readout tracks that factor, whether the relationship persists across device groups, and whether suspected shortcuts change the output under defensible interventions. The audit record should identify the model, patients, factor definitions, readout, and comparison. I want a result another researcher can challenge at the level of its assumptions and measurements.

## What I have not resolved

- How much converging evidence is sufficient to move from “clinically aligned readout” to a defensible claim of clinical reliance?
- How can I distinguish an unmeasured but valid diagnostic cue from a shortcut without treating current clinical annotations as exhaustive?
- When clinically meaningful and acquisition features are tightly coupled, which interventions can separate them without creating implausible ultrasound images?
- How should uncertainty in clinical factors propagate into an audit result for an individual patient?
