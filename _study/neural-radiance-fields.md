---
layout: study_note
title: "Neural Radiance Fields: A Scene Stored as a Function"
description: "NeRF replaces the 3-D data structure with a network you query. 5 MB holds what a voxel grid needs 500 MB for, and the bill arrives at 123 million network calls per frame."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Neural Networks & Representation"
order: 14
source: "Independent study"
written: true
updated: "2026-09-15"
---

Computer graphics goes from a model to an image. Computer vision goes from images to a model. NeRF is the second, and its answer to "what model" is unusual enough to be worth the whole note: **the scene is not a data structure. It is a function, and the function is a neural network.**

## Core question and definition

The network maps a 5-D input to a 2-D output:

$$
F_\Theta : (x, y, z, \theta, \phi) \longrightarrow (r, g, b, \sigma)
$$

Position in space and direction of view, to colour and volume density.[^nerf]

Two things earn their place there. **Density $$\sigma$$ depends only on position**: whether matter is present is not a matter of opinion. **Colour depends on position *and* direction**, which is what makes a wet surface bright from one angle and dull from another. A representation storing one colour per point cannot express specularity at all; that is why the input is 5-D rather than 3-D, and it is the cheapest possible fix for the problem.

Training needs only photographs and their camera poses: the latter recovered by classical structure-from-motion, which NeRF takes as given rather than contributing.[^colmap]

## Key concepts

### Rendering has to be differentiable, so it is an integral

To make a pixel, march a ray from the camera and accumulate:

$$
C(\mathbf r) = \int_{t_n}^{t_f} T(t)\,\sigma(\mathbf r(t))\,\mathbf c(\mathbf r(t), \mathbf d)\,dt,
\qquad
T(t) = \exp\!\left(-\int_{t_n}^{t}\sigma(\mathbf r(s))\,ds\right)
$$

$$T$$ is transmittance: the probability the ray got this far unobstructed. Once it passes through something dense, $$T$$ collapses and everything behind contributes nothing. That is occlusion, and it falls out of the integral rather than being coded.

The loss is then just squared error between rendered and photographed pixels. **Every operation is differentiable, so the gradient reaches back through the rendering into the weights**, and the network learns 3-D structure while never being shown any. It is supervised entirely by 2-D images.

Handling transparency, smoke and glass for free is a side effect: they are simply low $$\sigma$$, where a mesh would need a separate mechanism.

### The memory argument, and the bill

A network is a strange place to keep a scene until the numbers are compared. Against a dense voxel grid at 4 bytes per cell:

| representation | size | vs NeRF |
|---|---|---|
| NeRF MLP | ~5 MB | 1× |
| $$128^3$$ grid | 8.4 MB | 1.6× |
| $$256^3$$ grid | 67 MB | 12.8× |
| $$512^3$$ grid | **537 MB** | **102×** |

And the grid stores *density only*. Adding view-dependent colour multiplies it by the number of quantised directions; the MLP gets that dimension for free because it is a function of a continuous input rather than a table.

Then the cost. One $$800\times800$$ frame at 192 samples per ray is **122,880,000 network evaluations**. At 30 fps, 3.7 billion per second.

So the honest summary is a **trade of storage for computation**, and a steep one. Which is the right framing for the follow-up literature: everything since has been buying back the compute, and often by reintroducing the very grids NeRF removed, now as a cache.

### Positional encoding is what makes it work at all

Feeding raw $$(x,y,z)$$ produces blurry mush. The fix is the same one the [Transformer](/study/attention-and-the-transformer/) uses for a different reason: map each coordinate through a bank of sinusoids at geometrically increasing frequencies before the first layer.

The reason is **spectral bias**: an MLP on raw coordinates preferentially learns low-frequency functions, and a scene's detail is high-frequency. Two points a millimetre apart have nearly identical inputs, so the network must manufacture a sharp function of a slowly-varying input, which its inductive bias resists. The encoding makes nearby positions far apart in the input space at high frequencies, and the network no longer has to fight itself.

That the same construction solves "the model cannot see position" in one architecture and "the model cannot see *fine* position" in another is the kind of coincidence that is not one.

### What it cannot do

The scene is baked. Lighting, geometry and materials are entangled in weights, so you cannot relight it, move an object, or edit anything: you can only look from somewhere new. NeRF-in-the-wild handles varying illumination and transient occluders (tourists) by conditioning on per-image latent codes, which is a patch over the entanglement rather than a factorisation of it.[^nerfw]

## Why it matters for my work

The transferable idea is **the implicit neural representation**: store a signal as a function you query rather than as a sampled array, and get resolution-independence and compression together.

For medical imaging that is not a metaphor. A CT volume *is* a voxel grid, with exactly the cubic scaling above, and everything downstream inherits the sampling decision made at reconstruction. An implicit representation is queryable at arbitrary resolution, between slices included, which is the natural formulation of interpolating anisotropic data, where slice thickness typically exceeds in-plane resolution several-fold.

And the sparse-view case is the one that would matter most. NeRF reconstructs 3-D structure from a set of 2-D projections, which is a description of **tomographic reconstruction**. Dose is roughly proportional to projection count, so a method needing fewer views is a method needing less dose.

The caution is the one that should always attach to this. A NeRF trained on 100 photographs renders a plausible view from a new angle, and *plausible* is the operative word: the network interpolates and the result has no flag distinguishing measured structure from invented structure. In a photograph of a bulldozer that is fine. **In a reconstruction a radiologist will read, a confidently hallucinated feature is indistinguishable from a finding**, and the [faithfulness](/study/explanation-faithfulness-versus-plausibility/) problem arrives in its sharpest form: the output is an image, and images are trusted in a way that probability vectors are not.

## What I have not resolved

Whether uncertainty can be attached per-voxel to an implicit reconstruction in a way a reader could act on. The [ensemble approach](/study/bayesian-deep-learning-and-deep-ensembles/) suggests training several fields and rendering the disagreement as a confidence volume, but I do not know whether their disagreement tracks reconstruction error, or merely tracks where the sampling was sparse, which is related but not the same thing.

---

[^nerf]: Mildenhall, B., Srinivasan, P. P., Tancik, M., Barron, J. T., Ramamoorthi, R., & Ng, R. (2020). NeRF: Representing scenes as neural radiance fields for view synthesis. *ECCV*. [10.1007/978-3-030-58452-8_24](https://doi.org/10.1007/978-3-030-58452-8_24)

[^colmap]: Schönberger, J. L., & Frahm, J.-M. (2016). Structure-from-motion revisited. *CVPR*. [10.1109/CVPR.2016.445](https://doi.org/10.1109/CVPR.2016.445)

[^nerfw]: Martin-Brualla, R., Radwan, N., Sajjadi, M. S. M., Barron, J. T., Dosovitskiy, A., & Duckworth, D. (2021). NeRF in the wild: Neural radiance fields for unconstrained photo collections. *CVPR*. [arXiv:2008.02268](https://arxiv.org/abs/2008.02268)
