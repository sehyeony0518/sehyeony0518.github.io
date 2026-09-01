---
layout: post
title: "Knee Images Digital Analysis (KIDA): A Novel Method to Quantify Radiographic Features of Knee OA"
date: 2026-07-18 12:00:00 +0900
venue: "Osteoarthritis and Cartilage"
authors: "A. C. A. Marijnissen, K. L. Vincken, P. A. J. M. Vos, D. B. F. Saris, M. A. Viergever, J. W. J. Bijlsma, L. W. Bartels, F. P. J. G. Lafeber (2008)"
description: "A pre-deep-learning digital measurement system for knee-OA radiographic features — a reminder that 'objective, automated quantification' of joint space and osteophytes predates neural networks by well over a decade."
related_posts: false
---

**Paper.** *Knee Images Digital Analysis (KIDA): a novel method to quantify individual radiographic features of knee osteoarthritis in detail* — [Osteoarthritis and Cartilage (2008)](https://doi.org/10.1016/j.joca.2007.06.009)

## Why I read it

Deep-learning knee-OA papers often frame "automated, objective quantification of joint features" as a novel contribution of the deep-learning era. KIDA predates that framing by well over a decade, so I wanted to see what "digital, objective" measurement of the same features looked like before neural networks, and how much of the problem it had already solved.

## What the paper claims

Radiography remains the gold-standard imaging modality for OA features like joint space narrowing, osteophytes, and subchondral sclerosis, but the paper notes that manual assessment of these features is difficult to make fully objective across readers. KIDA is a semi-automated digital image-analysis method designed to quantify these individual radiographic features of the knee in more detail and reproducibility than holistic visual grading (like KL grade) allows.

## What convinced me

The paper's motivation — that manual, holistic grading struggles with objectivity and granularity — is the exact same motivation cited by every deep-learning knee-OA paper I've read since. Seeing that motivation already fully articulated and partially addressed with classical digital image-processing methods more than fifteen years earlier reframes how novel the "objective, automated" framing in newer deep-learning papers actually is.

## What it leaves open

As a semi-automated method, KIDA still requires meaningful operator involvement (landmark placement, calibration) rather than being fully automatic, and the paper's validation is on a specific cohort and imaging protocol — its reproducibility gains don't automatically establish how well it, or its successors, generalize across different radiographic acquisition setups.

## What I take from it

When a deep-learning paper claims novelty specifically for "automated, objective quantification" of a classical radiographic feature, I now check what the actual claimed advance is over methods like KIDA — full automation (removing the remaining manual steps), a genuinely different feature set, or just packaging an old idea in a new architecture. The underlying goal of moving past subjective holistic grading toward reproducible, granular measurement is not new; what a deep model adds on top of that goal is the part that actually needs justifying.
