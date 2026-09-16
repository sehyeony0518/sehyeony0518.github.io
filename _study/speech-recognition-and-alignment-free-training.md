---
layout: study_note
title: "Speech Recognition: Learning Without Knowing Where Anything Starts"
description: "MFCC features, CTC alignment marginalisation and forward–backward gradients, with exact frame-to-label path counts, repeated-label constraints and worked decoding examples."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Learning Models & Representation"
subgroup: "Sequence Models & Attention"
order: 10
source: "Independent study"
written: true
updated: "2026-09-15"
---

Speech recognition maps a sampled waveform to a shorter symbol sequence. The transcript supplies symbol order, but usually does not supply the time interval associated with each symbol.

Connectionist temporal classification, abbreviated CTC, defines a probability for the transcript by summing over compatible frame-level paths. “Alignment-free training” means that an alignment need not be provided as supervision. The model still contains a specific alignment structure: it is monotone, permits blanks, and imposes special rules for repeated labels.

## What is missing from the supervision

Let the acoustic input or encoded frame sequence be

$$
x=(x_1,\ldots,x_T),
$$

and the target token sequence be

$$
y=(y_1,\ldots,y_U).
$$

Tokens might be characters, phonemes, or subword units. Their definition is part of the system.

The missing variable is the alignment between these two sequences. We know the output order but not the frame at which each output should appear or how long it should persist.

The lengths are not unrelated. Speech duration affects the number of frames, and a particular alignment model constrains how many tokens can be represented. CTC, for example, requires enough encoder time steps to place every token and any mandatory separators.

Frame-level annotations can exist, and alignments can be estimated. CTC's benefit is that transcript training does not require them. It replaces a supplied alignment with a latent variable to be marginalized.

An acoustic model also need not use a separate language model. Context can be represented inside an encoder or decoder, and an external language model is an additional modeling choice. Ambiguous acoustics motivate linguistic context, but they do not force one particular factorization.

## From samples to frames: count the windows explicitly

Suppose a constructed recording contains

$$
N=16000
$$

samples at sampling frequency

$$
f_s=16000\ \text{samples/second}.
$$

Choose a frame length and hop of

$$
W=400,
\qquad
H=160.
$$

Their durations are

$$
\frac{W}{f_s}=0.025\ \text{seconds},
\qquad
\frac{H}{f_s}=0.010\ \text{seconds}.
$$

With no boundary padding and only complete frames, the number of frames is

$$
T_{\mathrm{frames}}
=
1+\left\lfloor\frac{N-W}{H}\right\rfloor
=
1+\left\lfloor97.5\right\rfloor
=
98.
$$

It is not automatically one hundred merely because the hop corresponds to one hundred positions per second. Frame length and boundary handling affect the exact count.

An encoder with temporal subsampling can reduce the number further. CTC feasibility must be checked against the encoder's output length, not the number of waveform samples or the number of pre-encoder feature frames.

For frame index $$t$$, a windowed frame is

$$
s_t[n]=w[n]x[tH+n],
\qquad
0\le n<W.
$$

Its DFT samples are

$$
X_t[k]
=
\sum_{n=0}^{W-1}
s_t[n]e^{-j2\pi kn/W}.
$$

Windowing localizes analysis in time but also changes the spectrum. The feature sequence is already the result of several choices before any neural network sees it.

## The actual MFCC pipeline

Mel-frequency cepstral coefficients are usually formed through the following operations:

1. Window the waveform and compute a short-time Fourier transform.
2. Form a power spectrum.
3. Sum spectral power through a mel-spaced filterbank.
4. Take logarithms of the filterbank energies.
5. Apply a discrete cosine transform, commonly DCT-II.
6. Optionally retain only a subset of coefficients.

The second transform is therefore not generally another Fourier transform of the raw log-magnitude spectrum. Implementations also differ in log scaling, normalization, and the number of retained coefficients. [Torchaudio MFCC definition and conventions](https://docs.pytorch.org/audio/main/generated/torchaudio.transforms.MFCC.html)

Define the power spectrum by

$$
P_t[k]=\lvert X_t[k]\rvert^2.
$$

With nonnegative filterbank weights,

$$
E_t[m]=\sum_k W_m[k]P_t[k].
$$

The weights pool nearby frequency bins. They operate before the logarithm, so

$$
\log\left(\sum_kW_m[k]P_t[k]\right)
$$

is generally different from averaging the individual log powers.

A mel convention supplies a nonlinear frequency coordinate. A logarithmic form can be written as

$$
m(f)=C\log\left(1+\frac{f}{f_{\mathrm{ref}}}\right),
$$

with constants fixed by the chosen convention. Its inverse is

$$
f=f_{\mathrm{ref}}\left(e^{m/C}-1\right).
$$

Equally spaced coordinates on this scale correspond to increasingly wide frequency intervals as physical frequency rises. This derives what the warping does; its perceptual calibration is an empirical modeling choice, not a theorem that an ear computes these exact features.

To avoid the logarithm of zero, a numerical implementation can use

$$
\ell_t[m]=\log\bigl(\max(E_t[m],\varepsilon)\bigr),
$$

for a chosen positive floor.

## Why logarithms and a cosine transform help

A simplified source–filter model writes speech as convolution:

$$
s[n]=(e*v)[n],
$$

where the excitation and filter represent different parts of signal production.

The convolution theorem gives

$$
S(e^{j\omega})=E(e^{j\omega})V(e^{j\omega}).
$$

Where the magnitudes are nonzero,

$$
\log\lvert S(e^{j\omega})\rvert
=
\log\lvert E(e^{j\omega})\rvert
+
\log\lvert V(e^{j\omega})\rvert.
$$

The logarithm turns multiplication into addition. Applying a linear transform afterward preserves this additive decomposition.

This identity is exact for the stated convolution model. Treating it as exact within every finite speech frame requires additional approximations because the vocal tract can change over time and windowing modifies the spectrum.

For $$B$$ log filterbank energies, an orthonormal DCT-II is

$$
c_t[q]
=
a_q
\sum_{m=0}^{B-1}
\ell_t[m]
\cos\left(
\frac{\pi q(m+\frac12)}{B}
\right),
$$

where

$$
a_0=\frac1{\sqrt B},
\qquad
a_q=\sqrt{\frac2B}\quad(q>0).
$$

The lowest coefficient measures the average log energy under this normalization. Higher coefficients represent increasingly rapid variation across filterbank index. Keeping only the first coefficients smooths that log-energy pattern.

A conventional real cepstrum instead inverse-transforms a log-magnitude spectrum. Its index can be interpreted as a time lag, called quefrency. For a constructed periodicity of eight milliseconds, the reciprocal frequency is

$$
\frac1{0.008}=125\ \text{Hz}.
$$

That arithmetic does not imply every cepstral peak is a clean pitch estimate. Nor do ordinary MFCC coefficient indices directly have units of milliseconds.

## A two-channel MFCC calculation

Construct two positive filterbank energies:

$$
E=[4,2].
$$

Their natural logarithms are

$$
\ell=[2\log2,\log2].
$$

For a two-channel orthonormal DCT,

$$
c_0=\frac{\ell_0+\ell_1}{\sqrt2}
=
\frac{3\log2}{\sqrt2},
$$

$$
c_1=\frac{\ell_0-\ell_1}{\sqrt2}
=
\frac{\log2}{\sqrt2}.
$$

The inverse is

$$
\ell_0=\frac{c_0+c_1}{\sqrt2},
\qquad
\ell_1=\frac{c_0-c_1}{\sqrt2},
$$

which exactly recovers the original two values.

If the second coefficient is discarded, both reconstructed log energies become

$$
\widetilde\ell_0=\widetilde\ell_1=\frac32\log2.
$$

Exponentiating gives

$$
\widetilde E_0=\widetilde E_1=2^{3/2}=\sqrt8.
$$

The reconstruction equalizes the channels at their geometric mean, not their arithmetic mean. This small example shows what compression in a log-spectrum basis actually removes: contrast across frequency channels.

## CTC defines a many-to-one map from paths to transcripts

Let the token alphabet be $$\mathcal A$$ and introduce a blank symbol $$\varnothing$$. At every encoder time step, the network outputs a distribution

$$
p_t(k\mid x),
\qquad
k\in\mathcal A\cup\{\varnothing\}.
$$

A path is a length-$$T$$ sequence

$$
\pi=(\pi_1,\ldots,\pi_T).
$$

CTC assigns it probability

$$
P(\pi\mid x)=\prod_{t=1}^{T}p_t(\pi_t\mid x).
$$

The collapse map first merges consecutive repeats of the same symbol, then removes blanks. For example,

$$
\mathcal B(a,a,b,\varnothing)=ab,
$$

but

$$
\mathcal B(a,\varnothing,a)=aa.
$$

The order matters. Removing blanks first would incorrectly merge the two tokens in the second example.

A run such as `hheelllloo` collapses to `helo`, not `hello`. To represent the doubled letter in `hello`, separate the two intended `l` tokens by at least one blank.

The transcript probability is the sum over all compatible paths:

$$
P(y\mid x)
=
\sum_{\pi:\mathcal B(\pi)=y}
\prod_{t=1}^{T}p_t(\pi_t\mid x).
$$

The training loss is

$$
\mathcal L_{\mathrm{CTC}}=-\log P(y\mid x).
$$

This is the latent-alignment likelihood underlying CTC. [Original CTC formulation](https://www.cs.toronto.edu/~graves/icml_2006.pdf)

The blank means “emit no token at this frame.” It is not a word-space token and need not correspond to physical silence.

## Exact path enumeration for a small target

Use three frames and the target `ab`. Construct these probabilities:

| Frame | $$a$$ | $$b$$ | Blank |
|---|---|---|---|
| $$1$$ | $$0.6$$ | $$0.1$$ | $$0.3$$ |
| $$2$$ | $$0.2$$ | $$0.5$$ | $$0.3$$ |
| $$3$$ | $$0.1$$ | $$0.6$$ | $$0.3$$ |

Every row sums to one.

Exactly five paths collapse to `ab`:

| Path | Probability |
|---|---|
| `aab` | $$0.6\cdot0.2\cdot0.6=0.072$$ |
| `abb` | $$0.6\cdot0.5\cdot0.6=0.180$$ |
| `a-b` | $$0.6\cdot0.3\cdot0.6=0.108$$ |
| `-ab` | $$0.3\cdot0.2\cdot0.6=0.036$$ |
| `ab-` | $$0.6\cdot0.5\cdot0.3=0.090$$ |

Here the hyphen denotes the blank.

Their sum is

$$
P(ab\mid x)
=
0.072+0.180+0.108+0.036+0.090
=
0.486
=
\frac{243}{500}.
$$

Therefore,

$$
\mathcal L_{\mathrm{CTC}}
=
-\log\left(\frac{243}{500}\right).
$$

Training against only the most likely path would use a probability of $$0.180$$ instead. CTC credits all compatible alignments, including those that place a token at different frames.

## Deriving the forward dynamic program

Insert blanks before, between, and after target tokens. For `ab`, the expanded state sequence is

$$
z=(\varnothing,a,\varnothing,b,\varnothing).
$$

For a target of length $$U$$, there are

$$
S=2U+1
$$

states.

Let

$$
\alpha_t(s)
$$

be the total probability of paths that have consumed the first $$t$$ frames and end at expanded state $$s$$, including the emission at that frame.

A path can reach a state by:

- staying at the same state;
- advancing one state;
- advancing two states when the destination is a nonblank token different from the token two states earlier.

The two-state transition skips an optional blank. It must be forbidden between identical target tokens, or they would merge during collapse.

With out-of-range terms defined as zero,

$$
\alpha_t(s)
=
p_t(z_s)
\left[
\alpha_{t-1}(s)
+
\alpha_{t-1}(s-1)
+
\chi_s\alpha_{t-1}(s-2)
\right],
$$

where

$$
\chi_s=
\begin{cases}
1,&s>2,\ z_s\ne\varnothing,\ z_s\ne z_{s-2},\\
0,&\text{otherwise}.
\end{cases}
$$

For a nonempty target, initialization is

$$
\alpha_1(1)=p_1(\varnothing),
\qquad
\alpha_1(2)=p_1(y_1),
$$

with all other states zero.

A completed path can end at the final token or trailing blank:

$$
P(y\mid x)=\alpha_T(S-1)+\alpha_T(S).
$$

There are a constant number of incoming transitions per state, so the calculation uses

$$
O(TU)
$$

arithmetic operations. Computing only the likelihood can use two state rows, requiring

$$
O(U)
$$

working memory.

For an empty target, the only compatible path is all blanks, with probability equal to the product of blank probabilities.

## Checking the dynamic program against enumeration

For the probability table above, the forward values are:

| Frame | Leading blank | First token $$a$$ | Middle blank | Second token $$b$$ | Trailing blank |
|---|---|---|---|---|---|
| $$1$$ | $$0.300$$ | $$0.600$$ | $$0$$ | $$0$$ | $$0$$ |
| $$2$$ | $$0.090$$ | $$0.180$$ | $$0.180$$ | $$0.300$$ | $$0$$ |
| $$3$$ | $$0.027$$ | $$0.027$$ | $$0.108$$ | $$0.396$$ | $$0.090$$ |

For example, the probability at the second token on the final frame is

$$
\alpha_3(4)
=
0.6(0.300+0.180+0.180)
=
0.396.
$$

The three terms correspond to staying at `b`, arriving from the middle blank, or skipping directly from `a`.

The final probability is

$$
0.396+0.090=0.486,
$$

matching the sum of all five enumerated paths.

This agreement is more informative than reporting that a library returned a plausible loss. The enumeration and recurrence expose the exact events being counted.

## Counting paths, including repeated labels

Let

$$
R=\sum_{u=2}^{U}\mathbf1[y_u=y_{u-1}]
$$

count adjacent repeated-token pairs.

Every target token requires a nonempty run of its symbol. There are $$U$$ such runs. There are also $$U+1$$ blank gaps: before the first run, after the last, and between consecutive runs.

Each repeated-token boundary requires at least one blank. Therefore the minimum path length is

$$
T_{\min}=U+R.
$$

Subtract one frame from every token run and one from each mandatory blank gap. The remaining

$$
T-U-R
$$

frames can be distributed among

$$
2U+1
$$

nonnegative run-extension and blank-gap variables.

The number of nonnegative integer assignments summing to $$q$$ across $$v$$ variables is

$$
\binom{q+v-1}{v-1}.
$$

One way to derive this is to arrange $$q$$ identical items and insert $$v-1$$ separators; choosing separator positions determines the allocation.

Thus, for a nonempty target,

$$
N_{\mathrm{paths}}
=
\binom{T+U-R}{2U},
\qquad T\ge U+R.
$$

Below the minimum length, the count is zero.

Examples:

| Frames | Target length | Adjacent repeats | Compatible paths |
|---|---|---|---|
| $$3$$ | $$2$$ | $$0$$ | $$\binom54=5$$ |
| $$3$$ | $$2$$ | $$1$$ | $$\binom44=1$$ |
| $$5$$ | $$2$$ | $$0$$ | $$\binom74=35$$ |
| $$5$$ | $$2$$ | $$1$$ | $$\binom64=15$$ |
| $$10$$ | $$3$$ | $$0$$ | $$\binom{13}{6}=1716$$ |
| $$100$$ | $$5$$ | $$0$$ | $$\binom{105}{10}=28{,}848{,}458{,}598{,}960$$ |

For `hello`, there is one adjacent repeat. Its corresponding count at one hundred frames is instead

$$
\binom{104}{10}=26{,}100{,}986{,}351{,}440.
$$

The large count is valid only after the target length and repeat structure are specified.

## Backward probabilities and the gradient

Define

$$
\beta_t(s)
$$

as the probability of completing the target after frame $$t$$, starting from state $$s$$, excluding the emission already counted at frame $$t$$.

At the final frame, set the final token and trailing blank states to one and all others to zero. The backward recurrence sums over valid outgoing transitions:

$$
\beta_t(s)
=
\sum_{r:\,s\to r}
p_{t+1}(z_r)\beta_{t+1}(r).
$$

The posterior probability of occupying expanded state $$s$$ at time $$t$$ is

$$
q_t(s)
=
\frac{\alpha_t(s)\beta_t(s)}{P(y\mid x)}.
$$

Aggregate states emitting the same symbol:

$$
\gamma_t(k)
=
\sum_{s:z_s=k}q_t(s).
$$

This is a soft alignment target inferred from the transcript and current network outputs.

To derive the gradient, differentiate the path sum. Every path containing symbol $$k$$ at frame $$t$$ contributes its probability divided by the corresponding frame probability. Therefore,

$$
\frac{\partial\log P(y\mid x)}
{\partial\log p_t(k)}
=
\gamma_t(k).
$$

Let the frame probabilities come from logits:

$$
p_t(k)=\frac{e^{a_t(k)}}{\sum_r e^{a_t(r)}}.
$$

Since

$$
\frac{\partial\log p_t(r)}{\partial a_t(k)}
=
\mathbf1[r=k]-p_t(k),
$$

and the posterior symbol probabilities sum to one,

$$
\frac{\partial\mathcal L_{\mathrm{CTC}}}{\partial a_t(k)}
=
p_t(k)-\gamma_t(k).
$$

The gradient resembles cross-entropy with a soft target, but the target is obtained by summing over compatible alignments rather than supplied frame annotations.

## A numerical posterior and gradient

Return to the five paths for `ab`. At the second frame:

- Paths emitting `a` have total probability $$0.072+0.036=0.108$$.
- Paths emitting `b` have total probability $$0.180+0.090=0.270$$.
- The path emitting blank has probability $$0.108$$.

Divide by the transcript probability:

$$
\gamma_2(a)=\frac{0.108}{0.486}=\frac29,
$$

$$
\gamma_2(b)=\frac{0.270}{0.486}=\frac59,
$$

$$
\gamma_2(\varnothing)=\frac29.
$$

The frame's original prediction was

$$
p_2=\left(\frac15,\frac12,\frac3{10}\right).
$$

Hence the logit gradient is

$$
p_2-\gamma_2
=
\left(
-\frac1{45},
-\frac1{18},
\frac7{90}
\right).
$$

Its entries sum to zero, as a softmax-logit gradient should.

The transcript encourages more probability on both tokens and less on blank at this frame. It does not force one hard alignment. That is the operational meaning of marginalization during learning.

## Numerical stability and impossible targets

Path probabilities multiply many values below one and can underflow. The forward recursion is therefore commonly evaluated in log space.

For numbers $$a_1,\ldots,a_m$$,

$$
\log\sum_i e^{a_i}
=
a_{\max}
+
\log\sum_i e^{a_i-a_{\max}},
$$

where

$$
a_{\max}=\max_i a_i.
$$

Subtracting the maximum leaves all exponential arguments nonpositive while preserving the exact mathematical value.

Unreachable states have log probability negative infinity. An impossible target has total probability zero and therefore infinite negative log-likelihood.

A basic feasibility check is

$$
T\ge U+R.
$$

This must use each example's true encoder length, excluding padded frames. Silently treating batch padding as real acoustic time changes the set of available alignments.

## Why greedy decoding can miss the most probable transcript

Greedy decoding selects the most probable symbol at each frame, then collapses the resulting path. Because path probabilities factorize, this finds a maximum-probability path.

It need not find a maximum-probability transcript, since many paths can share one transcript.

Construct two frames with

$$
p_t(\varnothing)=0.6,
\qquad
p_t(a)=0.4
$$

at both frames.

Greedy decoding selects two blanks. The empty transcript has probability

$$
0.6^2=0.36.
$$

The transcript `a` has three compatible paths:

$$
(a,a),\qquad
(a,\varnothing),\qquad
(\varnothing,a).
$$

Their total is

$$
0.4^2+0.4(0.6)+0.6(0.4)
=
0.64.
$$

Thus the greedy path decodes to a less probable transcript.

A prefix-based decoder must combine probabilities of paths that share an output prefix, with separate accounting for whether the prefix ends in blank. That separation preserves the repeated-label rule when another token is appended.

## What independence means, and what other models change

CTC factorizes path probability across time conditional on the input:

$$
P(\pi\mid x)=\prod_t p_t(\pi_t\mid x).
$$

This does not require the acoustic encoder to process frames independently. A frame distribution can depend on a wide context or the entire utterance.

The restriction is that the path factor at a frame does not additionally condition on the previously emitted path labels. A transducer introduces a prediction state based on the output prefix, allowing distributions to depend on both acoustic progress and label history.

That changes the alignment lattice and probability model. Replacing a recurrent encoder with a Transformer alone does not remove CTC's output factorization.

Streaming imposes another condition: a prediction must not depend on unavailable future audio beyond the allowed lookahead. This depends on the feature window, convolutions, attention masks, and decoder. The name of the encoder architecture does not establish the latency guarantee.

## Self-supervised audio learning solves a different missing-label problem

CTC assumes a transcript is available but its alignment is missing. Self-supervised pretraining can use audio without a transcript.

In wav2vec 2.0, a learned encoder produces latent acoustic features. A context network receives masked latent spans, while a quantization module provides target representations. The pretraining task distinguishes the correct target from distractors, with an additional objective encouraging codebook usage. This is not literal waveform reconstruction or a learned implementation of every MFCC step. [Original self-supervised speech formulation](https://arxiv.org/abs/2006.11477)

A contrastive term has the form

$$
\mathcal L_t
=
-\log
\frac{\exp(s(c_t,q_t)/\tau)}
{\sum_{q\in\mathcal Q_t}\exp(s(c_t,q)/\tau)}.
$$

The candidate set includes the correct target. The denominator turns similarity scores into a classification distribution.

For a constructed example with exponentiated scores

$$
2,\quad1,\quad1,
$$

where the first is correct, the target probability is

$$
\frac{2}{2+1+1}=\frac12,
$$

and the loss is

$$
\log2.
$$

This objective supplies representation-learning pressure without a transcript. CTC fine-tuning then supplies a different signal: which token sequences the acoustic representation should support.

Neither objective alone demonstrates a particular recognition accuracy or label-efficiency improvement on a new dataset.

## Revision checklist

| Check | What I should be able to reproduce |
|---|---|
| Frame count | Include window length, hop, padding, and encoder subsampling. |
| MFCC order | Apply power, filterbank pooling, logarithm, and DCT in the correct sequence. |
| Log representation | Derive additive source–filter structure under the stated model. |
| Feature compression | Reconstruct the two-channel example before and after discarding a coefficient. |
| CTC collapse | Explain why repeated target labels require separating blanks. |
| Likelihood | Enumerate and sum every compatible path in the three-frame example. |
| Forward recursion | Derive valid transitions, initialization, and terminal states. |
| Path count | Include adjacent repeats in the stars-and-bars calculation. |
| Gradient | Obtain the posterior occupancy and subtract it from the softmax output. |
| Numerical stability | Use log-sum-exp and detect impossible target lengths. |
| Decoding | Explain why the best path need not give the best transcript. |
| Model distinction | Separate missing alignments, missing transcripts, and streaming constraints. |

## Why it matters for my work

The transferable idea is to marginalize a structured missing variable rather than demand annotations for it. CTC is applicable when the latent alignment is monotone and its collapse rules fit the task. Spatial weak supervision in medical imaging does not automatically satisfy those assumptions, so the useful transfer is the likelihood-building method, not the speech loss unchanged.

## What I have not resolved

For a medical sequence task, I still need to specify which alignments are allowed, what a blank means, and whether repeated labels require separation. I also need a task-based justification before importing an auditory frequency scale into non-auditory physiological signals.
