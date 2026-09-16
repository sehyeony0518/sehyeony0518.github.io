---
layout: study_note
title: "Why Complex Exponentials: Choosing the Representation Is Most of the Work"
description: "The convolution integral that takes a page, the eigenfunction that takes one line, and what it costs to throw away the transient."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
subgroup: "Representations & System Response"
order: 1
source: "Independent study"
written: true
updated: "2026-09-15"
---

Complex exponentials are useful because a time shift changes them by multiplication. A linear time-invariant system combines shifted copies of its input, so it preserves an exponential's shape whenever the resulting sum or integral converges.

That statement has conditions. An exponential extending through all time is different from one switched on at time zero. A sinusoidal particular solution is different from the complete response. Transfer functions can describe transients; evaluating a transfer function at one frequency is the step that leaves them out.

## Defining an exponential with a complex argument

One consistent definition is the power series

$$
e^z=\sum_{n=0}^{\infty}\frac{z^n}{n!},
\qquad z\in\mathbb C.
$$

This is meaningful for complex arguments because each term requires only multiplication, addition, and division. The ratio of successive absolute term sizes is

$$
\frac{\lvert z\rvert^{n+1}/(n+1)!}
{\lvert z\rvert^n/n!}
=
\frac{\lvert z\rvert}{n+1}
\longrightarrow 0.
$$

Thus the series converges absolutely for every finite complex argument. There is no instruction to multiply something together an imaginary number of times.

The familiar exponential law also follows from this definition. Absolute convergence permits multiplying and regrouping the series:

$$
\begin{aligned}
e^z e^w
&=
\sum_{n=0}^{\infty}
\sum_{k=0}^{n}
\frac{z^k w^{n-k}}{k!(n-k)!}\\
&=
\sum_{n=0}^{\infty}
\frac{1}{n!}
\sum_{k=0}^{n}
\binom nk z^k w^{n-k}\\
&=
\sum_{n=0}^{\infty}\frac{(z+w)^n}{n!}
=
e^{z+w}.
\end{aligned}
$$

The middle step is the binomial theorem. This is why a definition involving an infinite sum recovers the multiplication rule associated with powers.

Termwise differentiation gives another essential property:

$$
\frac{d}{dt}e^{st}
=
\sum_{n=1}^{\infty}\frac{n s^n t^{n-1}}{n!}
=
s e^{st}.
$$

Differentiation changes an exponential only by a scalar. Time shifting will do the same.

## Euler's formula and the geometry of phase

Let the imaginary unit satisfy

$$
j^2=-1.
$$

Separate the even and odd terms in the exponential series:

$$
\begin{aligned}
e^{j\theta}
&=
\left(
1-\frac{\theta^2}{2!}+\frac{\theta^4}{4!}-\cdots
\right)\\
&\quad+
j\left(
\theta-\frac{\theta^3}{3!}+\frac{\theta^5}{5!}-\cdots
\right)\\
&=
\cos\theta+j\sin\theta.
\end{aligned}
$$

Consequently,

$$
\cos\theta=\frac{e^{j\theta}+e^{-j\theta}}{2},
\qquad
\sin\theta=\frac{e^{j\theta}-e^{-j\theta}}{2j}.
$$

Complex conjugation reverses the angle:

$$
\overline{e^{j\theta}}=e^{-j\theta}.
$$

Combining this with the exponential law,

$$
\lvert e^{j\theta}\rvert^2
=
e^{j\theta}e^{-j\theta}
=
1.
$$

A purely imaginary exponent therefore describes rotation on the unit circle, rather than growth.

For a general exponent,

$$
s=\sigma+j\omega,
\qquad
e^{st}=e^{\sigma t}e^{j\omega t}.
$$

The real part controls the envelope; the imaginary part controls rotation. This single notation represents a growing oscillation, a decaying oscillation, and a constant-amplitude sinusoid.

Multiplication by a complex number has the same separation. If

$$
C=r e^{j\phi},
$$

then

$$
C e^{j\omega t}=r e^{j(\omega t+\phi)}.
$$

The magnitude scales the oscillation and the angle shifts its phase. Those are precisely the two changes a real LTI system makes to a sinusoid in sinusoidal steady state.

## Why time shifts select this representation

Define a delay operator by

$$
(S_\tau x)(t)=x(t-\tau).
$$

Applying it to an exponential gives

$$
S_\tau e^{st}
=
e^{s(t-\tau)}
=
e^{-s\tau}e^{st}.
$$

The shifted function is a scalar multiple of the original function. This is the eigenfunction property for the shift operator.

Compare a cosine:

$$
\cos\bigl(\omega(t-\tau)\bigr)
=
\cos(\omega\tau)\cos(\omega t)
+
\sin(\omega\tau)\sin(\omega t).
$$

A delay mixes cosine and sine. The two-dimensional real space spanned by them is preserved, but either function alone generally is not. Complex notation packages that pair into one object whose transformation is multiplication.

This is the main saving. Complex numbers do not add a hidden physical oscillation. They provide coordinates in which a rotation no longer requires tracking two coupled real coefficients.

For a system initially defined on real signals, its complex extension is

$$
T(x_{\mathrm R}+jx_{\mathrm I})
=
T(x_{\mathrm R})+jT(x_{\mathrm I}).
$$

This definition is justified by real linearity and allows the real and imaginary parts to be recovered separately.

## Deriving convolution from linearity and time invariance

The discrete-time argument avoids the technicalities of an ideal continuous impulse. Let the unit impulse satisfy

$$
\delta[n]=
\begin{cases}
1,&n=0,\\
0,&n\ne0.
\end{cases}
$$

Every sequence can be written as

$$
x[n]=\sum_{k=-\infty}^{\infty}x[k]\delta[n-k].
$$

Let the system's response to the impulse be

$$
h[n]=T\{\delta[n]\}.
$$

Linearity moves the coefficients outside the system, while time invariance gives

$$
T\{\delta[n-k]\}=h[n-k].
$$

Therefore,

$$
\begin{aligned}
y[n]
&=
T\left\{\sum_k x[k]\delta[n-k]\right\}\\
&=
\sum_k x[k]h[n-k].
\end{aligned}
$$

For infinite sums, this argument requires convergence and an appropriate continuity assumption on the operator. Finite sums have no such interchange issue.

The continuous counterpart is

$$
x(t)=\int_{-\infty}^{\infty}x(\tau)\delta(t-\tau)\,d\tau,
$$

leading to

$$
y(t)=
\int_{-\infty}^{\infty}
x(\tau)h(t-\tau)\,d\tau
=
\int_{-\infty}^{\infty}
h(\tau)x(t-\tau)\,d\tau.
$$

The second form is particularly useful for exponentials.

This describes the zero-state response: the part produced by the input when the system has no independently specified initial energy. If a capacitor starts charged, or a differential equation has a nonzero initial condition, its zero-input response must also be included. A mapping with a fixed nonzero initial response is generally affine rather than linear, since zero input need not produce zero output.

## Deriving the exponential eigenfunction property

Insert an all-time exponential into convolution:

$$
\begin{aligned}
y(t)
&=
\int_{-\infty}^{\infty}
h(\tau)e^{s(t-\tau)}\,d\tau\\
&=
e^{st}
\int_{-\infty}^{\infty}
h(\tau)e^{-s\tau}\,d\tau.
\end{aligned}
$$

Define

$$
H(s)=
\int_{-\infty}^{\infty}
h(\tau)e^{-s\tau}\,d\tau.
$$

Whenever this integral converges,

$$
T\{e^{st}\}=H(s)e^{st}.
$$

The transfer function is therefore the multiplier associated with each admissible exponential input.

The convergence condition matters. Pulling out a factor does not make a divergent integral finite. The set of complex arguments for which the integral converges is the region of convergence.

For a causal impulse response,

$$
h(t)=0\qquad \text{for }t<0,
$$

the integral becomes

$$
H(s)=\int_0^\infty h(\tau)e^{-s\tau}\,d\tau.
$$

If the impulse response is absolutely integrable, the imaginary axis is admissible because

$$
\lvert e^{-j\omega\tau}\rvert=1
$$

and hence

$$
\int_{-\infty}^{\infty}
\lvert h(\tau)e^{-j\omega\tau}\rvert\,d\tau
=
\int_{-\infty}^{\infty}\lvert h(\tau)\rvert\,d\tau
<\infty.
$$

This connects BIBO stability to the existence of a frequency response for ordinary bounded sinusoidal inputs.

## Recovering a real sinusoidal response

Suppose the impulse response is real. Then

$$
H(-j\omega)=\overline{H(j\omega)}.
$$

This follows directly by conjugating the defining integral.

For the input

$$
x(t)=A\cos(\omega t+\theta)
=
\operatorname{Re}\left\{
A e^{j\theta}e^{j\omega t}
\right\},
$$

real linearity gives

$$
y(t)=
\operatorname{Re}\left\{
A e^{j\theta}H(j\omega)e^{j\omega t}
\right\}.
$$

Writing

$$
H(j\omega)=\lvert H(j\omega)\rvert e^{j\phi(\omega)}
$$

produces

$$
y(t)=
A\lvert H(j\omega)\rvert
\cos\bigl(\omega t+\theta+\phi(\omega)\bigr).
$$

The amplitude gain and phase shift are consequences of complex multiplication.

It is also useful to see the real arithmetic. If

$$
H(j\omega)=a+jb,
$$

then

$$
T\{\cos(\omega t)\}
=
a\cos(\omega t)-b\sin(\omega t).
$$

The complex calculation has solved for the two real coefficients simultaneously. Taking only the real part of the transfer function would lose the sine contribution and therefore the phase information.

## Worked example: a first-order system with startup retained

Consider the causal system

$$
\dot y(t)+y(t)=x(t).
$$

Its zero-state impulse response is

$$
h(t)=e^{-t}u(t),
$$

where the unit step is zero before time zero and one afterward. The step factor is essential: the causal impulse response does not extend backward as a growing exponential.

Its transfer function follows from an elementary integral:

$$
H(s)=
\int_0^\infty e^{-(1+s)t}\,dt
=
\frac{1}{1+s},
\qquad
\operatorname{Re}(s)>-1.
$$

For an all-time input at angular frequency one,

$$
H(j)=\frac{1}{1+j}=\frac{1-j}{2}.
$$

Therefore,

$$
\lvert H(j)\rvert=\frac{1}{\sqrt2},
\qquad
\arg H(j)=-\frac{\pi}{4},
$$

and the sinusoidal response is

$$
y_{\mathrm{sin}}(t)
=
\frac{\cos t+\sin t}{2}.
$$

Now change the problem. Switch the input on at time zero and impose zero initial state:

$$
x(t)=\cos t\,u(t),
\qquad
y(0)=0.
$$

The complex version of the convolution is

$$
\begin{aligned}
z(t)
&=
\int_0^t e^{-(t-\tau)}e^{j\tau}\,d\tau\\
&=
e^{-t}\int_0^t e^{(1+j)\tau}\,d\tau\\
&=
e^{-t}\frac{e^{(1+j)t}-1}{1+j}\\
&=
\frac{e^{jt}-e^{-t}}{1+j}.
\end{aligned}
$$

Taking the real part,

$$
y(t)=
\frac{\cos t+\sin t-e^{-t}}{2},
\qquad t\ge0.
$$

The additional exponential enforces the initial condition:

$$
y(0)=\frac{1+0-1}{2}=0.
$$

Differentiation provides an independent check:

$$
\dot y(t)
=
\frac{-\sin t+\cos t+e^{-t}}{2},
$$

so

$$
\dot y(t)+y(t)=\cos t.
$$

At a quarter cycle,

$$
y\left(\frac{\pi}{2}\right)
=
\frac{1-e^{-\pi/2}}{2}.
$$

Every value follows from the constructed equation and input. No numerical integration accuracy claim is needed.

For an arbitrary initial condition,

$$
y(0)=y_0,
$$

the complete response is

$$
y(t)=
\frac{\cos t+\sin t}{2}
+
\left(y_0-\frac12\right)e^{-t}.
$$

Thus the all-time sinusoidal solution corresponds to a particular initial state:

$$
y_0=\frac12.
$$

It is not the same experiment as switching on a cosine from rest.

## Quantifying when the transient can be neglected

For the zero-initial-state example, the absolute difference from the sinusoidal response is

$$
\lvert y(t)-y_{\mathrm{sin}}(t)\rvert
=
\frac12 e^{-t}.
$$

To make this difference at most a chosen absolute tolerance,

$$
\varepsilon=\frac{1}{100},
$$

solve

$$
\frac12 e^{-t}\le\frac{1}{100}.
$$

Taking logarithms gives

$$
t\ge\log 50.
$$

This is an exact settling bound for this example. It says nothing about another system's time scale or an application's acceptable error.

More generally,

$$
\left|y_0-\frac12\right|e^{-t}\le\varepsilon
$$

requires

$$
t\ge
\log\left(
\frac{\lvert y_0-\frac12\rvert}{\varepsilon}
\right)
$$

when the initial error exceeds the tolerance. Otherwise the condition already holds at startup.

The decision to discard a transient should therefore specify the initial-state assumptions, the decay rate, and the tolerance. “After a while” hides all three.

## Transfer functions do not inherently discard transients

Use the unilateral Laplace transform,

$$
Y(s)=\int_0^\infty y(t)e^{-st}\,dt.
$$

Integration by parts gives

$$
\mathcal L_+\{\dot y\}
=
sY(s)-y(0),
$$

assuming the boundary term at infinity vanishes.

For the same differential equation,

$$
(s+1)Y(s)=X(s)+y_0.
$$

The cosine transform can be obtained from its exponential representation:

$$
X(s)
=
\frac12\left(
\frac{1}{s-j}+\frac{1}{s+j}
\right)
=
\frac{s}{s^2+1}.
$$

Consequently,

$$
Y(s)
=
\frac{s}{(s+1)(s^2+1)}
+
\frac{y_0}{s+1}.
$$

Partial fractions give

$$
Y(s)=
\frac{s+1}{2(s^2+1)}
+
\frac{y_0-\frac12}{s+1}.
$$

Inverting returns the complete response derived above, including its transient.

The distinction is between using the full transform of the input and evaluating the transfer function at a single frequency. The former can describe startup. The latter gives the multiplier for a sustained exponential.

## When the convenient calculation fails

Consider an integrator:

$$
\dot y(t)=x(t).
$$

For a constant input switched on from rest,

$$
x(t)=1,\qquad y(0)=0,
$$

direct integration gives

$$
y(t)=t.
$$

There is no finite DC gain. The formal transfer function has a pole at the tested frequency:

$$
H(s)=\frac1s.
$$

Trying to substitute zero into this expression is not a shortcut to a steady output. It identifies the failure of that steady-output assumption.

Likewise, an unstable causal system can have an algebraically computable sinusoidal particular solution while its natural response grows. A particular solution does not become the long-time behavior unless the other components decay.

This is why the eigenfunction statement needs its convergence condition and why “particular,” “zero-state,” and “steady-state” should not be used interchangeably.

## Discrete time, sampling, and frequency ambiguity

For a discrete-time LTI system,

$$
\begin{aligned}
y[n]
&=
\sum_k h[k]\alpha^{n-k}\\
&=
\alpha^n\sum_k h[k]\alpha^{-k}.
\end{aligned}
$$

The multiplier is the [z-transform](/study/poles-zeros-and-the-z-transform/):

$$
H(z)=\sum_k h[k]z^{-k}.
$$

On the unit circle,

$$
\alpha=e^{j\omega},
$$

the input has constant magnitude and the multiplier is the discrete-time frequency response.

Discrete-time frequency is periodic because integer sample indices satisfy

$$
e^{j(\omega+2\pi m)n}
=
e^{j\omega n}e^{j2\pi mn}
=
e^{j\omega n},
\qquad m,n\in\mathbb Z.
$$

Sampling a continuous sinusoid at sampling frequency $$f_s$$ gives

$$
e^{j2\pi f(n/f_s)}
=
e^{j\omega n},
\qquad
\omega=\frac{2\pi f}{f_s}.
$$

Frequencies differing by an integer multiple of the sampling frequency therefore produce the same sampled complex exponential. This ambiguity is algebraic, not a defect in a Fourier-transform implementation.

The [DFT](/study/convolution-via-the-dft/) chooses a finite collection of these exponentials that are orthogonal over a finite periodic grid. The same representation principle then becomes finite-dimensional linear algebra.

## Revision checklist

| Check | What I should be able to reproduce |
|---|---|
| Complex exponential | Derive Euler's formula by separating even and odd powers. |
| Exponential law | Identify the binomial theorem inside the product of two power series. |
| Shift eigenfunction | Show why a delay multiplies an exponential by a scalar. |
| Convolution | Obtain convolution from shifted impulses, linearity, and time invariance. |
| Frequency response | Derive gain and phase from complex multiplication. |
| Startup | Recover the exponential term that enforces the initial condition. |
| Settling tolerance | Solve an explicit transient-error inequality. |
| Transform distinction | Explain why a full Laplace calculation retains transients. |
| Failure case | Explain why an integrator has no finite DC steady-state gain. |
| Sampling | Derive the periodicity of discrete-time frequency. |

## Why it matters for my work

The useful habit is to identify an operator's natural coordinates before calculating. Fourier features, graph eigenvectors, and learned representations all change which operations become simple. I also need to distinguish a convenient restricted calculation from the complete problem: a frequency response describes a sustained mode, while startup and initial conditions require additional information.

## What I have not resolved

For a real signal-processing pipeline, I still need to choose an acceptable startup error in the units of the downstream task. The decay equation supplies a bound only after that tolerance and the initial-state assumptions are specified.
