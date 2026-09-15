---
layout: study_note
title: "What Feedback Buys You, and the One Thing It Cannot"
description: "Closing the loop divides plant error and disturbance by the loop gain, and drives steady-state error to zero — but S + T = 1 means sensor noise and reference tracking trade off exactly, at every frequency, forever."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "feedback-control"
category_title: "Feedback Control & Classical Design"
order: 4
source: "Lecture notes, Ajou University"
written: true
updated: "2026-09-15"
---

Feedback can reduce tracking error, attenuate disturbances, and reduce sensitivity to plant uncertainty. These benefits come from a common denominator in the loop equations. The same equations also show why good tracking and sensor-noise rejection conflict at the same frequency.

The order of analysis matters: derive the interconnection, establish stability, and then calculate its performance. Large loop gain alone is not a stability argument, and a small error reported by the controller need not mean a small physical tracking error.

## Core question and definition

**Which signals does feedback suppress, which signals does it transmit, and what assumptions make the steady-state claims valid?**

We use a scalar, continuous-time LTI negative-feedback loop with zero initial conditions for the transfer calculations.

### Label the signals before reducing the loop

Let the physical output be $$y$$ and the reference be $$r$$. The disturbance $$w$$ is added **at the plant input, after the controller**. Sensor noise $$v$$ is added **to the output measurement, before the feedback subtraction**.

Define the signals as follows:

| Signal | Definition or location |
|---|---|
| $$r$$ | Desired output |
| $$y$$ | True physical output |
| $$v$$ | Additive measurement error, in output units |
| $$m=y+v$$ | Measured output |
| $$e=r-y$$ | True tracking error |
| $$e_m=r-m=r-y-v$$ | Measured error seen by the controller |
| $$u$$ | Controller output |
| $$w$$ | Additive disturbance in plant-input units |
| $$u+w$$ | Actual plant input |

With controller $$D(s)$$ and plant $$G(s)$$, the Laplace-domain equations are

$$
M=Y+V,
$$

$$
E_m=R-M=R-Y-V,
$$

$$
U=DE_m,
$$

$$
Y=G(U+W).
$$

The true error is separately defined by

$$
E=R-Y.
$$

Thus

$$
\boxed{E_m=E-V}.
$$

The controller acts on $$E_m$$. It does not directly know $$E$$.

### Deriving the output response to every input

Substitute the controller equation into the plant equation:

$$
Y=G(DE_m+W).
$$

Now substitute the measured error:

$$
\begin{aligned}
Y
&=G\left[D(R-Y-V)+W\right]\\
&=DGR-DGY-DGV+GW.
\end{aligned}
$$

Move the term containing $$Y$$ to the left:

$$
Y+DGY=DGR+GW-DGV.
$$

Factor:

$$
(1+DG)Y=DGR+GW-DGV.
$$

Therefore,

$$
\boxed{
Y=
\frac{DG}{1+DG}R
+\frac{G}{1+DG}W
-\frac{DG}{1+DG}V
}.
$$

A transfer path is obtained by setting the other independent inputs to zero:

$$
\boxed{
\left.\frac{Y}{R}\right|_{W=V=0}
=\frac{DG}{1+DG}
},
$$

$$
\boxed{
\left.\frac{Y}{W}\right|_{R=V=0}
=\frac{G}{1+DG}
},
$$

$$
\boxed{
\left.\frac{Y}{V}\right|_{R=W=0}
=-\frac{DG}{1+DG}
}.
$$

The disturbance path contains an extra factor of $$G$$ because the disturbance enters before the plant. The negative sign in the noise path comes from subtracting the noisy measurement.

These answers depend on the injection locations. For example, if a different disturbance $$W_o$$ were added directly to the physical output,

$$
Y=GD(R-Y-V)+W_o,
$$

then

$$
(1+DG)Y=DGR-DGV+W_o,
$$

so its path would be

$$
\frac{Y}{W_o}=\frac1{1+DG}.
$$

An output disturbance and a plant-input disturbance do not have the same transfer function.

### Sensitivity, complementary sensitivity, and their identity

Define the loop transfer function

$$
L=DG.
$$

Then define

$$
\boxed{
\mathcal{S}=\frac1{1+L}
}
\qquad\text{and}\qquad
\boxed{
\mathcal{T}=\frac{L}{1+L}
}.
$$

These are the **sensitivity** and **complementary sensitivity** functions. The output equation becomes

$$
\boxed{
Y=\mathcal{T}R+G\mathcal{S}W-\mathcal{T}V
}.
$$

Adding the two functions gives

$$
\begin{aligned}
\mathcal{S}+\mathcal{T}
&=\frac1{1+L}+\frac{L}{1+L}\\
&=\frac{1+L}{1+L}\\
&=1.
\end{aligned}
$$

Thus

$$
\boxed{\mathcal{S}+\mathcal{T}=1}.
$$

This is structural: it follows from the specified loop equations, without choosing a particular controller. It is an identity of transfer functions wherever their evaluations are finite, not a performance target achieved by tuning.

The original numerical checks found agreement to machine precision at several complex operating points. Those checks validate the calculation; the algebra explains why the identity holds.

The identity also holds algebraically for unstable loop designs. It does not establish stability.

### Deriving true error and measured error separately

Start with the true error:

$$
E=R-Y.
$$

Substitute the output equation:

$$
\begin{aligned}
E
&=R-\mathcal{T}R-G\mathcal{S}W+\mathcal{T}V\\
&=(1-\mathcal{T})R-G\mathcal{S}W+\mathcal{T}V.
\end{aligned}
$$

Using $$1-\mathcal{T}=\mathcal{S}$$,

$$
\boxed{
E=\mathcal{S}R-G\mathcal{S}W+\mathcal{T}V
}.
$$

Now subtract the sensor noise to obtain the measured error:

$$
\begin{aligned}
E_m
&=E-V\\
&=\mathcal{S}R-G\mathcal{S}W+(\mathcal{T}-1)V\\
&=\mathcal{S}R-G\mathcal{S}W-\mathcal{S}V.
\end{aligned}
$$

Therefore,

$$
\boxed{
E_m=\mathcal{S}R-G\mathcal{S}W-\mathcal{S}V
}.
$$

The reference and disturbance terms match. The noise terms do not:

$$
\frac{E}{V}=\mathcal{T},
\qquad
\frac{E_m}{V}=-\mathcal{S}.
$$

For completeness, the controller output is

$$
\begin{aligned}
U
&=DE_m\\
&=D\mathcal{S}R-DG\mathcal{S}W-D\mathcal{S}V\\
&=D\mathcal{S}R-\mathcal{T}W-D\mathcal{S}V,
\end{aligned}
$$

because $$DG\mathcal{S}=L/(1+L)=\mathcal{T}$$.

The measured output satisfies

$$
\begin{aligned}
M
&=Y+V\\
&=\mathcal{T}R+G\mathcal{S}W+(1-\mathcal{T})V\\
&=\mathcal{T}R+G\mathcal{S}W+\mathcal{S}V.
\end{aligned}
$$

All paths can now be collected without ambiguity:

| Response | From $$R$$ | From $$W$$ | From $$V$$ |
|---|---|---|---|
| True output $$Y$$ | $$\mathcal{T}$$ | $$G\mathcal{S}$$ | $$-\mathcal{T}$$ |
| True error $$E=R-Y$$ | $$\mathcal{S}$$ | $$-G\mathcal{S}$$ | $$\mathcal{T}$$ |
| Measured error $$E_m=R-Y-V$$ | $$\mathcal{S}$$ | $$-G\mathcal{S}$$ | $$-\mathcal{S}$$ |
| Measured output $$M=Y+V$$ | $$\mathcal{T}$$ | $$G\mathcal{S}$$ | $$\mathcal{S}$$ |
| Controller output $$U$$ | $$D\mathcal{S}$$ | $$-\mathcal{T}$$ | $$-D\mathcal{S}$$ |

## Key concepts

### Disturbance rejection: what is divided by sensitivity?

For comparison, remove the feedback and let the controller act directly on the reference:

$$
U=DR.
$$

With the same plant-input disturbance,

$$
Y_{\mathrm{ol}}=G(DR+W)=DGR+GW.
$$

The open-loop disturbance path is $$G$$. The closed-loop path is $$G\mathcal{S}$$. Their ratio is

$$
\frac{G\mathcal{S}}G=\mathcal{S}
$$

where the ratio is defined.

Thus small $$\lvert\mathcal{S}\rvert$$ means attenuation **relative to the open-loop disturbance response**. The absolute closed-loop path is still $$G\mathcal{S}$$, not just $$\mathcal{S}$$.

For large loop magnitude,

$$
\mathcal{S}=\frac1{1+L}\approx\frac1L,
$$

and hence

$$
G\mathcal{S}\approx\frac{G}{DG}=\frac1D.
$$

This distinction matters: increasing plant gain and increasing controller gain need not have the same effect on absolute disturbance transmission, even when both increase $$\lvert L\rvert$$.

The original cruise-control example—holding 60 km/h despite a hill or wind—corresponds to suppressing the disturbance path in the frequency range occupied by those disturbances.

### Why the sensitivity function really is relative sensitivity

A transfer function can have units. Comparing an absolute change in a quantity measured on a scale of $$10^6$$ with one measured on a scale of $$1$$ is not a useful measure of robustness by itself.

For a transfer function $$F$$ depending on the plant $$G$$, define the dimensionless relative sensitivity

$$
S_G^F
=
\frac{dF/F}{dG/G}
=
\frac{G}{F}\frac{dF}{dG}.
$$

Here the controller and the evaluation point $$s$$ are fixed. The normalised expression requires nonzero nominal $$G$$ and $$F$$.

#### Open-loop structure

The reference transfer function is

$$
F_{\mathrm{ol}}=DG.
$$

Differentiating with $$D$$ fixed,

$$
\frac{dF_{\mathrm{ol}}}{dG}=D.
$$

Therefore,

$$
\begin{aligned}
S_G^{F_{\mathrm{ol}}}
&=\frac{G}{DG}D\\
&=1.
\end{aligned}
$$

Thus

$$
\boxed{S_G^{F_{\mathrm{ol}}}=1}.
$$

#### Closed-loop structure

The reference transfer function is

$$
\mathcal{T}=\frac{DG}{1+DG}.
$$

Apply the quotient rule:

$$
\begin{aligned}
\frac{d\mathcal{T}}{dG}
&=
\frac{D(1+DG)-(DG)D}{(1+DG)^2}\\
&=
\frac{D+D^2G-D^2G}{(1+DG)^2}\\
&=
\frac{D}{(1+DG)^2}.
\end{aligned}
$$

Now form the relative sensitivity:

$$
\begin{aligned}
S_G^{\mathcal{T}}
&=\frac{G}{\mathcal{T}}
\frac{D}{(1+DG)^2}\\
&=
\frac{G(1+DG)}{DG}
\frac{D}{(1+DG)^2}\\
&=\frac1{1+DG}\\
&=\mathcal{S}.
\end{aligned}
$$

Hence

$$
\boxed{
\frac{d\mathcal{T}/\mathcal{T}}{dG/G}
=\mathcal{S}
}.
$$

The name is literal: the sensitivity function is the relative differential sensitivity of the closed-loop reference transfer function to the plant.

### Preserved sensitivity checks

The original numerical differentiation results are reproduced unchanged:

```text
 G=2.0 D=1.0 : open-loop sens=1.000000   closed-loop sens=0.333333
 G=2.0 D=50.0: open-loop sens=1.000000   closed-loop sens=0.009901
 G=2.0 D=0.02: open-loop sens=1.000000   closed-loop sens=0.961538
```

The exact closed-loop values follow directly from the formula:

$$
G=2.0,\ D=1.0:
\qquad
\mathcal{S}=\frac1{1+2\cdot1}=\frac13,
$$

$$
G=2.0,\ D=50.0:
\qquad
\mathcal{S}=\frac1{1+2\cdot50}=\frac1{101},
$$

$$
G=2.0,\ D=0.02:
\qquad
\mathcal{S}
=\frac1{1+2/50}
=\frac{25}{26}.
$$

These are the exact fractions behind the recorded rounded decimals.

### Infinitesimal sensitivity versus a finite plant change

The differential result describes an infinitesimal perturbation. To calculate a finite change, write

$$
\widetilde G=G(1+\delta),
$$

where $$\delta$$ is the relative plant change, and keep $$D$$ fixed. Then

$$
\widetilde L=L(1+\delta),
$$

and

$$
\widetilde{\mathcal{T}}
=
\frac{L(1+\delta)}{1+L+L\delta}.
$$

Subtract the nominal transfer function:

$$
\begin{aligned}
\widetilde{\mathcal{T}}-\mathcal{T}
&=
\frac{L(1+\delta)}{1+L+L\delta}
-\frac{L}{1+L}\\
&=
\frac{
L\left[(1+\delta)(1+L)-(1+L+L\delta)\right]
}{
(1+L+L\delta)(1+L)
}\\
&=
\frac{L\delta}{(1+L+L\delta)(1+L)}.
\end{aligned}
$$

Divide by the nominal $$\mathcal{T}=L/(1+L)$$:

$$
\frac{\widetilde{\mathcal{T}}-\mathcal{T}}{\mathcal{T}}
=
\frac{\delta}{1+L+L\delta}.
$$

Factoring $$1+L$$ out of the denominator gives

$$
\boxed{
\frac{\widetilde{\mathcal{T}}-\mathcal{T}}{\mathcal{T}}
=
\frac{\mathcal{S}\delta}{1+\mathcal{T}\delta}
}.
$$

Only when the additional denominator is close to one can this be approximated by

$$
\frac{\widetilde{\mathcal{T}}-\mathcal{T}}{\mathcal{T}}
\approx\mathcal{S}\delta.
$$

For open loop, in contrast,

$$
\widetilde F_{\mathrm{ol}}=DG(1+\delta),
$$

so

$$
\frac{\widetilde F_{\mathrm{ol}}-F_{\mathrm{ol}}}{F_{\mathrm{ol}}}
=\delta
$$

exactly, including for finite changes. A 10% plant change gives a 10% open-loop transfer change under this fixed-controller comparison.

The original statement that loop gain $$100$$ turns a $$10\%$$ plant error into approximately $$0.1\%$$ is a rounded, first-order estimate. Its linearised fractional change is

$$
\mathcal{S}\delta
=\frac1{101}\cdot\frac1{10}
=\frac1{1010}.
$$

As a percentage, this is

$$
\frac{10}{101}\%\approx0.1\%.
$$

For a finite **positive** 10% perturbation, the exact fractional change is instead

$$
\frac{1/10}{1+100(1+1/10)}
=\frac1{1110},
$$

or exactly

$$
\frac{10}{111}\%.
$$

No new decimal approximation is needed to see the distinction.

The denominator also identifies a limitation:

$$
1+\widetilde L=(1+L)(1+\mathcal{T}\delta).
$$

For dynamic uncertainty, the perturbed loop's stability still needs to be checked. A nominal small differential sensitivity is not a blanket guarantee for arbitrary finite perturbations.

### The structural trade-off is between complex functions

From the derived paths,

$$
\frac{E}{R}=\mathcal{S},
\qquad
\frac{Y}{V}=-\mathcal{T}.
$$

Good reference tracking asks for small $$\lvert\mathcal{S}\rvert$$. Sensor-noise rejection asks for small $$\lvert\mathcal{T}\rvert$$.

But

$$
\mathcal{T}=1-\mathcal{S}.
$$

In particular, if $$\lvert\mathcal{S}\rvert\le\epsilon$$ at a frequency, then

$$
\lvert\mathcal{T}-1\rvert
=\lvert\mathcal{S}\rvert
\le\epsilon,
$$

and the reverse triangle inequality gives

$$
\lvert\mathcal{T}\rvert\ge1-\epsilon.
$$

The two functions cannot both be arbitrarily small at that frequency. More generally,

$$
1=\lvert\mathcal{S}+\mathcal{T}\rvert
\le\lvert\mathcal{S}\rvert+\lvert\mathcal{T}\rvert.
$$

However,

$$
\lvert\mathcal{S}\rvert+\lvert\mathcal{T}\rvert
$$

is not generally equal to one. The identity is a complex sum, not a conserved budget of two nonnegative magnitudes.

For example, at a point where $$L=-1+\epsilon$$ with nonzero real $$\epsilon$$,

$$
\mathcal{S}=\frac1\epsilon,
\qquad
\mathcal{T}=1-\frac1\epsilon.
$$

Both magnitudes can be large while their complex sum remains one. This is why a loop near the critical value $$-1$$ can amplify errors and noise rather than offering a useful trade-off.

### Why a small measured error can hide a large true error

Set $$R=W=0$$ and consider the sensor-noise response:

$$
Y=-\mathcal{T}V,
$$

$$
E=\mathcal{T}V,
$$

$$
E_m=-\mathcal{S}V.
$$

In a frequency range with large loop gain,

$$
\mathcal{S}\approx0,
\qquad
\mathcal{T}\approx1.
$$

Consequently,

$$
E_m\approx0,
\qquad
Y\approx-V,
\qquad
E\approx V.
$$

The controller drives the measured output toward its reference by moving the physical output against the sensor error. A small measured error can therefore coexist with a physical tracking error approximately equal to the sensor error.

This is especially clear for a constant sensor bias. Integral action can remove the controller's measured error while preserving the bias in the true output. The final-value calculation below makes that statement exact.

### Separating requirements across frequency

When reference changes and important disturbances occupy lower frequencies than sensor noise, the usual design aim is

$$
\lvert L(j\omega)\rvert\gg1
\quad\text{in the tracking band},
$$

and

$$
\lvert L(j\omega)\rvert\ll1
\quad\text{in the noise-rejection band}.
$$

The corresponding approximations follow from the definitions:

| Loop magnitude | Sensitivity | Complementary sensitivity | Intended benefit |
|---|---|---|---|
| $$\lvert L\rvert\gg1$$ | $$\mathcal{S}\approx1/L$$ | $$\mathcal{T}\approx1$$ | Tracking and relative disturbance attenuation |
| $$\lvert L\rvert\ll1$$ | $$\mathcal{S}\approx1$$ | $$\mathcal{T}\approx L$$ | Sensor-noise attenuation |

For plant-input disturbances, also inspect $$G\mathcal{S}$$. For actuator effort, inspect $$D\mathcal{S}$$.

Frequency separation does not defeat the identity. It places different objectives in different frequency ranges. Overlap, transition-band amplification, and stability still constrain the design.

### Feedback changes poles through the characteristic equation

Write

$$
G=\frac{B_G}{A_G},
\qquad
D=\frac{B_D}{A_D}.
$$

Then

$$
1+DG
=
\frac{A_DA_G+B_DB_G}{A_DA_G}.
$$

The closed-loop characteristic polynomial is therefore

$$
\boxed{
P_{\mathrm{cl}}=A_DA_G+B_DB_G
}
$$

for the corresponding well-defined interconnection, retaining internal factors when assessing internal stability.

The plant and controller coefficients both enter this polynomial. Feedback gives a way to change pole locations; it does not guarantee that they move into the LHP. The stable gain windows in the Routh–Hurwitz note are concrete examples of the resulting inequalities.

## Steady-state error

### Final value theorem: what must be checked first

For reference tracking alone, set

$$
W=V=0.
$$

Then true and measured errors coincide:

$$
E=E_m=\mathcal{S}R.
$$

The final value theorem gives

$$
\boxed{
e_{\mathrm{ss}}
=
\lim_{t\to\infty}e(t)
=
\lim_{s\to0}sE(s)
}
$$

provided the rational error transform has the required pole structure: **all poles of the reduced expression $$sE(s)$$ lie strictly in the open LHP**.

Why this condition? It means $$E$$ has at most a simple pole at the origin, with all its other poles strictly in the LHP. Its partial fractions have the form

$$
E(s)=\frac{c}{s}
+\sum_i\sum_{\ell=1}^{m_i}
\frac{c_{i,\ell}}{(s-p_i)^\ell},
\qquad
\operatorname{Re}(p_i)<0.
$$

Inverting,

$$
e(t)=c+
\sum_i\sum_{\ell=1}^{m_i}
c_{i,\ell}
\frac{t^{\ell-1}}{(\ell-1)!}e^{p_it}.
$$

Every term in the sum decays, leaving $$c$$. Multiplying the transform by $$s$$ and taking its limit at zero also gives $$c$$.

This is why a simple pole of $$E$$ at the origin is allowed, while a pole of $$sE$$ at the origin is not. A repeated origin pole in $$E$$ produces polynomial growth rather than a finite final value.

Closed-loop stability must be established, but it does not alone guarantee a finite error for every reference. A ramp or parabola can leave poles at the origin in the error transform even when all closed-loop natural modes are stable.

### Why polynomial references are written as $$t^k/k!$$

For integer $$k\ge0$$, consider

$$
r_k(t)=\frac{t^k}{k!},
\qquad t\ge0.
$$

Integration by parts gives

$$
I_k(s)=\int_0^\infty t^k e^{-st}\,dt
=\frac{k}{s}I_{k-1}(s),
$$

starting from

$$
I_0(s)=\frac1s.
$$

Repeated substitution yields

$$
I_k(s)=\frac{k!}{s^{k+1}}.
$$

Therefore,

$$
\boxed{
R_k(s)=\frac1{s^{k+1}}
}.
$$

The factorial normalisation removes an unnecessary coefficient:

| Reference | Time function | Transform |
|---|---|---|
| Unit step | $$1$$ | $$1/s$$ |
| Unit ramp | $$t$$ | $$1/s^2$$ |
| Normalised parabola | $$t^2/2$$ | $$1/s^3$$ |

### Deriving the error constants

With reference input only,

$$
E(s)=\frac{R(s)}{1+L(s)}.
$$

#### Step input

For $$R=1/s$$,

$$
sE(s)=\frac1{1+L(s)}.
$$

Define the position error constant

$$
K_p=\lim_{s\to0}L(s).
$$

When the final value theorem applies,

$$
\boxed{
e_{\mathrm{ss,step}}=\frac1{1+K_p}
}.
$$

If the loop gain tends to infinity at DC and the closed loop is stable, this limit is zero.

Here $$K_p$$ is an error constant, not necessarily the proportional controller gain.

#### Ramp input

For $$R=1/s^2$$,

$$
sE(s)=\frac1{s(1+L(s))}
=\frac1{s+sL(s)}.
$$

Define

$$
K_v=\lim_{s\to0}sL(s).
$$

If $$K_v$$ is finite and nonzero and the pole condition holds,

$$
\boxed{
e_{\mathrm{ss,ramp}}=\frac1{K_v}
}.
$$

A diverging $$sL(s)$$ can instead give zero error. If $$K_v=0$$, the finite-final-value condition must be examined; writing “$$1/0$$” is not a valid use of the theorem.

#### Parabolic input

For $$R=1/s^3$$,

$$
sE(s)=\frac1{s^2(1+L(s))}
=\frac1{s^2+s^2L(s)}.
$$

Define

$$
K_a=\lim_{s\to0}s^2L(s).
$$

Under the corresponding finite-value conditions,

$$
\boxed{
e_{\mathrm{ss,parabola}}=\frac1{K_a}
}.
$$

The factors of $$s$$ and $$s^2$$ in these definitions are not arbitrary: they come directly from multiplying the reference transform by $$s$$ in the final value calculation.

### Deriving the system-type triangle

The **system type** is the number of uncancelled poles at the origin in the loop transfer function. Write its low-frequency form as

$$
L(s)=\frac{A(s)}{s^n},
\qquad
A(0)=A_0\ne0,
$$

where $$A$$ is analytic near the origin.

For the reference $$t^k/k!$$,

$$
\begin{aligned}
E(s)
&=\frac1{1+A(s)/s^n}\frac1{s^{k+1}}\\
&=\frac{s^n}{s^n+A(s)}\frac1{s^{k+1}}\\
&=\frac{s^{n-k-1}}{s^n+A(s)}.
\end{aligned}
$$

First take $$n\ge1$$. Then

$$
sE(s)=\frac{s^{n-k}}{s^n+A(s)},
$$

and the denominator tends to $$A_0$$.

#### More integrators than reference order: $$n>k$$

The numerator tends to zero:

$$
\lim_{s\to0}sE(s)=0.
$$

With stable closed-loop dynamics and the final-value pole condition,

$$
\boxed{e_{\mathrm{ss}}=0\qquad(n>k)}.
$$

#### Equal integrator and reference orders: $$n=k\ge1$$

The numerator is one:

$$
sE(s)=\frac1{s^n+A(s)}.
$$

Therefore,

$$
\boxed{
e_{\mathrm{ss}}=\frac1{A_0}
\qquad(n=k\ge1)
}.
$$

This is the diagonal entry. For type 1, $$A_0=K_v$$; for type 2, $$A_0=K_a$$.

#### Too few integrators: $$n<k$$

Near the origin,

$$
E(s)\sim\frac1{A_0s^{k+1-n}}.
$$

Using the polynomial-reference transform just derived,

$$
\boxed{
e(t)\sim
\frac{t^{k-n}}{A_0(k-n)!}
\qquad(t\to\infty)
}.
$$

Lower-order polynomial terms and decaying transients can also be present, but the displayed term determines the growth.

This is not an application of the finite final value theorem: $$sE$$ retains a pole at the origin. The error is unbounded in magnitude.

### Why the type-0 step entry is different

For type 0,

$$
L(s)=A(s),
$$

so the sensitivity is

$$
\mathcal{S}(s)=\frac1{1+A(s)}.
$$

There is no diverging integrator term that makes the one negligible. For a step,

$$
sE(s)=\frac1{1+A(s)},
$$

and therefore

$$
\boxed{
e_{\mathrm{ss}}=\frac1{1+A_0}
=\frac1{1+K_p}
\qquad(n=k=0)
}.
$$

The asymmetry is exactly the difference between

$$
s^n+A(s)\longrightarrow A_0
\qquad(n\ge1)
$$

and

$$
1+A(s)\longrightarrow1+A_0
\qquad(n=0).
$$

For higher-order references in a type-0 loop,

$$
E(s)\sim
\frac1{(1+A_0)s^{k+1}},
$$

so

$$
e(t)\sim
\frac{t^k}{(1+A_0)k!}.
$$

Assuming stable closed-loop dynamics and the positive low-frequency constants used in the examples, the familiar table follows:

| System type | Step, $$k=0$$ | Ramp, $$k=1$$ | Parabola, $$k=2$$ |
|---|---|---|---|
| **Type 0** | $$1/(1+K_p)$$ | $$\infty$$ | $$\infty$$ |
| **Type 1** | $$0$$ | $$1/K_v$$ | $$\infty$$ |
| **Type 2** | $$0$$ | $$0$$ | $$1/K_a$$ |

Here $$\infty$$ denotes unbounded error magnitude. If a leading coefficient has a different sign, the direction of growth follows the derived polynomial term.

One additional integrator moves the first nonzero tracking-error case up by one polynomial order. The claim concerns the loop's uncancelled origin poles and presumes that the resulting closed loop remains stable.

### Worked example: proportional control of a first-order plant

Use the original plant

$$
G(s)=\frac{a}{\tau s+1},
\qquad a>0,\quad\tau>0,
$$

with proportional controller

$$
D(s)=k_1,
\qquad k_1>0.
$$

Then

$$
L(s)=\frac{ak_1}{\tau s+1},
$$

and

$$
\mathcal{S}(s)
=
\frac{\tau s+1}{\tau s+1+ak_1}.
$$

The closed-loop pole is

$$
p=-\frac{1+ak_1}{\tau}<0.
$$

There is no loop integrator, so this is type 0:

$$
K_p=\lim_{s\to0}L(s)=ak_1.
$$

For a unit step,

$$
E(s)=
\frac{\tau s+1}{s(\tau s+1+ak_1)}.
$$

The full error response can also be obtained by partial fractions. Define

$$
c=\frac{1+ak_1}{\tau}.
$$

Then

$$
E(s)=\frac{s+1/\tau}{s(s+c)}
=\frac{A}{s}+\frac{B}{s+c}.
$$

Matching numerators gives

$$
s+\frac1\tau=(A+B)s+Ac.
$$

Therefore,

$$
A+B=1,
\qquad
Ac=\frac1\tau,
$$

so

$$
A=\frac1{1+ak_1},
\qquad
B=\frac{ak_1}{1+ak_1}.
$$

Thus

$$
\boxed{
e(t)=
\frac1{1+ak_1}
+
\frac{ak_1}{1+ak_1}
e^{-(1+ak_1)t/\tau}
}.
$$

The steady-state error is the constant term:

$$
e_{\mathrm{ss}}=\frac1{1+ak_1}.
$$

For the original parameter values,

$$
a=1,\quad k_1=2:
\qquad
K_p=2,\quad
e_{\mathrm{ss}}=\frac13\approx0.333333,
$$

$$
a=2,\quad k_1=2:
\qquad
K_p=4,\quad
e_{\mathrm{ss}}=\frac15=0.200000.
$$

A higher proportional gain reduces the step error, but finite gain does not make it zero.

### Worked example: adding integral action

Use the same plant with the PI controller

$$
D(s)=k_1+\frac{k_2}{s}
=\frac{k_1s+k_2}{s},
\qquad k_1,k_2>0.
$$

The loop transfer function is

$$
L(s)=
\frac{a(k_1s+k_2)}{s(\tau s+1)}.
$$

The characteristic polynomial is

$$
\begin{aligned}
P_{\mathrm{cl}}(s)
&=s(\tau s+1)+a(k_1s+k_2)\\
&=\tau s^2+(1+ak_1)s+ak_2.
\end{aligned}
$$

Its quadratic Routh first column is

$$
\tau,\qquad 1+ak_1,\qquad ak_2,
$$

which is strictly positive under the stated assumptions. The closed loop is stable.

The sensitivity function is

$$
\mathcal{S}(s)
=
\frac{s(\tau s+1)}
{\tau s^2+(1+ak_1)s+ak_2}.
$$

There is one uncancelled loop integrator, so the system is type 1. Its velocity error constant is

$$
\begin{aligned}
K_v
&=\lim_{s\to0}sL(s)\\
&=\lim_{s\to0}
\frac{a(k_1s+k_2)}{\tau s+1}\\
&=ak_2.
\end{aligned}
$$

For a unit step,

$$
E_{\mathrm{step}}(s)
=
\frac{\tau s+1}
{\tau s^2+(1+ak_1)s+ak_2},
$$

so

$$
\lim_{s\to0}sE_{\mathrm{step}}(s)=0.
$$

For a unit ramp,

$$
E_{\mathrm{ramp}}(s)
=
\frac{\tau s+1}
{s[\tau s^2+(1+ak_1)s+ak_2]},
$$

so

$$
\lim_{s\to0}sE_{\mathrm{ramp}}(s)
=
\frac1{ak_2}.
$$

For the original values,

$$
a=1,\qquad k_1=2,\qquad k_2=2,
$$

this gives

$$
K_v=2,
\qquad
e_{\mathrm{ss,ramp}}=\frac12=0.5,
\qquad
e_{\mathrm{ss,step}}=0.
$$

The original simulation records are reproduced unchanged:

```text
 P control on a/(tau s+1)  [TYPE 0]
   a=1 k1=2: Kp=2  1/(1+Kp)=0.333333  simulated=0.333333
   a=2 k1=2: Kp=4  1/(1+Kp)=0.200000  simulated=0.200000
 PI control on the same plant [TYPE 1]
   a=1 k1=2 k2=2: Kv=2  1/Kv=0.500000  ramp sim=0.500000  step sim=1.4e-14
```

The recorded step residual $$1.4e-14$$ is on the order of $$10^{-14}$$. The analytical step error is zero under the model assumptions; the residual belongs to the numerical calculation.

### System type describes reference tracking, not every disturbance path

The triangle was derived with $$W=V=0$$. It does not automatically classify the other transfer paths.

For constant inputs with transforms

$$
R=\frac{r_0}{s},
\qquad
W=\frac{w_0}{s},
\qquad
V=\frac{v_0}{s},
$$

apply the final value theorem to the full true-error expression:

$$
E=\mathcal{S}R-G\mathcal{S}W+\mathcal{T}V.
$$

When the relevant pole conditions hold,

$$
\boxed{
e_{\mathrm{ss}}
=
\mathcal{S}(0)r_0
-\left[\lim_{s\to0}G(s)\mathcal{S}(s)\right]w_0
+\mathcal{T}(0)v_0
}.
$$

The product limit is written explicitly because $$G(0)$$ may be unbounded even when $$G\mathcal{S}$$ has a finite DC limit.

For the measured error,

$$
\boxed{
e_{m,\mathrm{ss}}
=
\mathcal{S}(0)r_0
-\left[\lim_{s\to0}G(s)\mathcal{S}(s)\right]w_0
-\mathcal{S}(0)v_0
}.
$$

Two consequences follow.

**Sensor bias survives perfect measured tracking.** With a stable integrating loop, $$\mathcal{S}(0)=0$$ and $$\mathcal{T}(0)=1$$. If $$w_0=0$$,

$$
e_{m,\mathrm{ss}}=0,
\qquad
e_{\mathrm{ss}}=v_0,
\qquad
y_{\mathrm{ss}}=r_0-v_0.
$$

**An integrator in the plant need not reject a plant-input disturbance.** For example, take

$$
G(s)=\frac1s,
\qquad
D(s)=k,
\qquad k>0.
$$

Then

$$
L=\frac{k}{s},
\qquad
\mathcal{S}=\frac{s}{s+k},
\qquad
G\mathcal{S}=\frac1{s+k}.
$$

The loop is type 1 and has the stable closed-loop pole $$-k$$. It has zero step-reference error, but a constant plant-input disturbance produces

$$
e_{\mathrm{ss}}=-\frac{w_0}{k}
$$

when sensor noise is absent.

The injection point and the location of the integrator matter. Always derive the path for the signal whose rejection is being claimed.

### What integral action guarantees structurally

In the PI example, the zero step-reference error survives changes in the finite plant gain because

$$
\mathcal{S}(s)\to0
\qquad(s\to0)
$$

as long as the loop integrator remains uncancelled and the closed loop remains stable. The exact value of $$ak_2$$ changes the finite ramp error, but not the zero step-error result.

The corresponding open-loop claims must be separated:

- Exact tracking of arbitrary reference signals would require $$DG\equiv1$$, or an appropriate plant inverse.
- Zero steady-state error to a step only requires $$D(0)G(0)=1$$.

The second condition is less demanding than exact inversion. Indeed, for open loop with reference input only,

$$
E_{\mathrm{ol}}=(1-DG)R,
$$

so a step gives

$$
e_{\mathrm{ss,ol}}
=
[1-D(0)G(0)]r_0
$$

when the final value exists.

That DC matching can be achieved nominally, but plant drift changes the match. Integral feedback obtains the step-tracking result through the loop's low-frequency structure instead. This guarantee belongs to the stable linear model with the stated signal locations; it does not imply rejection of sensor bias or preservation under actuator saturation.

### Revision checklist

| Question | Calculation to reproduce | Assumption or common mistake |
|---|---|---|
| Where do disturbance and noise enter? | Write $$Y=G(U+W)$$ and $$M=Y+V$$ | Moving an injection point changes its transfer path |
| What error does the controller see? | $$E_m=R-Y-V$$ | It differs from true error $$E=R-Y$$ |
| How do I obtain each output path? | Expand $$Y=G[D(R-Y-V)+W]$$ | Set other independent inputs to zero when naming a path |
| Why does $$\mathcal{S}+\mathcal{T}=1$$? | Add their common-denominator definitions | Structural identity, not a stability or tuning result |
| Do the magnitudes sum to one? | Apply the triangle inequality | The identity is a complex sum |
| What is disturbance attenuation? | Compare $$G\mathcal{S}$$ with open-loop $$G$$ | Absolute transmission is $$G\mathcal{S}$$ |
| Why is relative plant sensitivity $$\mathcal{S}$$? | Differentiate $$DG/(1+DG)$$ and multiply by $$G/\mathcal{T}$$ | Controller and evaluation point are fixed |
| What changes for a finite perturbation? | Use $$\mathcal{S}\delta/(1+\mathcal{T}\delta)$$ | Differential sensitivity omits the additional denominator |
| When may I use the final value theorem? | Inspect the poles of the reduced $$sE(s)$$ | They must all lie strictly in the open LHP |
| Why these error constants? | Insert step, ramp, and parabolic transforms into $$sE$$ | The powers of $$s$$ come from the reference |
| What is system type? | Count uncancelled origin poles in $$L=DG$$ | It is not the number of closed-loop origin poles |
| Why is the diagonal $$1/A_0$$? | Evaluate $$s^{n-k}/[s^n+A(s)]$$ for $$n=k\ge1$$ | Type-0 step is the exception |
| Why is type-0 step error $$1/(1+K_p)$$? | Retain the one in $$1+L(0)$$ | Finite DC gain does not dominate the one exactly |
| How do I justify an infinite-error entry? | Invert the leading pole at the origin | Do not use a finite-value theorem when its condition fails |
| Does zero measured error prove correct output? | Compare the noise terms in $$E$$ and $$E_m$$ | Constant sensor bias can remain in true error |
| Does type determine disturbance rejection? | Examine $$G\mathcal{S}$$ or the appropriate disturbance path | The type triangle was derived for reference input alone |

## Why it matters for my work

The useful habit is to name the measured quantity and the true quantity separately before claiming that a correction loop is working. Reducing a measurement residual is not the same as reducing every physical error.

A second habit is to distinguish a structural identity, a local sensitivity, and a finite-perturbation guarantee. They answer different questions even when they share the same algebra.

## What I have not resolved

I want to formulate the design problem when reference, disturbance, and sensor-noise spectra overlap, including the cost of controller effort. I also want to understand which analogous limitations can be stated for nonlinear feedback without treating nonlinear operators as scalar transfer functions.

---

Sources: Ajou University lecture notes and the standard classical-control treatment in Franklin, Powell, and Emami-Naeini, Feedback Control of Dynamic Systems. The loop transfer paths, sensitivity identity, relative-sensitivity derivatives, final-value conditions, error constants, and system-type classification are derived above. The original numerical records are retained: checks of the sensitivity identity at complex operating points, numerical differentiation of open- and closed-loop relative sensitivity, and the proportional/PI step- and ramp-error simulations. New calculations are symbolic; the finite-perturbation example is kept in exact fractional form, and no new simulation results are claimed.
