---
layout: study_note
title: "Spurious Correlations in Medical AI"
description: "Associations that hold in the training distribution and carry no clinical meaning, and how to tell them apart from real signal."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "causality"
category_title: "Causality, Bias & Shortcuts"
order: 4
source: "Independent study"
written: true
updated: "2026-09-08"
---

A spurious correlation is an association that appears useful for prediction but does not provide the evidence the intended clinical claim requires. I use the term cautiously, because an unfamiliar or noncausal feature is not automatically an invalid diagnostic signal.

## Core question and definition

The question is whether a cue predicts the target because it reflects relevant clinical information or because of a contingent relationship in the dataset. Such relationships can arise through acquisition, selection, documentation, or chance.

An association is a property of the data distribution; reliance is a property of the trained model. Finding a cue-label relationship establishes an opportunity for shortcut learning. Showing that a classifier uses that opportunity requires additional evidence about its predictions.

## Key concepts

### Statistical significance does not establish clinical meaning

A small p-value can support incompatibility with a specified null association under the analysis assumptions. It does not identify the source of the relationship, its usefulness elsewhere, or its relevance to pathology. A large dataset can estimate an institution-specific association very precisely. I would therefore ask how the variables were generated and what would preserve their relationship before interpreting statistical strength as diagnostic evidence.

### Conditional comparisons can test alternative explanations

Let N be a suspected nuisance, C measured clinical factors, and Y the target. The condition P(Y|N,C)=P(Y|C) means N adds no information about Y after C is known. It does not prove that N is clinically meaningless: N could duplicate valid information, and C may be incomplete or measured poorly. Failure of the condition likewise does not establish a valid diagnostic mechanism.

### Stability depends on which environments are observed

A cue-label relationship that changes across hospitals or protocols is a candidate for further investigation. Persistence across those settings is useful evidence, but the settings may share the same referral or recording practice. I would avoid defining “real signal” solely as an association that survives external evaluation. The environments must vary the suspected source of the association while allowing a meaningful comparison of the clinical target.

### Diagnostic evidence can be an effect of disease

Many useful imaging findings are consequences of pathology, not causes of it. Conversely, a marker added after clinical suspicion may predict disease while primarily recording a clinician's prior decision. The relevant distinction concerns the intended diagnostic role and timing. I need to separate evidence visible in the tissue from information introduced by the care process, without assuming that every contextual variable is inappropriate for every clinical task.

## Worked examples in medical AI

[Winkler and colleagues](https://pubmed.ncbi.nlm.nih.gov/31411641/) compared dermoscopic images with and without surgical skin markings. Adding markings increased melanoma scores for benign nevi and increased false-positive classifications in the evaluated network. This demonstrates sensitivity to an introduced cue. I would not infer the exact training association from that result alone, because showing that a cue changes predictions does not reconstruct how the model acquired the behavior.

In a hypothetical gallbladder dataset, a particular caliper style appears mainly on images selected for further assessment. The style could predict the recorded diagnosis despite carrying no lesion morphology. A comparison including marked benign cases and unmarked suspicious cases would help separate the cue from the clinical finding. If those combinations are absent, the observed data provide little basis for distinguishing them.

## Evaluation methods and limitations

I would inspect cue-label associations within clinical and acquisition groups, compare simple cue-only baselines, and test performance where the association weakens or reverses. These analyses should preserve patient grouping and distinguish exploratory discoveries from comparisons specified before evaluation. A baseline's success identifies predictive opportunity, not image-model reliance.

Controlled cue additions or removals can test reliance more directly, but their realism and unintended effects need assessment. Removing an overlay may also erase underlying tissue; changing texture may alter clinical evidence. Agreement across observational comparisons and credible interventions supports a narrower, stronger conclusion than a heatmap or correlation alone.

## Research connections and open questions

For clinical faithfulness auditing in gallbladder ultrasound, I want candidate spurious cues paired with independently defined clinical factors. The aim is to determine both whether the cue drives predictions and whether clinically relevant evidence remains informative when that cue is challenged.

- How can I distinguish a redundant clinical signal from an irrelevant proxy when both correlate with the same descriptor?
- Which environments would actually break a suspected acquisition-label association?
- What evidence is sufficient to call an unfamiliar image feature spurious rather than merely unexplained?

## References

- Winkler et al., [Association Between Surgical Skin Markings in Dermoscopic Images and Diagnostic Performance of a Deep Learning Convolutional Neural Network for Melanoma Recognition](https://pubmed.ncbi.nlm.nih.gov/31411641/), JAMA Dermatology 2019.
