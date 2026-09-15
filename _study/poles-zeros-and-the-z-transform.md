---
layout: study_note
title: "Poles and Zeros: What Comes Out Uninvited, and What Goes In and Vanishes"
description: "Why exponentials are the natural test input for a linear system, the physical reading of a pole and a zero, and how a plot of two sets of points summarises a whole system."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
order: 2
source: "Independent study"
written: true
updated: "2026-09-15"
---

Given a system described by a difference equation, one question organises everything: **feed in $$\alpha^n$$ — what comes out?**

It looks like an arbitrary choice of test input. It is not, and the reason is the whole content of the z-transform.

## Core question and definition

Solve it the ordinary way, the way one solves a linear difference equation: find the homogeneous solution from the characteristic equation, then a particular solution. Guessing $$C\alpha^n$$ for the particular part works — substituting it in leaves an equation for $$C$$ alone — and the general answer has the shape

$$
y[n] = \underbrace{\text{terms from the characteristic roots}}_{\text{transient}} \;+\; \underbrace{H(\alpha)\,\alpha^n}_{\text{steady state}} .
$$

The second term is the point. After the transient dies away, the output is **the input multiplied by a single number**. The shape is untouched; only the amplitude and phase change.

That makes $$\alpha^n$$ an **eigenfunction** of any linear time-invariant system, with eigenvalue

$$
H(z) = \sum_n h[n]\,z^{-n},
$$

the z-transform of the impulse response. (Verified directly: feeding $$\alpha^n$$ through a filter and comparing against $$H(\alpha)\alpha^n$$ agrees to machine precision once the transient has passed.)

So the z-transform is not a formal device that happens to simplify convolution. It is the list of eigenvalues of the system, indexed by which exponential you feed it.

## Key concepts

### A pole is what comes out without being put in

$$H(z)$$ is a ratio of polynomials, so it has poles where the denominator vanishes and zeros where the numerator does. Both have readings in terms of that first question.

**Poles come from the characteristic equation** — the *homogeneous* part, the part of the solution that does not depend on the input at all. So a pole is a mode the system produces on its own: **output that appears without being put in**.

Which makes stability immediate. If a pole lies inside the unit circle its mode decays and the transient dies. If it lies outside, the mode grows without bound, and the system produces ever-larger output from an input that never asked for it. *Stable* means every pole inside the unit circle, and now that is a statement about behaviour rather than a rule to memorise.

### A zero is what goes in and does not come out

A zero is the mirror image: $$H(\alpha) = 0$$, so feed in $$\alpha^n$$ and **nothing comes out**. Not attenuated — annihilated.

This is worth seeing concretely. Take a ten-tap moving sum, $$y[n] = \sum_{k=0}^{9} x[n-k]$$. Its zeros sit at the ten 10th roots of unity except $$z=1$$, and feeding it a sinusoid of period exactly 10 produces an output that is **identically zero** — because every window of ten samples spans a complete period, and a complete period of a sinusoid sums to nothing.

Meanwhile at $$z=1$$ the gain is 10: DC passes at full strength. A pole–zero plot of that filter is a picture of a system that passes constants and completely erases specific periodicities, and reading it took no calculation.

### Walking the unit circle

Set $$z = e^{j\omega}$$ and the z-transform becomes the DTFT. Sweeping $$\omega$$ from $$0$$ to $$\pi$$ walks around the unit circle from DC to Nyquist, and $$|H|$$ along that path is the gain at each frequency while $$\angle H$$ is the phase shift.

That gives the pole–zero plot its practical value: **pass near a pole and the response rises; pass near a zero and it falls.** A pole near $$z=1$$ with zeros out near $$z=-1$$ is a lowpass filter, and you know that before computing anything. Sketching the magnitude and phase from a pole–zero plot — roughly, not precisely — is the skill that makes a filter's behaviour legible at a glance.

### The ROC is part of the answer

One subtlety that is easy to skip and expensive to skip. $$H(z)$$ as an algebraic expression does not determine the signal; the **region of convergence** is part of the specification, and the same formula with different ROCs is a different signal entirely.

The ROC is an annulus, and its shape says what kind of signal you have. Extending outward from the outermost pole means causal; extending inward means anticausal; a band between poles means two-sided. And **the DTFT exists exactly when the ROC contains the unit circle** — which is the same condition as stability, arriving from a different direction.

## Why it matters for my work

The pole–zero reading gives me a vocabulary I keep wanting for machine-learning systems, and the honest position is that the vocabulary transfers while the theorems do not.

The zero is the sharper half. A zero is an input the system maps exactly to nothing, and a system's zeros are invisible from its outputs — you cannot discover what a filter deletes by examining what it passes. That is the structure of a [blind spot](/study/shortcut-learning-in-medical-imaging/): a finding a model is constitutionally unable to respond to will never appear in any error analysis over cases the model saw, because those cases produce no distinctive output to analyse. Finding zeros requires probing deliberately for them, which is [exploration rather than evaluation](/study/monte-carlo-tree-search/).

The pole is the [deployment loop](/study/feedback-control-and-deployment-loops/) in miniature: output that appears without corresponding input, growing on its own when the loop's own dynamics put it outside the unit circle.

Where the analogy stops is worth stating plainly. All of this rests on linearity and time-invariance, and a deep network has neither. There is no characteristic equation for it, no finite set of poles, no theorem that says a given mode decays. What survives is the *question* — what does this system produce on its own, and what can it never produce — and the recognition that for a nonlinear model those questions have no closed-form answer and must be attacked empirically. Knowing precisely which guarantees are being given up is the useful part of knowing the linear theory.

---

Sources: the eigenfunction property of exponentials for LTI systems, the pole/zero and ROC characterisations of causality and stability, and the zeros of a moving-sum filter are standard results in discrete-time signal processing. The numerical claims here (the eigenfunction identity, the vanishing output at the 10th roots of unity, and the DC gain of 10) were computed directly.
