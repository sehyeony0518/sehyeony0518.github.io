---
layout: study_note
title: "Linearization: An Approximation Whose Licence Is Retrospective"
description: "Pendulum linearization, small-angle sine approximations, Taylor error bounds, phase drift, and the poles that distinguish hanging, inverted, and cart-pole dynamics."
og_image: "https://sehyeony0518.github.io/assets/img/og/linearization-and-the-inverted-pendulum.png"
tab: "ai-foundations"
tab_title: "AI Theory"
category: "feedback-control"
category_title: "Feedback Control & Classical Design"
subgroup: "Feedback & Local System Models"
order: 2
source: "Independent study"
written: true
updated: "2026-09-15"
---

Linearization replaces nonlinear dynamics with their first-order behavior near a specified operating point. Its usefulness is local, but its justification is not exclusively retrospective. Taylor bounds can control the neglected terms before simulation, and stability analysis can establish local conclusions.

Two corrections matter. The nonlinear pendulum is not an unsolvable equation: the unforced, undamped problem has an energy integral and a solution describable through elliptic functions. Numerical integration also does not require linearization. What the linear approximation supplies is a simpler model whose modes, response, and controller design can be analyzed directly.

The questions to keep separate are the error in the force law, the error in a trajectory over time, and the stability of an equilibrium. A small instantaneous approximation error does not automatically control all three.

## Deriving the fixed-pivot pendulum equation

Consider a point mass on a massless rod with fixed length. Measure its angle from the downward vertical. Its coordinates are

$$
x=\ell\sin\theta,
\qquad
y=-\ell\cos\theta.
$$

Differentiating gives

$$
\dot x=\ell\cos\theta\,\dot\theta,
\qquad
\dot y=\ell\sin\theta\,\dot\theta.
$$

Therefore,

$$
\dot x^2+\dot y^2
=
\ell^2(\cos^2\theta+\sin^2\theta)\dot\theta^2
=
\ell^2\dot\theta^2.
$$

The kinetic and gravitational potential energies are

$$
T=\frac12m\ell^2\dot\theta^2,
$$

$$
U=mg\ell(1-\cos\theta),
$$

where the potential is zero at the hanging equilibrium.

The Lagrangian is kinetic minus potential energy. Its relevant derivatives are

$$
\frac{\partial L}{\partial\dot\theta}
=
m\ell^2\dot\theta,
$$

$$
\frac{\partial L}{\partial\theta}
=
-mg\ell\sin\theta.
$$

Applying the Euler–Lagrange equation with an external torque and viscous damping gives

$$
\frac{d}{dt}
\frac{\partial L}{\partial\dot\theta}
-
\frac{\partial L}{\partial\theta}
=
\tau-b\dot\theta.
$$

Hence,

$$
m\ell^2\ddot\theta
+
b\dot\theta
+
mg\ell\sin\theta
=
\tau.
$$

The gravity term's sign follows from geometry: a small positive angle from the downward vertical produces a restoring torque.

All angles in the equations are in radians. Replacing an angle in radians by its numerical value in degrees invalidates the small-angle approximation.

This model also specifies the mass distribution. A uniform rod has a different moment of inertia and center of mass. Its coefficients must be derived accordingly rather than copied from the point-mass model.

## What linearization actually computes

For a nonlinear state equation,

$$
\dot x=f(x,u),
$$

choose an equilibrium satisfying

$$
f(x^*,u^*)=0.
$$

Introduce perturbations,

$$
\delta x=x-x^*,
\qquad
\delta u=u-u^*.
$$

A first-order expansion gives

$$
\dot{\delta x}
=
A\delta x+B\delta u+\text{higher-order terms},
$$

where

$$
A=\left.\frac{\partial f}{\partial x}\right|_{x^*,u^*},
\qquad
B=\left.\frac{\partial f}{\partial u}\right|_{x^*,u^*}.
$$

The constant term vanishes because the operating point is an equilibrium. Around a general point it would remain, and around a moving reference trajectory the linearization can become time-dependent.

For the pendulum, choose the state as angle and angular velocity:

$$
x=
\begin{bmatrix}
\theta\\
\omega
\end{bmatrix},
\qquad
\omega=\dot\theta.
$$

Then

$$
f(x,\tau)
=
\begin{bmatrix}
\omega\\
-\dfrac{g}{\ell}\sin\theta
-\dfrac{b}{m\ell^2}\omega
+\dfrac{\tau}{m\ell^2}
\end{bmatrix}.
$$

At an equilibrium with zero angular velocity,

$$
\tau^*=mg\ell\sin\theta^*.
$$

The Jacobian matrices are

$$
A=
\begin{bmatrix}
0&1\\
-\dfrac{g}{\ell}\cos\theta^*
&
-\dfrac{b}{m\ell^2}
\end{bmatrix},
\qquad
B=
\begin{bmatrix}
0\\
\dfrac1{m\ell^2}
\end{bmatrix}.
$$

Linearization therefore depends on the equilibrium. The same physical pendulum produces a different sign in its stiffness term when expanded around the upward configuration.

## An a priori small-angle error bound

For a nonnegative angle,

$$
\theta-\sin\theta
=
\int_0^\theta(1-\cos t)\,dt.
$$

Also,

$$
1-\cos t
=
\int_0^t\sin u\,du
\leq
\int_0^t u\,du
=
\frac{t^2}{2}.
$$

Substitute into the first integral:

$$
0\leq\theta-\sin\theta
\leq
\int_0^\theta\frac{t^2}{2}\,dt
=
\frac{\theta^3}{6}.
$$

Odd symmetry extends the absolute-value bound to negative angles:

$$
\lvert\sin\theta-\theta\rvert
\leq
\frac{\lvert\theta\rvert^3}{6}.
$$

Relative to the magnitude of the linear term,

$$
\frac{\lvert\sin\theta-\theta\rvert}{\lvert\theta\rvert}
\leq
\frac{\theta^2}{6},
\qquad \theta\neq0.
$$

This is a bound available before solving a trajectory.

The denominator matters. This is relative error measured against the linear approximation, not against the exact sine. If relative error against the exact force is required, that denominator must be bounded separately.

The following values are calculated directly from the sine function:

| Angle in radians | Actual error relative to the linear term | Upper bound |
|---|---|---|
| $$0.1$$ | $$0.1666\%$$ | $$0.1667\%$$ |
| $$0.2$$ | $$0.6653\%$$ | $$0.6667\%$$ |
| $$0.4$$ | $$2.6454\%$$ | $$2.6667\%$$ |
| $$0.8$$ | $$10.3305\%$$ | $$10.6667\%$$ |

To guarantee at most one percent by this definition, require

$$
\frac{\theta^2}{6}\leq0.01.
$$

Thus,

$$
\lvert\theta\rvert
\leq
\sqrt{0.06}
\approx0.24495\ \text{radians},
$$

or approximately fourteen degrees.

This is a force-law criterion. It is not a guarantee of one-percent trajectory accuracy over an arbitrary duration.

## Turning local force error into a trajectory bound

Consider the unforced, undamped pendulum released from rest at an amplitude smaller than the upright angle. Let the nonlinear and linear solutions start from the same initial conditions.

Define

$$
\omega_0=\sqrt{\frac g\ell},
$$

and let the nonlinear solution satisfy

$$
\ddot\theta_{\mathrm{nl}}+\omega_0^2\sin\theta_{\mathrm{nl}}=0.
$$

The linear solution satisfies

$$
\ddot\theta_{\mathrm{lin}}+\omega_0^2\theta_{\mathrm{lin}}=0.
$$

Define their difference:

$$
e=\theta_{\mathrm{nl}}-\theta_{\mathrm{lin}}.
$$

Subtracting the equations and adding the required linear term gives

$$
\ddot e+\omega_0^2e
=
\omega_0^2
\left(
\theta_{\mathrm{nl}}-\sin\theta_{\mathrm{nl}}
\right).
$$

The error has zero initial displacement and velocity. The forced oscillator solution is therefore

$$
e(t)
=
\omega_0
\int_0^t
\sin\bigl(\omega_0(t-s)\bigr)
\left(
\theta_{\mathrm{nl}}(s)-\sin\theta_{\mathrm{nl}}(s)
\right)\,ds.
$$

This kernel can be checked by differentiating twice: the integral contributes the forcing at its upper limit and otherwise satisfies the homogeneous oscillator equation.

Suppose the nonlinear angle remains within amplitude

$$
\alpha.
$$

Using the sine remainder and the fact that the kernel's sine magnitude is at most one gives

$$
\lvert e(t)\rvert
\leq
\frac{\omega_0\alpha^3t}{6}.
$$

The amplitude assumption can itself be justified by energy conservation. Release from rest gives energy equal to the potential at the initial amplitude. Kinetic energy is nonnegative, and potential increases with absolute angle before the upright position. The trajectory therefore cannot exceed its initial amplitude.

Introduce dimensionless time,

$$
\tau=\omega_0t.
$$

Then

$$
\frac{\lvert e(t)\rvert}{\alpha}
\leq
\frac{\alpha^2\tau}{6}.
$$

For a constructed amplitude of two-tenths of a radian and dimensionless duration ten,

$$
\lvert e(t)\rvert
\leq
\frac{(0.2)^3(10)}6
=
0.01333\ \text{radians}.
$$

This bound is conservative, but it explicitly contains amplitude and duration. It explains why a local approximation statement without a time horizon is incomplete.

## The nonlinear period and accumulated phase error

The conserved energy is

$$
E
=
\frac12m\ell^2\dot\theta^2
+
mg\ell(1-\cos\theta).
$$

Release from rest at amplitude

$$
\alpha
$$

gives

$$
E=mg\ell(1-\cos\alpha).
$$

Subtract potential from total energy:

$$
\dot\theta^2
=
\frac{2g}{\ell}(\cos\theta-\cos\alpha).
$$

Using the half-angle identity,

$$
\cos\theta-\cos\alpha
=
2\left(
\sin^2\frac\alpha2-\sin^2\frac\theta2
\right).
$$

Define

$$
k=\sin\frac\alpha2.
$$

One-quarter of the period is the time needed to travel between zero angle and the turning point. Thus,

$$
T
=
4\int_0^\alpha
\frac{d\theta}
{2\omega_0\sqrt{k^2-\sin^2(\theta/2)}}.
$$

Substitute

$$
\sin\frac\theta2=k\sin\phi.
$$

Differentiation gives

$$
d\theta
=
\frac{2k\cos\phi}
{\sqrt{1-k^2\sin^2\phi}}\,d\phi.
$$

The square-root factor involving the turning point cancels, yielding

$$
T
=
\frac4{\omega_0}
\int_0^{\pi/2}
\frac{d\phi}{\sqrt{1-k^2\sin^2\phi}}.
$$

This is an exact period formula for the stated undamped oscillation. Its integral is elliptic, not nonexistent.

For small amplitude, expand the integrand:

$$
(1-z)^{-1/2}
=
1+\frac z2+O(z^2).
$$

Since

$$
\int_0^{\pi/2}\sin^2\phi\,d\phi=\frac\pi4,
$$

the period becomes

$$
T
=
\frac{2\pi}{\omega_0}
\left[
1+\frac{k^2}{4}+O(k^4)
\right].
$$

Finally,

$$
k=\frac\alpha2+O(\alpha^3),
$$

so

$$
T
=
T_0
\left[
1+\frac{\alpha^2}{16}+O(\alpha^4)
\right],
\qquad
T_0=\frac{2\pi}{\omega_0}.
$$

The nonlinear pendulum has a slightly longer period. At amplitude four-tenths of a radian, the leading relative increase is

$$
\frac{0.4^2}{16}=0.01.
$$

A one-percent period discrepancy accumulates phase error over repeated cycles. To leading order, after a specified number of linear periods, the phase discrepancy is

$$
\Delta\phi
\approx
2\pi N\frac{\alpha^2}{16}.
$$

At twenty-five cycles in this example, that leading approximation is one-quarter of a full cycle.

The deterioration is continuous. There is no universal angle at which the linear approximation abruptly becomes useless. Usefulness depends on the error tolerance, duration, forcing, damping, and quantity being predicted.

## Hanging and inverted equilibria

With zero torque and damping, the hanging equilibrium is

$$
\theta^*=0.
$$

The perturbation equation is

$$
\ddot\eta+\omega_0^2\eta=0.
$$

Trying an exponential mode gives

$$
\lambda^2+\omega_0^2=0,
$$

so

$$
\lambda=\pm i\omega_0.
$$

The solution is

$$
\eta(t)
=
\eta_0\cos(\omega_0t)
+
\frac{\dot\eta_0}{\omega_0}\sin(\omega_0t).
$$

It remains bounded but does not decay.

For the upright equilibrium, write

$$
\theta=\pi+\eta.
$$

Since

$$
\sin(\pi+\eta)=-\sin\eta,
$$

the linearized equation is

$$
\ddot\eta-\omega_0^2\eta=0.
$$

Now

$$
\lambda=\pm\omega_0,
$$

and

$$
\eta(t)
=
\eta_0\cosh(\omega_0t)
+
\frac{\dot\eta_0}{\omega_0}\sinh(\omega_0t).
$$

A generic perturbation has a component along the growing mode. Special initial conditions can cancel that mode in the linear model, but this exceptional set does not make the equilibrium stable.

For an explicitly normalized construction with natural frequency one, choose

$$
\eta_0=0.01,\qquad \dot\eta_0=0.01.
$$

Then

$$
\eta(t)=0.01e^t.
$$

The linear prediction reaches two-tenths of a radian at

$$
t=\log20\approx2.9957.
$$

This is a local-model prediction of when the perturbation leaves a chosen region, not a claim that the linear model remains accurate indefinitely afterward.

The geometry already suggests the sign: the hanging equilibrium is a potential minimum and the upright equilibrium a maximum. The algebra quantifies the associated motion.

## What “stable” means here

The unforced hanging pendulum is locally stable in the sense that sufficiently small initial perturbations remain small. Its positive local energy and energy conservation establish this directly.

It is not asymptotically stable without damping, because the motion need not approach the equilibrium.

It is also important not to confuse bounded free motion with bounded-input, bounded-output stability of the linearized system. Apply a bounded resonant forcing:

$$
\ddot\theta+\omega_0^2\theta
=
a\cos(\omega_0t).
$$

A particular solution is

$$
\theta_p(t)
=
\frac{a}{2\omega_0}t\sin(\omega_0t).
$$

Substituting shows that differentiating the product produces the required cosine forcing while the remaining oscillator terms cancel. The amplitude grows with time despite the bounded input.

Thus the undamped linear oscillator is not BIBO stable.

For a general smooth nonlinear system, eigenvalues strictly in the left half-plane establish local exponential stability, while an eigenvalue with positive real part establishes instability. Eigenvalues on the imaginary axis are inconclusive without further analysis.

A one-dimensional example makes the boundary issue visible:

$$
\dot x=-x^3
$$

and

$$
\dot x=x^3
$$

both have zero linearization at the origin. The first moves small nonzero states toward zero; the second moves them away. The linear term alone cannot distinguish them.

## Deriving the cart-pole coupling

A cart-pole is not a fixed-pivot pendulum. The pivot accelerates in response to the cart force and the pole's motion.

Let the cart mass be

$$
M,
$$

and let the pole be a point mass at distance

$$
\ell
$$

on a massless rod. Use cart position and pole angle from the upward vertical as coordinates:

$$
x,\qquad\phi.
$$

The pole mass position is

$$
x_p=x+\ell\sin\phi,
\qquad
y_p=\ell\cos\phi.
$$

Expanding the squared velocities gives the total kinetic energy

$$
T
=
\frac12(M+m)\dot x^2
+
m\ell\cos\phi\,\dot x\dot\phi
+
\frac12m\ell^2\dot\phi^2.
$$

The potential energy is

$$
U=mg\ell\cos\phi.
$$

The cart has applied horizontal force, while the pivot supplies no independent control torque. The cart Euler–Lagrange equation is

$$
(M+m)\ddot x
+
m\ell\cos\phi\,\ddot\phi
-
m\ell\sin\phi\,\dot\phi^2
=
u.
$$

For the angular equation, the mixed velocity terms cancel:

$$
\begin{aligned}
\frac{d}{dt}\frac{\partial L}{\partial\dot\phi}
&=
m\ell\cos\phi\,\ddot x
-
m\ell\sin\phi\,\dot x\dot\phi
+
m\ell^2\ddot\phi,\\
\frac{\partial L}{\partial\phi}
&=
-m\ell\sin\phi\,\dot x\dot\phi
+
mg\ell\sin\phi.
\end{aligned}
$$

Therefore,

$$
\ell\ddot\phi+\cos\phi\,\ddot x-g\sin\phi=0.
$$

This cancellation is easy to miss when differentiating the coupled kinetic energy.

Eliminating angular acceleration gives the exact nonlinear cart acceleration:

$$
\ddot x
=
\frac{
u+m\ell\sin\phi\,\dot\phi^2
-mg\sin\phi\cos\phi
}{
M+m\sin^2\phi
}.
$$

Then

$$
\ddot\phi
=
\frac{g\sin\phi-\cos\phi\,\ddot x}{\ell}.
$$

These equations can be integrated directly. No linear approximation is required to construct this idealized simulator.

## Linear cart-pole dynamics and actuator-specific control

Around the upright equilibrium, discard terms above first order in the perturbations. The coupled equations become

$$
(M+m)\ddot x+m\ell\ddot\phi=u,
$$

$$
\ell\ddot\phi+\ddot x-g\phi=0.
$$

Eliminating one acceleration at a time yields

$$
\ddot x=\frac{u}{M}-\frac{mg}{M}\phi,
$$

$$
\ddot\phi
=
\frac{(M+m)g}{M\ell}\phi
-
\frac{u}{M\ell}.
$$

For the state ordered as cart position, cart velocity, pole angle, and angular velocity,

$$
A=
\begin{bmatrix}
0&1&0&0\\
0&0&-\dfrac{mg}{M}&0\\
0&0&0&1\\
0&0&\dfrac{(M+m)g}{M\ell}&0
\end{bmatrix},
$$

$$
B=
\begin{bmatrix}
0\\
1/M\\
0\\
-1/(M\ell)
\end{bmatrix}.
$$

Its open-loop eigenvalues are

$$
0,\quad0,\quad
\pm\sqrt{\frac{(M+m)g}{M\ell}}.
$$

The two zero modes concern cart translation. The unstable angular growth rate differs from the fixed-pivot result because the cart moves.

For a constructed parameter set,

$$
M=2,\qquad m=1,\qquad\ell=1,\qquad g=10,
$$

the angular eigenvalues are

$$
\pm\sqrt{15},
$$

whereas the fixed-pivot pendulum with the same length and gravity has eigenvalues

$$
\pm\sqrt{10}.
$$

A torque controller for a fixed pivot cannot simply be copied into the cart force input. The input matrix describes which acceleration the actuator actually influences.

For comparison, a directly torque-actuated inverted pendulum permits

$$
\tau=-k_p\eta-k_d\dot\eta.
$$

Its local equation becomes

$$
m\ell^2\ddot\eta
+
(b+k_d)\dot\eta
+
(k_p-mg\ell)\eta
=
0.
$$

Thus positive damping and restoring stiffness require

$$
b+k_d>0,
\qquad
k_p>mg\ell.
$$

With unit rotational inertia, gravitational coefficient ten, zero physical damping, proportional gain fourteen, and derivative gain four, the polynomial is

$$
s^2+4s+4=(s+2)^2.
$$

Both poles are negative. This is a local stability calculation for the specified torque actuator. Saturation, delay, and large angles require additional analysis.

## Revision checklist

| Check | What I should be able to reconstruct |
|---|---|
| Mechanics | Derive kinetic energy, potential energy, and the pendulum equation with consistent signs. |
| Operating point | Explain why the Jacobian depends on the equilibrium angle and input. |
| Small-angle bound | Derive the cubic sine remainder and distinguish its denominator conventions. |
| Time horizon | Convert force-law error into a trajectory bound with explicit duration. |
| Nonlinear period | Derive the energy integral and the elliptic period expression. |
| Phase drift | Recover the leading relative period correction $$\alpha^2/16$$. |
| Stability | Distinguish hanging oscillation, asymptotic convergence, and upright exponential growth. |
| Input response | Explain why an undamped oscillator can have bounded free motion but unbounded resonant response. |
| Cart-pole coupling | Reproduce the cancellation of the mixed velocity terms. |
| Linear cart-pole | Derive the acceleration equations, state matrices, and unstable growth rate. |
| Actuation | Distinguish direct pendulum torque from cart force. |
| Validation | State the angle range, duration, initial conditions, and actuator limits of any approximation claim. |

## Why it matters for my work

The useful discipline is to attach a domain and an error criterion to an approximation. “Locally accurate” must specify which quantity, around which operating point, and for how long.

The pendulum also separates errors that can be bounded analytically from discrepancies that require simulation or measurement. Both kinds of checking are useful; neither should be presented as the only justification.

## What I have not resolved

For an implemented simulator or controller, the remaining questions concern parameter uncertainty, numerical integration, delay, and saturation rather than the symbolic derivation alone.

Specify physical parameters and actuator limits, then compare nonlinear and linear trajectories over a declared initial-condition set and time horizon using a converged numerical solver.
