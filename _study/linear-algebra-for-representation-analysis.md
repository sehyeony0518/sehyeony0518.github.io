---
layout: study_note
title: "Linear Algebra for Representation Analysis"
description: "Eigenvalues, SVD, projection, and PCA as the working tools for asking what a learned representation contains."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "algebra-and-optimization"
category_title: "Linear Algebra & Optimization"
subgroup: "Linear Algebra & Geometry"
order: 1
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-07-02-weight-space-correlation-analysis"
---

A representation matrix contains two linked kinds of structure: directions in feature space and patterns across observations. Singular value decomposition, or SVD, connects them. From that connection, covariance eigenvalues, principal components, projection, reconstruction error, and several notions of effective rank follow.

The central question is precise: **along which feature directions do the observed representations vary, and how much variation belongs to each direction?** This is a question about the sampled matrix. Interpreting the directions as clinical information requires additional evidence.

## Constructing the matrix and choosing its origin

Let a dataset contain feature vectors arranged as rows:

$$
A=
\begin{bmatrix}
a_1^\top\\
\vdots\\
a_n^\top
\end{bmatrix}
\in\mathbb R^{n\times d}.
$$

Each observation has a feature vector in a space of dimension $$d$$. An observation might mean a frame, an examination, or a patient. That choice determines which observations receive weight in every subsequent calculation.

Define the sample mean and centered matrix by

$$
\bar a=\frac1n\sum_{i=1}^n a_i,
\qquad
X=A-\mathbf1\bar a^\top.
$$

Consequently,

$$
\mathbf1^\top X=0.
$$

The rows of the centered matrix therefore satisfy a linear dependence. Its rank obeys

$$
\operatorname{rank}(X)\leq \min(n-1,d).
$$

This matters when interpreting apparent dimensional collapse. With fewer observations than features, a centered representation matrix cannot have full feature rank, even if the underlying population varies in every feature direction.

Centering changes the question. To see this, substitute the decomposition of the raw matrix:

$$
A^\top A
=
(X+\mathbf1\bar a^\top)^\top
(X+\mathbf1\bar a^\top)
=
X^\top X+n\bar a\bar a^\top.
$$

The cross terms vanish because the centered columns sum to zero. Thus, an uncentered spectrum includes a contribution from the mean representation. A large leading singular value may describe a common offset rather than variation between observations.

Standardization is a further choice. Dividing each column by its sample standard deviation gives low-amplitude and high-amplitude coordinates comparable numerical influence. It does not merely improve the computation: it changes the matrix and the geometry being studied.

## Deriving the SVD from feature directions

Consider a unit feature direction:

$$
v\in\mathbb R^d,
\qquad
\lVert v\rVert_2=1.
$$

Projecting every observation onto it produces the score vector

$$
Xv=
\begin{bmatrix}
x_1^\top v\\
\vdots\\
x_n^\top v
\end{bmatrix}.
$$

The total squared score is

$$
\lVert Xv\rVert_2^2
=
v^\top X^\top Xv.
$$

Define

$$
M=X^\top X.
$$

This matrix is symmetric and positive semidefinite:

$$
M^\top=M,
\qquad
v^\top Mv=\lVert Xv\rVert_2^2\geq0.
$$

Why can its eigenvectors supply an orthonormal coordinate system? One way to understand the spectral theorem is to maximize the quadratic form on the unit sphere. A maximizer exists because the sphere is compact. At a maximizing vector, movement in any perpendicular direction must have zero first derivative. Therefore the matrix-vector product has no perpendicular component: it must be parallel to the maximizing vector.

Symmetry then preserves the perpendicular subspace. If a vector is perpendicular to the first eigenvector,

$$
v_1^\top w=0,
$$

then

$$
v_1^\top Mw
=
(Mv_1)^\top w
=
\lambda_1v_1^\top w
=
0.
$$

The same argument can be repeated inside that perpendicular subspace. This produces an orthonormal eigenbasis.

Write the positive eigenvalues and their eigenvectors as

$$
Mv_j=\lambda_jv_j,
\qquad
\lambda_1\geq\cdots\geq\lambda_r>0.
$$

Define the singular values by

$$
\sigma_j=\sqrt{\lambda_j}.
$$

For every positive singular value, define an observation-space vector:

$$
u_j=\frac{Xv_j}{\sigma_j}.
$$

These vectors are orthonormal, because

$$
u_i^\top u_j
=
\frac{v_i^\top X^\top Xv_j}{\sigma_i\sigma_j}
=
\frac{\lambda_jv_i^\top v_j}{\sigma_i\sigma_j}
=
\begin{cases}
1,&i=j,\\
0,&i\neq j.
\end{cases}
$$

The resulting thin SVD is

$$
X=U\Sigma V^\top
=
\sum_{j=1}^r \sigma_j u_jv_j^\top.
$$

Here, the columns of $$V$$ are feature directions; the columns of $$U$$ are normalized patterns across observations; and the diagonal entries of $$\Sigma$$ determine their magnitudes.

## What each singular triplet means

The two defining relations are

$$
Xv_j=\sigma_ju_j,
\qquad
X^\top u_j=\sigma_jv_j.
$$

The first relation says that projecting the observations onto feature direction $$v_j$$ produces scores proportional to observation pattern $$u_j$$.

The second says that combining observations according to that pattern recovers the corresponding feature direction.

A left singular vector alone is not a vector of principal component scores. It has unit length. The scores include the singular value:

$$
\text{scores for component }j=\sigma_ju_j.
$$

To see why the leading direction captures the most variation, expand an arbitrary unit vector in the complete right-singular-vector basis:

$$
v=\sum_j c_jv_j,
\qquad
\sum_j c_j^2=1.
$$

Then

$$
\lVert Xv\rVert_2^2
=
\sum_j \sigma_j^2c_j^2
\leq
\sigma_1^2\sum_jc_j^2
=
\sigma_1^2.
$$

The upper bound is attained by the first right singular vector. Requiring the next direction to be perpendicular to the first removes its coefficient, leaving the second singular vector as the maximizer. Repeating this gives the successive principal directions.

Signs are arbitrary: changing both vectors in a singular pair to their negatives leaves the matrix unchanged. If singular values are equal, rotations within their shared subspace also leave the decomposition valid. An individual axis can therefore change between computations while the represented subspace remains the same.

## Covariance and PCA follow from the same decomposition

For centered observations, the sample covariance is

$$
C=\frac{X^\top X}{n-1}.
$$

The denominator has a statistical justification under independent, identically distributed sampling. Let the population-centered observations have covariance $$C_0$$. The identity

$$
\sum_i(a_i-\bar a)(a_i-\bar a)^\top
=
\sum_i(a_i-\mu)(a_i-\mu)^\top
-
n(\bar a-\mu)(\bar a-\mu)^\top
$$

gives, after taking expectations,

$$
nC_0-n\frac{C_0}{n}
=
(n-1)C_0.
$$

Dividing by the remaining degrees of freedom makes the estimator unbiased under those assumptions. Repeated, correlated frames do not automatically satisfy that sampling argument.

Substituting the SVD gives

$$
C
=
V\frac{\Sigma^2}{n-1}V^\top.
$$

Therefore the covariance eigenvalues are

$$
\lambda_j(C)=\frac{\sigma_j^2}{n-1}.
$$

The variance of component scores is exactly the corresponding covariance eigenvalue. Total variance is

$$
\operatorname{tr}(C)
=
\frac{\sum_j\sigma_j^2}{n-1}.
$$

The fraction assigned to component $$j$$ is consequently

$$
p_j=\frac{\sigma_j^2}{\sum_\ell\sigma_\ell^2}.
$$

PCA uses these directions to order variation. Labels play no role in this optimization. A principal component with large variance need not be diagnostically useful, and a component with small variance may carry the entire distinction needed for a particular label.

## Projection as a least-squares problem

Suppose the columns of a matrix $$Q$$ form an orthonormal basis for a chosen feature subspace. To approximate a feature vector $$z$$ inside that subspace, solve

$$
\min_c\lVert z-Qc\rVert_2^2.
$$

Expanding the objective gives

$$
\lVert z\rVert_2^2-2c^\top Q^\top z+c^\top c.
$$

Its derivative with respect to the coefficient vector is zero when

$$
c=Q^\top z.
$$

Thus the projection and residual are

$$
z_{\parallel}=QQ^\top z,
\qquad
z_{\perp}=(I-QQ^\top)z.
$$

The residual is perpendicular to every basis vector:

$$
Q^\top z_{\perp}
=
Q^\top z-Q^\top QQ^\top z
=
0.
$$

This perpendicularity explains the Pythagorean decomposition:

$$
\lVert z\rVert_2^2
=
\lVert z_{\parallel}\rVert_2^2+
\lVert z_{\perp}\rVert_2^2.
$$

It also explains what projection removes: only the component inside the specified linear subspace.

Orthogonality does not establish independence. For example, let a scalar variable take the values $$-1,0,1$$ with equal probability. The variables

$$
Z,
\qquad
W=Z^2-\frac23
$$

have zero covariance because

$$
\mathbb E[ZW]
=
\mathbb E[Z^3]-\frac23\mathbb E[Z]
=
0.
$$

Nevertheless, the second variable is determined completely by the first. Removing a linearly associated direction cannot establish that all information about a nuisance factor has disappeared.

## Why truncating the SVD minimizes reconstruction error

For an orthonormal feature basis with $$k$$ columns, the best reconstruction inside its span is

$$
\hat X=XQQ^\top.
$$

Its squared reconstruction error is

$$
\lVert X-\hat X\rVert_F^2
=
\lVert X\rVert_F^2-\lVert XQ\rVert_F^2.
$$

The Frobenius norm sums the squares of every matrix entry. From the SVD,

$$
\lVert X\rVert_F^2
=
\operatorname{tr}(X^\top X)
=
\sum_j\sigma_j^2.
$$

The retained energy is

$$
\lVert XQ\rVert_F^2
=
\sum_j\sigma_j^2\lVert Q^\top v_j\rVert_2^2.
$$

Each squared projection weight lies between zero and one. Across a complete feature basis, those weights sum to the subspace dimension. To maximize the weighted sum, assign the available weight to the largest squared singular values.

Therefore,

$$
X_k=\sum_{j=1}^k\sigma_ju_jv_j^\top
$$

achieves

$$
\lVert X-X_k\rVert_F^2
=
\sum_{j>k}\sigma_j^2.
$$

This also covers arbitrary approximations of rank at most $$k$$: their rows lie in some subspace of that dimension, and orthogonal projection is already the best approximation within any fixed subspace.

The theorem is powerful because the criterion is explicit. It minimizes total squared reconstruction error in the chosen coordinates. It does not minimize classification error, preserve every subgroup, or guarantee that discarded directions are clinically irrelevant.

## A representation matrix that can be checked by hand

Consider four constructed observations:

$$
X=
\begin{bmatrix}
2&1&0\\
2&-1&0\\
-2&1&0\\
-2&-1&0
\end{bmatrix}.
$$

Every column is centered. The first two columns are perpendicular, so

$$
X^\top X=
\begin{bmatrix}
16&0&0\\
0&4&0\\
0&0&0
\end{bmatrix}.
$$

The positive singular values are

$$
\sigma_1=4,
\qquad
\sigma_2=2.
$$

The right singular vectors are the first two coordinate axes. The left singular vectors are

$$
u_1=\frac12
\begin{bmatrix}
1\\1\\-1\\-1
\end{bmatrix},
\qquad
u_2=\frac12
\begin{bmatrix}
1\\-1\\1\\-1
\end{bmatrix}.
$$

Multiplying each left vector by its singular value reproduces the corresponding column of the matrix.

The covariance eigenvalues are

$$
\frac{16}{3},
\qquad
\frac43,
\qquad
0.
$$

The first component explains

$$
\frac{16}{16+4}=\frac45
$$

of the sample variance.

The rank-one approximation is

$$
X_1=
\begin{bmatrix}
2&0&0\\
2&0&0\\
-2&0&0\\
-2&0&0
\end{bmatrix}.
$$

Each row loses a second coordinate of magnitude one, so the total squared reconstruction error is

$$
1+1+1+1=4.
$$

That agrees with the discarded squared singular value.

Now define a constructed binary label by whether the second coordinate is positive. The original representation separates the labels perfectly using that coordinate. After rank-one projection, each retained representation is shared by observations with opposite labels.

Thus, retaining $$80\%$$ of variance can remove all information about this particular constructed label. No empirical performance claim is needed: the failure follows directly from the rows and labels.

## Effective rank measures how energy is distributed

Algebraic rank counts nonzero singular values. It treats an extremely small positive singular value the same as a large one. Effective-rank summaries instead ask how many directions make substantial contributions.

There is no single universal definition. The formula must accompany the reported number.

### Entropy effective rank

Using variance fractions, define

$$
r_{\mathrm{entropy}}
=
\exp\left(-\sum_{j=1}^r p_j\log p_j\right).
$$

The exponential converts entropy into an equivalent number of equally weighted directions. If energy is spread equally over $$r$$ directions,

$$
p_j=\frac1r,
$$

then

$$
-\sum_jp_j\log p_j=\log r,
\qquad
r_{\mathrm{entropy}}=r.
$$

If one direction carries all energy, the result is one. More generally, concavity of the logarithm gives

$$
\sum_jp_j\log\frac1{p_j}
\leq
\log\left(\sum_jp_j\frac1{p_j}\right)
=
\log r.
$$

For the constructed matrix,

$$
p=(0.8,0.2),
$$

so

$$
r_{\mathrm{entropy}}
=
\exp(-0.8\log0.8-0.2\log0.2)
\approx1.6494.
$$

Some definitions normalize singular values themselves instead of their squares. That produces a different number. Here the weights deliberately represent variance.

### Stable rank

The spectral norm measures the largest amplification of a unit vector:

$$
\lVert X\rVert_2^2
=
\max_{\lVert v\rVert_2=1}\lVert Xv\rVert_2^2
=
\sigma_1^2.
$$

Stable rank is

$$
r_{\mathrm{stable}}
=
\frac{\lVert X\rVert_F^2}{\lVert X\rVert_2^2}
=
\frac{\sum_j\sigma_j^2}{\sigma_1^2}.
$$

It compares total energy with the energy of the strongest direction. In the example,

$$
r_{\mathrm{stable}}=\frac{20}{16}=1.25.
$$

### Participation rank

Another summary is

$$
r_{\mathrm{participation}}
=
\frac1{\sum_jp_j^2}
=
\frac{(\sum_j\sigma_j^2)^2}{\sum_j\sigma_j^4}.
$$

The denominator increases when energy concentrates in a few directions. Equal weights again produce the number of occupied directions.

For the example,

$$
r_{\mathrm{participation}}
=
\frac1{0.8^2+0.2^2}
=
\frac{25}{17}
\approx1.4706.
$$

All three summaries agree on the endpoints of equal-energy and single-direction representations. They emphasize unequal spectra differently.

## Reading a spectrum for collapse

Complete centered collapse means every observation has the same representation. Then the centered matrix is zero and every singular value is zero.

A raw matrix of identical nonzero rows can have rank one. That does not contradict complete collapse of differences between observations: centering removes the common vector.

Dimensional collapse is less extreme. Representations still vary, but most variation occupies a small subspace. For example, singular values

$$
(4,\varepsilon)
$$

give algebraic rank two whenever the second value is positive, while all three effective-rank summaries approach one as that value approaches zero.

Effective rank alone misses uniform shrinkage. Multiplying a matrix by a nonzero scalar changes every singular value by the same factor, leaving normalized energy fractions unchanged. A representation can become arbitrarily small without changing its effective rank.

A useful collapse report therefore includes both:

- Total centered energy, which records overall variation.
- The normalized spectrum, which records how variation is distributed.
- Sample size and feature dimension, which limit observable rank.
- The centering, normalization, and weighting conventions.

For a zero matrix, normalized spectral weights are undefined because their denominator is zero. Report complete collapse directly instead of forcing the effective-rank formula to return an arbitrary value.

A narrow spectrum is also a description rather than a diagnosis. A genuinely low-dimensional task can produce a low-dimensional useful representation. Conversely, a high-rank representation can contain abundant nuisance variation.

## Small singular values and unstable linear recovery

Suppose a linear probe fits targets by minimizing

$$
\min_w\lVert Xw-y\rVert_2^2.
$$

Write the identifiable part of its coefficient vector as

$$
w=\sum_j a_jv_j.
$$

Then

$$
Xw=\sum_j\sigma_ja_ju_j.
$$

Matching the component of the target along each left singular vector requires

$$
a_j=\frac{u_j^\top y}{\sigma_j}.
$$

Consequently, a small change in the target component is amplified by the reciprocal singular value. A direction can be present algebraically while requiring a large, unstable probe coefficient.

Adding a squared coefficient penalty gives

$$
\min_w
\left[
\lVert Xw-y\rVert_2^2+
\lambda\lVert w\rVert_2^2
\right].
$$

In singular coordinates, differentiating each scalar objective yields

$$
2\sigma_j(\sigma_ja_j-u_j^\top y)+2\lambda a_j=0,
$$

and therefore

$$
a_j=
\frac{\sigma_j}{\sigma_j^2+\lambda}u_j^\top y.
$$

Regularization reduces amplification along weak directions. It also changes what the probe can recover. Probe failure may reflect limited observations, regularization, or the probe family, rather than the complete absence of information.

## Making a representation analysis reproducible

Fit the mean, scaling, and principal directions on development observations. Transform held-out observations using those fixed quantities:

$$
s_{\mathrm{new}}
=
V_k^\top(a_{\mathrm{new}}-\bar a_{\mathrm{development}}).
$$

Recomputing the mean or basis on the evaluation set asks a different question and prevents a clean interpretation of the transformation as fixed.

Repeated frames change the matrix's weighting. Duplicating observations contributes their outer products again, so frequently represented patients can dominate the spectrum. Patient-balanced sampling or explicitly chosen weights should follow the intended analysis unit.

Finally, compare subspaces when eigenvalues are close. A sign flip or a rotation inside a nearly tied component group should not be interpreted as the appearance of a new clinical mechanism. The stable object may be the span of several directions.

## Revision checklist

| Question | What I should be able to reconstruct |
|---|---|
| What does centering remove? | Derive the mean contribution to the raw Gram matrix. |
| Why is centered rank sample-limited? | Use the linear dependence among centered rows. |
| How is the SVD constructed? | Obtain right vectors from the Gram matrix and left vectors from their scores. |
| What are component scores? | Explain why singular values multiply left singular vectors. |
| How does PCA connect to covariance? | Derive covariance eigenvalues from squared singular values. |
| Why does projection have its usual formula? | Solve the coefficient least-squares problem. |
| Why is truncated SVD optimal? | Maximize retained energy over feature subspaces. |
| Can high retained variance preserve the wrong information? | Reproduce the four-row label example. |
| Which effective rank did I report? | State its weights and calculate its value. |
| What can a collapse summary miss? | Separate overall scale, spectral concentration, and sampling limits. |
| Why can a probe become unstable? | Show reciprocal amplification by small singular values. |

## Why it matters for my work

For gallbladder ultrasound representations, I want to distinguish dominant variation from clinically useful variation. A spectrum can identify a subspace worth investigating, but patient weighting, acquisition effects, and probe stability determine what I can conclude from it.

## What I have not resolved

- Which patient-level weighting best matches the representation audit I intend to report?
- Measure whether clinically relevant probe information survives removal of the leading acquisition-associated subspaces.
