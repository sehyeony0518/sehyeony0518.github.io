---
layout: post
title: "Concept Bottleneck Models"
date: 2025-12-27 12:00:00 +0900
venue: "ICML 2020"
authors: "Pang Wei Koh, Thao Nguyen, Yew Siang Tang, Stephen Mussmann, Emma Pierson, Been Kim, Percy Liang (2020)"
description: "The paper that named and formalized the concept bottleneck — asking, using the paper's own example, whether a model would still predict severe arthritis if it didn't think there was a bone spur."
related_posts: false
---

**Paper.** *Concept Bottleneck Models* — [ICML 2020](https://arxiv.org/abs/2007.04612)

## Why I read it

I keep encountering "concept bottleneck" as a design pattern in breast-ultrasound and other medical-imaging papers before I'd actually read the paper that formalized it. Going back to the source clarified which parts of the pattern are load-bearing and which are just conventional implementation choices.

## What the paper claims

A concept bottleneck model forces a network to predict a set of human-defined, named intermediate concepts — the paper's own running example is "is there a bone spur in this x-ray" — before those concept predictions are used, and only those, to predict the final label (arthritis severity). Because the final layer only sees concepts, a clinician can inspect, and critically, intervene on them: manually correct a concept the model got wrong and observe whether the final prediction changes accordingly. The paper shows this intervention meaningfully improves accuracy in several domains, including x-ray-based severity grading.

## What convinced me

The framing of intervention as the test of the architecture is what separates this from purely decorative interpretability. The question isn't "can you show me a concept," it's "if this concept were fixed, would the answer change" — and the paper treats a bottleneck that fails this test (because the final layer leaks information around it) as a design bug to be identified and fixed, not glossed over.

## What it leaves open

Concept bottlenecks trade some raw accuracy for this checkability — the paper is honest that a fully end-to-end model without the bottleneck sometimes performs slightly better, since the bottleneck can only pass through information expressed in the chosen concept vocabulary. The paper also doesn't fully resolve how to choose a concept vocabulary that's both clinically meaningful and complete enough not to force the model to encode extra information illegitimately in the concepts it does have.

## What I take from it

This paper is the shared ancestor of the breast-ultrasound and other medical concept-bottleneck papers I've reviewed, and reading it directly clarified what "faithful to the bottleneck" actually requires: not just naming concepts, but demonstrating that correcting them changes the outcome. That's the bar I now hold any "interpretable by design" medical model to, and it's a bar most papers claiming interpretability don't actually clear.
