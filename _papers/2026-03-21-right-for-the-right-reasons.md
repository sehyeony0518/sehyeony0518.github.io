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

The paper's opening example is the single clearest illustration I've read of why accuracy alone can hide a dangerous, exactly-backwards clinical relationship, and it's a training-time fix rather than a purely diagnostic one, which made me want to understand the mechanism in detail.

## What the paper claims

A model trained to predict pneumonia-readmission risk learned that a patient having asthma was a *negative* predictor of readmission — the opposite of the true medical relationship, in which asthmatic pneumonia patients are at greater risk. The model learned this backwards association because, in the training data, asthmatic patients were routinely fast-tracked to intensive care, which improved their actual outcomes and made the raw statistical correlation point the wrong way. The authors propose a training-time penalty ("Right for the Right Reasons," RRR) that constrains a model's input-gradient explanation to be small on features annotated as irrelevant, effectively teaching the model not to rely on directions a domain expert has flagged as spurious — not just detecting the problem after the fact, but correcting it during training.

## What convinced me

The asthma example is convincing precisely because it isn't a synthetic shortcut — it's a real, high-stakes case where the confound (differential treatment intensity) is itself clinically meaningful and easy to miss, since the correlation looks like ordinary training data rather than an obvious artifact. It's a strong demonstration of why "the model is accurate" and "the model learned the correct causal direction" are entirely separate claims.

## What it leaves open

RRR requires a human to already know which input directions are spurious and annotate against them — it corrects a *known* shortcut, but offers no mechanism for discovering unknown ones. The penalty is also applied per-feature via gradients, which fits tabular clinical data naturally but is a less direct fit for raw pixel-space image inputs where "the wrong reason" doesn't correspond to a clean input direction.

## What I take from it

This paper reframed, for me, what it means for a shortcut to be dangerous: the asthma case isn't a spurious correlation in the usual sense of "irrelevant noise," it's a correlation caused by good clinical care that happens to point the statistical relationship backwards. When I audit a model for clinical faithfulness now, I explicitly ask whether a confound could be *care-induced* rather than acquisition-induced — a distinct failure mode from the scanner- and site-based shortcuts that dominate the medical-AI shortcut literature.
