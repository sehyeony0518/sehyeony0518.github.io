---
layout: study_note
title: "Linear MMSE Estimation and the Wiener Filter"
description: "The best linear estimate of one quantity from another, and why it needs only means and covariances rather than a distribution."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "signals-and-systems"
category_title: "Signals, Systems & Transforms"
order: 8
source: "Independent study"
written: true
updated: "2026-09-15"
---

Linear minimum mean-square error estimation chooses the best affine estimate under an expected squared-error criterion. Its central idea is geometric: once the estimate is optimal, no allowed linear adjustment based on the observations can improve it.

That statement becomes the orthogonality principle, which becomes the normal equations, which becomes the Wiener filter when the observations are samples of a stationary process.

The assumptions must be separated carefully. Finite-vector LMMSE estimation does not require stationarity. Wide-sense stationarity is what gives the time-series problem a shift-invariant covariance structure and permits the usual spectral Wiener solution.

All examples below specify their random variables or processes explicitly. Their numbers are population calculations from those constructions, not measured denoising results.

## Define the estimator and the loss

Let the target and observation be real random vectors:

$$
x\in\mathbb R^p,
\qquad
y\in\mathbb R^q.
$$

Assume finite second moments. Restrict the estimate to

$$
\widehat x=Ay+b,
$$

where

$$
A\in\mathbb R^{p\times q},
\qquad
b\in\mathbb R^p.
$$

The objective is

$$
J(A,b)
=
\mathbb E\left[\|x-Ay-b\|^2\right].
$$

“Linear MMSE” commonly includes this affine form. The offset is essential when the variables have nonzero means.

The expectation is over the joint distribution of target and observation. The estimator is chosen before seeing a particular observation, and its performance is averaged over that distribution.

Squared error makes large residuals contribute disproportionately, but it also creates a quadratic optimisation problem. Once a candidate's residual is orthogonal to every permitted adjustment, the remaining change in loss is nonnegative.

The affine restriction is separate from the loss choice. A nonlinear function of the same observation may have lower squared error. The derivation establishes optimality only within the stated class.

## Derive orthogonality by perturbing the estimate

Let a candidate residual be

$$
e=x-\widehat x.
$$

Consider any allowed change to the estimator:

$$
v=\Delta A\,y+\Delta b.
$$

For a real scalar perturbation size, use

$$
\widehat x_\varepsilon
=
\widehat x+\varepsilon v.
$$

Its residual is

$$
e_\varepsilon=e-\varepsilon v.
$$

Expand the loss directly:

$$
\begin{aligned}
J(\varepsilon)
&=\mathbb E[(e-\varepsilon v)^\top(e-\varepsilon v)]\\
&=
\mathbb E[e^\top e]
-2\varepsilon\mathbb E[e^\top v]
+\varepsilon^2\mathbb E[v^\top v].
\end{aligned}
$$

If the middle expectation were nonzero, a sufficiently small perturbation with the appropriate sign would decrease the loss. Therefore every optimum must satisfy

$$
\boxed{
\mathbb E[e^\top v]=0
\quad\text{for every allowed }v
}.
$$

This is the orthogonality principle.

It is also sufficient. If the middle term vanishes for every allowed change, then

$$
J(\varepsilon)
=
J(0)+\varepsilon^2\mathbb E[\|v\|^2]
\ge J(0).
$$

The argument proves global optimality, not merely that a derivative happens to vanish.

The word “orthogonal” uses the inner product between random quantities defined by expectation. It does not mean that the residual and observation multiply to zero for every individual outcome.

Nor does it mean independence. The residual can still depend nonlinearly on the observation even when all these expected linear products vanish.

## Constants determine the mean; observations determine the normal equations

First allow only a constant perturbation. Orthogonality to every constant vector gives

$$
\mathbb E[e]=0.
$$

Substituting the residual yields

$$
\mu_x-A\mu_y-b=0,
$$

so

$$
\boxed{
b=\mu_x-A\mu_y
}.
$$

The estimator therefore passes through the population means.

Define centred variables

$$
\widetilde x=x-\mu_x,
\qquad
\widetilde y=y-\mu_y.
$$

Then the estimate can be written as

$$
\widehat x
=
\mu_x+A\widetilde y,
$$

and the residual becomes

$$
e=\widetilde x-A\widetilde y.
$$

Now choose perturbations that place one observation component into one target component. Orthogonality for every such choice is equivalent to

$$
\mathbb E[e\widetilde y^\top]=0.
$$

Define the observation covariance and cross-covariance:

$$
C_y
=
\mathbb E[\widetilde y\widetilde y^\top],
$$

$$
C_{xy}
=
\mathbb E[\widetilde x\widetilde y^\top].
$$

Substitution gives

$$
C_{xy}-AC_y=0.
$$

Thus the normal equations are

$$
\boxed{
AC_y=C_{xy}
}.
$$

The word “normal” refers to perpendicularity: the residual is perpendicular, in the expectation inner product, to the space spanned by the available observations.

If the observation covariance is invertible,

$$
\boxed{
A=C_{xy}C_y^{-1}
}.
$$

Combining the mean and covariance parts,

$$
\boxed{
\widehat x
=
\mu_x+
C_{xy}C_y^{-1}(y-\mu_y)
}.
$$

The multiplication order follows from the dimensions. Reversing it is generally invalid.

For computation, the formula describes a linear solve. One normally solves

$$
C_yA^\top=C_{xy}^\top
$$

instead of explicitly constructing a matrix inverse.

## Singular covariance and the meaning of nonunique coefficients

An observation covariance can be singular when some observation components are redundant.

Suppose a vector lies in its null space:

$$
C_yv=0.
$$

Then

$$
\mathbb E[(v^\top\widetilde y)^2]
=
v^\top C_yv
=
0.
$$

A nonnegative random quantity with zero expectation is zero almost surely, so

$$
v^\top\widetilde y=0
\quad\text{almost surely}.
$$

That direction contains no varying observation information. It also satisfies

$$
C_{xy}v
=
\mathbb E[\widetilde x(v^\top\widetilde y)]
=
0.
$$

The normal equations are therefore consistent for valid population covariances.

A minimum-norm coefficient solution uses the Moore–Penrose pseudoinverse:

$$
A_0=C_{xy}C_y^\dagger.
$$

Other solutions can differ in how they act on the observation covariance's null space. They still produce the same estimate almost surely because the centred observation has no component in that space.

This is a useful distinction: coefficients can be nonunique while the estimated random vector is unique.

For estimated covariances, near-singularity is also a numerical and statistical problem. Small errors in a weakly observed direction can cause large coefficient changes. A pseudoinverse does not automatically establish that the estimated statistics are accurate.

## Derive the minimum error covariance

Define the target covariance by

$$
C_x=\mathbb E[\widetilde x\widetilde x^\top].
$$

The residual covariance is

$$
\begin{aligned}
C_e
&=
\mathbb E[
(\widetilde x-A\widetilde y)
(\widetilde x-A\widetilde y)^\top
]\\
&=
C_x-AC_{yx}-C_{xy}A^\top+AC_yA^\top.
\end{aligned}
$$

At the optimum,

$$
AC_y=C_{xy}.
$$

The last term therefore cancels one cross term, giving, in the nonsingular case,

$$
\boxed{
C_e
=
C_x-C_{xy}C_y^{-1}C_{yx}
}.
$$

The expected squared norm is the sum of component error variances:

$$
J_{\min}
=
\mathbb E[e^\top e]
=
\operatorname{tr}(C_e).
$$

For scalar target and observation,

$$
a=\frac{\operatorname{Cov}(x,y)}{\operatorname{Var}(y)},
$$

and

$$
\operatorname{Var}(e)
=
\operatorname{Var}(x)
-
\frac{\operatorname{Cov}(x,y)^2}{\operatorname{Var}(y)}.
$$

The first term is the error variance from always predicting the target mean. The subtracted term is the reduction obtainable from the observation through an affine estimator.

If the covariance between target and observation is zero, that affine improvement is zero. This does not establish that the target and observation are unrelated; a nonlinear dependence may remain.

## A complete scalar example with four outcomes

Let the signal take values

$$
x\in\{-2,2\}
$$

with equal probability. Let independent noise take values

$$
w\in\{-1,1\}
$$

with equal probability, and observe

$$
y=x+w.
$$

The means are zero. Independence and symmetry give

$$
\mathbb E[xw]=0.
$$

The variances are

$$
C_x=4,
\qquad
C_w=1.
$$

Therefore,

$$
C_y
=
\mathbb E[(x+w)^2]
=
4+1
=
5,
$$

and

$$
C_{xy}
=
\mathbb E[x(x+w)]
=
4.
$$

The optimal affine estimator is

$$
\widehat x=\frac45y.
$$

All four outcomes have probability one quarter:

| $$x$$ | $$w$$ | $$y$$ | $$\widehat x$$ | $$e=x-\widehat x$$ | $$ey$$ | $$e^2$$ |
|---|---|---|---|---|---|---|
| $$-2$$ | $$-1$$ | $$-3$$ | $$-12/5$$ | $$2/5$$ | $$-6/5$$ | $$4/25$$ |
| $$-2$$ | $$1$$ | $$-1$$ | $$-4/5$$ | $$-6/5$$ | $$6/5$$ | $$36/25$$ |
| $$2$$ | $$-1$$ | $$1$$ | $$4/5$$ | $$6/5$$ | $$6/5$$ | $$36/25$$ |
| $$2$$ | $$1$$ | $$3$$ | $$12/5$$ | $$-2/5$$ | $$-6/5$$ | $$4/25$$ |

The residual mean is zero. Its product with the observation also averages to zero:

$$
\mathbb E[ey]
=
\frac14
\left(
-\frac65+\frac65+\frac65-\frac65
\right)
=
0.
$$

The mean-square error is

$$
\mathbb E[e^2]
=
\frac14
\left(
\frac4{25}+\frac{36}{25}+\frac{36}{25}+\frac4{25}
\right)
=
\frac45.
$$

The covariance formula gives the same answer:

$$
4-\frac{4^2}{5}=\frac45.
$$

Passing the observation through unchanged would have error equal to negative noise and mean-square error one. Always returning zero would have mean-square error four.

The example also exposes the affine restriction. Here the sign of the observation identifies the signal exactly:

$$
x=2\,\operatorname{sign}(y).
$$

That nonlinear estimator has zero error under this constructed distribution.

The affine residual is consequently orthogonal to the observation without being independent of it. In fact, the table makes the residual a deterministic function of the observation.

## Why unrestricted MMSE uses the conditional mean

Let

$$
m(y)=\mathbb E[x\mid y].
$$

For any estimator based on the observation, write

$$
x-g(y)
=
[x-m(y)]+[m(y)-g(y)].
$$

Squaring and taking expectations produces a cross term. Conditional on the observation,

$$
\mathbb E[x-m(y)\mid y]=0,
$$

so that cross term vanishes. Therefore,

$$
\begin{aligned}
\mathbb E[(x-g(y))^2]
={}&
\mathbb E[(x-m(y))^2]\\
&+
\mathbb E[(m(y)-g(y))^2].
\end{aligned}
$$

The second term is minimised by choosing the conditional mean itself.

LMMSE projects onto the smaller space of affine functions. Unrestricted MMSE projects onto all suitable functions of the observation. The four-outcome example shows that those two spaces can give different answers even when the LMMSE derivation is completely correct.

No Gaussian assumption was used in deriving the affine solution. Means and covariances suffice because the affine squared-error objective expands entirely into first- and second-order moments.

## Denoising as covariance-dependent shrinkage

For vector observations of the form

$$
y=x+w,
$$

assume zero-mean noise uncorrelated with the signal. After centring,

$$
C_y=C_x+C_w,
\qquad
C_{xy}=C_x.
$$

Thus,

$$
\boxed{
\widehat x
=
\mu_x+
C_x(C_x+C_w)^{-1}(y-\mu_x)
}.
$$

The scalar version is

$$
\widehat x
=
\mu_x+
\frac{\sigma_x^2}{\sigma_x^2+\sigma_w^2}
(y-\mu_x).
$$

The gain approaches one when signal variance dominates and approaches zero when noise variance dominates.

For matrices, this is not entrywise division. Correlations can mix coordinates, so the interpretation should be made in an appropriate basis.

For example, suppose the noise covariance is

$$
C_w=\sigma_w^2I
$$

and diagonalise the signal covariance:

$$
C_x=U\Lambda U^\top,
\qquad
U^\top U=I.
$$

Substituting and cancelling the orthogonal factors gives

$$
A
=
U\Lambda(\Lambda+\sigma_w^2I)^{-1}U^\top.
$$

In the covariance eigenvector basis, each mode is multiplied by

$$
\frac{\lambda_i}{\lambda_i+\sigma_w^2}.
$$

The filter therefore shrinks directions according to their signal variance relative to noise variance.

This does not mean that every small individual signal value must be attenuated more than every large one. The weights are fixed by population second-order structure, and the estimator is applied to deviations from the mean. The scalar construction's same gain was applied to every observation.

If signal and noise are correlated, the simple covariance sums omit cross terms. The general LMMSE formula remains applicable, but the simplified denoising ratio does not.

## From vectors to stationary time-series filtering

Let the target and observed processes be zero mean for now. Restrict the estimator to a fixed linear filter:

$$
\widehat x[n]
=
\sum_{k\in\mathcal I}h[k]y[n-k].
$$

The allowed tap set defines the problem. It may contain a finite collection of past samples, all past and present samples, or samples on both sides of the target time.

For the standard stationary Wiener problem, assume the processes are jointly wide-sense stationary. Their means are constant, and all relevant covariance functions depend only on lag, including the cross-covariance:

$$
r_{yy}[\ell]
=
\mathbb E[y[n]y[n-\ell]],
$$

$$
r_{xy}[\ell]
=
\mathbb E[x[n]y[n-\ell]].
$$

Individual stationarity without stationary cross-covariance is insufficient for this joint estimation problem.

Orthogonality requires the error to be uncorrelated with every observation allowed in the estimate:

$$
\mathbb E[e[n]y[n-m]]=0,
\qquad m\in\mathcal I.
$$

Substitute the filter:

$$
r_{xy}[m]
-
\sum_{k\in\mathcal I}
h[k]\mathbb E[y[n-k]y[n-m]]
=
0.
$$

The lag between the two observations is

$$
(n-k)-(n-m)=m-k.
$$

Stationarity therefore gives the Wiener–Hopf normal equations:

$$
\boxed{
\sum_{k\in\mathcal I}
h[k]r_{yy}[m-k]
=
r_{xy}[m],
\qquad m\in\mathcal I
}.
$$

For a finite consecutive tap set, the covariance matrix has constant diagonals: each entry depends on the difference between its row and column indices. This is the Toeplitz structure supplied by stationarity.

## A two-tap Wiener filter from a constructed process

Let two mutually independent sequences consist of independent, equally likely values of minus one and one:

$$
u[n]\in\{-1,1\},
\qquad
v[n]\in\{-1,1\}.
$$

Define

$$
x[n]=u[n]+u[n-1],
$$

and observe

$$
y[n]=x[n]+v[n].
$$

All means are zero. Expanding products and using independence gives

$$
r_{xx}[0]=2,
$$

$$
r_{xx}[1]=r_{xx}[-1]=1,
$$

with zero covariance at larger lags. The unit-variance observation noise adds only to zero lag:

$$
r_{yy}[0]=3,
\qquad
r_{yy}[\pm1]=1.
$$

The cross-covariance is

$$
r_{xy}[0]=2,
\qquad
r_{xy}[\pm1]=1.
$$

Use only the current and previous observations:

$$
\widehat x[n]=h[0]y[n]+h[1]y[n-1].
$$

The normal equations are

$$
\begin{bmatrix}
3&1\\
1&3
\end{bmatrix}
\begin{bmatrix}
h[0]\\
h[1]
\end{bmatrix}
=
\begin{bmatrix}
2\\
1
\end{bmatrix}.
$$

From the first equation,

$$
h[1]=2-3h[0].
$$

Substitute into the second:

$$
h[0]+3(2-3h[0])=1,
$$

so

$$
h[0]=\frac58,
\qquad
h[1]=\frac18.
$$

The minimum error variance is

$$
\begin{aligned}
J_{\min}
&=
r_{xx}[0]
-
h[0]r_{xy}[0]
-
h[1]r_{xy}[1]\\
&=
2-\frac58\cdot2-\frac18\\
&=
\frac58.
\end{aligned}
$$

With only the current observation, the optimal gain would be

$$
\frac23
$$

and the error variance would be

$$
2-\frac{2^2}{3}=\frac23.
$$

The previous observation therefore reduces the error variance by

$$
\frac23-\frac58=\frac1{24}.
$$

That improvement follows from the shared latent sample in adjacent target values. Every covariance and error value is determined by the specified construction.

## Deriving the spectral Wiener solution

Now allow a two-sided filter with unrestricted integer tap locations. The normal equations hold for every integer lag:

$$
(h*r_{yy})[m]=r_{xy}[m].
$$

Assume sufficient regularity for the Fourier transforms below; absolutely summable covariance sequences are a convenient sufficient condition.

Define the spectra as transforms of the covariance functions:

$$
S_{yy}(\omega)
=
\sum_m r_{yy}[m]e^{-j\omega m},
$$

$$
S_{xy}(\omega)
=
\sum_m r_{xy}[m]e^{-j\omega m}.
$$

Transform the normal equations. Replacing the lag index by

$$
\ell=m-k
$$

separates the double sum:

$$
\begin{aligned}
&\sum_m\sum_k
h[k]r_{yy}[m-k]e^{-j\omega m}\\
&=
\left(\sum_kh[k]e^{-j\omega k}\right)
\left(\sum_\ell r_{yy}[\ell]e^{-j\omega\ell}\right).
\end{aligned}
$$

Therefore,

$$
H(\omega)S_{yy}(\omega)=S_{xy}(\omega),
$$

and wherever the observation spectrum is positive,

$$
\boxed{
H_{\mathrm{opt}}(\omega)
=
\frac{S_{xy}(\omega)}{S_{yy}(\omega)}
}.
$$

For additive noise uncorrelated with the signal at all lags,

$$
S_{xy}=S_{xx},
\qquad
S_{yy}=S_{xx}+S_{ww},
$$

so

$$
\boxed{
H_{\mathrm{opt}}(\omega)
=
\frac{S_{xx}(\omega)}
{S_{xx}(\omega)+S_{ww}(\omega)}
}.
$$

In the constructed process,

$$
S_{xx}(\omega)
=
2+e^{-j\omega}+e^{j\omega}
=
2+2\cos\omega,
$$

and

$$
S_{ww}(\omega)=1.
$$

Thus,

$$
H_{\mathrm{opt}}(\omega)
=
\frac{2+2\cos\omega}{3+2\cos\omega}.
$$

Its gains are

$$
H_{\mathrm{opt}}(0)=\frac45,
\qquad
H_{\mathrm{opt}}(\pi/2)=\frac23,
\qquad
H_{\mathrm{opt}}(\pi)=0.
$$

The zero at the highest frequency reflects the absence of signal power there in this construction. The observation still has noise power there.

This two-sided solution is a different estimator from the earlier two-tap causal filter. Its response is real, even, and nonconstant, so its impulse response is even and cannot be a nontrivial causal sequence. The simple spectral ratio must not be presented as an automatically causal implementation.

## What fails when the assumptions change

The formulas separate several assumptions that are often bundled together:

| Assumption or restriction | Its role | What changes when it fails |
|---|---|---|
| Finite second moments | Makes covariance and squared-error calculations finite. | The stated objective or covariance solution may be undefined. |
| Known means and covariances | Defines the population optimum. | Estimated statistics produce an estimated filter whose true risk must be assessed. |
| Affine estimation | Makes the objective depend only on second-order statistics. | Nonlinear estimators may exploit information absent from covariance. |
| Joint wide-sense stationarity | Produces lag-only covariances and a fixed convolutional solution. | Time-dependent covariances generally require time-dependent coefficients. |
| Uncorrelated additive noise | Gives the signal-plus-noise spectral ratio. | Cross-covariances must be retained. |
| Two-sided unrestricted filtering | Allows the pointwise spectral solution. | Causal or finite filters require their own constrained normal equations. |

Without stationarity, the finite-vector orthogonality argument still works. What disappears is the reason to use one fixed Toeplitz covariance matrix or one frequency response for every time.

Stationarity also does not by itself guarantee that averages along one observed record accurately estimate ensemble covariances. That substitution needs suitable ergodic assumptions and enough data.

Where the observation spectrum is zero, division is not defined. Valid joint statistics imply that the corresponding cross-spectrum is also zero there; the observations contain no energy in that component. Its filter value cannot be identified from a ratio and does not affect the estimate on that unsupported component.

Regularisation addresses a different issue. Adding a penalty

$$
\lambda\|A\|_F^2
$$

to the centred finite-vector objective changes the normal equations to

$$
A(C_y+\lambda I)=C_{xy}.
$$

This follows by expanding the quadratic penalty under the same coefficient perturbations. The resulting estimator can be more stable with estimated statistics, but it solves a modified objective. It is not automatically the unregularised population optimum.

Finally, truncating a noncausal Wiener impulse response or simply deleting its future taps does not generally produce the optimal causal filter. The retained observations are correlated, so changing the available tap set changes all the normal equations.

## Revision checklist

| Question | What I should be able to reproduce |
|---|---|
| Why must the residual be orthogonal to observations? | Expand the loss after an arbitrary allowed perturbation. |
| Why is orthogonality sufficient? | The remaining loss change is a nonnegative squared norm. |
| Where does the offset come from? | Orthogonality to constants forces the residual mean to zero. |
| How do the normal equations arise? | Substitute the centred residual into its cross-covariance with observations. |
| What does singular covariance mean? | Some observation directions vanish almost surely, allowing nonunique coefficients. |
| What does LMMSE optimality exclude? | Better nonlinear estimators and objectives other than squared error. |
| Where is stationarity needed? | In replacing time-pair covariances with lag-only functions. |
| Why is the spectral solution a ratio? | Fourier transformation turns the covariance convolution into multiplication. |
| Is the spectral ratio necessarily causal? | No; the allowed observation times define a separate constraint. |
| What must be checked with real data? | Statistical estimation, distribution changes, conditioning, and the validity of the signal-noise model. |

## Why it matters for my work

A denoising filter encodes which variations are expected to be signal and which are expected to be noise. I need to inspect that covariance model and its estimation data before interpreting a smoother output as a more faithful measurement.

## What I have not resolved

Estimate the relevant signal and noise covariances on appropriate data, test their stability across acquisition conditions, and compare affine estimation with a nonlinear baseline on held-out cases.
