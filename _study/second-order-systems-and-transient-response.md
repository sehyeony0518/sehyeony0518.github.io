---
layout: study_note
title: "Second-Order Systems: Four Numbers You Can Ask For, and Where They Put the Poles"
description: "Rise time, overshoot, peak time and settling time are not four independent wishes — each one carves a region out of the complex plane, and the design is whatever survives the intersection."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "feedback-control"
category_title: "Feedback Control & Classical Design"
order: 2
source: "Lecture notes, Ajou University"
written: true
updated: "2026-09-15"
---

A specification arrives in the language of time: *rise in under 0.6 seconds, overshoot no more than 10%, settle within 3 seconds.* A design happens in the language of the complex plane: *put the poles here.* The entire content of second-order analysis is the dictionary between those two languages, and the surprise is how tight the dictionary is — each time-domain demand turns into a clean geometric region, and the three regions either overlap or the specification was impossible.

## Core question and definition

Almost every closed loop worth analysing is written in the **standard second-order form**

$$
H(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2},
$$

whose poles are

$$
s = -\zeta\omega_n \pm j\,\omega_n\sqrt{1-\zeta^2} \;=\; -\sigma \pm j\omega_d .
$$

Three symbols, and each has a geometric meaning that is worth committing to memory as a *picture*, not a formula:

- $$\omega_n$$, the **natural frequency**, is the distance from the origin to the pole. It sets the overall speed.
- $$\sigma = \zeta\omega_n$$ is the **distance left of the imaginary axis**. It sets how fast things decay.
- $$\omega_d = \omega_n\sqrt{1-\zeta^2}$$ is the **height above the real axis**. It is the frequency you actually see ringing.
- $$\zeta$$, the **damping ratio**, is the *angle*. Specifically $$\zeta = \cos\theta$$ where $$\theta$$ is measured from the negative real axis.

That last identity is the one that makes the whole picture work, and it is easy to verify: at $$\zeta = 0.707$$ I computed the pole angle as $$45.01^\circ$$, and $$\cos(45^\circ) = 0.707$$. **The damping ratio is the pole angle.** A line through the origin at fixed angle is a line of constant damping.

## Key concepts

### The four specifications, and which ones are exact

Deriving the step response by partial fractions and then differentiating gives closed forms for the transient specifications. What matters practically is knowing **which are exact and which are fits**, because that determines how much slack to leave.

| Spec | Formula | Status |
|---|---|---|
| Peak time | $$t_p = \dfrac{\pi}{\omega_d}$$ | **Exact** |
| Overshoot | $$M_p = \exp\!\left(\dfrac{-\zeta\pi}{\sqrt{1-\zeta^2}}\right)$$ | **Exact** |
| Settling time (1%) | $$t_s \approx \dfrac{4.6}{\sigma}$$ | Envelope approximation |
| Rise time | $$t_r \approx \dfrac{1.8}{\omega_n}$$ | Empirical fit |

I checked each against direct simulation of the step response:

```
 zeta   Mp formula  Mp measured   tp formula   tp measured   tr 1.8/wn   tr measured
0.500      0.16303      0.16303       3.6276        3.6276      1.8000        1.6376
0.707      0.04325      0.04325       4.4422        4.4422      1.8000        2.1477
```

$$M_p$$ and $$t_p$$ agree to five decimal places — they are exact consequences of the form. The rise-time rule is off by roughly $$\pm 20\%$$ across this range of $$\zeta$$, in opposite directions at either end. That is the one to leave margin on. Settling time held up well: at $$\zeta = 0.70$$, $$\sigma = 0.700$$, the formula gives $$6.571$$ and simulation gives $$6.575$$.

A detail worth noticing: $$\zeta = 0.707$$ gives $$M_p = \exp(-\pi) = 0.04321$$ exactly, because $$\zeta/\sqrt{1-\zeta^2} = 1$$ there. The famous "$$\zeta = 0.707$$ is a good default" is partly this — it is the point where the algebra collapses to a clean number and the overshoot is a tidy 4.3%.

### Each spec is a region, not a point

This is the reframing that turns analysis into design.

- $$t_r \le T$$ requires $$\omega_n \ge 1.8/T$$ — the pole must lie **outside a circle** of that radius.
- $$M_p \le m$$ requires $$\zeta \ge \zeta_{\min}$$ — the pole must lie **inside a wedge**, since $$\zeta$$ is the angle.
- $$t_s \le T$$ requires $$\sigma \ge 4.6/T$$ — the pole must lie **left of a vertical line**.

Take the specification I opened with: $$t_r \le 0.6$$, $$M_p \le 10\%$$, $$t_s \le 3$$. Then

$$
\omega_n \ge \frac{1.8}{0.6} = 3, \qquad \zeta \ge 0.5912, \qquad \sigma \ge \frac{4.6}{3} = 1.5333 .
$$

The allowed region is the intersection: outside a circle of radius 3, inside a wedge of half-angle $$\arccos(0.5912) = 53.7^\circ$$, and left of $$\sigma = 1.533$$. A candidate at $$\zeta = 0.6$$, $$\omega_n = 3$$ lands at $$M_p = 0.0948$$, $$t_r \approx 0.600$$, $$t_s \approx 2.556$$, $$\sigma = 1.8$$ — inside on every count.

Textbooks often round $$\zeta \ge 0.6$$ for 10% overshoot. The exact value is $$0.5912$$, so the rounding is conservative and harmless, but it is worth knowing which direction the approximation errs.

**Three demands, three shapes, and the design is the overlap.** If the shapes do not intersect, no second-order system meets the spec — and that is a *result*, not a failure of effort. Knowing a specification is infeasible before building anything is the most valuable thing this machinery produces.

### Block-diagram algebra is bookkeeping, and it is exact

Before any of this can be applied, the loop has to be reduced to a single transfer function. Four rules do it:

| Configuration | Equivalent |
|---|---|
| Series | $$G_1 G_2$$ |
| Parallel | $$G_1 + G_2$$ |
| Negative feedback | $$\dfrac{G_1}{1 + G_1 G_2}$$ |
| Positive feedback | $$\dfrac{G_1}{1 - G_1 G_2}$$ |

I verified all four by evaluating them at three complex values of $$s$$ against brute-force solution of the loop equations — exact agreement in every case. The single sign difference between the last two is the entire difference between a system that converges and one that runs away, and it is the easiest thing on the page to get wrong.

### Why a "dominant pole" argument is allowed

Real systems are rarely second order. The justification for treating them as if they were is the **time constant**: a pole at $$-\sigma$$ contributes $$e^{-\sigma t}$$, with time constant $$\tau = 1/\sigma$$. A pole ten times further left decays ten times faster, and after the slow mode has done anything interesting, the fast mode is already gone.

So the poles nearest the imaginary axis — the **dominant poles** — govern what the response looks like, and a higher-order system gets analysed as the second-order system formed by its dominant pair. This is an approximation with a real failure mode: a nearby **zero** can distort the response substantially even when the dominant-pole story looks clean, which is why a design that checks out on paper still has to be simulated with the zeros left in.

## Why it matters for my work

The habit worth stealing is **turning a specification into a feasible region before optimising inside it**. When a clinical requirement arrives — sensitivity above some floor, false-positive rate below some ceiling, latency under some bound — the reflex is to train and then check. The better move is to ask first what the constraints jointly permit, because constraints in that setting also carve out regions, and they can fail to intersect. A sensitivity floor and a false-positive ceiling that no achievable operating point satisfies is the same situation as poles with no legal home, and it should be discovered by argument rather than by a month of training runs.

The second transferable point is the **exact-versus-fitted distinction**. $$M_p$$ is exact; $$t_r$$ is a fit good to about 20%. Any engineering estimate is one of those two things, and confusing them is how margin disappears. The analogue is a validation metric: a point estimate on a held-out set is a fit with a confidence interval, not an exact property, and designing as if it were exact is how a model that "meets spec" fails in deployment.

The third is **dominance**. Most of a complicated system's behaviour is governed by its slowest mode, and identifying that mode is usually more useful than modelling everything.

## What I have not resolved

The dominant-pole approximation has no clean error bound that I know of. "Ten times further left is negligible" is folklore, and I would like to know what the actual bound looks like as a function of the ratio and of where the zeros sit — particularly since the zero effect is the one that bit the worked example.

I also do not have a good feel for how these specifications interact when the plant has a right-half-plane zero. The standard form assumes none, and RHP zeros produce initial undershoot that the four formulas say nothing about.

---

Sources: the standard second-order form, the transient-response formulas, and block-diagram reduction rules are standard results in classical control theory. The numerical claims here — the identity $$\zeta = \cos\theta$$ checked against computed pole angles, the exactness of $$M_p$$ and $$t_p$$ versus the approximate nature of $$t_r$$ and $$t_s$$ checked against simulated step responses, the design-region arithmetic for the worked specification, and the four block-diagram identities verified at complex test points — were computed directly.
