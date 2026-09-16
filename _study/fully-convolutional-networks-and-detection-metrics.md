---
layout: study_note
title: "Fully Convolutional Networks, and Why Detection Needed Its Own Metric"
description: "Deriving fully convolutional networks from fully-connected layers, then computing IoU, detection matching, precision-recall, AP, and mAP under explicit evaluation conventions."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Neural Networks & Representation"
order: 9
source: "Independent study"
written: true
updated: "2026-09-15"
---

A dense prediction system needs two specifications: what its output tensor means, and how those predictions are evaluated.

A spatial tensor does not become a detector merely because it contains coordinates. The system also needs a decoding rule, class interpretation, confidence scores, and a policy for duplicate predictions. Likewise, a number called AP is incomplete without a matching rule, overlap threshold, and averaging convention.

The architectural and evaluation questions meet at the output, but neither can be deduced entirely from the other.

## Why a flatten-and-dense head fixes spatial dimensions

Suppose a feature map has shape

$$
H\times W\times C.
$$

Flattening gives a vector containing

$$
HWC
$$

entries. A dense layer with $$K$$ outputs uses

$$
W_{\mathrm{dense}}\in\mathbb R^{K\times HWC}.
$$

If the feature map changes from eight by eight to ten by ten while keeping 32 channels, the input length changes from

$$
8\cdot8\cdot32=2048
$$

to

$$
10\cdot10\cdot32=3200.
$$

The existing weight matrix no longer has the required number of columns.

Flattening itself is not information destruction. Given the original shape and ordering, reshaping can recover the feature map exactly. The restriction comes from connecting the flattened vector to a matrix whose dimensions were fixed during model construction.

A dense layer can also assign unrelated weights to different absolute locations. That is another distinction from a spatially shared operation.

There are alternatives besides removing every dense layer. Adaptive pooling can produce a fixed-size representation before a dense classifier. That solves the shape mismatch, although the pooling operation determines which spatial distinctions survive.

## Converting a dense operation into a convolution

Let a dense output act on a feature block of fixed size:

$$
y_j
=
b_j+
\sum_{u=0}^{H_0-1}
\sum_{v=0}^{W_0-1}
\sum_{c=1}^{C}
W_{j,u,v,c}X_{u,v,c}.
$$

Interpret each output's weights as a convolutional kernel with spatial extent

$$
H_0\times W_0.
$$

On an input block of exactly that size, valid convolution produces one spatial output per output channel, equal to the original dense result.

On a larger input, the same kernel slides over multiple blocks. The model applies the former dense computation at every valid location using shared weights.

Subsequent dense layers acting only across that output vector become one-by-one convolutions. They mix channels at each location without requiring a fixed number of locations.

This conversion explains how a classifier's learned weights can be reused for spatial predictions. It does not imply that every dense layer is equivalent to a one-by-one convolution: the first layer that consumes an entire spatial block generally needs a kernel spanning that block.

A fully convolutional model can still contain pooling, nonlinearities, normalization, skip connections, and interpolation. The phrase does not mean that every operation must literally be a convolution.

## A dense-to-convolution calculation

Take one input channel, kernel

$$
K=
\begin{bmatrix}
1&2\\
3&4
\end{bmatrix},
$$

and bias one.

Applied as a dense operation to

$$
\begin{bmatrix}
1&2\\
4&5
\end{bmatrix},
$$

the result is

$$
1+1(1)+2(2)+3(4)+4(5)=38.
$$

Now use the same weights as a valid cross-correlation on

$$
X=
\begin{bmatrix}
1&2&3\\
4&5&6\\
7&8&9
\end{bmatrix}.
$$

The four outputs are

$$
\begin{aligned}
Y_{00}&=1+1+4+12+20=38,\\
Y_{01}&=1+2+6+15+24=48,\\
Y_{10}&=1+4+10+21+32=68,\\
Y_{11}&=1+5+12+24+36=78.
\end{aligned}
$$

Thus

$$
Y=
\begin{bmatrix}
38&48\\
68&78
\end{bmatrix}.
$$

The parameter count remains four weights and one bias. The larger input produces more evaluations, not more parameters.

The outputs overlap in the input values they use. In a multilayer network, shared convolutional computation can avoid separately recomputing an entire feature hierarchy for every image crop. This is the computational reason spatial prediction is more than a reshaping trick.

## Deriving output size and receptive field

For a one-dimensional input of length $$H$$, kernel size $$k$$, dilation $$d$$, symmetric padding $$p$$, and stride $$s$$, the kernel's span is

$$
k_{\mathrm{eff}}=d(k-1)+1.
$$

The available padded length is

$$
H+2p.
$$

A kernel starting at zero fits. Its final valid starting position cannot exceed

$$
H+2p-k_{\mathrm{eff}}.
$$

Counting starts separated by stride gives

$$
H_{\mathrm{out}}
=
\left\lfloor
\frac{H+2p-d(k-1)-1}{s}
\right\rfloor+1.
$$

For input length nine, kernel three, padding one, dilation one, and stride two,

$$
H_{\mathrm{out}}
=
\left\lfloor\frac{9+2-3}{2}\right\rfloor+1
=5.
$$

Applying the same layer again gives length three.

Output resolution and receptive field are different quantities. Let $$j_l$$ be the spacing, measured in input coordinates, between adjacent outputs at layer $$l$$. Let $$r_l$$ be the theoretical receptive-field width. Starting with

$$
j_0=1,\qquad r_0=1,
$$

the recurrence is

$$
j_l=s_lj_{l-1},
$$

$$
r_l=r_{l-1}+(k_l-1)d_lj_{l-1}.
$$

The second equation follows because each additional kernel step reaches one previous-layer spacing farther into the input.

For three kernel-three layers with strides two, two, and one, the pairs are

$$
(r_1,j_1)=(3,2),
$$

$$
(r_2,j_2)=(7,4),
$$

$$
(r_3,j_3)=(15,4).
$$

Each final site can depend on a width of 15 input pixels, while adjacent sites are four pixels apart. Upsampling that map increases the number of output samples but does not reverse the earlier information loss.

## From feature maps to candidate detections

A dense detector can attach a fixed set of prediction channels to each spatial site. With $$A$$ anchors per site, four box coordinates per anchor, and $$C+1$$ mutually exclusive class scores including background, a head can emit

$$
A(4+C+1)
$$

channels.

For three anchors and three foreground classes,

$$
3(4+3+1)=24
$$

channels are sufficient under this particular parameterization.

A four-by-four feature map then describes

$$
4\cdot4\cdot3=48
$$

candidate boxes. Different formulations may use separate objectness, independent class labels, anchor-free distances, or a different output organization.

The network's tensor dimensions therefore do not specify its semantics by themselves. A channel might represent a normalized center offset, a logarithmic size correction, or a distance to one side of a box.

One-stage and two-stage designs also do not imply universal speed or accuracy rankings. A two-stage model introduces region-conditioned processing; its cost depends on the number of regions and the work performed per region. A one-stage model may still perform substantial dense computation and post-processing. Architecture names are not substitutes for a defined workload.

## Localization correctness requires a geometric convention

For predicted and reference regions,

$$
\operatorname{IoU}
=
\frac{\text{intersection area}}{\text{union area}}.
$$

The denominator penalizes both missed reference area and extra predicted area.

For two ten-by-ten boxes shifted horizontally by two pixels,

$$
I=8\cdot10=80,
$$

$$
U=100+100-80=120,
$$

so

$$
\operatorname{IoU}=\frac23.
$$

A five-pixel horizontal shift gives

$$
\operatorname{IoU}
=
\frac{5\cdot10}{100+100-50}
=
\frac13.
$$

Shifting by two pixels in both directions gives

$$
I=8\cdot8=64,
$$

$$
\operatorname{IoU}
=
\frac{64}{200-64}
=
\frac8{17}.
$$

That last overlap is below one half, despite the displacement being only two pixels along each axis.

IoU is unchanged by a common rescaling of both boxes, because intersection and union acquire the same area factor. It is not insensitive to object size at a fixed pixel error. The same displacement occupies a larger fraction of a small object.

An IoU threshold converts graded geometric agreement into a binary matching decision. It is an evaluation convention, not a proof that errors immediately above and below the threshold have sharply different practical consequences.

## Matching detections to objects

For a simple evaluation protocol, choose one class and one IoU threshold. Process predictions in decreasing score order within each image. A prediction is a true positive if it matches an eligible, previously unmatched ground-truth object at the required overlap. Otherwise it is a false positive.

Each ground-truth object can normally contribute at most one true positive. A second prediction of the same object is a duplicate, even if its coordinates are perfect.

Ground-truth objects left unmatched are false negatives. Predictions of the wrong class cannot count as correct matches for that class.

Exact evaluators differ in how they select among competing overlaps and handle ignored regions, crowd annotations, ties, and maximum detection counts. Those details matter in ambiguous cases. The examples here avoid such ambiguity and state the convention explicitly.

Three thresholds must not be conflated:

- A confidence threshold decides which predictions are submitted or displayed.
- An NMS threshold compares predicted boxes with other predicted boxes.
- An evaluation IoU threshold compares predictions with ground truth.

Increasing one threshold does not have the same effect as increasing another.

Detection also lacks a unique collection of true-negative objects. Empty space can be divided into arbitrarily many candidate windows. Consequently, candidate-level accuracy can be changed by changing the candidate generator without changing the useful detections.

## A complete ranked detection example

Construct one image with three ground-truth objects:

$$
G_1=[0,0,10,10],
$$

$$
G_2=[20,0,30,10],
$$

$$
G_3=[40,0,50,10].
$$

All have the same class. Submit the following predictions, already ordered by score:

| Rank | Prediction | Score | Outcome |
|---:|---|---:|---|
| 1 | $$[60,0,70,10]$$ | 0.99 | False positive |
| 2 | Exact copy of first object | 0.90 | True positive |
| 3 | Another exact copy of first object | 0.80 | Duplicate false positive |
| 4 | Exact copy of second object | 0.70 | True positive |
| 5 | Exact copy of third object | 0.60 | True positive |
| 6 | $$[80,0,90,10]$$ | 0.50 | False positive |

At an overlap threshold of one half, every claimed exact match has IoU one, while the unrelated boxes are disjoint.

At rank $$k$$, define

$$
P_k=\frac{\operatorname{TP}_k}{k},
\qquad
R_k=\frac{\operatorname{TP}_k}{3}.
$$

The resulting curve is

| Rank | Cumulative true positives | Precision | Recall |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 2 | 1 | $$1/2$$ | $$1/3$$ |
| 3 | 1 | $$1/3$$ | $$1/3$$ |
| 4 | 2 | $$1/2$$ | $$2/3$$ |
| 5 | 3 | $$3/5$$ | 1 |
| 6 | 3 | $$1/2$$ | 1 |

Lowering the score cutoff moves down this table. Recall increases only at a new true positive. A false positive changes precision without increasing recall.

The duplicate at rank three illustrates why detection evaluation needs matching, not merely a test that each predicted box overlaps some annotated object.

## Deriving average precision from recall increments

One non-interpolated definition of AP weights precision by each increase in recall:

$$
\operatorname{AP}_{\mathrm{raw}}
=
\sum_k
(R_k-R_{k-1})P_k.
$$

Why use recall increments? Each correctly recovered ground-truth object contributes an equal portion of the total relevant population. False positives contribute no new recall, but lower the precision attached to later discoveries.

With $$G$$ ground-truth objects and ordinary one-to-one matching, each true positive increases recall by

$$
\frac1G.
$$

Therefore

$$
\operatorname{AP}_{\mathrm{raw}}
=
\frac1G
\sum_{k:\,\text{true positive at }k}P_k.
$$

For the constructed example,

$$
\operatorname{AP}_{\mathrm{raw}}
=
\frac13
\left(
\frac12+\frac12+\frac35
\right)
=
\frac8{15}
\approx0.5333.
$$

An interpolated convention first replaces precision by an upper envelope:

$$
p_{\mathrm{interp}}(r)
=
\max_{k:R_k\ge r}P_k,
$$

with zero where the requested recall is unattainable.

Its continuous all-points AP is

$$
\operatorname{AP}_{\mathrm{interp}}
=
\int_0^1p_{\mathrm{interp}}(r)\,dr.
$$

In this example, the best precision available at every positive recall up to one is three fifths. Thus

$$
\operatorname{AP}_{\mathrm{interp}}=\frac35=0.6.
$$

Both answers are correct for their stated definitions. Reporting “AP” without naming the convention hides this difference.

Interpolation rewards the best operating precision available at or beyond a requested recall. It removes local downward fluctuations caused by individual false positives. It does not repair an evaluator or recover objects that were never detected.

## Missing objects, trailing errors, and localization thresholds

Suppose a fourth ground-truth object is added without adding a matching prediction. The precision values in the table remain the same, but maximum recall becomes

$$
\frac34.
$$

The interpolated precision is three fifths up to that recall and zero afterward. Hence

$$
\operatorname{AP}_{\mathrm{interp}}
=
\frac34\cdot\frac35
=
\frac9{20}
=
0.45.
$$

The denominator must include every relevant ground-truth object, not only those discovered.

By contrast, adding false positives after all true positives need not change this AP. The previous high-recall precision remains available to the envelope. This explains why AP is not a complete description of the false-positive burden at a permissive deployment threshold.

Localization thresholds create another axis of variation. Consider one ground-truth box and one prediction shifted horizontally by two pixels in the ten-by-ten construction. Their IoU is two thirds.

At an IoU threshold of one half, the only prediction is a true positive, so AP is one. At a threshold of three quarters, it is a false positive and the object is missed, so AP is zero.

Across the ten thresholds

$$
0.50,0.55,\ldots,0.95,
$$

the prediction passes four and fails six. Averaging the corresponding AP values gives

$$
\frac4{10}=0.4.
$$

This value is derived entirely from the constructed geometry.

## What the mean in mAP averages

For class-specific AP values, a macro-average is

$$
\operatorname{mAP}
=
\frac1C\sum_{c=1}^{C}\operatorname{AP}_c.
$$

If two classes have AP values 0.6 and 0.2, their macro-average is 0.4 regardless of their relative object counts.

Pooling every detection into one list answers a different question. It can allow frequent classes to dominate and requires scores from different classes to be comparable.

COCO-style detection AP additionally evaluates multiple IoU thresholds and uses a fixed recall sampling grid. Its standard evaluator also specifies area ranges, ignored annotations, and maximum detection counts. A continuous all-points integral is therefore not numerically interchangeable with every benchmark implementation.

A reproducible metric report should identify the evaluator and its settings, including the treatment of classes without ground-truth examples. Undefined classes should not silently become perfect scores or arbitrary zeros.

AP is principally a ranking summary. A strictly increasing transformation of scores preserves their ordering and therefore preserves AP when the submitted detections remain unchanged. It can nevertheless change which predictions pass a fixed numerical confidence cutoff. Ranking quality and probability calibration are separate properties.

## Evaluating the operating point as well as the curve

A deployed detector uses a particular selection policy. Its practical behavior should therefore be examined at specified confidence thresholds in addition to AP.

For a collection of images, two directly interpretable quantities are

$$
\text{sensitivity}
=
\frac{\text{matched objects}}{\text{annotated objects}},
$$

and

$$
\text{false positives per image}
=
\frac{\text{unmatched predictions}}{\text{number of images}}.
$$

Varying the score cutoff traces a sensitivity versus false-positive-burden curve. The denominator now describes an explicit unit of use.

Evaluation should preserve the intended independence structure. Images from one subject or acquisition can share information, so splitting individual images at random may not represent performance on new subjects.

For debugging, preserve the ranked predictions and matching assignments. They make it possible to distinguish missed objects, duplicate detections, class confusions, and poor localization. A single aggregate cannot reconstruct those distinctions after the fact.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| Explain the dense head's fixed-size constraint. | Identify the matrix dimension that changes. |
| Explain why flattening itself is reversible. | Separate reshaping from learned spatial mixing. |
| Convert a spatial dense layer to a convolution. | Use the correct kernel extent. |
| Reproduce the four numerical convolution outputs. | Obtain 38, 48, 68, and 78. |
| Derive output size from valid kernel starts. | Include stride, dilation, and padding. |
| Track receptive field and output spacing separately. | Reproduce widths 3, 7, and 15. |
| Compute IoU under horizontal and two-axis shifts. | Obtain two thirds and eight seventeenths. |
| Explain one-to-one matching and duplicate false positives. | Keep matching distinct from NMS. |
| Build the precision-recall table from ranked outcomes. | Count all ground-truth objects in recall. |
| Compute raw and interpolated AP. | Obtain eight fifteenths and three fifths. |
| Explain class and IoU averaging. | State which axes the reported mean includes. |
| Explain why AP does not specify deployment behavior. | Report a confidence operating point and false-positive burden. |

## Why it matters for my work

For medical detection, the evaluation object is the complete prediction pipeline. I need ranked outputs and matching records, not only mAP, to understand whether errors come from localization, classification, duplicate handling, or threshold selection.

## What I have not resolved

Define the acceptable localization error and false-positive burden for the actual annotation and use case before choosing a model-selection metric.
