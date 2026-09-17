---
layout: post
title: "CANet: Cross-Disease Attention Network for Joint Diabetic Retinopathy and Diabetic Macular Edema Grading"
date: 2026-03-01 12:00:00 +0900
venue: "IEEE TMI"
authors: "Xiaomeng Li, Xiaowei Hu, Lequan Yu, Lei Zhu, Chi-Wing Fu, Pheng-Ann Heng (2020)"
description: "Joint grading of two correlated diabetic-eye diseases via cross-disease attention, a structural bet that shared retinal evidence should inform both diagnoses at once, rather than training two separate classifiers that never talk to each other."
og_image: "https://sehyeony0518.github.io/assets/img/og/2026-03-01-canet-cross-disease-attention.png"
related_posts: false
---

**Paper.** *CANet: Cross-disease Attention Network for Joint Diabetic Retinopathy and Diabetic Macular Edema Grading.*

CANet asks whether the relationship between diabetic retinopathy and diabetic macular edema can improve image-based grading when the two tasks exchange information explicitly. Separate classifiers ignore potentially useful shared evidence. A generic shared network, however, may mix information without preserving what is specific to each task. The open architectural question is how to combine shared and task-specific representations.

The clinical relationship is a motivation rather than a complete specification. Two diagnoses can be correlated without being interchangeable, and the strength of their association can vary with the population and reference definitions. A network that exchanges information between them therefore makes a substantive modeling choice: evidence associated with one label is allowed to influence the other.

CANet uses disease-specific attention to form task-oriented features and disease-dependent attention to exchange information between branches. Training uses image-level grades rather than lesion-location annotations. The authors evaluate Messidor and IDRiD, comparing with separately trained networks, shared-backbone multitask baselines, larger comparison models, and attention ablations. Messidor uses ten-fold cross-validation; IDRiD uses the challenge's provided train and test split.

The reported joint accuracy is 85.1% on Messidor and 65.1% on IDRiD. Joint accuracy requires both task labels to be correct for the same image. Messidor AUCs are reported as 96.3% for DR and 92.4% for DME. The task definitions differ across datasets, including binary DR evaluation in Messidor, so these joint-accuracy values should not be interpreted as two estimates of an identical grading problem.

The ablations are useful because they ask whether the proposed structure contributes beyond simply training two outputs together. Comparisons with larger generic multitask models also address the possibility that additional capacity explains the gain. Within the evaluated settings, the results support the architecture as a useful way to combine these labels. They do not establish that the model's exchanged features correspond to the clinical relationship that motivated the design.

The meaning of the DME target is particularly important. In these photographic datasets, edema-risk labels use hard-exudate information and its position relative to the macula. Predicting that target is not the same measurement as directly establishing retinal thickening. The EyePACS protocol review makes the same broader distinction between a photographic surrogate and the full clinical condition. A clinical interpretation of CANet's output must preserve the reference definition.

Image-level supervision also leaves a gap between task performance and lesion understanding. A network can predict the correct grades without learning an explicit representation of each lesion named in a clinical scale. Disease-specific attention means that the architecture produces a task-conditioned weighting. It does not mean that those weights have been independently validated as lesion annotations.

The same caution applies to information exchange. A benefit from cross-disease attention can arise because the branches share useful retinal evidence, because one label helps predict the other, or because both correlate with acquisition or population characteristics. Aggregate performance cannot distinguish all of these explanations. The paper's architectural hypothesis is plausible, but the mechanism requires additional evidence.

The central weakness is dependence on the observed joint label distribution. If uncommon combinations are poorly represented, a model may learn that one diagnosis is a convenient proxy for the other. This can improve average results while making the unusual combinations more difficult. A clinical evaluation should therefore inspect the matrix of DR and DME label combinations, not only the two marginal metrics and their joint average.

For example, I would compare the joint model with a single-task baseline within each adequately represented DR stratum when evaluating the DME output. The corresponding analysis would examine DR performance conditional on DME grade. These are proposed tests, not results claimed by the paper. They would help determine where information exchange assists prediction and where it may encourage an overly restrictive association.

Joint accuracy itself deserves careful interpretation. An image with one correct output and one incorrect output receives the same joint failure indicator as an image with both outputs wrong. That is a reasonable challenge metric, but it does not assign clinical consequences to particular mistakes. A deployment evaluation would need to distinguish missed referral-relevant findings, unnecessary referrals, and errors that do not change the next action.

Comparison across public datasets is valuable, yet the reported experiments should not automatically be described as frozen cross-dataset transfer. Training and evaluating within Messidor and within the IDRiD challenge test two development settings. They do not by themselves establish that one trained model transports unchanged to a new service. The original review also does not establish whether every partition excludes all patient-related overlap, a detail to check before reproducing the evaluation.

This paper directly informs [Clinical Feature Annotation and Multi-Task Learning]({{ '/study/clinical-feature-annotation-and-multi-task-learning/' | relative_url }}). Additional tasks can help or interfere, and the meaning of their labels determines what supervision is supplied. CANet supports the value of related tasks while complicating the assumption that a useful auxiliary relationship is necessarily a clinically stable one.

[Attribution, Attention, and Counterfactual Explanations]({{ '/study/attribution-attention-and-counterfactual-explanations/' | relative_url }}) explains why attention coefficients should not be treated as direct evidence of input reliance. [Distribution Shift and Out-of-Distribution Generalization]({{ '/study/distribution-shift-and-out-of-distribution-generalization/' | relative_url }}) supplies the next question: what happens when the disease combination frequencies or the relationship between photographic labels and clinical disease changes?

For my work, the transferable idea is to make relationships between tasks explicit enough to test. A multitask ultrasound model could be evaluated with and without information exchange, using matched training conditions and independent clinical-feature annotations. I would inspect discordant task combinations, calibrate outputs separately where appropriate, and test whether performance gains survive changes in acquisition and case mix.

CANet shows that structured sharing can improve the evaluated grading tasks. Its stronger clinical promise remains a hypothesis: that sharing improves predictions because it transfers appropriate evidence. Establishing that promise requires tests aimed at the exchanged information, the reference labels, and the cases where the usual disease association does not hold.
