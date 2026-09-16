---
layout: study_note
title: "Optimising the Input: Visualisation, Style, and Adversarial Examples"
description: "What happens when the weights are frozen and the image becomes the free variable, and why the same procedure produces both a picture of a concept and a picture that fools the model."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Neural Networks & Representation"
order: 3
source: "Independent study"
written: true
updated: "2026-09-15"
---

Backpropagation can differentiate an objective with respect to the input as well as the weights. Freezing the weights changes which variables may move; it does not change the chain rule.

This produces several different experiments. Feature visualisation searches for inputs that strongly activate a chosen feature. Style transfer searches for an input whose feature statistics match selected references. An adversarial search looks for a nearby input that changes a decision or increases a loss.

The objective defines the desired behaviour. The feasible set or prior defines which changes are allowed. Both are necessary to understand what an optimised image establishes.

## Changing the variable while keeping the network fixed

Ordinary training solves an optimisation problem over parameters:

$$
\min_\theta
L\bigl(f_\theta(x),y\bigr).
$$

Input optimisation instead solves

$$
\min_x
L\bigl(f_\theta(x),y^\ast\bigr),
$$

with the parameters fixed. For a scalar objective built from a vector-valued network output,

$$
J(x)=\psi\bigl(f_\theta(x)\bigr),
$$

the input gradient is

$$
\nabla_xJ
=
J_{f_\theta}(x)^\top
\nabla_f\psi.
$$

To derive this, write the two differentials:

$$
\mathrm df=J_{f_\theta}(x)\,\mathrm dx,
\qquad
\mathrm dJ=(\nabla_f\psi)^\top\mathrm df.
$$

Substitution identifies the coefficient of the input differential:

$$
\mathrm dJ
=
\left[J_{f_\theta}(x)^\top\nabla_f\psi\right]^\top
\mathrm dx.
$$

The network weights still appear in this calculation. “Frozen” means that the optimisation does not update them. It does not mean that operations containing weights should be removed from the differentiation graph.

For a one-unit example, let

$$
f_w(x)=\operatorname{ReLU}(wx-1).
$$

At

$$
w=2,\qquad x=1,
$$

the activation is one, and

$$
\frac{\partial f_w}{\partial x}=2,
\qquad
\frac{\partial f_w}{\partial w}=1.
$$

Ascending in the input with step size one tenth gives

$$
x_{\mathrm{new}}=1+0.1\cdot2=1.2.
$$

The activation becomes

$$
f_w(1.2)=1.4.
$$

The derivative machinery is shared with training, but the two partial derivatives are different quantities and can have different shapes. Input optimisation asks how a fixed model responds to changes in an observation.

## Feature visualisation begins with a precisely chosen score

Let a scalar activation or class score be

$$
s_c(x).
$$

A basic feature visualisation solves

$$
\max_{x\in\mathcal X}s_c(x).
$$

The score might be one spatial unit, a channel average, or a class logit. These are different questions. A channel average rewards activity across positions; a single unit rewards activity at one position.

Even “maximise a class” needs clarification. If class probabilities come from logits,

$$
p_c(x)
=
\frac{\exp z_c(x)}
{\sum_j\exp z_j(x)},
$$

then

$$
\log p_c(x)
=
z_c(x)-\log\sum_j\exp z_j(x).
$$

Differentiation gives

$$
\nabla_x\log p_c
=
\nabla_xz_c
-
\sum_jp_j\nabla_xz_j.
$$

Increasing a class probability can therefore involve decreasing competing logits. Maximising one logit asks a different question from maximising its probability. The distinction between objectives and image priors is discussed in [Feature Visualization](https://distill.pub/2017/feature-visualization/).

Without restrictions, some objectives have no finite optimum. For an affine score,

$$
s(x)=a^\top x+b,
$$

choose an input in the gradient direction:

$$
x=ta.
$$

Then

$$
s(ta)=t\lVert a\rVert_2^2+b.
$$

For a nonzero coefficient vector, this increases without bound as the scale increases. The resulting problem does not specify a preferred image magnitude, let alone a preferred image appearance.

A constraint is therefore part of the question being asked. Searching all possible arrays, searching bounded pixel arrays, and searching outputs of a generator are different experiments even when the network score is identical.

## Deriving the effect of a norm constraint and a penalty

For the affine score, impose a Euclidean radius:

$$
\max_{\lVert x\rVert_2\le r}a^\top x.
$$

The Cauchy–Schwarz inequality gives

$$
a^\top x
\le
\lVert a\rVert_2\lVert x\rVert_2
\le
r\lVert a\rVert_2.
$$

Equality is attained by aligning the input with the coefficient vector:

$$
\boxed{x^\ast=r\frac{a}{\lVert a\rVert_2}}.
$$

Take the constructed example

$$
a=(3,4)^\top,
\qquad
r=2.
$$

Since the coefficient norm is five,

$$
x^\ast=(1.2,1.6)^\top,
\qquad
a^\top x^\ast=10.
$$

A coordinate-wise bound specifies a different problem:

$$
\max_{\lVert x\rVert_\infty\le2}a^\top x.
$$

Both coefficients are positive, so the maximum occurs at

$$
x^\ast=(2,2)^\top,
\qquad
a^\top x^\ast=14.
$$

The two answers differ because the permitted sets differ. The second answer has a larger Euclidean norm.

A quadratic penalty gives another formulation:

$$
\max_x
\left[
a^\top x-\frac{\lambda}{2}\lVert x\rVert_2^2
\right].
$$

Complete the square:

$$
a^\top x-\frac{\lambda}{2}\lVert x\rVert_2^2
=
-\frac{\lambda}{2}
\left\lVert x-\frac{a}{\lambda}\right\rVert_2^2
+
\frac{\lVert a\rVert_2^2}{2\lambda}.
$$

For a positive penalty coefficient, the unique optimum is therefore

$$
\boxed{x^\ast=\frac{a}{\lambda}}.
$$

With the same coefficient vector and a penalty coefficient of two,

$$
x^\ast=(1.5,2)^\top.
$$

Its score is

$$
3(1.5)+4(2)=12.5,
$$

and its penalty is

$$
\frac{2}{2}(1.5^2+2^2)=6.25.
$$

The penalised objective is consequently

$$
12.5-6.25=6.25.
$$

For this affine problem, a radius and a penalty can be matched by choosing

$$
\lambda=\frac{\lVert a\rVert_2}{r}.
$$

That correspondence should not be assumed for arbitrary nonconvex objectives. Different penalties or initialisations can select different local optima.

## Why a norm alone does not define a natural image

The brief needs one qualification: the feasible set or prior does essential work, but a norm constraint is neither necessary for every visualisation method nor sufficient for a meaningful image.

A squared pixel norm penalises magnitude, not spatial arrangement. Consider two two-pixel signals:

$$
x=(a,a)^\top,
\qquad
u=(a,-a)^\top.
$$

They have the same squared norm:

$$
\lVert x\rVert_2^2
=
\lVert u\rVert_2^2
=
2a^2.
$$

Yet one is constant and the other alternates. A magnitude penalty has no basis for preferring the smoother signal.

A spatial penalty can explicitly compare neighbouring pixels. Let a matrix compute selected neighbour differences:

$$
Dx.
$$

Define

$$
R_{\mathrm{smooth}}(x)
=
\frac12\lVert Dx\rVert_2^2.
$$

Its differential is

$$
\mathrm dR_{\mathrm{smooth}}
=
(Dx)^\top D\,\mathrm dx,
$$

so

$$
\nabla_xR_{\mathrm{smooth}}=D^\top Dx.
$$

For the two-pixel example, this penalty is zero for the constant signal and twice the squared amplitude for the alternating signal. It encodes a spatial preference that the ordinary pixel norm lacks.

Other restrictions can come from a parameterisation. If an image must satisfy

$$
x=G(z),
$$

then optimisation occurs through

$$
\nabla_zJ
=
J_G(z)^\top\nabla_xJ.
$$

Only images reachable through the generator are available. A recognisable result can consequently reflect both the interrogated model and the generator's prior.

An optimised image demonstrates that a particular input scores highly under a specified procedure. Establishing what a feature represents also requires examining multiple optima, real examples, and controlled changes to the hypothesised content.

## Style transfer as matching feature statistics

Let a frozen network produce a feature matrix:

$$
F(x)\in\mathbb R^{C\times M},
$$

where rows index channels and columns index spatial positions.

A content reference supplies a feature matrix at corresponding positions:

$$
F_c=F(x_c).
$$

One content loss is

$$
L_{\mathrm{content}}
=
\frac12\lVert F(x)-F_c\rVert_F^2.
$$

Differentiating entry by entry gives

$$
\nabla_FL_{\mathrm{content}}=F-F_c.
$$

This objective retains spatial correspondence in feature space. It need not retain every pixel detail, because different images can produce similar features.

For style, define a normalised Gram matrix:

$$
G(F)=\frac{1}{M}FF^\top.
$$

Its entries are

$$
G_{ab}
=
\frac{1}{M}
\sum_{j=1}^{M}F_{aj}F_{bj}.
$$

These are uncentred second moments of channel responses. They are not automatically covariances or correlation coefficients: the channel means have not been subtracted, and the variances have not been normalised.

Why use this statistic? Let a permutation matrix reorder spatial positions. Then

$$
G(FP)
=
\frac1M FPP^\top F^\top
=
\frac1M FF^\top
=
G(F).
$$

The Gram matrix ignores a common reordering of positions. It retains channel co-occurrence while discarding that spatial arrangement. This is the explicit invariance built into the style objective, rather than a proof that the statistic captures every human meaning of style.

The use of feature activations and Gram statistics comes from the [style-transfer formulation by Gatys, Ecker, and Bethge](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf).

To derive a style gradient, choose a symmetric target matrix and define

$$
E=G(F)-S,
\qquad
L_{\mathrm{style}}=\frac14\lVert E\rVert_F^2.
$$

The Gram differential is

$$
\mathrm dG
=
\frac1M
\left[(\mathrm dF)F^\top+F(\mathrm dF)^\top\right].
$$

Substitute it into

$$
\mathrm dL_{\mathrm{style}}
=
\frac12\operatorname{tr}(E^\top\mathrm dG).
$$

Because the error matrix is symmetric, the two resulting terms contribute equally. Matching the coefficient of the feature differential gives

$$
\boxed{
\nabla_FL_{\mathrm{style}}
=
\frac1M EF
}.
$$

For a numerical check, take

$$
F=
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix},
\qquad
S=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}.
$$

Then

$$
G=
\begin{bmatrix}
2.5&1\\
1&0.5
\end{bmatrix},
\qquad
E=
\begin{bmatrix}
1.5&1\\
1&-0.5
\end{bmatrix}.
$$

The loss and gradient are

$$
L_{\mathrm{style}}
=
\frac14(2.25+1+1+0.25)
=
1.125,
$$

$$
\nabla_FL_{\mathrm{style}}
=
\frac12
\begin{bmatrix}
1.5&1\\
1&-0.5
\end{bmatrix}
\begin{bmatrix}
1&2\\
0&1
\end{bmatrix}
=
\begin{bmatrix}
0.75&2\\
0.5&0.75
\end{bmatrix}.
$$

A complete input objective combines content, style, and any image regularisation. Backpropagation sends the resulting feature gradients through the frozen network to the pixels. Matching the selected statistics establishes success on that objective; it does not establish preservation of every semantic or clinical feature.

## Adversarial perturbation as constrained optimisation

Start from an observed input and its label:

$$
(x_0,y).
$$

An untargeted loss-based search solves

$$
\max_\delta
\ell\bigl(f_\theta(x_0+\delta),y\bigr)
$$

subject to

$$
\lVert\delta\rVert_p\le\varepsilon,
\qquad
x_0+\delta\in\mathcal X.
$$

The first constraint limits change from the original observation. The second enforces valid input values. The label must also remain valid under the allowed changes if the result is to demonstrate an adversarial error rather than a changed task.

A targeted search instead attempts to produce a specified alternative label, for example by minimising its cross-entropy:

$$
\min_\delta
\ell\bigl(f_\theta(x_0+\delta),y^\ast\bigr)
$$

under the same constraints. Increasing the true-label loss and decreasing a chosen target-label loss are generally different objectives in multiclass problems.

A high loss is also not identical to a changed prediction. The final decision must be checked directly.

## Deriving the gradient-sign and normalised-gradient steps

Let the input loss gradient at the original observation be

$$
g=\nabla_x\ell\bigl(f_\theta(x_0),y\bigr).
$$

The first-order approximation is

$$
\ell(x_0+\delta)
\approx
\ell(x_0)+g^\top\delta.
$$

For a coordinate-wise constraint, each displacement lies in an interval:

$$
-\varepsilon\le\delta_j\le\varepsilon.
$$

Each term in the linearised objective is maximised by selecting the endpoint with the same sign as its gradient component. Therefore,

$$
\boxed{
\delta^\ast
=
\varepsilon\operatorname{sign}(g)
}
$$

and the maximum linearised increase is

$$
g^\top\delta^\ast
=
\varepsilon\sum_j|g_j|
=
\varepsilon\lVert g\rVert_1.
$$

For a Euclidean constraint, Cauchy–Schwarz gives

$$
g^\top\delta
\le
\lVert g\rVert_2\lVert\delta\rVert_2
\le
\varepsilon\lVert g\rVert_2.
$$

Equality is attained by

$$
\boxed{
\delta^\ast
=
\varepsilon\frac{g}{\lVert g\rVert_2}
}
$$

when the gradient is nonzero.

For a sum-of-absolute-values constraint,

$$
g^\top\delta
\le
\max_j|g_j|\sum_j|\delta_j|
\le
\varepsilon\lVert g\rVert_\infty.
$$

Putting the entire budget on a largest-magnitude gradient coordinate attains the bound. These examples explain dual norms operationally: the perturbation norm determines which measure of gradient size controls the worst local change.

All three results solve the linearised problem. Nonlinear networks can change their gradients as the input moves, so one step need not solve the original constrained problem.

## A classifier perturbed across a known boundary

Define a synthetic ground-truth task by

$$
y(x)=\mathbf1[x_1>0.3].
$$

Consider a model with positive-class logit

$$
m(x)=2x_1-x_2-0.5,
$$

positive probability

$$
p(x)=\sigma(m(x)),
$$

and a positive prediction whenever its logit is positive.

At

$$
x_0=(0.6,0.4)^\top,
$$

the true label is positive and

$$
m(x_0)=0.3.
$$

For a positive label, the logistic loss is

$$
\ell(x)
=
-\log\sigma(m(x))
=
\log(1+\exp(-m(x))).
$$

Its gradient is

$$
\nabla_x\ell
=
-\sigma(-m(x))
\begin{bmatrix}2\\-1\end{bmatrix}.
$$

At the initial input,

$$
\nabla_x\ell
\approx
\begin{bmatrix}
-0.851115\\
0.425557
\end{bmatrix}.
$$

With a coordinate-wise budget of one fifth, the sign step is

$$
\delta=(-0.2,0.2)^\top.
$$

The new input remains inside the unit pixel box:

$$
x_{\mathrm{adv}}=(0.4,0.6)^\top.
$$

Its true label remains positive, but

$$
m(x_{\mathrm{adv}})
=
2(0.4)-0.6-0.5
=
-0.3.
$$

The model's prediction has changed. The loss increases from

$$
\log(1+\exp(-0.3))
\approx0.554355
$$

to

$$
\log(1+\exp(0.3))
\approx0.854355.
$$

The boundary distance is also exactly calculable. A coordinate-wise perturbation can reduce this affine logit by at most

$$
\varepsilon(2+1)=3\varepsilon.
$$

Thus the boundary is reached at

$$
\varepsilon=\frac{0.3}{3}=0.1.
$$

For a Euclidean budget, the corresponding boundary radius is

$$
\frac{0.3}{\sqrt{2^2+(-1)^2}}
=
\frac{0.3}{\sqrt5}
\approx0.134164.
$$

These are constructed geometric quantities, not measured robustness results.

## Iteration, preprocessing, and interpretation

Repeated projected ascent takes a step and returns the candidate to the allowed set:

$$
x^{(t+1)}
=
\Pi_{\mathcal C}
\left(
x^{(t)}+\alpha d^{(t)}
\right).
$$

For a coordinate-wise budget and unit-range pixels, the feasible interval for each coordinate is

$$
\max(0,x_{0j}-\varepsilon)
\le x_j\le
\min(1,x_{0j}+\varepsilon).
$$

Projection onto this intersection is coordinate-wise clipping. The step direction can be the gradient sign, while the total displacement remains bounded relative to the original input rather than the previous iterate.

The coordinates in which the budget is defined matter. If preprocessing uses

$$
u_j=\frac{x_j-\mu_j}{s_j},
$$

then

$$
\frac{\partial\ell}{\partial x_j}
=
\frac1{s_j}
\frac{\partial\ell}{\partial u_j}.
$$

A uniform budget in normalised coordinates generally becomes a nonuniform budget in original intensity units. A robustness statement must identify the input space, preprocessing, norm, radius, and allowed value range.

A failed optimisation does not prove that no admissible adversarial input exists. The search may encounter poor starting points, saturated gradients, discontinuous preprocessing, or an inadequate objective. Conversely, a successful search proves failure for the specific constructed input and constraint set, not a population-wide failure rate.

Pixel distance does not by itself establish perceptual or clinical equivalence. Feature validity and local robustness are also different properties: a constant classifier can be insensitive to perturbations while using no input-specific evidence. A classifier using a relevant feature can still place its threshold incorrectly.

## Revision checklist

| Question | What I should be able to reconstruct |
| --- | --- |
| What changes when the input is optimised? | The free variable changes; the chain rule remains the same. |
| What score is being maximised? | A specified unit, channel statistic, logit, or probability. |
| Why can unconstrained visualisation fail to have an optimum? | An affine score grows without bound along its coefficient vector. |
| What does a norm specify? | The geometry of allowed magnitude or displacement. |
| Does a pixel norm enforce smoothness? | No; constant and alternating signals can have identical norms. |
| What does a Gram matrix retain? | Uncentred channel second moments, invariant to common spatial permutations. |
| Where does the sign attack come from? | Maximising each coordinate of a linearised loss under an interval constraint. |
| Why use a normalised gradient for a Euclidean budget? | Cauchy–Schwarz identifies the optimal linearised direction. |
| What must an adversarial example preserve? | The task label under the specified allowed changes. |
| What does failed attack optimisation establish? | Failure of that search, without a general robustness guarantee. |

## Why it matters for my work

For ultrasound auditing, I need to specify which changes preserve the evidence under examination before interpreting an optimised input. A synthetic image, a style-matched image, and a nearby decision-changing image each answer a different question about the same frozen model.

## What I have not resolved

Which ultrasound input changes provide a defensible test of evidence stability, and which merely expose sensitivity in a coordinate system that has little connection to acquisition or clinical interpretation?
