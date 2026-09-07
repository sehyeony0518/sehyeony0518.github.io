---
layout: study_note
title: "Label Quality and Interobserver Variability"
description: "Evaluating against labels that expert readers themselves disagree about."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
order: 3
source: "Independent study"
written: true
updated: "2026-09-08"
---

Label quality concerns whether an annotation faithfully and consistently represents its intended target. Interobserver variability describes differences between readers, which may arise from error, ambiguous definitions, limited evidence, or genuine uncertainty.

## Core question and definition

The question is not simply how often experts agree. I want to know what they were asked to judge, what information they received, and why their judgments differ. Agreement is evidence about reproducibility under those conditions; it is not proof that the shared interpretation is correct.

This distinction matters when expert annotations supervise a model or serve as its evaluation reference. A model can disagree with a reader for legitimate reasons, but expert disagreement does not excuse arbitrary model errors. Both need examination against the evidence available.

## Key concepts

### Disagreement has several mechanisms

Readers may use different definitions, interpret a borderline finding differently, or see different views. Missing clinical context can also change a diagnostic judgment. I would separate these mechanisms where possible. Treating every disagreement as random label noise hides systematic differences and may encourage preprocessing or adjudication that removes clinically meaningful ambiguity.

### Agreement measures depend on the target

For two readers assigning nominal categories, Cohen's $$\kappa = \frac{p_o - p_e}{1 - p_e}$$, where $$p_o$$ is observed agreement and $$p_e$$ is agreement expected from their marginal category frequencies. [Cohen](https://doi.org/10.1177/001316446002000104) introduced this coefficient. Its dependence on those frequencies means raw agreement and the category table should also be reported. No universal verbal label for a $$\kappa$$ value establishes clinical acceptability.

### Measurement agreement differs from correlation

For continuous measurements, readers can correlate strongly while one systematically measures higher. [Bland and Altman](https://pubmed.ncbi.nlm.nih.gov/2868172/) examine differences between measurements rather than relying on correlation alone. Bias, variability of differences, and dependence on measurement size matter. For segmentation, overlap scores may hide disagreement at a small but consequential boundary. The metric should match the clinical feature and its use.

### Adjudication and soft labels change the reference

Consensus can resolve definitional mistakes and create a usable reference, but it may suppress minority interpretations. I would retain independent initial labels and the reasons for adjudication. A distribution of reader responses can represent disagreement, yet it is not automatically the patient's disease probability. Learning that distribution answers a different question from predicting pathology.

## Worked examples in medical AI

In a hypothetical gallbladder annotation study, readers may disagree about whether a polypoid finding has a broad attachment because the relevant interface is partly obscured. Forcing a binary answer would mix uncertainty about visibility with uncertainty about morphology. Recording “not assessable” separately would make the source of disagreement clearer.

A second hypothetical comparison concerns wall thickness. Readers might place endpoints consistently differently or choose different frames from the same examination. A model trained on one convention could appear inaccurate against the other even when its measurements are internally reproducible. I would examine the measurement protocol and paired differences before interpreting the discrepancy as model failure or human inferiority.

## Evaluation methods and limitations

I would use independent readings, a shared annotation guide, and a subset of repeated readings to distinguish interobserver from intraobserver variability. Reader access to diagnosis, other modalities, and model output should be specified. Sampling should include difficult and limited examinations rather than only clean examples, and confidence intervals should account for repeated observations from patients.

Evaluation against individual readers and against an adjudicated reference answers complementary questions. When a reader is part of the consensus used as truth, comparisons can favor that reader. Multi-reader studies also require attention to both case and reader sampling. An observed human agreement level is not an absolute ceiling for model performance, because the model and reference may use different information or aggregate evidence differently.

## Research connections and open questions

My clinical faithfulness work depends on independently annotated gallbladder findings. I would audit the annotation process itself before treating those findings as an external standard for model evidence. Otherwise, apparent explanation misalignment could partly reflect unstable feature definitions.

- Which disagreements reflect insufficient image evidence, and which can be reduced through a clearer annotation protocol?
- How should reader uncertainty enter feature supervision without being confused with disease risk?
- What agreement is sufficient for a feature to support a reliance audit, given the clinical consequence of misinterpreting it?

## References

- Cohen, [A Coefficient of Agreement for Nominal Scales](https://doi.org/10.1177/001316446002000104), Educational and Psychological Measurement 1960.
- Bland and Altman, [Statistical methods for assessing agreement between two methods of clinical measurement](https://pubmed.ncbi.nlm.nih.gov/2868172/), The Lancet 1986.
