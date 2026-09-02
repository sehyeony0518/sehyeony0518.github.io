---
layout: post
title: "Right for the Right Reasons: Training Differentiable Models by Constraining Their Explanations"
date: 2026-03-21 12:00:00 +0900
venue: "IJCAI 2017"
authors: "Andrew Slavin Ross, Michael C. Hughes, Finale Doshi-Velez (2017)"
description: "A clinical asthma-and-pneumonia case study opens this paper: a model that learned asthma predicts lower readmission risk, backwards from reality, because of how the training data was collected — and a method to penalize a model for explaining itself that way."
related_posts: false
---

**Paper.** *Right for the Right Reasons: Training Differentiable Models by Constraining their Explanations* — IJCAI 2017

## Why I read it

This is one of the foundational papers behind explanation regularization. It asks whether expert knowledge about an invalid feature can be converted into a training constraint so that a model remains accurate when the spurious correlation disappears.

## What the paper claims

Right for the Right Reasons penalizes input gradients in features or regions marked as irrelevant. The same framework can use expert annotations or generate multiple accurate classifiers with different gradient explanations. The objective therefore optimizes not only the prediction but also a first-order description of how the prediction changes with the input.

## What convinced me

The decoy experiments make the motivation concrete. A model trained on confounded data can achieve nearly perfect training performance yet fall to about 55% when the decoy changes. With a relatively small number of explanation annotations, the constrained model can recover test performance around 95% in the reported setting. This shows that a modest amount of reasoning supervision can be more valuable than additional labels drawn from the same confounded distribution.

## What it leaves open

Input gradients capture local first-order sensitivity, not every interaction or distributed feature. A model may satisfy the gradient penalty while encoding the forbidden information in another form, and later work such as CDEP shows failure cases involving higher-order cues. The approach also depends on correct and sufficiently complete relevance annotations.

## What I take from it

Reasoning constraints need an independent outcome test. After penalizing a suspected feature, I would reverse or remove it, evaluate subgroups, and inspect whether reliance moved elsewhere. The paper establishes the idea; modern medical use requires stronger explanation functionals and more rigorous post-intervention validation.
