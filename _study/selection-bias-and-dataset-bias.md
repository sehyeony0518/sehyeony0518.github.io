---
layout: study_note
title: "Selection Bias and Dataset Bias"
description: "How the assembly of a medical dataset, through who was scanned, labeled, and recorded, writes itself into the model."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "causality"
category_title: "Causality, Bias & Shortcuts"
order: 3
source: "Independent study"
written: true
updated: "2026-09-08"
---

A medical dataset is the endpoint of decisions about access, imaging, documentation, verification, and inclusion. Selection bias and other dataset biases concern how those decisions change the evidence available for a particular clinical or scientific claim.

## Core question and definition

The question I ask is whether the analyzed records support an inference about the intended patients. If S indicates inclusion, the observed distribution is P(X,Y|S=1), which need not equal the target distribution. Selection is not automatically bias: its consequences depend on what is being estimated and how the sample relates to that target.

“Dataset bias” is a broader description that can include selection, measurement, labeling, and representation problems. I would identify the specific mechanism instead of treating imbalance, missingness, and leakage as interchangeable defects. Each requires a different response.

## Key concepts

### Eligibility and inclusion define different populations

The intended users' patients, the hospital's scanned patients, and the research dataset are not necessarily the same group. Referral routes, examination indications, image quality requirements, and exclusions can narrow the sample repeatedly. A dataset can represent a defined specialist population well while poorly representing routine incidental findings. I therefore need both a clinical target population and a record of how eligible examinations became included observations.

### Conditioning on selection can create associations

If two variables influence inclusion, restricting analysis to included cases can associate them even without a corresponding relationship in the target population. [Hernán, Hernández-Díaz, and Robins](https://pubmed.ncbi.nlm.nih.gov/15308962/) describe this structure using causal diagrams. For example, conditioning on surgery can connect clinical suspicion and surgical fitness when both influence treatment selection. I would distinguish this mechanism from simple underrepresentation, because adding more patients through the same selection process may preserve the distortion.

### Verification determines which outcomes become knowable

An imaging dataset may obtain definitive labels only for patients receiving a subsequent procedure. Verification can depend on the initial findings, patient preferences, or follow-up availability. Performance among verified patients then answers a narrower question than performance among everyone scanned. Substituting a different reference for the remaining patients introduces another consideration: pathology, follow-up, and report impressions need not classify the same underlying target with the same error.

### Recording and leakage create additional distortions

A missing descriptor can mean absent, unassessed, unobservable, or omitted from a report. Treating these states identically can make documentation behavior predictive. Leakage is a separate problem: related examinations across development and evaluation, or information recorded after the intended decision, can give the model unavailable advantages. Patient-level separation helps prevent certain leakage routes, but it does not resolve selective verification or restore excluded clinical presentations.

## Worked examples in medical AI

Consider a hypothetical gallbladder study that includes only resected lesions. Pathology provides a strong reference for those lesions, but the selection process preferentially admits cases that reached surgery. A classifier evaluated there estimates discrimination within the surgical cohort. Applying its probabilities to all incidentally detected polyps would require additional evidence about the different population and verification process.

In another hypothetical ultrasound dataset, reviewers retain only frames where the lesion is clearly visible. The resulting model might classify curated views well while failing during examinations with incomplete visualization. Calling this an image-quality problem alone would miss the selection issue: difficult views were excluded before the evaluation could reveal the failure.

## Evaluation methods and limitations

I would document the cohort flow, exclusions, label sources, and timing, then compare included and excluded patients where records permit. Missingness and verification should be examined against both clinical factors and acquisition conditions. Evaluation should use a reference and sampling strategy suited to the intended clinical decision.

Weighting can address measured selection under assumptions. For example, inverse-probability weighting requires credible inclusion probabilities, nonzero inclusion chances in relevant groups, and an appropriate account of outcome-related selection. It cannot reconstruct absent clinical presentations or correct unknown label errors. Sensitivity analyses should make those remaining assumptions visible rather than imply that adjustment produced an unbiased dataset.

## Research connections and open questions

For gallbladder ultrasound AI, I would preserve how each examination and clinical annotation entered the audit. Clinical faithfulness measured only among well-visualized, verified lesions should be reported with that scope, alongside the patients whose evidence use remains untested.

- How can I evaluate unverified lesions without treating follow-up as equivalent to histology?
- Which exclusions are necessary for the intended task, and which remove precisely the cases a deployed model must handle?
- How much of retrospective image selection can be reconstructed from saved frames and examination records?

## References

- Hernán, Hernández-Díaz, and Robins, [A structural approach to selection bias](https://pubmed.ncbi.nlm.nih.gov/15308962/), Epidemiology 2004.
