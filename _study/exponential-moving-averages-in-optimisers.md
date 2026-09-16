---
layout: study_note
title: "The Exponential Moving Average: One Recursion Behind Momentum, RMSProp and Adam"
description: "Deriving the exponential moving average behind momentum, RMSProp and Adam, including bias correction, memory timescales, effective sample size and numerical updates."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "algebra-and-optimization"
category_title: "Linear Algebra & Optimization"
subgroup: "Losses & Gradient Optimization"
order: 7
source: "Independent study"
written: true
updated: "2026-09-15"
---

An exponential moving average stores a weighted history in a single state variable. In optimization, averaging gradients changes the update direction; averaging squared gradients changes the coordinatewise scale.

The recursion is simple, but several interpretations commonly attached to it are not equivalent. A decay timescale is not a literal window length. A squared-gradient average is not a variance. Bias correction normalizes startup weights; it does not make a changing gradient distribution stationary.

## Unrolling the finite recursion

For a scalar input sequence, define

$$
m_t=\beta m_{t-1}+(1-\beta)x_t,
\qquad
0\le\beta<1.
$$

Applying the recursion twice gives

$$
m_t
=
\beta^2m_{t-2}
+
(1-\beta)\beta x_{t-1}
+
(1-\beta)x_t.
$$

Continuing to the initial state yields the exact finite expression

$$
m_t
=
\beta^t m_0
+
(1-\beta)\sum_{j=1}^t\beta^{t-j}x_j.
$$

The contribution from the initial state is part of the result. With zero initialization, the data weights sum to

$$
(1-\beta)\sum_{k=0}^{t-1}\beta^k
=
1-\beta^t.
$$

They do not sum to one at finite time.

The familiar infinite-history expression,

$$
m_t=(1-\beta)\sum_{k=0}^{\infty}\beta^k x_{t-k},
$$

describes an indefinitely running filter under suitable boundedness or convergence conditions. It cannot simply replace the finite expression when analyzing the first few optimizer steps.

For vector inputs, the same recursion applies to every coordinate. One state value is required per coordinate rather than one scalar for the whole model. Adam maintains two such state arrays.

## Bias correction is finite-weight normalization

Suppose the input has the same expectation at every time:

$$
\mathbb E[x_t]=\mu,
$$

and initialize the state at zero. Taking expectations gives

$$
\mathbb E[m_t]
=
(1-\beta)\sum_{j=1}^t\beta^{t-j}\mu
=
(1-\beta^t)\mu.
$$

Dividing by the accumulated weight produces

$$
\widehat m_t=\frac{m_t}{1-\beta^t},
$$

with

$$
\mathbb E[\widehat m_t]=\mu.
$$

Independence is not required for this expectation calculation. A common expectation is required.

For a constant input, the correction is exact rather than merely correct on average:

$$
x_t=c
\quad\Longrightarrow\quad
m_t=c(1-\beta^t)
\quad\Longrightarrow\quad
\widehat m_t=c.
$$

For non-zero initialization, the data-only normalization would instead be

$$
\widehat m_t
=
\frac{m_t-\beta^tm_0}{1-\beta^t}.
$$

Some applications deliberately retain the initial state's contribution. That is a choice of averaging scheme, not an error that must always be corrected.

When input expectations change, the corrected state is still a weighted average:

$$
\mathbb E[\widehat m_t]
=
\frac{(1-\beta)\sum_{j=1}^t\beta^{t-j}\mathbb E[x_j]}
{1-\beta^t}.
$$

It need not equal the current expectation. Startup bias and tracking lag are different phenomena.

## A three-step example with every weight visible

Choose the decay and inputs

$$
\beta=\frac12,
\qquad
m_0=0,
\qquad
(x_1,x_2,x_3)=(2,4,-2).
$$

The raw states are

$$
m_1=1,
$$

$$
m_2=\frac12(1)+\frac12(4)=\frac52,
$$

and

$$
m_3=\frac12\left(\frac52\right)+\frac12(-2)=\frac14.
$$

The corrected values are:

| Step | Input | Raw state | Accumulated weight | Corrected state |
|---|---|---|---|---|
| $$1$$ | $$2$$ | $$1$$ | $$1/2$$ | $$2$$ |
| $$2$$ | $$4$$ | $$5/2$$ | $$3/4$$ | $$10/3$$ |
| $$3$$ | $$-2$$ | $$1/4$$ | $$7/8$$ | $$2/7$$ |

At the third step, the normalized weights on the observations are

$$
\left(\frac17,\frac27,\frac47\right).
$$

Thus the corrected value can be checked independently:

$$
\frac17(2)+\frac27(4)+\frac47(-2)
=
\frac27.
$$

It differs from the ordinary sample mean,

$$
\frac{2+4-2}{3}=\frac43,
$$

because the most recent negative observation has the largest weight. Bias correction does not turn an EMA into an equally weighted average.

## Several different meanings of memory

In the infinite-history representation, the weight assigned to an observation of age

$$
k
$$

is

$$
w_k=(1-\beta)\beta^k.
$$

The mass in the newest specified number of observations is

$$
\sum_{k=0}^{H-1}w_k=1-\beta^H.
$$

Consequently, a horizon close to

$$
H=\frac1{1-\beta}
$$

contains approximately a fraction

$$
1-e^{-1}
$$

of the mass when the decay is close to one. It does not contain all the mass.

The approximation follows by writing

$$
\beta=1-\varepsilon
$$

and using

$$
\log(1-\varepsilon)
=
-\varepsilon+O(\varepsilon^2).
$$

Then

$$
\beta^{1/(1-\beta)}
=
(1-\varepsilon)^{1/\varepsilon}
\longrightarrow e^{-1}.
$$

Other useful measures answer different questions.

The age at which an individual weight falls by half solves

$$
\beta^{h_{1/2}}=\frac12,
$$

so

$$
h_{1/2}=\frac{\log(1/2)}{\log\beta}.
$$

The e-folding age is

$$
h_e=-\frac1{\log\beta}.
$$

The mean age of the normalized infinite-history weights is

$$
\begin{aligned}
\sum_{k=0}^{\infty}k(1-\beta)\beta^k
&=
(1-\beta)\frac{\beta}{(1-\beta)^2}\\
&=
\frac{\beta}{1-\beta}.
\end{aligned}
$$

The differentiated geometric series supplies the intermediate identity.

For two example decays:

| Quantity | $$\beta=0.9$$ | $$\beta=0.99$$ |
|---|---|---|
| Approximate horizon $$1/(1-\beta)$$ | $$10$$ | $$100$$ |
| Mean age | $$9$$ | $$99$$ |
| Half-life | $$6.5788$$ | $$68.9676$$ |
| E-folding age | $$9.4912$$ | $$99.4992$$ |
| Weight in the stated approximate horizon | $$0.651322$$ | $$0.633968$$ |

These values come from the formulas above. Calling both decays “averages over the last so many gradients” hides their infinite tails and different possible definitions of memory.

## Variance reduction and effective sample size

Suppose inputs are independent with common variance

$$
\sigma^2.
$$

For a normalized weighted average,

$$
\operatorname{Var}\left(\sum_k w_kx_k\right)
=
\sigma^2\sum_k w_k^2.
$$

An equally weighted mean of a specified number of independent observations has variance equal to the original variance divided by that number. Matching these variances defines an effective sample size:

$$
N_{\mathrm{eff}}=\frac1{\sum_k w_k^2}.
$$

For the infinite EMA,

$$
\sum_{k=0}^{\infty}w_k^2
=
(1-\beta)^2\sum_{k=0}^{\infty}\beta^{2k}
=
\frac{1-\beta}{1+\beta}.
$$

Therefore

$$
\operatorname{Var}(m_t)
=
\sigma^2\frac{1-\beta}{1+\beta},
$$

and

$$
N_{\mathrm{eff}}=\frac{1+\beta}{1-\beta}.
$$

At decay nine tenths, this is nineteen rather than ten. There is no contradiction: variance matching and the e-folding horizon define different quantities.

For the corrected finite average, the squared weights sum to

$$
\frac{(1-\beta)^2}{(1-\beta^t)^2}
\frac{1-\beta^{2t}}{1-\beta^2}.
$$

After cancelling factors,

$$
N_{\mathrm{eff},t}
=
\frac{1+\beta}{1-\beta}
\frac{1-\beta^t}{1+\beta^t}.
$$

The three-step example therefore has

$$
N_{\mathrm{eff},3}
=
\frac1{(1/7)^2+(2/7)^2+(4/7)^2}
=
\frac73.
$$

Correlated inputs change the variance:

$$
\operatorname{Var}\left(\sum_k w_kx_k\right)
=
\sum_{j,k}w_jw_k\operatorname{Cov}(x_j,x_k).
$$

A gradient sequence is typically dependent because model parameters change and batches may share structure. The independent-input effective sample size is an interpretation under an assumption, not a literal count of independent training signals.

## Smoothing necessarily introduces lag

For an input that jumps from zero to a constant and stays there, starting from a zero state gives

$$
m_t=A(1-\beta^t).
$$

The remaining error is

$$
A-m_t=A\beta^t.
$$

The same decay that removes high-frequency variation also delays adaptation to a sustained change.

A linear trend gives an especially transparent result. Suppose, after initial transients,

$$
x_t=a+ct
$$

and seek a state of the form

$$
m_t=x_t-d.
$$

Substitute into the recursion:

$$
x_t-d
=
\beta(x_t-c-d)+(1-\beta)x_t.
$$

Cancelling the current input gives

$$
d=\beta(c+d),
$$

hence

$$
d=\frac{\beta c}{1-\beta}.
$$

The lag in value is the trend slope times the mean age of the weights.

This is why increasing the decay is not an unqualified improvement. It reduces variance under stable conditions while increasing lag when the underlying signal moves. A useful decay depends on the timescale of changes as well as the amount of noise.

## Momentum and its competing normalization conventions

One momentum convention averages gradients:

$$
m_t=\beta m_{t-1}+(1-\beta)g_t,
$$

$$
\theta_t=\theta_{t-1}-\eta_{\mathrm{EMA}}m_t.
$$

Another accumulates them without the new-gradient normalization:

$$
v_t=\beta v_{t-1}+g_t,
$$

$$
\theta_t=\theta_{t-1}-\eta_{\mathrm{sum}}v_t.
$$

With compatible zero initialization,

$$
m_t=(1-\beta)v_t.
$$

The parameter trajectories match when

$$
\eta_{\mathrm{sum}}
=
(1-\beta)\eta_{\mathrm{EMA}}.
$$

Two implementations using the same numerical learning rate and decay can therefore take different steps. The recurrence, not the method name, determines the convention.

To see how averaging separates stable and alternating components, consider a prescribed gradient sequence

$$
g_t=b+A(-1)^t.
$$

Seek its steady EMA in the form

$$
m_t=b+B(-1)^t.
$$

Substitution gives

$$
B=-\beta B+(1-\beta)A,
$$

so

$$
B=\frac{1-\beta}{1+\beta}A.
$$

The constant component passes unchanged, while the alternating component is attenuated. This is the algebra behind the familiar explanation that momentum smooths oscillation.

It is not, by itself, a convergence proof. In optimization the gradients depend on the parameter trajectory, so the input sequence changes when the optimizer changes.

A common Nesterov-style velocity formulation evaluates the gradient after a momentum look-ahead:

$$
v_t
=
\beta v_{t-1}
+
\nabla f(\theta_{t-1}-\eta\beta v_{t-1}),
$$

followed by

$$
\theta_t=\theta_{t-1}-\eta v_t.
$$

The look-ahead location and learning-rate convention must be read together. Simply inserting a look-ahead expression from an unnormalized velocity into a normalized EMA implementation changes its scale.

## A quadratic exposes momentum's stability limits

Use the scalar objective

$$
f(\theta)=\frac12a\theta^2,
\qquad a>0,
$$

with the normalized momentum convention. The gradient is

$$
g_t=a\theta_{t-1}.
$$

From the previous parameter update,

$$
m_{t-1}
=
\frac{\theta_{t-2}-\theta_{t-1}}{\eta}.
$$

Substituting this into the current update gives

$$
\theta_t
=
\left[1+\beta-\eta(1-\beta)a\right]\theta_{t-1}
-
\beta\theta_{t-2}.
$$

Try a solution proportional to a power of a scalar:

$$
\theta_t=r^t.
$$

The characteristic equation is

$$
r^2-
\left[1+\beta-\eta(1-\beta)a\right]r
+\beta=0.
$$

Convergence requires both roots to have magnitude below one.

Let

$$
k=\eta(1-\beta)a.
$$

For

$$
0\le\beta<1,
$$

the stability range is

$$
0<k<2(1+\beta).
$$

One way to check this is to inspect the characteristic polynomial at the two unit-circle crossings:

$$
P(1)=k,
\qquad
P(-1)=2(1+\beta)-k.
$$

If the roots are complex, their product is the decay, so their common magnitude is its square root and is below one. If the roots are real, positivity at both endpoints together with a product below one places them inside the interval precisely in the stated range.

At the boundaries a root reaches positive or negative one, preventing strict decay. Momentum can oscillate or diverge when the step is too large. Averaging gradients does not eliminate stability restrictions.

## RMSProp averages a raw second moment

AdaGrad accumulates coordinatewise squared gradients:

$$
s_t=s_{t-1}+g_t^2.
$$

A corresponding update divides the gradient by a square root of this accumulator, usually with a stabilizing constant.

For a constant non-zero gradient, the accumulator grows linearly with time, so the effective scale decreases like

$$
t^{-1/2}.
$$

It does not follow that every AdaGrad accumulator diverges. If squared gradients form a summable sequence, the accumulator remains bounded. Even a decreasing step size does not by itself imply that total possible movement is finite.

RMSProp replaces the cumulative sum with exponential forgetting:

$$
s_t=\beta_2s_{t-1}+(1-\beta_2)g_t^2.
$$

One common update convention is

$$
\theta_t
=
\theta_{t-1}
-
\eta\frac{g_t}{\sqrt{s_t}+\epsilon}.
$$

All operations are coordinatewise.

The averaged quantity is a raw second moment. For a random scalar gradient,

$$
\mathbb E[g^2]
=
\operatorname{Var}(g)+(\mathbb E[g])^2.
$$

This follows by expanding the definition of variance. A large accumulator can therefore reflect a persistent non-zero gradient, fluctuating gradients, or both. It is not a direct curvature estimate either.

Placing the stabilizer inside the square root,

$$
\sqrt{s_t+\epsilon},
$$

is a different convention from adding it outside. The constants have different units and different behaviour near zero. They should not be exchanged silently.

## Adam combines direction, scale, and startup normalization

Adam maintains two recursions:

$$
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,
$$

$$
s_t=\beta_2s_{t-1}+(1-\beta_2)g_t^2.
$$

For zero initial states, define

$$
\widehat m_t=\frac{m_t}{1-\beta_1^t},
\qquad
\widehat s_t=\frac{s_t}{1-\beta_2^t}.
$$

The update is

$$
\theta_t
=
\theta_{t-1}
-
\eta
\frac{\widehat m_t}{\sqrt{\widehat s_t}+\epsilon}.
$$

The correction matters to the ratio because the two accumulated weights generally differ.

For a constant non-zero gradient, the first uncorrected ratio is

$$
\frac{m_1}{\sqrt{s_1}}
=
\frac{1-\beta_1}{\sqrt{1-\beta_2}}
\operatorname{sign}(g).
$$

For the illustrative decays

$$
\beta_1=0.9,\qquad \beta_2=0.999,
$$

this scale factor is

$$
\frac{0.1}{\sqrt{0.001}}=\sqrt{10}.
$$

With both corrections and a zero stabilizer for this algebraic calculation, the ratio is exactly the gradient's sign.

A two-step example shows the interaction after a sign change. Choose

$$
\beta_1=\beta_2=\frac12,
\qquad
(g_1,g_2)=(2,-2),
\qquad
\eta=\frac1{10},
\qquad
\theta_0=0.
$$

Use a zero stabilizer only because both denominators in this constructed example are strictly positive.

| Step | $$m_t$$ | $$s_t$$ | $$\widehat m_t$$ | $$\widehat s_t$$ | Update ratio |
|---|---|---|---|---|---|
| $$1$$ | $$1$$ | $$2$$ | $$2$$ | $$4$$ | $$1$$ |
| $$2$$ | $$-1/2$$ | $$3$$ | $$-2/3$$ | $$4$$ | $$-1/3$$ |

Therefore

$$
\theta_1=-\frac1{10},
$$

and

$$
\theta_2
=
-\frac1{10}+\frac1{30}
=
-\frac1{15}.
$$

The squared-gradient estimate is unchanged after correction because both gradients have the same magnitude. The first-moment estimate partially cancels because their signs differ.

Even when both corrected moments are unbiased under a stationary model, their ratio need not be unbiased:

$$
\mathbb E\left[\frac{\widehat m_t}{\sqrt{\widehat s_t}}\right]
\ne
\frac{\mathbb E[\widehat m_t]}
{\sqrt{\mathbb E[\widehat s_t]}}
$$

in general. Normalizing an update is a non-linear operation.

## The same recurrence as a filter and a parameter average

Ignoring startup terms, take the transform of the EMA difference equation:

$$
M(z)=\beta z^{-1}M(z)+(1-\beta)X(z).
$$

The transfer function is

$$
H(z)=\frac{1-\beta}{1-\beta z^{-1}}.
$$

On the unit circle,

$$
\lvert H(e^{i\omega})\rvert^2
=
\frac{(1-\beta)^2}
{1+\beta^2-2\beta\cos\omega}.
$$

At zero frequency its gain is one. At the alternating frequency, its magnitude is

$$
\frac{1-\beta}{1+\beta},
$$

matching the direct alternating-sequence calculation.

The same recursion can average model parameters or target-network parameters. That shares the weighting mathematics, not necessarily the optimizer interpretation. In a non-linear model,

$$
f_{\mathbb E[\theta]}(x)
\ne
\mathbb E[f_\theta(x)]
$$

in general, so averaging parameters is not identical to averaging predictions.

Finally, adaptive scaling makes coupled quadratic regularization different from decoupled weight decay. With a fixed diagonal preconditioner for illustration, adding a regularization gradient gives

$$
\theta_{\mathrm{new}}
=
\theta-\eta Dg-\eta\lambda D\theta.
$$

Decoupled decay instead gives

$$
\theta_{\mathrm{new}}
=
(1-\eta\lambda)\theta-\eta Dg.
$$

The shrinkage differs by the preconditioner. In Adam, putting regularization into the gradient also changes the histories used to compute that preconditioner.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| Unroll a finite EMA | Retain the initial-state term |
| Derive bias correction | Sum the finite geometric weights |
| Explain what correction does not fix | Separate startup bias from tracking lag |
| Reproduce the three-step example | Obtain the normalized weights explicitly |
| Distinguish memory definitions | Compute half-life, mean age, and e-folding age |
| Derive effective sample size | State the independent-input assumption |
| Translate momentum conventions | Rescale the learning rate consistently |
| Derive the quadratic recurrence | Check the roots for stability |
| Interpret a squared-gradient average | Separate variance from raw second moment |
| Carry out two Adam updates | Correct both moments before taking the ratio |
| Identify implementation differences | Check stabilizer placement and weight decay |

## Why it matters for my work

Optimizer settings become interpretable when expressed in update steps, lag, and variance reduction. I should record the actual recurrence and batch schedule, since the same decay can represent very different amounts of data across experiments.

## What I have not resolved

I need controlled comparisons to determine whether a longer gradient history helps my datasets or mainly delays adaptation to changing batch composition. The EMA algebra predicts that tradeoff but does not determine its empirical balance.
