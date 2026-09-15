---
layout: study_note
title: "The FFT: Where a 200× Speedup Comes From"
description: "Splitting a transform into its even and odd samples, the recursion that turns N² into N log N, and why an algorithm can matter more than the hardware."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
order: 11
source: "Independent study"
written: true
updated: "2026-09-15"
---

Every use of the DFT so far — [filtering by multiplication](/study/convolution-via-the-dft/), spectral analysis, [resampling](/study/resampling-and-anti-aliasing/) — has assumed it is affordable. Computed directly it is not, and the algorithm that makes it affordable is worth seeing derived, because the trick is simple and the payoff is enormous.

## Core question and definition

$$
X[k] = \sum_{n=0}^{N-1} x[n]\,W_N^{nk}, \qquad W_N = e^{-2\pi j/N}.
$$

Each output needs $$N$$ complex multiplications and there are $$N$$ outputs, so the direct cost is $$N^2$$. Since a complex multiplication is four real multiplications and two real additions, $$N = 1024$$ means over a million complex multiplies — more than four million real ones — for a single transform. That is the wall.

## Key concepts

### Split the samples by parity

Separate the sum into even- and odd-indexed samples:

$$
X[k] = \underbrace{\sum_{r} x[2r]\,W_{N/2}^{rk}}_{E[k]} \;+\; W_N^{k}\underbrace{\sum_{r} x[2r+1]\,W_{N/2}^{rk}}_{O[k]}.
$$

The $$W_N^{2rk} = W_{N/2}^{rk}$$ collapse is the whole trick: **each half is itself a DFT of length $$N/2$$.**

Better still, $$E$$ and $$O$$ are periodic with period $$N/2$$ while $$W_N^{k+N/2} = -W_N^{k}$$, so the second half of the output is free:

$$
X[k] = E[k] + W_N^k O[k], \qquad X[k+N/2] = E[k] - W_N^k O[k].
$$

One multiplication, two outputs. That pairing is the butterfly, and it is where the factor of two per stage comes from.

### The recursion, and what it costs

Two half-length transforms plus $$N/2$$ twiddle multiplications:

$$
T(N) = 2\,T(N/2) + N/2 \quad\Longrightarrow\quad T(N) = \tfrac{N}{2}\log_2 N .
$$

Implementing it and counting confirms it exactly — 12 multiplications at $$N=8$$, 192 at $$N=64$$, 5120 at $$N=1024$$, matching $$(N/2)\log_2 N$$ in every case, with outputs agreeing with a library FFT to floating-point precision.

Set that against the direct cost:

| $$N$$ | direct $$N^2$$ | FFT $$(N/2)\log_2 N$$ | speedup |
|---|---|---|---|
| 8 | 64 | 12 | 5× |
| 64 | 4,096 | 192 | 21× |
| 1024 | 1,048,576 | 5,120 | **205×** |

And the gap widens without limit. Nothing was approximated — the output is *identical*, bit for bit up to rounding. This is the same arithmetic, reorganised.

### Bit reversal is the recursion's fingerprint

Splitting by parity repeatedly permutes the input, and the permutation has a clean description. For $$N=8$$ the order is

$$
0,\ 4,\ 2,\ 6,\ 1,\ 5,\ 3,\ 7,
$$

which is $$0..7$$ with each index's **binary digits reversed** — $$1 = 001 \to 100 = 4$$, $$3 = 011 \to 110 = 6$$. Repeatedly asking "even or odd" is repeatedly reading the low bit, so the recursion sorts by bits from the bottom up, and the reversal falls out. In-place implementations do this permutation first and then work forwards with no extra memory.

### Blocks, not zero padding

One practical consequence. To filter a long signal with a short filter, the [length condition](/study/convolution-via-the-dft/) says to pad to $$M+K-1$$ — but if $$M$$ is a million samples and $$K$$ is 512, padding the filter to a million and transforming both is absurd.

Instead, chop the signal into blocks sized to the filter, transform each, and reassemble. **Overlap-save** takes overlapping input blocks and discards the wrapped-around samples from each output; **overlap-add** uses non-overlapping blocks and sums the tails. Either way the cost becomes linear in signal length, and long-signal filtering becomes routine.

## Why it matters for my work

The headline result is that **an algorithmic change bought 200×, and it will buy 20,000× on a large enough input, with no hardware involved and no accuracy given up.** That is a different category of improvement from anything a faster machine provides, and it compounds with faster machines rather than competing with them.

That framing is worth keeping when reading claims about computational cost in machine learning. A great deal of effort goes into hardware and low-precision arithmetic — which trade accuracy for speed — and rather less into asking whether the computation is structured well. The FFT gives up nothing. Whenever a quantity is being recomputed in a loop with structure nobody exploited, there may be an exact reorganisation available, and it is worth a look before accepting an approximation.

The honest limit is the one the derivation makes obvious: the saving came from a **specific algebraic symmetry**, $$W_N^{2rk} = W_{N/2}^{rk}$$ plus the sign flip at the half period. It is not a general principle that clever restructuring always wins. Most computations have no such structure, and the reason this one does is that the DFT's kernel is an exponential on a group — which is also why the same decomposition generalises to other transforms with the same structure and stops at the boundary of that structure.

There is a small methodological point too, and it is the one I actually acted on here. The recursion above is three lines of algebra and easy to get subtly wrong; implementing it and checking against a library — exact match on the output, exact match on the operation count — took a few minutes and turned an argument I believed into one I had checked. That distinction is the thing these notes exist to maintain.

---

Sources: the radix-2 decimation-in-time decomposition is Cooley and Tukey's, published as J. W. Cooley & J. W. Tukey (1965), *An algorithm for the machine calculation of complex Fourier series*, **Mathematics of Computation** 19(90), 297–301, [10.1090/S0025-5718-1965-0178586-1](https://doi.org/10.1090/S0025-5718-1965-0178586-1). The operation counts, the bit-reversed ordering, and the agreement with a reference implementation reported here were computed directly.
