---
layout: post
title: "On Calibration of Modern Neural Networks"
date: 2026-01-27 12:00:00 +0900
venue: "ICML"
authors: "Guo, Pleiss, Sun, Weinberger (2017)"
description: "Modern networks are more accurate and less calibrated than their predecessors, and the fix (temperature scaling) is almost embarrassingly simple."
related_posts: false
---

**Paper.** *On Calibration of Modern Neural Networks.*

The paper asks whether the confidence reported by a neural classifier corresponds to its observed correctness, and whether that correspondence can be improved after training. This is distinct from asking whether the classifier is accurate. Two systems can make the same class predictions while assigning very different probabilities, and those probabilities can affect decisions about referral, review, and automated acceptance.

The question remained open because architectural and training improvements were usually judged through classification performance. Better accuracy does not mathematically require better probability estimates. In a multiclass setting, the winning class can stay unchanged while its predicted probability becomes more extreme. Evaluating only the winning label therefore misses a property that matters when confidence is used operationally.

Guo and colleagues evaluate neural networks on vision and language classification tasks and examine factors including depth, width, batch normalization, and weight decay. They compare post hoc calibration approaches while keeping the trained network fixed. Temperature scaling fits a single positive scalar on held-out validation data by minimizing negative log likelihood, then divides every logit by that scalar before applying softmax.

For logits $$z_k$$, the recalibrated probabilities are

$$
p_k(T)=\frac{\exp(z_k/T)}{\sum_j\exp(z_j/T)}, \qquad T>0.
$$

On the reported CIFAR-100 ResNet-110 experiment, expected calibration error decreases from 16.53% to 1.26%. The table uses 15 bins. This is a concrete result for that model, dataset, calibration procedure, and estimator. It is not a predicted improvement for a hospital dataset.

The design makes an important point: the network need not be retrained to improve the correspondence between confidence and correctness. Because a positive temperature preserves logit ordering within an example, the winning class remains unchanged. This allows a cleaner assessment of calibration than a procedure that simultaneously changes the classification model.

However, preservation of the winning class should not be expanded into an unrestricted ranking claim. In binary classification, temperature scaling is a monotone transformation of the logit difference, so it preserves the associated score ordering. In multiclass classification, softmax normalization depends on the other logits in each example. Ordering examples by a particular class probability or maximum confidence need not be preserved. This distinction matters for selective prediction and class-specific ranking metrics.

Calibration itself also needs a target. The paper's familiar confidence formulation asks whether predictions made with a given confidence are correct at that frequency. In clinical binary prediction, one often asks whether patients assigned a disease probability have the corresponding event rate. Multiclass confidence calibration does not automatically establish calibration for each diagnostic class, subgroup, or clinically relevant threshold.

Expected calibration error is a summary of differences within probability bins. Its value depends on how those bins are defined and on how many observations populate them. A small aggregate value can conceal opposite errors in different subgroups or poor behavior in a sparsely populated high-confidence region. I would therefore use reliability plots and proper scoring rules alongside ECE, while retaining counts and uncertainty rather than treating the bin averages as exact properties.

A useful thought experiment is a predictor that assigns every patient the population's disease prevalence. It can be calibrated in that population while providing no patient-specific discrimination. This illustrates why calibration and informativeness must be evaluated separately. A well-calibrated model is not necessarily a good diagnostic model, and a useful diagnostic ranking is not necessarily ready to support probability-based decisions.

The strongest limitation is distribution dependence. The fitted temperature estimates a correction under the calibration sample's relationship between scores and outcomes. A change in patients, disease prevalence, acquisition, or reference labels can alter that relationship. The original benchmark experiments do not establish that one temperature will transfer between hospitals or remain valid over time. External calibration is another measurement, not an inherited property.

A single scalar also has limited expressive power. It changes the overall sharpness of the distribution but cannot independently repair every class-specific or subgroup-specific distortion. Its simplicity is an advantage when calibration data are limited, because there are few parameters to estimate. That advantage should be weighed against whether the observed miscalibration resembles something a global temperature can correct.

For medical use, the calibration sample must remain distinct from the final evaluation. Selecting a temperature, choosing an abstention threshold, and then reporting performance on those same cases would mix development with estimation. Patient grouping matters here just as it does during model training. Many images from a few patients do not provide the same calibration evidence as independent patients.

This paper is central to [Calibration, Uncertainty, and Selective Prediction]({{ '/study/calibration-uncertainty-and-selective-prediction/' | relative_url }}). It supports treating probability interpretation as a separate evaluation target, while the note explains why uncertainty estimation and rejection policies add further questions. A calibrated confidence score does not by itself identify missing evidence or guarantee that rejected cases receive appropriate care.

[Evaluation Beyond AUROC]({{ '/study/evaluation-beyond-auroc/' | relative_url }}) provides the decision context. Ranking, probability accuracy, operating-point performance, and workload are different outputs of an evaluation. [Distribution Shift and Out-of-Distribution Generalization]({{ '/study/distribution-shift-and-out-of-distribution-generalization/' | relative_url }}) complicates the apparent simplicity of recalibration by asking which relationships remain stable between the calibration and deployment populations.

For my own diagnostic models, temperature scaling would be a useful baseline because it isolates one repair without changing the learned representation. I would compare uncalibrated and calibrated probabilities on independent patients, examine clinically relevant classes and subgroups, and evaluate any referral or rejection policy as a complete procedure. I would also keep evidence auditing separate: a classifier that relies on acquisition shortcuts can still produce calibrated probabilities in the environment where those shortcuts work.

The lasting contribution is not that calibration has a universal one-parameter solution. It is that confidence deserves direct measurement, and that a simple, carefully evaluated correction can improve one property of a model while leaving its other strengths and weaknesses intact.
