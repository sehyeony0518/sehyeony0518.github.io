---
layout: post
title: "Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV)"
date: 2025-09-19 12:00:00 +0900
venue: "ICML 2018"
authors: "Been Kim, Martin Wattenberg, Justin Gilmer, Carrie Cai, James Wexler, Fernanda Viégas, Rory Sayres (2018)"
description: "TCAV asks whether a model's prediction is sensitive to a human-named concept, such as 'striped' or 'malignant,' rather than to a single pixel, the tool that later work on shortcut detection in medical imaging builds directly on."
related_posts: false
---

**Paper.** *Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV)*. [ICML 2018](https://arxiv.org/abs/1711.11279)

## Why I read it

Pixel attributions are often too low-level for clinical reasoning. TCAV is foundational because it lets a researcher ask a model a hypothesis in human terms (for example, whether a class is sensitive to "microaneurysms" or "irregular margin") using sets of concept examples.

## What the paper claims

A linear classifier separates concept examples from random examples in a chosen activation space, and its normal vector defines a Concept Activation Vector. The directional derivative of the target logit along that vector measures local concept sensitivity. The TCAV score is the proportion of class examples with positive sensitivity, repeated across random sets for statistical testing.

## What convinced me

The framework is model- and domain-flexible and makes the hypothesis explicit. The original paper applies it across ImageNet and a diabetic-retinopathy model, showing that concept tests can reveal class-level sensitivities not visible from single-image saliency. Repeating the test with multiple random counterexample sets is also an important guard against reading too much into one fitted direction.

## What it leaves open

A CAV is a linear separator whose meaning depends on the examples, layer, and random controls. Correlated concepts may be inseparable, and a high TCAV score means directional sensitivity, not that the concept is necessary or sufficient. The method can test a named concept but cannot guarantee that the concept set is complete or clinically valid.

## What I take from it

TCAV is best used as a quantitative hypothesis test, followed by intervention. I would validate concept separability out of sample, report stability across layers and random sets, control for correlated concepts, and test whether changing the concept alters the diagnosis as predicted.
