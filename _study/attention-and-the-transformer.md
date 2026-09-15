---
layout: study_note
title: "Attention: Retrieval as a Differentiable Operation"
description: "Query, key and value are a soft dictionary lookup, and everything else in a Transformer is bookkeeping around it. Including why the scores are divided by √d, which is not a fudge factor."
tab: "ai-foundations"
tab_title: "Theory"
category: "neural-networks"
category_title: "Neural Networks & Representation"
order: 13
source: "Independent study"
written: true
updated: "2026-09-15"
---

> Fill in the blank: "the trophy didn't fit in the suitcase because **it** was too big."

What *it* refers to is not in the word. It is in the sentence, and swapping one adjective — *too small* — moves the referent. Any architecture that resolves this has to let a representation of "it" be revised by arbitrarily distant words, with the relevance of each word decided by content rather than by position.

## Core question and definition

**Attention** is the operation that does that, and it is a soft dictionary lookup.

Each token emits three vectors, each a learned linear projection of itself:

- a **query** — what information this token needs,
- a **key** — what information this token offers,
- a **value** — the information itself.

Token $$i$$ compares its query against every key, and takes a weighted average of the values with weights given by that match:

$$
\text{Attention}(Q,K,V) = \operatorname{softmax}\!\left(\frac{QK^{\mathsf T}}{\sqrt{d_k}}\right)V
$$

A hard dictionary returns `d[k]` when the key matches exactly. This returns a convex combination over all entries, weighted by similarity — which makes it differentiable, and therefore learnable.[^vaswani]

The tokens entering this are already vectors, not symbols. A categorical index carries no arithmetic — token 3475 is not three times token 1158 — so an **embedding** layer maps each token to a learned vector in a space where direction means something, the space in which *king* − *man* + *woman* lands near *queen*.[^w2v] Attention then operates on those vectors, and the space it operates in was itself learned.

**Self-attention** is the case where $$Q$$, $$K$$ and $$V$$ are all projections of the same sequence: every token queries every token, itself included.

Nothing in that expression refers to position. Distance costs nothing — a token 500 away is reached in exactly the same operation as its neighbour — and it is also why position must be injected separately.

## Key concepts

### The $$\sqrt{d_k}$$ is a variance correction, not a fudge

If query and key components are independent with unit variance, their dot product over $$d_k$$ dimensions has variance exactly $$d_k$$. I confirmed this numerically over 200,000 samples:

| $$d_k$$ | measured var($$q\cdot k$$) | std | std after $$/\sqrt{d_k}$$ |
|---|---|---|---|
| 8 | 8.00 | 2.83 | 1.000 |
| 64 | 63.92 | 8.00 | 0.999 |
| 512 | 513.36 | 22.66 | 1.001 |

So logits grow like $$\sqrt{d_k}$$, and softmax saturates on large logits. Scaling the same logits by 8 turns a distribution of $$(0.09, 0.24, 0.67)$$ into $$(0.000, 0.0003, 0.9997)$$; by 30, into a one-hot vector. A saturated softmax has a vanishing gradient, so without the correction, wider models train worse for a reason that has nothing to do with capacity.

Dividing by $$\sqrt{d_k}$$ returns the logit standard deviation to 1 at every width.

### Multi-head costs nothing, which is the point

One attention operation produces one weighted average — one notion of relevance. But a token may need several at once: its syntactic subject, its coreferent, its modifier.

**Multi-head attention** runs $$h$$ attention operations in parallel on lower-dimensional projections and concatenates. What is easy to miss is that it is free:

| | parameters |
|---|---|
| 8 heads, $$d_k = 512/8 = 64$$ each | $$8 \times 3 \times 512 \times 64 = 786{,}432$$ |
| 1 head at full width $$d_k = 512$$ | $$3 \times 512 \times 512 = 786{,}432$$ |

Identical. The same budget is partitioned rather than enlarged, buying several independent relevance patterns instead of one — an argument about *representational diversity at fixed capacity*, which is a strictly better deal than it first appears.

### What it costs, and where the crossover sits

Self-attention is $$O(n^2 d)$$ per layer; recurrence is $$O(n d^2)$$. With $$d=512$$:

| $$n$$ | self-attention $$n^2d$$ | recurrent $$nd^2$$ |
|---|---|---|
| 10 | 51,200 | 2,621,440 |
| 100 | 5,120,000 | 26,214,400 |
| 1000 | 512,000,000 | 262,144,000 |

**The crossover is at $$n = d$$.** For sequences shorter than the model width — most sentences — attention is cheaper *and* better. Past it the quadratic bites, which is the entire motivation for the long-context literature.

But the decisive number is not cost, it is **maximum path length**: $$O(1)$$ for attention against $$O(n)$$ for recurrence. In an RNN, information from token 1 reaching token 500 passes through 499 multiplications; that is what vanishing gradients *are*. Attention makes it one hop. And the whole sequence is processed in parallel, where recurrence is inherently sequential — which is why Transformers could be scaled and LSTMs could not.

### Position has to be added back

Since attention is permutation-equivariant, position must be supplied. The sinusoidal encoding uses a bank of frequencies:

$$
PE_{(pos,2i)} = \sin\!\left(\frac{pos}{10000^{2i/d}}\right), \qquad
PE_{(pos,2i+1)} = \cos\!\left(\frac{pos}{10000^{2i/d}}\right)
$$

The clean way to see it is as a **continuous binary counter**. Counting 0–7 in binary, the last column alternates every step, the middle every two, the first every four. The sinusoidal encoding is that with real-valued columns: wavelengths run from $$2\pi \approx 6.3$$ to $$10000 \cdot 2\pi \approx 62{,}832$$, so fast components resolve adjacent positions and slow ones carry coarse location.

Two consequences. Positions beyond the training length still receive distinct codes, where a learned lookup table has nothing to return. And because $$\sin(a+b)$$ and $$\cos(a+b)$$ are linear in $$\sin a, \cos a$$, a fixed offset is a linear transformation of the encoding — relative position is *linearly recoverable*, which is what the attention projections need.

It is **added** rather than concatenated, which costs no dimensions; in a high-dimensional space the two signals can occupy near-orthogonal subspaces.

### Three masks, one operation

The encoder–decoder split is easiest to read as three uses of the same computation, differing only in who supplies $$Q$$, $$K$$, $$V$$ and what is masked:

| | Q from | K,V from | mask |
|---|---|---|---|
| encoder self-attention | source | source | none |
| decoder self-attention | target | target | causal — future positions set to $$-\infty$$ |
| cross-attention | target | **source** | none |

The causal mask exists because generation is sequential: predicting token $$t$$ having seen token $$t{+}1$$ is not a harder version of the task, it is a different and trivial one. Setting the logits to $$-\infty$$ before the softmax makes them exactly zero after it.

BERT uses the unmasked form and is trained to fill gaps; GPT uses the causal form and is trained to continue.[^bert] The common shorthand that "BERT is the encoder and GPT is the decoder" is close enough to be useful and wrong in a specific way — the Transformer's decoder also has cross-attention, which GPT has nothing to attend across.

## Why it matters for my work

Attention is the first architecture in the corpus whose **learned relevance is explicitly represented as a number I can read**. The weight token $$i$$ assigns to token $$j$$ is not inferred from a gradient or a perturbation; it is computed in the forward pass and sits in a matrix.

That looks like it should be a gift to auditing, and the caution is that it is not — or not obviously. A high attention weight says the value vector at $$j$$ contributed heavily to the updated representation at $$i$$. It does not say that token $$j$$ *caused* the output, because the value vector at $$j$$ has already been contaminated by earlier layers of attention over other tokens. By layer 6, "the value at position $$j$$" is a summary of much of the sequence. **Attention is interpretable as a routing diagram and not as an attribution**, and the literature disputing "attention is explanation" is disputing exactly this conflation — which the [faithfulness](/study/explanation-faithfulness-versus-plausibility/) note frames generally and which attention makes unusually concrete, because here there *is* a plausible-looking number to over-read.

The second point is the one I expect to matter more in practice. **Attention's cost is quadratic in sequence length, and a medical image is a long sequence.** A $$512\times512$$ slice at $$16\times16$$ patches is 1024 tokens — past the crossover. A volume is worse by a factor of the slice count. So the architectural choice for medical imaging is not "Transformer or CNN" in the abstract; it is a question about where the $$n=d$$ crossover falls for the input in hand, and the convolutional prior that [invariance and equivariance](/study/translation-invariance-and-equivariance/) describes is not obviously worth discarding when data are scarce. The instinct I have settled on — convolutions to reduce the image to a manageable token count, attention to relate those tokens — is what the strongest hybrid results do, and it is a statement about inductive bias rather than about which architecture is better.

## What I have not resolved

Whether the position encoding matters for volumetric medical data in a way it does not for text. Anatomical position is not a sequence index — it is a 3-D coordinate in a space with real metric structure, and flattening a volume into a sequence discards that the way a bag of words discards syntax. Whether the standard encodings recover it, or whether the geometry has to be built in, I do not know.

---

[^vaswani]: Vaswani, A., et al. (2017). Attention is all you need. *NeurIPS*. [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)

[^bert]: Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. *NAACL-HLT*. [10.18653/v1/N19-1423](https://doi.org/10.18653/v1/N19-1423)

[^w2v]: Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. [arXiv:1301.3781](https://arxiv.org/abs/1301.3781)
