---
layout: study_note
title: "All-Pass Systems and Group Delay: Distortion That Every Magnitude Test Passes"
description: "A system that leaves every frequency's amplitude untouched and still scrambles the signal, and why the magnitude spectrum is exactly the wrong place to look for it."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
order: 5
source: "Independent study"
written: true
updated: "2026-09-15"
---

An all-pass system passes every frequency at exactly the same amplitude. Its magnitude response is a flat constant, so by any amplitude measurement it does nothing at all.

It can still ruin a signal, and following how is the point of this note.

## Core question and definition

The building block is

$$
H(z) = \frac{z^{-1} - a^*}{1 - a z^{-1}},
$$

a pole at $$a$$ paired with a zero at $$1/a^*$$ — reflected through the unit circle, so a pole inside at radius $$r$$ has its zero outside at radius $$1/r$$. The reflection is what makes the magnitude constant: at every point on the unit circle the distance ratio to the pole and to the zero works out the same. Evaluating $$|H(e^{j\omega})|$$ across $$\omega$$ returns $$1$$ to machine precision at every frequency.

Cascade as many of these as you like and the product is still flat.

## Key concepts

### Group delay is where the content is

If the magnitude is constant, everything the system does lives in the phase. The useful summary of phase is not the phase itself but its slope:

$$
\tau(\omega) = -\frac{d\,\angle H(e^{j\omega})}{d\omega},
$$

the **group delay**, which is the delay experienced by a narrowband packet centred at $$\omega$$.

A **linear** phase means $$\tau$$ is constant — every frequency is held up by the same amount, so the whole signal shifts in time and its shape survives intact. A delay that is the same for everything is not distortion.

A curved phase means $$\tau$$ varies with frequency, and *that* is distortion, even though no amplitude has changed. Different frequency components arrive at different times. Build a signal from two narrowband wavelets, one centred at $$0.25\pi$$ and one at $$0.6\pi$$, push it through an all-pass filter whose group delay is around twenty samples at the first and near zero at the second, and the packets separate. Push it further and they can **swap order** — the second-arriving component comes out first.

Nothing was amplified. Nothing was attenuated. The signal is unrecognisable.

### The DTFT of a windowed cosine is not a delta

One methodological point that came up while testing this and is worth keeping. Computing the transform of a finite stretch of $$\cos(0.25\pi n)$$ does not give a clean spike, and the reason is not numerical error.

You did not transform a cosine. A cosine runs from $$-\infty$$ to $$\infty$$; what is in the array is a cosine *multiplied by a rectangular window*. Multiplication in time is convolution in frequency, so the delta becomes a delta convolved with the window's transform — a peak with sidelobes. Every spectrum computed from finite data is the true spectrum smeared by whatever window was used, including the rectangular one you get by default for not having chosen.

## Why it matters for my work

An all-pass system is a clean instance of a general hazard: **a transformation that is invisible to the measurement you are making and consequential for the thing you care about.**

Take the measurement literally. If your check on a processing chain is a magnitude spectrum — and magnitude is what almost every spectral summary reports, because it is real-valued and plots easily — an all-pass stage passes perfectly. Not marginally, not within tolerance: it is *exactly* right at every frequency. Phase is where the temporal structure lives, and discarding it is the default rather than a decision anyone makes.

The transferable shape is the one I keep meeting. A metric that is invariant to a given failure will never report that failure, no matter how carefully it is computed or how many samples it is computed over. [Accuracy is invariant to which class you get wrong](/study/matthews-correlation-coefficient/); a magnitude spectrum is invariant to time structure; a [held-out score](/study/robustness-subgroup-performance-and-external-validation/) is invariant to whether the signal being used is clinically valid. Adding data does not fix an invariance. Only a different measurement does, and knowing which one requires knowing what the current one cannot see.

There is a narrower version too, for anything time-resolved — ECG, EEG, perfusion curves, motion in a cine series. Filtering is routine, and an IIR filter has a frequency-dependent group delay by construction. Filtering such a signal shifts the apparent timing of features by an amount that depends on their frequency content, and if the clinical quantity *is* a timing — an interval, a latency, a time-to-peak — the filter has altered the measurement while leaving the amplitudes it was judged on entirely correct. The standard defence is a zero-phase filter, applied forwards and backwards, and that it is standard practice does not mean it was checked here.

---

Sources: the pole–zero reflection, constant modulus, and group delay of all-pass sections are standard results in discrete-time signal processing; the numerical statements above ($$|H| = 1$$ across $$\omega$$, $$|{\rm zero}| = 1/|{\rm pole}|$$, packet reordering) were reproduced directly rather than taken from a text.
