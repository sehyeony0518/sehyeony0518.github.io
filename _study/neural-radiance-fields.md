---
layout: study_note
title: "Neural Radiance Fields: A Scene Stored as a Function"
description: "Deriving NeRF camera rays, volume density, transmittance, alpha compositing, rendering gradients, positional encoding, and the storage-computation tradeoff against voxel grids."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Neural Networks & Representation"
order: 14
source: "Independent study"
written: true
updated: "2026-09-15"
---

A neural radiance field represents a scene through functions queried at spatial coordinates and viewing directions. Rendering evaluates those functions along camera rays and combines the returned quantities into pixels.

The representation does not eliminate data structures: network weights are a data structure. Its distinctive choice is to encode a continuous field through shared parameters instead of storing an independent value at every spatial sample.

Nor does continuity guarantee recovered detail. A function can be queried between observed samples while remaining uncertain or wrong there.

## What the field predicts

A basic radiance-field model predicts density and color:

$$
\sigma=\sigma_\theta(\mathbf x),
$$

$$
\mathbf c=\mathbf c_\theta(\mathbf x,\mathbf d).
$$

Position has three degrees of freedom. A unit viewing direction has two, although it is often represented by three constrained Cartesian components. The conventional description is therefore a five-dimensional input with four scalar outputs: density and three color channels.

Density is nonnegative:

$$
\sigma(\mathbf x)\ge0.
$$

It acts as an extinction coefficient in the renderer, with units of inverse distance. It should not automatically be interpreted as physical mass density or as a calibrated probability that matter exists.

Color depends on direction so that the representation can fit view-dependent appearance. Density is held independent of direction in this basic factorization, providing a shared spatial structure across views.

This does not produce an explicit decomposition into geometry, material, and illumination. A direction-dependent color field can reproduce some appearance changes without explaining the physical light transport that caused them.

Training requires images and an associated camera model. Camera poses and intrinsics can be supplied, estimated separately, or optimized in an extended method, but they are part of the inverse problem rather than information that rendering makes unnecessary.

## Constructing a camera ray

In a pinhole model, a homogeneous pixel coordinate is

$$
\tilde p=(u,v,1)^{\mathsf T}.
$$

Given the camera intrinsic matrix $$K$$, a corresponding camera-coordinate direction is proportional to

$$
K^{-1}\tilde p.
$$

Normalize it and rotate it into world coordinates:

$$
\mathbf d
=
R
\frac{K^{-1}\tilde p}{\lVert K^{-1}\tilde p\rVert_2}.
$$

If the camera center is $$\mathbf o$$, the ray is

$$
\mathbf r(t)=\mathbf o+t\mathbf d.
$$

With a unit direction, $$t$$ measures distance along the ray. Without normalization, interval lengths must include the direction vector's norm when converting density into optical thickness.

For a constructed camera, let both focal lengths be two and the principal point be zero. Pixel coordinates

$$
(u,v)=(2,0)
$$

give an unnormalized direction

$$
(1,0,1).
$$

With identity rotation,

$$
\mathbf d=\frac{(1,0,1)}{\sqrt2}.
$$

Starting at the origin and traveling distance $$\sqrt2$$ reaches

$$
\mathbf r(\sqrt2)=(1,0,1).
$$

This connects image coordinates to the three-dimensional locations queried by the network. Pixel-center conventions, coordinate handedness, and camera-to-world versus world-to-camera transformations must remain consistent.

## Deriving transmittance from local attenuation

Let $$T(t)$$ be the fraction of radiance surviving from the near boundary to distance $$t$$.

Over a sufficiently short interval,

$$
T(t+\Delta t)
=
T(t)\left(1-\sigma(\mathbf r(t))\Delta t\right)
+
o(\Delta t).
$$

Subtract the current value, divide by the interval, and take the limit:

$$
\frac{dT}{dt}
=
-\sigma(\mathbf r(t))T(t).
$$

For positive transmittance,

$$
\frac{d\log T}{dt}
=
-\sigma(\mathbf r(t)).
$$

With initial condition

$$
T(t_n)=1,
$$

integration yields

$$
T(t)
=
\exp\left(
-\int_{t_n}^{t}\sigma(\mathbf r(s))\,ds
\right).
$$

The exponential is therefore a consequence of multiplicative survival through successive small intervals.

The quantity

$$
T(t)\sigma(\mathbf r(t))
$$

is the rate at which surviving weight terminates at that location. Since

$$
-T'(t)=T(t)\sigma(\mathbf r(t)),
$$

its integral is

$$
\int_{t_n}^{t_f}T(t)\sigma(\mathbf r(t))\,dt
=
1-T(t_f).
$$

The remaining weight reaches the far boundary.

This survival interpretation belongs to the rendering model. It is not a posterior uncertainty distribution over possible scenes.

## The rendering equation and its background term

Under an emission–absorption model, the rendered color is

$$
\mathbf C(\mathbf r)
=
\int_{t_n}^{t_f}
T(t)\sigma(\mathbf r(t))
\mathbf c(\mathbf r(t),\mathbf d)\,dt
+
T(t_f)\mathbf c_{\mathrm{bg}}.
$$

The first term accumulates visible contributions from the field. The second accounts for radiance that survives through the modeled interval and reaches a background.

Without the background term, the accumulated weights need not sum to one. An apparently dark pixel may then reflect missing opacity rather than dark local color.

Occlusion appears through transmittance: density closer to the camera reduces the weight available to farther locations.

The integral is used because the model describes a continuous medium along a ray. Being an integral is not what makes it differentiable. Differentiability depends on the field parameterization, integrand, approximation, and any discrete operations around the renderer.

The model also has physical limits. Straight-ray emission–absorption rendering does not automatically simulate refraction through glass, multiple scattering, or arbitrary relighting. Fitting images containing those effects is not the same as recovering their physical causes.

## Deriving discrete alpha compositing

Divide the ray into intervals of lengths $$\Delta_i$$. Approximate density and color as constant within interval $$i$$.

The probability mass, or opacity weight, absorbed within that interval conditional on reaching it is

$$
\alpha_i
=
\int_0^{\Delta_i}
\sigma_i e^{-\sigma_i s}\,ds.
$$

Integrating,

$$
\alpha_i
=
1-e^{-\sigma_i\Delta_i}.
$$

The transmittance entering the interval is

$$
T_i
=
\exp\left(
-\sum_{j<i}\sigma_j\Delta_j
\right)
=
\prod_{j<i}(1-\alpha_j).
$$

Its contribution weight is

$$
w_i=T_i\alpha_i.
$$

The rendered approximation becomes

$$
\hat{\mathbf C}
=
\sum_iw_i\mathbf c_i
+
T_{N+1}\mathbf c_{\mathrm{bg}}.
$$

The weights have a useful telescoping identity:

$$
w_i=T_i-T_{i+1}.
$$

Therefore

$$
\sum_{i=1}^{N}w_i
=
1-T_{N+1}.
$$

Including the background weight makes the total exactly one.

For small optical thickness,

$$
\sigma_i\Delta_i\ll1,
$$

the exponential expansion gives

$$
\alpha_i
=
1-\left(1-\sigma_i\Delta_i+\cdots\right)
\approx\sigma_i\Delta_i.
$$

The linear approximation is useful for intuition, but it can exceed one for large thickness. The exponential expression remains bounded between zero and one for nonnegative density.

## A three-slab rendering calculation

Construct three unit-length intervals with densities

$$
\sigma_1=\log2,
\qquad
\sigma_2=\log2,
\qquad
\sigma_3=\log4.
$$

Their opacities are

$$
\alpha_1=\frac12,
\qquad
\alpha_2=\frac12,
\qquad
\alpha_3=\frac34.
$$

The incoming transmittances are

$$
T_1=1,
\qquad
T_2=\frac12,
\qquad
T_3=\frac14.
$$

Thus

$$
w_1=\frac12,
\qquad
w_2=\frac14,
\qquad
w_3=\frac3{16}.
$$

The remaining transmittance is

$$
T_4
=
\frac12\cdot\frac12\cdot\frac14
=
\frac1{16}.
$$

Assign red, green, and blue to the intervals:

$$
\mathbf c_1=(1,0,0),
\quad
\mathbf c_2=(0,1,0),
\quad
\mathbf c_3=(0,0,1),
$$

and use a white background:

$$
\mathbf c_{\mathrm{bg}}=(1,1,1).
$$

The rendered color is

$$
\begin{aligned}
\hat{\mathbf C}
&=
\frac12(1,0,0)
+
\frac14(0,1,0)
+
\frac3{16}(0,0,1)
+
\frac1{16}(1,1,1)\\
&=
\left(
\frac9{16},
\frac5{16},
\frac4{16}
\right).
\end{aligned}
$$

The weights sum to

$$
\frac8{16}+\frac4{16}+\frac3{16}+\frac1{16}=1.
$$

Every number follows from the specified densities, interval lengths, and colors.

A second implementation of this example should reproduce both the color and the remaining background weight. Matching only the RGB output can conceal a compensating error in opacity or background handling.

## Depth is another weighted quantity, with a convention attached

Suppose the three intervals are represented by depths one, two, and three. Using the discrete weights, the unnormalized depth moment is

$$
\sum_iw_it_i
=
\frac12(1)+\frac14(2)+\frac3{16}(3)
=
\frac{25}{16}.
$$

The total foreground weight is

$$
\frac{15}{16}.
$$

Conditioning on termination within the modeled foreground gives

$$
\hat D_{\mathrm{conditional}}
=
\frac{\sum_iw_it_i}{\sum_iw_i}
=
\frac{25}{15}
=
\frac53.
$$

Using the unnormalized moment instead gives a different number. Assigning the surviving background mass a far-plane depth gives another.

These are not interchangeable depth definitions. A reported depth map should state whether it is conditioned on opacity, includes the background, or uses another statistic such as a maximum-weight sample.

The sample depths also approximate where termination occurs within an interval. Exact interval opacity does not imply an exact depth moment when the entire interval is represented by one location.

## How rendering sends gradients to the field

For squared photometric loss,

$$
L=
\frac12
\left\lVert
\hat{\mathbf C}-\mathbf C_{\mathrm{target}}
\right\rVert_2^2,
$$

the color derivative is

$$
\frac{\partial L}{\partial\hat{\mathbf C}}
=
\hat{\mathbf C}-\mathbf C_{\mathrm{target}}.
$$

Holding densities fixed, the derivative of rendered color with respect to interval color is simply its weight:

$$
\frac{\partial\hat{\mathbf C}}{\partial\mathbf c_i}
=
w_iI.
$$

For the density derivative, collect everything behind interval $$i$$ into a conditional color $$\mathbf B_i$$. Then

$$
\hat{\mathbf C}
=
\mathbf C_{\mathrm{before}}
+
T_i
\left[
\alpha_i\mathbf c_i
+
(1-\alpha_i)\mathbf B_i
\right].
$$

Since

$$
\frac{\partial\alpha_i}{\partial\sigma_i}
=
\Delta_i(1-\alpha_i),
$$

we obtain

$$
\frac{\partial\hat{\mathbf C}}{\partial\sigma_i}
=
T_i\Delta_i(1-\alpha_i)
(\mathbf c_i-\mathbf B_i).
$$

Increasing density replaces some contribution from behind with the interval's own color. It does not merely “add more color.”

For interval two in the slab example, the conditional color behind it is

$$
\mathbf B_2
=
\frac34(0,0,1)+\frac14(1,1,1)
=
\left(\frac14,\frac14,1\right).
$$

Therefore

$$
\frac{\partial\hat{\mathbf C}}{\partial\sigma_2}
=
\frac12\cdot1\cdot\frac12
\left[
(0,1,0)-\left(\frac14,\frac14,1\right)
\right]
=
\left(
-\frac1{16},\frac3{16},-\frac14
\right).
$$

The renderer provides a concrete gradient path, but a useful gradient is not the same as unique recovery of the scene.

## Photometric agreement does not identify a unique field

Consider one grayscale interval against a black background. Its rendered value is

$$
y=\alpha c.
$$

The measurement

$$
y=\frac14
$$

is consistent with both

$$
\alpha=\frac12,\qquad c=\frac12,
$$

and

$$
\alpha=\frac14,\qquad c=1.
$$

For unit interval length, the corresponding densities are

$$
\sigma=\log2
$$

and

$$
\sigma=-\log\frac34.
$$

Both produce the same pixel despite assigning different opacity and color.

Additional views and shared spatial parameterization constrain these ambiguities, but do not guarantee complete identifiability. Unobserved regions can remain unconstrained. Camera error, exposure variation, and overly flexible appearance can also trade off against geometry.

A low training-image loss therefore establishes consistency with those measurements under the chosen renderer. It does not establish that every reconstructed surface is correct.

## Fourier features and sampling

A coordinate encoding can provide sinusoidal features:

$$
\gamma_L(x)
=
\left[
\sin(\pi x),\cos(\pi x),
\ldots,
\sin(2^{L-1}\pi x),\cos(2^{L-1}\pi x)
\right].
$$

For three frequency pairs, compare coordinates zero and one quarter. At zero, every pair is

$$
(0,1).
$$

At one quarter, the pairs are

$$
\left(\frac{\sqrt2}{2},\frac{\sqrt2}{2}\right),
\qquad
(1,0),
\qquad
(0,-1).
$$

Higher frequencies create larger feature changes over shorter coordinate distances. Their derivatives contain the corresponding frequency factors:

$$
\frac{d}{dx}\sin(\omega x)=\omega\cos(\omega x).
$$

This changes the functions the network can represent and learn conveniently. It does not create evidence for details absent from the observations, and periodic features can introduce their own ambiguities.

Ray sampling also matters. A coarse pass can assign weights to intervals and use normalized weights to concentrate later samples.

For interval probabilities

$$
(0.5,0.25,0.25),
$$

the cumulative probabilities are

$$
(0.5,0.75,1).
$$

A uniform draw of 0.7 selects the second interval. If that interval spans one to two and density is uniform within the proposal bin, the sampled location is

$$
1+\frac{0.7-0.5}{0.25}=1.8.
$$

This is an inverse-CDF construction. The resulting rendering procedure must still account for the new sample spacing. Concentrating samples is a numerical strategy, not an uncertainty estimate.

## Storage, computation, and the tomography distinction

Construct an MLP with one million parameters stored as 32-bit floats. Its parameter storage is

$$
10^6\cdot4=4{,}000{,}000
$$

bytes, excluding activations and optimizer state.

A grid with 128 samples per axis contains

$$
128^3=2{,}097{,}152
$$

cells. One float per cell uses eight MiB. Density plus three color channels uses 32 MiB. Doubling all three dimensions multiplies storage by eight.

These figures compare specified representations, not equal reconstruction quality. There is no universal compression ratio between a neural field and a voxel grid.

A constructed image of 256 by 256 pixels, sampled at 64 positions per ray, requires

$$
256\cdot256\cdot64=4{,}194{,}304
$$

field-query points. Those queries can be batched; they are not necessarily separate network launches.

The implicit-field idea can transfer to tomography, but the forward model must change. For ideal monochromatic transmission,

$$
I=I_0\exp\left(-\int\mu(\mathbf r(t))\,dt\right).
$$

Taking a negative logarithm gives

$$
-\log\frac{I}{I_0}
=
\int\mu(\mathbf r(t))\,dt.
$$

That line integral of attenuation is not the NeRF RGB emission–absorption integral. A neural attenuation field must be trained through the appropriate measurement model.

Arbitrary-resolution queries do not increase the information in the measured projections. Sparse measurements and noise still constrain what can be recovered.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| State the field's input degrees of freedom and four scalar outputs. | Distinguish density from color and uncertainty. |
| Construct a normalized camera ray. | Reproduce the focal-length example. |
| Derive transmittance from local survival. | Solve the attenuation differential equation. |
| Derive interval opacity. | Integrate constant density over one interval. |
| Prove the weight-sum identity. | Include the surviving background weight. |
| Render the three colored slabs. | Obtain nine sixteenths, five sixteenths, and one quarter. |
| Explain competing depth conventions. | Calculate the conditional depth of five thirds. |
| Derive the density gradient. | Interpret color replacement and occlusion. |
| Construct an ambiguous opacity-color pair. | Reproduce the same grayscale measurement twice. |
| Explain what Fourier features and extra samples change. | Separate representation and numerical accuracy from new evidence. |
| Calculate storage and query counts. | State precision and all included components. |
| Distinguish radiance rendering from transmission tomography. | Write the correct forward operator for each. |

## Why it matters for my work

The transferable idea is a coordinate-based signal representation trained through an explicit measurement model. For medical reconstruction, that model and its identifiability limits matter more than the ability to render a visually plausible image.

## What I have not resolved

Determine whether uncertainty from repeated field fits predicts reconstruction error in unobserved regions, rather than only disagreement among optimization runs.
