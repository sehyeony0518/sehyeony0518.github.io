---
layout: study_note
title: "Matrix Calculus for Reading Papers: Determinants, Cofactors, and the Gaussian MLE"
description: "The minimum of matrix differentiation that lets you read a derivation instead of skipping it — and the derivation of the Gaussian mean and covariance estimators that it exists to serve."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "algebra-and-optimisation"
category_title: "Linear Algebra & Optimisation"
order: 2
source: "Independent study"
written: true
updated: "2026-09-15"
---

Reading a paper at full detail is rarely worth the time, and reading one without any detail is not reading. The useful middle is abstraction: recognising that a block of equations is *solving this kind of problem, in this kind of way*, and moving on with the intention of returning if it matters. That move is only available if you can see what kind of problem it is — and the notation is what tells you. Skipping the mathematics does not buy speed; it removes the ability to abstract, which is what would have bought the speed.

The honest form of the claim is uncomfortable but worth stating: "I understood the paper but not the equations" is often a description of a limit that has not been recognised as one.

## Core question and definition

Two kinds of mathematics are in play, and both are needed.

The **formal** kind defines a derivative as a limit and proves things from the definition. The **engineer's** kind asks what changes when the input is perturbed: $$(x+\delta)^3 = x^3 + 3x^2\delta + O(\delta^2)$$, so the rate is $$3x^2$$. The second is less rigorous and closer to the physical meaning, and it is frequently what the author was thinking before the formal version was written down. Historically the intuition often precedes the formulation. When reading, you want to be able to move in both directions.

This note collects the matrix machinery that shows up repeatedly in probabilistic machine learning, in the engineer's style, and then spends it on one worked problem: the [maximum-likelihood estimates](/study/estimation-likelihood-and-posterior/) of a Gaussian's mean and covariance. A second problem in the same family — recovering the rotation that aligns two sets of corresponding points — is solved by the same tools and was settled decades ago.[^kabsch]

## Key concepts

### Determinant, minor, cofactor, adjugate

For a square $$A$$, the **minor** $$M_{ij}$$ is the determinant of what remains after deleting row $$i$$ and column $$j$$. The **cofactor** attaches the checkerboard sign,

$$
C_{ij} = (-1)^{i+j} M_{ij},
$$

and the determinant is the expansion along any row,

$$
\det A = \sum_j a_{ij}\,C_{ij}.
$$

This is recursive: a $$4\times 4$$ determinant is four $$3\times3$$ determinants, each of which is three $$2\times2$$ determinants. Collecting every cofactor into a matrix $$C$$ and transposing gives the **adjugate**, $$\operatorname{adj}(A) = C^{\mathsf T}$$, and from it

$$
A^{-1} = \frac{\operatorname{adj}(A)}{\det A}.
$$

In principle that inverts any invertible matrix. In practice nobody computes it this way — the cost is factorial, and [LU or Cholesky factorisation](/study/linear-algebra-for-representation-analysis/) is what actually runs. The adjugate formula earns its place because it is what you differentiate, not what you evaluate.

A note on names: the Korean renderings (여인수, 여인자) carry none of the meaning and collide with each other. "Cofactor" is the term that can be looked up.

### The derivative with respect to a matrix, and the convention trap

Define $$\partial f/\partial A$$ as the matrix whose $$(i,j)$$ entry is $$\partial f / \partial a_{ij}$$. That is the complete and unambiguous statement, and it is all the definition requires. Everything that follows is bookkeeping for writing it compactly.

The compact form is the matrix analogue of $$df = (\partial f/\partial x)^{\mathsf T} dx$$:

$$
df = \operatorname{tr}\!\left( \left(\frac{\partial f}{\partial A}\right)^{\!\mathsf T} dA \right).
$$

This is also the *method*. To find a matrix derivative, expand $$f(A + \Delta A) - f(A)$$, keep the terms linear in $$\Delta A$$, push them into a single trace with $$\Delta A$$ on the right, and read off what is sitting to its left.

**Where the trap is.** Whether the transpose belongs in the definition of $$\partial f/\partial A$$ or in the update rule that uses it is a *convention*, not a fact. Write a gradient step as $$A_{\text{new}} = A_{\text{old}} + \eta\,\partial f/\partial A$$ and you have implicitly chosen one; textbooks differ, and a derivation that silently switches midway produces a transposed answer that still typechecks. Pick one and hold it. This note puts no transpose in the definition and lets it appear in the results.

### The results worth memorising

Using $$\operatorname{tr}(AB) = \operatorname{tr}(BA)$$ throughout:

$$
\frac{\partial\,\operatorname{tr}(WA)}{\partial A} = W^{\mathsf T},
\qquad
\frac{\partial \log\det A}{\partial A} = A^{-\mathsf T},
\qquad
\frac{\partial \det A}{\partial A} = \det(A)\,A^{-\mathsf T}.
$$

The $$\log\det$$ result comes straight from the cofactor expansion. Since $$\det A = \sum_j a_{ij} C_{ij}$$ and no cofactor $$C_{ij}$$ contains $$a_{ij}$$, differentiating picks out exactly one term:

$$
\frac{\partial \det A}{\partial a_{ij}} = C_{ij}
\;\Longrightarrow\;
\frac{\partial \det A}{\partial A} = C = \operatorname{adj}(A)^{\mathsf T} = \det(A)\,A^{-\mathsf T},
$$

and dividing by $$\det A$$ gives $$\partial \log\det A/\partial A = A^{-\mathsf T}$$. Equivalently, in differential form, $$\log\det(A + \Delta A) - \log\det A \approx \operatorname{tr}(A^{-1}\Delta A)$$ — which is worth checking numerically once on a small random matrix, because seeing the two sides agree to three digits is more convincing than the derivation.

For quadratic forms, with $$x$$ fixed:

$$
\frac{\partial\,(x^{\mathsf T} A x)}{\partial A} = x x^{\mathsf T},
\qquad
\frac{\partial\,(x^{\mathsf T} A^{-1} x)}{\partial A} = -A^{-1} x x^{\mathsf T} A^{-1},
\qquad
\frac{\partial\,(x^{\mathsf T} A x)}{\partial x} = (A + A^{\mathsf T})\,x .
$$

The middle one looks unapproachable until you ask the perturbation question about the inverse itself. Requiring $$(A + \Delta A)(A^{-1} + \Delta B) = I$$ and dropping second-order terms gives

$$
(A+\Delta A)^{-1} \approx A^{-1} - A^{-1}\,\Delta A\,A^{-1},
$$

after which the result falls out in one line. Standard reference tables collect many more of these.[^mn][^giles]

### The worked problem: Gaussian maximum likelihood

For $$x_1,\dots,x_N$$ drawn i.i.d. from $$\mathcal{N}(\mu, \Sigma)$$, the log-likelihood, dropping the constant, is

$$
\ell(\mu,\Sigma) = -\frac{N}{2}\log\det\Sigma \;-\; \frac{1}{2}\sum_{i=1}^{N}(x_i-\mu)^{\mathsf T}\Sigma^{-1}(x_i-\mu).
$$

Every piece needed is now on the table. Writing $$S = \sum_i (x_i-\mu)(x_i-\mu)^{\mathsf T}$$ and using symmetry of $$\Sigma$$,

$$
\frac{\partial \ell}{\partial \Sigma} = -\frac{N}{2}\Sigma^{-1} + \frac{1}{2}\Sigma^{-1} S\, \Sigma^{-1} = 0 .
$$

Multiplying on both sides by $$\Sigma$$ clears the inverses and leaves $$N\Sigma = S$$, so

$$
\hat\Sigma = \frac{1}{N}\sum_i (x_i - \hat\mu)(x_i - \hat\mu)^{\mathsf T}.
$$

Differentiating in $$\mu$$ gives $$\sum_i \Sigma^{-1}(x_i - \mu) = 0$$, and since $$\Sigma^{-1}$$ is invertible, $$\hat\mu = \frac{1}{N}\sum_i x_i$$.

Two things this does **not** say. It does not say these are the best estimators — only that they maximise the likelihood, which is a different claim and one the [choice-of-estimator question](/study/choosing-an-estimator/) takes up directly; $$\hat\Sigma$$ is famously biased. And the derivation treated $$\Sigma$$ as a free matrix, ignoring that it must be symmetric and positive definite. Imposing symmetry would change the off-diagonal derivatives by a factor of two, which happens not to move the stationary point here. That it works out is a fact about this problem, not a general licence.

## Why it matters for my work

The narrow payoff is that $$\log\det$$ and $$\Sigma^{-1}$$ appear everywhere downstream — in [EM for mixtures](/study/why-em-works/), in variational objectives, in [MMSE estimation](/study/linear-mmse-and-the-wiener-filter/) — and reading those derivations at all requires this much.

The broader one concerns how claims get audited. Most of what a paper asserts about reliability is asserted in the derivation, not the results table: the independence assumptions, the point at which a posterior is replaced by a point estimate, the constraint that was quietly dropped because the answer came out the same anyway. A reader who skips the mathematics cannot see those choices and has no option but to accept the paper's own summary of what it established. That is precisely the position an audit is supposed to avoid. The unconstrained-$$\Sigma$$ step above is a small, benign instance of the general shape — and the only reason it can be called benign here is that someone checked.

---

[^mn]: Magnus, J. R., & Neudecker, H. (2019). *Matrix Differential Calculus with Applications in Statistics and Econometrics* (3rd ed.). Wiley. [10.1002/9781119541219](https://doi.org/10.1002/9781119541219)

[^giles]: Giles, M. B. (2008). Collected matrix derivative results for forward and reverse mode algorithmic differentiation. In *Advances in Automatic Differentiation*, 35–44. [10.1007/978-3-540-68942-3_4](https://doi.org/10.1007/978-3-540-68942-3_4)

[^kabsch]: Kabsch, W. (1976). A solution for the best rotation to relate two sets of vectors. *Acta Crystallographica Section A*, 32(5), 922–923. [10.1107/S0567739476001873](https://doi.org/10.1107/S0567739476001873)
