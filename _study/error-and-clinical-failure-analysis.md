---
layout: study_note
title: "Error and Clinical Failure Analysis"
description: "Reading the cases a model gets wrong as evidence about what it learned."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
order: 11
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-11-10-oakden-rayner-hidden-stratification"
  - "2025-10-28-degrave-covid-shortcut"
---

An error case is a disagreement between a model output and a specified reference. Clinical failure analysis asks how that disagreement arose, what consequence it could have, and whether similar failures form a reproducible pattern.

## Core question and definition

I do not expect a gallery of incorrect predictions to explain what a model learned. It can suggest hypotheses, but those hypotheses need comparison cases and deliberate tests. The most visually striking errors may be unrepresentative of the failures that matter most.

Clinical failure is also broader than classification error. An accurate prediction delivered too late, assigned to the wrong examination, or interpreted as more certain than intended can fail within a workflow. I would distinguish failures of the model from failures of the surrounding system while examining their interaction.

## Key concepts

### Locate the failure along the pathway

I would trace acquisition, input selection, preprocessing, prediction, aggregation, presentation, and clinical response. A lesion omitted from the supplied frames creates a different problem from a visible lesion assigned the wrong class. This distinction matters because changing the classifier may not address a failure introduced before inference or after the output reaches a clinician.

### Classify consequence as well as error direction

False positives and false negatives describe disagreement, not severity. A false positive that prompts another view differs from one that leads to an invasive procedure. A missed finding may already be recognized through other evidence or may be the sole opportunity for detection. Consequence categories should follow the intended workflow and should distinguish plausible harm from observed patient outcomes.

### Look inside broad diagnostic labels

[Oakden-Rayner and colleagues](https://doi.org/10.1145/3368555.3384468) describe hidden stratification, where clinically distinct subsets are concealed within a benchmark class. Subtle appearances, uncommon subtypes, and treatment-associated cues can produce different failure rates. I would use clinical knowledge to propose categories, then examine whether those categories explain more than the initial selected examples.

### Turn a pattern into a testable hypothesis

Suppose errors often contain a caliper. That observation is insufficient because calipers may also be common in correct cases. I would compare error rates conditional on marker presence, inspect associated lesion and acquisition differences, and test controlled edits where appropriate. Correct predictions also deserve review: shortcut reliance can produce the right answer until the association changes.

## Worked examples in medical AI

In the hidden-stratification study, pneumothorax classification performed differently on radiographs with and without chest drains. The clinical concern is that recognizing a treatment-associated cue can help on already managed cases while offering less assistance for untreated disease. The subgroup result motivates a mechanism investigation; it does not describe every prediction's computation.

[DeGrave and colleagues](https://doi.org/10.1038/s42256-021-00338-7) investigated shortcut use in radiographic COVID-19 detection through complementary analyses. Their study illustrates why an explanation image alone is insufficient. For a hypothetical gallbladder model, I would similarly combine case review, acquisition metadata, and controlled interventions before attributing a cluster of errors to overlay reliance.

## Evaluation methods and limitations

I would create a review form covering reference validity, visibility of relevant anatomy, lesion characteristics, acquisition quality, model confidence, and possible consequences. Initial clinical assessment should be independent of the model explanation where feasible, so the visualization does not determine the supposed cause. Sampling should include correct cases and uncertain references alongside errors, with denominators retained for every proposed pattern.

A useful taxonomy should support consistent review by more than one assessor. I would record disagreements and separate confirmed causes from plausible explanations. Patterns discovered on one dataset should be tested on another or on reserved cases. Masking and editing can help test dependence, but altered images may introduce artifacts, so even an intervention requires appropriate controls.

## Research connections and open questions

For my clinical faithfulness work, failure analysis is a way to choose audit questions grounded in actual gallbladder cases. I want to connect a prediction's error pattern to independent clinical findings without treating a compelling retrospective story as proof of reliance.

- Which failures are preventable through better acquisition, and which require changes to the model?
- What correct predictions depend on evidence that would fail in another setting?
- How can I prioritize rare but consequential failures without losing a representative view of routine performance?

## References

- Oakden-Rayner et al., [Hidden Stratification Causes Clinically Meaningful Failures in Machine Learning for Medical Imaging](https://doi.org/10.1145/3368555.3384468), ACM CHIL 2020.
- DeGrave, Janizek, and Lee, [AI for radiographic COVID-19 detection selects shortcuts over signal](https://doi.org/10.1038/s42256-021-00338-7), Nature Machine Intelligence 2021.
