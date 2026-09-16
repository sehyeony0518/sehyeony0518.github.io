---
layout: study_note
title: "Recommender Systems: Embeddings, Interactions, and a Field That Audited Itself"
description: "Deriving recommendation from sparse categorical features through embeddings, matrix factorization, feature interactions, ranking losses, retrieval metrics, and reproducible evaluation."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Learning Models & Representation"
subgroup: "Margins, Kernels & Embeddings"
order: 7
source: "Independent study"
written: true
updated: "2026-09-15"
---

A recommender assigns scores to items under a user and context, then uses those scores to select or order candidates.

The target must be specified. Predicting an explicit rating, predicting an observed click, ranking relevant items, and choosing an action that improves long-term utility are different problems. A model can be good at one and poor at another.

The sparse representation problem is equally specific: category identifiers are useful inputs, but arithmetic on the raw identifiers has no reason to reflect preference.

## Sparse identifiers become shared parameters

Suppose a categorical feature has $$F$$ possible values. Its one-hot representation has one nonzero entry:

$$
x=e_i.
$$

A linear model uses

$$
w^{\mathsf T}x=w_i.
$$

An embedding table instead assigns a vector to each category:

$$
E\in\mathbb R^{F\times d},
\qquad
h_i=E^{\mathsf T}e_i.
$$

The lookup returns one row's learned parameters. It need not construct the full one-hot vector.

The embedding dimension controls how many shared latent coordinates describe each category. A small dimension can reduce model size relative to storing an independent parameter for every possible interaction, but an embedding table can still be large because it contains one row per identifier.

For a constructed table with one million rows, 64 coordinates per row, and four bytes per coordinate, storage is

$$
10^6\cdot64\cdot4
=
256{,}000{,}000
$$

bytes before gradients or optimizer state.

Sparse input does not mean sparse model storage. It means that one example usually accesses only a small subset of the available rows.

The learned geometry serves the objective. There is no guarantee that a coordinate corresponds to genre, difficulty, or another named property unless the model or supervision constrains it that way.

## Matrix factorization as a low-rank score model

Let user and item vectors be

$$
p_u,q_i\in\mathbb R^d.
$$

A score model with biases is

$$
s_{ui}
=
\mu+b_u+b_i+p_u^{\mathsf T}q_i.
$$

The inner product combines latent compatibility, while the biases can represent a global level, a user's general rating tendency, and an item's general popularity or rating tendency.

Ignoring biases and collecting vectors into matrices gives

$$
S=PQ^{\mathsf T}.
$$

Each latent coordinate contributes one outer product:

$$
S=\sum_{a=1}^{d}P_{:a}Q_{:a}^{\mathsf T}.
$$

Every term has rank at most one, so

$$
\operatorname{rank}(S)\le d.
$$

This is the sharing assumption: the full user–item score matrix is explained by a limited number of factors.

For a constructed user vector

$$
p=(1,2),
$$

and items

$$
q_A=(2,0),\quad
q_B=(0,2),\quad
q_C=(1,1),
$$

the scores are

$$
s_A=2,\qquad s_B=4,\qquad s_C=3.
$$

The ranking is B, C, A.

A second user with vector

$$
p'=(2,1)
$$

gets scores four, two, and three, reversing the preference between A and B.

A user-specific additive bias does not change the ranking for that user because it shifts every candidate score equally. Item biases can change that ranking.

## The embedding coordinates are not uniquely identifiable

Suppose an invertible matrix $$A$$ transforms the factors:

$$
p_u'=Ap_u,
\qquad
q_i'=A^{-\mathsf T}q_i.
$$

The score remains

$$
\begin{aligned}
p_u'^{\mathsf T}q_i'
&=
p_u^{\mathsf T}A^{\mathsf T}A^{-\mathsf T}q_i\\
&=
p_u^{\mathsf T}q_i.
\end{aligned}
$$

The transformed user and item spaces can have different distances and coordinate interpretations while making identical predictions.

For example,

$$
p=(1,1),\qquad q=(2,1)
$$

have dot product three. With

$$
A=
\begin{bmatrix}
2&0\\
0&1
\end{bmatrix},
$$

the transformed vectors are

$$
p'=(2,1),\qquad q'=(1,1),
$$

and their dot product is still three.

An L2 regularizer removes some of this freedom by penalizing changes in norms, but orthogonal rotations still preserve both scores and norms.

Thus interpreting one learned axis as a real-world attribute requires more evidence than observing a plausible arrangement of a few items. Prediction can be identifiable even when the latent coordinates are not.

Also, dot product and cosine similarity are not interchangeable. For query

$$
p=(1,0),
$$

items

$$
q_1=(10,10),\qquad q_2=(1,0)
$$

have dot products ten and one. Their cosine similarities are one over square root two and one. Normalization reverses their order.

## Fitting only observed ratings

Let $$\Omega$$ be the set of observed user–item ratings. A regularized squared-error objective is

$$
L=
\frac12
\sum_{(u,i)\in\Omega}
(s_{ui}-r_{ui})^2
+
\frac{\lambda}{2}
\left(
\sum_u\lVert p_u\rVert_2^2+
\sum_i\lVert q_i\rVert_2^2
\right).
$$

Missing entries are absent from the first sum. Treating every missing rating as zero would define a different problem.

For one interaction, write

$$
e=p_u^{\mathsf T}q_i-r_{ui}
$$

with biases fixed. Its factor gradients are

$$
\nabla_{p_u}L=e q_i+\lambda p_u,
$$

$$
\nabla_{q_i}L=e p_u+\lambda q_i.
$$

The item vector determines which user coordinates receive an error signal, and vice versa. This is how an observed interaction influences other scores involving the same factors.

For a numerical step, choose

$$
p=(1,0),\quad q=(1,1),\quad r=3,
$$

with zero regularization and learning rate 0.1. The initial score is one, so

$$
e=-2.
$$

Using the original vectors for both simultaneous updates,

$$
p_{\mathrm{new}}
=
(1,0)-0.1[-2(1,1)]
=
(1.2,0.2),
$$

$$
q_{\mathrm{new}}
=
(1,1)-0.1[-2(1,0)]
=
(1.2,1).
$$

The new score is

$$
1.2(1.2)+0.2(1)=1.64.
$$

The half-squared error decreases from two to

$$
\frac12(3-1.64)^2=0.9248.
$$

This one step illustrates optimization, not convergence or generalization.

## Implicit feedback and ranking losses

A missing click is ambiguous. The user may dislike the item, never have seen it, or have liked it without taking the logged action.

One approach treats observed interactions as positive and unobserved pairs as weak negative evidence, with explicit confidence weights:

$$
L=
\sum_{u,i}
c_{ui}(y_{ui}-s_{ui})^2.
$$

The choice of $$c_{ui}$$ determines how strongly missing events influence the fit. Calling an unobserved pair a training negative does not establish that it is a known negative preference.

For a Bernoulli observation model,

$$
p_{ui}=\sigma(s_{ui})
=
\frac{1}{1+e^{-s_{ui}}},
$$

and the negative log-likelihood is

$$
\ell
=
-y\log p-(1-y)\log(1-p).
$$

Substituting the sigmoid simplifies it to

$$
\ell=\log(1+e^s)-ys,
$$

whose derivative is

$$
\frac{\partial\ell}{\partial s}=\sigma(s)-y.
$$

A pairwise ranking model instead compares a preferred item with another item:

$$
\Delta=s_{ui}-s_{uj}.
$$

If

$$
P(i\succ j)=\sigma(\Delta),
$$

the positive-pair loss is

$$
\ell_{\mathrm{pair}}
=
-\log\sigma(\Delta)
=
\log(1+e^{-\Delta}).
$$

Its derivative is

$$
\frac{\partial\ell_{\mathrm{pair}}}{\partial\Delta}
=
\sigma(\Delta)-1.
$$

For

$$
\Delta=\log3,
$$

the modeled preference probability is three quarters, the loss is

$$
\log\frac43,
$$

and the derivative is negative one quarter. Increasing the preferred item's score or decreasing the other score reduces the loss.

The result depends on how comparison items are sampled. Changing that distribution changes which ordering errors the model sees most often.

## Why explicit interactions become expensive

A linear model over sparse features is

$$
s(x)=w_0+\sum_{i=1}^{F}w_ix_i.
$$

It can assign independent contributions to active categories but cannot make the contribution of one feature depend on another without additional terms.

A full pairwise model adds

$$
\sum_{i<j}w_{ij}x_ix_j.
$$

The number of unordered pairs is

$$
\binom{F}{2}=\frac{F(F-1)}{2}.
$$

For 50,000 features, this is

$$
\frac{50{,}000\cdot49{,}999}{2}
=
1{,}249{,}975{,}000.
$$

That count excludes self-interactions and counts each unordered pair once.

A factorization machine replaces each independent pair coefficient by an inner product:

$$
w_{ij}=v_i^{\mathsf T}v_j.
$$

Its score is

$$
s(x)
=
w_0+\sum_iw_ix_i
+
\sum_{i<j}(v_i^{\mathsf T}v_j)x_ix_j.
$$

This shares parameters across pairs. A feature vector learned from one set of interactions can contribute to a pair that has rarely or never appeared directly.

It also restricts the interaction model. Factorization is useful because it imposes sharing, not because it can represent every arbitrary interaction table with a tiny latent dimension.

## Deriving the efficient factorization-machine computation

Expand the interaction term by latent coordinate:

$$
I(x)
=
\sum_{f=1}^{d}\sum_{i<j}v_{if}v_{jf}x_ix_j.
$$

For each coordinate,

$$
\left(\sum_i v_{if}x_i\right)^2
=
\sum_i v_{if}^2x_i^2
+
2\sum_{i<j}v_{if}v_{jf}x_ix_j.
$$

Subtract the diagonal terms and divide by two:

$$
I(x)
=
\frac12
\sum_{f=1}^{d}
\left[
\left(\sum_i v_{if}x_i\right)^2
-
\sum_i v_{if}^2x_i^2
\right].
$$

This identity avoids enumerating all active pairs.

If only $$m$$ features are nonzero, both inner sums need only those features, giving work proportional to

$$
md
$$

rather than

$$
m^2d.
$$

For a worked example, choose

$$
x=(1,2,0,1),
$$

with active embeddings

$$
v_1=(1,0),\quad
v_2=(1,1),\quad
v_4=(0,2).
$$

Direct pairwise calculation gives

$$
(v_1^{\mathsf T}v_2)(1)(2)=2,
$$

$$
(v_1^{\mathsf T}v_4)(1)(1)=0,
$$

$$
(v_2^{\mathsf T}v_4)(2)(1)=4.
$$

The total is six.

For the efficient expression, the weighted vector sum is

$$
1(1,0)+2(1,1)+1(0,2)=(3,4),
$$

whose squared norm is 25. The sum of the weighted vectors' individual squared norms is

$$
1+8+4=13.
$$

Therefore

$$
I(x)=\frac12(25-13)=6.
$$

The two calculations agree exactly.

Differentiating the efficient form also gives a reusable gradient:

$$
\frac{\partial I}{\partial v_{if}}
=
x_i
\left(
\sum_jv_{jf}x_j-v_{if}x_i
\right).
$$

The subtracted term removes self-interaction.

## Retrieval imposes an upper bound on ranking

A large system often first retrieves a candidate set $$C_u$$, then applies a richer ranker within it.

Let $$R_u$$ be the relevant items. Any final recommendation list drawn only from the candidates satisfies

$$
\operatorname{Recall}
\le
\frac{\lvert R_u\cap C_u\rvert}{\lvert R_u\rvert}.
$$

The ranker cannot recover an item that was never supplied.

For a constructed user, suppose relevant items are

$$
R_u=\{A,B,C\},
$$

while retrieval returns

$$
C_u=\{A,D,E\}.
$$

Even a perfect ranker can retrieve at most one of the three relevant items. Its recall ceiling is one third, although precision at the first position can still be one.

Candidate generation and ranking should therefore be evaluated separately. A final ranking failure might be caused by poor retrieval coverage rather than poor discrimination among available candidates.

Retrieval can use a dot-product score suitable for an efficient index, while ranking uses additional context and feature interactions. If the index uses a different similarity, normalization, or item snapshot from training, that mismatch changes the candidate set before the ranker runs.

## Ranking metrics from an explicit list

Suppose five ranked items have binary relevance

$$
(1,0,1,0,1),
$$

and these are the user's only three relevant items.

At cutoff three,

$$
P@3=\frac23,
\qquad
R@3=\frac23.
$$

Average precision rewards the positions at which relevant items appear:

$$
AP
=
\frac13
\left(
1+\frac23+\frac35
\right)
=
\frac{34}{45}
\approx0.7556.
$$

The denominator is the total number of relevant items, not merely those appearing above a chosen cutoff.

A discounted gain metric assigns less credit at lower ranks. With binary gains,

$$
DCG@K
=
\sum_{k=1}^{K}
\frac{r_k}{\log_2(k+1)}.
$$

The logarithm is a chosen discount convention, not a physical law of user attention.

For the first three positions,

$$
DCG@3
=
1+\frac1{\log_2 4}
=
1.5.
$$

The ideal top three would all be relevant:

$$
IDCG@3
=
1+\frac1{\log_2 3}+\frac12.
$$

Thus

$$
NDCG@3
=
\frac{1.5}{1+1/\log_2 3+1/2}
\approx0.7039.
$$

Normalizing by the ideal gain makes the scale comparable across relevance sets under the same convention.

Metrics computed against sampled negative items can differ substantially from full-catalog metrics. If an irrelevant item scores 0.9 and the relevant item scores 0.8, the relevant item is not ranked first. Remove the higher-scoring negative from the evaluation sample, and it becomes first without any model change.

The candidate universe is part of the metric definition.

## Exposure, cold start, and what an audit must hold fixed

If a click requires exposure, then

$$
P(\text{click}\mid u,i)
=
P(\text{exposure}\mid u,i)
P(\text{click}\mid\text{exposure},u,i).
$$

Observed clicks therefore reflect both user response and the policy that chose what to show. A model can reproduce exposure patterns without identifying the preference quantity one intended to estimate.

Inverse-propensity weighting can correct a specified selection mechanism under assumptions. If an outcome $$Y$$ is observed when $$E=1$$, and exposure probability is $$\pi(X)>0$$, conditional independence gives

$$
\mathbb E\left[\frac{EY}{\pi(X)}\mid X\right]
=
\frac{\mathbb E[E\mid X]\mathbb E[Y\mid X]}{\pi(X)}
=
\mathbb E[Y\mid X].
$$

The equality depends on the assumptions. Very small propensities also create large weights and potentially high variance.

Cold start is another information problem. A new item can receive a new embedding row immediately, but that row has little interaction evidence. Content features, shared category parameters, or an inductive encoder can provide an initial representation.

A user's recent history can likewise produce a representation without a trained user identifier, for example

$$
h_u=\frac1{\lvert H_u\rvert}\sum_{i\in H_u}q_i.
$$

This average loses order and some interaction information, but it supplies a defined cold-start computation.

Graph aggregation can share information through neighbors. It does not automatically solve cold start when nodes have only untrained identifiers and no informative neighbors.

The reproducibility lesson is to hold the actual comparison fixed: temporal split, candidate universe, negative sampling, filtering, tuning budget, early stopping, and metric implementation. A neural method beating one weak baseline does not establish that its architecture caused the improvement.

Reproduction results concern the methods and protocols tested. They should not be inflated into a claim that all progress in recommendation, or an unrelated field, is illusory.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| Explain an embedding lookup as sparse matrix multiplication. | Separate sparse access from table storage. |
| Derive the low-rank score matrix. | Express it as a sum of outer products. |
| Explain latent-coordinate non-identifiability. | Preserve scores with paired linear transformations. |
| Derive matrix-factorization gradients. | Reproduce the simultaneous update to score 1.64. |
| Distinguish missing feedback from known dislike. | State the confidence or sampling assumption. |
| Derive pointwise and pairwise ranking losses. | Calculate the log-three margin example. |
| Count unordered feature interactions. | Avoid counting every pair twice. |
| Derive the efficient FM identity. | Subtract diagonal terms and divide by two. |
| Reproduce both FM calculations. | Obtain interaction value six. |
| Prove the candidate-recall ceiling. | Explain why ranking cannot recover absent items. |
| Calculate AP and NDCG from a relevance list. | State the candidate universe and denominator. |
| Explain exposure bias and cold-start limitations. | Identify the information each proposed remedy requires. |

## Why it matters for my work

Sparse categories and rare combinations matter in medical data as well as recommendation. The useful transfer is parameter sharing with explicit assumptions, accompanied by evaluation that separates representation, candidate selection, and the process that generated observations.

## What I have not resolved

Identify which missing outcomes in my intended recommendation problem mean “not observed” rather than “negative,” and determine whether exposure probabilities are available or estimable.
