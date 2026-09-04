---
layout: post
title: "Can You Trust This Prediction? Auditing Pointwise Reliability After Learning"
date: 2027-01-22 12:00:00 +0900
venue: "AISTATS 2019"
authors: "Peter Schulam, Suchi Saria (2019)"
description: "Resampling Uncertainty Estimation asks a narrower, more auditable question than most uncertainty methods: not how confident is the model in general, but how much would this specific prediction have changed if the model had been fit on slightly different training data."
related_posts: false
---

**Paper.** *Can You Trust This Prediction? Auditing Pointwise Reliability After Learning* — [AISTATS 2019](https://proceedings.mlr.press/v89/schulam19a.html)

## Why I read it

Most uncertainty-estimation approaches I encounter require building uncertainty into the model itself, through a Bayesian architecture or an ensemble trained from scratch. This paper is explicitly framed as a post hoc audit: something applied after a model is already trained, which fits the retraining-free auditing constraint at the center of my own thesis work.

## What the paper claims

Average error on held-out data is the field's default reliability signal, but the authors point out it says nothing under dataset shift and can hide large errors on individual, atypical inputs even when the aggregate is low. They propose Resampling Uncertainty Estimation (RUE), which estimates how much a specific prediction would change if the model had instead been fit on a different draw of training data, without literally refitting the model on many resampled datasets. The method uses the gradient and Hessian of the model's loss function to approximate this counterfactual retraining effect and build an ensemble of plausible predictions cheaply. The result is a pointwise reliability score attached to each individual prediction, evaluated in the paper primarily as an error-detection tool: does a low RUE score for a given prediction correlate with that prediction actually being wrong.

## What convinced me

Framing the question as pointwise rather than aggregate is the right level for a clinical audit, since a clinician does not act on a model's average error rate, they act on the prediction in front of them for one patient. Building the retraining-sensitivity estimate from the loss function's existing gradient and Hessian, rather than requiring literal ensemble retraining, is also a meaningful practical constraint: it makes the method something that can be applied to an already-trained model rather than something that has to be designed in before training begins, the same retraining-free property I want from any auditing tool I use on ultrasound models.

## What it leaves open

RUE approximates how sensitive a prediction is to which training data the model happened to see, which is a specific and narrow notion of unreliability. It says nothing directly about whether the prediction rests on clinically valid evidence in the first place, a model could be very stable across resampled training sets while still being stable in its reliance on an acquisition-linked shortcut, since the shortcut would be present in every resampled draw too. The Hessian-based approximation is also a local, first-order picture of the loss landscape and inherits whatever it misses about a model's true global sensitivity to its training data.

## What I take from it

Stability under resampling and clinical faithfulness are separate axes that happen to sound similar. A prediction can be reliably reproduced across plausible retrainings of the same model on the same confounded data and still be reliably wrong for the same clinically invalid reason every time. I would want a RUE-style pointwise reliability score reported alongside, not instead of, an evidence-based faithfulness check, the same complementary pairing I keep arriving at with uncertainty estimation more generally in this collection.
