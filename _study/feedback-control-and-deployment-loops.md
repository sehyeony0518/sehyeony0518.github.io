---
layout: study_note
title: "Feedback Control: Open Loop, Feedforward, and Why More Feedback Can Be Worse"
description: "The three ways to make a system do what you want, the shower that scalds you because the thermostat is by the door, and what that says about a model retraining on data its own deployment produced."
og_image: "https://sehyeony0518.github.io/assets/img/og/feedback-control-and-deployment-loops.png"
tab: "ai-foundations"
tab_title: "AI Theory"
category: "feedback-control"
category_title: "Feedback Control & Classical Design"
subgroup: "Feedback & Local System Models"
order: 1
source: "Independent study"
written: true
updated: "2026-09-15"
---

Feedback uses a measurement of a system to change an input that affects that system. Whether this improves behavior depends on the dynamics, the measurement process, the controller, and the delay.

Monitoring alone is not feedback control. A dashboard closes no control loop unless its measurements change an action. Similarly, observing an incoming disturbance becomes feedforward control only when the observation is used to compensate for that disturbance.

These distinctions matter when describing deployed machine learning. Retraining can create a feedback loop, but the word “feedback” does not establish its sign, gain, stability, or usefulness. Those properties must come from an explicit model.

## Start with a dynamic plant

Consider a scalar system,

$$
m\dot y+by=u+d,
$$

with positive inertia and drag coefficients. The controlled input is represented by the first right-hand term, while the second is an external disturbance.

For a velocity interpretation, inertia is mass, drag is proportional to velocity, and input and disturbance are forces. Other applications can use different units while preserving the same mathematical structure.

The state matters because the output does not jump immediately to the equilibrium associated with a new input. With constant input and disturbance, the equilibrium is

$$
y_\infty=\frac{u+d}{b}.
$$

To derive the transient, subtract this equilibrium:

$$
m\frac{d}{dt}(y-y_\infty)+b(y-y_\infty)=0.
$$

Separating variables and integrating gives

$$
y(t)-y_\infty
=
\bigl(y(0)-y_\infty\bigr)e^{-bt/m}.
$$

The time constant is therefore

$$
\frac{m}{b}.
$$

It is the time at which the initial discrepancy has been multiplied by the reciprocal of the exponential constant.

A controller changes both the equilibrium response and, usually, the transient. Examining only whether the final output can equal the target misses half the problem.

## Open loop, feedforward, and feedback

Suppose the desired trajectory is

$$
r(t).
$$

If the model is exact and there is no disturbance, substituting the desired trajectory into the plant suggests

$$
u_{\mathrm{nominal}}=m\dot r+br.
$$

This is an open-loop reference input. It produces the desired motion if the initial condition agrees and the assumptions hold.

If a disturbance estimate is available, feedforward compensation gives

$$
u_{\mathrm{ff}}
=
m\dot r+br-\widehat d.
$$

The estimate is subtracted because the disturbance enters the same input channel as the control.

Now add proportional feedback:

$$
u
=
m\dot r+br-\widehat d+k(r-y).
$$

Define tracking error as reference minus output:

$$
e=r-y.
$$

Substitute the controller into the plant:

$$
m\dot y+by
=
m\dot r+br-\widehat d+ke+d.
$$

Move output terms to the reference side and use the error definition:

$$
m\dot e+(b+k)e=\widehat d-d.
$$

This equation exposes the roles of the three components. Reference feedforward supplies the nominal input. Disturbance feedforward cancels the measured disturbance. Feedback corrects the remaining discrepancy.

Feedforward and feedback are therefore compatible. A useful controller often uses both.

## A numerical tracking example

Construct a plant with

$$
m=2,\qquad b=1,
$$

and a constant target

$$
r=10.
$$

Let the disturbance be a constant opposing force,

$$
d=-4,
$$

and suppose there is no disturbance estimate.

With nominal feedforward and no feedback, the commanded input is ten. The steady output is

$$
y_\infty=\frac{10-4}{1}=6,
$$

so the steady error is four.

Add proportional gain

$$
k=3.
$$

The error equation becomes

$$
2\dot e+4e=4.
$$

Thus,

$$
e_\infty=1,
$$

and

$$
e(t)=1+\bigl(e(0)-1\bigr)e^{-2t}.
$$

The steady output is nine. At that output, the controller commands

$$
u=10+3(10-9)=13.
$$

Substitution into the plant checks the equilibrium directly:

$$
1(9)=13-4.
$$

Feedback reduced the steady disturbance error from four to one and reduced the time constant from two to one-half. These numbers follow from the constructed equation.

There is also an actuator requirement. If the largest permitted input were twelve, the largest sustainable output under the same disturbance would be

$$
y_{\max}=\frac{12-4}{1}=8.
$$

No gain choice can make that actuator maintain an output of ten. A controller cannot overcome an infeasible equilibrium merely by requesting larger corrections.

## Deriving the standard closed-loop transfer functions

Use a linear plant and controller in the Laplace domain, with zero initial conditions for the transfer-function calculation.

Let

$$
Y=P(U+D),
$$

and suppose the sensor measures output plus noise:

$$
Y_{\mathrm{measured}}=Y+N.
$$

For ordinary output feedback,

$$
U=C(R-Y-N).
$$

Substitute the controller equation:

$$
Y=PC(R-Y-N)+PD.
$$

Collect the output terms:

$$
(1+PC)Y=PC\,R+P\,D-PC\,N.
$$

Define the loop transfer function,

$$
L=PC,
$$

the sensitivity,

$$
S=\frac1{1+L},
$$

and complementary sensitivity,

$$
T=\frac{L}{1+L}.
$$

The output becomes

$$
Y=T R+PS D-T N.
$$

The denominators are not decorative. They contain the characteristic equation determining closed-loop poles:

$$
1+L(s)=0.
$$

The names also encode a useful identity:

$$
S+T
=
\frac1{1+L}+\frac{L}{1+L}
=
1.
$$

At frequencies where the loop magnitude is large and its phase is suitable, sensitivity can be small. Disturbance effects and certain model errors are then suppressed. But complementary sensitivity is close to one, so measurement noise in that frequency range is transmitted to the output with nearly unit magnitude and opposite sign.

There is no universal claim here that more gain always amplifies output noise beyond its original magnitude. The precise claim comes from the frequency-dependent transfer function.

These formulas describe the zero-state input–output relation. Internal stability additionally requires checking internal modes, including any unstable modes hidden by cancellations.

## Why sensitivity measures sensitivity

Consider the closed-loop reference transfer function with a fixed controller:

$$
T(P)=\frac{PC}{1+PC}.
$$

Differentiate with respect to the plant transfer value:

$$
\frac{\partial T}{\partial P}
=
\frac{C}{(1+PC)^2}.
$$

For a small perturbation,

$$
\frac{\delta T}{T}
\approx
\frac{P}{T}\frac{\partial T}{\partial P}
\frac{\delta P}{P}.
$$

Substituting and simplifying gives

$$
\frac{\delta T}{T}
\approx
\frac1{1+PC}\frac{\delta P}{P}
=
S\frac{\delta P}{P}.
$$

Thus sensitivity converts a small relative plant error into a relative closed-loop transfer error, at frequencies where these ratios are defined.

This is one reason feedback can make performance less dependent on an exact plant model. The qualification is that the loop must remain stable. A small nominal sensitivity at selected frequencies is insufficient if model error moves a closed-loop pole into an unstable region.

The same denominator that reduces error can also become small near a poorly damped mode. Large response peaks are therefore possible even when the feedback sign is conventionally called negative.

## Sampling produces a discrete-time system

A deployed controller acts at discrete times. Even a continuous plant should therefore be connected to its sampling interval.

Hold the input and disturbance constant over a time interval of length

$$
h.
$$

The previously derived first-order solution gives

$$
y_{k+1}
=
e^{-bh/m}y_k
+
\frac{1-e^{-bh/m}}{b}(u_k+d_k).
$$

This is exact for the scalar plant under the stated hold assumption.

The coefficients depend on the sampling interval. A controller tuned for one interval does not automatically have the same dynamics if measurements arrive more slowly.

More generally, a discrete linear approximation has the form

$$
x_{t+1}=ax_t+cu_t.
$$

With instantaneous proportional feedback,

$$
u_t=-kx_t,
$$

the closed-loop recursion is

$$
x_{t+1}=(a-ck)x_t.
$$

Repeated substitution gives

$$
x_t=(a-ck)^t x_0.
$$

Hence the origin is asymptotically stable exactly when

$$
\lvert a-ck\rvert<1.
$$

The unit circle is the discrete-time stability boundary because powers of a multiplier decay inside it and grow outside it.

## One delayed measurement can reverse stability

Construct a discrete integrator,

$$
x_{t+1}=x_t+u_t.
$$

With current-state feedback,

$$
u_t=-kx_t,
$$

the closed-loop multiplier is

$$
1-k.
$$

It is stable for

$$
0<k<2.
$$

Now delay the measurement by one step:

$$
u_t=-kx_{t-1}.
$$

The recursion becomes

$$
x_{t+1}=x_t-kx_{t-1}.
$$

Try a mode of the form

$$
x_t=z^t.
$$

After substitution and division by the common power, the characteristic equation is

$$
z^2-z+k=0.
$$

Its roots are

$$
z_\pm=\frac{1\pm\sqrt{1-4k}}2.
$$

For positive gains up to one-quarter, both roots are real and inside the unit circle. Above one-quarter they form a complex-conjugate pair. Their product is the gain, so their common magnitude is

$$
\lvert z_\pm\rvert=\sqrt{k}.
$$

The delayed system is therefore stable for

$$
0<k<1.
$$

The allowable gain range has shrunk.

Choose the constructed gain

$$
k=1.5.
$$

Without delay, the multiplier is negative one-half, so oscillations decay. With one-step delay, the root magnitude is

$$
\sqrt{1.5}\approx1.2247,
$$

so oscillations grow.

Starting the delayed system with both required initial states equal to one gives:

| Time | No delay, starting at one | One-step delay, both initial states one |
|---|---|---|
| $$0$$ | $$1$$ | $$1$$ |
| $$1$$ | $$-0.5$$ | $$-0.5$$ |
| $$2$$ | $$0.25$$ | $$-2$$ |
| $$3$$ | $$-0.125$$ | $$-1.25$$ |
| $$4$$ | $$0.0625$$ | $$1.75$$ |
| $$5$$ | $$-0.03125$$ | $$3.625$$ |

Every delayed entry follows by subtracting one-and-a-half times the previous-but-one entry from the current entry.

Reducing the gain to one-half gives delayed roots

$$
\frac12\pm\frac12 i,
$$

with magnitude

$$
\frac1{\sqrt2}.
$$

This stabilizes this particular system. “Reduce the gain” is not a general theorem for every unstable feedback loop, because the open-loop dynamics and the sign of the response also matter.

## Integral action removes a constant offset

Proportional feedback leaves a constant disturbance error in the earlier plant. To accumulate persistent error, introduce an integral state:

$$
\dot I=e.
$$

For a constant reference, use

$$
u=br+k_p e+k_i I.
$$

Substituting into the plant yields

$$
m\dot e+(b+k_p)e+k_i I=-d.
$$

If the disturbance is constant, differentiation gives

$$
m\ddot e+(b+k_p)\dot e+k_i e=0.
$$

The characteristic polynomial is

$$
ms^2+(b+k_p)s+k_i.
$$

For positive inertia, both roots have negative real parts when

$$
b+k_p>0,\qquad k_i>0.
$$

For real roots, their negative sum and positive product put both on the negative real axis. For complex-conjugate roots, their real part is half the negative coefficient of the first-order term after normalization.

At equilibrium, the integral state's derivative must vanish, so

$$
e_\infty=0.
$$

The integral state takes the value needed to cancel the disturbance:

$$
k_i I_\infty=-d.
$$

Integral action has introduced both a benefit and an additional dynamic state. With delays or saturation, the simple polynomial above no longer describes the whole loop.

If the actuator saturates while error persists, the integral state can keep growing despite the requested correction being unavailable. When the actuator leaves saturation, the accumulated command can produce a large overshoot. This is integral windup. Its remedy requires accounting for the actuator limit, rather than pretending that the commanded input was applied.

## Retraining as a distribution-response map

A deployment loop can be represented abstractly without assuming that it behaves like a shower or a motor.

Let the deployed parameter determine a data distribution:

$$
\mathcal D(\theta).
$$

Retraining on that distribution defines an update map:

$$
F(\theta)
=
\arg\min_\phi
\mathbb E_{Z\sim\mathcal D(\theta)}
[\ell(\phi;Z)].
$$

For this notation, assume a particular minimizer selection rule when the optimum is not unique.

Repeated retraining gives

$$
\theta_{t+1}=F(\theta_t).
$$

A fixed point satisfies

$$
\theta^*=F(\theta^*).
$$

This means that retraining on the distribution induced by the deployed model returns the same model. It does not establish that the fixed point maximizes welfare, minimizes every deployment cost, or corresponds to an externally defined truth.

For a scalar differentiable map, write a small perturbation as

$$
\theta_t=\theta^*+\delta_t.
$$

A first-order expansion gives

$$
\delta_{t+1}
=
F'(\theta^*)\delta_t+O(\delta_t^2).
$$

The linearized perturbation decays when

$$
\lvert F'(\theta^*)\rvert<1.
$$

For vectors, the corresponding local condition is that all eigenvalues of the update Jacobian have magnitude below one. Equality on the boundary requires further analysis.

The derivative includes the effect of deployment on data and the effect of changed data on retraining. Neither part is visible from a static test-set score alone.

## Smoothing helps some response maps and fails on others

Construct a scalar prediction update,

$$
F(q)=0.2+0.5q.
$$

Its fixed point is obtained by solving

$$
q^*=0.2+0.5q^*,
$$

so

$$
q^*=0.4.
$$

Starting from eight-tenths gives successive values

$$
0.8,\quad0.6,\quad0.5,\quad0.45,\ldots
$$

The error from the fixed point halves on each update.

A smoothed update blends the old and newly fitted values:

$$
q_{t+1}=(1-\alpha)q_t+\alpha F(q_t).
$$

Its local derivative is

$$
1-\alpha+\alpha F'(q^*).
$$

If the original response slope is negative two, smoothing with one-half gives

$$
1-\frac12+\frac12(-2)=-\frac12.
$$

An oscillatory unstable update becomes locally stable.

But if the original slope is positive one-point-two, smoothing gives

$$
1-\alpha+1.2\alpha
=
1+0.2\alpha.
$$

Every positive smoothing coefficient leaves this multiplier above one. Smaller updates slow the divergence but do not stabilize the fixed point.

This directly limits the advice to “retrain more cautiously.” Whether smaller updates solve the problem depends on the response map.

## A stable measurement loop can converge to the wrong answer

Construct a population with a true positive fraction of one-half. Suppose a deployed score determines the fraction of cases that receive verification, and unverified positives are incorrectly recorded as negatives.

If each true positive is verified with probability equal to the score, the expected recorded positive fraction is

$$
F(q)=\frac12 q.
$$

Retraining a constant predictor on those recorded labels gives

$$
q_{t+1}=\frac12q_t.
$$

This loop is stable and converges to zero. The underlying positive fraction remains one-half by construction.

The failure is therefore not instability. It is a measurement process that makes the recorded target depend on the current predictor.

A smaller update can change the convergence speed while preserving the same wrong fixed point. Fixing the problem requires changing or identifying the observation process, for example through a verification stream whose selection is known.

Conversely, a prediction can alter the outcome through a beneficial intervention. In that case, lower observed outcome risk after deployment need not mean the original prediction was inaccurate. The system must distinguish an outcome under the deployed policy from an untreated or otherwise counterfactual outcome.

A realistic deployment analysis must specify which quantity the measurement is intended to estimate before borrowing the language of tracking error.

## Revision checklist

| Check | What I should be able to reconstruct |
|---|---|
| Plant dynamics | Derive the first-order equilibrium and exponential transient. |
| Control architecture | Distinguish reference feedforward, disturbance feedforward, and output feedback. |
| Tracking error | Derive the error equation with a consistent sign convention. |
| Worked example | Recover steady outputs of six and nine and the required input of thirteen. |
| Transfer functions | Derive reference, disturbance, and sensor-noise paths. |
| Sensitivity | Recover both the identity $$S+T=1$$ and the relative-perturbation interpretation. |
| Sampling | Explain how the update interval changes discrete plant coefficients. |
| Delay | Derive the delayed characteristic polynomial and its reduced stable gain range. |
| Integral action | Show why constant error vanishes and why an extra state appears. |
| Retraining | Define a distribution-response map and linearize it around a fixed point. |
| Smoothing | Explain why it stabilizes some negative slopes but not a slope above one. |
| Measurement validity | Reconstruct a stable loop that converges to a biased target. |

## Why it matters for my work

I should draw the loop through model outputs, human actions, verification, outcomes, and retraining. Monitoring is useful only when its target and the resulting action are clear.

The strongest correction to the original analogy is that stability and validity are separate. A deployment loop can settle smoothly while progressively distorting its own evidence.

## What I have not resolved

The response map and observation delays of a real deployment remain unknown. A scalar gain cannot simply be inferred from how strongly clinicians appear to use a prediction.

Identify the measured target, verification mechanism, action response, outcome delay, retraining rule, and local sensitivity of each link.
