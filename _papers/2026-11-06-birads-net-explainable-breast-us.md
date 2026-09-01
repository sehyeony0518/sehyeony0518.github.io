---
layout: post
title: "BI-RADS-Net: An Explainable Multitask Learning Approach for Cancer Diagnosis in Breast Ultrasound"
date: 2026-11-06 12:00:00 +0900
venue: "IEEE ISBI 2021"
authors: "Boyu Zhang, Aleksandar Vakanski, Min Xian (2021)"
description: "A multitask model that predicts BI-RADS descriptors alongside malignancy — one of the earlier attempts at the same explainable-by-BI-RADS idea that later concept-bottleneck papers pushed further."
related_posts: false
---

**Paper.** *BI-RADS-Net: An Explainable Multitask Learning Approach for Cancer Diagnosis in Breast Ultrasound Images* — IEEE ISBI (2021)

## Why I read it

Having already read the BUS-CBM concept-bottleneck paper, I wanted to see an earlier point in the same line of work — a multitask, rather than strict-bottleneck, approach to tying a breast-ultrasound classifier's output to BI-RADS descriptors — to understand what the bottleneck architecture specifically improved on relative to this precedent.

## What the paper claims

The authors argue that establishing clinician trust requires explaining a model's decision-making process, and that typical CAD systems for breast-cancer diagnosis fall short by only outputting a benign/malignant category or a tumor localization, without connecting that output to the diagnostic reasoning a radiologist would use. BI-RADS-Net addresses this with a multitask architecture that jointly predicts BI-RADS descriptors (such as shape and margin) and the final malignancy classification, sharing representations between the two tasks rather than strictly gating the final prediction through the BI-RADS outputs.

## What convinced me

Naming the specific shortfall of prior CAD systems — a category or a bounding box, with no connection to diagnostic reasoning — is a clear and accurate framing of the trust gap, and treating BI-RADS descriptor prediction as a first-class task alongside classification (not just a post hoc visualization) is a reasonable multitask formulation.

## What it leaves open

Multitask learning, unlike a strict concept bottleneck, doesn't force the final classification to depend *only* on the predicted BI-RADS concepts — the malignancy head can still draw on shared representations directly, bypassing the descriptor predictions. That means the BI-RADS outputs here are best read as auxiliary, correlated evidence of what the model may be attending to, not a guarantee (the way BUS-CBM's bottleneck and its concept-intervention test aim to guarantee) that the final decision actually routes through them.

## What I take from it

Reading this alongside BUS-CBM clarified the real architectural distinction between "multitask, explanation as an auxiliary output" and "bottleneck, explanation as the only channel to the final decision" — and why the latter supports a much stronger faithfulness test (concept intervention) than the former does. When a paper describes itself as "explainable via BI-RADS," I now check which of these two architectures it actually is before assuming the explanation is causally load-bearing.
