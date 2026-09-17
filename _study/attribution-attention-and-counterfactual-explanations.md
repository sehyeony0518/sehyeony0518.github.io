---
layout: study_note
title: "Attribution, Attention, and Counterfactual Explanations"
description: "The main families of post-hoc explanation for medical images, and what each actually measures."
og_image: "https://sehyeony0518.github.io/assets/img/og/attribution-attention-and-counterfactual-explanations.png"
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "alignment"
category_title: "Clinical Alignment & Interpretability"
subgroup: "Explanations & Clinical Faithfulness"
order: 3
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-01-01-selvaraju-gradcam"
  - "2026-03-13-arun-assessing-saliency"
  - "2025-12-06-roentmod-counterfactual-cxr"
---

Explanation methods compute different quantities. Their visual similarity does not make those quantities interchangeable. A gradient, an allocated score difference, an attention coefficient, and a prediction-changing edit each require a separate interpretation.

## Core question and definition

Let $$F(x)$$ be the scalar model output to explain. The target might be a logit, probability, or score contrast; that choice is part of the method specification.

The main families can be distinguished by their mathematical question.

| Family | Quantity being computed |
|---|---|
| Input gradient | Local derivative of the selected output |
| Path attribution | Allocation of a baseline-to-input score difference along a chosen path |
| Occlusion | Finite output change under a chosen replacement |
| Local surrogate | A simpler model fitted to the predictor in a weighted neighborhood |
| Shapley attribution | Average marginal contribution to a specified feature-coalition value |
| Class activation map | Spatial summary of selected feature maps and their relation to an output |
| Attention inspection | Coefficients used to combine internal value representations |
| Counterfactual explanation | A constrained alternative input that changes a specified prediction |

The explanatory claim should follow from the computed quantity. A local sensitivity map should not be described as a complete allocation of the prediction unless an additional derivation justifies that interpretation.

## Key concepts

### Input gradients measure local sensitivity

For a differentiable predictor, the gradient is

$$
\nabla_x F(x)
=
\left(
\frac{\partial F}{\partial x_1},
\ldots,
\frac{\partial F}{\partial x_d}
\right).
$$

For a small displacement $$\delta$$,

$$
F(x+\delta)-F(x)
=
\nabla F(x)^\top\delta
+
o(\|\delta\|).
$$

The derivative tells us how the selected output changes per unit change in an input coordinate near the current input. It does not directly say how much of the current score that coordinate contributed.

The units already reveal the distinction. A derivative has units of output per input unit. A score contribution has units of output.

Multiplying by a displacement produces the first-order estimate

$$
A_i^{\mathrm{local}}
=
(x_i-x_i^0)\frac{\partial F(x)}{\partial x_i}.
$$

Summing these terms gives

$$
\sum_i A_i^{\mathrm{local}}
=
\nabla F(x)^\top(x-x^0).
$$

This equals the finite score difference for an affine model. For a nonlinear model, it need not.

### Completeness is an accounting axiom

Suppose an attribution method claims to allocate the entire difference between $$F(x)$$ and a baseline output $$F(x^0)$$. A natural accounting requirement is

$$
\sum_{i=1}^{d} A_i
=
F(x)-F(x^0).
$$

This is the **completeness axiom**.

It is an axiom selected for contribution methods, rather than a theorem that every valid explanation must satisfy. A correctly computed local gradient can be useful without satisfying it. What requires proof is that a proposed contribution method actually meets the axiom.

Consider

$$
F(x)=x^2,
\qquad
x^0=0,
\qquad
x=1.
$$

The finite difference is

$$
F(1)-F(0)=1.
$$

The endpoint derivative is

$$
F'(1)=2.
$$

The displacement-scaled endpoint gradient is therefore

$$
(1-0)F'(1)=2,
$$

which does not equal the score difference.

The derivative is correct. Its interpretation as the complete finite contribution is incorrect.

A small gradient can also coexist with a nonzero finite difference. Define

$$
F(x)=
\begin{cases}
0, & x\leq 0,\\
x, & 0<x<1,\\
1, & x\geq 1.
\end{cases}
$$

At $$x=2$$, the derivative is zero, but relative to $$x^0=0$$,

$$
F(2)-F(0)=1.
$$

The function changed earlier along the path and then became flat. Inspecting only the endpoint misses that history.

### Deriving integrated gradients from the chain rule

Choose the straight path from baseline to input:

$$
\gamma(\alpha)
=
x^0+\alpha(x-x^0),
\qquad
0\leq\alpha\leq 1.
$$

Define the attribution to coordinate $$i$$ as

$$
A_i^{\mathrm{IG}}
=
(x_i-x_i^0)
\int_0^1
\frac{\partial F(\gamma(\alpha))}{\partial x_i}
\,d\alpha.
$$

To see why the contributions sum correctly, differentiate the output along the path:

$$
\frac{d}{d\alpha}F(\gamma(\alpha))
=
\sum_i
\frac{\partial F(\gamma(\alpha))}{\partial x_i}
\frac{d\gamma_i(\alpha)}{d\alpha}.
$$

Because

$$
\frac{d\gamma_i(\alpha)}{d\alpha}
=
x_i-x_i^0,
$$

we obtain

$$
\frac{d}{d\alpha}F(\gamma(\alpha))
=
\sum_i
(x_i-x_i^0)
\frac{\partial F(\gamma(\alpha))}{\partial x_i}.
$$

Integrating,

$$
\begin{aligned}
\sum_i A_i^{\mathrm{IG}}
&=
\int_0^1
\frac{d}{d\alpha}F(\gamma(\alpha))
\,d\alpha \\
&=
F(\gamma(1))-F(\gamma(0)) \\
&=
F(x)-F(x^0).
\end{aligned}
$$

This proof requires the usual conditions for applying the chain rule along the path and the fundamental theorem of calculus. Continuous differentiability is sufficient; suitable piecewise differentiable networks also permit the argument when the path composition is absolutely continuous.

For the square example,

$$
A^{\mathrm{IG}}
=
(1-0)\int_0^1 2\alpha\,d\alpha
=
\left[\alpha^2\right]_0^1
=
1.
$$

The path integral captures the varying slope that the endpoint approximation missed.

Numerical integration only approximates this identity. The residual

$$
F(x)-F(x^0)-\sum_i\widehat A_i^{\mathrm{IG}}
$$

is a useful numerical check. A small residual establishes accounting accuracy, not clinical validity of the baseline.

### Completeness does not uniquely determine the allocation

For any suitable path $$\gamma$$ from $$x^0$$ to $$x$$, define

$$
A_i^\gamma
=
\int_0^1
\frac{\partial F(\gamma(t))}{\partial x_i}
\gamma_i'(t)\,dt.
$$

The same chain-rule argument gives

$$
\sum_i A_i^\gamma
=
F(x)-F(x^0).
$$

Different paths can nevertheless allocate interactions differently.

Take

$$
F(x_1,x_2)=x_1x_2,
$$

from baseline $$x^0=(0,0)$$ to input $$x=(1,1)$$.

Along the straight path,

$$
\gamma(\alpha)=(\alpha,\alpha),
$$

the partial derivatives are

$$
\frac{\partial F}{\partial x_1}=\alpha,
\qquad
\frac{\partial F}{\partial x_2}=\alpha.
$$

Therefore,

$$
A_1=A_2=\int_0^1\alpha\,d\alpha=\frac12.
$$

Now move the first coordinate before the second.

During the first segment, $$x_2=0$$, so changing $$x_1$$ does not change the product. During the second segment, $$x_1=1$$, so the entire increase is assigned to $$x_2$$:
$$
(A_1,A_2)=(0,1).
$$

Reversing the order gives

$$
(A_1,A_2)=(1,0).
$$

All three allocations are complete. Their different answers express different ways of allocating the interaction.

For medical images, a path through interpolated intensities is a mathematical reference construction. It is not automatically a sequence of plausible examinations or a progression of disease.

### Occlusion and local surrogates specify a neighborhood

For an occluded region $$J$$ and replacement operator $$T_J$$, a basic effect is

$$
\Delta_J(x)
=
F(x)-F(T_J(x)).
$$

The replacement is part of the quantity. Zeroing a patch, blurring it, or reconstructing it from surrounding anatomy can give different effects.

A local surrogate instead fits a simpler function $$g$$ to the predictor near the input. One generic objective is

$$
g_x^*
=
\arg\min_{g\in\mathcal G}
\left\{
\mathbb E_{Z\sim Q_x}
\left[
w_x(Z)\bigl(F(Z)-g(Z)\bigr)^2
\right]
+
\lambda\Omega(g)
\right\}.
$$

Here:

- $$Q_x$$ generates neighboring inputs.
- $$w_x$$ weights their relevance to the original input.
- $$\mathcal G$$ determines the surrogate family.
- $$\Omega$$ penalizes complexity.

A coefficient of $$g_x^*$$ describes the fitted approximation under this neighborhood and weighting. It is not generally a coefficient of the original model.

Changing the neighborhood can change the surrogate. A simple surrogate with poor local fit cannot support a detailed account of model behavior merely because its coefficients are easy to display.

### Shapley attribution allocates a declared coalition value

Let $$N$$ be the set of features, and let $$V(J)$$ assign a model-related value to each subset $$J\subseteq N$$.

The missing-feature convention defines $$V$$. Two examples are:

$$
V_{\mathrm{cond}}(J)
=
\mathbb E[F(X)\mid X_J=x_J],
$$

and

$$
V_{\mathrm{marg}}(J)
=
\mathbb E_{X_{\bar J}}
\left[
F(x_J,X_{\bar J})
\right].
$$

The second draws missing features from their joint marginal distribution without conditioning them on the retained values. Neither definition is automatically a causal intervention on the patient's disease.

For a uniformly random ordering $$\pi$$ of the features, let $$P_i^\pi$$ be the features preceding $$i$$. The Shapley contribution is

$$
\phi_i
=
\mathbb E_\pi
\left[
V(P_i^\pi\cup\{i\})-V(P_i^\pi)
\right].
$$

For any fixed ordering, summing these incremental differences telescopes:

$$
\sum_i
\left[
V(P_i^\pi\cup\{i\})-V(P_i^\pi)
\right]
=
V(N)-V(\varnothing).
$$

Taking the expectation over orderings gives

$$
\sum_i\phi_i
=
V(N)-V(\varnothing).
$$

Thus completeness follows for the chosen coalition value. It does not choose that value for us.

For a concrete example, suppose

$$
P(X_1=X_2=0)
=
P(X_1=X_2=1)
=
\frac12,
$$

and

$$
F(x_1,x_2)=x_1.
$$

Explain $$x=(1,1)$$. Under conditional values,

$$
V(\varnothing)=\frac12,
\qquad
V(\{1\})=V(\{2\})=V(\{1,2\})=1.
$$

There are two feature orderings. Hence

$$
\phi_1
=
\frac12
\left[
\left(1-\frac12\right)+(1-1)
\right]
=
\frac14,
$$

and similarly

$$
\phi_2=\frac14.
$$

The second feature receives credit because observing it reveals the first, even though the predictor's formula uses only the first.

Under marginal replacement,

$$
V(\{1\})=1,
\qquad
V(\{2\})=\frac12.
$$

The contributions become

$$
\phi_1
=
\frac12
\left[
\left(1-\frac12\right)
+
\left(1-\frac12\right)
\right]
=
\frac12,
$$

and

$$
\phi_2=0.
$$

Both answers sum to the same difference,

$$
1-\frac12=\frac12.
$$

They answer different questions about statistical information and functional dependence. The missing-feature convention must accompany the attribution.

### What Grad-CAM computes

Let $$A^k_{uv}$$ denote spatial feature map $$k$$ at the selected layer, with $$Z$$ spatial positions. For target score $$F$$, Grad-CAM forms channel weights

$$
\alpha_k
=
\frac{1}{Z}
\sum_{u,v}
\frac{\partial F}{\partial A^k_{uv}},
$$

and a spatial map

$$
L_{uv}
=
\operatorname{ReLU}
\left(
\sum_k\alpha_k A^k_{uv}
\right).
$$

The spatial average compresses the gradient field into one coefficient per channel. Weighting the feature maps then creates a coarse spatial summary. The rectifier retains positive values in that summary.

A special case explains its relationship to a score decomposition. Suppose the target is exactly a linear function of globally averaged feature maps:

$$
F
=
b+
\sum_k
w_k
\left(
\frac{1}{Z}
\sum_{u,v}A^k_{uv}
\right).
$$

Then

$$
\frac{\partial F}{\partial A^k_{uv}}
=
\frac{w_k}{Z},
$$

so

$$
\alpha_k
=
\frac{1}{Z}
\sum_{u,v}\frac{w_k}{Z}
=
\frac{w_k}{Z}.
$$

The unrectified map therefore satisfies

$$
\sum_{u,v}\sum_k\alpha_k A^k_{uv}
=
F-b.
$$

This exact identity relies on the stated linear architecture and concerns the map before rectification. A nonlinear downstream network does not generally have this decomposition, and removing negative values changes the sum.

Resizing a coarse map adds display pixels, not new spatial evidence. A highlighted organ is consequently neither a segmentation boundary nor proof that a particular finding within the organ drove the diagnosis.

### Why attention coefficients are not generally input attributions

For one attention operation, write

$$
\alpha_{ij}
=
\frac{\exp(a_{ij})}
{\sum_\ell\exp(a_{i\ell})},
\qquad
a_{ij}
=
\frac{q_i^\top k_j}{\sqrt{d_k}},
$$

and

$$
u_i
=
\sum_j\alpha_{ij}v_j.
$$

A simplified residual update is

$$
z_i=x_i+W_Ou_i.
$$

The attention coefficient $$\alpha_{ij}$$ is one factor in a weighted value contribution. The final output also depends on the values, output projection, residual path, other heads, and subsequent transformations.

A scalar construction makes the problem visible:

$$
\alpha_1=\frac9{10},
\qquad
\alpha_2=\frac1{10},
\qquad
v_1=0,
\qquad
v_2=10.
$$

The attention output is

$$
u
=
\frac9{10}\cdot0
+
\frac1{10}\cdot10
=
1.
$$

The higher-weighted value contributes zero to this sum; the lower-weighted value contributes one. Ranking the coefficients alone gives a different ranking from the weighted value contributions.

Even the product is only an intermediate contribution. To see why coefficients do not equal input derivatives, consider

$$
F(x)
=
r(x)+\sum_j\alpha_j(x)v_j(x).
$$

Differentiation gives

$$
\frac{\partial F}{\partial x_k}
=
\frac{\partial r}{\partial x_k}
+
\sum_j
v_j
\frac{\partial\alpha_j}{\partial x_k}
+
\sum_j
\alpha_j
\frac{\partial v_j}{\partial x_k}.
$$

Attention weights account for only part of the final term. They omit the residual derivative and the changes in the weights themselves.

There is another useful exact derivative. Holding values fixed, softmax differentiation gives

$$
\frac{\partial\alpha_j}{\partial a_k}
=
\alpha_j
\left(
\mathbf 1\{j=k\}-\alpha_k
\right).
$$

Therefore,

$$
\begin{aligned}
\frac{\partial u}{\partial a_k}
&=
\sum_jv_j
\frac{\partial\alpha_j}{\partial a_k} \\
&=
\alpha_kv_k
-
\alpha_k\sum_j\alpha_jv_j \\
&=
\alpha_k(v_k-u).
\end{aligned}
$$

Sensitivity to an attention logit depends on how its value differs from the current weighted average, as well as on its attention weight.

In the constructed example,

$$
\frac{\partial u}{\partial a_1}
=
-\frac9{10},
\qquad
\frac{\partial u}{\partial a_2}
=
\frac9{10}.
$$

The coefficients alone do not reveal these signed effects.

Restricted linear settings can permit exact contribution calculations from attention-weighted values. There is no general identity equating raw attention weights with attributions to the original image regions.

### Counterfactual explanations solve a constrained prediction problem

A basic counterfactual explanation seeks

$$
x^*
=
\arg\min_{x'\in\mathcal F}
d(x,x')
$$

subject to

$$
a(F(x'))=a_{\mathrm{target}},
$$

where:

- $$d$$ defines proximity.
- $$\mathcal F$$ defines admissible changes.
- $$a$$ converts the model output into a decision.
- $$a_{\mathrm{target}}$$ is the desired alternative decision.

The constraint establishes a changed model answer. The distance and feasible set determine what counts as a small or acceptable change.

Consider normalized toy coordinates with score

$$
F(x_1,x_2)=2x_1+x_2,
$$

and a positive decision when

$$
F(x)\geq3.
$$

Starting at $$x=(0,0)$$, minimize Euclidean distance without additional constraints. Any positive candidate must satisfy

$$
2x_1'+x_2'\geq3.
$$

By the Cauchy-Schwarz inequality,

$$
2x_1'+x_2'
\leq
\sqrt{2^2+1^2}
\sqrt{(x_1')^2+(x_2')^2}.
$$

Thus every feasible candidate has distance at least

$$
\|x'\|_2\geq\frac3{\sqrt5}.
$$

Equality holds when $$x'$$ is proportional to $$(2,1)$$. Setting

$$
x'=t(2,1)
$$

and imposing the boundary gives

$$
5t=3,
\qquad
t=\frac35.
$$

The nearest alternative is therefore

$$
x^*
=
\left(\frac65,\frac35\right).
$$

If the first coordinate cannot change, the feasible set instead requires

$$
x_1'=0.
$$

Then the nearest positive point is

$$
x^*=(0,3).
$$

The classifier is unchanged. The explanation changes because admissibility changed.

These numbers are properties of the toy construction, not clinical intervention thresholds.

### Different counterfactual claims require different validation

A counterfactual should be evaluated at the level of the claim being made.

| Claimed property | Necessary check |
|---|---|
| Prediction changes | Evaluate the edited input with the specified predictor and decision rule |
| The intended feature changes | Independently assess that feature in the edit |
| Other evidence is preserved | Check changes to competing findings, anatomy, and acquisition cues |
| The image is plausible | Assess whether it could represent an admissible examination |
| The change is actionable | Restrict edits to actions available in the stated setting |
| The edit represents a patient-level causal alternative | Supply and justify the causal assumptions connecting the intervention to the patient state |
| The result is dependable | Examine sensitivity to small edit variations and model uncertainty |

A nonactionable hypothetical can still answer a descriptive question. It should not be presented as a feasible recommendation.

Likewise, a realistic image that flips a prediction does not establish that the patient's diagnosis would change. The generator may modify a shortcut or exploit a classifier vulnerability. Clinical validity of the edit requires evidence beyond the classifier's own response.

### Revision checklist

| Question | What I should be able to derive or specify |
|---|---|
| What does a gradient measure? | A first-order output response per input unit |
| What is completeness? | An accounting requirement for a baseline-relative allocation |
| Why can an endpoint gradient violate it? | A finite difference need not equal one endpoint slope times displacement |
| Why are integrated gradients complete? | The chain rule followed by integration along the path |
| Why can complete methods disagree? | Paths and coalition values allocate interactions differently |
| What defines an occlusion effect? | The replaced region and replacement mechanism |
| What does a local surrogate explain? | A fitted approximation under a specified neighborhood |
| What does a Shapley value allocate? | Marginal contributions to the declared coalition value |
| What limits Grad-CAM? | Channel averaging, selected-layer resolution, nonlinear downstream computation, and rectification |
| Why inspect more than attention weights? | Values, weight dependence, residual routes, and downstream transformations affect the output |
| What does a counterfactual flip establish? | Predictive change under the specified edit, with further claims requiring further checks |

## Why it matters for my work

For ultrasound auditing, I need to select the explanatory quantity before selecting its visualization. Clinical assessability determines which feature-level interpretations can be checked, while Faithfulness requires agreement with the stated model quantity. A familiar anatomical display does not bridge those two requirements.

## What I have not resolved

- Which baselines and feature replacements preserve the acquisition context needed to interpret ultrasound?
- How can generated edits be checked for subtle changes to clinical evidence beyond the nominated feature?

---

Sources: Sundararajan, Taly, and Yan, Axiomatic Attribution for Deep Networks; Lundberg and Lee, A Unified Approach to Interpreting Model Predictions; Selvaraju and colleagues, Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization; Jain and Wallace, Attention is not Explanation. Numerical examples and accompanying calculations are constructed here. These are study notes for research purposes, not clinical guidance.
