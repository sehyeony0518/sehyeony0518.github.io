---
layout: post
title: "Shortcut Learning in Deep Neural Networks"
date: 2025-09-06 12:00:00 +0900
venue: "Nature Machine Intelligence"
authors: "Geirhos, Jacobsen, Michaelis, Zemel, Brendel, Bethge, Wichmann (2020)"
description: "The paper that gave the field a shared vocabulary for models that solve the benchmark without solving the task."
related_posts: false
---

**Paper.** *Shortcut Learning in Deep Neural Networks*. [Nature Machine Intelligence 2020](https://www.nature.com/articles/s42256-020-00257-z)

## Why I read it

This perspective provides the conceptual vocabulary for much of my research. It unifies failures that are often described separately (texture bias, background reliance, dataset artifacts, poor transfer) under the idea that a model learns an easy decision rule that succeeds on the benchmark but fails under a more revealing test.

## What the paper claims

A shortcut is a decision rule that performs well under the standard training and test conditions yet does not transfer to the intended real-world conditions. The authors connect examples from machine learning with related phenomena in psychology, education, and linguistics, then argue for better benchmarks, interpretation, robustness testing, and study of learning dynamics.

## What convinced me

The definition shifts attention from whether a feature is visually "spurious" to whether the decision rule remains valid under the target conditions. That is important in medicine, where a scanner marker, demographic variable, or care-pathway cue may be genuinely correlated with disease but still be unsuitable as the basis of a diagnostic claim. The paper also explains why in-distribution accuracy cannot distinguish a robust rule from a shortcut when both solve the benchmark.

## What it leaves open

This is a perspective, not a detector or mitigation algorithm. It does not provide a universal boundary between legitimate context and shortcut, and the correct distinction depends on the deployment claim. A model can also combine valid evidence and shortcuts, so the problem is often quantitative rather than binary.

## What I take from it

A shortcut should be defined relative to a stated clinical use and tested by changing the environment, evidence, or correlation that makes the rule easy. This paper gives the umbrella concept; the rest of the portfolio asks how to measure availability, utilization, clinical alignment, and generalization separately.
