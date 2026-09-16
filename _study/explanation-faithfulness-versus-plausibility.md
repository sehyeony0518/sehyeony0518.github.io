---
layout: study_note
title: "Explanation Faithfulness versus Plausibility"
description: "Looking right to a clinician and reflecting the model's computation are different properties, and the gap between them is where trouble lives."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "alignment"
category_title: "Clinical Alignment & Interpretability"
subgroup: "Explanations & Clinical Faithfulness"
order: 4
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-03-13-arun-assessing-saliency"
  - "2026-02-15-posthoc-explanations-spurious-correlation"
  - "2026-07-28-auditing-inference-processes-generative-counterfactuals"
---

An explanation makes a claim about a model. Clinical plausibility asks whether that claim agrees with a reader's expectations. Faithfulness asks whether it accurately describes the property of the model that it claims to explain. These questions require different evidence.

## Core question and definition

Let $$F$$ be a fixed model output, such as a class logit, a probability, or a difference between class scores. Let $$E_F(x)$$ be an explanation of that output at input $$x$$.

Before judging the explanation, specify its **explanatory claim**. It might claim to report:

- The derivative of the output with respect to each input.
- Contributions to a score difference relative to a baseline.
- Responses to removing or replacing features.
- Sensitivity along a concept direction.
- The role of a particular internal computational pathway.

These are different mathematical objects. An explanation can accurately report one while being unsuitable for another.

Write the object being claimed as

$$
\Gamma_F(x;\mathcal C),
$$

where $$\mathcal C$$ records the explanatory conditions: output, baseline, intervention, layer, feature grouping, and other necessary choices. A possible faithfulness discrepancy is

$$
L_{\mathrm{faith}}
=
\mathbb E_X
\left[
d\left(E_F(X),\Gamma_F(X;\mathcal C)\right)
\right].
$$

Here $$d$$ measures disagreement appropriate to the claim. For a gradient explanation, the comparison object might be the actual derivative. For a perturbation explanation, it might be the output changes under specified interventions.

Clinical plausibility has a different reference. If $$H(x)$$ represents a clinical annotation or human expectation, a plausibility discrepancy might be

$$
L_{\mathrm{plaus}}
=
\mathbb E_X
\left[
d_H\left(E_F(X),H(X)\right)
\right].
$$

The first comparison is between an explanation and the model. The second is between an explanation and a human reference. Neither expression supplies a universal metric; each makes the object of comparison explicit.

A functional explanation need not reproduce every internal operation. Conversely, agreement with the model's input-output behavior does not establish an additional claim about which internal circuit implements it. The level of explanation must remain part of the claim.

## Key concepts

### A constructed example establishes logical independence

Consider two binary inputs:

- $$C$$: a clinically relevant feature.
- $$S$$: a shortcut, such as an acquisition marker.

For this construction, the clinical expectation is that an explanation should identify $$C$$.

Define two predictors:

$$
F_C(C,S)=C,
\qquad
F_S(C,S)=S.
$$

At the input

$$
x=(1,1),
$$

both predictors return

$$
F_C(x)=F_S(x)=1.
$$

Use the baseline

$$
x^0=(0,0).
$$

Because these predictors are additive, their contributions relative to the baseline are unambiguous:

$$
F_C(x)-F_C(x^0)
=
1\cdot(1-0)+0\cdot(1-0),
$$

so the contribution vector is

$$
A_C=(1,0).
$$

Similarly,

$$
F_S(x)-F_S(x^0)
=
0\cdot(1-0)+1\cdot(1-0),
$$

giving

$$
A_S=(0,1).
$$

Now combine each predictor with either displayed explanation.

| Actual predictor | Displayed contributions | Faithful? | Plausible under the stated clinical expectation? |
|---|---|---|---|
| $$F_C=C$$ | $$A_C=(1,0)$$ | Yes | Yes |
| $$F_S=S$$ | $$A_S=(0,1)$$ | Yes | No |
| $$F_S=S$$ | $$A_C=(1,0)$$ | No | Yes |
| $$F_C=C$$ | $$A_S=(0,1)$$ | No | No |

All four combinations exist. This establishes **logical independence**: neither property implies the other. It does not assert that the properties are statistically independent in a real collection of explanations.

The unfaithful but plausible explanation is particularly dangerous as an explanation: it gives a clinically reassuring account of a shortcut-dependent predictor. The faithful but implausible explanation can be useful precisely because it exposes that shortcut.

This does not make the underlying shortcut model safe. It distinguishes a dangerous predictor that an explanation reveals from a dangerous predictor that an explanation conceals.

The construction also shows why completeness alone cannot establish faithfulness. Both displayed vectors satisfy

$$
A_1+A_2=1=F(x)-F(x^0).
$$

A correct total does not establish a correct allocation.

### Human expectation is a reference with limitations

Plausibility is conditional on what the human reference expects. A clinician may recognize an invalid anatomical location, but the annotation may omit relevant context or describe a different task.

A lesion mask answers where a lesion is. It does not, by itself, identify which appearance within that lesion supported a diagnosis. A model could respond to a caliper, texture artifact, or device-dependent pattern inside the same mask.

Conversely, evidence outside a lesion boundary can matter. Surrounding tissue and acoustic relationships may be relevant to interpreting an ultrasound finding. Treating every extralesional attribution as incorrect would encode a clinical assumption that itself needs justification.

The comparison therefore needs an operational statement:

- Is the reference an anatomical boundary?
- A region in which a finding is assessable?
- An annotation of a specific diagnostic feature?
- A reader's expectation about evidence use?
- A record of what the reader actually inspected?

Agreement with one of these references should not silently become agreement with all of them.

### The selected output changes the explanation

Suppose the model produces a logit $$z(x)$$ and a probability

$$
p(x)=\frac{1}{1+e^{-z(x)}}.
$$

Differentiating with respect to the logit gives

$$
\frac{dp}{dz}
=
\frac{e^{-z}}{(1+e^{-z})^2}.
$$

Since

$$
p=\frac{1}{1+e^{-z}},
\qquad
1-p=\frac{e^{-z}}{1+e^{-z}},
$$

this becomes

$$
\frac{dp}{dz}=p(1-p).
$$

The chain rule therefore gives

$$
\nabla_x p(x)
=
p(x)\bigl(1-p(x)\bigr)\nabla_x z(x).
$$

A probability gradient can be small when the probability is near either endpoint, even when the corresponding logit gradient is substantial. This is a property of the selected output transformation.

Likewise, a perturbation can produce a large logit change and a small probability change. Neither measurement is automatically wrong, but they answer different questions. The output being explained must be recorded before comparing explanation magnitudes or deletion curves.

### Deriving the quantity measured by a perturbation test

Let $$J$$ be a set of input features or image regions. Let

$$
T_J(x,U)
$$

replace those features according to a specified mechanism. The random variable $$U$$ represents replacement randomness, with distribution $$Q$$.

For a fixed input, define the expected score drop

$$
\Delta_Q(J;x)
=
F(x)
-
\mathbb E_{U\sim Q}
\left[
F\bigl(T_J(x,U)\bigr)
\right].
$$

This is the quantity a perturbation test measures. Its definition includes both the removed features and what replaces them.

With independent replacement draws $$U_1,\ldots,U_B$$, the Monte Carlo estimate is

$$
\widehat{\Delta}_Q(J;x)
=
F(x)
-
\frac{1}{B}
\sum_{b=1}^{B}
F\bigl(T_J(x,U_b)\bigr).
$$

Taking the expectation over those draws,

$$
\begin{aligned}
\mathbb E[\widehat{\Delta}_Q(J;x)]
&=
F(x)
-
\frac{1}{B}
\sum_{b=1}^{B}
\mathbb E\left[F\bigl(T_J(x,U_b)\bigr)\right] \\
&=
F(x)
-
\mathbb E_Q\left[F\bigl(T_J(x,U)\bigr)\right] \\
&=
\Delta_Q(J;x).
\end{aligned}
$$

Thus the estimate is unbiased for the stated perturbation quantity, conditional on the fixed input, feature set, and replacement distribution.

That result says nothing about whether the replacements represent a clinically meaningful absence of evidence. More replacement samples can reduce Monte Carlo uncertainty while leaving the wrong explanatory question unchanged.

### What a deletion ranking evaluates

Suppose an explanation ranks disjoint regions, and $$J_k$$ contains the first $$k$$ regions in that ranking. A simple summary is

$$
D_Q(E;x)
=
\frac{1}{d}
\sum_{k=1}^{d}
\Delta_Q(J_k;x),
$$

where $$d$$ is the total number of regions.

This rewards rankings whose early deletions produce large score drops under $$Q$$. Other deletion summaries use different integration weights or summarize remaining scores instead of drops. Their direction and normalization must be stated.

The test requires several choices that affect its meaning:

1. **Feature grouping.** Pixels, patches, anatomical regions, and concepts define different interventions.
2. **Replacement.** Zeroing, blurring, reference sampling, and conditional inpainting remove and introduce different information.
3. **Ranking convention.** Removing positive evidence should usually reduce the explained score; removing negative evidence can correctly increase it.
4. **Budget.** Rankings should be compared at matched area, feature count, or another declared intervention budget.
5. **Controls.** Random rankings, low-ranked regions, and relevant nuisance regions help interpret the result.

A high deletion score establishes responsiveness under these choices. It does not establish that the edited input is a plausible patient state.

### The local limit connects perturbation tests to gradients

For a differentiable model, consider a small perturbation

$$
x'=x+\varepsilon\delta.
$$

If the model is sufficiently smooth near the input, Taylor expansion gives

$$
F(x+\varepsilon\delta)
=
F(x)
+
\varepsilon\nabla F(x)^\top\delta
+
O(\varepsilon^2).
$$

The corresponding score drop is

$$
F(x)-F(x+\varepsilon\delta)
=
-\varepsilon\nabla F(x)^\top\delta
+
O(\varepsilon^2).
$$

A gradient explanation therefore predicts the first-order response to a small displacement. Testing that prediction requires respecting its scale and direction.

A finite occlusion is not generally a small displacement. Comparing a point gradient with the effect of replacing an entire structure tests additional assumptions about how the model behaves between the original and edited inputs.

A failed large-deletion prediction does not automatically show that the gradient was calculated incorrectly. It can show that local sensitivity was interpreted as a finite contribution without justification.

### Redundancy and interaction defeat simple removal logic

Consider a model with redundant binary evidence:

$$
F(x_1,x_2)=\max(x_1,x_2).
$$

At $$x=(1,1)$$,

$$
F(1,1)=1.
$$

Deleting either feature alone gives

$$
F(0,1)=F(1,0)=1.
$$

Both individual drops are therefore zero. Deleting both gives

$$
F(0,0)=0,
$$

so the joint drop is one.

The absence of an individual deletion effect does not establish that a feature could never support the prediction. The other feature can substitute for it.

Now consider an interaction:

$$
G(x_1,x_2)=x_1x_2.
$$

Again start at $$x=(1,1)$$. Then

$$
G(1,1)=1,
\qquad
G(0,1)=G(1,0)=G(0,0)=0.
$$

Each individual deletion produces a drop of one, but the joint deletion also produces a drop of one.

| Model at $$x=(1,1)$$ | Delete first feature | Delete second feature | Delete both |
|---|---|---|---|
| $$F=\max(x_1,x_2)$$ | Drop $$0$$ | Drop $$0$$ | Drop $$1$$ |
| $$G=x_1x_2$$ | Drop $$1$$ | Drop $$1$$ | Drop $$1$$ |

Individual deletion effects need not add to the total score difference. An additive explanation must adopt a convention for distributing interactions or redundancy.

It is therefore inappropriate to demand that every additive attribution simultaneously equal every subset-removal effect. Those requirements can be mathematically incompatible.

### Replacement can change the question even without changing the model

Suppose the data contain two perfectly correlated binary features:

$$
X_1=X_2,
$$

and the model is

$$
F(x_1,x_2)=x_1.
$$

At $$x=(1,1)$$, replacing the first feature with zero gives

$$
F(1,1)-F(0,1)=1.
$$

But a conditional replacement drawn from the data distribution given $$X_2=1$$ must restore

$$
X_1'=1.
$$

The corresponding drop is

$$
F(1,1)-F(1,1)=0.
$$

The model has not changed. The comparison has.

Zero replacement asks about forcing an input coordinate to a reference value. Conditional replacement asks what happens when that coordinate is reconstructed from the information retained in the other coordinates.

Both quantities can be useful. Calling either one the unique amount of model reliance would hide the distinction.

Perfect correlation also creates an identification problem for observational audits. If clinical features and acquisition markers always co-occur in the audit data, observing prediction agreement on those data cannot distinguish reliance on one from reliance on the other. A discriminating test needs informative variation or a defensible intervention.

### A perturbation effect is not automatically a clinical causal effect

An image edit acts on the model's input. It does not necessarily correspond to changing the patient's disease, changing a finding while preserving other findings, or performing an available clinical intervention.

For a clinical interpretation of a perturbation effect, the audit must justify that:

- The nominated feature actually changed.
- Competing evidence was preserved or its changes were measured.
- The replacement did not introduce a new diagnostic cue.
- Acquisition artifacts did not dominate the response.
- The edited input is appropriate for the model and explanatory question.

An inpainting method can produce a realistic image while changing more than the intended feature. A mask can produce an unrealistic image whose prediction changes because the model detects corruption. Visual realism and intervention specificity therefore need separate checks.

The defensible conclusion is often narrower: the output changed under the declared input intervention. A claim about clinical evidence reliance needs the additional bridge from that intervention to the clinical factor.

### Different checks close different gaps

Model randomization and label randomization ask whether explanations depend on learned parameters and learned task structure. They are useful challenges to model-specific interpretations.

Their interpretation still requires care. Shared anatomical edges can persist across models, and normalizing each heatmap separately can conceal changes in magnitude. A comparison should establish what changed in model behavior and whether the explanation was expected to reflect that change.

A practical audit can separate the following questions:

| Audit question | Evidence it can provide | What remains unresolved |
|---|---|---|
| Does the map overlap an anatomical annotation? | Spatial agreement | Which evidence inside that region was used |
| Does it respond to relevant model changes? | Dependence on aspects of the fitted predictor | Clinical appropriateness of that dependence |
| Does it predict controlled output changes? | Behavioral agreement under specified interventions | Validity of the intervention as a clinical change |
| Does it agree with independent clinical-factor assessments? | Alignment with measured clinical properties | Whether association reflects actual use |
| Does its interpretation remain useful across cases and settings? | Scope and stability of the explanatory claim | Untested mechanisms and populations |

These results should be reported separately. Collapsing them into a single “explainability” score obscures which link has actually been tested.

Clinical-factor labels also need provenance. A descriptor assessed with knowledge of the diagnosis may partly reproduce that diagnosis. A factor annotated only in easy, well-visualized cases supports a restricted population claim. The audit reference must be sufficiently independent and assessable for the interpretation being made.

### Revision checklist

| Question | What I should be able to state |
|---|---|
| What is explained? | The exact output, model version, and inference conditions |
| What is the explanatory claim? | A derivative, allocation, finite effect, concept sensitivity, or internal mechanism |
| What establishes plausibility? | A specified human reference with known scope and limitations |
| Why are plausibility and faithfulness independent? | All four cells exist in the constructed example |
| What does deletion measure? | An output change under a declared replacement mechanism |
| Why can a useful feature have zero deletion effect? | Another feature can provide redundant information |
| Why do individual deletion effects fail to add? | Interactions change the effect of removing features jointly |
| What does conditional replacement preserve? | Information reconstructable from retained features |
| What makes a clinical reliance claim stronger? | Independent factor assessment plus discriminating behavioral evidence |
| What does a convincing display establish by itself? | Its visual or semantic agreement with the chosen reference |

## Why it matters for my work

For gallbladder ultrasound, I need to distinguish anatomical agreement, model-sensitive readouts, and evidence that the predictor uses an independently assessed finding. In the ontology, Plausibility does not establish Faithfulness, and Faithfulness does not establish Clinical evidence reliance. Clinical assessability also limits which factor-level claims the available images can support.

## What I have not resolved

- Which ultrasound interventions change a nominated finding while preserving competing evidence and acquisition context?
- How should an audit represent cases in which clinical plausibility is assessable but model reliance remains unidentified?

---

Sources: Arun and colleagues, Assessing the Trustworthiness of Saliency Maps for Localizing Abnormalities in Medical Imaging; Adebayo and colleagues, Sanity Checks for Saliency Maps. The mathematical examples are constructed demonstrations, not empirical clinical results. These are study notes for research purposes, not clinical guidance.
