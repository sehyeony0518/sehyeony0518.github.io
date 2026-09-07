---
layout: study_note
title: "Causal Inference for Medical AI"
description: "Causal graphs, mediators and colliders, counterfactuals, and intervention as a language for asking why a feature predicts an outcome."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "causality"
category_title: "Causality, Bias & Shortcuts"
order: 2
source: "Independent study"
written: true
updated: "2026-09-08"
---

A feature can predict disease because it reflects pathology, shares a cause with it, or records a consequence of clinical suspicion. Causal inference gives me a language for distinguishing these possibilities and stating what an intervention would need to change.

## Why it matters here

Predictive accuracy does not identify the process that produced an association. Medical AI adds several connected processes: disease generates findings, care decisions determine measurements, and training turns recorded associations into predictions. A causal account helps separate these relationships before I decide what evidence a model should use or how to evaluate it.

In my clinical faithfulness work, I need to distinguish effects on a classifier from effects on a patient. Changing an image can reveal model dependence, but it does not directly identify disease causation. A clinically valid diagnostic feature may itself be a consequence of disease, so requiring every useful feature to cause the diagnosis would be mistaken.

## The core ideas

### A causal graph states assumptions about a process

A directed acyclic graph represents variables and hypothesized direct causal relationships without directed cycles. An arrow is a claim about how one variable affects another, not merely a correlation found in the dataset. Missing arrows are assumptions too. For ultrasound, I might distinguish underlying pathology, visible morphology, acquisition settings, recorded labels, and the model output. The graph should also represent important unmeasured causes or selection processes. The graph makes those assumptions inspectable.

### Confounders, mediators, and colliders play different roles

A common cause of an exposure and outcome can create confounding. A mediator lies on a causal pathway between them. A collider is a common effect of two variables; conditioning on it or certain descendants can open an otherwise blocked path. If clinical concern and surgical fitness both influence surgery, restricting analysis to operated patients can associate them. Adjusting for a mediator can change the target from a total effect, while adjusting for a collider can introduce bias. These roles depend on the specific causal question.

### Observation and intervention answer different questions

$$P(Y \mid X = x)$$ describes outcomes among observations with $$X = x$$. $$P(Y \mid do(X = x))$$ describes a specified intervention that sets X, replacing its usual generating mechanism in the causal model. [Pearl's overview of causal inference](https://doi.org/10.1214/09-SS057) makes this distinction explicit. A comparison between images from different devices remains observational because the patients and examination conditions may differ. Editing a device marker is an intervention on the supplied image, but its effect concerns that edit, not everything that changing the physical device would do.

### Counterfactuals require a model of what remains the same

A counterfactual asks what would have happened for the same unit under a different intervention. A structural causal model supports this by using observed information to infer background conditions, changing a mechanism, and deriving the alternative outcome. The unobserved alternative is not available for direct comparison. A generated ultrasound image that flips a classifier's label is therefore not automatically a valid patient counterfactual. The generator may change unrecognized findings or introduce an image pattern that has no credible clinical counterpart.

### Identification comes before numerical estimation

A causal effect is identifiable when the assumed causal structure and available data determine it. A standard adjustment analysis requires no unmeasured confounding after adjustment, adequate overlap, and a well-defined intervention. More observations do not resolve an effect that the design cannot identify. Nor does a flexible regression model repair omitted common causes by itself. I would state the intervention and assumptions before choosing an estimator, then examine plausible alternatives.

## Where it touches my work

For gallbladder ultrasound auditing, I would draw separate relationships for pathology, clinical descriptors, acquisition, selection for verification, and model predictions. That graph would help decide whether controlling for diagnosis clarifies the audit question or removes the relationship of interest. I would then combine observational comparisons with narrow model interventions, such as a controlled overlay edit. The claim would name its scope: dependence of this classifier on this edited cue, under the conditions tested.

## What I have not resolved

- Which causal assumptions about referral and image selection can clinicians substantiate from the available records?
- How can I define interventions on ultrasound texture without changing several clinically relevant properties at once?
- When do alternative plausible graphs lead to different interpretations of the same evidence-alignment result?
- What validation would justify calling a generated image a clinical counterfactual rather than an input that changes the model's answer?

## References

- Pearl, [Causal inference in statistics: An overview](https://doi.org/10.1214/09-SS057), Statistics Surveys, 2009.
