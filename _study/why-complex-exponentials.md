---
layout: study_note
title: "Why Complex Exponentials: Choosing the Representation Is Most of the Work"
description: "The convolution integral that takes a page, the eigenfunction that takes one line, and what it costs to throw away the transient."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
order: 1
source: "Independent study"
written: true
updated: "2026-09-15"
---

Signal processing is written in $$e^{j\omega t}$$ rather than sines and cosines, and the usual reaction is that this is mysticism dressed up as convenience. It is neither. It is bookkeeping, and the saving is large enough to justify the whole apparatus.

## Core question and definition

First, a smaller point that blocks people before they reach the main one. $$e^x$$ was introduced as repeated multiplication, and $$e^{jx}$$ makes no sense under that reading — you cannot multiply something together $$j$$ times.

The resolution is that repeated multiplication was never the definition. It is a *property* that holds when the exponent happens to be a positive integer, and taking it for the essence blocks every extension. The definition is the series,

$$
e^z = \sum_{n=0}^{\infty}\frac{z^n}{n!},
$$

which accepts any complex $$z$$ without complaint and reduces to repeated multiplication in the special case where that idea applies.

This pattern is worth naming, because it recurs. What you learn first about a concept is usually a property under restricted conditions, and mistaking it for the definition means the general case looks like nonsense rather than like the general case.

## Key concepts

### Convolution, and then the difficulty

For a linear time-invariant system, write any input as a sum of shifted impulses:

$$
x(t) = \int x(\tau)\,\delta(t-\tau)\,d\tau .
$$

Push that through. Linearity lets the system act inside the integral; time invariance says its response to $$\delta(t-\tau)$$ is $$h(t-\tau)$$. So

$$
y(t) = \int x(\tau)\,h(t-\tau)\,d\tau .
$$

**Knowing the impulse response determines the response to everything**, which is a remarkable result and the reason $$h$$ is worth measuring.

It is also, as a calculation, unpleasant. Take the simplest possible system, $$\dot i + i = v$$, whose impulse response is $$e^{-t}$$, and feed it $$\cos(\omega t)$$. The convolution is $$\int_0^t \cos(\omega\tau)\,e^{-(t-\tau)}d\tau$$ — doable, tedious, and this is the easiest non-trivial case there is. The answer comes out as

$$
y(t) = A\cos(\omega t) + B\sin(\omega t) + (\text{decaying transient}),
$$

**same frequency**, different amplitude and phase. That is the fact worth having. Getting it cost a page.

### The same fact in one line

Now use $$e^{st}$$ instead. It is an [eigenfunction](/study/poles-zeros-and-the-z-transform/): in goes $$e^{st}$$, out comes $$H(s)e^{st}$$. One multiplication.

Since $$\cos(\omega t) = \tfrac12\!\left(e^{j\omega t} + e^{-j\omega t}\right)$$, the cosine case follows immediately, and

$$
|H(j\omega)| = \text{amplitude gain}, \qquad \angle H(j\omega) = \text{phase shift}.
$$

For the system above, $$H(s) = 1/(s+1)$$, so at $$\omega = 1$$ the gain is $$0.7071$$ and the phase is $$-0.7854$$ rad; at $$\omega = 3$$, $$0.3162$$ and $$-1.2490$$. Integrating the differential equation numerically and comparing against $$|H|\cos(\omega t + \angle H)$$ after the transient dies gives agreement to $$10^{-12}$$.

So: a page of integration, or reading off one complex number. Nothing deep happened. $$\cos$$ and $$\sin$$ are the real and imaginary parts of a single object, and tracking that object once is half the work of tracking two real quantities that are always carried together anyway. **If you decline complex notation you must do the harder version, and there is no third option** — which is why nobody reasonable declines.

### What gets thrown away

The transfer-function route gives the steady state and discards the transient, and that is a *choice*, not a free simplification.

It is usually the right one, for a reason that is more practical than principled: the transient depends on initial conditions, and you rarely know them. Whatever charge happened to be on a capacitor when the circuit was switched on is not something the analysis can supply. Giving up a quantity you could not determine anyway costs little.

## Why it matters for my work

Two things, pulling in different directions.

The first is the headline: **choosing the representation is most of the work.** The fact about what an LTI system does to a sinusoid did not change between the two derivations. What changed was the basis it was expressed in, and that turned a page of integration into a lookup. Nothing in the problem announced which basis was the good one; that is knowledge about the problem class, arrived at by people who had done the hard version first.

That generalises directly. An embedding, a [kernel](/study/the-kernel-trick/), a [graph Laplacian](/study/the-graph-laplacian/), a [spectral basis](/study/spectral-filtering-and-graph-convolution/) — each is a choice of representation that makes some questions trivial and others invisible, and the choice is made before any analysis starts. "Which representation makes this easy" is a better question than "which model is best," and it gets asked far less.

The second is the discarded transient, and here I want to resist the analogy rather than extend it.

Steady-state analysis is the right default for a circuit because the transient is short, unknowable, and harmless. **For a deployed clinical model none of those three holds.** The transient is the rollout period, when clinicians are unfamiliar with the tool, when trust is uncalibrated in both directions, when workflow has not settled. It is not short — it can run for months. It is not unknowable; it can be observed, and rarely is. And it is not harmless: it is plausibly the interval of greatest risk, precisely because everyone's expectations are furthest from the system's actual behaviour.

Reporting asymptotic performance and discarding the startup behaviour is importing a convention from a setting where it was justified into one where it is not. The mathematics is the same; the reason it was acceptable is absent. Noticing which assumptions travel and which only look like they do is, in the end, most of what reading this material carefully is for.

---

Sources: the series definition of the exponential, the convolution representation of LTI systems, and the eigenfunction property of complex exponentials are standard results. The numerical agreement reported here between $$|H(j\omega)|\cos(\omega t + \angle H(j\omega))$$ and the integrated differential equation was computed directly.
