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

The OARSI atlas is the visual reference behind many component-level knee labels. I read it because an AI model cannot be more clinically interpretable than the definition and reproducibility of the features it is trained to predict.

## What the paper provides

The revised atlas presents reference radiographs for individual osteoarthritis findings in the hand, hip, and knee. Features such as osteophytes and joint-space narrowing are organized by anatomical location and sequenced from normal through grades 1+, 2+, and 3+. The images were selected and arranged by expert consensus for use in clinical studies and trials.

## What convinced me

The atlas makes severity operational and visual. Rather than relying on a prose definition alone, a grader can compare a specific compartment and feature with ordered exemplars. This is particularly useful for machine learning because it separates anatomy, feature type, and severity — information that a single KL grade collapses.

## What it leaves open

The atlas is a reference standard, not a guarantee of high reader agreement. The selected examples cannot cover every projection, anatomy, or borderline case, and ordinal categories remain coarse. Joint-space narrowing on a two-dimensional radiograph also reflects positioning and projection, not only cartilage loss.

## What I take from it

When using OARSI labels, I would preserve site-specific outputs, document the atlas version and reader protocol, and quantify inter-reader uncertainty. The atlas is most useful as an explicit evidence ontology; the model still needs tests showing that those features, rather than correlated image artifacts, drive its final prediction.
