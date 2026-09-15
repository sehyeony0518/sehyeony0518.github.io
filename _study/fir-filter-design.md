---
layout: study_note
title: "FIR Filter Design: When the Optimal Answer Is Optimal for the Wrong Norm"
description: "Why truncating the ideal filter is provably best in the L2 sense and still not what you want, what linear phase costs, and the symmetry constraints that forbid whole filter types outright."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
order: 4
source: "Independent study"
written: true
updated: "2026-09-15"
---

Nobody designs filters by hand any more — you hand a specification to a function and it returns coefficients. The reason to follow the methods anyway is that they are an extended worked example of everything else: the DTFT, convolution, windowing, and pole–zero placement all appear, doing real work, on a problem with a checkable answer.

One result in here is worth the trip on its own: the obvious approach is **provably optimal**, and is still the wrong thing to do.

## Core question and definition

A filter specification has more parts than it first appears. Between the passband and the stopband sits a **transition band** of non-zero width, because the drop cannot be vertical. Inside the passband the response ripples by some $$\delta_p$$ rather than sitting flat at 1; inside the stopband it ripples by $$\delta_s$$ rather than sitting at 0. You want the transition narrow and both ripples small, and every one of those is paid for in filter length.

Even "the cutoff frequency" needs a convention, since the response no longer has an edge. The usual one is the half-power point: $$|H|^2 = 1/2$$, so $$|H| = 1/\sqrt2$$, and

$$
20\log_{10}\!\left(1/\sqrt2\right) = -3.01\ \text{dB}.
$$

That is where the famous $$-3$$ dB comes from — not a round number someone liked, but the point at which half the power gets through.

Two quick sanity checks on any coefficient list, worth doing before anything else: summing the coefficients gives the DC gain ($$\omega = 0$$), and summing them with alternating signs gives the gain at $$\omega=\pi$$. An 11-tap moving average sums to 1 (0 dB at DC) and alternates to $$1/11$$, which is $$-20.8$$ dB at Nyquist — a real but unimpressive lowpass, and now you know that without plotting anything.

## Key concepts

### FIR versus IIR is a trade, not a ranking

**FIR** has no feedback, hence no poles, hence unconditional stability. It can be made *exactly* linear phase. It is relatively forgiving of coefficient quantisation. And it can be computed through the [FFT](/study/convolution-via-the-dft/) when it gets long.

**IIR** is recursive and buys sharpness cheaply: a transition that costs an FIR a hundred taps may cost an IIR three coefficients. The price is that it has poles, so stability must be maintained; it is sensitive to coefficient precision because errors feed back; and — the part that usually decides it — **its phase cannot be made linear.** Group delay varies with frequency, which is [distortion the magnitude response will not show](/study/all-pass-systems-and-group-delay/).

### Linear phase is a symmetry, and it forbids things

An FIR filter has linear phase exactly when its coefficients are symmetric or antisymmetric about their centre. That is the whole condition, and the four combinations of (odd/even length) × (symmetric/antisymmetric) are the four types.

The types are not interchangeable, because the symmetry forces the response to vanish at particular frequencies:

| Type | Length | Symmetry | $$H(0)$$ | $$H(\pi)$$ | Cannot build |
|---|---|---|---|---|---|
| I | odd | symmetric | free | free | — |
| II | even | symmetric | free | **0** | highpass |
| III | odd | antisymmetric | **0** | **0** | lowpass, highpass |
| IV | even | antisymmetric | **0** | free | lowpass |

These are structural. Asking a Type II filter for a highpass is asking for a response that is simultaneously large and provably zero at $$\omega=\pi$$ — no optimiser will find it, and none will explain why. Type III is forced to zero at both ends, so it is a bandpass or a differentiator and nothing else.

### Truncation is L2-optimal, and L2 is the wrong norm

The natural design: take the ideal brick-wall lowpass, inverse-transform it to get a sinc, keep $$2M+1$$ coefficients around the centre, shift to make it causal. Symmetric by construction, so linear phase comes free.

And it is optimal. By Parseval, squared error in the frequency domain equals squared error in the coefficients, so for a fixed number of taps, **keeping the largest-magnitude coefficients and discarding the rest minimises the integrated squared error**. It is not a heuristic; it is the best possible answer to the question as posed.

The result is visibly bad. Truncating is multiplying by a rectangular window, which in frequency convolves the ideal response with the window's transform, and produces overshoot near the discontinuity that does not shrink as taps are added — Gibbs ringing.

The resolution is that **the question was posed wrong.** Total squared error is not what a filter specification asks about. A spec says *no ripple anywhere exceeds $$\delta_s$$* — a constraint on the maximum, not the sum. A design can have small total error while one excursion is far too large, and L2 has no opinion about that because a single narrow spike contributes almost nothing to an integral.

That is the general lesson, and it is not about filters. A provably optimal solution is optimal for a stated objective, and the objective is a modelling choice. When the answer looks wrong despite the proof being right, the objective is the thing to doubt.

### Fixing it: better windows, or the right objective

**Windowing** attacks the symptom. Replace the rectangular window with Hamming, Hann, or Blackman and you trade a wider main lobe for much lower sidelobes — a wider transition band for smaller ripple. It works, it is one line of code, and it is still fundamentally a repair.

**Frequency sampling** takes a different route: specify the response at $$L$$ points, inverse-DFT to get coefficients. Because the DFT samples the DTFT, the resulting filter matches your specification *exactly* at those points — and is uncontrolled between them, which is where the ripple reappears.

**Parks–McClellan** changes the objective to the right one. It minimises the *maximum* error, giving an equiripple design: every ripple the same height, none exceeding the spec, and the shortest filter meeting it. `scipy.signal.remez` is the implementation, and for a serious specification it is what to use.

## Why it matters for my work

The truncation result is the piece I expect to keep reaching for, because the structure recurs far outside signal processing. A [loss function](/study/support-vector-machines/) is a stated objective, an optimiser finds its optimum, and the optimum can be exactly correct and useless because average-case error was minimised when the requirement was about worst case. A model with excellent mean performance and one catastrophic failure mode is an L2-optimal filter with a Gibbs spike, and no amount of additional training data closes a gap that the objective does not measure.

The linear-phase table is the second half of the same thought, in a better direction. Those zeros are constraints derived *before* any optimisation — the structure of the model tells you which specifications are unreachable, and you learn it from the symmetry rather than from a training run that fails for unclear reasons. Knowing what a model class cannot represent is usually more informative than a benchmark of what it can, and it is available much earlier.

---

Sources: the linear-phase types and their endpoint constraints, the Gibbs phenomenon, and the Parks–McClellan/Remez exchange are standard results in discrete-time signal processing. The numerical claims here ($$-3.01$$ dB, the 11-tap moving average at 0 and $$-20.83$$ dB, and the $$H(0)$$/$$H(\pi)$$ pattern across all four types) were verified directly.
