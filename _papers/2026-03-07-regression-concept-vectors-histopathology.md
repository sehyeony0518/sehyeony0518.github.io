---
layout: post
title: "Regression Concept Vectors for Bidirectional Explanations in Histopathology"
date: 2026-03-07 12:00:00 +0900
venue: "MICCAI 2018 Workshop"
authors: "Mara Graziani, Vincent Andrearczyk, Henning Müller (2018)"
description: "An extension of TCAV to continuous, graded concepts — used to show that nuclei texture, not just its presence, is a directional driver of tumor-grade predictions in lymph-node histopathology."
related_posts: false
---

**Paper.** *Regression Concept Vectors for Bidirectional Explanations in Histopathology* — [MICCAI 2018 Interpretability Workshop](https://arxiv.org/abs/1904.04520)

## Why I read it

TCAV's concept vectors work with binary concepts — a feature is present or absent. Most clinically meaningful concepts (tumor grade, degree of pleomorphism, texture severity) are graded rather than binary, so I wanted to see how the idea extends to a continuous setting, and whether that extension holds up on real histopathology.

## What the paper claims

The authors introduce Regression Concept Vectors (RCVs), which extend TCAV-style concept vectors to continuous-valued concepts by regressing a concept's numeric value from a layer's activations rather than classifying its presence. The directional derivative along the RCV then measures the model's sensitivity to a *change in degree* of the concept, not just its presence. Applied to breast-cancer grading in lymph-node histopathology, nuclei texture emerges as a relevant, directionally consistent concept the model's tumor-detection decisions are sensitive to, backed by a statistical robustness and consistency evaluation across the dataset.

## What convinced me

Moving from "is this concept present" to "how does sensitivity change as the concept's degree changes" is a meaningfully richer question for grading tasks, where the clinically relevant fact is often severity, not presence. Backing the nuclei-texture finding with a statistical consistency check — rather than a single qualitative example — gives the result more weight than a typical interpretability case study.

## What it leaves open

As with TCAV, RCVs require someone to have measured or annotated the continuous concept in the first place (here, a texture metric), so the method only tells you about sensitivity to concepts you already thought to quantify. The workshop-scale evaluation is also on a specific breast-cancer grading task; whether nuclei-texture sensitivity generalizes as a pattern across other histopathology grading problems isn't established here.

## What I take from it

Grading tasks — knee-OA severity, DR severity, BI-RADS category — are exactly the setting where a binary concept test understates what's actually needed: the question is rarely "does the model see this feature" but "does more of this feature move the prediction the right amount, in the right direction." RCVs are the right shape of tool for that question, and I want to bring this framing to my own audits of severity-grading models rather than defaulting to presence/absence concept tests.
