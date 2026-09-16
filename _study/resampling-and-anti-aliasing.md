---
layout: study_note
title: "Resampling and Anti-Aliasing: Why Half of a Checkerboard Is Grey"
description: "How downsampling folds the spectrum, why anti-aliasing must come first, and how interpolation, rational resampling, and checkerboard resizing set the filter cutoff."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
subgroup: "Sampling, Interpolation & Estimation"
order: 8
source: "Independent study"
written: true
updated: "2026-09-15"
---

Resampling changes the locations at which a signal is represented. The main difficulty is that a new grid can represent a different range of frequencies from the old grid.

A finer grid requires an interpolation model. A coarser grid requires deciding which information to remove before it becomes indistinguishable from something else.

The checkerboard makes that distinction visible. If black and white are represented by zero and one, averaging a complete checkerboard cell gives one half. Keeping only a particular subset of its pixels can instead give all zero or all one. Both outputs are smooth, but they answer different questions.

To understand why filtering belongs before one operation and after the other, start with the spectrum of sampling itself.

## Sampling creates shifted spectral copies

Use frequency in hertz for a continuous-time signal:

$$
X_c(f)
=
\int_{-\infty}^{\infty}
x_c(t)e^{-j2\pi ft}\,dt.
$$

Let the sampling period and rate be

$$
T_s=\frac1{F_s}.
$$

Ideal sampling multiplies the signal by an impulse train:

$$
p(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT_s).
$$

The sampled impulse train is therefore

$$
x_s(t)
=
x_c(t)p(t)
=
\sum_n x_c(nT_s)\delta(t-nT_s).
$$

Why does this create spectral copies? The sampling train is periodic, so write its Fourier series:

$$
p(t)=\sum_{k=-\infty}^{\infty}c_k e^{j2\pi kF_st}.
$$

Choose a period containing exactly one impulse. Its Fourier-series coefficient is

$$
c_k
=
\frac1{T_s}
\int_{\text{one period}}
p(t)e^{-j2\pi kF_st}\,dt
=
\frac1{T_s}
=
F_s.
$$

Thus, in the distributional sense appropriate to impulses,

$$
p(t)=F_s\sum_k e^{j2\pi kF_st}.
$$

Multiplying the original signal gives

$$
x_s(t)
=
F_s\sum_k x_c(t)e^{j2\pi kF_st}.
$$

For each term, substitute into the Fourier-transform integral:

$$
\int x_c(t)e^{j2\pi kF_st}e^{-j2\pi ft}\,dt
=
X_c(f-kF_s).
$$

Consequently,

$$
\boxed{
X_s(f)=F_s\sum_{k=-\infty}^{\infty}X_c(f-kF_s)
}.
$$

Sampling replicates the original spectrum at every integer multiple of the sampling rate and adds the replicas together. This is an exact description of ideal sampling, not a numerical approximation.

## Nyquist is a non-overlap condition

Assume a baseband signal whose spectrum is zero outside

$$
-B\le f\le B.
$$

The copy centred at zero occupies that interval. The neighbouring copy centred at the sampling rate occupies

$$
F_s-B\le f\le F_s+B.
$$

To leave a gap between them, require

$$
B<F_s-B,
$$

or

$$
\boxed{F_s>2B}.
$$

The familiar Nyquist condition is therefore a geometric condition on the support of the spectral copies.

At exact equality, the copies touch. Boundary spectral lines need special treatment. For example,

$$
x_c(t)=\sin(2\pi(F_s/2)t)
$$

has samples

$$
x_c(nT_s)=\sin(\pi n)=0.
$$

A nonzero continuous signal has become indistinguishable from zero. Statements allowing equality require assumptions about what happens at the band edge. A strict bandwidth margin avoids that ambiguity.

Aliasing also follows directly from the samples of an exponential:

$$
e^{j2\pi(f+kF_s)n/F_s}
=
e^{j2\pi fn/F_s}e^{j2\pi kn}
=
e^{j2\pi fn/F_s}.
$$

Frequencies separated by an integer multiple of the sampling rate produce identical sampled exponentials.

For a constructed example, sampling a cosine at $$6\,\mathrm{Hz}$$ with rate $$8\,\mathrm{Hz}$$ gives

$$
\cos\left(2\pi\frac68n\right)
=
\cos\left(2\pi\frac28n\right).
$$

Both yield

$$
[1,0,-1,0,1,0,-1,0,\ldots].
$$

The sampled data alone cannot determine which cosine was present.

This is the sense in which aliasing is irreversible: the sampling map is many-to-one over the unrestricted signal class. Additional prior information can sometimes identify a signal, but ordinary post-filtering cannot separate arbitrary components that have already been added together.

The baseband condition is not the most general possible sampling condition. Special bandpass or sparse spectra can support other sampling arrangements. The low-pass rules in this note concern preserving an arbitrary baseband signal.

## Reconstruction selects and rescales one copy

When the copies do not overlap, an ideal reconstruction filter can select the central copy. Since sampling multiplied its spectrum by the sampling rate, the reconstruction gain must undo that factor:

$$
R_c(f)=
\begin{cases}
T_s,& |f|<F_s/2,\\
0,& |f|>F_s/2.
\end{cases}
$$

Within the signal band,

$$
R_c(f)X_s(f)=T_sF_sX_c(f)=X_c(f).
$$

The inverse transform of the reconstruction filter is

$$
\begin{aligned}
r_c(t)
&=
T_s\int_{-F_s/2}^{F_s/2}e^{j2\pi ft}\,df\\
&=
\frac{\sin(\pi F_st)}{\pi F_st}\\
&=
\operatorname{sinc}(t/T_s),
\end{aligned}
$$

where the normalized sinc is defined by

$$
\operatorname{sinc}(u)=\frac{\sin(\pi u)}{\pi u},
\qquad
\operatorname{sinc}(0)=1.
$$

Convolving the sampled impulse train with this response gives

$$
x_c(t)
=
\sum_n x[n]\operatorname{sinc}(t/T_s-n).
$$

This explains both the interpolation kernel and its gain. The filter selects one spectral copy while retaining the amplitudes of the original continuous signal.

It also identifies an assumption that finite arrays cannot establish by themselves: ideal reconstruction assumes an appropriate bandlimited signal and samples extending over the required time range.

## Deriving the spectrum of downsampling

Now work with a discrete-time sequence and its DTFT:

$$
X(\omega)
=
\sum_{n=-\infty}^{\infty}x[n]e^{-j\omega n}.
$$

The frequency variable is in radians per input sample, and the DTFT repeats every full turn:

$$
X(\omega+2\pi)=X(\omega).
$$

Downsampling by a positive integer $$M$$ retains

$$
y[m]=x[mM].
$$

Use a selector that is one at multiples of the downsampling factor and zero elsewhere:

$$
s_M[n]
=
\frac1M\sum_{r=0}^{M-1}e^{j2\pi rn/M}.
$$

If the index is a multiple of the factor, every term is one. Otherwise, the finite geometric series sums to zero.

Let $$\Omega$$ denote radians per output sample. Then

$$
\begin{aligned}
Y(\Omega)
&=\sum_m x[mM]e^{-j\Omega m}\\
&=\sum_n x[n]s_M[n]e^{-j\Omega n/M}\\
&=
\frac1M\sum_{r=0}^{M-1}
\sum_n x[n]e^{-j(\Omega-2\pi r)n/M}.
\end{aligned}
$$

Therefore,

$$
\boxed{
Y(\Omega)
=
\frac1M
\sum_{r=0}^{M-1}
X\left(\frac{\Omega-2\pi r}{M}\right)
}.
$$

There are multiple contributions to each output frequency. The summation is the aliasing mechanism.

A single input exponential makes the frequency scaling easier to picture:

$$
x[n]=e^{j\omega_0n}
\quad\Longrightarrow\quad
y[m]=e^{jM\omega_0m}.
$$

Thus,

$$
\Omega_0=M\omega_0
\pmod{2\pi}.
$$

The frequency occupies a larger fraction of a full turn per output sample because output samples are farther apart in time.

## Why decimation needs a low-pass filter first

The output sampling rate is

$$
F_{\mathrm{out}}=\frac{F_{\mathrm{in}}}{M}.
$$

Its Nyquist frequency, expressed in physical units, is

$$
\frac{F_{\mathrm{in}}}{2M}.
$$

Converting that frequency into radians per input sample gives

$$
\omega_c
=
2\pi
\frac{F_{\mathrm{in}}/(2M)}{F_{\mathrm{in}}}
=
\frac{\pi}{M}.
$$

For arbitrary baseband input, the ideal anti-aliasing filter is therefore

$$
H_{\mathrm{AA}}(\omega)=
\begin{cases}
1,&|\omega|<\pi/M,\\
0,&\pi/M<|\omega|\le\pi.
\end{cases}
$$

The operational order is

$$
\boxed{
\text{low-pass filtering}
\;\longrightarrow\;
\text{keeping every }M\text{th sample}
}.
$$

The filter removes content that the new grid cannot represent before that content folds into the retained band.

Consider a constructed conversion from $$40\,\mathrm{kHz}$$ to $$10\,\mathrm{kHz}$$. The factor is four, and the new Nyquist frequency is $$5\,\mathrm{kHz}$$.

Choose the input

$$
x[n]
=
\cos\left(2\pi\frac3{40}n\right)
+
\frac12\cos\left(2\pi\frac7{40}n\right).
$$

It contains a unit-amplitude component at $$3\,\mathrm{kHz}$$ and a half-amplitude component at $$7\,\mathrm{kHz}$$.

Keeping every fourth sample without filtering gives

$$
y[m]
=
\cos(0.6\pi m)
+
\frac12\cos(1.4\pi m).
$$

For integer output indices,

$$
\cos(1.4\pi m)
=
\cos(2\pi m-0.6\pi m)
=
\cos(0.6\pi m).
$$

Hence

$$
y[m]=\frac32\cos(0.6\pi m).
$$

The unwanted higher-frequency tone has increased the amplitude of the wanted tone. Both now occupy the same output frequency.

Filtering first with an ideal cutoff at $$5\,\mathrm{kHz}$$ removes the second term and yields

$$
y_{\mathrm{filtered}}[m]=\cos(0.6\pi m).
$$

A filter applied afterward sees only the combined coefficient. It cannot know how much came from each original tone.

## The checkerboard and the limits of simple averaging

Define a two-dimensional checkerboard by

$$
I[p,q]=\frac{1+(-1)^{p+q}}2.
$$

A reduction by two along both axes that retains even-indexed pixels gives

$$
I[2r,2s]=1.
$$

Changing the sampling offset can instead give

$$
I[2r+1,2s]=0.
$$

By contrast, every complete two-by-two cell contains two zeros and two ones:

$$
\frac14(1+0+0+1)=\frac12.
$$

Thus grey is the answer for an output pixel defined as the average over that cell. A two-by-two reduction covers four input pixels, not two. The intended pixel footprint and grid alignment are part of the definition of resizing.

In one dimension, consider the centred three-tap filter

$$
h[-1]=\frac14,
\qquad
h[0]=\frac12,
\qquad
h[1]=\frac14.
$$

Its response is

$$
\begin{aligned}
H(\omega)
&=\frac14e^{j\omega}+\frac12+\frac14e^{-j\omega}\\
&=\frac12+\frac12\cos\omega\\
&=\cos^2(\omega/2).
\end{aligned}
$$

At the alternating sequence's frequency,

$$
H(\pi)=0.
$$

It therefore removes the alternating part exactly, leaving the constant mean.

That success does not make it an ideal anti-aliasing filter. For downsampling by two, all frequencies above $$\pi/2$$ are outside the desired input passband, but this short filter is generally nonzero there. For example,

$$
H(3\pi/4)=\frac{2-\sqrt2}{4}\approx0.1464.
$$

A component at that frequency survives with reduced amplitude and can still alias.

The checkerboard is therefore a useful test of one particular frequency and sampling phase. Passing it is not proof of adequate attenuation throughout the stopband.

## Why interpolation needs a low-pass filter afterward

Upsampling by a positive integer $$L$$ inserts zeros:

$$
u[n]=
\begin{cases}
x[n/L],&n\text{ is a multiple of }L,\\
0,&\text{otherwise}.
\end{cases}
$$

Compute its DTFT:

$$
\begin{aligned}
U(\Omega)
&=\sum_m x[m]e^{-j\Omega Lm}\\
&=X(L\Omega).
\end{aligned}
$$

The original spectrum is compressed along the new normalized frequency axis. Since the original DTFT is periodic, repeated images appear inside the new frequency interval.

The central image occupies

$$
|\Omega|<\pi/L.
$$

An ideal interpolation filter keeps that image:

$$
H_{\mathrm{I}}(\Omega)=
\begin{cases}
L,&|\Omega|<\pi/L,\\
0,&\pi/L<|\Omega|\le\pi.
\end{cases}
$$

The gain deserves a derivation. Start with a constant sequence whose value is $$c$$. After inserting zeros, only one sample in each group of $$L$$ is nonzero. The constant Fourier-series component of that periodic sequence is therefore

$$
c/L.
$$

Removing its nonzero-frequency images leaves that constant component. Gain $$L$$ restores the desired value $$c$$.

The original retained samples were not individually divided by the upsampling factor. Their amplitudes stayed unchanged. The gain corrects the selected spectral component after zero insertion.

The filter's impulse response is

$$
\begin{aligned}
h_{\mathrm{I}}[n]
&=
\frac{L}{2\pi}
\int_{-\pi/L}^{\pi/L}e^{j\Omega n}\,d\Omega\\
&=
\operatorname{sinc}(n/L).
\end{aligned}
$$

At original sample locations,

$$
h_{\mathrm{I}}[Lm]=\operatorname{sinc}(m),
$$

which is one for zero index and zero at every other integer. Consequently, ideal interpolation preserves the original samples while filling the intervening positions.

No new information has been measured. The new values follow from the reconstruction model.

## Rational resampling and the common frequency axis

For a sampling-rate ratio

$$
\frac{F_{\mathrm{out}}}{F_{\mathrm{in}}}=\frac{L}{M},
$$

reduce the ratio to relatively prime integers and use

$$
x
\;\longrightarrow\;
\uparrow L
\;\longrightarrow\;
H
\;\longrightarrow\;
\downarrow M.
$$

The intermediate sampling rate is

$$
F_{\mathrm{mid}}=LF_{\mathrm{in}}.
$$

At that rate, interpolation requires removing images above $$\pi/L$$, while the later downsampling requires suppressing content above $$\pi/M$$. The ideal combined filter therefore has gain $$L$$ and cutoff

$$
\boxed{
\Omega_c=\min(\pi/L,\pi/M)
}.
$$

Both cutoffs are expressed in radians per intermediate sample. Comparing cutoffs normalized to different sampling rates would be meaningless.

In physical frequency,

$$
F_c
=
\frac12\min(F_{\mathrm{in}},F_{\mathrm{out}}).
$$

For a constructed conversion from $$12\,\mathrm{kHz}$$ to $$18\,\mathrm{kHz}$$,

$$
L=3,
\qquad
M=2,
\qquad
F_{\mathrm{mid}}=36\,\mathrm{kHz}.
$$

The combined cutoff is

$$
\Omega_c=\min(\pi/3,\pi/2)=\pi/3,
$$

or

$$
F_c=6\,\mathrm{kHz}.
$$

If one instead first decimated the input to $$6\,\mathrm{kHz}$$, anti-aliasing at that intermediate rate would restrict the signal to below $$3\,\mathrm{kHz}$$. A component at $$4\,\mathrm{kHz}$$ would be removed even though both the original and final grids can represent it.

This explains the standard conceptual ordering. Special rearrangements can be valid when bandwidth restrictions are already satisfied or when multirate identities are applied carefully; the example does not establish a universal prohibition on every reordered implementation.

Efficient software need not materialize the inserted zeros. Combining filtering and output selection gives

$$
y[m]
=
\sum_k x[k]h[mM-kL].
$$

Only taps in one residue class modulo the interpolation factor contribute to a particular output. This is the basis of polyphase evaluation.

For the ratio above, the selected phases are

$$
2m\bmod3=0,2,1,0,2,1,\ldots.
$$

The mathematics is unchanged; unnecessary multiplications by inserted zeros are avoided.

## Practical cutoffs require a transition band

An ideal cutoff jumps instantly from full transmission to complete rejection. A finite filter cannot reproduce that response exactly.

A practical specification needs at least a passband edge, a stopband edge, an allowed passband error, and an allowed stopband leakage. “Cutoff” alone does not state those requirements.

For the earlier conversion to $$10\,\mathrm{kHz}$$, one possible design specification is a passband ending at $$4\,\mathrm{kHz}$$ and a stopband beginning at $$5\,\mathrm{kHz}$$. These are chosen design values, not measured performance.

At the original rate, they correspond to

$$
\omega_p=0.2\pi,
\qquad
\omega_s=0.25\pi.
$$

A conservative design reaches its required stopband attenuation by the new Nyquist limit. Any residual response beyond that limit creates residual aliasing.

Image resizing has the same issue along each spatial axis. Changing the scale requires changing the relevant bandwidth restriction. Merely choosing a smooth interpolation kernel does not establish that it suppresses the frequencies forbidden by the new grid.

A strided convolution also needs precise language: it already includes convolution by a filter, followed by sample selection. The problem is that an arbitrary learned kernel is not guaranteed to be a suitable low-pass filter. Its aliasing behaviour must be assessed from its response and the signal entering it.

Boundary extension, grid origin, and filter delay also affect the output. Zero extension, reflection, and periodic extension supply different values outside the observed array. Those choices belong in the description of the resampling operation.

## Revision checklist

| Question | What I should be able to reproduce |
|---|---|
| Why does sampling replicate a spectrum? | Expand the impulse train and apply the modulation identity. |
| Where does the Nyquist condition come from? | Prevent neighbouring support intervals from overlapping. |
| Why is exact equality delicate? | A sinusoid at the boundary can disappear at every sample. |
| What does downsampling do? | Sum scaled, shifted DTFT copies through the sample selector. |
| Why filter before decimation? | Prevent distinct input components from reaching the same output frequency. |
| Which cutoff is required? | Use the new Nyquist limit expressed on the filter's sampling-rate axis. |
| Why is interpolation gain needed? | The selected constant component after zero insertion is reduced by the interpolation factor. |
| Why combine the rational-resampling filters? | Both constraints apply at the common intermediate rate. |
| What does a checkerboard test miss? | Frequencies other than the alternating pattern and effects of boundaries. |
| What makes a practical specification complete? | Passband, transition band, stopband attenuation, alignment, and boundary handling. |

## Why it matters for my work

Image and volume preprocessing changes the spatial frequencies available to a model. I need to record the resampling ratio, physical spacing, kernel, grid alignment, and boundary rule, then check whether the filter is appropriate for that ratio.

## What I have not resolved

Measure the frequency response and aliasing of the exact resize and volume-resampling configurations used in my pipeline, across the scale factors present in the data.
