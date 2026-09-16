---
layout: study_note
title: "Matrix Calculus for Reading Papers: Determinants, Cofactors, and the Gaussian MLE"
description: "Matrix differentiation through determinants, cofactors, log determinants and inverses, followed by a complete derivation of Gaussian mean and covariance maximum-likelihood estimators."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "algebra-and-optimisation"
category_title: "Linear Algebra & Optimisation"
order: 2
source: "Independent study"
written: true
updated: "2026-09-15"
---

Matrix calculus becomes manageable when every derivative is treated as a linear description of a small perturbation. The essential task is to express the first-order change in a scalar objective as an inner product with the perturbation.

This note fixes that convention, derives the identities needed for Gaussian maximum likelihood, and checks them on small examples. Shape, symmetry, invertibility, and positive definiteness are part of each result.

## The gradient is defined by the differential

For a real matrix and a scalar-valued differentiable function, define the gradient entrywise:

$$
(\nabla_A f)_{ij}
=
\frac{\partial f}{\partial a_{ij}}.
$$

It has the same shape as the matrix.

The first-order expansion is

$$
f(A+H)
=
f(A)+\sum_{i,j}(\nabla_A f)_{ij}H_{ij}
+o(\lVert H\rVert).
$$

The Frobenius inner product writes the sum compactly:

$$
\langle G,H\rangle_F
=
\operatorname{tr}(G^{\mathsf T}H)
=
\sum_{i,j}G_{ij}H_{ij}.
$$

Thus

$$
df=\operatorname{tr}\left((\nabla_A f)^{\mathsf T}dA\right).
$$

This is both a definition and a method:

1. Differentiate the scalar expression.
2. Collect all first-order terms.
3. Rearrange them into a trace containing the matrix perturbation.
4. Read off the coefficient using the fixed transpose convention.

For a column vector, the corresponding convention is

$$
df=(\nabla_x f)^{\mathsf T}dx.
$$

A gradient descent update subtracts this gradient. A plus sign represents ascent under this convention; changing a transpose convention does not reverse the direction of optimisation.

The differential is a linear map applied to a perturbation. The gradient represents that map under the chosen inner product. Keeping those ideas separate helps when a paper uses a different matrix layout or a non-Euclidean parameterisation.

## Trace identities are bookkeeping, not commutativity

For compatible matrices,

$$
\operatorname{tr}(AB)=\operatorname{tr}(BA).
$$

Expanding entries proves it:

$$
\operatorname{tr}(AB)
=
\sum_i\sum_j A_{ij}B_{ji}
=
\sum_j\sum_i B_{ji}A_{ij}
=
\operatorname{tr}(BA).
$$

More generally, cyclic rotations preserve a product's trace:

$$
\operatorname{tr}(ABC)
=
\operatorname{tr}(BCA)
=
\operatorname{tr}(CAB).
$$

Arbitrary rearrangements do not. The products themselves generally do not commute.

For a fixed compatible matrix,

$$
df=d\,\operatorname{tr}(WA)=\operatorname{tr}(W\,dA),
$$

so

$$
\nabla_A\operatorname{tr}(WA)=W^{\mathsf T}.
$$

By contrast,

$$
\nabla_A\operatorname{tr}(W^{\mathsf T}A)=W.
$$

The transpose is determined by the entrywise definition. It is not a decoration that can be added after checking dimensions.

The product rule follows directly from perturbation:

$$
(A+dA)(B+dB)
=
AB+(dA)B+A(dB)+(dA)(dB).
$$

Discarding the second-order term gives

$$
d(AB)=(dA)B+A(dB).
$$

The order of factors remains unchanged.

## Quadratic forms and least squares

For a fixed square matrix,

$$
f(x)=x^{\mathsf T}Ax.
$$

Differentiating both occurrences of the vector gives

$$
df=(dx)^{\mathsf T}Ax+x^{\mathsf T}A\,dx.
$$

The first term is a scalar, so transpose it:

$$
(dx)^{\mathsf T}Ax=x^{\mathsf T}A^{\mathsf T}dx.
$$

Hence

$$
df=x^{\mathsf T}(A^{\mathsf T}+A)\,dx,
$$

and

$$
\nabla_xf=(A+A^{\mathsf T})x.
$$

Only when the matrix is symmetric does this reduce to

$$
2Ax.
$$

If instead the vector is fixed and the matrix varies,

$$
df=x^{\mathsf T}(dA)x
=
\operatorname{tr}(xx^{\mathsf T}dA),
$$

so

$$
\nabla_A(x^{\mathsf T}Ax)=xx^{\mathsf T}.
$$

The same expression has different derivatives depending on which object is variable.

Now let

$$
F(W)=\frac12\lVert AW-B\rVert_F^2.
$$

Define the residual matrix

$$
R=AW-B.
$$

Because

$$
F=\frac12\operatorname{tr}(R^{\mathsf T}R),
$$

the product rule and equality of a trace with its transpose give

$$
dF=\operatorname{tr}(R^{\mathsf T}dR).
$$

Since the design matrix is fixed,

$$
dR=A\,dW.
$$

Therefore

$$
dF
=
\operatorname{tr}(R^{\mathsf T}A\,dW)
=
\operatorname{tr}\left((A^{\mathsf T}R)^{\mathsf T}dW\right),
$$

and

$$
\nabla_WF=A^{\mathsf T}(AW-B).
$$

The shape also checks: the result has the same number of rows and columns as the parameter matrix.

For a numerical example, use

$$
A=
\begin{pmatrix}1&2\\0&1\end{pmatrix},
\qquad
w=
\begin{pmatrix}1\\-1\end{pmatrix},
\qquad
b=
\begin{pmatrix}0\\1\end{pmatrix}.
$$

The residual and gradient are

$$
Aw-b=
\begin{pmatrix}-1\\-2\end{pmatrix},
\qquad
\nabla_wF=
\begin{pmatrix}-1\\-4\end{pmatrix}.
$$

Perturb only the second coefficient by a scalar step. Direct substitution gives

$$
F(w+he_2)
=
\frac12\left[(-1+2h)^2+(-2+h)^2\right]
=
\frac52-4h+\frac52h^2.
$$

The coefficient of the first-order term is negative four, exactly the second gradient entry.

## Cofactors explain the determinant derivative

The minor associated with an entry is the determinant remaining after deleting its row and column. Its cofactor is

$$
C_{ij}=(-1)^{i+j}M_{ij}.
$$

Expanding along a chosen row gives

$$
\det A=\sum_j a_{ij}C_{ij}.
$$

Every cofactor in that expansion excludes the chosen row. Differentiating with respect to an entry in that row therefore leaves

$$
\frac{\partial\det A}{\partial a_{ij}}=C_{ij}.
$$

Collecting these entries,

$$
\nabla_A\det A=C.
$$

The adjugate is the transpose of the cofactor matrix:

$$
\operatorname{adj}(A)=C^{\mathsf T}.
$$

Why does it produce the inverse? The diagonal entries of

$$
A\operatorname{adj}(A)
$$

are ordinary cofactor expansions of the determinant. An off-diagonal entry is the corresponding expansion of a matrix with one row replaced by another existing row. Such a matrix has repeated rows and determinant zero. Hence

$$
A\operatorname{adj}(A)=(\det A)I.
$$

For an invertible matrix,

$$
A^{-1}=\frac{\operatorname{adj}(A)}{\det A},
$$

so

$$
\nabla_A\det A
=
(\det A)A^{-\mathsf T}.
$$

The cofactor derivative exists even at singular matrices. The expression using an inverse does not. A singular determinant does not make the determinant function non-differentiable; it makes this particular representation unavailable.

Cofactor expansions are useful for derivation and small checks. Large numerical determinant and inverse computations should use appropriate factorizations rather than recursive expansion.

## The log determinant and a check that detects a transpose error

For a real logarithm, assume the determinant is positive. The scalar chain rule gives

$$
d\log\det A
=
\frac{d\det A}{\det A}
=
\operatorname{tr}(A^{-1}dA).
$$

Thus

$$
\nabla_A\log\det A=A^{-\mathsf T}.
$$

Covariance applications impose the stronger condition of symmetry and positive definiteness, which guarantees a positive determinant.

Use the non-symmetric matrix

$$
A=
\begin{pmatrix}2&1\\0&3\end{pmatrix}.
$$

Its determinant and cofactor matrix are

$$
\det A=6,
\qquad
C=
\begin{pmatrix}3&0\\-1&2\end{pmatrix}.
$$

Now perturb the lower-left entry:

$$
A(t)=
\begin{pmatrix}2&1\\t&3\end{pmatrix}.
$$

Directly,

$$
\det A(t)=6-t.
$$

Therefore the determinant derivative in this direction is negative one and the log-determinant derivative at zero is

$$
-\frac16.
$$

The matrix formula gives

$$
A^{-\mathsf T}
=
\begin{pmatrix}
1/2&0\\
-1/6&1/3
\end{pmatrix},
$$

whose lower-left entry agrees.

At the constructed step

$$
t=0.06,
$$

the exact log change is

$$
\log\frac{5.94}{6}
=
\log(0.99)
\approx -0.01005034.
$$

The linear prediction is

$$
-\frac16(0.06)=-0.01.
$$

Using the untransposed inverse as the gradient would incorrectly predict zero in this direction. Symmetric test matrices would conceal that error, which is why a non-symmetric check is useful.

## Differentiating an inverse without guessing

Start from the identity

$$
AA^{-1}=I.
$$

Differentiate using the product rule:

$$
(dA)A^{-1}+A\,d(A^{-1})=0.
$$

Multiplying on the left by the inverse gives

$$
d(A^{-1})=-A^{-1}(dA)A^{-1}.
$$

Equivalently, for a sufficiently small perturbation,

$$
(A+H)^{-1}
=
A^{-1}-A^{-1}HA^{-1}
+
O(\lVert H\rVert^2).
$$

The two surrounding inverses are essential. The scalar rule cannot be applied entrywise to a matrix.

For a fixed vector, consider

$$
f(A)=x^{\mathsf T}A^{-1}x.
$$

The inverse differential gives

$$
df
=
-x^{\mathsf T}A^{-1}(dA)A^{-1}x.
$$

Move the fixed factors into a trace:

$$
df
=
-\operatorname{tr}
\left(A^{-1}xx^{\mathsf T}A^{-1}dA\right).
$$

Reading off the gradient yields

$$
\nabla_Af
=
-A^{-\mathsf T}xx^{\mathsf T}A^{-\mathsf T}.
$$

For a symmetric matrix this simplifies to

$$
-A^{-1}xx^{\mathsf T}A^{-1}.
$$

That simplified form should not be used for arbitrary non-symmetric matrices.

The same small matrix provides an exact check. With

$$
x=
\begin{pmatrix}1\\1\end{pmatrix},
$$

direct inversion gives

$$
x^{\mathsf T}A(t)^{-1}x
=
\frac{4-t}{6-t}.
$$

Its derivative at zero is

$$
\frac{-6+4}{36}=-\frac1{18}.
$$

For the matrix-gradient formula,

$$
A^{-1}x=
\begin{pmatrix}1/3\\1/3\end{pmatrix},
\qquad
A^{-\mathsf T}x=
\begin{pmatrix}1/2\\1/6\end{pmatrix},
$$

so

$$
\nabla_Af
=
-
\begin{pmatrix}1/2\\1/6\end{pmatrix}
\begin{pmatrix}1/3&1/3\end{pmatrix}.
$$

Its lower-left entry is negative one eighteenth, as required.

## Symmetric variables have a restricted perturbation space

A covariance matrix is symmetric. Its admissible perturbations are symmetric too.

If an ambient calculation gives a gradient matrix, then for symmetric perturbations,

$$
\operatorname{tr}(G^{\mathsf T}dA)
=
\operatorname{tr}
\left[
\left(\frac{G+G^{\mathsf T}}2\right)^{\mathsf T}dA
\right].
$$

The skew-symmetric part contributes zero. Under the Frobenius inner product, the gradient on the symmetric-matrix space is therefore

$$
\operatorname{sym}(G)=\frac{G+G^{\mathsf T}}2.
$$

A different coordinate description uses one parameter for each distinct off-diagonal entry. If a scalar parameter changes both symmetric positions, its derivative is

$$
\frac{\partial f}{\partial a_{ij}}
+
\frac{\partial f}{\partial a_{ji}}.
$$

For a symmetric ambient gradient, this is twice one off-diagonal entry. This factor comes from the coordinate map; it does not contradict the matrix differential.

Positive-definite matrices form an open subset of the symmetric-matrix space. At an interior point, all sufficiently small symmetric perturbations remain allowed. This makes ordinary differential stationarity legitimate there. It does not allow a singular stationary candidate to be called an interior covariance estimate.

The distinction becomes decisive in the Gaussian likelihood problem.

## Why Gaussian likelihood contains an inverse and a log determinant

Let a standard normal vector have independent coordinates and density

$$
p_Z(z)
=
(2\pi)^{-d/2}
\exp\left(-\frac12z^{\mathsf T}z\right).
$$

Construct

$$
X=\mu+LZ,
\qquad
\Sigma=LL^{\mathsf T},
$$

with an invertible factor. Then

$$
z=L^{-1}(x-\mu),
$$

and

$$
z^{\mathsf T}z
=
(x-\mu)^{\mathsf T}\Sigma^{-1}(x-\mu).
$$

The change-of-variables Jacobian contributes

$$
\frac1{\lvert\det L\rvert}
=
\frac1{\sqrt{\det\Sigma}}.
$$

Thus

$$
p(x\mid\mu,\Sigma)
=
(2\pi)^{-d/2}
(\det\Sigma)^{-1/2}
\exp\left[
-\frac12(x-\mu)^{\mathsf T}\Sigma^{-1}(x-\mu)
\right].
$$

The inverse measures distance after accounting for covariance. The determinant accounts for the volume expansion of the transformation. Both terms are necessary: reducing covariance raises the density normalisation but also increases penalties for deviations.

For independent observations, the joint density is a product. Taking logarithms and dropping the constant independent of the parameters gives

$$
\ell(\mu,\Sigma)
=
-\frac N2\log\det\Sigma
-
\frac12\sum_{i=1}^N
(x_i-\mu)^{\mathsf T}\Sigma^{-1}(x_i-\mu).
$$

## Deriving the mean and covariance estimators

For fixed positive-definite covariance, differentiate in the mean:

$$
\nabla_\mu\ell
=
\sum_i\Sigma^{-1}(x_i-\mu).
$$

The positive sign follows because differentiating the residual introduces a minus sign, which cancels the likelihood's negative quadratic sign.

Stationarity gives

$$
\Sigma^{-1}
\left(\sum_i x_i-N\mu\right)=0.
$$

Invertibility yields

$$
\widehat\mu=\bar x=\frac1N\sum_i x_i.
$$

This is also a global optimum in the mean. The residual cross-product identity is

$$
\sum_i(x_i-\mu)(x_i-\mu)^{\mathsf T}
=
S+N(\mu-\bar x)(\mu-\bar x)^{\mathsf T},
$$

where

$$
S=\sum_i(x_i-\bar x)(x_i-\bar x)^{\mathsf T}.
$$

The cross terms vanish because centred observations sum to zero. The additional quadratic contribution to negative log-likelihood is non-negative and vanishes only at the sample mean.

Now hold the mean at that value. Since

$$
\sum_i
(x_i-\bar x)^{\mathsf T}\Sigma^{-1}(x_i-\bar x)
=
\operatorname{tr}(\Sigma^{-1}S),
$$

the covariance gradient is

$$
\nabla_\Sigma\ell
=
-\frac N2\Sigma^{-1}
+
\frac12\Sigma^{-1}S\Sigma^{-1}.
$$

All matrices here are symmetric where required. Set this equal to zero and multiply on the left and right by the covariance:

$$
-N\Sigma+S=0.
$$

The candidate is

$$
\widehat\Sigma=\frac SN.
$$

Obtaining a stationary formula is not the end. We must check that it is positive definite and that it maximises the likelihood.

## Proving maximality and identifying when the MLE does not exist

Use the precision matrix

$$
\Omega=\Sigma^{-1}.
$$

The profile log-likelihood becomes

$$
\ell(\Omega)
=
\frac N2\log\det\Omega
-
\frac12\operatorname{tr}(\Omega S).
$$

For a symmetric direction, differentiate the log determinant a second time:

$$
d^2\log\det\Omega[H,H]
=
-\operatorname{tr}(\Omega^{-1}H\Omega^{-1}H).
$$

Write the trace as

$$
-\left\lVert
\Omega^{-1/2}H\Omega^{-1/2}
\right\rVert_F^2.
$$

It is strictly negative for a non-zero symmetric direction. Thus the log determinant is strictly concave on positive-definite matrices, while the trace term is linear.

The stationary point is therefore the unique global maximum when it exists:

$$
\frac N2\Omega^{-1}-\frac12S=0,
$$

so

$$
\Omega=NS^{-1},
\qquad
\Sigma=\frac SN.
$$

Existence requires positive-definite scatter. Its rank obeys

$$
\operatorname{rank}(S)\le\min(d,N-1),
$$

because the centred observations sum to zero. Having more observations than dimensions is necessary for full rank, but not sufficient if observations lie in a lower-dimensional affine subspace.

If scatter is singular, there is a direction with no observed centred variation. Shrink the covariance eigenvalue in that direction toward zero while keeping the other directions fixed. The quadratic term in that direction remains zero, while the log-determinant term sends log-likelihood upward without bound:

$$
-\frac N2\log\varepsilon\longrightarrow+\infty
\qquad\text{as }\varepsilon\downarrow 0.
$$

There is then no finite maximiser over positive-definite covariance matrices. The singular sample covariance is not an admissible interior MLE for that model.

Adding a ridge, using a prior, or imposing covariance structure creates a different estimation problem. Such changes can be sensible, but they should be named.

## A covariance example and the source of its bias

Use four observations:

$$
(0,0),\quad(2,0),\quad(0,2),\quad(2,2).
$$

The mean is

$$
\bar x=(1,1)^{\mathsf T}.
$$

The centred vectors have coordinates equal to positive or negative one. Their outer products sum to

$$
S=
\begin{pmatrix}4&0\\0&4\end{pmatrix}.
$$

Therefore

$$
\widehat\Sigma=I.
$$

Ignoring the same additive constant in every comparison, the log-likelihood at this covariance is

$$
\ell(I)=-\frac12\operatorname{tr}(4I)=-4.
$$

For twice the identity,

$$
\ell(2I)
=
-4\log 2-2
\approx -4.77259.
$$

For half the identity,

$$
\ell(I/2)
=
4\log 2-8
\approx -5.22741.
$$

Both have lower likelihood, consistent with the global argument.

Why does the MLE divide by the observation count while an unbiased covariance estimate uses one less? Let the true mean and covariance be fixed. The identity

$$
S
=
\sum_i(x_i-\mu)(x_i-\mu)^{\mathsf T}
-
N(\bar x-\mu)(\bar x-\mu)^{\mathsf T}
$$

gives, under independent sampling,

$$
\mathbb E[S]
=
N\Sigma-N\frac{\Sigma}{N}
=
(N-1)\Sigma.
$$

Hence

$$
\mathbb E[\widehat\Sigma]
=
\frac{N-1}{N}\Sigma.
$$

Dividing scatter by one less than the sample count removes this expectation bias. It does not maximise the same likelihood. Maximum likelihood and unbiasedness are different criteria.

## Differentiating a solve instead of materialising a Jacobian

Suppose a vector is defined implicitly by

$$
Ax=b.
$$

Differentiating gives

$$
(dA)x+A\,dx=db,
$$

hence

$$
dx=A^{-1}(db-(dA)x).
$$

Let a scalar objective have vector gradient

$$
r=\nabla_xf.
$$

Solve the transposed system

$$
A^{\mathsf T}u=r.
$$

Then

$$
df=r^{\mathsf T}dx
=
u^{\mathsf T}db-u^{\mathsf T}(dA)x.
$$

Therefore

$$
\nabla_bf=u,
\qquad
\nabla_Af=-ux^{\mathsf T}.
$$

The backward calculation needs a linear solve and an outer product, not a huge tensor containing every entry of the inverse's derivative.

For any proposed matrix gradient, a useful directional check is

$$
\frac{f(A+hH)-f(A-hH)}{2h}
\longrightarrow
\operatorname{tr}\left((\nabla_Af)^{\mathsf T}H\right).
$$

Choose perturbations that respect the domain. For a covariance, use symmetric directions and steps small enough to preserve positive definiteness. Exact small examples, such as those above, also reveal errors without depending on floating-point tolerances.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| State the gradient convention | Write the Frobenius differential |
| Move factors inside a trace correctly | Use cyclic rotations rather than arbitrary swaps |
| Differentiate a quadratic form | Keep both occurrences of the vector |
| Derive a least-squares gradient | Check its dimensions |
| Derive the determinant gradient | Use cofactors before introducing an inverse |
| Explain the transpose in a log-determinant gradient | Verify a non-symmetric example |
| Differentiate an inverse | Start from the identity product |
| Handle symmetric parameters | Distinguish matrix gradients from distinct-entry coordinates |
| Derive Gaussian MLEs | Include the Jacobian, mean, and covariance steps |
| Prove the covariance candidate is maximal | Use concavity in the precision matrix |
| Recognise a nonexistent positive-definite MLE | Check the scatter rank |
| Explain the covariance denominator | Derive the expected scatter |
| Differentiate through a solve | Use an adjoint linear system |

## Why it matters for my work

These identities let me inspect Gaussian objectives, covariance regularisation, and differentiable linear algebra without treating them as black boxes. The most useful checks are often domain checks: whether an inverse exists and whether a claimed covariance estimate is admissible.

## What I have not resolved

I need to compare covariance restrictions and regularisation choices for the representation dimensions and sample sizes in my experiments. The unconstrained MLE derivation identifies the failure mode but does not choose its replacement.
