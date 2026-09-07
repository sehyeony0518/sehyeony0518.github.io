---
layout: study_note
title: "Foundation Models for Medical Imaging"
description: "What large pretrained imaging models change about medical AI, and what they do not change about validation."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "systems"
category_title: "Medical AI Systems & Deployment"
order: 1
source: "Independent study"
written: true
updated: "2026-09-08"
---

Foundation models provide pretrained representations or capabilities that can be adapted to multiple downstream tasks. For medical imaging, the question is what this reusable starting point contributes to a specific clinical problem, and what still requires task-specific evidence.

## Core question and definition

[Bommasani and colleagues](https://arxiv.org/abs/2108.07258) introduced the foundation-model framing around broad pretraining and adaptation across downstream uses. Size alone is an incomplete definition. A large classifier trained for one narrow output does not acquire general clinical competence simply by having many parameters.

I understand the practical change as a shift in where learning occurs. A substantial part of the representation is learned before the local study begins. That can reduce downstream annotation needs, but it also makes the model's inherited data, objectives, and limitations part of the study.

## Key concepts

### Pretraining supplies an objective, not clinical understanding

A model may learn through image-text matching, reconstruction, contrastive learning, or supervised segmentation. Each objective rewards particular regularities. Recovering missing pixels does not directly require recognizing malignant morphology, and matching reports may reward language or acquisition correlates. Transfer is useful when the learned structure supports the downstream task, which must be demonstrated rather than inferred from scale.

### Adaptation determines what is being evaluated

With a frozen encoder z = φ(x), a linear probe learns only a restricted mapping from representation to target. Fine-tuning changes some or all pretrained parameters; parameter-efficient methods modify a smaller subset or add trainable components. These procedures test different capabilities and use different amounts of supervision. I would report them separately, including the resources used for model selection.

### Prompts are additional task information

A segmentation prompt can specify which structure to outline, while a text prompt can define candidate categories. The source and precision of that information matter. A bounding box derived from the reference mask creates different conditions from a box drawn by a user who must first find the lesion. “Zero-shot” also needs a precise definition of which downstream labels or examples were unavailable.

### Breadth can propagate shared weaknesses

A reusable encoder can distribute useful representations across tasks, but it can also distribute the same acquisition biases or missing coverage. Uncertain pretraining provenance complicates assessment of benchmark overlap. I would document what is known about training sources and treat unverifiable independence as a limitation, rather than assume that a publicly released checkpoint never encountered the evaluation data.

## Worked examples in medical AI

[Ma and colleagues' MedSAM](https://doi.org/10.1038/s41467-024-44824-z) adapts a promptable segmentation model to medical images across modalities. Its bounding-box prompts help specify the segmentation target. This demonstrates a form of reuse across medical segmentation tasks, but it does not make segmentation equivalent to autonomous lesion detection or diagnosis.

For a hypothetical gallbladder application, I might compare a frozen pretrained encoder with conventional supervised pretraining and training from scratch. If a prompted segmentation model supplies the lesion region, its localization input and failures belong to the evaluated pipeline. A good mask alone would not establish that a downstream malignancy classifier uses wall architecture or other clinically relevant evidence.

## Evaluation methods and limitations

I would compare methods under matched downstream labels, patient splits, and tuning budgets, while reporting differences in pretraining resources. Learning curves can show whether an advantage persists as local annotation increases. External testing should include relevant scanners, lesion presentations, and limited examinations. A broad average across tasks should not conceal poor performance on the particular gallbladder task I care about.

Evaluation also needs the exact checkpoint, preprocessing, prompts, and adaptation procedure. Improvements from manual prompting or local tuning should not be attributed entirely to the base model. Small downstream datasets may produce unstable comparisons, and testing many checkpoints can consume the independence of a validation set. No pretraining objective removes the need to assess calibration, reference quality, and clinical consequences.

## Research connections and open questions

For clinical faithfulness auditing, foundation models raise a useful distinction between evidence available in a representation and evidence actually used after adaptation. I would compare both, asking whether local fine-tuning strengthens clinical reliance or creates a new shortcut.

- Which pretrained features transfer to ultrasound morphology rather than merely to image appearance?
- Does fine-tuning preserve or change the evidence that supports predictions?
- How can I assess evaluation independence when the pretraining dataset is only partly documented?

## References

- Bommasani et al., [On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258), arXiv 2021.
- Ma et al., [Segment anything in medical images](https://doi.org/10.1038/s41467-024-44824-z), Nature Communications 2024.
