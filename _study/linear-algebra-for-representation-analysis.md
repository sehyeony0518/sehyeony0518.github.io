---
layout: page
title: "Linear Algebra for Representation Analysis"
description: "Eigenvalues, SVD, projection, and PCA, and why they are the working tools for asking what a learned representation actually contains."
section: "F"
section_title: "Mathematical and Statistical Foundations"
branch: "Branch 01"
order: 1
written: true
---

Linear algebra lets me describe a learned representation as a collection of directions, combinations, and subspaces. Eigenvalues, singular value decomposition, and projection turn “the model encodes this” into a more specific question about variation and recoverable structure.

## Why it matters here

A medical image representation contains more than the information needed for its diagnostic label. Clinical findings, patient anatomy, and acquisition characteristics can vary together. Linear algebra provides tools for separating directions of variation, but a mathematical decomposition does not automatically separate their clinical causes.

For clinical faithfulness auditing, I need to understand what a representation analysis actually measures. A component associated with lesion size might also track image magnification. Before naming that component clinically, I would examine how it was constructed, which patients determined it, and whether the association survives a change in acquisition setting.

## The core ideas

### A representation matrix makes the analysis explicit

I can arrange feature vectors into a matrix X, with observations in rows and features in columns. The meaning of an observation matters: a frame, examination, and patient are different units. Column centering subtracts each feature's mean, while standardization also changes its scale. These choices alter the decomposition. If one patient contributes many similar frames, that patient can disproportionately determine the variation I later describe as characteristic of the dataset.

### Eigenvalues describe variation along particular directions

An eigenvector of a square matrix is a direction that the matrix maps to a scalar multiple of itself; the multiplier is its eigenvalue. For a sample covariance matrix, eigenvectors can be chosen orthonormal, and eigenvalues describe the variance along them. Large eigenvalues identify substantial variation, not necessarily useful diagnostic evidence. Nearly equal eigenvalues also make individual directions harder to interpret consistently: the associated subspace can remain stable while its chosen axes change.

### SVD connects the data matrix to its covariance

The singular value decomposition writes X as UΣVᵀ, separating observation patterns, nonnegative singular values, and feature directions. For centered X with n observations, the eigenvalues of XᵀX/(n-1) are the squared singular values divided by n-1. This connects SVD directly to covariance-based analysis without requiring X to be square. Retaining the largest singular values gives a best approximation of a chosen rank under squared reconstruction error, but that criterion does not know which clinical information matters.

### Projection selects a subspace and leaves a residual

For a column vector z and a matrix Q with orthonormal columns, QQᵀz is its orthogonal projection onto the subspace spanned by Q. The remaining vector is orthogonal to that subspace. This makes projection useful for examining candidate clinical or acquisition directions. Orthogonality, however, does not imply statistical independence. Removing a direction associated with scanner identity may leave scanner information elsewhere, or remove clinical information that shared the same direction.

### PCA prioritizes variance rather than diagnostic relevance

Principal component analysis applies these ideas to find successive orthogonal directions of greatest variance in centered data. Component scores locate observations along those directions; loadings describe how the original features contribute. A low-variance direction can still discriminate an important clinical subgroup. I would fit preprocessing and PCA on the development data, then apply the fixed transformation to held-out patients. Choosing components after inspecting evaluation labels would compromise the independence of the analysis.

## Where it touches my work

For gallbladder ultrasound, I would examine principal component scores alongside lesion descriptors, image depth, device identity, and patient membership. I would also compare what a diagnostic probe recovers before and after projection, with the probe fitted separately from its evaluation. These analyses could identify a subspace worth investigating in a shortcut audit. A change in the frozen classifier's output after projection would require further interpretation, because the altered representation may no longer correspond to a plausible ultrasound image.

## What I have not resolved

- When eigenvalues are similar, should I report associations with an entire subspace instead of assigning meaning to individual components?
- How can I remove acquisition-related variation without discarding clinical information that is correlated with it?
- Which reconstruction errors matter clinically when a small residual may contain the finding relevant to a rare diagnosis?
