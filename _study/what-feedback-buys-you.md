---
layout: study_note
title: "What Feedback Buys You, and the One Thing It Cannot"
description: "Closing the loop divides plant error and disturbance by the loop gain, and drives steady-state error to zero — but S + T = 1 means sensor noise and reference tracking trade off exactly, at every frequency, forever."
tab: "ai-foundations"
tab_title: "Theory"
category: "feedback-control"
category_title: "Feedback Control & Classical Design"
order: 4
source: "Lecture notes, Ajou University"
written: true
updated: "2026-09-15"
---

A control specification usually has four parts, in this order: **be stable**, **ignore disturbances**, **respond quickly**, and **end up in the right place**. The third is transient response and is settled by pole placement. The other three are all answered by the same small piece of algebra, and that algebra also produces a hard limit that no amount of design effort removes.

## Core question and definition

Put the plant $$G$$ and controller $$D$$ in a loop, with a disturbance $$w$$ entering at the plant input and sensor noise $$v$$ on the measurement. Solving the loop equations gives

$$
Y = \underbrace{\frac{DG}{1+DG}}_{\mathcal{T}} R \;+\; \underbrace{\frac{G}{1+DG}}_{\text{disturbance}} W \;-\; \mathcal{T} V,
\qquad
E = \mathcal{S}R - \mathcal{S}G\,W + \mathcal{T}V ,
$$

where

$$
\mathcal{S} = \frac{1}{1+DG} \quad\text{(sensitivity)}, \qquad \mathcal{T} = \frac{DG}{1+DG} \quad\text{(complementary sensitivity)} .
$$

And immediately, by construction:

$$
\boxed{\;\mathcal{S} + \mathcal{T} = 1\;}
$$

I verified this at several complex operating points — it holds to machine precision, always, because it is an identity and not an approximation. Everything that follows is a consequence of those few lines.

## Key concepts

### Three things feedback genuinely gives you

**Disturbance rejection.** Open loop, $$Y = DGR + GW$$: the disturbance passes through with gain $$G$$ and there is nothing in the structure you can adjust, because $$G$$ is given and $$W$$ comes from outside. Closed loop, the disturbance is multiplied by $$G/(1+DG)$$. Large loop gain makes it small. A cruise control that holds 60 km/h up a hill, into a wind, with a full tank, is this term being driven down.

**Insensitivity to plant error.** The transfer function you were handed is a model — linearised, approximated, and drifting as things wear. The relevant question is how much an error in $$G$$ propagates into the closed-loop behaviour, and the right way to ask it is in relative terms:

$$
S^{\mathcal{T}}_{G} = \frac{\partial \mathcal{T}/\mathcal{T}}{\partial G/G} .
$$

Computing this numerically for both structures:

```
 G=2.0 D=1.0 : open-loop sens=1.000000   closed-loop sens=0.333333
 G=2.0 D=50.0: open-loop sens=1.000000   closed-loop sens=0.009901
 G=2.0 D=0.02: open-loop sens=1.000000   closed-loop sens=0.961538
```

Open loop it is **exactly 1**, at every operating point — a 10% error in the plant gives a 10% error in the result, no better and no worse. Closed loop it is $$1/(1+DG) = \mathcal{S}$$. With loop gain 100, a 10% plant error becomes a 0.1% error in the closed loop.

That the answer is $$\mathcal{S}$$ again, exactly, is the elegant part: **the sensitivity function really is the sensitivity**, in the plain calculus sense. Relative units matter here — comparing absolute changes when $$G$$ is measured in units of $$10^6$$ and $$D$$ in units of 1 produces meaningless ratios, which is why the definition is in percentages.

**Pole placement.** The closed-loop characteristic equation is $$1 + DG = 0$$, whose roots have no particular relationship to the poles of $$G$$. So an unstable plant can be stabilised — as the Routh-criterion examples make concrete. The honest statement is not "feedback makes things stable"; it is that **feedback gives you control over pole location**, and the same mechanism will happily destabilise a perfectly good plant if you point it the wrong way.

### The thing it cannot do

$$\mathcal{S} + \mathcal{T} = 1$$ means $$\mathcal{S}$$ and $$\mathcal{T}$$ cannot both be small. Look at the error equation again:

$$
E = \mathcal{S}R - \mathcal{S}G\,W + \mathcal{T}V .
$$

Tracking the reference well and rejecting disturbances both want $$\mathcal{S} \to 0$$. But $$\mathcal{S} \to 0$$ forces $$\mathcal{T} \to 1$$, and then **sensor noise passes into the output unattenuated**. Drive $$\mathcal{T} \to 0$$ to kill the noise and $$\mathcal{S} \to 1$$, destroying tracking. This is not a design difficulty to be engineered around. It is an identity.

The escape is not to beat the constraint but to **spend it across frequency**. These are functions of $$s$$; the trade-off is per-frequency, and the two signals usually live in different bands. References are typically low-frequency — a thermostat schedule changes over hours. Sensor noise is typically high-frequency. So: make the loop gain large at low frequency (small $$\mathcal{S}$$, good tracking and disturbance rejection where the reference lives) and small at high frequency (small $$\mathcal{T}$$, noise rejected where the noise lives). The trade-off is still paid in full at every frequency — it is just paid where it costs nothing.

### Steady-state error: system type and the error constants

For the final value, the final value theorem gives $$e_{ss} = \lim_{s\to 0} s\,\mathcal{S}(s)R(s)$$. Defining

$$
K_p = \lim_{s\to 0} DG, \qquad K_v = \lim_{s\to 0} s\,DG, \qquad K_a = \lim_{s\to 0} s^2 DG,
$$

the standard references give $$e_{ss} = 1/(1+K_p)$$ for a step, $$1/K_v$$ for a ramp, $$1/K_a$$ for a parabola. Checked against simulation:

```
 P control on a/(tau s+1)  [TYPE 0]
   a=1 k1=2: Kp=2  1/(1+Kp)=0.333333  simulated=0.333333
   a=2 k1=2: Kp=4  1/(1+Kp)=0.200000  simulated=0.200000
 PI control on the same plant [TYPE 1]
   a=1 k1=2 k2=2: Kv=2  1/Kv=0.500000  ramp sim=0.500000  step sim=1.4e-14
```

The **system type** $$n$$ is the number of poles at the origin in $$DG$$ — the number of integrators in the loop. Since $$1/s$$ has infinite gain at DC, each integrator sends one error constant to infinity and kills one order of steady-state error. For a reference $$t^k/k!$$:

| | step ($$k{=}0$$) | ramp ($$k{=}1$$) | parabola ($$k{=}2$$) |
|---|---|---|---|
| **type 0** | $$1/(1{+}K_p)$$ | $$\infty$$ | $$\infty$$ |
| **type 1** | 0 | $$1/K_v$$ | $$\infty$$ |
| **type 2** | 0 | 0 | $$1/K_a$$ |

I verified the general shape by taking the limit directly: the result is **strictly triangular** — zero when $$n > k$$, a finite constant $$1/A_0$$ when $$n = k$$, and infinite when $$n < k$$. One integrator buys exactly one order.

This is the cleanest argument for integral action I know. The PI controller's step error is not merely small, it is zero — the simulation returns $$10^{-14}$$, i.e. numerical noise — and it is zero *structurally*, not because anything was tuned. Compare the open-loop route to zero steady-state error, which requires the controller to be exactly $$1/G$$: unachievable, and it would drift anyway. Closed loop, the requirement is merely "make the loop gain large" or "add an integrator", both of which are easy and neither of which requires precision.

## Why it matters for my work

The idea I expect to reuse most is **the conserved quantity**. $$\mathcal{S} + \mathcal{T} = 1$$ says two desirable properties sum to a constant, so effort spent on one is taken from the other — and the productive response is not to fight it but to find the axis along which the two objectives are separated, and spend the budget there. Precision and recall have this shape. So does the bias–variance decomposition. Recognising that a trade-off is an identity rather than an engineering shortfall changes what one does about it: stop optimising, start looking for the axis of separation.

The parameter-sensitivity result has a direct analogue too. Open loop, model error propagates with gain exactly 1; closed loop, it is divided by $$1 + DG$$. A system that measures its own output and corrects is robust to being wrong about itself in a way that an open-loop pipeline simply is not. A model deployed without any measurement of its realised performance inherits its calibration error at gain 1, forever.

And **system type** is a nice reframing of structural versus tuned guarantees. Zero steady-state error from an integrator is a property of the loop's structure; it survives parameter drift. Anything obtained by tuning does not. It is worth asking of any pipeline property: is this structural, or did I tune it into place?

## What I have not resolved

The frequency-separation argument assumes references are low-frequency and noise is high-frequency. When they overlap there is no free lunch, and I do not know what the principled move is — presumably the trade-off simply has to be priced, but I would like to see how that is formulated.

I also do not know how far the $$\mathcal{S} + \mathcal{T} = 1$$ structure survives outside LTI systems. The identity follows from the loop algebra rather than from linearity as such, which suggests something analogous should hold more generally, but I have not found the statement.

---

Sources: the sensitivity and complementary sensitivity functions, the identity $$\mathcal{S} + \mathcal{T} = 1$$, the error constants, and the system-type classification are standard results in classical control theory. The numerical claims here — the identity checked at complex operating points, the open- and closed-loop parameter sensitivities computed by numerical differentiation, the error constants checked against simulated step and ramp responses, and the type-versus-input triangle evaluated by direct limits — were computed directly.
