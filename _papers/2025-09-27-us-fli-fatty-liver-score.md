---
layout: post
title: "Ultrasonographic Fatty Liver Indicator, a Novel Score Which Rules Out NASH and Is Correlated with Metabolic Parameters in NAFLD"
date: 2025-09-27 12:00:00 +0900
venue: "Liver International"
authors: "Stefano Ballestri, Amedeo Lonardo, Dante Romagnoli, Lucia Carulli, Luisa Losi, Christopher P. Day, Paola Loria (2012)"
description: "A hand-crafted, semi-quantitative ultrasound score (US-FLI) built from four visual features — the kind of clinically legible scoring system that a learned model in the same space should be able to match or explain, not just outperform."
related_posts: false
---

**Paper.** *Ultrasonographic fatty liver indicator, a novel score which rules out NASH and is correlated with metabolic parameters in NAFLD* — [Liver International (2012)](https://doi.org/10.1111/j.1478-3231.2012.02804.x)

## Why I read it

Much of my reading on ultrasound-based liver-steatosis AI compares learned models against a small set of classical scores. US-FLI is one of the most cited of those scores, so I wanted to understand exactly what it measures before judging whether a CNN "beating" it is actually learning something new or just interpolating the same handful of visual cues more smoothly.

## What the paper claims

In 53 patients, the authors built a semi-quantitative score (range 2–8) from four B-mode ultrasound features — hepatorenal echogenicity contrast, posterior beam attenuation, vessel-wall blurring, and difficulty visualizing the gallbladder wall/diaphragm — each scored on a simple ordinal scale and summed. US-FLI correlated with metabolic markers (HOMA-IR, insulin, uric acid, ALT, bilirubin) and, more importantly, was associated with NASH on biopsy (Kleiner criteria), with a US-FLI below 4 giving 94% negative predictive value for severe NASH.

## What convinced me

What makes US-FLI a useful comparator rather than a strawman is that it's fully legible: every point in the score maps to a named, visually checkable feature. A radiologist can look at the same four things the score looks at and say why the number is what it is. That is exactly the property that a learned model competing against it needs to either preserve or explicitly justify giving up.

## What it leaves open

The study is small (53 patients), single-center, and the score's four features were chosen by expert consensus rather than derived data-first — so it's unclear how much of its correlation with NASH reflects genuine biological signal versus features that happen to correlate with disease severity in this particular cohort. It also only weakly discriminates the degree of NASH; it's framed explicitly as a rule-out tool, not a full severity grader.

## What I take from it

When I see a deep model outperform US-FLI on an internal test set, my first question is whether the model is finding features beyond these four legible ones — and if so, whether those additional features are visually explainable to a radiologist or are shortcuts correlated with disease in that dataset. A model that only matches US-FLI's four features with more precision is answering a narrower question than a model that claims a genuinely new, clinically groundable signal.
