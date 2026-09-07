---
layout: study_note
title: "Auditing and Evaluating Generative Medical AI"
description: "What evaluation means when the output is text or an image rather than a label."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "systems"
category_title: "Medical AI Systems & Deployment"
order: 7
source: "Independent study"
written: true
updated: "2026-09-08"
---

Generative medical AI produces structured or open-ended content, such as reports, answers, or synthetic images. Evaluation asks whether that content is supported, complete enough for its purpose, and safe to use in the intended clinical workflow.

## Core question and definition

A classifier usually selects from a defined output set. A generator can express many individually plausible statements or image structures, creating more ways to be partly correct. I would specify whether the task is description, reconstruction, translation, explanation, or data synthesis before deciding what an error means.

The central question is conditional correctness. An image can look medically realistic while misrepresenting the supplied patient, and a report can read naturally while omitting the finding that should change management. Surface quality and clinical validity require different evidence.

## Key concepts

### Likelihood is not factual support

A conditional generator models an output distribution p_θ(y | x), where x may include images, text, or other context. A likely output under that model need not be true for the patient. The training objective rewards patterns in the available data, which may include common descriptions, incomplete reports, and source-specific conventions.

### Text must be evaluated as clinical claims

I would separate incorrect findings, omitted findings, wrong location, mistaken comparison, and inappropriate certainty. Negation can reverse a statement's clinical meaning while changing very few words. A cited sentence also needs checking against its source. Agreement with a reference report is useful, but that report may itself omit details or depend on information unavailable to the model.

### Image realism differs from patient fidelity

Distribution-level similarity does not guarantee preservation of a particular patient's anatomy or disease. [Cohen and colleagues](https://arxiv.org/abs/1805.08841) show how distribution-matching objectives in medical image translation can introduce or remove features. Pixel similarity is also incomplete: a small altered region may carry substantial diagnostic meaning while contributing little to a global image metric.

### Generation creates a sampling and selection problem

Outputs may vary with prompts, decoding settings, random seeds, and model versions. Selecting the best result after inspecting several samples evaluates a different system from one that returns the first output. I would specify the generation and selection procedure, including whether a clinician edits or rejects the result before use.

## Worked examples in medical AI

[Yu and colleagues](https://doi.org/10.1016/j.patter.2023.100802) examined how report-generation metrics align with radiologists' assessments of errors in chest X-ray reports. Their work illustrates why linguistic overlap alone cannot establish clinical correctness. Metrics informed by clinical entities and relations can be more relevant, but still need validation against the errors and population of interest.

In a hypothetical gallbladder audit, an image generator removes a caliper and also smooths the adjacent wall. A changed malignancy score could then reflect loss of wall evidence rather than reliance on the marker. The generated image might appear convincing to a casual viewer while invalidating the intervention. I would require local clinical review and control edits before interpreting that score change.

## Evaluation methods and limitations

For text, I would combine structured factual assessment with expert review of clinically consequential omissions and contradictions. An automated model acting as judge needs its own evaluation, including whether it recognizes unsupported claims and whether its errors correlate with those of the generator. Reader instructions, access to clinical context, and adjudication should be documented.

For generated images, I would test preservation of anatomy and pathology, local artifact introduction, and effects on downstream decisions. If synthetic data augment training, usefulness must be demonstrated on untouched real evaluation cases. Privacy also requires separate assessment; visual novelty does not prove that training examples were not memorized. Across both output types, curated examples cannot replace representative sampling, repeated generation, and reporting of unsuccessful outputs.

## Research connections and open questions

Generative methods could help my gallbladder work create controlled tests or communicate model evidence. I would treat the generator as another model needing an audit, especially when its output becomes the basis for a claim about a classifier's clinical faithfulness.

- How can I verify that a generated edit changes only the intended factor?
- Which report errors matter most for the specific decision the output supports?
- How much agreement with expert review is needed before an automated evaluator can guide model selection?

## References

- Cohen, Luck, and Honari, [Distribution Matching Losses Can Hallucinate Features in Medical Image Translation](https://arxiv.org/abs/1805.08841), MICCAI 2018.
- Yu et al., [Evaluating progress in automatic chest X-ray radiology report generation](https://doi.org/10.1016/j.patter.2023.100802), Patterns 2023.
