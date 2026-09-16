---
layout: study_note
title: "The Transfer Function Is a Gain, Not a Spectrum"
description: "Why H(s) sits in a different category from X(s) and Y(s), what the two numbers in H(jω) actually do to a sine, and why every pole must live in the left half-plane."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
subgroup: "Representations & System Response"
order: 2
source: "Lecture notes, Ajou University"
written: true
updated: "2026-09-15"
---

The central distinction is between **a signal** and **the system acting on it**. $$X(s)$$ and $$Y(s)$$ describe a particular input and output. $$H(s)$$ describes the input–output relationship:

$$
Y(s)=H(s)X(s).
$$

Changing the input changes $$X$$ and $$Y$$; it does not change $$H$$.

There is one qualification to the title: $$H(s)$$ is itself the Laplace transform of the system's impulse response. It therefore has a time-domain counterpart. What distinguishes it from $$X(s)$$ is its role: it characterises the system rather than the particular signal being processed. Also, a Laplace transform is not automatically an energy spectrum; even the persistent sinusoids used below have infinite total energy.

## Core question and definition

**Given a differential equation, how do I obtain the transfer function, and why does evaluating it at $$s=j\omega$$ predict the sinusoidal response?**

We work with continuous-time, causal, real-coefficient linear time-invariant (LTI) systems. The rational transfer functions below describe finite-dimensional systems. Initial conditions and stability assumptions will be stated where they matter.

### From the differential equation to the transfer function

Start with

$$
a_n y^{(n)}+\cdots+a_1\dot y+a_0y
=
b_m x^{(m)}+\cdots+b_1\dot x+b_0x.
$$

Why does differentiation become multiplication by $$s$$? Using the one-sided Laplace transform and integration by parts,

$$
\begin{aligned}
\mathcal{L}\{\dot y\}
&=\int_{0^-}^{\infty}\dot y(t)e^{-st}\,dt\\
&=\left[y(t)e^{-st}\right]_{0^-}^{\infty}
+s\int_{0^-}^{\infty}y(t)e^{-st}\,dt\\
&=sY(s)-y(0^-).
\end{aligned}
$$

The boundary term at infinity vanishes in the transform's region of convergence. Repeating the same operation gives, for example,

$$
\mathcal{L}\{\ddot y\}
=s^2Y(s)-sy(0^-)-\dot y(0^-).
$$

With the system initially at rest, the initial-condition terms vanish. Define the coefficient polynomials

$$
A(s)=a_ns^n+\cdots+a_1s+a_0,
\qquad
B(s)=b_ms^m+\cdots+b_1s+b_0.
$$

The differential equation becomes

$$
A(s)Y(s)=B(s)X(s),
$$

so the **zero-state transfer function** is

$$
\boxed{H(s)=\frac{B(s)}{A(s)}}.
$$

The familiar notation $$H=Y/X$$ expresses this relationship wherever the ratio is defined. The definition does not require dividing by an input transform at one of its zeros.

The initial-condition restriction is essential. For example,

$$
\dot y+y=x,\qquad y(0^-)=y_0
$$

gives

$$
sY-y_0+Y=X,
$$

and hence

$$
Y(s)=\underbrace{\frac{1}{s+1}X(s)}_{\text{zero-state response}}
+\underbrace{\frac{y_0}{s+1}}_{\text{zero-input response}}.
$$

The transfer function remains $$1/(s+1)$$. Initial stored energy supplies an additional response; it does not redefine the system's gain.

### Why the impulse response is the time-domain counterpart

An impulse has Laplace transform

$$
\mathcal{L}\{\delta(t)\}=1.
$$

Therefore, with zero initial conditions,

$$
X(s)=1
\quad\Longrightarrow\quad
Y(s)=H(s).
$$

If $$h(t)$$ denotes the output to that impulse, then

$$
H(s)=\mathcal{L}\{h(t)\}.
$$

To see how this determines the response to other inputs, write an input as a superposition of shifted impulses:

$$
x(t)=\int_{-\infty}^{\infty}x(\lambda)\delta(t-\lambda)\,d\lambda.
$$

Time invariance makes the response to a shifted impulse $$h(t-\lambda)$$. Linearity allows their responses to be added:

$$
y(t)=\int_{-\infty}^{\infty}x(\lambda)h(t-\lambda)\,d\lambda.
$$

For causal signals starting at zero,

$$
\boxed{y(t)=\int_0^t h(\tau)x(t-\tau)\,d\tau}.
$$

This is convolution. For a strictly proper rational transfer function, the impulse response is an ordinary function for positive time. A proper transfer function may also contain a direct term: $$H(s)=d+H_0(s)$$ adds $$d\delta(t)$$ to the impulse response and $$dx(t)$$ to the output.

| Object | Meaning | Depends on the chosen input? |
|---|---|---|
| $$x(t),X(s)$$ | Input signal and its transform | Yes |
| $$y(t),Y(s)$$ | Output signal and its transform | Yes |
| $$h(t),H(s)$$ | Impulse response and transfer function | No |
| $$H(j\omega)$$ | Complex gain at one sinusoidal frequency, when the steady-state interpretation applies | No |

A gain need not be dimensionless. For example, a transfer function from force to velocity has units of velocity divided by force.

### Why exponentials keep their shape

The useful property of an exponential is

$$
\frac{d^k}{dt^k}e^{s_0t}=s_0^k e^{s_0t}.
$$

Take the input $$x(t)=C e^{s_0t}$$ and seek a particular solution $$y_p(t)=Qe^{s_0t}$$. Substitution into the differential equation gives

$$
A(s_0)Qe^{s_0t}=B(s_0)Ce^{s_0t}.
$$

If $$A(s_0)\ne0$$,

$$
Q=\frac{B(s_0)}{A(s_0)}C=H(s_0)C,
$$

and therefore

$$
\boxed{y_p(t)=H(s_0)Ce^{s_0t}}.
$$

The exponential is reproduced with a different coefficient. This is the reason for calling exponentials **eigenfunctions** of LTI systems.

The particular solution alone need not satisfy the initial conditions. The full solution also contains homogeneous terms. For distinct characteristic roots,

$$
y(t)=\sum_i c_i e^{p_i t}+H(s_0)Ce^{s_0t}.
$$

Repeated roots introduce polynomial factors multiplying their exponentials, derived below. If $$s_0$$ is itself a pole, division by $$A(s_0)$$ is invalid: the resonant case needs a different particular solution.

### From a complex exponential to a real sinusoid

Write a real sinusoidal input as an imaginary part:

$$
x(t)=A\sin(\omega t+\phi)
=\operatorname{Im}\left\{Ae^{j\phi}e^{j\omega t}\right\}.
$$

Because the differential equation has real coefficients, taking the imaginary part of a complex solution produces the solution to the imaginary part of its input.

Write the frequency response in polar form:

$$
H(j\omega)=M(\omega)e^{j\theta(\omega)}.
$$

The sinusoidal particular solution is then

$$
\begin{aligned}
y_p(t)
&=\operatorname{Im}\left\{
M e^{j\theta}Ae^{j\phi}e^{j\omega t}
\right\}\\
&=AM\sin(\omega t+\phi+\theta).
\end{aligned}
$$

If all natural modes decay, this is the response that remains:

$$
\boxed{
y_{\mathrm{ss}}(t)
=A\lvert H(j\omega)\rvert
\sin\!\left(\omega t+\phi+\arg H(j\omega)\right)
}.
$$

Thus the frequency stays the same, the amplitude is multiplied by the magnitude, and the phase is shifted by the argument.

The qualification is **steady state**. Switching a sinusoid on generally excites additional natural modes during the transient. Also, evaluating a rational expression at $$j\omega$$ does not by itself prove that those modes decay.

### Worked example: the entire response to a switched-on sine

Use the original example,

$$
H(s)=\frac{1}{s+1},
\qquad
x(t)=\sin(10t),\quad t\ge0,
\qquad y(0)=0.
$$

First find the input transform. Since

$$
\int_0^\infty e^{-(s-j\omega)t}\,dt=\frac{1}{s-j\omega},
$$

taking the imaginary part for real $$s>0$$ gives

$$
\mathcal{L}\{\sin(\omega t)\}
=\frac{\omega}{s^2+\omega^2}.
$$

Consequently,

$$
Y(s)=\frac{10}{(s+1)(s^2+100)}.
$$

Use partial fractions:

$$
\frac{10}{(s+1)(s^2+100)}
=
\frac{A}{s+1}+\frac{Bs+C}{s^2+100}.
$$

Multiplying through,

$$
\begin{aligned}
10
&=A(s^2+100)+(Bs+C)(s+1)\\
&=(A+B)s^2+(B+C)s+(100A+C).
\end{aligned}
$$

Equating coefficients gives

$$
A+B=0,\qquad B+C=0,\qquad 100A+C=10.
$$

The first two equations give $$B=-A$$ and $$C=A$$, so

$$
101A=10,
\qquad
A=\frac{10}{101},
\quad B=-\frac{10}{101},
\quad C=\frac{10}{101}.
$$

Therefore,

$$
Y(s)=
\frac{10}{101}\frac{1}{s+1}
-\frac{10}{101}\frac{s}{s^2+100}
+\frac{1}{101}\frac{10}{s^2+100}.
$$

The exponential integral above also gives the cosine transform by taking its real part. Inverting each term,

$$
\boxed{
y(t)=
\underbrace{\frac{10}{101}e^{-t}}_{\text{transient}}
+
\underbrace{\frac{1}{101}\sin(10t)
-\frac{10}{101}\cos(10t)}_{\text{sinusoidal steady state}}
}.
$$

Two direct checks catch algebra errors.

**Initial condition:**

$$
y(0)=\frac{10}{101}-\frac{10}{101}=0.
$$

**Differential equation:**

$$
\dot y(t)=
-\frac{10}{101}e^{-t}
+\frac{10}{101}\cos(10t)
+\frac{100}{101}\sin(10t),
$$

so

$$
\dot y+y=\sin(10t).
$$

Now convert the steady-state part into one sinusoid. Expanding

$$
R\sin(10t+\theta)
=R\cos\theta\,\sin(10t)+R\sin\theta\,\cos(10t)
$$

and matching coefficients gives

$$
R\cos\theta=\frac{1}{101},
\qquad
R\sin\theta=-\frac{10}{101}.
$$

Squaring and adding,

$$
R^2=\frac{1+100}{101^2}=\frac{1}{101}.
$$

The cosine coefficient is positive and the sine coefficient negative, so the phase lies in the fourth quadrant:

$$
R=\frac{1}{\sqrt{101}},
\qquad
\theta=-\arctan(10).
$$

The frequency-domain calculation gives exactly the same quantities:

$$
H(j10)
=\frac{1}{1+j10}
=\frac{1-j10}{(1+j10)(1-j10)}
=\frac{1-j10}{101}.
$$

Hence

$$
\lvert H(j10)\rvert=\frac{1}{\sqrt{101}}\approx0.099504,
\qquad
\arg H(j10)=-\arctan(10)\approx-84.289^\circ.
$$

The original numerical integration recorded amplitude $$0.099504$$ and phase $$-84.279^\circ$$, with amplitude agreement within $$10^{-8}$$. These are the previously recorded numerical checks. The derivation supplies the exact target; a measured discrepancy can include integration, finite-transient, and phase-estimation effects.

Notice where the terms came from: the pole at $$-1$$ supplies the decaying exponential, while the input's poles at $$\pm j10$$ supply the persistent sinusoid.

### Phase shift is not generally a fixed time delay

At a single positive frequency,

$$
\sin(\omega t+\theta)=\sin\!\left(\omega(t-\tau_\phi)\right)
$$

when

$$
\tau_\phi=-\frac{\theta}{\omega}.
$$

This equivalent delay depends on the phase branch and is only determined modulo a sinusoidal period.

A true delay by a fixed time $$\tau$$ acts on every complex exponential as

$$
e^{j\omega(t-\tau)}
=e^{-j\omega\tau}e^{j\omega t}.
$$

It therefore has unit magnitude and phase $$-\omega\tau$$. For our first-order system, instead,

$$
\theta(\omega)=-\arctan\omega,
\qquad
\tau_\phi(\omega)=\frac{\arctan\omega}{\omega}.
$$

Both attenuation and equivalent delay vary with frequency. A general waveform passing through this system is therefore not simply a delayed copy of itself.

## Key concepts

### A pole and a zero are not symmetric

Write the transfer function after cancelling common factors:

$$
H(s)=\frac{B(s)}{A(s)}.
$$

A pole is a root of the remaining denominator; a zero is a root of the remaining numerator.

The asymmetry comes directly from the differential equation. Set the input to zero and try $$y(t)=ce^{pt}$$:

$$
A(p)ce^{pt}=0.
$$

A nonzero homogeneous response is possible when $$A(p)=0$$. A pole therefore identifies a natural mode visible in this input–output description.

A zero answers a different question. For an exponential input at $$s=z$$, with $$A(z)\ne0$$,

$$
y_p(t)=\frac{B(z)}{A(z)}Ce^{zt}=0
$$

when $$B(z)=0$$. The corresponding exponential particular response is suppressed.

The phrase “an input frequency disappears” needs care: a general zero is a point in the complex plane, not necessarily a sinusoidal frequency. A sinusoidal notch requires a zero on the imaginary axis. For example, with $$a>0$$ and $$\omega_0>0$$,

$$
H(s)=\frac{s^2+\omega_0^2}{(s+a)^2}
$$

has

$$
H(j\omega_0)
=\frac{-\omega_0^2+\omega_0^2}{(a+j\omega_0)^2}=0.
$$

Its steady-state response at that frequency is zero. A switched-on sinusoid can still produce a decaying transient.

**Poles determine which natural modes can persist or grow; zeros determine how inputs excite and combine those modes.** Zeros do not independently add homogeneous modes, but they are not unimportant to design.

In particular, steady-state gain depends on the numerator as well as the denominator:

$$
H(0)=\frac{B(0)}{A(0)}
$$

when this value exists. “Stability is determined by poles” does not mean “all behaviour is determined by poles.”

### Why repeated poles produce polynomial factors

For a simple pole,

$$
\mathcal{L}\{e^{pt}\}
=\int_0^\infty e^{-(s-p)t}\,dt
=\frac{1}{s-p},
\qquad \operatorname{Re}(s-p)>0.
$$

Differentiating this identity $$k$$ times with respect to $$s$$ gives

$$
\int_0^\infty t^k e^{-(s-p)t}\,dt
=\frac{k!}{(s-p)^{k+1}}.
$$

Thus

$$
\boxed{
\mathcal{L}^{-1}\left\{\frac{1}{(s-p)^r}\right\}
=\frac{t^{r-1}}{(r-1)!}e^{pt}
}.
$$

A repeated pole therefore produces terms such as $$te^{pt}$$, not just several copies of $$e^{pt}$$.

For a conjugate pair $$p=\sigma\pm j\omega_d$$, combining conjugate exponential terms gives a real response of the form

$$
e^{\sigma t}
\left(C\cos\omega_d t+D\sin\omega_d t\right).
$$

The imaginary part determines the oscillation frequency. The real part determines the exponential envelope.

### Why the left half-plane is the stability region

The magnitude of an exponential mode is

$$
\lvert e^{(\sigma+j\omega_d)t}\rvert=e^{\sigma t}.
$$

Therefore:

| Pole location | Time-domain factor | Consequence |
|---|---|---|
| $$\sigma<0$$ | $$e^{\sigma t}$$ | Decays |
| $$\sigma=0$$, simple pole | Constant or sustained sinusoid | Does not decay |
| $$\sigma>0$$ | $$e^{\sigma t}$$ | Grows |
| Repeated pole | $$t^k e^{\sigma t}$$ | Polynomial factor must also be considered |

A repeated LHP pole still decays. Writing $$\sigma=-\alpha$$ with $$\alpha>0$$,

$$
t^k e^{-\alpha t}
=\exp(k\ln t-\alpha t)\longrightarrow0,
$$

because the linear term in time eventually dominates the logarithm.

A pole on the imaginary axis is not asymptotically stable: its mode does not return to zero. Repetition can make matters worse by introducing a growing polynomial factor.

The strict condition for decay of every mode in a minimal finite-dimensional realisation is consequently

$$
\boxed{\operatorname{Re}(p_i)<0\quad\text{for every pole}}.
$$

Here **minimal** means that the realisation contains no internal modes hidden from its input–output transfer function.

### Bounded input is a separate stability question

**Bounded-input, bounded-output (BIBO) stability** asks whether every bounded input produces a bounded zero-state output.

Suppose $$\lvert x(t)\rvert\le M$$. Convolution gives

$$
\begin{aligned}
\lvert y(t)\rvert
&\le\int_0^t\lvert h(\tau)\rvert
\lvert x(t-\tau)\rvert\,d\tau\\
&\le M\int_0^\infty\lvert h(\tau)\rvert\,d\tau.
\end{aligned}
$$

An absolutely integrable impulse response therefore supplies a finite bound on the output. A finite direct term adds at most $$\lvert d\rvert M$$.

For a proper rational transfer function with LHP poles, the impulse response is a finite sum of decaying exponential terms and their polynomial multiples. Each has finite absolute integral; for example,

$$
\int_0^\infty t^k e^{-\alpha t}\,dt
=\frac{k!}{\alpha^{k+1}},
\qquad \alpha>0.
$$

This is the preceding Laplace integral evaluated at $$s-p=\alpha$$.

Why exclude imaginary-axis poles even when the unforced oscillation is bounded? For a modal impulse response $$e^{j\omega_0t}$$, driving at the same frequency gives

$$
\int_0^t
e^{j\omega_0(t-\lambda)}e^{j\omega_0\lambda}\,d\lambda
=t e^{j\omega_0t}.
$$

The input is bounded, but the output envelope grows. Taking real and imaginary components gives the corresponding real sinusoidal resonance.

An uncancelled RHP mode can be excited by a bounded pulse and continue growing after the pulse ends. For a simple modal kernel, a unit pulse lasting $$T$$ produces, for $$t>T$$,

$$
\int_0^T e^{p(t-\lambda)}\,d\lambda
=e^{pt}\frac{1-e^{-pT}}{p}.
$$

For $$\operatorname{Re}(p)>0$$, the coefficient is nonzero and the exponential grows. Repeated poles retain the same growth problem.

Thus, for a causal **proper rational** transfer function,

$$
\boxed{\text{BIBO stable}\iff
\text{all uncancelled poles lie strictly in the LHP}}.
$$

Properness matters: the ideal differentiator discussed below has no finite poles, but it is not BIBO stable.

### A small unstable disturbance eventually dominates

For an unstable mode with initial magnitude $$\varepsilon>0$$,

$$
y(t)=\varepsilon e^{\sigma t},
\qquad \sigma>0.
$$

To find when it reaches a level $$B>\varepsilon$$, solve

$$
B=\varepsilon e^{\sigma t_B}.
$$

Taking logarithms,

$$
\boxed{t_B=\frac{1}{\sigma}\ln\frac{B}{\varepsilon}}.
$$

Using the original example, $$\sigma=1\,\mathrm{s}^{-1}$$, $$\varepsilon=10^{-12}$$, and $$B=1$$,

$$
t_B=\ln(10^{12})\,\mathrm{s}
=12\ln(10)\,\mathrm{s}
\approx27.6\,\mathrm{s}.
$$

A tiny starting coefficient delays the problem logarithmically; it does not change stability.

The unstable mode does require some excitation. That excitation can be an initial perturbation, noise, or an input coupled to the mode. Exact zero remains zero in the mathematical model, but stability must hold for nearby initial conditions too.

### A transfer function can hide an internal unstable mode

The LHP test on a reduced transfer function concerns its input–output behaviour. Internal stability requires checking all internal modes.

Consider the realisation

$$
\dot q=q,\qquad
\dot z=-z+x,\qquad
y=z+q.
$$

With both initial states zero, $$q(t)=0$$ and

$$
(s+1)Z=X,\qquad Y=Z,
$$

so

$$
H(s)=\frac{1}{s+1}.
$$

Nevertheless, an initial perturbation $$q(0)=q_0$$ gives

$$
q(t)=q_0e^t.
$$

The transfer function did not show this mode because the chosen input cannot excite it from zero state. The realisation is not minimal.

This is also why an algebraic pole–zero cancellation is insufficient evidence of internal stability: removing a factor from an input–output formula does not, by itself, show that the corresponding internal motion has disappeared.

### Deriving the first-order Bode plot

A Bode plot separates two questions: amplitude scaling and phase shift.

Take the normalised first-order form

$$
H(s)=\frac{K}{1+s\tau},
\qquad K>0,\quad \tau>0.
$$

Rationalising its frequency response gives

$$
H(j\omega)
=\frac{K(1-j\omega\tau)}{1+(\omega\tau)^2}.
$$

Therefore,

$$
\lvert H(j\omega)\rvert
=\frac{K}{\sqrt{1+(\omega\tau)^2}},
\qquad
\theta(\omega)=-\arctan(\omega\tau).
$$

For a dimensionless amplitude ratio, define the magnitude in decibels by

$$
M_{\mathrm{dB}}=20\log_{10}\lvert H(j\omega)\rvert.
$$

Why the factor 20? When power is proportional to amplitude squared under the same impedance or normalisation,

$$
10\log_{10}\frac{P_{\mathrm{out}}}{P_{\mathrm{in}}}
=
10\log_{10}\lvert H\rvert^2
=
20\log_{10}\lvert H\rvert.
$$

For a dimensional gain, the logarithm must instead use a specified reference gain to form a dimensionless ratio.

Substituting the first-order magnitude,

$$
M_{\mathrm{dB}}
=
20\log_{10}K
-10\log_{10}\left(1+(\omega\tau)^2\right).
$$

The straight-line approximation follows from two limits.

**Low frequency:** if $$\omega\tau\ll1$$,

$$
1+(\omega\tau)^2\approx1,
\qquad
M_{\mathrm{dB}}\approx20\log_{10}K.
$$

**High frequency:** if $$\omega\tau\gg1$$,

$$
1+(\omega\tau)^2\approx(\omega\tau)^2,
$$

so

$$
M_{\mathrm{dB}}\approx
20\log_{10}K-20\log_{10}(\omega\tau).
$$

Increasing frequency by one decade means replacing $$\omega$$ by $$10\omega$$. The high-frequency asymptote changes by

$$
-20\log_{10}(10\omega\tau)
+20\log_{10}(\omega\tau)
=-20\log_{10}10=-20\ \mathrm{dB}.
$$

That is the derivation of **minus 20 dB per decade**.

The asymptotes intersect where $$\omega\tau=1$$:

$$
\boxed{\omega_c=\frac{1}{\tau}}.
$$

At that frequency the exact values are

$$
\lvert H(j\omega_c)\rvert=\frac{K}{\sqrt2},
\qquad
\theta(\omega_c)=-\arctan1=-\frac{\pi}{4},
$$

and

$$
M_{\mathrm{dB}}(\omega_c)-20\log_{10}K
=-10\log_{10}2\approx-3.01\ \mathrm{dB}.
$$

The squared amplitude ratio relative to DC is

$$
\left(\frac{K/\sqrt2}{K}\right)^2=\frac12.
$$

This is the half-power statement, under the power interpretation above.

The actual curve is smooth. It is the **asymptotic sketch**, not the exact magnitude, that stays flat up to the corner and then becomes a straight descending line.

| Frequency range | Magnitude | Phase |
|---|---|---|
| $$\omega\tau\ll1$$ | Approximately $$K$$ | Approaches $$0$$ |
| $$\omega\tau=1$$ | Exactly $$K/\sqrt2$$ | Exactly $$-\pi/4$$ |
| $$\omega\tau\gg1$$ | Approximately $$K/(\omega\tau)$$ | Approaches $$-\pi/2$$ |

The pole is $$p=-1/\tau$$. Thus, for this first-order factor, the pole magnitude and corner frequency coincide.

### The same pole in a step response

For the original system and a unit step,

$$
X(s)=\frac1s,
\qquad
Y(s)=\frac{1}{s(s+1)}.
$$

Since

$$
\frac{1}{s(s+1)}
=\frac1s-\frac{1}{s+1},
$$

the response is

$$
y(t)=1-e^{-t}.
$$

More generally,

$$
\frac{K}{s(1+s\tau)}
=\frac{K}{s}-\frac{K}{s+1/\tau},
$$

so

$$
y(t)=K\left(1-e^{-t/\tau}\right).
$$

At $$t=\tau$$, the remaining error has fallen to $$e^{-1}$$ of its initial magnitude. This explains the definition of the **time constant**.

To reduce that relative error to a prescribed fraction $$0<\epsilon<1$$,

$$
e^{-t/\tau}\le\epsilon
\quad\Longleftrightarrow\quad
t\ge\tau\ln\frac1\epsilon.
$$

The connection is now explicit:

$$
\boxed{
p=-\frac1\tau,\qquad
\omega_c=\frac1\tau,\qquad
\text{step-error factor}=e^{-t/\tau}
}.
$$

The same parameter determines transient decay and frequency attenuation.

### Why pole and zero contributions add in Bode plots

For a factored transfer function,

$$
H(s)=K
\frac{\prod_i(s-z_i)}{\prod_j(s-p_j)}.
$$

Each complex factor can be written in polar form. Multiplying factors multiplies their magnitudes and adds their angles; division reverses those operations. Hence

$$
\lvert H(j\omega)\rvert
=
\lvert K\rvert
\frac{\prod_i\lvert j\omega-z_i\rvert}
{\prod_j\lvert j\omega-p_j\rvert},
$$

and

$$
\arg H(j\omega)
=
\arg K+\sum_i\arg(j\omega-z_i)
-\sum_j\arg(j\omega-p_j)
\pmod{2\pi}.
$$

Taking logarithms converts the magnitude product into a sum:

$$
M_{\mathrm{dB}}
=
20\log_{10}\lvert K\rvert
+\sum_i20\log_{10}\lvert j\omega-z_i\rvert
-\sum_j20\log_{10}\lvert j\omega-p_j\rvert.
$$

The logarithmic frequency axis then turns power-law asymptotes into straight lines.

For example, a normalised real LHP zero contributes

$$
\lvert1+j\omega\tau\rvert
=\sqrt{1+(\omega\tau)^2}.
$$

Above its corner this is approximately $$\omega\tau$$, so its asymptotic slope is $$+20$$ dB/decade. A real LHP pole supplies the reciprocal factor and contributes $$-20$$ dB/decade.

This also gives a geometric reading: $$j\omega-p_j$$ is the vector from a pole to the evaluation point. Its length enters the denominator of the gain, while its angle is subtracted from the phase.

### Integrators and differentiators as frequency weights

For positive frequency,

$$
\frac{1}{j\omega}=-\frac{j}{\omega}
=\frac1\omega e^{-j\pi/2},
\qquad
j\omega=\omega e^{j\pi/2}.
$$

Thus:

| Element | Magnitude | Phase | Magnitude slope |
|---|---|---|---|
| Integrator $$1/s$$ | $$1/\omega$$ | $$-\pi/2$$ | $$-20$$ dB/decade |
| Differentiator $$s$$ | $$\omega$$ | $$+\pi/2$$ | $$+20$$ dB/decade |

The slopes follow directly from

$$
20\log_{10}(1/\omega)=-20\log_{10}\omega,
\qquad
20\log_{10}\omega.
$$

Substituting the frequencies used in the original note:

| $$\omega$$ | Integrator magnitude $$1/\omega$$ | Differentiator magnitude $$\omega$$ |
|---|---|---|
| $$0.01=1/100$$ | $$1/(1/100)=100$$ | $$0.01$$ |
| $$1$$ | $$1/1=1$$ | $$1$$ |
| $$100$$ | $$1/100=0.01$$ | $$100$$ |

The integrator weights low frequencies more strongly. Its DC gain is unbounded because a constant input keeps accumulating:

$$
x(t)=1
\quad\Longrightarrow\quad
y(t)=\int_0^t1\,d\lambda=t.
$$

It is therefore not BIBO stable by itself.

Even at nonzero frequency, the stable-system steady-state argument needs care. With zero initial output,

$$
y(t)=\int_0^t\sin(\omega\lambda)\,d\lambda
=\frac{1-\cos(\omega t)}{\omega}.
$$

The oscillating component has magnitude $$1/\omega$$ and phase $$-\pi/2$$, exactly as $$1/(j\omega)$$ predicts, but an additional constant persists. There is no decaying mode to remove it. Integral action's ability to eliminate certain tracking errors must therefore be analysed inside a stable closed loop.

The differentiator has the opposite weighting:

$$
\frac{d}{dt}\sin(\omega t)
=\omega\cos(\omega t)
=\omega\sin(\omega t+\pi/2).
$$

For a noise component $$n(t)=\varepsilon\sin(\Omega t)$$,

$$
\dot n(t)=\varepsilon\Omega\cos(\Omega t).
$$

Its output amplitude is $$\varepsilon\Omega$$. Small-amplitude noise at sufficiently high frequency can therefore dominate a differentiated measurement.

The ideal differentiator is improper: its numerator degree exceeds its denominator degree. A direct bounded-input counterexample to BIBO stability is

$$
x(t)=\sin(t^2),
\qquad
y(t)=2t\cos(t^2),
$$

whose input is bounded while its derivative is unbounded.

### Revision checklist

| Question | What to do | Assumption to check |
|---|---|---|
| What is the transfer function? | Transform the differential equation and form $$B/A$$ | Zero initial conditions |
| What remains under sinusoidal forcing? | Compute $$H(j\omega)$$ and multiply amplitude/add phase | Natural modes must decay for a unique attracting steady state |
| What sets the transient rates? | Factor the denominator and inspect multiplicities | Hidden internal modes may require the full realisation |
| Is the zero-state map BIBO stable? | Check every uncancelled pole is strictly LHP | Causal, proper, rational transfer function |
| Does a zero remove a sinusoid? | Evaluate $$H(j\omega)$$ | The zero must be at that imaginary-axis frequency |
| Is the Bode line exact? | Compare the exact factor with its low/high-frequency limits | Straight segments are asymptotes |
| Is phase a fixed delay? | Examine whether phase is linear in frequency | A single-frequency equivalent delay is insufficient |

## Why it matters for my work

The useful habit is to separate the input signal, the system model, and the initial condition before interpreting a response. A measured transient is not automatically a property of the input, and an input–output transfer function is not automatically a complete description of internal stability.

For learned or nonlinear systems, these calculations require a justified LTI model, possibly a local approximation. The questions remain useful, but the sinusoidal-response theorem cannot be assumed without its hypotheses.

## What I have not resolved

I want to work through two extensions: how local linearisation limits the amplitude range over which frequency-response measurements remain meaningful, and how exact sampling versus numerical integration changes the continuous-time stability picture.

---

Sources: Ajou University lecture notes; the standard classical-control treatment in Franklin, Powell, and Emami-Naeini, Feedback Control of Dynamic Systems. The transfer-function definition, impulse-response interpretation, exponential response, pole/zero distinction, and LHP stability criteria are standard linear-systems results. The recorded numerical checks from the original note are the gain and phase at angular frequency 10 for 1/(s+1), the first-order corner attenuation, the growth time of the noise-seeded unstable mode, and the integrator/differentiator weighting table. The additional calculations here are derived analytically; no new simulation results are claimed.
