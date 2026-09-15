---
layout: study_note
title: "Bayesian Inverse Problems in Imaging"
description: "Denoising and restoration written as inference: an acquisition model as the likelihood, an image prior as the assumption, and what a Markov random field assumes to stay computable."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "math-foundations"
category_title: "Mathematical & Statistical Foundations"
order: 9
source: "Independent study"
written: true
updated: "2026-09-15"
---

A clean image $$x$$ passes through an acquisition process and arrives as $$y$$. Recovering $$x$$ from $$y$$ is an inference problem, and writing it that way makes the assumptions visible — which is the reason to write it that way even when a learned model will do the work.

## Core question and definition

The generative direction is the one that can be modelled honestly: $$x$$ is what exists, $$y$$ is what the sensor produced. Inference runs the other way.

$$
p(x \mid y) \;\propto\; p(y \mid x)\, p(x).
$$

The likelihood $$p(y \mid x)$$ is the **acquisition model** — blur, subsampling, noise, whatever the physics does. The prior $$p(x)$$ is the statement of what images look like. Without it, the estimate that maximises the likelihood is the trivial one: assume nothing was corrupted and return $$y$$.

Because the normalising constant requires integrating over all images, the usual move is to drop it and take the mode:

$$
\hat{x} = \arg\max_x \; \big[\log p(y \mid x) + \log p(x)\big].
$$

Under additive Gaussian noise the first term becomes a squared-error fit to the observation, and the second becomes a penalty. Restoration then reads as a fidelity term plus a regulariser — which is where most classical image processing already was, arrived at from the other direction.

## Key concepts

### The prior is the hard half, and it is a choice

An image of a thousand by a thousand pixels is a million random variables. Writing $$p(x)$$ over that jointly is not something anyone does directly.

The **Markov property** is the assumption that makes it possible: conditioned on its neighbours, a pixel is independent of everything further away. Assume that, and the joint distribution factorises over cliques — the fully connected subsets of the neighbourhood graph. With pairwise cliques only, the prior becomes a sum over adjacent pairs:

$$
-\log p(x) \;=\; \sum_{(i,j)\in\mathcal{N}} \psi(x_i, x_j) + \text{const}.
$$

Choosing $$\psi$$ to penalise difference is the statement that neighbouring pixels should be similar. That is a small assumption written in few parameters, and for a hand-designed prior it is a reasonable one. [Besag](https://doi.org/10.1111/j.2517-6161.1974.tb00999.x) (1974) worked out the lattice case; [Geman and Geman](https://doi.org/10.1109/TPAMI.1984.4767596) (1984) connected Gibbs distributions to Bayesian image restoration.

What matters is that the smoothness is an assumption about images, not a fact about them. Edges violate it, and the whole subsequent literature on edge-preserving priors is the admission.

### Learning the prior changes which problem is being solved

Setting $$\psi$$ by hand caps how good the prior can be. Learning it means the parameters of the prior are also unknown, alongside the image — which is the both-unknown case, and why [EM and variational methods](/study/latent-variables-em-and-variational-inference/) turn up here. A learned restoration model is doing this implicitly: the prior is in the weights, and it is no longer inspectable as a few parameters.

That trade is worth naming. The hand-written prior is weaker and legible. The learned prior is stronger and is an assumption you can no longer read.

### Sequential estimation is the same structure over time

When the hidden quantity evolves — an object moving, a patient's state changing — the estimate can be carried forward rather than recomputed. Recursive Bayesian estimation predicts the state from the previous estimate through a transition model, then corrects it against the new observation.

Particle filters represent the distribution by samples rather than in closed form, which is what allows non-Gaussian, multi-modal beliefs: the cloud of particles is diffuse when position is uncertain and concentrates as observations accumulate. [Arulampalam and colleagues](https://doi.org/10.1109/78.978374) (2002) give the standard treatment; [Rabiner](https://doi.org/10.1109/5.18626) (1989) covers the discrete case as hidden Markov models.

## Where this touches my work

The acquisition model is the part I care about most, and for an unwelcome reason. In restoration, $$p(y \mid x)$$ is written down deliberately because it has to be. In a diagnostic pipeline the same process is present and is usually never written down at all — and it is the process through which scanner, operator and protocol enter the image. Formulating restoration Bayesian-style is good practice for naming an acquisition model, which is the thing an evidence audit needs and rarely has.

The second transfer is about priors. A restoration prior that prefers smoothness will suppress a small bright structure, because that is what it was asked to do. Applying restoration or enhancement before a diagnostic model therefore inserts an assumption between the patient and the prediction, and whether that assumption is compatible with the finding being sought is a question I have not seen asked often enough.

## What I have not resolved

Whether the acquisition model for clinical ultrasound can be specified well enough to be useful, given that operator behaviour — probe angle, gain, depth, which frame gets saved — is part of the process and is not a physics term.

## References

- Besag (1974). [Spatial Interaction and the Statistical Analysis of Lattice Systems](https://doi.org/10.1111/j.2517-6161.1974.tb00999.x). *JRSS B*.
- Geman & Geman (1984). [Stochastic Relaxation, Gibbs Distributions, and the Bayesian Restoration of Images](https://doi.org/10.1109/TPAMI.1984.4767596). *IEEE TPAMI*.
