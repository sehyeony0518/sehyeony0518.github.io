---
layout: post
title: "EyePACS Digital Retinal Image Grading Protocol"
date: 2026-01-17 12:00:00 +0900
venue: "EyePACS Grading Protocol"
authors: "EyePACS"
description: "The internal grading manual behind the EyePACS diabetic-retinopathy dataset — the lesion-by-lesion rulebook that every EyePACS-trained DR model's labels ultimately trace back to."
related_posts: false
---

**Paper.** *EyePACS Digital Retinal Image Grading Protocol Narrative* — EyePACS grading documentation

## Why I read it

EyePACS is one of the most widely used public diabetic-retinopathy datasets, and a large fraction of DR-grading deep learning papers I read train or benchmark on it without describing how its labels were actually produced. I wanted to read the grading manual itself rather than keep taking "EyePACS-labeled" at face value.

## What the document specifies

The protocol defines exactly which lesions a human grader is looking for and scoring — microaneurysms, hemorrhages with or without microaneurysms, cotton wool spots, intraretinal microvascular abnormalities, venous beading, new vessels (disc and elsewhere), fibrous proliferation, vitreous or preretinal hemorrhage, and hard exudates — each against reference grading templates, feeding into the overall DR severity label.

## What convinced me

Having an explicit, lesion-by-lesion rulebook behind the labels is exactly the kind of grounding I want before trusting a DR-severity dataset as a training target. It means a "grade 3" label isn't a holistic gestalt call; it's traceable, in principle, back to specific named findings a grader was instructed to look for.

## What it leaves open

A written protocol constrains what graders are *supposed* to look for, but doesn't guarantee consistency in how individual graders apply it — crowd-sourced or distributed grading of the scale EyePACS operates at inevitably has inter-grader variability the protocol document itself can't quantify. It also doesn't specify how disagreements between graders on the same image are resolved into a single training label.

## What I take from it

Reading the actual grading protocol changed how I read reported inter-rater agreement statistics on EyePACS-trained models — a lesion-level protocol like this is a meaningfully stronger foundation than an unstructured "assign a severity grade" instruction, but it's still not a substitute for lesion-level ground truth (e.g., pixel annotations) when auditing whether a model is actually keying on the lesions the protocol defines rather than a correlated shortcut.
