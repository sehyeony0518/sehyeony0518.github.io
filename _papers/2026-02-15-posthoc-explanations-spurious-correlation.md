---
layout: post
title: "Post hoc Explanations May Be Ineffective for Detecting Unknown Spurious Correlation"
date: 2026-02-15 12:00:00 +0900
venue: "ICLR 2022"
authors: "Julius Adebayo, Michael Muelly, Hal Abelson, Been Kim (2022)"
description: "A sobering stress test of the exact interpretability toolkit I lean on elsewhere in this collection (feature attribution, concept activation, and training-point ranking) against spurious signals the practitioner doesn't already know to look for."
related_posts: false
---

**Paper.** *Post hoc Explanations May Be Ineffective for Detecting Unknown Spurious Correlation*. [ICLR 2022](https://arxiv.org/abs/2212.04629)

## Why I read it

A major promise of post hoc explanation is that it can reveal an unexpected shortcut. This paper tests that promise under controlled conditions where the spurious feature is known to the experimenter but deliberately unknown to the explanation user.

## What the paper claims

The authors evaluate feature attributions, concept-based explanations, and training-point rankings on semi-synthetic medical and natural-image tasks with inserted tags, stripes, or blur. They ask whether a practitioner could discover the unknown spurious correlation from the explanation output, rather than merely confirm a shortcut that had already been named.

## What convinced me

The distinction between visible and non-visible shortcuts is particularly important. Methods sometimes highlighted a conspicuous tag or stripe, but performance deteriorated sharply for diffuse blur and for settings where the explanation itself could be misread. Some attribution methods also appeared to implicate a spurious feature even when the classifier was not actually relying on it. Thus an explanation can produce both missed detections and false narratives.

## What it leaves open

The study cannot exhaust every explanation method or every discovery workflow, and a domain expert with a specific hypothesis may use explanations more effectively than a blind evaluator. The result is therefore not that post hoc explanations have no value. It is that they are poorly suited to guaranteeing discovery of unknown unknowns.

## What I take from it

Explanation should be used to test a stated hypothesis, then checked with a behavioral intervention. Unknown-shortcut discovery requires broader tools: data-source analysis, subgroup and error auditing, counterfactual tests, and acquisition metadata. A heatmap should not be treated as a universal shortcut detector.
