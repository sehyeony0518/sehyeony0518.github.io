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

An all-pass filter can preserve the magnitude of every frequency component while changing how those components combine in time.

Two qualifications matter. “Magnitude test” here means a test of frequency-response magnitude or spectral magnitude; a test of a waveform's peak amplitude can detect changes. And waveform distortion does not imply destruction of information: an ideal all-pass transformation is invertible when its complete output and phase response are available.

The problem is that a magnitude spectrum does not report the relative phases responsible for the shape of a waveform.

This note derives a stable causal all-pass section, distinguishes phase delay from group delay, and constructs signals for which the invisible spectral change becomes visible in time.

## What an all-pass response preserves

For a linear time-invariant system,

$$
Y(e^{j\omega})=H(e^{j\omega})X(e^{j\omega}).
$$

Write its response as

$$
H(e^{j\omega})
=
A(\omega)e^{j\phi(\omega)},
$$

where the magnitude is nonnegative and the phase is defined modulo a full turn.

A unit-gain all-pass filter satisfies

$$
A(\omega)=|H(e^{j\omega})|=1.
$$

It follows immediately that

$$
|Y(e^{j\omega})|=|X(e^{j\omega})|.
$$

The magnitude of every sinusoidal component is preserved. Their phases need not be.

For a real filter and a cosine input,

$$
x[n]=\cos(\omega_0n),
$$

the steady-state output is

$$
y[n]
=
A(\omega_0)
\cos(\omega_0n+\phi(\omega_0)).
$$

An all-pass filter therefore preserves this sinusoid's amplitude and changes its phase. A single sinusoid by itself cannot demonstrate relative timing distortion between different frequencies.

A general waveform contains many components. Their sum depends on whether their peaks reinforce or cancel at each time. Changing those relative phases can redistribute the waveform's energy over time while preserving its spectral magnitude.

This is why flat gain is insufficient to establish that a processing stage preserves waveform shape.

## Constructing a reciprocal pole and zero pair

Begin with a first-order denominator

$$
D(z)=1-az^{-1}.
$$

Its pole is at

$$
z=a.
$$

On the unit circle, its complex conjugate is

$$
D(e^{j\omega})^*
=
1-a^*e^{j\omega}.
$$

Multiply that conjugate by a one-sample delay:

$$
e^{-j\omega}D(e^{j\omega})^*
=
e^{-j\omega}-a^*.
$$

This suggests the transfer function

$$
\boxed{
H(z)=\frac{z^{-1}-a^*}{1-az^{-1}}
}.
$$

On the unit circle,

$$
H(e^{j\omega})
=
e^{-j\omega}
\frac{D(e^{j\omega})^*}{D(e^{j\omega})}.
$$

Taking magnitudes gives

$$
|H(e^{j\omega})|
=
|e^{-j\omega}|
\frac{|D(e^{j\omega})^*|}{|D(e^{j\omega})|}
=
1.
$$

The equality follows from conjugation and unit-magnitude delay. No frequency sweep is needed to prove it.

For a nonzero pole coefficient, the numerator vanishes when

$$
z^{-1}=a^*,
$$

so the zero is located at

$$
z_0=\frac1{a^*}.
$$

If

$$
a=re^{j\theta},
$$

then

$$
z_0=\frac1r e^{j\theta}.
$$

The pole and zero have the same angle and reciprocal radii. A pole inside the unit circle is paired with a zero outside it.

The normalising coefficient must not be lost when writing the factor in terms of its roots:

$$
H(z)
=
-a^*
\frac{z-1/a^*}{z-a}.
$$

The unscaled ratio of pole and zero distances does not itself have unit magnitude. The leading factor supplies the required normalisation.

For a causal stable section, require

$$
|a|<1.
$$

This places the pole inside the unit circle and makes the causal impulse response decay. When the coefficient is zero, the section reduces to the pure delay

$$
H(z)=z^{-1}.
$$

The reciprocal-zero formula is then interpreted through that limiting case rather than by dividing by zero.

## The impulse response and what stability contributes

Expand the denominator as a geometric series:

$$
\frac1{1-az^{-1}}
=
\sum_{n=0}^{\infty}a^nz^{-n},
\qquad |z|>|a|.
$$

Multiplying by the numerator gives

$$
H(z)
=
(z^{-1}-a^*)
\sum_{n=0}^{\infty}a^nz^{-n}.
$$

The coefficient at zero delay is

$$
h[0]=-a^*.
$$

For positive indices,

$$
\begin{aligned}
h[n]
&=a^{n-1}-a^*a^n\\
&=(1-|a|^2)a^{n-1}.
\end{aligned}
$$

Thus,

$$
h[n]=
\begin{cases}
0,&n<0,\\
-a^*,&n=0,\\
(1-|a|^2)a^{n-1},&n\ge1.
\end{cases}
$$

The pole-magnitude condition makes both the absolute sum and the energy sum finite.

For the concrete choice

$$
a=\frac12,
$$

the impulse response begins

$$
h=
\left[
-\frac12,
\frac34,
\frac38,
\frac3{16},
\frac3{32},
\ldots
\right].
$$

An input impulse has become a negative first sample followed by a positive decaying tail. That is already a change of shape despite the exactly flat frequency-response magnitude.

Its energy remains one:

$$
\begin{aligned}
\sum_n|h[n]|^2
&=
|a|^2
+
(1-|a|^2)^2
\sum_{n=1}^{\infty}|a|^{2(n-1)}\\
&=
|a|^2
+
\frac{(1-|a|^2)^2}{1-|a|^2}\\
&=1.
\end{aligned}
$$

For implementation, multiply the transfer-function equation through by its denominator:

$$
Y(z)-az^{-1}Y(z)
=
z^{-1}X(z)-a^*X(z).
$$

The resulting difference equation is

$$
y[n]
=
ay[n-1]+x[n-1]-a^*x[n].
$$

The response derived above assumes initial rest for an impulse input. For periodic steady-state examples, the filter state must instead be consistent with the preceding periodic input.

## Phase delay is a ratio; group delay is a slope

The phase response itself is an angle:

$$
\phi(\omega)=\arg H(e^{j\omega}),
$$

with a continuous, unwrapped branch chosen over the interval being studied.

The **phase delay** is

$$
\boxed{
\tau_p(\omega)=-\frac{\phi(\omega)}{\omega}
},
\qquad \omega\ne0.
$$

Its definition comes from rewriting a sinusoidal output:

$$
\cos(\omega n+\phi(\omega))
=
\cos\left(\omega[n-\tau_p(\omega)]\right).
$$

The phase angle has been expressed as a delay of that particular sinusoid.

The **group delay** is

$$
\boxed{
\tau_g(\omega)=-\frac{d\phi(\omega)}{d\omega}
}.
$$

Both are measured in samples when angular frequency is measured in radians per sample. Multiplying either by the sampling period converts it to seconds.

For a pure delay,

$$
H(e^{j\omega})=e^{-jD\omega},
$$

so

$$
\phi(\omega)=-D\omega,
\qquad
\tau_p(\omega)=\tau_g(\omega)=D.
$$

For nonlinear phase, the ratio and derivative generally differ.

Phase delay also depends on the selected phase branch. Adding a full turn to the phase changes the ratio by a frequency-dependent amount, while a constant branch offset does not change the derivative.

At zero frequency, the phase-delay formula is undefined. If the chosen phase has zero intercept and is differentiable, its limit is

$$
\lim_{\omega\to0}
-\frac{\phi(\omega)}{\omega}
=
-\phi'(0).
$$

A phase plot should therefore be unwrapped before differentiation, and any reported phase delay should state its branch convention.

## Why group delay describes a narrowband envelope

Consider a complex modulated signal

$$
x[n]=b(n)e^{j\omega_0n},
$$

where the envelope varies slowly and its spectrum is concentrated near zero. Here the envelope is written as a continuous bandlimited function evaluated at integer positions, so a fractional shift of the envelope has a defined meaning.

Let the offset from the carrier frequency be

$$
\nu=\omega-\omega_0.
$$

Across a sufficiently narrow band, approximate the filter phase by its tangent:

$$
\phi(\omega_0+\nu)
\approx
\phi(\omega_0)+\phi'(\omega_0)\nu.
$$

If the magnitude is approximately constant there, then

$$
H(\omega_0+\nu)
\approx
A_0e^{j\phi(\omega_0)}e^{-j\tau_g(\omega_0)\nu}.
$$

Multiplying the envelope spectrum by the last exponential delays the envelope. The output is approximately

$$
y[n]
\approx
A_0
e^{j[\omega_0n+\phi(\omega_0)]}
b\bigl(n-\tau_g(\omega_0)\bigr).
$$

The carrier phase is governed by the phase value at the centre frequency. The envelope displacement is governed by the local slope.

That is why phase delay and group delay describe different aspects of a modulated signal.

The approximation has a condition: the phase must be close to its tangent across the envelope's entire bandwidth. Equivalently, the residual

$$
\phi(\omega_0+\nu)
-
\phi(\omega_0)
+
\tau_g(\omega_0)\nu
$$

must remain small over that band.

If the slope changes substantially within the packet, the envelope is distorted instead of simply delayed. A group-delay value at one frequency does not predict the exact output of an arbitrarily broadband pulse.

For an all-pass filter, magnitude variation is absent, but this phase-curvature limitation remains.

## Deriving the group delay of one all-pass section

Write

$$
a=re^{j\theta},
\qquad
u=\omega-\theta,
$$

and define

$$
D(\omega)=1-re^{-ju}.
$$

From the all-pass construction,

$$
H(e^{j\omega})
=
e^{-j\omega}\frac{D(\omega)^*}{D(\omega)}.
$$

If the denominator phase is

$$
\psi(\omega)=\arg D(\omega),
$$

a continuous phase representation is

$$
\phi(\omega)=-\omega-2\psi(\omega).
$$

To differentiate the angle, write the logarithm locally as magnitude plus phase:

$$
\log D=\log|D|+j\psi.
$$

Differentiating gives

$$
\psi'(\omega)
=
\operatorname{Im}\left(\frac{D'(\omega)}{D(\omega)}\right).
$$

Since

$$
D'(\omega)=jre^{-ju},
$$

we obtain

$$
\psi'(\omega)
=
\operatorname{Re}\left(
\frac{re^{-ju}}{1-re^{-ju}}
\right).
$$

Multiply numerator and denominator by the denominator's conjugate. The real part becomes

$$
\psi'(\omega)
=
\frac{r\cos u-r^2}{1+r^2-2r\cos u}.
$$

Therefore,

$$
\begin{aligned}
\tau_g(\omega)
&=1+2\psi'(\omega)\\
&=
\boxed{
\frac{1-r^2}
{1+r^2-2r\cos(\omega-\theta)}
}.
\end{aligned}
$$

The denominator is the squared distance from the rotating unit-circle point to the pole. Near the pole angle, that distance is smallest, so the group delay is largest.

For a real positive coefficient,

$$
\tau_g(0)=\frac{1+a}{1-a},
$$

and

$$
\tau_g(\pi)=\frac{1-a}{1+a}.
$$

Moving the pole toward the unit circle increases the peak delay and lengthens the impulse-response tail. These are two descriptions of the same increasingly persistent system memory.

## Numerical comparison of the two delays

Continue with

$$
a=\frac12.
$$

The group delays at three frequencies are

$$
\tau_g(0)=3,
$$

$$
\tau_g(\pi/2)
=
\frac{1-1/4}{1+1/4}
=
\frac35,
$$

and

$$
\tau_g(\pi)=\frac13.
$$

Now evaluate the actual complex response at the middle frequency:

$$
\begin{aligned}
H(e^{j\pi/2})
&=
\frac{-j-1/2}{1+j/2}\\
&=
-\frac45-\frac35j.
\end{aligned}
$$

Its magnitude is exactly one because

$$
\left(\frac45\right)^2+\left(\frac35\right)^2=1.
$$

Choose the phase branch that starts at zero and decreases continuously. The phase here is

$$
\phi(\pi/2)
=
-\pi+\arctan(3/4).
$$

The phase delay is therefore

$$
\begin{aligned}
\tau_p(\pi/2)
&=
-\frac{-\pi+\arctan(3/4)}{\pi/2}\\
&=
2-\frac2\pi\arctan(3/4)\\
&\approx1.59033.
\end{aligned}
$$

The group delay at the same frequency is only

$$
0.6.
$$

There is no inconsistency. One number describes the phase displacement of the carrier; the other describes the displacement of a sufficiently narrow envelope around it.

| Frequency | Phase delay | Group delay |
|---|---|---|
| Zero-frequency limit | $$3$$ | $$3$$ |
| $$\pi/2$$ | $$2-\frac2\pi\arctan(3/4)\approx1.59033$$ | $$3/5$$ |
| $$\pi$$ | $$1$$ | $$1/3$$ |

The equality at the zero-frequency limit does not extend across the band.

## A waveform change that a spectral-magnitude test misses

Construct the periodic input

$$
x[n]
=
\cos(\pi n/3)+\cos(2\pi n/3).
$$

One period is

$$
x=[2,0,-1,0,-1,0].
$$

For the same all-pass section, direct substitution gives

$$
H(e^{j\pi/3})
=
-\frac12-j\frac{\sqrt3}{2}
=
e^{-j2\pi/3},
$$

and

$$
H(e^{j2\pi/3})
=
-\frac{13}{14}
-j\frac{3\sqrt3}{14}.
$$

The second magnitude is also exactly one:

$$
\frac{169}{196}+\frac{27}{196}=1.
$$

The steady-state output is

$$
\begin{aligned}
y[n]
={}&
\cos(\pi n/3-2\pi/3)\\
&-\frac{13}{14}\cos(2\pi n/3)
+\frac{3\sqrt3}{14}\sin(2\pi n/3).
\end{aligned}
$$

Evaluating the six sample positions gives

$$
y=
\frac17[-10,9,8,-3,2,-6].
$$

Every number follows from the two stated sinusoidal responses. For example, the first sample is

$$
y[0]
=
-\frac12-\frac{13}{14}
=
-\frac{10}{7}.
$$

The input's energy over one period is

$$
2^2+(-1)^2+(-1)^2=6.
$$

The output's energy is

$$
\frac{100+81+64+9+4+36}{49}
=
6.
$$

A six-point DFT of the input has magnitude three at the positive and negative bins corresponding to the two cosines, and zero at the other bins. The output has exactly those same magnitudes because each occupied bin was multiplied by a unit-magnitude response.

Yet the waveform is visibly different.

It is not merely a common delay of both cosines. A pure delay would require

$$
H(e^{j2\pi/3})=
\left[H(e^{j\pi/3})\right]^2.
$$

The square of the first response is

$$
-\frac12+j\frac{\sqrt3}{2},
$$

which is not the second response.

This example assumes periodic steady state. Filtering a short isolated segment from rest introduces transients, and truncating the output can discard part of the response. Those operations can change a finite-record magnitude comparison even though the underlying system is all-pass.

## Cascades, inversion, and practical tests

Cascading all-pass sections multiplies their responses:

$$
H_{\mathrm{total}}(z)
=
z^{-D}
\prod_{m=1}^{P}
\frac{z^{-1}-a_m^*}{1-a_mz^{-1}}.
$$

For a causal construction, the explicit delay is a nonnegative integer and the poles lie inside the unit circle.

Magnitudes multiply, so the total magnitude remains one. Phases add, so group delays add:

$$
\tau_{\mathrm{total}}(\omega)
=
D+\sum_{m=1}^{P}\tau_m(\omega).
$$

Real-valued filtering requires real coefficients. Complex poles can be combined with their conjugates to produce real second-order sections.

The positive numerator and denominator in the derived first-order group-delay formula also show that each stable causal section contributes positive delay. Phase equalisation with these sections adds delay where needed; it does not provide unrestricted causal time advancement.

An ideal all-pass response has inverse

$$
H^{-1}(e^{j\omega})=H(e^{j\omega})^*.
$$

Thus full information can be recovered in the ideal setting. However, the zeros outside the unit circle become poles of the inverse. The straightforward causal inverse is unstable; a stable inverse generally requires noncausal processing.

A magnitude-only representation has already discarded the information needed for that inversion. The filter and the representation therefore have different information-loss properties.

Forward-backward filtering also needs care. For real coefficients, its ideal interior response is

$$
H(e^{j\omega})H(e^{-j\omega})
=
|H(e^{j\omega})|^2.
$$

The phase cancels, but a general filter's magnitude is squared. For an all-pass filter this product is one. Finite-record boundary handling still matters, and using future samples makes the operation unsuitable as a zero-latency streaming solution.

A useful validation sequence is to verify the pole locations, check the analytic magnitude identity, inspect unwrapped phase, and examine group delay over the occupied band. Then use impulses and multitone signals to inspect waveform changes.

Numerically differentiating wrapped phase creates false spikes at branch jumps. A coarse frequency grid can also miss a narrow delay peak near a pole close to the unit circle. The analytic formula is a useful reference against which numerical plots can be checked.

## Revision checklist

| Question | What I should be able to reproduce |
|---|---|
| Why is the magnitude flat? | Express the numerator as a delayed conjugate of the denominator on the unit circle. |
| Where is the zero? | Take the reciprocal conjugate of the pole and retain the gain factor. |
| What makes the causal section stable? | A pole strictly inside the unit circle. |
| What does phase delay measure? | The phase shift of one sinusoid expressed as a time displacement. |
| What does group delay measure? | The local phase slope and the displacement of a sufficiently narrow envelope. |
| Why can the delays differ? | A phase-to-frequency ratio need not equal a local derivative. |
| How does the pole set the delay? | Derive the denominator's phase derivative and identify the peak near the pole angle. |
| What does the worked waveform preserve? | Spectral magnitudes and period energy, while changing relative phase and shape. |
| Is the transformation irreversible? | No, but a stable inverse may require noncausal processing. |
| What can invalidate a finite test? | Initial-state transients, output truncation, phase wrapping, and inadequate frequency resolution. |

## Why it matters for my work

For time-resolved measurements, preserving spectral power does not establish that feature timing is preserved. I need the phase response and the occupied signal band before interpreting a filtered peak, interval, or latency.

## What I have not resolved

Audit the filters used before timing-related measurements in my work, including their group delay, initial-state handling, and finite-record boundary effects.
