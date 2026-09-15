---
layout: study_note
title: "Root Locus and Stability Margins: Two Pictures of the Same Boundary"
description: "Watching the closed-loop poles move as a gain sweeps, and reading how much gain and phase you have left off a plot of the open loop — two methods that meet exactly at the edge of stability."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "feedback-control"
category_title: "Feedback Control & Classical Design"
order: 5
source: "Lecture notes, Ajou University"
written: true
updated: "2026-09-15"
---

Design is pole placement, and pole placement means turning a knob and seeing where the poles go. The **root locus** answers that directly: plot the roots of $$1 + K L(s) = 0$$ as $$K$$ sweeps from 0 to $$\infty$$. The **Bode margins** answer a different-looking question — given a measured frequency response of the *open* loop, how much gain and phase can I still afford before the *closed* loop goes unstable. They turn out to be two views of the same boundary, and checking that they agree is the most satisfying thing in this material.

## Core question and definition

A point $$s$$ is on the root locus exactly when $$1 + K L(s) = 0$$, i.e. when

$$
|K L(s)| = 1 \qquad\text{and}\qquad \angle L(s) = 180^\circ \pmod{360^\circ}.
$$

The second condition — **the angle condition** — is the one that does the work, because it does not involve $$K$$ at all. Every rule for sketching a locus is a consequence of it.

The basic facts follow immediately from writing $$1 + K\,b(s)/a(s) = 0$$ as $$a(s) + K\,b(s) = 0$$: at $$K=0$$ the roots are the roots of $$a$$ (**the open-loop poles**), and as $$K \to \infty$$ they approach the roots of $$b$$ (**the open-loop zeros**), with the surplus $$n - m$$ branches escaping to infinity along asymptotes.

## Key concepts

### Two loci worth knowing by heart

**$$L(s) = 1/(s(s+1))$$.** Characteristic equation $$s^2 + s + K = 0$$. The branches start at $$0$$ and $$-1$$, meet on the real axis, and then go vertical:

```
 K=0     roots = [-1, 0]           (the open-loop poles)
 K=0.25  roots = [-0.5, -0.5]      (breakaway: a double root)
 K=2.0   roots = -0.5 +/- 1.3229j
 K=10.0  roots = -0.5 +/- 3.1225j
```

Past $$K = 1/4$$ the real part is **pinned at $$-1/2$$ forever**. Increasing the gain buys more $$\omega_d$$ — faster oscillation — and not one bit more decay. Since $$\zeta$$ is the pole angle, raising $$K$$ steadily *reduces* the damping ratio. That is a design conclusion, and it is visible in a single picture: this loop can never be made to settle faster than $$e^{-t/2}$$, whatever the gain.

If I want $$\zeta = 1/2$$, that is a pole at $$60^\circ$$ from the negative real axis. On the line $$\operatorname{Re} = -1/2$$ that means $$s = -0.5 \pm 0.866j$$, giving $$K = 1.0$$ and $$\zeta = 0.5000$$ exactly. The design reduces to *reading a value off the locus*.

**$$L(s) = s/(s^2+1)$$** — a plant with poles on the imaginary axis and a zero at the origin:

```
 K=0    roots = +/-1j       |roots| = 1
 K=1.0  roots = -0.5+/-0.866j   |roots| = 1
 K=2.0  roots = [-1, -1]        |roots| = 1   <- break-IN
 K=3.0  roots = [-2.618, -0.382]
 K=10   roots = [-9.899, -0.101]
```

For $$0 < K < 2$$ the roots sit **exactly on the unit circle** (their product is 1), then meet at $$-1$$ and split along the real axis — one heading to the zero at the origin, one to infinity. This is the counterpart to the first example: here the branches come *in* to the real axis (break-in) rather than leaving it (breakaway), and the zero is what pulls one branch back.

### Departure angles, without memorising the formula

The textbook formula for the angle at which a branch leaves a complex pole is long enough that it invites memorisation and therefore error. It is better derived each time. Put a test point $$s$$ infinitesimally away from pole $$p_\ell$$ in the direction you want to find. The angle condition must hold at $$s$$; every *other* pole and zero is so far away that the angle to it is unchanged if you replace $$s$$ by $$p_\ell$$ itself. The only term that depends on the direction is the one from $$p_\ell$$, which *is* the departure angle. Solving:

$$
\phi_\ell = 180^\circ + \sum_i \angle(p_\ell - z_i) - \sum_{j \ne \ell} \angle(p_\ell - p_j).
$$

I checked this against numerically traced loci — perturbing $$K$$ off zero and measuring the direction the nearest root actually moves:

```
 poles -1, -2+/-2j; zero at -3
   pole  (-1+0j): formula -180.00  traced -180.00   OK
   pole  (-2+2j): formula  +36.87  traced  +36.87   OK
   pole  (-2-2j): formula  -36.87  traced  -36.87   OK
```

Agreement across four different pole/zero configurations. The derivation is short enough to redo under exam conditions, which makes it strictly better than the formula.

### Breakaway points are candidates, not answers

Where branches meet, the characteristic equation has a repeated root, which happens exactly where $$dK/ds = 0$$, i.e. $$a'b - ab' = 0$$. This is a **necessary** condition, and the distinction matters:

```
 1 + K s/(s^2+1):  a'b - ab' = s^2 - 1 = 0  ->  s = +/-1
   s=+1: K = -A/B = -2.0000  -> rejected (K<0), not on the K>0 locus
   s=-1: K = -A/B = +2.0000  -> valid, BREAK-IN
```

Half the candidates are spurious. Solving the equation gives you points that would be multiple roots *for some* $$K$$, including negative $$K$$, which is not the locus you are drawing. Every candidate must be checked by computing its $$K$$ and discarding the ones that come out negative.

### Where the locus crosses the imaginary axis

The crossing is the stability boundary, and there is a clean way to find it: substitute $$s = j\omega$$ into the characteristic polynomial and separate real and imaginary parts. Since even powers of $$j\omega$$ are real and odd powers imaginary, the even-power terms and odd-power terms must each vanish. Two equations, two unknowns ($$\omega$$ and $$K$$), and if they have no consistent solution then the locus never crosses and the loop is stable for all $$K > 0$$.

There is also a structural rule worth knowing: when $$n - m \ge 3$$, the asymptotes leave at angles $$60^\circ, 180^\circ, 300^\circ$$ (or tighter), which guarantees that some branch heads into the right half-plane. **A pole-zero excess of three or more means the loop goes unstable at sufficiently high gain, always.** That is a conclusion available from counting alone, before any drawing.

### The same boundary, seen from the Bode plot

Now the other picture. Suppose you have measured $$L(j\omega)$$ — magnitude and phase versus frequency — and you want to know how much room is left.

- **Gain margin**: at the frequency where $$\angle L = -180^\circ$$, read $$|L|$$. The reciprocal is the factor by which the gain may still grow.
- **Phase margin**: at the frequency where $$|L| = 1$$ (0 dB), read how far the phase is above $$-180^\circ$$.

Taking the same plant Routh–Hurwitz analysis showed is stable for $$0 < K < 6$$:

```
 K=1   wc=0.4457  PM=+53.41deg | w180=1.4142 GM=6.000x (+15.56dB)  stable
 K=2   wc=0.7494  PM=+32.61deg | w180=1.4142 GM=3.000x ( +9.54dB)  stable
 K=6   wc=1.4142  PM= -0.00deg | w180=1.4142 GM=1.000x ( +0.00dB)  BOUNDARY
 K=12  wc=1.9545  PM=-17.25deg | w180=1.4142 GM=0.500x ( -6.02dB)  unstable
```

**The gain margin is exactly $$6/K$$.** At $$K=1$$ you may grow the gain sixfold; at $$K=2$$, threefold; at $$K=6$$ the margin is exactly 1 and the phase margin is exactly zero. The algebraic criterion and the frequency-domain reading agree to the last digit, and they agree *because they are the same statement*: the Routh boundary is the gain at which the locus crosses $$j\omega$$, which is the gain at which $$|L| = 1$$ where $$\angle L = -180^\circ$$.

This is what makes margins useful in practice: $$L(j\omega)$$ can be **measured experimentally** on hardware whose transfer function you never derived. You get a stability verdict for the closed loop without ever writing down a model.

One reading convenience: changing $$K$$ shifts the magnitude curve vertically and leaves the phase untouched. So one Bode plot serves all gains — instead of redrawing, slide the 0 dB reference line by $$20\log_{10}K$$ and read the margins against the moved line.

The honest caveat, which the lecture is careful about: the simple reading assumes the system goes from stable to unstable **once** as $$K$$ increases. When the locus crosses the axis several times, the phase can pass $$-180^\circ$$ repeatedly and no single margin number decides the question. That is what the Nyquist criterion exists to handle.

## Why it matters for my work

The idea I most want to carry over is **margin as a first-class quantity**. Classical control does not ask "does this work?" but "how far is this from not working, and in which direction?" — and it produces two different distances, because there are two different ways to fail. A model evaluated at a single operating point reports the equivalent of "currently stable". The useful question is how much the input distribution can shift, or how much the threshold can move, before the answer changes. I do not routinely compute that, and this is a good argument that I should.

The second is the **two-views discipline**. The same boundary computed two independent ways — an algebraic criterion on coefficients and a reading off a measured frequency response — agreeing exactly is strong evidence both are right. When a result is available by two genuinely different routes, computing it both ways is cheap insurance, and it caught nothing here only because nothing was wrong.

The third is smaller but practical: **necessary conditions generate candidates, not answers**. The breakaway equation produces spurious roots that must be filtered by checking $$K > 0$$. Any time I solve a derivative-equals-zero condition, half the output may be extraneous, and the filtering step is not optional.

## What I have not resolved

Gain and phase margin can both look healthy while the system is fragile to a *simultaneous* small change in both. I have seen this asserted and I have not worked through an example that exhibits it, nor do I know the standard robust-control answer (I believe it involves the minimum distance from the Nyquist curve to $$-1$$, but I have not verified that).

I also do not know how to sketch a locus when two parameters vary. The single-parameter case is a curve; two parameters give a surface, and the geometric rules that make the sketch tractable seem to depend on there being exactly one knob.

---

Sources: the root-locus construction rules, the departure- and arrival-angle conditions, the breakaway condition, and the gain/phase margin definitions are standard results in classical control theory. The numerical claims here — both loci traced root-by-root, the departure-angle formula validated against numerically traced loci in four pole/zero configurations, the breakaway candidates checked and the negative-$$K$$ one rejected, and the gain and phase margins computed from the open-loop frequency response and cross-checked against the Routh-derived boundary — were computed directly.
