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

An FIR design is an approximation problem with explicit constraints: a finite number of coefficients, a permitted delay, selected frequency bands, and a definition of error. Changing any of these changes what “optimal” means.

Truncating an ideal impulse response is optimal for an unweighted integrated squared-error problem with fixed support. It does not generally minimize the largest passband or stopband error. A small filter can demonstrate this distinction exactly, without an optimizer or a measured benchmark.

## Start with the specification, including units

A causal FIR filter of length $$N$$ has

$$
y[n]=\sum_{r=0}^{N-1}h[r]x[n-r],
$$

and frequency response

$$
H(e^{j\omega})
=
\sum_{r=0}^{N-1}h[r]e^{-j\omega r}.
$$

Angular frequency is measured in radians per sample. If the sampling frequency is $$f_s$$ and physical frequency is $$f$$,

$$
\omega=\frac{2\pi f}{f_s}.
$$

A low-pass specification might require

$$
1-\delta_p\le\lvert H(e^{j\omega})\rvert\le1+\delta_p
\qquad
(0\le\omega\le\omega_p),
$$

and

$$
\lvert H(e^{j\omega})\rvert\le\delta_s
\qquad
(\omega_s\le\omega\le\pi).
$$

The interval between the passband and stopband edges is the transition band:

$$
\omega_p<\omega<\omega_s.
$$

No desired value need be imposed there. This freedom is important because a finite sum of exponentials is continuous in frequency. It cannot reproduce a discontinuous brick-wall response exactly.

A “cutoff” is not a universal mathematical object. A half-power point satisfies

$$
\lvert H\rvert^2=\frac12,
$$

so its amplitude is

$$
\lvert H\rvert=\frac1{\sqrt2}.
$$

The corresponding gain in decibels is

$$
20\log_{10}\left(\frac1{\sqrt2}\right)
=
-10\log_{10}2.
$$

A half-amplitude point instead has

$$
\lvert H\rvert=\frac12,
$$

giving

$$
20\log_{10}\left(\frac12\right)
=
-20\log_{10}2.
$$

These differ. In particular, `scipy.signal.firwin` specifies a half-amplitude cutoff, whereas other filter-design interfaces use half power. The convention must be read, not inferred from the word “cutoff.” [SciPy FIR window-design documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html)

## Stability and the precise FIR–IIR distinction

For a bounded input,

$$
\lvert x[n]\rvert\le B,
$$

an FIR output obeys

$$
\lvert y[n]\rvert
\le
B\sum_{r=0}^{N-1}\lvert h[r]\rvert.
$$

A finite list of finite coefficients has a finite absolute sum. This proves BIBO stability.

It is common to say an FIR has “no poles,” but that depends on notation. Written in positive powers of the transform variable,

$$
H(z)
=
\frac{h[0]z^{N-1}+h[1]z^{N-2}+\cdots+h[N-1]}
{z^{N-1}},
$$

it can have poles at the origin. These represent delays, not unstable feedback modes.

FIR describes finite impulse-response support. A direct tapped-delay implementation is nonrecursive, but a recursive implementation can sometimes realize an FIR through cancellation. Implementation structure and impulse-response support are related concepts, not identical definitions.

An IIR can use a recursive state to obtain an infinite impulse response. It may meet some magnitude specifications with fewer coefficients, but its stability depends on pole locations in a causal realization.

For real causal filters with exact generalized linear phase about a finite center, the impulse response must have the relevant symmetry. Causality then forces finite support: sufficiently late samples are paired with negative-time samples, which must be zero. A genuinely infinite causal impulse response therefore cannot satisfy that exact symmetry.

Forward–backward filtering can produce a noncausal zero-phase operation, but it changes the problem and requires future data. It does not supply a causal IIR with zero delay.

## Linear phase comes from pairing coefficients

Suppose the real coefficients are symmetric:

$$
h[n]=h[N-1-n].
$$

Define the center

$$
\alpha=\frac{N-1}{2}.
$$

Pair terms at indices $$n$$ and $$N-1-n$$:

$$
\begin{aligned}
&h[n]e^{-j\omega n}
+h[n]e^{-j\omega(N-1-n)}\\
&\qquad=
2h[n]e^{-j\omega\alpha}
\cos\bigl(\omega(\alpha-n)\bigr).
\end{aligned}
$$

All pairs share the same phase factor, so

$$
H(e^{j\omega})=e^{-j\omega\alpha}A(\omega),
$$

where $$A(\omega)$$ is real.

Where the amplitude is nonzero and keeps its sign, the phase is

$$
-\omega\alpha
$$

up to a constant multiple of pi. The group delay is therefore

$$
\tau_g(\omega)
=
-\frac{d}{d\omega}\arg H(e^{j\omega})
=
\alpha.
$$

Zeros require care: phase is undefined at a zero, and the sign of the real amplitude can create phase jumps. “Linear phase” does not mean a wrapped phase plot must look like one uninterrupted straight line.

For antisymmetric coefficients,

$$
h[n]=-h[N-1-n],
$$

the same pairing gives

$$
H(e^{j\omega})
=
j e^{-j\omega\alpha}B(\omega),
$$

with real $$B(\omega)$$. The extra constant phase does not change the group delay away from zeros.

The delay is a cost of the chosen finite symmetric support. Increasing the length of a causal linear-phase filter increases its center delay.

## Deriving the four endpoint constraints

At DC,

$$
H(1)=\sum_{n=0}^{N-1}h[n].
$$

Antisymmetric pairs cancel, so both antisymmetric types must have zero DC response.

At Nyquist,

$$
H(-1)=\sum_{n=0}^{N-1}(-1)^n h[n].
$$

For an even-length symmetric filter, paired indices have opposite parity:

$$
(-1)^{N-1-n}=-(-1)^n.
$$

Their Nyquist contributions cancel.

For an odd-length antisymmetric filter, paired indices have the same parity but opposite coefficients, so they also cancel. The center coefficient is zero by antisymmetry.

This produces the standard table:

| Type | Length | Coefficient symmetry | DC response | Nyquist response |
|---|---|---|---|---|
| I | Odd | Symmetric | Unconstrained | Unconstrained |
| II | Even | Symmetric | Unconstrained | Forced zero |
| III | Odd | Antisymmetric | Forced zero | Forced zero |
| IV | Even | Antisymmetric | Forced zero | Unconstrained |

“Unconstrained” means the symmetry does not force a zero; the chosen coefficients still might.

A Type II design cannot have a nonzero passband extending through Nyquist. A Type III design cannot have a nonzero passband extending through either endpoint. Antisymmetric filters are also useful for phase-changing operations such as Hilbert-transform approximations, so endpoint constraints should not be mistaken for a complete list of applications.

These are representational limits. No optimization method can overcome a zero imposed by the selected symmetry class.

## Deriving the ideal low-pass impulse response

Define a zero-phase ideal response by

$$
D(\omega)=
\begin{cases}
1,&\lvert\omega\rvert<\omega_c,\\
0,&\omega_c<\lvert\omega\rvert\le\pi.
\end{cases}
$$

Its inverse DTFT is

$$
h_d[n]
=
\frac1{2\pi}
\int_{-\pi}^{\pi}D(\omega)e^{j\omega n}\,d\omega
=
\frac1{2\pi}
\int_{-\omega_c}^{\omega_c}e^{j\omega n}\,d\omega.
$$

For nonzero integer indices,

$$
\begin{aligned}
h_d[n]
&=
\frac{e^{j\omega_c n}-e^{-j\omega_c n}}
{2\pi jn}\\
&=
\frac{\sin(\omega_c n)}{\pi n}.
\end{aligned}
$$

At the center, evaluate the integral directly:

$$
h_d[0]=\frac{\omega_c}{\pi}.
$$

The response is real and symmetric, but it extends infinitely in both directions. It is neither a finite causal filter nor an implementable finite coefficient list.

To obtain a length-$$2M+1$$ filter, retain coefficients on

$$
-M\le n\le M
$$

and shift the result by $$M$$ samples. That shift multiplies the frequency response by

$$
e^{-j\omega M},
$$

giving causal linear phase.

## Why fixed-support truncation minimizes integrated squared error

Let the centered finite approximation be $$g[n]$$, constrained to vanish outside a fixed support set $$S$$. Let its DTFT be $$G(\omega)$$.

Consider

$$
E_2=
\frac1{2\pi}
\int_{-\pi}^{\pi}
\lvert G(\omega)-D(\omega)\rvert^2\,d\omega.
$$

To see why this becomes coefficient error, write the error transform as

$$
E(\omega)=\sum_n e[n]e^{-j\omega n},
\qquad
e[n]=g[n]-h_d[n].
$$

Expanding its squared magnitude introduces terms

$$
e[n]\overline{e[m]}e^{-j\omega(n-m)}.
$$

The integral of the exponential factor is

$$
\frac1{2\pi}
\int_{-\pi}^{\pi}e^{-j\omega(n-m)}\,d\omega
=
\begin{cases}
1,&n=m,\\
0,&n\ne m.
\end{cases}
$$

Therefore Parseval's identity gives

$$
E_2=\sum_n\lvert g[n]-h_d[n]\rvert^2.
$$

Separate the constrained and unconstrained coordinates:

$$
E_2
=
\sum_{n\in S}\lvert g[n]-h_d[n]\rvert^2
+
\sum_{n\notin S}\lvert h_d[n]\rvert^2.
$$

The second sum cannot be changed. The first is minimized by setting every retained coefficient equal to its ideal value:

$$
g[n]=h_d[n],
\qquad n\in S.
$$

This proves truncation is optimal for this particular problem.

It does not say that the central coefficients are always the globally largest coefficients. Fixed contiguous support and selection of an arbitrary sparse support are different optimization problems. It also does not establish optimality under frequency weighting, endpoint normalization, or maximum-error constraints.

## A three-tap example of squared error versus peak error

Choose

$$
\omega_c=\frac{\pi}{2}.
$$

The centered three-tap truncation is

$$
\left[\frac1\pi,\frac12,\frac1\pi\right].
$$

After shifting to causal indices, its signed zero-phase amplitude is

$$
A_{\mathrm{trunc}}(\omega)
=
\frac12+\frac2\pi\cos\omega.
$$

Its DC response is

$$
A_{\mathrm{trunc}}(0)=\frac12+\frac2\pi,
$$

which exceeds one. Integrated squared-error optimality did not impose exact unity at DC.

Now evaluate a concrete band specification:

$$
0\le\omega\le\frac{\pi}{3}
\quad\text{is the passband},
$$

$$
\frac{2\pi}{3}\le\omega\le\pi
\quad\text{is the stopband}.
$$

The desired signed amplitude is one in the passband and zero in the stopband.

Because cosine decreases on this interval, the extrema occur at band endpoints. For the truncated filter, the worst absolute error is

$$
\delta_{\mathrm{trunc}}
=
\frac12-\frac1\pi.
$$

This follows from the passband-edge amplitude

$$
A_{\mathrm{trunc}}\left(\frac{\pi}{3}\right)
=
\frac12+\frac1\pi
$$

and the equal stopband-edge amplitude

$$
A_{\mathrm{trunc}}\left(\frac{2\pi}{3}\right)
=
\frac12-\frac1\pi.
$$

We can now solve the peak-error problem exactly and compare objectives on the same finite filter class.

## Solving a minimax FIR design by hand

Any real symmetric three-tap filter has coefficients

$$
h=[a,b,a]
$$

and signed amplitude

$$
A(\omega)=b+2a\cos\omega.
$$

For the bands above, suppose the maximum error is at most $$\delta$$. Four necessary endpoint inequalities are

$$
b+2a\le1+\delta,
$$

$$
b+a\ge1-\delta,
$$

$$
b-a\le\delta,
$$

$$
b-2a\ge-\delta.
$$

Subtracting the third inequality from the second gives

$$
2a\ge1-2\delta,
\qquad
a\ge\frac12-\delta.
$$

Subtracting the fourth from the first gives

$$
4a\le1+2\delta,
\qquad
a\le\frac14+\frac{\delta}{2}.
$$

Both can hold only if

$$
\frac12-\delta
\le
\frac14+\frac{\delta}{2},
$$

which implies

$$
\delta\ge\frac16.
$$

Now choose

$$
a=\frac13,
\qquad
b=\frac12.
$$

The four endpoint amplitudes become

$$
\frac76,\qquad
\frac56,\qquad
\frac16,\qquad
-\frac16.
$$

Their signed errors alternate:

$$
\frac16,\qquad
-\frac16,\qquad
\frac16,\qquad
-\frac16.
$$

Since the amplitude is monotone within each band, no interior point has larger error. The construction achieves the lower bound, proving

$$
h_{\mathrm{minimax}}
=
\left[\frac13,\frac12,\frac13\right],
\qquad
\delta_{\min}=\frac16.
$$

The truncated design has larger peak error:

$$
\frac12-\frac1\pi>\frac16.
$$

A common normalized smoother,

$$
h=\left[\frac14,\frac12,\frac14\right],
$$

has exact DC gain one and a Nyquist zero, but its worst error for these bands is

$$
\frac14.
$$

The three designs answer different questions. Exact DC normalization, integrated squared error, and worst-band error are not interchangeable objectives.

## Windowing and what changes in frequency

Truncation multiplies the ideal impulse response by a rectangular window:

$$
w_R[n]=
\begin{cases}
1,&-M\le n\le M,\\
0,&\text{otherwise}.
\end{cases}
$$

Its transform is

$$
W_R(\omega)
=
\sum_{n=-M}^{M}e^{-j\omega n}
=
\frac{\sin((M+\frac12)\omega)}
{\sin(\omega/2)},
$$

with the removable limit at zero equal to $$2M+1$$. The formula follows by summing a finite geometric series and factoring out the center phase.

Multiplication in time becomes periodic convolution in frequency:

$$
G(\omega)
=
\frac1{2\pi}
\int_{-\pi}^{\pi}
D(\theta)W_R(\omega-\theta)\,d\theta.
$$

The rectangular window's oscillating positive and negative lobes are therefore integrated across the ideal response's sharp edge. The resulting response can overshoot and ring, as the three-tap example already demonstrates at DC.

No continuous finite response can uniformly approximate a unit jump with error below one half arbitrarily close to both sides of the jump. If its value at the discontinuity is $$a$$, continuity forces the two limiting errors to approach

$$
\lvert a-1\rvert
\quad\text{and}\quad
\lvert a\rvert,
$$

whose maximum is at least one half. This explains why a nonzero transition band is a substantive part of a practical specification.

A tapered window changes the convolution kernel. For example, a centered Hann window is

$$
w_H[n]=
\frac12\left(1+\cos\frac{\pi n}{M}\right),
\qquad
-M\le n\le M,
$$

for positive $$M$$. It gradually reduces coefficients toward the support endpoints.

Expanding the cosine shows its transform is a weighted sum of shifted rectangular-window transforms:

$$
W_H(\omega)
=
\frac12W_R(\omega)
+
\frac14W_R\left(\omega-\frac{\pi}{M}\right)
+
\frac14W_R\left(\omega+\frac{\pi}{M}\right).
$$

Window selection therefore changes the transition and sidelobe structure through explicit frequency-domain interference. It is a design family, not a proof that the final filter satisfies a particular ripple bound.

## Frequency sampling and weighted minimax design

Frequency sampling begins with desired values at DFT frequencies:

$$
D[k],\qquad \omega_k=\frac{2\pi k}{N}.
$$

Define coefficients by the inverse DFT:

$$
h[n]=\frac1N\sum_{k=0}^{N-1}D[k]e^{j\omega_k n}.
$$

DFT orthogonality guarantees

$$
H(e^{j\omega_k})=D[k].
$$

Between those sample frequencies,

$$
H(e^{j\omega})
=
\frac1N
\sum_{k=0}^{N-1}D[k]
\sum_{n=0}^{N-1}e^{-j(\omega-\omega_k)n}.
$$

Thus the continuous response is an interpolation by finite exponential sums. Matching the design grid does not independently bound the response between grid points. Real coefficients also require the appropriate conjugate symmetry in the specified DFT values.

For a linear-phase minimax design, optimize the signed amplitude after removing the known phase factor:

$$
\min_h
\max_{\omega\in\mathcal B}
W(\omega)\lvert A_h(\omega)-D(\omega)\rvert.
$$

The set $$\mathcal B$$ contains the constrained passbands and stopbands, excluding the transition region.

Weights encode relative tolerances. Choosing

$$
W_p=\frac1{\delta_p},
\qquad
W_s=\frac1{\delta_s}
$$

means an optimum weighted error at most one satisfies both requested bounds.

Equal weighted ripples do not mean equal unweighted ripples. A more heavily weighted band receives a smaller allowed raw error.

Parks–McClellan design uses the Remez exchange approach for this fixed-length approximation problem. `scipy.signal.remez` takes the number of taps as an input; it does not automatically return the shortest filter satisfying arbitrary tolerances. Length selection and verification remain separate steps. [SciPy minimax-design documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.remez.html)

A practical verification should check the actual band extrema, endpoint constraints, symmetry, and delay. Sampling a coarse frequency grid can miss a narrow excursion. For a finite cosine expansion, extrema can also be sought through roots of its derivative within each constrained band.

## Revision checklist

| Check | What I should be able to reproduce |
|---|---|
| Specification | Separate passband, stopband, transition width, and frequency units. |
| Cutoff convention | Derive the distinction between half power and half amplitude. |
| FIR stability | Bound the output using the finite coefficient absolute sum. |
| Linear phase | Factor the common delay by pairing symmetric coefficients. |
| Four types | Derive each forced endpoint zero from parity and symmetry. |
| Ideal filter | Integrate the brick-wall response to obtain the sinc coefficients. |
| Squared-error optimum | Prove fixed-support truncation using Parseval's identity. |
| Minimax example | Derive the lower bound and construct the three-tap optimum. |
| Windowing | Explain why multiplying coefficients convolves responses in frequency. |
| Design software | Distinguish fixed-length optimization from finding a feasible length. |

## Why it matters for my work

This is a concrete example of an optimization objective failing to express the operational requirement. Average spectral error, worst-band error, delay, and endpoint normalization are different quantities. I want the same distinction made when a model's average loss is used to justify behavior under a stricter requirement.

## What I have not resolved

For any physiological preprocessing task, the passband, stopband, and permitted delay must come from the signal and downstream use. I have not established those application-specific tolerances here, and a generic low-pass design cannot supply them.
