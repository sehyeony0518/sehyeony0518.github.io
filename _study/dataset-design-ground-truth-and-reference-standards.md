---
layout: study_note
title: "Dataset Design, Ground Truth, and Reference Standards"
description: "What counts as truth in a medical dataset, and how that choice bounds every result that follows."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalisation & Reliability"
subgroup: "Task Definition & Ground Truth"
order: 3
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-01-08-busbra-breast-ultrasound-dataset"
  - "2025-12-19-eyepacs-grading-protocol"
  - "2026-06-25-international-clinical-dr-severity-scale"
---

A medical dataset contains labels produced by a reference process. It also contains patients selected through an enrollment process. Both processes determine what an evaluation estimates.

## Core question and definition

The central question is:

> Does the combination of sampling, verification, and labeling identify the clinical quantity I intend to measure?

A **reference standard** is the procedure used to establish the target condition for evaluation. It can involve pathology, expert interpretation, laboratory measurements, follow-up, or a prespecified combination. A defensible reference must match the intended condition, anatomical unit, and time.

“Gold standard” is used inconsistently. It sometimes means the best available reference and sometimes implies an error-free determination of the target. These meanings should be separated. In a mathematical derivation, an error-free standard means the recorded reference equals the target. Calling a procedure a gold standard does not establish that equality in practice.

The FDA's methodological guidance distinguishes an appropriate reference standard from a comparison method whose correctness is not established; agreement with the latter cannot by itself identify diagnostic accuracy. [FDA guidance on reporting diagnostic-test studies](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/statistical-guidance-reporting-results-studies-evaluating-diagnostic-tests-guidance-industry-and-fda).

Throughout this note, let:

- $$D\in\{0,1\}$$ be the specified clinical target.
- $$T\in\{0,1\}$$ be the index test's result at a fixed operating point.
- $$R\in\{0,1\}$$ be the recorded reference result.
- $$V=1$$ indicate that the reference procedure was completed.
- $$S=1$$ indicate inclusion in the dataset.

The target sensitivities and specificities concern $$D$$. The observed dataset may permit only comparisons with $$R$$ among selected and verified participants.

## Key concepts

### 1. Separate diagnosis, visibility, and reference provenance

A patient diagnosis, a lesion diagnosis, and an image finding are different targets.

| Target | What the label must establish | What another label does not automatically establish |
|---|---|---|
| Patient-level disease | Whether the patient has the specified condition | Which image contains evidence |
| Lesion diagnosis | The identity of the particular imaged lesion | The diagnosis of every other lesion |
| Examination-level finding | Whether the finding is supported by the examination | Whether every frame depicts it |
| Frame-level finding | Whether the feature is assessable and present in that frame | The patient's complete diagnosis |
| Future outcome | Whether an event occurred over a defined period | What would have happened under different care |

For example, pathology may establish a lesion's tissue diagnosis while leaving unresolved whether its attachment or boundary was visible in a saved ultrasound frame.

Copying the diagnosis to every frame creates a patient-status label attached to images. That can be useful for a carefully defined weakly supervised examination task. It does not turn every frame into a positive example of visible lesion morphology.

A useful record therefore separates:

1. The clinical target.
2. The reference method.
3. The anatomical and temporal match.
4. The observable findings.
5. Whether those findings are assessable.
6. Remaining uncertainty.

### 2. Define the accuracy quantities before examining missing references

Write true sensitivity and specificity as

$$
s=\Pr(T=1\mid D=1),
$$

$$
c=\Pr(T=0\mid D=0).
$$

Let prevalence be

$$
\pi=\Pr(D=1).
$$

The population confusion-matrix fractions are

$$
\begin{aligned}
\Pr(T=1,D=1)&=\pi s,\\
\Pr(T=0,D=1)&=\pi(1-s),\\
\Pr(T=1,D=0)&=(1-\pi)(1-c),\\
\Pr(T=0,D=0)&=(1-\pi)c.
\end{aligned}
$$

These expressions describe the intended population. Replacing it with selected or verified patients changes the conditioning.

For example,

$$
\Pr(T=1\mid D=1,V=1)
$$

need not equal

$$
\Pr(T=1\mid D=1).
$$

Verification bias arises when that difference matters for the reported claim.

### 3. Partial verification is a design; verification bias is a consequence

**Partial verification** means only some participants receive the reference procedure.

It does not inevitably cause bias. A random reference subsample can still support valid inference with appropriate analysis. Bias arises when verification changes the composition relevant to the accuracy estimate and the analysis ignores that selection.

To isolate this mechanism, assume the reference is correct whenever performed:

$$
R=D\quad\text{when }V=1.
$$

Define

$$
v_{td}=\Pr(V=1\mid T=t,D=d).
$$

Among disease-positive patients,

$$
\Pr(T=1,V=1\mid D=1)=s\,v_{11},
$$

and

$$
\Pr(T=0,V=1\mid D=1)=(1-s)v_{01}.
$$

Therefore, sensitivity in verified patients is

$$
\boxed{
s_V=
\frac{s\,v_{11}}
{s\,v_{11}+(1-s)v_{01}}.
}
$$

Similarly, among disease-negative patients,

$$
\boxed{
c_V=
\frac{c\,v_{00}}
{c\,v_{00}+(1-c)v_{10}}.
}
$$

The verified estimates recover the intended quantities when verification does not distinguish test results within each disease class:

$$
v_{11}=v_{01},
\qquad
v_{00}=v_{10}.
$$

Equal verification probability for everyone is sufficient, but stronger than necessary.

### 4. Derive the usual direction of verification bias

Suppose verification depends only on the index-test result:

$$
\Pr(V=1\mid T=1,D)=v_1,
$$

$$
\Pr(V=1\mid T=0,D)=v_0,
$$

with $$v_1>v_0>0$$.

Then the odds of a positive test among verified disease-positive patients are

$$
\begin{aligned}
\frac{s_V}{1-s_V}
&=
\frac{s\,v_1}{(1-s)v_0}\\
&=
\frac{s}{1-s}\frac{v_1}{v_0}.
\end{aligned}
$$

Since $$v_1/v_0>1$$, verified sensitivity exceeds true sensitivity.

For specificity,

$$
\begin{aligned}
\frac{c_V}{1-c_V}
&=
\frac{c\,v_0}{(1-c)v_1}\\
&=
\frac{c}{1-c}\frac{v_0}{v_1}.
\end{aligned}
$$

Verified specificity is lower.

The mechanism is selective retention:

- Test-positive diseased patients are retained more often than false negatives.
- Test-positive nondiseased patients are retained more often than true negatives.

These directions follow from the stated verification rule. They are not universal laws for every missing-reference process. Selection by severity, symptoms, or other information can produce different distortions.

### 5. A constructed partial-verification example

Construct 200 patients with the following true results:

| Index result | Disease present | Disease absent | Total |
|---|---:|---:|---:|
| Positive | 80 | 20 | 100 |
| Negative | 20 | 80 | 100 |
| Total | 100 | 100 | 200 |

True sensitivity and specificity are both

$$
\frac{80}{100}=\frac45.
$$

Verify every index-positive patient and half the index-negative patients. Construct the verified subset as follows:

| Index result | Verified disease present | Verified disease absent |
|---|---:|---:|
| Positive | 80 | 20 |
| Negative | 10 | 40 |

An analysis restricted to these verified patients reports

$$
\widehat s_V
=
\frac{80}{80+10}
=
\frac89,
$$

and

$$
\widehat c_V
=
\frac{40}{40+20}
=
\frac23.
$$

The model has not changed. The reference procedure is perfect. Selection alone changes the reported accuracy.

Now consider a different analysis: retain all 200 patients but code every unverified patient as disease-negative.

The 50 unverified patients include ten truly diseased patients and 40 truly nondiseased patients. All had negative index tests, so all 50 are added to the apparent true-negative cell.

The resulting reference-based table is

| Index result | Recorded positive reference | Recorded negative reference |
|---|---:|---:|
| Positive | 80 | 20 |
| Negative | 10 | 90 |

It reports

$$
\widehat s_R=\frac89,
$$

and

$$
\widehat c_R=\frac{90}{110}=\frac9{11}.
$$

Excluding unverified patients and assigning them negative labels create different estimands and different distortions. “Handling missing labels” is not a neutral cleaning step.

### 6. When inverse-verification weighting can recover the target

Suppose verification probability is known or estimable from observed variables:

$$
e(T,X)=\Pr(V=1\mid T,X).
$$

Assume:

1. Verification is conditionally independent of disease after accounting for those variables:

$$
V\perp D\mid T,X.
$$

2. Every relevant stratum has positive verification probability:

$$
e(T,X)>0.
$$

3. The performed reference adequately establishes $$D$$.

For any function $$h(T,D,X)$$,

$$
\begin{aligned}
\mathbb E\left[\frac{Vh(T,D,X)}{e(T,X)}\right]
&=
\mathbb E\left[
h(T,D,X)
\frac{\mathbb E[V\mid T,D,X]}{e(T,X)}
\right]\\
&=
\mathbb E[h(T,D,X)].
\end{aligned}
$$

The second equality uses the conditional-independence assumption.

Choose $$h$$ to indicate each confusion-matrix cell. Weighted verified observations can then estimate the population cell probabilities.

For example,

$$
\widehat s_{\mathrm{weighted}}
=
\frac{
\sum_i V_iT_iD_i/e_i
}{
\sum_i V_iD_i/e_i
}.
$$

This ratio is generally consistent under the assumptions; it is not automatically exactly unbiased in a finite sample.

In the constructed example, verified positive tests receive weight one and verified negative tests receive weight two:

$$
\widehat s_{\mathrm{weighted}}
=
\frac{80}{80+2(10)}
=
\frac45,
$$

$$
\widehat c_{\mathrm{weighted}}
=
\frac{2(40)}{2(40)+20}
=
\frac45.
$$

Weighting succeeds because the construction supplies the required probabilities and verification mechanism.

If verification depends on unrecorded clinical suspicion related to disease, the conditional-independence assumption may fail. If no test-negative patients are ever verified, their disease composition cannot be recovered by giving observed patients larger weights.

### 7. Differential verification changes the label-generating process

**Differential verification** means participants receive different reference procedures.

It is distinct from partial verification: everybody may receive a reference, but its errors can differ across groups.

Return to the 200-patient construction. Suppose:

- Every index-positive patient receives a perfect reference.
- Every index-negative patient receives a second reference that detects half the truly diseased patients and correctly labels every nondiseased patient.

Among index-negative patients, the second procedure labels ten of the 20 diseased patients positive. The other ten receive negative labels alongside the 80 nondiseased patients.

The observed table is again

| Index result | Reference positive | Reference negative |
|---|---:|---:|
| Positive | 80 | 20 |
| Negative | 10 | 90 |

Thus,

$$
\widehat s_R=\frac89,
\qquad
\widehat c_R=\frac9{11}.
$$

Here nobody lacks a reference. The distortion comes from using a less sensitive reference specifically among index-negative patients.

The same observed table can therefore arise from different mechanisms. Participant flow and reference provenance are needed to distinguish them.

### 8. Even a common imperfect reference can distort accuracy

Suppose everybody receives the same imperfect reference. Let its sensitivity and specificity be

$$
u=\Pr(R=1\mid D=1),
\qquad
v=\Pr(R=0\mid D=0).
$$

For this derivation, assume the index test and reference are conditionally independent given disease:

$$
T\perp R\mid D.
$$

The apparent true-positive fraction is

$$
\begin{aligned}
\Pr(T=1,R=1)
&=\Pr(D=1)\Pr(T=1,R=1\mid D=1)\\
&\quad+\Pr(D=0)\Pr(T=1,R=1\mid D=0)\\
&=\pi su+(1-\pi)(1-c)(1-v).
\end{aligned}
$$

The reference-positive fraction is

$$
\Pr(R=1)=\pi u+(1-\pi)(1-v).
$$

Therefore,

$$
\boxed{
\Pr(T=1\mid R=1)
=
\frac{\pi su+(1-\pi)(1-c)(1-v)}
{\pi u+(1-\pi)(1-v)}.
}
$$

Similarly,

$$
\boxed{
\Pr(T=0\mid R=0)
=
\frac{\pi(1-s)(1-u)+(1-\pi)cv}
{\pi(1-u)+(1-\pi)v}.
}
$$

These are not generally $$s$$ and $$c$$. They can also depend on prevalence even when the true sensitivity and specificity remain fixed.

Conditional independence is an explanatory assumption, not a default property of medical tests. Shared visual evidence or shared acquisition artifacts can correlate their errors and invalidate these particular formulas.

### 9. Derive what composite reference rules do

A composite reference combines several sources through an explicit rule. The rule is part of the reference definition.

Suppose two component tests have sensitivities $$s_1,s_2$$ and specificities $$c_1,c_2$$, and are conditionally independent given disease.

For an **OR rule**, the composite is positive if either component is positive.

Among diseased patients, the composite misses disease only when both components miss it:

$$
s_{\mathrm{OR}}
=
1-(1-s_1)(1-s_2).
$$

Among nondiseased patients, it is negative only when both components are negative:

$$
c_{\mathrm{OR}}=c_1c_2.
$$

For an **AND rule**, the composite is positive only when both components are positive:

$$
s_{\mathrm{AND}}=s_1s_2,
$$

$$
c_{\mathrm{AND}}
=
1-(1-c_1)(1-c_2).
$$

Construct components with sensitivity and specificity both equal to $$4/5$$.

| Reference rule | Sensitivity | Specificity |
|---|---|---|
| Either component alone | $$4/5$$ | $$4/5$$ |
| OR | $$1-(1/5)^2=24/25$$ | $$(4/5)^2=16/25$$ |
| AND | $$(4/5)^2=16/25$$ | $$1-(1/5)^2=24/25$$ |

Combining evidence does not automatically improve every property. OR and AND rules move the balance in different directions.

With three conditionally independent components, each correct with probability $$p$$ within each disease class, majority voting is correct when exactly two or all three are correct:

$$
\Pr(\text{majority correct})
=
3p^2(1-p)+p^3.
$$

At the constructed value $$p=4/5$$,

$$
3\left(\frac45\right)^2\frac15
+
\left(\frac45\right)^3
=
\frac{112}{125}.
$$

This exceeds $$4/5$$. But if all three components make exactly the same errors, majority voting remains correct only with probability $$4/5$$.

The gain depends on complementary information and error dependence, not merely the number of components.

### 10. Incorporating the index test can manufacture agreement

Suppose the composite reference is defined as

$$
R=T\lor R_2.
$$

Whenever the index test is positive, the reference must also be positive. Therefore,

$$
\Pr(T=1,R=0)=0.
$$

If reference-negative cases exist, apparent specificity is one:

$$
\Pr(T=0\mid R=0)=1.
$$

This follows from the construction even if the index test produces true false positives against disease.

The reference has incorporated the result being evaluated. Its favorable agreement is partly built into the label rule.

Independent initial assessments, a prespecified combination rule, and preservation of component results make this problem more inspectable. Reviewing only disagreements can also privilege the index test unless the resolution procedure and sampling are appropriately designed.

### 11. Sampling determines which population quantities are identifiable

Let

$$
a_d=\Pr(S=1\mid D=d).
$$

If sampling depends on disease class but is otherwise representative within each class,

$$
S\perp T\mid D,
$$

then

$$
\Pr(T=1\mid D=1,S=1)=s,
$$

and

$$
\Pr(T=0\mid D=0,S=1)=c.
$$

However, sampled prevalence becomes

$$
\boxed{
\pi_S
=
\frac{a_1\pi}
{a_1\pi+a_0(1-\pi)}.
}
$$

Without knowledge of the sampling fractions or target prevalence, the dataset does not identify the target population's disease frequency.

Positive predictive value is

$$
\operatorname{PPV}
=
\frac{\pi s}{\pi s+(1-\pi)(1-c)}.
$$

Thus estimating sensitivity and specificity does not suffice to identify target predictive values without prevalence information.

Construct an enriched dataset with 100 diseased and 100 nondiseased patients, sensitivity $$4/5$$, and specificity $$4/5$$. It contains 80 true positives and 20 false positives:

$$
\operatorname{PPV}_{\mathrm{enriched}}=\frac{80}{100}=\frac45.
$$

Now construct a target cohort of 1,000 patients with 100 diseased and 900 nondiseased patients, keeping the same conditional performance. It contains 80 true positives and 180 false positives:

$$
\operatorname{PPV}_{\mathrm{target}}
=
\frac{80}{260}
=
\frac4{13}.
$$

The enriched dataset's raw predictive value does not describe the target service.

### 12. Compare the main sampling designs

| Design | What it can estimate under appropriate reference and follow-up | Main limitation |
|---|---|---|
| Consecutive eligible patients | Local prevalence, predictive values, workload, and class-conditional accuracy | Represents that eligibility rule, service, and period |
| Representative case-control sampling within disease classes | Sensitivity, specificity, and class-conditional score distributions | Artificial class proportions do not identify target prevalence |
| Enrichment with known selection probabilities | Population quantities through justified weighting | Requires overlap and an adequate selection model |
| Purposive selection of obvious cases and healthy controls | Performance on that selected contrast | May omit subtle disease and realistic alternative diagnoses |
| Surgical or otherwise strongly verified cohort | Performance among patients reaching that verification pathway | Stronger labels can coexist with poor population representativeness |

“Enriched” describes a changed composition, not one unique design. Its inferential consequences depend on how the extra cases were selected.

Case-control sampling also does not automatically preserve sensitivity and specificity. Selecting advanced disease cases and unusually healthy controls changes the within-class spectrum, violating the representative-within-class assumption.

### 13. Timing, indeterminate results, and missingness belong in the dataset

A reference should be matched to the relevant lesion and disease state. Intervening treatment, progression, or a different sampled location can change the meaning of the comparison.

Indeterminate results should remain visible. Removing them estimates performance among determinate cases:

$$
\Pr(\text{correct}\mid\text{determinate}),
$$

which differs from performance in all eligible patients when difficulty and determinacy are related.

A useful participant-flow record preserves:

- Eligibility and enrollment.
- Reasons for exclusion.
- Index-test availability and indeterminate outputs.
- Reference method and completion.
- Reference timing and anatomical match.
- Component reference results.
- Unresolved disagreement and missing follow-up.

Restricting analysis to the strongest reference can improve label confidence while increasing selection bias. Neither “use every case” nor “keep only perfect labels” is universally sufficient.

### 14. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| Reference standard versus gold standard? | A reference is an operational procedure; error-free truth is an additional assumption |
| Why separate diagnosis and visibility? | A patient diagnosis does not establish evidence in every frame |
| Does partial verification always bias accuracy? | No; bias depends on selection and analysis |
| How does index-dependent verification distort estimates? | It reweights positive and negative index results within disease classes |
| Why is coding unverified cases negative different from exclusion? | It changes labels as well as the analyzed population |
| When can verification weighting work? | Positive verification probabilities and an adequate conditional missingness assumption |
| What is differential verification? | Reference methods, and potentially their errors, differ across participants |
| Can a composite improve its components? | Yes, with useful complementary information; dependence and combination rules matter |
| Why is incorporation dangerous? | Agreement can follow mechanically from including the index result in its own reference |
| What does case-control sampling identify? | Conditional performance under representative class sampling, not target prevalence by itself |

In the ontology, reference-standard adjudication supports clinical validity, while selection and verification bias limit the claims an evaluation can establish. Clinical assessability remains a separate constraint on interpreting image-level evidence.

## Why it matters for my work

For gallbladder ultrasound, I need linked records for diagnosis, visible findings, and reference provenance. That separation prevents pathology confidence from being mistaken for frame-level assessability, and makes it possible to distinguish model error from selection or reference mismatch.

## What I have not resolved

- How should pathology and longitudinal follow-up be combined without concealing different verification mechanisms?
- Which unverified patients most limit the intended population claim?
- Which findings can be annotated reliably at frame, lesion, and examination levels?

---

Sources: Independent study, with reference-standard terminology checked against the FDA methodological guidance linked above. All numerical examples are constructed, and their calculations are shown. These are study notes for research purposes, not clinical guidance.
