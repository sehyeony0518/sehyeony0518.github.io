---
layout: post
title: "Knee-xRAI: An Explainable AI Framework for Automatic Kellgren-Lawrence Grading of Knee Osteoarthritis"
date: 2026-11-27 12:00:00 +0900
venue: "arXiv preprint"
authors: "Azmul A. Irfan, Nur Ahmad Khatim, Alfan Alfian Irfan, Achmad Zaki, Erike A. Suwarsono, Mansur M. Arief (2026)"
description: "A framework built around the fact that a single-grade disagreement on the KL scale can redirect a patient from conservative therapy to a surgical pathway — explainability motivated directly by clinical stakes, not as a generic add-on."
related_posts: false
---

**Paper.** *Knee-xRAI: An Explainable AI Framework for Automatic Kellgren-Lawrence Grading of Knee Osteoarthritis* — arXiv preprint (2026)

## Why I read it

This is the most recent knee-OA paper in my reading list, and having already read the OARSI atlas, the Kellgren-Lawrence primer, and several classical and deep-learning grading papers, I wanted to see how the field's most current explainable-AI work frames the same reliability problem those earlier sources all point to: KL grading is poorly reproducible across readers.

## What the paper claims

The authors open with the concrete clinical stakes of KL-grading disagreement: because a single-grade disagreement on the Kellgren-Lawrence scale can alter surgical management or redirect a patient from conservative therapy toward intra-articular injection, the poor reproducibility of KL grading across readers isn't just a measurement nuisance — it's a decision-relevant source of error. Knee-xRAI is proposed as an explainable AI framework for automatic KL grading that surfaces the visual evidence behind its grade assignment, aimed at making the model's output checkable against exactly the kind of borderline, clinically consequential disagreements the introduction highlights.

## What convinced me

Opening with the treatment-pathway consequence of a single-grade disagreement, rather than a generic accuracy or agreement statistic, is the right way to motivate explainability for this specific task — it locates the value of interpretability precisely at the KL scale's known weak point (grade boundaries), which is also exactly where the inter-rater unreliability documented across the classification literature concentrates.

## What it leaves open

As a recent preprint, the framework's explanations haven't yet been validated the way, for instance, BUS-CBM's concept intervention was — the paper doesn't report whether correcting or challenging Knee-xRAI's stated visual evidence changes its output the way a genuinely faithful explanation should, which is the test I've come to look for before treating an "explainable" grading model as trustworthy at the specific grade boundaries where it matters most.

## What I take from it

Reading this last, after the OARSI atlas, the KL primer, KIDA, and the individual-feature grading paper, closed a loop for me: this entire chain of knee-OA papers converges on the same fact from different angles — the scale's ordinal boundaries carry real clinical consequence and real reader disagreement, and every automated system built on it inherits that ambiguity whether or not it's explainable. An explainability layer is valuable exactly to the extent it helps a clinician see *why* a borderline case landed where it did — and that value still needs to be demonstrated with an intervention-style test, not just an attention map.
