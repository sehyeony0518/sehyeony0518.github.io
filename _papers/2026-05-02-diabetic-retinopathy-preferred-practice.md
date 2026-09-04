---
layout: post
title: "Diabetic Retinopathy Preferred Practice Pattern"
date: 2026-05-02 12:00:00 +0900
venue: "American Academy of Ophthalmology"
authors: "American Academy of Ophthalmology, Retina/Vitreous PPP Panel (2024)"
description: "The clinical practice guideline that defines how diabetic retinopathy is actually meant to be screened, staged, and managed, the standard any AI screening tool is ultimately deployed to support, not replace."
related_posts: false
---

**Paper.** *Diabetic Retinopathy Preferred Practice Pattern*, American Academy of Ophthalmology (approved September 2024)

## Why I read it

An AI system for diabetic retinopathy should be evaluated against the clinical workflow it is meant to support, not only against a benchmark label. I read this guideline to identify the decisions, examination conditions, and safety boundaries that give a DR prediction clinical meaning.

## What the guideline provides

The Preferred Practice Pattern organizes evidence for detection, grading, follow-up, treatment, and patient counseling. It distinguishes disease severity from diabetic macular edema, emphasizes adequate retinal examination and image quality, and links findings to management rather than treating the grade as an isolated classification target. The document was approved by the Academy's Board of Trustees on September 13, 2024.

## What convinced me

The clinically important output is not simply "correct class." The guideline repeatedly connects severity, edema, visual symptoms, prior treatment, and systemic context to different monitoring or referral decisions. This exposes a mismatch in many AI studies: a model can agree with a five-level label while failing to recognize an ungradable image, a sight-threatening lesion, or a case whose management depends on information outside the photograph.

## What it leaves open

A guideline is not a machine-readable ontology, and recommendations must still be interpreted for the local setting, available imaging, and patient circumstances. It also cannot substitute for direct evidence that an AI system improves outcomes or workflow. Translating prose recommendations into model targets requires explicit clinical and regulatory choices.

## What I take from it

I would evaluate a retinal AI system as a decision-support pathway: image quality and gradability first, disease and edema evidence second, calibrated referral recommendation third, and uncertainty throughout. Benchmark agreement is necessary, but clinical usefulness begins where the benchmark label ends.
