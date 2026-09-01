---
layout: post
title: "Automatic Grading of Individual Knee Osteoarthritis Features in Plain Radiographs Using Deep CNNs"
date: 2026-09-18 12:00:00 +0900
venue: "Scientific Reports"
authors: "Aleksei Tiulpin, Simo Saarakkala (2020)"
description: "Rather than predicting a single aggregate KL grade, this model grades each individual OARSI-atlas feature — osteophytes, joint space narrowing, and more — separately, matching the atlas's own granularity."
related_posts: false
---

**Paper.** *Automatic Grading of Individual Knee Osteoarthritis Features in Plain Radiographs using Deep Convolutional Neural Networks* — [Scientific Reports (2020)](https://arxiv.org/abs/1907.08020)

## Why I read it

Having read the OARSI atlas itself and the Kellgren-Lawrence classification primer, I wanted to see a deep-learning paper that engages with the atlas's actual granularity — individual feature grades — rather than collapsing straight to a single aggregate KL score, since that collapse is exactly where I've found a lot of clinical nuance gets lost.

## What the paper claims

Instead of predicting a single holistic KL grade, Tiulpin and Saarakkala train a deep CNN to grade each individual OARSI-atlas feature separately — osteophytes at multiple joint compartments and joint space narrowing among them — providing a fine-grained severity assessment that mirrors how the atlas itself is structured, rather than the coarser five-point aggregate scale typically used as a single training target.

## What convinced me

Matching the model's output granularity to the atlas's own granularity is the right design choice given everything I'd already read about how much subjective aggregation happens when multiple individual features get compressed into one KL number. Predicting individual feature grades keeps the model's output at the same resolution as the clinical reference standard, rather than adding an extra, unmodeled aggregation step.

## What it leaves open

Predicting more, finer-grained labels means more label targets, each of which likely carries its own inter-rater variability — the paper doesn't fully address whether that per-feature noise compounds into a less reliable model overall compared to training on the coarser but more consistently-applied aggregate KL grade. It's a real tradeoff between granularity and label reliability that the paper doesn't fully resolve.

## What I take from it

This is a concrete example of a broader principle I want to apply when I audit grading models: check whether the model's output granularity matches the granularity of its actual clinical reference standard, or whether there's a hidden aggregation step (many features into one score) happening either in the labels or in the model architecture. A model trained on individual OARSI features, like this one, is answering a more specific and more checkable question than one trained only on aggregate KL grade.
