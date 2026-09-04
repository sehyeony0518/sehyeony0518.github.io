---
layout: post
title: "Transparent Medical Image AI via an Image-Text Foundation Model Grounded in Medical Literature"
date: 2026-08-30 12:00:00 +0900
venue: "Nature Medicine"
authors: "Chanwoo Kim, Soham U. Gadgil, Alex J. DeGrave, Jesutofunmi A. Omiye, Zhuo Ran Cai, Roxana Daneshjou, Su-In Lee (2024)"
description: "MONET learns a dense, concept-scoring image-text space from 105,550 dermatology images paired with literature descriptions, then uses that space for data auditing, model auditing, and interpretation — including recovering a spurious redness-malignancy correlation that flipped sign between two hospitals."
related_posts: false
---

**Paper.** *Transparent medical image AI via an image-text foundation model grounded in medical literature* — [Nature Medicine (2024)](https://doi.org/10.1038/s41591-024-02887-x)

## Why I read it

This is the third paper I have read from Su-In Lee's group, after the COVID shortcut study and the counterfactual dermatology audit, and it is the most ambitious: rather than auditing one classifier at a time, it trains a general-purpose concept-scoring model meant to support auditing across the entire AI development pipeline.

## What the paper claims

MONET (medical concept retriever) is trained on 105,550 dermatological images paired with natural-language descriptions drawn from a large collection of medical literature, learning a joint image-text representation that can densely score any image for the presence of a named clinical concept without requiring a dataset hand-annotated for that concept. The authors position this as infrastructure for three tasks: auditing training data for spurious correlations before a model is ever trained, auditing a trained model's reliance on a suspected concept, and building inherently interpretable models whose predictions route through MONET-scored concepts. Concept-annotation accuracy was verified against board-certified dermatologists and found competitive with supervised models trained on datasets specifically annotated for those concepts.

## What convinced me

The clearest demonstration is a site-comparison finding rather than an aggregate score: at Hospital Barcelona, redness was positively correlated with malignancy in the training data, while at Medical University of Vienna the same feature correlated negatively, a sign flip in what a spurious correlation even means depending on which site's data trained the model. MONET's use as an auditing tool identified this site-dependent, spuriously correlated concept, and the authors then constructed a reversed-correlation test set to check whether a model trained on one site's spurious association would fail when that association no longer held. Recovering a real, previously known-to-differ site effect, rather than a synthetic inserted confound, is stronger evidence than a controlled benchmark alone would be.

## What it leaves open

MONET's concept vocabulary is grounded in whatever concepts appear in the medical-literature descriptions it trained on, so a clinically important concept that is rarely described in text, or described inconsistently across sources, may be scored less reliably than one with abundant literature coverage. The reported concept-accuracy comparison against board-certified dermatologists is itself a form of expert-agreement validation, which is necessary but, as I have found reading saliency-validation papers elsewhere in this collection, not sufficient on its own to establish that a concept score is causally load-bearing in a downstream model's decision rather than merely correlated with it.

## What I take from it

Using a concept-scoring foundation model to audit training data before a model is trained, not only to audit a model after training, is a genuinely different point of intervention from most of the shortcut-detection literature I have read, which mostly diagnoses problems after the fact. The Barcelona-Vienna redness reversal is also a concrete, real-world instance of a pattern I want to keep watching for in my own work: a feature's correlation with the label is not a fixed property of the feature, it is a property of the site, and a model trained at one site can encode a relationship that is simply false at another.
