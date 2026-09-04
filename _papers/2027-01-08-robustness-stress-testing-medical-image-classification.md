---
layout: post
title: "Robustness Stress Testing in Medical Image Classification"
date: 2027-01-08 12:00:00 +0900
venue: "arXiv preprint"
authors: "Mobarakol Islam, Zeju Li, Ben Glocker (2023)"
description: "Progressive stress testing with five perturbation types at six severity levels, applied to chest X-ray and skin-lesion classifiers, separates iid test accuracy from robustness and finds that pretraining choice, not just architecture, shapes how a model degrades."
related_posts: false
---

**Paper.** *Robustness Stress Testing in Medical Image Classification* — [arXiv (2023)](https://arxiv.org/abs/2308.06889)

## Why I read it

I had just read a dermatology-specific stress-testing paper limited to a handful of realistic perturbations. This one generalizes the idea into a structured, graded methodology and applies it across two modalities, which let me see whether the underlying finding, that iid accuracy hides real fragility, replicates outside dermatology.

## What the paper claims

The authors argue that when test data is drawn from the same distribution as training data, iid test-set performance can be an unreliable estimate of accuracy on new data, and propose progressive stress testing as a systematic alternative: five bidirectional and unidirectional image perturbations, each applied at six increasing severity levels, evaluated with a threshold-agnostic AUC metric so that degradation can be tracked continuously rather than at one operating point. They apply this to chest X-ray disease detection using CheXpert for development and MIMIC-CXR for external validation, and to skin-lesion detection using the multi-site ISIC dataset, which lets them examine both within-domain severity effects and cross-site domain shift together.

## What convinced me

Two findings stood out precisely because they run against a natural assumption. First, some models held roughly stable AUC across demographic subgroups while their true positive and false positive rates diverged, meaning a single aggregate AUC figure was hiding a real shift in operating characteristics between groups, a subtler failure than an aggregate performance drop. Second, transformer-based architectures showed evidence of greater robustness under progressive stress than the compared convolutional models, and pretraining characteristics carried through to affect downstream robustness, which argues that robustness is not solely a property of the final fine-tuned architecture but is partly inherited from how the model was pretrained.

## What it leaves open

Progressive stress testing evaluates robustness to a defined set of image perturbations chosen by the authors; it does not claim to cover every way a deployed model's inputs could differ from training data, and a model robust to these five perturbation families is not thereby shown to be robust to acquisition-linked shortcuts of the kind other papers in this collection document. The AUC-stable-but-TPR/FPR-diverging finding also needs a follow-up account of mechanism: the paper documents that this divergence happens, not why a given model's operating point drifts differently by subgroup under stress.

## What I take from it

An aggregate metric that stays flat under stress is not the same claim as a model that is actually stable, since operating-point behavior can diverge underneath a flat top-line number. I would now want subgroup-stratified operating characteristics, not just an aggregate metric, reported at each stress severity level, and I would treat pretraining data and procedure as a robustness variable worth reporting explicitly rather than an incidental detail of the methods section.
