---
layout: study_note
title: "The FFT: Where a 200× Speedup Comes From"
description: "Splitting a transform into its even and odd samples, the recursion that turns N² into N log N, and why an algorithm can matter more than the hardware."
og_image: "https://sehyeony0518.github.io/assets/img/og/the-fast-fourier-transform.png"
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
subgroup: "Fourier Computation & Filter Design"
order: 5
source: "Independent study"
written: true
updated: "2026-09-15"
---

The fast Fourier transform is an algorithm for computing the discrete Fourier transform. It changes how the calculation is organized, while preserving the mathematical transform.

The number in this note's title needs a qualification: approximately two hundred is a ratio of multiplication counts for a particular transform length and counting convention. It is not a measured runtime speedup. Actual runtime also depends on memory access, implementation, arithmetic, and hardware.

The useful question is therefore precise: which calculations in the direct DFT can be reused, and how does that reuse change the cost?

## The DFT and the work done by direct evaluation

For a sequence of length $$N$$, define the forward DFT by

$$
X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi nk/N},
\qquad k=0,\ldots,N-1,
$$

where $$j^2=-1$$. Introduce the abbreviation

$$
W_N=e^{-j2\pi/N},
$$

so that

$$
X[k]=\sum_{n=0}^{N-1}x[n]W_N^{nk}.
$$

The exponential is a rotating complex number. For a fixed output index, advancing the input index rotates the multiplier by a fixed angle. Different output indices test different rotation rates. Components whose rotations align with the multiplier add coherently; others cancel over the complete record.

The output indices are periodic:

$$
X[k+N]
=
\sum_{n=0}^{N-1}x[n]W_N^{nk}e^{-j2\pi n}
=
X[k].
$$

There are therefore only $$N$$ distinct outputs.

Direct evaluation forms $$N$$ products for each of those outputs. Counting every product, including products by one, gives

$$
M_{\mathrm{direct}}(N)=N^2.
$$

Adding $$N$$ terms requires $$N-1$$ additions, so the corresponding addition count is

$$
A_{\mathrm{direct}}(N)=N(N-1).
$$

These are counts for a straightforward implementation, not lower bounds. A direct implementation can also simplify trivial multipliers. Nevertheless, its general growth remains quadratic because every output is evaluated separately.

The FFT finds structure shared across outputs. The derivation below assumes

$$
N=2^p
$$

for a nonnegative integer $$p$$. This is a requirement of this radix-2 algorithm, not a requirement of the DFT itself.

## Deriving the even and odd decomposition

Every input index belongs to exactly one of two sets:

$$
n=2r
\quad\text{or}\quad
n=2r+1,
\qquad
r=0,\ldots,N/2-1.
$$

Substitute those two possibilities into the original sum:

$$
X[k]
=
\sum_{r=0}^{N/2-1}x[2r]W_N^{2rk}
+
\sum_{r=0}^{N/2-1}x[2r+1]W_N^{(2r+1)k}.
$$

The odd exponent separates into two factors:

$$
W_N^{(2r+1)k}=W_N^{2rk}W_N^k.
$$

The factor $$W_N^k$$ does not depend on the summation index, so it can be taken outside the odd sum.

Next, reduce the exponent in the remaining factors:

$$
W_N^{2rk}
=
e^{-j2\pi(2rk)/N}
=
e^{-j2\pi rk/(N/2)}
=
W_{N/2}^{rk}.
$$

This is the decisive identity. The kernel inside each sum is exactly the kernel of a shorter DFT. Define

$$
E[k]
=
\sum_{r=0}^{N/2-1}x[2r]W_{N/2}^{rk},
$$

and

$$
O[k]
=
\sum_{r=0}^{N/2-1}x[2r+1]W_{N/2}^{rk}.
$$

Then

$$
X[k]=E[k]+W_N^kO[k].
$$

The even and odd transforms treat their samples as adjacent elements in shorter arrays. The odd samples, however, originally occupied positions displaced by one original sample. The multiplier $$W_N^k$$ accounts for that displacement. This rotating multiplier is called the **twiddle factor**.

Calling this decimation in time does not mean that half the original data are discarded. Both subsequences are retained. Consequently, this decomposition does not require the anti-aliasing filter used when physically reducing a signal's sampling rate.

At this point, there is still an apparent problem: two shorter transforms supply only half as many distinct frequency indices as the original transform. Their periodicity resolves it.

## Deriving the butterfly

Because both shorter transforms have length $$N/2$$,

$$
E[k+N/2]=E[k],
\qquad
O[k+N/2]=O[k].
$$

For example,

$$
E[k+N/2]
=
\sum_r x[2r]W_{N/2}^{rk}e^{-j2\pi r}
=
E[k].
$$

The twiddle behaves differently:

$$
W_N^{k+N/2}
=
W_N^k e^{-j\pi}
=
-W_N^k.
$$

Therefore, for each index in the first half,

$$
\begin{aligned}
X[k]&=E[k]+W_N^kO[k],\\
X[k+N/2]&=E[k]-W_N^kO[k],
\end{aligned}
\qquad
k=0,\ldots,N/2-1.
$$

One twiddle product supplies two outputs. Write the computation explicitly:

$$
t=W_N^kO[k],
$$

$$
u=E[k]+t,
\qquad
v=E[k]-t.
$$

Then store

$$
X[k]=u,
\qquad
X[k+N/2]=v.
$$

This is the **butterfly**: one multiplication and two additions, counting subtraction as an addition.

The second output is not literally free. It needs a subtraction and a write. What is reused is the product, together with the two shorter-transform outputs.

The same operation can be expressed as

$$
\begin{bmatrix}
X[k]\\
X[k+N/2]
\end{bmatrix}
=
\begin{bmatrix}
1&W_N^k\\
1&-W_N^k
\end{bmatrix}
\begin{bmatrix}
E[k]\\
O[k]
\end{bmatrix}.
$$

That matrix also shows why overwriting inputs prematurely is dangerous. Both outputs depend on the original even-transform value. An in-place implementation must preserve that value until both results have been formed.

The decomposition can now be applied to each shorter transform. It stops at a length-one transform, whose output is its input. Equivalently, the smallest nontrivial transform is

$$
[a,b]\longmapsto[a+b,a-b].
$$

No general complex multiplication is needed for this smallest case.

## A complete eight-point worked example

Take the constructed input

$$
x=[1,2,3,4,5,6,7,8].
$$

Its even and odd subsequences are

$$
x_e=[1,3,5,7],
\qquad
x_o=[2,4,6,8].
$$

First compute the even transform. Split its input again:

$$
[1,5]\longmapsto[6,-4],
$$

$$
[3,7]\longmapsto[10,-4].
$$

Since

$$
W_4^0=1,
\qquad
W_4^1=-j,
$$

the four-point butterfly gives

$$
\begin{aligned}
E[0]&=6+10=16,\\
E[2]&=6-10=-4,\\
E[1]&=-4+(-j)(-4)=-4+4j,\\
E[3]&=-4-(-j)(-4)=-4-4j.
\end{aligned}
$$

Thus

$$
E=[16,-4+4j,-4,-4-4j].
$$

For the odd transform, the two-point transforms are

$$
[2,6]\longmapsto[8,-4],
$$

$$
[4,8]\longmapsto[12,-4].
$$

Combining them gives

$$
O=[20,-4+4j,-4,-4-4j].
$$

The final stage uses these four twiddles:

$$
W_8^0=1,
\quad
W_8^1=\frac{1-j}{\sqrt2},
\quad
W_8^2=-j,
\quad
W_8^3=\frac{-1-j}{\sqrt2}.
$$

The products required by the final butterflies are

$$
\begin{aligned}
t_0&=20,\\
t_1&=\frac{1-j}{\sqrt2}(-4+4j)=4\sqrt2\,j,\\
t_2&=(-j)(-4)=4j,\\
t_3&=\frac{-1-j}{\sqrt2}(-4-4j)=4\sqrt2\,j.
\end{aligned}
$$

For the second product, the intermediate multiplication is

$$
(1-j)(-4+4j)
=
-4+4j+4j-4j^2
=
8j.
$$

That cancellation is easy to miss when carrying the complex arithmetic mentally.

Now add and subtract each product:

| $$k$$ | $$E[k]$$ | $$t_k$$ | $$X[k]$$ | $$X[k+4]$$ |
|---|---|---|---|---|
| $$0$$ | $$16$$ | $$20$$ | $$36$$ | $$-4$$ |
| $$1$$ | $$-4+4j$$ | $$4\sqrt2\,j$$ | $$-4+4(1+\sqrt2)j$$ | $$-4+4(1-\sqrt2)j$$ |
| $$2$$ | $$-4$$ | $$4j$$ | $$-4+4j$$ | $$-4-4j$$ |
| $$3$$ | $$-4-4j$$ | $$4\sqrt2\,j$$ | $$-4+4(\sqrt2-1)j$$ | $$-4-4(1+\sqrt2)j$$ |

Several checks are available without trusting an FFT library.

The zero-frequency coefficient must be the sum of the samples:

$$
X[0]=1+2+3+4+5+6+7+8=36.
$$

The halfway coefficient uses alternating signs:

$$
X[4]=1-2+3-4+5-6+7-8=-4.
$$

For real input, coefficients at opposite frequencies are conjugates. This follows directly from

$$
\begin{aligned}
X[N-k]
&=\sum_n x[n]e^{-j2\pi n(N-k)/N}\\
&=\sum_n x[n]e^{j2\pi nk/N}\\
&=X[k]^*.
\end{aligned}
$$

The table satisfies that relation. It is useful to check both the arithmetic and the placement of the outputs: correct values stored at incorrect indices still constitute an incorrect transform.

## Solving the cost recurrence

Let $$T(N)$$ denote total arithmetic work. Two half-length transforms are followed by a number of butterfly operations proportional to the original length:

$$
T(N)=2T(N/2)+cN,
$$

where $$c$$ is a constant under the chosen operation model.

Expand once:

$$
T(N)
=
2\left[2T(N/4)+cN/2\right]+cN
=
4T(N/4)+2cN.
$$

After $$r$$ expansions,

$$
T(N)=2^rT(N/2^r)+rcN.
$$

The recursion reaches length one when

$$
N/2^r=1,
\qquad
r=\log_2N.
$$

Substituting gives

$$
T(N)=NT(1)+cN\log_2N.
$$

Hence the arithmetic work is

$$
T(N)=\Theta(N\log N).
$$

The same result has a useful stage interpretation. At each level, the total length of all subproblems is still $$N$$. Each level therefore costs proportional to $$N$$, and there are logarithmically many levels.

For an explicit multiplication count, count one twiddle multiplication in every butterfly, even when its value is one:

$$
M(N)=2M(N/2)+N/2,
\qquad
M(1)=0.
$$

Every level contains $$N/2$$ butterflies, so

$$
M(N)=\frac{N}{2}\log_2N.
$$

Each butterfly also performs two additions:

$$
A(N)=2A(N/2)+N,
\qquad
A(1)=0,
$$

which gives

$$
A(N)=N\log_2N.
$$

Under this deliberately simple multiplication convention:

| Length | Direct products | FFT twiddle products | Ratio of counts |
|---|---|---|---|
| $$8$$ | $$64$$ | $$12$$ | $$16/3\approx5.33$$ |
| $$64$$ | $$4096$$ | $$192$$ | $$64/3\approx21.33$$ |
| $$1024$$ | $$1{,}048{,}576$$ | $$5120$$ | $$204.8$$ |

An optimized implementation skips multiplication by one and handles factors such as $$-j$$ through sign changes and component exchanges. Its count of general complex multiplications is smaller. The table is therefore meaningful only together with its counting convention.

Nor does the table predict elapsed time. It leaves out data movement, allocation, instruction scheduling, and computation or loading of twiddles. The derivation establishes the growth rate and a transparent arithmetic comparison.

## Why bit reversal appears

For an eight-point input, recursively visiting the even branch before the odd branch reaches the original sample indices in this order:

$$
0,4,2,6,1,5,3,7.
$$

Write each original index using three binary digits. The first split reads the least significant bit: zero means even, one means odd. The next split reads the next bit, and the final split reads the most significant bit.

The recursion therefore encounters the digits in the reverse of their usual order:

$$
001\longrightarrow100,
\qquad
011\longrightarrow110.
$$

These correspond to

$$
1\longrightarrow4,
\qquad
3\longrightarrow6.
$$

A common iterative implementation first places inputs in this bit-reversed order. It then computes adjacent two-point transforms, combines those into four-point transforms, and continues until it reaches the full length.

Bit reversal is a consequence of this particular traversal and storage arrangement. It is not an additional mathematical operation required by every FFT algorithm. A recursive implementation can hide the permutation in its indexing, and other FFT arrangements distribute the ordering work differently.

This distinction matters when debugging: bit-reversed output can look numerically plausible while assigning every coefficient to the wrong frequency.

## The inverse transform and checks that expose mistakes

The inverse DFT uses the opposite exponential sign and a normalizing factor:

$$
x[n]
=
\frac1N\sum_{k=0}^{N-1}X[k]e^{j2\pi nk/N}.
$$

To see why, substitute the forward transform:

$$
\frac1N
\sum_{m=0}^{N-1}x[m]
\sum_{k=0}^{N-1}e^{j2\pi(n-m)k/N}.
$$

If the two sample indices agree, every term in the inner sum is one, giving $$N$$. Otherwise, the inner sum is a geometric series with ratio

$$
q=e^{j2\pi(n-m)/N},
$$

where

$$
q^N=1,
\qquad q\ne1.
$$

Its sum is

$$
\frac{1-q^N}{1-q}=0.
$$

Only the desired sample survives. This also explains why forgetting the inverse normalization multiplies the recovered signal by the transform length.

The same orthogonality gives the energy identity

$$
\sum_{n=0}^{N-1}|x[n]|^2
=
\frac1N\sum_{k=0}^{N-1}|X[k]|^2.
$$

Indeed, expanding the squared magnitude of the inverse transform produces cross terms whose inner exponential sums vanish unless their frequency indices agree.

For the worked example,

$$
\sum_{n=0}^{7}|x[n]|^2=204,
$$

so the output must satisfy

$$
\sum_{k=0}^{7}|X[k]|^2=8\cdot204=1632.
$$

Useful checks therefore include the sample sum, the alternating sum, conjugate symmetry, reconstruction, and energy. They test different failure modes.

The FFT and direct DFT agree in exact arithmetic. Floating-point implementations need not agree bit for bit because they add and multiply in different orders. “Same transform” is a mathematical statement; bitwise equality is a separate implementation property.

## Padding, convolution, and choosing the actual problem

Appending zeros changes the transform length and the frequency grid. It does not leave the original DFT unchanged.

For a finite record, the DFT evaluates its discrete-time Fourier transform at equally spaced frequencies. Padding supplies more evaluation points on that same finite-record spectrum. It does not supply additional observed samples or undo the consequences of a short observation interval.

Padding has a different, essential role in FFT convolution. A length-$$P$$ inverse DFT of a product computes circular convolution:

$$
y_P[n]
=
\sum_{k=0}^{P-1}
x[k]h[(n-k)\bmod P].
$$

The modulo appears because the DFT represents periodic sequences. Contributions beyond the last index wrap to the beginning.

For input and filter lengths $$B$$ and $$K$$, the final possible index in linear convolution is

$$
(B-1)+(K-1)=B+K-2.
$$

There are therefore

$$
B+K-1
$$

output samples. Choosing

$$
P\ge B+K-1
$$

and padding both inputs prevents nonzero output samples from wrapping.

For a concrete overlap-add example, take

$$
x=[1,2,3,4],
\qquad
h=[1,1,1].
$$

Split the input into two blocks:

$$
[1,2],
\qquad
[3,4].
$$

Each block can use a four-point transform because

$$
2+3-1=4.
$$

Their linear convolutions are

$$
[1,2]*[1,1,1]=[1,3,3,2],
$$

and

$$
[3,4]*[1,1,1]=[3,7,7,4].
$$

The second block starts two samples later. Align and add:

$$
[1,3,3,2,0,0]
+
[0,0,3,7,7,4]
=
[1,3,6,9,7,4].
$$

The overlap contains contributions from both input blocks; discarding one tail would change the filter.

For a long signal, the filter transform can be reused across blocks. With fixed filter and block sizes, the work then grows linearly with the total number of input samples. The block size still controls a tradeoff between transform efficiency, useful output per block, working memory, and latency.

A single very large transform is not inherently invalid. Block processing is useful because its resource and latency requirements can be controlled. The appropriate choice depends on the actual filtering task.

## Revision checklist

| Question | What I should be able to reproduce |
|---|---|
| Why are the two subproblems DFTs? | Reduce the doubled exponent to a length-half kernel. |
| Where does the twiddle come from? | Factor the extra one-sample displacement of the odd indices. |
| Why does one product yield two outputs? | Combine half-length periodicity with the twiddle sign change. |
| What does a butterfly compute? | One shared product, followed by a sum and a difference. |
| Why is the cost logarithmic in stages? | Expand the recurrence until the subproblem length reaches one. |
| What does the advertised ratio count? | Twiddle multiplications under an explicit convention, not runtime. |
| Why does bit reversal occur? | Repeated parity splits read index bits from least to most significant. |
| How can I check a result? | Check sums, conjugate symmetry, inverse reconstruction, and energy. |
| Why pad for convolution? | Prevent the linear-convolution tail from wrapping around. |

## Why it matters for my work

FFT-based filtering and spectral features are only as reliable as their indexing, normalization, and boundary assumptions. I want to be able to reconstruct the butterfly and explain the padding rule before treating a library call as an understood operation.

## What I have not resolved

Benchmark the transform and block lengths used in my own preprocessing pipeline, including allocation and data movement, before attaching a runtime speedup to the arithmetic comparison.
