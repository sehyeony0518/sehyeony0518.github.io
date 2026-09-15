---
layout: study_note
title: "Bayesian Decision Theory: Risk, Loss, and Where the Boundary Goes"
description: "Why the best decision is not always the most probable class, and what a cost matrix does to a threshold."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "probability-and-inference"
category_title: "Probability & Statistical Inference"
order: 4
source: "Independent study"
written: true
updated: "2026-09-15"
---

Given everything — the priors, the class-conditional densities, the cost of each mistake — there is a best decision rule, and it can be written down. Nothing in practice has all of that, but knowing the optimum tells you what the gap consists of.

## Core question and definition

A class $$\omega_j$$ is unobserved; a measurement $$\mathbf{x}$$ is observed; an action $$\alpha_i$$ must be taken. The **conditional risk** of taking $$\alpha_i$$ having seen $$\mathbf{x}$$ is the expected cost:

$$
R(\alpha_i \mid \mathbf{x}) = \sum_j \lambda(\alpha_i \mid \omega_j)\, P(\omega_j \mid \mathbf{x}),
$$

where $$\lambda$$ is the loss incurred by choosing $$\alpha_i$$ when the truth is $$\omega_j$$. The optimal rule takes whichever action minimises this, and the risk of that rule is the Bayes risk — the floor no decision procedure beats given this information.

The separation worth holding onto is between a **class** and an **action**. Deciding what is present and deciding what to do are different, and they come apart whenever mistakes cost differently.

## Key concepts

### Observing anything is never worse than not observing

Before any measurement, the best available rule is to pick the commoner class, and the error rate is $$\min_j P(\omega_j)$$. With a measurement, the rule becomes: choose the class with the larger posterior.

Writing out the error of the posterior rule and applying the law of total probability shows it is bounded by the prior-only error. Measurement cannot hurt — at worst the observation carries nothing about the class and the two rules coincide. The gain comes entirely from how much the likelihoods differ.

### The rule reduces to a likelihood ratio against a threshold

Substituting Bayes and cancelling the shared evidence term turns the comparison into

$$
\frac{p(\mathbf{x}\mid\omega_1)}{p(\mathbf{x}\mid\omega_2)}
\;\gtrless\;
\frac{(\lambda_{12}-\lambda_{22})\,P(\omega_2)}{(\lambda_{21}-\lambda_{11})\,P(\omega_1)}.
$$

Everything about priors and costs lives on the right-hand side, as a single number. The data enters only on the left. So changing the prevalence or the cost of a miss does not change what the measurement says — it moves the threshold the measurement is compared against. [Neyman and Pearson](https://doi.org/10.1098/rsta.1933.0009) (1933) established the optimality of ratio tests in the closely related hypothesis-testing setting.

### Zero-one loss is the special case everyone assumes

If every error costs one and every correct answer costs nothing, minimising risk reduces to maximising the posterior, and the threshold collapses to the prior ratio. This is the rule people have in mind when they say "pick the most likely class."

It is a special case, and an unusual one in medicine. Calling a healthy patient sick and sending a sick patient home do not cost the same, and once they do not, a posterior above one half is no longer sufficient reason to act. The lecture's example is exact: with an asymmetric penalty you may be unwilling to answer with the more probable class, because being wrong in that direction costs too much.

### Discriminant functions, and why boundaries take the shapes they do

Any monotonically increasing transformation of the decision quantity leaves the ordering — and therefore the decision — unchanged. That freedom is why taking logs is standard and why a discriminant can be implemented by anything at all, including a network, so long as it preserves the ordering.

For Gaussian class-conditionals the log makes the geometry visible. With equal covariances the quadratic terms cancel and the boundary is **linear** — which is the condition under which a linear classifier is exactly optimal rather than merely convenient, and under equal priors it reduces to nearest-mean. With unequal covariances the quadratic terms survive and the boundary becomes a conic: an ellipse, a hyperbola, sometimes two disjoint regions.

Two Gaussians can therefore produce a decision region that is not connected. Real class-conditionals are messier than Gaussians, so the honest expectation is that optimal boundaries are more complicated still.

## Where this touches my work

The threshold result is the one I keep returning to. A model's output is evidence; where the threshold sits is a separate decision encoding prevalence and cost. A model moved to a screening population needs a new threshold even if nothing about its learned evidence changed — and a model reported at a fixed operating point has had that decision made for it, usually by whoever chose the validation set.

The cost matrix is also the piece routinely missing. Accuracy, and AUROC over all thresholds, both implicitly assume symmetric costs. Neither is the quantity a clinician needs, and asking what $$\lambda$$ actually is turns out to be a conversation about the clinical pathway rather than about the model.

## What I have not resolved

Whether a defensible loss matrix can be elicited for the tasks I work on. The asymmetry between missing a malignancy and over-calling one is real and obvious in direction, but I have not seen it given a number that survives scrutiny, and an arbitrary number would just hide the judgement inside an equation.

## References

- Neyman & Pearson (1933). [On the problem of the most efficient tests of statistical hypotheses](https://doi.org/10.1098/rsta.1933.0009). *Phil. Trans. R. Soc. A*.
