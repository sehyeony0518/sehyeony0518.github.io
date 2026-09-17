---
layout: post
title: "Knee Images Digital Analysis (KIDA): A Novel Method to Quantify Individual Radiographic Features of Knee Osteoarthritis in Detail"
date: 2026-04-15 12:00:00 +0900
venue: "Osteoarthritis and Cartilage"
authors: "A. C. A. Marijnissen, K. L. Vincken, P. A. J. M. Vos, D. B. F. Saris, M. A. Viergever, J. W. J. Bijlsma, L. W. Bartels, F. P. J. G. Lafeber (2008)"
description: "A pre-deep-learning digital measurement system for knee-OA radiographic features, a reminder that 'objective, automated quantification' of joint space and osteophytes predates neural networks by well over a decade."
og_image: "https://sehyeony0518.github.io/assets/img/og/2026-04-15-knee-images-digital-analysis-kida.png"
related_posts: false
---

**Paper.** *Knee Images Digital Analysis (KIDA): a novel method to quantify individual radiographic features of knee osteoarthritis in detail*. [Osteoarthritis and Cartilage (2008)](https://doi.org/10.1016/j.joca.2007.06.009)

## The problem before explainable AI

A composite severity grade is convenient, but it compresses several structural findings into one category. Two knees assigned the same grade need not have the same pattern of joint-space loss, osteophytes, or bone changes. A stable category can also conceal a smaller change in one component.

KIDA asks whether those individual radiographic features can be quantified reproducibly using a digital measurement workflow. The question is important independently of machine learning. Before a model can expose meaningful evidence, the evidence itself needs an operational definition and a measurement procedure.

I read this paper as part of that measurement tradition. It shows why auditability cannot be reduced to displaying an explanation after prediction. An explicit quantity, attached to a recognizable anatomical location, can provide a stronger starting point for scrutiny than an unconstrained importance map.

## What the study actually did

The study used standardized, semiflexed radiographs of 20 healthy and 55 osteoarthritic knees. KIDA measured joint-space width, osteophyte area, subchondral bone density, joint angle, and tibial eminence height as continuous variables.

Two observers each evaluated the radiographs twice, blinded to their source and previous measurements. The authors examined within- and between-observer differences using Bland–Altman analysis, compared healthy and osteoarthritic knees, and assessed associations with Kellgren–Lawrence grade. They reported small observer variation and differences between the groups. [Authors' abstract](https://pure.amsterdamumc.nl/en/publications/knee-images-digital-analysis-kida-a-novel-method-to-quantify-indi)

This is a reader-assisted digital measurement study. The presence of software should not be taken to mean that the complete process is autonomous or free of reader judgment.

The repeated-reading design holds the acquired radiograph fixed while changing the reading occasion or observer. That is exactly what makes it useful for evaluating the analysis procedure. It also defines what variability the experiment does not capture.

## Why the design is convincing within its scope

The paper evaluates identifiable measurements rather than asking readers whether a numerical output looks plausible. Each quantity can, in principle, be traced back to a region or geometric construction on the image.

Repeating readings matters because a continuous output can appear more precise simply by containing more decimal places. Numerical resolution is not measurement reliability. Observer comparisons test whether the workflow produces similar values when repeated under the stated conditions.

Comparing with KL grade addresses whether the measurements behave coherently with an established radiographic severity system. Comparing healthy and osteoarthritic groups asks whether the measurements discriminate between populations expected to differ structurally.

Those are useful but distinct forms of evidence. Repeatability concerns the stability of measurement. Group separation concerns differences between sampled populations. Correlation with a grade concerns association with another assessment. None should be substituted for the others.

## What the result does not establish

A reproducible measurement on a fixed image does not establish repeatability after reacquisition. Repositioning, projection geometry, exposure, and the structures visible in the radiograph can change the input before the software is used.

Likewise, separating healthy from osteoarthritic knees cross-sectionally does not demonstrate sensitivity to progression within an individual. Between-person differences may be much larger than the changes a longitudinal study needs to detect.

This distinction is particularly important for a proposed treatment-response endpoint. A system could separate widely different knees reliably yet fail to distinguish small structural change from acquisition variation. A longitudinal claim needs a reference for change and an estimate of the full measurement process's noise.

KL correlation has a further limit: KL is itself a composite judgment involving related radiographic features. Association is expected and useful, but it is not independent confirmation that every component is measured accurately.

Finally, a radiographic quantity is not automatically a direct measure of the underlying tissue process or of patient experience. Structural measurement, symptoms, functional limitation, and treatment decisions need their own relationships established.

## The careful reader's objection

My strongest objection to overinterpreting this study would be the gap between reading repeatability and clinical measurement repeatability. The acquired image is treated as stable in the reader experiment. In use, image formation is part of the measurement instrument.

I would also want the size and pattern of disagreement for each feature, rather than a single characterization of variation as small. An error can be modest in absolute terms but substantial relative to the change of interest. Errors may also increase with severity or with difficulty identifying the relevant boundary.

Correlation between repeated measurements would be insufficient for this purpose. Two readers could rank all knees similarly while one systematically measures larger values. Agreement analysis is valuable precisely because it examines differences rather than relying only on ordering.

The small cohort also limits the range of anatomy and acquisition difficulty represented. The study can establish feasibility and reproducibility in its sample without settling performance in advanced deformity, unusual positioning, or images from another acquisition pipeline.

## Connections to the study notes

[Label Quality and Interobserver Variability](/study/label-quality-and-interobserver-variability/) distinguishes validity, interobserver agreement, intraobserver agreement, and assessability. KIDA provides a concrete example of why these should remain separate. A reproducible feature still requires evidence that it represents the intended construct.

[Auditable-by-Design Medical AI](/study/auditable-by-design-medical-ai/) argues for outputs whose semantics and provenance can be challenged. KIDA supports that principle through explicit measurements. Its contribution is the inspectable interface between image and quantity, even though further validation remains necessary.

[Clinical Feature Annotation and Multi-Task Learning](/study/clinical-feature-annotation-and-multi-task-learning/) separates observation from diagnostic interpretation. KIDA suggests useful targets for a modern system, but a network trained to imitate these measurements would first need to demonstrate measurement agreement. Accurate auxiliary outputs would still not establish that a diagnostic head uses them.

The later component-based knee-grading paper in this corpus addresses a related but different target: ordinal feature grades. Continuous measurement and ordinal grading should not be treated as interchangeable forms of explanation.

## What I would carry into a modern study

I would preserve the measurement definition, anatomical location, reader provenance, and units for every proposed model output. I would evaluate automated measurements against repeated independent readings and inspect systematic as well as random error.

A second experiment would include repeat acquisitions with repositioning. That would estimate the variability of the combined acquisition-and-analysis process, which is the quantity relevant to longitudinal use.

Only then would I assess whether changes in the measurements relate to the clinical outcome or decision of interest. KIDA's enduring lesson for trustworthy AI is practical: build the evidence interface around quantities that can be measured and challenged, then validate each link from image to measurement to clinical interpretation.
