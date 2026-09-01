---
layout: post
title: "Detecting Shortcut Learning for Fair Medical AI Using Shortcut Testing"
date: 2025-10-18 12:00:00 +0900
venue: "arXiv preprint"
authors: "Alexander Brown, Nenad Tomasev, Jan Freyberg, Yuan Liu, Alan Karthikesalingam, Jessica Schrouff (2023)"
description: "A method (ShorT) for directly testing whether a clinical model is using shortcut correlations — with the uncomfortable finding that shortcuts are not always the reason a model is unfair."
related_posts: false
---

**Paper.** *Detecting Shortcut Learning for Fair Medical AI Using Shortcut Testing* — Google Research / DeepMind (2023)

## Why I read it

Fairness and shortcut learning are often discussed as if they're the same problem wearing two names — a model performs worse on some subgroup, therefore it must be relying on a shortcut correlated with that subgroup. This paper is one of the few I've found that treats that assumption as a hypothesis to test rather than a conclusion to assume.

## What the paper claims

Using multi-task learning, the authors propose a way to directly test for the *presence* of shortcut learning in a clinical model — whether the model is basing its prediction on an improper correlation, such as a sensitive attribute, rather than genuine disease evidence — and apply it to real radiology and dermatology tasks. Diagnosing this is hard precisely because sensitive attributes (age, sex, skin tone) can be causally linked to disease prevalence, so a model attending to them isn't automatically shortcutting.

## What convinced me

The paper's most useful move is negative: it shows cases where subgroup performance gaps exist but shortcutting, as directly tested, is *not* responsible. That result argues against a reflexive equivalence between "unfair" and "shortcutting," and toward treating fairness mitigation as needing its own diagnosis rather than inheriting whatever fix worked for a different, superficially similar problem.

## What it leaves open

If shortcut learning isn't the cause of an observed disparity, the paper doesn't hand you the actual cause — data imbalance, label noise correlated with subgroup, or genuine differences in how disease presents could each be at play, and distinguishing them needs separate tools. The method also still requires the sensitive attribute or shortcut candidate to be named in advance to test for it.

## What I take from it

This is a useful discipline to import directly: when I find a model relying on a spurious correlate, I should not assume that's automatically the explanation for any fairness gap I've also observed in the same model. The two questions — "is this model shortcutting" and "is this model unfair to this subgroup" — need independent evidence, even though they're often caused by the same underlying data problems.
