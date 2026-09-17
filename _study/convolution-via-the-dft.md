---
layout: study_note
title: "Convolution via the DFT: Circular, Linear, and the Padding You Forgot Was a Choice"
description: "Why multiplying two DFTs gives the wrong answer, the length condition that fixes it, and why full/same/valid is the same decision a CNN makes at every layer."
og_image: "https://sehyeony0518.github.io/assets/img/og/convolution-via-the-dft.png"
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
subgroup: "Fourier Computation & Filter Design"
order: 4
source: "Independent study"
written: true
updated: "2026-09-15"
---

Multiplying DFTs does not give an incorrect convolution. It gives circular convolution, the convolution appropriate to a periodic index set. The mistake is to ask for a finite linear convolution while silently supplying periodic boundary conditions.

The distinction can be derived from one finite geometric sum. Once that sum is understood, the padding rule, wrapped filter indices, and block-processing algorithms follow from the same calculation.

## Fixing the indexing before transforming

Let the input have support

$$
x[n]=0\quad\text{outside }0\le n\le M-1,
$$

and the filter have support

$$
h[n]=0\quad\text{outside }0\le n\le K-1.
$$

Their linear convolution is

$$
y[n]=\sum_{m=-\infty}^{\infty}x[m]h[n-m].
$$

A nonzero product requires both

$$
0\le m\le M-1
$$

and

$$
0\le n-m\le K-1.
$$

The smallest possible output index is zero. The largest is

$$
(M-1)+(K-1)=M+K-2.
$$

There are therefore at most

$$
M+K-1
$$

output positions. If the stated endpoint coefficients are nonzero, both extreme output samples are nonzero, so this support length is attained.

This argument explains why a convolution needs extra storage. The output index is a sum of an input index and a filter index. A buffer large enough to hold either operand need not be large enough to hold their sum.

The zero extension here is an explicit mathematical choice. A physical recording is not necessarily zero outside its observed interval, but treating the finite array as a zero-extended sequence defines a complete, reproducible calculation.

## Deriving the inverse DFT from orthogonality

For a length-$$L$$ array, use

$$
X[k]
=
\sum_{n=0}^{L-1}
x[n]e^{-j2\pi kn/L},
\qquad
0\le k\le L-1.
$$

The essential identity is

$$
\frac1L
\sum_{k=0}^{L-1}e^{j2\pi kr/L}
=
\begin{cases}
1,&r\equiv0\pmod L,\\
0,&r\not\equiv0\pmod L.
\end{cases}
$$

To derive it, set

$$
q=e^{j2\pi r/L}.
$$

If the integer $$r$$ is a multiple of $$L$$, every summand equals one. Otherwise,

$$
\sum_{k=0}^{L-1}q^k
=
\frac{1-q^L}{1-q}
=
0,
$$

because

$$
q^L=e^{j2\pi r}=1
$$

while the denominator is nonzero.

Now insert the forward transform into the proposed inverse:

$$
\begin{aligned}
\frac1L\sum_{k=0}^{L-1}X[k]e^{j2\pi kn/L}
&=
\sum_{m=0}^{L-1}x[m]
\left(
\frac1L\sum_{k=0}^{L-1}
e^{j2\pi k(n-m)/L}
\right)\\
&=x[n].
\end{aligned}
$$

Thus

$$
x[n]=
\frac1L\sum_{k=0}^{L-1}X[k]e^{j2\pi kn/L}.
$$

The normalization is forced by the fact that the matching exponential sum equals $$L$$. Other conventions distribute this normalization between the forward and inverse transforms, but their product must still give the identity.

## The relationship to the DTFT

For a finite zero-extended sequence,

$$
X_{\mathrm{DTFT}}(e^{j\omega})
=
\sum_{n=0}^{L-1}x[n]e^{-j\omega n}.
$$

Evaluating at equally spaced frequencies gives

$$
X[k]
=
X_{\mathrm{DTFT}}(e^{j\omega})
\bigg|_{\omega=2\pi k/L}.
$$

This is an exact sampling relationship for the specified finite sequence.

The continuous frequency variable does not make the DTFT useless computationally. Its value at any chosen frequency is a finite sum here. The DFT provides a particular collection of samples that also supports exact finite-dimensional inversion.

For an arbitrary infinite sequence, a length-$$L$$ DFT of a truncated segment is the sampled DTFT of that segment, not automatically the sampled DTFT of the entire original sequence. Truncation has already changed the signal.

Likewise, zero-padding a fixed segment samples its same DTFT more densely. It adds frequency-grid points without adding observations or making two unresolved components intrinsically separable.

## Deriving circular convolution from a product of DFTs

Let

$$
Y[k]=X[k]H[k].
$$

Expand both forward transforms inside the inverse:

$$
\begin{aligned}
y_{\mathrm c}[n]
&=
\frac1L\sum_{k=0}^{L-1}
X[k]H[k]e^{j2\pi kn/L}\\
&=
\sum_{m=0}^{L-1}
\sum_{r=0}^{L-1}
x[m]h[r]
\left(
\frac1L\sum_{k=0}^{L-1}
e^{j2\pi k(n-m-r)/L}
\right).
\end{aligned}
$$

The parenthesized sum is nonzero exactly when

$$
n-m-r\equiv0\pmod L.
$$

Therefore,

$$
y_{\mathrm c}[n]
=
\sum_{m=0}^{L-1}
x[m]h[(n-m)\bmod L].
$$

This is circular convolution. The modular index is not an implementation accident. It is the direct consequence of the DFT's orthogonality relation.

Another way to express the result is to first compute the zero-extended linear convolution and then fold it:

$$
y_{\mathrm c}[n]
=
\sum_{q\in\mathbb Z}y_{\mathrm{lin}}[n+qL],
\qquad
0\le n\le L-1.
$$

Output samples whose indices differ by a multiple of the transform length are added together. This is time-domain aliasing.

## A complete numerical example, including the wrong length

Construct

$$
x=[1,2,3],
\qquad
h=[1,-1,2].
$$

Direct linear convolution gives

$$
\begin{aligned}
y[0]&=1,\\
y[1]&=-1+2=1,\\
y[2]&=2-2+3=3,\\
y[3]&=4-3=1,\\
y[4]&=6.
\end{aligned}
$$

Hence

$$
y_{\mathrm{lin}}=[1,1,3,1,6].
$$

A length-three transform folds this into

$$
y_{\mathrm c}=[1+1,\;1+6,\;3]=[2,7,3].
$$

A length-four transform folds only the final sample:

$$
y_{\mathrm c}=[1+6,\;1,\;3,\;1]=[7,1,3,1].
$$

The length-four frequency-domain calculation is small enough to verify directly. Pad the operands to

$$
x_4=[1,2,3,0],
\qquad
h_4=[1,-1,2,0].
$$

Their DFTs are

$$
X=[6,\;-2-2j,\;2,\;-2+2j],
$$

$$
H=[2,\;-1+j,\;4,\;-1-j].
$$

Pointwise multiplication gives

$$
Y=[12,4,8,4].
$$

For instance,

$$
(-2-2j)(-1+j)=4.
$$

The inverse transform yields

$$
\begin{aligned}
y_{\mathrm c}[0]&=\frac{12+4+8+4}{4}=7,\\
y_{\mathrm c}[1]&=\frac{12+4j-8-4j}{4}=1,\\
y_{\mathrm c}[2]&=\frac{12-4+8-4}{4}=3,\\
y_{\mathrm c}[3]&=\frac{12-4j-8+4j}{4}=1.
\end{aligned}
$$

This exactly matches the folded linear result.

At length five, the complete linear output fits in one period:

$$
y_{\mathrm c}=[1,1,3,1,6].
$$

The padding condition is therefore

$$
L\ge M+K-1.
$$

It guarantees correctness for all operand values with those support bounds. Shorter transforms can happen to work for special coefficients or cancellations, but they do not provide that general guarantee.

## Why a simple checksum cannot detect wraparound

Convolution satisfies

$$
\sum_n y_{\mathrm{lin}}[n]
=
\left(\sum_n x[n]\right)
\left(\sum_n h[n]\right).
$$

The derivation is just a rearrangement:

$$
\sum_n\sum_m x[m]h[n-m]
=
\sum_m x[m]\sum_r h[r].
$$

For the example,

$$
\sum_n x[n]=6,
\qquad
\sum_n h[n]=2,
$$

so the output sum is twelve.

But both incorrect circular outputs also sum to twelve:

$$
2+7+3=12,
\qquad
7+1+3+1=12.
$$

Folding preserves the sum. It redistributes samples rather than necessarily changing their total.

A DC-gain check is useful, but it cannot replace an index-by-index comparison or a support argument. A test must be sensitive to the failure mode it is intended to catch.

## Centered filters and negative indices

Consider a symmetric smoothing filter centered at zero:

$$
h[-1]=\frac14,
\qquad
h[0]=\frac12,
\qquad
h[1]=\frac14.
$$

For a length-five circular buffer, the correct placement is

$$
h_{\mathrm{buf}}
=
\left[\frac12,\frac14,0,0,\frac14\right].
$$

The coefficient at negative one belongs in buffer position four because

$$
-1\equiv4\pmod5.
$$

Apply this filter to the zero-extended input

$$
x=[1,2,3].
$$

The chronological linear output, indexed from negative one through three, is

$$
\begin{array}{c|ccccc}
n&-1&0&1&2&3\\ \hline
y[n]&\frac14&1&2&2&\frac34
\end{array}.
$$

For example,

$$
y[1]
=
\frac14(1)+\frac12(2)+\frac14(3)
=
2.
$$

The circular-buffer result is

$$
\left[1,2,2,\frac34,\frac14\right].
$$

The final buffer entry is the output at negative one. Moving it to the front restores chronological order.

If the coefficients are instead stored as

$$
\left[\frac14,\frac12,\frac14,0,0\right],
$$

the array represents a causal filter delayed by one sample. Its values resemble the centered filter, but its time origin differs.

A delay has a frequency-domain signature:

$$
h_{\mathrm{delayed}}[n]=h[n-1]
\quad\Longrightarrow\quad
H_{\mathrm{delayed}}(e^{j\omega})
=
e^{-j\omega}H(e^{j\omega}).
$$

An indexing error can therefore preserve magnitude while changing phase and alignment.

## Output cropping and boundary extension are separate decisions

For the zero-extended convolution above, `full`, `same`, and `valid` select different output positions. They do not, by themselves, define three different extension rules.

When the input is at least as long as the filter:

- `full` retains all $$M+K-1$$ output positions.
- A centered `same` convention retains $$M$$ positions.
- `valid` retains $$M-K+1$$ positions where all filter taps overlap observed input samples.

For

$$
x=[1,2,3],
\qquad
h=[1,-1,2],
$$

the full result is

$$
[1,1,3,1,6].
$$

The centered same-length crop is

$$
[1,3,1],
$$

and the valid result is

$$
[3].
$$

The valid output is the sample at index two, where all three filter coefficients overlap the three observed input values.

API conventions require care. NumPy's `same` result has the length of the longer operand, and its `valid` length is the difference between operand lengths plus one. Even-length kernels also require a choice of which side receives the extra discarded sample. These are documented conventions, not universal consequences of the word “same.” [NumPy convolution documentation](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html)

Boundary extension is a separate choice: zeros, periodic repetition, reflection, or another rule. One can apply a same-length crop after any of those extensions. The valid interior avoids reliance on the extension, but it does not recover output near unobserved boundaries.

## Convolution, correlation, and translation

Many neural-network layers called convolution implement cross-correlation. For real coefficients, a one-dimensional correlation-like operation is

$$
c[n]=\sum_k h[k]x[n+k].
$$

The sign of the filter index differs from convolution:

$$
y[n]=\sum_k h[k]x[n-k].
$$

With

$$
x=[1,2,3],
\qquad
h=[1,2],
$$

the valid convolution samples are

$$
[2+2,\;3+4]=[4,7].
$$

The valid correlation samples are

$$
[1+4,\;2+6]=[5,8].
$$

Symmetric filters can conceal this distinction because reversal leaves their coefficients unchanged. An asymmetric test filter exposes it immediately.

On an infinite domain, convolution is translation equivariant. If

$$
x_r[n]=x[n-r],
$$

then

$$
(h*x_r)[n]=(h*x)[n-r].
$$

The output moves with the input. It is not invariant, which would require the output to remain unchanged.

Finite cropping and boundary extension can break the corresponding relation near the edges. This can be demonstrated from the index formulas without claiming a measured effect in a particular neural network.

## Why the FFT reduces the arithmetic

The direct DFT computes each of $$L$$ outputs using $$L$$ terms, giving quadratic arithmetic cost.

For an even transform length, split the sum into even and odd input indices:

$$
\begin{aligned}
X[k]
&=
\sum_{r=0}^{L/2-1}
x[2r]e^{-j2\pi kr/(L/2)}\\
&\quad+
e^{-j2\pi k/L}
\sum_{r=0}^{L/2-1}
x[2r+1]e^{-j2\pi kr/(L/2)}.
\end{aligned}
$$

Calling the two smaller transforms $$E[k]$$ and $$O[k]$$,

$$
X[k]=E[k]+e^{-j2\pi k/L}O[k].
$$

The other half follows from the same quantities:

$$
X[k+L/2]=E[k]-e^{-j2\pi k/L}O[k].
$$

For power-of-two lengths, recursive splitting gives

$$
T(L)=2T(L/2)+O(L).
$$

There are logarithmically many levels, with linear work per level:

$$
T(L)=O(L\log L).
$$

The FFT is an algorithm for the DFT, not a different transform.

FFT convolution therefore replaces a direct cost proportional to the product of operand lengths with transforms and pointwise products. The practical crossover depends on hardware, implementation, filter reuse, and memory movement. A very short filter can still favor direct convolution.

## Overlap-add: making room for every block's tail

For a long input, split it into blocks of length $$B$$. Each block convolved with a length-$$K$$ filter has length

$$
B+K-1.
$$

Transform each block using at least that length, then place its output at the block's original starting index. Adjacent outputs overlap because each block produces a filter tail.

Take

$$
x=[1,2,3,4],
\qquad
h=[1,1,1],
$$

and split the input into two blocks:

$$
x_0=[1,2],
\qquad
x_1=[3,4].
$$

Their separate linear convolutions are

$$
y_0=[1,3,3,2],
\qquad
y_1=[3,7,7,4].
$$

The second block begins at index two. Aligning and adding gives

$$
\begin{aligned}
y
&=
[1,3,3,2,0,0]\\
&\quad+
[0,0,3,7,7,4]\\
&=
[1,3,6,9,7,4].
\end{aligned}
$$

The overlapping values are added because the original convolution is linear: both input blocks contribute to those output times.

Discarding either tail would change the answer. The extra storage is a consequence of the filter's support, not optional padding for numerical convenience.

## Overlap-save: discard exactly the contaminated prefix

Overlap-save takes a different approach. Use a transform length $$L$$ and filter length $$K$$. Each block contains

$$
B=L-K+1
$$

new input samples plus the previous

$$
K-1
$$

samples.

Circular convolution contaminates the first $$K-1$$ outputs through wraparound. The remaining $$B$$ outputs agree with the desired linear convolution.

For the same example, choose

$$
L=4,
\qquad
K=3,
\qquad
B=2.
$$

The input blocks, including startup and final flushing, are

$$
[0,0,1,2],
\qquad
[1,2,3,4],
\qquad
[3,4,0,0].
$$

Circularly convolving each with the padded filter

$$
[1,1,1,0]
$$

gives

$$
[3,2,1,3],
\qquad
[8,7,6,9],
\qquad
[3,7,7,4].
$$

Discard the first two entries of each result:

$$
[1,3],
\qquad
[6,9],
\qquad
[7,4].
$$

Concatenating recovers

$$
[1,3,6,9,7,4].
$$

Overlap-add preserves and sums tails. Overlap-save preserves input history and discards the known corrupted prefix. Both follow from the same support and wrapping calculation.

## Revision checklist

| Check | What I should be able to reproduce |
|---|---|
| Output support | Derive the maximum output index from the operand supports. |
| DFT inversion | Evaluate the finite geometric sum that gives modular orthogonality. |
| Convolution theorem | Show precisely where the modular index enters. |
| Padding | Derive the sufficient transform-length condition. |
| Worked example | Recover both the linear result and its shorter-period folds. |
| Negative indices | Place a centered filter's negative-time taps at the buffer end. |
| Cropping | Separate output selection from boundary extension. |
| Correlation | Use an asymmetric filter to distinguish it from convolution. |
| FFT cost | Derive the even–odd decomposition and recursion cost. |
| Block processing | Explain which samples are added or discarded, and why. |

## Why it matters for my work

Convolutional preprocessing and neural-network layers both make boundary and alignment choices. I want those choices stated separately from output shape. A result can have the expected dimensions and DC gain while still wrapping, shifting, or reversing the intended operation.

## What I have not resolved

The fastest implementation for a real workload requires measurement with its actual input lengths, filter reuse, and latency requirements. The algebra determines correctness; it does not determine that implementation crossover.
