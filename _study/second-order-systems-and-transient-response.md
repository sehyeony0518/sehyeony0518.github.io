---
layout: study_note
title: "Second-Order Systems: Four Numbers You Can Ask For, and Where They Put the Poles"
description: "Rise time, overshoot, peak time and settling time are not four independent wishes: each one carves a region out of the complex plane, and the design is whatever survives the intersection."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "feedback-control"
category_title: "Feedback Control & Classical Design"
subgroup: "Transient Response & Stability"
order: 3
source: "Lecture notes, Ajou University"
written: true
updated: "2026-09-15"
---

A specification arrives in time-domain language: *rise in under 0.6 seconds, overshoot no more than 10%, settle within 3 seconds.* A design places poles in the complex plane. Second-order analysis connects these descriptions.

The connection has two levels. Peak time and overshoot follow exactly from the standard underdamped step response. Common rise-time and settling-time rules simplify that response, so their geometric design regions are preliminary estimates. A useful study habit is to carry the assumptions alongside each formula.

## Core question and definition

**How do the poles of a second-order system determine its step response, and how do response specifications restrict the pole locations?**

Start with the standard form

$$
H(s)=\frac{\omega_n^2}
{s^2+2\zeta\omega_n s+\omega_n^2},
\qquad \omega_n>0.
$$

The numerator makes the DC gain unity:

$$
H(0)=\frac{\omega_n^2}{\omega_n^2}=1.
$$

This note derives the response to a **unit step with zero initial conditions**. The main formulas assume

$$
0<\zeta<1,
$$

so the poles are a stable complex-conjugate pair. A different numerator, extra poles, or nonzero initial conditions can change the response even if the denominator contains the same pair.

### Deriving the pole coordinates

Set the denominator to zero and apply the quadratic formula:

$$
\begin{aligned}
s
&=\frac{-2\zeta\omega_n
\pm\sqrt{(2\zeta\omega_n)^2-4\omega_n^2}}{2}\\
&=-\zeta\omega_n
\pm\omega_n\sqrt{\zeta^2-1}.
\end{aligned}
$$

For the underdamped case,

$$
\sqrt{\zeta^2-1}=j\sqrt{1-\zeta^2}.
$$

Define

$$
\sigma=\zeta\omega_n,
\qquad
\omega_d=\omega_n\sqrt{1-\zeta^2}.
$$

Then

$$
\boxed{p_\pm=-\sigma\pm j\omega_d}.
$$

The definitions also give

$$
\begin{aligned}
\sigma^2+\omega_d^2
&=\zeta^2\omega_n^2+\omega_n^2(1-\zeta^2)\\
&=\omega_n^2.
\end{aligned}
$$

Thus the distance from either pole to the origin is

$$
\lvert p_\pm\rvert
=\sqrt{\sigma^2+\omega_d^2}
=\omega_n.
$$

### Why the damping ratio is the cosine of the pole angle

Use the upper pole $$p_+=-\sigma+j\omega_d$$. Let $$\theta$$ be the angle between its position vector and the negative real axis.

The right triangle has adjacent side $$\sigma$$, opposite side $$\omega_d$$, and hypotenuse $$\omega_n$$. Therefore,

$$
\cos\theta=\frac{\sigma}{\omega_n}
=\frac{\zeta\omega_n}{\omega_n}
=\zeta,
$$

and

$$
\sin\theta=\frac{\omega_d}{\omega_n}
=\sqrt{1-\zeta^2}.
$$

Hence

$$
\boxed{\zeta=\cos\theta},
\qquad
\boxed{\theta=\arccos\zeta}.
$$

The damping ratio is not literally an angle: it is the angle's cosine. Fixed damping means a fixed ray from the origin.

The original numerical check recorded a pole angle of $$45.01^\circ$$ at $$\zeta=0.707$$. At exactly $$45^\circ$$,

$$
\cos45^\circ=\frac{1}{\sqrt2}\approx0.707.
$$

The distinction between the exact value and its rounded decimal will matter when simplifying the overshoot formula.

| Quantity | Pole geometry | Time-domain role |
|---|---|---|
| $$\omega_n$$ | Distance from the origin | Sets the time scale at fixed damping |
| $$\sigma=\zeta\omega_n$$ | Distance left of the imaginary axis | Exponential decay rate |
| $$\omega_d$$ | Distance above or below the real axis | Oscillation frequency |
| $$\zeta=\cos\theta$$ | Cosine of angle from the negative real axis | Determines the response shape after normalizing time |

## Key concepts

### Deriving the step response by partial fractions

For a unit step,

$$
X(s)=\frac1s.
$$

Thus

$$
Y(s)=
\frac{\omega_n^2}
{s(s^2+2\zeta\omega_n s+\omega_n^2)}.
$$

Set up the partial fractions without skipping the numerator of the quadratic term:

$$
Y(s)=\frac{A}{s}
+\frac{Bs+C}{s^2+2\zeta\omega_n s+\omega_n^2}.
$$

Multiply by the common denominator:

$$
\begin{aligned}
\omega_n^2
&=A(s^2+2\zeta\omega_n s+\omega_n^2)
+s(Bs+C)\\
&=(A+B)s^2+(2A\zeta\omega_n+C)s+A\omega_n^2.
\end{aligned}
$$

Matching coefficients of equal powers of $$s$$ gives

$$
A+B=0,
\qquad
2A\zeta\omega_n+C=0,
\qquad
A\omega_n^2=\omega_n^2.
$$

Since $$\omega_n>0$$,

$$
A=1,\qquad B=-1,\qquad C=-2\zeta\omega_n.
$$

Therefore,

$$
Y(s)=\frac1s
-\frac{s+2\zeta\omega_n}
{s^2+2\zeta\omega_n s+\omega_n^2}.
$$

Now complete the square:

$$
\begin{aligned}
s^2+2\zeta\omega_n s+\omega_n^2
&=s^2+2\zeta\omega_n s+\zeta^2\omega_n^2
+\omega_n^2-\zeta^2\omega_n^2\\
&=(s+\zeta\omega_n)^2+\omega_n^2(1-\zeta^2)\\
&=(s+\sigma)^2+\omega_d^2.
\end{aligned}
$$

The numerator must be rewritten around the same shift:

$$
s+2\zeta\omega_n=(s+\sigma)+\sigma.
$$

Consequently,

$$
Y(s)=
\frac1s
-\frac{s+\sigma}{(s+\sigma)^2+\omega_d^2}
-\frac{\sigma}{(s+\sigma)^2+\omega_d^2}.
$$

To identify the inverse transforms, start from

$$
\int_0^\infty e^{-(s+\sigma)t}e^{j\omega_dt}\,dt
=
\frac{1}{s+\sigma-j\omega_d}
=
\frac{s+\sigma+j\omega_d}
{(s+\sigma)^2+\omega_d^2}.
$$

Taking real and imaginary parts gives the transform pairs

$$
\mathcal{L}\{e^{-\sigma t}\cos\omega_dt\}
=
\frac{s+\sigma}{(s+\sigma)^2+\omega_d^2},
$$

$$
\mathcal{L}\{e^{-\sigma t}\sin\omega_dt\}
=
\frac{\omega_d}{(s+\sigma)^2+\omega_d^2}.
$$

The last partial-fraction term therefore needs the coefficient $$\sigma/\omega_d$$. Inverting,

$$
\boxed{
y(t)=1-e^{-\sigma t}
\left(
\cos\omega_dt+\frac{\sigma}{\omega_d}\sin\omega_dt
\right)
},
\qquad t\ge0.
$$

Substituting the definitions gives the equivalent standard form:

$$
\boxed{
y(t)=
1-e^{-\zeta\omega_nt}
\left[
\cos\!\left(\omega_n\sqrt{1-\zeta^2}\,t\right)
+
\frac{\zeta}{\sqrt{1-\zeta^2}}
\sin\!\left(\omega_n\sqrt{1-\zeta^2}\,t\right)
\right]
}.
$$

Two immediate checks are

$$
y(0)=1-1=0
$$

and, because $$\sigma>0$$,

$$
\lim_{t\to\infty}y(t)=1.
$$

These verify the initial output and unit final value.

### Differentiating the response without losing the cancellation

Define

$$
f(t)=\cos\omega_dt+\frac{\sigma}{\omega_d}\sin\omega_dt.
$$

Then

$$
y(t)=1-e^{-\sigma t}f(t),
$$

so the product rule gives

$$
\dot y(t)=e^{-\sigma t}\left[\sigma f(t)-\dot f(t)\right].
$$

Differentiate the bracket:

$$
\dot f(t)
=-\omega_d\sin\omega_dt+\sigma\cos\omega_dt.
$$

Substitute both expressions:

$$
\begin{aligned}
\dot y(t)
&=e^{-\sigma t}
\left[
\sigma\cos\omega_dt
+\frac{\sigma^2}{\omega_d}\sin\omega_dt
+\omega_d\sin\omega_dt
-\sigma\cos\omega_dt
\right]\\
&=e^{-\sigma t}
\left(\frac{\sigma^2+\omega_d^2}{\omega_d}\right)
\sin\omega_dt\\
&=\frac{\omega_n^2}{\omega_d}
e^{-\sigma t}\sin\omega_dt.
\end{aligned}
$$

Thus

$$
\boxed{
\dot y(t)=
\frac{\omega_n^2}{\omega_d}
e^{-\sigma t}\sin\omega_dt
}.
$$

The cosine terms cancel exactly. This cancellation is why the peak-time calculation becomes simple.

It also checks the initial slope:

$$
\dot y(0)=0,
$$

as required by the zero-initial-condition second-order equation.

### Stationary points, peak time, and overshoot

For finite time, the prefactor in the derivative is positive:

$$
\frac{\omega_n^2}{\omega_d}e^{-\sigma t}>0.
$$

Therefore,

$$
\dot y(t)=0
\quad\Longleftrightarrow\quad
\sin\omega_dt=0.
$$

The stationary times are

$$
\omega_dt=k\pi,
$$

or

$$
\boxed{t_k=\frac{k\pi}{\omega_d}},
\qquad k=0,1,2,\ldots.
$$

The point $$k=0$$ is the initial endpoint. On the interval

$$
0<t<\frac{\pi}{\omega_d},
$$

the sine is positive, so the response increases. Immediately after $$\pi/\omega_d$$, the sine is negative, so the response decreases. The first positive stationary point is therefore a maximum:

$$
\boxed{t_p=\frac{\pi}{\omega_d}}.
$$

For an additional classification check, differentiate once more:

$$
\ddot y(t)=
\frac{\omega_n^2}{\omega_d}e^{-\sigma t}
\left[
\omega_d\cos\omega_dt-\sigma\sin\omega_dt
\right].
$$

At a stationary time,

$$
\ddot y(t_k)
=\omega_n^2e^{-\sigma t_k}(-1)^k.
$$

Odd $$k$$ gives a maximum; positive even $$k$$ gives a minimum.

Now substitute $$t_k$$ into the response itself:

$$
\begin{aligned}
y(t_k)
&=1-e^{-\sigma k\pi/\omega_d}
\left[
\cos(k\pi)+\frac{\sigma}{\omega_d}\sin(k\pi)
\right]\\
&=1-(-1)^k e^{-\sigma k\pi/\omega_d}.
\end{aligned}
$$

At the first maximum,

$$
y(t_p)=1+e^{-\sigma\pi/\omega_d}.
$$

Define fractional overshoot relative to the final value:

$$
M_p=\frac{y(t_p)-y(\infty)}{y(\infty)}.
$$

Because $$y(\infty)=1$$,

$$
M_p=e^{-\sigma\pi/\omega_d}.
$$

Finally,

$$
\frac{\sigma}{\omega_d}
=
\frac{\zeta\omega_n}{\omega_n\sqrt{1-\zeta^2}}
=
\frac{\zeta}{\sqrt{1-\zeta^2}},
$$

so

$$
\boxed{
M_p=
\exp\!\left(
-\frac{\zeta\pi}{\sqrt{1-\zeta^2}}
\right)
}.
$$

Percentage overshoot is $$100M_p\%$$. Later maxima have larger positive odd $$k$$ and smaller exponential factors, so the first maximum is the largest.

Two design consequences follow directly:

- At fixed damping, increasing $$\omega_n$$ decreases peak time.
- Overshoot depends on $$\zeta$$ alone because $$\omega_n$$ cancels from the exponent.

### The exact identity behind the rounded value 0.707

The convenient simplification is

$$
\frac{\zeta}{\sqrt{1-\zeta^2}}=1.
$$

Since both sides are positive in the underdamped range, square and solve:

$$
\zeta^2=1-\zeta^2,
\qquad
2\zeta^2=1,
\qquad
\zeta=\frac1{\sqrt2}.
$$

Therefore,

$$
\boxed{
\zeta=\frac1{\sqrt2}
\quad\Longrightarrow\quad
M_p=\exp(-\pi)
}.
$$

The original note's “$$\zeta=0.707\ \to\ \exp(-\pi)$$” is shorthand for this exact identity. The decimal $$0.707$$ is a rounded representation of $$1/\sqrt2$$; taken literally, it does not make the ratio exactly one.

Preserving the recorded values,

$$
\exp(-\pi)\approx0.04321,
$$

or approximately $$4.3\%$$ overshoot. The simulation table below instead uses the literal value $$\zeta=0.707$$ and records $$0.04325$$. These statements are consistent once the rounding is made explicit.

### Deriving the settling-time envelope

Define the error relative to the final value:

$$
e(t)=1-y(t)
=e^{-\sigma t}
\left(
\cos\omega_dt+\frac{\sigma}{\omega_d}\sin\omega_dt
\right).
$$

To combine the two trigonometric terms, write

$$
\cos u+a\sin u=R\cos(u-\phi).
$$

Expanding the right-hand side,

$$
R\cos(u-\phi)
=R\cos\phi\cos u+R\sin\phi\sin u.
$$

Coefficient matching requires

$$
R\cos\phi=1,\qquad R\sin\phi=a.
$$

Squaring and adding,

$$
R^2=1+a^2.
$$

Here $$a=\sigma/\omega_d$$, so

$$
\begin{aligned}
R
&=\sqrt{1+\frac{\sigma^2}{\omega_d^2}}\\
&=\frac{\sqrt{\omega_d^2+\sigma^2}}{\omega_d}\\
&=\frac{\omega_n}{\omega_d}\\
&=\frac1{\sqrt{1-\zeta^2}}.
\end{aligned}
$$

Hence the error can be written

$$
e(t)=
\frac{e^{-\sigma t}}{\sqrt{1-\zeta^2}}
\cos(\omega_dt-\phi),
$$

where

$$
\cos\phi=\frac{\omega_d}{\omega_n},
\qquad
\sin\phi=\frac{\sigma}{\omega_n}.
$$

Because the absolute value of cosine cannot exceed one,

$$
\boxed{
\lvert e(t)\rvert
\le
\frac{e^{-\sigma t}}{\sqrt{1-\zeta^2}}
}.
$$

This is the exponential envelope.

For a relative tolerance $$0<\delta<1$$, define the actual settling time as the earliest time after which the response stays in the band:

$$
t_s(\delta)=
\inf\left\{
t:\lvert e(u)\rvert\le\delta
\text{ for every }u\ge t
\right\}.
$$

A sufficient condition is that the envelope has entered the band:

$$
\frac{e^{-\sigma t}}{\sqrt{1-\zeta^2}}\le\delta.
$$

Solve this inequality step by step:

$$
e^{-\sigma t}\le\delta\sqrt{1-\zeta^2},
$$

$$
-\sigma t
\le
\ln\delta+\frac12\ln(1-\zeta^2),
$$

$$
\sigma t
\ge
\ln\frac1\delta-\frac12\ln(1-\zeta^2).
$$

Define the envelope time

$$
\boxed{
t_{\mathrm{env}}(\delta)
=
\frac{
\ln(1/\delta)-\frac12\ln(1-\zeta^2)
}{\sigma}
}.
$$

The envelope decreases monotonically, so

$$
\boxed{t_s(\delta)\le t_{\mathrm{env}}(\delta)}.
$$

The equality need not hold. The actual error contains a cosine factor and may make its last band crossing earlier than the envelope does.

### Where 4.6 and 3.9 come from

If the damping-dependent prefactor is omitted, the simplified condition is

$$
e^{-\sigma t}\approx\delta,
$$

which gives

$$
t\approx\frac{\ln(1/\delta)}{\sigma}.
$$

For a 1% band,

$$
\delta=\frac1{100},
\qquad
\ln(1/\delta)=\ln100\approx4.6.
$$

For a 2% band,

$$
\delta=\frac1{50},
\qquad
\ln(1/\delta)=\ln50\approx3.9.
$$

These produce the familiar estimates

$$
t_s(1\%)\approx\frac{4.6}{\sigma},
\qquad
t_s(2\%)\approx\frac{3.9}{\sigma}.
$$

There are two approximations here: omitting the factor $$1/\sqrt{1-\zeta^2}$$ and rounding the logarithm. The omitted correction is

$$
-\frac{\ln(1-\zeta^2)}{2\sigma}>0.
$$

Therefore, the simplified formulas are **not guaranteed envelope bounds**. The full logarithmic expression is the bound; the actual settling time is a last-crossing calculation.

Near critical damping, the envelope prefactor becomes large even though the actual response remains well behaved. The bound can become conservative because it treats the sinusoid's amplitude independently of the cancellation occurring in the response.

### Rise time: exact scaling, fitted coefficient

Use the **10%–90% rise time**:

$$
t_r=t_{90}-t_{10},
$$

where each time is the first crossing of the corresponding fraction of the final value. This differs from a 0%–100% rise-time definition.

Introduce dimensionless time and a damping-dependent factor:

$$
q=\omega_nt,
\qquad
\beta=\sqrt{1-\zeta^2}.
$$

The exact response becomes

$$
y(q)=
1-e^{-\zeta q}
\left[
\cos(\beta q)+\frac{\zeta}{\beta}\sin(\beta q)
\right].
$$

For a crossing level $$\alpha$$, the first crossing $$q_\alpha$$ solves

$$
e^{-\zeta q_\alpha}
\left[
\cos(\beta q_\alpha)
+\frac{\zeta}{\beta}\sin(\beta q_\alpha)
\right]
=1-\alpha.
$$

Use $$\alpha=1/10$$ and $$\alpha=9/10$$. Returning to dimensional time,

$$
t_{10}=\frac{q_{1/10}}{\omega_n},
\qquad
t_{90}=\frac{q_{9/10}}{\omega_n}.
$$

Therefore,

$$
\boxed{
t_r=
\frac{r(\zeta)}{\omega_n},
\qquad
r(\zeta)=q_{9/10}-q_{1/10}
}.
$$

The inverse dependence on $$\omega_n$$ is exact at fixed damping. The coefficient $$r(\zeta)$$ is not constant: it comes from two transcendental crossing equations.

The rule

$$
\boxed{t_r\approx\frac{1.8}{\omega_n}}
$$

replaces that damping-dependent coefficient by a representative fitted value. Plotted against $$1/\omega_n$$, it is a straight line with slope $$1.8$$. It is not a theorem that the same slope works at every damping ratio.

For these notes, use it as a rough initial estimate in the moderate-damping neighborhood represented by $$\zeta=0.500$$ through $$0.707$$ in the original table. Those endpoint checks do not establish a uniform error bound throughout the interval, and the rule should not be extrapolated toward zero or critical damping without checking the crossing equations.

### Preserved numerical checks: exact formulas versus estimates

The original simulation table is reproduced unchanged:

```text
 zeta   Mp formula  Mp measured   tp formula   tp measured   tr 1.8/wn   tr measured
0.500      0.16303      0.16303       3.6276        3.6276      1.8000        1.6376
0.707      0.04325      0.04325       4.4422        4.4422      1.8000        2.1477
```

These are the normalized-frequency checks with $$\omega_n=1$$. Peak time and overshoot agree to the displayed precision because their formulas are exact for the assumed model.

The rise-time estimate is larger than the measured value in the first row and smaller in the second. The original description, “roughly $$\pm20\%$$,” is a rough summary of these discrepancies, not a guaranteed tolerance for the rule.

The original settling-time check is also retained: at $$\zeta=0.70$$ and $$\sigma=0.700$$, the simplified formula gives $$6.571$$ and the simulation gives $$6.575$$. Their closeness in this example does not turn the simplified expression into an exact last-crossing formula.

| Specification | Expression | Status |
|---|---|---|
| Peak time | $$\pi/\omega_d$$ | Exact for the standard underdamped unit-step response |
| Fractional overshoot | $$\exp[-\zeta\pi/\sqrt{1-\zeta^2}]$$ | Exact under the same assumptions |
| Settling envelope time | $$[\ln(1/\delta)-\frac12\ln(1-\zeta^2)]/\sigma$$ | Sufficient upper bound on actual settling time |
| Settling time, 1% | $$4.6/\sigma$$ | Simplified estimate |
| Settling time, 2% | $$3.9/\sigma$$ | Simplified estimate |
| 10%–90% rise time | $$r(\zeta)/\omega_n$$ | Exact scaling; crossing equations determine $$r$$ |
| 10%–90% rise time | $$1.8/\omega_n$$ | Fitted approximation |

### Each specification becomes an inequality on pole location

Write a pole as

$$
p=x+jy,
\qquad
x=-\sigma,\qquad
\lvert y\rvert=\omega_d.
$$

Then

$$
\omega_n=\sqrt{x^2+y^2},
\qquad
\zeta=\frac{-x}{\sqrt{x^2+y^2}}.
$$

#### Rise time gives an approximate circle

Using the fitted rule,

$$
t_r\le T_r
\quad\leadsto\quad
\frac{1.8}{\omega_n}\le T_r.
$$

Since the quantities are positive,

$$
\omega_n\ge\frac{1.8}{T_r},
$$

or

$$
\boxed{
x^2+y^2\ge\left(\frac{1.8}{T_r}\right)^2
}.
$$

This is the exterior of a circle centred at the origin.

The exact condition instead uses $$r(\zeta)$$:

$$
\omega_n\ge\frac{r(\zeta)}{T_r}.
$$

Because that coefficient varies with the pole angle, the exact rise-time boundary is not generally one circle.

#### Overshoot gives an exact damping wedge

Let the maximum allowed fractional overshoot be $$0<m<1$$. Starting from

$$
\exp\!\left(
-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}
\right)\le m,
$$

take logarithms:

$$
-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}\le\ln m.
$$

Set $$\ell=-\ln m>0$$ and reverse the inequality when multiplying by minus one:

$$
\frac{\pi\zeta}{\sqrt{1-\zeta^2}}\ge\ell.
$$

Both sides are nonnegative, so squaring preserves the inequality:

$$
\frac{\pi^2\zeta^2}{1-\zeta^2}\ge\ell^2.
$$

Multiply by the positive denominator and rearrange:

$$
\pi^2\zeta^2\ge\ell^2-\ell^2\zeta^2,
$$

$$
(\pi^2+\ell^2)\zeta^2\ge\ell^2.
$$

Thus

$$
\boxed{
\zeta\ge\zeta_{\min}
=
\frac{\ell}{\sqrt{\pi^2+\ell^2}}
}.
$$

Using $$\zeta=\cos\theta$$,

$$
\boxed{\theta\le\arccos\zeta_{\min}}.
$$

For both conjugate poles, this is a wedge around the negative real axis. In coordinates it is

$$
\lvert y\rvert
\le
(-x)\frac{\sqrt{1-\zeta_{\min}^2}}{\zeta_{\min}},
\qquad x<0.
$$

#### Settling time gives an approximate half-plane

For the 1% simplified estimate,

$$
t_s\le T_s
\quad\leadsto\quad
\frac{4.6}{\sigma}\le T_s.
$$

Therefore,

$$
\sigma\ge\frac{4.6}{T_s},
$$

or

$$
\boxed{x\le-\frac{4.6}{T_s}}.
$$

The pole must lie left of a vertical line.

For a guaranteed envelope condition, retain the full expression:

$$
\boxed{
\sigma\ge
\frac{
\ln(1/\delta)-\frac12\ln(1-\zeta^2)
}{T_s}
}.
$$

At a fixed damping ratio this is again a bound on the real part. Across varying damping ratios, its boundary depends on $$\zeta$$ and is not one vertical line.

### Worked specification: rise, overshoot, and settling together

Use the original requirements:

$$
t_r\le0.6,
\qquad
M_p\le10\%,
\qquad
t_s(1\%)\le3.
$$

The approximate rise-time condition is

$$
\omega_n\ge\frac{1.8}{0.6}=3.
$$

For overshoot, use $$m=1/10$$, so $$\ell=\ln10$$:
$$
\zeta_{\min}
=
\frac{\ln10}{\sqrt{\pi^2+(\ln10)^2}}
\approx0.5912.
$$

The recorded decimal $$0.5912$$ is the rounded value of this exact expression. Its wedge half-angle is

$$
\arccos(0.5912)\approx53.7^\circ.
$$

The simplified settling condition gives

$$
\sigma\ge\frac{4.6}{3}\approx1.5333.
$$

Thus the preliminary sketch is:

- Outside the circle of radius $$3$$.
- Inside the damping wedge with half-angle approximately $$53.7^\circ$$.
- Left of $$x=-1.5333$$, also recorded in rounded form as the boundary $$\sigma=1.533$$.

These three regions combine an exact overshoot condition with approximate rise and settling conditions.

#### Carrying the original candidate through the algebra

Choose the original candidate

$$
\zeta=0.6=\frac35,
\qquad
\omega_n=3.
$$

Then

$$
\sqrt{1-\zeta^2}
=
\sqrt{1-\frac9{25}}
=
\frac45,
$$

$$
\sigma=\zeta\omega_n
=\frac35\cdot3
=\frac95
=1.8,
$$

and

$$
\omega_d
=3\cdot\frac45
=\frac{12}{5}.
$$

Its poles are therefore exactly

$$
p_\pm=-\frac95\pm j\frac{12}{5}.
$$

The exact overshoot is

$$
\begin{aligned}
M_p
&=\exp\!\left(
-\pi\frac{3/5}{4/5}
\right)\\
&=\exp\!\left(-\frac{3\pi}{4}\right)
\approx0.0948.
\end{aligned}
$$

The original fitted response values are retained:

$$
t_r\approx\frac{1.8}{3}=0.600,
$$

$$
t_s(1\%)\approx\frac{4.6}{1.8}\approx2.556.
$$

The candidate passes the overshoot requirement and the preliminary geometric screen. Its rise-time estimate sits exactly on the requested limit, so the fit provides no allowance for its own error.

#### Checking settling with the full envelope

For this candidate,

$$
\frac1{\sqrt{1-\zeta^2}}=\frac54,
$$

so

$$
\lvert e(t)\rvert\le\frac54e^{-9t/5}.
$$

Requiring the envelope to be no larger than $$1/100$$ gives

$$
\frac54e^{-9t/5}\le\frac1{100},
$$

$$
e^{-9t/5}\le\frac1{125},
$$

and hence

$$
\boxed{t_{\mathrm{env}}(1\%)=\frac59\ln125}.
$$

This bound is below the required time of $$3$$. That comparison can be established without introducing a new decimal approximation. The positive-term exponential series gives

$$
e^{9/5}
>
1+\frac95+\frac{(9/5)^2}{2}+\frac{(9/5)^3}{6}
=
\frac{674}{125}
>
5.
$$

Thus

$$
\ln5<\frac95.
$$

Since $$125=5^3$$,

$$
\frac59\ln125
=
\frac53\ln5
<
\frac53\cdot\frac95
=
3.
$$

The full envelope therefore certifies the settling requirement for the standard second-order candidate.

#### What remains to check for rise time

The candidate's exact response is

$$
y(t)=
1-e^{-9t/5}
\left[
\cos\left(\frac{12t}{5}\right)
+\frac34\sin\left(\frac{12t}{5}\right)
\right].
$$

The first 10% crossing solves

$$
e^{-9t_{10}/5}
\left[
\cos\left(\frac{12t_{10}}5\right)
+\frac34\sin\left(\frac{12t_{10}}5\right)
\right]
=
\frac9{10},
$$

and the first 90% crossing solves

$$
e^{-9t_{90}/5}
\left[
\cos\left(\frac{12t_{90}}5\right)
+\frac34\sin\left(\frac{12t_{90}}5\right)
\right]
=
\frac1{10}.
$$

Only after those crossings are found can the actual requirement

$$
t_{90}-t_{10}\le0.6
$$

be decided.

Solving those two crossing equations numerically settles it, and the answer is not the one the fit predicted:

$$
t_{10}=0.1103,\qquad t_{90}=0.7283,\qquad t_{90}-t_{10}=0.6180 .
$$

**The candidate fails.** The requirement was $$t_r\le0.6$$ and the true rise time is $$0.6180$$: over by 3%. The fit $$1.8/\omega_n$$ returned exactly $$0.600$$ and so reported the candidate as sitting precisely on the limit, when in fact it sits outside it.

This is the note's own distinction biting in the only place it could do real damage. $$M_p$$ and $$t_p$$ are exact, so a design checked against them is safe; $$t_r\approx1.8/\omega_n$$ is a fitted coefficient, and here it is optimistic by about 3%. Measuring the true scaling at $$\zeta=0.6$$ gives

$$
t_r\,\omega_n = 1.8541 \quad\Longrightarrow\quad t_r\le0.6 \iff \omega_n\ge 3.0901 ,
$$

against the $$\omega_n\ge3$$ that the fit claimed. Taking $$\omega_n=3.1$$ restores a design that genuinely meets all three:

| $$\omega_n$$ | $$t_r$$ (measured) | $$M_p$$ | $$t_s(1\%)$$ envelope | verdict |
|---|---|---|---|---|
| 3.00 | 0.6180 | 0.0948 | 2.6824 | **fails** $$t_r$$ |
| 3.09 | 0.6000 | 0.0948 | 2.6043 | on the boundary |
| 3.10 | 0.5981 | 0.0948 | 2.5959 | meets all three |

The practical rule: never design onto the boundary of a specification using an approximate formula. Leave margin equal to at least the approximation's error, or check the exact crossing.

Rounding the damping requirement upward to $$\zeta\ge0.6$$ is conservative for overshoot because it exceeds the recorded threshold $$0.5912$$. It does not automatically provide margin on rise time.

**The design is the intersection of the response constraints and the pole locations the actual plant and controller can achieve.** Passing an approximate sketch is a reason to examine a candidate, not a substitute for checking its response.

### Block-diagram reduction from the loop equations

The second-order formulas apply to the resulting input–output transfer function, so derive that function before reading off its coefficients.

Let $$R$$ be the reference, $$E$$ the signal entering the forward block, $$Y$$ the output, and $$G_2Y$$ the returned measurement. For negative feedback,

$$
E=R-G_2Y,
\qquad
Y=G_1E.
$$

Substitute the first equation into the second:

$$
Y=G_1(R-G_2Y).
$$

Distribute:

$$
Y=G_1R-G_1G_2Y.
$$

Move the output terms to the same side and factor:

$$
Y+G_1G_2Y=G_1R,
$$

$$
(1+G_1G_2)Y=G_1R.
$$

Therefore,

$$
\boxed{
\frac{Y}{R}=\frac{G_1}{1+G_1G_2}
}.
$$

The plus sign in the denominator follows from moving the subtracted feedback term to the left-hand side.

For positive feedback, begin instead with

$$
E=R+G_2Y.
$$

The same substitution gives

$$
Y=G_1R+G_1G_2Y,
$$

$$
(1-G_1G_2)Y=G_1R,
$$

and hence

$$
\frac{Y}{R}=\frac{G_1}{1-G_1G_2}.
$$

The series and parallel rules follow from the same signal bookkeeping:

| Configuration | Signal equations | Equivalent |
|---|---|---|
| Series | $$V=G_1R,\quad Y=G_2V=G_2G_1R$$ | $$G_1G_2$$ for scalar blocks |
| Parallel addition | $$Y=G_1R+G_2R$$ | $$G_1+G_2$$ |
| Negative feedback | $$(1+G_1G_2)Y=G_1R$$ | $$G_1/(1+G_1G_2)$$ |
| Positive feedback | $$(1-G_1G_2)Y=G_1R$$ | $$G_1/(1-G_1G_2)$$ |

These relations assume compatible LTI blocks, zero initial conditions for the transfer calculation, and a well-defined interconnection.

The original note records agreement between these four reductions and direct solutions of the loop equations at three complex test points. Their exactness comes from the algebra; the numerical checks test its implementation.

The feedback sign changes the characteristic equation, but the sign alone does not decide stability. The resulting poles must still be examined.

### What changes outside the underdamped case?

The quadratic roots already show the distinction:

| Damping | Roots | Consequence for the formulas above |
|---|---|---|
| $$\zeta=0$$ | $$\pm j\omega_n$$ | No exponential decay; no settling to the final value |
| $$0<\zeta<1$$ | $$-\sigma\pm j\omega_d$$ | Underdamped derivation applies |
| $$\zeta=1$$ | Repeated root at $$-\omega_n$$ | Use the repeated-root limit |
| $$\zeta>1$$ | $$-\omega_n(\zeta\mp\sqrt{\zeta^2-1})$$ | Two negative real roots; no real oscillation frequency $$\omega_d$$ |

For $$\zeta>1$$, both roots are negative because

$$
\sqrt{\zeta^2-1}<\zeta.
$$

The critical response follows directly by taking the limit in the underdamped expression. As $$\zeta\to1^-$$,

$$
\sigma\to\omega_n,
\qquad
\omega_d\to0,
$$

and

$$
\cos\omega_dt\to1,
\qquad
\frac{\sin\omega_dt}{\omega_d}\to t.
$$

Therefore,

$$
\boxed{
y(t)\to1-(1+\omega_nt)e^{-\omega_nt}
}.
$$

Its derivative is

$$
\dot y(t)=\omega_n^2t\,e^{-\omega_nt}>0
\qquad(t>0).
$$

It approaches the final value monotonically, so there is no finite overshoot peak to which the underdamped peak-time formula can be applied.

### Why a dominant-pole approximation needs residues as well as pole locations

A simple pole at $$-\sigma$$ contributes a term proportional to $$e^{-\sigma t}$$. Its time constant is

$$
\tau=\frac1\sigma,
$$

because at $$t=\tau$$ the exponential has decreased to $$e^{-1}$$.

A pole ten times farther left has decay rate $$10\sigma$$. At that same time,

$$
e^{-(10\sigma)\tau}=e^{-10},
$$

while the slow exponential is $$e^{-1}$$. This explains the intuition that fast modes disappear before slow modes do.

But the coefficients multiplying the modes matter. Suppose the omitted simple-pole terms are

$$
r(t)=\sum_{i\in F}c_i e^{p_i t},
\qquad
\operatorname{Re}(p_i)\le-\alpha<0.
$$

Then

$$
\begin{aligned}
\lvert r(t)\rvert
&\le\sum_{i\in F}\lvert c_i\rvert
e^{\operatorname{Re}(p_i)t}\\
&\le
\left(\sum_{i\in F}\lvert c_i\rvert\right)e^{-\alpha t}.
\end{aligned}
$$

Thus a usable bound is

$$
\boxed{
\lvert r(t)\rvert\le B_F e^{-\alpha t},
\qquad
B_F=\sum_{i\in F}\lvert c_i\rvert
}.
$$

Pole separation controls the decay rate. The residues control the prefactor. A fast mode with a large coefficient can matter during the rise even if it is negligible later.

Zeros change these coefficients. For the zero-free standard transfer function $$H_0$$, introduce a zero using

$$
H_z(s)=\left(1+\frac{s}{z}\right)H_0(s),
\qquad z\ne0.
$$

For a unit step,

$$
Y_z(s)=\frac{H_z(s)}s
=
\frac{H_0(s)}s+\frac{H_0(s)}z.
$$

Since $$Y_0=H_0/s$$ and $$y_0(0)=0$$,

$$
H_0(s)=sY_0(s)=\mathcal{L}\{\dot y_0(t)\}.
$$

Consequently,

$$
\boxed{
y_z(t)=y_0(t)+\frac1z\dot y_0(t)
}.
$$

The denominator and pole locations can remain the same while the step response acquires a derivative term. This is a direct reason that the standard overshoot and rise-time formulas cannot be applied unchanged when zeros are present.

A dominant pair is therefore an approximation to justify through both pole locations and modal coefficients, not a rule that permits the rest of the transfer function to be discarded automatically.

### Revision checklist

| Question | Calculation to reproduce | Assumption or common mistake |
|---|---|---|
| What are the poles? | Apply the quadratic formula and identify $$\sigma,\omega_d$$ | Complex-pole formulas assume $$0<\zeta<1$$ |
| Why is $$\zeta=\cos\theta$$? | Divide horizontal distance $$\sigma$$ by radius $$\omega_n$$ | Measure from the negative real axis |
| What is the step response? | Partial fractions, complete the square, invert shifted sine/cosine terms | Unit step, zero initial conditions, standard numerator |
| Where are the stationary points? | Factor $$\dot y$$ and solve $$\sin\omega_dt=0$$ | The initial endpoint is not the first positive peak |
| Why is $$t_p=\pi/\omega_d$$? | Check that the derivative changes from positive to negative | Requires an underdamped oscillation |
| How is overshoot obtained? | Substitute the peak time and subtract the unit final value | Fractional overshoot differs from percentage overshoot |
| When does $$M_p=\exp(-\pi)$$ exactly? | Solve $$\zeta/\sqrt{1-\zeta^2}=1$$ | Exact damping is $$1/\sqrt2$$, not literal $$0.707$$ |
| What is the settling envelope? | Combine cosine and sine into one sinusoid | Keep the prefactor $$1/\sqrt{1-\zeta^2}$$ |
| Is $$4.6/\sigma$$ a guaranteed bound? | Compare it with the full logarithmic envelope time | It omits a positive correction and rounds the logarithm |
| Why does rise time scale as $$1/\omega_n$$? | Substitute $$q=\omega_nt$$ | The coefficient still depends on damping |
| What do the design regions mean? | Convert bounds on $$\omega_n,\zeta,\sigma$$ into geometry | The standard circle and half-plane use approximations |
| How is negative feedback reduced? | Substitute $$E=R-G_2Y$$ into $$Y=G_1E$$ | Derive the sign instead of recalling it |
| Can I use only a dominant pair? | Bound the omitted modal terms and inspect zeros | Pole separation alone does not bound early response error |

## Why it matters for my work

The useful habit is to translate requirements into explicit inequalities while keeping exact results, bounds, and fitted estimates separate. A candidate on the boundary of an approximate rule needs further checking.

The dominant-pole discussion adds a second habit: reducing a model requires an argument about the terms being omitted, including their coefficients.

## What I have not resolved

I want to quantify when a dominant-pair approximation preserves threshold-crossing times, rather than only bounding output error. I also want to work through how a right-half-plane zero restricts achievable transient specifications beyond the standard zero-free model.

---

Sources: Ajou University lecture notes and the standard classical-control treatment in Franklin, Powell, and Emami-Naeini, Feedback Control of Dynamic Systems. The standard second-order response, transient specifications, pole geometry, and block-diagram reductions are derived above. The original numerical records are retained: the pole-angle check, the simulated peak-time, overshoot, rise-time and settling-time comparisons, the worked design-specification values, and the block-diagram checks at complex test points. Rounded values are distinguished from exact identities. New calculations are symbolic; the additional rise-time crossing calculation is marked for verification, and no new simulation results are claimed.
