---
layout: study_note
title: "Segmentation: Resolution Against Context, and the Things/Stuff Divide"
description: "Semantic, instance, and panoptic segmentation derived through pixel losses, receptive fields, encoder-decoder reconstruction, atrous convolution, center offsets, and panoptic quality."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Neural Networks & Representation"
order: 12
source: "Independent study"
written: true
updated: "2026-09-15"
---

Segmentation requires a decision about what a pixel label means before it requires an architecture.

A semantic label identifies a category. An instance label additionally identifies which object of that category owns the pixel. A panoptic output combines category labels with instance identities while enforcing a single assignment at each evaluated pixel.

Knowing the image dimensions fixes the number of pixel locations. It does not fix the number of objects, remove the grouping problem, or make instance segmentation automatically simpler than detection.

## Three output spaces

For semantic segmentation with $$C$$ classes, a model can emit logits

$$
z\in\mathbb R^{H\times W\times C}.
$$

A class label at each pixel is obtained from those logits. Two adjacent objects of the same class have identical semantic labels even if a human annotation treats them as distinct objects.

An instance prediction is naturally a collection:

$$
\mathcal I=\{(M_k,c_k,s_k)\}_{k=1}^{K},
$$

where each mask $$M_k$$ identifies an object, $$c_k$$ gives its class, and $$s_k$$ is a confidence score. The number of instances can vary.

Instance identifiers have no intrinsic order. Exchanging the names “instance one” and “instance two” does not change the segmentation if the associated pixel sets remain the same. Evaluation and training must account for this permutation freedom.

A panoptic output assigns

$$
p\longmapsto(c_p,i_p)
$$

to each evaluated pixel. For thing classes, the identifier distinguishes instances. For stuff classes, the instance identifier is not used in the same way.

The things/stuff distinction belongs to the annotation ontology. An organ can be treated as a countable object when separate organs matter, or as a semantic region when they do not. “Medical anatomy” is not inherently stuff, and “small region” is not inherently a thing.

A single-layer panoptic partition also cannot directly encode arbitrary overlapping labels. If an organ mask includes a lesion's pixels and the lesion is separately labeled, the task may require a hierarchy or multiple label layers.

## Deriving pixelwise cross-entropy

For mutually exclusive labels, define a per-pixel categorical distribution:

$$
p_{pc}
=
\frac{e^{z_{pc}}}{\sum_{j=1}^{C}e^{z_{pj}}}.
$$

If the observed label at pixel $$p$$ is $$y_p$$, its likelihood is

$$
p_{p,y_p}.
$$

Multiplying the per-pixel likelihood factors and taking the negative logarithm gives

$$
L_{\mathrm{CE}}
=
-\sum_p\log p_{p,y_p}.
$$

The sum follows from the logarithm of a product. The factorization is a modeling choice; it does not mean nearby pixels are physically independent. Their predicted probabilities may depend on a shared image representation.

For logits zero and $$\log3$$, the class probabilities are

$$
\left(\frac14,\frac34\right).
$$

If the second class is correct, the pixel loss is

$$
-\log\frac34=\log\frac43.
$$

If the first class is correct, it is

$$
-\log\frac14=\log4.
$$

The loss therefore distinguishes uncertainty from confident error.

Class weighting changes the objective:

$$
L=-\sum_p w_{y_p}\log p_{p,y_p}.
$$

It can increase the influence of rare classes, but the resulting scores should not automatically be interpreted as calibrated probabilities under the unweighted population distribution.

If several labels can legitimately be present at one pixel, separate Bernoulli outputs may be appropriate. A categorical softmax would force a competition that the annotation scheme does not intend.

## IoU, Dice, and why their denominators differ

For a foreground class, let the true-positive, false-positive, and false-negative pixel counts be $$TP$$, $$FP$$, and $$FN$$.

The union contains every correctly predicted foreground pixel, every extra predicted pixel, and every missed foreground pixel:

$$
J=\operatorname{IoU}
=
\frac{TP}{TP+FP+FN}.
$$

Dice counts the intersection twice and divides by the sum of the two mask sizes:

$$
D=
\frac{2TP}{2TP+FP+FN}.
$$

This is also the binary foreground F1 score. The doubled intersection compensates for the fact that correctly shared pixels appear once in each mask size.

The metrics are related algebraically. Since

$$
FP+FN=TP\left(\frac1J-1\right),
$$

substitution gives

$$
D
=
\frac{2TP}{2TP+TP(1/J-1)}
=
\frac{2J}{1+J}.
$$

Conversely,

$$
J=\frac{D}{2-D}.
$$

Thus they rank individual binary mask pairs identically when computed from the same counts. Their averages across images or classes need not be related by simply applying this nonlinear conversion to the average.

For a concrete construction, let the true foreground be pixels one through ten. Predict pixels one through six, plus pixels eleven and twelve.

Then

$$
TP=6,\qquad FP=2,\qquad FN=4.
$$

Therefore

$$
J=\frac6{12}=\frac12,
\qquad
D=\frac{12}{18}=\frac23.
$$

No image appearance or benchmark measurement is needed to verify these values.

## Pixel imbalance and soft overlap losses

Consider an image with 100 pixels: 90 background and ten foreground. Predict background everywhere.

Pixel accuracy is

$$
\frac{90}{100}=0.9.
$$

Foreground IoU is zero. Background IoU is

$$
\frac{90}{100}=0.9.
$$

The two-class mean IoU is therefore 0.45. Each metric answers a different aggregation question.

A differentiable Dice-like loss replaces the hard predicted mask by foreground probabilities:

$$
L_{\mathrm{Dice}}
=
1-
\frac{
2\sum_p q_py_p+\epsilon
}{
\sum_p q_p+\sum_p y_p+\epsilon
}.
$$

Here $$y_p$$ is a binary target and $$q_p$$ a predicted foreground probability.

This expression encourages agreement at the level of total overlap. Unlike pixelwise cross-entropy, its denominator couples the pixels: changing one prediction changes the normalization affecting the whole mask.

The smoothing constant prevents division by zero, but also defines behavior for empty masks. Its role is not merely numerical when the true foreground is absent.

Different implementations may square denominator terms, aggregate across a batch, or compute losses class by class. These variants are not interchangeable. The exact formula should accompany any claim about the loss.

A combined cross-entropy and overlap loss can emphasize both local labeling and regional agreement, but the combination weights determine the objective. There is no universally correct mixture independent of the task.

## Deriving the context–resolution tradeoff

A convolutional feature needs a sufficiently large input neighborhood to distinguish visually similar local patches. Downsampling increases the input spacing between feature sites, allowing later kernels to cover a larger input region.

Let $$r_l$$ be receptive-field width and $$j_l$$ the input spacing between adjacent features. Then

$$
j_l=s_lj_{l-1},
$$

$$
r_l=r_{l-1}+(k_l-1)d_lj_{l-1}.
$$

The added width comes from the kernel's extra positions, separated by dilation and by the previous layer's spacing.

A stride of 16 means neighboring feature sites are 16 input pixels apart. A feature map has one sixteenth as many sites along each axis, or one two-hundred-and-fifty-sixth as many spatial sites overall, assuming divisible dimensions.

This reduction does not imply that every sub-grid positional distinction has vanished: channels may encode some information. It does mean that producing a dense boundary requires the decoder to infer fine structure from a representation sampled more coarsely.

A theoretical receptive field states which pixels can influence a feature. It does not say that the trained model uses all of them equally. Nor does a large field establish that the representation contains the specific contextual relationship required by the task.

## What an encoder–decoder can recover

A decoder increases spatial resolution. Recovery is possible only from information retained in its inputs or inferred from learned regularities.

Consider max pooling a block:

$$
X=
\begin{bmatrix}
1&4\\
3&2
\end{bmatrix}.
$$

The pooled value is four, and the winning index is the top-right position. Unpooling with that index can produce

$$
\begin{bmatrix}
0&4\\
0&0
\end{bmatrix}.
$$

The values one, three, and two cannot be recovered from the maximum and its index. Many different input blocks produce the same stored information.

Skip connections transmit additional encoder features to the decoder. Concatenation retains separate channel groups; addition combines compatible groups directly. Neither operation guarantees accurate boundaries, but both can supply information unavailable in the deepest representation alone.

A transposed convolution is also not generally an inverse convolution. Write a simple convolutional linear map as

$$
A=
\begin{bmatrix}
1&1&0\\
0&1&1
\end{bmatrix}.
$$

For

$$
x=(1,2,3)^{\mathsf T},
$$

we obtain

$$
Ax=(3,5)^{\mathsf T}.
$$

Applying the transpose gives

$$
A^{\mathsf T}Ax=(3,8,5)^{\mathsf T},
$$

which is not the original vector.

The transpose reverses the direction of the linear mapping and redistributes contributions. It does not undo information loss unless additional special conditions hold.

## Atrous convolution expands spacing, not information for free

For a one-dimensional kernel with $$k$$ taps and dilation $$d$$, the first and last taps are separated by

$$
(k-1)d
$$

positions. Including both endpoints gives effective width

$$
k_{\mathrm{eff}}=(k-1)d+1.
$$

For a three-by-three spatial kernel, the two-dimensional span is

$$
(2d+1)\times(2d+1).
$$

At dilation six, that span is thirteen by thirteen, but the kernel still samples only nine spatial positions per input–output channel pair.

The parameter count is

$$
9C_{\mathrm{in}}C_{\mathrm{out}}
$$

before biases, not nine parameters for the entire multi-channel layer.

At stride one, stacking three-tap kernels with dilation rates one, two, four, and eight gives receptive-field widths

$$
3,\quad7,\quad15,\quad31,
$$

because

$$
1+2(1+2+4+8)=31.
$$

The larger span does not guarantee dense or equally strong use of every enclosed location. Repeating dilation two, for example, keeps sampling paths on an even-offset lattice. Some positions are never reached from a given output.

Combining rates can fill such gaps. Rates one and two allow offsets formed as

$$
a+2b,
\qquad
a,b\in\{-1,0,1\},
$$

which cover every integer from negative three through three.

Atrous convolution preserves the number of feature sites at a given layer. Keeping more sites can increase activation memory and total computation compared with a downsampled alternative. Its advantage is controlled sampling geometry, not costless global context.

## Multi-scale context and center-offset grouping

Parallel branches can gather context at different spatial scales and concatenate the results. Global pooling supplies a summary of the whole feature map; dilated branches supply differently spaced local evidence. A decoder can then combine this contextual representation with finer features.

For instance grouping, a center-offset formulation predicts a semantic label, an instance-center heatmap, and a two-dimensional offset at each pixel.

For an instance mask $$M_k$$, define its centroid by

$$
c_k=
\frac{1}{\lvert M_k\rvert}
\sum_{p\in M_k}p.
$$

The target offset for one of its pixels is

$$
o(p)=c_k-p.
$$

Therefore the ideal voted location is

$$
p+o(p)=c_k.
$$

After detecting center locations, assign a foreground pixel to the nearest voted center:

$$
\hat k(p)
=
\arg\min_k
\left\lVert
p+\hat o(p)-\hat c_k
\right\rVert_2.
$$

The subtraction in the target is essential. It makes all pixels of one instance point to the same coordinate despite beginning at different positions.

Consider a two-by-two object occupying rows zero and one, columns zero and one. Its center is

$$
c_1=(0.5,0.5).
$$

A second object at the same rows and columns three and four has center

$$
c_2=(0.5,3.5).
$$

For pixel

$$
p=(1,0),
$$

the first object's target offset is

$$
o(p)=(-0.5,0.5).
$$

For pixel

$$
q=(0,4),
$$

the second object's offset is

$$
o(q)=(0.5,-0.5).
$$

Adding each offset returns the appropriate center exactly.

## A centroid need not lie inside its object

Take an object consisting of four pixels at

$$
(0,0),\quad(0,2),\quad(2,0),\quad(2,2).
$$

Its centroid is

$$
(1,1),
$$

which is not one of its pixels.

That does not invalidate offset regression. Every object pixel can still point to that coordinate, and a center heatmap defined over the image can place a peak there. An implementation that only permits centers on foreground pixels would introduce an additional restriction.

The more fundamental ambiguity is that distinct objects can have coincident or nearly coincident centroids. A representation using only center location may then be insufficient to distinguish them.

Grouping also depends on center detection. Missing a center can merge an object's votes into a neighbor; duplicate centers can split one object.

In the two-object example, the centers are three pixels apart. With exact predicted centers, a vote whose error is less than 1.5 pixels in Euclidean norm is guaranteed to remain closer to its own center than the other. This follows from the triangle inequality: its distance to the other center exceeds three minus its own error.

The bound explains a grouping margin. It is not a claim that learned offsets achieve that error.

## Why panoptic matching uses a strict overlap threshold

Panoptic predictions form non-overlapping segments. Ground-truth segments also form a non-overlapping partition, apart from explicitly ignored regions.

Suppose two disjoint predicted segments both matched one ground-truth segment at IoU strictly above one half. Each intersection would have to contain more than half the ground-truth segment, because the union is at least as large as that ground truth.

Their disjoint intersections would then contain more pixels than the ground-truth segment itself. This is impossible.

The same argument with prediction and ground truth exchanged prevents one prediction from matching two ground-truth segments.

The strict inequality matters. Two predictions that each cover exactly one half of one object can each have IoU one half. Excluding equality avoids that ambiguity.

This uniqueness result relies on non-overlapping masks. It cannot be transferred unchanged to arbitrary overlapping instance predictions.

## Deriving and calculating panoptic quality

For one class, let matched pairs be true positives. Let unmatched predictions and ground-truth segments be false positives and false negatives.

Panoptic quality is

$$
PQ=
\frac{
\sum_{(p,g)\in TP}\operatorname{IoU}(p,g)
}{
\lvert TP\rvert
+\frac12\lvert FP\rvert
+\frac12\lvert FN\rvert
}.
$$

Factor it as

$$
PQ=SQ\cdot RQ,
$$

where

$$
SQ=
\frac{
\sum_{(p,g)\in TP}\operatorname{IoU}(p,g)
}{
\lvert TP\rvert
},
$$

and

$$
RQ=
\frac{
2\lvert TP\rvert
}{
2\lvert TP\rvert+\lvert FP\rvert+\lvert FN\rvert
}.
$$

The second term is object-level F1. The half-weights in the original denominator are what make this factorization work.

Construct three true instances:

$$
G_1=\{1,2,3,4\},
$$

$$
G_2=\{5,6,7,8\},
$$

$$
G_3=\{9,10,11,12\}.
$$

Predict

$$
P_1=\{1,2,3,4,13\},
$$

$$
P_2=\{5,6,7\},
$$

$$
P_3=\{14,15\}.
$$

The first two match with overlaps

$$
\frac45,\qquad\frac34.
$$

The third prediction is unmatched, and the third true instance is missed. Therefore

$$
\lvert TP\rvert=2,\quad
\lvert FP\rvert=1,\quad
\lvert FN\rvert=1.
$$

The overlap sum is

$$
\frac45+\frac34=\frac{31}{20}.
$$

Hence

$$
SQ=\frac{31}{40},
\qquad
RQ=\frac23,
$$

and

$$
PQ=\frac{31}{60}\approx0.5167.
$$

Averaging PQ across classes is not generally equivalent to multiplying separately averaged SQ and RQ.

Two equally sized true objects merged into one exact union provide a useful extreme case: semantic foreground IoU can be one, while each instance overlap is exactly one half and neither matches under the strict rule. Perfect foreground coverage does not imply correct instance recognition.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| Specify the semantic, instance, and panoptic output spaces. | Explain why instance identifiers can be permuted. |
| Derive pixelwise cross-entropy from a categorical likelihood. | State the label-exclusivity assumption. |
| Derive the Dice–IoU relationship. | Explain why averaging breaks the simple conversion. |
| Compute all-background accuracy and mean IoU. | Obtain 0.9 and 0.45 in the constructed image. |
| Explain what pooling indices retain. | Identify the values that unpooling cannot recover. |
| Show that transposed convolution is not an inverse. | Reproduce the matrix example. |
| Derive dilated-kernel span and stacked receptive field. | Distinguish sampled sites from enclosed area. |
| Construct center-offset targets. | Add the offsets back to recover both centers. |
| Explain why an external centroid is valid. | Identify coincident centers as a different problem. |
| Explain uniqueness of panoptic matching above one half. | Use non-overlap and the strict inequality. |
| Calculate PQ, SQ, and RQ from explicit masks. | Obtain thirty-one sixtieths for PQ. |
| Separate semantic coverage from instance correctness. | Explain the merged-object counterexample. |

## Why it matters for my work

The annotation ontology should determine whether a medical task needs semantic masks, separate instances, or overlapping label layers. I should evaluate object counts and boundaries separately when both affect the intended use.

## What I have not resolved

Quantify center collisions, offset errors, and boundary errors for the actual lesion shapes and image spacing in my data, rather than assuming non-convexity alone invalidates center regression.
