---
layout: post
title: "CLEAR: An Auditable Foundation Model for Radiology Grounded in Clinical Concepts"
date: 2026-07-15 12:00:00 +0900
venue: "Nature Biomedical Engineering"
authors: "Tianyu Han, Riga Wu, Yu Tian, Firas Khader, Lisa C. Adams, Keno K. Bressem, Christos Davatzikos, Jakob Nikolas Kather, et al. (2026)"
description: "A foundation model trained on 0.87 million image-report pairs, built from the ground up around clinical-concept embeddings rather than bolting interpretability onto a black box afterward, auditability as a design constraint, not an add-on."
related_posts: false
---

**Paper.** *CLEAR: an auditable foundation model for radiology grounded in clinical concepts*. [Nature Biomedical Engineering (2026)](https://doi.org/10.1038/s41551-026-01741-4)

## Why I read it

Foundation models usually become harder to inspect as their scale increases. CLEAR interested me because it asks whether scale and auditability can be designed together by making radiological observations, rather than opaque latent dimensions, the model's representational interface.

## What the paper claims

CLEAR is trained on more than 0.87 million chest X-ray–report pairs from 239,391 patients. It maps images into a concept space built from 368,294 report-derived radiological observations and decomposes each prediction into weighted contributions from those concepts. The same representation supports zero-shot classification, linear probing, retrieval, and concept intervention.

## What convinced me

The paper does more than show concept examples. CLEAR improved zero-shot AUROC over CheXzero on VinDr (78.2 versus 75.0) and PadChest (70.0 versus 66.8), while linear probing on CheXpert reached a mean AUROC of 87.0. More importantly for faithfulness, correcting the concept for enlarged cardiomediastinum improved its AUROC from 0.727 to 0.784 without retraining the encoder. In a reader assessment, 89.8% of the highest-weighted concepts were judged diagnostically relevant, with substantial inter-reader agreement.

## What it leaves open

The vocabulary is mined from reports, so it inherits reporting conventions, omissions, and institution-specific language. A weighted concept decomposition is also not a spatial localization or a causal proof that every concept was necessary. Performance on consolidation remained below the radiologist reference, illustrating that a large concept space can still be incomplete for particular findings.

## What I take from it

The strongest part of CLEAR is the editable concept interface, not merely the readable vocabulary. For an auditable foundation model, I would evaluate three properties separately: concept coverage, decomposition fidelity, and whether clinically valid concept interventions change predictions in the expected direction.
