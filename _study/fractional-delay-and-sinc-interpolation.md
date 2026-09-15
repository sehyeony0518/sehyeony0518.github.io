---
layout: study_note
title: "Fractional Delay: Half a Sample Is Not Half of Two Samples"
description: "What it means to shift a discrete signal by a non-integer amount, why the answer is spread over all time, and why the intuitive picture is the one that is wrong."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "learning-principles"
category_title: "Learning Principles"
order: 12
source: "Independent study"
written: true
updated: "2026-09-15"
---

Delay a discrete signal by one sample and everything moves one step right. Delay it by *half* a sample and the question stops being obvious — there is no position between two array indices for a value to sit.

The answer is well defined, and it is not what intuition offers.

## Core question and definition

A discrete sequence, on its own, says nothing about what happens between its samples. To shift by a fraction you need a claim about the in-between, and the [sampling theorem](/study/resampling-and-anti-aliasing/) supplies exactly one: *assume the samples came from a band-limited continuous signal at a rate above Nyquist.* That signal is then unique, and the recipe follows — reconstruct it, resample at offset positions, and the result is the fractional delay.

Reconstruction is sinc interpolation:

$$
x(t) = \sum_n x[n]\,\operatorname{sinc}\!\left(\frac{t - nT_s}{T_s}\right),
$$

so delaying by $$d$$ samples gives coefficients $$h[n] = \operatorname{sinc}(n - d)$$.

For $$d$$ an integer this collapses to a shifted impulse — $$\operatorname{sinc}$$ is $$1$$ at zero and exactly $$0$$ at every other integer, so the filter is a single tap and ordinary shifting is recovered. For $$d = 1/2$$ every tap misses a zero crossing, and none of them vanish.

## Key concepts

### What half a sample of delay actually looks like

Take the simplest possible signal, $$\delta[n]$$, and delay it by half a sample. The result is $$\operatorname{sinc}(n - 1/2)$$:

$$
\dots,\ -0.0909,\ 0.1273,\ -0.2122,\ \mathbf{0.6366},\ \mathbf{0.6366},\ -0.2122,\ 0.1273,\ -0.0909,\ \dots
$$

Three things in that row are worth stopping on.

**The two central taps are 0.6366, not 0.5.** The intuitive answer — split it evenly between the neighbours — is wrong, and wrong by 27%. The true value is $$2/\pi$$.

**The tails alternate in sign and decay slowly**, as $$1/n$$. About **16% of the energy lies outside the two nearest taps**, so an impulse — something localised at a single index — becomes, after half a sample of delay, a waveform spread across the entire signal, ringing in both directions. Including backwards: a fractional delay is not causal.

**It is still correct.** The taps sum to 1, so DC is preserved, and integer delays reproduce a shifted impulse exactly.

### Why the intuitive picture is the wrong one

Applied to a triangular pulse, or a rectangular one, the half-sample delay does not look like a triangle or rectangle nudged sideways. It overshoots and rings near the corners.

The temptation is to call that an artefact. It is not — it is the consequence of the assumption, and the assumption was band-limiting. A clean triangle with sharp corners has energy at *every* frequency, including well past Nyquist, so it is not a signal that could have produced those samples under the sampling theorem. The band-limited signal that *did* produce them is smoother, overshoots at the corners, and its intermediate values are exactly the ones computed.

So the mental image — connect the dots, read off the midpoint — is not a rough approximation of the right answer. It is the answer to a different question, one that assumes the signal has arbitrarily sharp features between samples, which is precisely what sampling it at a finite rate ruled out.

## Why it matters for my work

The direct application is any registration or resampling step, which is to say most medical imaging preprocessing. Aligning two volumes, correcting for motion, or resampling to a common grid all require values at non-integer positions, and **the interpolation kernel is a modelling assumption that gets chosen by default far more often than it gets chosen deliberately.**

The options are not equivalent. Nearest-neighbour preserves intensity values exactly and destroys geometry. Linear interpolation is cheap and acts as a lowpass filter, blurring fine texture — quantitatively, in a way that depends on the sub-pixel offset, so structures land differently depending on where they happened to fall relative to the grid. Sinc-family kernels are closest to the sampling theorem's answer and introduce ringing at sharp edges, which in CT near bone or metal can look like pathology. Each choice is defensible; none is neutral; the effect on a downstream [radiomic texture feature](/study/clinical-feature-annotation-and-multi-task-learning/) is not small.

The broader point is the one this whole stretch of signal processing keeps making. **"Between the data points" is not a place you can read from the data.** Getting a value there requires an assumption, the assumption has consequences, and the most dangerous version is the one nobody made explicitly — the default argument in a resample call. The $$0.5$$ versus $$0.6366$$ gap is a small, exactly quantifiable instance: the intuitive answer is confidently wrong, it is wrong by a specific amount, and nothing in the output announces it.

---

Sources: sinc interpolation and fractional-delay filters are standard results in discrete-time signal processing. The coefficient values above, the $$2/\pi$$ central taps, the 16% out-of-pair energy, and the exact collapse to a shifted impulse at integer delays were computed directly rather than quoted.
