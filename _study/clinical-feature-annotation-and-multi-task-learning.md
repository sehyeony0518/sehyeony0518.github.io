---
layout: study_note
title: "Clinical Feature Annotation and Multi-Task Learning"
description: "Building supervision from structured sonographic findings rather than the diagnosis alone."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "hepatobiliary"
category_title: "Hepatobiliary Medicine & Imaging"
subgroup: "Clinical-to-AI Connections"
order: 16
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-11-29-concept-bottleneck-models"
---

Clinical feature annotation records structured sonographic findings separately from the final diagnosis. Multi-task learning can use these findings as additional prediction targets, but the usefulness of that supervision depends on what was actually visible and how it was labeled.

## Clinical overview

A diagnostic label compresses a case. “Gallbladder malignancy” does not specify whether the supplied image shows an irregular margin, focal wall thickening, a solid mass, or only a partial view. Feature annotation preserves some of that intermediate evidence. I see its value first as clinical documentation, before assuming it will improve a model.

The annotation unit needs to match the observation. Echogenicity may be assessable in a frame, mobility requires an examination sequence, and tenderness requires patient interaction. A feature should not be assigned to every image simply because it appeared somewhere in the examination.

## Anatomy and pathophysiology

Sonographic findings describe different tissue and physical properties. Luminal echoes may reflect sludge, stones, or solid tissue; mural thickening can accompany edema, fibrosis, or infiltration. Posterior shadowing and comet-tail artifacts arise through acoustic interactions rather than being direct histological labels. A structured vocabulary should preserve these distinctions.

Features also overlap across diagnoses. Adenomyomatosis can produce thickening with intramural cystic spaces, while inflammation and cancer can both disrupt an otherwise simple wall appearance. [Yu and colleagues](https://doi.org/10.3748/wjg.v26.i22.2967) illustrate this overlap. I would not define a feature as “present” merely because it is commonly associated with the known diagnosis.

## Diagnostic workflow and imaging findings

### Define the feature before collecting labels

Each term needs an operational description and examples of its boundaries. “Irregular margin” should identify which margin and what counts as irregularity. Echogenicity needs a reference tissue where comparison is required. Focal and diffuse wall changes need separate definitions. For measurements, the protocol should specify the plane, endpoints, and relevant preparation. Consistency begins with a shared question, not with a numerical agreement score.

### Record presence and assessability separately

The options should distinguish present, absent, and not assessable, with uncertainty retained when needed. No detectable Doppler flow is meaningful only relative to the acquisition conditions. Mobility cannot be judged when repositioning was not performed or retained. Missing annotations should also be distinguishable from genuinely unassessable features. I would avoid silently converting either state into a negative finding.

### Attach evidence to the appropriate view

A lesion-level record can link findings to supporting frames, clips, and regions. The annotation should identify whether the entire relevant boundary is visible and whether markers obscure it. A wall label derived from one plane should not imply that the same feature is demonstrated in another. This linkage also allows a reviewer to inspect the evidence rather than trust a detached checklist.

### Preserve disagreement and provenance

Readers can disagree because the vocabulary is ambiguous, the image is limited, or the finding is genuinely borderline. Independent initial readings followed by adjudication can separate these possibilities. I would retain the original assessments, reader identities, and reasons for revision. When the purpose is independent morphology assessment, diagnosis and model output should be withheld where feasible; necessary clinical context should be specified rather than inconsistently supplied.

## Differential diagnosis and management context

Structured findings support the differential without replacing it. A shadowing mobile focus and an attached nonshadowing lesion imply different possibilities, but each still needs context. Feature completeness should not be confused with diagnostic certainty. The final clinical assessment may use laboratory results, additional modalities, or pathology that were unavailable to the annotator reviewing a selected image.

## Implications for medical AI

My proposed multi-task model would share an image representation and predict diagnosis alongside selected observable findings. A possible objective is

$$
L = L_{\text{diagnosis}} + \sum_j \lambda_j L_{\text{feature},j},
$$

with unobserved labels excluded from their corresponding losses. The weights express modeling choices, not established clinical importance. [Caruana](https://doi.org/10.1023/A:1007379606734) provides the general multi-task learning framework. I would compare against diagnosis-only training and evaluate each feature, including disagreement and missingness patterns, rather than report only diagnostic improvement.

A separate concept bottleneck constrains diagnosis to pass through predicted concepts, as in [Koh and colleagues](https://proceedings.mlr.press/v119/koh20a.html). Ordinary auxiliary feature heads do not impose that constraint: accurate feature prediction does not prove that the diagnostic head uses those features. For clinical faithfulness auditing, I would test that reliance separately. Neither architecture guarantees that a feature predictor learned anatomy rather than correlated markers, and neither resolves an incomplete or poorly defined clinical vocabulary.

## References

- Yu et al., [Benign gallbladder diseases: Imaging techniques and tips for differentiating with malignant gallbladder diseases](https://doi.org/10.3748/wjg.v26.i22.2967), World Journal of Gastroenterology 2020.
- Caruana, [Multitask Learning](https://doi.org/10.1023/A:1007379606734), Machine Learning 1997.
- Koh et al., [Concept Bottleneck Models](https://proceedings.mlr.press/v119/koh20a.html), ICML 2020.
