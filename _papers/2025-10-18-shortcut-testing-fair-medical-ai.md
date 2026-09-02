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

A sensitive attribute can be encoded by a medical model for many reasons, including legitimate disease associations. I read ShorT because it does not equate attribute predictability with harmful use; it intervenes on how strongly the representation encodes the attribute and tests whether fairness changes.

## What the paper claims

Shortcut Testing uses multitask learning to generate a family of clinical models with different levels of sensitive-attribute encoding. It then measures the association between encoding strength and a prespecified fairness metric. A systematic relationship indicates that the attribute is driving unfair performance; no relationship suggests that another mechanism should be investigated.

## What convinced me

The controlled age–effusion experiment behaves as expected. In the original data, encoding and unfairness had a modest association (Spearman ρ = −0.224); after strengthening the age–label correlation it became much larger (ρ = −0.668), while a balanced dataset showed no significant relationship. For cardiomegaly, race encoding was associated with unfairness (ρ = 0.469, p < 0.001). In contrast, an acne model was unfair and encoded age, but ShorT did not identify age shortcutting, preventing an overly simple diagnosis.

## What it leaves open

The conclusion depends on the fairness criterion, the intervention range, and the assumption that multitask training changes attribute encoding without introducing other systematic differences. A null association can reflect low power or an incomplete intervention. ShorT identifies a mechanism of unfairness; it does not define which fairness objective is clinically appropriate.

## What I take from it

Fairness auditing needs mechanism tests, not only subgroup gaps and representation probes. ShorT provides a useful pattern: deliberately vary a suspected dependency and observe whether harm tracks it. The same logic can be applied to scanner, frequency band, or clinical-concept reliance.
