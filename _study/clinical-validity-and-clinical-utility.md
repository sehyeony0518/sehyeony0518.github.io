---
layout: study_note
title: "Clinical Validity and Clinical Utility"
description: "The difference between a model that measures something real and a model that changes a decision."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
order: 7
source: "Independent study"
written: true
updated: "2026-09-08"
---

Clinical validity concerns whether an output supports its intended clinical interpretation. Clinical utility concerns whether using that output improves relevant consequences compared with an alternative. The connection between them is a decision pathway, not a metric conversion.

## Core question and definition

A validity claim needs an explicit target, population, prediction time, unit of analysis, and reference standard.

A utility claim additionally needs an action, comparator, outcome, and account of the consequences of using the system.

For example, agreement with pathology can support a diagnostic interpretation under an appropriate sampling and matching procedure. Agreement with a referral decision supports an interpretation about referral behavior. Neither alone establishes that introducing the model improves care.

The chain to inspect is

$$
\text{available information}
\longrightarrow
\text{model output}
\longrightarrow
\text{clinical interpretation}
\longrightarrow
\text{action}
\longrightarrow
\text{consequence}.
$$

Errors can enter at every step. Correct predictions may not change actions. Changed actions may not improve outcomes. An apparent outcome improvement may arise from differences between the compared populations rather than from the system.

## Key concepts

### 1. Validity is agreement with an appropriate reference for a specified claim

Let $$Z$$ denote the clinical state of interest and $$Y$$ the recorded reference label.

A standard supervised evaluation compares a prediction with $$Y$$. The intended clinical claim may concern $$Z$$. Moving from one to the other requires a defensible relationship between the reference and the target.

| Reference | What it can support | Important limitation to examine |
|---|---|---|
| Tissue diagnosis | Findings in the sampled tissue | Sampling, patient selection, and matching tissue to the imaged target |
| Expert adjudication | A specified clinical interpretation | Information available to reviewers, disagreement, and independence |
| Follow-up outcome | What was observed over a defined period | Missing follow-up, treatment effects, and outcome ascertainment |
| Registry or administrative code | What was recorded in that system | Coding purpose, timing, and correspondence with the clinical definition |
| Management decision | What clinicians chose to do | Decisions also reflect resources, preferences, and uncertainty |

Even an accurate reference at one level may not identify the target at another. A patient-level diagnosis does not establish that every image frame contains visible evidence of that diagnosis.

Validity therefore includes the intended interpretation of the output. A model trained to recognize selected lesion images has not automatically been validated for finding lesions in an unselected examination.

### 2. A simple derivation shows why reference error matters

Consider a deliberately simplified binary model. Suppose the reference flips the true state independently with probability $$\varepsilon$$:

$$
Y=
\begin{cases}
Z,&\text{with probability }1-\varepsilon,\\
1-Z,&\text{with probability }\varepsilon.
\end{cases}
$$

Assume this flipping process is independent of the prediction and patient features conditional on the true state, with the same error probability in both classes.

Let

$$
a=\Pr(f(X)=Z)
$$

be the prediction's true agreement with the clinical state.

Agreement with the recorded label occurs in two mutually exclusive ways:

1. The prediction is correct and the reference is not flipped.
2. The prediction is wrong and the reference is flipped.

Therefore,

$$
\begin{aligned}
\Pr(f(X)=Y)
&=a(1-\varepsilon)+(1-a)\varepsilon\\
&=a-a\varepsilon+\varepsilon-a\varepsilon\\
&=\boxed{\varepsilon+(1-2\varepsilon)a}.
\end{aligned}
$$

Measured agreement is not true agreement.

This is an explanatory construction, not a general correction formula. Real reference errors can depend on disease subtype, visibility, reader access, or the model's own output. Without the simplifying independence assumptions and knowledge of $$\varepsilon$$, the equation cannot simply be inverted to recover clinical validity.

A reference created using the prediction itself can also produce circular agreement. Independence of adjudication is therefore part of what an agreement estimate is worth.

### 3. Prediction quality leaves the action unspecified

Suppose a model provides a risk estimate $$p$$. Knowing that the estimate is calibrated does not identify which action should follow it.

The answer depends on:

- What action is available.
- What benefit that action produces when indicated.
- What harm it produces when unnecessary.
- What current practice would otherwise do.
- Whether the action can occur in time.
- Whether the system changes workload or access for other patients.

A model can rank cases correctly while making no difference near the actual decision boundary. Conversely, a modest prediction improvement near that boundary can matter more than a large improvement among patients whose management would already be clear.

The decision analysis below makes these statements algebraic.

### 4. Derive the threshold probability from benefits and harms

For this calculation, let $$Y$$ represent an adequately ascertained binary target. Whether the actual dataset provides such a target remains a separate assumption.

Consider two actions: act or do not act. Subtract the utility of not acting within each outcome state. This sets the incremental utility of not acting to zero without assuming that missed disease is harmless.

Let:

- $$B>0$$ be the incremental benefit of acting when $$Y=1$$.
- $$H>0$$ be the incremental harm of acting when $$Y=0$$.

The incremental utility table is

| Action | $$Y=1$$ | $$Y=0$$ |
|---|---|---|
| Act | $$B$$ | $$-H$$ |
| Do not act | $$0$$ | $$0$$ |

For a patient with probability $$p$$ of the target state, expected incremental utility from acting is

$$
pB-(1-p)H.
$$

Acting is preferred when

$$
\begin{aligned}
pB-(1-p)H&\geq0,\\
pB-H+pH&\geq0,\\
p(B+H)&\geq H,\\
p&\geq\frac{H}{B+H}.
\end{aligned}
$$

Define the threshold probability

$$
\boxed{p_t=\frac{H}{B+H}.}
$$

Then

$$
\begin{aligned}
\frac{p_t}{1-p_t}
&=
\frac{H/(B+H)}{B/(B+H)}\\
&=\boxed{\frac HB}.
\end{aligned}
$$

Threshold odds encode the relative harm of an unnecessary action compared with the benefit of an appropriate one.

The threshold is therefore a statement about consequences. It is not intrinsically the cutoff maximizing accuracy, a geometric point on an ROC curve, or the most convenient division of model scores.

### 5. Derive net benefit

For a binary action rule evaluated in $$n$$ patients, total incremental utility under the preceding assumptions is

$$
B\cdot TP-H\cdot FP.
$$

Divide by $$n$$ to obtain utility per patient:

$$
\frac{BTP-HFP}{n}.
$$

Then divide by $$B$$ to express the result in units of true-positive benefit:

$$
\begin{aligned}
\operatorname{NB}
&=\frac{BTP-HFP}{nB}\\
&=\frac{TP}{n}-\frac{FP}{n}\frac HB\\
&=\boxed{
\frac{TP}{n}
-
\frac{FP}{n}\frac{p_t}{1-p_t}
}.
\end{aligned}
$$

This is net benefit.

False negatives do not appear explicitly because their lost benefit is encoded by the true positives not obtained. In the underlying utility table, the baseline has already absorbed the consequences of not acting within each state.

This derivation assumes constant $$B$$ and $$H$$ for the compared patients and actions. It also assumes the target state identifies when the stipulated benefit applies. A diagnostic label by itself does not establish the magnitude of a treatment's benefit.

### 6. Derive the usual comparator curves

Let prevalence be

$$
\pi=\Pr(Y=1).
$$

If nobody receives the action,

$$
\operatorname{NB}_{\mathrm{none}}=0.
$$

If everybody receives it,

$$
\begin{aligned}
\operatorname{NB}_{\mathrm{all}}
&=\pi-(1-\pi)\frac{p_t}{1-p_t}\\
&=\frac{\pi(1-p_t)-(1-\pi)p_t}{1-p_t}\\
&=\boxed{\frac{\pi-p_t}{1-p_t}}.
\end{aligned}
$$

Thus, acting on everyone has positive modeled value relative to acting on no one exactly when

$$
\pi>p_t.
$$

A perfect binary rule, with no additional implementation cost, acts on all positive patients and no negative patients:

$$
\operatorname{NB}_{\mathrm{perfect}}=\pi.
$$

These are useful reference strategies, but existing care may perform much better than either “all” or “none.” A model needs comparison with the relevant alternative, not just with an intentionally weak baseline.

### 7. A constructed example: lower accuracy, higher modeled utility

Construct a cohort of 100 patients containing 20 positives and 80 negatives.

Compare a new decision rule with an existing rule:

| Rule | TP | FP | FN | TN | Accuracy |
|---|---:|---:|---:|---:|---|
| New rule | 14 | 8 | 6 | 72 | $$86/100=43/50$$ |
| Existing rule | 12 | 4 | 8 | 76 | $$88/100=22/25$$ |

The new rule is less accurate because it makes more false-positive errors than the number of false negatives it avoids.

Now stipulate an abstract benefit of four units for an appropriate action and a harm of one unit for an unnecessary action:

$$
B=4,
\qquad H=1.
$$

These are constructed utility units, not clinical estimates.

The threshold probability is

$$
p_t=\frac1{4+1}=\frac15,
$$

and its odds are

$$
\frac{p_t}{1-p_t}=\frac14.
$$

For the new rule,

$$
\begin{aligned}
\operatorname{NB}_{\mathrm{new}}
&=\frac{14}{100}-\frac8{100}\cdot\frac14\\
&=\frac{14}{100}-\frac2{100}\\
&=\frac{12}{100}=\frac3{25}.
\end{aligned}
$$

For existing care,

$$
\begin{aligned}
\operatorname{NB}_{\mathrm{existing}}
&=\frac{12}{100}-\frac4{100}\cdot\frac14\\
&=\frac{12}{100}-\frac1{100}\\
&=\frac{11}{100}.
\end{aligned}
$$

The difference is

$$
\boxed{
\operatorname{NB}_{\mathrm{new}}
-
\operatorname{NB}_{\mathrm{existing}}
=
\frac1{100}.
}
$$

The same result follows directly from the changed decisions. The new rule finds two additional positives, gaining eight utility units, while producing four additional false-positive actions, losing four units. Net gain is four units across 100 patients. Dividing by $$100B=400$$ gives $$1/100$$.

At this threshold, acting on everyone gives

$$
\frac{20}{100}-\frac{80}{100}\cdot\frac14=0,
$$

the same net benefit as acting on no one.

The new rule is imperfect and less accurate, but more useful under the stipulated consequence model. Accuracy weights every correct classification equally; this decision does not.

### 8. Why a valid model can be useless

Suppose a model identifies the target state perfectly, but existing care already takes exactly the same actions, at the same time, with the same outcomes and resource use.

Let $$a_M(X)$$ be the model-supported action and $$a_C(X)$$ the comparator action. If

$$
a_M(X)=a_C(X)
$$

for every relevant patient, the model produces no incremental decision benefit in this setting.

More generally, with

$$
w=\frac{p_t}{1-p_t},
$$

the difference in modeled net benefit is

$$
\boxed{
\Delta\operatorname{NB}
=
\mathbb E[
(a_M-a_C)\{Y-w(1-Y)\}
].
}
$$

If the actions are identical, the difference is zero.

A valid model can also fail to add value because:

- Its information arrives after the decision.
- Its output does not resolve uncertainty relevant to an available action.
- The action has no meaningful benefit for the detected state.
- Workload or implementation costs exceed the gains.
- Clinicians cannot or do not act on the recommendation.

These are failures of the pathway from information to consequence, even if the prediction itself is sound.

Conversely, usefulness does not require perfect prediction. The constructed table shows that errors can be acceptable when the overall decision trade-off is favorable. This does not excuse an inappropriate target or invalid reference.

### 9. Costs and heterogeneous consequences change the calculation

Suppose introducing the model adds cost $$c$$ per patient in the same utility units as $$B$$ and $$H$$. Net benefit becomes

$$
\operatorname{NB}_{\mathrm{with\ cost}}
=
\operatorname{NB}-\frac cB.
$$

In the constructed example, the new rule's incremental net benefit is $$1/100$$. An added normalized cost exceeding $$1/100$$ per patient would erase that advantage.

Consequences may also differ between patients. If benefits and harms depend on patient information,

$$
B=B(X),
\qquad
H=H(X),
$$

then the preferred action satisfies

$$
p(X)B(X)-[1-p(X)]H(X)\geq0,
$$

or

$$
\boxed{
p(X)\geq\frac{H(X)}{B(X)+H(X)}.
}
$$

There is no longer one universal threshold probability unless the consequence ratio is constant.

A decision curve with a shared threshold represents a common preference ratio. It does not automatically account for individual preferences, different treatment effects, contraindications, or capacity-dependent delays.

### 10. What calibration contributes to decision analysis

Net benefit can be calculated for any fixed binary decision rule using observed outcomes and a stipulated consequence ratio. The model does not need to be calibrated for this arithmetic.

Calibration matters when a numerical probability is interpreted as the risk to compare with $$p_t$$.

If

$$
\Pr(Y=1\mid Q=q)=q,
$$

then among patients with forecast $$q$$, expected incremental utility of acting is

$$
qB-(1-q)H.
$$

Thresholding calibrated forecasts at $$p_t$$ is therefore optimal among rules using only that forecast, under the homogeneous consequence assumptions.

This does not imply optimality among all rules using the full clinical information. A calibrated score can discard useful distinctions.

For a miscalibrated score, the expected utility at score value $$q$$ instead depends on

$$
\eta(q)B-[1-\eta(q)]H.
$$

The meaningful risk boundary is

$$
\eta(q)\geq p_t,
$$

which need not be equivalent to $$q\geq p_t$$.

Thus a favorable decision curve can evaluate an actual rule despite miscalibration, but an unvalidated probability interpretation can lead to a poor choice of rule.

### 11. A decision curve varies a preference, not merely a score cutoff

For each threshold probability, a decision curve evaluates the corresponding policy using the associated harm-benefit ratio.

Changing $$p_t$$ changes:

1. The consequences being represented through $$p_t/(1-p_t)$$.
2. Usually, which patients the prediction rule selects.

The clinical preference cannot be chosen after seeing the test set merely because one threshold makes the model look favorable. Plausible thresholds need a defensible relationship to the action.

The evaluation should also examine the actual comparator, available capacity, and added model costs. A curve above “act on all” and “act on none” can still be inferior to current practice.

Uncertainty belongs to the comparison. Small differences in estimated net benefit may be unstable when few independent patients determine the changes in action.

### 12. Modeled net benefit is not demonstrated causal benefit

Decision analysis calculates value under assumptions about what actions accomplish. A utility study asks what happens when the system is actually introduced.

Let $$O^{M}$$ be the outcome that would occur under the model-supported policy and $$O^{C}$$ the outcome under comparator care. For an outcome utility function $$u$$, the target is

$$
\Delta
=
\mathbb E[u(O^{M})]
-
\mathbb E[u(O^{C})].
$$

This is a comparison of policies, including interpretation, adherence, timing, workload, and downstream care.

For illustration, suppose patients are randomly assigned to policy $$A\in\{M,C\}$$. Under consistency, the observed outcome equals the potential outcome for the assigned policy. Under random assignment, assignment is independent of potential outcomes. Therefore,

$$
\begin{aligned}
\mathbb E[u(O)\mid A=M]
&=\mathbb E[u(O^{M})\mid A=M]\\
&=\mathbb E[u(O^{M})],
\end{aligned}
$$

and similarly,

$$
\mathbb E[u(O)\mid A=C]
=
\mathbb E[u(O^{C})].
$$

Subtracting identifies $$\Delta$$, subject to appropriate outcome observation and a well-defined intervention.

If policies compete for shared resources, one patient's assignment may affect another patient's care. The intervention and study unit must then reflect that interaction rather than assuming isolated patient effects.

An observational comparison does not inherit randomization. Differences may reflect which patients or clinicians received the system. Additional assumptions and an appropriate design are needed to attribute outcome differences to its introduction.

### 13. Outcome labels can change when the model changes care

For diagnostic agreement, the reference may aim to measure a state already present. For prognosis, the observed outcome can depend on subsequent treatment.

A model predicting an adverse event from historical care predicts outcomes under that care process. If its introduction changes treatment, it may change the event itself.

Consequently:

- A treated high-risk patient without an event is not automatically an original false-positive risk prediction.
- A model that predicts historical treatment decisions is not automatically estimating untreated disease risk.
- A retrospective event label does not by itself identify who benefits from a new intervention.

The decision analysis must connect the target to the action's effects. Otherwise a well-calibrated forecast of observed outcomes can be used to justify an unsupported treatment-benefit claim.

### 14. Faithfulness, validity, and utility remain separate claims

Clinical evidence reliance asks whether predictions depend on appropriate evidence. Clinical validity asks whether their intended interpretation is supported. Clinical utility asks whether their use improves consequences.

A locally useful shortcut can remain fragile under transfer. A clinically faithful model can add no value beyond an experienced reader. A model with strong reference agreement can still rely on information unavailable at the intended decision time.

These possibilities motivate complementary evaluations rather than a single ladder in which one favorable metric proves every later claim.

Clinical assessability also limits what an evidence-reliance audit can establish. If a finding cannot be judged reliably from the supplied image, disagreement with an image annotation is not automatically evidence of clinically inappropriate model reasoning.

### 15. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| What makes a validity claim specific? | Target, population, timing, unit, reference, and intended interpretation |
| Why is agreement with a label insufficient by itself? | The recorded reference may differ from the clinical state |
| Where does the threshold probability come from? | $$pB-(1-p)H\geq0$$ gives $$p_t=H/(B+H)$$ |
| Why do threshold odds appear in net benefit? | They equal the false-positive harm to true-positive benefit ratio |
| Why are false negatives absent from the displayed formula? | Their lost benefit is represented by true positives not obtained |
| Why compare with current practice? | Added value depends on changes relative to the actual alternative |
| Can lower accuracy yield higher utility? | Yes, when the relevant error consequences are asymmetric |
| Does calculating net benefit require calibration? | No; interpreting a probability threshold as a risk decision does |
| What does a decision curve establish? | Modeled value under specified consequences and data assumptions |
| What establishes effects of actual use? | A suitable comparative evaluation of the complete policy |

In the ontology, the clinical target sets requirements for methods and metrics. Reference-standard adjudication supports clinical validity; decision analysis evaluates modeled consequences. Neither reference agreement nor evidence reliance alone establishes clinical utility.

## Why it matters for my work

For a gallbladder model, I need to name the decision it might improve and compare against how that decision is currently made. Faithfulness auditing can accompany the evaluation by testing the evidence behind predictions. It cannot substitute for measuring appropriate review, unnecessary work, missed findings, and downstream consequences.

## What I have not resolved

- Which gallbladder decision leaves enough uncertainty for the model to add useful information?
- Which comparator reflects current care, including timing and workload?
- Which outcomes would capture benefit without overlooking unnecessary investigations or delayed diagnoses?

---

Sources: Independent study; the reference-error construction, threshold derivation, net-benefit calculations, and policy comparison are developed above. Numerical examples use stipulated counts and utility units, not estimated clinical effects. These are study notes for research purposes, not clinical guidance.
