---
layout: study_note
title: "Intervention-Based Auditing"
description: "Ablation, masking, and controlled edits as tests of what a prediction actually depends on."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "auditing"
category_title: "Evidence Auditing"
order: 3
source: "Independent study"
written: true
updated: "2026-09-08"
---

An intervention-based audit changes a specified part of the input or computation and measures what happens to the prediction. Its value depends on whether the intervention isolates the evidence named in the question.

## Core question and definition

I want to distinguish a model responding to a clinical feature from a model responding to something correlated with that feature. An intervention makes the comparison explicit: evaluate the same model before and after a controlled change. The comparison is stronger than visual agreement alone, but its interpretation remains conditional on the edit.

For a fixed target score s and transformation T, I can measure Δ_T(x) = s(T(x)) − s(x). This is an effect on the model's output under T. It is not automatically the effect of a clinical feature in isolation, and it is not the effect of changing the patient's disease.

## Key concepts

### Ablation requires a defined replacement

Masking a region can mean setting it to zero, replacing it with a local average, blurring it, or synthesizing replacement tissue. These operations remove different information and introduce different artifacts. I would describe the replacement explicitly rather than write only “the lesion was removed.” Cropping also changes context and scale, so its effect cannot always be attributed to the excluded region.

### Necessity and sufficiency are conditional

Removing evidence tests whether it is needed under that removal procedure. Retaining evidence while removing other content tests a restricted form of sufficiency. Redundant cues can make a useful feature appear unnecessary. An artificial retained-region image can preserve a prediction for reasons unrelated to the intended evidence. These tests need complementary controls before they support a broad reliance claim.

### Controls test the intervention itself

A useful control changes a comparable area, intensity range, or image property without targeting the proposed evidence. Multiple replacement methods can expose sensitivity to the editing technique. Clinical review should assess whether relevant morphology remains interpretable. I would also examine unintended changes around the edited region, especially when a generative method can modify texture beyond the requested target.

### Retraining changes the question

Testing a frozen model measures its response to altered inputs. Removing features and retraining measures what a new training procedure can recover from the remaining data. [Hooker and colleagues](https://papers.nips.cc/paper_files/paper/2019/hash/fe4b8556000d0f0cae99daa5c5c5a410-Abstract.html) introduced a removal-and-retraining benchmark for feature importance. That approach addresses limitations of evaluating corrupted inputs directly, but it does not reveal the unchanged model's exact dependency.

## Worked examples in medical AI

[Lin and colleagues](https://papers.miccai.org/miccai-2024/695-Paper0423.html) investigated calipers and text as shortcuts in fetal ultrasound segmentation. This is a published example where changing clinical annotations helps expose a model's dependence on the documentation process. It motivates a gallbladder marker audit, while leaving the magnitude and form of any local reliance to be established.

In a hypothetical gallbladder experiment, I would compare a marked frame with its original unmarked counterpart when available. Removing a caliper over the wall through inpainting would be a less direct comparison because the hidden tissue must be estimated. A separate intervention suppressing posterior shadowing would need review for changes to the stone and surrounding tissue. These interventions target different evidence and should not be summarized as one generic robustness test.

## Evaluation methods and limitations

I would preserve model weights, preprocessing, and the target output, then report paired score changes and clinically relevant decision changes. Multiple edits from one patient are correlated observations. Uncertainty estimates should reflect that structure, and primary contrasts should be specified before examining favorable examples.

An intervention audit should report edit validity alongside prediction effects. Large changes under visibly implausible edits are difficult to interpret; small changes can reflect redundancy, output saturation, or incomplete removal. Performance against an unchanged disease label can measure information loss, but a synthetic disease-changing counterfactual needs its own justified target. Neither visual realism nor stable predictions establishes that the intended feature was isolated.

## Research connections and open questions

For clinical faithfulness auditing, I see interventions as tests of specific dependence hypotheses in an existing gallbladder model. I would combine them with independent feature annotations and report where realistic isolation was impossible, rather than treat every editable pixel pattern as a valid clinical factor.

- Which gallbladder findings can be altered independently enough to support a meaningful paired comparison?
- How should I quantify edit validity when the source tissue is obscured by an annotation?
- What controls distinguish reliance on posterior acoustics from sensitivity to the texture changes introduced while editing them?

## References

- Hooker et al., [A Benchmark for Interpretability Methods in Deep Neural Networks](https://papers.nips.cc/paper_files/paper/2019/hash/fe4b8556000d0f0cae99daa5c5c5a410-Abstract.html), NeurIPS 2019.
- Lin et al., [Shortcut Learning in Medical Image Segmentation](https://papers.miccai.org/miccai-2024/695-Paper0423.html), MICCAI 2024.
