---
layout: post
title: "Regression Concept Vectors for Bidirectional Explanations in Histopathology"
date: 2026-01-20 12:00:00 +0900
venue: "MICCAI 2018 Workshop"
authors: "Mara Graziani, Vincent Andrearczyk, Henning Müller (2018)"
description: "An extension of TCAV to continuous, graded concepts: used to show that nuclei texture, not just its presence, is a directional driver of tumor-grade predictions in lymph-node histopathology."
og_image: "https://sehyeony0518.github.io/assets/img/og/2026-01-20-regression-concept-vectors-histopathology.png"
featured: true
related_posts: false
---

**Paper.** *Regression Concept Vectors for Bidirectional Explanations in Histopathology.*

The paper asks how to explain a network using a concept that has a measurable degree, rather than a binary presence label. This is a natural question in medicine. Nuclear area, texture, lesion irregularity, and tissue density are quantities for which “more” and “less” may be more informative than “present” and “absent.” A binary concept classifier can discard that structure.

The setup extends the idea behind concept activation vectors. A concept direction connects a named property to a direction in an internal representation. The open issue is how to obtain that direction from continuous measurements and preserve the sign and consistency of the network's response. The paper proposes Regression Concept Vectors, or RCVs, together with a bidirectional relevance summary.

The experiment should be described precisely. Although histological grading motivates the concepts, the evaluated network classifies patches as tumor or non-tumor. It is not a demonstrated system for predicting an ordinal tumor grade. The authors train a ResNet101 using Camelyon16 and Camelyon17 patches. A separate nuclei-annotation dataset supplies 300 breast-tissue patches for concept measurements, and sensitivity analysis uses 300 Camelyon17 patches. These sets serve different roles and should not be collapsed into a single training cohort.

For a frozen network, a linear regression predicts a concept measurement from activations at a chosen layer. Its coefficient vector supplies the RCV. The directional derivative of the diagnostic output along that vector measures local sensitivity. The proposed relevance score combines regression fit with the mean sensitivity relative to its variability. Thus, a concept direction is assessed both for how well it represents the measured concept and for how consistently movement along it relates to the output.

The reported analysis identifies nuclear texture contrast and correlation as relevant measurements. The output association reported for contrast is approximately 0.41 using Pearson correlation, not Spearman correlation. The sensitivity analysis also distinguishes directions associated with increasing tumor output from those associated with decreasing output. Repeated analyses and comparisons across layers are more informative than presenting one concept vector as a fixed property of the entire network.

The key contribution is the separation of three questions that are easy to conflate. First, does the measured concept associate with the diagnostic output across images? Second, can a linear probe recover the concept from an internal representation? Third, is the downstream output locally sensitive along the estimated concept direction? These questions concern different objects. A positive answer to one is not a substitute for the others.

For example, a representation can contain information about nuclear area even if the final classifier ignores it. Conversely, a concept and prediction can be associated because both track another property of the tissue. Neither observation alone establishes diagnostic reliance. The directional derivative adds a model-conditioned quantity, but its interpretation still depends on whether the fitted direction actually corresponds to the intended concept.

That is the main weakness I would raise. A regression coefficient points in a direction that predicts a measurement under the observed data. Moving activations along that direction need not correspond to a realizable image in which only that measurement changes. Texture, stain, morphology, tissue composition, and acquisition effects can be correlated. The direction may combine them, even when its clinical name refers to only one.

The word “bidirectional” also needs a bounded interpretation. Positive and negative sensitivity describe the direction of local output change along the estimated vector. They do not establish two-way clinical causation, nor do they show that editing nuclei in a real slide would produce the predicted change. The method is an analysis of a learned representation and its downstream computation.

The summary score introduces further choices. A high value can reflect strong concept recoverability, a consistent sensitivity sign, or both. A low average can conceal different patient or tissue subsets with opposing responses. I would therefore inspect the distribution of sensitivities and regression performance separately before interpreting their combination. Reporting only a normalized relevance ranking could make concepts look more directly comparable than the underlying measurements justify.

The small concept dataset is another reason to treat this as a methodological demonstration. Patches from the same slide or patient share information, so patch counts alone do not determine independent evidence. A future implementation should separate concept fitting, model selection, and evaluation at the appropriate patient or slide level. It should also evaluate concept prediction outside the fitted samples; a flexible representation can make in-sample linear recovery look reassuring.

This paper directly extends [Clinical Concepts and Concept-Based Interpretability]({{ '/study/clinical-concepts-and-concept-based-interpretability/' | relative_url }}). The note distinguishes recoverable information, computational sensitivity, and actual use of the intended clinical concept. RCVs enrich the available measurements without collapsing those distinctions. They support continuous concept analysis while complicating the assumption that a clinically named direction has a uniquely clinical meaning.

It is also a practical example for [Representation-Level Auditing]({{ '/study/representation-level-auditing/' | relative_url }}). The layer and probe define what information is accessible, while the fixed diagnostic head determines whether a perturbation reaches the output. [Explanation Faithfulness versus Plausibility]({{ '/study/explanation-faithfulness-versus-plausibility/' | relative_url }}) explains why agreement with familiar pathology concepts is encouraging but insufficient to establish the stronger reliance claim.

For ultrasound, I would consider continuous measurements only after defining how they are observed and how reliably they can be annotated. A wall-thickness or irregularity concept would need a specified view, spatial scale, and assessability rule. I would evaluate probe generalization, compare correlated candidate concepts, inspect subgroup sensitivity distributions, and seek controlled image-level tests that preserve other evidence.

The useful lesson is that concept explanations can become more quantitative without becoming automatically causal. RCVs provide a way to ask whether a frozen model responds along directions associated with measured clinical properties. Their strongest role in my work would be to generate and refine specific hypotheses about representation and reliance, followed by independent tests of what those directions mean.
