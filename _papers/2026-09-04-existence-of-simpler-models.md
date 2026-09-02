---
layout: post
title: "On the Existence of Simpler Machine Learning Models"
date: 2026-09-04 12:00:00 +0900
venue: "ACM FAccT 2022"
authors: "Lesia Semenova, Cynthia Rudin, Ronald Parr (2022)"
description: "The Rashomon-set argument: for a given dataset, there are often many equally accurate models, some far simpler and more interpretable than others — so 'we needed the complex model for accuracy' is a claim that should be checked, not assumed."
related_posts: false
---

**Paper.** *On the Existence of Simpler Machine Learning Models* — [ACM FAccT 2022](https://arxiv.org/abs/1908.01755)

## Why I read it

In high-stakes medical AI, a complex model is often accepted because it performs marginally better — or because no one checked whether an equally accurate simpler model exists. This paper gives a formal reason to make that search part of model development rather than an optional afterthought.

## What the paper claims

The authors study the Rashomon set: all models in a hypothesis class whose loss is close to optimal. They define the Rashomon ratio as the volume of this set relative to the full hypothesis space and show conditions under which a large Rashomon set contains accurate models from simpler classes. Similar performance across substantially different learning algorithms is proposed as a practical signal that such a set may be large.

## What convinced me

The paper connects a familiar empirical pattern — linear models, trees, boosted models, and neural networks achieving nearly the same score — to a testable modeling decision. Its theoretical results do not merely celebrate model multiplicity; they explain why a simpler class may approximate many near-optimal functions and obtain favorable generalization guarantees. The empirical analyses then show that datasets with similar performance across model families often admit sparse or otherwise simpler alternatives.

## What it leaves open

The heuristic is not a guarantee. Similar validation scores can hide different subgroup failures, calibration, or shortcut reliance, and estimating the Rashomon ratio is itself difficult in large neural-network spaces. "Simple" also needs a task-relevant definition: a small parameter count is not necessarily clinically interpretable.

## What I take from it

Before defending a black box, I would establish a performance tolerance and actively search within it for transparent alternatives. If several architectures tie on accuracy, the next comparison should be evidence use, stability, and clinical auditability — not another decimal place of AUROC.
