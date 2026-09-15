---
layout: study_note
title: "Support Vector Machines: Margin as an Inductive Bias, and What Infeasibility Tells You"
description: "Deriving the hard-margin problem from a stability argument, watching it become infeasible when the classes overlap, and reading the soft-margin fix as a priced assumption rather than a repair."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "learning-principles"
category_title: "Learning Principles"
order: 6
source: "Independent study"
written: true
updated: "2026-09-15"
---

An SVM is a linear classifier. Everything distinctive about it is in *how the parameters are chosen*, not in what the model can represent. It is worth holding onto that, because the derivation is long enough that the model at the end can seem more exotic than $$f(x) = w^{\mathsf T}x + b$$.

## Core question and definition

Given labelled samples with $$y_i \in \{-1,+1\}$$, we want $$y_i\,f(x_i) > 0$$ for every $$i$$. When the data are linearly separable there are infinitely many such $$w, b$$ — and by training error they are all equally good. Something other than training error has to break the tie.

The SVM's answer is the **margin**: prefer the boundary that sits as far as possible from the nearest samples on both sides. The justification is stability rather than accuracy. If the samples are perturbed slightly — noise, a different scanner, a different day — a boundary crowding the nearest point flips its label first. A boundary with room to spare tolerates the perturbation.

This is an **inductive bias**, chosen, not derived. Nothing in the data says that maximum margin generalises best; the argument is a prior about what kind of perturbation the deployment will bring.

## Key concepts

### From the stability argument to a quadratic program

The distance from $$x_i$$ to the hyperplane is $$\lvert w^{\mathsf T}x_i + b\rvert / \lVert w\rVert$$, and because $$y_i$$ carries the sign, this is $$y_i(w^{\mathsf T}x_i+b)/\lVert w\rVert$$ for a correctly classified point — the absolute value disappears and both classes are handled by one expression. The margin is twice the distance to the nearest sample, so the goal is

$$
\max_{w,b}\ \min_i\ \frac{y_i\,(w^{\mathsf T}x_i+b)}{\lVert w\rVert}.
$$

Introducing $$\varepsilon$$ for that minimum turns it into: maximise $$\varepsilon/\lVert w\rVert$$ subject to $$y_i(w^{\mathsf T}x_i+b) \ge \varepsilon$$ for all $$i$$. Now notice that $$(w,b)$$ and $$(cw,cb)$$ describe the same hyperplane — the problem is scale-invariant. So we may spend that freedom fixing $$\varepsilon = 1$$, and maximising $$1/\lVert w\rVert$$ becomes minimising $$\lVert w\rVert^2$$:

$$
\min_{w,b}\ \tfrac{1}{2}\lVert w\rVert^2
\quad\text{subject to}\quad
y_i\,(w^{\mathsf T}x_i + b) \ge 1 \ \ \forall i .
$$

A convex quadratic objective under linear constraints: a **quadratic program**, with margin $$2/\lVert w\rVert$$. The $$\tfrac12$$ is there only to tidy the derivative.

### Two ways to write the decision boundary

The primal keeps $$w$$ and $$b$$. The [dual](/study/primal-and-dual-problems/) introduces one multiplier $$\alpha_i$$ per constraint, and it turns out that

$$
w = \sum_i \alpha_i y_i x_i,
\qquad
f(x) = \sum_i \alpha_i y_i \langle x_i, x\rangle + b .
$$

Only the samples sitting exactly on the margin have $$\alpha_i \neq 0$$. Those are the **support vectors**, and both readings of the name are in these two equations: the boundary is a weighted sum *of* the support vectors, and classifying a new point is a matter of taking inner products *with* them. Everything else in the training set could be deleted without changing the answer.

That the boundary depends on the data only through inner products is what makes the kernel substitution possible, which is the historical reason the dual form mattered.[^boser][^cv]

### Running it, and the error message that is a result

Handing this to a QP solver means writing it in the solver's convention — typically $$\min \tfrac12 z^{\mathsf T}Pz + q^{\mathsf T}z$$ subject to $$Gz \le h$$. Stacking the parameters as $$z = [w_1, w_2, b]$$ for a 2-D problem gives

$$
P = \begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix},\qquad q = 0,
$$

with the zero in the corner because the bias is not penalised, and the constraints negated into $$-y_i(w^{\mathsf T}x_i+b) \le -1$$. Two practical notes: that $$P$$ is positive *semi*definite, not definite, which some solvers dislike and which is a real consequence of leaving $$b$$ unregularised rather than a typing mistake; and the matrices must be built in the solver's own float type, which is the source of most first-attempt errors.

The instructive experiment is to raise the noise. With well-separated clouds the boundary lands where you would draw it by hand. Push the noise up until the classes interpenetrate and the solver does not return a worse boundary — it reports that **no feasible point exists**. The constraints say every sample must be correctly classified with margin at least 1, and once a positive sample sits among the negatives, that is simply false.

This is worth pausing on. The formulation failed loudly. It did not silently return a boundary with 85% accuracy and leave you to discover the overlap later; it said the assumption you encoded is not satisfiable by this data. Very little of machine learning is built to fail that way.

The solver also prints the primal and dual objective values at each iteration, and the gap between them. That gap is the [duality bound](/study/primal-and-dual-problems/) made concrete: you may not know the optimum, but you know it lies between those two numbers.

### Soft margin prices the assumption instead of repairing it

The fix is to make the constraint negotiable. Introduce a slack $$\xi_i \ge 0$$ per sample:

$$
\min_{w,b,\xi}\ \tfrac{1}{2}\lVert w\rVert^2 + C\sum_i \xi_i
\quad\text{s.t.}\quad
y_i(w^{\mathsf T}x_i+b) \ge 1 - \xi_i,\quad \xi_i \ge 0 .
$$

A point on the right side of the margin has $$\xi_i = 0$$ and costs nothing. A point inside the margin, or across the boundary entirely, has $$\xi_i$$ proportional to how far past the line it sits — the geometric violation distance, scaled by $$\lVert w\rVert$$. Penalising in proportion to that distance is the natural choice, though squaring it is a defensible alternative and gives a different classifier.

What the slack does *not* do is make the linear-separability assumption true. It converts a hard constraint into a cost, and hands the exchange rate to the practitioner as $$C$$. There is no value of $$C$$ the data alone can supply; it encodes how much margin you are willing to trade for one misclassification, and that is a judgement about the deployment.

## Why it matters for my work

Two things carry over, and they pull in opposite directions.

The first is that infeasibility is a form of honest reporting that most evaluation lacks. A hard-margin SVM on overlapping classes refuses to answer. A deep classifier on the same data returns a confident boundary and an accuracy figure, and nothing in the output announces that the classes overlap in the feature space it learned. Overlap is precisely the situation in which an [operating-point](/study/statistical-inference-for-diagnostic-studies/) is a clinical policy choice rather than a technical one, and the model's silence on it is a genuine loss of information. Designing evaluations that can come back "this question is not answerable from these features" is harder than it looks and worth more than another decimal place.

The second is the warning against reading the margin story as a reliability guarantee. Large margin means stable under *small perturbations in the learned feature space*. If that space encodes a [shortcut](/study/shortcut-learning-in-medical-imaging/) — a scanner artefact, an annotation marker — the SVM will place a wide, stable, maximally confident boundary through it. Margin measures separation, not whether the thing being separated is the thing you meant. The same is true of $$C$$: tuning it on a validation set drawn from the same source optimises the exchange rate for that source and says nothing about the next one.

---

[^boser]: Boser, B. E., Guyon, I. M., & Vapnik, V. N. (1992). A training algorithm for optimal margin classifiers. *COLT '92*, 144–152. [10.1145/130385.130401](https://doi.org/10.1145/130385.130401)

[^cv]: Cortes, C., & Vapnik, V. (1995). Support-vector networks. *Machine Learning*, 20, 273–297. [10.1007/BF00994018](https://doi.org/10.1007/BF00994018)
