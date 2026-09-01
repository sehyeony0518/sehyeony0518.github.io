---
layout: post
title: "Diabetic Retinopathy Preferred Practice Pattern"
date: 2026-05-02 12:00:00 +0900
venue: "American Academy of Ophthalmology"
authors: "American Academy of Ophthalmology, Retina/Vitreous PPP Panel (2024)"
description: "The clinical practice guideline that defines how diabetic retinopathy is actually meant to be screened, staged, and managed — the standard any AI screening tool is ultimately deployed to support, not replace."
related_posts: false
---

**Paper.** *Diabetic Retinopathy Preferred Practice Pattern* — American Academy of Ophthalmology (approved September 2024)

## Why I read it

Deep-learning DR-screening papers usually cite disease severity scales (ICDR, EyePACS) but rarely engage with the full clinical guideline that governs what happens *after* a screening result — referral timing, follow-up intervals, treatment thresholds. I read the PPP to understand the clinical workflow an AI screening tool is actually meant to slot into.

## What the document specifies

The AAO's Preferred Practice Pattern lays out evidence-graded, consensus clinical guidance for diagnosing and managing diabetic retinopathy and diabetic macular edema — screening intervals by disease stage, referral criteria to a retina specialist, and treatment recommendations, developed and externally reviewed by ophthalmology, retina, and endocrinology experts without industry funding.

## What convinced me

Reading the guideline made clear how much of a DR-screening tool's real-world value depends on downstream integration — a model with excellent severity-classification accuracy is only useful if its output maps cleanly onto the referral and follow-up decisions the PPP defines. Accuracy on a held-out DR grade is a necessary but far from sufficient condition for clinical usefulness.

## What it leaves open

The PPP is a synthesis of the current evidence base, not a primary study — it doesn't itself generate new data about AI screening tools, and as guidelines are periodically revised, screening-interval or referral-threshold recommendations here could shift in future updates in ways that would change what "correct" AI output means downstream.

## What I take from it

I now think about DR-AI evaluation less as "does the model output the right ICDR grade" and more as "does the model's output, plugged into this PPP's referral and follow-up logic, produce the same clinical action a specialist reading the guideline would recommend." A grading model can be accurate on the label yet still misalign with the guideline's decision logic if it's evaluated only against the numeric grade and never against the downstream action the grade is supposed to trigger.
