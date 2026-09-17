---
layout: study_note
title: "Robustness, Subgroup Performance, and External Validation"
description: "Robustness to acquisition variability, subgroup analysis, and multi-center validation as tests of generalizability."
og_image: "https://sehyeony0518.github.io/assets/img/og/robustness-subgroup-performance-and-external-validation.png"
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
subgroup: "Calibration & Generalization"
order: 12
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-12-13-seyyed-kalantari-underdiagnosis"
  - "2025-10-02-zech-variable-generalization"
  - "2026-08-23-robustness-stress-testing-medical-image-classification"
---

Robustness is useful behavior under specified changes. Subgroup evaluation asks for whom that behavior holds. External validation asks whether it carries to a specified setting separated from development.

## Core question and definition

The central question is:

> Which patients, acquisition conditions, and reference processes are covered by the evidence for this model?

“Generalizes” is incomplete without a destination and an endpoint. It might mean:

- Similar ranking in another patient mixture.
- Adequate sensitivity at the same threshold.
- Calibrated probabilities after transfer.
- Stable examination-level decisions across devices.
- Useful performance against a different reference definition.
- Continued reliance on the intended clinical evidence.

These are different claims. A favorable answer to one does not establish the others.

Let $$f$$ be a frozen pipeline, including preprocessing, aggregation, calibration, and the operating rule. Let

$$
L=\ell(f(X),Y)
$$

be the loss being evaluated.

## Key concepts

### 1. Define subgroup performance as a conditional estimand

For a subgroup variable $$G$$, define

$$
R_g=\mathbb E[L\mid G=g].
$$

The group definition must be operational: how membership is measured, at what time, and with what uncertainty.

Groups may describe:

- Clinical subtype or presentation.
- Visibility and examination completeness.
- Demographic characteristics.
- Scanner or acquisition protocol.
- Referral setting.
- Reference method.
- Combinations of these factors.

When groups form a mutually exclusive, exhaustive partition,

$$
\boxed{
R=\sum_g\Pr(G=g)R_g.
}
$$

This follows from the law of total expectation.

Overlapping groups cannot be added this way without double-counting. Separate overlapping analyses remain useful, but an overall decomposition requires a partition, such as defined intersections.

### 2. Use the correct weights for each metric

Overall sensitivity is

$$
\Pr(T=1\mid D=1).
$$

Partitioning disease-positive patients by group gives

$$
\boxed{
s=\sum_g\Pr(G=g\mid D=1)s_g,
}
$$

where

$$
s_g=\Pr(T=1\mid D=1,G=g).
$$

Specificity instead uses

$$
\boxed{
c=\sum_g\Pr(G=g\mid D=0)c_g.
}
$$

The weights are group frequencies within the relevant disease class. They are not generally the overall group proportions.

Predictive values involve another conditioning direction. Within group $$g$$,

$$
\operatorname{PPV}_g
=
\frac{\pi_gs_g}
{\pi_gs_g+(1-\pi_g)(1-c_g)},
$$

where

$$
\pi_g=\Pr(D=1\mid G=g).
$$

Equal sensitivity and specificity across groups do not imply equal predictive values when prevalences differ. A fairness or robustness claim must identify which property is required and why.

### 3. Construct a case-mix change with unchanged subgroup performance

Suppose a population contains two presentation groups. Construct the following source cohort:

| Group | Patients | Errors | Error rate |
|---|---:|---:|---|
| Common presentation | 90 | 9 | $$1/10$$ |
| Subtle presentation | 10 | 4 | $$2/5$$ |
| Total | 100 | 13 | $$13/100$$ |

Now construct a target cohort with equal numbers from the two groups:

| Group | Patients | Errors | Error rate |
|---|---:|---:|---|
| Common presentation | 50 | 5 | $$1/10$$ |
| Subtle presentation | 50 | 20 | $$2/5$$ |
| Total | 100 | 25 | $$1/4$$ |

The conditional error rates are unchanged. Aggregate error increases because the more difficult presentation becomes more common:

$$
R_s
=
\frac9{10}\frac1{10}
+
\frac1{10}\frac25
=
\frac{13}{100},
$$

$$
R_t
=
\frac12\frac1{10}
+
\frac12\frac25
=
\frac14.
$$

The difference is

$$
R_t-R_s=\frac{12}{100}=\frac3{25}.
$$

A performance decline therefore need not mean the model became worse within every clinical subgroup. The new mixture can be sufficient.

These labels describe a constructed example; they are not measured error rates for subtle medical findings.

### 4. Decompose an external performance difference

Let

$$
w_{sg}=\Pr_s(G=g),
\qquad
w_{tg}=\Pr_t(G=g),
$$

and

$$
R_{sg}=\mathbb E_s[L\mid G=g],
\qquad
R_{tg}=\mathbb E_t[L\mid G=g].
$$

Assume the loss and group definitions are comparable across settings.

Then

$$
R_t-R_s
=
\sum_g w_{tg}R_{tg}
-
\sum_g w_{sg}R_{sg}.
$$

Add and subtract $$\sum_gw_{tg}R_{sg}$$:

$$
\boxed{
R_t-R_s
=
\underbrace{\sum_g(w_{tg}-w_{sg})R_{sg}}_{\text{mixture change}}
+
\underbrace{\sum_gw_{tg}(R_{tg}-R_{sg})}_{\text{within-group change}}.
}
$$

The first term asks what would happen if only group frequencies changed. The second records changes within the chosen groups.

This is an algebraic decomposition, not a causal attribution. An apparent within-group change can still reflect unmeasured case mix inside a broad category, altered labels, or acquisition differences.

A standardized comparison uses common weights $$w_g^*$$:

$$
R_s^{\mathrm{std}}=\sum_gw_g^*R_{sg},
$$

$$
R_t^{\mathrm{std}}=\sum_gw_g^*R_{tg}.
$$

Their difference compares conditional performance under the same declared mixture. It requires relevant groups to be represented in both settings.

### 5. Derive why smaller subgroup estimates are less precise

For a fixed subgroup containing $$n_g$$ independent patients and a binary success probability $$p_g$$,

$$
\widehat p_g=\frac1{n_g}\sum_{i:G_i=g}Z_i.
$$

Independence gives

$$
\boxed{
\operatorname{Var}(\widehat p_g)
=
\frac{p_g(1-p_g)}{n_g}.
}
$$

If two groups have the same underlying success probability, their standard-error ratio is

$$
\frac{\operatorname{SE}(\widehat p_g)}
{\operatorname{SE}(\widehat p_h)}
=
\sqrt{\frac{n_h}{n_g}}.
$$

A group with one sixteenth as many relevant patients has four times the standard error under this model.

For subgroup sensitivity, the relevant count is positive patients within the group. A large subgroup with very few positive outcomes can still have highly uncertain sensitivity.

Clustering reduces independent information further. Multiple frames from a small number of patients cannot solve that limitation.

### 6. Carry subgroup intervals through exact arithmetic

Use the Wilson score interval with the illustrative critical value $$z=2$$. Its nominal normal-reference level is $$2\Phi(2)-1$$.

In count form, its center and half-width are

$$
\text{center}
=
\frac{x+z^2/2}{n+z^2},
$$

$$
\text{half-width}
=
\frac{z}{n+z^2}
\sqrt{\frac{x(n-x)}{n}+\frac{z^2}{4}}.
$$

Construct two groups with the same observed success proportion:

| Group | Successes | Patients | Observed proportion |
|---|---:|---:|---|
| Small | 12 | 16 | $$3/4$$ |
| Large | 192 | 256 | $$3/4$$ |

For the small group,

$$
\text{center}=\frac{12+2}{16+4}=\frac7{10},
$$

and

$$
\text{half-width}
=
\frac2{20}\sqrt{\frac{12\cdot4}{16}+1}
=
\frac1{10}\sqrt4
=
\frac15.
$$

Its interval is

$$
\boxed{\left[\frac12,\frac9{10}\right]}.
$$

For the large group,

$$
\text{center}
=
\frac{192+2}{256+4}
=
\frac{97}{130},
$$

and

$$
\text{half-width}
=
\frac2{260}
\sqrt{\frac{192\cdot64}{256}+1}
=
\frac1{130}\sqrt{49}
=
\frac7{130}.
$$

Its interval is

$$
\boxed{
\left[\frac{90}{130},\frac{104}{130}\right]
=
\left[\frac9{13},\frac45\right].
}
$$

The point estimates are identical. The evidence supporting them is not equally precise.

A subgroup with a wide interval should not be described as performing equivalently merely because its difference from another group is nonsignificant.

### 7. Small groups and multiplicity compound each other

Suppose a study examines $$M$$ subgroup claims.

For a simultaneous error probability bounded by $$\alpha$$, one simple approach uses per-comparison level $$\alpha/M$$. By the union bound,

$$
\Pr(\text{at least one false claim})
\leq
\sum_{g=1}^M\frac{\alpha}{M}
=
\alpha.
$$

A corresponding normal critical value is

$$
z_M=\Phi^{-1}\left(1-\frac{\alpha}{2M}\right).
$$

An approximate subgroup half-width is then

$$
h_g\approx
z_M\sqrt{\frac{p_g(1-p_g)}{n_g}}.
$$

More detailed subgrouping can simultaneously:

- Reduce the number of cases in each group.
- Increase the critical value needed for a simultaneous claim.

This does not mean small groups should be ignored. It means the scope of the claim must match the information.

Prespecified clinically important groups can support confirmatory analyses. Newly discovered intersections can generate hypotheses for additional data collection.

### 8. Distinguish a subgroup difference from a difference in significance

Suppose model A is compared with model B in two groups. Define

$$
\Delta_g=p_{Ag}-p_{Bg},
$$

$$
\Delta_h=p_{Ah}-p_{Bh}.
$$

The question of whether the improvement differs between groups concerns

$$
\boxed{I=\Delta_g-\Delta_h.}
$$

A significant result for $$\Delta_g$$ and a nonsignificant result for $$\Delta_h$$ does not establish $$I\neq0$$. The groups may have the same effect but different precision.

For disjoint independent patient groups,

$$
\operatorname{Var}(\widehat I)
=
\operatorname{Var}(\widehat\Delta_g)
+
\operatorname{Var}(\widehat\Delta_h).
$$

Overlapping groups require covariance terms.

A subgroup disparity also does not identify its cause. Disease spectrum, image quality, label reliability, and workflow may differ together. Mechanism claims need additional evidence.

### 9. Derive what external validation adds to internal validation

Let a representative internal test estimate source risk:

$$
\mathbb E[\widehat R_s]=R_s.
$$

If it is used to estimate target risk $$R_t$$, its bias for that target is

$$
\mathbb E[\widehat R_s]-R_t=R_s-R_t.
$$

Its mean squared error relative to the target is

$$
\begin{aligned}
\mathbb E[(\widehat R_s-R_t)^2]
&=
\mathbb E[
(\widehat R_s-R_s+R_s-R_t)^2
]\\
&=
\boxed{
\operatorname{Var}(\widehat R_s)
+
(R_s-R_t)^2
}.
\end{aligned}
$$

The cross-term vanishes because $$\mathbb E[\widehat R_s-R_s]=0$$.

Increasing the internal sample can reduce the first term. It does not identify or remove the second.

A representative, independently evaluated target sample can estimate

$$
R_t=\mathbb E_t[L].
$$

This is the information external validation supplies: outcomes under conditions the internal sample did not observe.

It still does not guarantee performance in every other target. It estimates the particular external population under the reference, timing, and workflow used there.

### 10. A multicenter dataset can support a site shortcut

Construct two sites:

| Site | Positive patients | Negative patients | Model score |
|---|---:|---:|---|
| H | 90 | 10 | 1 for everyone |
| L | 10 | 90 | 0 for everyone |

The model recognizes only site. It makes no distinctions within either site.

There are 100 positives and 100 negatives overall.

For AUROC:

- The 90 positive patients at H outrank the 90 negative patients at L: 8,100 wins.
- Positive-negative pairs within H contribute 900 ties.
- Positive-negative pairs within L contribute 900 ties.
- Positive patients at L lose to negative patients at H.

Giving half credit to ties,

$$
\begin{aligned}
\operatorname{AUROC}
&=
\frac{8100+\frac12(900+900)}{100\cdot100}\\
&=
\frac{9000}{10000}\\
&=\boxed{\frac9{10}}.
\end{aligned}
$$

Within either site, all scores tie:

$$
\operatorname{AUROC}_{H}
=
\operatorname{AUROC}_{L}
=
\frac12.
$$

A random patient split containing both sites in training and testing can preserve this shortcut.

If the sites' positive and negative counts are reversed while the score rule remains fixed, pooled AUROC becomes

$$
\frac{100+\frac12(900+900)}{10000}
=
\frac1{10}.
$$

The constructed model's success depends on the site-outcome association, not clinical discrimination within a site.

“Multicenter” therefore describes data provenance. It does not by itself establish generalization to unseen institutions or freedom from site-associated prediction.

### 11. State what generalization means along each axis

| Axis | What may change | What a successful evaluation can support |
|---|---|---|
| Case mix | Disease prevalence, severity, subtype, competing diagnoses | Performance in the tested target mixture and represented subgroups |
| Acquisition | Device, settings, operator, view selection, reconstruction | Tolerance of the actual acquisition differences evaluated |
| Label definition | Target definition, reference method, adjudication, follow-up | Agreement with that target reference, which may differ from the source estimand |
| Workflow | Timing, users, aggregation, action thresholds, capacity | Performance or utility of the tested operational pathway |

For case mix, report both the overall target result and relevant conditional results.

For acquisition, establish whether the clinical evidence remains available. A technically unfamiliar image may still preserve the finding; a familiar-looking image may omit it.

For label changes, distinguish disagreement caused by a new reference process from failure to recognize the same clinical state. If the target definition changes, “same task at a new site” may no longer be an adequate description.

### 12. Robustness requires a valid perturbation target

Let $$T$$ transform an input. For a classification task, one may expect

$$
f(T(X))\approx f(X)
$$

when the transformation preserves both the intended target and the relevant evidence.

Preserving the patient's disease state is not sufficient. Erasing a lesion leaves the patient diseased while removing information available to an image classifier.

For localization or segmentation, the desired relationship may be equivariance:

$$
f(T(X))\approx T_Y(f(X)),
$$

where $$T_Y$$ applies the corresponding transformation to the output. A shifted image should generally produce a shifted localization, not an unchanged mask.

A perturbation test therefore needs an explicit statement about what should remain invariant and what should transform.

Synthetic brightness or noise changes can test a defined sensitivity. They do not automatically reproduce a device's full acquisition process.

### 13. Connect score sensitivity to a decision margin

Let $$s(X)$$ be a score and $$t$$ the decision threshold. Suppose a justified bound holds over a perturbation set:

$$
|s(T(X))-s(X)|\leq L\varepsilon.
$$

If the original score is positive with margin

$$
s(X)-t>L\varepsilon,
$$

then

$$
s(T(X))
\geq s(X)-L\varepsilon
>t.
$$

The classification remains positive.

Similarly, if

$$
t-s(X)>L\varepsilon,
$$

the classification remains negative.

Thus a sufficient condition for decision stability is

$$
\boxed{|s(X)-t|>L\varepsilon.}
$$

This connects a perturbation bound to an operating-point claim.

It does not establish correctness. A confidently wrong score can remain wrong under every tested transformation. Nor does a maximum change observed over a few edits establish a bound over all possible acquisition changes.

Clinical robustness needs both a meaningful perturbation set and an appropriate performance criterion.

### 14. Separate frozen transfer from local adaptation

An external evaluation should first specify what was frozen:

- Input selection and preprocessing.
- Model parameters.
- Examination-level aggregation.
- Probability calibration.
- Decision thresholds.
- Missing-input and abstention handling.

If target data are used to revise these components, the adapted system is a new evaluated procedure.

Adaptation can be useful. Its data access should be declared, and its final performance should be evaluated on cases independent of adaptation.

A successful recalibration can repair probability interpretation without repairing missing clinical information. An unchanged AUROC after recalibration is not evidence that acquisition robustness improved.

### 15. Build an external-validation report around its scope

For each source and target, record:

- Eligibility and referral pathways.
- Patient and outcome counts.
- Clinical subgroup composition.
- Acquisition and operator information.
- Reference procedures and label definitions.
- Missingness and assessability.
- The fixed operating point and workload.
- Adaptation, if any.
- Uncertainty and unsupported subgroups.

Stable performance does not prove stable evidence reliance. The same shortcut may persist across all tested settings.

Conversely, reduced performance can occur when target images genuinely contain less assessable evidence. That should prompt investigation of acquisition and intended use, not an automatic conclusion that every failure is a model shortcut.

### 16. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| What is subgroup risk? | Expected loss conditional on a defined group |
| How does overall risk combine groups? | A prevalence-weighted sum for a mutually exclusive partition |
| Which weights combine sensitivities? | Group frequencies among disease-positive patients |
| Why can aggregate performance change with stable group rates? | Case-mix weights change |
| Why are small subgroup intervals wider? | Proportion variance scales as $$1/n_g$$ |
| How does multiplicity compound sparsity? | More comparisons require stronger simultaneous protection while groups contain fewer cases |
| Does significance in one group imply a group difference? | No; the interaction must be evaluated directly |
| What can more internal data fail to resolve? | The source-target risk difference |
| Why is pooled multicenter performance insufficient? | Site-outcome associations can support prediction without within-site clinical discrimination |
| What makes a perturbation meaningful? | It preserves or appropriately transforms the evidence and target |
| What does decision stability establish? | Resistance to specified score changes, not correctness or clinical utility |

In the ontology, subgroup evaluation and external validation assess specific aspects of robustness and transportability. Clinical targets set the acceptable operating behavior. Clinical evidence reliance requires its own assessment across the settings being claimed.

## Why it matters for my work

For gallbladder ultrasound, I would organize transfer tests around actual device, operator, presentation, and referral differences. Prediction quality and evidence reliance should be evaluated together, while preserving whether the relevant findings remain assessable in each setting.

## What I have not resolved

- Which acquisition changes preserve the findings the model is expected to use?
- Which clinically important intersections are too sparse or absent?
- Which target settings are sufficiently represented to support the intended deployment claim?

---

Sources: Independent study; the mixture decomposition, subgroup intervals, external-risk calculation, site-only classifier example, and decision-margin argument are derived above. Numerical examples are constructed rather than empirical claims about particular hospitals or groups. These are study notes for research purposes, not clinical guidance.
