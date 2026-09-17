---
layout: study_note
title: "Optimization for Machine Learning"
description: "Gradients, regularization, and constrained optimization as the assumptions a training procedure quietly imposes."
og_image: "https://sehyeony0518.github.io/assets/img/og/optimization-for-machine-learning.png"
tab: "ai-foundations"
tab_title: "AI Theory"
category: "algebra-and-optimization"
category_title: "Linear Algebra & Optimization"
subgroup: "Losses & Gradient Optimization"
order: 5
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-02-03-right-for-the-right-reasons"
  - "2026-02-09-underspecification-credibility-ml"
---

Optimization turns an objective into a sequence of parameter choices. Its guarantees depend on properties of that objective: convexity determines whether local optimality is sufficient, smoothness limits how inaccurate a local linear prediction can become, and strong convexity prevents the objective from becoming arbitrarily flat near its minimizer.

The condition number combines the last two properties. It explains why one learning rate can be simultaneously too large for one direction and too small for another. The derivations below make these relationships explicit before considering regularization and constraints.

## The objective and the assumptions being analyzed

A typical empirical objective is

$$
f(\theta)
=
\frac1N\sum_{i=1}^N\ell_i(\theta)
+
\lambda R(\theta).
$$

The average specifies weighting as well as fit. If observations are frames, patients with more frames receive more total weight unless the objective or sampler compensates for that. Changing class weights similarly changes the objective being optimized.

For the deterministic convergence results, assume an unconstrained, differentiable objective over Euclidean parameter space. Whenever a minimizer is used, assume it exists and write

$$
\theta^\star\in\arg\min_\theta f(\theta),
\qquad
f^\star=f(\theta^\star).
$$

The optimization error is

$$
\Delta_t=f(\theta_t)-f^\star.
$$

This quantity differs from parameter error, training loss itself, generalization error, and clinical validity. A theorem about one does not automatically establish a result about the others.

The gradients in this note are exact gradients of the declared objective. Replacing them with minibatch estimates adds a variance term, derived in the separate note on stochastic gradient descent.

## Convexity and the guarantee it supplies

A function is convex when its value along any segment lies below the corresponding chord:

$$
f((1-\alpha)x+\alpha y)
\leq
(1-\alpha)f(x)+\alpha f(y),
\qquad
0\leq\alpha\leq1.
$$

For a differentiable function, this implies a supporting-plane inequality. Subtract the value at the first endpoint and divide by the segment fraction:

$$
\frac{f(x+\alpha(y-x))-f(x)}{\alpha}
\leq
f(y)-f(x).
$$

Taking the limit as the fraction approaches zero gives

$$
f(y)\geq f(x)+\nabla f(x)^\top(y-x).
$$

This is the key operational form: the tangent plane is a global lower bound.

If the gradient vanishes, then

$$
f(y)\geq f(x)
$$

for every candidate point. Every stationary point is therefore a global minimizer.

A local minimizer is also global. Suppose a better point existed. The convexity inequality would make every sufficiently short step toward that point improve the objective, contradicting local minimality.

Convexity does not guarantee that a minimizer exists. The convex function

$$
f(x)=e^x
$$

has infimum zero but never attains it at a finite point. Convexity also does not guarantee uniqueness. The function

$$
f(x,y)=x^2
$$

is minimized at every point with first coordinate zero.

These distinctions matter when reading claims that an optimizer “converges to the solution.” The statement needs an attained optimum and must identify whether the solution is unique.

## Smoothness gives an upper quadratic model

An objective is smooth with constant $$L$$ when its gradient is Lipschitz:

$$
\lVert\nabla f(y)-\nabla f(x)\rVert_2
\leq
L\lVert y-x\rVert_2.
$$

The condition limits how quickly the gradient can change. It does not require convexity.

To derive the useful upper bound, consider a displacement $$s$$ and integrate the derivative along its segment:

$$
f(x+s)-f(x)
=
\int_0^1\nabla f(x+\tau s)^\top s\,d\tau.
$$

Separate the gradient at the starting point:

$$
f(x+s)-f(x)-\nabla f(x)^\top s
=
\int_0^1
[\nabla f(x+\tau s)-\nabla f(x)]^\top s\,d\tau.
$$

Cauchy–Schwarz and smoothness bound the integrand by

$$
L\tau\lVert s\rVert_2^2.
$$

Integrating gives the descent lemma:

$$
f(x+s)
\leq
f(x)+\nabla f(x)^\top s+
\frac L2\lVert s\rVert_2^2.
$$

The quadratic term is the cost of trusting the local linear approximation over a finite displacement.

For a twice differentiable objective, smoothness corresponds to controlling the magnitude of Hessian eigenvalues. For a convex objective, they are nonnegative, so an upper bound on the largest eigenvalue provides the relevant curvature limit.

A local estimate of curvature is not automatically a global smoothness constant. A learning rate justified near one point can fail after the trajectory enters a sharper region.

## Why the gradient step has its form

The negative gradient is the direction of greatest first-order decrease per unit Euclidean displacement. For any unit direction,

$$
\nabla f(x)^\top u
\geq
-\lVert\nabla f(x)\rVert_2,
$$

with equality when the direction is opposite the gradient.

The complete gradient update can also be derived by minimizing a local model:

$$
\min_s
\left[
\nabla f(x)^\top s+
\frac1{2\eta}\lVert s\rVert_2^2
\right].
$$

Setting its derivative to zero gives

$$
\nabla f(x)+\frac{s}{\eta}=0,
$$

so

$$
x^+=x-\eta\nabla f(x).
$$

The step size controls the quadratic cost assigned to movement.

Insert this displacement into the smoothness bound:

$$
f(x^+)
\leq
f(x)
-
\eta\left(1-\frac{L\eta}{2}\right)
\lVert\nabla f(x)\rVert_2^2.
$$

The coefficient is positive when

$$
0<\eta<\frac2L.
$$

A convenient choice is

$$
\eta=\frac1L,
$$

which yields

$$
f(x^+)
\leq
f(x)-\frac1{2L}\lVert\nabla f(x)\rVert_2^2.
$$

This proves objective decrease directly. At the boundary step size, the bound no longer guarantees strict decrease, and a quadratic can oscillate indefinitely.

## Deriving the rate for smooth convex objectives

Assume convexity, smoothness, and an attained minimizer. Use the step size above and abbreviate the current gradient as

$$
g_t=\nabla f(\theta_t).
$$

Expand squared parameter distance after an update:

$$
\lVert\theta_{t+1}-\theta^\star\rVert_2^2
=
\lVert\theta_t-\theta^\star\rVert_2^2
-
\frac2L g_t^\top(\theta_t-\theta^\star)
+
\frac1{L^2}\lVert g_t\rVert_2^2.
$$

Rearranging gives

$$
g_t^\top(\theta_t-\theta^\star)
=
\frac L2
\left(
\lVert\theta_t-\theta^\star\rVert_2^2
-
\lVert\theta_{t+1}-\theta^\star\rVert_2^2
\right)
+
\frac1{2L}\lVert g_t\rVert_2^2.
$$

Convexity bounds the current objective gap by the gradient inner product:

$$
f(\theta_t)-f^\star
\leq
g_t^\top(\theta_t-\theta^\star).
$$

Smoothness gives the decrease to the next objective value:

$$
f(\theta_{t+1})
\leq
f(\theta_t)-\frac1{2L}\lVert g_t\rVert_2^2.
$$

Combining them cancels the gradient-norm term:

$$
f(\theta_{t+1})-f^\star
\leq
\frac L2
\left(
\lVert\theta_t-\theta^\star\rVert_2^2
-
\lVert\theta_{t+1}-\theta^\star\rVert_2^2
\right).
$$

This cancellation is the step that turns local descent into a global rate.

Sum from the initial update through update $$T$$. The squared-distance terms telescope:

$$
\sum_{t=0}^{T-1}
[f(\theta_{t+1})-f^\star]
\leq
\frac L2\lVert\theta_0-\theta^\star\rVert_2^2.
$$

The objective values are nonincreasing, so every term on the left is at least the final gap. Consequently,

$$
f(\theta_T)-f^\star
\leq
\frac{
L\lVert\theta_0-\theta^\star\rVert_2^2
}{
2T
}.
$$

This is an inverse-iteration rate in objective error. It does not assert an equally fast rate for parameter distance without an additional relationship between distance and objective value.

## Strong convexity supplies that missing relationship

Strong convexity with positive constant $$\mu$$ strengthens the supporting-plane inequality:

$$
f(y)
\geq
f(x)+\nabla f(x)^\top(y-x)
+
\frac\mu2\lVert y-x\rVert_2^2.
$$

Every tangent plane now has a quadratic lower bound above it. For a twice differentiable function, this corresponds to every Hessian eigenvalue being at least the strong-convexity constant.

At an unconstrained minimizer, the gradient vanishes. Thus,

$$
f(x)-f^\star
\geq
\frac\mu2\lVert x-\theta^\star\rVert_2^2.
$$

The objective gap controls squared parameter distance, and two distinct minimizers cannot exist.

Another consequence links gradient size to objective gap. Complete the square in the lower bound:

$$
\nabla f(x)^\top(y-x)+
\frac\mu2\lVert y-x\rVert_2^2
=
\frac\mu2
\left\lVert y-x+\frac{\nabla f(x)}{\mu}\right\rVert_2^2
-
\frac{\lVert\nabla f(x)\rVert_2^2}{2\mu}.
$$

The squared term is nonnegative. Taking the infimum over candidate points therefore gives

$$
f^\star
\geq
f(x)-\frac{\lVert\nabla f(x)\rVert_2^2}{2\mu}.
$$

Equivalently,

$$
\lVert\nabla f(x)\rVert_2^2
\geq
2\mu[f(x)-f^\star].
$$

This says that a large objective gap cannot coexist with an arbitrarily small gradient under strong convexity.

Combine this inequality with the smoothness decrease:

$$
\Delta_{t+1}
\leq
\Delta_t-\frac1{2L}\lVert g_t\rVert_2^2
\leq
\left(1-\frac\mu L\right)\Delta_t.
$$

Repeated substitution gives

$$
\Delta_T
\leq
\left(1-\frac\mu L\right)^T\Delta_0.
$$

This is geometric convergence, often called a linear rate. Here “linear” describes a constant multiplicative reduction per iteration, not a straight-line decrease of the error.

## Why the condition number matters

Define

$$
\kappa=\frac L\mu.
$$

The convergence factor becomes

$$
1-\frac1\kappa.
$$

Using the elementary inequality

$$
1-a\leq e^{-a},
$$

the gap satisfies

$$
\Delta_T\leq e^{-T/\kappa}\Delta_0.
$$

Thus a sufficient iteration count for target error is

$$
T\geq
\kappa\log\frac{\Delta_0}{\varepsilon}.
$$

The condition number measures the disparity between the steepest permitted curvature and the weakest guaranteed curvature. A large value means that stability in steep directions restricts progress in shallow directions.

Raw curvature magnitude alone is insufficient. Multiplying the whole objective by a positive scalar multiplies both constants by that scalar and leaves their ratio unchanged. Rescaling the learning rate inversely produces the same parameter trajectory.

Conditioning is also coordinate-dependent. Changing parameter units can alter the curvature ratio even when the represented model family is unchanged. This is one reason preprocessing and preconditioning can matter greatly for optimization.

These guarantees require a positive lower curvature bound. An indefinite neural-network Hessian does not acquire a strongly convex convergence guarantee merely by taking a ratio of two of its eigenvalues.

## Quadratic objectives reveal the directional dynamics

Consider a positive definite quadratic:

$$
f(\theta)
=
\frac12\theta^\top H\theta-b^\top\theta.
$$

Its gradient is

$$
\nabla f(\theta)=H\theta-b,
$$

and its minimizer solves

$$
H\theta^\star=b.
$$

Let the parameter error be

$$
e_t=\theta_t-\theta^\star.
$$

Gradient descent gives

$$
e_{t+1}=(I-\eta H)e_t.
$$

Expand the error in the Hessian eigenbasis:

$$
e_t=\sum_j a_{j,t}q_j.
$$

Each coefficient evolves independently:

$$
a_{j,t+1}=(1-\eta\lambda_j)a_{j,t}.
$$

This equation explains both convergence and oscillation. A positive factor shrinks without sign changes. A negative factor of magnitude below one shrinks while alternating. A factor of magnitude above one diverges.

All directions contract exactly when

$$
|1-\eta\lambda_j|<1
$$

for every eigenvalue, which gives

$$
0<\eta<\frac2{\lambda_{\max}}.
$$

For a fixed step on this quadratic, the best worst-direction contraction balances the extreme factors:

$$
1-\eta\mu=-(1-\eta L).
$$

Solving gives

$$
\eta_{\mathrm{balanced}}=\frac2{L+\mu},
$$

with parameter contraction factor

$$
q=\frac{L-\mu}{L+\mu}
=
\frac{\kappa-1}{\kappa+1}.
$$

The objective gap is a weighted sum of squared error coefficients, so its worst-case factor is the square of the parameter contraction factor.

## A complete two-coordinate example

Use the constructed objective

$$
f(x,y)=\frac12(x^2+9y^2).
$$

The minimum is at the origin. Its curvature constants and condition number are

$$
\mu=1,
\qquad
L=9,
\qquad
\kappa=9.
$$

Start from

$$
(x_0,y_0)=(1,1),
\qquad
f_0=5.
$$

With step size

$$
\eta=\frac19,
$$

the update is

$$
x_{t+1}=\frac89x_t,
\qquad
y_{t+1}=0.
$$

The first two iterates give

$$
(x_1,y_1)=\left(\frac89,0\right),
\qquad
f_1=\frac{32}{81},
$$

and

$$
(x_2,y_2)=\left(\frac{64}{81},0\right),
\qquad
f_2=\frac{2048}{6561}.
$$

The sharp direction disappears immediately, but the shallow direction contracts slowly.

The balanced step is

$$
\eta=\frac2{9+1}=\frac15.
$$

It produces

$$
x_{t+1}=0.8x_t,
\qquad
y_{t+1}=-0.8y_t.
$$

Therefore,

$$
f_t=5(0.64)^t.
$$

The first two objective values are

$$
f_1=3.2,
\qquad
f_2=2.048.
$$

This step has a better asymptotic worst-direction contraction, but a worse first step for this particular starting point. “Optimal fixed step” does not mean best at every finite iteration from every initialization.

Finally, choose

$$
\eta=\frac14.
$$

The second coordinate multiplies by

$$
1-\frac94=-1.25,
$$

so it diverges. The first objective value already rises to

$$
\frac12(0.75^2+9\cdot1.25^2)=7.3125.
$$

Every number follows from the two scalar recurrences.

## Preconditioning and regularization change different things

In the example, define new coordinates

$$
z_1=x,
\qquad
z_2=3y.
$$

Then

$$
f=\frac12(z_1^2+z_2^2).
$$

The curvature is equal in both directions. A unit gradient step in these coordinates reaches the minimum immediately.

More generally, for an invertible coordinate map,

$$
z=B\theta,
$$

the transformed gradient is

$$
\nabla_z f(B^{-1}z)=B^{-\top}\nabla_\theta f.
$$

A gradient step in the new coordinates becomes

$$
\theta^+
=
\theta-\eta B^{-1}B^{-\top}\nabla_\theta f.
$$

This is preconditioning: changing how the update measures and scales parameter movement. Finding an ideal transformation may itself be expensive, and a changing neural-network Hessian makes a fixed ideal transformation unlikely.

Regularization instead changes the objective. Adding

$$
\frac\lambda2\lVert\theta\rVert_2^2
$$

to a quadratic shifts every Hessian eigenvalue:

$$
H_{\mathrm{regularized}}=H+\lambda I.
$$

Its condition number becomes

$$
\frac{L+\lambda}{\mu+\lambda}.
$$

This can improve conditioning, but the optimum generally moves. For example,

$$
\frac12(\theta-2)^2+\frac\lambda2\theta^2
$$

has derivative

$$
(\theta-2)+\lambda\theta,
$$

so its minimizer is

$$
\theta^\star=\frac2{1+\lambda}.
$$

Better conditioning is not a free improvement to the original estimation problem; the penalty imposes a preference for a different solution.

## Constraints alter the optimality condition

For a constrained problem, a nonzero gradient can be entirely compatible with optimality.

Consider

$$
\min_{-1\leq x\leq1}\frac12(x-3)^2.
$$

The optimum is the right boundary:

$$
x^\star=1,
\qquad
f'(x^\star)=-2.
$$

The negative gradient points outside the feasible interval. There is no permitted descent direction.

For differentiable convex optimization over a convex feasible set, the relevant condition is

$$
\nabla f(x^\star)^\top(z-x^\star)\geq0
\qquad
\text{for every feasible }z.
$$

Necessity follows by considering short feasible segments from the optimum. Sufficiency follows from the convex supporting-plane inequality.

In the scalar example,

$$
-2(z-1)\geq0
$$

for every feasible point, confirming optimality.

A soft penalty need not enforce the same constraint. Replacing the upper bound with

$$
\frac12(x-3)^2+
\frac\lambda2\max(0,x-1)^2
$$

gives, in the violating region,

$$
(x-3)+\lambda(x-1)=0.
$$

The solution is

$$
x=\frac{3+\lambda}{1+\lambda}>1
$$

for every finite nonnegative penalty weight. Some penalty formulations can be exact under additional conditions; this particular quadratic penalty is not.

## What remains true without convexity

Smoothness alone still gives a useful statement if the objective is bounded below. Sum the descent inequality:

$$
\frac1{2L}\sum_{t=0}^{T-1}
\lVert\nabla f(\theta_t)\rVert_2^2
\leq
f(\theta_0)-f_{\mathrm{lower}}.
$$

At least one iterate must therefore satisfy

$$
\min_{0\leq t<T}
\lVert\nabla f(\theta_t)\rVert_2^2
\leq
\frac{2L[f(\theta_0)-f_{\mathrm{lower}}]}{T}.
$$

This establishes progress toward a small gradient under the stated assumptions. A small gradient can occur near a minimum, a saddle, or a flat region. It does not certify a global minimum.

Likewise, low training loss establishes success against the chosen objective. The objective may still reward unwanted acquisition cues, and checkpoint selection adds a further criterion. Optimization analysis and evidence-use auditing answer different questions that need to be connected explicitly.

## Revision checklist

| Question | What I should be able to derive |
|---|---|
| What does convexity guarantee? | Prove that stationary points and local minima are global minima. |
| What does it not guarantee? | Give examples without an attained optimum or without uniqueness. |
| Why does smoothness produce a quadratic bound? | Integrate the gradient along a segment. |
| Where does the gradient update come from? | Minimize the local linear-plus-quadratic model. |
| Which step sizes ensure descent? | Substitute the update into the smoothness inequality. |
| Why is the convex rate inverse in iteration count? | Reproduce the cancellation and telescoping argument. |
| Why does strong convexity give geometric convergence? | Relate gradient norm to objective gap. |
| Why does the condition number matter? | Explain competing curvature scales and loss-rescaling invariance. |
| How do quadratic directions evolve? | Derive the scalar multiplier for each eigenvector. |
| Are preconditioning and regularization equivalent? | Identify whether the coordinate system or objective changes. |
| Can a constrained optimum have a nonzero gradient? | Check the boundary example. |
| What survives without convexity? | Derive a small-gradient guarantee and state its limits. |

## Why it matters for my work

Optimization theory helps me separate a training failure from a mismatch between the objective and the clinical question. I want to record sampling weights, regularization, constraints, and checkpoint selection as concrete choices that shape the model being audited.

## What I have not resolved

- Which clinically motivated requirements can be expressed through measurements that training cannot satisfy superficially?
- Compare evidence-use audits across checkpoints with similar held-out predictive performance but different training procedures.
