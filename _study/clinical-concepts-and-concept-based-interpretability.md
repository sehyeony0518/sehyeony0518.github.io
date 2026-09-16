---
layout: study_note
title: "Clinical Concepts and Concept-Based Interpretability"
description: "Concept bottlenecks and concept activation vectors as attempts to make a model speak in clinical terms."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "alignment"
category_title: "Clinical Alignment & Interpretability"
subgroup: "Clinical Supervision & Concepts"
order: 2
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-11-29-concept-bottleneck-models"
  - "2025-09-19-tcav-concept-activation-vectors"
  - "2026-08-10-concept-gradients-nonlinear-interpretation"
---

Concept-based interpretability connects model variables to named properties such as lesion attachment, size, or echogenicity. Its central difficulty is establishing what those variables measure and what role they actually play in prediction.

## Core question and definition

Three claims must be separated:

1. **A concept is recoverable from a representation.**
2. **The model output responds to a specified change in that representation.**
3. **The model uses the intended clinical concept to make its prediction.**

The first is a measurement claim about a readout. The second is a computational sensitivity claim. The third additionally requires a valid connection between the computational change and the clinical concept.

A concept label does not establish that connection merely by naming a variable. Nor does high concept-prediction accuracy establish that the diagnostic head uses the concept.

Two major approaches address different parts of this problem:

- A **concept activation vector** probes an existing model representation.
- A **concept bottleneck** places predicted concepts on the path to the final output.

Both need independent scrutiny of concept definitions, measurement quality, and the information available to the predictor.

## Key concepts

### A clinical concept starts with an observation protocol

A concept should specify what is assessed and under what conditions.

| Concept property | Required clarification |
|---|---|
| Unit | Frame, lesion, examination, or patient |
| Definition | The observable property and permitted categories or measurement scale |
| Reference | What comparison makes the judgment meaningful |
| Visibility | Which views or acquisition conditions are required |
| Uncertainty | How borderline, missing, and unassessable cases are represented |
| Provenance | Who assessed it, using what information, and with what adjudication |
| Timing | Whether the assessment corresponds to the model's prediction time |

Size needs a measurement convention. Echogenicity needs a reference. Attachment may be difficult to assess in a saved view that does not show the relevant interface.

“Not visible,” “not assessed,” and “absent” are different states. Coding all three as absence trains a concept predictor to reproduce a mixture of biology, acquisition, and annotation practice.

The model may still predict a likely concept from correlated information when that concept is not directly assessable. Such a prediction is an inference. It should not be described as evidence that the finding was visible in the image.

### Constructing a concept activation vector

Let a fixed network produce layer activations

$$
z=h_\ell(x)\in\mathbb R^d.
$$

Let the selected output downstream of that layer be

$$
F_k(x)=H_{\ell,k}(z).
$$

Collect concept examples and comparison examples. Give their set-membership labels

$$
t_i\in\{-1,+1\}.
$$

A linear probe predicts membership using

$$
q(z)=w^\top z+b.
$$

For example, it can be fitted with regularized logistic loss:

$$
\min_{w,b}
\frac1n
\sum_{i=1}^{n}
\log\left(1+\exp(-t_i(w^\top z_i+b))\right)
+
\frac{\lambda}{2}\|w\|_2^2.
$$

This optimization asks whether a linear boundary separates the example sets in the chosen activation coordinates. It does not directly optimize the diagnostic model or identify a disease mechanism.

The separating boundary is

$$
w^\top z+b=0.
$$

Its normal direction is $$w$$. To see why, consider a displacement $$u$$ within the boundary. The probe value remains unchanged when

$$
w^\top u=0.
$$

Thus directions tangent to the boundary are orthogonal to $$w$$.

Orient $$w$$ toward the positive concept examples and normalize it:

$$
v_C=\frac{w}{\|w\|_2},
$$

provided $$w\neq0$$.

Moving by $$\varepsilon v_C$$ changes the probe score by

$$
\begin{aligned}
q(z+\varepsilon v_C)-q(z)
&=
w^\top(\varepsilon v_C) \\
&=
\varepsilon
\frac{w^\top w}{\|w\|_2} \\
&=
\varepsilon\|w\|_2.
\end{aligned}
$$

The normalized direction therefore moves toward increasing membership score per unit Euclidean displacement in activation space.

That is what the construction guarantees geometrically. Whether increasing membership score means increasing the intended clinical property is an additional assumption about the examples and representation.

### Deriving sensitivity along the concept direction

The directional derivative of the selected output is

$$
D_{C,k,\ell}(x)
=
\lim_{\varepsilon\to0}
\frac{
H_{\ell,k}(h_\ell(x)+\varepsilon v_C)
-
H_{\ell,k}(h_\ell(x))
}{\varepsilon}.
$$

If the downstream function is differentiable at the activation,

$$
H_{\ell,k}(z+\varepsilon v_C)
=
H_{\ell,k}(z)
+
\varepsilon
\nabla_z H_{\ell,k}(z)^\top v_C
+
o(\varepsilon).
$$

Subtracting the original output, dividing by $$\varepsilon$$, and taking the limit gives

$$
D_{C,k,\ell}(x)
=
\nabla_z H_{\ell,k}(h_\ell(x))^\top v_C.
$$

This quantity measures the local output response to a unit displacement along the fitted direction.

It is not measured in physical concept units. A unit displacement along $$v_C$$ is not a unit increase in lesion size or a change from one clinical category to another.

The displaced activation may also have no corresponding real image. A valid directional derivative remains a derivative of the network's downstream function even when the displacement leaves the set of activations produced by plausible inputs. Its clinical interpretation then requires caution.

### A perfect probe can identify a concept the model ignores

Consider four equally weighted activation vectors:

$$
z\in
\{
(1,1),(1,-1),(-1,1),(-1,-1)
\}.
$$

Define the concept label as

$$
t=z_1.
$$

Fit a least-squares linear probe, followed by a sign decision. Its average squared loss is

$$
L(w_1,w_2,b)
=
\frac14
\sum_z
(w_1z_1+w_2z_2+b-z_1)^2.
$$

Rewrite the residual:

$$
w_1z_1+w_2z_2+b-z_1
=
(w_1-1)z_1+w_2z_2+b.
$$

Across the four points,

$$
\mathbb E[z_1]
=
\mathbb E[z_2]
=
\mathbb E[z_1z_2]
=
0,
$$

and

$$
\mathbb E[z_1^2]
=
\mathbb E[z_2^2]
=
1.
$$

Expanding the square and averaging therefore removes the cross terms:

$$
L(w_1,w_2,b)
=
(w_1-1)^2+w_2^2+b^2.
$$

The unique minimizer is

$$
w=(1,0),
\qquad
b=0.
$$

The probe classifies all four concept labels correctly, and its normalized direction is

$$
v_C=(1,0).
$$

Now let the diagnostic score be

$$
H(z)=z_2.
$$

Its gradient is

$$
\nabla H(z)=(0,1),
$$

so

$$
D_C(z)
=
(0,1)^\top(1,0)
=
0.
$$

More strongly, changing the first coordinate by any amount leaves the output unchanged:

$$
H(z_1+\delta,z_2)=z_2=H(z_1,z_2).
$$

The concept is perfectly recoverable, but this diagnostic head ignores it.

The example uses a least-squares classifier to make the calculation explicit. The logical distinction does not depend on this particular probe-fitting loss.

The converse also needs care: a failed linear probe does not establish that the representation contains no concept information. The information may be nonlinear, inadequately sampled, or poorly matched to the chosen operational definition.

### What a TCAV summary reports

For evaluated examples whose reference class is $$k$$, a sign-based TCAV summary is

$$
\widehat T_{C,k,\ell}
=
\frac{1}{n_k}
\sum_{i:Y_i=k}
\mathbf 1
\left\{
D_{C,k,\ell}(x_i)>0
\right\}.
$$

It estimates the frequency of positive directional sensitivity in the stated class and evaluation population, conditional on the fitted concept direction.

It is not the fraction of the prediction explained by the concept.

For example, consider

$$
H_\varepsilon(z)
=
\varepsilon z_1+z_2,
\qquad
\varepsilon>0,
$$

with $$v_C=(1,0)$$. Then

$$
D_C(z)=\varepsilon
$$

for every input. Every nonempty evaluated class set therefore has

$$
\widehat T_C=1.
$$

Yet the directional effect can be made arbitrarily small by reducing $$\varepsilon$$. A score of one here means that all evaluated slopes have positive sign, not that the concept accounts for the entire output.

Concept directions can also overlap. Positive sensitivities for several correlated concepts need not sum to one or partition the model's evidence.

A zero local derivative does not generally establish absence of finite dependence. That stronger conclusion held in the previous example because the entire downstream function was explicitly independent of the first coordinate.

### Assumptions behind a meaningful concept direction

The CAV construction requires more than a well-fitted separating boundary.

**The example contrast must represent the intended concept.** If all positive examples come from one scanner and comparison examples from another, the separating direction may represent acquisition. If the comparison set contains unrecognized positive cases, the learned contrast is between example sets rather than clean concept presence and absence.

**The audit needs informative variation.** If a concept and a nuisance never vary separately, their roles cannot be identified from that sample alone. Matching or stratification can help when the data contain relevant overlap; they cannot manufacture missing combinations.

**The coordinate system matters.** A probe normal and its unit normalization use the geometry of the selected activations. Rescaling activation coordinates changes Euclidean distance and can change the resulting normalized direction. The direction is not automatically an intrinsic clinical axis.

**Local linearity has a scope.** A useful separating direction near observed examples need not remain meaningful after a large displacement or in a different population.

**The downstream intervention must be interpretable.** Adding a vector to activations can alter several encoded properties. A directional derivative establishes response to that vector, not a selective intervention on the named clinical concept.

Probe performance, directional sensitivity, and semantic validity should consequently be reported as separate results.

### What a strict concept bottleneck guarantees

A strict concept bottleneck has the form

$$
\widehat c=g(x),
\qquad
F(x)=h(\widehat c).
$$

The diagnostic predictor receives only the concept representation.

Its exact structural implication is

$$
g(x)=g(x')
\quad\Longrightarrow\quad
F(x)=F(x').
$$

The model cannot distinguish inputs that produce exactly the same bottleneck values.

This is a real restriction, but it concerns the values actually passed through the bottleneck. It does not establish that those values contain only the semantics suggested by their names.

An auxiliary concept head has a different structure:

$$
z=f(x),
\qquad
\widehat c=g(z),
\qquad
F(x)=h(z).
$$

Here the diagnostic head can use any available component of $$z$$. Accurate concept prediction does not force diagnosis to depend on the predicted concepts.

A hybrid architecture,

$$
F(x)=h(g(x),r(x)),
$$

also permits information to bypass the concepts through $$r(x)$$. Such an architecture may be useful, but its interpretation must acknowledge that additional route.

### Training arrangements change the intervention interface

Several training choices are possible.

- The downstream predictor can be trained on annotated concepts.
- It can be trained on predicted concepts produced by a fitted concept model.
- Both stages can be optimized jointly using diagnostic and concept losses.

These arrangements expose the downstream predictor to different distributions.

A predictor trained on clean concept annotations may receive noisy predictions at deployment. A predictor trained on soft predictions may receive unfamiliar values when a user replaces them with hard annotations. Joint optimization can encourage scores to carry diagnostic information beyond their named concepts.

The relevant question is therefore not just whether concepts can be edited. It is whether the downstream predictor has been evaluated under the values, uncertainty, and combinations that actual edits will create.

### A constructed example of leakage through continuous concept scores

Let the input contain two independent fair bits,

$$
X=(C,Z),
$$

and let the prediction target be

$$
Y=Z.
$$

The named concept is $$C$$. The diagnostic signal $$Z$$ is available in the input; the construction does not supply the outcome file to the model at inference.

Because $$C$$ and $$Y$$ are independent, any predictor receiving only the exact hard concept $$C$$ has accuracy one half:

$$
P(h(C)=Y\mid C)=\frac12,
$$

and hence

$$
P(h(C)=Y)=\frac12.
$$

Now transmit a continuous “concept probability”

$$
\widehat C
=
(1-C)\varepsilon(1+Z)
+
C\left[1-\varepsilon(2-Z)\right],
$$

where

$$
0<\varepsilon<\frac14.
$$

Its four possible values are

| True concept $$C$$ | Target $$Y=Z$$ | Transmitted score $$\widehat C$$ |
|---|---|---|
| $$0$$ | $$0$$ | $$\varepsilon$$ |
| $$0$$ | $$1$$ | $$2\varepsilon$$ |
| $$1$$ | $$0$$ | $$1-2\varepsilon$$ |
| $$1$$ | $$1$$ | $$1-\varepsilon$$ |

Thresholding at one half recovers $$C$$ perfectly. The condition on $$\varepsilon$$ ensures that both scores for concept absence lie below one half and both scores for concept presence lie above it.

The concept mean squared error is

$$
\begin{aligned}
\mathbb E[(\widehat C-C)^2]
&=
\frac14
\left[
\varepsilon^2
+
(2\varepsilon)^2
+
(-2\varepsilon)^2
+
(-\varepsilon)^2
\right] \\
&=
\frac{10\varepsilon^2}{4} \\
&=
\frac52\varepsilon^2.
\end{aligned}
$$

This can be arbitrarily small while the four score values remain distinct.

For the concrete choice

$$
\varepsilon=\frac1{10},
$$

the scores are

$$
\frac1{10},
\quad
\frac15,
\quad
\frac45,
\quad
\frac9{10},
$$

and the mean squared error is

$$
\frac52\left(\frac1{10}\right)^2
=
\frac1{40}.
$$

The downstream predictor can recover the target perfectly. First recover the concept by thresholding:

$$
C^\dagger
=
\mathbf 1\{\widehat C>1/2\}.
$$

Define

$$
b(C^\dagger)
=
\begin{cases}
\varepsilon, & C^\dagger=0,\\
1-2\varepsilon, & C^\dagger=1.
\end{cases}
$$

Then, on the four constructed values,

$$
Y
=
\frac{\widehat C-b(C^\dagger)}{\varepsilon}.
$$

The continuous score transmits the target in small deviations around the nominal concept value.

Thus perfect thresholded concept accuracy and arbitrarily small concept squared error do not establish a semantically pure bottleneck.

Hardening these particular scores removes the hidden bit. In general, however, hardening is not a complete safeguard: predicted hard concepts can still be wrong in diagnostically informative ways, and discretization can discard useful uncertainty.

Extra information in a soft score is not automatically undesirable. The interpretive problem is claiming that the entire diagnostic computation is explained by the named concept when additional information is being transmitted.

### Concept interventions are computational interventions

In a bottleneck model, replacing concept coordinate $$j$$ with an assessed value $$c_j^*$$ gives

$$
F^{(j\leftarrow c_j^*)}(x)
=
h(
\widehat c_1,\ldots,
c_j^*,\ldots,
\widehat c_p
).
$$

The intervention effect is

$$
\Delta_j
=
F^{(j\leftarrow c_j^*)}(x)-F(x).
$$

This is an exact question about the downstream function and the replacement value. It does not establish what would happen if the patient's disease or anatomy changed.

A useful intervention evaluation checks:

- Whether the supplied value is independently assessable.
- Whether it is correct under the concept's operational definition.
- Whether the edited combination is clinically coherent.
- Whether the downstream predictor encountered comparable values during training.
- Whether correcting the concept improves the intended decision.
- Whether the correction removes unintended information encoded in the original score.

A correction can worsen the diagnostic output if the downstream model learned an inappropriate relationship or relied on score details erased by the correction. That failure is evidence about the interface and model, rather than proof that clinical correction is inherently unhelpful.

### Designing a concept audit

A defensible audit separates four levels.

| Level | Main question | Example evidence |
|---|---|---|
| Measurement | Does the concept readout correspond to an independently assessed finding? | Held-out concept agreement, assessability, reader disagreement |
| Representation | Is the concept recoverable from the selected activations? | Probe performance under appropriate controls |
| Computation | Does the output respond to the specified concept representation? | Directional derivatives, controlled bottleneck interventions |
| Clinical interpretation | Does the computational change correspond to the intended clinical evidence? | Valid edits, matched comparisons, review of competing findings |

Evaluation should also distinguish uncertainty from the fitted probe and uncertainty from the patient sample. Multiple frames from one patient do not become independent concept examples simply because they yield separate activations.

Repeating probes with different comparison samples can reveal instability. It does not by itself establish semantic validity. A confounded concept can be learned consistently.

### Revision checklist

| Question | What I should be able to explain |
|---|---|
| What is the concept? | Its unit, definition, reference, visibility, and uncertainty states |
| How is a CAV constructed? | Fit a linear contrast, orient its normal, and state normalization |
| Why is the probe normal relevant? | Moving along it increases the linear membership score |
| What is the directional derivative? | The downstream gradient dotted with the fitted direction |
| What does probe accuracy establish? | Recoverability under the probe and evaluation protocol |
| Why does recoverability not imply use? | A diagnostic head can ignore a perfectly decodable coordinate |
| What does the TCAV sign summary mean? | Frequency of positive local sensitivity in a stated population |
| What does a strict bottleneck enforce? | Equal bottleneck values imply equal model outputs |
| How can continuous concepts leak information? | Small score variations can encode information beyond the named labels |
| What does a concept correction test? | The downstream response to a specified computational replacement |
| What supports clinical evidence reliance? | Valid concept measurement plus evidence linking that concept to model behavior |

## Why it matters for my work

For gallbladder ultrasound, concepts can make an audit clinically specific, but only if their assessability and computational role are tested separately. The ontology distinction between Clinical feature annotation and Clinical evidence reliance is essential: a readable or accurate concept interface does not establish that the diagnostic model uses the intended finding.

## What I have not resolved

- Which clinical concepts retain reliable meaning across views, acquisition settings, and uncertain examinations?
- How can useful concept uncertainty be preserved while detecting diagnostic information hidden beyond the stated concept semantics?

---

Sources: Kim and colleagues, Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors; Koh and colleagues, Concept Bottleneck Models; Mahinpei and colleagues, Promises and Pitfalls of Black-Box Concept Learning Models. Probe and leakage examples are constructed demonstrations. These are study notes for research purposes, not clinical guidance.
