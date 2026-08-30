---
layout: post
title: "Shortcut Learning in Radiology AI: A Practitioner's Field Guide"
date: 2026-06-06 12:00:00 +0900
venue: "Radiology"
authors: "Boland et al. (2024)"
description: "A synthesis, aimed at radiologists rather than ML researchers, of how shortcut learning actually shows up in clinical imaging AI — and what to check for before trusting a model."
related_posts: false
---

**Paper.** *Shortcut Learning in Medical AI* — Boland et al., Radiology (2024)

## Why I read it

Most of the shortcut-learning literature I have read is written by and for machine-learning researchers. This paper is useful precisely because it translates the same concerns into the language and workflow of a practicing radiologist deciding whether to trust a vendor's AI product.

## What it adds

Rather than one dramatic case study, the paper works as a taxonomy: acquisition-linked shortcuts (scanner make, protocol, site markers), population-linked shortcuts (age, sex, comorbidity patterns that correlate with the label in a particular dataset but not causally), and workflow-linked shortcuts (the presence of a prior report, a treatment device, or an ordering pattern that leaks information about the outcome). Each category comes with the kind of question a radiologist evaluating a deployed tool could actually ask: was training data pooled across sites with different disease prevalence? Were cases and controls collected under different protocols? Does the tool's performance hold on images from equipment the developer didn't train on?

The framing I found most useful is the shift from "is this model accurate" to "what would have to be true about my patient population for this model's shortcuts, if any, to still produce correct answers." That's a question a clinical user can actually evaluate without needing to audit the model's internals.

## What it leaves open

As a synthesis rather than a new empirical study, it does not resolve the harder technical question — how to detect a shortcut without external data or ground-truth annotation of the confounding variable. It is deliberately positioned as the translation layer between the technical literature (Geirhos, Zech, DeGrave) and clinical deployment decisions.

## What I take from it

This is the register I want my own writing to be able to shift into: the same auditing concerns, but phrased as questions a clinician can ask a vendor, not just a proof a machine-learning researcher can construct. If clinical faithfulness auditing is going to matter outside a lab, it needs exactly this kind of translation.
