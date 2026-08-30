---
layout: post
title: "Shortcuts Over Signal: What COVID Radiograph Models Actually Learned"
date: 2025-11-08 12:00:00 +0900
venue: "Nature Machine Intelligence"
authors: "DeGrave, Janizek, Lee (2021)"
description: "During a pandemic, dozens of high-accuracy COVID detectors were published. This paper showed many were reading laterality markers, patient positioning, and dataset provenance."
related_posts: false
---

**Paper.** *AI for radiographic COVID-19 detection selects shortcuts over signal* — [Nature Machine Intelligence 2021](https://www.nature.com/articles/s42256-021-00338-7)

## Why I read it

It is the cleanest natural experiment the field has had. Under time pressure, with datasets assembled from disparate sources, the community produced many models with excellent reported accuracy. This paper asked what those models were looking at.

## What they found

Using saliency methods and, more convincingly, **generative image manipulation** to test counterfactuals, the authors showed that models attended to image regions outside the lungs: laterality markers, arrows, patient positioning, text annotations, and other traces of where each image came from. COVID-positive and negative images had typically been drawn from *different datasets*, so provenance alone separated the classes.

Performance on internal test data was excellent. Performance on properly matched external data was not.

## The methodological lesson

The counterfactual analysis is what elevates the paper. Attribution maps suggest where a model looks; generating modified images and observing whether the prediction follows tests whether that region is actually doing the work. Explanation becomes falsifiable.

## What it leaves open

The approach requires a generative model faithful enough that manipulations stay on the data manifold. For modalities where that is hard — ultrasound, where speckle and physics are difficult to synthesize plausibly — the counterfactual route is not straightforwardly available. Finding auditing evidence that does not depend on high-quality synthesis is part of what I am working on.

## What I take from it

A benchmark constructed by combining case and control data from different sources is not a benchmark for disease. It is a benchmark for source classification, wearing a clinical label.
