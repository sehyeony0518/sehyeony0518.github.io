---
layout: post
title: "Underspecification Presents Challenges for Credibility in Modern Machine Learning"
date: 2026-03-28 12:00:00 +0900
venue: "JMLR"
authors: "Alexander D'Amour, Katherine Heller, Dan Moldovan, Ben Adlam, Babak Alipanahi, Alex Beutel, Christina Chen, Jonathan Deaton, et al. (2020)"
description: "Two models with identical training accuracy, identical architecture, and different random seeds can behave completely differently under distribution shift — a Google-scale audit of just how common this is, including in a dermatology model."
related_posts: false
---

**Paper.** *Underspecification Presents Challenges for Credibility in Modern Machine Learning* — [arXiv (2020)](https://arxiv.org/abs/2011.03395)

## Why I read it

Two models can have indistinguishable held-out performance and still behave very differently after deployment. I read this paper because it explains why that is not an unusual edge case but a structural consequence of how modern pipelines select models.

## What the paper claims

A learning problem is underspecified when the available training and validation criteria admit many predictors that satisfy the stated requirements but differ on deployment-relevant behavior. The paper demonstrates this across computer vision, medical imaging, natural language processing, clinical risk prediction, and genomics. Standard in-distribution test performance does not determine which solution a training run will find.

## What convinced me

The cross-domain evidence is the paper's strength. Repeated training runs and architectures can occupy a narrow band of benchmark accuracy while varying substantially on stress tests, subgroup behavior, robustness, or clinically relevant associations. This makes random seed and model-selection criterion scientific variables, not implementation details. The paper also distinguishes underspecification from distribution shift: the ambiguity exists before deployment because the development objective never ruled out the competing solutions.

## What it leaves open

The diagnosis does not provide a universal model-selection rule. Stress tests must be designed from domain knowledge, and a finite panel can still miss the behavior that matters later. The original work circulated in 2020, but the final JMLR publication is 2022; the portfolio metadata should make that distinction clear.

## What I take from it

A single checkpoint cannot represent the credibility of a pipeline. I would report seed variation, define deployment-relevant stress tests before model selection, and prefer models whose evidence use is stable across near-optimal solutions. Accuracy ties should trigger deeper auditing rather than arbitrary selection.
