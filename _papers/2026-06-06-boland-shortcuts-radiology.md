---
layout: post
title: "There Are No Shortcuts to Anywhere Worth Going: Identifying Shortcuts in Deep Learning Models for Medical Image Analysis"
date: 2026-06-06 12:00:00 +0900
venue: "MIDL 2024"
authors: "Christopher Boland, Keith A. Goatman, Sotirios A. Tsaftaris, Sonia Dahdouh (2024)"
description: "A method for locating which layer of a network a shortcut's features actually manifest in, using Prediction Depth and KL divergence — moving from 'the model has a shortcut' to 'here is where in the network it lives.'"
related_posts: false
---

**Paper.** *There Are No Shortcuts to Anywhere Worth Going: Identifying Shortcuts in Deep Learning Models for Medical Image Analysis* — [MIDL 2024](https://proceedings.mlr.press/v250/)

## Why I read it

Most of the shortcut-learning papers I've read establish *that* a model relies on a spurious feature — a scanner marker, an acquisition site — through performance drops or counterfactual tests. This paper asks a more mechanistic question: *where inside the network* does that reliance actually show up. That's a different, more actionable kind of evidence than anything else in my reading list so far.

## What the paper claims

The authors propose a method built on Prediction Depth (a sample-difficulty metric measuring how early in a network a prediction becomes stable) combined with KL divergence, to identify the specific layers where a shortcut's learned features manifest. Testing across several shortcuts, model architectures, and datasets, they show their method can isolate these layers consistently, and find a correlation between a shortcut's visual complexity, how deep in the network its features emerge, and how much it degrades model performance. They also report a nuanced relationship between learning rate and the degree of shortcut reliance.

## What convinced me

Localizing a shortcut to specific layers is a genuinely different and more useful claim than detecting its presence at the output. If a shortcut's features consistently manifest early (shallow, low-complexity) versus late (deep, high-complexity) depending on its visual complexity, that's a testable structural regularity — not just a post hoc explanation of one specific failure case, but a pattern that could inform where in a network to intervene.

## What it leaves open

The method identifies *where* a shortcut lives in a trained network; it doesn't by itself say how to remove reliance on it once located, or whether interventions at the identified layer (e.g., targeted fine-tuning or feature suppression) actually fix the underlying generalization problem. The learning-rate relationship is also reported as "nuanced" — the paper doesn't yet give a clean, actionable rule for how learning-rate choice should be adjusted to discourage shortcut formation.

## What I take from it

Most of my reading treats shortcut detection as binary — a model either shows evidence of relying on a confound or it doesn't. This paper's layer-localization angle suggests a richer diagnostic: not just whether a shortcut is present, but how deep into the model's representation it has been absorbed, which plausibly says something about how hard it will be to dislodge. That's a dimension I want to start asking about in my own audits, not just presence or absence.
