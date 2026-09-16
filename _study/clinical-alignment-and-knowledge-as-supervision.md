---
layout: study_note
title: "Clinical Alignment and Knowledge as Supervision"
description: "Using clinical knowledge to shape what a model learns, rather than only to judge it afterwards."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "alignment"
category_title: "Clinical Alignment & Interpretability"
subgroup: "Clinical Supervision & Concepts"
order: 1
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-11-29-concept-bottleneck-models"
  - "2026-02-03-right-for-the-right-reasons"
  - "2026-05-11-cdep-penalizing-explanations"
---

Clinical knowledge becomes supervision when it changes a model's training objective, admissible architecture, or required behavior. The resulting model still needs to be tested for the intended evidence use. A clinically named loss is a mechanism for training, not a certificate of alignment.

## Core question and definition

I use clinical alignment to mean satisfaction of explicit, task-specific expectations about the model's inputs, intermediate variables, outputs, and responses to changes in evidence.

For a gallbladder classifier, such expectations might concern lesion attachment, wall architecture, posterior acoustics, or recognition that the available views are insufficient for an assessment.

These expectations need to be separated into different kinds of claims:

- **Measurement:** a predicted descriptor agrees with an assessable clinical finding.
- **Dependence:** the diagnostic output responds appropriately to that finding.
- **Invariance:** changes declared irrelevant do not substantially alter the relevant output.
- **Decision behavior:** uncertainty, referral, or abstention follows the intended use.
- **Information restriction:** specified inputs or pathways cannot influence the result.

Knowledge supervision can target one or more of these properties. Success on one does not establish the others.

A segmentation target can improve localization without making the diagnosis depend on lesion morphology. A concept head can recognize attachment while the diagnostic head uses acquisition cues. A gradient penalty can reduce local sensitivity while leaving a finite shortcut effect intact.

## Key concepts

### Different forms of supervision impose different obligations

| Form of knowledge | How it enters learning | Immediate object being optimized or restricted |
|---|---|---|
| Finding annotation | A supervised concept or feature target | Agreement with annotated findings |
| Region annotation | Segmentation, localization, or spatial loss | Agreement with an annotated region |
| Auxiliary task | Additional loss on a shared representation | Joint performance on the main and auxiliary tasks |
| Architectural constraint | Restriction of available input paths | Which variables can reach the predictor |
| Explanation regularization | Penalty on a model-derived or learned explanation | Agreement with the chosen explanation target |
| Behavioral consistency | Loss comparing outputs under selected transformations | Stability under those transformations |
| Decision rule | Thresholds, abstention, or referral constraints | Actions permitted for particular outputs and uncertainty states |

The wording of the claim should identify which row supplies its evidence.

Clinical knowledge also has scope. A descriptive finding is not a deterministic diagnostic rule. A relationship that is useful in one examination context may be inappropriate when another finding or acquisition limitation changes its meaning.

### Deriving a multitask objective

Let the model have:

- Diagnostic output $$F_\theta(x)$$.
- Concept outputs $$g_{\theta,j}(x)$$.
- Diagnostic label $$y$$.
- Concept labels $$c_j$$.

A basic objective is

$$
L(\theta)
=
L_{\mathrm{diag}}(\theta)
+
\sum_j\lambda_j L_{\mathrm{concept},j}(\theta).
$$

For a batch with concept availability indicators $$M_{ij}$$, one possible concept loss is

$$
L_{\mathrm{concept},j}
=
\frac{
\sum_i M_{ij}
\ell_j(g_{\theta,j}(x_i),c_{ij})
}{
\sum_i M_{ij}
},
$$

when the denominator is positive. If no concept labels are available in a batch, that concept term is omitted.

This avoids treating unavailable annotations as negative findings.

However, masking missing labels does not make the remaining cases representative. At the population level,

$$
\frac{\mathbb E[M_j\ell_j]}{\mathbb E[M_j]}
=
\frac{
P(M_j=1)\mathbb E[\ell_j\mid M_j=1]
}{
P(M_j=1)
}
=
\mathbb E[\ell_j\mid M_j=1].
$$

The loss is evaluated on the annotated subset. If assessable, clearly visualized, or diagnostically easy cases are more likely to be annotated, the concept objective has that restricted scope.

Missingness, unassessability, and concept absence should consequently remain distinguishable in the data and evaluation.

### Loss weights are optimization weights

For shared parameters, define

$$
g_d=\nabla_\theta L_{\mathrm{diag}},
\qquad
g_c=\nabla_\theta L_{\mathrm{concept}}.
$$

With one auxiliary concept loss, a gradient step is

$$
\theta'
=
\theta-\eta(g_d+\lambda g_c).
$$

Expand the diagnostic loss around the original parameters:

$$
L_{\mathrm{diag}}(\theta')
=
L_{\mathrm{diag}}(\theta)
+
g_d^\top(\theta'-\theta)
+
O(\eta^2).
$$

Substitution gives

$$
L_{\mathrm{diag}}(\theta')
-
L_{\mathrm{diag}}(\theta)
=
-\eta\|g_d\|_2^2
-
\eta\lambda g_d^\top g_c
+
O(\eta^2).
$$

The inner product matters.

- If $$g_d^\top g_c>0$$, the auxiliary direction helps reduce diagnostic loss to first order relative to the same diagnostic step.
- If $$g_d^\top g_c<0$$, it opposes that reduction.
- A sufficiently strong opposing auxiliary term can increase diagnostic loss.

The value of $$\lambda$$ is therefore not clinical importance by definition. Its effect depends on gradient directions, loss scales, parameterization, and optimization.

### A concrete example of conflicting supervision

Consider two nonnegative quadratic losses:

$$
L_d(\theta)
=
\frac12
\left[
(\theta_1-1)^2+\theta_2^2
\right],
$$

and

$$
L_c(\theta)
=
\frac12
\left[
(\theta_1+2)^2+(\theta_2-1)^2
\right].
$$

At

$$
\theta=(0,0),
$$

their gradients are

$$
g_d=(-1,0),
\qquad
g_c=(2,-1).
$$

Their inner product is

$$
g_d^\top g_c=-2.
$$

With $$\lambda=1$$, the combined gradient is

$$
g_d+g_c=(1,-1).
$$

A step of size $$\eta$$ therefore produces

$$
\theta'=(-\eta,\eta).
$$

The diagnostic loss becomes

$$
\begin{aligned}
L_d(\theta')
&=
\frac12
\left[
(-\eta-1)^2+\eta^2
\right] \\
&=
\frac12+\eta+\eta^2.
\end{aligned}
$$

It increases for every positive step size.

The concept loss becomes

$$
\begin{aligned}
L_c(\theta')
&=
\frac12
\left[
(2-\eta)^2+(\eta-1)^2
\right] \\
&=
\frac52-3\eta+\eta^2.
\end{aligned}
$$

For the constructed step

$$
\eta=\frac1{10},
$$

the changes are

| Loss | Before | After |
|---|---|---|
| Diagnostic | $$1/2$$ | $$61/100$$ |
| Concept | $$5/2$$ | $$221/100$$ |

The auxiliary task improves while the diagnostic task worsens.

This is not an empirical claim that concept supervision generally harms diagnosis. It demonstrates why improvement on an auxiliary task is not, by itself, evidence of improvement on the main task or of clinically appropriate diagnostic reliance.

### Architecture can impose a stronger restriction than an auxiliary loss

A strict concept bottleneck has

$$
F(x)=h(g(x)),
$$

where $$g(x)$$ contains the predicted concepts.

It enforces

$$
g(x)=g(x')
\quad\Longrightarrow\quad
F(x)=F(x').
$$

An auxiliary concept head does not enforce this implication if the diagnostic head also receives unrestricted features.

A fixed input restriction can provide another exact guarantee. Suppose

$$
F(x)=h(P_Mx),
$$

where $$P_M$$ retains a fixed set of permitted input coordinates. For a perturbation $$\delta$$ entirely outside that set,

$$
P_M\delta=0.
$$

Then

$$
\begin{aligned}
F(x+\delta)
&=
h(P_Mx+P_M\delta) \\
&=
h(P_Mx) \\
&=
F(x).
\end{aligned}
$$

This is finite invariance, not just a small-gradient claim.

The guarantee requires the complete computation to respect the restriction. Excluded pixels can still influence the result indirectly if they affect crop selection, global normalization, metadata, or another input route.

The restriction may also encode the wrong clinical assumption. Posterior acoustic information can lie outside a lesion mask. A model that is invariant to every extralesional change may be prevented from using valid evidence.

Architecture can enforce the restriction that was specified. It cannot establish that the restriction was clinically appropriate.

### What gradient-based explanation regularization penalizes

Let $$M$$ mark the input region in which sensitivity is permitted. A generic penalty on sensitivity outside that region is

$$
R_{\mathrm{grad}}(\theta)
=
\mathbb E_{\mathrm{train}}
\left[
\left\|
(1-M)\odot\nabla_x F_\theta(X)
\right\|_2^2
\right].
$$

The complete objective could be

$$
L(\theta)
=
L_{\mathrm{diag}}(\theta)
+
\lambda R_{\mathrm{grad}}(\theta).
$$

Because the explanation is calculated from $$F_\theta$$, this penalty can change the predictor. It is more than training an unrelated display.

Its direct target is nevertheless local sensitivity at the sampled inputs, for the selected output. It does not automatically constrain all finite changes in the prohibited region.

The distinction matters even when the penalty is exactly zero.

### A predictor can have a perfect local gradient map and still use a shortcut

Let $$C$$ be a clinically relevant binary signal and $$S$$ a binary shortcut. The true target in this toy example is

$$
Y=C.
$$

Define the smooth function

$$
q(s)=3s^2-2s^3.
$$

Its derivative is

$$
q'(s)=6s-6s^2=6s(1-s).
$$

At the binary endpoints,

$$
q(0)=0,
\qquad
q(1)=1,
$$

but

$$
q'(0)=q'(1)=0.
$$

Now define the model score

$$
F(C,S)=C+2q(S),
$$

with a positive decision when

$$
F(C,S)\geq\frac32.
$$

The input derivatives are

$$
\frac{\partial F}{\partial C}=1,
$$

and

$$
\frac{\partial F}{\partial S}
=
2q'(S)
=
12S(1-S).
$$

For every observed binary input,

$$
\nabla F(C,S)=(1,0).
$$

A gradient map identifies only the clinical coordinate. A penalty on the shortcut derivative is zero at every one of these points.

Yet the finite shortcut effect is

$$
\begin{aligned}
F(C,1)-F(C,0)
&=
2\bigl(q(1)-q(0)\bigr) \\
&=
2.
\end{aligned}
$$

The decision behavior is

| Clinical signal $$C$$ | Shortcut $$S$$ | Score $$F(C,S)$$ | Predicted class | Correct for $$Y=C$$? |
|---|---|---|---|---|
| $$0$$ | $$0$$ | $$0$$ | $$0$$ | Yes |
| $$0$$ | $$1$$ | $$2$$ | $$1$$ | No |
| $$1$$ | $$0$$ | $$1$$ | $$0$$ | No |
| $$1$$ | $$1$$ | $$3$$ | $$1$$ | Yes |

If the development data contain only cases with

$$
C=S,
$$

the model predicts the target correctly on all observed cases. It also has the desired local gradient map. When the shortcut and clinical signal disagree, it fails both constructed cases.

There are two distinct conclusions.

First, this gradient is faithful to local sensitivity. It was computed correctly. Calling it a complete account of finite evidence reliance would exceed its meaning.

Second, the zero gradient penalty does not establish finite invariance. The derivative becomes nonzero between the observed endpoints, where the training constraint supplied no protection.

### What would justify a finite invariance bound?

Separate the input into clinical variables $$c$$ and nuisance variables $$s$$. Suppose that, along the entire straight path from $$s$$ to $$s'$$,

$$
\|\nabla_s F(c,s+t(s'-s))\|_2
\leq\varepsilon,
\qquad
0\leq t\leq1.
$$

Define

$$
\gamma(t)=s+t(s'-s).
$$

By the chain rule and integration,

$$
F(c,s')-F(c,s)
=
\int_0^1
\nabla_s F(c,\gamma(t))^\top(s'-s)
\,dt.
$$

Applying the Cauchy-Schwarz inequality,

$$
\begin{aligned}
|F(c,s')-F(c,s)|
&\leq
\int_0^1
\|\nabla_s F(c,\gamma(t))\|_2
\|s'-s\|_2
\,dt \\
&\leq
\varepsilon\|s'-s\|_2.
\end{aligned}
$$

This is a finite-change bound because the derivative is bounded along the whole relevant path.

A small empirical gradient penalty at isolated examples does not establish that uniform condition. A certificate would need additional control over the intervening region, and a clinical interpretation would also need that region to represent the intended nuisance changes.

### An independent explanation head can improve without changing reliance

Suppose a diagnostic model has parameters $$\theta$$, while a separate explainer has parameters $$\psi$$:
$$
F_\theta(x),
\qquad
E_\psi(x).
$$

Train with

$$
L(\theta,\psi)
=
L_{\mathrm{diag}}(\theta)
+
\lambda
\mathbb E
\left[
\|E_\psi(X)-M(X)\|_2^2
\right].
$$

If the explanation term has no dependence on $$\theta$$, then

$$
\nabla_\theta
\mathbb E
\left[
\|E_\psi(X)-M(X)\|_2^2
\right]
=
0.
$$

The explanation can learn to reproduce clinical masks while leaving the diagnostic predictor's evidence use unaffected by that supervision.

This is a different failure from the preceding gradient example:

- The separate explanation may provide an unfaithful but plausible account of the predictor.
- The gradient explanation can faithfully report local sensitivity while being overinterpreted as finite clinical reliance.

The architecture and explanatory claim determine which concern applies.

### Behavioral consistency has a defined support

Another objective compares predictions before and after a transformation:

$$
R_{\mathrm{cons}}
=
\mathbb E_{X,T}
\left[
\bigl(F(TX)-F(X)\bigr)^2
\right].
$$

If this nonnegative population expectation is zero, then

$$
F(TX)=F(X)
$$

almost surely under the specified distribution of inputs and transformations.

That is a statement about the support of the training expectation. It does not imply invariance to transformations absent from that distribution. Zero empirical loss on finitely many transformations has an even narrower scope.

The transformation also needs to preserve the information relevant to the desired output. A patient's disease can remain unchanged while image degradation removes visible evidence. Requiring an unchanged confident probability after destroying evidence would be an inappropriate constraint.

Clinical knowledge should distinguish nuisance variation that preserves assessability from variation that should increase uncertainty or trigger reacquisition.

### Clinical knowledge can be incomplete or incorrectly formalized

A useful clinical descriptor may change meaning with context. Enforcing a fixed monotonic relationship between one descriptor and malignancy risk asserts a conditional rule: risk must change in the same direction while all other model inputs are held fixed.

A marginal association in a dataset does not establish that stronger rule. Nor does a common teaching pattern establish that exceptions should receive the same penalty as annotation mistakes.

Knowledge supervision should therefore document:

- Which statement is observational and which is intended as a constraint.
- The population and examination context in which it applies.
- Whether the relevant finding is assessable.
- Which exceptions or competing explanations are permitted.
- How disagreement and uncertainty enter the target.
- What evidence would lead to revising the constraint.

For ultrasound, an anatomical mask is especially easy to overinterpret. A region annotation can identify where an organ lies without specifying all the acoustic evidence relevant to its interpretation.

### Evaluating what the supervision actually changed

A useful evaluation has several distinct comparisons.

**Training-procedure comparison.** Compare otherwise appropriate baselines with and without the knowledge term, accounting for annotation and tuning resources. This estimates the effect of changing the training procedure.

**Concept measurement.** Evaluate finding predictions against independent assessments, including unassessable cases and acquisition subgroups.

**Frozen-model behavior.** Examine responses to controlled changes in the nominated evidence and nuisances. This addresses the fitted model's dependence.

**Diagnostic and decision performance.** Evaluate discrimination, calibration, operating-point errors, abstention, and consequences for the intended workflow.

Ablating a supervision term and retraining does not directly reveal the mechanism of one fitted model. The new training run can learn a different representation. Conversely, a successful intervention on a frozen model does not establish that the training method will consistently produce the same behavior across datasets or seeds.

Training annotations should not also serve as an unquestioned audit reference. Agreement with the same annotation convention can reward reproduction of its errors.

### Revision checklist

| Question | What I should be able to state |
|---|---|
| What does alignment mean here? | A task-specific measurement, dependence, invariance, or decision claim |
| How does knowledge enter training? | Annotation, auxiliary loss, architecture, explanation penalty, or behavioral constraint |
| What does masking unavailable labels do? | Avoid false negative supervision while retaining an annotated-subset objective |
| Why are loss weights not clinical importance? | Their effects depend on loss scale and gradient interaction |
| What can an auxiliary head fail to establish? | That the diagnostic head uses the predicted concepts |
| What does a strict architecture guarantee? | A stated restriction on complete computational paths |
| What does a gradient penalty control directly? | Local sensitivity at the evaluated inputs |
| Why can zero local gradients conceal finite dependence? | The function can change between constrained points |
| What supports a finite-change bound? | A derivative bound along the entire relevant path |
| When can explanation supervision be cosmetic? | When it improves a display without adequately constraining the predictor |
| What separates training benefit from reliance evidence? | Retraining comparisons and frozen-model interventions answer different questions |

## Why it matters for my work

Clinical alignment gives my gallbladder research explicit hypotheses about evidence use before training. The ontology keeps the obligation visible: Clinical feature annotation can support an audit of Clinical evidence reliance, but the annotation and the loss built from it do not confer that property. Clinical assessability limits both supervision and the claims made from it.

## What I have not resolved

- Which knowledge constraints remain appropriate when acquisition quality changes what evidence is available?
- How can an audit distinguish improved clinical reliance from improved agreement with the explanation target used during training?

---

Sources: Ross, Hughes, and Doshi-Velez, Right for the Right Reasons: Training Differentiable Models by Constraining their Explanations; Koh and colleagues, Concept Bottleneck Models. The objectives used here are stated explicitly, and the numerical counterexamples are constructed demonstrations. These are study notes for research purposes, not clinical guidance.
