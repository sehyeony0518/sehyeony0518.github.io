---
layout: study_note
title: "Explanation Faithfulness versus Plausibility"
description: "Looking right to a clinician and reflecting the model's computation are different properties, and the gap between them is where trouble lives."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "alignment"
category_title: "Clinical Alignment & Interpretability"
order: 4
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-03-13-arun-assessing-saliency"
---

An explanation is plausible when it agrees with a reader's expectations; it is faithful when it accurately reflects the relevant behavior of the model. A convincing anatomical display can satisfy the first property while providing little evidence for the second.

## Why it matters here

Plausibility is useful because clinicians can recognize impossible anatomy, irrelevant regions, or incoherent descriptions. Their judgment addresses clinical coherence, however, rather than directly observing the model's computation. A faithful explanation could reveal reliance on a shortcut and consequently look clinically wrong. These outcomes need different interpretations.

This distinction is central to my clinical faithfulness research. I want model readouts that are both tied to the predictor and meaningfully connected to independent clinical factors. Neither property can certify the other. If I evaluate only visual agreement, I risk selecting explanations that reassure the reader while leaving the model's actual dependence unresolved.

## The core ideas

### Faithfulness needs a defined explanatory claim

An explanation might claim to identify locally sensitive pixels, allocate a score difference, or summarize dependence on a concept. Each claim requires a different comparison. Faithfulness does not necessarily mean recovering every internal operation, but the scope must be explicit. I would specify the model output, reference conditions, and level of aggregation before evaluating a readout. A method that faithfully measures local sensitivity may still be unsuitable for explaining the evidence supporting a decision over larger, clinically meaningful changes.

### Anatomical plausibility tests agreement with a reference

Overlap with a lesion annotation evaluates spatial agreement, subject to the quality and purpose of the annotation. It does not show which feature inside the region matters, and legitimate contextual evidence may lie outside it. [Arun and colleagues](https://doi.org/10.1148/ryai.2021200267) evaluated saliency methods using localization, model randomization, repeatability, and reproducibility as separate criteria. That separation matters to me: a localization result should remain a localization result until additional evidence supports a claim about the predictor's dependence.

### Model sensitivity is a basic check with limited reach

[Sanity Checks for Saliency Maps](https://proceedings.neurips.cc/paper/2018/hash/294a8ed24b1ad22ec2e7efea049b8737-Abstract.html) tests explanation dependence on learned parameters and training labels. If substantial changes to learned behavior leave an explanation largely unchanged, its interpretation as model-specific evidence deserves scrutiny. Passing such a check is not proof of clinical validity or complete faithfulness. The comparison also needs to match the explanation's claim: some shared image structure may persist legitimately, and numerical similarity depends on normalization and the chosen comparison measure.

### Behavioral tests require credible alternatives

Deletion tests remove highly attributed regions and observe the output; insertion tests restore them from a reference. These tests can examine whether an attribution ranking predicts model behavior under the chosen changes. They can also reward methods that identify regions whose corruption produces unfamiliar inputs. Redundant evidence creates another complication: removing one useful feature may have little effect when another remains. I would compare against controlled alternatives and report the perturbation mechanism, rather than treating a single deletion curve as a universal faithfulness score.

### Clinical alignment needs its own independent evidence

After testing the relationship between readout and model behavior, I still need to ask whether the readout corresponds to clinically meaningful factors. A correlation with a clinical descriptor can be influenced by diagnosis, acquisition, or selection into the annotated sample. I would therefore examine the factor's provenance, relevant stratification, and the stability of the relationship. Clinical alignment supports a bounded claim about the evaluated factors. It cannot establish that the explanation captures every valid cue or excludes every shortcut.

## Where it touches my work

For gallbladder ultrasound, I would report anatomical agreement, model sensitivity, and clinical-factor alignment as separate findings. A plausible map that fails model sensitivity would not support a reliance claim. A model-sensitive explanation pointing to an overlay would instead motivate a shortcut investigation. A readout passing both checks would still need testing against lesion descriptors and acquisition conditions. I would show representative failures alongside successful examples, so the explanation's visual persuasiveness does not become stronger than the evidence supporting its interpretation.

## What I have not resolved

- Which behavioral tests can challenge an explanation without making unrealistic ultrasound inputs the main source of prediction change?
- How should I assess stability when different trained models achieve similar performance through different evidence?
- What evidence would justify using an explanation to influence a clinician's confidence in an individual prediction?
- How can I communicate a plausible explanation whose model faithfulness remains unresolved without inviting reassurance beyond what was tested?
