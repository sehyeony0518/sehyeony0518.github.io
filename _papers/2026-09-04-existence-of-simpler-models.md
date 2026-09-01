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

I regularly read medical-AI papers that justify a complex, opaque model with some version of "a simpler model wasn't accurate enough." This paper directly interrogates that justification, asking when it's actually true versus an assumption nobody tested.

## What the paper claims

Finding optimal sparse, accurate models — small decision trees, integer-coefficient linear models, short rule lists — is generally NP-hard, so in practice teams reach for complex models rather than search for simpler ones that might perform just as well. The authors formalize and study the "Rashomon set": the set of models, of any given form, that achieve near-optimal accuracy on a dataset. Their central hypothesis, which they give theoretical and empirical support for, is that when a dataset admits many complex models achieving similar top accuracy, it typically also contains simple, interpretable models achieving comparably good accuracy — the Rashomon set for simple models is often non-empty precisely when the Rashomon set for complex models is large.

## What convinced me

The theoretical framing turns "should we have used a simpler model" from a vague intuition into an empirically checkable question: characterize the Rashomon set for a given problem, and see whether a simple, interpretable model actually lives inside it. That's a testable claim, not a slogan about preferring interpretability for its own sake.

## What it leaves open

Whether a simple, accurate model exists in the Rashomon set for a *specific* dataset still isn't free to determine — the underlying search problem remains hard, and the paper's guarantees are about typical/expected behavior across problem classes, not a promise for any individual dataset a researcher happens to be working with. A team still needs to actually do the (expensive) search to find out.

## What I take from it

This paper gives me a principled challenge to raise whenever a medical-AI paper defends model complexity purely on accuracy grounds: has an interpretable model actually been searched for and found wanting, or has interpretability simply not been attempted? Given how much clinical trust depends on legibility, the burden this paper implies is on the complex model to demonstrate the search was done — not on critics to prove a simple alternative exists.
