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

Knowing that a shortcut exists is useful, but locating where it emerges may tell us whether it is an early texture cue, a later semantic feature, or something that becomes dominant only near the classifier. This paper treats shortcut learning as a layer-wise process rather than a single model-level property.

## What the paper claims

The authors combine prediction depth with distributional comparisons to identify the layers at which a shortcut becomes predictive and increasingly shapes the representation. They test shortcuts of different visual complexity across dermatology and chest-radiograph tasks, asking whether simple artifacts are learned earlier and exert a larger performance effect than complex objects.

## What convinced me

The controlled experiments show a consistent complexity pattern. A simple square shortcut caused roughly a 10–15% AUC loss when the correlation changed, whereas a more complex object shortcut produced a smaller decline of about 3–7%. The layer analyses place the simple cue earlier in the network and the complex cue deeper, supporting the idea that shortcut accessibility affects both where and how strongly it is used.

## What it leaves open

Layer localization is diagnostic, not causal proof. The experiments mainly use inserted shortcuts whose location and form are known, while real acquisition bias can be diffuse, entangled, and distributed across layers. The method also does not by itself determine which layer should be modified or whether suppressing that representation preserves valid clinical evidence.

## What I take from it

A shortcut audit can benefit from a depth dimension: availability, utilization, and emergence layer are distinct properties. I would use layer localization to guide targeted interventions, then verify the result behaviorally under shortcut removal and correlation reversal.
