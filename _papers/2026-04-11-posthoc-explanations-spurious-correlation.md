---
layout: post
title: "Post hoc Explanations May Be Ineffective for Detecting Unknown Spurious Correlation"
date: 2026-04-11 12:00:00 +0900
venue: "ICLR 2022"
authors: "Julius Adebayo, Michael Muelly, Hal Abelson, Been Kim (2022)"
description: "A sobering stress test of the exact interpretability toolkit I lean on elsewhere in this collection — feature attribution, concept activation, and training-point ranking — against spurious signals the practitioner doesn't already know to look for."
related_posts: false
---

**Paper.** *Post hoc Explanations May Be Ineffective for Detecting Unknown Spurious Correlation* — [ICLR 2022](https://arxiv.org/abs/2212.04629)

## Why I read it

I've built a fair amount of my own audit thinking on TCAV, Grad-CAM, and concept-based explanations elsewhere in this collection. This paper directly tests whether that class of methods can do the thing I most want from it in practice: flag a model's reliance on a spurious signal I didn't already know to test for. Reading it felt necessary rather than optional.

## What the paper claims

The authors test three families of post hoc explanation — feature attribution, concept activation, and training-point ranking — on their ability to detect a model's reliance on spurious training signals, under the realistic condition that the specific spurious artifact is *unknown at test time* to whoever is using the explanation method. Using semi-synthetic datasets with pre-specified, verifiable spurious artifacts, they build models that provably rely on those artifacts, then measure whether each explanation method actually surfaces that reliance. The finding is negative on both sides: the methods are largely ineffective at detecting reliance on unknown artifacts — especially non-visible ones like a background blur — and, separately, feature attribution methods are prone to falsely indicating spurious reliance even in models that don't actually have it.

## What convinced me

The semi-synthetic design is what makes this trustworthy rather than anecdotal: because the spurious artifact is deliberately injected and its presence in the model verified independently, the paper can state with certainty whether an explanation method caught a real, known dependency — rather than relying on a plausible-looking heatmap as its own evidence, the exact failure mode Adebayo's own earlier "Sanity Checks for Saliency Maps" paper warned about.

## What it leaves open

The paper tests detection under semi-synthetic, controlled artifacts; it doesn't fully characterize how these methods perform against the kind of subtle, naturally occurring shortcuts (acquisition site, scanner-linked noise) that dominate the medical-imaging shortcut-learning literature I've read elsewhere in this collection — those may be easier or harder to catch than the paper's constructed artifacts, and it's not obvious which.

## What I take from it

This is the most important corrective in my reading list to date, because it's aimed squarely at the tools I already treat as load-bearing. TCAV and Grad-CAM are, respectively, closely related to the concept-activation and feature-attribution families this paper tests — and finding them unreliable specifically for *unknown* spurious signals means I can no longer treat "I ran a concept-activation check and found nothing" as evidence of absence. It's only evidence against the specific shortcuts I already thought to name. Discovering an unnamed shortcut remains an open problem this entire toolkit does not solve.
