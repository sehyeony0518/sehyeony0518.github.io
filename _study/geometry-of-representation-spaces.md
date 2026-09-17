---
layout: study_note
title: "Geometry of Representation Spaces"
description: "Cosine similarity, manifolds, metric spaces, and what the shape of a latent space says about what a model encodes."
og_image: "https://sehyeony0518.github.io/assets/img/og/geometry-of-representation-spaces.png"
tab: "ai-foundations"
tab_title: "AI Theory"
category: "algebra-and-optimization"
category_title: "Linear Algebra & Optimization"
subgroup: "Linear Algebra & Geometry"
order: 3
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-09-19-tcav-concept-activation-vectors"
  - "2026-08-10-concept-gradients-nonlinear-interpretation"
  - "2026-07-02-weight-space-correlation-analysis"
---

A representation does not come with a uniquely correct meaning of “near.” Euclidean distance, cosine similarity, and covariance-adjusted distance preserve different relationships. Before interpreting a neighborhood, I need to identify which changes its geometry treats as important and which changes it deliberately ignores.

High dimension adds another issue: under explicit distributional assumptions, most pairwise distances become similar relative to their average size. Understanding that statement requires distinguishing distance from squared distance, ambient dimension from effective dimension, and pairwise concentration from a claim about every nearest neighbor.

## What a norm commits me to

A norm measures vector magnitude. It satisfies positivity, absolute homogeneity, and the triangle inequality:

$$
\lVert x\rVert\geq0,
\qquad
\lVert x\rVert=0\iff x=0,
$$

$$
\lVert ax\rVert=\lvert a\rvert\lVert x\rVert,
$$

$$
\lVert x+y\rVert\leq\lVert x\rVert+\lVert y\rVert.
$$

Defining distance through differences,

$$
d(x,y)=\lVert x-y\rVert,
$$

makes distance translation-invariant. Moving every point by the same vector does not change any difference. Homogeneity says that doubling a displacement doubles its measured length. The triangle inequality says a direct displacement cannot be longer than a route through an intermediate point.

These are substantive choices about geometry. They do not, by themselves, specify a probability distribution or establish clinical similarity.

Three familiar norms are

$$
\lVert x\rVert_1=\sum_j\lvert x_j\rvert,
\qquad
\lVert x\rVert_2=\sqrt{\sum_jx_j^2},
\qquad
\lVert x\rVert_\infty=\max_j\lvert x_j\rvert.
$$

For the first, every coordinate contributes additively. For the last, the largest coordinate controls the result. The Euclidean norm combines coordinates through squared magnitude.

Consider two constructed changes:

$$
a=(1,0),
\qquad
b=(0.6,0.6).
$$

Their lengths are

$$
\lVert a\rVert_1=1,
\qquad
\lVert b\rVert_1=1.2,
$$

but

$$
\lVert a\rVert_2=1,
\qquad
\lVert b\rVert_2=\sqrt{0.72}<1.
$$

The first norm regards the distributed change as larger; the second regards it as smaller. A perturbation budget expressed using a norm therefore defines which kinds of changes are affordable.

For the Euclidean triangle inequality, expand the squared length and apply Cauchy–Schwarz:

$$
\lVert x+y\rVert_2^2
=
\lVert x\rVert_2^2+
2x^\top y+
\lVert y\rVert_2^2
\leq
(\lVert x\rVert_2+\lVert y\rVert_2)^2.
$$

Taking square roots gives the desired inequality. Squared Euclidean distance itself is not a metric: on the real line, the squared distance from zero to two is four, while the two intermediate squared distances through one sum to two.

## Coordinate scales are part of the distance

Euclidean distance assumes the supplied coordinate units can be combined directly:

$$
d_E(x,y)^2=\sum_j(x_j-y_j)^2.
$$

Changing the units of one coordinate can change neighbor rankings. Suppose two candidates differ from a query by

$$
\delta_A=(5,0),
\qquad
\delta_B=(0,2).
$$

Their Euclidean distances are five and two, so the second candidate is nearer.

Now suppose development data indicate that the first coordinate has standard deviation ten and the second has standard deviation one. Measuring displacement in those units gives

$$
d_{\mathrm{scaled}}(\delta_A)=\frac5{10}=0.5,
\qquad
d_{\mathrm{scaled}}(\delta_B)=\frac21=2.
$$

The ranking reverses. Neither ranking is algebraically mistaken. They answer different questions: absolute coordinate displacement versus displacement relative to the selected feature scales.

More generally, let a symmetric positive definite matrix define

$$
\lVert x\rVert_M=\sqrt{x^\top Mx}.
$$

Its eigendecomposition provides a square root:

$$
M=Q\Lambda Q^\top,
\qquad
M^{1/2}=Q\Lambda^{1/2}Q^\top.
$$

Therefore,

$$
\lVert x\rVert_M=\lVert M^{1/2}x\rVert_2.
$$

This proves that the weighted norm is ordinary Euclidean length after a coordinate transformation. Its norm properties follow from the Euclidean properties and the invertibility of the transformation.

If the matrix is merely positive semidefinite, a nonzero displacement in its nullspace can have zero length. The resulting distance is a pseudometric on the original space: it treats some distinct points as equivalent.

## Mahalanobis distance and the meaning of whitening

For a positive definite covariance matrix, Mahalanobis distance is

$$
d_M(x,y)^2=(x-y)^\top C^{-1}(x-y).
$$

Why the inverse covariance? Write

$$
C=Q\Lambda Q^\top.
$$

The transformed displacement

$$
u=\Lambda^{-1/2}Q^\top(x-y)
$$

first rotates into covariance eigenvectors and then divides each coordinate by its standard deviation. Its squared Euclidean length is

$$
u^\top u
=
(x-y)^\top Q\Lambda^{-1}Q^\top(x-y).
$$

Thus a displacement along a high-variance direction costs less than the same absolute displacement along a low-variance direction.

There is also a probabilistic interpretation, if a Gaussian model is explicitly assumed. Its density has the form

$$
p(x)=
\frac{
\exp\left[-\frac12(x-\mu)^\top C^{-1}(x-\mu)\right]
}{
(2\pi)^{d/2}\det(C)^{1/2}
}.
$$

Taking the negative logarithm leaves half the squared Mahalanobis distance from the mean plus terms constant in the observation. Under this model, the distance measures relative plausibility.

The geometric construction remains usable without believing the data are Gaussian. The probabilistic interpretation does not.

Whitening can amplify unstable directions. If a covariance eigenvalue is very small, division by its square root magnifies variation along its eigenvector. With more features than independent observations, the sample covariance can be singular. Restricting to a supported subspace or regularizing the covariance changes the metric and should be reported.

Importantly, high population variance is not synonymous with nuisance variation. Whitening may suppress a genuinely useful direction. Its appropriateness depends on the intended comparison.

## Why cosine and Euclidean distance disagree

For nonzero vectors, cosine similarity is

$$
c(x,y)=
\frac{x^\top y}{\lVert x\rVert_2\lVert y\rVert_2}.
$$

The denominator removes positive changes of scale:

$$
c(ax,by)=c(x,y)
\qquad
\text{for }a,b>0.
$$

This is exactly what cosine is designed to ignore. Multiplying a vector by a negative scalar reverses its direction and does not preserve the similarity.

Let the two vector lengths be

$$
r=\lVert x\rVert_2,
\qquad
s=\lVert y\rVert_2.
$$

Expanding Euclidean distance gives

$$
\lVert x-y\rVert_2^2
=
r^2+s^2-2rs\,c(x,y).
$$

Rearrange it as

$$
\lVert x-y\rVert_2^2
=
(r-s)^2+2rs(1-c(x,y)).
$$

The first term measures a difference in magnitude. The second measures directional disagreement, weighted by the lengths. Cosine similarity keeps the directional comparison while discarding the first term and the length weighting.

Consider a query and two candidates:

$$
q=(1,0),
\qquad
a=(10,0),
\qquad
b=(1,1).
$$

Their Euclidean distances from the query are

$$
\lVert q-a\rVert_2=9,
\qquad
\lVert q-b\rVert_2=1.
$$

Their cosine similarities are

$$
c(q,a)=1,
\qquad
c(q,b)=\frac1{\sqrt2}.
$$

Euclidean distance chooses the second candidate; cosine chooses the first. The disagreement is completely explained by the first candidate's large magnitude and identical direction.

Cosine is appropriate when positive radial scaling is a nuisance or when the representation and downstream task were deliberately defined on normalized directions. Euclidean distance is appropriate when absolute displacement, including magnitude, is relevant. Whether representation norm actually reflects confidence, image quality, or another useful quantity is an empirical question; the norm's existence does not establish any particular interpretation.

## Normalization, metric properties, and the origin

Normalize each nonzero representation:

$$
\hat x=\frac{x}{\lVert x\rVert_2}.
$$

Then

$$
\lVert\hat x-\hat y\rVert_2^2
=
2-2c(x,y).
$$

Consequently, cosine similarity and Euclidean distance on normalized vectors give the same neighbor ordering. Taking a square root does not change the ordering because it is increasing on nonnegative values.

The commonly used dissimilarity

$$
d_{\cos}(x,y)=1-c(x,y)
$$

is not generally a metric, even on the unit sphere. To check the triangle inequality directly, take unit vectors at angles

$$
0,\qquad \frac{\pi}{3},\qquad \frac{2\pi}{3}.
$$

The two adjacent cosine dissimilarities are each

$$
1-\cos\frac{\pi}{3}=\frac12.
$$

The endpoint dissimilarity is

$$
1-\cos\frac{2\pi}{3}=\frac32.
$$

It exceeds the sum of the two adjacent dissimilarities. Euclidean chord distance on the unit sphere avoids this failure. Angular distance,

$$
d_{\mathrm{angle}}(x,y)=\arccos c(x,y),
$$

also defines a metric on unit directions: it is the length of the shortest spherical arc, and concatenating two arcs cannot shorten that minimum.

Cosine additionally depends on the origin. Start with

$$
x=(1,0),
\qquad
y=(0,1),
$$

whose cosine is zero. Add the same offset to both:

$$
x'=(11,10),
\qquad
y'=(10,11).
$$

Their Euclidean distance remains unchanged, but their cosine becomes

$$
c(x',y')=\frac{220}{221}.
$$

Centering before cosine comparison can therefore change neighborhoods substantially. There is no universal rule that centering is always correct; the intended meaning of the origin decides.

Cosine is undefined for a zero vector. Adding a numerical constant to its denominator creates a modified score, whose treatment of very small vectors must be understood separately.

## Deriving concentration of squared distances

Consider a specific model:

$$
X,Y\overset{\mathrm{ind}}{\sim}\mathcal N(0,I_d).
$$

Their coordinate differences are independent Gaussian variables with mean zero and variance two. Write

$$
X_i-Y_i=\sqrt2\,G_i,
\qquad
G_i\sim\mathcal N(0,1).
$$

The squared distance is

$$
S=\lVert X-Y\rVert_2^2
=
2\sum_{i=1}^dG_i^2.
$$

The needed Gaussian moments can be derived by integration by parts. For the standard Gaussian density,

$$
\phi'(g)=-g\phi(g).
$$

Vanishing boundary terms give

$$
\mathbb E[G^2]
=
-\int g\phi'(g)\,dg
=
1,
$$

and

$$
\mathbb E[G^4]
=
-\int g^3\phi'(g)\,dg
=
3\int g^2\phi(g)\,dg
=
3.
$$

Therefore,

$$
\operatorname{Var}(G^2)
=
3-1^2
=
2.
$$

Independence across coordinates now gives

$$
\mathbb E[S]=2d,
\qquad
\operatorname{Var}(S)=8d.
$$

Its relative standard deviation is

$$
\frac{\sqrt{\operatorname{Var}(S)}}{\mathbb E[S]}
=
\frac{\sqrt{8d}}{2d}
=
\sqrt{\frac2d}.
$$

The average squared distance grows linearly with dimension, while its standard deviation grows only as the square root. Relative differences therefore shrink.

These are calculated properties of the constructed Gaussian model:

| Dimension | Mean squared distance | Standard deviation of squared distance | Relative standard deviation |
|---|---:|---:|---:|
| $$50$$ | $$100$$ | $$20$$ | $$0.20$$ |
| $$200$$ | $$400$$ | $$40$$ | $$0.10$$ |
| $$800$$ | $$1600$$ | $$80$$ | $$0.05$$ |

The table describes squared distances. It does not claim that the mean distance equals the square root of the mean squared distance.

## Turning relative variance into a concentration statement

Chebyshev's inequality gives, for positive tolerance,

$$
\Pr\left(
\left|\frac{S}{2d}-1\right|\geq\varepsilon
\right)
\leq
\frac{2}{d\varepsilon^2}.
$$

The right side may exceed one, in which case the bound is uninformative. The useful conclusion is its dependence on dimension for a fixed tolerance.

To transfer the result to ordinary distance, let

$$
R=\frac{S}{2d}.
$$

Then

$$
\left|\sqrt R-1\right|
=
\frac{|R-1|}{\sqrt R+1}
\leq
|R-1|.
$$

Thus the distance divided by the root-mean-square distance also approaches one in probability.

This is not the statement that absolute differences vanish. Under the model, relative squared-distance variation shrinks even though the standard deviation of squared distance grows. Confusing absolute and relative spread can make a distance histogram appear to contradict concentration when it does not.

Nor does a pairwise statement automatically cover every point in a very large database. For a fixed query and a collection of $$m$$ independent Gaussian candidates, each squared distance has the marginal distribution above. A union bound gives

$$
\Pr(\text{at least one distance violates the tolerance})
\leq
\frac{2m}{d\varepsilon^2}.
$$

The distances share the query, but independence between those distances is unnecessary for this bound.

If all distances satisfy the tolerance, with tolerance below one, then

$$
\frac{D_{\max}}{D_{\min}}
\leq
\sqrt{\frac{1+\varepsilon}{1-\varepsilon}}.
$$

The dependence on database size matters. A concentration statement for one pair does not justify an unrestricted claim that nearest and farthest neighbors must be indistinguishable.

## Why cosine does not automatically escape concentration

For independent isotropic Gaussian vectors, normalized directions are uniformly distributed on the unit sphere. Rotational symmetry lets me fix the first direction to the first coordinate axis.

The cosine is then the first coordinate of the second unit direction:

$$
c=V_1.
$$

Symmetry gives zero mean. Because all coordinates have equal second moments and their squares sum to one,

$$
\sum_{j=1}^d\mathbb E[V_j^2]=1,
\qquad
\mathbb E[V_1^2]=\frac1d.
$$

Therefore,

$$
\mathbb E[c]=0,
\qquad
\operatorname{Var}(c)=\frac1d.
$$

Random directions become nearly perpendicular as dimension increases. Applying Chebyshev again gives

$$
\Pr(|c|\geq\tau)\leq\frac1{d\tau^2}.
$$

Normalization removes radial variation. It does not create meaningful angular structure where the assumed distribution contains none.

The important distinction is between a random isotropic model and a learned representation. A trained representation can have clusters, correlated features, nonzero means, and low-dimensional structure. The calculation provides a baseline to test against, rather than a universal description of learned embeddings.

## Effective dimension controls anisotropic concentration

Replace the identity covariance with a positive semidefinite covariance:

$$
X,Y\overset{\mathrm{ind}}{\sim}\mathcal N(0,C).
$$

In its eigenbasis, the squared distance becomes

$$
S=2\sum_j\lambda_jG_j^2.
$$

Using the same moments,

$$
\mathbb E[S]=2\sum_j\lambda_j=2\operatorname{tr}(C),
$$

and

$$
\operatorname{Var}(S)
=
8\sum_j\lambda_j^2
=
8\operatorname{tr}(C^2).
$$

Hence,

$$
\frac{\operatorname{Var}(S)}{\mathbb E[S]^2}
=
\frac{2\operatorname{tr}(C^2)}
{\operatorname{tr}(C)^2}.
$$

Define the participation dimension by

$$
d_{\mathrm{eff}}
=
\frac{\operatorname{tr}(C)^2}{\operatorname{tr}(C^2)}.
$$

The relative variance is therefore

$$
\frac2{d_{\mathrm{eff}}}.
$$

This connects distance concentration to the spectrum in the linear algebra note. Adding many zero coordinates increases ambient dimension without changing any distance or the effective dimension. A representation with many coordinates but only a few substantial covariance eigenvalues need not resemble the isotropic high-dimensional example.

The Gaussian assumption is still doing work: diagonalizing covariance also gives independent Gaussian coordinates. Zero covariance alone would not establish the independence needed for the variance calculation in an arbitrary distribution.

## Manifolds and projection change which paths are available

A manifold model asserts that local neighborhoods resemble a lower-dimensional Euclidean space. It does not imply that straight lines through ambient feature space remain on the set of plausible representations.

For a circle of radius $$R$$ and angular separation $$\theta$$ up to a half-turn, the arc length is

$$
d_{\mathrm{arc}}=R\theta.
$$

Bisecting the isosceles triangle between the two radii gives chord length

$$
d_{\mathrm{chord}}=2R\sin\frac\theta2.
$$

For nearby points, the sine is approximately its argument, so the distances agree to first order. For opposite points on a unit circle, the chord is two while the shortest arc is $$\pi$$.

A manifold distance therefore incorporates assumptions about permitted paths. A smooth-looking visualization does not establish that interpolating along those paths corresponds to disease progression or a feasible change in an ultrasound image.

Projection adds another limitation. For an orthonormal projection matrix,

$$
\lVert x-y\rVert_2^2
=
\lVert Q^\top(x-y)\rVert_2^2
+
\lVert(I-QQ^\top)(x-y)\rVert_2^2.
$$

Displayed distance omits the second term. Two points separated only in a discarded coordinate can overlap perfectly in a plot. Visual clusters should therefore be checked using the original representation and the declared metric.

## Geometry can change while predictions stay identical

Suppose a linear classifier uses

$$
s=w^\top z.
$$

Apply an invertible feature transformation and compensate in the classifier:

$$
z'=Az,
\qquad
w'=A^{-\top}w.
$$

Then

$$
w'^\top z'=w^\top z.
$$

Predictions remain identical, although a general transformation changes Euclidean distances and cosine similarities. Information preserved by invertibility is a broader notion than geometry preserved by a particular metric.

For an orthogonal transformation,

$$
A^\top A=I,
$$

both dot products and Euclidean lengths remain unchanged. This is why rotated coordinate axes can describe the same Euclidean geometry while individual feature coordinates have different interpretations.

A representation audit should therefore specify its invariances. It should also distinguish recoverable information from decision reliance. Scanner identity being predictable from neighborhoods or a probe establishes something about the representation. It does not, by itself, establish that the diagnostic output uses scanner identity.

## Revision checklist

| Question | What I should be able to demonstrate |
|---|---|
| What does a norm assume? | Explain translation invariance, scaling, and the triangle inequality. |
| Can coordinate units change neighbors? | Reproduce the scaled two-coordinate example. |
| Why use inverse covariance? | Derive whitening and its squared Euclidean distance. |
| Why do cosine and Euclidean rankings disagree? | Separate radial and angular terms. |
| When do their rankings agree? | Normalize both vectors and derive the chord-distance identity. |
| Is cosine dissimilarity a metric? | Check the three-angle counterexample. |
| Does centering affect cosine? | Recalculate the shared-offset example. |
| What concentrates in high dimension? | Derive the mean and variance of squared Gaussian distance. |
| What does database size change? | Explain the union bound and its limitations. |
| Does normalization remove concentration? | Derive the cosine variance for random directions. |
| Which dimension matters? | Relate anisotropic concentration to participation dimension. |
| Can geometry change without changing outputs? | Construct an invertible transformation and compensate the classifier. |

## Why it matters for my work

I want ultrasound neighborhoods to support explicit comparisons across patients, lesions, and acquisition settings. Choosing a distance means deciding whether magnitude, covariance scale, and the representation's origin should influence those comparisons. Those choices need to be recorded before interpreting the neighbors clinically.

## What I have not resolved

- Which parts of representation magnitude are useful for my intended audit?
- Compare patient-separated neighborhoods under raw Euclidean, normalized Euclidean, and regularized covariance-adjusted distances.
