---
layout: study_note
title: "Post-hoc Model Auditing"
description: "Auditing a model as it stands, and what a structured audit of a deployed system contains."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "auditing"
category_title: "Evidence Auditing"
order: 2
source: "Independent study"
written: true
updated: "2026-09-08"
---

Post-hoc model auditing examines an existing model and its surrounding system against explicit clinical claims. It asks what the current system does, where it fails, and what evidence supports its continued or proposed use.

## Core question and definition

I understand an audit as a structured investigation rather than a collection of favorable metrics. Its scope includes the intended task, inputs, preprocessing, model version, output interpretation, and clinical workflow. Auditing a checkpoint alone may miss failures introduced before or after inference.

“Post-hoc” identifies when the investigation occurs relative to model development. It does not limit the methods to post-hoc explanations, and it does not require that the model already be deployed. [Liu and colleagues](https://pubmed.ncbi.nlm.nih.gov/35396183/) propose a medical algorithmic audit organized around possible errors, their sources, and their clinical consequences.

## Key concepts

### The claim determines the audit

A system intended to flag suspicious lesions needs a different audit from one intended to measure wall thickness. The claim should specify population, setting, user, and decision. I would translate it into testable questions about discrimination, calibration, missing inputs, failure handling, and evidence reliance. An audit cannot establish fitness for an unspecified purpose.

### The deployed system is the unit of concern

Image selection, resizing, normalization, model inference, thresholding, and display can each change behavior. A reproducible audit needs the relevant versions and transformations. If the original system cannot be reconstructed, that is a limitation of the audit itself. Access also matters: output-only testing supports different claims from an investigation that can inspect representations and training records.

### Audit coverage requires several methods

External validation, subgroup analysis, error review, intervention tests, and explanation checks address different failure modes. No one method substitutes for the others. I would include successful cases as well as errors, because a correct prediction can still depend on an unreliable cue. Clinical review should connect an observed failure to the decision it could affect.

### Findings need ownership and follow-up

An audit result should identify the tested condition, evidence, uncertainty, and proposed response. Some findings call for data review or monitoring; others may justify restricting a use case or changing the system. Retesting after a modification requires a new version record. A documented response process makes the audit actionable, but does not turn a limited evaluation into a universal safety guarantee.

## Worked examples in medical AI

[Zech and colleagues](https://doi.org/10.1371/journal.pmed.1002683) evaluated pneumonia models across chest-radiograph datasets and investigated hospital-related information. Their results showed why internal performance can be misleading when site and disease prevalence are associated. I read this as an example of an audit expanding from a performance discrepancy to a candidate mechanism, rather than stopping at an external AUC.

For a hypothetical gallbladder deployment, I would first verify what images reach the model, including whether they are selected after a clinician identifies a lesion. I would then examine performance by machine, clinical presentation, visualization quality, and reference standard. Marker sensitivity or systematic errors in contracted gallbladders would become separate findings with their own evidence and follow-up, rather than being hidden in one aggregate score.

## Evaluation methods and limitations

The audit dataset should represent the intended use and remain separate from development decisions. I would prespecify major comparisons, record exploratory analyses, account for multiple frames per patient, and report uncertainty. Sparse subgroups should remain visible as evidence gaps. Repeatedly tuning on the audit set would turn it into development data and weaken the independence of subsequent claims.

Deployed evaluation also needs attention to human interaction, overrides, and downstream decisions. [DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9) provides reporting guidance for early live clinical evaluation, including the system's use in context. It is not an audit certification. Outcome delays, selective follow-up, workflow changes, and missing records can all limit what monitoring establishes.

## Research connections and open questions

For my gallbladder work, a post-hoc audit is a way to study clinical faithfulness without first changing the model. I would keep descriptive findings, reliance tests, and mitigation experiments distinct, so the report makes clear what was observed and what remains a proposed remedy.

- What minimum access is needed to make a useful clinical-faithfulness claim about a proprietary model?
- How should audit cases be refreshed without losing the ability to compare model versions?
- Which failures can be detected through routine monitoring when definitive diagnostic outcomes are selectively available?

## References

- Liu et al., [The medical algorithmic audit](https://pubmed.ncbi.nlm.nih.gov/35396183/), The Lancet Digital Health 2022.
- Zech et al., [Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs: A cross-sectional study](https://doi.org/10.1371/journal.pmed.1002683), PLOS Medicine 2018.
- Vasey et al., [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9), Nature Medicine 2022.
