---
layout: post
title: "EyePACS Digital Retinal Image Grading Protocol"
date: 2026-01-17 12:00:00 +0900
venue: "EyePACS Grading Protocol"
authors: "EyePACS"
description: "The internal grading manual behind the EyePACS diabetic-retinopathy dataset, the lesion-by-lesion rulebook that every EyePACS-trained DR model's labels ultimately trace back to."
related_posts: false
---

**Paper.** *EyePACS Digital Retinal Image Grading Protocol Narrative*, EyePACS grading documentation

## Why I read it

Retinal benchmarks often present a final DR class without showing the grading rules that produced it. I read the EyePACS protocol because label construction (especially image quality, lesion certainty, and missing retinal field) directly determines what model errors mean.

## What the protocol specifies

Graders assess individual lesions such as microaneurysms, hemorrhages, cotton-wool spots, venous beading, neovascularization, and hard exudates. An algorithm then combines those lesion grades into overall retinopathy and macular-edema severity. The protocol also defines certainty and gradability rules rather than forcing every photograph into a disease category.

## What convinced me

The operational details expose uncertainty that is hidden in a benchmark CSV. A lesion is recorded as present when the grader is at least 50% certain. An image can be marked ungradable when more than half of the relevant retinal area is missing or obscured; when less is missing, graders are instructed to infer that the unseen area resembles the visible retina. These rules can materially affect both labels and apparent model performance.

## What it leaves open

Protocol consistency does not eliminate reader disagreement or the limitations of a restricted photographic field. Macular-edema grading relies on hard exudates as a surrogate because retinal thickening is not directly observed in color photographs. Models trained on the summary label may therefore learn grading conventions rather than the full clinical condition.

## What I take from it

Dataset labels should be accompanied by their grading algorithm and uncertainty policy. I would model gradability explicitly, preserve lesion-level outputs when available, and analyze disagreements near the protocol's certainty and field-coverage boundaries instead of treating every mismatch as the same error.
