---
layout: post
title: "The Model Could Read the Hospital: Variable Generalization in Pneumonia Detection"
date: 2025-10-11 12:00:00 +0900
venue: "PLOS Medicine"
authors: "Zech, Badgeley, Liu, Costa, Titano, Oermann (2018)"
description: "CNNs detected the treating institution from chest radiographs and used it as a proxy for disease prevalence — an early, concrete demonstration of confounding by site."
related_posts: false
---

**Paper.** *Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs* — [PLOS Medicine 2018](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002683)

## Why I read it

This is the study people cite when they say "the model learned the hospital." I wanted to see how directly that was shown, because my own work depends on the claim being real rather than folkloric.

## What they showed

Models trained on chest radiographs from multiple health systems performed worse when transferred externally — the familiar result. The striking part is the mechanism: the authors demonstrated that a CNN could **identify the source institution and even the specific department** from the radiograph itself, with high accuracy. Since pneumonia prevalence differed by site, site identity was a usable predictor of the label.

The model did not need to understand consolidation. It could infer where the image came from and apply that site's base rate.

## Why it convinced me

The evidence is constructive rather than inferential. Rather than arguing "performance dropped, therefore confounding," they trained a model to predict the confounder and showed it was recoverable from the pixels. That is the shape of argument I want in my own auditing work: don't infer the shortcut from a performance gap — demonstrate that the signal is present and usable.

## What it leaves open

Knowing that site is recoverable does not tell us how much of any given prediction rests on it. The paper establishes availability, not attribution. Quantifying the share of a decision attributable to a confounder — per model, per case — is still open, and is the part I find hardest.

## What I take from it

Multi-site training data does not automatically produce site-invariant models. If anything, pooling sites with different prevalences *creates* the shortcut. Data diversity helps only when the diversity is decorrelated from the label.
