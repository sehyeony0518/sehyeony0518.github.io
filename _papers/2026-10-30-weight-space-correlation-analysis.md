---
layout: post
title: "Weight Space Correlation Analysis: Quantifying Feature Utilization in Deep Learning Models"
date: 2026-10-30 12:00:00 +0900
venue: "MIDL 2026"
authors: "Chun Kit Wong, Paraskevas Pegios, Nina Weng, Emilie Pi Fogtmann Sejer, Martin Grønnebæk Tolsgaard, Anders Nymark Christensen, Aasa Feragen (2026)"
description: "A method for detecting shortcut reliance by looking directly at correlations in a network's weight space, rather than at its activations or explanations — a different vantage point on the same underlying question."
related_posts: false
---

**Paper.** *Weight Space Correlation Analysis: Quantifying Feature Utilization in Deep Learning Models* — MIDL 2026

## Why I read it

Nearly every shortcut-detection method I've read operates on activations, gradients, or generated counterfactual images — inputs and intermediate representations. This paper instead looks at the trained weights themselves, which is a different enough vantage point on the same underlying question that I wanted to see what it reveals that the more common approaches don't.

## What the paper claims

Deep learning models in medical imaging are susceptible to shortcut learning, often relying on confounding metadata — the paper's example is scanner model — that ends up encoded in image embeddings. The central question the authors pose is whether a model *actively uses* that encoded confounding information in producing its final prediction, and they propose analyzing correlation structure directly in the model's weight space to quantify how much a given feature (including scanner-linked ones) is actually utilized, as distinct from merely being present in the model's internal representation.

## What convinced me

Separating "the confound is encoded somewhere in the representation" from "the confound is actively used in the final decision" is an important and frequently glossed-over distinction — a model's embeddings can contain scanner information incidentally, correlated with other content, without that information being what drives the output. A weight-space method aimed specifically at utilization, rather than mere presence, is targeting the more clinically relevant half of that distinction.

## What it leaves open

Weight-space correlation is a structural property of the trained network; connecting it back to a concrete, checkable clinical claim (this specific prediction, on this specific image, used the scanner-linked signal) likely requires pairing it with an instance-level method like TCAV or a counterfactual test, rather than standing alone as a full explanation.

## What I take from it

This paper reinforces a distinction I now try to keep explicit in my own audits: encoding versus utilization. A model's activations containing recoverable information about acquisition site or scanner doesn't by itself mean the model is relying on that information for its actual clinical predictions — and a weight-space method that targets utilization specifically is a useful complement to the more common activation-based and counterfactual-based shortcut-detection tools I've read elsewhere in this collection.
