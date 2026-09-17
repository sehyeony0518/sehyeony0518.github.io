---
layout: post
title: "Robustness Stress Testing in Medical Image Classification"
date: 2026-08-23 12:00:00 +0900
venue: "arXiv preprint"
authors: "Mobarakol Islam, Zeju Li, Ben Glocker (2023)"
description: "Progressive stress testing with five perturbation types at six severity levels, applied to chest X-ray and skin-lesion classifiers, separates iid test accuracy from robustness and finds that pretraining choice, not just architecture, shapes how a model degrades."
og_image: "https://sehyeony0518.github.io/assets/img/og/2026-08-23-robustness-stress-testing-medical-image-classification.png"
related_posts: false
---

**Paper.** *Robustness Stress Testing in Medical Image Classification*. [arXiv manuscript](https://arxiv.org/abs/2308.06889)

This paper asks how to compare models that look similarly acceptable on an ordinary test set but behave differently as input conditions change. The question goes beyond whether performance drops under corruption. It concerns the shape of that decline, the patients affected, and the training choices associated with it. I read the paper after the dermatology clinic-readiness study because a graded evaluation can reveal patterns that a small collection of isolated failure examples cannot.

The proposed tests modify gamma, contrast, brightness, sharpness, and Gaussian blur, using a grid of six severity levels with signed adjustments where applicable. These are test-time transformations of existing images. Within a model's stress evaluation, its trained parameters and the reference labels remain fixed while the input rendering changes. That paired structure helps isolate sensitivity to the chosen transformation, although it still requires checking whether the altered image supports the original clinical target.

The chest X-ray experiments use CheXpert for development and MIMIC-CXR for external evaluation. The skin-lesion experiments use multisite ISIC data. The comparisons include DenseNet, ResNet, ViT, and Swin-Transformer models, together with examinations of pretraining and augmentation. The design therefore covers both controlled appearance changes and differences between data sources. These are complementary tests: a transformation changes specified properties, while an external dataset can differ along many observed and unobserved dimensions.

The authors report that transformer-based models can show more stable operating characteristics than the compared convolutional models under the selected stresses, and that pretraining affects downstream robustness. I would retain the conditional wording. A comparison between particular trained systems does not establish that attention is intrinsically robust or that convolution is intrinsically fragile. Architecture, pretraining, optimization, and augmentation interact, and the tested tasks constrain the result.

A particularly useful finding is that subgroup true positive and false positive rates can move while AUROC remains similar. This is possible because AUROC measures ranking across thresholds, whereas sensitivity and false positive rate describe behavior at an operating rule. A model can preserve much of its ordering while shifting the scale or location of its scores. The threshold used in practice then divides those scores differently.

A simple constructed example makes this distinction explicit. Adding the same constant to every score preserves the ordering of positive and negative cases, so it preserves AUROC. Keeping the numerical threshold fixed can nevertheless change both the true positive and false positive rates. This is not a reconstruction of a particular experiment in the paper. It shows why stable AUROC cannot mathematically guarantee stable decisions.

The subgroup result also needs to be interpreted conditionally. An aggregate performance curve can hide a group-specific decline, but a subgroup point estimate can itself be uncertain. Event counts, group definitions, and uncertainty intervals determine how much a visible difference supports. Broad demographic categories may also conceal differences in acquisition, clinical presentation, or referral patterns. A disparity under stress identifies a problem to investigate; it does not automatically establish the mechanism that caused it.

The strongest contribution is the evaluation structure. Instead of asking whether a model passes one corruption level, the analyst can inspect where deterioration begins, whether the direction of a change matters, and whether performance rankings reverse. That is useful for model selection and failure analysis. It can also reveal that a method with stronger clean-data performance degrades faster, making the intended operating conditions part of the comparison.

The principal weakness is the relationship between numerical severity and clinical plausibility. A fixed blur parameter has a clear computational definition, but its clinical meaning can differ across image resolutions and modalities. Brightness and contrast operations applied to exported pixels do not reproduce every change in acquisition or reconstruction. At sufficiently severe settings, the transformation may erase the finding. A failure under that condition is different from sensitivity to a harmless nuisance.

This distinction becomes especially important when adapting the method to ultrasound. Gain, depth compensation, compression, and acoustic conditions can change different parts of the image in different ways. A global brightness transformation is therefore a useful synthetic test with limited scope. I would compare its effects with actual acquisition variation before describing it as a scanner simulation. Readers should identify which findings remain assessable at each stress level.

Pretraining comparisons require similar discipline. If two pretrained models differ in data, objective, scale, and initialization, a robustness difference belongs to the resulting training recipes. Isolating one cause requires holding the others fixed as far as practical. For a reproduction, I would preserve development splits, model-selection criteria, and evaluation transformations across the compared recipes, and repeat training enough to distinguish a consistent pattern from seed variation.

A practical report should show clean performance beside the stress curves, with class-specific and subgroup operating characteristics. It should state whether thresholds were fixed or adapted and which data informed that choice. Recalibrating separately under every stress condition answers a different question from evaluating the original pipeline. Repeated transformed images should also remain grouped by their source patient when estimating uncertainty, so the number of transformations does not inflate the apparent sample size.

The paper directly supports [Evaluation Beyond AUROC](/study/evaluation-beyond-auroc/) through the separation between discrimination and threshold-dependent behavior. It also supports [Robustness, Subgroup Performance, and External Validation](/study/robustness-subgroup-performance-and-external-validation/) by showing why robustness needs a named change, population, and endpoint. “Robust” without those conditions is too broad to evaluate.

The connection to [Distribution Shift and Out-of-Distribution Generalization](/study/distribution-shift-and-out-of-distribution-generalization/) supplies the main limitation. Passing these transformations does not establish robustness to changes in disease prevalence, label generation, referral practice, or concept–label relationships. For my own work, I would use progressive stress testing to characterize a frozen model's sensitivity to specified appearance changes, then combine it with external and evidence-reliance audits that address the shifts this transformation grid cannot represent.
