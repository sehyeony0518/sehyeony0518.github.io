---
layout: study_note
title: "Auditable-by-Design Medical AI"
description: "Building models whose evidence can be checked, instead of auditing whatever is left afterwards."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "auditing"
category_title: "Evidence Auditing"
order: 5
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-11-29-concept-bottleneck-models"
---

Auditable-by-design medical AI makes its inputs, evidence pathway, outputs, and limitations accessible to planned checks. It treats auditability as a design requirement, while leaving clinical validity and appropriate reliance to be demonstrated.

## Core question and definition

The question is what an independent reviewer would need to examine a clinical claim after the system is built. I use auditability to mean the practical ability to reconstruct relevant behavior, inspect the evidence available, and run meaningful tests. It is broader than interpretability and more concrete than a promise of transparency.

A simple architecture can still be difficult to audit if its preprocessing, training population, or reference labels are undocumented. Conversely, a complex model can support useful audits when the relevant artifacts and interfaces are preserved. The design should make particular claims checkable rather than imply that every internal operation will become understandable.

## Key concepts

### Define the input and decision contract

The system should specify its intended patient group, point of use, available inputs, output meaning, and response to inadequate data. A model used before lesion recognition should not silently require postmeasurement frames. I would make these assumptions testable through representative examples and documented exclusions. [Model Cards](https://doi.org/10.1145/3287560.3287596) provide a framework for reporting intended uses, evaluation conditions, and limitations.

### Make the evidence pathway inspectable

A concept-based design can expose predicted clinical features and their role in the final score. In f(x) = g(c(x)), changing c allows inspection of the downstream computation, as illustrated by [concept bottleneck models](https://proceedings.mlr.press/v119/koh20a.html). This is only a semantic explanation if c actually represents the declared concepts. A hidden bypass or information encoded within concept scores can undermine that interpretation.

### Preserve the artifacts needed for replay

An audit needs the relevant model version, preprocessing, output settings, and links to source evidence. Intermediate features may be useful when their retention serves a defined test. I would also preserve how reference labels were established and which images supported them. A later reviewer should be able to distinguish model change from altered image selection or postprocessing.

### Design uncertainty and review behavior

The system should distinguish an absent finding from one that cannot be assessed, and specify what happens when its inputs are inadequate. Exposed feature predictions need evaluation for accuracy and uncertainty, just like the final output. An explanation display can increase confidence without increasing correctness, so the interface itself belongs within the evaluation scope.

## Worked examples in medical AI

Consider a hypothetical gallbladder characterization system that records the analyzed views, identifies whether lesion attachment is assessable, and exposes predictions for selected wall and acoustic findings. The diagnostic output can then be checked against both source images and intermediate claims. This design creates opportunities for audit; it does not establish that the feature detectors or final score are clinically reliable.

A contrasting hypothetical implementation exports only a malignancy probability and a heatmap, without recording which frame or preprocessing version produced them. Even if its retrospective discrimination is similar, investigating an unexpected clinical result becomes harder. The relevant design difference is whether a reviewer can reconstruct the case, test candidate cues, and identify where the evidence pathway failed.

## Evaluation methods and limitations

I would test auditability directly by giving an independent reviewer predefined questions and checking whether the retained artifacts permit reproducible answers. Examples include tracing an output to its inputs, reproducing a score, evaluating an intermediate feature, and comparing behavior after a controlled edit. Missing access or ambiguous records should count as limitations rather than being hidden behind documentation volume.

Clinical evaluation must still assess performance, calibration, failure handling, and the effects of human interaction. [DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9) addresses early live evaluation of decision support in context. A concept interface may create extra review burden or encourage users to accept familiar but incorrect feature descriptions. Audit-friendly structure therefore needs independent testing, and exposing internal quantities does not make those quantities meaningful.

## Research connections and open questions

For my gallbladder work, I would design the annotation scheme, evidence pathway, and audit protocol together. The aim is to make clinical-faithfulness claims easier to challenge and refine, including failures that remain despite good diagnostic accuracy.

- Which intermediate findings are worth exposing because they support reliable review rather than merely adding interface detail?
- How can a design preserve clinically useful information outside an incomplete concept vocabulary without making the decision pathway uncheckable?
- What evidence should trigger a new audit when preprocessing, acquisition practice, or the clinical workflow changes?

## References

- Mitchell et al., [Model Cards for Model Reporting](https://doi.org/10.1145/3287560.3287596), FAT* 2019.
- Koh et al., [Concept Bottleneck Models](https://proceedings.mlr.press/v119/koh20a.html), ICML 2020.
- Vasey et al., [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9), Nature Medicine 2022.
