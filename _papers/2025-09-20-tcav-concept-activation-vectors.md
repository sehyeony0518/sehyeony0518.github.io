---
layout: post
title: "Interpretability Beyond Feature Attribution: TCAV"
date: 2025-09-20 12:00:00 +0900
venue: "ICML 2018"
authors: "Been Kim, Martin Wattenberg, Justin Gilmer, Carrie Cai, James Wexler, Fernanda Viégas, Rory Sayres (2018)"
description: "TCAV asks whether a model's prediction is sensitive to a human-named concept, such as 'striped' or 'malignant,' rather than to a single pixel — the tool that later work on shortcut detection in medical imaging builds directly on."
related_posts: false
---

**Paper.** *Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV)* — [ICML 2018](https://arxiv.org/abs/1711.11279)

## Why I read it

A large share of the medical-AI interpretability literature I read — including the concept-bottleneck and concept-vector papers I've reviewed elsewhere on this page — traces back to TCAV. I wanted to go to the source rather than keep encountering it secondhand as "the concept-activation-vector method."

## What the paper claims

Saliency maps show *where* in an image a model is looking, in pixel space. TCAV instead asks whether a model's prediction is sensitive to a human-interpretable *concept* — "striped," "young," "malignant nuclei" — regardless of where or how that concept appears spatially. It works by collecting example images that do and don't exhibit the concept, training a linear classifier in the model's activation space to separate them, and using the resulting vector's direction to compute a directional derivative: how much would the model's output change if this input moved slightly toward "more striped"? Aggregated across many examples, this gives a concept-level sensitivity score without ever retraining the model or requiring concept labels during training.

## What convinced me

The elegance of the method is that it separates *what concept the model uses* from *how faithfully it uses it*, and it does so post hoc, on any layer of any trained network, using only a handful of example images per concept. The zebra-stripes-versus-random-image validation and the "does a model trained to detect diabetic retinopathy respond to microaneurysms" case study both show the method finding sensible, checkable answers rather than a black box producing an uncheckable score.

## What it leaves open

TCAV tells you the model is (or isn't) sensitive to a concept you already thought to test for. It has nothing to say about concepts nobody defined a probe set for — including the acquisition-linked or demographic shortcuts that are often the most clinically dangerous, precisely because no one thought to look for them. The concept examples themselves also need curation, and a poorly chosen concept set can produce a misleading concept vector.

## What I take from it

TCAV reframes "is this model faithful to clinical evidence" as a testable, falsifiable question, provided you can name the evidence you expect it to use. That reframing is directly useful for my own audits: rather than asking "is this model interpretable," I can ask "is this model's sensitivity to laterality markers, scanner artifacts, or acquisition site higher than its sensitivity to the pathology it's meant to detect" — and TCAV gives a concrete way to measure that comparison.
