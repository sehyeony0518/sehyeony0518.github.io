---
layout: study_note
title: "Information Theory"
description: "Entropy, mutual information, and KL divergence as ways to quantify how much a signal carries and how far two distributions have moved."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "foundations"
category_title: "Mathematical & Statistical Foundations"
order: 5
source: "Independent study"
written: true
updated: "2026-09-08"
---

Information theory quantifies uncertainty, statistical dependence, and mismatch between probability distributions. These quantities help me ask what a signal carries, while leaving the clinical value and causal role of that information to be established separately.

## Why it matters here

A representation can carry information about diagnosis and about the device that produced the image. Both are statistical dependencies, but they have different implications for a model's intended use. A large information measure therefore needs an identified variable, a defined population, and a clinical interpretation before it becomes useful evidence.

In clinical faithfulness auditing, I am interested in how much a model readout tells me about an independently assessed clinical factor. I also want to know whether that relationship persists after accounting for acquisition conditions. Information theory offers a broader language than linear correlation, but estimating its quantities reliably from medical imaging datasets is a substantial part of the problem.

## The core ideas

### Entropy describes uncertainty in a specified distribution

For a discrete variable, entropy is the expected negative logarithm of its outcome probability. It is zero for a certain outcome and largest for a uniform distribution over a fixed finite set of possibilities. The logarithm base determines the units, such as bits or nats. Predictive entropy summarizes a model's reported distribution, so a confidently wrong prediction can have low entropy. Differential entropy for continuous variables behaves differently, including dependence on measurement scale, and should not be interpreted as a direct replacement.

### Mutual information measures dependence without choosing a direction

Mutual information compares a joint distribution with the product of its marginals. For discrete variables, it also equals the reduction in one variable's entropy after observing the other. It is nonnegative and zero exactly when the variables are independent. Unlike Pearson correlation, it can detect dependence that is not linear. It remains symmetric, however: information shared between a readout and a clinical factor does not identify which causes which, or whether the classifier relies on that factor.

### Conditional information asks what remains after other variables are known

Conditional mutual information measures dependence between two variables within the conditioning information, averaged over that information's distribution. For example, I could ask whether an evidence score remains informative about a lesion descriptor given device identity. Conditioning does not automatically remove confounding or establish causality. It can expose or create associations, depending on how the variables arise. I would define the conditioning set from the audit question, rather than treating every available metadata field as a desirable adjustment.

### KL divergence describes an asymmetric distribution mismatch

KL divergence from P to Q averages the log ratio of their probabilities or densities under P. It is nonnegative but generally asymmetric and is not a metric. It can be infinite when Q assigns zero probability where P assigns positive probability. In classification, expected cross-entropy equals the entropy of the target distribution plus its KL divergence from the predicted distribution. This explains the loss's probabilistic target, while leaving open whether the training distribution represents the clinical setting.

### Estimation and processing limit what the numbers establish

Exact information quantities and their estimates are different objects. [McAllester and Stratos](https://proceedings.mlr.press/v108/mcallester20a.html) establish limitations on distribution-free, high-confidence lower bounds for mutual information from finite samples. A small estimated bound therefore need not imply little dependence. The data processing inequality adds a separate constraint: processing an observation through a fixed mapping cannot increase its true mutual information with a target when no additional target information enters. A learned representation can nevertheless make existing information easier for a restricted probe to recover.

## Where it touches my work

For gallbladder ultrasound shortcut auditing, I would compare dependencies involving diagnosis, clinical descriptors, device metadata, and model readouts, while checking sensitivity to the estimator and sampling scheme. A KL-based comparison across hospitals would require specifying which distribution is being compared, such as score distributions rather than the full image distribution. Even a clear shift would not identify its clinical cause. I would connect the result to subgroup behavior and evidence interventions before interpreting it as a failure of clinical faithfulness.

## What I have not resolved

- Which dependence estimates remain credible when representations have many dimensions and clinically labeled patients are limited?
- How can I separate additional clinical information from information shared with a device or referral pathway?
- What distributional changes would justify an audit response when a small aggregate shift could conceal a consequential change in a rare subgroup?
