---
layout: post
title: "Learning a Clinically-Relevant Concept Bottleneck for Lesion Detection in Breast Ultrasound"
date: 2025-11-01 12:00:00 +0900
venue: "MICCAI 2024"
authors: "Arianna Bunnell, Yannik Glaser, Dustin Valdez, Thomas Wolfgruber, Aleen Altamirano, Carol Zamora González, Brenda Y. Hernandez, Peter Sadowski, John A. Shepherd (2024)"
description: "A concept bottleneck that predicts BI-RADS features before the final cancer classification — and shows that letting a radiologist correct the intermediate concepts actually improves the final diagnosis."
related_posts: false
---

**Paper.** *Learning a Clinically-Relevant Concept Bottleneck for Lesion Detection in Breast Ultrasound* (BUS-CBM) — [MICCAI 2024](https://github.com/hawaii-ai/bus-cbm)

## Why I read it

Concept bottleneck models are one of the more concrete answers to "how do you make a model's reasoning checkable by a clinician" — force it to pass through a layer of named, clinically meaningful concepts before the final prediction. I wanted to see the idea applied somewhere I could evaluate the concepts myself: breast ultrasound, where BI-RADS already gives a standard vocabulary.

## What the paper claims

BUS-CBM predicts standard BI-RADS lexicon features — shape, margin, orientation, and related descriptors — in an intermediate layer before making a final benign/malignant classification, on a dataset of over 8,000 images from 994 women. It outperforms prior state-of-the-art lesion detection by a wide margin on average precision, and — the result that matters most for trustworthiness — allowing a radiologist to intervene on the predicted BI-RADS concepts (correcting a wrong intermediate prediction) measurably improves the downstream cancer-classification AUC.

## What convinced me

The concept-intervention result is the strongest evidence I've seen that a bottleneck isn't just cosmetic interpretability bolted onto a black box. If correcting the intermediate concept actually changes the final prediction in the right direction, that means the final layer is genuinely using the concept layer's output as computational substrate, not routing around it. That's a testable, falsifiable claim about faithfulness, not just a plausible-sounding architecture diagram.

## What it leaves open

The bottleneck is only as trustworthy as the completeness of the concept vocabulary — BI-RADS features that aren't in the lexicon can't be checked or corrected, and the model may still be encoding non-BI-RADS shortcut information in the bottleneck's residual capacity if the bottleneck isn't strictly enforced. The paper doesn't fully characterize how much information leaks around the intended concept channel.

## What I take from it

Concept intervention is the right standard to ask for from any "interpretable by design" medical model: not "can you name the concepts it uses" but "if I correct one, does the final answer change accordingly." I want to apply exactly this test — intervene on a claimed clinical concept and check whether the prediction moves — to the models I audit for clinical faithfulness in my own research area.
