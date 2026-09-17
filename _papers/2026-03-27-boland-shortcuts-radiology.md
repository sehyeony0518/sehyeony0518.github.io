---
layout: post
title: "There Are No Shortcuts to Anywhere Worth Going: Identifying Shortcuts in Deep Learning Models for Medical Image Analysis"
date: 2026-03-27 12:00:00 +0900
venue: "MIDL 2024"
authors: "Christopher Boland, Keith A. Goatman, Sotirios A. Tsaftaris, Sonia Dahdouh (2024)"
description: "A method for locating which layer of a network a shortcut's features actually manifest in, using Prediction Depth and KL divergence, moving from 'the model has a shortcut' to 'here is where in the network it lives.'"
og_image: "https://sehyeony0518.github.io/assets/img/og/2026-03-27-boland-shortcuts-radiology.png"
related_posts: false
---

**Paper.** *There Are No Shortcuts to Anywhere Worth Going: Identifying Shortcuts in Deep Learning Models for Medical Image Analysis*. [MIDL paper](https://proceedings.mlr.press/v250/boland24a.html)

## Why locating a shortcut is an open question

A performance drop after removing an artifact can establish that something about the intervention mattered. It does not show where the corresponding information became useful inside the network. Conversely, finding that an artifact is decodable from an early layer does not establish that the diagnostic head depends on it.

This paper investigates an intermediate question: can changes in the depth at which examples become predictively separable help locate shortcut-related computation? That is useful because mitigation methods sometimes target early layers on the assumption that shortcuts are simple, superficial features.

For medical imaging, the assumption is questionable. A corner marker and a treatment device can both support an inappropriate diagnostic rule while requiring different visual processing. The clinically inappropriate nature of a feature does not determine its computational complexity.

## What the authors actually compare

The experiments use Waterbirds, CheXpert pneumothorax classification, and ISIC skin-lesion classification. Controlled shortcuts include squares at fixed or varying locations and a more complex curved object. Matched architectures are trained with and without the introduced class-correlated shortcut, then evaluated on the same test set with the shortcut balanced across classes.

Prediction depth is calculated using nearest-neighbor probes at successive layers. It is the depth after which subsequent probes agree on the prediction. The authors compare prediction-depth distributions and examine individual contributions to their KL divergence, then inspect examples associated with prominent differences. [Methods and experiments](https://openreview.net/pdf/3c6888b96f569bccf12925981f91ed4bc7d9a6d0.pdf)

Holding the evaluation images fixed is essential to the interpretation. Otherwise, a shift in prediction depth could simply reflect a different case mix. Comparing corresponding training conditions also makes the inserted shortcut a concrete experimental factor.

However, the original medical datasets serve as controls for the added artifacts. Calling those controls “clean” should not imply that every naturally occurring acquisition shortcut has been excluded.

## What prediction depth means

I find the method easiest to interpret as a description of when a particular probing procedure can settle an example's class. An example resolved early may have an easily accessible cue. An example resolved later may require additional feature transformations.

That interpretation has boundaries. Probe predictions are not the network's internal decisions made visible. The original model does not necessarily classify by nearest neighbors at every layer. Its final head can combine information differently.

Depth also depends on the architecture and where probes are attached. A numerical layer index is not a universal measure of semantic abstraction across networks. Comparisons are most convincing within a defined architecture and probe protocol.

KL divergence adds a contrast against a reference distribution. It can highlight a layer that would be overlooked by inspecting the largest raw prediction-depth peak. But a large divergence contribution does not, on its own, identify the particular feature responsible. The controlled shortcut construction supplies much of that interpretation.

## What the results support

The experiments associate simpler shortcuts with earlier manifestations and larger performance damage, while more complex shortcuts can appear deeper. The paper also finds that optimization settings affect the observed behavior. [Results](https://proceedings.mlr.press/v250/boland24a.html)

The useful conclusion is that shortcut localization should not be restricted to the first few layers. A late shortcut signature is entirely compatible with an inappropriate decision rule.

I would resist turning this into a universal hierarchy in which squares are always learned first and devices always appear late. Visibility, location, size, training correlation, competing disease evidence, and architecture all affect accessibility. Visual complexity is an experimental dimension here, not a complete explanation of shortcut strength.

The relationship between complexity and harm is also conditional on the available alternative rule. A shortcut may dominate because it is easy, because the clinical signal is weak, or because the training sample makes it unusually reliable. Those mechanisms can coexist.

## The main weakness

The strongest limitation is the dependence on a meaningful reference model and controlled shortcut contrast. In an actual hospital dataset, I may not have an otherwise comparable training set from which the suspicious acquisition effect has been removed.

An observed layer difference between two independently trained models can reflect more than one representational change. Even with matched settings, retraining changes many parameters. Localization therefore identifies a promising place to investigate, rather than proving that one layer uniquely contains the shortcut mechanism.

The divergence threshold also needs careful language. Selecting unusually large layer contributions is a localization heuristic. It should not automatically be interpreted as a calibrated statistical test of a causal mechanism.

Grad-CAM inspection can help recognize what selected examples share, but this adds another measurement with its own assumptions. A plausible artifact-focused heatmap strengthens a hypothesis; it does not make the probe and divergence analysis a causal intervention.

## What would make the finding actionable

Layer localization is a starting point rather than a result. What it produces is a hypothesis about where a cue is represented, and a hypothesis of that kind has to be tested against the model's actual behaviour before it supports any claim about what the model uses. The paper does not carry that step, and the gap between the two is where most of the difficulty sits.

If a representation direction or channel were suppressed, I would also test whether clinically relevant information was damaged. A layer can encode both acquisition and anatomy. Broad suppression could improve one counter-shortcut benchmark while impairing subtle disease recognition.

The most useful audit record would connect three observations for the same cases: the input intervention, the layerwise response, and the original head's response. Agreement among them would be more informative than any isolated layer plot.

## Connections to the study notes

[Representation-Level Auditing](/study/representation-level-auditing/) distinguishes recoverability, representation change, and downstream use. This paper adds a depth-sensitive measurement to the first two. It supports examining multiple layers, while reinforcing the need to keep probe behavior separate from the original classifier.

[Intervention-Based Auditing](/study/intervention-based-auditing/) supplies the next step. A localization result can guide where to intervene, but the intervention must specify what changes and what information should remain intact.

[Spurious Correlations in Medical AI](/study/spurious-correlations-in-medical-ai/) separates a cue's predictive opportunity from its actual use. Boland's controlled designs help bridge those questions because the cue-label relationship is manipulated explicitly. Natural clinical confounding offers fewer guarantees.

For my own work, the paper suggests a concrete role for layer analysis: prioritize hypotheses and interventions. I would treat an emergence layer as a useful experimental lead, then require behavioral evidence before claiming that the relevant shortcut has been identified or removed.
