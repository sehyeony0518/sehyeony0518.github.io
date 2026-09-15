---
layout: study_note
title: "Invariance and Equivariance: Two Jobs One Network Cannot Do at Once"
description: "Detection asks a network to be blind to translation and to track it, simultaneously. R-FCN's fix and the feature pyramid are both answers to that conflict, and the conflict generalises well past detection."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Neural Networks & Representation"
order: 11
source: "Independent study"
written: true
updated: "2026-09-15"
---

Shift a cat five pixels to the right. The label is still "cat." The bounding box has moved five pixels.

## Core question and definition

Those two sentences describe incompatible requirements, and detection asks for both from one network.

- **Translation invariance**: the output does not change when the input shifts. This is what classification needs, and what pooling and a classification-trained backbone are built to provide.
- **Translation equivariance**: the output shifts *with* the input. This is what localisation needs — a box regressor that ignored translation would be useless.

Formally, for a shift operator $$T_\delta$$: invariance is $$f(T_\delta x) = f(x)$$; equivariance is $$f(T_\delta x) = T_\delta f(x)$$. A backbone pre-trained on ImageNet has been explicitly optimised for the first. Detection then bolts on a head that needs the second, using features that were trained to discard exactly the information it requires.

I think this is the most useful single idea in the detection literature, and it is not really about detection.

## Key concepts

### The conflict explains a speed problem

Two-stage detectors are slow because a per-region head runs hundreds of times per image. The obvious fix — make the shared trunk heavier and the per-region head lighter — had been tried and did not work, and R-FCN's contribution is the diagnosis of *why*.[^rfcn]

The per-region head could not be made light because it was doing the hard part: recovering positional sensitivity from a backbone that had been trained to destroy it. The head was carrying the whole invariance-to-equivariance conversion, so shrinking it broke the detector.

R-FCN's fix is to change what the backbone is asked to learn. Instead of a channel meaning "cat," channels mean **"top-left of a cat," "top-centre of a cat," "bottom-right of a cat"** — a $$k\times k$$ grid of position-sensitive score maps per class. These labels *do* change under translation, by construction, so the backbone is now trained to be equivariant and the conflict is resolved before the head ever runs.

Position-sensitive RoI pooling then samples each grid cell from its own corresponding map — top-left region from the top-left channel, and so on — and averages. A genuine detection has every cell agreeing: yes, I am the top-left of a cat; yes, I am the centre. A shifted box fails cell by cell. The per-region computation becomes a pooling operation and an average, with no learned parameters, which is exactly the lightening that had been impossible.

The vote-counting structure is what makes it work: the head is cheap because the backbone already did the discrimination, and the backbone could do it because the labels were redefined to be equivariant.

### Feature pyramids answer a different half

The second structural problem is scale: finding a small object needs fine resolution, and identifying it needs the semantic depth that only comes after downsampling. One feature map cannot supply both.

The design space has four points, and each corresponds to a detector:

| approach | structure | detector |
|---|---|---|
| image pyramid | resize input, run detector at each scale | classical; too slow to train |
| single deep map | predict only from the final layer | YOLO v1 |
| pyramidal features | predict from each level independently | SSD |
| feature pyramid | top-down path merges deep semantics into shallow maps | FPN |

FPN's move is the top-down path.[^fpn] Deep, semantically strong, spatially coarse features are upsampled $$2\times$$ and added to shallower maps, which pass through a $$1\times1$$ convolution first to reconcile channel counts. Every level of the resulting pyramid is both fine-grained and semantically informed.

The intuition the lecturer offered is the right one: segmenting an object well requires looking closely *and* stepping back, repeatedly. Neither view alone is enough, and the top-down path is how you give a network both. That is why FPN shows up in Mask R-CNN and far beyond detection[^mask] — it answers a question about multi-scale evidence, not a question about boxes.

### What the controlled comparison found

By 2017 the field had a real problem: architectures, backbones, training data and input resolutions all varied together across papers, so no reported difference could be attributed to any one of them. A controlled study — holding backbone and data fixed, varying only the meta-architecture — was needed to say anything.[^huang]

Its finding: Faster R-CNN leads on accuracy, SSD leads in the fast regime, R-FCN sits between, and a substantial share of what earlier tables credited to architecture was backbone and data. Meanwhile YOLO v2's own ablation shows batch normalisation and high-resolution fine-tuning — neither of them architectural — accounting for several mAP points each.

I find that a healthier reading of the whole literature than a ranking. The comparisons that changed my mind were the ones that held things fixed.

## Why it matters for my work

The invariance/equivariance conflict names something I keep running into without a vocabulary for it. **A model trained for one kind of insensitivity cannot be assumed to retain the sensitivity a different task needs**, and transfer learning is precisely the practice of assuming otherwise.

The concrete case: a backbone pre-trained on classification has been rewarded for discarding whatever does not change the class label. If I then fine-tune it to localise a lesion, I am asking features selected for positional blindness to support a positional judgement. Where it succeeds, it succeeds because fine-tuning partially undid the pre-training — and where it fails, the failure looks like insufficient data rather than like a representation that was optimised against the task.

There is a sharper version for [faithfulness](/study/explanation-faithfulness-versus-plausibility/). Attribution maps assume a spatial correspondence between features and input locations — that a high-attribution region means the model used evidence *there*. In a network trained toward invariance, that correspondence is exactly what training worked to weaken. R-FCN is the existence proof: it took an explicit architectural intervention, redefining the labels, to make features positionally meaningful. A saliency map drawn over an invariance-trained backbone is asserting a positional semantics the representation was never built to have.

And the philosophical objection the lecturer raised is worth keeping. Is invariance even what we want? A model that reports "cat" identically regardless of where the cat is has discarded information that, in a clinical image, is often the diagnosis — a finding's location relative to anatomy frequently *is* the evidence. Invariance is not neutral. It is a decision about what may be ignored, made once, at pre-training time, by someone solving a different problem.

## What I have not resolved

Whether the position-sensitive trick generalises usefully to medical detection, where "top-left of a lesion" may be a far less stable concept than "top-left of a cat" — lesions lack canonical orientation, and the grid-cell voting scheme leans on there being a consistent one.

---

[^rfcn]: Dai, J., Li, Y., He, K., & Sun, J. (2016). R-FCN: Object detection via region-based fully convolutional networks. *NeurIPS*. [arXiv:1605.06409](https://arxiv.org/abs/1605.06409)

[^fpn]: Lin, T.-Y., Dollár, P., Girshick, R., He, K., Hariharan, B., & Belongie, S. (2017). Feature pyramid networks for object detection. *CVPR*. [10.1109/CVPR.2017.106](https://doi.org/10.1109/CVPR.2017.106)

[^mask]: He, K., Gkioxari, G., Dollár, P., & Girshick, R. (2017). Mask R-CNN. *ICCV*. [10.1109/ICCV.2017.322](https://doi.org/10.1109/ICCV.2017.322)

[^huang]: Huang, J., et al. (2017). Speed/accuracy trade-offs for modern convolutional object detectors. *CVPR*. [10.1109/CVPR.2017.351](https://doi.org/10.1109/CVPR.2017.351)
