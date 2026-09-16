---
layout: study_note
title: "Fractional Delay: Half a Sample Is Not Half of Two Samples"
description: "What it means to shift a discrete signal by a non-integer amount, why the answer is spread over all time, and why the intuitive picture is the one that is wrong."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
order: 7
source: "Independent study"
written: true
updated: "2026-09-15"
---

An integer delay moves samples to other sample positions. A fractional delay asks for values between those positions.

Those values are not determined by an array alone. They become determined only after choosing a model for the signal between samples. This note uses bandlimited reconstruction: the samples represent a continuous signal whose spectrum lies below the sampling boundary.

Under that assumption, a fractional delay has an exact answer involving a shifted sinc. Linear interpolation supplies a different answer, which can be a useful approximation over a restricted band. The distinction should be established by derivation rather than by treating one interpolation method as universally correct.

## Specify the signal that is being delayed

Let the original sampling period be $$T_s$$ and write

$$
x[n]=x_c(nT_s).
$$

A delay of $$d$$ samples means a physical delay of

$$
dT_s.
$$

The desired output is

$$
y[n]=x_c((n-d)T_s).
$$

For integer delay, the requested positions are already sample locations:

$$
y[n]=x[n-d].
$$

For noninteger delay, the expression on the right would refer to an undefined array index. The continuous signal provides the missing interpretation.

Assume the complete sample sequence represents a bandlimited signal, with no problematic spectral line exactly at the Nyquist boundary. For finite-energy signals, reconstruction can be understood in the mean-square sense. A finite observed record additionally requires a rule for the unavailable samples outside its boundaries.

Define the normalised sinc by

$$
\operatorname{sinc}(u)=
\begin{cases}
\dfrac{\sin(\pi u)}{\pi u},&u\ne0,\\
1,&u=0.
\end{cases}
$$

The value at zero is the continuous limit.

Bandlimited reconstruction is

$$
x_c(t)
=
\sum_{k=-\infty}^{\infty}
x[k]\operatorname{sinc}(t/T_s-k).
$$

Substituting the desired delayed time gives

$$
y[n]
=
\sum_k x[k]\operatorname{sinc}(n-d-k).
$$

Compare this with convolution:

$$
y[n]=\sum_k x[k]h[n-k].
$$

The required impulse response is therefore

$$
h_d[n]=\operatorname{sinc}(n-d).
$$

This substitution identifies the answer. The frequency-domain derivation explains why the answer has that form and why implementing it exactly is difficult.

## A delay is a linear phase term

First consider a continuous-time delay

$$
y_c(t)=x_c(t-dT_s).
$$

Using the Fourier-transform definition and substituting

$$
u=t-dT_s
$$

gives

$$
\begin{aligned}
Y_c(f)
&=\int x_c(t-dT_s)e^{-j2\pi ft}\,dt\\
&=\int x_c(u)e^{-j2\pi f(u+dT_s)}\,du\\
&=e^{-j2\pi fdT_s}X_c(f).
\end{aligned}
$$

The multiplier has unit magnitude. It changes the phase of each frequency by an amount proportional to that frequency.

Discrete-time angular frequency is

$$
\omega=2\pi fT_s.
$$

Consequently, on the represented frequency band, the ideal fractional-delay response is

$$
\boxed{
H_d(e^{j\omega})=e^{-j\omega d}
}.
$$

Its phase is

$$
\phi(\omega)=-\omega d,
$$

and its group delay is

$$
-\frac{d\phi}{d\omega}=d.
$$

Every narrowband component receives the same delay. There is no intended amplitude shaping.

The sign is worth checking. A positive delay moves a feature toward a later sample index. With the forward Fourier-transform convention using a negative exponential, that delay produces a negative phase slope.

The same result follows for an integer shift directly from the DTFT sum. For a noninteger shift, however, one cannot substitute a fractional index into that sum without first defining the interpolation model.

## Deriving the shifted sinc from the inverse DTFT

The ideal response is specified over one principal frequency interval:

$$
H_d(e^{j\omega})=e^{-j\omega d},
\qquad -\pi<\omega<\pi.
$$

Apply the inverse DTFT:

$$
\begin{aligned}
h_d[n]
&=
\frac1{2\pi}
\int_{-\pi}^{\pi}
H_d(e^{j\omega})e^{j\omega n}\,d\omega\\
&=
\frac1{2\pi}
\int_{-\pi}^{\pi}
e^{j\omega(n-d)}\,d\omega.
\end{aligned}
$$

When the denominator below is nonzero,

$$
\begin{aligned}
h_d[n]
&=
\frac{e^{j\pi(n-d)}-e^{-j\pi(n-d)}}{2\pi j(n-d)}\\
&=
\frac{2j\sin(\pi(n-d))}{2\pi j(n-d)}\\
&=
\frac{\sin(\pi(n-d))}{\pi(n-d)}.
\end{aligned}
$$

At zero argument, the integral is simply the interval length divided by its normalisation, giving one. Therefore,

$$
\boxed{
h_d[n]=\operatorname{sinc}(n-d)
}.
$$

For integer delay $$D$$, every noncentral argument is a nonzero integer, so

$$
\operatorname{sinc}(n-D)=\delta[n-D].
$$

The ideal filter collapses to a single delayed impulse. This checks both the sign and the normalisation.

For noninteger delay, none of the integer sample positions reaches a sinc zero. The response extends indefinitely in both directions.

That discontinuous change in support is not a contradiction. The noncentral coefficients approach zero as the delay approaches an integer, but they are nonzero for every noninteger value.

## Why the ideal response is infinite and noncausal

For integer sample indices,

$$
\sin(\pi(n-d))
=
(-1)^{n+1}\sin(\pi d).
$$

Hence, for noninteger delay,

$$
h_d[n]
=
\frac{(-1)^{n+1}\sin(\pi d)}{\pi(n-d)}.
$$

The numerator has constant nonzero magnitude, while the denominator grows linearly. The tails therefore decay like the reciprocal of the index.

There are nonzero coefficients at arbitrarily negative indices. In convolution,

$$
y[n]=\sum_k h_d[k]x[n-k],
$$

a negative filter index refers to a future input sample. The exact full-band fractional delay is consequently noncausal.

Adding a finite integer delay moves the response to the right but does not eliminate its infinite negative tail. Finite latency makes a truncated approximation implementable; it does not make the exact ideal response causal.

There is also a stability distinction. The squared coefficients are summable because their tails behave like

$$
\sum_n\frac1{n^2},
$$

whereas their absolute values are not summable because they behave like

$$
\sum_n\frac1{|n|}.
$$

Thus the ideal filter is an energy-preserving operator on finite-energy sequences, but it does not satisfy the usual absolute-summability condition for bounded-input, bounded-output stability on every bounded sequence.

The slowly decaying tail has a frequency-domain explanation. Every DTFT must be periodic, but

$$
e^{-j(\omega+2\pi)d}
=
e^{-j\omega d}e^{-j2\pi d}
$$

equals its original value only when the delay is an integer.

For a noninteger delay, periodically extending the response defined on the principal interval introduces a jump at the boundary. The sinc tail is the inverse-transform consequence of that jump.

This also explains why an exact Nyquist-frequency tone is delicate. Sampling does not identify its continuous-time phase uniquely. The ideal full-band response should therefore be interpreted with its endpoint assumptions stated, rather than applied casually to that exceptional component.

## A half-sample impulse, with every coefficient traceable

Take

$$
x[n]=\delta[n],
\qquad
d=\frac12.
$$

The output is the filter itself:

$$
y[n]=\operatorname{sinc}(n-1/2).
$$

Several coefficients are:

| Index | Exact coefficient | Decimal approximation |
|---|---|---|
| $$-3$$ | $$-2/(7\pi)$$ | $$-0.090946$$ |
| $$-2$$ | $$2/(5\pi)$$ | $$0.127324$$ |
| $$-1$$ | $$-2/(3\pi)$$ | $$-0.212207$$ |
| $$0$$ | $$2/\pi$$ | $$0.636620$$ |
| $$1$$ | $$2/\pi$$ | $$0.636620$$ |
| $$2$$ | $$-2/(3\pi)$$ | $$-0.212207$$ |
| $$3$$ | $$2/(5\pi)$$ | $$0.127324$$ |
| $$4$$ | $$-2/(7\pi)$$ | $$-0.090946$$ |

For example,

$$
h[0]
=
\frac{\sin(-\pi/2)}{-\pi/2}
=
\frac2\pi.
$$

The symmetry is around the desired delayed location, halfway between the two central indices.

The two central coefficients sum to

$$
\frac4\pi>1.
$$

The alternating tails are therefore necessary to restore the correct constant-signal gain. In the appropriate Fourier-series limiting sense,

$$
\sum_n h_d[n]=H_d(1)=1.
$$

This sum is not an absolutely convergent sum for noninteger delay, so arbitrary rearrangement of its terms is not justified.

The energy calculation is cleaner. Parseval's identity gives

$$
\sum_n|h_d[n]|^2
=
\frac1{2\pi}
\int_{-\pi}^{\pi}|H_d(e^{j\omega})|^2\,d\omega
=
1.
$$

The identity follows by expanding the squared Fourier series: integrating a cross term gives zero unless its two integer indices agree. The finite-energy limit extends that calculation to the sinc sequence.

The energy in the two central coefficients is

$$
2\left(\frac2\pi\right)^2
=
\frac8{\pi^2}.
$$

Therefore the energy outside them is

$$
\boxed{
1-\frac8{\pi^2}
\approx0.18943
}.
$$

Approximately $$18.94\%$$ lies outside the central pair. The earlier value of sixteen percent was incorrect.

This is a statement about the impulse response, not a universal percentage of interpolation error for every input. Error for a particular signal also depends on where that signal places its spectral energy.

## What linear interpolation actually implements

For a delay between zero and one sample, linear interpolation uses

$$
y_{\mathrm{lin}}[n]
=
(1-d)x[n]+dx[n-1].
$$

Its response is

$$
H_{\mathrm{lin}}(e^{j\omega})
=
(1-d)+de^{-j\omega}.
$$

Multiply by the complex conjugate to obtain its squared magnitude:

$$
\begin{aligned}
|H_{\mathrm{lin}}|^2
&=(1-d)^2+d^2+2d(1-d)\cos\omega\\
&=1-2d(1-d)(1-\cos\omega)\\
&=1-4d(1-d)\sin^2(\omega/2).
\end{aligned}
$$

The gain depends on both frequency and fractional offset.

At half a sample,

$$
\begin{aligned}
H_{\mathrm{lin}}(e^{j\omega})
&=\frac12(1+e^{-j\omega})\\
&=
e^{-j\omega/2}\cos(\omega/2).
\end{aligned}
$$

Within the open principal interval, the cosine factor is positive. The filter therefore has the desired half-sample phase delay but attenuates frequencies increasingly toward Nyquist.

For a fully worked signal example, choose

$$
x[n]=\cos(\pi n/2).
$$

Its samples repeat as

$$
[1,0,-1,0,\ldots].
$$

The ideal delayed samples are

$$
y[n]
=
\cos\left(\frac\pi2(n-\frac12)\right),
$$

or

$$
\left[
\frac{\sqrt2}{2},
\frac{\sqrt2}{2},
-\frac{\sqrt2}{2},
-\frac{\sqrt2}{2},
\ldots
\right].
$$

Linear interpolation gives

$$
y_{\mathrm{lin}}[n]
=
\frac12x[n]+\frac12x[n-1],
$$

or

$$
\left[
\frac12,\frac12,-\frac12,-\frac12,\ldots
\right].
$$

The phase alignment is correct, but the sinusoid's amplitude is multiplied by

$$
\cos(\pi/4)=\frac1{\sqrt2}.
$$

At low frequencies, this gain approaches one. Linear interpolation can consequently be a good approximation for signals whose bandwidth occupies only a small part of the available interval.

It is also exact for its own piecewise-linear interpolation model. The mistake is to identify that model with ideal bandlimited reconstruction without checking the difference.

Sampling a signal does not prove that the original signal lacked sharp corners. Bandlimiting is an assumption made before invoking the sampling theorem. If the physical signal violates it, the reconstruction model may not recover the physical waveform.

## Windowing trades exactness for finite support

A practical finite filter selects and weights a finite set of ideal coefficients:

$$
h_w[n]=h_d[n]w[n],
$$

where the window is zero outside the retained interval.

To see the effect in frequency, substitute the inverse transform of the ideal response into the finite sum:

$$
\begin{aligned}
H_w(\omega)
&=\sum_n w[n]h_d[n]e^{-j\omega n}\\
&=
\frac1{2\pi}
\int_{-\pi}^{\pi}
H_d(\theta)
\left[
\sum_n w[n]e^{-j(\omega-\theta)n}
\right]d\theta.
\end{aligned}
$$

The bracketed sum is the window transform. Thus,

$$
H_w(\omega)
=
\frac1{2\pi}
\int_{-\pi}^{\pi}
H_d(\theta)W(\omega-\theta)\,d\theta.
$$

Multiplication by a window mixes neighbouring frequencies through periodic convolution.

This changes the ideal response. A finite design can have amplitude ripple, phase error, and error concentrated near the periodic boundary. Choosing a taper changes those errors; it does not simply remove an unwanted tail without other consequences.

Normalising the finite coefficients to sum to one enforces correct gain at zero frequency:

$$
\widetilde h_w[n]
=
\frac{h_w[n]}{\sum_k h_w[k]}.
$$

That corrects one frequency only. It does not guarantee unit magnitude across the band.

A longer filter supplies more freedom to approximate the target response, at the cost of additional computation, boundary dependence, and usually additional latency. Its useful accuracy must be stated over a chosen passband.

## A four-tap construction and its measurable cost

Retain the half-sample sinc coefficients at indices

$$
-1,0,1,2.
$$

Before tapering they are

$$
\left[
-\frac2{3\pi},
\frac2\pi,
\frac2\pi,
-\frac2{3\pi}
\right].
$$

Choose the explicit symmetric taper

$$
w=\left[\frac13,1,1,\frac13\right].
$$

The weighted coefficients become

$$
\left[
-\frac2{9\pi},
\frac2\pi,
\frac2\pi,
-\frac2{9\pi}
\right].
$$

Their sum is

$$
-\frac4{9\pi}+\frac4\pi
=
\frac{32}{9\pi}.
$$

Normalising by that sum gives

$$
q=
\left[
-\frac1{16},
\frac9{16},
\frac9{16},
-\frac1{16}
\right].
$$

These coefficients still occupy indices beginning at negative one. Shift them right by one sample to obtain a causal filter at indices zero through three:

$$
g=
\left[
-\frac1{16},
\frac9{16},
\frac9{16},
-\frac1{16}
\right].
$$

Its intended total delay is now

$$
D=1+\frac12=\frac32.
$$

Pair coefficients at equal distances from the centre:

$$
\begin{aligned}
G(\omega)
&=
e^{-j3\omega/2}
\left[
\frac98\cos(\omega/2)
-
\frac18\cos(3\omega/2)
\right].
\end{aligned}
$$

The paired exponential terms became cosines through

$$
e^{j\alpha}+e^{-j\alpha}=2\cos\alpha.
$$

At zero frequency, the bracket equals one. At the earlier example frequency,

$$
\begin{aligned}
|G(\pi/2)|
&=
\frac98\frac{\sqrt2}{2}
-
\frac18\left(-\frac{\sqrt2}{2}\right)\\
&=
\frac{5\sqrt2}{8}\\
&\approx0.883883.
\end{aligned}
$$

For comparison, the two-tap half-sample interpolator has gain

$$
\frac1{\sqrt2}\approx0.707107
$$

there, while the ideal response has gain one.

The four-tap construction therefore has less amplitude error at this chosen frequency. That is a derived comparison at one frequency, not a claim that it is uniformly optimal.

Its coefficient symmetry gives exact linear phase wherever the real bracket retains its sign. General fractional delays do not automatically align with an integer or half-integer symmetry centre. Windowed designs for those delays can have phase error as well as magnitude error.

## Evaluate error over the signal band and handle boundaries

After accounting for any added integer latency, let the approximate and ideal responses differ by

$$
E_H(\omega)=H_{\mathrm{approx}}(\omega)-H_{\mathrm{ideal}}(\omega).
$$

For an input spectrum $$X(\omega)$$, the output-error spectrum is

$$
E_y(\omega)=E_H(\omega)X(\omega).
$$

Parseval then gives

$$
\sum_n|e_y[n]|^2
=
\frac1{2\pi}
\int_{-\pi}^{\pi}
|E_H(\omega)|^2|X(\omega)|^2\,d\omega.
$$

This formula explains why the same interpolation filter can work well for one signal and poorly for another.

If the input is confined to a band where

$$
|E_H(\omega)|\le\varepsilon,
$$

then pulling that bound outside the integral yields

$$
\sum_n|e_y[n]|^2
\le
\varepsilon^2\sum_n|x[n]|^2.
$$

A useful specification therefore states the occupied band and an error bound within it, rather than demanding exact fractional delay over the entire frequency interval.

Finite records introduce another source of error. The ideal sum requests samples outside the observed array. Zero padding assumes the signal vanishes there; reflection assumes a mirrored continuation; wrapping assumes periodic continuation. Each changes values near a boundary.

A tone test should therefore either use a periodic construction or separate boundary effects from interior filter behaviour. An impulse test checks coefficient placement and latency. A constant-input test checks normalisation. None alone replaces a frequency-response check over the band of interest.

For spatial interpolation, the same reasoning applies along each axis. When the operation also reduces resolution, fractional positioning and anti-aliasing are separate requirements: computing a shifted value does not by itself impose the lower bandwidth required by the new grid.

## Revision checklist

| Question | What I should be able to reproduce |
|---|---|
| What does a fractional delay assume? | A specified continuous reconstruction between discrete samples. |
| Why is its phase linear? | Substitute the time shift into the Fourier-transform integral. |
| Why is the impulse response a shifted sinc? | Evaluate the inverse DTFT of the linear phase term. |
| What happens at an integer delay? | Every coefficient except the shifted impulse vanishes. |
| Why is the ideal filter noncausal? | Nonzero negative-index coefficients request arbitrarily distant future samples. |
| How much half-sample impulse energy lies outside the central pair? | Subtract the pair's energy from one to obtain approximately eighteen point nine four percent. |
| What does linear interpolation change? | Its frequency-dependent magnitude, and generally its phase approximation. |
| What does windowing cost? | Frequency-response error, finite support, and a latency choice. |
| What does DC normalisation guarantee? | Correct gain at zero frequency only. |
| How should accuracy be tested? | Align latency, inspect the occupied band, and state boundary assumptions. |

## Why it matters for my work

Registration and resampling require a model for values between voxels. I want to distinguish the desired geometric displacement from the filtering introduced by its implementation, especially when repeated interpolation could alter features used downstream.

## What I have not resolved

Compare interpolation error and accumulated filtering for the actual offsets, spatial bandwidths, and boundary rules used in my registration pipeline.
