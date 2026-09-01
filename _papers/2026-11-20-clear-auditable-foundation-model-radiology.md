---
layout: post
title: "CLEAR: An Auditable Foundation Model for Radiology Grounded in Clinical Concepts"
date: 2026-11-20 12:00:00 +0900
venue: "Nature Biomedical Engineering"
authors: "Tianyu Han, Riga Wu, Yu Tian, Firas Khader, Lisa C. Adams, Keno K. Bressem, Christos Davatzikos, Jakob Nikolas Kather, et al. (2026)"
description: "A foundation model trained on 0.87 million image-report pairs, built from the ground up around clinical-concept embeddings rather than bolting interpretability onto a black box afterward — auditability as a design constraint, not an add-on."
related_posts: false
---

**Paper.** *CLEAR: an auditable foundation model for radiology grounded in clinical concepts* — [Nature Biomedical Engineering (2026)](https://doi.org/10.1038/s41551-026-01741-4)

## Why I read it

Nearly everything else in this collection audits or explains a model that was trained conventionally, after the fact. CLEAR is the opposite move — a foundation model explicitly built, from training onward, around clinical-concept structure — and given how much of my own interest is in whether trustworthiness has to be retrofitted or can be designed in from the start, I wanted to see this large-scale attempt at the latter.

## What the paper claims

The authors motivate CLEAR by noting that "black box" deep learning models for medical image interpretation limit both clinical trust and the ability to analyze performance degradation over time or across sites. CLEAR — Concept-Level Embeddings for Auditable Radiology — is a foundation model trained on over 0.87 million image-report pairs from 239,391 patients, learning a visual representation structured around clinical concepts rather than an unconstrained embedding space, so that its behavior can be audited at the level of named clinical concepts rather than only through post hoc explanation methods applied after training.

## What convinced me

Building the concept structure into the representation during large-scale pretraining, rather than adding a bottleneck or explanation layer on top of a model trained without any concept constraint, is a meaningfully different and more ambitious bet than most of the interpretability literature I've read — it's foundation-model scale applied to a design philosophy usually only demonstrated on narrow, single-task models like the breast-ultrasound concept bottlenecks I've reviewed elsewhere.

## What it leaves open

Scale and concept-grounding are somewhat in tension — the more a foundation model's representation is constrained around a predefined concept vocabulary, the more it risks missing predictive signal not captured by that vocabulary, exactly the concern raised in narrower concept-bottleneck papers. Whether CLEAR's scale is enough to avoid that tradeoff, or whether it makes the same accuracy-for-auditability tradeoff at a larger scale, isn't something a single paper's own reported numbers can fully settle without independent external replication.

## What I take from it

CLEAR is the clearest example I've found of the field explicitly treating auditability as a first-class training objective for a foundation model, not an afterthought bolted onto a pretrained black box — which is the direction I think medical-AI trustworthiness research needs to keep moving. The open question it leaves me with is exactly the one at the center of my own research: at foundation-model scale, does concept-grounding still support the same kind of intervention test (correct a concept, check the prediction moves) that gives narrower bottleneck models their strongest faithfulness evidence, or does scale change what auditability can even mean.
