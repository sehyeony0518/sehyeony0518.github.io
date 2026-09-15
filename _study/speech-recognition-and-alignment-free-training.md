---
layout: study_note
title: "Speech Recognition: Learning Without Knowing Where Anything Starts"
description: "You can label an utterance; you cannot label a 10-millisecond frame. CTC sums over all 28 trillion ways the label could line up — and that trick is worth more than the speech application."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
order: 12
source: "Independent study"
written: true
updated: "2026-09-15"
---

Speech recognition looks like classification and is not, for a reason that recurs far outside speech: **the input and output have different, unrelated, data-dependent lengths, and nothing says which part of the input produced which part of the output.**

## Core question and definition

A 30-minute lecture at 44.1 kHz is 79,380,000 numbers. The transcript is a few thousand characters. Between them:

- the lengths are unrelated, and vary per utterance;
- the alignment is unknown — a slow speaker's "hello" occupies five times the frames of a fast one's, and both are "hello";
- **frame-level labels do not exist**, because nobody will annotate which 10-millisecond window is the `h`.

That last point is the binding constraint. Labelling an utterance is cheap. Labelling 180,000 frames per utterance is not, and it is the labelling that has to scale.

The classical pipeline factorises the problem into three models — **acoustic** (waveform → phonemes), **pronunciation** (phonemes → words), **language** (words → plausible sentences) — chained through a transducer. All three survive in end-to-end systems, either explicitly or absorbed into the weights.

The reason the language model cannot be dropped is that acoustics genuinely underdetermine the answer. *Recognise speech* and *wreck a nice beach* are nearly the same signal; only the sentence prior separates them.

## Key concepts

### MFCCs, and what "cepstral" is doing

The feature standard held for decades, which usually means it is doing something right.

Window the waveform into ~25 ms frames every 10 ms — 400 samples at 16 kHz, hopping 160. Then per frame: Fourier transform, take the **log** magnitude, warp the frequency axis to the **mel** scale, and Fourier transform *again*.

Each step corresponds to something the ear does. The log matches perceived loudness — we hear doublings, not increments. The mel warping matches frequency resolution — the gap between 100 and 200 Hz is audible in a way the gap between 10.0 and 10.1 kHz is not, both being factors the linear axis treats identically.

The second transform is the odd one, and the name records the joke: a transform of a log spectrum is a **cepstrum**, on a **quefrency** axis. What it buys is real. Voiced speech has harmonics at regular intervals set by the pitch; regular structure in the frequency domain becomes a *peak* in the cepstral domain, which is why a peak near 7 ms reads directly as a pitch near 143 Hz. It also separates source from filter: the vocal folds' excitation and the vocal tract's shaping overlap multiplicatively in the spectrum, so the log makes them additive and the second transform puts them in different places.

The compression is substantial — 39 numbers per frame turns that 30-minute lecture from 79 million samples into 7 million, an 11× reduction — but compression is not the argument. **The argument is that the representation is one the ear already computes**, and speech evolved to be heard.

### CTC sums over every alignment

Given per-frame outputs and an utterance-level label, CTC defines the loss as the total probability of **every frame-to-label alignment consistent with the transcript**.[^ctc] Introduce a blank symbol; collapse repeats; then `hheelllloo`, `h-e-l-l-o-`, and `hhhhello---` all decode to `hello`, and training maximises their sum.

The count is the part worth seeing:

| frames $$T$$ | label length $$L$$ | valid alignments |
|---|---|---|
| 5 | 2 | 35 |
| 10 | 3 | 1,716 |
| 50 | 5 | 29,248,649,430 |
| 100 | 5 | **28,848,458,598,960** |

One second of speech against a five-character label admits nearly 29 trillion alignments. Enumerating them is impossible; a forward–backward dynamic program computes the sum in $$O(TL)$$ because the alignments share prefixes.

This is the same structural trick as the [combinatorial explosion](/study/the-combinatorial-explosion-and-learned-pruning/) note: an exponential space made tractable by exploiting structure rather than by more compute. And the payoff is about *annotation*, not accuracy — **CTC converts a labelling problem that cannot be afforded into one that can**, by summing out the variable nobody wants to label.

Its cost is a conditional-independence assumption between frames, which is why RNN-Transducer feeds the previous output back in, and why Transformer variants replace the recurrence while masking attention to a sliding window so that streaming stays possible.

### Filling in gaps in a waveform

wav2vec 2.0 is BERT for audio: mask spans of the encoded signal and train the model to identify what belonged there, from context.[^w2v2]

The move that is easy to skip past is that it starts from the **raw waveform**, with the MFCC pipeline learned rather than specified. That is the paper's title and not its main contribution — the pre-training is — which is itself a comment on what the authors thought was worth claiming.

The strategic point is about which data are scarce. Transcribed speech is expensive and limited. *Untranscribed* speech is effectively unlimited. Pre-training on the abundant kind and fine-tuning on the scarce kind reverses which resource binds, and the reported result — competitive word error rate after hours rather than thousands of hours of labelled fine-tuning — is that reversal paying off.

## Why it matters for my work

The alignment problem is not about speech. **It is the general case of supervision at a coarser granularity than the model's output**, and medical imaging is full of it.

A radiology report says "small nodule in the right upper lobe." It does not say which voxels. A pathology slide has a patient-level diagnosis and no per-region annotation. In both, the label exists at the level of the study and the prediction is needed at the level of the region — which is exactly speech's mismatch, with space substituted for time. The corpus already frames this as [multiple-instance learning](/study/self-supervised-and-weakly-supervised-learning/); CTC is the same idea with the extra constraint that the fine-grained units are *ordered*, and it makes the accounting explicit by summing over placements rather than pooling over them.

That reframes what "we lack annotated data" usually means. Often the data are annotated — at the wrong granularity. The question is whether the loss can marginalise over the missing alignment rather than whether someone can be paid to supply it.

The wav2vec strategy transfers directly and is, I suspect, underused. Every institution holds far more unreported imaging than reported imaging. Masked-region pre-training on the unlabelled majority, fine-tuned on the reported minority, uses the asymmetry that is actually present rather than the one the benchmark assumes.

## What I have not resolved

Whether the mel warping's justification survives the move to medical signals. It encodes human auditory perception, which is the right prior for speech because speech evolved to be heard. An ultrasound echo, an ECG, an EEG were not shaped by anything's perceptual system — so importing a perceptually-motivated frequency warping is importing an assumption that has no reason to hold, and I have not seen it examined rather than inherited.

---

[^ctc]: Graves, A., Fernández, S., Gomez, F., & Schmidhuber, J. (2006). Connectionist temporal classification: labelling unsegmented sequence data with recurrent neural networks. *ICML*. [10.1145/1143844.1143891](https://doi.org/10.1145/1143844.1143891)

[^w2v2]: Baevski, A., Zhou, H., Mohamed, A., & Auli, M. (2020). wav2vec 2.0: A framework for self-supervised learning of speech representations. *NeurIPS*. [arXiv:2006.11477](https://arxiv.org/abs/2006.11477)
