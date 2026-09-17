---
layout: study_note
title: "Attention: Retrieval as a Differentiable Operation"
description: "Deriving query-key-value attention, softmax, square-root dimension scaling, multi-head computation, positional encoding, causal masks, and Transformer costs through explicit examples."
og_image: "https://sehyeony0518.github.io/assets/img/og/attention-and-the-transformer.png"
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Learning Models & Representation"
subgroup: "Sequence Models & Attention"
order: 9
source: "Independent study"
written: true
updated: "2026-09-15"
---

Attention computes a content-dependent weighted combination of stored vectors. A query specifies what is being requested, keys determine compatibility, and values supply the information combined into the answer.

The operation is simple enough to calculate by hand. Its consequences are less simple: scaling affects gradients, masks define the information available to a prediction, and positional structure determines which permutations the computation can distinguish.

A Transformer also needs nonlinear feature processing, residual paths, and normalization. These components are not merely bookkeeping around attention.

## From token identifiers to query, key, and value matrices

A token identifier is a category, not a measured quantity. Let a vocabulary contain $$V$$ categories, and let an embedding table be

$$
E\in\mathbb R^{V\times d}.
$$

For token $$i$$, a one-hot row vector $$e_i^{\mathsf T}$$ selects its embedding:

$$
x_i=e_i^{\mathsf T}E.
$$

A software lookup performs this row selection without constructing the sparse one-hot vector.

For a sequence of $$n$$ representations,

$$
X\in\mathbb R^{n\times d},
$$

one attention head forms

$$
Q=XW_Q,\qquad
K=XW_K,\qquad
V=XW_V.
$$

The projection shapes can be

$$
W_Q,W_K\in\mathbb R^{d\times d_k},
\qquad
W_V\in\mathbb R^{d\times d_v}.
$$

Consequently,

$$
QK^{\mathsf T}\in\mathbb R^{n\times n}.
$$

Its entry at row $$i$$ and column $$j$$ compares query $$i$$ with key $$j$$.

In cross-attention, queries and memories come from different sequences. With $$n$$ queries and $$m$$ memory positions, the score matrix has shape

$$
n\times m.
$$

Query and key dimensions must agree for the dot product. Value dimension need not equal them.

The learned embedding coordinates acquire usefulness from the training objective. Their axes and distances do not automatically possess a fixed linguistic interpretation.

## Why softmax produces attention weights

For one query, suppose compatibility scores are $$s_1,\ldots,s_m$$. We need nonnegative weights that sum to one.

One derivation chooses weights to maximize compatibility while retaining entropy:

$$
\max_{a_j\ge0,\;\sum_j a_j=1}
\left[
\sum_j a_js_j
-
\tau\sum_j a_j\log a_j
\right].
$$

The positive temperature $$\tau$$ controls the preference for spreading mass.

Introduce a multiplier for the sum constraint. Differentiating with respect to a positive weight gives

$$
s_j-\tau(\log a_j+1)+\lambda=0.
$$

Rearranging,

$$
\log a_j=\frac{s_j}{\tau}+\frac{\lambda}{\tau}-1.
$$

Exponentiation shows that all weights share one multiplicative constant:

$$
a_j=C e^{s_j/\tau}.
$$

Normalization determines that constant:

$$
a_j=
\frac{e^{s_j/\tau}}{\sum_\ell e^{s_\ell/\tau}}.
$$

This is softmax. It balances high scores against a preference for a distributed selection.

The output is

$$
y=\sum_j a_jv_j.
$$

It lies in the convex hull of the value vectors for this head. That restriction applies to the weighted combination itself, not necessarily to the complete layer after output projection and residual addition.

Softmax is unchanged by adding the same constant to every score:

$$
\frac{e^{s_j-c}}{\sum_\ell e^{s_\ell-c}}
=
\frac{e^{s_j}}{\sum_\ell e^{s_\ell}}.
$$

Subtracting the largest score is therefore a numerically useful transformation that leaves the mathematical result unchanged.

## Deriving square-root dimension scaling

Let

$$
S=q^{\mathsf T}k=\sum_{a=1}^{d_k}q_ak_a.
$$

Assume the components are zero-mean, unit-variance, independent across coordinates, and that the query and key components are independent.

Each product has mean

$$
\mathbb E[q_ak_a]
=
\mathbb E[q_a]\mathbb E[k_a]
=
0.
$$

Its second moment is

$$
\mathbb E[q_a^2k_a^2]
=
\mathbb E[q_a^2]\mathbb E[k_a^2]
=
1.
$$

Thus each product has variance one. Cross-coordinate covariance terms vanish under the assumptions, giving

$$
\operatorname{Var}(S)
=
\sum_{a=1}^{d_k}\operatorname{Var}(q_ak_a)
=
d_k.
$$

The standard deviation grows as

$$
\sqrt{d_k}.
$$

Dividing by that quantity gives

$$
\operatorname{Var}\left(\frac{S}{\sqrt{d_k}}\right)=1.
$$

Scaled dot-product attention therefore uses

$$
A=
\operatorname{softmax}
\left(
\frac{QK^{\mathsf T}}{\sqrt{d_k}}+M
\right),
$$

$$
Y=AV.
$$

Softmax is applied separately to each row, and $$M$$ is a mask or additive bias.

The variance argument is conditional on its assumptions. Learned queries and keys can be correlated and can have non-unit variance. In self-attention, both projections originate from the same sequence, so independence is not a universal description of trained activations.

The scaling is a useful dimensional normalization, not a guarantee that every trained attention row has a particular entropy or variance.

## A complete attention calculation

Use a scalar query and three scalar keys:

$$
q=1,
\qquad
k=(0,\log2,\log3).
$$

Since key dimension is one, the scaling factor is one. The logits are

$$
s=(0,\log2,\log3).
$$

Exponentiation gives

$$
e^s=(1,2,3),
$$

so the weights are exactly

$$
a=\left(\frac16,\frac13,\frac12\right).
$$

Choose value vectors

$$
v_1=(2,0),
\qquad
v_2=(0,3),
\qquad
v_3=(4,2).
$$

The output is

$$
\begin{aligned}
y
&=
\frac16(2,0)
+
\frac13(0,3)
+
\frac12(4,2)\\
&=
\left(\frac13,0\right)
+
(0,1)
+
(2,1)\\
&=
\left(\frac73,2\right).
\end{aligned}
$$

The values determine what is retrieved. The keys determine how much each value contributes. Equal keys with different values would receive equal weights while still supplying different information.

Now mask the third memory position by assigning its logit negative infinity. Its exponential becomes zero, and the remaining weights are renormalized:

$$
a_{\mathrm{masked}}
=
\left(\frac13,\frac23,0\right).
$$

The new output is

$$
y_{\mathrm{masked}}
=
\frac13(2,0)+\frac23(0,3)
=
\left(\frac23,2\right).
$$

Masking is not equivalent to setting the third value to zero. That would preserve its weight in the denominator and produce a different result.

## Softmax derivatives and saturation

Write

$$
a_i=\frac{e^{s_i}}{Z},
\qquad
Z=\sum_j e^{s_j}.
$$

Differentiating the quotient gives

$$
\frac{\partial a_i}{\partial s_j}
=
a_i(\mathbf1[i=j]-a_j).
$$

For a two-entry row, the diagonal derivative is

$$
a(1-a).
$$

With logits zero and $$\log3$$, the weights are one quarter and three quarters. The diagonal derivative is

$$
\frac14\frac34=\frac3{16}=0.1875.
$$

Multiply both logits by four. The weights become

$$
\left(\frac1{82},\frac{81}{82}\right),
$$

because

$$
e^{4\log3}=81.
$$

The corresponding derivative is

$$
\frac{81}{82^2}\approx0.01205.
$$

This explicitly shows the reduced sensitivity of a saturated softmax.

It does not establish that every gradient in a complete model vanishes. The result depends on the surrounding computation and loss. For example, combining softmax with a negative log-likelihood can simplify derivatives in ways that require separate analysis.

Holding values fixed, attention's derivative with respect to one logit is especially informative:

$$
\begin{aligned}
\frac{\partial y}{\partial s_j}
&=
\sum_i v_i a_i(\mathbf1[i=j]-a_j)\\
&=
a_jv_j-a_j\sum_i a_iv_i\\
&=
a_j(v_j-y).
\end{aligned}
$$

A high weight does not ensure a large effect on the output. If that value already equals the weighted average, changing its logit has zero first-order effect.

## Multi-head attention divides a budget, but is not free

With $$h$$ heads, each head has separate projections and produces a separate weighted combination:

$$
H_r=
\operatorname{softmax}
\left(
\frac{Q_rK_r^{\mathsf T}}{\sqrt{d_k}}+M_r
\right)V_r.
$$

The outputs are concatenated and projected:

$$
Y=\operatorname{Concat}(H_1,\ldots,H_h)W_O.
$$

If each head uses

$$
d_k=d_v=\frac dh,
$$

the three input projection families contain

$$
3h\,d\frac dh=3d^2
$$

weights. The output projection adds

$$
d^2.
$$

Ignoring biases, the total is

$$
4d^2.
$$

For model width eight, one full-width head and two width-four heads both use 256 projection weights under this construction.

That is equality of a particular parameter count. It is not equality of every resource cost.

For sequence length four, one head has 16 attention scores, while two heads have 32. The heads can express different routing patterns, but each operates on a smaller projected space.

Execution overhead, attention storage, numerical behavior, and hardware efficiency can change with head count. Multiple heads do not guarantee a strictly better representation for every task at the same parameter budget.

## Accounting for the complete layer

Dense query, key, value, and output projections require approximately

$$
4nd^2
$$

multiply-accumulate operations.

Score formation and value aggregation together require approximately

$$
2n^2d
$$

when head dimensions sum to the model width.

A two-layer feed-forward network with hidden width $$d_{\mathrm{ff}}$$ adds approximately

$$
2ndd_{\mathrm{ff}}.
$$

A useful leading-order accounting is therefore

$$
4nd^2+2n^2d+2ndd_{\mathrm{ff}},
$$

excluding biases, softmax, normalization, and activation costs.

For a constructed layer with

$$
n=4,\qquad d=8,\qquad d_{\mathrm{ff}}=32,
$$

the three terms are

$$
1024,\qquad256,\qquad2048,
$$

for a total of 3328 multiply-accumulates.

The attention matrix computation is only one part of the layer.

Comparing only

$$
n^2d
$$

with a recurrent term

$$
nd^2
$$

produces a crossover at equal sequence length and model width. That simplified comparison is not a universal Transformer-versus-RNN latency threshold. It omits projections, feed-forward layers, constants, memory movement, and implementation choices.

Full attention creates pairwise interactions that grow quadratically with sequence length. An implementation can avoid storing the entire score matrix simultaneously without removing those mathematical interactions.

## Residual paths, normalization, and nonlinear feature processing

One possible pre-normalized block is

$$
U=X+\operatorname{MHA}(\operatorname{LN}(X)),
$$

$$
Z=U+\operatorname{FFN}(\operatorname{LN}(U)).
$$

A residual path preserves a direct route for the incoming representation. The sublayer learns an update rather than being solely responsible for reconstructing everything useful from its input.

For one token vector, layer normalization computes

$$
\mu=\frac1d\sum_{a=1}^{d}x_a,
$$

$$
v=\frac1d\sum_{a=1}^{d}(x_a-\mu)^2,
$$

and then

$$
\operatorname{LN}(x)_a
=
\gamma_a\frac{x_a-\mu}{\sqrt{v+\epsilon}}+\beta_a.
$$

The normalization here operates across a token's feature dimensions, not across the sequence positions.

A feed-forward sublayer can be written

$$
\operatorname{FFN}(x)
=
W_2\phi(W_1x+b_1)+b_2.
$$

It applies a learned nonlinear transformation independently at each position, using shared parameters. Attention mixes information between positions; the feed-forward network transforms the resulting features.

Different normalization placements and activation choices produce different architectures. The equations above define one block clearly, rather than treating every Transformer variant as identical.

## Proving permutation equivariance without positional structure

Let $$P$$ permute sequence positions. If queries, keys, and values all come from the permuted input, then

$$
Q'=PQ,\qquad K'=PK,\qquad V'=PV.
$$

The score matrix becomes

$$
Q'K'^{\mathsf T}
=
PQK^{\mathsf T}P^{\mathsf T}.
$$

Permuting both rows and columns permutes each row's entries without changing their normalization. Thus

$$
A'=PAP^{\mathsf T}.
$$

The output satisfies

$$
Y'=A'V'
=
PAP^{\mathsf T}PV
=
PAY
$$

only if the final symbol were the values, so the correct final substitution is

$$
Y'=PAV=PY.
$$

The result is permutation equivariance: reorder the inputs and the outputs reorder correspondingly.

This derivation assumes no fixed positional information and either no mask or a mask transformed consistently with the permutation. A fixed causal mask breaks arbitrary permutation symmetry because it encodes an ordering of permissible connections.

Permutation equivariance is useful for sets. A sequence model generally needs additional information about order, distance, or geometry.

## Sinusoidal position features and relative displacement

For frequency $$\omega$$, define

$$
p_\omega(t)=
\begin{bmatrix}
\sin(\omega t)\\
\cos(\omega t)
\end{bmatrix}.
$$

Using angle-addition identities,

$$
p_\omega(t+\Delta)
=
\begin{bmatrix}
\cos(\omega\Delta)&\sin(\omega\Delta)\\
-\sin(\omega\Delta)&\cos(\omega\Delta)
\end{bmatrix}
p_\omega(t).
$$

A fixed displacement therefore acts through a fixed linear transformation of this two-dimensional feature pair.

The inner product also has a useful identity:

$$
p_\omega(t)^{\mathsf T}p_\omega(u)
=
\cos(\omega(t-u)).
$$

It depends on relative displacement rather than absolute position.

A bank of frequencies supplies several scales of variation. The standard sinusoidal construction uses

$$
\omega_i=10000^{-2i/d},
$$

and places the sine and cosine values into alternating dimensions.

The identities explain why these features can support relative-position computations. They do not prove that a trained attention projection will learn the desired relation, or that the model will extrapolate reliably beyond training lengths.

Adding token and position vectors preserves the model width, but the two contributions are not guaranteed to occupy orthogonal subspaces. Learned projections must use their combination.

For images or volumes, the relevant position can include multiple spatial axes and physical spacing. A flattened sequence index alone does not uniquely describe those geometric relationships.

## Masks, generation, and what attention weights explain

A causal self-attention mask permits a query at position $$i$$ to use positions no later than itself:

$$
M_{ij}=
\begin{cases}
0,&j\le i,\\
-\infty,&j>i.
\end{cases}
$$

During teacher-forced training, shifted targets allow many next-token predictions to be computed in parallel without exposing their future answers.

During generation, future tokens do not yet exist. Previously computed keys and values can be cached. A new query compares against the available history, so its attention work grows with history length even though earlier key and value projections need not be recomputed.

Padding masks are separate from causal masks. Cross-attention may need to exclude padded memory positions as well. A row with every position masked has no valid normalized distribution and requires explicit handling.

Finally, an attention coefficient is a routing weight, not automatically a causal attribution. Suppose two scalar values are zero and ten, with weights 0.9 and 0.1. Their output is one. The larger weight multiplies a zero value.

In a complete model, value vectors already contain contextual information, output projections can cancel directions, and residual paths provide additional routes. Removing a token can also change the weights themselves.

Attention matrices are informative internal measurements. Interpreting them as explanations requires a claim about the complete computation and an appropriate test of that claim.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| State all query, key, value, and score shapes. | Include cross-attention with unequal sequence lengths. |
| Derive softmax from entropy-regularized selection. | Solve for the normalization constant. |
| Derive dot-product variance. | State the independence and variance assumptions. |
| Reproduce the three-memory example. | Obtain output seven thirds and two. |
| Explain why masking differs from zeroing a value. | Renormalize the permitted weights. |
| Derive the softmax Jacobian. | Calculate the saturation example. |
| Derive the attention-output derivative. | Obtain weight times value-minus-output. |
| Count multi-head parameters and attention entries separately. | Explain why equal parameters do not mean free computation. |
| Account for the entire Transformer layer. | Include projections and feed-forward computation. |
| Prove permutation equivariance. | Track both row and column permutations. |
| Derive the sinusoidal displacement identity. | Use the angle-addition formulas. |
| Explain the limits of attention as attribution. | Include values, projections, and residual paths. |

## Why it matters for my work

For medical imaging, I should choose tokenization and positional structure using the spatial relationships the task needs. Attention costs must include the full layer, and readable attention weights should be treated as hypotheses about information routing.

## What I have not resolved

Compare positional encodings using physical coordinates and voxel spacing against sequence-index encodings under controlled resampling and acquisition changes.
