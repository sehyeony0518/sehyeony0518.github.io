---
layout: study_note
title: "Dataset Design, Ground Truth, and Reference Standards"
description: "What counts as truth in a medical dataset, and how that choice bounds every result that follows."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
order: 2
source: "Independent study"
written: true
updated: "2026-09-08"
---

A medical dataset's labels are observations produced by a reference process, not direct access to an unquestionable biological truth. Dataset design determines which patients enter that process and which claims the resulting labels can support.

## Core question and definition

I distinguish the clinical condition of interest from the recorded target used to evaluate it. A reference standard is the method used to establish that target, such as pathology, expert interpretation, laboratory testing, follow-up, or a specified combination. Calling it “ground truth” should not erase its limitations.

The central question is whether the reference identifies the intended condition adequately in the population and time window being studied. A carefully collected label can still answer the wrong question, and an excellent reference in selected surgical patients may not characterize the broader diagnostic population.

## Key concepts

### Define the condition before choosing the reference

A lesion's histology, an imaging feature, and a clinical syndrome require different evidence. Pathology may establish tissue diagnosis, but it does not establish whether a particular feature was visible in the supplied ultrasound frame. I would specify whether the label concerns the patient, lesion, examination, or image before deciding which source can justify it.

### Sampling determines the cases available

Consecutive or otherwise systematically sampled eligible patients can preserve the clinical range of presentations better than selecting obvious positive and negative examples. A surgical-only cohort may exclude many indeterminate or conservatively managed findings. Case-control enrichment can support some comparisons, but its artificial disease frequency cannot directly establish predictive values or referral burden in routine care.

### Verification can depend on the index test

Partial verification occurs when only some participants receive the reference procedure; differential verification uses different reference methods across participants. These can bias accuracy when verified cases are systematically selected or reference methods differ in accuracy. Incorporation bias arises when the index test contributes to its own reference classification. [QUADAS-2](https://pubmed.ncbi.nlm.nih.gov/22007046/) provides a framework for examining these risks and applicability concerns.

### Timing and matching are part of the label

The reference must correspond to the imaged lesion and relevant disease state. A later specimen may be highly informative, but treatment, stone passage, or disease progression can change the comparison. A benign result from one sampled lesion does not automatically label every lesion in the examination. I would retain the reference date, method, anatomical match, and any unresolved uncertainty.

## Worked examples in medical AI

In a hypothetical gallbladder malignancy dataset, positive cases might have surgical pathology while negative cases are defined by an unrevealing report. This creates different levels and types of verification. A model evaluated against those labels could be penalized for detecting an overlooked lesion or rewarded for recognizing the acquisition patterns associated with surgery. The reference process needs examination before either interpretation is accepted.

A second hypothetical dataset might assign a pathology diagnosis to every frame from a patient's study. Frames that do not depict the lesion then receive a label unsupported by their visible content. That design may still support an examination-level prediction task if the complete study is supplied and aggregation is defined. It does not automatically support claims about image-level lesion recognition.

## Evaluation methods and limitations

I would document participant flow from eligibility through inclusion, reference assessment, and analysis, including exclusions and unavailable results. [STARD 2015](https://doi.org/10.1136/bmj.h5527) asks for reporting that makes these choices assessable, including the reference standard and handling of indeterminate or missing results. A complete report does not remove bias, but it allows readers to identify what the study actually estimates.

Sensitivity analyses can compare reference-standard groups, restrict to adequately matched cases, or examine plausible alternative labels. None restores missing truth without assumptions. Restricting to the strongest reference can increase selection bias, while treating all uncertain cases as negative introduces a different distortion. I would report these tradeoffs rather than present one cleaned dataset as uniquely correct.

## Research connections and open questions

For clinical faithfulness auditing, I need linked but separate records for diagnosis, observable findings, and reference provenance. That separation helps distinguish a model's failure to use clinical evidence from a disagreement created by incomplete or mismatched labels.

- How should I combine pathology and longitudinal follow-up without implying that they provide identical verification?
- Which excluded or unverified patients most limit the relevance of my gallbladder dataset?
- How can uncertainty in the reference be represented without turning every difficult case into an unusable label?

## References

- Whiting et al., [QUADAS-2: a revised tool for the quality assessment of diagnostic accuracy studies](https://pubmed.ncbi.nlm.nih.gov/22007046/), Annals of Internal Medicine 2011.
- Bossuyt et al., [STARD 2015: an updated list of essential items for reporting diagnostic accuracy studies](https://doi.org/10.1136/bmj.h5527), BMJ 2015.
