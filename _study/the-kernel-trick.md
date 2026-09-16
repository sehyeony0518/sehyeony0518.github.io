---
layout: study_note
title: "The Kernel Trick: Similarity Instead of Coordinates"
description: "Why the SVM dual admits a kernel at all, what a kernel is being asked to encode, and how one-class SVM and SVDD turn the same machinery into novelty detection."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Learning Models & Representation"
subgroup: "Margins, Kernels & Embeddings"
order: 6
source: "Independent study"
written: true
updated: "2026-09-15"
---

A kernel evaluates an inner product between feature representations without requiring their coordinates to be constructed explicitly. The feature space can be finite-dimensional or infinite-dimensional.

An infinite-dimensional feature space does not make the primal optimisation problem meaningless. A norm-regularised optimum can often be represented by finitely many training features. The kernel trick concerns representation and computation, not the nonexistence of a primal solution.

## A non-linear boundary from a linear feature-space rule

Let an input be mapped to a feature vector:

$$
x\mapsto\phi(x).
$$

A linear rule in that space is

$$
f(x)=\langle w,\phi(x)\rangle+b.
$$

It need not be linear in the original input.

For example, the feature map

$$
\phi(x_1,x_2)=(x_1^2,x_2^2)
$$

allows the rule

$$
f(x)=x_1^2+x_2^2-r^2.
$$

The zero set is a circle in the original coordinates, even though the rule is linear in the two transformed features.

The feature space need not always have more dimensions than the original space. What matters is that the transformation changes which functions can be represented as linear functionals.

A fixed kernel specifies this geometry in advance. Representation learning can instead learn a transformation, and the two approaches can also be combined. The distinction is not an absolute division between “chosen features” and “learned features.”

## A polynomial kernel, expanded and checked numerically

Define

$$
K(x,z)=(x^{\mathsf T}z)^2
$$

for two-dimensional inputs. Expanding the square gives

$$
K(x,z)
=
x_1^2z_1^2
+
2x_1x_2z_1z_2
+
x_2^2z_2^2.
$$

This is an ordinary inner product after the map

$$
\phi(x)
=
\begin{pmatrix}
x_1^2\\
\sqrt2\,x_1x_2\\
x_2^2
\end{pmatrix}.
$$

The square-root factor is necessary: multiplying the middle feature coordinates must reproduce the factor of two in the polynomial expansion.

For the constructed inputs

$$
x=(1,2)^{\mathsf T},
\qquad
z=(3,-1)^{\mathsf T},
$$

the direct calculation is

$$
x^{\mathsf T}z=3-2=1,
\qquad
K(x,z)=1.
$$

The feature-space calculation is

$$
\phi(x)=(1,2\sqrt2,4)^{\mathsf T},
$$

$$
\phi(z)=(9,-3\sqrt2,1)^{\mathsf T},
$$

and

$$
\phi(x)^{\mathsf T}\phi(z)
=
9-12+4=1.
$$

The kernel calculation and explicit feature calculation agree exactly. The trick becomes useful when an analogous expansion contains many terms, while the original kernel expression remains inexpensive.

The linear kernel,

$$
K(x,z)=x^{\mathsf T}z,
$$

is also a genuine kernel. Its feature map is simply the original input.

## Positive semidefiniteness is a consistency requirement

For training inputs, define the Gram matrix

$$
K_{ij}=K(x_i,x_j).
$$

If a feature representation exists, then for any coefficient vector,

$$
\begin{aligned}
c^{\mathsf T}Kc
&=
\sum_{i,j}c_ic_j
\langle\phi(x_i),\phi(x_j)\rangle\\
&=
\left\lVert\sum_i c_i\phi(x_i)\right\rVert^2\\
&\ge 0.
\end{aligned}
$$

The matrix must therefore be symmetric and positive semidefinite for every finite input collection.

This condition is stronger than assigning high values to similar objects. Consider the proposed Gram matrix

$$
K=
\begin{pmatrix}
1&2\\
2&1
\end{pmatrix}.
$$

For

$$
c=(1,-1)^{\mathsf T},
$$

we get

$$
c^{\mathsf T}Kc=-2.
$$

It cannot represent inner products in a real Hilbert space. The same failure appears in the implied squared distance:

$$
\lVert\phi(x_1)-\phi(x_2)\rVert^2
=
K_{11}+K_{22}-2K_{12}
=
-2.
$$

A similarity formula that implies a negative squared distance is inconsistent with the geometry required by a standard kernel method.

Checking one Gram matrix is only a check on that sample. Kernel validity requires the condition for every finite collection from the intended domain.

## Why the PSD condition also gives a feature space

For a single positive semidefinite Gram matrix, use its eigendecomposition:

$$
K=Q\Lambda Q^{\mathsf T},
\qquad
\Lambda\succeq 0.
$$

Set

$$
B=Q\Lambda^{1/2}.
$$

Then

$$
K=BB^{\mathsf T}.
$$

The rows of the factor are explicit feature vectors for that finite set of inputs. Zero eigenvalues indicate feature directions that are unnecessary for representing those pairwise products.

A construction for the entire input domain follows the same idea without choosing coordinates. Introduce formal symbols associated with inputs and finite linear combinations of them. Define their inner product by

$$
\left\langle
\sum_i a_iK_{x_i},
\sum_j b_jK_{z_j}
\right\rangle
=
\sum_{i,j}a_ib_jK(x_i,z_j).
$$

Positive semidefiniteness makes squared lengths non-negative. Identify combinations whose squared length is zero, then complete the resulting inner-product space. The map

$$
\phi(x)=K_x
$$

satisfies

$$
\langle\phi(x),\phi(z)\rangle=K(x,z).
$$

This explains why the finite-set PSD criterion is enough for an implicit feature representation. Mercer-style eigenfunction expansions provide a related representation under additional assumptions on the domain, measure, and kernel. Those assumptions should not be silently added to, or confused with, the basic PSD definition.

The feature coordinates are not unique. Rotating every feature vector by the same orthogonal transformation preserves all inner products. A kernel identifies a geometry relevant to the method, not one privileged coordinate system.

## Constructing kernels and deriving the Gaussian feature expansion

Several useful kernel constructions can be checked directly.

If two kernels have feature maps and their coefficients are non-negative, then

$$
aK_1(x,z)+bK_2(x,z)
$$

has the concatenated feature map

$$
\phi(x)=
\begin{pmatrix}
\sqrt a\,\phi_1(x)\\
\sqrt b\,\phi_2(x)
\end{pmatrix}.
$$

A product kernel corresponds to products of feature coordinates. In a finite-dimensional case,

$$
K_1(x,z)K_2(x,z)
=
\sum_{i,j}
\phi_{1i}(x)\phi_{2j}(x)
\phi_{1i}(z)\phi_{2j}(z).
$$

The paired coordinates form a feature map for the product. Adding a non-negative constant corresponds to appending a constant feature.

The Gaussian kernel is

$$
K(x,z)
=
\exp\left(
-\frac{\lVert x-z\rVert^2}{2\sigma^2}
\right),
\qquad \sigma>0.
$$

In one dimension, expand the squared difference:

$$
K(x,z)
=
e^{-x^2/(2\sigma^2)}
e^{-z^2/(2\sigma^2)}
e^{xz/\sigma^2}.
$$

Now expand the final exponential:

$$
e^{xz/\sigma^2}
=
\sum_{k=0}^{\infty}
\frac{x^kz^k}{\sigma^{2k}k!}.
$$

Therefore a countably infinite feature map is

$$
\phi_k(x)
=
e^{-x^2/(2\sigma^2)}
\frac{x^k}{\sigma^k\sqrt{k!}},
\qquad k=0,1,\ldots.
$$

Its inner product reproduces the Gaussian kernel. Its squared norm is finite:

$$
\sum_{k=0}^{\infty}\phi_k(x)^2
=
K(x,x)=1.
$$

In several dimensions, multiply the one-dimensional expansions across coordinates. This produces features indexed by tuples of non-negative integer powers.

Thus the infinite-dimensional representation is not a metaphor. Its coordinates and their summable squared lengths can be written explicitly, even though evaluating them all would be unnecessary.

For a numerical check, choose the bandwidth so that

$$
\sigma^2=\frac1{2\log 2}.
$$

Then inputs one unit apart have kernel value

$$
e^{-\log 2}=\frac12,
$$

while inputs two units apart have value

$$
e^{-4\log 2}=\frac1{16}.
$$

The effect is through squared distance, so doubling distance does not merely halve similarity.

## Bandwidth changes geometry, not just a curve's appearance

For distinct inputs, as the bandwidth approaches zero,

$$
K(x_i,x_j)\longrightarrow
\begin{cases}
1,&i=j,\\
0,&i\ne j.
\end{cases}
$$

Training feature vectors become approximately orthogonal. An observation can then have little kernel similarity to all training points unless it is extremely close to one.

As the bandwidth grows without bound,

$$
K(x_i,x_j)\longrightarrow 1.
$$

The Gram matrix approaches a rank-one matrix. The representation increasingly treats different inputs as similar.

These limits explain why bandwidth changes model behaviour, but they do not prove that one setting overfits or another generalises. The regularisation strength, sample distribution, and target function also matter.

Input scaling changes the squared distances inside the kernel. A coordinate measured in larger numerical units can dominate unless its scale is intentionally accounted for. Fitting a scaling transformation using held-out observations also changes the information available to training, so preprocessing belongs inside the training procedure.

## Why a finite representation exists even for the primal

Consider the norm-regularised feature-space problem

$$
\min_{w,b}
\frac{\lambda}{2}\lVert w\rVert_{\mathcal H}^2
+
\sum_i
\ell\left(
y_i,\langle w,\phi(x_i)\rangle+b
\right),
\qquad \lambda>0.
$$

Decompose any candidate weight into a component in the span of the training features and an orthogonal component:

$$
w=w_\parallel+w_\perp.
$$

For every training input,

$$
\langle w_\perp,\phi(x_i)\rangle=0.
$$

Thus the orthogonal component changes none of the fitted training values. But

$$
\lVert w\rVert^2
=
\lVert w_\parallel\rVert^2+\lVert w_\perp\rVert^2.
$$

Removing a non-zero orthogonal component strictly lowers the penalty while preserving the loss. An optimum therefore has a representation

$$
w=\sum_i c_i\phi(x_i).
$$

Predictions become

$$
f(x)=\sum_i c_iK(x_i,x)+b.
$$

This is the central finite-span argument behind representer results. It works directly in the primal and does not require the feature space itself to have finite dimension.

The assumptions matter. The data enter the objective only through fitted values, and the penalty increases with the norm. An arbitrary objective involving other aspects of the function need not have this form.

## Kernel ridge regression, solved both ways

For simplicity omit the intercept and consider

$$
\min_w
\frac12\sum_i
\left(\langle w,\phi(x_i)\rangle-y_i\right)^2
+
\frac{\lambda}{2}\lVert w\rVert^2.
$$

The Hilbert-space stationarity equation is

$$
\lambda w+
\sum_i
\left(\langle w,\phi(x_i)\rangle-y_i\right)\phi(x_i)
=0.
$$

Consequently, one can choose coefficients satisfying

$$
c_i=\frac{y_i-f(x_i)}{\lambda}.
$$

Since the fitted training values are the Gram matrix times the coefficient vector,

$$
\lambda c=y-Kc.
$$

Therefore

$$
(K+\lambda I)c=y.
$$

The matrix is positive definite for positive regularisation, even when the original Gram matrix is singular.

Take the linear kernel in one dimension, inputs one and two, responses one and two, and regularisation one:

$$
K=
\begin{pmatrix}1&2\\2&4\end{pmatrix}.
$$

Then

$$
K+I=
\begin{pmatrix}2&2\\2&5\end{pmatrix},
$$

whose inverse is

$$
\frac16
\begin{pmatrix}5&-2\\-2&2\end{pmatrix}.
$$

Thus

$$
c=
\begin{pmatrix}1/6\\1/3\end{pmatrix}.
$$

The prediction rule is

$$
f(x)=\frac16x+\frac13(2x)=\frac56x.
$$

At input three, it predicts

$$
f(3)=\frac52.
$$

The direct primal calculation gives the same answer:

$$
\min_w
\frac12[(w-1)^2+(2w-2)^2]+\frac12w^2.
$$

Its derivative is

$$
(w-1)+2(2w-2)+w=6w-5,
$$

so the optimum is five sixths.

This example also warns against cancelling a singular Gram matrix from a coefficient stationarity equation. The regularised linear system above follows from the feature-space first-order condition and remains valid without that cancellation.

## A complete non-linear SVM example

Use four inputs with labels:

$$
(1,1):+1,\qquad
(-1,-1):+1,\qquad
(1,-1):-1,\qquad
(-1,1):-1.
$$

A linear hard-margin classifier in the original coordinates cannot satisfy them. Adding the two positive-class margin inequalities gives

$$
2b\ge 2,
$$

while adding the two negative-class inequalities gives

$$
-2b\ge 2.
$$

The intercept would have to be both at least one and at most negative one.

Use the quadratic kernel from earlier. In the displayed order, its Gram matrix is

$$
K=
\begin{pmatrix}
4&4&0&0\\
4&4&0&0\\
0&0&4&4\\
0&0&4&4
\end{pmatrix}.
$$

Set every hard-margin dual multiplier to

$$
\alpha_i=\frac18.
$$

They are non-negative and satisfy the label balance condition

$$
\sum_i\alpha_i y_i=0.
$$

The resulting feature-space weight is

$$
w
=
\sum_i\alpha_i y_i\phi(x_i)
=
\begin{pmatrix}
0\\1/\sqrt2\\0
\end{pmatrix}.
$$

With zero intercept,

$$
f(x)=x_1x_2.
$$

Every training signed margin is exactly one. The primal objective is

$$
\frac12\lVert w\rVert^2=\frac14.
$$

The dual objective is

$$
\sum_i\alpha_i-\frac12\lVert w\rVert^2
=
\frac12-\frac14
=
\frac14.
$$

Feasibility and matching objectives prove optimality. The non-linear boundary is obtained without a numerical optimisation claim or a plotted boundary that merely looks plausible.

## Centring a Gram matrix

Some methods require centred feature vectors. Define the training feature mean

$$
\bar\phi=\frac1n\sum_i\phi(x_i).
$$

For centred features, expand the inner product:

$$
\begin{aligned}
K^{\mathrm c}_{ij}
&=
\langle\phi(x_i)-\bar\phi,\phi(x_j)-\bar\phi\rangle\\
&=
K_{ij}
-\frac1n\sum_rK_{rj}
-\frac1n\sum_sK_{is}
+\frac1{n^2}\sum_{r,s}K_{rs}.
\end{aligned}
$$

Define the centring matrix

$$
H=I-\frac1n\mathbf1\mathbf1^{\mathsf T}.
$$

The expression becomes

$$
K^{\mathrm c}=HKH.
$$

For a new input, subtract the same training feature mean. Recentring a test set around its own mean defines a different transformation.

Centring illustrates a general rule: when an algorithm is rewritten in kernel form, every operation involving the feature representation must be translated, not just the most conspicuous inner product.

## One-class SVM: deriving its constraints and coefficients

A one-class SVM uses a feature-space hyperplane to describe training inputs without a second labelled class. One formulation is

$$
\begin{aligned}
\min_{w,\rho,\xi}\quad
&
\frac12\lVert w\rVert^2-\rho
+\frac1{\nu n}\sum_i\xi_i\\
\text{subject to}\quad
&
\rho-\langle w,\phi(x_i)\rangle-\xi_i\le 0,\\
&
\xi_i\ge 0,
\end{aligned}
$$

where

$$
0<\nu\le 1.
$$

The negative threshold term rewards placing the hyperplane away from the origin; the norm and slack terms prevent that reward from being obtained without cost.

Let the two sets of multipliers be non-negative. Stationarity gives

$$
w=\sum_i\alpha_i\phi(x_i),
$$

$$
\sum_i\alpha_i=1,
$$

and

$$
\alpha_i+\beta_i=\frac1{\nu n}.
$$

After substitution, the dual is

$$
\min_\alpha\frac12\alpha^{\mathsf T}K\alpha
$$

subject to

$$
\sum_i\alpha_i=1,
\qquad
0\le\alpha_i\le\frac1{\nu n}.
$$

The score is

$$
f(x)=\sum_i\alpha_iK(x_i,x)-\rho.
$$

An interior multiplier supplies

$$
\rho=\sum_j\alpha_jK(x_j,x_i).
$$

Two counting properties follow directly from the constraints. If there are a specified number of positive coefficients, their sum cannot exceed that number times the coefficient ceiling. Thus

$$
\#\{i:\alpha_i>0\}\ge\nu n.
$$

Positive slack forces the coefficient to its ceiling. Since all coefficients sum to one,

$$
\#\{i:\xi_i>0\}\le\nu n.
$$

These statements concern training support coefficients and strict slack violations. They do not make the score a calibrated probability of novelty, nor do they guarantee a chosen error rate on an arbitrary shifted test distribution.

## SVDD and when the sphere and hyperplane agree

Support vector data description seeks a small enclosing feature-space sphere with slack:

$$
\min_{a,q,\xi}
q+C\sum_i\xi_i
$$

subject to

$$
\lVert\phi(x_i)-a\rVert^2\le q+\xi_i,
\qquad
\xi_i\ge 0.
$$

Here the scalar represents squared radius. For the following derivation, allow it to range over the real line and choose

$$
C>\frac1n.
$$

A negative value cannot be optimal. If it were negative, increasing it to zero and decreasing every slack by its absolute amount preserves feasibility and non-negativity of the slacks. The objective change is

$$
q(Cn-1)<0.
$$

Thus this unconstrained scalar representation still has a non-negative optimal squared radius.

Stationarity in the squared radius, centre, and slacks gives

$$
\sum_i\alpha_i=1,
\qquad
a=\sum_i\alpha_i\phi(x_i),
\qquad
0\le\alpha_i\le C.
$$

Substituting into the Lagrangian yields the dual

$$
\max_\alpha
\sum_i\alpha_iK(x_i,x_i)
-
\alpha^{\mathsf T}K\alpha.
$$

The squared distance of a new input from the fitted centre is

$$
d^2(x)
=
K(x,x)
-
2\sum_i\alpha_iK(x_i,x)
+
\sum_{i,j}\alpha_i\alpha_jK(x_i,x_j).
$$

No explicit feature coordinates are required.

If the kernel has a constant diagonal over the entire input domain,

$$
K(x,x)=\kappa,
$$

then the first dual term is constant because the coefficients sum to one. With the same coefficient ceiling, the sphere and one-class hyperplane duals have the same minimisers.

At an interior support observation,

$$
q=\kappa-2\rho+\lVert a\rVert^2.
$$

Therefore

$$
d^2(x)\le q
\quad\Longleftrightarrow\quad
\langle a,\phi(x)\rangle\ge\rho.
$$

The acceptance regions agree. Gaussian kernels have this constant-diagonal property.

Constancy only on the training inputs is insufficient for agreement on new inputs. With a linear kernel and training values negative one and positive one, equal coefficients place the sphere centre at zero with squared radius one. The one-class hyperplane instead has zero weight and zero threshold. Input two is outside the sphere, but its hyperplane score is zero. The test-input diagonal matters.

## Computational size and what similarity does not guarantee

A dense Gram matrix contains a quadratic number of entries in the sample count. A kernel method can avoid constructing enormous feature vectors while still becoming expensive in the number of observations.

For an SVM, predictions can use only observations with non-zero dual coefficients. That is exact, but there is no universal guarantee that only a small fraction will have positive coefficients. A linear SVM can instead store its explicit weight vector and avoid retaining training inputs for prediction.

The rule

$$
f(x)=\sum_i\alpha_i y_iK(x_i,x)+b
$$

resembles a similarity-weighted vote, but it is not a nearest-neighbour rule. Its coefficients are learned jointly through an optimisation problem, need not be normalised as voting probabilities, and can reflect global constraints.

Finally, “similar under the kernel” is the actual mathematical criterion. A kernel sensitive to acquisition protocol can regard a familiar protocol as normal even when the clinically relevant content differs. The optimisation does not correct a mismatch between the chosen geometry and the intended meaning of similarity.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| Expand a polynomial kernel | Recover the square-root feature factors |
| Prove a Gram matrix must be PSD | Express its quadratic form as a squared norm |
| Reject an invalid similarity | Construct a negative quadratic form |
| Explain feature-map existence | Use a Gram factorisation or the formal feature-space construction |
| Derive a Gaussian feature expansion | Expand the exponential after separating squared norms |
| Prove the finite-span property | Remove the orthogonal weight component |
| Solve kernel ridge regression | Obtain the regularised Gram system |
| Verify the non-linear SVM example | Match primal and dual objectives |
| Centre features through kernels | Derive the two means and grand-mean correction |
| Derive the one-class dual | Obtain the unit-sum constraint and coefficient ceiling |
| Compare one-class SVM and SVDD | State the constant-diagonal condition |
| Assess computational cost | Count samples as well as feature dimensions |

## Why it matters for my work

A kernel makes the representation's similarity assumptions explicit. That is useful when auditing whether a model responds to anatomy, acquisition conditions, or preprocessing. A novelty detector inherits the same assumptions and needs its own evaluation.

## What I have not resolved

I need to determine which similarities remain stable across the data sources I use. Kernel validity guarantees coherent geometry, not that the geometry captures the distinctions my application needs.
