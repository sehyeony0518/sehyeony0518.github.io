---
layout: post
title: "Auditing the Inference Processes of Medical-Image Classifiers by Leveraging Generative AI and the Expertise of Physicians"
date: 2026-12-04 12:00:00 +0900
venue: "Nature Biomedical Engineering"
authors: "Alex J. DeGrave, Zhuo Ran Cai, Joseph D. Janizek, Roxana Daneshjou, Su-In Lee (2025)"
description: "Generative counterfactuals read by two blinded dermatologists across five academic and consumer skin-lesion classifiers — the closest published template I have found for the audit I want to run on ultrasound models."
related_posts: false
---

**Paper.** *Auditing the inference processes of medical-image classifiers by leveraging generative AI and the expertise of physicians* — [Nature Biomedical Engineering (2025)](https://doi.org/10.1038/s41551-023-01160-9)

## Why I read it

This is the paper my own question keeps converging on: not whether a classifier is accurate, but what evidence it uses, stated in terms a clinician can actually judge. It comes from the group behind the COVID shortcut study I reviewed earlier, and it generalizes that one-off finding into a reusable auditing framework.

## What the paper claims

The authors pair generative counterfactuals with blinded expert annotation to characterize five melanoma classifiers spanning academic and consumer software: DeepDerm, ModelDerm 2018, Scanoma, SSCD, and a SIIM-ISIC competition-style model. An improved Explanation by Progressive Exaggeration produces a "benign" and a "malignant" counterfactual from each reference image, with a key modification over the original method — the generator is trained to alter an attribute only when that change actually moves the classifier's output, so a difference observed in a pair can be attributed to the classifier rather than to generative drift. Two board-certified dermatologists then annotated thousands of randomized, quality-screened pairs.

## What convinced me

The validation experiment is what elevates this above a gallery of plausible edits. Counterfactuals suggested that background "pinkness" — effectively lighting and colour balance — sways predictions, so the authors programmatically shifted chromaticity in CIELUV space across all 20,260 ISIC images and recovered the same direction per classifier, including opposite signs: pinker images read as more benign to DeepDerm and more malignant to Scanoma. That converts an expert impression into a measured, classifier-specific dependency. The attribute profile is also genuinely mixed rather than uniformly damning: darker lesional pigmentation was the top attribute for every classifier, consistent with dermatologist practice, alongside undesirable reliance on background texture, hair, and colour balance.

## What it leaves open

The framework describes AI reasoning in human-nameable terms, which the authors note may miss attributes with no convenient clinical vocabulary. Generative inductive biases can suppress certain edits — large geometric changes such as lesion size — and the method says nothing about interactions between attributes. Annotator variability also means the reported frequencies support direction and presence, not fine-grained comparisons of effect size.

## What I take from it

This is the design I would want to imitate for ultrasound: counterfactual generation constrained so that observed differences are attributable to the classifier, blinded reading by clinicians who name attributes in their own vocabulary, and then a programmatic intervention that tests one named attribute directly. The last step matters most. An expert-annotated counterfactual is a hypothesis about evidence use; the colour-shift experiment is what turns it into a measurement.
