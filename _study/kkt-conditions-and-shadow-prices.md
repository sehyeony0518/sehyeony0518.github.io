---
layout: study_note
title: "KKT Conditions and Shadow Prices: What a Lagrange Multiplier Is Actually Telling You"
description: "Complementary slackness, the multiplier as the sensitivity of the optimum to its constraint, and reading the SVM's alphas as a statement about which samples matter."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "algebra-and-optimisation"
category_title: "Linear Algebra & Optimisation"
subgroup: "Constraints & Duality"
order: 10
source: "Independent study"
written: true
updated: "2026-09-15"
---

A constrained optimum contains more information than the location of its minimiser. Its multipliers describe which restrictions support the solution and how the optimal objective responds when those restrictions change.

That interpretation requires care. An active constraint can have a zero multiplier. A multiplier is a derivative only when the optimal-value function is differentiable. Comparing multiplier magnitudes without checking constraint units is meaningless. The purpose of this note is to derive the conditions and their interpretation together.

## Fixing the problem and its sign convention

Consider

$$
\begin{aligned}
\min_{x\in\mathbb R^d}\quad & f(x)\\
\text{subject to}\quad
& g_i(x)\le 0,\qquad i=1,\ldots,m,\\
& h_j(x)=0,\qquad j=1,\ldots,r.
\end{aligned}
$$

Initially assume differentiable functions. Any additional restrictions on the variable must be included in the formulation. Otherwise a stationarity equation can accidentally allow directions that the original problem forbids.

Define the Lagrangian by

$$
L(x,\lambda,\nu)
=
f(x)+\sum_i\lambda_i g_i(x)+\sum_j\nu_j h_j(x),
\qquad
\lambda_i\ge 0.
$$

Why must the inequality multipliers be non-negative? At a feasible point,

$$
\lambda_i g_i(x)\le 0,
\qquad
\nu_jh_j(x)=0.
$$

Therefore

$$
L(x,\lambda,\nu)\le f(x).
$$

The dual function

$$
q(\lambda,\nu)=\inf_x L(x,\lambda,\nu)
$$

is consequently a lower bound on every feasible objective:

$$
q(\lambda,\nu)\le L(x,\lambda,\nu)\le f(x).
$$

A negative inequality multiplier would reverse the contribution of a satisfied inequality and destroy this argument. Equality multipliers have no sign restriction because their terms vanish at every feasible point.

Signs also depend on how a constraint is written. The requirement

$$
x+y\ge b
$$

becomes

$$
b-x-y\le 0.
$$

Its multiplier enters the Lagrangian as

$$
\lambda(b-x-y).
$$

Writing the equivalent inequality in the opposite direction while keeping the same multiplier convention changes the problem.

## Deriving the four KKT conditions

Suppose a primal optimum and dual optimum attain the same finite value:

$$
f(x^\star)=q(\lambda^\star,\nu^\star).
$$

Apply the lower-bound chain at those points:

$$
q(\lambda^\star,\nu^\star)
\le
L(x^\star,\lambda^\star,\nu^\star)
\le
f(x^\star).
$$

The endpoints agree, so both inequalities must be equalities.

The first equality says that the primal optimum minimises the Lagrangian with the optimal multipliers fixed. For an unconstrained differentiable inner minimisation, this gives stationarity:

$$
\nabla f(x^\star)
+
\sum_i\lambda_i^\star\nabla g_i(x^\star)
+
\sum_j\nu_j^\star\nabla h_j(x^\star)
=0.
$$

The second equality gives

$$
\sum_i\lambda_i^\star g_i(x^\star)=0,
$$

because the equality-constraint terms vanish. Every term in this sum is non-positive. A sum of non-positive numbers can equal zero only when every term equals zero:

$$
\lambda_i^\star g_i(x^\star)=0
\qquad\text{for every }i.
$$

This is complementary slackness. Together, the conditions are

$$
\begin{array}{ll}
\text{Primal feasibility:}
&
g_i(x^\star)\le 0,\quad h_j(x^\star)=0,
\\[3pt]
\text{Dual feasibility:}
&
\lambda_i^\star\ge 0,
\\[3pt]
\text{Stationarity:}
&
\nabla_xL(x^\star,\lambda^\star,\nu^\star)=0,
\\[3pt]
\text{Complementary slackness:}
&
\lambda_i^\star g_i(x^\star)=0.
\end{array}
$$

They are not four unrelated equations to memorise. Feasibility establishes the lower-bound chain; stationarity and complementary slackness make its two inequalities exact.

For a convex problem, where the objective and inequality functions are convex and equality constraints are affine, these conditions are sufficient for global optimality. Stationarity then makes the candidate a global minimiser of the convex Lagrangian. For every feasible comparison point,

$$
f(x)
\ge L(x,\lambda^\star,\nu^\star)
\ge L(x^\star,\lambda^\star,\nu^\star)
=f(x^\star).
$$

That is the certificate.

## Necessity requires a constraint qualification

Convexity makes a valid KKT certificate sufficient. It does not automatically ensure that suitable multipliers exist.

A standard sufficient regularity condition is Slater's condition: a point satisfies the affine equalities and satisfies every inequality strictly. For differentiable convex functions on the full variable space, a finite attained optimum together with this condition gives the usual necessity of KKT.

The failure without regularity is visible in one dimension:

$$
\min_x x
\qquad\text{subject to}\qquad
x^2\le 0.
$$

The only feasible point is

$$
x^\star=0,
$$

so it is certainly optimal. But stationarity would require

$$
1+2\lambda x^\star=0,
$$

which becomes

$$
1=0.
$$

No finite multiplier works. The feasible set is a single point, but the constraint gradient is zero there. Its first-order description fails to represent the restriction.

Non-convexity introduces a different limitation. Consider

$$
\min_x -x^2
\qquad\text{subject to}\qquad
-1\le x\le 1.
$$

At the origin, both inequalities are strict, their multipliers can be zero, and the objective gradient is zero. All KKT conditions hold. Yet the origin has objective zero, while either endpoint has objective negative one.

Thus there are two separate questions:

1. Must an optimum satisfy KKT?
2. Does satisfying KKT establish an optimum?

Constraint qualifications address the first. Convexity supplies a useful answer to the second.

## What complementary slackness actually implies

An inequality is active when

$$
g_i(x^\star)=0.
$$

Complementary slackness gives the implications

$$
g_i(x^\star)<0
\quad\Longrightarrow\quad
\lambda_i^\star=0,
$$

and

$$
\lambda_i^\star>0
\quad\Longrightarrow\quad
g_i(x^\star)=0.
$$

The converses are false.

For example,

$$
\min_x x^2
\qquad\text{subject to}\qquad
-x\le 0
$$

has optimum zero. The constraint is active, but stationarity gives

$$
2x^\star-\lambda^\star=0
\quad\Longrightarrow\quad
\lambda^\star=0.
$$

The unconstrained objective already prefers the boundary point. No positive multiplier is needed to hold it there.

Geometrically, stationarity balances the objective gradient against constraint normals. For affine constraints, the gradient of a constraint points toward increasing violation. Non-negative combinations of active inequality normals can oppose the direction in which the objective wants to decrease. Equality normals can be used with either sign because movement across either side violates an equality.

This interpretation also explains why a multiplier need not be unique. If two active constraints have the same normal, their contributions can be redistributed while leaving the stationarity equation unchanged.

## A quadratic example with an exact shadow price

Define the entire problem:

$$
p(b)
=
\min_{x,y}
\frac{x^2+y^2}{5}
\qquad
\text{subject to}\qquad
x+y\ge b,\quad x\le 2.
$$

For

$$
0<b<4,
$$

the upper bound on the first variable will be inactive. To see the minimiser directly, write

$$
x^2+y^2
=
\frac{(x+y)^2+(x-y)^2}{2}.
$$

For a fixed sum, the objective is smallest when the two variables agree. Since the required sum is positive, increasing it beyond the requirement increases the minimum possible objective. Therefore

$$
x^\star=y^\star=\frac b2,
\qquad
p(b)=\frac{b^2}{10}.
$$

Now obtain the same answer from KKT. The Lagrangian is

$$
L
=
\frac{x^2+y^2}{5}
+\lambda(b-x-y)
+\mu(x-2).
$$

Stationarity gives

$$
\frac{2x}{5}-\lambda+\mu=0,
\qquad
\frac{2y}{5}-\lambda=0.
$$

Since the first variable is strictly below its upper bound,

$$
\mu=0.
$$

The sum constraint is active, so

$$
x+y=b.
$$

Solving yields

$$
x^\star=y^\star=\frac b2,
\qquad
\lambda^\star=\frac b5.
$$

At a requirement of one, all quantities are explicit:

$$
(x^\star,y^\star)=\left(\frac12,\frac12\right),
\qquad
p(1)=0.1,
\qquad
(\lambda^\star,\mu^\star)=(0.2,0).
$$

The constraint slacks are zero and one and a half, respectively. Their products with the multipliers are both zero.

Tightening the requirement gives

$$
p(1.1)-p(1)
=
\frac{1.21-1}{10}
=
0.021.
$$

The first-order prediction is

$$
\lambda^\star(0.1)=0.020.
$$

The remaining amount is exactly

$$
\frac{(0.1)^2}{10}=0.001.
$$

Relaxing the requirement instead gives

$$
p(0.9)-p(1)
=
\frac{0.81-1}{10}
=
-0.019.
$$

The derivative predicts negative two hundredths; curvature again contributes one thousandth. These are calculated values of a specified problem, not observations from an unspecified solver run.

The active set eventually changes. When the requirement exceeds four, the symmetric solution would violate the upper bound. Then

$$
x^\star=2,\qquad y^\star=b-2,
$$

and

$$
p(b)=\frac{4+(b-2)^2}{5}.
$$

Stationarity now gives

$$
\lambda^\star=\frac{2(b-2)}5,
\qquad
\mu^\star=\frac{2(b-4)}5.
$$

The formerly inactive restriction acquires a positive multiplier. A shadow price belongs to a particular problem and parameter regime.

## Deriving sensitivity, including its minus sign

Perturb the general inequalities to

$$
g_i(x)\le u_i
$$

and let the new optimal value be

$$
p(u).
$$

The perturbed Lagrangian is

$$
L_u(x,\lambda,\nu)
=
L(x,\lambda,\nu)-\lambda^{\mathsf T}u.
$$

Fix an optimal multiplier for the unperturbed problem. Weak duality for the perturbed problem gives

$$
p(u)
\ge
q(\lambda^\star,\nu^\star)
-
(\lambda^\star)^{\mathsf T}u.
$$

If strong duality holds at the original problem, this becomes

$$
p(u)
\ge
p(0)-(\lambda^\star)^{\mathsf T}u.
$$

The vector of negative multipliers defines a supporting affine lower bound on the value function. When that function is differentiable,

$$
\nabla p(0)=-\lambda^\star.
$$

The minus sign has a concrete meaning: increasing the right-hand side relaxes an inequality, so the minimum cannot increase.

In the quadratic example, increasing the requirement tightens the constraint. That parameter has the opposite sign from an inequality relaxation, which explains why

$$
p'(b)=\lambda^\star
$$

there.

Differentiability cannot be assumed. Consider

$$
p(u)
=
\min_x x
\qquad
\text{subject to}\qquad
-x\le u,\quad -x\le 0.
$$

Directly,

$$
p(u)=\max(-u,0).
$$

At zero, stationarity requires

$$
\lambda_1+\lambda_2=1,
\qquad
\lambda_1,\lambda_2\ge 0.
$$

There are many optimal multipliers. Their negatives supply the slopes between negative one and zero that support the kink. There is no single derivative to report.

A zero multiplier also needs a precise interpretation. Under a global primal–dual certificate, relaxing just that constraint cannot improve the optimum: the supporting lower bound remains the original value, and the old solution remains feasible. Tightening it may change the value, including at second order. Removing it can introduce additional optimal solutions, even when the existing optimum remains optimal.

## Constraint scaling changes the reported price

Replace a constraint by an equivalent scaled form:

$$
g_i(x)\le 0
\qquad\longleftrightarrow\qquad
c\,g_i(x)\le 0,
\qquad c>0.
$$

To preserve the same Lagrangian contribution, the new multiplier must satisfy

$$
\widetilde\lambda_i c=\lambda_i,
\qquad
\widetilde\lambda_i=\frac{\lambda_i}{c}.
$$

The feasible set and optimum have not changed, but the numerical multiplier has.

For the quadratic example, writing the sum requirement as

$$
10(b-x-y)\le 0
$$

changes its multiplier at the original requirement from

$$
0.2
\quad\text{to}\quad
0.02.
$$

Consequently, the largest raw multiplier is not automatically the most important bottleneck. A useful comparison specifies physically meaningful changes and computes

$$
-\sum_i\lambda_i^\star\Delta u_i.
$$

Multiplier units are objective units per unit of constraint relaxation.

Redundant constraints create another ambiguity. Duplicating the same inequality can split its original multiplier among two copies. The total contribution to stationarity is identifiable even when the individual numbers are not.

## Reading SVM multipliers without reversing implications

The soft-margin SVM solves

$$
\min_{w,b,\xi}
\frac12\lVert w\rVert^2+C\sum_i\xi_i
$$

subject to

$$
1-\xi_i-y_i(w^{\mathsf T}x_i+b)\le 0,
\qquad
-\xi_i\le 0.
$$

Attach multipliers

$$
\alpha_i\ge 0,\qquad \beta_i\ge 0
$$

to these constraints. Stationarity in each slack variable gives

$$
C-\alpha_i-\beta_i=0.
$$

Thus

$$
0\le\alpha_i\le C.
$$

Let the signed functional margin be

$$
m_i=y_i(w^{\mathsf T}x_i+b).
$$

Complementary slackness is

$$
\alpha_i(1-\xi_i-m_i)=0,
\qquad
(C-\alpha_i)\xi_i=0.
$$

The correct cases are:

| Multiplier | Consequence |
|---|---|
| $$\alpha_i=0$$ | $$\xi_i=0$$ and $$m_i\ge 1$$ |
| $$0<\alpha_i<C$$ | $$\xi_i=0$$ and $$m_i=1$$ |
| $$\alpha_i=C$$ | $$m_i=1-\xi_i\le 1$$ |

Both endpoint cases permit a point exactly on the margin. A zero multiplier does not force strict separation from the margin, and a multiplier at its upper bound does not prove misclassification.

Stationarity in the weight vector gives

$$
w=\sum_i\alpha_i y_i x_i.
$$

A zero coefficient contributes nothing to this representation. With the summed-loss convention and a fixed penalty, deleting such a sample preserves the existing optimal solution through the same primal–dual certificate. It need not preserve uniqueness, and changing the normalisation or penalty changes the comparison.

For an interior multiplier, the margin equality determines the intercept:

$$
b=y_i-w^{\mathsf T}x_i.
$$

If no multiplier is interior, a heuristic is unnecessary. The endpoint inequalities give bounds on the intercept.

Writing

$$
t_i=w^{\mathsf T}x_i,
$$

the lower bounds are

$$
b\ge 1-t_i
\quad\text{for }y_i=1,\ \alpha_i=0,
$$

and

$$
b\ge -1-t_i
\quad\text{for }y_i=-1,\ \alpha_i=C.
$$

The other two label and endpoint combinations give upper bounds:

$$
b\le -1-t_i
\quad\text{for }y_i=-1,\ \alpha_i=0,
$$

and

$$
b\le 1-t_i
\quad\text{for }y_i=1,\ \alpha_i=C.
$$

Intersect these bounds.

For two observations at the same zero-valued input with opposite labels and penalty one, both multipliers equal one and the weight is zero. The allowed intercept interval is

$$
-1\le b\le 1.
$$

The slacks are

$$
\xi_+=1-b,\qquad \xi_-=1+b,
$$

so their sum is always two. Every intercept in the interval has the same objective. The missing interior support vector reflects real non-uniqueness.

## What to check in a numerical solution

A solver returns approximate quantities. Check the conditions separately:

$$
r_{\mathrm{ineq}}=\max_i\max(g_i(x),0),
\qquad
r_{\mathrm{eq}}=\max_j\lvert h_j(x)\rvert,
$$

$$
r_{\mathrm{stat}}=\lVert\nabla_xL\rVert,
\qquad
r_{\mathrm{comp}}=\max_i\lvert\lambda_i g_i(x)\rvert.
$$

Also check multiplier signs. A small complementary product alone proves little: a negative multiplier can make it small while invalidating the dual bound.

For the quadratic example, try

$$
x=y=0.51,\qquad \lambda=0.2,\qquad \mu=0.
$$

This point is feasible, but its stationarity residual in each coordinate is

$$
\frac{2(0.51)}5-0.2=0.004.
$$

Its objective is

$$
0.10404,
$$

while the dual value at the stated multipliers is exactly

$$
0.1.
$$

The resulting gap is

$$
0.00404.
$$

That gap bounds objective suboptimality. Whether it is an acceptable tolerance depends on objective scale. A dimensionless stopping rule and the actual residual definitions should accompany any reported solver accuracy.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| Explain why inequality multipliers are non-negative | Recover the lower-bound chain |
| Derive complementary slackness | Use equality of primal and dual values |
| Separate necessity from sufficiency | State regularity and convexity assumptions |
| Give an active constraint with zero multiplier | Minimise a square over the non-negative half-line |
| Reproduce the quadratic perturbation example | Obtain $$0.021=0.020+0.001$$ |
| Explain the sign of a shadow price | Distinguish relaxation from tightening |
| Handle a non-differentiable value function | Interpret multipliers as supporting slopes |
| Compare prices in meaningful units | Account for constraint scaling |
| Recover an SVM intercept without an interior multiplier | Intersect KKT bounds |
| Audit an approximate solution | Check feasibility, signs, stationarity, and complementarity |

## Why it matters for my work

Multipliers give interpretable sensitivity only for a specified optimisation problem. I should use them when analysing explicit resource or error constraints. An AUROC, an ablation, or a change in cohort composition is not automatically a primal value or a shadow price.

## What I have not resolved

For non-convex learning problems, I still need a reliable way to distinguish multipliers describing one local solution from sensitivity that persists across alternative solutions and training runs.
