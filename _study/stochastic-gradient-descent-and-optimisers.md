---
layout: study_note
title: "Stochastic Gradient Descent and the Optimizers Built On It"
description: "Mini-batch gradient estimates, variance, momentum, per-parameter rates in AdaGrad, RMSProp and Adam, and what saddle points and local minima do not explain."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "algebra-and-optimization"
category_title: "Linear Algebra & Optimization"
subgroup: "Losses & Gradient Optimization"
order: 6
source: "Independent study"
written: true
updated: "2026-09-15"
papers:
  - "2026-02-09-underspecification-credibility-ml"
---

Stochastic gradient descent replaces an exact objective gradient with a random estimate. Its usefulness begins with computation, but its behavior depends on the estimate's bias, variance, and dependence on the sampling procedure. Momentum and adaptive optimizers then modify how a sequence of those estimates becomes parameter movement.

Two corrections are essential. Full-batch gradient descent does not require the entire dataset in memory simultaneously. Also, a decaying learning rate is not universally necessary for every form of stochastic optimization. Its role becomes clear when persistent gradient noise, fixed batch size, and convergence of the unaveraged iterates are considered together.

## Start with an average and a sampling rule

Define the empirical objective as an average:

$$
f(\theta)=\frac1N\sum_{i=1}^N\ell_i(\theta).
$$

Its exact gradient is

$$
G(\theta)=\nabla f(\theta)
=
\frac1N\sum_{i=1}^N\nabla\ell_i(\theta).
$$

The average matters. A uniformly sampled per-example gradient estimates this average. To estimate the gradient of an unnormalized sum, it would need an additional factor equal to the dataset size.

An exact full gradient can be accumulated by processing smaller groups while keeping parameters fixed, summing their appropriately weighted gradients, and updating only after the complete pass. It requires full-dataset computation per update, but not simultaneous storage of every example.

Adding an example also does not invalidate a fixed-parameter gradient. At the same parameter vector,

$$
G_{N+1}(\theta)
=
\frac{N}{N+1}G_N(\theta)
+
\frac1{N+1}\nabla\ell_{N+1}(\theta).
$$

Changing the parameters generally changes the old gradients, which is a different issue.

The simple analysis below assumes a separable per-example objective. Operations that couple examples inside a batch, such as training-mode batch normalization, require care: their batch gradient need not be an unbiased estimate of the particular fixed per-example average written above.

## Deriving unbiasedness

At a fixed parameter vector, abbreviate the per-example gradients as

$$
g_i=\nabla\ell_i(\theta).
$$

Sample an index uniformly. Then

$$
\mathbb E[g_I]
=
\sum_{i=1}^N\frac1N g_i
=
G.
$$

For a minibatch of independent draws with replacement,

$$
\hat G=\frac1B\sum_{b=1}^B g_{I_b}.
$$

Linearity of expectation gives

$$
\mathbb E[\hat G]=G.
$$

During training, the parameter vector is itself random because it depends on earlier batches. The meaningful statement is conditional: given the current parameters and all previous randomness, fresh uniform independent sampling has expectation equal to the current full gradient.

Write the estimate as

$$
\hat G_t=G(\theta_t)+\xi_t,
\qquad
\mathbb E[\xi_t\mid\mathcal F_t]=0,
$$

where the conditioning information contains the current state before drawing the next batch.

This does not imply that one batch points downhill, or that successive gradients are independent. It says the fresh estimation error has zero conditional mean under the specified sampler.

If examples are sampled with probabilities other than uniform, an unweighted gradient estimates a different objective. An importance-weighted estimate,

$$
\hat g=\frac{g_I}{Np_I},
$$

restores the original expectation because

$$
\mathbb E[\hat g]
=
\sum_i p_i\frac{g_i}{Np_i}
=
G.
$$

The probabilities must be positive wherever the objective assigns weight. Very small sampling probabilities can also produce large weighted gradients and substantial variance.

## Deriving the minibatch variance

Define the population covariance of per-example gradients at the current parameters:

$$
C=
\frac1N\sum_{i=1}^N(g_i-G)(g_i-G)^\top.
$$

The total gradient variance is its trace:

$$
\sigma^2=\operatorname{tr}(C)
=
\frac1N\sum_i\lVert g_i-G\rVert_2^2.
$$

For independent sampling with replacement, let the centered draw be

$$
\delta_b=g_{I_b}-G.
$$

The minibatch error is

$$
\xi=\frac1B\sum_b\delta_b.
$$

Expand its covariance:

$$
\mathbb E[\xi\xi^\top]
=
\frac1{B^2}\sum_{b,c}
\mathbb E[\delta_b\delta_c^\top].
$$

For distinct draws, independence and zero mean make the cross terms zero. The remaining diagonal terms each equal the population covariance. Therefore,

$$
\operatorname{Cov}(\hat G)=\frac CB,
\qquad
\mathbb E\lVert\xi\rVert_2^2=\frac{\sigma^2}{B}.
$$

Expanding the squared estimated gradient similarly gives

$$
\mathbb E\lVert\hat G\rVert_2^2
=
\lVert G\rVert_2^2+\frac{\sigma^2}{B}.
$$

The cross term disappears because the estimation error has zero mean. This identity is where gradient variance enters the optimization bound.

Without replacement, distinct draws are negatively correlated. Since the centered gradients sum to zero,

$$
\sum_{i\neq j}(g_i-G)(g_j-G)^\top=-NC.
$$

A uniformly chosen ordered pair of distinct examples consequently has cross-covariance

$$
-\frac C{N-1}.
$$

Substituting the diagonal and off-diagonal terms into the batch covariance gives

$$
\operatorname{Cov}(\hat G)
=
\frac{N-B}{B(N-1)}C.
$$

It correctly becomes zero when the batch contains the entire dataset.

This fixed-parameter result should not be confused with conditional unbiasedness during random reshuffling across an epoch. After earlier examples have been observed, the remaining examples are not a fresh uniform draw from the entire dataset.

## A finite dataset with exactly calculable noise

Construct four scalar losses:

$$
\ell_i(\theta)=\frac12(\theta+c_i)^2,
\qquad
c_i\in\{1,3,5,7\}.
$$

At zero, their gradients are

$$
1,\quad3,\quad5,\quad7.
$$

The full gradient is four, and the population variance is

$$
\sigma^2
=
\frac{(1-4)^2+(3-4)^2+(5-4)^2+(7-4)^2}{4}
=
5.
$$

A batch of two draws with replacement has gradient variance

$$
\frac52.
$$

Without replacement, the six possible batch means are

$$
2,\quad3,\quad4,\quad4,\quad5,\quad6.
$$

Their mean is four, and their variance is

$$
\frac{4+1+0+0+1+4}{6}
=
\frac53.
$$

This agrees with the finite-population formula:

$$
5\frac{4-2}{2(4-1)}=\frac53.
$$

The complete objective can also be simplified. Write the constants as their mean plus centered deviations. The cross terms average to zero, giving

$$
f(\theta)
=
\frac12(\theta+4)^2+\frac52.
$$

The minimizer is therefore

$$
\theta^\star=-4.
$$

At that optimum, the full gradient is zero, but the individual gradients are

$$
-3,\quad-1,\quad1,\quad3.
$$

The noise remains. A zero full gradient does not require every training example to have a zero gradient.

## The variance term in expected descent

For an objective smooth with constant $$L$$, an SGD update is

$$
\theta^+=\theta-\eta\hat G.
$$

Apply the smoothness inequality:

$$
f(\theta^+)
\leq
f(\theta)
-\eta G^\top\hat G
+\frac{L\eta^2}{2}\lVert\hat G\rVert_2^2.
$$

Take expectation conditional on the current state. Unbiasedness gives

$$
\mathbb E[G^\top\hat G]=\lVert G\rVert_2^2.
$$

The second-moment identity then yields

$$
\mathbb E[f(\theta^+)]
\leq
f(\theta)
-
\eta\left(1-\frac{L\eta}{2}\right)\lVert G\rVert_2^2
+
\frac{L\eta^2\sigma^2}{2B}.
$$

The deterministic decrease competes with a positive variance term. Near a stationary point, the full gradient may become small while the per-example variance remains substantial.

This explains why the full objective can rise after a valid stochastic update. A reported minibatch loss has another source of variation: successive values may be evaluated on different observations. Comparing those values is not the same as measuring the objective before and after a step on a fixed dataset.

If the objective is also strongly convex with constant $$\mu$$, and the step size is at most the reciprocal smoothness constant, the gradient-gap inequality gives

$$
\mathbb E[\Delta_{t+1}]
\leq
(1-\mu\eta)\mathbb E[\Delta_t]
+
\frac{L\eta^2\sigma^2}{2B},
$$

assuming the displayed variance is a uniform upper bound.

For a fixed step size, the additive term does not disappear. Iterating a recurrence of the form

$$
a_{t+1}\leq qa_t+c
$$

gives

$$
a_t\leq q^ta_0+c\frac{1-q^t}{1-q}.
$$

Consequently, the bound approaches

$$
\frac{L\eta\sigma^2}{2\mu B}.
$$

This is an upper bound on a possible error floor, not an exact formula for every objective.

## An exact noise floor and the reason for decay

For the constructed quadratic, let

$$
e_t=\theta_t+4.
$$

A single-example gradient has the form

$$
g_t=e_t+\xi_t,
\qquad
\mathbb E[\xi_t]=0,
\qquad
\mathbb E[\xi_t^2]=5.
$$

With fresh independent draws,

$$
e_{t+1}=(1-\eta)e_t-\eta\xi_t.
$$

Squaring and taking expectations removes the cross term:

$$
\mathbb E[e_{t+1}^2]
=
(1-\eta)^2\mathbb E[e_t^2]+5\eta^2.
$$

When the step size is between zero and two, the limiting mean-squared error is

$$
\frac{5\eta^2}{1-(1-\eta)^2}
=
\frac{5\eta}{2-\eta}.
$$

For the constructed choice

$$
\eta=\frac15,
$$

this becomes

$$
\lim_t\mathbb E[e_t^2]=\frac59.
$$

Because objective gap is half the squared error,

$$
\lim_t\mathbb E[f(\theta_t)-f^\star]=\frac5{18}.
$$

These values are derived from the finite dataset, not measured from a training run.

Reducing the step size reduces the size of newly injected noise. A classical sufficient schedule, under smooth strong convexity and bounded conditional gradient variance, satisfies

$$
\sum_t\eta_t=\infty,
\qquad
\sum_t\eta_t^2<\infty.
$$

The first condition prevents the total available movement from becoming too small. The second makes the accumulated variance-weighted squared steps finite.

For schedules of the form

$$
\eta_t=\frac{c}{(t+t_0)^\alpha},
$$

both hold when

$$
\frac12<\alpha\leq1.
$$

The reason is the convergence rule for power sums: the first series diverges when the exponent is at most one, while the squared-step series converges when twice the exponent exceeds one. The offset can keep early steps inside a required stability bound.

These are sufficient conditions for the stated setting, not a universal command to decay every learning rate. Growing batches, variance reduction, or vanishing per-example gradients can reduce noise by other means. Averaging iterates also changes the relevant convergence question. The exact quadratic example establishes the narrower claim: persistent noise and a constant step generally prevent the raw iterates from settling exactly at the optimum.

## Momentum modifies the direction over time

For the optimizer recurrences below, initialize state at step zero and evaluate each new gradient at the previous parameter vector.

One momentum convention uses an exponential moving average:

$$
m_t=\beta m_{t-1}+(1-\beta)g_t,
\qquad
\theta_t=\theta_{t-1}-\eta m_t,
\qquad
m_0=0.
$$

Unroll the recurrence:

$$
m_t
=
(1-\beta)\sum_{s=1}^t\beta^{t-s}g_s.
$$

Older gradients receive geometrically smaller weights. Only the current average must be stored.

This gives a concrete explanation for directional smoothing. With the constructed choice

$$
\beta=\frac12,
$$

two gradients equal to two produce averages one and one-and-a-half. Gradients two followed by negative two produce averages one and negative one-half. Persistent directions accumulate, while opposing directions partly cancel.

For a stationary scalar gradient stream with independent noise of variance $$\sigma^2$$, the limiting noise variance in the average is

$$
(1-\beta)^2\sigma^2\sum_{k=0}^{\infty}\beta^{2k}
=
\frac{1-\beta}{1+\beta}\sigma^2.
$$

This is a property of the averaging filter under those assumptions. During optimization, gradients change with the parameters and are generally correlated, so the calculation is not a complete convergence theorem for momentum.

Momentum also introduces lag. In a scalar quadratic with curvature $$\lambda$$, eliminating the average from successive parameter updates gives

$$
e_{t+1}
=
[1+\beta-\eta(1-\beta)\lambda]e_t
-
\beta e_{t-1}.
$$

The next error depends on two previous positions. Memory can accelerate movement through a shallow direction, but it can also sustain overshoot.

Another common convention omits the factor multiplying the new gradient. For fixed momentum, its accumulator is the normalized average divided by that factor. Learning rates must be adjusted accordingly before comparing the two conventions.

## AdaGrad changes coordinate scales using accumulated history

For each parameter coordinate, AdaGrad accumulates squared gradients:

$$
s_{t,j}=s_{t-1,j}+g_{t,j}^2,
\qquad
s_{0,j}=0.
$$

The update is

$$
\theta_{t,j}
=
\theta_{t-1,j}
-
\eta\frac{g_{t,j}}{\sqrt{s_{t,j}}+\epsilon}.
$$

The denominator gives coordinates with substantial accumulated gradient energy smaller effective learning rates. It is a diagonal scaling rule, not an estimate of the full Hessian.

The square root is important for units. Scaling an entire coordinate's gradient history by a positive constant scales the numerator and, ignoring the numerical stabilizer, its denominator by the same constant.

Consider the prescribed gradient sequence

$$
g_1=(2,1),
\qquad
g_2=(2,0),
\qquad
g_3=(0,1).
$$

With unit base step and zero stabilizer for this nonzero-denominator example,

$$
s_1=(4,1),
\qquad
\Delta\theta_1=(-1,-1),
$$

$$
s_2=(8,1),
\qquad
\Delta\theta_2=\left(-\frac1{\sqrt2},0\right),
$$

and

$$
s_3=(8,2),
\qquad
\Delta\theta_3=\left(0,-\frac1{\sqrt2}\right).
$$

The second coordinate has accumulated less squared gradient, so an equal future gradient magnitude can receive a larger step there.

The accumulator never decreases, but saying “learning inevitably stops” is too strong. Under a constant nonzero scalar gradient,

$$
s_t=tg^2,
$$

so the step magnitude is

$$
\frac{\eta}{\sqrt t}.
$$

It approaches zero, but its sum diverges. If squared gradients are summable, the accumulator need not diverge at all. The actual issue is that old gradients permanently influence the denominator, which can make adaptation sluggish after the gradient scale changes.

## RMSProp discounts old squared gradients

RMSProp replaces the growing sum with a moving average:

$$
r_t=\beta_2r_{t-1}+(1-\beta_2)g_t^2,
$$

$$
\theta_t
=
\theta_{t-1}
-
\eta\frac{g_t}{\sqrt{r_t}+\epsilon}.
$$

All squares, roots, and divisions are coordinatewise. Unlike AdaGrad's accumulator, the scale estimate can decrease when recent gradients become smaller.

For a constant scalar gradient and zero initial state,

$$
r_t=g^2(1-\beta_2^t).
$$

This follows by summing the geometric weights. Ignoring the stabilizer, the update magnitude approaches the base learning rate. The denominator therefore does not itself supply the long-run decay seen with AdaGrad under a constant gradient.

For example, with gradient two and decay factor one-half,

$$
r_1=2,
\qquad
r_2=3,
\qquad
r_t\longrightarrow4.
$$

The first two gradient-to-scale ratios are

$$
\frac2{\sqrt2},
\qquad
\frac2{\sqrt3},
$$

and their limit is one.

Zero initialization makes early scale estimates smaller than their stationary value. The basic RMSProp recurrence shown here does not correct that initialization effect. Adam applies an explicit correction to both its moving averages.

## Adam combines direction and scale, then corrects initialization

Adam maintains a first-moment average and a second-raw-moment average:

$$
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,
$$

$$
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2.
$$

Both start at zero. Suppose, temporarily, that the gradient stream has a constant mean. Unrolling the first recurrence gives

$$
\mathbb E[m_t]
=
(1-\beta_1)\sum_{s=1}^t\beta_1^{t-s}\mathbb E[g_s].
$$

The weights sum to

$$
(1-\beta_1)\frac{1-\beta_1^t}{1-\beta_1}
=
1-\beta_1^t.
$$

Hence,

$$
\mathbb E[m_t]
=
(1-\beta_1^t)\mathbb E[g].
$$

The same argument for a constant second raw moment gives

$$
\mathbb E[v_t]
=
(1-\beta_2^t)\mathbb E[g^2].
$$

This derives the corrections:

$$
\hat m_t=\frac{m_t}{1-\beta_1^t},
\qquad
\hat v_t=\frac{v_t}{1-\beta_2^t}.
$$

The update is

$$
\theta_t
=
\theta_{t-1}
-
\eta\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}.
$$

Even when gradients change over time, division by the geometric weight sum turns each corrected moment into a normalized weighted average of past observations. It does not make that historical average an unbiased estimate of the current gradient.

The second raw moment is also not the variance:

$$
\mathbb E[g^2]
=
(\mathbb E[g])^2+\operatorname{Var}(g).
$$

Finally, correcting the moments does not make their nonlinear ratio an unbiased full-gradient update. Expectation does not generally commute with division or square roots.

## Carrying Adam's first two updates through

Use a constructed scalar gradient stream:

$$
g_1=2,
\qquad
g_2=4,
$$

with

$$
\beta_1=\beta_2=\frac12,
\qquad
\eta=0.1,
\qquad
\epsilon=0.
$$

These deliberately simple choices make every operation visible.

At the first step,

$$
m_1=1,
\qquad
v_1=2.
$$

The correction denominator is one-half, giving

$$
\hat m_1=2,
\qquad
\hat v_1=4.
$$

Thus,

$$
\Delta\theta_1
=
-0.1\frac2{\sqrt4}
=
-0.1.
$$

At the second step,

$$
m_2=\frac12(1)+\frac12(4)=2.5,
$$

$$
v_2=\frac12(2)+\frac12(16)=9.
$$

Now the correction denominator is three-quarters:

$$
\hat m_2=\frac{2.5}{0.75}=\frac{10}{3},
\qquad
\hat v_2=\frac9{0.75}=12.
$$

The update is

$$
\Delta\theta_2
=
-0.1\frac{10/3}{\sqrt{12}}
\approx-0.096225.
$$

The corrected first moment is not the current gradient of four. It is the weighted average

$$
\frac{2+2\cdot4}{3}=\frac{10}{3}.
$$

The correction removes missing startup weight; it does not remove temporal averaging.

## What these modifications do not establish

An adaptive denominator is not automatically a curvature estimate. Squared gradients contain both signal and sampling variability. Their magnitudes also depend on parameterization and objective scaling.

Weight decay needs its own specification. Even without momentum, applying a diagonal preconditioner to a gradient containing a squared-norm penalty gives

$$
\theta^+
=
\theta-\eta Dg-\eta\lambda D\theta.
$$

Decoupled decay instead gives

$$
\theta^+
=
(1-\eta\lambda)\theta-\eta Dg.
$$

The shrinkage terms differ unless the preconditioner acts like the identity on the parameters being decayed. The phrase “weight decay” therefore does not fully specify an adaptive update.

The claim that high dimension makes saddle points replace local minima as a universal explanation for training difficulty is also unjustified. The quadratic

$$
f(\theta)=\frac12\lVert\theta\rVert_2^2
$$

has a positive definite minimum in every dimension.

A saddle such as

$$
f(x,y)=x^2-y^2
$$

does have a descending direction at its stationary point. But exact gradient descent initialized there stays there, and momentum initialized with zero velocity does too. Noise can help leave it only if the perturbation reaches a useful direction. None of these observations proves that a particular optimizer will find a clinically preferable solution.

## Revision checklist

| Question | What I should be able to reconstruct |
|---|---|
| Which objective does a sampled gradient estimate? | Distinguish the average, the sum, and nonuniform sampling. |
| Does full-batch training require all examples in memory? | Explain fixed-parameter gradient accumulation. |
| What does unbiasedness mean during training? | State the conditional expectation with fresh sampling. |
| Why does minibatch variance decrease? | Expand covariance and identify vanishing cross terms. |
| What changes without replacement? | Derive the finite-population correction. |
| Can noise persist at the optimum? | Reproduce the four-loss example. |
| Where does the variance term enter descent? | Take expectations in the smoothness inequality. |
| Why might steps decay? | Derive the exact quadratic noise floor and state alternatives. |
| What does momentum average? | Unroll its weights and distinguish normalization conventions. |
| How do AdaGrad and RMSProp differ? | Compare accumulated and discounted squared gradients. |
| Why does Adam divide by geometric factors? | Sum the missing startup weights. |
| What does bias correction not fix? | Separate initialization, temporal lag, and the nonlinear update ratio. |
| What must an optimizer comparison report? | Include sampler, schedule, state conventions, and decay implementation. |

## Why it matters for my work

The sampler and optimizer jointly determine which model a training run produces. For shortcut auditing, I need to distinguish instability caused by gradient noise from systematic effects of patient weighting, objective design, and checkpoint selection.

## What I have not resolved

- How much audit variation remains after controlling patient sampling and model selection?
- Compare shortcut-reliance measurements across repeated runs with the same declared objective and different batch orders.
