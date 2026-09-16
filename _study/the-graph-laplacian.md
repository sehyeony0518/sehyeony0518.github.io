---
layout: study_note
title: "The Graph Laplacian: There Is More Than One, and Choosing Is the Modelling"
description: "What the heat equation, spectral clustering and graph networks share in the word Laplacian, why the smallest eigenvectors are the balanced states, and why writing D minus A reflexively skips a decision."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
subgroup: "Graph Signals & Spectral Methods"
order: 11
source: "Independent study"
written: true
updated: "2026-09-15"
---

A graph Laplacian turns local differences into an operator. Its quadratic form measures disagreement across edges, its nullspace identifies connected components, and its eigenvectors solve constrained smoothness problems.

Several distinctions matter. Nonzero-eigenvalue eigenvectors are modes, not equilibria. The random-walk Laplacian acts differently on node values and probability distributions. The random-walk and symmetric normalized Laplacians are related by a change of coordinates, so they are not unrelated alternatives with unrelated spectra.

## Assumptions and the sign convention

Take a finite undirected graph with symmetric nonnegative weights:

$$
A_{ij}=A_{ji}\ge0.
$$

Assume no self-loops for the initial derivations. Define degree and degree matrix by

$$
d_i=\sum_jA_{ij},
\qquad
D=\operatorname{diag}(d_1,\ldots,d_N).
$$

The combinatorial Laplacian is

$$
L=D-A.
$$

Its action at one node is

$$
(Lx)_i
=
d_i x_i-\sum_jA_{ij}x_j
=
\sum_jA_{ij}(x_i-x_j).
$$

A node above its weighted neighborhood has a positive graph-Laplacian value.

This sign is opposite the common continuous Laplacian convention. In one dimension, Taylor expansion gives

$$
u(s+a)
=
u(s)+a u'(s)+\frac{a^2}{2}u''(s)+O(a^3),
$$

$$
u(s-a)
=
u(s)-a u'(s)+\frac{a^2}{2}u''(s)+O(a^3).
$$

Adding more terms shows

$$
\frac{u(s+a)-2u(s)+u(s-a)}{a^2}
=
u''(s)+O(a^2).
$$

The graph operator instead uses the negative of this second difference:

$$
2u(s)-u(s-a)-u(s+a).
$$

Thus graph heat flow is written

$$
\frac{dx}{dt}=-Lx,
$$

matching the continuous heat equation with a positive coefficient multiplying the continuous Laplacian.

Without this sign check, a diffusion equation can accidentally become an equation that amplifies differences.

## Deriving the quadratic form

Expand

$$
x^{\mathsf T}Lx
=
\sum_i d_i x_i^2
-
\sum_{i,j}A_{ij}x_ix_j.
$$

Since degrees are row sums,

$$
\sum_i d_i x_i^2
=
\sum_{i,j}A_{ij}x_i^2.
$$

Symmetry allows the same quantity to be written with the other endpoint:

$$
\sum_i d_i x_i^2
=
\sum_{i,j}A_{ij}x_j^2.
$$

Average those two expressions:

$$
\begin{aligned}
x^{\mathsf T}Lx
&=
\frac12
\sum_{i,j}A_{ij}
\left(x_i^2+x_j^2-2x_ix_j\right)\\
&=
\frac12
\sum_{i,j}A_{ij}(x_i-x_j)^2.
\end{aligned}
$$

The factor one half appears because the double sum counts each undirected edge twice. Summing each edge only once gives

$$
x^{\mathsf T}Lx
=
\sum_{\{i,j\}\in E}w_{ij}(x_i-x_j)^2.
$$

Nonnegative weights make every term nonnegative, proving positive semidefiniteness.

The adjacency matrix itself need not be positive semidefinite. A single edge has adjacency matrix

$$
A=
\begin{bmatrix}
0&1\\
1&0
\end{bmatrix},
$$

with eigenvalues one and negative one, while

$$
L=
\begin{bmatrix}
1&-1\\
-1&1
\end{bmatrix}
$$

has eigenvalues zero and two.

Therefore a graph affinity matrix need not be a positive-semidefinite kernel in the kernel-method sense. Similarity graphs and reproducing-kernel constructions should not be identified solely because both use pairwise similarities.

## Incidence matrices explain gradient and divergence

Assign an arbitrary orientation to each undirected edge. For an edge directed from node $$j$$ to node $$i$$, let its incidence column be

$$
b_e=e_i-e_j.
$$

Collect these columns into a matrix $$B$$, and put edge weights in a diagonal matrix $$W_E$$.

The edge differences are

$$
B^{\mathsf T}x.
$$

For the chosen edge, the corresponding component is

$$
x_i-x_j.
$$

Weighted differences are

$$
W_EB^{\mathsf T}x.
$$

Applying the incidence matrix again returns net differences to nodes:

$$
BW_EB^{\mathsf T}x.
$$

Each edge contributes the block

$$
w_{ij}
\begin{bmatrix}
1&-1\\
-1&1
\end{bmatrix}
$$

on its endpoints. Summing these contributions gives

$$
L=BW_EB^{\mathsf T}.
$$

Reversing an edge orientation negates one incidence column twice in this product, so the operator is unchanged.

The energy becomes

$$
x^{\mathsf T}Lx
=
(B^{\mathsf T}x)^{\mathsf T}
W_E
(B^{\mathsf T}x).
$$

This makes the gradient-like interpretation literal: take differences on edges, weight them, and accumulate them back at nodes.

## A four-node example checked by edges and matrices

Use edges between nodes

$$
\{1,2\},\quad
\{2,3\},\quad
\{2,4\},\quad
\{3,4\},
$$

all with weight one. The degrees are

$$
d=(1,3,2,2).
$$

The Laplacian is

$$
L=
\begin{bmatrix}
1&-1&0&0\\
-1&3&-1&-1\\
0&-1&2&-1\\
0&-1&-1&2
\end{bmatrix}.
$$

Choose

$$
x=
\begin{bmatrix}1\\2\\0\\0\end{bmatrix}.
$$

Matrix multiplication gives

$$
Lx=
\begin{bmatrix}-1\\5\\-2\\-2\end{bmatrix}.
$$

The quadratic form is

$$
x^{\mathsf T}Lx
=
1(-1)+2(5)=9.
$$

The edge calculation gives the same result:

$$
(1-2)^2+(2-0)^2+(2-0)^2+(0-0)^2
=
1+4+4+0=9.
$$

Now take an explicit diffusion step of size one quarter:

$$
x^+=x-\frac14Lx
=
\begin{bmatrix}
\frac54\\
\frac34\\
\frac12\\
\frac12
\end{bmatrix}.
$$

Its total remains three, matching the initial total. Its energy is

$$
\left(\frac54-\frac34\right)^2
+
2\left(\frac34-\frac12\right)^2
=
\frac14+\frac18
=
\frac38.
$$

The hottest node loses value to its neighbors, and the energy falls in this constructed step.

More generally,

$$
x_i^+
=
(1-\eta d_i)x_i
+
\eta\sum_jA_{ij}x_j.
$$

If

$$
0\le\eta\le\frac1{d_{\max}},
$$

the coefficients are nonnegative and sum to one. Each updated value is then a weighted average of the old value and its neighbors. This is a direct sufficient condition for an averaging interpretation.

## Nullspace, components, and local equilibrium

Every row of the Laplacian sums to zero:

$$
L\mathbf1=0.
$$

A constant assignment has no edge differences.

Conversely, if

$$
Lx=0,
$$

then

$$
x^{\mathsf T}Lx=0.
$$

The energy is a sum of nonnegative terms, so every positive-weight edge must satisfy

$$
x_i=x_j.
$$

Following paths through a connected component shows that the value is constant throughout that component.

Therefore,

$$
\dim\ker L
=
\text{number of connected components}.
$$

On a connected finite graph, a globally harmonic signal is constant. The statement that many nonconstant fields can have zero Laplacian needs a boundary or a local interpretation.

For example, on a three-node path with values

$$
[0,1,2],
$$

the middle node has

$$
(Lx)_2=2(1)-0-2=0.
$$

It is locally balanced, but the endpoint Laplacian values are nonzero. If the endpoints are held fixed as boundary conditions, the interior can be harmonic without the entire field being constant.

The distinction is between equilibrium at selected interior nodes and equilibrium of a closed connected system.

## Eigenvectors solve a constrained smoothness problem

Unconstrained minimization of

$$
x^{\mathsf T}Lx
$$

allows zero and all constant assignments. To find a nontrivial mode, impose

$$
x^{\mathsf T}x=1,
\qquad
x^{\mathsf T}\mathbf1=0.
$$

The Lagrangian is

$$
\mathcal J(x,\lambda,\mu)
=
x^{\mathsf T}Lx
-\lambda(x^{\mathsf T}x-1)
-2\mu x^{\mathsf T}\mathbf1.
$$

Stationarity gives

$$
Lx=\lambda x+\mu\mathbf1.
$$

Multiply on the left by the constant vector's transpose. Since

$$
\mathbf1^{\mathsf T}L=0,
\qquad
\mathbf1^{\mathsf T}x=0,
$$

we obtain

$$
\mu=0.
$$

Thus a stationary point satisfies

$$
Lx=\lambda x.
$$

For a unit vector,

$$
x^{\mathsf T}Lx=\lambda.
$$

To identify the minimum, expand in an orthonormal eigenbasis. The orthogonality constraint removes the constant component, and the energy is an eigenvalue-weighted sum of squared coefficients. Its smallest possible value is the smallest remaining eigenvalue.

On a connected graph, this is the second-smallest eigenvalue. On a disconnected graph, there are multiple zero modes, so “take the second eigenvector” does not automatically produce a meaningful nontrivial partition.

Eigenvectors are stationary configurations of a constrained optimization problem. Under heat flow, a nonzero-eigenvalue eigenvector evolves as

$$
x(t)=e^{-\lambda t}x(0).
$$

It decays. Only nullspace modes are time-independent equilibria.

## The example graph's spectrum can be verified directly

For the four-node graph, the following eigenvectors are mutually orthogonal:

| Eigenvalue | Unnormalized eigenvector | Squared norm |
|---|---|---|
| $$0$$ | $$[1,1,1,1]^{\mathsf T}$$ | $$4$$ |
| $$1$$ | $$[-2,0,1,1]^{\mathsf T}$$ | $$6$$ |
| $$3$$ | $$[0,0,1,-1]^{\mathsf T}$$ | $$2$$ |
| $$4$$ | $$[1,-3,1,1]^{\mathsf T}$$ | $$12$$ |

Multiplying each vector by the displayed Laplacian verifies its eigenvalue. Dividing by the square root of its squared norm gives an orthonormal basis.

The eigenvector at eigenvalue one separates the pendant node from the two nodes in the triangle's far side, with the hub assigned zero. A threshold must decide how to handle that zero coordinate.

This example shows both the usefulness and the limit of the spectral relaxation. It provides a smooth nonconstant coordinate. Turning that coordinate into discrete groups is another operation, and the existence of a coordinate does not establish that the data contain a scientifically meaningful cluster structure.

## Degree normalization changes the norm and coordinates

For positive degrees, define

$$
L_{\mathrm{rw}}=D^{-1}L=I-D^{-1}A
$$

and

$$
L_{\mathrm{sym}}
=
D^{-1/2}LD^{-1/2}
=
I-D^{-1/2}AD^{-1/2}.
$$

The normalized smoothness problem uses the quotient

$$
\frac{f^{\mathsf T}Lf}{f^{\mathsf T}Df}.
$$

The denominator measures signal size with degree weights. Under constraints

$$
f^{\mathsf T}Df=1,
\qquad
f^{\mathsf T}D\mathbf1=0,
$$

the same Lagrange-multiplier argument gives

$$
Lf=\lambda Df.
$$

Multiplying by the inverse degree matrix yields

$$
L_{\mathrm{rw}}f=\lambda f.
$$

Now change coordinates:

$$
u=D^{1/2}f.
$$

Then

$$
L_{\mathrm{sym}}u=\lambda u.
$$

Equivalently,

$$
L_{\mathrm{sym}}
=
D^{1/2}L_{\mathrm{rw}}D^{-1/2}.
$$

The two normalized Laplacians are similar and have the same eigenvalues. Their eigenvectors represent related coordinates.

The symmetric normalized energy is

$$
u^{\mathsf T}L_{\mathrm{sym}}u
=
\frac12
\sum_{i,j}A_{ij}
\left(
\frac{u_i}{\sqrt{d_i}}
-
\frac{u_j}{\sqrt{d_j}}
\right)^2.
$$

Its null vector is therefore

$$
u_0\propto D^{1/2}\mathbf1,
$$

not generally the unweighted constant vector.

Isolated nodes require a separate convention because inverse degree factors are undefined there. They should be handled explicitly rather than silently divided by zero.

## Random-walk probabilities and node values are different objects

Define the row-stochastic transition matrix

$$
P=D^{-1}A.
$$

Its entries are

$$
P_{ij}=\frac{A_{ij}}{d_i},
$$

the probability of moving from node $$i$$ to node $$j$$.

For node values,

$$
(Pf)_i=\sum_jP_{ij}f_j
$$

is an average of neighboring values. Since rows sum to one,

$$
P\mathbf1=\mathbf1,
\qquad
L_{\mathrm{rw}}\mathbf1=0.
$$

A probability distribution evolves differently. If it is stored as a row vector,

$$
p_{t+1}^{\mathsf T}=p_t^{\mathsf T}P.
$$

If stored as a column vector,

$$
p_{t+1}=P^{\mathsf T}p_t.
$$

For an undirected graph, define

$$
\pi_i=\frac{d_i}{\sum_jd_j}.
$$

Then

$$
\begin{aligned}
(\pi^{\mathsf T}P)_j
&=
\sum_i
\frac{d_i}{\sum_r d_r}
\frac{A_{ij}}{d_i}\\
&=
\frac{\sum_iA_{ij}}{\sum_r d_r}\\
&=
\pi_j.
\end{aligned}
$$

Thus the stationary distribution is a left eigenvector of the row-stochastic transition matrix and a left null vector of the random-walk Laplacian:

$$
\pi^{\mathsf T}L_{\mathrm{rw}}=0.
$$

For the example graph,

$$
\pi=
\begin{bmatrix}
\frac18\\
\frac38\\
\frac14\\
\frac14
\end{bmatrix}.
$$

It is not a right null vector. At the pendant node,

$$
(L_{\mathrm{rw}}\pi)_1
=
\frac18-\frac38
=
-\frac14.
$$

This explicit calculation catches the row-versus-column confusion.

A stationary probability describes probabilities or expected proportions. A finite collection of walkers does not produce those exact counts at every time.

## Stationarity does not guarantee convergence

On a two-node graph with one edge,

$$
P=
\begin{bmatrix}
0&1\\
1&0
\end{bmatrix}.
$$

The stationary distribution is uniform, but a walker population initially concentrated at the first node alternates:

$$
\begin{bmatrix}1\\0\end{bmatrix},
\quad
\begin{bmatrix}0\\1\end{bmatrix},
\quad
\begin{bmatrix}1\\0\end{bmatrix},
\ldots
$$

The distribution does not converge. Periodicity is the obstruction.

A lazy walk uses

$$
P_{\mathrm{lazy}}=\frac12(I+P).
$$

If a mode has transition eigenvalue $$\mu$$, its lazy-walk eigenvalue is

$$
\frac{1+\mu}{2}.
$$

The oscillating eigenvalue negative one becomes zero. The associated Laplacian is

$$
I-P_{\mathrm{lazy}}
=
\frac12L_{\mathrm{rw}}.
$$

This particular laziness changes the time scale while preserving the eigenvectors and stationary distribution. It does not create an unrelated set of spectral coordinates.

The normalized Laplacian spectrum lies between zero and two. Nonnegativity follows from its energy. For the upper bound, use

$$
(a-b)^2\le2(a^2+b^2)
$$

inside the normalized energy sum to obtain

$$
u^{\mathsf T}L_{\mathrm{sym}}u
\le2u^{\mathsf T}u.
$$

The Rayleigh quotient then bounds every eigenvalue by two.

## Diffusion normalization can represent node capacity

Suppose edge weights describe conductance and each node has a positive capacity. Let the diagonal capacity matrix be $$C$$. Conservation gives

$$
C\dot x=-Lx.
$$

Since

$$
\mathbf1^{\mathsf T}L=0,
$$

the weighted total is conserved:

$$
\frac{d}{dt}\left(\mathbf1^{\mathsf T}Cx\right)=0.
$$

Choosing unit capacities gives combinatorial diffusion. Choosing capacities proportional to degree gives

$$
\dot x=-D^{-1}Lx.
$$

This is one concrete modeling interpretation of normalization. It changes how much a node's value responds to a given net flow.

At equilibrium on a connected graph, the value is constant, but its final constant is determined by the conserved quantity. Unit capacities preserve the ordinary mean; degree capacities preserve the degree-weighted mean.

Normalization is therefore more precise than a claim that hubs are “unfair.” It specifies a measure on nodes and a corresponding dynamics.

## Deriving spectral clustering from cut objectives

For a node subset $$S$$, define the cut weight as the total weight crossing to its complement. Its indicator vector satisfies

$$
\mathbf1_S^{\mathsf T}L\mathbf1_S
=
\operatorname{cut}(S,\bar S),
$$

because each crossing edge has squared difference one and each internal edge has difference zero.

Minimizing cut weight alone can favor a small isolated group. Balanced objectives add a size measure.

Let

$$
a=\lvert S\rvert,
\qquad
b=\lvert\bar S\rvert,
\qquad
a+b=N.
$$

Assign the two values

$$
f_i=
\begin{cases}
\sqrt{b/a},&i\in S,\\
-\sqrt{a/b},&i\in\bar S.
\end{cases}
$$

Then

$$
f^{\mathsf T}\mathbf1=0,
\qquad
f^{\mathsf T}f=N.
$$

Every crossing edge has squared difference

$$
\left(\sqrt{b/a}+\sqrt{a/b}\right)^2
=
\frac{N^2}{ab}.
$$

Therefore,

$$
\frac{f^{\mathsf T}Lf}{f^{\mathsf T}f}
=
\operatorname{cut}(S,\bar S)
\left(\frac1a+\frac1b\right).
$$

This is the RatioCut objective. Relaxing the requirement that the vector take exactly those two values leads to the ordinary spectral problem.

For normalized cuts, use volumes

$$
v_S=\sum_{i\in S}d_i,
\qquad
v_{\bar S}=\sum_{i\in\bar S}d_i,
$$

and assign values

$$
f_i=
\begin{cases}
1/v_S,&i\in S,\\
-1/v_{\bar S},&i\in\bar S.
\end{cases}
$$

The degree-weighted mean is zero, and direct substitution gives

$$
\frac{f^{\mathsf T}Lf}{f^{\mathsf T}Df}
=
\operatorname{cut}(S,\bar S)
\left(\frac1{v_S}+\frac1{v_{\bar S}}\right).
$$

Relaxation now yields the generalized eigenproblem.

For the example graph, compare two cuts:

| Subset | Cut weight | RatioCut | Normalized cut |
|---|---|---|---|
| $$\{1\}$$ | $$1$$ | $$4/3$$ | $$8/7$$ |
| $$\{1,2\}$$ | $$2$$ | $$2$$ | $$1$$ |

Counting nodes favors the first of these cuts; counting degree volume favors the second. The difference follows directly from the objectives.

Thresholding an eigenvector converts a continuous relaxation back into a discrete partition. It need not solve the original discrete problem exactly. These relationships are developed in the author's spectral-clustering tutorial. [Spectral-clustering derivations](https://www.cs.columbia.edu/~jebara/4772/papers/Luxburg07_tutorial.pdf)

## Revision checklist

| Check | What I should be able to reproduce |
|---|---|
| Sign convention | Relate the graph operator to the negative continuous second derivative. |
| Energy | Derive the edge-difference sum and its factor of one half. |
| Incidence form | Construct the Laplacian from oriented edge differences. |
| Worked graph | Verify the energy and diffusion step by direct arithmetic. |
| Nullspace | Prove that zero modes are constant on connected components. |
| Eigenvectors | Derive the constrained smoothness problem and distinguish modes from equilibria. |
| Normalization | Derive the generalized eigenproblem and coordinate change. |
| Random walk | Separate the constant right eigenvector from the stationary left distribution. |
| Convergence | Explain the two-node oscillation and the effect of laziness. |
| Capacity | Identify which weighted total a diffusion preserves. |
| Clustering | Derive RatioCut and normalized cut from two-valued vectors. |

## Why it matters for my work

A patient-similarity or anatomical graph specifies which differences count as disagreement. The Laplacian and its normalization then specify how those differences are measured and propagated. I need to justify both choices, rather than treating a graph-based result as independent of its similarity construction and node weighting.

## What I have not resolved

For a clinical graph, I have not established whether node count, degree volume, or another measure matches the intended notion of balance. Cluster interpretation also requires evidence beyond the existence of an eigenvector and a thresholded partition.
