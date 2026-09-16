---
layout: study_note
title: "Spectral Filtering: Why the Fourier Transform Is a Special Case"
description: "The analyse-scale-reconstruct template behind the word spectral, the fact that the Fourier basis is the eigenbasis of a ring graph's Laplacian, and what that licenses for graphs with no coordinates."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
subgroup: "Graph Signals & Spectral Methods"
order: 12
source: "Independent study"
written: true
updated: "2026-09-15"
---

A spectral filter analyzes a signal in an operator's eigenbasis, scales the resulting coordinates, and reconstructs the signal. For an undirected graph, a symmetric Laplacian supplies an orthonormal basis and a precise measure of variation across edges.

The Fourier basis is an eigenbasis of a cycle graph's Laplacian. That connection is exact, but it has a limitation: a scalar function of the undirected Laplacian cannot represent every directional circular filter. Repeated eigenvalues make that distinction unavoidable.

## From graph variation to spectral coordinates

Assume a finite undirected graph with symmetric nonnegative edge weights. Let

$$
L=D-A
$$

be its combinatorial Laplacian.

For a real node signal,

$$
x^{\mathsf T}Lx
=
\frac12\sum_{i,j}A_{ij}(x_i-x_j)^2.
$$

The expression is nonnegative and measures disagreement across weighted edges. Its derivation is given in the [graph Laplacian note](/study/the-graph-laplacian/).

Because the Laplacian is real symmetric, it has an orthonormal eigendecomposition:

$$
L=U\Lambda U^{\mathsf T},
\qquad
U^{\mathsf T}U=I.
$$

Write the signal in this basis:

$$
\widehat x=U^{\mathsf T}x,
\qquad
x=U\widehat x.
$$

Substitution into the variation measure gives

$$
\begin{aligned}
x^{\mathsf T}Lx
&=
\widehat x^{\mathsf T}
U^{\mathsf T}U\Lambda U^{\mathsf T}U
\widehat x\\
&=
\sum_k\lambda_k\widehat x_k^2.
\end{aligned}
$$

Likewise,

$$
\lVert x\rVert_2^2=\sum_k\widehat x_k^2.
$$

For equal coefficient energy, a component with larger eigenvalue contributes more edge disagreement. That is the mathematical reason for calling it a higher graph frequency.

This frequency is relative to the chosen graph and Laplacian. It is not automatically a physical frequency in hertz.

## What a scalar spectral filter means

Choose a scalar response function $$g$$. Define

$$
g(L)=U g(\Lambda)U^{\mathsf T},
$$

where

$$
g(\Lambda)
=
\operatorname{diag}
\bigl(g(\lambda_0),\ldots,g(\lambda_{N-1})\bigr).
$$

Filtering is

$$
y=g(L)x
=
U g(\Lambda)U^{\mathsf T}x.
$$

The three operations are explicit:

1. Project onto graph modes.
2. Multiply each coefficient by the response at that mode's eigenvalue.
3. Reconstruct in node coordinates.

If the response equals one everywhere on the spectrum,

$$
g(L)=UU^{\mathsf T}=I.
$$

The transform itself has therefore discarded nothing. Information is lost only if filtering removes components or if the representation is truncated.

For real gains, the output norm satisfies

$$
\lVert y\rVert_2^2
=
\sum_k g(\lambda_k)^2\widehat x_k^2.
$$

Hence

$$
\lVert g(L)x\rVert_2
\le
\left(\max_k\lvert g(\lambda_k)\rvert\right)
\lVert x\rVert_2.
$$

This gives an exact energy-gain bound for the fixed graph. A learned response whose magnitude exceeds one can amplify components; “spectral” does not imply smoothing.

## Deriving the Fourier eigenvectors of a cycle

Consider a simple cycle with at least three nodes, indexed periodically. Its Laplacian acts as

$$
(Lx)[n]
=
2x[n]-x[n-1]-x[n+1],
$$

with indices taken modulo $$N$$.

Test the normalized complex exponential

$$
u_k[n]=\frac1{\sqrt N}e^{j2\pi kn/N}.
$$

Its neighbors are scalar multiples:

$$
u_k[n-1]=e^{-j2\pi k/N}u_k[n],
$$

$$
u_k[n+1]=e^{j2\pi k/N}u_k[n].
$$

Therefore,

$$
\begin{aligned}
(Lu_k)[n]
&=
\left(
2-e^{-j2\pi k/N}-e^{j2\pi k/N}
\right)u_k[n]\\
&=
\left(
2-2\cos\frac{2\pi k}{N}
\right)u_k[n].
\end{aligned}
$$

Thus

$$
\lambda_k
=
2-2\cos\frac{2\pi k}{N}
=
4\sin^2\frac{\pi k}{N}.
$$

The finite geometric-sum identity from the [DFT note](/study/convolution-via-the-dft/) establishes orthonormality:

$$
\sum_{n=0}^{N-1}
\overline{u_k[n]}u_\ell[n]
=
\begin{cases}
1,&k=\ell,\\
0,&k\ne\ell.
\end{cases}
$$

For this complex basis, reconstruction uses the conjugate transpose:

$$
L=U\Lambda U^{\mathsf H}.
$$

The graph Fourier transform is the unitary DFT under the corresponding sign convention.

For small angular frequency,

$$
\lambda=4\sin^2(\omega/2)\approx\omega^2,
$$

because the leading term of the sine series is its argument. The Laplacian eigenvalue measures squared frequency near zero, consistent with a second-derivative operator.

## A four-node filtering example with every coefficient shown

For a four-node cycle,

$$
L=
\begin{bmatrix}
2&-1&0&-1\\
-1&2&-1&0\\
0&-1&2&-1\\
-1&0&-1&2
\end{bmatrix}.
$$

A real orthonormal eigenbasis is

$$
u_0=\frac12
\begin{bmatrix}1\\1\\1\\1\end{bmatrix},
\qquad
u_c=\frac1{\sqrt2}
\begin{bmatrix}1\\0\\-1\\0\end{bmatrix},
$$

$$
u_s=\frac1{\sqrt2}
\begin{bmatrix}0\\1\\0\\-1\end{bmatrix},
\qquad
u_\pi=\frac12
\begin{bmatrix}1\\-1\\1\\-1\end{bmatrix}.
$$

Their eigenvalues are

$$
0,\quad2,\quad2,\quad4.
$$

Take a unit impulse at the first node:

$$
x=
\begin{bmatrix}1\\0\\0\\0\end{bmatrix}.
$$

Its coefficients are

$$
\widehat x=
\begin{bmatrix}
\frac12\\
\frac1{\sqrt2}\\
0\\
\frac12
\end{bmatrix}.
$$

Their squared sum is

$$
\frac14+\frac12+\frac14=1,
$$

matching the input's squared norm.

Choose the response

$$
g(\lambda)=1-\frac{\lambda}{4}.
$$

The gains are

$$
1,\quad\frac12,\quad\frac12,\quad0.
$$

Reconstruction gives

$$
\begin{aligned}
y
&=
\frac12u_0+\frac1{2\sqrt2}u_c\\
&=
\begin{bmatrix}
\frac12\\
\frac14\\
0\\
\frac14
\end{bmatrix}.
\end{aligned}
$$

The same result follows without eigenvectors:

$$
g(L)=I-\frac14L=\frac12I+\frac14A.
$$

Half the impulse remains at its node, and one quarter reaches each neighbor. The opposite node is two edges away and receives nothing from this degree-one polynomial.

The original edge energy is two. The output's four edge differences have magnitudes one quarter, so

$$
y^{\mathsf T}Ly
=
4\left(\frac14\right)^2
=
\frac14.
$$

The spectral calculation agrees:

$$
\sum_k\lambda_k\widehat y_k^2
=
2\left(\frac1{2\sqrt2}\right)^2
=
\frac14.
$$

This checks the interpretation of graph frequency against direct edge arithmetic.

## A low-pass response derived from an optimization problem

Suppose the task is to remain close to observed values while penalizing edge disagreement:

$$
\min_z
\left[
\frac12\lVert z-x\rVert_2^2
+
\frac{\tau}{2}z^{\mathsf T}Lz
\right],
\qquad \tau\ge0.
$$

Differentiate with respect to the candidate signal:

$$
z-x+\tau Lz=0.
$$

Therefore,

$$
z=(I+\tau L)^{-1}x.
$$

Since the eigenvalues of the matrix being inverted are

$$
1+\tau\lambda_k>0,
$$

the solution is unique. In spectral coordinates,

$$
\widehat z_k
=
\frac{1}{1+\tau\lambda_k}\widehat x_k.
$$

Thus the optimization problem derives the low-pass response

$$
g(\lambda)=\frac{1}{1+\tau\lambda}.
$$

Large-variation modes are penalized more strongly. The constant mode is preserved because its eigenvalue is zero.

For the four-node example, choose

$$
\tau=\frac12.
$$

The gains become

$$
1,\quad\frac12,\quad\frac12,\quad\frac13.
$$

Applying them to the same impulse gives

$$
z=
\begin{bmatrix}
\frac7{12}\\
\frac16\\
\frac1{12}\\
\frac16
\end{bmatrix}.
$$

Unlike the degree-one filter, this response reaches the opposite node. An inverse matrix is generally dense even when the original Laplacian is sparse.

The prior is visible in the objective: neighboring nodes are encouraged to have similar output values. Whether that is appropriate depends on what an edge means.

## Diffusion gives another response function

Consider graph heat flow:

$$
\frac{dx(t)}{dt}=-Lx(t).
$$

Project into the eigenbasis:

$$
\frac{d\widehat x_k(t)}{dt}
=
-\lambda_k\widehat x_k(t).
$$

Each coordinate solves an independent first-order equation:

$$
\widehat x_k(t)
=
e^{-t\lambda_k}\widehat x_k(0).
$$

Therefore,

$$
x(t)=Ue^{-t\Lambda}U^{\mathsf T}x(0).
$$

The heat response is

$$
g_t(\lambda)=e^{-t\lambda}.
$$

This is a low-pass filter because larger eigenvalues decay faster. It also makes clear that nonzero-eigenvalue modes are decaying modes, not equilibrium states.

A finite-time heat filter is generally not strictly local. Its series contains powers of every order:

$$
e^{-tL}
=
I-tL+\frac{t^2L^2}{2!}-\cdots.
$$

Sparse edges define how influence propagates, but they do not imply that every function of a sparse Laplacian has finite spatial support.

## Why not every circular filter is a function of the Laplacian

The cycle spectrum satisfies

$$
\lambda_k=\lambda_{N-k}.
$$

Positive and negative angular frequencies therefore share a Laplacian eigenvalue. Any scalar response must assign them the same gain:

$$
g(\lambda_k)=g(\lambda_{N-k}).
$$

Now consider a one-sample circular delay:

$$
(Sx)[n]=x[n-1].
$$

Its Fourier multiplier is

$$
e^{-j2\pi k/N}.
$$

For the four-node cycle, the two modes with eigenvalue two receive multipliers

$$
-j
\quad\text{and}\quad
j.
$$

One scalar value at eigenvalue two cannot equal both. Thus

$$
S\ne g(L)
$$

for any scalar function of this undirected cycle Laplacian.

The Fourier basis diagonalizes all circular convolutions. Scalar Laplacian filters form a restricted family within those operators, treating the paired directions alike.

Even commutation with the Laplacian is insufficient to imply that an operator is a scalar function of it. Within a repeated eigenspace, an operator can act nontrivially while still commuting with the Laplacian, which acts there as a scalar multiple of the identity.

This is the precise limitation behind the Fourier analogy. Directional filtering requires additional structure beyond an undirected scalar Laplacian response.

## Eigenvector ambiguity and basis-independent filtering

An eigenvector can be negated without changing its eigenvalue. For a repeated eigenvalue, any orthonormal rotation within the eigenspace is also valid.

Suppose a repeated eigenspace has basis matrix $$U_E$$, and replace it by

$$
U_E'=U_EQ,
\qquad
Q^{\mathsf T}Q=I.
$$

If the filter uses one scalar gain throughout that eigenspace, its contribution is unchanged:

$$
U_EQ\bigl(g(\lambda)I\bigr)Q^{\mathsf T}U_E^{\mathsf T}
=
g(\lambda)U_EU_E^{\mathsf T}.
$$

The projector is invariant even though the individual eigenvectors are not.

Arbitrary separate gains inside a repeated eigenspace do not have this property. On the four-node cycle, projecting onto $$u_c$$ alone maps the first-node impulse to

$$
u_cu_c^{\mathsf T}x
=
\begin{bmatrix}
\frac12\\0\\-\frac12\\0
\end{bmatrix}.
$$

Rotate the chosen eigenvector to

$$
v=\frac{u_c+u_s}{\sqrt2}
=
\frac12
\begin{bmatrix}1\\1\\-1\\-1\end{bmatrix}.
$$

Projecting onto this equally valid eigenvector gives

$$
vv^{\mathsf T}x
=
\frac14
\begin{bmatrix}1\\1\\-1\\-1\end{bmatrix}.
$$

The graph and repeated eigenvalue are unchanged, but the operator differs. A per-eigenvector parameterization therefore needs a basis convention or a design that respects eigenspace ambiguity.

## Polynomial filters and the proof of locality

Choose a polynomial response,

$$
g(\lambda)=\sum_{r=0}^{K}\theta_r\lambda^r.
$$

Using orthonormality repeatedly,

$$
L^r=U\Lambda^rU^{\mathsf T}.
$$

Hence

$$
g(L)x=\sum_{r=0}^{K}\theta_rL^r x.
$$

No eigenvectors are needed to evaluate this expression.

To understand locality, expand a matrix-power entry:

$$
(L^r)_{ij}
=
\sum_{v_1,\ldots,v_{r-1}}
L_{iv_1}L_{v_1v_2}\cdots L_{v_{r-1}j}.
$$

A nonzero factor either stays at a node through a diagonal entry or crosses an edge through an off-diagonal entry. A product of $$r$$ factors cannot connect nodes more than $$r$$ edges apart.

Therefore,

$$
\operatorname{dist}(i,j)>K
\quad\Longrightarrow\quad
g(L)_{ij}=0.
$$

This is an exact support result for polynomial filters.

Repeated sparse matrix–vector products evaluate the filter with cost proportional to

$$
K(N+\lvert E\rvert)
$$

for one scalar feature, up to implementation constants. Explicitly forming dense powers would throw away that advantage.

The localized polynomial construction is the basis of Chebyshev graph filtering. [Original localized-filter formulation](https://arxiv.org/abs/1606.09375)

## Why Chebyshev polynomials are convenient

Define Chebyshev polynomials through

$$
T_r(\cos\theta)=\cos(r\theta).
$$

The cosine addition identity gives

$$
T_{r+1}(s)=2sT_r(s)-T_{r-1}(s),
$$

starting from

$$
T_0(s)=1,
\qquad
T_1(s)=s.
$$

Choose an upper bound on the largest Laplacian eigenvalue,

$$
\bar\lambda\ge\lambda_{\max}>0,
$$

and rescale:

$$
\widetilde L=\frac{2}{\bar\lambda}L-I.
$$

Its spectrum lies inside the interval from negative one to one.

A degree-$$K$$ filter can be represented as

$$
g(L)x=
\sum_{r=0}^{K}\theta_rT_r(\widetilde L)x.
$$

Compute the vectors recursively:

$$
v_0=x,
\qquad
v_1=\widetilde Lx,
$$

$$
v_{r+1}=2\widetilde Lv_r-v_{r-1}.
$$

Then combine them with the learned coefficients.

The recurrence avoids an eigendecomposition and avoids constructing matrix powers. Since each term remains a polynomial of the corresponding degree, the same locality proof applies.

A learned polynomial need not be low-pass. Its coefficients can produce amplification, suppression, or sign changes anywhere on the graph spectrum.

## From a first-order spectral expression to a GCN layer

For the symmetric normalized Laplacian, write

$$
L_{\mathrm{sym}}=I-S,
\qquad
S=D^{-1/2}AD^{-1/2}.
$$

Using the spectral bound two as the scaling value, a first-order Chebyshev expression becomes

$$
\theta_0I+\theta_1(L_{\mathrm{sym}}-I)
=
\theta_0I-\theta_1S.
$$

Tying parameters as

$$
\theta_0=-\theta_1=\theta
$$

gives

$$
\theta(I+S).
$$

A common GCN then adds self-loops and renormalizes:

$$
\widehat A=A+I,
\qquad
\widehat D_{ii}=\sum_j\widehat A_{ij},
$$

$$
\widehat S=
\widehat D^{-1/2}\widehat A\widehat D^{-1/2}.
$$

Its layer has the form

$$
H^{(\ell+1)}
=
\sigma\left(
\widehat S H^{(\ell)}W^{(\ell)}
\right).
$$

This is a modeling construction motivated by first-order filtering. Replacing the earlier matrix by the self-loop normalized matrix is not an algebraic identity. [Original GCN formulation](https://arxiv.org/abs/1609.02907)

For a regular graph of degree $$d$$,

$$
I+S=I+\frac1dA,
$$

whereas

$$
\widehat S=\frac{A+I}{d+1}.
$$

Even these simple formulas give different self-to-neighbor weight ratios.

At a node, the linear aggregation is

$$
(\widehat SH)_i
=
\sum_j
\frac{\widehat A_{ij}}
{\sqrt{\widehat d_i\widehat d_j}}
H_j.
$$

Feature mixing and nonlinear activation then follow. Once nonlinearities are included, the whole network is not one fixed diagonal spectral multiplier.

## Permutation equivariance and repeated smoothing

Relabel nodes with a permutation matrix $$P$$:

$$
L'=PLP^{\mathsf T},
\qquad
x'=Px.
$$

For a polynomial filter,

$$
(L')^r=PL^rP^{\mathsf T},
$$

so

$$
g(L')x'=Pg(L)x.
$$

The output changes only by the same relabeling. This is permutation equivariance, the appropriate consistency property when node numbering is arbitrary.

Repeated fixed linear smoothing can also be read spectrally. If a symmetric propagation matrix has eigenvalues $$\mu_k$$, then

$$
S^\ell x
=
U\operatorname{diag}(\mu_k^\ell)U^{\mathsf T}x.
$$

Components with magnitude below one decay under repetition. If exactly one mode has eigenvalue one and all others have smaller magnitude, only that mode survives in the limit.

For symmetric normalized propagation, the surviving mode is generally proportional to square-root degree, not an unweighted constant vector. Actual networks with learned weights, residual paths, and nonlinearities require additional analysis; the linear limit identifies a mechanism rather than proving every network must behave identically.

## Revision checklist

| Check | What I should be able to reproduce |
|---|---|
| Graph frequency | Express edge energy as an eigenvalue-weighted coefficient sum. |
| Cycle connection | Apply the cycle Laplacian to a complex exponential. |
| Worked filter | Obtain the four-node output both spectrally and by neighbor averaging. |
| Regularization | Derive the resolvent response from a quadratic objective. |
| Diffusion | Solve the independent modal differential equations. |
| Directionality | Show why a circular delay is not a scalar function of the cycle Laplacian. |
| Repeated eigenvalues | Distinguish invariant eigenspace projectors from arbitrary basis choices. |
| Locality | Derive the hop limit from products of sparse matrix entries. |
| Chebyshev evaluation | Obtain the recurrence from the cosine identity. |
| GCN construction | Separate first-order motivation, parameter tying, and renormalization. |
| Equivariance | Prove that relabeling commutes with filtering in the appropriate sense. |

## Why it matters for my work

A graph filter makes an assumption about which node differences should be suppressed. For patient, sensor, or anatomical graphs, that assumption must be justified by the edge construction and task. Polynomial locality and permutation equivariance are useful guarantees, but neither establishes that smoothing preserves the clinically relevant signal.

## What I have not resolved

I still need a task-specific reason to choose a graph, a Laplacian normalization, and a spectral response. Directional information and sharp local abnormalities may require operators beyond a scalar undirected Laplacian filter.
