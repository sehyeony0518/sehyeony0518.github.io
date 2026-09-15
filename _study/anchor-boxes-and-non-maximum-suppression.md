---
layout: study_note
title: "Anchor Boxes and Non-Maximum Suppression: Where the Priors Are Hidden"
description: "A detector predicts corrections to reference boxes it was handed, and then deletes most of its own output. Both steps are hand-chosen priors that no accuracy number reports."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Neural Networks & Representation"
order: 10
source: "Independent study"
written: true
updated: "2026-09-15"
---

A one-stage detector emits thousands of boxes and keeps a handful. What happens between those two facts is where most of the engineering lives, and almost none of it is learned.

## Core question and definition

Asking a network to output an arbitrary box at an arbitrary location is asking it to regress unbounded coordinates — a target whose scale depends on image size, object size, and position all at once. **Anchor boxes** replace that with a bounded question: here is a reference box of known size and aspect ratio; tell me how this object differs from it.[^fasterrcnn]

The reference set is chosen in advance. SSD assigns each feature map a scale and a set of aspect ratios $$r \in \{1, 2, \tfrac12, 3, \tfrac13\}$$, and constructs anchors of width $$s\sqrt{r}$$ and height $$s/\sqrt{r}$$ — which preserves area at $$s^2$$ while varying shape, so that ratio and scale are genuinely independent knobs. At $$s=21$$ the $$1{:}1$$ anchor is $$21\times21$$ and the $$2{:}1$$ anchor is $$29.70\times14.85$$, both of area 441. An extra square anchor at $$\sqrt{s_k s_{k+1}}$$ — $$\sqrt{21\cdot45} = 30.74$$ — fills the gap between consecutive scales, which is why some maps carry 4 anchors and others 6.[^ssd]

The shallower, higher-resolution maps get small anchors and the deeper ones get large anchors. That is the whole of SSD's multi-scale idea: a feature map's receptive field determines what size of object it can see, so match the anchor to the map.

## Key concepts

### The network predicts corrections, not coordinates

Because a fully convolutional head is translation-shared, the same filter runs at every spatial site — so it cannot output an absolute position. It outputs an offset, and the site supplies the origin.

SSD's encoding is:

$$
\hat g^{cx} = \frac{g^{cx} - d^{cx}}{d^{w}}, \qquad
\hat g^{cy} = \frac{g^{cy} - d^{cy}}{d^{h}}, \qquad
\hat g^{w} = \log\frac{g^{w}}{d^{w}}, \qquad
\hat g^{h} = \log\frac{g^{h}}{d^{h}}
$$

where $$d$$ is the anchor and $$g$$ the ground truth. Centres are expressed as a fraction of anchor size; sizes as a log ratio. Decoding inverts it: $$g^{cx} = d^{cx} + d^{w}\hat g^{cx}$$ and $$g^{w} = d^{w}\exp(\hat g^{w})$$.

Two things are worth drawing out. The log on width and height makes the target symmetric under doubling and halving — predicting $$+0.69$$ and $$-0.69$$ are equally sized errors, whereas in raw pixels a factor of two is a different magnitude for a small box than a large one. And **the loss function is where the decoding is decided**: writing the regression target as $$\hat g$$ commits you to interpreting the network's output as $$\hat g$$ forever after. The decoder is not a separate design choice; it is the loss read backwards.

The variance scaling factors that appear in reference implementations have, as far as I can find, no justification in the paper beyond empirical tuning.

### Non-maximum suppression deletes most of the output

One object produces many firing anchors — a person is detected by the anchor centred on their torso, the one on their head, and several neighbours. So after thresholding on confidence (which removes the overwhelming majority of the 8732 boxes), overlapping survivors must be merged.

NMS is greedy: sort by score, take the highest, delete everything overlapping it beyond an IoU threshold, repeat on what remains.

The important detail is that it is applied **per class**. A person holding a dog produces two heavily overlapping boxes that are both correct, so suppression across classes would destroy one. Within a class it is a hard constraint, and the consequence is exact and unavoidable: **two people standing closer than the IoU threshold cannot both be detected.** With a 0.5 threshold, two same-size boxes must be separated by more than a third of a box-width or one of them is deleted — not scored low, deleted, by a rule with no parameters that were learned from data.

This is a failure mode built into the post-processing rather than the model, and no amount of training data removes it.

### Learning the anchors instead of choosing them

YOLO v2 replaced hand-chosen ratios with **dimension priors**: run $$k$$-means over the ground-truth boxes in the training set and use the cluster centroids as anchors. Five clusters was the chosen trade-off between count and accuracy.[^yolo9000]

That is a genuine improvement in honesty — the priors now come from the data rather than from the authors' intuition — and the paper's ablation table is the useful part of it. Anchors alone *reduced* mAP while raising recall; anchors plus dimension priors plus direct location prediction raised both. The lesson I take is that the components were not independent, and reporting any one of them alone would have been misleading.

The box budgets tell the trajectory plainly: YOLO v1 predicted $$7\times7\times2 = 98$$ boxes; v2 predicted $$13\times13\times5 = 845$$; v3, across three scales, predicts $$(13^2 + 26^2 + 52^2)\times3 = 10{,}647$$.[^yolov3]

### Softmax versus sigmoid, which is a claim about the world

YOLO v3 replaced the class softmax with independent sigmoids. The reason is not numerical.

Softmax asserts that the classes are mutually exclusive — the scores sum to one, so evidence for one class is evidence against every other. That is true for "dog or cat" and false for "woman and person," or "tree and conifer," where an object legitimately carries several labels at once. Sigmoid per class drops the exclusivity assumption and asks each question independently.

Choosing between them is choosing a claim about the label space, not a layer.

## Why it matters for my work

The anchor set is a **prior about object geometry that is fixed before training and invisible afterwards.** SSD's ratios were selected because they worked best among the options tried; nothing in the resulting mAP distinguishes "the model learned this object well" from "the anchor set happened to fit this object's shape."

For medical imaging this is not a small point. Lesion shape distributions are not the VOC distribution, and a detector inheriting COCO-tuned anchors starts with a geometric prior fitted to cars and people. The $$k$$-means approach is the right instinct — but it makes the prior a function of the training set, which means a detector trained at one institution carries that institution's lesion-size distribution as a structural bias, not merely a statistical one. When it underperforms elsewhere, [external validation](/study/robustness-subgroup-performance-and-external-validation/) will show the drop and will not say that the anchors were the cause.

The NMS point is sharper still, because it is the clearest case I know of a **clinically relevant failure that is provably not in the model**. If two adjacent lesions are closer than the IoU threshold, one is deleted after inference, deterministically. Attribution methods will not show it; the model's own confidence for the deleted box was high. Auditing the model cannot find a fault that lives in the post-processing, which argues for treating the inference pipeline — not the network — as the object under audit.

## What I have not resolved

Whether soft-NMS or the learned alternatives change this in practice or only soften it, and whether any of them have been evaluated on the adjacent-lesion case specifically rather than on aggregate mAP, where a handful of deleted boxes is invisible.

---

[^fasterrcnn]: Ren, S., He, K., Girshick, R., & Sun, J. (2017). Faster R-CNN: Towards real-time object detection with region proposal networks. *IEEE TPAMI*, 39(6), 1137–1149. [10.1109/TPAMI.2016.2577031](https://doi.org/10.1109/TPAMI.2016.2577031)

[^ssd]: Liu, W., et al. (2016). SSD: Single Shot MultiBox Detector. *ECCV*. [10.1007/978-3-319-46448-0_2](https://doi.org/10.1007/978-3-319-46448-0_2)

[^yolo9000]: Redmon, J., & Farhadi, A. (2017). YOLO9000: Better, faster, stronger. *CVPR*. [10.1109/CVPR.2017.690](https://doi.org/10.1109/CVPR.2017.690)

[^yolov3]: Redmon, J., & Farhadi, A. (2018). YOLOv3: An incremental improvement. [arXiv:1804.02767](https://arxiv.org/abs/1804.02767)
