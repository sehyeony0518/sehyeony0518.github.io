---
layout: post
title: "Confidence Matters: Saurabh Sharma on Selective Knowledge Transfer in Medical Image Classification"
date: 2026-09-05 12:00:00 +0900
description: "Notes on UDCD: mean-teacher self-distillation, contrastive relation matrices, entropy-based confidence weighting, and why a medical-AI student should not imitate every signal from its teacher equally."
tag: "MICCAI"
related_posts: false
---

Knowledge distillation is usually described through a reassuring metaphor: an experienced teacher passes its knowledge to a student, and the student becomes more accurate without becoming larger.

But what happens when the teacher is uncertain, or worse, when the teacher has learned the same class imbalance and shortcuts that already exist in the training data?

This post is based on Saurabh Sharma's RISE-MICCAI Journal Club presentation of [*Confidence Matters: Enhancing Medical Image Classification Through Uncertainty-Driven Contrastive Self-Distillation*](https://papers.miccai.org/miccai-2024/153-Paper1765.html), published at MICCAI 2024 with Atul Kumar and Joydeep Chandra (IIT Patna), with an [official implementation](https://github.com/philsaurabh/UDCD_MICCAI) on GitHub. ([MICCAI Society][1])

The method: **Uncertainty-Driven Contrastive Self-Distillation (UDCD)**: targets medical image classification under data scarcity, class imbalance, high inter-class similarity, and high intra-class variance. Its central idea is simple even though the implementation is dense:

> Knowledge should not be transferred merely because it came from the teacher. The amount transferred should depend on how confident the models are in that knowledge.

Any errors of interpretation are mine.

## Part 1. A teacher can transfer its mistakes

Distillation adds supervision beyond hard labels: the teacher's soft probabilities, representations, and inter-class relations, "dark knowledge", reveal which classes the teacher considers similar and why. Under limited data this extra regularization helps.

But more transferred knowledge is not automatically better knowledge. A teacher trained on an imbalanced dataset reproduces its majority-class preference in its soft predictions and its representation geometry. If the student imitates every signal equally, distillation reproduces the teacher's weakness rather than correcting it. The question is not only *how can the student receive more knowledge* but *which knowledge should the student trust*.

## Part 2. UDCD is self-regularization, not compression

UDCD's teacher is not a separately trained expert. It is a **mean teacher**: an exponential moving average of the student's own parameters, updated as θ_T ← α·θ_T + (1−α)·θ_S. The student learns by gradient descent; the teacher follows slowly, integrating information across steps into a smoother target, and avoiding the need to train a dedicated teacher for every disease, when the data are already too scarce to train one model reliably.

Teacher and student share the same architecture, and at inference the teacher and projection heads are discarded, so deployment cost equals the plain student. The contribution is therefore best understood as **self-distillation for regularization** rather than model compression, the teacher is useful because it is a temporally smoothed student, not because it holds independent clinical expertise.

## Part 3. Why medical images make ordinary distillation difficult

Three dataset properties motivate the design. **High intra-class variance**: two fundus images with the same diabetic-retinopathy grade can differ greatly in illumination, lesion distribution, and field of view. **High inter-class similarity**: adjacent severity grades or skin-lesion categories may differ by only subtle local patterns. **Class imbalance**: HAM10000's largest class dominates while several minority classes have only hundreds of examples: and in supervised contrastive learning, the majority class also supplies far more positive pairs, so the learned geometry tilts toward classes that already dominate.

## Part 4. Relation matrices transfer structure, gated by entropy

Each image is processed in two augmented views (one by the student, one by the teacher) and trained with weighted cross-entropy (favoring rare classes), KL distillation, supervised contrastive learning, and relational alignment.

The distinctive component is the **Contrastive Relation Matrix (CRM)**. Class-level anchors are built from memory embeddings, and every example is described by its similarity to all *n* anchors, so a minority class occupies a defined position in the geometry rather than being drowned out by sample counts. The student is then trained (via a Huber loss) to reproduce the teacher's *relational structure* (which classes are near, how clusters are organized) instead of copying embedding coordinates point by point. A hard label cannot express that an image graded "mild" sits closer to "severe" than to "normal"; the CRM can.

The gate on all of this is **predictive entropy**: u(x) = −Σ p·log p. Concentrated predictions (low entropy) count as confident. Normalized entropy yields certainty factors that regulate how strongly the teacher's relations and the student's own contrastive signal influence training relative to plain supervision. When a signal looks unreliable, the student leans back on the labels.

One caution: this is entropy as an **internal training-control signal**. The paper does not show the probabilities are calibrated, separate epistemic from aleatoric uncertainty, or support clinical abstention. "Uncertainty-driven" here means loss weighting, not a validated confidence system a clinician could safely read.

## Part 5. What the experiments show

On **APTOS** (3,662 fundus images, five DR grades): 85.01% accuracy, 73.38% average precision, 71.42% recall, 71.31% F1, the best accuracy and AP among reported methods, though SSD-KD edged recall and CRCKD edged F1. On **HAM10000** (10,015 dermoscopic images, seven classes): 90.28% accuracy, 85.12% AP, 83.83% F1, with one baseline still higher on recall. Under artificially severe imbalance (largest/smallest class ratio 144), UDCD held 90.24% accuracy and 87.84% AP, gains of roughly 2–5 accuracy points and up to 11 AP points over the nearest baselines depending on the setting.

The pattern: UDCD's advantage is not maximal sensitivity but a **stronger balance across metrics as class frequencies and data volume change**. Supporting analyses: t-SNE cluster separation, few-shot fractions, multiple backbones (DenseNet/ResNet/EfficientNet/MobileNet), and ablations, are consistent with the intended mechanism, though t-SNE is qualitative and subsampling a public dataset is not the same as validating on a genuinely rare disease or a new hospital.

## Part 6. What the study does not yet establish

**Confidence is not correctness.** If the teacher has learned a scanner artifact or demographic correlate, it may transfer that knowledge *with high confidence*, entropy gating can even amplify an easy-to-learn shortcut. **The teacher is not independent**: as an EMA of the student, its errors are correlated with the student's; smoothing cannot create information the data never contained. **Calibration was not evaluated** (no ECE, reliability diagrams, or selective prediction), **external generalization was not tested** (no site, scanner, or temporal shift), and the authors describe the public code as a basic single-dataset implementation, so full reproduction may need author contact. The scope is single-modality classification; multimodal and federated extensions were discussed in Q&A but not evaluated.

A sharp audience question captured the open issue: are clinically related classes actually *near each other* in the learned space? UDCD improves discriminative geometry; whether that geometry is **clinically aligned**, organized by pathology rather than texture or acquisition, was not measured.

## A researcher's takeaway

The durable contribution is the principle that **knowledge transfer should be selective**. The teacher is treated as useful but fallible, its influence varying per example and objective: a principle that extends to foundation-model transfer, multimodal fusion, and post-deployment updating alike.

But the study also exposes the limit of confidence-driven learning: *confidence tells us how strongly a model believes a signal, not whether the signal is clinically valid.* Uncertainty-driven distillation asks how consistently information is represented; clinical evidence auditing asks **what** is represented and whether it deserves belief. The two are complements: a future framework could gate transfer not only on entropy but on calibration, cross-site stability, subgroup error, and alignment with clinically defined evidence, then test whether the most-trusted knowledge is also the knowledge that survives transfer.

Confidence matters. Confidence in the right evidence matters more.

[1]: https://miccai.org/2025/05/01/join-the-next-rise-miccai-journal-club-may-17-2025/ "RISE-MICCAI Journal Club, May 17, 2025"
[2]: https://github.com/philsaurabh/UDCD_MICCAI "Official UDCD implementation (MICCAI 2024)"
