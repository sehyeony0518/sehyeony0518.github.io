---
layout: study_note
title: "KKT Conditions and Shadow Prices: What a Lagrange Multiplier Is Actually Telling You"
description: "Complementary slackness, the multiplier as the sensitivity of the optimum to its constraint, and reading the SVM's alphas as a statement about which samples matter."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "algebra-and-optimisation"
category_title: "Linear Algebra & Optimisation"
order: 8
source: "Independent study"
written: true
updated: "2026-09-15"
---

A Lagrange multiplier is usually introduced as a bookkeeping device — a number you invent to absorb a constraint and then discard once the answer appears. It is not. At the optimum, each multiplier is a measurement, and it answers a question the objective value alone cannot: *how much is this constraint costing me?*

## Core question and definition

Take a convex problem with inequality constraints $$g_i(x) \le 0$$ and Lagrangian $$L = f_0(x) + \sum_i \lambda_i g_i(x)$$. At an optimum, four conditions hold together — the **KKT conditions**:[^kt][^boyd]

$$
\nabla_x L = 0, \qquad g_i(x^\star) \le 0, \qquad \lambda_i^\star \ge 0, \qquad \lambda_i^\star\, g_i(x^\star) = 0 .
$$

Stationarity, primal feasibility, dual feasibility, and — the one that carries the content — **complementary slackness**. The product $$\lambda_i g_i$$ is zero, so for every constraint at least one of two things is true: the multiplier is zero, or the constraint is **active** (tight, satisfied with equality).

The contrapositive is the useful reading. A non-zero multiplier means the constraint is pressing against the solution. A zero multiplier means the solution sits strictly inside that constraint and could not care less about it.

## Key concepts

### The multiplier is a derivative of the optimal value

Something stronger than "cares / does not care" is true. Perturb the constraint to $$g_i(x) \le u_i$$ and let $$p^\star(u)$$ be the resulting optimal value. Then

$$
\lambda_i^\star = -\frac{\partial p^\star}{\partial u_i}\bigg|_{u=0}.
$$

The multiplier is the **shadow price** of the constraint: the rate at which the objective improves per unit of relaxation.

This is checkable, and checking it is what makes it stick. Take a small quadratic program with a constraint $$x+y \ge 1$$ whose multiplier solves to $$0.2$$. Tighten the constraint to $$x+y \ge 1.1$$ and re-solve: the minimum rises by about $$0.021$$. The prediction was $$0.2 \times 0.1 = 0.020$$. The gap is not an error — $$\lambda$$ is a *derivative*, so the linear prediction is exact only in the limit, and the extra $$0.001$$ is the curvature term. Relax instead, to $$x+y\ge 0.9$$, and the objective falls by roughly the same $$0.02$$.

Now the other constraint in that problem, the one whose solution sits well inside the feasible region with room to spare. Its multiplier is $$0$$. Move its boundary by $$0.1$$ in either direction and the optimum does not move at all. The multiplier said so in advance.

### Which constraint is the bottleneck

That gives the multipliers a use beyond the derivation. Solve a constrained problem, look at the multipliers, and you have ranked the constraints by how much each is costing you. The largest is the bottleneck. If you are going to negotiate one requirement — more budget, a looser latency target, a relaxed tolerance — that is the one to negotiate, and the multiplier quantifies what you would get back. Constraints with zero multipliers can be loosened for free and will buy you nothing.

Solvers report this. What comes back from a QP is not only $$x^\star$$ but the slack variables $$s$$ (how much room each constraint has) and the multipliers $$z$$. Multiply them elementwise and you get zeros — complementary slackness, confirmed numerically rather than assumed.

### Reading the SVM's multipliers

In a [soft-margin SVM](/study/support-vector-machines/), $$\alpha_i + \beta_i = C$$ with both non-negative, so $$\alpha_i \in [0, C]$$, and complementary slackness sorts every training sample into exactly three cases:

- $$\alpha_i = 0$$. Then $$\beta_i = C \neq 0$$, which forces $$\xi_i = 0$$, and the margin constraint is slack. The sample sits safely inside its own side. Since $$w = \sum_i \alpha_i y_i x_i$$, it contributes **nothing**: delete it and the boundary is unchanged.
- $$0 < \alpha_i < C$$. Both multipliers are non-zero, so both constraints are tight: $$\xi_i = 0$$ *and* $$y_i(w^{\mathsf T}x_i + b) = 1$$. The sample lies exactly on the margin. These are the informative ones — the equation can be solved for the bias, $$b = y_i - w^{\mathsf T}x_i$$.
- $$\alpha_i = C$$. Then $$\beta_i = 0$$ and $$\xi_i$$ is free to be positive. The sample is inside the margin or misclassified.

So $$\alpha$$ is not an intermediate quantity to be discarded — it is a per-sample statement about influence, and the three cases are visible in a plot. There is also a practical wrinkle worth recording: recovering $$b$$ needs at least one sample in the middle case, and on some datasets there is none. The workaround is a heuristic — take the $$\alpha_i$$ furthest from both $$0$$ and $$C$$ and accept the numerical imprecision — and it is worth being clear that this is expedience, not theory.

## Why it matters for my work

The habit worth importing is that the *sensitivity* of a result is separate information from the result, and is often the part that matters.

Reporting an AUROC is reporting $$p^\star$$. It says nothing about which constraint produced it — whether the number would move if the inclusion criteria were loosened, if one site were dropped, if the [label definition](/study/label-quality-and-interobserver-variability/) shifted by one category. Those are shadow-price questions, and a pipeline that only ever reports the optimum has discarded them. Ablations and leave-one-site-out analyses are the empirical stand-in: not better estimates, but estimates of how much each design decision is holding the number up.

The complementary-slackness structure has a second use as a warning. Zero multiplier means *this constraint is not binding at the current solution* — and that is a local statement. A criterion that costs nothing on the development cohort may become the binding one after [shift](/study/robustness-subgroup-performance-and-external-validation/), with no advance notice from the development analysis. A constraint that is currently free is not a constraint that can be removed.

The SVM's $$\alpha$$ is the concrete version of something I keep wanting from larger models: a per-sample account of which training data the decision actually rests on. For a linear SVM it falls out of the optimality conditions exactly. For a deep network the analogous quantity has to be approximated, and the approximation is the thing under dispute — which is a fair summary of why [influence-based auditing](/study/shortcut-learning-in-medical-imaging/) is hard rather than routine.

---

[^kt]: Kuhn, H. W., & Tucker, A. W. (1951). Nonlinear programming. *Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability*, 481–492. Reprinted in *Traces and Emergence of Nonlinear Programming* (2014). [10.1007/978-3-0348-0439-4_11](https://doi.org/10.1007/978-3-0348-0439-4_11)

[^boyd]: Boyd, S., & Vandenberghe, L. (2004). *Convex Optimization*, §5.5–5.6. Cambridge University Press. [10.1017/CBO9780511804441](https://doi.org/10.1017/CBO9780511804441)
