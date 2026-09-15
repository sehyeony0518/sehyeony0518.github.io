---
layout: study_note
title: "The Transfer Function Is a Gain, Not a Spectrum"
description: "Why H(s) sits in a different category from X(s) and Y(s), what the two numbers in H(jω) actually do to a sine, and why every pole must live in the left half-plane."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
order: 13
source: "Lecture notes, Ajou University"
written: true
updated: "2026-09-15"
---

Three Laplace transforms appear on the same page, and two of them are a different kind of object from the third. $$X(s)$$ and $$Y(s)$$ are **spectra** — they describe signals, things that exist in time and carry energy. $$H(s) = Y(s)/X(s)$$ is a **gain** — it describes a system, and it has no time-domain existence of its own.

Confusing the two is the most common way to misread a block diagram, and the confusion survives because all three are written the same way. A price analogy makes the distinction hard to lose: if an item costs 500 won and the price doubles, the 500 and the 1000 are prices, and the "2×" is not a price. It is what acts on prices. $$H$$ is the 2×.

## Core question and definition

The question that generates all of this: **feed a system a sinusoid — what comes out?**

For a linear time-invariant system, solve the differential equation the ordinary way. The homogeneous solution comes from the characteristic equation; the particular solution, for a sinusoidal input, can be found by guessing a sinusoid of the same frequency. What emerges has the shape

$$
y(t) = \underbrace{\textstyle\sum_i c_i e^{p_i t}}_{\text{transient, from the poles}} \;+\; \underbrace{|H(j\omega)|\,\sin\!\big(\omega t + \angle H(j\omega)\big)}_{\text{steady state}} .
$$

Two facts are packed into the second term, and both matter.

**The frequency does not change.** A sine goes in at $$\omega$$; a sine comes out at $$\omega$$. Not a distorted sine, not a sine plus harmonics — the same frequency. This is the defining privilege of linearity and time-invariance, and it is what makes frequency-domain analysis possible at all. A nonlinear system does not have this property, which is why none of what follows survives contact with a neural network.

**Only two numbers change.** The amplitude is multiplied by $$|H(j\omega)|$$ and the phase is shifted by $$\angle H(j\omega)$$. That is the entire effect of the system on that frequency. $$H(j\omega)$$ is a complex number whose magnitude is a gain and whose angle is a delay — nothing more is hiding in it.

### The worked example, checked numerically

Take $$H(s) = \dfrac{1}{s+1}$$ and drive it with $$\sin(10t)$$. Then

$$
H(j10) = \frac{1}{1 + j10}, \qquad |H(j10)| = \frac{1}{\sqrt{101}} = 0.099504, \qquad \angle H(j10) = -\arctan(10) = -84.289^\circ .
$$

I integrated the differential equation numerically and measured the steady-state output directly. The amplitude came out as $$0.099504$$ — agreeing with the prediction to within $$10^{-8}$$ — and the phase lag as $$-84.279^\circ$$. The prediction is not an approximation that happens to be close; it is exact, and the residual is integration error.[^lti]

It is worth pausing on the size of that attenuation. A signal at $$\omega = 10$$ comes out at about a tenth of its input amplitude and nearly a quarter-period late. Neither number was put into the system by hand. Both were already implicit in the single pole at $$s = -1$$, and computing $$H(j\omega)$$ is just reading them off.

## Key concepts

### A pole and a zero are not symmetric

They look symmetric on the page — roots of the denominator, roots of the numerator — and they are not.

A **pole** is a mode the system produces *on its own*. Set the input to zero and the system still rings at $$e^{p t}$$, because the homogeneous solution does not care what the input is. This is output you did not ask for. A **zero** is the opposite: at that frequency the input goes in and *vanishes*, producing nothing. One is uninvited output; the other is swallowed input.

The asymmetry has a practical edge. An uninvited mode that grows is a catastrophe; an input that vanishes is merely a limitation. That is why stability is stated entirely in terms of poles and says nothing about zeros.

### Why the left half-plane, quantitatively

A pole at $$s = \sigma + j\omega$$ contributes $$e^{\sigma t}$$ to the response. If $$\sigma > 0$$ that term grows without bound, and this is where the "you did not ask for it" framing earns its keep.

Nobody injects the unstable mode. It is seeded by whatever noise is present — thermal noise, quantisation, a rounding error. I simulated a system with a right-half-plane pole at $$\sigma = 1$$ seeded by a perturbation of $$10^{-12}$$, and the output crossed unity at $$t = 27.6\,\text{s}$$. From an initial disturbance twelve orders of magnitude below the signal, the system reaches full scale in under half a minute, and there is nothing in the input that explains it. *Every* pole must satisfy $$\operatorname{Re}(p_i) < 0$$; one bad pole out of ten is still an unstable system, because the growing exponential eventually dominates every decaying one no matter how small its coefficient starts.

A small aside on notation that is more than pedantry: the convention is **left half-plane**, written LHP, and the "hand" is doing real work. In English *left* also means "remaining" and *right* also means "correct", so "the left side" and "the right side" are both ambiguous in a way that "the left-hand side" and "the right-hand side" are not. The redundancy is there to kill the ambiguity.

### Reading the Bode plot as two separate questions

Plotting $$|H(j\omega)|$$ in decibels against $$\log \omega$$, and $$\angle H(j\omega)$$ against $$\log \omega$$, answers the two questions separately: how much does this frequency get scaled, and how much does it get delayed. The log-log choice is what makes the magnitude plot a set of straight lines — products become sums, and each pole or zero contributes an independent slope.

For the single pole above, the magnitude is flat until $$\omega = 1$$ and then falls at $$-20$$ dB/decade. The corner sits exactly at $$|p|$$, and at that corner the gain is $$-3.01$$ dB — half power. The pole location is not an abstract root; it is the frequency at which the system starts giving up.

### The integrator and the differentiator as frequency weights

$$1/s$$ and $$s$$ are the two simplest transfer functions and they are exact opposites as frequency weights:

| $$\omega$$ | $$\lvert 1/j\omega \rvert$$ | $$\lvert j\omega \rvert$$ |
|---|---|---|
| 0.01 | 100 | 0.01 |
| 1 | 1 | 1 |
| 100 | 0.01 | 100 |

An integrator amplifies low frequencies and suppresses high ones — it smooths, and it has infinite gain at DC, which is the fact that later makes integral control able to drive steady-state error to zero. A differentiator does the reverse, which is exactly why differentiating a noisy measurement is a bad idea: the noise lives at high frequency and the differentiator is a high-frequency amplifier. Neither of these is a rule to memorise; both are read directly off $$|H(j\omega)|$$.

## Why it matters for my work

The habit worth taking from this is the **category distinction**, not the algebra. When I write down a pipeline — images in, predictions out — it is worth asking which objects in it are signals and which are gains. A calibration temperature, a class-weight, a learning rate: these act on things, and they are not themselves the things. Treating a gain as if it were a signal is how one ends up "normalising" a quantity that was never a distribution.

The second transferable idea is that **the transient is not the system**. Everything that decays is gone in steady state, and the steady-state behaviour is a property of the poles alone. The analogue in training is that the early loss curve is mostly transient, and reading a final property off it is reading the wrong part of the trajectory.

The third is the sharpest: an unstable mode needs no input. In a deployment loop where a model's outputs influence the data it later trains on, there is a feedback path, and if its loop gain exceeds one there is a mode that grows from nothing but noise. The linear theory does not transfer, but the *question* does — is there a path by which this system's own output re-enters its input, and what is the gain around it?

## What I have not resolved

The eigenfunction property is what makes all of this work, and it holds only for LTI systems. I can state precisely what is given up for a nonlinear model — no characteristic equation, no finite pole set, no decay theorem — but I do not have a useful substitute. Lyapunov analysis is the textbook answer and it requires a candidate function I would have to invent per system.

I also do not have a good sense of how much the LHP criterion degrades under discretisation. A continuous-time system with all poles in the LHP maps to the unit disc in $$z$$, but the mapping depends on the sampling rate, and I have not worked out how close to the boundary one can sit before sample-rate jitter matters.

---

Sources: the eigenfunction property of complex exponentials for LTI systems, the pole/zero characterisation of the transfer function, and the left-half-plane stability criterion are standard results in linear systems theory. The numerical claims here — the gain and phase at $$\omega = 10$$ for $$1/(s+1)$$ checked against direct integration, the $$-3$$ dB point coinciding with the pole magnitude, the growth time of a noise-seeded unstable mode, and the integrator/differentiator weighting table — were computed directly.

[^lti]: The agreement is exact in principle because the steady-state response of an LTI system to a sinusoid *is* $$|H(j\omega)|\sin(\omega t + \angle H(j\omega))$$ — this is a theorem, not a fit. The measured discrepancy of $$9.7 \times 10^{-9}$$ reflects the tolerance of the numerical integrator and the finite time allowed for the transient to decay, not any error in the prediction.
