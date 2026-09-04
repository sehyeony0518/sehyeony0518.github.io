---
layout: post
title: "Stress Testing Reveals Gaps in Clinic Readiness of Image-Based Diagnostic Artificial Intelligence Models"
date: 2026-12-25 12:00:00 +0900
venue: "npj Digital Medicine"
authors: "Albert T. Young, Kristen Fernandez, Jacob Pfau, Rasika Reddy, Nhat Anh Cao, Max Y. von Franque, Arjun Johal, Benjamin V. Wu, Rachel R. Wu, Jennifer Y. Chen, Raj P. Fadadu, Juan A. Vasquez, Andrew Tam, Michael J. Keiser, Maria L. Wei (2021)"
description: "A skin-lesion classifier at dermatologist-level AUC gave false positive or negative predictions for up to 22% of lesions under a simple image rotation — a direct test of whether an acceptable benchmark score means the model is ready for a clinic."
related_posts: false
---

**Paper.** *Stress testing reveals gaps in clinic readiness of image-based diagnostic artificial intelligence models* — [npj Digital Medicine (2021)](https://doi.org/10.1038/s41746-020-00380-6)

## Why I read it

An acceptable AUROC on a held-out test set is the most common evidence offered for clinical readiness in the papers I read, and this paper directly interrogates the gap between that number and readiness for real, non-curated clinical use.

## What the paper claims

The authors evaluate dermatologist-level convolutional neural networks for melanoma classification not on a fresh dataset, but on the same images subjected to simple, clinically realistic perturbations, including rotation and other transformations meant to approximate real-world image variation rather than adversarial attack. They call this a computational stress test, distinct from ordinary external validation. Repeated predictions on images captured under only slightly different conditions, or transformed in simple ways, were often inconsistent with each other, producing false positive or false negative predictions for 6.5 to 22% of skin lesions across the test datasets examined.

## What convinced me

The perturbations used here are not adversarial in the usual sense, crafted to fool a model. They are the kind of incidental variation, rotation and repeated capture, that occurs routinely in an actual clinic. A model whose prediction flips under that kind of ordinary variation is failing a bar well below what an adversarial robustness paper would test, which makes the 6.5 to 22% instability rate a more immediately clinically relevant finding than an adversarial perturbation result would be.

## What it leaves open

Stress testing under simple transformations checks stability against one class of nuisance variation. It does not by itself diagnose why a prediction flips, whether the model is relying on a texture or artifact sensitive to rotation, or whether the instability concentrates in particular lesion types or skin tones. Calibration, the paper's other central concern, is treated as a related but distinct property, and improving stability under stress tests does not automatically improve calibration.

## What I take from it

An accuracy or AUROC figure reported on a single, fixed test set is a claim about one specific realization of the data, not a claim about stability under the ordinary variation a clinic will actually produce. I would now want stress testing under simple, clinically plausible transformations, repeated capture, rotation, minor cropping, reported as a standard companion to any single-number performance claim, not as an optional robustness appendix.
