---
layout: study_note
title: "Primal and Dual Problems: The Max-Min Inequality and What the Gap Certifies"
description: "The one inequality the whole of Lagrangian duality rests on, why swapping to the dual changes the size of the problem, and why a duality gap is useful information rather than a failure."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "algebra-and-optimisation"
category_title: "Linear Algebra & Optimisation"
subgroup: "Constraints & Duality"
order: 9
source: "Independent study"
written: true
updated: "2026-09-15"
---

The primal problem searches for a feasible solution with a small objective. The dual searches for a large lower bound on every feasible objective. When the two values meet, neither search can improve.

This interpretation separates three questions that are often compressed into “solve the dual”: how the lower bound is constructed, when it can become exact, and whether optimising that bound is computationally useful.

## The max–min inequality, with the order exposed

For any function on a product of two non-empty sets,

$$
\sup_y\inf_x F(x,y)
\le
\inf_x\sup_y F(x,y),
$$

whenever the expressions are well-defined as extended values.

Fix arbitrary points in the two sets. By the definitions of infimum and supremum,

$$
\inf_{x'}F(x',y)
\le
F(x,y)
\le
\sup_{y'}F(x,y').
$$

The left expression no longer depends on the fixed first argument. The right expression no longer depends on the fixed second argument. Hence, for every fixed first argument,

$$
\sup_y\inf_{x'}F(x',y)
\le
\sup_{y'}F(x,y').
$$

Taking the infimum of the right side establishes the result.

The distinction between an extremum and a supremum or infimum matters. For example,

$$
\inf_{x\in\mathbb R}e^x=0,
$$

but there is no minimiser. A sequence can approach the optimal value without any finite point attaining it. This distinction later explains why a zero duality gap need not provide finite optimal multipliers.

A finite example also shows that swapping the order can change the answer. Let the first player minimise over rows and the second maximise over columns:

$$
F=
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
$$

For either fixed column, the row player can obtain negative one. Thus

$$
\max_{\text{column}}\min_{\text{row}}F=-1.
$$

For either fixed row, the column player can obtain positive one. Thus

$$
\min_{\text{row}}\max_{\text{column}}F=1.
$$

The inequality is strict even though every extremum is attained. Equality requires additional structure; it is not an algebraic permission to exchange two symbols.

## Encoding a constraint by an infinite penalty

Consider the minimisation problem

$$
p^\star
=
\inf_x f(x)
\quad\text{subject to}\quad
g_i(x)\le 0,\quad h_j(x)=0.
$$

For a scalar inequality value,

$$
\sup_{\lambda\ge 0}\lambda g
=
\begin{cases}
0,&g\le 0,\\
+\infty,&g>0.
\end{cases}
$$

If the inequality holds, choosing a zero multiplier gives zero and no non-negative multiplier gives a larger value. If the inequality fails, increasing the multiplier makes the expression arbitrarily large.

For an equality,

$$
\sup_{\nu\in\mathbb R}\nu h
=
\begin{cases}
0,&h=0,\\
+\infty,&h\ne 0.
\end{cases}
$$

The unrestricted sign allows the multiplier to follow the sign of any violation.

With

$$
L(x,\lambda,\nu)
=
f(x)+\lambda^{\mathsf T}g(x)+\nu^{\mathsf T}h(x),
$$

the primal is therefore exactly

$$
p^\star
=
\inf_x\sup_{\lambda\ge 0,\nu}L(x,\lambda,\nu).
$$

The inner supremum preserves the objective at feasible points and excludes infeasible ones with an infinite value. This is an exact representation of constraints, not a finite penalty approximation.

Interchanging the order defines the Lagrange dual:

$$
d^\star
=
\sup_{\lambda\ge 0,\nu}q(\lambda,\nu),
\qquad
q(\lambda,\nu)=\inf_xL(x,\lambda,\nu).
$$

The max–min inequality immediately gives

$$
d^\star\le p^\star.
$$

This is weak duality.

## Why every dual feasible point supplies a bound

The same result has a direct proof that is especially useful when reading a solver output.

For any primal feasible point and non-negative inequality multipliers,

$$
L(x,\lambda,\nu)\le f(x).
$$

Taking an infimum over the Lagrangian's first argument gives

$$
q(\lambda,\nu)\le f(x).
$$

Thus a single dual feasible point bounds all primal feasible points. It does not need to be dual optimal.

An important qualification is that the inner infimum must actually be evaluated or bounded from below. Substituting an arbitrary trial point into the Lagrangian gives an upper bound on its infimum:

$$
q(\lambda,\nu)\le L(\widetilde x,\lambda,\nu).
$$

That substituted value is not automatically a valid lower bound on the primal optimum. Solving the inner problem is part of constructing the certificate.

The dual function can also equal negative infinity. For example,

$$
\inf_{x\in\mathbb R}cx
=
\begin{cases}
0,&c=0,\\
-\infty,&c\ne 0.
\end{cases}
$$

This observation is responsible for many constraints that appear in dual formulations. A coefficient must vanish to prevent an unconstrained linear direction from driving the inner problem downward without bound.

## The dual is concave even when the primal is not

For fixed primal variables, the Lagrangian is affine in the multipliers. Taking an infimum of affine functions gives a concave function.

To verify the direction, write two multiplier vectors collectively as two points and choose a mixing weight between zero and one. Then

$$
\begin{aligned}
q(tz_1+(1-t)z_2)
&=
\inf_x\left[tL(x,z_1)+(1-t)L(x,z_2)\right]\\
&\ge
t\inf_xL(x,z_1)+(1-t)\inf_xL(x,z_2)\\
&=
tq(z_1)+(1-t)q(z_2).
\end{aligned}
$$

The inequality holds because each Lagrangian value is at least its own infimum.

Maximising this concave function over a convex multiplier domain is a convex optimisation problem. That does not mean it exactly solves a non-convex primal. The dual may optimise a lower bound whose best possible value remains strictly below the primal optimum.

Nor does concavity make evaluation cheap. The inner infimum can itself be a difficult global optimisation problem. A compact outer representation does not remove the cost hidden inside the function being optimised.

## A complete quadratic example and an early stopping certificate

Take

$$
\min_{x,y}x^2+y^2
\qquad
\text{subject to}\qquad
x+y=1.
$$

Substitute the equality into the objective:

$$
x^2+(1-x)^2
=
2\left(x-\frac12\right)^2+\frac12.
$$

Hence

$$
x^\star=y^\star=\frac12,
\qquad
p^\star=\frac12.
$$

Use the equality multiplier convention

$$
L=x^2+y^2+\nu(1-x-y).
$$

Completing squares gives

$$
L
=
\left(x-\frac\nu2\right)^2
+
\left(y-\frac\nu2\right)^2
+
\nu-\frac{\nu^2}{2}.
$$

The inner infimum is now visible:

$$
q(\nu)=\nu-\frac{\nu^2}{2},
$$

attained at

$$
x=y=\frac\nu2.
$$

Complete the remaining square:

$$
q(\nu)
=
\frac12-\frac12(\nu-1)^2.
$$

The dual optimum is

$$
\nu^\star=1,
\qquad
d^\star=\frac12.
$$

Both sides independently give the same value.

Now stop before reaching either optimum. Choose the feasible primal point

$$
(x,y)=(0.6,0.4),
$$

whose objective is

$$
P=0.36+0.16=0.52.
$$

Choose the dual point

$$
\nu=0.8,
$$

whose value is

$$
D=0.8-\frac{0.64}{2}=0.48.
$$

Weak duality gives the interval

$$
0.48\le p^\star\le 0.52.
$$

The primal candidate is therefore at most

$$
P-D=0.04
$$

above the true optimum. Its actual error is two hundredths, but that fact was not needed to establish the certificate.

Notice that the inner minimiser corresponding to the chosen multiplier is

$$
(x,y)=(0.4,0.4),
$$

which violates the primal equality. Minimising a Lagrangian at arbitrary multipliers does not automatically recover a feasible primal solution.

## What a primal–dual gap measures

For primal feasible variables and dual feasible multipliers,

$$
0\le f(x)-p^\star\le f(x)-q(\lambda,\nu).
$$

The rightmost difference is a computable upper bound on objective suboptimality. It remains useful even before either side is optimal.

It can be decomposed as

$$
f(x)-q(\lambda,\nu)
=
\underbrace{f(x)-L(x,\lambda,\nu)}_{\text{constraint contribution}}
+
\underbrace{L(x,\lambda,\nu)-q(\lambda,\nu)}_{\text{inner minimisation error}}.
$$

Both terms are non-negative for a feasible primal point. The first vanishes through complementary slackness. The second vanishes when the primal point minimises the Lagrangian.

This connects duality directly to the [KKT conditions](/study/kkt-conditions-and-shadow-prices/).

A printed difference between two objective values is only a certificate when the associated feasibility conditions hold. In the quadratic example, the infeasible point at the origin has objective zero. Comparing that zero with the optimal dual value would produce a negative “gap,” which signals an invalid comparison, not a better solution.

Also distinguish the candidate gap from the optimal duality gap:

$$
\text{candidate gap}=f(x)-q(\lambda,\nu),
$$

$$
\text{optimal gap}=p^\star-d^\star.
$$

An algorithmic gap may shrink through better optimisation. A positive optimal gap cannot be eliminated by solving the same primal and dual formulations more accurately.

## Strong duality needs more than the word convex

For convex objectives and inequalities with affine equalities, Slater's strict-feasibility condition is a standard sufficient condition for strong duality. Under the usual finite-value assumptions it also provides dual attainment.

The geometric idea uses the value of the problem as its constraint bounds vary. Convexity makes the epigraph of this perturbation value convex. A supporting hyperplane at the original optimum supplies multiplier coefficients. Regularity prevents the only available support from being vertical, which would fail to provide finite useful prices.

Convexity alone is insufficient. Consider the domain and problem

$$
y>0,
\qquad
\min_{x,y}e^{-x}
\quad\text{subject to}\quad
\frac{x^2}{y}\le 0.
$$

The constraint forces

$$
x=0,
$$

so every feasible point has objective one:

$$
p^\star=1.
$$

Both functions are convex. For the constraint function,

$$
\nabla^2\left(\frac{x^2}{y}\right)
=
\frac2y
\begin{pmatrix}
1\\-x/y
\end{pmatrix}
\begin{pmatrix}
1&-x/y
\end{pmatrix},
$$

which is positive semidefinite.

For any non-negative finite multiplier,

$$
L(x,y,\lambda)
=
e^{-x}+\lambda\frac{x^2}{y}
\ge 0.
$$

Along the sequence

$$
x=t,\qquad y=t^3,\qquad t\to\infty,
$$

the Lagrangian becomes

$$
e^{-t}+\frac{\lambda}{t}\longrightarrow 0.
$$

Therefore

$$
q(\lambda)=0
\qquad\text{for every }\lambda\ge 0,
$$

and

$$
d^\star=0<p^\star=1.
$$

Strict feasibility is impossible because the constraint function is never negative.

Failure of Slater's condition does not always produce a gap. For instance, minimising the identity function subject to its argument's square being non-positive has equal primal and dual optimal values, but the dual optimum is approached only as the multiplier grows without bound. Regularity, equality of values, and attainment are related but distinct properties.

## Convex conjugates from their definition

The convex conjugate of a function is

$$
f^\ast(s)
=
\sup_x\left(s^{\mathsf T}x-f(x)\right).
$$

It records the largest intercept adjustment needed when comparing the function with a linear slope.

The definition immediately implies

$$
s^{\mathsf T}x-f(x)\le f^\ast(s),
$$

or

$$
f(x)+f^\ast(s)\ge s^{\mathsf T}x.
$$

This is the Fenchel–Young inequality. It is another lower-bound mechanism.

For the squared Euclidean norm, complete the square:

$$
s^{\mathsf T}x-\lVert x\rVert^2
=
-\left\lVert x-\frac s2\right\rVert^2
+\frac14\lVert s\rVert^2.
$$

Hence

$$
f^\ast(s)=\frac14\lVert s\rVert^2.
$$

For the absolute value in one dimension,

$$
f^\ast(s)=\sup_x(sx-\lvert x\rvert).
$$

If the absolute value of the slope is at most one, then

$$
sx-\lvert x\rvert\le 0,
$$

with equality at zero. If the slope exceeds that interval, choosing a sufficiently large argument with the matching sign sends the expression to positive infinity. Thus

$$
f^\ast(s)
=
\begin{cases}
0,&\lvert s\rvert\le 1,\\
+\infty,&\lvert s\rvert>1.
\end{cases}
$$

A non-smooth penalty in the primal has become a constraint in the conjugate. This is why conjugate tables often contain indicator functions rather than ordinary-looking formulas.

To derive a general dual, rewrite

$$
\min_x f(x)+g(Ax)
$$

using an auxiliary variable:

$$
\min_{x,z}f(x)+g(z)
\qquad\text{subject to}\qquad
Ax-z=0.
$$

Its Lagrangian separates:

$$
L=f(x)+g(z)+u^{\mathsf T}(Ax-z).
$$

Taking the two infima gives

$$
\inf_x\left[f(x)+(A^{\mathsf T}u)^{\mathsf T}x\right]
=
-f^\ast(-A^{\mathsf T}u),
$$

and

$$
\inf_z\left[g(z)-u^{\mathsf T}z\right]
=
-g^\ast(u).
$$

The dual is therefore

$$
\sup_u
\left[
-f^\ast(-A^{\mathsf T}u)-g^\ast(u)
\right].
$$

The signs come from the chosen equality, not from a formula that should be memorised independently. Equality of primal and dual values still requires appropriate regularity.

## Minimum norm: a smaller dual with a numerical check

Consider

$$
\min_x\lVert x\rVert^2
\qquad\text{subject to}\qquad
Ax=b.
$$

Using

$$
L=\lVert x\rVert^2+u^{\mathsf T}(Ax-b),
$$

stationarity in the primal variable gives

$$
2x+A^{\mathsf T}u=0,
\qquad
x=-\frac12A^{\mathsf T}u.
$$

Substitution yields

$$
q(u)
=
-\frac14u^{\mathsf T}AA^{\mathsf T}u-b^{\mathsf T}u.
$$

When the rows of the matrix are independent,

$$
AA^{\mathsf T}
$$

is invertible. The dual stationarity equation is

$$
-\frac12AA^{\mathsf T}u-b=0,
$$

so

$$
u^\star=-2(AA^{\mathsf T})^{-1}b,
$$

and

$$
x^\star=A^{\mathsf T}(AA^{\mathsf T})^{-1}b.
$$

The rank assumption is essential. Without it, one must solve the consistent linear system or use an appropriate generalised inverse; writing an ordinary inverse does not make it exist.

Take

$$
A=
\begin{pmatrix}
1&1&0\\
0&1&1
\end{pmatrix},
\qquad
b=
\begin{pmatrix}1\\1\end{pmatrix}.
$$

Then

$$
AA^{\mathsf T}
=
\begin{pmatrix}2&1\\1&2\end{pmatrix},
\qquad
(AA^{\mathsf T})^{-1}
=
\frac13
\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
$$

The solution is

$$
x^\star=
\begin{pmatrix}
1/3\\2/3\\1/3
\end{pmatrix},
\qquad
u^\star=
\begin{pmatrix}
-2/3\\-2/3
\end{pmatrix}.
$$

The constraints give one in each row, and the primal objective is

$$
\frac19+\frac49+\frac19=\frac23.
$$

For the dual,

$$
(u^\star)^{\mathsf T}AA^{\mathsf T}u^\star=\frac83,
\qquad
b^{\mathsf T}u^\star=-\frac43,
$$

so

$$
q(u^\star)
=
-\frac14\frac83+\frac43
=
\frac23.
$$

Feasibility and matching values certify the result.

## An unconstrained problem can still have a useful dual

The claim that an unconstrained least-squares problem has “nothing to dualise” is misleading. Introduce its residual explicitly:

$$
\min_x\frac12\lVert Ax-b\rVert^2
=
\min_{x,r}\frac12\lVert r\rVert^2
\quad\text{subject to}\quad
Ax-b-r=0.
$$

The Lagrangian is

$$
L=\frac12\lVert r\rVert^2+u^{\mathsf T}(Ax-b-r).
$$

Its infimum over the residual occurs at

$$
r=u.
$$

Its infimum over the unrestricted primal variable is finite only when

$$
A^{\mathsf T}u=0.
$$

Thus the dual becomes

$$
\max_u
-\frac12\lVert u\rVert^2-b^{\mathsf T}u
\qquad
\text{subject to}\qquad
A^{\mathsf T}u=0.
$$

At an optimum, the dual variable is the residual, and its constraint says that the residual is orthogonal to the columns of the design matrix. This is the geometry behind the normal equations.

For

$$
A=
\begin{pmatrix}1\\1\end{pmatrix},
\qquad
b=
\begin{pmatrix}1\\3\end{pmatrix},
$$

the primal optimum is two, with residual

$$
u=
\begin{pmatrix}1\\-1\end{pmatrix}.
$$

The primal objective is one. The dual constraint holds because the residuals sum to zero, and the dual value is

$$
-\frac12(1+1)-(1-3)=1.
$$

Dual variables often encode a familiar residual or balance condition once the algebra is completed.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| Prove the max–min inequality | Keep track of which variable each bound depends on |
| Encode an inequality using a supremum | Explain why its multiplier is non-negative |
| Produce a lower bound from one dual point | Evaluate the inner infimum correctly |
| Prove dual concavity | Use the infimum of affine functions |
| Certify an approximate primal solution | Check feasibility before computing a gap |
| Separate strong duality from attainment | Give a case where only a limiting multiplier works |
| Explain why convexity alone is insufficient | Reproduce the positive-gap example |
| Derive a conjugate | Complete a square or analyse unbounded directions |
| Recover the minimum-norm solution | State the row-rank condition |
| Dualise least squares | Identify the dual variable as an orthogonal residual |

## Why it matters for my work

A primal–dual gap is useful because it is a proved bound on a specified optimisation objective. I should preserve that meaning. Benchmark scores and stress tests can complement one another, but they do not automatically bracket deployment performance.

## What I have not resolved

For objectives used in my experiments, I need to identify which tractable relaxations provide informative lower bounds and which produce gaps dominated by the relaxation rather than incomplete optimisation.
