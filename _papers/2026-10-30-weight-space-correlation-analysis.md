---
layout: post
title: "Weight Space Correlation Analysis: Quantifying Feature Utilization in Deep Learning Models"
date: 2026-10-30 12:00:00 +0900
venue: "MIDL 2026"
authors: "Chun Kit Wong, Paraskevas Pegios, Nina Weng, Emilie Pi Fogtmann Sejer, Martin Grønnebæk Tolsgaard, Anders Nymark Christensen, Aasa Feragen (2026)"
description: "A method for detecting shortcut reliance by looking directly at correlations in a network's weight space, rather than at its activations or explanations, a different vantage point on the same underlying question."
related_posts: false
---

**Paper.** *Weight Space Correlation Analysis: Quantifying Feature Utilization in Deep Learning Models*, MIDL 2026

## Why I read it

A model can encode scanner, site, or demographic information without using it for the clinical task. I read this paper because it tackles that availability–utilization distinction directly, which is central to any credible shortcut audit.

## What the paper claims

The method trains auxiliary heads to predict metadata from a shared representation, summarizes their weight directions with principal components, and measures alignment between those directions and the primary clinical head. High metadata predictability indicates that a signal is available; weight-space alignment is intended to indicate whether the task head is oriented toward using it.

## What convinced me

The paper first validates the measure in controlled shortcut settings, where increasing a spurious association produces the expected increase in weight-space alignment. It then analyzes a spontaneous-preterm-birth ultrasound model. Scanner and other metadata could be decoded from the representation, yet the clinical head aligned more strongly with cervical length, a clinically relevant measurement, than with scanner identity. That result shows why a metadata probe alone can generate false alarms: representation leakage and decision reliance are not the same phenomenon.

## What it leaves open

The analysis is global and depends on relatively simple prediction heads and a geometric approximation of their directions. It does not provide patient-specific attribution, and nonlinear or distributed utilization may not be captured by cosine alignment in weight space. Alignment also remains an observational proxy unless paired with an intervention.

## What I take from it

Shortcut auditing should report at least two layers of evidence: whether a nuisance signal is recoverable, and whether the diagnostic decision changes when that signal is manipulated or suppressed. Weight-space correlation is a useful middle layer between a weak presence test and a stronger causal intervention.
