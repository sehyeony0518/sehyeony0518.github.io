---
layout: post
title: "Breast Tumor Classification of Ultrasound Images Using Wavelet-Based Channel Energy and ImageJ"
date: 2026-02-22 12:00:00 +0900
venue: "IEEE JSTSP"
authors: "Hsieh-Wei Lee, Bin-Da Liu, King-Chu Hung, Sheau-Fang Lei, Po-Chin Wang, Tsung-Lung Yang (2009)"
description: "A pre-deep-learning approach to breast-ultrasound CAD: hand-engineered wavelet channel-energy features meant to capture how infiltrative a lesion's margin looks, a useful reminder of what feature engineering used to make explicit."
related_posts: false
---

**Paper.** *Breast Tumor Classification of Ultrasound Images Using Wavelet-Based Channel Energy and ImageJ.*

The paper asks whether an explicit multiscale description of a lesion contour can help distinguish benign and malignant breast tumors in ultrasound images. Its motivation is clinically recognizable: the shape and local irregularity of a boundary may contain diagnostic information. The engineering question is how to turn that qualitative observation into a reproducible feature rather than leaving it as an unspecified impression.

This is useful to read alongside deep learning because it exposes the assumptions between image and prediction. A contour must first be obtained. It must then be represented as a signal, transformed, and summarized. Each step makes choices about which variation is retained. The final classifier may be simple, but its input is already the product of a substantial measurement process.

The method represents a lesion boundary as a one-dimensional signal and analyzes it using a discrete periodized wavelet transform. The proposed channel-energy features summarize contour variation at selected scales. The authors describe informative high-octave energies as channels close to low-frequency bands. That terminology should not be casually rewritten as “high-frequency texture”: the signal being analyzed is a contour representation, not the complete ultrasound image.

The reported performance differs between manual and ImageJ-generated contour settings. For the manual setting, AUC is 0.991, accuracy 0.951, sensitivity 0.985, and specificity 0.933. For the ImageJ setting, AUC is 0.934 and accuracy 0.844. These values support the usefulness of the descriptor under the evaluated conditions and highlight the importance of how the contour enters the pipeline.

The existing review does not document the exact sample size, patient grouping, split procedure, or whether every reported contour comparison used precisely matched cases and evaluation choices. I would verify those details before treating the numbers as a fully controlled estimate of the effect of replacing manual segmentation. The observed performance gap is informative, but assigning its entire magnitude to contour quality requires that the other relevant conditions be comparable.

The strongest aspect of the approach is its inspectable intermediate representation. If a case receives a high score, a reader can examine the boundary, the resulting signal, and the scales contributing energy. That makes it possible to ask a specific question about failure. Did the segmentation miss part of the lesion, did a sampling choice exaggerate a small irregularity, or did the descriptor fail to distinguish two clinically different shapes?

Nevertheless, inspectability does not automatically establish clinical faithfulness. Wavelet energy measures variation under a chosen signal representation. Calling that energy an infiltration measure requires evidence that it corresponds to the intended pathological or imaging property. A contour can be irregular for several reasons, including delineation choices and image quality. The method's clinical motivation is a hypothesis about the feature, not a guarantee that every large value has the same biological meaning.

Manual contours also contain human input that should remain visible in the performance claim. A reader may use subtle image evidence when deciding where the lesion ends. The downstream classifier then receives a boundary informed by that judgment. High classification performance conditional on such a boundary does not establish equivalent performance when a routine system must first locate and delineate the lesion automatically.

This is the main weakness I would raise: the diagnostic score is conditional on the upstream measurement, and that measurement can carry both error and expert information. Reporting only the best contour-conditioned result risks attributing the whole pipeline's performance to the final feature. The ImageJ comparison makes the issue visible, but it does not remove the need to characterize segmentation failures and their consequences.

A modern replication should examine contour uncertainty directly. I would compare multiple plausible reader contours and controlled boundary variations, then measure how much the diagnostic score changes. The perturbations would need to reflect plausible delineation differences. Arbitrarily jagged boundaries could make any contour descriptor appear fragile without representing actual annotation uncertainty.

Spatial scale is another important consideration. A one-dimensional sampled contour depends on how points are spaced and how the shape is normalized. Resampling can alter which variations occupy particular wavelet bands. Before transferring a trained decision rule, I would preserve and report those choices. A transparent feature definition still needs a stable measurement convention.

The method also captures only part of the information available in breast ultrasound. A useful contour descriptor does not establish that other findings are redundant. Conversely, a neural model that improves over it might gain from additional image information rather than a superior representation of the same contour. A fair comparison should state whether the competing methods have access to equivalent inputs.

This paper connects directly to [Representation-Level Auditing]({{ '/study/representation-level-auditing/' | relative_url }}), especially its argument that frequency needs spatial meaning. Here, frequency refers to variation along a constructed boundary signal. It cannot be interpreted interchangeably with image-frequency content or a network's internal spectral behavior. Naming the signal is necessary before assigning meaning to its bands.

[Clinical Concepts and Concept-Based Interpretability]({{ '/study/clinical-concepts-and-concept-based-interpretability/' | relative_url }}) provides another useful caution. A measurable proxy for a named concept is valuable, but the proxy and concept are not identical by definition. [Ultrasound Acquisition Variability and Image Quality]({{ '/study/ultrasound-acquisition-variability-and-image-quality/' | relative_url }}) explains why the boundary itself depends on whether the relevant interface remains assessable.

BUS-BRA offers a natural resource for investigating these questions with explicit patient partitions and reference masks. I would compare contour-based classification using reference and predicted masks, report the performance of the complete automatic pipeline, and retain cases where a contour cannot be obtained reliably. I would also compare against simple geometric descriptors before concluding that the wavelet representation adds useful information.

The lasting value of the paper is its explicit evidence path. It provides a baseline against which a more complex model can be asked to justify its benefit. That benefit should be measured under comparable inputs and realistic upstream uncertainty. A legible final score becomes useful when the measurement feeding it is equally well characterized.
