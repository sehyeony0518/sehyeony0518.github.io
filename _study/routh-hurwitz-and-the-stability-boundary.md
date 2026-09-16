---
layout: study_note
title: "Routh–Hurwitz: Deciding Stability Without Finding a Single Root"
description: "A table of divisions answers a question about polynomial roots that has no formula past degree four, and turns 'is this stable?' into 'for which gains is this stable?'"
tab: "ai-foundations"
tab_title: "AI Theory"
category: "feedback-control"
category_title: "Feedback Control & Classical Design"
subgroup: "Transient Response & Stability"
order: 4
source: "Lecture notes, Ajou University"
written: true
updated: "2026-09-15"
---

Stability asks whether every root of a characteristic polynomial lies strictly in the left half-plane. Numerical root-finding can answer that question for a particular set of coefficients. Design often asks a different question: **for which values of a controller parameter does the property hold?**

Routh–Hurwitz converts that question into inequalities on coefficients. The useful distinction is not that numerical roots are unavailable, there are effective numerical methods, but that an array can describe an entire parameter interval symbolically.

The table is a record of polynomial elimination. Understanding that construction explains both the alternating coefficients and the exceptional cases.

## Core question and definition

**How can coefficient arithmetic count unstable roots, and how does that count become a stability region in controller parameters?**

Let

$$
P(s)=a_ns^n+a_{n-1}s^{n-1}+\cdots+a_1s+a_0,
\qquad n\ge1,
$$

have real coefficients and nonzero leading coefficient. Multiply the whole polynomial by minus one if necessary so that

$$
a_n>0.
$$

This changes none of its roots.

A polynomial is **Hurwitz** when every root satisfies

$$
\operatorname{Re}(p_i)<0.
$$

For a system, choose the polynomial appropriate to the stability question. A reduced transfer-function denominator describes its visible input–output poles. Internal stability requires the full characteristic polynomial, including modes that a particular transfer function may hide.

### The root-count theorem, stated precisely

For a real polynomial whose ordinary Routh array has no zero pivots, the number of sign changes down the first column equals the number of roots in the **open right half-plane**, counted with algebraic multiplicity.

When a zero pivot or an all-zero row occurs, use the corresponding extension described below before counting. Roots on the imaginary axis require separate identification; they are not RHP roots.

Thus the essential statement is

$$
\boxed{
N_{\mathrm{RHP}}
=
\text{number of first-column sign changes}
}.
$$

For the regular case, with $$a_n>0$$, strict stability is equivalent to every first-column entry being positive. An array that required an auxiliary-polynomial repair needs an additional boundary-root check: a repaired positive column can coexist with imaginary-axis roots.

In particular,

$$
\boxed{
N_{\mathrm{RHP}}=0
\quad\text{does not by itself imply}\quad
P\text{ is Hurwitz}.
}
$$

The criterion counts roots on one side of a boundary. By itself, it gives neither their distances from the imaginary axis nor the locations of transfer-function zeros.

### Why the first rows contain alternating coefficients

Every real polynomial splits uniquely into even and odd parts:

$$
P(s)=P_e(s)+P_o(s),
$$

where

$$
P_e(s)=\frac{P(s)+P(-s)}2,
\qquad
P_o(s)=\frac{P(s)-P(-s)}2.
$$

An even power survives the addition and cancels in the subtraction; an odd power does the reverse. Therefore,

$$
P_e(s)=a_0+a_2s^2+a_4s^4+\cdots,
$$

$$
P_o(s)=a_1s+a_3s^3+a_5s^5+\cdots.
$$

Why is this split useful for stability? On the imaginary axis,

$$
(j\omega)^{2k}=(-1)^k\omega^{2k},
$$

$$
(j\omega)^{2k+1}=j(-1)^k\omega^{2k+1}.
$$

Consequently,

$$
P(j\omega)=E(\omega)+jO(\omega),
$$

with real polynomials

$$
E(\omega)=\sum_k a_{2k}(-1)^k\omega^{2k},
$$

$$
O(\omega)=\sum_k a_{2k+1}(-1)^k\omega^{2k+1}.
$$

An imaginary-axis root must satisfy both

$$
E(\omega)=0,
\qquad
O(\omega)=0.
$$

The even and odd parts separate the two components of the polynomial along the stability boundary.

For the array, put the part containing the highest power first:

$$
F_n(s)=a_ns^n+a_{n-2}s^{n-2}+a_{n-4}s^{n-4}+\cdots,
$$

$$
F_{n-1}(s)=a_{n-1}s^{n-1}+a_{n-3}s^{n-3}+\cdots.
$$

If $$n$$ is even, these are the even and odd parts respectively. If $$n$$ is odd, the order reverses.

Their coefficient lists are exactly the first two rows:

| Row | First entry | Second entry | Third entry |
|---|---|---|---|
| $$s^n$$ | $$a_n$$ | $$a_{n-2}$$ | $$a_{n-4}$$ |
| $$s^{n-1}$$ | $$a_{n-1}$$ | $$a_{n-3}$$ | $$a_{n-5}$$ |

Missing coefficients must be entered as zeros. Otherwise the powers represented by subsequent columns shift and the calculation changes.

### Deriving the recurrence by eliminating a leading term

Suppose the two current row polynomials are

$$
F_m(s)=u_0s^m+u_1s^{m-2}+u_2s^{m-4}+\cdots,
$$

$$
F_{m-1}(s)=v_0s^{m-1}+v_1s^{m-3}+v_2s^{m-5}+\cdots,
$$

with $$v_0\ne0$$.

Multiplying the second polynomial by $$s$$ aligns its powers with the first. To cancel the leading term, subtract

$$
\frac{u_0}{v_0}sF_{m-1}(s).
$$

Define the remainder

$$
\begin{aligned}
F_{m-2}(s)
&=F_m(s)-\frac{u_0}{v_0}sF_{m-1}(s)\\
&=\left(u_1-\frac{u_0v_1}{v_0}\right)s^{m-2}
+\left(u_2-\frac{u_0v_2}{v_0}\right)s^{m-4}
+\cdots.
\end{aligned}
$$

Thus the next row entries are

$$
\boxed{
w_j=
\frac{v_0u_{j+1}-u_0v_{j+1}}{v_0}
}.
$$

In particular,

$$
w_0=\frac{v_0u_1-u_0v_1}{v_0}.
$$

This is the familiar determinant calculation, with its sign fixed by the elimination:

$$
w_0=
-\frac1{v_0}
\begin{vmatrix}
u_0&u_1\\
v_0&v_1
\end{vmatrix}.
$$

Then repeat using $$F_{m-1}$$ and $$F_{m-2}$$.

The construction is a polynomial remainder sequence. In the regular case,

$$
\frac{F_m}{F_{m-1}}
=
\frac{u_0}{v_0}s+\frac{F_{m-2}}{F_{m-1}}
=
\frac{u_0}{v_0}s+
\frac{1}{F_{m-1}/F_{m-2}}.
$$

Repeated elimination therefore also generates a continued-fraction structure. This is the connection to Euclidean and Sturm-like methods: successive remainders retain information about the original polynomials through their signs and common factors.

The elimination derives the array. The Routh–Hurwitz theorem supplies the additional result that its first-column sign variations count RHP roots; that conclusion does not follow merely from noticing alternating coefficients.

## Key concepts

### Why every coefficient must be present and have the same sign

Assume every root lies strictly in the LHP.

Each real root can be written $$-\alpha$$ with $$\alpha>0$$ and contributes a factor

$$
s+\alpha.
$$

Each nonreal conjugate pair can be written

$$
-\sigma\pm j\omega,
\qquad \sigma>0.
$$

Its real quadratic factor is

$$
\begin{aligned}
(s+\sigma-j\omega)(s+\sigma+j\omega)
&=(s+\sigma)^2+\omega^2\\
&=s^2+2\sigma s+(\sigma^2+\omega^2).
\end{aligned}
$$

Every coefficient in either type of factor is strictly positive. Multiplying such factors produces coefficients that are sums of positive products. No power between the leading term and constant term is missing.

With the positive leading-coefficient normalization,

$$
\boxed{
P\text{ Hurwitz}
\quad\Longrightarrow\quad
a_k>0\text{ for every }k.
}
$$

Before normalization, this says all coefficients must be nonzero and have the same sign.

A zero or a coefficient of the opposite sign therefore rules out strict LHP stability. It does not necessarily prove an RHP root: a polynomial can instead have roots on the imaginary axis.

The converse is false. Positive coefficients rule out positive **real** roots because

$$
P(s)>0\qquad\text{for real }s>0,
$$

but complex RHP roots can still occur.

### Positive coefficients are not sufficient: a complete counterexample

Use one of the original validation polynomials:

$$
P(s)=s^4+2s^3+3s^2+4s+5.
$$

The first rows are

$$
F_4=s^4+3s^2+5,
\qquad
F_3=2s^3+4s.
$$

Eliminate:

$$
\begin{aligned}
F_2
&=F_4-\frac12sF_3\\
&=(s^4+3s^2+5)-(s^4+2s^2)\\
&=s^2+5.
\end{aligned}
$$

Next,

$$
\begin{aligned}
F_1
&=F_3-2sF_2\\
&=(2s^3+4s)-(2s^3+10s)\\
&=-6s.
\end{aligned}
$$

Finally,

$$
F_0
=F_2-\frac{1}{-6}sF_1
=(s^2+5)-s^2
=5.
$$

The full array is

| Row | First entry | Second entry | Third entry |
|---|---|---|---|
| $$s^4$$ | $$1$$ | $$3$$ | $$5$$ |
| $$s^3$$ | $$2$$ | $$4$$ | $$0$$ |
| $$s^2$$ | $$1$$ | $$5$$ | $$0$$ |
| $$s^1$$ | $$-6$$ | $$0$$ | $$0$$ |
| $$s^0$$ | $$5$$ | $$0$$ | $$0$$ |

The first-column signs are

$$
+,\ +,\ +,\ -,\ +.
$$

There are two sign changes, so there are two RHP roots despite every original coefficient being positive.

### What a zero means depends on whether the entire row vanishes

The recurrence divides by the leading entry of the preceding row. Two different failures are possible:

| Situation | Polynomial interpretation | Required action |
|---|---|---|
| Leading entry zero, later entry nonzero | The remainder has lower degree than the row label expects | Replace the zero pivot by $$\varepsilon>0$$ and read limiting signs |
| Entire row zero | The elimination has reached an exact common factor | Form the auxiliary polynomial and use its derivative |

Neither case permits simply deleting the row or counting the zero as a positive entry.

If the original constant term is zero, first identify roots at the origin explicitly. If

$$
a_0=\cdots=a_{q-1}=0,
\qquad a_q\ne0,
$$

then

$$
P(s)=s^qQ(s),
\qquad Q(0)\ne0.
$$

There are $$q$$ roots at the origin, counted with multiplicity. Apply the Routh calculation to $$Q$$ to count its RHP roots. The original polynomial is already known not to be strictly Hurwitz.

### Degenerate case 1: a zero pivot with a nonzero remainder

Take the original fifth-degree example

$$
P(s)=s^5+2s^4+2s^3+4s^2+11s+10.
$$

Its initial row polynomials are

$$
F_5=s^5+2s^3+11s,
$$

$$
F_4=2s^4+4s^2+10.
$$

Elimination gives

$$
\begin{aligned}
F_3
&=F_5-\frac12sF_4\\
&=(s^5+2s^3+11s)-(s^5+2s^3+5s)\\
&=6s.
\end{aligned}
$$

The nominal $$s^3$$ row is therefore

$$
[0,\ 6,\ 0].
$$

The polynomial is not zero; its degree has dropped farther than the regular recursion expects.

Replace only the leading zero with $$\varepsilon>0$$:

$$
[0,\ 6,\ 0]\longrightarrow[\varepsilon,\ 6,\ 0].
$$

The next row has first entry

$$
b_\varepsilon
=
\frac{4\varepsilon-2\cdot6}{\varepsilon}
=
4-\frac{12}{\varepsilon},
$$

and second entry

$$
\frac{10\varepsilon-2\cdot0}{\varepsilon}=10.
$$

The following first entry is

$$
\begin{aligned}
c_\varepsilon
&=\frac{6b_\varepsilon-10\varepsilon}{b_\varepsilon}\\
&=6-\frac{10\varepsilon}{b_\varepsilon}\\
&=6-\frac{10\varepsilon^2}{4\varepsilon-12}.
\end{aligned}
$$

The completed regularized array is

| Row | First entry | Second entry | Third entry |
|---|---|---|---|
| $$s^5$$ | $$1$$ | $$2$$ | $$11$$ |
| $$s^4$$ | $$2$$ | $$4$$ | $$10$$ |
| $$s^3$$ | $$\varepsilon$$ | $$6$$ | $$0$$ |
| $$s^2$$ | $$b_\varepsilon$$ | $$10$$ | $$0$$ |
| $$s^1$$ | $$c_\varepsilon$$ | $$0$$ | $$0$$ |
| $$s^0$$ | $$10$$ | $$0$$ | $$0$$ |

For sufficiently small positive $$\varepsilon$$,

$$
b_\varepsilon=4-\frac{12}{\varepsilon}<0.
$$

Since $$b_\varepsilon<0$$,

$$
c_\varepsilon=6-\frac{10\varepsilon}{b_\varepsilon}>6>0,
$$

and

$$
\lim_{\varepsilon\to0^+}c_\varepsilon=6.
$$

The limiting sign sequence is

$$
+,\ +,\ +,\ -,\ +,\ +.
$$

There are two sign changes, hence two RHP roots.

The divergent entry $$b_\varepsilon\to-\infty$$ is not a pole moving to infinity. It is an intermediate coefficient in a regularized calculation. The division obstruction is removable by the limiting procedure even though every intermediate entry need not have a finite limit.

Nor does a zero pivot by itself imply an imaginary-axis root. For this example,

$$
\operatorname{Re}P(j\omega)
=2\omega^4-4\omega^2+10.
$$

Completing the square,

$$
\operatorname{Re}P(j\omega)
=
2\left[(\omega^2-1)^2+4\right]>0
$$

for every real $$\omega$$. Therefore $$P(j\omega)$$ cannot vanish: this polynomial has no imaginary-axis roots.

Use a symbolic $$\varepsilon$$ and its limiting signs. An arbitrary small floating-point replacement can obscure cancellation or produce misleading intermediate magnitudes.

### Degenerate case 2: why an entire zero row reveals a common factor

Suppose an elimination step produces

$$
F_{m-2}(s)=0.
$$

Then

$$
F_m(s)=\frac{u_0}{v_0}sF_{m-1}(s).
$$

The preceding row polynomial divides the one above it. Work backward through the recurrence:

$$
F_{k}(s)
=
\frac{\text{leading coefficient of }F_k}
{\text{leading coefficient of }F_{k-1}}
sF_{k-1}(s)+F_{k-2}(s).
$$

If a polynomial divides two consecutive remainders, it also divides the preceding polynomial. Continuing backward shows that the last nonzero remainder divides both initial parity parts and hence their sum $$P$$.

This last nonzero row defines the **auxiliary polynomial** $$A(s)$$.

Its powers differ by two, so it has a definite parity:

$$
A(-s)=A(s)
\quad\text{or}\quad
A(-s)=-A(s).
$$

Consequently,

$$
A(r)=0
\quad\Longrightarrow\quad
A(-r)=0.
$$

Its nonzero roots occur in origin-symmetric pairs. With real coefficients, conjugation adds another symmetry: a root off both axes is accompanied by its negative, its conjugate, and the negative of its conjugate.

After roots at the origin have been removed, an auxiliary factor with nonzero constant term is even.

The important conclusion is **origin symmetry**, not automatically “imaginary-axis poles.” Symmetric roots can be imaginary, real with opposite signs, or in complex quartets.

### Why differentiating the auxiliary polynomial is the repair

Suppose the auxiliary row represents

$$
A(s)=b_0s^m+b_1s^{m-2}+b_2s^{m-4}+\cdots.
$$

Its derivative is

$$
A'(s)
=
mb_0s^{m-1}
+(m-2)b_1s^{m-3}
+(m-4)b_2s^{m-5}
+\cdots.
$$

These are precisely the powers needed by the missing next row. The replacement coefficients are therefore

$$
mb_0,\quad (m-2)b_1,\quad (m-4)b_2,\quad\ldots.
$$

But matching powers alone does not explain why this preserves the root count. The reason is a limiting displacement of the symmetric factor.

Consider

$$
A_\delta(s)=A(s+\delta),
\qquad \delta>0.
$$

If $$r$$ is a root of $$A$$, then $$r-\delta$$ is a root of $$A_\delta$$. Thus a sufficiently small positive shift:

- leaves strictly RHP roots in the RHP;
- leaves strictly LHP roots in the LHP;
- moves imaginary-axis roots into the LHP.

It therefore preserves the number of strictly RHP roots while resolving boundary roots to the left.

For an even auxiliary polynomial, Taylor expansion gives

$$
A(s+\delta)
=
A(s)+\delta A'(s)
+\frac{\delta^2}{2}A''(s)
+\frac{\delta^3}{6}A'''(s)+\cdots.
$$

The same-parity and opposite-parity parts are

$$
A(s)+\frac{\delta^2}{2}A''(s)+\cdots
$$

and

$$
\delta A'(s)+\frac{\delta^3}{6}A'''(s)+\cdots,
$$

respectively.

Divide the second part by the positive number $$\delta$$. As $$\delta\to0^+$$, the two row polynomials approach

$$
A(s),\qquad A'(s).
$$

This limiting construction explains the derivative row: it supplies the missing parity component associated with an infinitesimal leftward displacement. It is the standard continuation of the root-count procedure, not an assertion that the roots of $$A'$$ replace the system's roots.

If further zero rows occur, repeat the auxiliary-polynomial procedure. Retain and examine the original auxiliary factor to identify boundary roots and their multiplicities.

Multiplying a row by a positive constant does not change the sign count. Multiplying it by a negative constant is not an innocuous simplification.

### Working the all-zero-row example completely

Use the other original fifth-degree example:

$$
P(s)=s^5+7s^4+6s^3+42s^2+8s+56.
$$

The first rows are

$$
F_5=s^5+6s^3+8s,
$$

$$
F_4=7s^4+42s^2+56.
$$

They satisfy

$$
F_5=\frac17sF_4.
$$

Hence

$$
F_3=F_5-\frac17sF_4=0.
$$

The auxiliary polynomial is the row above:

$$
A(s)=7s^4+42s^2+56.
$$

Differentiate:

$$
A'(s)=28s^3+84s.
$$

Replace the zero $$s^3$$ row by

$$
[28,\ 84,\ 0].
$$

The next entries are

$$
\frac{28\cdot42-7\cdot84}{28}=21,
$$

$$
\frac{28\cdot56-7\cdot0}{28}=56.
$$

Then

$$
\frac{21\cdot84-28\cdot56}{21}
=
\frac{196}{21}
=
\frac{28}{3}.
$$

The completed array is

| Row | First entry | Second entry | Third entry |
|---|---|---|---|
| $$s^5$$ | $$1$$ | $$6$$ | $$8$$ |
| $$s^4$$ | $$7$$ | $$42$$ | $$56$$ |
| $$s^3$$, replaced | $$28$$ | $$84$$ | $$0$$ |
| $$s^2$$ | $$21$$ | $$56$$ | $$0$$ |
| $$s^1$$ | $$28/3$$ | $$0$$ | $$0$$ |
| $$s^0$$ | $$56$$ | $$0$$ | $$0$$ |

Every first-column entry is positive, so there are no RHP roots.

Now inspect the auxiliary polynomial instead of concluding strict stability:

$$
\begin{aligned}
A(s)
&=7(s^4+6s^2+8)\\
&=7(s^2+2)(s^2+4).
\end{aligned}
$$

Its roots are

$$
s=\pm j\sqrt2,\qquad s=\pm2j.
$$

The complete original polynomial factors as

$$
\begin{aligned}
P(s)
&=(s+7)(s^4+6s^2+8)\\
&=(s+7)(s^2+2)(s^2+4).
\end{aligned}
$$

There are four simple imaginary-axis roots and one LHP root at $$-7$$. This agrees with the original validation result: zero RHP roots, four roots on the axis.

The unforced modes associated with the imaginary roots do not decay. This is not strict asymptotic stability, and a transfer function retaining these poles is not BIBO stable.

### An all-zero row need not mean marginal stability

A symbolic counterexample makes the distinction explicit:

$$
P(s)=s^2-a^2,
\qquad a>0.
$$

The first two rows are

$$
[1,\ -a^2],
\qquad
[0,\ 0].
$$

The auxiliary polynomial is $$A=P$$ and

$$
A'(s)=2s.
$$

The repaired array is

| Row | First entry | Second entry |
|---|---|---|
| $$s^2$$ | $$1$$ | $$-a^2$$ |
| $$s^1$$, replaced | $$2$$ | $$0$$ |
| $$s^0$$ | $$-a^2$$ | $$0$$ |

Its signs are

$$
+,\ +,\ -,
$$

so it has one RHP root. Direct factorization confirms

$$
P(s)=(s-a)(s+a).
$$

The roots are origin-symmetric, but they are real, not imaginary. An all-zero row is therefore a reason to inspect the auxiliary factor, not a stability verdict.

### Preserved validation records

The original exact-arithmetic implementation was checked against numerical roots on these six polynomials. The records are reproduced unchanged:

```text
 s^3+3s^2+2s+6         Routh: 0 RHP | actual 0 RHP, 2 on jw-axis   OK
 s^3+3s^2+2s+1         Routh: 0 RHP | actual 0 RHP, 0 on jw-axis   OK
 s^3+3s^2+2s+10        Routh: 2 RHP | actual 2 RHP                 OK
 s^4+2s^3+3s^2+4s+5    Routh: 2 RHP | actual 2 RHP                 OK
 s^5+2s^4+2s^3+4s^2+11s+10   Routh: 2 RHP | actual 2 RHP           OK
 s^5+7s^4+6s^3+42s^2+8s+56   Routh: 0 RHP | actual 0, 4 on jw-axis OK
```

The first and last rows show why the number of RHP roots and the number of imaginary-axis roots must be reported separately.

### Gain example 1: deriving the complete interval

Take unity negative feedback around

$$
L_K(s)=\frac{K}{s(s+1)(s+2)}.
$$

The characteristic equation is

$$
1+L_K(s)=0,
$$

or, before cancelling any factors,

$$
s(s+1)(s+2)+K=0.
$$

Expand:

$$
(s+1)(s+2)=s^2+3s+2,
$$

so

$$
P_K(s)=s^3+3s^2+2s+K.
$$

The first two row polynomials are

$$
F_3=s^3+2s,
\qquad
F_2=3s^2+K.
$$

The next remainder is

$$
\begin{aligned}
F_1
&=F_3-\frac13sF_2\\
&=(s^3+2s)-\left(s^3+\frac K3s\right)\\
&=\frac{6-K}{3}s.
\end{aligned}
$$

Write

$$
b=\frac{6-K}{3}.
$$

When $$b\ne0$$,

$$
F_0=F_2-\frac3b sF_1
=(3s^2+K)-3s^2
=K.
$$

Thus the full array is

| Row | First entry | Second entry |
|---|---|---|
| $$s^3$$ | $$1$$ | $$2$$ |
| $$s^2$$ | $$3$$ | $$K$$ |
| $$s^1$$ | $$(6-K)/3$$ | $$0$$ |
| $$s^0$$ | $$K$$ | $$0$$ |

The first two entries are already positive. Strict stability requires

$$
\frac{6-K}{3}>0
\quad\Longleftrightarrow\quad
K<6,
$$

and

$$
K>0.
$$

Therefore,

$$
\boxed{0<K<6}.
$$

The coefficient test alone would only require $$K>0$$. The additional Routh inequality supplies the upper limit.

Outside the boundaries:

| Gain range | First-column signs | RHP roots |
|---|---|---|
| $$K<0$$ | $$+,+,+,-$$ | $$1$$ |
| $$0<K<6$$ | $$+,+,+,+$$ | $$0$$ |
| $$K>6$$ | $$+,+,-,+$$ | $$2$$ |

The boundary values require direct examination.

#### Lower boundary: a root at the origin

At $$K=0$$,

$$
P_0(s)=s(s+1)(s+2).
$$

The roots are $$0,-1,-2$$. There is no RHP root, but the origin root prevents strict stability.

This is a characteristic-polynomial statement. Substituting zero gain into a particular reference transfer function and obtaining zero output would not remove the system's free modes.

#### Upper boundary: an imaginary-axis pair

At $$K=6$$, the $$s^1$$ row is entirely zero:

$$
[0,\ 0].
$$

The auxiliary polynomial from the $$s^2$$ row is

$$
A(s)=3s^2+6=3(s^2+2).
$$

Its derivative is

$$
A'(s)=6s.
$$

Replacing the row and continuing gives

| Row | First entry | Second entry |
|---|---|---|
| $$s^3$$ | $$1$$ | $$2$$ |
| $$s^2$$ | $$3$$ | $$6$$ |
| $$s^1$$, replaced | $$6$$ | $$0$$ |
| $$s^0$$ | $$6$$ | $$0$$ |

There are no RHP roots, but

$$
A(s)=0
\quad\Longrightarrow\quad
s=\pm j\sqrt2.
$$

The remaining factor follows by multiplication:

$$
(s+3)(s^2+2)
=s^3+3s^2+2s+6.
$$

Thus the marginal roots at exactly $$K=6$$ are

$$
\boxed{-3,\quad \pm j\sqrt2}.
$$

The original gain sweep is retained unchanged:

```text
 K=1.0: max Re(pole) = -0.337641  stable
 K=5.9: max Re(pole) = -0.004568  stable
 K=6.0: max Re(pole) = +0.000000  marginal   <- boundary
 K=6.5: max Re(pole) = +0.022186  UNSTABLE
```

Here “marginal” describes the nondecaying, simple imaginary-axis modes. It does not mean strict LHP or BIBO stability.

### Gain example 2: stabilizing an unstable plant within a window

Now take

$$
G(s)=\frac1{(s-1)(s+2)(s+3)}.
$$

The plant has a pole at $$s=+1$$ and is unstable before feedback.

With proportional gain $$K$$ and unity negative feedback, the characteristic polynomial is

$$
P_K(s)=(s-1)(s+2)(s+3)+K.
$$

Expand the factors explicitly:

$$
(s+2)(s+3)=s^2+5s+6,
$$

$$
\begin{aligned}
(s-1)(s^2+5s+6)
&=s^3+5s^2+6s-s^2-5s-6\\
&=s^3+4s^2+s-6.
\end{aligned}
$$

Therefore,

$$
P_K(s)=s^3+4s^2+s+(K-6).
$$

The first row polynomials are

$$
F_3=s^3+s,
\qquad
F_2=4s^2+(K-6).
$$

Eliminate:

$$
\begin{aligned}
F_1
&=F_3-\frac14sF_2\\
&=(s^3+s)-\left(s^3+\frac{K-6}{4}s\right)\\
&=\left(1-\frac{K-6}{4}\right)s\\
&=\frac{10-K}{4}s.
\end{aligned}
$$

The final remainder is $$K-6$$, so the full array is

| Row | First entry | Second entry |
|---|---|---|
| $$s^3$$ | $$1$$ | $$1$$ |
| $$s^2$$ | $$4$$ | $$K-6$$ |
| $$s^1$$ | $$(10-K)/4$$ | $$0$$ |
| $$s^0$$ | $$K-6$$ | $$0$$ |

The conditions are

$$
\frac{10-K}{4}>0
\quad\Longleftrightarrow\quad
K<10,
$$

and

$$
K-6>0
\quad\Longleftrightarrow\quad
K>6.
$$

Hence

$$
\boxed{6<K<10}.
$$

This window has two distinct mechanisms at its boundaries.

At $$K=6$$,

$$
P_6(s)=s(s^2+4s+1).
$$

The quadratic roots are

$$
s=\frac{-4\pm\sqrt{16-4}}2
=-2\pm\sqrt3.
$$

Both are negative because $$\sqrt3<2$$. The remaining root is at the origin.

At $$K=10$$,

$$
\begin{aligned}
P_{10}(s)
&=s^3+4s^2+s+4\\
&=(s+4)(s^2+1).
\end{aligned}
$$

The roots are $$-4$$ and $$\pm j$$. The corresponding auxiliary polynomial is

$$
A(s)=4s^2+4,
$$

whose derivative $$8s$$ supplies the missing $$s^1$$ row.

Away from these boundaries:

| Gain range | First-column signs | RHP roots |
|---|---|---|
| $$K<6$$ | $$+,+,+,-$$ | $$1$$ |
| $$6<K<10$$ | $$+,+,+,+$$ | $$0$$ |
| $$K>10$$ | $$+,+,-,+$$ | $$2$$ |

The original numerical sweep is reproduced unchanged:

```text
 K=5.0:  max Re(pole) = +0.377203  UNSTABLE   (too little gain)
 K=7.0:  max Re(pole) = -0.096850  stable
 K=9.0:  max Re(pole) = -0.030267  stable
 K=11.0: max Re(pole) = +0.028635  UNSTABLE   (too much gain)
```

Too little gain leaves an unstable mode; too much gain produces a different instability. Feedback changes the characteristic polynomial, but increasing gain is not monotonically stabilizing.

### Why unstable-pole cancellation does not establish internal stability

A controller zero can cancel a plant pole in a particular transfer function without removing the internal mode.

Consider

$$
G(s)=\frac1{s-1},
\qquad
D(s)=\frac{s-1}{s+a},
\qquad a>0.
$$

The nominal loop transfer function simplifies to

$$
D(s)G(s)=\frac1{s+a}.
$$

The reference-to-output transfer function appears stable:

$$
\begin{aligned}
T(s)
&=\frac{DG}{1+DG}\\
&=\frac{1/(s+a)}{1+1/(s+a)}\\
&=\frac1{s+a+1}.
\end{aligned}
$$

But retaining the plant and controller denominators gives the characteristic polynomial

$$
\begin{aligned}
P_{\mathrm{cl}}(s)
&=(s-1)(s+a)+(s-1)\\
&=(s-1)(s+a+1).
\end{aligned}
$$

The unstable mode at $$s=1$$ is still present. It is cancelled from this particular reference path.

To expose it, introduce a disturbance $$W$$ at the plant input, after the controller. With the reference set to zero,

$$
Y=G(-DY+W).
$$

Therefore,

$$
(1+GD)Y=GW,
$$

and

$$
\begin{aligned}
\frac{Y}{W}
&=\frac{G}{1+GD}\\
&=\frac{1/(s-1)}{1+1/(s+a)}\\
&=\frac{s+a}{(s-1)(s+a+1)}.
\end{aligned}
$$

The unstable pole is visible in the disturbance response even under exact nominal cancellation.

Uncertain parameters create an additional problem. If the actual plant pole is $$1+\Delta$$ while the controller zero remains at $$1$$,

$$
D(s)G_{\mathrm{actual}}(s)
=
\frac{s-1}{(s+a)(s-1-\Delta)},
$$

and the nominal cancellation no longer occurs when $$\Delta\ne0$$.

Component tolerances such as 1% or 5%, and parameter drift, illustrate why exact matching should not be presumed. The internal-mode calculation shows that uncertainty is not even necessary for cancellation to be an inadequate stability argument.

### What the criterion does not tell you

**It does not directly measure decay rate.** A pole at $$-0.001$$ satisfies the LHP condition, but its mode

$$
e^{-0.001t}
$$

has time constant

$$
\tau=\frac1{0.001}.
$$

Strict stability alone does not decide whether that response is fast enough.

Nor is the magnitude of a first-column entry a universal distance to instability. Positive row rescaling can change that magnitude while leaving the root count unchanged.

A specified decay margin can nevertheless be tested with a new polynomial. To require

$$
\operatorname{Re}(p_i)<-\alpha,
\qquad \alpha>0,
$$

define

$$
Q(z)=P(z-\alpha).
$$

If $$P(p_i)=0$$, then

$$
Q(p_i+\alpha)=P(p_i)=0.
$$

Thus the roots of $$Q$$ are $$p_i+\alpha$$, and

$$
Q\text{ Hurwitz}
\quad\Longleftrightarrow\quad
\operatorname{Re}(p_i)<-\alpha.
$$

This requires applying the criterion to the shifted polynomial; the original sign count does not report the margin automatically.

**It does not locate transfer-function zeros.** Applying the array to a characteristic polynomial counts that polynomial's roots. It contains no independent information about a transfer-function numerator. However, a plant numerator can enter the closed-loop characteristic equation through feedback, so “the criterion does not inspect zeros” does not mean zeros are irrelevant to design.

**It does not establish robustness without an uncertainty model.** A nominal gain interval is useful, but coefficient uncertainty can move its boundaries. Multiple uncertain parameters require simultaneous inequalities rather than a single nominal calculation.

### Revision checklist

| Question | Calculation to reproduce | Assumption or common mistake |
|---|---|---|
| Which polynomial should I test? | Derive the characteristic equation before cancelling factors | A reduced reference transfer function can hide internal modes |
| Why alternating coefficients? | Split $$P$$ into its even and odd parts | The split also separates real and imaginary parts on $$j\omega$$ |
| How is a new row formed? | Subtract $$\frac{u_0}{v_0}sF_{m-1}$$ from $$F_m$$ | Preserve missing coefficients as zeros |
| What does a sign change count? | Read successive signs down the first column | RHP roots are counted with multiplicity |
| Does zero RHP count prove strict stability? | Inspect origin factors and auxiliary polynomials | Imaginary-axis roots are not RHP roots |
| Why must all coefficients have the same sign? | Multiply positive-coefficient real LHP factors | Necessary, not sufficient |
| What if only the first entry is zero? | Replace it by $$\varepsilon>0$$ and take limiting signs | Do not replace the whole row |
| What if the entire row is zero? | Form $$A$$ from the row above and insert coefficients of $$A'$$ | This indicates a common origin-symmetric factor |
| Why use the derivative? | Expand $$A(s+\delta)$$ and separate its parity parts | The derivative is a limiting repair, not a replacement characteristic polynomial |
| Does a zero row imply imaginary roots? | Factor or solve the auxiliary polynomial | Real opposite-sign pairs and complex quartets are also possible |
| How is a gain interval found? | Require all regular first-column entries positive | Examine equality cases separately |
| Can more gain destabilize? | Compare the first-column signs on both sides of each boundary | A stabilizing interval can have both lower and upper limits |
| Does the table give a decay margin? | Apply Routh to $$P(z-\alpha)$$ for a specified margin | Raw entry magnitudes are not pole distances |
| Is pole–zero cancellation enough? | Check internal modes and other input–output paths | Nominal cancellation can hide an unstable mode |

## Why it matters for my work

The useful habit is to turn a desired property into inequalities on parameters before sampling designs. A numerical sweep checks selected points; a symbolic argument explains the interval between them.

The cancellation example adds a second habit: a favourable response along one measured path does not prove that every internal mode is stable.

## What I have not resolved

I want to work through a multi-parameter example with coefficient uncertainty and compare its admissible region with a required decay-rate margin. I also want to connect the algebraic gain boundaries here to the frequency-domain margins in the next note.

---

Sources: Ajou University lecture notes and the standard classical-control treatment in Franklin, Powell, and Emami-Naeini, Feedback Control of Dynamic Systems. The even/odd polynomial construction, Routh–Hurwitz root-count theorem, zero-pivot and auxiliary-polynomial procedures, and internal-stability distinction are standard linear-systems results. The original numerical records are retained: six validation polynomials checked using exact-rational Routh arrays and numerical roots, and both gain-window sweeps checked pole-by-pole. The added arrays, factorizations, boundary calculations, and cancellation example are derived symbolically; no new numerical root or simulation results are claimed.
