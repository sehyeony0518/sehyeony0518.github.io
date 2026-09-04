---
layout: post
title: "Learning a Clinically-Relevant Concept Bottleneck for Lesion Detection in Breast Ultrasound"
date: 2025-11-01 12:00:00 +0900
venue: "MICCAI 2024"
authors: "Arianna Bunnell, Yannik Glaser, Dustin Valdez, Thomas Wolfgruber, Aleen Altamirano, Carol Zamora González, Brenda Y. Hernandez, Peter Sadowski, John A. Shepherd (2024)"
description: "A concept bottleneck that predicts BI-RADS features before the final cancer classification, and shows that letting a radiologist correct the intermediate concepts actually improves the final diagnosis."
featured: true
related_posts: false
---

**Paper.** *Learning a Clinically-Relevant Concept Bottleneck for Lesion Detection in Breast Ultrasound* (BUS-CBM). [MICCAI 2024](https://github.com/hawaii-ai/bus-cbm)

## Why I read it

BUS-CBM is one of the closest precedents to my interest in auditable-by-design ultrasound models. It unifies lesion detection, BI-RADS concept prediction, cancer classification, and clinician correction within one pipeline, so its intervention evidence matters more than a visually plausible explanation.

## What the paper claims

The model detects and segments a lesion, predicts BI-RADS mass descriptors, and then classifies cancer from the concept representation, with variants that trade stricter bottlenecking for additional visual information. It is trained on 8,854 images from 994 women with expert concepts and histologic cancer labels.

## What convinced me

The lesion model reached average precision 0.489, exceeding the compared detection baselines. More importantly, concept intervention improved cancer AUROC from 0.876 to 0.885. The gain is modest, but it is direct evidence that correcting the explanatory interface can improve the final decision. Concept performance was also heterogeneous: echo pattern, shape, margin, and orientation were predicted well, whereas posterior features were harder and had only fair reader agreement.

## What it leaves open

The effect of intervention was mixed across concepts, and the vocabulary may not capture every malignancy cue. Models with an auxiliary visual side channel can perform better but weaken the claim that the decision is fully explained by BI-RADS. The dataset is internal, and concept labels inherit inter-reader subjectivity, posterior features had Cohen's κ around 0.31.

## What I take from it

The paper shows both the promise and cost of concept bottlenecks. I would report the performance–auditability frontier explicitly, test leakage around the bottleneck, and evaluate interventions by concept and subgroup. A concept layer is valuable when correcting it reliably controls the diagnosis, not merely when its labels are readable.
