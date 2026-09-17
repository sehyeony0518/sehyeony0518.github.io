---
layout: study_note
title: "Bayesian Inverse Problems in Imaging"
description: "Denoising and restoration written as inference: an acquisition model as the likelihood, an image prior as the assumption, and what a Markov random field assumes to stay computable."
og_image: "https://sehyeony0518.github.io/assets/img/og/bayesian-inverse-problems-in-imaging.png"
tab: "ai-foundations"
tab_title: "AI Theory"
category: "probability-and-inference"
category_title: "Probability & Statistical Inference"
subgroup: "Bayesian Imaging & Model Uncertainty"
order: 12
source: "Independent study"
written: true
updated: "2026-09-15"
---

An inverse problem begins with a model of how an unknown object produces observations. In imaging, the unknown might be pixel intensities, attenuation coefficients, or another representation of the object. The data may be blurred, subsampled, transformed, or noisy measurements of that object.

Writing the reconstruction as Bayesian inference makes three choices explicit: the acquisition model, the noise distribution, and the image prior. Under a linear forward model, independent additive Gaussian noise, and a Gaussian prior, the posterior is Gaussian and the reconstruction follows from a linear system. Tikhonov regularization and the Wiener estimator are closely related forms of this result, with assumptions that should be stated rather than hidden.

## The forward model determines the likelihood

Represent the unknown image by $$x\in\mathbb R^n$$ and the measurements by $$y\in\mathbb R^m$$. Begin with

$$
y=Ax+\epsilon.
$$

The known matrix $$A$$ describes the acquisition operation. Identity acquisition gives denoising; a convolution operator gives a blur model; selected rows of an operator can represent missing measurements. The dimensions need not agree.

Assume the noise is independent of the image and distributed as

$$
\epsilon\sim\mathcal N(0,R),
\qquad
R\succ0.
$$

Conditioned on the image, the measurement is just the noise translated by the predicted observation. Translation has unit Jacobian, so

$$
p(y\mid x)=p_\epsilon(y-Ax).
$$

Substituting the Gaussian noise density gives

$$
p(y\mid x)
=
(2\pi)^{-m/2}|R|^{-1/2}
\exp\left[
-\frac12(y-Ax)^\top R^{-1}(y-Ax)
\right].
$$

The negative log-likelihood is therefore

$$
-\log p(y\mid x)
=
\frac12(y-Ax)^\top R^{-1}(y-Ax)
+\frac12\log|R|
+\frac m2\log(2\pi).
$$

If the noise covariance is itself being estimated, its log-determinant term is not constant and must be retained. Dropping it would change the problem: a larger assumed variance could reduce the weighted residual without paying the required density-normalization cost.

The squared residual is a consequence of the Gaussian noise assumption. It is not the definition of a general imaging likelihood.

For independent equal-variance noise,

$$
R=\sigma^2I,
$$

and the image-dependent term becomes

$$
\frac{1}{2\sigma^2}\lVert y-Ax\rVert^2.
$$

For unequal independent variances, each squared residual is divided by its own variance. Correlated noise requires the full inverse covariance. Equivalently, if

$$
R=BB^\top,
$$

then

$$
(y-Ax)^\top R^{-1}(y-Ax)
=
\lVert B^{-1}y-B^{-1}Ax\rVert^2.
$$

This is whitening: transform residuals so that the assumed noise covariance becomes the identity.

Without a prior, Gaussian maximum likelihood minimizes this residual. It does not generally return the observed image. Returning the observation is the special unconstrained denoising case where the forward operator is the identity. In deblurring or subsampling, the observation may not even lie in the same space as the unknown.

For white noise and a full-column-rank forward matrix, differentiating the residual gives

$$
A^\top(Ax-y)=0,
\qquad
\widehat x_{\mathrm{ML}}
=(A^\top A)^{-1}A^\top y.
$$

A rank-deficient operator leaves some directions unidentified by the likelihood. A nearly rank-deficient operator can amplify noise severely when inverted.

## The prior becomes a penalty through Bayes' rule

Choose an image prior $$p(x)$$. Bayes' rule gives

$$
p(x\mid y)
=
\frac{p(y\mid x)p(x)}{p(y)}.
$$

For fixed acquisition, noise, and prior parameters, the evidence does not depend on the candidate image. The maximum a posteriori estimate is

$$
\widehat x_{\mathrm{MAP}}
\in
\arg\min_x
\left[
-\log p(y\mid x)-\log p(x)
\right].
$$

The evidence can be dropped for this optimization whether or not it is easy to compute. In the Gaussian case below, it is analytically available; an intractable normalizing constant is not a prerequisite for using MAP.

Suppose the prior is

$$
x\sim\mathcal N(x_0,C_0),
\qquad
C_0\succ0.
$$

Its negative log density contains the quadratic penalty

$$
\frac12(x-x_0)^\top C_0^{-1}(x-x_0).
$$

The prior mean supplies a reference image. The covariance specifies which deviations are plausible and how image coordinates vary together. Small prior variance in a direction produces a large penalty for moving in that direction.

Discarding only terms independent of the image gives

$$
J(x)
=
\frac12(y-Ax)^\top R^{-1}(y-Ax)
+
\frac12(x-x_0)^\top C_0^{-1}(x-x_0).
$$

This is a balance between fit and prior plausibility measured in their respective uncertainty units. Changing the noise or prior variance changes that balance.

MAP is a posterior mode. A posterior mean answers a different decision problem. For any proposed estimate $$a$$, write the posterior mean as $$\mu$$ and expand:

$$
\mathbb E[\lVert x-a\rVert^2\mid y]
=
\mathbb E[\lVert x-\mu\rVert^2\mid y]
+\lVert\mu-a\rVert^2.
$$

The cross term vanishes because the centred posterior has mean zero. Therefore the posterior mean minimizes expected squared error. Mean and mode coincide for the Gaussian posterior derived next, but need not coincide in other models.

## Complete the square to obtain the entire posterior

Expand both quadratic terms in the MAP objective:

$$
J(x)
=
\frac12x^\top Hx-b^\top x+\text{constant},
$$

where

$$
H=A^\top R^{-1}A+C_0^{-1},
\qquad
b=A^\top R^{-1}y+C_0^{-1}x_0.
$$

For every nonzero vector,

$$
v^\top Hv
=
(Av)^\top R^{-1}(Av)+v^\top C_0^{-1}v>0.
$$

The second term is strictly positive because the prior covariance is positive definite. Thus the posterior precision is positive definite even when the acquisition operator has a null space.

The derivative is

$$
\nabla_xJ=Hx-b.
$$

Setting it to zero gives the unique minimizer

$$
\mu=H^{-1}b.
$$

To identify the posterior distribution rather than just its mode, use the identity

$$
x^\top Hx-2b^\top x
=
(x-\mu)^\top H(x-\mu)-\mu^\top H\mu.
$$

The last term is independent of the candidate image. The remaining exponential is therefore a Gaussian with

$$
\boxed{
C_{\mathrm{post}}
=
(A^\top R^{-1}A+C_0^{-1})^{-1}
}
$$

and

$$
\boxed{
\widehat x_{\mathrm{MAP}}
=
\mathbb E[x\mid y]
=
C_{\mathrm{post}}
(A^\top R^{-1}y+C_0^{-1}x_0)
}.
$$

The posterior covariance is independent of the observed values when the operator and covariances are fixed. It still depends on the acquisition geometry and the assumed uncertainty scales. This is conditional uncertainty under the model, not a guarantee of calibration under a misspecified acquisition process.

The formulas also assume the unknown ranges over the full real vector space. Enforcing nonnegativity, bounded intensities, or another image constraint generally changes the mode and removes the simple unconstrained formula.

## Recover Tikhonov regularization and its assumptions

For white noise, specify a quadratic prior precision through an operator $$L$$:

$$
R=\sigma^2I,
\qquad
C_0^{-1}=\tau^{-2}L^\top L.
$$

If the operator has full column rank, this defines a proper Gaussian prior. Multiplying the MAP objective by the positive constant $$2\sigma^2$$ leaves its minimizer unchanged:

$$
\widehat x
=
\arg\min_x
\left[
\lVert y-Ax\rVert^2
+\lambda\lVert L(x-x_0)\rVert^2
\right],
\qquad
\lambda=\frac{\sigma^2}{\tau^2}.
$$

Here the regularization parameter is the coefficient of the squared penalty. Some conventions call that coefficient the square of the regularization parameter; the distinction must be checked before comparing formulas.

Differentiating gives

$$
A^\top(Ax-y)+\lambda L^\top L(x-x_0)=0.
$$

Hence the general Tikhonov solution is

$$
\boxed{
\widehat x
=
(A^\top A+\lambda L^\top L)^{-1}
(A^\top y+\lambda L^\top Lx_0)
}.
$$

When the reference image is zero and the penalty operator is the identity, this reduces to

$$
\widehat x
=
(A^\top A+\lambda I)^{-1}A^\top y.
$$

The identity penalty shrinks image energy. A finite-difference operator instead penalizes spatial variation. These express different prior beliefs.

There is an important qualification for derivative penalties. If $$L$$ annihilates constant images, then

$$
\exp\left[-\frac1{2\tau^2}\lVert L(x-x_0)\rVert^2\right]
$$

does not integrate to a finite value over all real images: shifting along an unpenalized direction does not change its value. It is an improper prior unless that direction is anchored or otherwise constrained.

A proper posterior can still result. For positive regularization weight,

$$
v^\top(A^\top A+\lambda L^\top L)v
=
\lVert Av\rVert^2+\lambda\lVert Lv\rVert^2.
$$

This is strictly positive for every nonzero vector exactly when

$$
\ker(A)\cap\ker(L)=\{0\}.
$$

Thus the observations must identify every direction left unpenalized by the prior. This is the precise uniqueness condition for the quadratic reconstruction with a possibly rank-deficient penalty.

## The Wiener form is the same Gaussian solution

The posterior mean can also be written as a correction to the prior mean:

$$
\widehat x
=
x_0+
C_0A^\top(AC_0A^\top+R)^{-1}(y-Ax_0).
$$

Rather than quote a matrix identity, verify it. Using the posterior precision already defined,

$$
\begin{aligned}
HC_0A^\top
&=
A^\top R^{-1}AC_0A^\top+A^\top\\
&=
A^\top R^{-1}(AC_0A^\top+R).
\end{aligned}
$$

Right-multiplying by the inverse measurement covariance gives

$$
H\left[
C_0A^\top(AC_0A^\top+R)^{-1}
\right]
=A^\top R^{-1}.
$$

Therefore the bracket equals the correction matrix obtained from the normal equations:

$$
H^{-1}A^\top R^{-1}
=
C_0A^\top(AC_0A^\top+R)^{-1}.
$$

The term $$y-Ax_0$$ is the observation's deviation from what the prior mean predicts. The correction matrix decides how much each measurement should change the reconstruction.

This linear estimator also has a broader justification. Let the centred image and observation be $$u$$ and $$v$$, and consider linear estimates $$Bv$$. Their mean squared error is

$$
\mathbb E[\lVert u-Bv\rVert^2]
=
\operatorname{tr}(C_{uu})
-2\operatorname{tr}(BC_{vu})
+\operatorname{tr}(BC_{vv}B^\top).
$$

Differentiation gives

$$
BC_{vv}=C_{uv},
\qquad
B=C_{uv}C_{vv}^{-1}.
$$

For additive noise uncorrelated with the image,

$$
C_{uv}=C_0A^\top,
\qquad
C_{vv}=AC_0A^\top+R.
$$

This yields the same Wiener matrix. Gaussianity is unnecessary for optimality among affine estimators with these second moments. Gaussianity is what additionally makes the posterior mean affine and makes it equal to the MAP estimate. With non-Gaussian distributions, the best affine estimator need not be the best unrestricted estimator or the posterior mode.

## Derive the frequency-domain filter

A diagonal frequency-domain formula requires more structure than a general linear acquisition model. Assume periodic convolution and noise and prior covariances diagonalized by the same unitary discrete Fourier transform. With transform matrix $$U$$,

$$
\begin{aligned}
A&=U^*\operatorname{diag}(h_\omega)U,\\
C_0&=U^*\operatorname{diag}(S_x(\omega))U,\\
R&=U^*\operatorname{diag}(S_\epsilon(\omega))U.
\end{aligned}
$$

The star denotes conjugate transpose. The spectra are variances of the corresponding centred Fourier coefficients under this normalization.

Substitution into the Wiener matrix makes every frequency independent in the matrix calculation:

$$
\widehat x_\omega
=
(x_0)_\omega
+
\frac{
S_x(\omega)\overline{h_\omega}
}{
|h_\omega|^2S_x(\omega)+S_\epsilon(\omega)
}
\left[y_\omega-h_\omega(x_0)_\omega\right].
$$

For positive signal spectrum, the correction factor can be written

$$
W_\omega
=
\frac{\overline{h_\omega}}
{|h_\omega|^2+S_\epsilon(\omega)/S_x(\omega)}.
$$

The conjugate comes from the adjoint acquisition operator. The extra denominator term limits noise amplification where the acquisition response is weak.

With a white prior and white noise,

$$
S_x(\omega)=\tau^2,
\qquad
S_\epsilon(\omega)=\sigma^2,
$$

so

$$
W_\omega
=
\frac{\overline{h_\omega}}{|h_\omega|^2+\lambda},
\qquad
\lambda=\frac{\sigma^2}{\tau^2}.
$$

This is the frequency-domain identity-penalty Tikhonov solution. If the acquisition response is zero and the noise variance is positive, the correction is zero: that frequency remains at its prior mean.

If a full-rank penalty operator shares the Fourier basis, with response $$l_\omega$$, its Gaussian prior has spectrum

$$
S_x(\omega)=\frac{\tau^2}{|l_\omega|^2}.
$$

This follows by inverting the diagonal prior precision. With white noise, substitution gives the general quadratic-penalty filter

$$
W_\omega
=
\frac{\overline{h_\omega}}
{|h_\omega|^2+\lambda|l_\omega|^2}.
$$

A derivative penalty with a zero response needs the null-space treatment described earlier rather than an ordinary finite prior variance at that frequency.

For finite images, stationarity alone does not guarantee exact diagonalization by the discrete Fourier transform. Periodic boundary assumptions produce circulant structure; other boundaries generally produce different matrices. An FFT implementation therefore encodes a boundary model as well as a filtering formula.

## A two-mode reconstruction with every number specified

Treat two coordinates as image modes, one well observed and one attenuated. Construct

$$
A=
\begin{pmatrix}
1&0\\
0&0.1
\end{pmatrix},
\qquad
x_0=
\begin{pmatrix}0\\0\end{pmatrix},
\qquad
C_0=I,
\qquad
R=0.01I.
$$

Choose a true vector and one noise realization:

$$
x_{\mathrm{true}}=
\begin{pmatrix}1\\1\end{pmatrix},
\qquad
\epsilon=
\begin{pmatrix}0\\0.1\end{pmatrix}.
$$

The observation is exactly

$$
y=Ax_{\mathrm{true}}+\epsilon
=
\begin{pmatrix}1\\0.2\end{pmatrix}.
$$

Unregularized inversion gives

$$
\widehat x_{\mathrm{ML}}
=
\begin{pmatrix}1\\2\end{pmatrix}.
$$

The noise in the second observation has been multiplied by ten.

The prior and noise scales give regularization weight $$\lambda=0.01$$. The Tikhonov equations are

$$
\begin{pmatrix}
1.01&0\\
0&0.02
\end{pmatrix}
\widehat x
=
\begin{pmatrix}1\\0.02\end{pmatrix}.
$$

Therefore

$$
\widehat x_{\mathrm{MAP}}
=
\begin{pmatrix}
1/1.01\\
0.02/0.02
\end{pmatrix}
=
\begin{pmatrix}
0.990099\ldots\\
1
\end{pmatrix}.
$$

The posterior precision and covariance are

$$
H=
\begin{pmatrix}
101&0\\
0&2
\end{pmatrix},
\qquad
C_{\mathrm{post}}
=
\begin{pmatrix}
1/101&0\\
0&1/2
\end{pmatrix}.
$$

| Quantity | Well-observed mode | Attenuated mode |
|---|---:|---:|
| Prior variance | $$1$$ | $$1$$ |
| Posterior variance | $$0.009901\ldots$$ | $$0.5$$ |
| ML estimate | $$1$$ | $$2$$ |
| MAP estimate | $$0.990099\ldots$$ | $$1$$ |

The second reconstructed value happens to equal the constructed truth. That coincidence is not an accuracy estimate. The posterior variance still shows substantially less information about that mode.

The penalized objective can also be checked. Under unregularized inversion, the residual is zero, but the penalty is

$$
0.01(1^2+2^2)=0.05.
$$

At the MAP estimate,

$$
\lVert y-A\widehat x\rVert^2
=
(1-1/1.01)^2+0.1^2
\approx0.010098030,
$$

and

$$
0.01\lVert\widehat x\rVert^2
=
0.01\left[(1/1.01)^2+1\right]
\approx0.019802960.
$$

The total is approximately $$0.029900990$$, below the unregularized solution's penalized objective. The reconstruction accepts a residual because exact measurement fit would amplify a direction that the model regards as uncertain.

## Markov priors express local dependence through precision

A large joint image distribution can be specified directly. A Gaussian prior is one example. The challenge is representing and computing with its structure efficiently, not the logical impossibility of writing a joint distribution.

Let $$D$$ contain finite-difference rows for neighbouring pixels. Each row subtracts one neighbour from the other. Then

$$
\lVert Dx\rVert^2
=
\sum_{(i,j)\in\mathcal E}(x_i-x_j)^2,
$$

so a quadratic smoothness penalty has precision proportional to $$D^\top D$$. Adding a positive diagonal anchor gives a proper example:

$$
P=\tau^{-2}D^\top D+\kappa I,
\qquad
\kappa>0.
$$

To see the Markov property, take a centred Gaussian with precision $$P$$. Keeping only terms involving one coordinate,

$$
\log p(x_i\mid x_{-i})
=
-\frac12P_{ii}x_i^2
-x_i\sum_{j\ne i}P_{ij}x_j
+\text{constant}.
$$

Completing the square gives conditional mean and variance

$$
\mathbb E[x_i\mid x_{-i}]
=
-\frac1{P_{ii}}\sum_{j\ne i}P_{ij}x_j,
\qquad
\operatorname{Var}(x_i\mid x_{-i})=\frac1{P_{ii}}.
$$

Zero off-diagonal precision entries remove the corresponding coordinates from this conditional distribution. Sparse precision therefore expresses local conditional dependence. Covariance can still connect distant pixels.

A local Markov assumption does not, by itself, make all inference or normalization easy. Pairwise potentials are a modelling choice, and nonquadratic potentials generally lose the Gaussian linear-system solution.

The smoothing effect can be checked with two pixels. Take identity acquisition, observation $$y=(0,2)$$, and objective

$$
J(x_1,x_2)
=
x_1^2+(x_2-2)^2+\lambda(x_2-x_1)^2.
$$

Define their average and contrast:

$$
a=\frac{x_1+x_2}{2},
\qquad
d=x_2-x_1.
$$

Substitution gives

$$
J(a,d)
=
2(a-1)^2+\frac12(d-2)^2+\lambda d^2.
$$

Differentiating yields

$$
a=1,
\qquad
d=\frac2{1+2\lambda}.
$$

For regularization weight one, the reconstructed pixels are

$$
(x_1,x_2)=\left(\frac23,\frac43\right).
$$

The average is preserved, but the contrast shrinks from two to two thirds. A quadratic neighbour prior suppresses sharp differences because that is exactly what its penalty rewards. Whether a sharp difference is noise or a meaningful structure requires additional information.

## Unknown acquisition parameters connect back to EM

The closed forms above assume the operator and uncertainty scales are known. If they are estimated from the same data, the inference problem changes. A learned reconstruction also need not correspond to an explicit normalized image prior merely because it produces plausible images.

For a concrete EM connection, suppose the forward operator and image prior are fixed but white-noise variance is unknown. The image is latent. Under the old variance, let its posterior mean and covariance be $$\mu$$ and $$C$$.

Expanding around the posterior mean gives

$$
\mathbb E[\lVert y-Ax\rVert^2\mid y]
=
\lVert y-A\mu\rVert^2
+\operatorname{tr}(ACA^\top).
$$

The cross term vanishes because the centred image has conditional mean zero. The trace is the expected squared measurement-space deviation due to image uncertainty.

Writing the candidate variance as $$s$$, its auxiliary objective is

$$
Q(s)
=
-\frac m2\log s
-\frac1{2s}
\mathbb E[\lVert y-Ax\rVert^2\mid y]
+\text{constant}.
$$

Differentiate, set to zero, and solve:

$$
s_{\mathrm{new}}
=
\frac{
\lVert y-A\mu\rVert^2+\operatorname{tr}(ACA^\top)
}{m}.
$$

Replacing the latent image by its posterior mean alone would omit the nonnegative uncertainty term. This is a concrete reason the E step takes an expectation of the complete-data objective rather than filling in a single reconstructed image.

## Revision checklist

| Can I reconstruct this without looking? | Check |
|---|---|
| How does a noise model produce a likelihood? | Evaluate its density at the forward-model residual. |
| When is the data term ordinary squared error? | Independent equal-variance additive Gaussian noise. |
| Does maximum likelihood generally return the observation? | Only in special cases such as unconstrained identity acquisition. |
| Why does a Gaussian prior give regularization? | Its negative log density is a quadratic penalty. |
| What is the posterior precision? | Acquisition information plus prior precision. |
| When do MAP and posterior mean coincide here? | Under the unconstrained linear Gaussian model. |
| What is the Tikhonov weight in this convention? | Noise variance divided by prior scale variance. |
| When is a derivative-penalty reconstruction unique? | Acquisition and penalty operators have no shared nonzero null direction. |
| Does the Wiener estimator require Gaussianity? | Its best-affine property does not; its identification with Gaussian MAP does. |
| What permits independent Fourier filtering? | Simultaneous Fourier diagonalization, including compatible boundary assumptions. |
| What does sparse Gaussian precision encode? | Conditional dependence on a limited set of coordinates. |
| What does the EM noise update add beyond a fitted residual? | The posterior uncertainty trace term. |

## Why it matters for my work

An acquisition model makes scanner and protocol assumptions explicit. A restoration prior can suppress the same small structures a downstream diagnostic task needs, so reconstruction quality and preservation of relevant evidence must be assessed separately.

## What I have not resolved

Which parts of ultrasound acquisition can be modelled usefully from available metadata, and how operator choices should enter that model without being absorbed into the image prior?
