---
layout: study_note
title: "Invariance and Equivariance: Two Jobs One Network Cannot Do at Once"
description: "Deriving translation invariance and equivariance, including convolution, pooling, stride, boundaries, R-FCN position-sensitive pooling, and feature pyramids for detection."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Learning Models & Representation"
subgroup: "Spatial Models & Visual Prediction"
order: 13
source: "Independent study"
written: true
updated: "2026-09-15"
---

Move an object to the right without changing its identity. Its class should remain the same, while its coordinates should change.

These requirements are compatible within one network. An equivariant feature map can feed an invariant classification head and an equivariant localization head. The actual impossibility concerns a representation that has already discarded position: a later deterministic head cannot recover information that is absent from its input.

That qualification matters. Classification training does not prove that every intermediate feature has become position-blind, and convolution does not automatically make a complete network translation invariant.

## Transformations act on inputs and outputs differently

For a discrete one-dimensional signal, define translation by

$$
(T_\delta x)[n]=x[n-\delta].
$$

A positive displacement moves the signal to the right. For an image, the index and displacement become two-dimensional vectors, but the reasoning is unchanged.

An invariant function satisfies

$$
f(T_\delta x)=f(x).
$$

An equivariant function satisfies

$$
f(T_\delta x)=\rho_\delta f(x),
$$

where $$\rho_\delta$$ specifies how the output should transform. Writing the same translation symbol on both sides is convenient for feature maps, but it hides an important distinction: output transformations depend on the task.

For a box represented by its center, width, and height,

$$
b=(c_x,c_y,w,h),
$$

the appropriate transformation is

$$
\rho_\delta b
=
(c_x+\delta_x,c_y+\delta_y,w,h).
$$

For a detected object, the class remains unchanged while the box moves. For a set of detections, this transformation applies to every box; the ordering of the list is not itself part of the physical prediction.

Invariance is a special case of equivariance in which the output action is the identity. The question is therefore not whether a network “has equivariance.” It is which transformations act on which outputs.

Translations on an infinite lattice form a group:

$$
T_{\delta_1}T_{\delta_2}=T_{\delta_1+\delta_2},
\qquad
T_0=I,
\qquad
T_\delta^{-1}=T_{-\delta}.
$$

These identities support the algebra below. Cropping a translated image back into a fixed frame can destroy information, so that practical operation requires separate treatment.

## Deriving convolutional equivariance

Consider convolution with a fixed kernel:

$$
(C_kx)[n]
=
\sum_m k[m]x[n-m].
$$

Apply it to a shifted input:

$$
\begin{aligned}
(C_kT_\delta x)[n]
&=
\sum_m k[m](T_\delta x)[n-m]\\
&=
\sum_m k[m]x[n-m-\delta]\\
&=
(C_kx)[n-\delta]\\
&=
(T_\delta C_kx)[n].
\end{aligned}
$$

The crucial step is the third line. The kernel weights are unchanged, and the entire output expression is evaluated at a shifted location. This is what weight sharing buys.

Deep learning libraries commonly implement cross-correlation rather than mathematical convolution. Replacing the input index by $$n+m$$ changes the kernel orientation but not this argument.

Multiple channels also preserve the result:

$$
y_b[n]
=
\sum_a\sum_m k_{ba}[m]x_a[n-m]+b_b.
$$

The bias must be shared across spatial positions. A position-specific bias would introduce an absolute coordinate dependence.

A pointwise nonlinearity also commutes with translation:

$$
\begin{aligned}
\phi(T_\delta x)[n]
&=\phi(x[n-\delta])\\
&=(T_\delta\phi(x))[n].
\end{aligned}
$$

Finally, equivariance survives composition. If both layers commute with translation,

$$
g(f(T_\delta x))
=
g(T_\delta f(x))
=
T_\delta g(f(x)).
$$

Thus a stack of stride-one convolutions and pointwise nonlinearities is equivariant under the assumptions used in the proof. Padding, subsampling, coordinate channels, and spatially varying operations must be checked individually.

## A convolution example that can be checked entry by entry

Use a six-position circular signal, so indices wrap around:

$$
x=(0,1,0,0,0,0).
$$

Choose the operation

$$
y[n]=x[n]+2x[n-1].
$$

Only two output locations can be nonzero:

$$
y[1]=1+2(0)=1,
\qquad
y[2]=0+2(1)=2.
$$

Therefore

$$
y=(0,1,2,0,0,0).
$$

Shift the input by two positions:

$$
T_2x=(0,0,0,1,0,0).
$$

The same operation now produces

$$
C_k(T_2x)=(0,0,0,1,2,0)=T_2y.
$$

The output changes, but it changes predictably. This is equivariance, not invariance.

Now average the output:

$$
g(y)=\frac{1}{6}\sum_{n=0}^{5}y[n].
$$

Both versions give

$$
g(y)=g(T_2y)=\frac{3}{6}=\frac12.
$$

One computation has therefore produced a spatial representation that tracks translation and a scalar readout that ignores it. No contradiction is involved.

The example also separates two meanings of “same features.” The values appearing in the map are the same after translation, but their indexed locations are different. A localization head can use those locations even when a global average cannot.

## How pooling creates invariance, and where information is lost

Suppose a feature map is defined on a finite circular domain with $$N$$ sites. Global average pooling gives

$$
G(z)=\frac{1}{N}\sum_n z[n].
$$

Because circular translation permutes the sites,

$$
\begin{aligned}
G(T_\delta z)
&=
\frac{1}{N}\sum_n z[n-\delta]\\
&=
\frac{1}{N}\sum_m z[m]\\
&=
G(z).
\end{aligned}
$$

The change of variable is valid because every original site appears exactly once. Global maximum pooling is invariant for the same reason: permuting a collection does not change its maximum.

Now suppose an intermediate representation is exactly invariant:

$$
h(T_\delta x)=h(x).
$$

Every deterministic downstream head then satisfies

$$
q(h(T_\delta x))=q(h(x)).
$$

If the required localization output instead obeys

$$
b(T_\delta x)=\rho_\delta b(x)\ne b(x),
$$

that head cannot be correct on both inputs. This is an information bottleneck, not an optimization difficulty.

The conclusion does not apply to a backbone feature map merely because its final classifier was trained with image-level labels. If classification uses

$$
f(x)=q(G(h(x))),
$$

the loss constrains the composition. It does not require $$h(x)$$ itself to be invariant. The map can retain extensive spatial information that the pooling operation subsequently removes.

Nor does global pooling preserve every useful property. Two feature maps can have identical channel averages while containing different arrangements. An invariant readout deliberately identifies some distinct inputs with the same representation.

## Why stride breaks equivariance to single-pixel shifts

Define subsampling by stride $$s$$:

$$
(D_sx)[n]=x[sn].
$$

For a shift that is an integer multiple of the stride,

$$
\begin{aligned}
(D_sT_{s\delta}x)[n]
&=x[sn-s\delta]\\
&=x[s(n-\delta)]\\
&=(T_\delta D_sx)[n].
\end{aligned}
$$

A shift of $$s\delta$$ input pixels becomes a shift of $$\delta$$ output sites.

For a one-pixel shift, however,

$$
(D_sT_1x)[n]=x[sn-1].
$$

Those samples come from a different sampling phase. In general, no integer translation of the original subsampled output reproduces them.

For example, with stride two,

$$
x=(1,0,0,0),
\qquad
D_2x=(1,0).
$$

After shifting right by one,

$$
T_1x=(0,1,0,0),
\qquad
D_2T_1x=(0,0).
$$

The nonzero response disappeared. An output shift cannot turn a nonzero vector into the zero vector.

Local pooling does not magically remove this problem. Pool adjacent pairs by their maximum:

$$
x=(0,1,2,0,0,0)
\quad\longrightarrow\quad
(1,2,0).
$$

A circular one-position shift gives

$$
T_1x=(0,0,1,2,0,0)
\quad\longrightarrow\quad
(0,2,0).
$$

These pooled outputs are not translated copies. Two peaks that occupied different windows now occupy the same window.

Low-pass filtering before subsampling can reduce sensitivity to sampling phase by suppressing rapid variation. It does not, by itself, create exact discrete equivariance to every possible input shift.

## Finite images and padding change the problem

The infinite-lattice proof assumes access to all required input values. A finite image needs a boundary rule.

Take

$$
x=(1,2,3)
$$

and use a three-point sum with zero padding:

$$
y[n]=x[n-1]+x[n]+x[n+1].
$$

The output is

$$
y=(3,6,5).
$$

Shift the input right, discard the final element, and fill the new position with zero:

$$
T_1x=(0,1,2).
$$

Filtering gives

$$
C_k(T_1x)=(1,3,3).
$$

Shifting the previous output gives

$$
T_1(C_kx)=(0,3,6).
$$

They differ at the boundaries. The middle position still satisfies the expected relation because its computation has not encountered the changed boundary conditions.

Even global averaging is not invariant to this finite-frame operation:

$$
\operatorname{mean}(1,2,3)=2,
\qquad
\operatorname{mean}(0,1,2)=1.
$$

This is not a counterexample to the pooling proof. The shift here is not a permutation: one observed value has been removed.

When testing a model, distinguish translating a scene within a sufficiently large canvas from cropping away part of that scene. Also distinguish translating the entire image from moving one object relative to its background. The latter changes relationships within the scene and need not preserve the desired prediction.

## R-FCN uses position relative to a proposed region

R-FCN organizes score channels by class and relative position within a region of interest. For a grid with $$k$$ rows and columns, a class has $$k^2$$ position-sensitive maps.

For region $$R$$, let $$B_{ij}(R)$$ be its corresponding bin. A simplified class score is

$$
s_c(R)
=
\frac{1}{k^2}
\sum_{i,j}
\frac{1}{\lvert B_{ij}(R)\rvert}
\sum_{p\in B_{ij}(R)}
z_{cij}(p).
$$

The top-left bin reads the top-left channel, rather than all bins reading one undifferentiated class map.

The channel meaning is relative to the object or proposed region. Translating the whole image does not turn a top-left channel into a bottom-right channel. Instead, the spatial activation within the same channel translates.

A small construction makes this distinction explicit. Use four channels on a two-row, three-column map. Give each channel exactly one nonzero value:

| Channel | Nonzero coordinate, row and column | Value |
|---|---|---:|
| Top-left | $$(0,0)$$ | 8 |
| Top-right | $$(0,1)$$ | 8 |
| Bottom-left | $$(1,0)$$ | 8 |
| Bottom-right | $$(1,1)$$ | 8 |

All unlisted entries are zero. Let a two-by-two region use one spatial site per bin.

For the region covering columns zero and one, the selected values are

$$
(8,8,8,8),
$$

so its score is eight.

Move only the proposed region one column right. It now reads each channel at a location where that channel is zero, giving score zero.

Move both the feature maps and the region right together, and the score returns to eight.

The construction shows both desired behaviors: invariance to a joint translation of image evidence and proposal, and sensitivity to proposal misalignment relative to that evidence. It does not require an object to have a canonical semantic orientation.

## Feature pyramids combine resolutions, not transformation guarantees

A feature pyramid addresses a related but distinct issue: useful semantic evidence and fine spatial sampling may occur at different network depths.

Let $$C_l$$ denote a backbone map. A top-down construction can be written as

$$
T_L=W_L^{1\times1}*C_L,
$$

$$
T_l=W_l^{1\times1}*C_l+\operatorname{Up}(T_{l+1}),
$$

followed by

$$
P_l=W_l^{3\times3}*T_l.
$$

The lateral projections make the channel counts compatible. Upsampling makes the spatial shapes compatible. Addition combines information; the final convolution processes the combined map.

For a constructed example, suppose successive backbone maps have spatial sizes

$$
32\times32,\quad16\times16,\quad8\times8,\quad4\times4.
$$

Project every level to 64 channels. An upsampled deeper map can then be added to its shallower neighbor without changing that neighbor's spatial grid.

A projection from 256 channels to 64 channels needs

$$
256\cdot64=16{,}384
$$

weights before biases. The same weights operate at every site.

Upsampling cannot recover detail that the deeper branch never retained. The shallower branch supplies additional information. Conversely, combining several resolutions does not prove exact scale equivariance: changing object size can still alter sampling, receptive fields, and feature responses in complicated ways.

“Multi-scale features” describes an architectural resource. “Scale equivariance” is an algebraic property that requires its own definition and proof.

## Invariant predictions can still have spatially meaningful gradients

It is too strong to say that an invariant classifier cannot support a spatial attribution map.

Represent a circular translation by a permutation matrix $$P$$. Suppose a differentiable scalar classifier satisfies

$$
f(Px)=f(x).
$$

Differentiate with respect to $$x$$:

$$
P^{\mathsf T}\nabla f(Px)=\nabla f(x).
$$

Because a permutation matrix is orthogonal,

$$
PP^{\mathsf T}=I,
$$

multiplying by $$P$$ gives

$$
\nabla f(Px)=P\nabla f(x).
$$

The scalar prediction is invariant, while its input gradient is equivariant.

This does not prove that a gradient map is a faithful explanation of a decision. Gradients describe local sensitivity, and an explanation claim may require interventions or other evidence. It does show that output invariance and spatially structured sensitivity are mathematically compatible.

A classifier can recognize the same pattern wherever it appears and remain locally sensitive to the pixels currently forming that pattern.

## Turning the definitions into a diagnostic

For a feature map, an equivariance discrepancy can compare the two computation paths:

$$
E_\delta(x)
=
\frac{
\lVert F(T_\delta x)-\rho_\delta F(x)\rVert_2
}{
\lVert F(x)\rVert_2+\epsilon
}.
$$

The denominator controls for overall feature magnitude; the positive constant prevents division by zero. This is a diagnostic definition, not a universal quality metric.

The comparison must use compatible coordinates. A stride-four feature map should first be tested with shifts divisible by four. Boundary-affected sites can be excluded using a common valid region. For detection sets, boxes must be compared after accounting for translation and matching instances.

Training augmentation imposes a different kind of constraint. Shifted images should receive unchanged class labels but shifted localization targets. Success on sampled augmentations provides evidence of approximate behavior on those transformations. It does not establish an architectural identity over all inputs.

The transformation itself must also preserve the task. If location relative to anatomy is meaningful, moving an isolated finding while leaving the anatomy fixed can change the label. Equivariance is a statement about a specified action on the whole input–output pair, not permission to treat every geometric edit as irrelevant.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| Define the input translation and the corresponding output action separately. | Explain why box centers move while class labels do not. |
| Derive convolutional equivariance from the indexed sum. | Identify where weight sharing enters. |
| Explain invariant classification and equivariant localization in one network. | Use an equivariant map with separate readouts. |
| Prove that an exactly invariant bottleneck cannot recover absolute location. | Apply an arbitrary deterministic downstream head. |
| Derive the stride restriction. | Show why input shifts divisible by stride are special. |
| Construct a pooling counterexample. | Reproduce the adjacent-window example. |
| Explain the finite-boundary failure. | Identify the value that cropping removes. |
| Distinguish proposal-relative position from absolute position in R-FCN. | Move the proposal alone, then move image and proposal together. |
| Explain what FPN adds and what it does not guarantee. | Separate resolution fusion from scale equivariance. |
| Derive how an invariant scalar's gradient transforms. | Apply the chain rule to a permutation matrix. |

## Why it matters for my work

For medical localization, I should inspect where spatial information is retained and where it is discarded. Classification pre-training alone does not answer that question. Translation tests should separate sampling effects, boundary effects, and changes to anatomical relationships.

## What I have not resolved

Measure classification stability and localization equivariance separately for the backbone and heads I actually use, with boundary-controlled shifts and a stated coordinate convention.
