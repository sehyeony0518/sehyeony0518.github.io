---
layout: study_note
title: "Anchor Boxes and Non-Maximum Suppression: Where the Priors Are Hidden"
description: "Deriving anchor-box geometry, normalized box regression, IoU matching, and non-maximum suppression, with worked examples of reference boxes, losses, and overlapping detections."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Neural Networks & Representation"
order: 10
source: "Independent study"
written: true
updated: "2026-09-15"
---

Anchor boxes specify reference geometry. A network predicts how to modify that geometry, and a post-processing rule selects among the resulting candidates.

Neither operation should be confused with a theorem about objects. Anchors are a parameterization and an inductive bias. Non-maximum suppression is a selection rule applied to predicted boxes. Its behavior depends on coordinates, scores, classes, and thresholds.

An important correction comes first: ordinary normalized anchor offsets are not bounded. Normalizing a coordinate removes units; it does not impose a finite range.

## Fix the coordinate convention before doing arithmetic

Represent an axis-aligned rectangle by

$$
b=(x_1,y_1,x_2,y_2),
\qquad
x_2>x_1,\quad y_2>y_1.
$$

Use continuous coordinates, or equivalently half-open pixel intervals. Its area is

$$
A(b)=(x_2-x_1)(y_2-y_1).
$$

There is no added one in this convention. An inclusive integer-pixel convention uses different arithmetic, so mixing implementations can create discrepancies even when the coordinates appear identical.

The center-size representation is

$$
c_x=\frac{x_1+x_2}{2},
\qquad
c_y=\frac{y_1+y_2}{2},
$$

$$
w=x_2-x_1,
\qquad
h=y_2-y_1.
$$

The inverse transformation is

$$
x_1=c_x-\frac{w}{2},
\qquad
x_2=c_x+\frac{w}{2},
$$

with the analogous expressions for the vertical coordinates.

These are representations of the same box, not different localization targets. Losses computed in the two representations can nevertheless behave differently, because a change of coordinates does not generally preserve Euclidean distance.

## Deriving anchor width and height from scale and ratio

Let an anchor have area $$s^2$$ and aspect ratio $$r$$:

$$
wh=s^2,
\qquad
\frac{w}{h}=r.
$$

Substitute $$w=rh$$ into the area equation:

$$
rh^2=s^2.
$$

For positive dimensions,

$$
h=\frac{s}{\sqrt r},
\qquad
w=s\sqrt r.
$$

The square root is therefore required by the simultaneous area and ratio constraints.

For a constructed scale of 12 and ratio of four,

$$
w=12\sqrt4=24,
\qquad
h=\frac{12}{\sqrt4}=6.
$$

The area remains

$$
24\cdot6=144=12^2.
$$

A square anchor at the same scale has dimensions 12 by 12. Shape changes while area remains fixed.

Suppose neighboring scales are 12 and 48. A scale halfway between them in logarithmic space satisfies

$$
\log s_{\mathrm{mid}}
=
\frac{\log12+\log48}{2}.
$$

Exponentiating gives

$$
s_{\mathrm{mid}}=\sqrt{12\cdot48}=24.
$$

The multiplicative gaps are equal:

$$
\frac{24}{12}=\frac{48}{24}=2.
$$

An arithmetic midpoint of 30 would make the additive gaps equal instead. Geometric spacing is appropriate when scale errors are naturally understood as ratios.

The number of anchors also follows directly from construction. A four-by-four map with three anchors per site contributes 48 anchors. A two-by-two map with three contributes 12. Together they supply 60 candidates before any image-dependent prediction.

## Why centers use normalized differences and sizes use logarithms

Let the anchor be

$$
a=(a_x,a_y,a_w,a_h)
$$

and its matched target be

$$
g=(g_x,g_y,g_w,g_h).
$$

A common encoding is

$$
t_x=\frac{g_x-a_x}{a_w},
\qquad
t_y=\frac{g_y-a_y}{a_h},
$$

$$
t_w=\log\frac{g_w}{a_w},
\qquad
t_h=\log\frac{g_h}{a_h}.
$$

The center offsets are dimensionless. A displacement of four pixels relative to an eight-pixel anchor has the same encoded magnitude as a displacement of 40 pixels relative to an 80-pixel anchor.

The size coordinates describe multiplicative changes additively. If width doubles,

$$
t_w=\log2.
$$

If width halves,

$$
t_w=\log\frac12=-\log2.
$$

Successive rescalings also add:

$$
\log\frac{w_3}{w_1}
=
\log\frac{w_3}{w_2}
+
\log\frac{w_2}{w_1}.
$$

This is why logarithms are useful here. They do not imply that a log-coordinate loss equals an overlap loss.

The inverse encoding is obtained by ordinary algebra:

$$
g_x=a_x+a_wt_x,
\qquad
g_y=a_y+a_ht_y,
$$

$$
g_w=a_w e^{t_w},
\qquad
g_h=a_h e^{t_h}.
$$

Exponentiation ensures positive predicted dimensions. Both center offsets and log-size offsets can take arbitrarily large positive or negative values.

If all image coordinates are multiplied by a positive factor, these targets remain unchanged. That scale normalization helps reuse a parameterization across image sizes, although resizing can still change the visual information available to the network.

## A complete encoding and decoding example

Choose

$$
a=(10,10,8,4),
\qquad
g=(12,9,16,2).
$$

The encoded center targets are

$$
t_x=\frac{12-10}{8}=\frac14,
\qquad
t_y=\frac{9-10}{4}=-\frac14.
$$

The size targets are

$$
t_w=\log2,
\qquad
t_h=-\log2.
$$

Decode them:

$$
\hat g_x=10+8\left(\frac14\right)=12,
$$

$$
\hat g_y=10+4\left(-\frac14\right)=9,
$$

$$
\hat g_w=8e^{\log2}=16,
\qquad
\hat g_h=4e^{-\log2}=2.
$$

The reconstructed target is exact.

Some implementations scale the targets:

$$
u_j=\frac{t_j}{v_j}.
$$

With chosen center scales of 0.1 and size scales of 0.2,

$$
u=
\left(
2.5,-2.5,
\frac{\log2}{0.2},
-\frac{\log2}{0.2}
\right),
$$

so the final two entries are approximately positive and negative 3.4657.

Decoding must first recover

$$
t_j=v_ju_j.
$$

Calling these constants “variances” does not automatically give them a probabilistic interpretation. Algebraically, they rescale coordinates and therefore change the relative gradients assigned to errors in those coordinates.

A useful implementation check is a round trip: encode a known box, decode the result, and verify the original coordinates. The test should include non-square boxes and negative center offsets.

## Deriving intersection over union

For boxes $$A$$ and $$B$$, the intersection width is

$$
w_I=
\max\left(
0,
\min(A_{x_2},B_{x_2})
-
\max(A_{x_1},B_{x_1})
\right).
$$

The intersection height is defined similarly, giving

$$
I=w_Ih_I.
$$

The union follows from inclusion–exclusion:

$$
U=A(A)+A(B)-I.
$$

Thus

$$
\operatorname{IoU}(A,B)=\frac{I}{U}.
$$

Subtracting the intersection once prevents the shared region from being counted twice.

The anchor from the encoding example has corners

$$
(6,8,14,12),
$$

and its target has corners

$$
(4,8,20,10).
$$

Both have area 32. Their intersection is eight units wide and two high:

$$
I=16,
\qquad
U=32+32-16=48.
$$

Therefore

$$
\operatorname{IoU}(a,g)=\frac13.
$$

The target is perfectly representable by the decoder even though the initial overlap is modest. Anchor overlap affects assignment and optimization; it is not a hard limit on the set of boxes the regression formula can express.

## Matching determines which predictions receive which targets

Before computing regression loss, training must assign anchors to ground-truth objects.

Consider three anchors:

$$
A_1=[0,0,10,10],
$$

$$
A_2=[2,0,12,10],
$$

$$
A_3=[20,0,30,10],
$$

and two objects:

$$
G_1=[0,0,10,10],
\qquad
G_2=[20,0,30,10].
$$

Their overlaps are

| Anchor | IoU with first object | IoU with second object |
|---|---:|---:|
| First | 1 | 0 |
| Second | $$2/3$$ | 0 |
| Third | 0 | 1 |

At a positive threshold of one half, all three anchors can be positive. Two anchors represent the first object.

This is why the number of positive training examples is not necessarily the number of annotated objects. Conversely, a small or unusually shaped object may have no anchor above the chosen threshold.

Assignment schemes may force a best match, reserve an ignored interval between positive and negative thresholds, or resolve competing matches differently. Each choice changes the training problem. A forced best match also needs a collision policy when multiple objects prefer the same anchor.

Training matching and inference suppression answer different questions. Matching connects predictions to supervision. NMS compares predictions with other predictions. Neither should be described simply as “remove overlapping boxes,” because the objects being compared and the purpose of the comparison differ.

## Localization loss and its gradients

A common coordinate penalty is smooth L1. With transition parameter $$\beta>0$$,

$$
\ell_\beta(e)=
\begin{cases}
\dfrac{e^2}{2\beta},& |e|<\beta,\\[6pt]
|e|-\dfrac{\beta}{2},& |e|\ge\beta.
\end{cases}
$$

Its derivative is

$$
\ell_\beta'(e)=
\begin{cases}
e/\beta,& |e|<\beta,\\
\operatorname{sign}(e),& |e|\ge\beta.
\end{cases}
$$

One way to derive the loss is to begin with this desired gradient: linear near zero, capped in magnitude outside the transition region. Integrating the gradient gives the quadratic and linear branches. The constant in the second branch makes the loss continuous at the transition.

With $$\beta=1$$ and coordinate errors

$$
e=(0.5,-2,0,1),
$$

the summed loss is

$$
\frac{0.5^2}{2}
+
\left(2-\frac12\right)
+
0
+
\frac12
=
2.125.
$$

The corresponding gradients are

$$
(0.5,-1,0,1).
$$

Regression is normally applied only to matched positive predictions. A negative anchor has no target object's coordinates to regress toward.

A combined objective may normalize the summed losses by the positive count:

$$
L=
\frac{
L_{\mathrm{classification}}
+
\lambda L_{\mathrm{localization}}
}{
\max(1,N_+)
}.
$$

This is one convention, not a universal definition. Negative sampling, weighting, and the handling of images without positives must be stated separately.

## Greedy non-maximum suppression, worked through

For one class, hard NMS repeatedly selects the highest-scoring remaining box and removes candidates whose overlap with it exceeds a threshold.

Use four boxes:

| Box | Coordinates | Score |
|---|---|---:|
| A | $$[0,0,10,10]$$ | 0.90 |
| B | $$[2,0,12,10]$$ | 0.80 |
| C | $$[4,0,14,10]$$ | 0.70 |
| D | $$[20,0,30,10]$$ | 0.60 |

Their relevant overlaps are

$$
\operatorname{IoU}(A,B)=\frac{80}{120}=\frac23,
$$

$$
\operatorname{IoU}(B,C)=\frac23,
$$

$$
\operatorname{IoU}(A,C)=\frac{60}{140}=\frac37.
$$

Set the threshold to one half, with suppression for strictly greater overlap.

First select A. B is suppressed, while C survives because

$$
\frac37<\frac12.
$$

D also survives because it is disjoint.

Next select C, then D. The retained set is

$$
\{A,C,D\}.
$$

Notice that B overlapped both A and C strongly, but A and C did not overlap each other strongly. “Overlaps above threshold” is not a transitive relation, so it does not partition candidates into simple duplicate groups.

Greedy selection is also not guaranteed to maximize the sum of retained scores. On the first three boxes, change the scores to

$$
s_B=0.95,\qquad s_A=0.90,\qquad s_C=0.80.
$$

NMS selects B and suppresses both neighbors. Yet A and C are mutually compatible and have combined score 1.70. This comparison describes a graph optimization objective; it does not mean that adding confidence scores is always the right detection objective.

## What the overlap threshold implies geometrically

Take equal boxes of width $$w$$ and height $$h$$, shifted horizontally by $$d$$, where

$$
0\le d\le w.
$$

Their intersection is

$$
I=(w-d)h,
$$

and their union is

$$
U=2wh-(w-d)h=(w+d)h.
$$

Therefore

$$
\operatorname{IoU}=\frac{w-d}{w+d}.
$$

For suppression threshold $$\tau$$,

$$
\frac{w-d}{w+d}>\tau
$$

is equivalent to

$$
w-d>\tau w+\tau d,
$$

and hence

$$
d<w\frac{1-\tau}{1+\tau}.
$$

At a threshold of one half, suppression occurs when the horizontal displacement is less than one third of the width. Equality is retained under the strict comparison used here.

This is a statement about these predicted boxes. It does not prove that two nearby physical objects can never both be detected: their predicted boxes may have different dimensions or lower mutual overlap. The exact claim is that two candidates with excessive mutual overlap cannot both survive that NMS step.

Class-wise NMS avoids suppressing candidates solely because they belong to different classes. Class-agnostic NMS also exists. The appropriate choice depends on the label ontology and the intended duplicate policy.

## Softer selection and class probabilities

A simple soft-NMS rule reduces a candidate's score instead of immediately deleting it:

$$
s_j'
=
s_j\left(1-\operatorname{IoU}(M,B_j)\right)
$$

when overlap with the selected box $$M$$ exceeds a chosen threshold.

For two candidates with overlap two thirds and a lower score of 0.8,

$$
s_j'=0.8\left(1-\frac23\right)=\frac{0.8}{3}\approx0.2667.
$$

A final score cutoff of 0.25 keeps it; a cutoff of 0.30 removes it. Soft suppression therefore changes the selection behavior without guaranteeing that crowded objects survive. Scores must also be reconsidered after updates.

Classification probabilities encode another modeling choice. A categorical softmax uses

$$
p_c=\frac{e^{z_c}}{\sum_j e^{z_j}},
\qquad
L=-\log p_y,
$$

for one mutually exclusive label.

Separate Bernoulli labels instead use

$$
p_c=\frac{1}{1+e^{-z_c}},
$$

$$
L=
-\sum_c
\left[
y_c\log p_c+(1-y_c)\log(1-p_c)
\right].
$$

This permits multiple labels to be positive. It does not prove that the real labels are statistically independent; it defines the prediction and training factorization.

Similarly, multiplying objectness by a conditional class probability has a probability interpretation only when those quantities represent the corresponding events. A score used for ranking is not automatically calibrated.

## Auditing anchor coverage separately from final detection

For ground-truth boxes $$G_j$$ and anchors $$A_i$$, define pre-regression coverage at threshold $$\tau$$:

$$
Q_\tau
=
\frac{1}{N}
\sum_{j=1}^{N}
\mathbf1
\left[
\max_i\operatorname{IoU}(A_i,G_j)\ge\tau
\right].
$$

This measures how often the reference geometry starts near an object. It is not final recall: regression may improve a weak match, and classification or suppression may discard a strong one.

Coverage should be examined by object size and aspect ratio. A pooled value can hide an entire poorly covered subgroup.

Data-derived anchor clusters can adapt the reference set to training geometry, but they inherit that dataset's distribution. Moreover, if clustering uses an IoU-based distance, an arithmetic centroid is not automatically the exact minimizer of the cluster objective. The update rule and distance must be considered together.

To locate a failure, retain intermediate candidates and compare coverage, post-regression overlap, classification scores, and post-NMS recall. A final metric alone cannot identify which stage removed the useful prediction.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| Convert between corner and center-size coordinates. | State whether coordinates are continuous or inclusive integers. |
| Derive anchor dimensions from area and aspect ratio. | Recover both square-root expressions. |
| Explain geometric scale spacing. | Show equal multiplicative gaps. |
| Encode and decode a non-square target. | Reproduce the full numerical round trip. |
| Explain why normalized offsets are unbounded. | Separate units from range constraints. |
| Compute IoU from corners. | Use inclusion–exclusion for the union. |
| Distinguish matching from suppression. | Identify what is compared in each stage. |
| Derive smooth L1 from its gradient. | Check continuity at the transition. |
| Execute greedy NMS by hand. | Reproduce the retained set and the non-transitive overlap example. |
| Derive the horizontal suppression condition. | Preserve the strict inequality convention. |
| Explain what soft-NMS does not guarantee. | Include the final score cutoff. |
| Separate anchor coverage from detector recall. | Track the prediction through the whole pipeline. |

## Why it matters for my work

For lesion detection, I need to inspect the candidates that existed before suppression. Anchor coverage and NMS can produce distinct failure modes, and neither is explained by an attribution map of the network alone.

## What I have not resolved

Measure how many annotated adjacent objects lose a valid candidate specifically at the suppression stage, stratified by predicted overlap, object size, and class.
