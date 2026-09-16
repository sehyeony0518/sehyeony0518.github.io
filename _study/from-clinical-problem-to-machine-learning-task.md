---
layout: study_note
title: "From Clinical Problem to Machine Learning Task"
description: "The translation step where most medical AI projects are decided, long before a model is trained."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalisation & Reliability"
subgroup: "Task Definition & Ground Truth"
order: 1
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-03-07-diabetic-retinopathy-preferred-practice"
  - "2025-12-19-eyepacs-grading-protocol"
---

A clinical problem does not uniquely define a prediction task. The translation requires choosing a decision, target, prediction unit, population, input boundary, reference standard, and operating rule. Those choices determine what a successful model can establish.

## Core question and definition

A concern such as missed gallbladder malignancy could motivate several different systems:

- An acquisition aid that identifies insufficient visualization.
- A detector that finds an unsuspected lesion.
- A classifier that characterizes an already identified lesion.
- A triage system that prioritizes examinations for review.
- A decision-support system that combines imaging with clinical information.

These systems can process overlapping data while answering different questions.

A useful task specification includes the following.

| Element | Required statement | What the choice limits |
|---|---|---|
| Clinical decision | What action could change because of the output? | Which benefits and harms are relevant |
| Comparator | What happens without the proposed system? | The improvement that can be claimed |
| Target | What state or event is being predicted? | The meaning of a correct prediction |
| Reference standard | How is the target operationally assessed? | What the labels can establish |
| Prediction unit | Frame, lesion, examination, or patient | The denominator and required aggregation |
| Population | Who is eligible at the intended point of use? | Where performance is intended to apply |
| Prediction time | When must the output be available? | Which inputs are permissible |
| Output | Score, category, location, uncertainty, or action | How a user can interpret it |
| Operating rule | Threshold, abstention, capacity, and fallback | Which errors and workloads occur |
| Evaluation design | What evidence tests the intended claim? | The scope of the resulting conclusion |

The specification should make difficult cases meaningful: missing views, multiple lesions, uncertain reference labels, technically inadequate examinations, and outputs arriving too late to affect the decision.

## Key concepts

### Start from a decision and a comparator

A prediction has clinical value only through a role in care. The first question is what the user would do differently with the output.

A second reader, triage aid, acquisition assistant, and replacement test have different comparators. A second reader might be compared with the same clinician working without assistance. A triage system might be compared with the existing review order. An acquisition aid might be compared with the current scanning workflow.

This distinction changes the relevant error.

- A triage miss can delay review.
- A false triage alert can divert attention from another examination.
- An acquisition false negative can leave an examination incomplete.
- An acquisition false positive can produce unnecessary repeat scanning.
- A characterization error can influence a diagnostic or referral decision.

The task should identify the current failure mechanism before selecting an algorithm. If the relevant lesion is never captured in the available images, improving a classifier on carefully selected lesion frames addresses only a later stage of the problem.

### Separate the clinical target from the observed label

Let

- $$D$$ be the clinical state of interest.
- $$L$$ be the recorded training label.
- $$X$$ be the permitted input.
- $$S=1$$ indicate inclusion in the development dataset.

For a probabilistic binary predictor $$q(x)$$, the conditional population cross-entropy on that dataset is

$$
\ell(q;x)
=
-p_L(x)\log q
-
\bigl(1-p_L(x)\bigr)\log(1-q),
$$

where

$$
p_L(x)=P(L=1\mid X=x,S=1).
$$

Differentiate with respect to $$q$$:

$$
\begin{aligned}
\frac{\partial\ell}{\partial q}
&=
-\frac{p_L}{q}
+
\frac{1-p_L}{1-q} \\
&=
\frac{-p_L(1-q)+(1-p_L)q}{q(1-q)} \\
&=
\frac{q-p_L}{q(1-q)}.
\end{aligned}
$$

For an interior optimum,

$$
q=p_L.
$$

The loss is convex in $$q$$, so this is the population minimizer. Endpoint cases are obtained by the corresponding limits.

Thus, with sufficient flexibility and successful population optimization, the learning objective targets

$$
P(L=1\mid X=x,S=1).
$$

It does not automatically target

$$
P(D=1\mid X=x)
$$

in the intended population.

The two quantities coincide only under appropriate relationships between the clinical state, reference label, selection process, and population. More training data can improve estimation of the wrong conditional probability.

Finite models and finite datasets introduce further estimation and optimization limitations; they do not repair a mismatch in the target being learned.

### A constructed example: predicting management is not predicting disease

Suppose a toy population contains one hundred patients:

- Twenty have disease.
- Eighty do not.
- Every diseased patient receives a management action.
- Twenty nondiseased patients also receive that action because of another indication.

The action label and disease state are therefore:

| Disease state | Action performed | Action not performed | Total |
|---|---:|---:|---:|
| Disease present | 20 | 0 | 20 |
| Disease absent | 20 | 60 | 80 |
| Total | 40 | 60 | 100 |

Imagine a model predicts the action label perfectly.

Its action accuracy is one. If its positive output is instead interpreted as a disease prediction, the disease confusion counts become

$$
TP=20,
\qquad
FP=20,
\qquad
FN=0,
\qquad
TN=60.
$$

Consequently,

$$
\operatorname{Sensitivity}
=
\frac{20}{20}
=
1,
$$

$$
\operatorname{Specificity}
=
\frac{60}{80}
=
\frac34,
$$

and

$$
\operatorname{PPV}
=
\frac{20}{40}
=
\frac12.
$$

Disease accuracy is

$$
\frac{20+60}{100}
=
\frac45.
$$

The model's perfect performance on the recorded target has not become perfect disease prediction.

In real task design, surgery, referral, additional imaging, and specialist review are management events. They can reflect symptoms, uncertainty, suitability, local resources, and policy as well as disease.

Predicting such an event can be a legitimate task. It must be named as that task, and its transportability includes the stability of the management policy.

### The reference standard must match the target and unit

A pathology label, imaging interpretation, follow-up outcome, and registry code answer different questions.

A specimen-level diagnosis needs to be matched to the imaged lesion and relevant examination. A patient-level cancer diagnosis does not establish that every saved frame contains a visible malignant finding.

Similarly:

- A lesion annotation can support lesion detection evaluation.
- An examination diagnosis can support examination-level classification.
- A reader's adequacy assessment can support acquisition-quality evaluation.
- A future outcome can support prognosis over a defined horizon.

Using a broader label for a smaller unit requires an explicit observation model. If every frame from a positive patient receives a positive image label, the model is trained on patient association, including frames where the relevant lesion is absent.

That may be usable in a multiple-instance design, where the examination is the labeled unit and frames are instances. It should not be described as independently verified frame-level disease labeling.

Uncertain or partially verified cases also need a policy. Excluding them can change the population; treating them as negative can change the target. Neither choice should occur invisibly during data cleaning.

### Frame-level risk and examination-level risk are different estimands

Suppose patient or examination $$i$$ contributes $$m_i$$ frames. Let $$\ell_{ij}$$ be the error loss on frame $$j$$, and define that examination's average frame loss as

$$
\overline\ell_i
=
\frac1{m_i}
\sum_{j=1}^{m_i}\ell_{ij}.
$$

The pooled frame-level average is

$$
\begin{aligned}
\widehat R_{\mathrm{frame}}
&=
\frac{
\sum_i\sum_j\ell_{ij}
}{
\sum_i m_i
} \\
&=
\frac{
\sum_i m_i\overline\ell_i
}{
\sum_i m_i
}.
\end{aligned}
$$

Examinations with more frames receive more weight.

An equally weighted average of examination-specific frame losses would instead be

$$
\frac1n\sum_i\overline\ell_i.
$$

Even that is not the risk of an examination-level decision. If $$A$$ aggregates frame scores and $$a$$ converts the aggregate into an action, examination-level risk is

$$
\widehat R_{\mathrm{exam}}
=
\frac1n
\sum_i
\ell\left(
a\left(A(F(x_{i1}),\ldots,F(x_{im_i}))\right),
D_i
\right).
$$

The aggregation and action occur before evaluating the examination-level loss.

Changing the prediction unit therefore changes both weighting and the decision rule being evaluated.

### Aggregation changes the operating point

Consider a constructed negative examination containing $$m$$ frames. Suppose each frame has false-positive probability $$p$$ and the examination is flagged if any frame is positive.

If frame false-positive events are independent conditional on the negative examination, then

$$
P(\text{no frame is positive})=(1-p)^m.
$$

The examination false-positive probability is

$$
P(\text{examination flagged})
=
1-(1-p)^m.
$$

For the toy values

$$
p=\frac1{10},
\qquad
m=2,
$$

this becomes

$$
1-\left(\frac9{10}\right)^2
=
1-\frac{81}{100}
=
\frac{19}{100}.
$$

The examination-level false-positive probability is already different from the frame-level value.

Independence is an assumption, not a property of medical image sequences. If the two false-positive events are identical, the examination false-positive probability remains one tenth.

More generally, if each frame has marginal false-positive probability $$p$$,

$$
p
\leq
P\left(\bigcup_{j=1}^{m}\{\text{frame }j\text{ positive}\}\right)
\leq
\min(mp,1).
$$

The lower bound follows because the union contains each individual event. The upper bound follows from the union bound and the fact that a probability cannot exceed one.

The number and dependence of frames can therefore alter examination behavior even when the frame classifier is unchanged. The complete aggregation rule must be evaluated on examinations representative of intended use.

### Conditional component performance can conceal pipeline failures

Let:

- $$A$$: the relevant evidence is adequately acquired.
- $$B$$: the lesion is successfully detected.
- $$C$$: the detected lesion receives the required positive classification.

For a diseased patient, the probability of success through this specified pipeline is

$$
\begin{aligned}
P(A\cap B\cap C\mid D=1)
&=
P(A\mid D=1) \\
&\quad\times P(B\mid A,D=1) \\
&\quad\times P(C\mid A,B,D=1).
\end{aligned}
$$

This is the probability chain rule. It does not require independence between the stages.

Construct twenty positive examinations:

- Sixteen adequately capture the relevant evidence.
- Twelve of those sixteen have the lesion detected.
- Eleven of those twelve are classified positively.

Then

$$
P(A\cap B\cap C\mid D=1)
=
\frac{16}{20}
\cdot
\frac{12}{16}
\cdot
\frac{11}{12}
=
\frac{11}{20}.
$$

A study of supplied, detected lesions would report classification sensitivity

$$
\frac{11}{12}.
$$

The specified end-to-end pipeline succeeds on

$$
\frac{11}{20}
$$

of the positive examinations.

Both fractions are correct for their denominators. They support different claims.

If the actual system has fallback review, reacquisition, or another route to detection, that pathway must be incorporated into the workflow evaluation. The product above describes only the stated sequential route.

### Prediction time defines the information boundary

Let $$t_0$$ be the time at which the prediction must be available. The input should contain only information available to the intended user and system by $$t_0$$.

A system for detecting an unsuspected lesion cannot silently receive:

- A crop selected after the lesion was recognized.
- A caliper placed because a clinician already identified the abnormality.
- A report completed after diagnostic review.
- An examination selected because pathology later confirmed the target.

Some of these inputs can be legitimate for a different task. A lesion-characterization model may appropriately receive targeted views and localization. The issue is whether the inputs match the claimed point of use.

Prognostic tasks need additional timing choices. A future-event label requires a baseline, an outcome definition, and a prediction horizon. Incomplete follow-up is not automatically an event-free outcome. Outcomes observed under existing care also do not directly label what would have happened without that care.

### Population selection determines the meaning of performance

Let the intended population distribution be $$P_{\mathrm{use}}$$. The desired risk is

$$
R_{\mathrm{use}}
=
\mathbb E_{P_{\mathrm{use}}}
\left[
\ell(a(F(X)),D)
\right].
$$

A selected retrospective dataset instead estimates a quantity such as

$$
R_{\mathrm{selected}}
=
\mathbb E
\left[
\ell(a(F(X)),D)
\mid S=1
\right].
$$

The quantities need not agree.

A referral population can contain different disease stages, difficult benign mimics, acquisition protocols, and prior testing than an unselected clinical population. Restricting a dataset to verified or well-visualized lesions changes both the cases and the conditions under which the task is attempted.

The task specification should state whether it concerns:

- All eligible examinations.
- Examinations with sufficient technical quality.
- Patients with an identified lesion.
- Patients already referred for specialist assessment.
- Cases with a particular available reference standard.

These are legitimate scopes when stated explicitly. Evidence from one scope does not automatically support another.

### Clinical assessability places an information limit on the task

An image-only model can use only the information present in its permitted inputs, including population associations. It cannot guarantee that an unobserved finding was visually identified.

Suppose the same available input $$x$$ is compatible with both disease states, with

$$
P(D=1\mid X=x)=\eta(x),
\qquad
0<\eta(x)<1.
$$

A deterministic positive decision has conditional error

$$
1-\eta(x).
$$

A deterministic negative decision has conditional error

$$
\eta(x).
$$

The smallest possible conditional classification error is therefore

$$
\min\{\eta(x),1-\eta(x)\}.
$$

Averaging yields the Bayes error for the specified input and population:

$$
R^*
=
\mathbb E_X
\left[
\min\{\eta(X),1-\eta(X)\}
\right].
$$

This does not say that a particular clinical dataset has a known irreducible error. It shows why overlapping information states can prevent perfect image-only classification even with ideal learning.

The appropriate task response may be uncertainty, additional views, a request for another modality, or referral. That response must be defined rather than forcing every inadequate examination into a confident diagnostic category.

### Deriving the operating point from error consequences

Assume a binary action with:

- False-positive cost $$C_{\mathrm{FP}}>0$$.
- False-negative cost $$C_{\mathrm{FN}}>0$$.
- Zero loss for correct actions in this simplified formulation.

Let

$$
p=P(D=1\mid X=x)
$$

be the relevant disease probability in the intended setting.

The expected loss of a positive action is

$$
R_+(x)
=
C_{\mathrm{FP}}(1-p).
$$

The expected loss of a negative action is

$$
R_-(x)
=
C_{\mathrm{FN}}p.
$$

Choose the positive action when

$$
C_{\mathrm{FP}}(1-p)
\leq
C_{\mathrm{FN}}p.
$$

Rearranging,

$$
C_{\mathrm{FP}}
\leq
p(C_{\mathrm{FP}}+C_{\mathrm{FN}}),
$$

so the threshold is

$$
p
\geq
\frac{C_{\mathrm{FP}}}
{C_{\mathrm{FP}}+C_{\mathrm{FN}}}.
$$

A threshold of one half follows only when the two error costs are equal in this formulation.

The derivation concerns a relevant probability and specified consequences. Applying the formula to an uncalibrated score does not preserve its decision-theoretic meaning. Real workflows can also require additional terms for review burden, delay, adverse consequences of action, and patient preferences.

### A worked example: equal utility can imply different workloads

Construct an evaluation set with twenty positive and eighty negative cases. Two operating points on a score produce:

| Operating point | True positives | False positives | False negatives | True negatives | Positive actions |
|---|---:|---:|---:|---:|---:|
| Lower cutoff | 18 | 24 | 2 | 56 | 42 |
| Higher cutoff | 14 | 8 | 6 | 72 | 22 |

These counts can come from nested decision sets: raising the cutoff removes four true positives and sixteen false positives.

Suppose, for this construction only, that a true-positive action has benefit

$$
B=4
$$

and a false-positive action has harm

$$
H=1,
$$

both measured relative to taking no action.

The lower cutoff has utility

$$
U_{\mathrm{lower}}
=
18\cdot4-24\cdot1
=
48.
$$

The higher cutoff has utility

$$
U_{\mathrm{higher}}
=
14\cdot4-8\cdot1
=
48.
$$

Their benefit-normalized net benefit per case is also equal:

$$
NB
=
\frac{TP}{100}
-
\frac{FP}{100}\frac{H}{B}.
$$

For the lower cutoff,

$$
NB_{\mathrm{lower}}
=
\frac{18}{100}
-
\frac{24}{100}\frac14
=
\frac{12}{100}
=
\frac3{25}.
$$

For the higher cutoff,

$$
NB_{\mathrm{higher}}
=
\frac{14}{100}
-
\frac8{100}\frac14
=
\frac{12}{100}
=
\frac3{25}.
$$

But one point produces forty-two actions and the other twenty-two. With a constructed capacity of thirty reviews, the first is infeasible under a policy requiring review of every positive output; the second is feasible.

This does not establish that the higher cutoff is globally optimal. A capacity-aware policy could require a different ranking or tie-breaking rule. It establishes that equal net benefit under a simplified loss does not imply equal workflow demands.

The clinical task must specify the action and capacity constraint before an operating point can be called appropriate.

### Two gallbladder tasks require different evidence

Consider two hypothetical systems.

| Design choice | Acquisition assessment | Characterization of an identified lesion |
|---|---|---|
| Immediate question | Are the required structures and views adequately visualized? | What can be inferred about the identified lesion? |
| Input | The acquisition sequence available at the assessment time | Permitted targeted views and localization |
| Unit | Acquisition episode or examination | Lesion, with an examination-level policy if needed |
| Reference | Independent assessment of adequacy under a defined protocol | A lesion-matched clinical reference standard |
| Important failure | Declaring an inadequate examination sufficient | Mischaracterizing a lesion or overstating certainty |
| Useful output | Adequate, specific missing information, or request for another view | Risk estimate, category, uncertainty, or referral recommendation |
| Evaluation | Adequacy errors, repeat scanning, time, and workflow consequences | Diagnostic performance, calibration, operating-point consequences, and population scope |

A cancer diagnosis is an indirect label for acquisition adequacy. An adequacy annotation is not a reference standard for malignancy.

A characterization model evaluated only after localization cannot claim that it detects unsuspected lesions. An acquisition aid cannot claim diagnostic benefit solely from agreement with adequacy annotations. The connection to clinical outcomes requires evaluation of the relevant workflow.

### Validation should test the declared task

The task specification determines the validation design.

- Split and analyze at the unit needed to prevent information sharing between development and evaluation cases.
- Reproduce input availability at the intended prediction time.
- Include technical failures, abstentions, and missing inputs in the appropriate denominators.
- Validate the aggregation rule and operating point as part of the system.
- Use reference information matched to the target, lesion, and time.
- Evaluate the intended population and relevant changes in case mix, acquisition, and labeling.
- Compare the human-system workflow with its declared comparator when claiming clinical benefit.

Thresholds, aggregation rules, and failure policies should be selected without using the final test outcomes. A final test set becomes development data if it repeatedly determines those choices.

Reporting frameworks help make these decisions visible. Clear reporting cannot repair an invalid target or supply missing evidence of benefit. A prediction study and an evaluation of clinical use remain different studies.

### Revision checklist

| Question | What I should be able to state |
|---|---|
| What decision changes? | The intended action, user, timing, and comparator |
| What is the clinical target? | A disease state, finding, management event, or future outcome |
| What does the training objective learn? | The conditional distribution of the recorded label in the sampled population |
| Where does the label come from? | Its reference standard, unit, timing, uncertainty, and verification process |
| What is the prediction unit? | The unit on which outputs and consequences are evaluated |
| How are multiple images combined? | A declared aggregation rule evaluated at the action unit |
| What component denominator is being reported? | All eligible cases or a conditional subset |
| Which inputs are permitted? | Information available before the intended decision |
| What population is covered? | Eligibility, setting, case mix, and technical requirements |
| What sets the operating point? | Relevant probabilities, error consequences, workload, and fallback |
| What happens when evidence is insufficient? | An explicit uncertainty, abstention, reacquisition, or referral policy |
| What supports clinical benefit? | Evaluation of the system's effect relative to the intended comparator |

## Why it matters for my work

The task defines which clinical evidence a gallbladder model should be expected to use. In the ontology, the ClinicalTarget setsRequirementsFor the method and its evaluation. Clinical assessability then limits the conclusions available from the chosen inputs. An acquisition model and a malignancy model should consequently face different evidence-reliance audits.

## What I have not resolved

- Which decision in the available clinical workflow can realistically improve with the data and reference information I can obtain?
- How should the system respond when the intended clinical question cannot be answered from the examination supplied?

---

Sources: Standard conditional-risk and decision-theoretic derivations, with constructed examples in this note; TRIPOD+AI for transparent prediction-model reporting; DECIDE-AI for early clinical evaluation of AI decision support and its human interaction. These are study notes for research purposes, not clinical guidance.
