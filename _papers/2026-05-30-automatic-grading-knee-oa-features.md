---
layout: post
title: "Automatic Grading of Individual Knee Osteoarthritis Features in Plain Radiographs Using Deep CNNs"
date: 2026-05-30 12:00:00 +0900
venue: "Scientific Reports"
authors: "Aleksei Tiulpin, Simo Saarakkala (2020)"
description: "Rather than predicting a single aggregate KL grade, this model grades each individual OARSI-atlas feature (osteophytes, joint space narrowing, and more) separately, matching the atlas's own granularity."
related_posts: false
---

**Paper.** *Automatic Grading of Individual Knee Osteoarthritis Features in Plain Radiographs Using Deep Convolutional Neural Networks*. [Publisher's article](https://www.mdpi.com/2075-4418/10/11/932)

The front matter names Scientific Reports, but the publisher identifies this article as Diagnostics (2020).

## The question beyond predicting KL grade

A composite Kellgren–Lawrence grade is a compressed description of radiographic osteoarthritis. It does not separately report which structural features are present or where they occur.

Predicting individual features could make automated assessment more useful. A reader could inspect medial joint-space narrowing separately from a lateral osteophyte and identify which part of the assessment is questionable.

The open question is whether a model can produce that more detailed profile reliably, including outside its development cohort. Another question follows immediately: does the accompanying KL prediction actually depend on those feature outputs?

This paper addresses the first question more directly than the second. That distinction is central to its relevance for trustworthy medical AI.

## What the authors built

The system jointly predicts KL grade and six compartment-specific OARSI grades: femoral osteophytes, tibial osteophytes, and joint-space narrowing on the medial and lateral sides.

It uses ImageNet-pretrained residual-network variants, independent output heads, and ensembling. Development uses 19,704 knee images from OAI; independent testing uses 11,743 from MOST. Model selection uses subject-wise cross-validation within OAI.

Both cohorts use fixed-flexion radiographs with a standardized positioning frame and beam angle. Images undergo knee localization, alignment, cropping, and intensity preprocessing. [Methods](https://www.mdpi.com/2075-4418/10/11/932)

The image counts should not be interpreted as numbers of independent people. The datasets include repeated observations. Subject-wise development splits are therefore an important design choice.

The implemented feature set is also specific. This is not an automated assessment of every feature that an osteoarthritis atlas might describe. Its contribution should be judged against the six named outputs and the composite KL task.

## What external validation establishes

On MOST, the reported Cohen's kappa for KL is 0.82, with balanced accuracy 66.68%. Kappa values for the individual features range approximately from 0.79 to 0.94. Binary radiographic OA detection reaches AUROC and average precision near 0.98. [Results](https://www.mdpi.com/2075-4418/10/11/932)

The independent cohort is the strongest part of the evidence. The model is not evaluated solely on another partition of its training collection.

However, this is transfer between two cohorts with related acquisition conventions. It does not establish equivalent performance on arbitrary clinical radiographs, different projections, or another preprocessing pipeline.

The difference between strong binary detection and more modest balanced grading accuracy is also instructive. Recognizing whether a thresholded disease definition is met can be easier than assigning the exact ordinal grade across the full range.

These endpoints should not be substituted for one another. A model suitable for broad case identification may still make too many grade-boundary errors for progression assessment or another use that depends on fine distinctions.

## Why the component outputs are useful

A structured profile makes disagreement more inspectable. If the model and reader disagree on KL grade, the feature outputs can help identify whether joint-space narrowing or osteophyte assessment is also disputed.

That is valuable even before making a strong interpretability claim. A clinician or researcher can evaluate each component against its own reference and investigate errors that a single composite label would conceal.

The outputs can also expose asymmetric failure. A pooled grade metric might hide weaker performance in one compartment or on a less common feature severity.

But this practical value depends on retaining uncertainty. A confident categorical display can make an uncertain feature look settled. In an application, it would be useful to preserve probabilities, assessability, and the image region needed for review rather than show only an integer.

## The main interpretability limit

The OARSI heads and KL head share learned image features, but the KL head is not described as a function restricted to the six displayed OARSI predictions.

Therefore, correct component outputs do not prove that the composite decision uses them. The model could predict the components accurately and still obtain its KL output through another correlated feature in the shared representation.

This is an architectural distinction, not a criticism that multi-task learning is inherently inappropriate. Auxiliary outputs can improve usefulness and training while leaving the diagnostic pathway only partially exposed.

A stronger claim would require either an explicit concept bottleneck or a carefully designed intervention on the relevant shared representation. Simply changing a displayed component value would not affect a separate KL head unless that value actually lies on its computational path.

Even a strict bottleneck would need validation of the concept values and their intervention behavior. The presence of named intermediate outputs does not settle their semantics.

## The weakness a careful reader should raise

The reference labels are reader-dependent ordinal judgments. Agreement with them measures reproduction of a grading process, not direct recovery of an unobserved biological severity.

A high kappa also needs the grade distribution and confusion matrix for interpretation. Frequent categories, uncommon severe grades, and systematic adjacent-grade errors can affect the practical meaning of the summary.

Repeated images introduce another issue: confidence intervals should reflect the dependence structure relevant to the claim. The paper includes an additional first-follow-up evaluation, which is useful, but uncertainty across patients and across acquisition settings remains conceptually different from uncertainty across images.

I would also examine whether component disagreements are clinically coherent. For example, do errors occur around subtle grade boundaries, or does the model sometimes assign a structurally implausible combination? Aggregate agreement cannot answer that question.

Clinical utility would require a further comparison with the workflow the model is intended to support. Faster grading, more reproducible research measurements, and better patient decisions are distinct possible benefits.

## Connections to the study notes

[Clinical Feature Annotation and Multi-Task Learning](/study/clinical-feature-annotation-and-multi-task-learning/) explicitly separates feature accuracy from diagnostic use. This paper supports the usefulness of shared training and structured outputs while illustrating why an auxiliary head is not a complete explanation.

[Label Quality and Interobserver Variability](/study/label-quality-and-interobserver-variability/) provides the framework for interpreting agreement against ordinal reader labels. Category-specific errors and reader provenance remain necessary even when the overall kappa is favorable.

[Auditable-by-Design Medical AI](/study/auditable-by-design-medical-ai/) distinguishes an exposed concept pathway from a bypass through unrestricted features. The independent heads here make that distinction concrete.

KIDA, also reviewed in this corpus, complements this work by focusing on continuous measurements. The two approaches should be compared according to their intended outputs: agreement on ordinal grades and agreement on physical measurements are different validation problems.

## What I would take into my own system

I would expose clinically defined feature outputs, evaluate each independently, and document whether the final diagnosis uses those outputs or merely shares their representation.

For a gallbladder model, I would retain feature assessability and reader disagreement rather than convert every uncertain observation into a hard negative label.

If the intended claim is faithful clinical reasoning, I would add a computational path that supports meaningful concept correction and test the resulting diagnostic changes. This paper demonstrates that a transferable structural profile is feasible. Establishing that the composite prediction follows that profile is the next experiment.
