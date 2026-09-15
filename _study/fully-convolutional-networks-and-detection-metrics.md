---
layout: study_note
title: "Fully Convolutional Networks, and Why Detection Needed Its Own Metric"
description: "How dropping the fully-connected head decouples a network from input size, and why mAP exists — the same argument against accuracy that class imbalance forces on classification, arriving by a different road."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Neural Networks & Representation"
order: 9
source: "Independent study"
written: true
updated: "2026-09-15"
---

A convolutional network with a fully-connected head has a fixed input size, and the reason is worth stating plainly because everything else follows from it. The flatten step multiplies out a feature map of known spatial extent into a vector of known length, and the first dense layer's weight matrix is shaped to that length. Change the input resolution and the matrix no longer fits.

## Core question and definition

A **fully convolutional network** removes that constraint by removing the dense layers: every layer is a convolution, so the output is a spatial map whose size scales with the input rather than a vector whose size is fixed.[^fcn]

The consequence is not merely convenience. A fixed-size vector output can answer "what is in this image." A spatial output can answer "what is *where*," because the output retains a coordinate system that the flatten operation destroyed. Semantic segmentation, depth estimation, super-resolution and detection are all the same architectural move: keep the map.

This is the building block. Everything in one-stage detection is a fully convolutional network whose output channels are interpreted as box coordinates and class scores at each spatial site.

## Key concepts

### Localisation needs a graded notion of correct

Classification has an unambiguous notion of a correct answer. Detection does not: a predicted box is never exactly the ground-truth box, so "correct" has to be defined by a threshold on overlap.

**Intersection over union** is that definition — the area of the intersection divided by the area of the union. It is scale-free, which is what makes it usable across object sizes, and it punishes both misses and overreach with one number.

It is also far stricter than intuition suggests. For a $$10\times10$$ box, sliding it 2 pixels sideways already drops IoU to $$0.667$$; sliding it 5 pixels — still half-overlapping, still visually "on" the object — gives $$0.333$$, below the conventional $$0.5$$ threshold. A box nested inside another at half the linear size scores $$0.25$$. In one dimension, the shift that lands exactly on $$\text{IoU}=0.5$$ for a box of side $$w$$ is $$w/3$$.

I find that last figure clarifying. "IoU > 0.5" sounds permissive and is not: it permits roughly a third of a box-width of error and nothing more.

### mAP exists because accuracy is meaningless here

Count the predictions a detector makes. SSD at $$300\times300$$ emits **8732** boxes per image, from six feature maps:

| feature map | anchors/site | boxes |
|---|---|---|
| $$38\times38$$ | 4 | 5776 |
| $$19\times19$$ | 6 | 2166 |
| $$10\times10$$ | 6 | 600 |
| $$5\times5$$ | 6 | 150 |
| $$3\times3$$ | 4 | 36 |
| $$1\times1$$ | 4 | 4 |
| | | **8732** |

An image contains perhaps three objects. A detector that predicts "no object" at all 8732 sites is correct 99.97% of the time and useless — which is the same collapse that makes accuracy uninformative under class imbalance, met again in a setting where the imbalance is a structural consequence of the output format rather than a property of the disease.

The lecturer's version of this is a test that calls all 1000 patients healthy, scores 99% accuracy, and finds none of the 10 who are sick. The [MCC note](/study/matthews-correlation-coefficient/) works through why that number is not salvageable by any single-threshold summary. Detection's answer is **average precision**: sweep the confidence threshold, record precision at a series of recall levels, and average. **mAP** is that averaged once more over object classes — the "m" is the outer average, which is the easier half to remember and the less interesting one.[^voc]

AP is doing the same job for precision-recall that AUROC does for the ROC curve: collapsing an operating *curve* into one number so that two systems can be ranked without first agreeing on a threshold. The cost is identical too — the number describes the curve, and no deployment ever runs on a curve.

### Two stages versus one

**Two-stage** detectors propose regions first, then classify each one. R-CNN ran a CNN separately on every proposal; Fast R-CNN shared the convolutional computation and cropped features instead of pixels; Faster R-CNN replaced the external proposal algorithm with a learned region proposal network, making the whole thing trainable end to end.[^rcnn][^fastrcnn][^fasterrcnn]

The structure is a loop: a per-region subnetwork runs hundreds of times per image. That loop is the speed ceiling, and it cannot be lifted by making the shared trunk heavier, because the trunk runs once and the head runs hundreds of times.

**One-stage** detectors delete the loop. One forward pass emits every box, which is why the box count is large and fixed rather than data-dependent. SSD reads predictions from several feature maps at different depths; YOLO v1 used a fully-connected head over a $$7\times7$$ grid with 2 boxes per cell — **98** boxes, and a $$7\times7\times30$$ output tensor where $$30 = 2\times5 + 20$$.[^ssd][^yolo]

The trade was accuracy for speed, and the gap narrowed from both directions until a controlled comparison — same backbones, same data, varying only the meta-architecture — was needed to say anything at all.[^huang] That paper's finding is the honest summary: Faster R-CNN leads on accuracy, SSD leads in the fast regime, and much of what earlier tables attributed to architecture was backbone and training data.

## Why it matters for my work

The structural point is that **mAP was invented because the metric a task needs is not deducible from the model — it is deducible from what the output means.** Detection needed a new metric not because detection is harder but because its output format made the negative class overwhelming and positional error graded rather than binary.

That generalises directly to medical imaging, where the equivalent question is asked too late or not at all. A lesion-detection model inherits detection's imbalance structure; a segmentation model inherits the graded-correctness problem in a form where the IoU threshold is doing enormous unexamined work. If a third of a box-width of error is the difference between a hit and a miss at IoU 0.5, then reporting a single mAP for a lesion detector is reporting one point on a sensitivity curve whose shape was chosen by convention rather than by clinical consequence.

The second point is about what the box count means for auditing. 8732 candidate boxes per image means that whatever a detector has learned about *where* objects tend to be is distributed across a fixed spatial grid that is identical for every image. A dataset in which lesions sit in a characteristic part of the frame — a scanner's standard view, an acquisition protocol's framing — hands the detector a positional prior that is indistinguishable, at the level of mAP, from having learned the lesion. This is [shortcut learning](/study/shortcut-learning-in-medical-imaging/) with a spatial index, and the metric cannot see it.

## What I have not resolved

Whether IoU is the right correctness criterion for clinical detection at all. It is symmetric between over- and under-segmentation, and clinical consequence is not: a margin drawn too wide and one drawn too narrow are different errors with different costs. Metrics that break that symmetry exist; I do not yet know what the evidence says about whether they change which models get selected, or only how they are described.

---

[^fcn]: Long, J., Shelhamer, E., & Darrell, T. (2015). Fully convolutional networks for semantic segmentation. *CVPR*. [10.1109/CVPR.2015.7298965](https://doi.org/10.1109/CVPR.2015.7298965)

[^voc]: Everingham, M., Van Gool, L., Williams, C. K. I., Winn, J., & Zisserman, A. (2010). The Pascal Visual Object Classes (VOC) Challenge. *IJCV*, 88, 303–338. [10.1007/s11263-009-0275-4](https://doi.org/10.1007/s11263-009-0275-4)

[^rcnn]: Girshick, R., Donahue, J., Darrell, T., & Malik, J. (2014). Rich feature hierarchies for accurate object detection and semantic segmentation. *CVPR*. [10.1109/CVPR.2014.81](https://doi.org/10.1109/CVPR.2014.81)

[^fastrcnn]: Girshick, R. (2015). Fast R-CNN. *ICCV*. [10.1109/ICCV.2015.169](https://doi.org/10.1109/ICCV.2015.169)

[^fasterrcnn]: Ren, S., He, K., Girshick, R., & Sun, J. (2017). Faster R-CNN: Towards real-time object detection with region proposal networks. *IEEE TPAMI*, 39(6), 1137–1149. [10.1109/TPAMI.2016.2577031](https://doi.org/10.1109/TPAMI.2016.2577031)

[^ssd]: Liu, W., et al. (2016). SSD: Single Shot MultiBox Detector. *ECCV*. [10.1007/978-3-319-46448-0_2](https://doi.org/10.1007/978-3-319-46448-0_2)

[^yolo]: Redmon, J., Divvala, S., Girshick, R., & Farhadi, A. (2016). You Only Look Once: Unified, real-time object detection. *CVPR*. [10.1109/CVPR.2016.91](https://doi.org/10.1109/CVPR.2016.91)

[^huang]: Huang, J., et al. (2017). Speed/accuracy trade-offs for modern convolutional object detectors. *CVPR*. [10.1109/CVPR.2017.351](https://doi.org/10.1109/CVPR.2017.351)
