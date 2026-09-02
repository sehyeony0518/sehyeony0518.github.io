---
layout: post
title: "Proposed International Clinical Diabetic Retinopathy and Diabetic Macular Edema Disease Severity Scales"
date: 2026-10-23 12:00:00 +0900
venue: "Ophthalmology"
authors: "C. P. Wilkinson, Frederick L. Ferris III, Ronald E. Klein, Paul P. Lee, Carl David Agardh, et al. (2003)"
description: "The ICDR scale — a 31-person, 16-country consensus process behind the DR severity labels nearly every retinal AI paper trains against, built via a modified Delphi method rather than a single objective measurement."
related_posts: false
---

**Paper.** *Proposed International Clinical Diabetic Retinopathy and Diabetic Macular Edema Disease Severity Scales* — [Ophthalmology (2003)](https://doi.org/10.1016/S0161-6420(03)00475-5)

## Why I read it

This paper is not an AI method, but it defines one of the label systems that retinal AI models are trained to reproduce. I read it to understand what a "ground-truth" diabetic-retinopathy grade actually represents before treating the labels as natural biological categories.

## What the paper claims

Using a modified Delphi process, 31 participants from 16 countries developed a practical five-stage clinical DR scale: no apparent retinopathy, mild, moderate, and severe nonproliferative DR, followed by proliferative DR. Diabetic macular edema is recorded separately as apparently present or absent, with distance from the foveal center added when examination resources permit.

## What convinced me

The scale is explicitly designed as a communication and care-delivery compromise. It translates evidence from more detailed research systems into categories that clinicians with different equipment and training can apply internationally. That design history explains both its usefulness and its coarseness: the categories are meant to support common clinical decisions, not to preserve every lesion-level distinction.

## What it leaves open

A consensus taxonomy is not an error-free biological truth. Its application still depends on image field, image quality, reader judgment, and available examination tools. Collapsing a continuous and heterogeneous disease process into five stages also creates boundary ambiguity that an AI model cannot eliminate simply by achieving high accuracy.

## What I take from it

Clinical labels should be documented as operational constructs: who defined them, for what decision, under which examination conditions, and with what uncertainty. For retinal AI, I would evaluate ungradable cases and lesion-level evidence separately from agreement with the final ordinal category.
