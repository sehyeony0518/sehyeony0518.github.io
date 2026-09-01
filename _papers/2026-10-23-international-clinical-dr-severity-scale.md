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

The International Clinical Diabetic Retinopathy (ICDR) scale is the label space behind most DR-severity deep-learning papers I've read, usually cited as a fixed reference rather than examined for how it was actually built. I wanted to trace it back to its origin the same way I did for Kellgren-Lawrence in knee OA.

## What the paper claims

A group of 31 individuals from 16 countries — comprehensive ophthalmologists, retina subspecialists, endocrinologists, and epidemiologists — set out to build consensus clinical severity scales for diabetic retinopathy and diabetic macular edema that could be used consistently worldwide. Starting from an initial classification grounded in the ETDRS and Wisconsin Epidemiologic Study of DR, the group used a modified Delphi process — anonymous rounds of review and revision — to converge on separate, simplified severity scales for DR and DME suitable for routine clinical communication, distinct from the more granular research-grade ETDRS scale.

## What convinced me

Being explicit that this is a consensus process, not a measurement, is exactly the kind of transparency I want from a label-defining paper — it tells you upfront that the scale trades some of ETDRS's granularity for international, cross-practice consistency, a deliberate simplification rather than an oversight.

## What it leaves open

A Delphi-consensus process converges on agreement among the specific panel involved; it doesn't guarantee the resulting simplified scale carves disease severity at its most clinically meaningful joints, and the paper doesn't quantify how much information is lost relative to the more granular ETDRS scale it was derived to simplify.

## What I take from it

Every DR-AI paper reporting "accuracy against ICDR grade" is implicitly reporting accuracy against a deliberately simplified, consensus-built label space — not a direct clinical measurement. That's a reasonable design tradeoff for clinical communication, but it means a model's ICDR-grade accuracy understates how much finer-grained disease information (of the kind ETDRS captures) the model might be missing or, alternatively, might be capturing without credit for it. I now read ICDR-based accuracy claims with that simplification explicitly in mind.
