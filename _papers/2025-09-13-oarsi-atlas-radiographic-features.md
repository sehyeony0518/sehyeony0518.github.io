---
layout: post
title: "Atlas of Individual Radiographic Features in Osteoarthritis, Revised"
date: 2025-09-13 12:00:00 +0900
venue: "Osteoarthritis and Cartilage"
authors: "R. D. Altman, G. E. Gold (2007)"
description: "The OARSI atlas that turns joint-space narrowing, osteophytes, and sclerosis into graded reference images — the ground truth that any automated knee-OA grader is ultimately trying to reproduce."
related_posts: false
---

**Paper.** *Atlas of individual radiographic features in osteoarthritis, revised* — [Osteoarthritis and Cartilage (2007)](https://doi.org/10.1016/j.joca.2006.11.009)

## Why I read it

Every deep-learning paper I read on automated Kellgren-Lawrence grading or knee-OA severity prediction ultimately reduces to a supervised-learning problem against labels that came from somewhere. This atlas is where a large share of those labels come from. Before judging whether a model's grading is trustworthy, I wanted to understand what the human reference standard actually looks like — and how much judgment is baked into it.

## What the atlas provides

Altman and Gold's revision of the 1995 OARSI atlas gives radiologists a set of reference images, organized by joint (hand, hip, knee) and by feature (osteophytes, joint space narrowing, sclerosis, cysts), each graded on an ordinal scale against representative photographs. It is explicitly built for clinical-trial and screening use — a common visual anchor so that "grade 2 osteophyte" means roughly the same thing across readers and sites.

## What convinced me

The atlas is not a formula; it is a set of exemplar images and a shared vocabulary. That is a deliberate design choice, and it is also the atlas's core limitation as a machine-learning target: an ordinal category assigned by comparing a new radiograph to a small set of reference photos still carries meaningful inter-observer variability, and a deep model trained on it inherits that variability as label noise rather than a hard ceiling of "ground truth" it should try to exceed.

## What it leaves open

The atlas does not tell you how to combine individual feature grades into a single severity score, nor how to handle borderline cases between two reference images. It also doesn't quantify how much of the label variability across readers is due to genuinely ambiguous radiographs versus reader inattention or training differences — a distinction that matters enormously for how confidently a model's disagreement with a single reader should be interpreted as model error.

## What I take from it

When I read a knee-OA grading paper reporting near-perfect agreement with ground truth, my first question is now: which ground truth, graded by how many readers, using this atlas or a derivative of it? A model that matches one radiologist's atlas-based grade may simply be learning to imitate that radiologist's application of the atlas, not the underlying pathology the atlas is a proxy for. Auditing clinical faithfulness in this domain has to start with auditing the label-generation process, not just the model.
