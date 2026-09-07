---
layout: study_note
title: "Self-Supervised and Weakly Supervised Learning"
description: "Learning from medical data whose labels are scarce, noisy, or only available at the study level."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "systems"
category_title: "Medical AI Systems & Deployment"
order: 3
source: "Independent study"
written: true
updated: "2026-09-08"
---

Self-supervised learning constructs a training signal from the data themselves. Weakly supervised learning uses supervision that is incomplete, coarse, or unreliable relative to the intended task, such as an examination diagnosis without frame-level lesion labels.

## Core question and definition

Both approaches can reduce dependence on detailed expert annotation, but they remove different requirements. Self-supervision replaces manual targets for a pretraining objective. Weak supervision retains external information while accepting a mismatch between the available label and the desired prediction.

I do not understand either approach as learning without assumptions. The choice of augmented views, reconstruction target, bag structure, or label-extraction rule determines what the model is rewarded for learning. Those choices need clinical scrutiny just as a diagnostic label does.

## Key concepts

### Contrastive learning defines what should stay similar

Contrastive methods encourage representations of related views to agree while distinguishing other examples. [SimCLR](https://proceedings.mlr.press/v119/chen20j.html) demonstrates the importance of augmentation choices in this framework. For medical imaging, the definition of a positive pair carries a clinical assumption. Two crops of one image may not contain the same lesion, and strong intensity changes may alter evidence the downstream task needs.

### Reconstruction rewards recoverable image structure

Masked reconstruction trains a model to predict hidden image content from what remains. This can encourage learning of anatomy and spatial context, but the objective measures reconstruction rather than diagnosis. Common texture may dominate the signal while a rare lesion contributes little. I would judge the resulting representation through downstream tasks and evidence audits, not through reconstruction quality alone.

### Multiple-instance learning separates bags from instances

In multiple-instance learning, a bag B = {x_1, ..., x_m} receives a label while individual instances may remain unlabeled. A classical binary assumption is that a positive bag contains at least one positive instance. That assumption is task-dependent. A malignant patient label does not guarantee that the selected ultrasound frames visibly depict malignancy, so bag construction is part of the scientific model.

### Weak labels have structured errors

Report-derived labels, administrative codes, and pseudo-labels from another model can all supply supervision, but their errors may depend on site, wording, disease severity, or acquisition. An unmentioned finding is not automatically absent. Pseudo-labeling can reinforce a teacher's confident mistakes. I would retain label provenance and distinguish uncertainty in the recorded target from uncertainty in the image itself.

## Worked examples in medical AI

[Campanella and colleagues](https://doi.org/10.1038/s41591-019-0508-1) trained computational pathology systems using whole-slide diagnoses rather than exhaustive region annotations. The study demonstrates a practical use of weak supervision when detailed labeling is costly. Its success does not establish that every highly weighted region is a faithful explanation or that the same assumptions hold for ultrasound examinations.

In a hypothetical gallbladder study, self-supervised pretraining could use unlabeled cine clips, followed by examination-level classification from labeled studies. Nearby frames provide related views, but some may omit the lesion or show a different interface. I would compare a clinically reviewed sampling strategy with unrestricted frame pairing, then evaluate whether any performance gain corresponds to better representation of relevant morphology.

## Evaluation methods and limitations

A useful comparison holds downstream labels and evaluation patients fixed while varying the pretraining or supervision scheme. I would report learning curves across annotation budgets, conventional pretraining baselines, and both frozen-encoder and fine-tuned results where relevant. Patient overlap must be checked during pretraining as well as supervised training. Unlabeled access to evaluation cases changes the experimental setting and needs explicit disclosure.

Weak supervision also needs an independently reviewed subset to characterize label errors and instance-level behavior. Attention weights within a bag are not sufficient evidence of lesion localization or causal reliance. External evaluation can reveal whether the method learned transferable clinical structure or source-specific regularities. Label efficiency alone does not establish robustness, and abundant unlabeled data can still be unrepresentative.

## Research connections and open questions

For my gallbladder work, these methods could reduce the amount of detailed annotation needed for representation learning. I would still reserve independently annotated clinical features for auditing, because using the same noisy supervision to train and justify a model risks circular evidence.

- Which ultrasound transformations preserve the clinical factors I want the representation to retain?
- When does an examination-level diagnosis justify a positive bag assumption?
- Can I identify useful pretraining objectives without selecting them solely through downstream classification accuracy?

## References

- Chen et al., [A Simple Framework for Contrastive Learning of Visual Representations](https://proceedings.mlr.press/v119/chen20j.html), ICML 2020.
- Campanella et al., [Clinical-grade computational pathology using weakly supervised deep learning on whole slide images](https://doi.org/10.1038/s41591-019-0508-1), Nature Medicine 2019.
