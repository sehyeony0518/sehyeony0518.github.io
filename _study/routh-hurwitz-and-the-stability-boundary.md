---
layout: study_note
title: "Routh–Hurwitz: Deciding Stability Without Finding a Single Root"
description: "A table of divisions answers a question about polynomial roots that has no formula past degree four, and turns 'is this stable?' into 'for which gains is this stable?'"
tab: "ai-foundations"
tab_title: "Theory"
category: "feedback-control"
category_title: "Feedback Control & Classical Design"
order: 3
source: "Lecture notes, Ajou University"
written: true
updated: "2026-09-15"
---

Stability asks whether every root of the characteristic polynomial lies in the left half-plane. The obvious approach is to find the roots and look. This fails for two reasons: there is no general formula past degree four, and — more importantly — the useful question is not *"is this particular system stable?"* but *"for which values of my gain is it stable?"* Root-finding answers the first question one gain at a time. It cannot answer the second at all.

Routh–Hurwitz answers both, and it never finds a root.

## Core question and definition

Given $$a_n s^n + a_{n-1}s^{n-1} + \cdots + a_0$$, build a table. The first two rows are the alternating coefficients; every subsequent entry is a $$2\times2$$ determinant of the two rows above divided by the leading entry of the row directly above. The claim:

> **The number of roots in the right half-plane equals the number of sign changes in the first column.**

Zero sign changes means stable. That is the whole criterion.

I implemented the array over exact rational arithmetic and checked it against numerically computed roots:

```
 s^3+3s^2+2s+6         Routh: 0 RHP | actual 0 RHP, 2 on jw-axis   OK
 s^3+3s^2+2s+1         Routh: 0 RHP | actual 0 RHP, 0 on jw-axis   OK
 s^3+3s^2+2s+10        Routh: 2 RHP | actual 2 RHP                 OK
 s^4+2s^3+3s^2+4s+5    Routh: 2 RHP | actual 2 RHP                 OK
 s^5+2s^4+2s^3+4s^2+11s+10   Routh: 2 RHP | actual 2 RHP           OK
 s^5+7s^4+6s^3+42s^2+8s+56   Routh: 0 RHP | actual 0, 4 on jw-axis OK
```

The last two are the special cases, which is why they are in the list.

## Key concepts

### The two degenerate cases, and what each one means

The recursion divides by the first entry of the previous row, so a zero there breaks it. There are two distinct ways this happens and they mean different things.

**A zero in the first column, rest of the row non-zero.** Replace the zero with a small symbol $$\varepsilon$$, continue, and take $$\varepsilon \to 0^+$$ when reading signs. This is pure bookkeeping — a removable singularity in the algorithm, not a feature of the system.

**An entire row of zeros.** This one is substantive: it signals roots symmetric about the origin, which in practice means **a pair of poles sitting exactly on the imaginary axis** — the system is oscillating, marginally stable, neither decaying nor growing. The fix is to form the auxiliary polynomial from the row above, differentiate it, and use its coefficients as the zero row. The fifth-degree example above exercises this and correctly reports 0 RHP roots with 4 on the axis.

The distinction matters because the second case is *the boundary you are usually looking for*. An all-zero row is the algorithm telling you it has found the exact edge of stability.

### From "is it stable" to "for which K"

This is where the method earns its place. Take unity feedback around $$K/\big(s(s+1)(s+2)\big)$$. The characteristic polynomial is

$$
s^3 + 3s^2 + 2s + K .
$$

The $$s^1$$ entry of the Routh array is $$(6-K)/3$$, and the $$s^0$$ entry is $$K$$. Requiring both positive gives

$$
\boxed{0 < K < 6}
$$

in one line, with no root-finding. Checking against actual poles:

```
 K=1.0: max Re(pole) = -0.337641  stable
 K=5.9: max Re(pole) = -0.004568  stable
 K=6.0: max Re(pole) = +0.000000  marginal   <- boundary
 K=6.5: max Re(pole) = +0.022186  UNSTABLE
```

At exactly $$K = 6$$ the poles are $$-3$$ and $$\pm j\sqrt{2}$$ — precisely on the imaginary axis, precisely what the all-zero-row case describes.

### Feedback can stabilise an unstable plant, but only in a window

The more interesting result is that the bound need not be one-sided. Take the genuinely unstable plant $$1/\big((s-1)(s+2)(s+3)\big)$$, which has a pole at $$s = +1$$. With gain $$K$$ and unity feedback the characteristic polynomial is

$$
s^3 + 4s^2 + s + (K - 6),
$$

and Routh requires both $$K - 6 > 0$$ and $$4 > K - 6$$, giving

$$
6 < K < 10 .
$$

A **lower** bound as well as an upper one. Verified:

```
 K=5.0:  max Re(pole) = +0.377203  UNSTABLE   (too little gain)
 K=7.0:  max Re(pole) = -0.096850  stable
 K=9.0:  max Re(pole) = -0.030267  stable
 K=11.0: max Re(pole) = +0.028635  UNSTABLE   (too much gain)
```

Two things follow. First, **feedback really can stabilise something that is unstable on its own** — the open-loop plant has a right-half-plane pole and the closed loop does not. Second, **more gain is not monotonically better**; there is a window, and both walls are real. The instinct that "turn the gain up until it tracks well" is safe is simply wrong, and this is the cheapest possible demonstration.

### Why you cannot cancel an unstable pole instead

The tempting shortcut is to put a zero exactly on top of the bad pole and cancel it. Algebraically this works. Physically it does not, for reasons worth stating because the same reasoning recurs elsewhere:

- You never know the pole's location exactly. A resistor is specified to 1% or 5%; a complex plant's poles are known far less precisely than that.
- Parameters **drift**. Components age, temperatures change, mass changes. The pole moves and your fixed zero does not follow it.
- Worst of all, the failure is **hidden**. A near-cancellation looks fine in nominal conditions and the uncancelled unstable mode reappears only in some specific corner of operation — which is more dangerous than an obvious instability, because nothing warns you.

Cancellation replaces a visible problem with an invisible one. Placing the closed-loop poles by feedback does not depend on knowing the open-loop poles exactly, which is precisely why it is the robust move.

## Why it matters for my work

The transferable idea is **deciding a property of a solution set without computing the solutions**. The Routh array answers a question about roots using only coefficients, and it does so for a whole family of systems at once. That pattern — reason about the region of parameter space where a property holds, rather than sampling parameters and testing — is the same move as characterising a feasible region rather than grid-searching it.

The unstable-plant result reframes something I default to assuming. If a deployment loop has a self-reinforcing path — a model whose outputs shape the data it is later retrained on — the intuition "reduce the feedback strength until it is safe" may be exactly backwards. There are configurations where too *little* corrective feedback is what leaves a bad mode growing. The window has two walls.

And the pole-cancellation argument is a general warning about **fixes that depend on knowing a parameter exactly**. Any correction calibrated to a nominal value silently stops working when that value drifts, and the failure appears only in the corner where it matters. A threshold tuned on a development set is exactly this kind of fix.

## What I have not resolved

Routh–Hurwitz gives a yes/no answer and a parameter range. It says nothing about **how** stable — a system with a pole at $$-0.001$$ passes and is useless. The margin questions belong to the frequency-domain treatment and I want to understand the exact relationship between "distance from a sign change in the first column" and the gain margin, if there is a clean one.

I also have not worked out the multi-parameter case properly. The examples above vary one gain. With two free parameters the stability region is an area in a plane, and the worked approach I have seen amounts to gridding it and testing each point — which works but abandons the very thing that made the criterion elegant.

---

Sources: the Routh–Hurwitz criterion, its two degenerate cases, and the pole-cancellation robustness argument are standard results in classical control theory. The numerical claims here — the Routh array implemented over exact rationals and validated against computed roots on six polynomials including both special cases, and the two gain-range examples checked pole-by-pole — were computed directly.
