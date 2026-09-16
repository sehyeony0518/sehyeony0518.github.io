---
layout: study_note
title: "Convolution via the DFT: Circular, Linear, and the Padding You Forgot Was a Choice"
description: "Why multiplying two DFTs gives the wrong answer, the length condition that fixes it, and why full/same/valid is the same decision a CNN makes at every layer."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
order: 3
source: "Independent study"
written: true
updated: "2026-09-15"
---

Convolving a signal with a filter directly is perfectly correct, and for short filters it is what you should do. The reason to learn a more roundabout route is economy: the same answer, far cheaper, which in practice means a better filter on the same hardware, or the same filter on cheaper hardware, or more throughput on what you already own.

The roundabout route has a trap in it, and the trap is more interesting than the speedup.

## Core question and definition

The convolution theorem says filtering is multiplication in the frequency domain, so the obvious plan is: transform $$x$$, transform $$h$$, multiply, transform back.

With the **discrete-time** Fourier transform this is a non-starter. $$X(e^{j\omega})$$ is a function of a continuous $$\omega$$, and inverting it means evaluating an integral. Nothing about that is computable on a machine that stores finitely many numbers; it is a correct statement about mathematics and a useless instruction for a computer.

The **DFT** is the computable version, and the relationship between the two is exactly what you would hope: the DFT is the DTFT **sampled** at $$L$$ equally spaced frequencies,

$$
X[k] = X(e^{j\omega})\Big|_{\omega = 2\pi k/L}.
$$

So multiply two DFTs, invert, and you get… not the convolution you wanted.

## Key concepts

### Multiplying DFTs gives circular convolution

Sampling in frequency is periodisation in time. Taking the DFT implicitly treats your finite signal as one period of something that repeats forever, so what the product of two DFTs computes is **circular** convolution: the filter that runs off the end of the buffer wraps around and re-enters at the beginning, corrupting the first few outputs with data from the last few.

The fix is a length condition. If $$x$$ has $$M$$ non-zero samples and $$h$$ has $$K$$, their linear convolution has $$M+K-1$$, so choosing

$$
L \ \ge\ M + K - 1
$$

and zero-padding both to length $$L$$ leaves room for the tail and nothing wraps. Circular convolution then equals linear convolution exactly.

This is worth confirming rather than believing. With $$M = 9$$ and $$K = 5$$, the requirement is $$L \ge 13$$; sweeping $$L$$ and comparing against `np.convolve` gives disagreement at $$L = 9, 11, 12$$ and exact agreement at $$L = 13$$. The boundary is sharp, and there is no gradual degradation to warn you: $$L = 12$$ is simply wrong, by an amount concentrated entirely in the first few samples.

Combined with the FFT, which computes a length-$$L$$ DFT in $$O(L\log L)$$ rather than $$O(L^2)$$,[^ct] this beats direct convolution comfortably for any filter that is not very short. Whether a filter *is* short is the only question worth asking before choosing.

### Non-causal filters wrap to the far end

A filter with taps at negative indices, a centred smoothing kernel, say, has no natural home in a buffer indexed from zero. Under the periodic interpretation the answer is forced: the negative-index taps belong at the **end** of the array, because index $$-1$$ and index $$L-1$$ are the same place. The output comes back with the same convention, and the piece that belongs before time zero must be read off the end and moved back.

This is the sort of thing that produces a result which is right in the middle and mangled at both edges, which is exactly the failure that survives a casual look at a plot.

### full, same, and valid are three answers to one question

Direct convolution asks the same question in plainer clothes. `np.convolve` offers three modes, and with $$M=9$$, $$K=5$$ they return lengths 13, 9, and 5:

- **full** ($$M+K-1$$) keeps every output the filter produces, including those where it hangs off the edge with only partial overlap.
- **same** ($$M$$) keeps the middle, so output length matches input length.
- **valid** ($$M-K+1$$) keeps only outputs where the filter sat entirely inside real data.

These are not conveniences. They are three different claims about what exists outside the signal: *full* and *same* assert that it is zero, and *valid* declines to assert anything and shrinks instead.

## Why it matters for my work

Every convolutional layer makes this choice, and `padding='same'` is the near-universal default because nobody wants feature maps shrinking. What gets padded in is zeros, and that is a claim: **the world outside this image is zero.**

It is false for a medical image, and worse, it is *informative*. Zero padding makes the border of a feature map systematically different from its interior, and that difference is a signal. A network can read absolute spatial position out of it, this is demonstrated, not speculated, which quietly breaks the translation invariance convolution is assumed to provide.[^kayhan][^islam] It also creates a border region where the effective receptive field is degraded, producing blind spots along the edges.[^pad]

The consequence for auditing is specific. If lesion position correlates with anything in a dataset, and it often does, because acquisition protocols centre the anatomy of interest, then a network can learn to use position, and the padding it was given is part of how it gets there. That is a [shortcut](/study/shortcut-learning-in-medical-imaging/) whose origin is a default argument rather than anything in the data, and no attribution map over image content will point at it, because the culprit is not in the image.

The $$L = 12$$ versus $$L = 13$$ result is the general lesson in miniature. A pipeline can be off by one in a boundary condition and produce output that is correct almost everywhere, wrong at the edges, and entirely plausible on inspection. Boundary handling is where signal processing keeps its silent errors, and the only reliable defence is the one used above: compute the same quantity two ways and compare.

---

[^ct]: Cooley, J. W., & Tukey, J. W. (1965). An algorithm for the machine calculation of complex Fourier series. *Mathematics of Computation*, 19(90), 297–301. [10.1090/S0025-5718-1965-0178586-1](https://doi.org/10.1090/S0025-5718-1965-0178586-1)

[^kayhan]: Kayhan, O. S., & van Gemert, J. C. (2020). On translation invariance in CNNs: convolutional layers can exploit absolute spatial location. *CVPR 2020*, 14262–14273. [10.1109/CVPR42600.2020.01428](https://doi.org/10.1109/CVPR42600.2020.01428)

[^islam]: Islam, M. A., Jia, S., & Bruce, N. D. B. (2020). How much position information do convolutional neural networks encode? *ICLR 2020*. [arXiv:2001.08248](https://arxiv.org/abs/2001.08248)

[^pad]: Alsallakh, B., Kokhlikyan, N., Miglani, V., Yuan, J., & Reblitz-Richardson, O. (2021). Mind the Pad: CNNs can develop blind spots. *ICLR 2021*. [arXiv:2010.02178](https://arxiv.org/abs/2010.02178)
