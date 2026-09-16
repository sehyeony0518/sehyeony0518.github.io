---
layout: study_note
title: "Root Locus and Stability Margins: Two Pictures of the Same Boundary"
description: "Watching the closed-loop poles move as a gain sweeps, and reading how much gain and phase you have left off a plot of the open loop: two methods that meet exactly at the edge of stability."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "feedback-control"
category_title: "Feedback Control & Classical Design"
order: 5
source: "Lecture notes, Ajou University"
written: true
updated: "2026-09-15"
---

Root locus follows the closed-loop poles as a gain changes. Frequency-domain margins examine how the open-loop response approaches the critical value that makes the closed-loop characteristic equation vanish.

The connection is exact: a root-locus point on the imaginary axis satisfies the same equation used to identify a gain or phase boundary in the frequency response. For the cubic example shared with the Routh–Hurwitz note, all three descriptions produce the boundary $$K=6$$.

## Core question and definition

**How does changing a positive gain move the closed-loop poles, and how can the same stability boundary be read from the open-loop frequency response?**

Separate the adjustable gain from the fixed loop dynamics:

$$
L_0(s)=\frac{b(s)}{a(s)},
\qquad
\mathcal{L}_K(s)=K L_0(s).
$$

Here $$L_0$$ is gain-free and $$\mathcal{L}_K$$ is the complete loop transfer function at the chosen gain. This distinction prevents accidentally counting $$K$$ twice.

Assume real, coprime polynomials with

$$
n=\deg a>m=\deg b.
$$

For the construction below, take both polynomials as monic. Any positive leading-coefficient ratio can be absorbed into the definition of $$K$$. We consider

$$
K\ge0.
$$

The closed-loop characteristic equation is

$$
1+K L_0(s)=0,
$$

or equivalently,

$$
\boxed{a(s)+K b(s)=0}.
$$

The root locus is the set of its roots as $$K$$ varies, with roots and branches counted according to multiplicity.

### Deriving the magnitude and angle conditions

At a finite point that is neither a pole nor a zero of $$L_0$$,

$$
1+K L_0(s)=0
\quad\Longleftrightarrow\quad
K L_0(s)=-1.
$$

Write

$$
L_0(s)=\lvert L_0(s)\rvert e^{j\phi(s)}.
$$

For positive $$K$$,

$$
K\lvert L_0(s)\rvert e^{j\phi(s)}
=e^{j(2q+1)\pi}
$$

for some integer $$q$$. Matching magnitudes and angles gives

$$
\boxed{K\lvert L_0(s)\rvert=1},
$$

$$
\boxed{\arg L_0(s)=(2q+1)\pi}.
$$

Equivalently, the angle must be $$180^\circ$$ modulo $$360^\circ$$.

The angle condition contains no $$K$$. It determines which finite points belong to the positive-gain locus. Once such a point is found, the magnitude condition assigns its gain:

$$
\boxed{K=\frac1{\lvert L_0(s)\rvert}}.
$$

Conversely, if the angle is not an odd multiple of $$\pi$$, multiplying by a positive real gain cannot rotate the complex number onto the negative real axis.

Thus:

- The angle condition determines the locus geometry.
- The magnitude condition parameterises that geometry by gain.
- Poles and zeros are limiting endpoints, where this finite-point calculation must be interpreted through limits.

## Key concepts

### Why the branches start at poles and end at zeros

At $$K=0$$, the characteristic polynomial is

$$
a(s)+0\cdot b(s)=a(s).
$$

Its roots are the open-loop poles. There are $$n$$ roots counting multiplicity, so there are $$n$$ branches leaving these starting locations as gain increases.

The magnitude condition gives the same endpoint interpretation. Near an uncancelled pole,

$$
\lvert L_0(s)\rvert\to\infty,
$$

so

$$
K=\frac1{\lvert L_0(s)\rvert}\to0.
$$

For large gain, divide the characteristic equation by $$K$$:

$$
\frac{a(s)}K+b(s)=0.
$$

If a branch approaches a finite limit $$z$$ as $$K\to\infty$$, then

$$
b(z)=0.
$$

It must approach an open-loop zero. Near such a zero,

$$
\lvert L_0(s)\rvert\to0,
$$

so the magnitude condition gives $$K\to\infty$$.

The limiting polynomial $$b$$ has $$m$$ finite roots counting multiplicity. Those account for $$m$$ branch endpoints. The remaining

$$
\boxed{n-m}
$$

branches escape to infinity.

The endpoint rules therefore use the characteristic polynomial and the limiting magnitude condition. The angle condition specifies the directions from which the branches approach those endpoints.

### Why the locus is symmetric about the real axis

Because $$a$$ and $$b$$ have real coefficients and $$K$$ is real,

$$
\overline{a(s)+Kb(s)}
=a(\overline s)+Kb(\overline s).
$$

If $$s$$ is a root, then $$\overline s$$ is a root at the same gain. The root locus is therefore symmetric about the real axis.

This symmetry is useful when sketching: a branch computed above the axis determines its reflected branch below it.

### Deriving the real-axis segment rule

Factor the gain-free loop as

$$
L_0(s)=
\frac{\prod_{i=1}^{m}(s-z_i)}
{\prod_{j=1}^{n}(s-p_j)}.
$$

Its angle is

$$
\arg L_0(s)
=
\sum_i\arg(s-z_i)-\sum_j\arg(s-p_j)
\pmod{2\pi}.
$$

Take a real test point $$s=x$$ that is not itself a pole or zero.

A real pole or zero to the left gives a positive real factor and contributes zero angle. One to the right gives a negative real factor and contributes $$\pi$$.

A conjugate pair contributes no net angle modulo $$2\pi$$, because

$$
(x-a-jb)(x-a+jb)=(x-a)^2+b^2>0.
$$

Let $$N_z$$ and $$N_p$$ count the real zeros and poles to the right of $$x$$, including multiplicity. Then

$$
\arg L_0(x)
=
\pi(N_z-N_p)
\pmod{2\pi}.
$$

But

$$
(N_z-N_p)-(N_z+N_p)=-2N_p,
$$

so the parity of the difference equals the parity of the sum. The angle condition is therefore satisfied exactly when

$$
\boxed{N_z+N_p\text{ is odd}}.
$$

This is the real-axis rule: a segment belongs to the positive-gain locus when the total number of real poles and zeros to its right is odd.

### Deriving the asymptote angles

Let

$$
q=n-m>0.
$$

For large $$\lvert s\rvert$$, each vector $$s-z_i$$ and $$s-p_j$$ has approximately the angle of $$s$$. If $$\theta=\arg s$$,

$$
\arg L_0(s)
\approx m\theta-n\theta=-q\theta.
$$

The angle condition requires

$$
-q\theta=\pi\pmod{2\pi}.
$$

The distinct directions are therefore

$$
\boxed{
\theta_\ell=\frac{(2\ell+1)\pi}{q},
\qquad
\ell=0,\ldots,q-1
}.
$$

There are $$q=n-m$$ directions, matching the number of branches escaping to infinity.

The magnitude condition is consistent with this result. Since

$$
L_0(s)\sim\frac1{s^q},
$$

we have

$$
K\lvert L_0(s)\rvert\sim\frac{K}{\lvert s\rvert^q}=1,
$$

so

$$
\lvert s\rvert\sim K^{1/q}.
$$

The angles specify the directions; the magnitude condition specifies how far along them the roots move as gain grows.

### Deriving the asymptote centroid

The leading large-distance approximation gives directions but not the point through which the asymptote lines pass. Retain one more coefficient.

Define the sums

$$
P_\Sigma=\sum_{j=1}^{n}p_j,
\qquad
Z_\Sigma=\sum_{i=1}^{m}z_i.
$$

Expanding the monic factorizations,

$$
a(s)=s^n-P_\Sigma s^{n-1}+O(s^{n-2}),
$$

$$
b(s)=s^m-Z_\Sigma s^{m-1}+O(s^{m-2}).
$$

Hence

$$
\begin{aligned}
\frac{a(s)}{b(s)}
&=
s^q
\frac{1-P_\Sigma/s+O(s^{-2})}
{1-Z_\Sigma/s+O(s^{-2})}\\
&=
s^q
\left[
1+\frac{Z_\Sigma-P_\Sigma}{s}
+O(s^{-2})
\right].
\end{aligned}
$$

Writing $$\Delta=P_\Sigma-Z_\Sigma$$,

$$
\frac{a(s)}{b(s)}
=
s^q-\Delta s^{q-1}+O(s^{q-2}).
$$

Now shift the coordinate:

$$
s=w+c.
$$

The leading terms become

$$
\begin{aligned}
s^q-\Delta s^{q-1}
&=(w+c)^q-\Delta(w+c)^{q-1}\\
&=w^q+(qc-\Delta)w^{q-1}+O(w^{q-2}).
\end{aligned}
$$

Choose $$c$$ to cancel the next-highest term:

$$
qc-\Delta=0.
$$

Thus

$$
\boxed{
c=\frac{\sum_jp_j-\sum_i z_i}{n-m}
}.
$$

The characteristic equation $$a/b=-K$$ now has the asymptotic form

$$
w^q+O(w^{q-2})=-K.
$$

Consequently, the escaping roots approach lines of the form

$$
\boxed{
s=c+\rho e^{j\theta_\ell},
\qquad \rho\to\infty
}.
$$

This $$c$$ is the asymptote centroid. It is real because the sums of roots of real polynomials are real.

The centroid is not generally a point at which actual branches meet. It is the common intersection of their asymptotic lines.

### What a pole-zero excess of three implies

If $$q=n-m=3$$, the asymptote angles are

$$
60^\circ,\qquad180^\circ,\qquad300^\circ.
$$

Two point into the RHP.

More generally, for $$q\ge3$$,

$$
0<\frac{\pi}{q}\le\frac{\pi}{3}<\frac{\pi}{2}.
$$

The asymptote at $$\pi/q$$ has positive real direction. Along it,

$$
\operatorname{Re}(s)
=c+\rho\cos(\pi/q)\to+\infty.
$$

Therefore, under the stated positive-gain, strictly proper rational assumptions,

$$
\boxed{
n-m\ge3
\quad\Longrightarrow\quad
\text{the closed loop is unstable at sufficiently large gain}
}.
$$

This follows from the derived asymptotes, before any detailed tracing.

### First worked locus: fixed decay rate after breakaway

Take

$$
L_0(s)=\frac1{s(s+1)}.
$$

The characteristic equation is

$$
s(s+1)+K=0,
$$

or

$$
s^2+s+K=0.
$$

The quadratic formula gives

$$
s_\pm=\frac{-1\pm\sqrt{1-4K}}2.
$$

For $$0\le K\le1/4$$, the roots are real. For $$K>1/4$$,

$$
\begin{aligned}
s_\pm
&=-\frac12
\pm\frac j2\sqrt{4K-1}\\
&=-\frac12\pm j\sqrt{K-\frac14}.
\end{aligned}
$$

The original traced values are retained unchanged:

```text
 K=0     roots = [-1, 0]           (the open-loop poles)
 K=0.25  roots = [-0.5, -0.5]      (breakaway: a double root)
 K=2.0   roots = -0.5 +/- 1.3229j
 K=10.0  roots = -0.5 +/- 3.1225j
```

The construction rules reproduce this shape:

- Between $$-1$$ and $$0$$, there is one real pole to the right, so that segment belongs to the locus.
- There are no finite zeros, so both branches go to infinity.
- The centroid is

$$
c=\frac{(-1)+0}{2}=-\frac12.
$$

- The two asymptote angles are

$$
\frac{\pi}{2},\qquad\frac{3\pi}{2},
$$

so the branches become vertical through the centroid.

Comparing the characteristic polynomial with the standard second-order denominator,

$$
s^2+2\zeta\omega_ns+\omega_n^2,
$$

gives

$$
\omega_n^2=K,
\qquad
2\zeta\omega_n=1.
$$

Thus

$$
\omega_n=\sqrt K,
\qquad
\zeta=\frac1{2\sqrt K},
\qquad
\sigma=\zeta\omega_n=\frac12.
$$

After breakaway, increasing gain raises $$\omega_d$$ and reduces damping ratio, while the exponential decay rate remains fixed. The modal envelope contains $$e^{-t/2}$$.

This does not mean every settling-time threshold is independent of gain: the oscillation frequency and response coefficients still change. The precise statement is that proportional gain cannot move this complex pair farther left.

#### Selecting a damping ratio on the locus

For the requested damping ratio

$$
\zeta=\frac12,
$$

the pole angle from the negative real axis is

$$
\theta=\arccos\frac12=60^\circ.
$$

Using the derived damping expression,

$$
\frac1{2\sqrt K}=\frac12
\quad\Longrightarrow\quad
K=1.
$$

The poles are exactly

$$
s=-\frac12\pm j\frac{\sqrt3}{2},
$$

recorded in rounded form as

$$
s\approx-0.5\pm0.866j.
$$

The original design values are $$K=1.0$$ and $$\zeta=0.5000$$. The damping value and gain are exact; the displayed imaginary coordinate is rounded.

### Second worked locus: a circle followed by break-in

Take

$$
L_0(s)=\frac{s}{s^2+1}.
$$

The characteristic equation becomes

$$
s^2+Ks+1=0,
$$

so

$$
s_\pm=\frac{-K\pm\sqrt{K^2-4}}2.
$$

For $$0<K<2$$,

$$
s_\pm=-\frac K2\pm j\sqrt{1-\frac{K^2}{4}}.
$$

The squared magnitude of either root is

$$
\lvert s_\pm\rvert^2
=
\frac{K^2}{4}
+\left(1-\frac{K^2}{4}\right)
=1.
$$

Thus both roots lie exactly on the unit circle in this gain interval. Their product being one gives the same conclusion because they are a conjugate pair; a product of one alone would not imply equal magnitudes for arbitrary roots.

The original traced values are retained unchanged:

```text
 K=0    roots = +/-1j       |roots| = 1
 K=1.0  roots = -0.5+/-0.866j   |roots| = 1
 K=2.0  roots = [-1, -1]        |roots| = 1   <- break-IN
 K=3.0  roots = [-2.618, -0.382]
 K=10   roots = [-9.899, -0.101]
```

At $$K=2$$, the roots meet at $$-1$$. For $$K>2$$, they are real and negative because

$$
\sqrt{K^2-4}<K.
$$

The root approaching the finite zero can be rationalised:

$$
\begin{aligned}
s_{\mathrm{slow}}
&=\frac{-K+\sqrt{K^2-4}}2\\
&=-\frac{K-\sqrt{K^2-4}}2\\
&=-\frac{2}{K+\sqrt{K^2-4}}.
\end{aligned}
$$

Therefore,

$$
s_{\mathrm{slow}}\to0^-
\qquad(K\to\infty).
$$

The other root is

$$
s_{\mathrm{fast}}
=-\frac{K+\sqrt{K^2-4}}2\to-\infty.
$$

There is one finite zero at the origin and one asymptote. Its centroid is

$$
c=\frac{j+(-j)-0}{1}=0,
$$

and its angle is $$\pi$$. This agrees with one branch approaching the zero and the other escaping along the negative real axis.

For a negative real test point, the zero at the origin lies to its right; the complex poles contribute no net angle. The entire negative real axis therefore satisfies the real-axis segment rule.

The two branches arrive on that axis as gain increases through $$2$$: this is break-in.

### Departure angle from a simple pole: taking the limit

Let $$p_\ell$$ be a simple pole, distinct from every zero and other pole. Put a test point on a nearby branch:

$$
s=p_\ell+\rho e^{j\phi},
\qquad \rho\to0^+.
$$

Then

$$
\arg(s-p_\ell)=\phi.
$$

For every other pole and zero, the corresponding difference tends to a nonzero complex number:

$$
s-z_i\to p_\ell-z_i,
$$

$$
s-p_j\to p_\ell-p_j,
\qquad j\ne\ell.
$$

Their arguments therefore approach fixed values modulo $$2\pi$$. Applying the angle condition and taking the limit,

$$
\sum_i\arg(p_\ell-z_i)
-\sum_{j\ne\ell}\arg(p_\ell-p_j)
-\phi
=
\pi\pmod{2\pi}.
$$

Solving,

$$
\boxed{
\phi_\ell
=
\pi+\sum_i\arg(p_\ell-z_i)
-\sum_{j\ne\ell}\arg(p_\ell-p_j)
\pmod{2\pi}
}.
$$

The sign can also be checked with a local expansion. Near the pole,

$$
L_0(s)=\frac{C_\ell}{s-p_\ell}+O(1),
$$

where

$$
C_\ell
=
\frac{b(p_\ell)}{a'(p_\ell)}
=
\frac{\prod_i(p_\ell-z_i)}
{\prod_{j\ne\ell}(p_\ell-p_j)}.
$$

Substitution into $$1+KL_0=0$$ gives, to leading order,

$$
s-p_\ell=-KC_\ell+O(K^2).
$$

Thus the departure direction as $$K$$ increases from zero is

$$
\arg(-C_\ell)=\pi+\arg C_\ell,
$$

which matches the angle formula.

### Arrival angle at a simple zero: define the direction carefully

Let $$z_\ell$$ be a simple zero, and write a nearby point as

$$
s=z_\ell+\rho e^{j\psi},
\qquad \rho\to0^+.
$$

Here $$\psi$$ is the angle of the vector **from the zero to the nearby locus point**.

The angle condition becomes, in the limit,

$$
\psi
+\sum_{i\ne\ell}\arg(z_\ell-z_i)
-\sum_j\arg(z_\ell-p_j)
=
\pi\pmod{2\pi}.
$$

Hence

$$
\boxed{
\psi_\ell
=
\pi-\sum_{i\ne\ell}\arg(z_\ell-z_i)
+\sum_j\arg(z_\ell-p_j)
\pmod{2\pi}
}.
$$

This defines the geometric ray along which the branch approaches the zero. The direction of motion **toward** the zero is opposite that ray.

To see this explicitly, write the local expansion

$$
L_0(s)=C_\ell^{(z)}(s-z_\ell)+O((s-z_\ell)^2),
$$

where

$$
C_\ell^{(z)}=\frac{b'(z_\ell)}{a(z_\ell)}.
$$

The characteristic equation gives

$$
s-z_\ell
=
-\frac1{K C_\ell^{(z)}}+O(K^{-2}).
$$

Differentiating the leading term with respect to gain,

$$
\frac{ds}{dK}
=
\frac1{K^2C_\ell^{(z)}}+O(K^{-3}).
$$

The gain-direction tangent differs from the outward ray by $$\pi$$. Stating which vector defines an “arrival angle” avoids a $$180^\circ$$ ambiguity.

Both formulas above assume simple poles or zeros. For a repeated factor, its multiplicity multiplies the unknown angular term in the angle condition and produces multiple departure or arrival directions.

### Preserved departure-angle validation

The original validation used poles at $$-1$$ and $$-2\pm2j$$, with a zero at $$-3$$, ```text
 poles -1, -2+/-2j; zero at -3
   pole  (-1+0j): formula -180.00  traced -180.00   OK
   pole  (-2+2j): formula  +36.87  traced  +36.87   OK
   pole  (-2-2j): formula  -36.87  traced  -36.87   OK
```

For the upper complex pole,

$$
C_\ell
=
\frac{1+2j}{(-1+2j)(4j)}
=
\frac{1+2j}{-8-4j}.
$$

Rationalising,

$$
\begin{aligned}
C_\ell
&=\frac{(1+2j)(-8+4j)}{(-8)^2+4^2}\\
&=\frac{-16-12j}{80}\\
&=-\frac15-\frac{3}{20}j.
\end{aligned}
$$

Therefore,

$$
-C_\ell=\frac15+\frac{3}{20}j,
$$

and the departure angle is

$$
\phi_\ell
=
\arctan\left(\frac{3/20}{1/5}\right)
=
\arctan\frac34
\approx36.87^\circ.
$$

The lower-pole direction is its conjugate reflection.

For the real pole at $$-1$$,

$$
C_\ell
=
\frac{2}{(1-2j)(1+2j)}
=
\frac25>0.
$$

Thus $$-C_\ell$$ points along the negative real axis, giving $$-\pi$$ or equivalently $$\pi$$. This agrees with the recorded $$-180.00$$.

The original note reports checks across four pole/zero configurations; the displayed configuration is retained here with its local algebra.

### Deriving the breakaway condition

From

$$
a(s)+Kb(s)=0,
$$

solve for gain wherever $$b(s)\ne0$$:

$$
K(s)=-\frac{a(s)}{b(s)}.
$$

Differentiate:

$$
\boxed{
\frac{dK}{ds}
=
-\frac{a'(s)b(s)-a(s)b'(s)}{b(s)^2}
}.
$$

Therefore,

$$
\boxed{
\frac{dK}{ds}=0
\quad\Longleftrightarrow\quad
a'b-ab'=0
}
$$

at points where $$b\ne0$$.

Why does this identify repeated-root candidates? A repeated characteristic root must satisfy both

$$
a(s)+Kb(s)=0
$$

and

$$
a'(s)+Kb'(s)=0.
$$

Substituting $$K=-a/b$$ into the second equation gives

$$
a'-\frac{a}{b}b'
=
\frac{a'b-ab'}b
=0.
$$

Thus the derivative condition identifies algebraic multiple-root candidates. It does not by itself establish a positive-gain real-axis breakaway:

- The candidate may require negative or nonreal gain.
- It may not lie on the real axis.
- A higher-order degeneracy may need further local analysis.
- Even a valid real meeting point must be classified as breakaway or break-in.

#### The rejected negative-gain candidate

For

$$
L_0(s)=\frac{s}{s^2+1},
$$

we have

$$
a=s^2+1,\qquad b=s,
$$

so

$$
a'b-ab'
=(2s)s-(s^2+1)
=s^2-1.
$$

The candidates are $$s=\pm1$$. Their gains are

$$
K(s)=-\frac{s^2+1}{s}.
$$

Hence

$$
K(+1)=-2,
\qquad
K(-1)=2.
$$

The original candidate check is retained unchanged:

```text
 1 + K s/(s^2+1):  a'b - ab' = s^2 - 1 = 0  ->  s = +/-1
   s=+1: K = -A/B = -2.0000  -> rejected (K<0), not on the K>0 locus
   s=-1: K = -A/B = +2.0000  -> valid, BREAK-IN
```

One of the two candidates is rejected in this example. There is no general rule that half the candidates will be extraneous.

#### Distinguishing breakaway from break-in

For the first locus,

$$
K(s)=-s(s+1)
=\frac14-\left(s+\frac12\right)^2.
$$

Real roots near $$-1/2$$ therefore exist for gains below $$1/4$$. Increasing gain past the maximum makes the displacement imaginary: the branches leave the real axis.

For the second locus,

$$
K(s)=-s-\frac1s.
$$

Its derivatives are

$$
K'(s)=-1+\frac1{s^2},
\qquad
K''(s)=-\frac2{s^3}.
$$

At $$s=-1$$,

$$
K=2,\qquad K'=0,\qquad K''=2.
$$

The local expansion is

$$
K=2+(s+1)^2+O((s+1)^3).
$$

Real displacements occur on the higher-gain side of the meeting point. The branches enter the real axis as gain increases: break-in.

### Deriving imaginary-axis crossings from even and odd parts

Write the characteristic polynomial as

$$
P_K(s)=\sum_{\ell=0}^{n}c_\ell(K)s^\ell.
$$

Substitute $$s=j\omega$$. Even powers are real and odd powers are imaginary:

$$
P_K(j\omega)
=
\sum_r(-1)^r c_{2r}(K)\omega^{2r}
+
j\sum_r(-1)^r c_{2r+1}(K)\omega^{2r+1}.
$$

Therefore an imaginary-axis root requires

$$
\boxed{
\sum_r(-1)^r c_{2r}(K)\omega^{2r}=0
},
$$

$$
\boxed{
\sum_r(-1)^r c_{2r+1}(K)\omega^{2r+1}=0
}.
$$

These are simultaneous equations in $$K$$ and $$\omega$$. Include $$\omega=0$$: a root at the origin is also a stability boundary.

A solution identifies a boundary root, but the locus might cross the axis or merely touch it. Root counts on either side determine the stability change.

Conversely, finding no boundary root does not prove stability by itself. Over a finite gain interval with continuous coefficients and unchanged polynomial degree, the RHP root count cannot change without an axis crossing. A known stable gain in that interval is still needed to establish stability throughout it.

### The cubic crossing is exactly the Routh boundary

Use the loop shared with the Routh–Hurwitz note:

$$
\mathcal{L}_K(s)=\frac{K}{s(s+1)(s+2)}.
$$

Its characteristic polynomial is

$$
P_K(s)=s^3+3s^2+2s+K.
$$

Substituting $$s=j\omega$$ gives

$$
\begin{aligned}
P_K(j\omega)
&=-j\omega^3-3\omega^2+2j\omega+K\\
&=(K-3\omega^2)+j\omega(2-\omega^2).
\end{aligned}
$$

Thus

$$
K-3\omega^2=0,
$$

$$
\omega(2-\omega^2)=0.
$$

The origin solution is

$$
\omega=0,\qquad K=0.
$$

For a positive nonzero frequency,

$$
\omega^2=2,
\qquad
\omega=\sqrt2,
$$

and then

$$
K=3\omega^2=6.
$$

Hence

$$
\boxed{K_{\mathrm{crit}}=6,\qquad\omega_{\mathrm{crit}}=\sqrt2}.
$$

The Routh first column for this same polynomial is

$$
1,\qquad3,\qquad\frac{6-K}{3},\qquad K.
$$

Strict positivity gives

$$
0<K<6.
$$

At $$K=6$$, the $$s^1$$ row vanishes, and the auxiliary polynomial is

$$
A(s)=3s^2+6.
$$

Its imaginary roots satisfy

$$
-3\omega^2+6=0,
$$

which is exactly the real-part equation above at the boundary. The original polynomial factors as

$$
P_6(s)=(s+3)(s^2+2).
$$

Thus both methods identify the roots

$$
-3,\qquad\pm j\sqrt2.
$$

The Routh zero row and the simultaneous even/odd equations are two descriptions of the same common-factor event.

### Deriving gain margin from the critical loop value

The closed-loop characteristic equation on the imaginary axis is

$$
1+\mathcal{L}_K(j\omega)=0.
$$

Therefore its critical loop value is

$$
\boxed{\mathcal{L}_K(j\omega)=-1}.
$$

Let $$\omega_\pi$$ be a phase-crossover frequency where the loop response lies on the negative real axis. Write

$$
\mathcal{L}_K(j\omega_\pi)
=-\lvert\mathcal{L}_K(j\omega_\pi)\rvert.
$$

Now multiply the nominal loop by an additional positive gain factor $$g$$. To place this frequency-response point at $$-1$$,

$$
-g\lvert\mathcal{L}_K(j\omega_\pi)\rvert=-1.
$$

Hence

$$
g=\frac1{\lvert\mathcal{L}_K(j\omega_\pi)\rvert}.
$$

This defines the gain-margin factor at that crossing:

$$
\boxed{
GM=\frac1{\lvert\mathcal{L}_K(j\omega_\pi)\rvert}
}.
$$

Its decibel form is

$$
\boxed{GM_{\mathrm{dB}}=20\log_{10}GM}.
$$

Interpreting this factor as the amount of gain increase a stable loop can tolerate requires the relevant stability and crossing assumptions. A factor below one is not an available positive gain-increase allowance.

### Deriving phase margin at gain crossover

Let $$\omega_c$$ be a gain-crossover frequency:

$$
\lvert\mathcal{L}_K(j\omega_c)\rvert=1.
$$

Write its phase, using the relevant continuous branch near $$-\pi$$, as $$\phi_c$$. An added phase lag $$\delta_\phi$$ changes the point to

$$
e^{-j\delta_\phi}\mathcal{L}_K(j\omega_c).
$$

Its magnitude remains one. To reach the critical point $$-1$$, its phase must become $$-\pi$$:
$$
\phi_c-\delta_\phi=-\pi.
$$

Therefore,

$$
\boxed{
PM=\delta_\phi=\pi+\phi_c
}.
$$

In degrees,

$$
\boxed{
PM=180^\circ+\arg\mathcal{L}_K(j\omega_c)
}.
$$

This is the additional phase lag at gain crossover that would move that point to the critical value. As with gain margin, a stability interpretation needs the surrounding loop geometry, not just the arithmetic at one point.

### Why the gain margin is exactly 6/K

For

$$
\mathcal{L}_K(s)=\frac{K}{s(s+1)(s+2)},
\qquad K>0,
$$

evaluate the denominator on the imaginary axis:

$$
\begin{aligned}
(j\omega)(1+j\omega)(2+j\omega)
&=(j\omega)\left[(2-\omega^2)+3j\omega\right]\\
&=-3\omega^2+j\omega(2-\omega^2).
\end{aligned}
$$

For $$\omega>0$$ its real part is negative. The loop response lies on the negative real axis exactly when the imaginary part of this denominator vanishes:

$$
\omega(2-\omega^2)=0.
$$

Excluding the singular point $$\omega=0$$,

$$
\boxed{\omega_\pi=\sqrt2}.
$$

At this frequency,

$$
-3\omega_\pi^2=-6,
$$

so

$$
\boxed{
\mathcal{L}_K(j\sqrt2)=-\frac K6
}.
$$

The phase is $$-\pi$$ on the continuous positive-frequency phase branch, and the magnitude is $$K/6$$.

The magnitude can also be obtained factor by factor:

$$
\lvert\mathcal{L}_K(j\omega)\rvert
=
\frac{K}
{\omega\sqrt{1+\omega^2}\sqrt{4+\omega^2}}.
$$

At $$\omega=\sqrt2$$,

$$
\begin{aligned}
\lvert\mathcal{L}_K(j\sqrt2)\rvert
&=\frac{K}{\sqrt2\sqrt3\sqrt6}\\
&=\frac{K}{\sqrt{36}}\\
&=\frac K6.
\end{aligned}
$$

Invert this magnitude:

$$
\boxed{GM=\frac6K}.
$$

The corresponding boundary gain is

$$
GM\cdot K=\frac6K K=6.
$$

This is exactly the Routh boundary and exactly the root-locus imaginary-axis crossing. No numerical approximation is involved.

### Computing phase margin for the same cubic

For positive frequency, the three denominator factors have phases

$$
\arg(j\omega)=\frac{\pi}{2},
$$

$$
\arg(1+j\omega)=\arctan\omega,
$$

$$
\arg(2+j\omega)=\arctan\frac{\omega}{2}.
$$

Therefore the continuous loop phase is

$$
\phi(\omega)
=
-\frac{\pi}{2}
-\arctan\omega
-\arctan\frac{\omega}{2}.
$$

The gain-crossover condition is

$$
\frac{K}
{\omega_c\sqrt{1+\omega_c^2}\sqrt{4+\omega_c^2}}
=1.
$$

Squaring,

$$
K^2
=
\omega_c^2(1+\omega_c^2)(4+\omega_c^2).
$$

Set $$u=\omega_c^2$$. Then

$$
\boxed{
u^3+5u^2+4u-K^2=0
}.
$$

For $$u\ge0$$, the derivative of the left-hand side with respect to $$u$$ is

$$
3u^2+10u+4>0.
$$

Thus there is exactly one positive gain-crossover frequency for every $$K>0$$, and it increases with gain.

The phase margin is

$$
\boxed{
PM
=
\frac{\pi}{2}
-\arctan\omega_c
-\arctan\frac{\omega_c}{2}
}.
$$

At $$K=6$$, the gain-crossover frequency is $$\sqrt2$$ because the magnitude there is one. The loop phase is $$-\pi$$, so

$$
PM=0.
$$

For smaller positive gain, crossover occurs at a lower frequency and the phase margin is positive. For larger gain, crossover moves higher and the phase margin is negative. In this example, that transition agrees with the Routh stability interval.

The original margin table is retained unchanged:

```text
 K=1   wc=0.4457  PM=+53.41deg | w180=1.4142 GM=6.000x (+15.56dB)  stable
 K=2   wc=0.7494  PM=+32.61deg | w180=1.4142 GM=3.000x ( +9.54dB)  stable
 K=6   wc=1.4142  PM= -0.00deg | w180=1.4142 GM=1.000x ( +0.00dB)  BOUNDARY
 K=12  wc=1.9545  PM=-17.25deg | w180=1.4142 GM=0.500x ( -6.02dB)  unstable
```

The displayed $$-0.00$$ at the boundary represents the numerical zero; the exact phase margin is zero.

At $$K=12$$, the factor $$0.500x$$ identifies the gain reduction to the boundary. It is not an allowable gain increase for a stable nominal loop, because the nominal loop is already unstable.

### One Bode plot can serve several positive gains

Since

$$
\mathcal{L}_K=K L_0,
$$

the magnitude in decibels satisfies

$$
20\log_{10}\lvert\mathcal{L}_K\rvert
=
20\log_{10}K
+
20\log_{10}\lvert L_0\rvert.
$$

Positive gain adds no phase:

$$
\arg\mathcal{L}_K=\arg L_0.
$$

Thus increasing gain shifts the magnitude curve upward by $$20\log_{10}K$$ while leaving the phase curve unchanged.

If the gain-free curve remains fixed instead, the gain-crossover condition is read at

$$
20\log_{10}\lvert L_0(j\omega_c)\rvert
=
-20\log_{10}K.
$$

This gives the direction of the shifted reference level explicitly.

### When a single gain or phase margin is insufficient

The cubic example has a particularly clear structure: one positive-frequency phase crossover, one gain crossover, and a single upper stability boundary for positive gain. More general loops need not behave that way.

- Multiple negative-real-axis crossings produce several gain factors at which boundary roots may occur.
- Multiple gain crossovers produce several phase-margin readings.
- A boundary point can represent entry into or exit from an unstable region.
- Open-loop RHP poles affect the closed-loop root count.
- Imaginary-axis open-loop poles require the appropriate contour treatment.
- A reduced input–output model can hide internal modes.

The Nyquist criterion is the general tool for relating the frequency-response curve to closed-loop stability: it combines encirclements of the critical point $$-1$$ with the open-loop RHP pole count.

Frequency-response measurements are therefore valuable even when a detailed transfer-function model is unavailable. But a single reported margin does not remove the need for the stability information and crossing structure required to interpret it.

### Separate gain and phase margins do not measure every perturbation

Gain margin asks about radial scaling of a loop-response point. Phase margin asks about angular motion at unit magnitude. A simultaneous gain-and-phase perturbation moves in a different direction in the complex plane.

The distance from a loop-response point to the critical point is

$$
d(\omega)=\lvert-1-\mathcal{L}_K(j\omega)\rvert
=\lvert1+\mathcal{L}_K(j\omega)\rvert.
$$

From the preceding note,

$$
\mathcal{S}(j\omega)
=\frac1{1+\mathcal{L}_K(j\omega)},
$$

so

$$
\boxed{
\lvert\mathcal{S}(j\omega)\rvert=\frac1{d(\omega)}
}.
$$

A close approach to $$-1$$ therefore corresponds exactly to a large sensitivity magnitude, even if separate gain and phase readings do not make that approach obvious.

This pointwise geometric fact is not yet a complete robustness guarantee. Such a guarantee must specify what perturbations are allowed and whether they can arise from a consistent dynamical system.

### Revision checklist

| Question | Calculation to reproduce | Assumption or common mistake |
|---|---|---|
| Which transfer function contains the gain? | Define $$L_0$$ and $$\mathcal{L}_K=KL_0$$ separately | Do not count $$K$$ twice |
| Why is the angle condition decisive? | Write $$KL_0=-1$$ in polar form | Positive real gain changes magnitude, not angle |
| How is gain assigned to a locus point? | $$K=1/\lvert L_0(s)\rvert$$ | The point must first satisfy the angle condition |
| Where do branches start and end? | Examine $$a+Kb=0$$ as $$K\to0$$ and $$K\to\infty$$ | Count multiplicities and distinguish finite zeros from infinity |
| Why the odd-count real-axis rule? | Add angles of real factors and cancel conjugate-pair contributions | Count poles and zeros to the right |
| How many asymptotes are there? | Count the $$n-m$$ branches without finite endpoints | The derivation assumes the stated strictly proper loop |
| What are their angles? | Apply the angle condition to $$L_0(s)\sim s^{-(n-m)}$$ | Use odd multiples of $$\pi/(n-m)$$ |
| Where is the centroid? | Retain the next term of $$a/b$$ and shift away its coefficient | It is an asymptote intersection, not necessarily a branch intersection |
| How is departure angle derived? | Isolate the pole factor and take the nearby-point limit | Other factors must remain nonzero |
| What does arrival angle mean? | Define the vector $$s-z$$ before applying the limit | The inward direction of motion differs by $$\pi$$ |
| What does $$a'b-ab'=0$$ provide? | Differentiate $$K=-a/b$$ and check repeated-root conditions | Candidates still require real, positive gain and local classification |
| How are axis crossings found? | Set both real and imaginary parts of $$P_K(j\omega)$$ to zero | Include the origin and distinguish crossing from tangency |
| Does absence of crossings prove stability? | Establish a root count at an anchor gain | The count may be constant and nonzero |
| Why is $$GM=6/K$$ here? | Find $$\omega_\pi=\sqrt2$$, evaluate $$\mathcal{L}_K=-K/6$$, and invert its magnitude | The factor multiplies the current gain |
| How is phase margin obtained? | At unit magnitude, solve $$\phi_c-\delta_\phi=-\pi$$ | Multiple crossovers need separate interpretation |
| When is Nyquist needed? | Examine the full critical-point encirclement and open-loop pole count | One margin number need not decide stability |
| How does sensitivity connect to geometry? | Use $$\lvert\mathcal{S}\rvert=1/\lvert1+\mathcal{L}_K\rvert$$ | Separate gain and phase changes do not cover every perturbation |

## Why it matters for my work

The useful habit is to calculate how a system approaches a failure boundary, not only whether it currently passes a stability test. The Routh, root-locus, and frequency-response calculations are strongest when their assumptions and boundary conditions are compared explicitly.

The breakaway calculation reinforces a second habit: solving an algebraic condition generates candidates; checking their admissibility is part of the solution.

## What I have not resolved

I want to work through a concrete example where combined gain and phase uncertainty exposes a weakness that separate margins obscure. I also want to study how the single-gain locus extends to a constrained design with two controller parameters.

---

Sources: Ajou University lecture notes and the standard classical-control treatment in Franklin, Powell, and Emami-Naeini, Feedback Control of Dynamic Systems. The root-locus conditions, asymptotic construction, departure and arrival limits, repeated-root condition, and gain/phase margin definitions are derived above. The original numerical records are retained: both traced loci, the displayed departure-angle validation from the reported four configurations, the positive- and negative-gain breakaway candidates, and the margin table cross-checked against the Routh boundary. The additional calculations are symbolic; the identity GM=6/K follows exactly from the same characteristic equation that gives the imaginary-axis crossing, and no new numerical traces or simulation results are claimed.
