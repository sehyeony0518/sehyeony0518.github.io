---
layout: study_note
title: "Error and Clinical Failure Analysis"
description: "Reading the cases a model gets wrong as evidence about what it learned."
og_image: "https://sehyeony0518.github.io/assets/img/og/error-and-clinical-failure-analysis.png"
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
subgroup: "Failure Analysis & Clinical Translation"
order: 13
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-11-10-oakden-rayner-hidden-stratification"
  - "2025-10-28-degrave-covid-shortcut"
  - "2026-04-28-reveal-to-revise-spurious-behavior"
---

An error case is a disagreement with a specified reference. Clinical failure analysis asks where the failure arose, what consequences it could produce, and what evidence would justify a particular repair.

## Core question and definition

The central question is:

> Can I turn a reproducible failure pattern into a testable mechanism and an actionable change?

A gallery of mistakes can suggest hypotheses. It cannot determine whether a visible feature is unusually associated with error, whether the reference is correct, or whether changing that feature would improve performance.

Clinical failure is also broader than classification error. A correct prediction can be assigned to the wrong examination, delivered too late, or acted on inappropriately.

I distinguish:

- **Reference disagreement:** the model output differs from the recorded label.
- **Confirmed prediction error:** further assessment supports that the prediction is wrong for the intended target.
- **Workflow failure:** the system does not accomplish its defined role.
- **Clinical harm:** an adverse consequence occurs or becomes more likely.

These are related events, not interchangeable labels.

## Key concepts

### 1. Define the error before explaining it

For a binary classifier at a fixed threshold, let

$$
E=\mathbf1\{\widehat Y\neq R\},
$$

where $$R$$ is the evaluation reference.

The observed error rate is

$$
\widehat R_{\mathrm{error}}
=
\frac1n\sum_{i=1}^n E_i.
$$

This quantity changes if the reference, threshold, aggregation, or evaluation unit changes.

A frame-level disagreement is not automatically an examination-level failure. A disagreement with a preliminary report is not automatically disagreement with the patient's clinical state.

Before reviewing a case, record:

- The intended target.
- The prediction moment.
- The actual supplied inputs.
- The aggregation and decision rule.
- The reference and its provenance.
- The clinical action the output was intended to support.

Otherwise the explanation can drift toward a different task after the result is known.

### 2. Trace the pathway through which success must occur

Consider a simplified workflow with three stages and no recovery branch:

- $$A$$: adequate evidence reaches the system.
- $$B$$: the model-supported decision is correct.
- $$C$$: the decision reaches the intended action appropriately.

Workflow success requires

$$
A\cap B\cap C.
$$

By the chain rule,

$$
\boxed{
\Pr(\text{success})
=
\Pr(A)\Pr(B\mid A)\Pr(C\mid A,B).
}
$$

No independence assumption is used.

Construct 100 examinations:

- 80 supply adequate evidence.
- Of those 80, 70 receive the correct decision.
- Of those 70, 63 reach the intended action.

Then

$$
\begin{aligned}
\Pr(\text{success})
&=\frac{80}{100}\frac{70}{80}\frac{63}{70}\\
&=\frac{63}{100}.
\end{aligned}
$$

The model's conditional decision accuracy is

$$
\frac{70}{80}=\frac78.
$$

That does not describe the whole pathway.

The remaining examinations can be partitioned by first failed stage:

| First failed stage | Count |
|---|---:|
| Adequate evidence not supplied | 20 |
| Incorrect decision despite adequate evidence | 10 |
| Correct decision not translated into intended action | 7 |
| Total unsuccessful pathways | 37 |

This is an accounting construction, not a claim that inadequate initial images inevitably cause clinical failure. A real workflow may recover through repeat acquisition, abstention, or another assessment route. Those branches must be represented explicitly.

### 3. Use a taxonomy that points toward a test and an owner

A useful category identifies where evidence is needed and what change could address the problem.

| Category | Observable question | Candidate response to test |
|---|---|---|
| Reference mismatch | Does the label correspond to the imaged target and time? | Repair matching or perform independent adjudication |
| Evidence unavailable | Was the relevant anatomy or finding supplied? | Change acquisition, input completeness checks, or abstention |
| Evidence present but missed | Is the finding assessable yet not detected? | Investigate representation, training coverage, or localization |
| Clinical mimic | Does another process produce similar appearance? | Add discriminating context or refine the target |
| Acquisition dependence | Is failure associated with device, overlay, or protocol? | Test dependence and acquisition-specific preprocessing |
| Aggregation failure | Do correct frame outputs produce an incorrect examination result? | Revise and validate aggregation |
| Threshold or probability failure | Does the score support an inappropriate action? | Evaluate calibration and decision thresholds |
| Presentation or routing failure | Does the output reach the right user and examination? | Change the interface or routing process |
| Response failure | Is the recommendation misunderstood, delayed, or infeasible? | Evaluate the actual workflow and resources |

These are candidate mechanisms. Assigning a category is not equivalent to proving a cause.

A case can have multiple contributing factors. Use multiple descriptive tags where appropriate, while defining a mutually exclusive primary category if counts must sum to the total. The primary category is an accounting convention unless causal evidence supports it.

### 4. Derive the difference between an error rate and an error pattern

For mutually exclusive groups $$G$$,

$$
\Pr(E=1)
=
\sum_g\Pr(G=g)\Pr(E=1\mid G=g).
$$

The overall rate averages over the case mixture.

An error gallery instead samples from

$$
\Pr(G=g\mid E=1).
$$

By Bayes' rule,

$$
\boxed{
\Pr(G=g\mid E=1)
=
\frac{
\Pr(E=1\mid G=g)\Pr(G=g)
}{
\Pr(E=1)
}.
}
$$

A category can dominate errors because it is common, because its conditional error rate is high, or both.

The fraction of errors containing a feature is therefore insufficient to establish that the feature predicts failure.

### 5. A marker example with the denominators retained

Construct 100 cases:

| Marker status | Cases | Errors | Error rate |
|---|---:|---:|---|
| Present | 80 | 8 | $$1/10$$ |
| Absent | 20 | 2 | $$1/10$$ |
| Total | 100 | 10 | $$1/10$$ |

Among errors,

$$
\Pr(\text{marker present}\mid E=1)
=
\frac8{10}
=
\frac45.
$$

Most mistakes contain the marker. But most cases contain it:

$$
\Pr(\text{marker present})=\frac45.
$$

Conditional error rates are identical. The gallery provides no evidence of an error-rate association with marker presence.

Now construct a different cohort:

| Marker status | Cases | Errors | Error rate |
|---|---:|---:|---|
| Present | 20 | 10 | $$1/2$$ |
| Absent | 80 | 10 | $$1/8$$ |

The marker is present in half the errors but only one fifth of cases. The conditional error-rate ratio is

$$
\frac{1/2}{1/8}=4.
$$

This establishes an association in the constructed data. It still does not prove marker reliance.

Markers may be used more often on difficult findings, selected lesions, or particular devices. Those factors can produce the association without the marker causing the prediction error.

### 6. Hidden stratification can preserve the headline metric

A broad benchmark label can contain clinically distinct subtypes whose performance differs.

Construct 100 reference-positive cases:

- 90 have a common presentation.
- Ten have a rare presentation.

Compare two models:

| Presentation | Cases | Model A misses | Model B misses |
|---|---:|---:|---:|
| Common | 90 | 0 | 9 |
| Rare | 10 | 10 | 1 |
| Total | 100 | 10 | 10 |

Both models have overall sensitivity

$$
1-\frac{10}{100}=\frac9{10}.
$$

Their subgroup sensitivities differ:

$$
s_{A,\mathrm{common}}=1,
\qquad
s_{A,\mathrm{rare}}=0,
$$

$$
s_{B,\mathrm{common}}=\frac9{10},
\qquad
s_{B,\mathrm{rare}}=\frac9{10}.
$$

The aggregate hides complete failure on the rare presentation by A.

This construction concerns sensitivity among positive cases. It does not compare specificity or overall clinical utility, which require additional information.

If the dataset records only the broad positive label, the subgroup failure cannot be estimated until the subtype is identified. Clinical knowledge is therefore useful for proposing meaningful strata, but post hoc discoveries require independent confirmation.

### 7. Separate a discovered pattern from a confirmed mechanism

A useful progression is:

| Evidence level | What has been established |
|---|---|
| Case observation | A feature occurs in one or more reviewed cases |
| Cohort association | Error rates differ with the feature after denominators are retained |
| Replicated association | The pattern occurs in independent cases or settings |
| Intervention-supported dependence | A controlled change affects the prediction under defensible assumptions |
| Workflow mechanism | The change has a demonstrated effect on the operational failure |

Moving between levels requires new evidence.

For example, “errors often contain a caliper” is a case observation. Comparing all marker-positive and marker-negative cases establishes an association. A controlled edit may test model dependence. A prospective change in acquisition or software may test whether removing that dependence actually improves the workflow.

An explanation image alone does not complete this sequence.

### 8. Design controlled edits to test a specific hypothesis

Let $$T$$ be an edit intended to remove a suspected nuisance cue. A paired score change is

$$
\Delta_i=s(X_i)-s(T(X_i)).
$$

Its mean estimates the response to that particular editing procedure:

$$
\overline\Delta=\frac1n\sum_i\Delta_i.
$$

Interpreting the change as reliance on the intended cue requires that the edit does not also alter relevant evidence, introduce a new artifact, or shift the image in another consequential way.

Useful controls include:

- Edits of similarly sized irrelevant regions.
- Alternative removal methods.
- Checks that lesion visibility and image quality remain adequate.
- Correctly predicted cases as well as errors.
- Independent clinical assessment of the edited image.
- Patient-level uncertainty for paired changes.

A masked region may remove clinical information along with an overlay. A model response then establishes sensitivity to the edit, not uniquely sensitivity to the overlay.

Correct predictions are important controls because a shortcut can produce a correct answer while its usual association holds.

### 9. Review errors and controls under a reproducible protocol

A review form should distinguish observation from interpretation.

| Field | Example of what to record |
|---|---|
| Reference status | Established, disputed, mismatched, or unresolved |
| Assessability | Whether the relevant feature can be judged from the supplied input |
| Clinical findings | Independently assessed features and alternatives |
| Acquisition | Device, protocol, quality, view selection, overlays |
| Prediction | Score, decision, aggregation, and confidence |
| Error direction | False positive, false negative, localization failure, or another defined mismatch |
| Workflow consequence | Additional review, delay, missed opportunity, inappropriate action |
| Mechanism hypothesis | A proposed explanation with supporting and contradictory evidence |
| Evidence strength | Observation, association, replication, or intervention support |
| Proposed response | A change that can be tested and its success criterion |

Initial clinical assessment should be performed without seeing the model explanation where feasible. Otherwise the explanation can shape the finding annotation later used to validate it.

Independent reviewers should record disagreements before adjudication. A category that cannot be assigned consistently may need a clearer definition or an uncertainty category.

### 10. Sampling for review changes what can be estimated

Reviewing every severe error is sensible for investigation. It does not produce a representative sample for estimating ordinary failure rates.

Likewise, a balanced review sample containing equal numbers of errors and correct cases does not preserve the dataset's error prevalence.

Suppose a fixed cohort contains $$N$$ cases. Case $$i$$ is reviewed with known probability $$q_i>0$$, and let $$V_i$$ indicate review. Let $$h_i$$ be a quantity that complete review would establish, such as a severity-weighted failure value.

Then

$$
\widehat H
=
\frac1N\sum_i\frac{V_ih_i}{q_i}.
$$

Conditional on the fixed cohort,

$$
\begin{aligned}
\mathbb E_V[\widehat H]
&=
\frac1N\sum_i
\frac{\mathbb E[V_i]h_i}{q_i}\\
&=
\frac1N\sum_i
\frac{q_ih_i}{q_i}\\
&=
\boxed{\frac1N\sum_i h_i}.
\end{aligned}
$$

Known review probabilities permit correction for deliberate oversampling.

If some relevant cases have zero probability of review, their review-derived failure properties are not identified by this calculation. A convenience collection of memorable mistakes lacks the probabilities needed for population-rate estimation.

Case discovery and rate estimation can use different samples, provided their purposes remain explicit.

### 11. Count error direction and severity separately

False positives and false negatives describe disagreement, not its consequence.

Let $$C$$ contain clinical context, and let:

- $$h_{\mathrm{FN}}(C)$$ be the stipulated harm associated with a false-negative action.
- $$h_{\mathrm{FP}}(C)$$ be the stipulated harm associated with a false-positive action.

A weighted classification loss is

$$
\boxed{
L
=
h_{\mathrm{FN}}(C)\mathbf1\{D=1,a=0\}
+
h_{\mathrm{FP}}(C)\mathbf1\{D=0,a=1\}.
}
$$

Expected loss is

$$
\begin{aligned}
\mathbb E[L]
&=
\Pr(\mathrm{FN})
\mathbb E[h_{\mathrm{FN}}(C)\mid\mathrm{FN}]\\
&\quad+
\Pr(\mathrm{FP})
\mathbb E[h_{\mathrm{FP}}(C)\mid\mathrm{FP}].
\end{aligned}
$$

This follows by conditioning on the two error events.

The same error direction can have different consequences depending on whether another clinician already recognized the problem, what action follows, and how much delay matters.

The formula covers the stipulated classification consequences. Additional workflow failures require additional loss terms.

### 12. Carry a severity-weighted comparison through

Construct two systems evaluated on 100 decisions. Both make ten errors:

| System | Minor errors | Severe errors | Total errors |
|---|---:|---:|---:|
| A | 8 | 2 | 10 |
| B | 9 | 1 | 10 |

Assign abstract loss one to a minor error and ten to a severe error. These are illustrative weights, not estimated patient harms.

For A,

$$
\widehat R_A
=
\frac{8(1)+2(10)}{100}
=
\frac{28}{100}
=
\frac7{25}.
$$

For B,

$$
\widehat R_B
=
\frac{9(1)+1(10)}{100}
=
\frac{19}{100}.
$$

The error rates are identical, but the weighted consequences differ.

Keep the weights symbolic. If minor and severe losses are $$L$$ and $$H$$,

$$
100(\widehat R_A-\widehat R_B)
=
(8L+2H)-(9L+H)
=
H-L.
$$

B has lower weighted loss whenever

$$
H>L.
$$

This sensitivity analysis shows that the ordering does not depend on the particular illustrative choice of ten versus one.

A different comparison can depend strongly on the weights. If system C makes 20 minor errors and no severe errors,

$$
100(\widehat R_A-\widehat R_C)
=
8L+2H-20L
=
2H-12L.
$$

A is worse than C when

$$
H>6L.
$$

The preferred system then depends on how severe failures are valued. That dependence should be reported rather than hidden inside one arbitrary score.

### 13. Distinguish potential severity from observed harm

A missed finding may plausibly delay care, but an error label alone does not establish that delay occurred. Other information or clinicians may correct the pathway.

Conversely, a correct prediction can still cause harm if its presentation leads to an inappropriate action.

A failure report should distinguish:

1. The observed prediction or workflow event.
2. The plausible consequence under the intended pathway.
3. A modeled expected loss.
4. An observed patient outcome.
5. A causal claim that the system changed that outcome.

These require progressively different evidence.

Severity categories can guide investigation before effects are known. They should not be presented as measured causal harms without the necessary follow-up and comparison.

### 14. Make categories actionable without claiming more than the evidence supports

An actionable category should identify:

- A reproducible inclusion rule.
- Its denominator and estimated frequency.
- The clinical or operational consequence.
- A plausible mechanism.
- A change capable of addressing that mechanism.
- A metric that would show whether the change worked.
- Cases reserved for evaluating the change.

For example:

> Examinations with an inadequately visualized lesion interface have elevated disagreement on attachment morphology. The proposed response is an assessability check that requests additional views. Evaluation must measure recovered assessability, retained diagnostic performance, and acquisition workload.

This is more useful than “the model struggles with difficult images.” It names what is missing, what action could supply it, and what evidence would test the response.

If the root cause remains uncertain, the action can be an investigation rather than a model modification.

### 15. Avoid turning failure analysis into another source of overfitting

After errors are used to choose new features, interventions, thresholds, or training cases, those errors have entered development.

Performance on the same cases can describe whether the intended repair affected them. It cannot independently establish that the repair generalizes.

A disciplined sequence is:

1. Discover candidate patterns.
2. Define the category and mechanism hypothesis.
3. Check annotations and denominators.
4. Test the hypothesis with appropriate controls.
5. Develop the response.
6. Evaluate on reserved or newly collected cases.
7. Check for new failures introduced elsewhere.

Improving a selected error category can worsen another one. The final evaluation should retain the complete operating-point and subgroup view, including correctly predicted cases that may now fail.

### 16. Prioritize frequency, severity, and preventability together

A frequent minor failure and a rare severe failure create different priorities. Frequency alone is insufficient, but severity alone can also produce an unrepresentative anecdote list.

For category $$g$$, a simple expected-loss contribution is

$$
\Pr(G=g)\mathbb E[L\mid G=g].
$$

If a proposed intervention changes conditional loss from $$R_g$$ to $$R_g^{\mathrm{new}}$$ without changing the case mixture, its contribution to expected improvement is

$$
\Pr(G=g)(R_g-R_g^{\mathrm{new}}).
$$

The unknown improvement must be estimated or bounded. It should not be assumed from a plausible causal story.

Implementation cost, review workload, and unintended consequences also enter the decision. A repair that reduces model error while creating an infeasible review queue may not improve the overall system.

### 17. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| What is an error case? | A disagreement relative to a specified reference and decision rule |
| Why is clinical failure broader? | Input, aggregation, presentation, timing, and response can fail despite correct classification |
| What does a gallery of errors omit? | Comparison cases and denominators |
| Why can a common feature dominate errors without increasing risk? | Error composition depends on both feature prevalence and conditional error rate |
| What is hidden stratification? | Different failure rates inside a broad benchmark label |
| Does an association prove model reliance? | No; mechanism tests need controls and defensible interventions |
| Why review correct predictions? | Shortcuts and fragile evidence use can produce correct answers |
| How should severe failures be counted? | Through explicit consequences or weights alongside raw counts |
| What does oversampling require for rate estimation? | Known review probabilities and appropriate weighting |
| What makes a category actionable? | A reproducible definition, a testable mechanism, a proposed response, and an evaluation criterion |
| When does the audit set become development data? | When its findings are used to adapt the model or audit procedure |

In the ontology, failure analysis connects observed findings and threats to reassessment of methods and properties. Clinical targets determine which consequences matter. Clinical assessability limits whether a disagreement can support a claim about evidence reliance.

## Why it matters for my work

For gallbladder faithfulness audits, failure analysis should identify concrete questions about visibility, acquisition, and clinical findings. I want the resulting categories to support controlled tests and practical responses while preserving uncertainty about the reference and mechanism.

## What I have not resolved

- Which failures are preventable through acquisition or workflow changes?
- Which correct predictions depend on evidence that may fail after transfer?
- How can rare consequential failures be investigated without losing representative estimates of routine performance?

---

Sources: Independent study; the pathway factorization, error-pattern calculations, hidden-subgroup example, review weighting, and severity comparisons are developed above. Numerical examples and harm weights are constructed for reasoning, not empirical clinical claims. These are study notes for research purposes, not clinical guidance.
