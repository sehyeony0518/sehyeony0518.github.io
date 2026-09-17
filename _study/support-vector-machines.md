---
layout: study_note
title: "Support Vector Machines: Margin as an Inductive Bias, and What Infeasibility Tells You"
description: "Deriving the hard-margin problem from a stability argument, watching it become infeasible when the classes overlap, and reading the soft-margin fix as a priced assumption rather than a repair."
og_image: "https://sehyeony0518.github.io/assets/img/og/support-vector-machines.png"
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Learning Models & Representation"
subgroup: "Margins, Kernels & Embeddings"
order: 5
source: "Independent study"
written: true
updated: "2026-09-15"
---

An SVM chooses a linear decision rule in a specified feature space. Its defining choices are the margin criterion, the norm penalty, and the treatment of margin violations. A kernel can make that feature space implicit and the resulting boundary non-linear in the original inputs.

The derivation is worth following because the same equations explain geometric robustness, infeasibility, hinge loss, support coefficients, and the limits of interpreting scores as probabilities.

## Functional margin and geometric distance

For labels in two classes, write

$$
y_i\in\{-1,+1\},
\qquad
f(x)=w^{\mathsf T}x+b.
$$

The signed functional margin is

$$
m_i=y_if(x_i).
$$

It is positive for a correctly classified point, negative for an incorrectly classified point, and zero on the decision boundary.

It is not a distance. Multiplying the weight and intercept by a positive constant changes every functional margin but leaves the boundary unchanged.

To derive distance, find the smallest perturbation that places an input on the hyperplane:

$$
w^{\mathsf T}(x+\delta)+b=0.
$$

Thus

$$
w^{\mathsf T}\delta=-f(x).
$$

Cauchy–Schwarz gives

$$
\lvert f(x)\rvert
=
\lvert w^{\mathsf T}\delta\rvert
\le
\lVert w\rVert\lVert\delta\rVert.
$$

Therefore every such perturbation satisfies

$$
\lVert\delta\rVert
\ge
\frac{\lvert f(x)\rvert}{\lVert w\rVert}.
$$

Equality is achieved by

$$
\delta^\star
=
-\frac{f(x)}{\lVert w\rVert^2}w.
$$

Hence the distance to the hyperplane is

$$
\frac{\lvert f(x)\rvert}{\lVert w\rVert}.
$$

For labelled data, the signed geometric margin is

$$
\gamma_i
=
\frac{y_i(w^{\mathsf T}x_i+b)}{\lVert w\rVert}.
$$

This quantity is invariant to positive rescaling of the decision rule.

## What the margin says about perturbations

For a correctly classified input perturbed within a Euclidean ball,

$$
\lVert\delta\rVert\le r,
$$

the new signed score satisfies

$$
\begin{aligned}
y f(x+\delta)
&=
y f(x)+y w^{\mathsf T}\delta\\
&\ge
y f(x)-\lVert w\rVert r.
\end{aligned}
$$

Thus the sign remains positive whenever

$$
r<
\frac{y f(x)}{\lVert w\rVert}.
$$

The margin is an exact robustness radius for arbitrary Euclidean perturbations of the chosen feature vector.

The choice of geometry matters. Rescaling one feature changes Euclidean distances and the norm penalty. A large margin in features encoding a scanner marker does not establish robustness to a change that removes or reverses that marker.

The maximum-margin criterion is therefore an inductive bias: among separating rules, prefer one robust to perturbations measured in a specified geometry. The calculation establishes that geometric property. It does not, by itself, establish a generalization guarantee for an unspecified deployment distribution.

## Deriving the hard-margin problem

Suppose the finite training set is linearly separable. The objective is to maximize the smallest signed geometric margin:

$$
\max_{w,b}
\min_i
\frac{y_i(w^{\mathsf T}x_i+b)}{\lVert w\rVert}.
$$

A separating rule has a positive minimum functional margin. Divide the weight and intercept by that minimum. The rescaled rule has minimum functional margin one and describes the same boundary.

Under this normalization, maximize the reciprocal of the weight norm subject to all signed scores being at least one. Equivalently,

$$
\begin{aligned}
\min_{w,b}\quad
&\frac12\lVert w\rVert^2\\
\text{subject to}\quad
&y_i(w^{\mathsf T}x_i+b)\ge 1
\quad\text{for every }i.
\end{aligned}
$$

The factor of one half simplifies the derivative. It does not change the minimizer.

The distance from the decision boundary to either supporting margin hyperplane is

$$
\frac1{\lVert w\rVert}.
$$

The width between the two margin hyperplanes is

$$
\frac2{\lVert w\rVert}.
$$

Some descriptions call the first quantity “the margin”; others use the full width. Specifying which quantity is intended avoids a factor-of-two disagreement.

The objective is convex and the constraints are affine. This makes the hard-margin SVM a convex quadratic program, provided the constraints are feasible.

## A hard-margin solution that can be certified by inspection

Take four one-dimensional observations:

$$
(-2,-1),\quad(-1,-1),\quad(1,+1),\quad(2,+1),
$$

where each pair contains an input and label.

The two inner observations require

$$
w-b\ge 1,
\qquad
w+b\ge 1.
$$

Together,

$$
w\ge 1+\lvert b\rvert.
$$

Thus the smallest possible squared weight is attained at

$$
w^\star=1,\qquad b^\star=0.
$$

The outer observations then have signed scores two, so their constraints also hold.

The objective is

$$
P=\frac12.
$$

The distance to the nearest point is one, and the full margin width is two.

The hard-margin dual, derived below as a limiting form of the soft-margin dual, is

$$
\max_{\alpha\ge 0}
\sum_i\alpha_i
-
\frac12
\left\lVert\sum_i\alpha_i y_ix_i\right\rVert^2
$$

subject to

$$
\sum_i\alpha_i y_i=0.
$$

Choose zero coefficients for the outer observations and one half for each inner observation:

$$
\alpha=
\left(0,\frac12,\frac12,0\right)^{\mathsf T}.
$$

The label-weighted coefficient sum is zero, and

$$
\sum_i\alpha_i y_ix_i=1.
$$

The dual objective is

$$
D=1-\frac12=\frac12.
$$

Primal feasibility, dual feasibility, and matching objectives certify optimality. No graph or numerical optimizer is needed.

The inner points have positive coefficients and support the solution. The outer points have strict margin slack and zero coefficients.

## Writing the quadratic program and recognizing infeasibility

Stack the parameters as

$$
z=
\begin{pmatrix}w\\b\end{pmatrix}.
$$

For the standard quadratic-program convention,

$$
\min_z\frac12z^{\mathsf T}Pz+q^{\mathsf T}z
\qquad
\text{subject to}\qquad
Gz\le h,
$$

the linear SVM uses

$$
P=
\begin{pmatrix}
I_d&0\\
0&0
\end{pmatrix},
\qquad
q=0,
$$

and row constraints

$$
G_i=-y_i
\begin{pmatrix}
x_i^{\mathsf T}&1
\end{pmatrix},
\qquad
h_i=-1.
$$

The final zero on the objective diagonal means the intercept is unpenalized. Adding a positive entry there to satisfy a preferred solver interface changes the optimization problem.

For the four-point example,

$$
G=
\begin{pmatrix}
-2&1\\
-1&1\\
-1&-1\\
-2&-1
\end{pmatrix},
\qquad
h=
\begin{pmatrix}-1\\-1\\-1\\-1\end{pmatrix}.
$$

Substituting the proposed solution verifies every row directly.

An infeasible example is equally explicit. Put two observations at input zero and give them opposite labels. Their constraints become

$$
b\ge 1,
\qquad
b\le -1.
$$

No parameters satisfy both.

This proves failure of the specified hard-margin model on those observations. It does not establish that every possible representation or learning method must fail. For example, some non-separable patterns become separable after a feature transformation. Opposite labels at exactly the same available features present a different obstruction.

A solver's status also needs numerical interpretation. Ill-conditioning or loose tolerances are not mathematical proofs of infeasibility. An explicit contradiction such as the one above is a proof.

## Soft margins and the exact origin of hinge loss

Introduce non-negative slack variables:

$$
\begin{aligned}
\min_{w,b,\xi}\quad
&
\frac12\lVert w\rVert^2+C\sum_i\xi_i\\
\text{subject to}\quad
&
y_i(w^{\mathsf T}x_i+b)\ge 1-\xi_i,\\
&
\xi_i\ge 0,
\end{aligned}
$$

with

$$
C>0.
$$

For fixed weight and intercept, each slack must satisfy

$$
\xi_i\ge 1-y_if(x_i),
\qquad
\xi_i\ge 0.
$$

Since increasing slack increases the objective, its optimal value is

$$
\xi_i=\max(0,1-y_if(x_i)).
$$

Substitution yields the equivalent unconstrained problem

$$
\min_{w,b}
\frac12\lVert w\rVert^2
+
C\sum_i\max(0,1-y_if(x_i)).
$$

The second term is hinge loss.

Its cases are more informative than calling every positive slack a mistake:

| Slack at its optimal value | Signed score | Interpretation |
|---|---|---|
| $$\xi_i=0$$ | $$y_if(x_i)\ge 1$$ | On or beyond the required margin |
| $$0<\xi_i<1$$ | $$0<y_if(x_i)<1$$ | Correct side, inside the margin |
| $$\xi_i=1$$ | $$y_if(x_i)=0$$ | On the decision boundary |
| $$\xi_i>1$$ | $$y_if(x_i)<0$$ | Incorrect side |

The penalty prices functional margin violation, not a fixed charge per misclassification. A deeply incorrect prediction costs more than a barely incorrect one.

Hinge loss upper-bounds a zero-one error convention that counts non-positive signed scores as errors:

$$
\mathbf1\{yf(x)\le 0\}
\le
\max(0,1-yf(x)).
$$

This follows by checking the two sign cases. Its usefulness as a surrogate does not make it the unique or universally “closest” convex approximation to classification error.

## Deriving the soft-margin dual step by step

Write the constraints in non-positive form and attach non-negative multipliers:

$$
L
=
\frac12\lVert w\rVert^2
+
C\sum_i\xi_i
+
\sum_i\alpha_i(1-\xi_i-y_i(w^{\mathsf T}x_i+b))
-
\sum_i\beta_i\xi_i.
$$

Group terms:

$$
\begin{aligned}
L
&=
\frac12\lVert w\rVert^2
-
w^{\mathsf T}\sum_i\alpha_i y_ix_i
+
\sum_i\alpha_i\\
&\qquad
-b\sum_i\alpha_i y_i
+
\sum_i(C-\alpha_i-\beta_i)\xi_i.
\end{aligned}
$$

The slack non-negativity constraints are already represented in the Lagrangian, so its inner infimum treats the slack coordinates as unrestricted. A non-zero coefficient of an unrestricted linear variable makes that infimum negative infinity.

Therefore finite dual values require

$$
\sum_i\alpha_i y_i=0
$$

and

$$
C-\alpha_i-\beta_i=0.
$$

Since both multiplier families are non-negative,

$$
0\le\alpha_i\le C.
$$

Define

$$
v=\sum_i\alpha_i y_ix_i.
$$

The remaining weight terms are

$$
\frac12\lVert w\rVert^2-w^{\mathsf T}v
=
\frac12\lVert w-v\rVert^2-\frac12\lVert v\rVert^2.
$$

Their infimum occurs at

$$
w=v.
$$

The dual is consequently

$$
\begin{aligned}
\max_\alpha\quad
&
\sum_i\alpha_i
-
\frac12\sum_{i,j}
\alpha_i\alpha_jy_iy_jx_i^{\mathsf T}x_j\\
\text{subject to}\quad
&
0\le\alpha_i\le C,\\
&
\sum_i\alpha_i y_i=0.
\end{aligned}
$$

The penalty becomes an upper bound on each dual coefficient because it appears in the slack stationarity equation.

For positive penalty, the primal has a strictly feasible point: choose zero weight and intercept and set every slack to two. Convexity and this strict feasibility support strong duality. A feasible primal and dual pair with matching values is therefore an exact certificate.

Removing slack variables gives the hard-margin dual, where the coefficient ceiling disappears.

## A two-point soft-margin problem solved for every penalty

Use the observations

$$
(-1,-1),\qquad(1,+1).
$$

The dual equality requires equal coefficients:

$$
\alpha_1=\alpha_2=a.
$$

The reconstructed weight is

$$
w=2a.
$$

The dual objective reduces to

$$
D(a)=2a-2a^2,
\qquad
0\le a\le C.
$$

Its derivative is

$$
D'(a)=2-4a,
$$

so

$$
a^\star=\min\left(C,\frac12\right).
$$

If the penalty is at least one half, the weight is one and the intercept is zero. Both points have unit signed margin.

If the penalty is smaller than one half,

$$
w=2C.
$$

Choosing zero intercept gives both slacks equal to

$$
1-2C.
$$

The primal objective is

$$
\frac12(2C)^2+2C(1-2C)
=
2C-2C^2,
$$

which matches the dual objective.

For the explicit penalty

$$
C=\frac14,
$$

the solution includes

$$
\alpha_1=\alpha_2=\frac14,
\qquad
w=\frac12,
\qquad
b=0,
\qquad
\xi_1=\xi_2=\frac12.
$$

The objective is

$$
P=\frac18+\frac14=\frac38,
$$

and

$$
D=\frac12-\frac18=\frac38.
$$

Both observations are correctly classified, yet both incur hinge loss.

There is also an interval of optimal intercepts:

$$
2C-1\le b\le 1-2C.
$$

Within this interval, both signed margins are at most one and the total hinge loss is

$$
(1-w+b)+(1-w-b)=2-2w.
$$

It does not depend on the intercept.

At the stated penalty, the interval is

$$
-\frac12\le b\le\frac12.
$$

This example shows that the weight can be unique while the unpenalized intercept is not.

## KKT identifies support vectors and bounds the intercept

Complementary slackness gives

$$
\alpha_i(1-\xi_i-y_if(x_i))=0
$$

and

$$
(C-\alpha_i)\xi_i=0.
$$

Therefore:

| Coefficient | Consequence |
|---|---|
| $$\alpha_i=0$$ | Zero slack and signed margin at least one |
| $$0<\alpha_i<C$$ | Zero slack and signed margin exactly one |
| $$\alpha_i=C$$ | Signed margin at most one |

A point on the margin can have a zero coefficient. A coefficient at its ceiling can correspond to a point on the margin, inside it, or incorrectly classified. The implications should not be reversed.

For an interior coefficient,

$$
y_i(w^{\mathsf T}x_i+b)=1,
$$

so

$$
b=y_i-w^{\mathsf T}x_i.
$$

When several such observations exist, their equations agree at an exact solution. Disagreement measures numerical inconsistency.

When none exists, use inequalities. Define the score without intercept:

$$
t_i=w^{\mathsf T}x_i.
$$

The admissible interval has lower endpoint

$$
\max\left(
\{1-t_i:y_i=1,\alpha_i=0\}
\cup
\{-1-t_i:y_i=-1,\alpha_i=C\}
\right),
$$

and upper endpoint

$$
\min\left(
\{-1-t_i:y_i=-1,\alpha_i=0\}
\cup
\{1-t_i:y_i=1,\alpha_i=C\}
\right).
$$

An empty collection contributes no bound in its direction. In an exact optimal solution, the combined interval is non-empty.

For the two-point example at penalty one quarter, the negative observation at the ceiling gives the lower bound negative one half. The positive observation at the ceiling gives the upper bound positive one half. These are exactly the intercept limits found directly from hinge loss.

Selecting the coefficient “closest to the interior” is not required by the theory.

## Kernelization and the actual number of variables

The dual and prediction rule use inputs through inner products:

$$
f(x)=\sum_i\alpha_i y_i x_i^{\mathsf T}x+b.
$$

Replace these products with a positive semidefinite kernel:

$$
K(x_i,x_j)=\langle\phi(x_i),\phi(x_j)\rangle.
$$

Then

$$
f(x)=\sum_i\alpha_i y_iK(x_i,x)+b.
$$

The dual still has one coefficient per observation. Its quadratic matrix is

$$
Q_{ij}=y_iy_jK(x_i,x_j).
$$

For any vector,

$$
c^{\mathsf T}Qc
=
(Yc)^{\mathsf T}K(Yc)\ge 0,
$$

where the diagonal label matrix multiplies each coordinate by its label. Thus the maximized dual objective remains concave.

The explicit hard-margin primal has the feature coefficients and an intercept. The slack formulation adds one slack per observation; eliminating slacks gives a non-smooth objective in the weight and intercept. Counting only coefficients without noting which formulation is being used can be misleading.

An infinite-dimensional feature space still admits a primal formulation. The [finite-span argument](/study/the-kernel-trick/) shows why a norm-regularized optimum can be represented using training features. The dual is a convenient route to this representation, not proof that the primal cannot exist.

Nor is sparsity guaranteed. Some problems give non-zero coefficients to many or all observations. For a linear kernel, prediction can use the reconstructed weight directly, avoiding a sum over stored support inputs.

## Hinge scores are not class probabilities

Fix an input with positive-class probability

$$
p=P(Y=1\mid X=x).
$$

For a scalar score, the conditional hinge risk is

$$
R(z)
=
p\max(0,1-z)+(1-p)\max(0,1+z).
$$

Inside the interval between negative one and positive one,

$$
R(z)=1+(1-2p)z.
$$

If the positive class is more probable, this decreases toward the right endpoint. If the negative class is more probable, it decreases toward the left endpoint.

For an interior probability unequal to one half, the conditional minimizer is therefore

$$
z^\star=
\begin{cases}
1,&p>1/2,\\
-1,&p<1/2.
\end{cases}
$$

At equal probabilities, every score in the interval minimizes risk.

Different probabilities on the same side of one half can therefore have the same optimal hinge score. The score's sign can be appropriate for classification without encoding the underlying probability.

For comparison, logistic conditional risk is

$$
R_{\log}(z)=\log(1+e^z)-pz.
$$

Its derivative is

$$
R_{\log}'(z)=\frac1{1+e^{-z}}-p.
$$

The optimum satisfies

$$
z^\star=\log\frac p{1-p}.
$$

This is why logistic scores have a population probability interpretation after the inverse-logit transformation, while hinge scores do not acquire that interpretation automatically.

## Penalty conventions and what a solver gap certifies

The summed-loss SVM objective is

$$
\frac12\lVert w\rVert^2+C\sum_i\ell_i.
$$

Divide by the positive constant given by penalty times sample count:

$$
\frac1{2Cn}\lVert w\rVert^2+\frac1n\sum_i\ell_i.
$$

Thus it corresponds to mean loss with regularization coefficient

$$
\lambda=\frac1{Cn}.
$$

Keeping the same summed-loss penalty while changing the sample count changes the regularization strength relative to average loss.

Observation-specific penalties likewise produce observation-specific dual ceilings:

$$
C_i-\alpha_i-\beta_i=0
\quad\Longrightarrow\quad
0\le\alpha_i\le C_i.
$$

For any feasible dual coefficient vector and any primal weight and intercept, setting slacks to their hinge values provides a feasible primal point. Compute

$$
P=\frac12\lVert w\rVert^2+C\sum_i\max(0,1-y_if(x_i)),
$$

and

$$
D=\sum_i\alpha_i-\frac12\alpha^{\mathsf T}Q\alpha.
$$

Then

$$
D\le p^\star\le P.
$$

The difference bounds optimization error for this training objective. It does not bound classification error on new data.

Deleting an observation with a zero coefficient preserves an existing optimum when the summed-loss penalty is fixed and the same certificate applies. It can change the set of optimal intercepts, and rescaling the objective after deletion can change the problem. “The point has no coefficient” is a precise optimization statement, not a general causal claim about the observation's importance.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| Derive distance to a hyperplane | Construct the minimum-length perturbation |
| Distinguish functional and geometric margins | Check positive rescaling |
| Derive hard-margin normalization | Fix the smallest functional margin at one |
| Certify the four-point example | Match its primal and dual objectives |
| Encode the quadratic program | Leave the intercept unpenalized |
| Prove a simple infeasibility claim | Exhibit contradictory constraints |
| Eliminate slack variables | Obtain hinge loss exactly |
| Derive the dual | Identify which linear coefficients must vanish |
| Solve the two-point soft-margin problem | Recover the penalty-dependent coefficient |
| Interpret KKT endpoint cases | Avoid reversing implications |
| Recover the intercept without interior coefficients | Intersect the bounds |
| Explain why scores are not probabilities | Minimize conditional hinge risk |
| Translate penalty conventions | Relate summed loss to mean-loss regularization |
| Interpret a small duality gap | Separate optimization from generalization |

## Why it matters for my work

The SVM makes the representation, margin geometry, and training tradeoff explicit. I can use that transparency to audit a baseline, while keeping optimization certificates separate from claims about calibration or robustness across data sources.

## What I have not resolved

I need to determine whether the feature geometry used by my baselines preserves clinically relevant similarity across acquisition conditions. A large training margin cannot answer that question.
