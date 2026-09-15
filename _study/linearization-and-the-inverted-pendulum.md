---
layout: study_note
title: "Linearization: An Approximation Whose Licence Is Retrospective"
description: "Replacing sin θ with θ makes an unsolvable equation solvable, the justification arrives only after checking, and a single sign decides whether the system oscillates forever or runs away."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "feedback-control"
category_title: "Feedback Control & Classical Design"
order: 6
source: "Independent study"
written: true
updated: "2026-09-15"
---

A pendulum obeys

$$
\ddot\theta + \frac{g}{\ell}\sin\theta = \frac{\tau}{m\ell^2},
$$

and that equation has no closed-form solution. The $$\sin$$ is the whole problem: every tool that makes linear systems tractable — superposition, the Laplace transform, poles and zeros, the entire [transfer-function apparatus](/study/poles-zeros-and-the-z-transform/) — assumes linearity, and this equation does not have it.

So you write $$\sin\theta \approx \theta$$ and carry on.

## Core question and definition

What licenses that? The usual answer is "small angles," which is true and does not say how small.

The honest answer is that **the justification is retrospective**. You make the substitution, solve the linear system, and then check the result against the real one. If they agree over the range you care about, the approximation was fine. If they do not, it was not. There is no clean a priori criterion, and pretending otherwise is worse than admitting it.

Checking is cheap, and the numbers are instructive. Integrating the true pendulum against $$\theta_0\cos(\sqrt{g/\ell}\,t)$$ over ten seconds:

| initial angle | max disagreement |
|---|---|
| 2.9° | 0.01° |
| 5.7° | 0.11° |
| 11.5° | 0.86° |
| 22.9° | **6.86°** |
| 45.8° | **52.6°** |

The failure is not gradual. Through about 10° the approximation is essentially exact. By 23° the error is a third of the amplitude. By 46° the disagreement **exceeds the amplitude itself** — the linear model is not approximately right, it is describing a different motion, having accumulated phase error until the two swing in opposition.

So the small-angle approximation is excellent, then abruptly useless, and the transition sits inside a range of angles that all sound small when described in words.

## Key concepts

### A sign decides stability

Two systems, same derivation, opposite geometry: a load hanging from a crane, and a pole balanced upright on a cart. Both linearize to $$\ddot\theta = \mp(g/\ell)\theta$$, and the sign is the only difference.

$$
\text{hanging: poles at } \pm 3.13j
\qquad\qquad
\text{inverted: poles at } \pm 3.13 .
$$

The hanging pendulum's poles are purely imaginary — the load swings forever at fixed amplitude, annoying but bounded. The inverted pendulum has a pole on the **positive real axis**, and a positive real pole means $$e^{+3.13t}$$: any disturbance grows exponentially, and the pole falls over.

Both are "a pendulum." Both linearize the same way. One is stable and one cannot be left alone for a second, and *nothing in the physical description announces which* — the answer appears when the algebra is done and the poles are located. That is the argument for doing the modelling rather than reasoning about the system in words.

### Why anyone bothers, and why anyone stops

The cart-pole is the canonical control problem, and deriving its equations of motion is genuinely laborious: force balances in two directions, a torque balance, a projection onto a rotating coordinate frame, then eliminating the internal reaction forces to get one input–output relation. Several pages, several opportunities for a sign error.

It is also the canonical reinforcement-learning benchmark, where an agent learns to balance it from nothing but left/right actions and a reward — no equations at all. Having ground through the derivation, the appeal of skipping it is not subtle.

The trade is the honest part. Deriving the model gives you the poles, and therefore *why* the system is unstable and how unstable, before building anything. A learned controller gives you a policy that works on the system it was trained on, with no such account. Neither dominates; they answer different questions, and for a system too complex or too poorly characterised to model, only one of them is available at all.

## Why it matters for my work

The linearization table is the thing I want to keep, because it is a rare case where the cost of a modelling assumption can be **measured exactly**.

Nearly every applied model rests on approximations of this kind: that an effect is additive, that a relationship is monotone, that a nuisance variable can be adjusted for linearly, that a risk score can be thresholded. Each is defensible in some regime. Almost none comes with the range stated, and the pattern above is the one to expect — accurate, accurate, accurate, then wrong by more than the signal, with the transition somewhere nobody looked.

What makes the pendulum tractable is that the exact answer is available to compare against. In medicine it usually is not, which is exactly why the discipline matters more there and gets applied less: you cannot integrate the true system, so the only substitute is checking whether the approximation's *consequences* hold where you can observe them, and declining to extrapolate past that. "Valid for small angles" with no number attached is the same sentence as "works in the relevant population" with no definition attached, and both are doing the same work of sounding like a constraint while imposing none.

The sign result is the second half. Two systems can be structurally identical and behave oppositely because of one term, and the difference is invisible until the analysis is finished. A model that is [stable in deployment and one that runs away](/study/feedback-control-and-deployment-loops/) can differ by that little — which is an argument for computing the thing rather than reasoning about it from its description, and for being suspicious of any intuition about a system whose equations have not been written down.

---

Sources: the small-angle approximation, the pendulum equation, and the pole locations of hanging versus inverted configurations are standard results in classical mechanics and control theory. The numerical table and the pole values here were computed directly by integrating the nonlinear equation and comparing against the linear solution.
