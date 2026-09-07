---
layout: study_note
title: "Data Leakage and Validation Design"
description: "How information crosses from test to train in medical data, and what each validation design can claim."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
order: 4
source: "Independent study"
written: true
updated: "2026-09-08"
---

Data leakage occurs when model development gains information that should be unavailable for an independent evaluation, or when prediction uses information unavailable at its intended clinical moment. Validation design determines which future uses a performance estimate can reasonably represent.

## Core question and definition

I want to distinguish learning a clinical relationship from benefiting from accidental access to the answer, related patients, or the evaluation set. Leakage can occur without copying a diagnostic label into the input. Repeated images, preprocessing, model selection, and decisions made after inspecting test errors can all compromise independence.

A validation result is conditional on its design. Performance on new patients from the same source answers a different question from performance at a new hospital. Neither becomes a general statement about deployment simply because the test set was called independent.

## Key concepts

### Identify the unit that must remain independent

Medical data are nested: frames within examinations, examinations within patients, and patients within institutions. If the intended claim concerns unseen patients, all examinations from a patient should remain in one partition. An image-level split may distribute nearly identical views across training and testing. Legitimate use of earlier patient history requires a different, explicitly longitudinal task definition.

### Include the whole pipeline inside the boundary

Imputation, normalization learned from data, feature selection, hyperparameter tuning, calibration, and threshold selection belong to model development. They must use development data rather than the final test set. During cross-validation, learned preprocessing must be fitted within each training fold. A transformation computed separately from each image is different from estimating population parameters across the entire dataset.

### Separate selection from performance estimation

Using the same cross-validation results to select a model and report its performance can produce optimistic estimates. [Varma and Simon](https://doi.org/10.1186/1471-2105-7-91) demonstrated this problem and examined nested cross-validation. Inner folds select the procedure; outer folds estimate its performance. That estimate concerns the development procedure under the specified sampling scheme, rather than independently certifying the final model refitted on all available data.

### State what each split tests

A random patient split mainly tests generalization within the sampled source. A temporal split tests later cases under the changes that actually occurred. A geographic split tests transfer to the particular held-out sites. Patient separation remains necessary where identities overlap. Temporal and external validation can reveal additional failures, but neither guarantees performance under every future population or acquisition change.

## Worked examples in medical AI

[Wen and colleagues](https://doi.org/10.1016/j.media.2020.101694) examined reproducible evaluation of Alzheimer's disease classification from MRI and documented leakage concerns, including splitting slices rather than subjects. The lesson transfers beyond MRI: abundant image samples do not create abundant independent patients.

In a hypothetical gallbladder study, adjacent cine frames could enter different partitions while retaining the same lesion, speckle pattern, and annotations. High test accuracy might then partly reflect recognition of a familiar examination. A separate availability problem arises if a detection model receives only frames selected after a radiologist identified the lesion. Patient separation would address the first problem but would not make the second task representative of initial detection.

## Evaluation methods and limitations

I would establish patient and examination identifiers before generating frames or augmentations, then audit overlap, duplicate files, and suspiciously similar images. The audit should also trace how preprocessing parameters, checkpoints, thresholds, and calibration were selected. File hashes alone cannot identify every duplicate after cropping or compression.

A final holdout should remain outside adaptive development. If repeated inspection changes the model, that set has become part of development and a fresh evaluation is needed. Conversely, a low external score does not by itself prove leakage in the original study. Population differences, reference standards, and acquisition changes also require investigation.

## Research connections and open questions

For my gallbladder shortcut audits, independence must extend to the evidence used to design the audit. A test repeatedly adapted to familiar failures can overstate how reliably it will identify shortcuts in new models or datasets.

- Which identifiers and acquisition records are sufficient to detect related examinations in retrospectively assembled data?
- How much temporal and institutional variation can my validation design actually represent?
- How should I reserve cases for evaluating an audit after using other cases to develop its intervention rules?

## References

- Varma and Simon, [Bias in error estimation when using cross-validation for model selection](https://doi.org/10.1186/1471-2105-7-91), BMC Bioinformatics 2006.
- Wen et al., [Convolutional neural networks for classification of Alzheimer's disease: Overview and reproducible evaluation](https://doi.org/10.1016/j.media.2020.101694), Medical Image Analysis 2020.
