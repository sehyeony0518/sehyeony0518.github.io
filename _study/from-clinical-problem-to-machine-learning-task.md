---
layout: study_note
title: "From Clinical Problem to Machine Learning Task"
description: "The translation step where most medical AI projects are decided, long before a model is trained."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
order: 1
source: "Independent study"
written: true
updated: "2026-09-08"
---

Translating a clinical problem into a machine learning task means specifying which decision the model should support, using what information, for whom, and at what point in care. That translation determines what a successful prediction would actually accomplish.

## Core question and definition

A clinical concern such as missed gallbladder malignancy does not uniquely define a classification problem. Possible tasks include improving acquisition, detecting a lesion, characterizing an identified abnormality, or prioritizing specialist review. Each uses different inputs and creates different consequences when it fails.

I would define a task through its population, setting, prediction unit, input availability, target, intended user, and downstream action. This is more than a project description. It constrains the dataset, reference standard, comparison method, and interpretation of every reported metric.

## Key concepts

### Start with a decision and comparator

The relevant question is what would change if the model were available. A second reader, triage aid, and replacement test occupy different positions in a workflow. Their comparators may be usual care, another diagnostic method, or the same clinician without assistance. I would identify the present source of failure before assuming that better image classification is the appropriate intervention.

### Match the prediction unit to the action

A frame, lesion, examination, and patient are different units. If the clinical action follows an examination, frame-level accuracy is only an intermediate result. A rule for aggregating predictions must be specified and evaluated. Otherwise, the model may appear successful on selected images while failing when the lesion is absent from most frames or several findings coexist.

### Define what is available at prediction time

Inputs should reflect the intended point of use. A system meant to detect an unsuspected lesion cannot silently depend on a frame selected after recognition or a diagnostic annotation added later. Clinical history may be appropriate when available to the intended user. I would explicitly distinguish an image-only task from a multimodal task rather than allow that boundary to emerge accidentally.

### Keep the target close to the intended claim

Pathology, an imaging finding, a clinician's decision, and a later outcome represent different targets. Predicting surgery does not directly mean predicting malignancy, because surgery also reflects symptoms, uncertainty, and patient suitability. [TRIPOD+AI](https://doi.org/10.1136/bmj-2023-078378) emphasizes transparent reporting of prediction-model aims and methods. Clear reporting helps expose a target mismatch, but does not repair it.

## Worked examples in medical AI

Consider a hypothetical gallbladder acquisition aid. Its immediate task is to identify whether the neck and relevant wall are adequately visualized. The reference might be expert assessment of examination completeness, and useful outcomes could include fewer incomplete studies without excessive repeat scanning. A cancer diagnosis would be an indirect and poorly matched label for this task.

A separate hypothetical system characterizes an already identified mural lesion. It may legitimately receive targeted views and lesion localization. Its evaluation should include difficult benign mimics and the actual referral population. Comparing these two systems through the same frame-level AUROC would conceal their different purposes. Neither design can claim clinical benefit simply because its internal prediction target is learned accurately.

## Evaluation methods and limitations

I would review the task specification with clinicians using concrete cases, including missing views, incidental findings, multiple lesions, and uncertain diagnoses. The aim is to expose situations where the output has no clear meaning or where the proposed action requires unavailable information. Dataset inclusion criteria should follow that specification rather than redefine the clinical problem around convenient records.

Evaluation then needs to test both the model and its role in use. [DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9) addresses early live evaluation of AI decision support, including human interaction and workflow. A useful standalone score may still create inappropriate referrals, delays, or misplaced confidence. These effects require evaluation beyond retrospective prediction accuracy.

## Research connections and open questions

For my gallbladder and clinical faithfulness work, task definition determines which evidence reliance should be expected. A model supporting acquisition and one estimating malignant likelihood should not be judged against the same explanation criteria, even when they process similar images.

- Which clinical decision offers a realistic opportunity for improvement with the data I can obtain?
- What information is genuinely available before that decision, and what enters the record only afterward?
- How should a model's output represent an examination that cannot answer the intended question?

## References

- Collins et al., [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378), BMJ 2024.
- Vasey et al., [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9), Nature Medicine 2022.
