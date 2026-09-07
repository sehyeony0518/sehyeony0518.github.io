---
layout: page
title: "Geometry of Representation Spaces"
description: "Cosine similarity, manifolds, metric spaces, and representation geometry, and what the shape of a latent space says about what a model encodes."
section: "F"
section_title: "Mathematical and Statistical Foundations"
branch: "Branch 01"
order: 6
written: true
---

A representation space is the set of feature vectors a model produces at a particular layer. Its geometry describes which inputs become close, which become separated, and which changes in an image produce substantial changes in its representation.

## Why it matters here

A medical image classifier can separate diagnostic labels while also organizing images by hospital, device, or acquisition protocol. Looking at representation geometry gives me a way to investigate these competing structures. The difficulty is that a visible pattern does not explain how it arose or whether the classifier uses it.

For my research, the useful question is whether relationships between representations correspond to independently described clinical differences. If gallbladder ultrasound images become neighbors, I want to understand what they share: lesion morphology, surrounding anatomy, image settings, or something I have not measured. Geometry makes that question testable, but it does not supply the clinical interpretation.

## The core ideas

### A distance defines what counts as close

A metric space combines a set of objects with a distance function that is nonnegative, symmetric, zero only between identical objects, and satisfies the triangle inequality. Euclidean distance is one choice for feature vectors. Its meaning depends on the coordinates and their scales: a feature with large numerical variation can dominate distance. I therefore need to describe the layer, preprocessing, and scaling before interpreting any nearest-neighbor result.

### Cosine similarity preserves direction and discards magnitude

For nonzero vectors, cosine similarity is their dot product divided by the product of their lengths. It compares direction, so multiplying either vector by a positive scalar leaves the similarity unchanged. This is useful when magnitude is irrelevant, but normalization can also remove information worth studying. The commonly used quantity one minus cosine similarity is not generally a metric. On unit vectors, Euclidean distance gives the same neighbor ordering as cosine similarity, while satisfying the metric requirements.

### A manifold is a hypothesis about local structure

A manifold is a space that locally resembles a Euclidean space of some dimension. The manifold hypothesis suggests that structured data may lie near a lower-dimensional subset of a much larger ambient space. A curved surface provides the intuition: straight-line distance through the surrounding space can differ from distance along the surface. For ultrasound representations, I would treat this as a modeling assumption. A smooth-looking embedding does not establish that disease progression follows a single continuous path.

### Encoded information and decision reliance are different

If a probe can predict the scanner from a representation, scanner information is recoverable by that probe. That result does not establish that the diagnostic output depends on it. Conversely, a failed linear probe only limits what that particular probe recovered; information may remain available through nonlinear relationships. I need to connect representation analysis to the classifier's output, then ask whether controlled changes to suspected acquisition information alter its decisions.

### Coordinate systems and projections limit interpretation

Feature coordinates are not automatically comparable across independently trained networks. A shared orthogonal rotation preserves pairwise Euclidean distances and cosine similarities while changing individual coordinates. Representation comparison methods therefore make choices about which transformations to ignore, a concern developed in [Kornblith and colleagues' study](https://proceedings.mlr.press/v97/kornblith19a.html). A two-dimensional projection introduces another limitation: it cannot preserve every relationship in the original space. I would check apparent clusters and separations using the original representations before assigning them clinical meaning.

## Where it touches my work

In gallbladder ultrasound shortcut auditing, I would compare neighborhoods against clinical descriptors and acquisition metadata, with patients kept separate across development and evaluation. I would also inspect whether the same patient's different views remain close and whether clinically similar lesions remain neighbors across devices. These comparisons could identify candidates for a clinical faithfulness audit. Establishing reliance would still require evidence about how the diagnostic output responds, especially when clinical and acquisition factors vary together.

## What I have not resolved

- Which distance preserves clinically relevant differences without making acquisition settings the main source of separation?
- How should I distinguish useful invariance across ultrasound views from the loss of a finding visible in only one view?
- What evidence would justify interpreting a direction in representation space as a clinical factor rather than a correlated mixture?
