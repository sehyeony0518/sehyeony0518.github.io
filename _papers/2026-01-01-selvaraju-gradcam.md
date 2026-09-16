---
layout: post
title: "Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization"
date: 2026-01-01 12:00:00 +0900
venue: "ICCV"
authors: "Selvaraju, Cogswell, Das, Vedantam, Parikh, Batra (2017)"
description: "The saliency method almost every medical-imaging paper cites, and a good place to be precise about what its heatmap actually certifies."
related_posts: false
---

**Paper.** *Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization.*

Grad-CAM asks how to obtain a class-specific spatial explanation from an already trained convolutional network without changing its architecture. Earlier class activation mapping imposed architectural restrictions, while detailed gradient visualizations could emphasize image structure without clearly distinguishing the target class. The open problem was therefore practical as well as conceptual: produce a useful localization interface for a wider range of existing predictors.

That framing matters because the paper introduces a visualization method, not a clinical lesion detector. Its original experiments concern natural-image recognition and related vision tasks. Medical applications inherit a computational procedure from the paper, but they must supply their own evidence that its outputs answer a medical question. A heatmap over a radiograph does not acquire a clinical interpretation merely because the underlying classifier predicts a diagnosis.

For a target score $$y^c$$ and convolutional feature maps $$A^k$$, Grad-CAM averages the score gradients spatially to obtain one weight per channel. It then forms a weighted combination of the feature maps and applies a rectifier:

$$
\alpha_k^c=\frac{1}{Z}\sum_{i,j}\frac{\partial y^c}{\partial A_{ij}^k},
\qquad
L^c=\operatorname{ReLU}\left(\sum_k\alpha_k^c A^k\right).
$$

The result is a coarse map at the selected layer's spatial resolution. The authors also combine it with guided backpropagation to produce Guided Grad-CAM, a visually more detailed output.

The original evaluation includes weakly supervised object localization, comparisons between target classes, demonstrations of dataset bias, and human studies of model assessment. These experiments support the method's usefulness as an interface for investigating spatial focus. The important control is that the predictor can remain fixed while the explanatory target or visualization method changes. Generating the map does not require training a new lesion-localization head.

The equation gives several limits directly. Spatially averaging the gradients compresses potentially different local sensitivities into a single channel weight. The final feature maps may be much smaller than the input image. Upsampling makes the output easier to display, but it does not restore spatial information that the map never represented. Applying the rectifier also means that the usual display emphasizes positive support and discards negative values in the weighted combination.

These properties affect what a red region means. It is a location with a large value under this particular combination of features and target-conditioned gradients. It is not a probability that a lesion occupies the location, and it is not an estimate of how much removing those pixels would change the diagnosis. The selected score also matters: a class logit, a probability, and a contrast between classes can produce different gradients. An explanation report should identify the quantity it explains.

For ultrasound, coarse localization can conceal the distinction I actually care about. A map centered on the gallbladder may be compatible with reliance on its wall, a nearby annotation, posterior acoustic behavior, or a broad acquisition pattern. Anatomical overlap narrows the investigation but does not identify the diagnostic feature. A spatially plausible answer can therefore remain inadequate for a claim about clinical evidence use.

The most substantial weakness is the gap between a readable visualization and a validated explanation claim. The original localization and user studies are informative for their tasks, but they do not show that Grad-CAM reliably detects all shortcuts or identifies necessary clinical findings. Later work in this corpus, particularly Arun and colleagues' saliency evaluation, makes clear why each proposed use needs its own test. That does not justify attributing every failure of every saliency method to Grad-CAM specifically.

A localization claim should be tested against independent localization annotations, with the conversion from heatmap to region specified in advance. A model-dependence claim calls for checks that alter the learned predictor. A reliance claim requires observing how predictions respond to a justified change in evidence. These tests address different questions. Passing a weight-randomization check, for example, is necessary evidence of model dependence in that setting, but it does not establish that the highlighted structure is the clinically intended one.

Perturbation testing also needs care. Covering a bright region with a black rectangle may introduce an unfamiliar artifact, erase several findings at once, or alter surrounding context. A large score change would then establish sensitivity to that edit, not necessarily dependence on the named lesion. I would compare targeted edits with matched control edits and inspect whether the relevant clinical information remains assessable.

This paper is a direct companion to [Attribution, Attention, and Counterfactual Explanations]({{ '/study/attribution-attention-and-counterfactual-explanations/' | relative_url }}). That note separates gradients, attention coefficients, allocated score differences, and prediction-changing edits. Grad-CAM illustrates why visually similar overlays can represent different mathematical quantities. Guided Grad-CAM should also be identified explicitly rather than treated as a higher-resolution version with automatically identical explanatory guarantees.

It further supports [Explanation Faithfulness versus Plausibility]({{ '/study/explanation-faithfulness-versus-plausibility/' | relative_url }}). Human agreement with a highlighted region measures a different property from agreement with the predictor's actual computation. [Intervention-Based Auditing]({{ '/study/intervention-based-auditing/' | relative_url }}) supplies the next step: turn an apparent focus into a named dependency that can be challenged through a controlled experiment.

In my work, I would retain Grad-CAM as an inexpensive first inspection. I would freeze the layer, target score, normalization, and display convention before comparing groups or methods, and include failures and controls rather than selecting only attractive examples. Its useful output is a more specific research question: which evidence might this model be using, and what experiment would distinguish that explanation from alternatives? The original method makes that investigation accessible. It does not complete the clinical validation of the explanation.
