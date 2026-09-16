---
layout: study_note
title: "Choosing the Loss: Squared Error, Absolute Error, and What Each One Believes"
description: "Squared error, absolute error and Huber loss: deriving their prediction targets, checking how one bad point affects a fit, and understanding weighted classification losses."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "algebra-and-optimization"
category_title: "Linear Algebra & Optimization"
subgroup: "Losses & Gradient Optimization"
order: 4
source: "Independent study"
written: true
updated: "2026-09-15"
---

A loss determines which prediction is optimal for a given distribution of outcomes. Squared error asks for a conditional mean. Absolute error asks for a conditional median. Asymmetric absolute error asks for a conditional quantile. These can be different answers even with unlimited data and perfect optimization.

Choosing a loss therefore involves more than making gradients convenient. It specifies a target, gives different observations different influence, and determines what a fitted output can mean.

## Separate the prediction target from its fitted approximation

Let an input and outcome have a joint distribution, and let a predictor return an action or estimate. Population risk is

$$
R(f)=\mathbb E[\ell(f(X),Y)].
$$

Using conditional expectation,

$$
R(f)
=
\mathbb E_X
\left[
\mathbb E[\ell(f(X),Y)\mid X]
\right].
$$

If the predictor can choose its output independently at every input, minimizing population risk reduces to the pointwise problem

$$
a^\star(x)
\in
\arg\min_a
\mathbb E[\ell(a,Y)\mid X=x].
$$

This is the prediction target implied by the loss.

Actual learning introduces further restrictions. We choose a parameterized model and minimize an empirical objective such as

$$
\widehat R(\theta)
=
\frac1n\sum_{i=1}^n
\ell(f_\theta(x_i),y_i)
+
\lambda\Omega(\theta).
$$

Finite data, a restricted model family, regularization, and imperfect optimization can all prevent the fitted function from reaching the population target.

A loss can be selected through validation or learned within a larger system. That does not remove the need for an external criterion: the selection procedure still needs to know what counts as success. There is no mathematical rule saying that loss functions cannot be searched, but a search cannot supply its own scientific objective.

## Why squared error estimates a mean

Fix an input and write its conditional mean as

$$
\mu=\mathbb E[Y\mid X=x].
$$

Assume the conditional second moment is finite. Expand the squared error:

$$
\begin{aligned}
\mathbb E[(Y-a)^2\mid X=x]
&=
\mathbb E[((Y-\mu)+(\mu-a))^2\mid X=x]\\
&=
\mathbb E[(Y-\mu)^2\mid X=x]
+
2(\mu-a)\mathbb E[Y-\mu\mid X=x]\\
&\qquad+(\mu-a)^2.
\end{aligned}
$$

The middle term vanishes by the definition of the mean. Therefore

$$
\mathbb E[(Y-a)^2\mid X=x]
=
\operatorname{Var}(Y\mid X=x)+(\mu-a)^2.
$$

Only the second term depends on the prediction, so the unique optimum is

$$
a^\star(x)=\mu.
$$

Normality was not used. Squared error targets a mean for any conditional distribution with a finite second moment.

This matters when explaining what a regression model predicts. A mean can lie in a region where few outcomes occur. If an outcome takes only zero and four, a prediction of one need not represent a typical observed outcome. It can still be the optimal squared-error prediction.

## Why absolute error estimates a median

Consider

$$
R_1(a)=\mathbb E[\lvert Y-a\rvert].
$$

When the outcome distribution is continuous, differentiating with respect to the prediction gives

$$
R_1'(a)
=
P(Y<a)-P(Y>a)
=
2F(a)-1.
$$

Increasing the prediction increases the error for outcomes below it and decreases the error for outcomes above it. The optimum balances those two probabilities:

$$
F(a)=\frac12.
$$

With atoms, ordinary derivatives may not exist. The left and right derivatives give the more general condition

$$
F(a^-)\le\frac12\le F(a).
$$

That is exactly the definition of a median. There can be an interval of minimizers, as happens for an even sample whose two middle values differ.

Now use a fully specified distribution:

$$
P(Y=0)=\frac34,
\qquad
P(Y=4)=\frac14.
$$

Its mean is one and its median is zero.

Under squared error,

$$
R_2(0)=\frac34(0)^2+\frac14(4)^2=4,
$$

while

$$
R_2(1)=\frac34(1)^2+\frac14(3)^2=3.
$$

Under absolute error,

$$
R_1(0)=\frac34(0)+\frac14(4)=1,
$$

while

$$
R_1(1)=\frac34(1)+\frac14(3)=1.5.
$$

The losses disagree because they ask different questions. Neither calculation needs contamination, an optimization failure, or an inaccurate model.

## Deriving linear least squares and its assumptions

For linear predictions, collect the input vectors as rows of a design matrix. Include a constant column if an intercept is required. The objective is

$$
J(w)=\frac12\lVert Xw-y\rVert^2.
$$

Set the residual vector to

$$
r=Xw-y.
$$

Its differential is

$$
dr=X\,dw,
$$

so

$$
dJ=r^{\mathsf T}dr
=r^{\mathsf T}X\,dw.
$$

Reading off the column gradient gives

$$
\nabla_wJ=X^{\mathsf T}(Xw-y).
$$

A stationary point therefore satisfies the normal equations:

$$
X^{\mathsf T}Xw=X^{\mathsf T}y.
$$

The Hessian is

$$
\nabla_w^2J=X^{\mathsf T}X.
$$

For any direction,

$$
v^{\mathsf T}X^{\mathsf T}Xv
=
\lVert Xv\rVert^2\ge 0.
$$

Thus the objective is convex in the linear coefficients. It is strictly convex, with a unique minimizer, when the columns are linearly independent. Only under that rank condition can we write

$$
\widehat w=(X^{\mathsf T}X)^{-1}X^{\mathsf T}y.
$$

If columns are dependent, predictions may still be uniquely determined while coefficients are not.

In computation, solving the least-squares system using a suitable factorization avoids explicitly constructing this inverse. The formula explains the estimator; it does not prescribe the numerically best implementation.

Also, squared error being convex in its prediction does not make a neural network's objective convex in its parameters. Composition with a non-linear parameterization changes the optimization problem.

## One contaminated observation, with the entire dataset specified

Start with ten inputs and an exact line:

$$
x_i=i,\qquad y_i=2i+1,\qquad i=1,\ldots,10.
$$

The clean responses are

$$
3,5,7,9,11,13,15,17,19,21.
$$

Increase only the response at input six by fifty. The observed responses become

$$
3,5,7,9,11,63,15,17,19,21.
$$

For a line with an intercept, the least-squares slope and intercept follow from the normal equations:

$$
\widehat b
=
\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}
{\sum_i(x_i-\bar x)^2},
\qquad
\widehat a=\bar y-\widehat b\bar x.
$$

Here

$$
\bar x=\frac{11}{2},
\qquad
\bar y=17,
$$

and

$$
S_{xx}
=
\sum_{i=1}^{10}\left(i-\frac{11}{2}\right)^2
=
\frac{165}{2}.
$$

For the clean line, the cross-product sum is twice this quantity. The contamination changes it by

$$
50\left(6-\frac{11}{2}\right)=25.
$$

Therefore

$$
S_{xy}=165+25=190,
$$

and

$$
\widehat b
=
\frac{190}{165/2}
=
\frac{76}{33}
\approx 2.30303.
$$

The intercept is

$$
\widehat a
=
17-\frac{76}{33}\frac{11}{2}
=
\frac{13}{3}
\approx 4.33333.
$$

The relative change in slope is

$$
\frac{76/33-2}{2}
=
\frac5{33}
\approx 0.151515.
$$

Every number follows from the listed observations.

For this particular construction, least absolute deviations recovers the clean line exactly. That claim can also be proved without relying on a solver.

Write a candidate line as the clean line plus an affine perturbation:

$$
\delta(x)=u+vx.
$$

Its absolute-error objective minus the clean line's objective is

$$
\sum_{i\ne 6}\lvert\delta(i)\rvert
+
\lvert 50-\delta(6)\rvert
-50.
$$

The reverse triangle inequality bounds this below by

$$
\sum_{i\ne 6}\lvert\delta(i)\rvert-\lvert\delta(6)\rvert.
$$

Because six is the midpoint of five and seven,

$$
\delta(6)=\frac{\delta(5)+\delta(7)}2,
$$

so

$$
\lvert\delta(5)\rvert+\lvert\delta(7)\rvert
\ge 2\lvert\delta(6)\rvert.
$$

If the perturbation at six is non-zero, the objective increase is strictly positive. If it is zero but the affine perturbation is not identically zero, at least one clean observation has a non-zero residual, again giving a strictly positive increase.

Thus the clean line is the unique absolute-error optimum here. The proof depends on this construction; it is not a claim that absolute-error regression always ignores one corrupted observation.

## Residual influence is only part of robustness

For a residual defined as prediction minus outcome,

$$
r_i=w^{\mathsf T}x_i-y_i,
$$

let

$$
\psi(r)=\frac{d\ell(r)}{dr}
$$

where the derivative exists. The contribution to the coefficient gradient is

$$
\nabla_w\ell(r_i)=\psi(r_i)x_i.
$$

For squared error,

$$
\psi(r)=2r.
$$

For absolute error away from zero,

$$
\psi(r)=\operatorname{sign}(r).
$$

The squared-error contribution grows without bound as the residual grows. Absolute error bounds the residual-dependent factor.

But the input vector remains. A large or badly positioned input can have substantial leverage even when the residual score is bounded. Robustness to unusual outcomes and robustness to unusual inputs are different issues.

Nor does a large residual prove that a record is wrong. It can represent a valid rare outcome, model misspecification, or an omitted subgroup. Reducing its influence changes what the fitted model prioritizes. That change should be justified by the target and data-generating assumptions, not by declaring inconvenient observations uninteresting.

## Huber loss and an exact compromise example

Huber loss combines a quadratic centre with linear tails:

$$
\ell_\delta(r)
=
\begin{cases}
\frac12r^2,&\lvert r\rvert\le\delta,\\
\delta\lvert r\rvert-\frac12\delta^2,&\lvert r\rvert>\delta.
\end{cases}
$$

The subtraction in the tail is chosen for continuity. At the positive threshold, both pieces equal half the squared threshold. Their derivatives also agree:

$$
\psi_\delta(r)
=
\begin{cases}
r,&\lvert r\rvert\le\delta,\\
\delta\operatorname{sign}(r),&\lvert r\rvert>\delta.
\end{cases}
$$

Thus the function is differentiable, although its second derivative changes abruptly at the thresholds. Its derivative is non-decreasing, which establishes convexity.

Take an intercept-only dataset consisting of nine zeros and one observation of fifty.

Squared error selects the mean:

$$
a_{\mathrm{square}}=5.
$$

Absolute error selects the median:

$$
a_{\mathrm{absolute}}=0.
$$

For Huber loss with threshold one, suppose the optimum lies between zero and one. The nine clean residuals then use the quadratic branch, while the large observation contributes a clipped derivative of negative one. Stationarity gives

$$
9a-1=0,
$$

so

$$
a_{\mathrm{Huber}}=\frac19.
$$

This lies in the assumed interval, and the contaminated residual remains in the linear tail. Since the objective is convex, the stationary point is globally optimal.

The threshold has units of the response. Multiplying all outcomes by a constant while leaving the threshold unchanged alters which residuals are treated as central and which are treated as tail observations. A threshold should therefore be interpreted relative to a meaningful residual scale.

Non-smooth objectives are not beyond optimization. Absolute-error regression can be written as a linear program using auxiliary variables:

$$
\min_{w,t}\sum_i t_i
$$

subject to

$$
-t_i\le x_i^{\mathsf T}w-y_i\le t_i.
$$

This formulation also forces non-negative auxiliary variables. Subgradient methods, proximal methods, and suitable constrained solvers provide other approaches. Ordinary differentiable gradient descent is not the complete description.

## Likelihood explains familiar losses, but does not define their only use

Assume independent Gaussian residuals with a common fixed variance:

$$
p(y_i\mid x_i,w)
=
\frac1{\sqrt{2\pi}\sigma}
\exp\left(
-\frac{(y_i-x_i^{\mathsf T}w)^2}{2\sigma^2}
\right).
$$

The negative log-likelihood is

$$
-\log p(y\mid X,w)
=
n\log(\sqrt{2\pi}\sigma)
+
\frac1{2\sigma^2}\sum_i r_i^2.
$$

For a fixed scale, minimizing it is equivalent to least squares.

For independent Laplace residuals with fixed scale,

$$
p(r_i)=\frac1{2b}\exp\left(-\frac{\lvert r_i\rvert}{b}\right),
$$

the negative log-likelihood is

$$
n\log(2b)+\frac1b\sum_i\lvert r_i\rvert.
$$

Its minimizer is the absolute-error fit.

If Gaussian variances differ across observations and are known, the same calculation gives

$$
\sum_i\frac{r_i^2}{2\sigma_i^2}
$$

plus terms independent of the regression coefficients. Inverse-variance weighting follows from a particular probabilistic model.

These connections explain why the losses arise. They do not mean that using squared error asserts Gaussianity in every application. The conditional-mean derivation required no Gaussian distribution.

There is also no universal rule that usable residual powers lie between one and two. For powers greater than one, the second derivative away from zero is

$$
\frac{d^2}{dr^2}\lvert r\rvert^p
=
p(p-1)\lvert r\rvert^{p-2}\ge 0.
$$

Powers above two are convex and deliberately penalize large deviations more strongly. Powers below one are non-convex. Neither fact alone determines whether the scientific objective is appropriate.

## Asymmetric error costs lead to quantiles

Suppose underprediction and overprediction have different costs. Define the residual as outcome minus prediction and use the pinball loss:

$$
\rho_\tau(r)
=
\begin{cases}
\tau r,&r\ge 0,\\
(\tau-1)r,&r<0,
\end{cases}
\qquad
0<\tau<1.
$$

Underprediction receives slope proportional to the chosen quantile level; overprediction receives slope proportional to its complement.

For a continuous outcome distribution, differentiating expected loss with respect to the prediction gives

$$
\frac{d}{da}\mathbb E[\rho_\tau(Y-a)]
=
-\tau P(Y>a)+(1-\tau)P(Y<a).
$$

Therefore

$$
R'(a)=F(a)-\tau,
$$

and the optimum satisfies

$$
F(a)=\tau.
$$

With atoms, the condition is

$$
F(a^-)\le\tau\le F(a).
$$

The median is the special case with equal costs. The loss does not estimate the mean and then attach a different interpretation to it; it changes the population target from the start.

## Classification loss, probabilities, and class weighting

Let the true conditional probability of the positive class be

$$
p=P(Y=1\mid X=x),
$$

and let the model report a probability in the open unit interval. Binary log loss has conditional risk

$$
R(q)=-p\log q-(1-p)\log(1-q).
$$

Its derivative is

$$
R'(q)
=
-\frac pq+\frac{1-p}{1-q}
=
\frac{q-p}{q(1-q)}.
$$

The derivative changes sign at the true probability, so the unique optimum is

$$
q^\star=p
$$

when the true probability is interior. Boundary probabilities are obtained as limits.

For a logit,

$$
q=\frac1{1+e^{-z}},
$$

substitution gives the loss

$$
\ell(z,y)=\log(1+e^z)-yz.
$$

Differentiating gives

$$
\frac{\partial\ell}{\partial z}=q-y.
$$

This explains why the output error appears directly in logistic-regression gradients.

Now give positive examples weight one constant and negative examples another:

$$
R(q)
=
-a p\log q-b(1-p)\log(1-q).
$$

Stationarity gives

$$
q^\star
=
\frac{ap}{ap+b(1-p)}.
$$

Weighted log loss generally targets a transformed probability. For the constructed values

$$
p=0.1,\qquad a=9,\qquad b=1,
$$

the optimum is

$$
q^\star=\frac{0.9}{0.9+0.9}=\frac12.
$$

A raw output of one half therefore does not represent the original positive-class probability in this ideal weighted problem.

If weights and the ideal relationship are known, the inverse transformation is

$$
p
=
\frac{bq}{a(1-q)+bq}.
$$

Finite model capacity and imperfect optimization mean this algebra alone does not establish calibration in a fitted model.

A separate decision threshold can encode misclassification costs. If a false positive costs one specified amount and a false negative another, the expected costs of the two actions are

$$
\operatorname{Cost}(+)=c_{\mathrm{FP}}(1-p),
\qquad
\operatorname{Cost}(-)=c_{\mathrm{FN}}p.
$$

Choose the positive action when

$$
p>
\frac{c_{\mathrm{FP}}}{c_{\mathrm{FP}}+c_{\mathrm{FN}}}.
$$

Probability estimation and action selection can therefore be separate stages. Class imbalance does not by itself dictate a particular training weight.

Finally, loss normalization affects regularization. The objectives

$$
\sum_i\ell_i+\lambda\Omega
$$

and

$$
\frac1n\sum_i\ell_i+\lambda\Omega
$$

do not express the same tradeoff at the same numerical regularization coefficient. Multiplying the second objective by the sample count makes the difference explicit.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| Derive the squared-error target | Decompose risk into variance and squared bias |
| Derive the absolute-error target | Balance probability on either side of a median |
| Obtain the normal equations | State the rank condition for an inverse |
| Reproduce the contaminated-line coefficients | Use the explicitly listed observations |
| Prove the absolute-error result for that construction | Use the midpoint inequality |
| Distinguish residual robustness from leverage | Keep the input factor in the gradient |
| Derive the Huber estimate for nine zeros and one large value | Solve the clipped-score equation |
| Connect losses to likelihoods | Identify fixed scales and independence assumptions |
| Derive a quantile target | Differentiate asymmetric absolute risk |
| Interpret weighted log loss | Derive its transformed probability |
| Separate estimation from decisions | Derive a cost-based threshold |
| Compare regularized objectives | Check sum versus mean normalization |

## Why it matters for my work

Loss choice should follow the quantity I want to estimate and the errors I want to penalize. A discrepancy between robust and squared-error fits is a reason to inspect labels, leverage, and model assumptions, not proof that the robust fit is correct.

## What I have not resolved

I need to determine which extreme residuals in my datasets are recording errors and which represent valid cases that the model must handle. A loss function alone cannot make that distinction.
