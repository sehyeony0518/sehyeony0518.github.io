---
layout: study_note
title: "Primal and Dual Problems: The Max-Min Inequality and What the Gap Certifies"
description: "The one inequality the whole of Lagrangian duality rests on, why swapping to the dual changes the size of the problem, and why a duality gap is useful information rather than a failure."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "math-foundations"
category_title: "Mathematical & Statistical Foundations"
order: 19
source: "Independent study"
written: true
updated: "2026-09-15"
---

Duality is one of those topics where opening a textbook at page one is a bad plan — there is far too much of it, and almost none of the first hundred pages is what you need to read a paper. What you actually need is small. The underlying idea is not complicated; proving that it holds in generality was the hard part, and that work is done.

## Core question and definition

Everything rests on one inequality:

$$
\max_{y}\ \min_{x}\ f(x,y) \;\le\; \min_{x}\ \max_{y}\ f(x,y).
$$

The proof is three lines. For any particular $$x$$ and $$y$$,

$$
\min_{x'} f(x',y) \;\le\; f(x,y) \;\le\; \max_{y'} f(x,y').
$$

The left end depends only on $$y$$; the right end only on $$x$$. So maximising the left over $$y$$ and minimising the right over $$x$$ leaves the inequality intact, and that is the result. It is worth having the proof once, but the thing to carry away is the statement — **committing to your move first can only cost you**. Whoever chooses second gets to respond.

(Strictly this should be $$\sup$$ and $$\inf$$: $$\max_x 1/x$$ over $$x>0$$ does not exist while the supremum does. Engineering texts write $$\max$$ and mean $$\sup$$, and chasing the distinction here obscures the point rather than sharpening it.)

## Key concepts

### Turning a constraint into a maximisation

Take $$\min_{x} f_0(x)$$ subject to $$h(x) = 0$$. Define

$$
F(x) = \begin{cases} f_0(x) & h(x) = 0\\ +\infty & \text{otherwise,}\end{cases}
$$

so that $$\min_x F(x)$$ is the original problem with the constraint absorbed into the objective. The trick is that this $$F$$ has a variational form:

$$
F(x) = \max_{\lambda \in \mathbb{R}} \; \big[\, f_0(x) + \lambda\, h(x) \,\big].
$$

If $$h(x)=0$$ the bracket is $$f_0(x)$$ for every $$\lambda$$; if $$h(x)\neq 0$$, $$\lambda$$ can be driven to $$\pm\infty$$ and the maximum is $$+\infty$$. For an inequality constraint $$h(x)\le 0$$ the same construction works with $$\lambda \ge 0$$ — a violation still buys $$+\infty$$, and satisfaction pins the optimal multiplier at zero.

So the **primal** is $$\min_x \max_\lambda L(x,\lambda)$$ and the **dual** is $$\max_\lambda \min_x L(x,\lambda)$$, with $$L$$ the Lagrangian. They are the two sides of the max-min inequality applied to the same function. Nothing has been invented; the order of two operations has been swapped, and the inequality says which direction the swap costs.

### A worked case, both ways

Minimise $$x^2+y^2$$ subject to $$x+y=1$$ — the squared distance from the origin to a line, so the answer is known to be $$\tfrac12$$. With $$L = x^2+y^2+\lambda(1-x-y)$$, the inner minimisation is unconstrained, so setting derivatives to zero gives $$x = y = \lambda/2$$. Substituting back,

$$
g(\lambda) = \frac{\lambda^2}{2} + \lambda\left(1 - \lambda\right) = \lambda - \frac{\lambda^2}{2},
$$

which is maximised at $$\lambda = 1$$ with value $$\tfrac12$$. The two agree, as they must for a convex problem.

### Why swap at all: the count of unknowns changes

The usual first reaction is that the dual is not obviously easier. That reaction is right, and "easier" is the wrong word. What changes is the **number of variables**: the primal carries one per component of $$x$$, the dual one per constraint. When you are optimising over a thousand-dimensional $$x$$ subject to three constraints, that is a three-variable problem after the swap. Sometimes it is dramatic, sometimes it is a wash, and occasionally it goes the wrong way.

The other reasons are more common in practice than the size argument: some methods alternate between the two, and some objectives are only tractable when written in the $$\min_x\max_\lambda$$ form and attacked there directly. The support vector machine is where most people meet this for the first time, and the dual form is what makes the kernel substitution possible at all.[^svm]

### The duality gap is a measurement, not a defect

The difference between the primal and dual optima is the **duality gap**. For convex problems under mild conditions it is zero — strong duality — which is what makes the swap lossless.[^boyd]

When it is not zero, the situation is still better than not knowing. Suppose you have run the primal down to some feasible value and the dual up to some value. The true optimum is trapped between them. You do not know the answer, but you know how far from it you could possibly be. A gap of $$10^{-4}$$ is a certificate; an unbounded search with no dual bound gives you a number and no way to judge it.

### Convex conjugates: the same move, generalised

For harder objectives the multiplier construction is replaced by the **convex conjugate** (Fenchel transform),

$$
f^*(y) = \sup_x \; \big[\, y^{\mathsf T}x - f(x) \,\big],
$$

which represents $$f$$ as a maximisation and thereby exposes the same swap.[^rock] The practical fact is that you look conjugates up in a table rather than deriving them, the way you look up integrals.

Take $$\min \lVert x\rVert^2$$ subject to $$Ax=b$$ with $$A$$ wide. Writing $$f(x)=\lVert x\rVert^2$$ and $$g$$ for the indicator of $$\{b\}$$, the table gives $$f^*(u) = \tfrac14\lVert u\rVert^2$$ and $$g^*(y) = b^{\mathsf T}y$$, so the dual is

$$
\max_y \; \left[-\tfrac14\, y^{\mathsf T} A A^{\mathsf T} y \;-\; b^{\mathsf T} y\right],
$$

an unconstrained quadratic in $$y$$ alone. Setting the [matrix derivative](/study/matrix-calculus-for-reading-papers/) to zero gives $$y = -2(AA^{\mathsf T})^{-1}b$$ and hence

$$
x = -\tfrac12 A^{\mathsf T} y = A^{\mathsf T}(AA^{\mathsf T})^{-1} b,
$$

the right [pseudo-inverse](/study/linear-mmse-and-the-wiener-filter/) — the same answer the plain Lagrangian gives. The overdetermined case, $$\min\lVert Ax-b\rVert^2$$, has no constraint to dualise and goes straight to the normal equations, $$x = (A^{\mathsf T}A)^{-1}A^{\mathsf T}b$$.

Doing a solved problem twice looks wasteful. It is the point: the conjugate machinery reproduces the elementary answer here, which is the evidence that it can be trusted where no elementary answer exists.

## Why it matters for my work

The habit worth taking from duality is not the algebra. It is that a bound from the other side is worth more than a better estimate from the same side.

A [held-out score](/study/robustness-subgroup-performance-and-external-validation/) is a primal quantity: run the model, read a number. Nothing in it says how far that number could be from what deployment will produce. What supplies the other side is evidence of a different kind — a stress test that tries to make the model fail, an [attribution audit](/study/shortcut-learning-in-medical-imaging/) that looks for a shortcut rather than for accuracy, a prospective run. Those do not improve the estimate; they bracket it. A claim with only one side is a claim you cannot bound, however precisely it is reported.

The honest limitation: strong duality is a theorem, and the evaluation analogy has no theorem. Nothing guarantees that an adversarial test and a benchmark bracket the deployment performance between them, and a model can fail in a way neither probes. The transferable part is narrower — the value of measuring from the opposite direction, and the discipline of reporting the interval instead of the point.

---

[^boyd]: Boyd, S., & Vandenberghe, L. (2004). *Convex Optimization*. Cambridge University Press. [10.1017/CBO9780511804441](https://doi.org/10.1017/CBO9780511804441)

[^rock]: Rockafellar, R. T. (1970). *Convex Analysis*. Princeton University Press. [10.1515/9781400873173](https://doi.org/10.1515/9781400873173)

[^svm]: Cortes, C., & Vapnik, V. (1995). Support-vector networks. *Machine Learning*, 20, 273–297. [10.1007/BF00994018](https://doi.org/10.1007/BF00994018)
