---
layout: study_note
title: "Evaluation Beyond AUROC"
description: "Sensitivity and specificity at the operating point that matters, decision curves, and clinical utility."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalisation & Reliability"
subgroup: "Validation Design & Performance Measures"
order: 7
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-01-27-guo-calibration"
  - "2025-12-13-seyyed-kalantari-underdiagnosis"
  - "2026-08-23-robustness-stress-testing-medical-image-classification"
---

AUROC describes how a score orders positive and negative cases. A clinical decision requires additional information: where the threshold will be placed, how common the target condition is, what each resulting action costs, and whether that action benefits patients.

## Core question and definition

The central question is:

> What does this evaluation establish about the decision the model will support?

Four different questions need separate answers.

| Question | Property | Example of an appropriate evaluation |
|---|---|---|
| Are positive cases generally ranked above negative cases? | Discrimination | ROC curve and AUROC |
| What happens at the selected decision rule? | Operating-point performance | Sensitivity, specificity, predictive values, workload |
| Do predicted probabilities correspond to observed frequencies? | Calibration | Calibration assessment and proper scoring rules |
| Does acting on the output improve the relevant consequences? | Clinical utility | Decision analysis and comparative evaluation of the workflow |

A ranking metric cannot answer the other three questions by itself. This follows from its mathematical definition, rather than from a general preference for reporting more metrics.

Throughout this note, let:

- $$Y\in\{0,1\}$$ denote the target outcome.
- $$S=s(X)$$ denote a fixed model score, with larger values indicating stronger evidence for $$Y=1$$.
- $$\pi=\Pr(Y=1)$$ denote prevalence in the evaluated population.
- $$t$$ denote a threshold, with a positive prediction when $$S\geq t$$.

Assume both outcome classes occur. Whether the recorded outcome is an adequate reference for the clinical target is a separate validity question.

## Key concepts

### 1. Start with the two conditional score distributions

At threshold $$t$$, define

$$
r(t)=\Pr(S\geq t\mid Y=1)
$$

and

$$
f(t)=\Pr(S\geq t\mid Y=0).
$$

Here $$r(t)$$ is sensitivity, or true-positive rate, and $$f(t)$$ is false-positive rate. Specificity is

$$
1-f(t)=\Pr(S<t\mid Y=0).
$$

The ROC curve plots

$$
\bigl(f(t),r(t)\bigr)
$$

as the threshold decreases from accepting nobody to accepting everybody.

The two probabilities condition on outcome class. Their denominators are different:

$$
\widehat r(t)=\frac{TP}{TP+FN},
\qquad
\widehat f(t)=\frac{FP}{FP+TN}.
$$

Consequently, a false-positive rate describes the fraction of negative patients who receive a positive result. It does not describe the fraction of positive results that are false. The latter quantity also depends on how many positive and negative patients enter the service.

### 2. Derive AUROC as a probability of correct ordering

First assume continuous score distributions, so ties have probability zero. Let

$$
F_1(t)=\Pr(S\leq t\mid Y=1),
\qquad
F_0(t)=\Pr(S\leq t\mid Y=0).
$$

Then

$$
r(t)=1-F_1(t),
\qquad
f(t)=1-F_0(t).
$$

As the threshold moves from positive infinity to negative infinity, the false-positive rate moves from zero to one. Therefore,

$$
\begin{aligned}
\operatorname{AUROC}
&=\int_{t=+\infty}^{t=-\infty}r(t)\,df(t)\\
&=\int_{t=+\infty}^{t=-\infty}
[1-F_1(t)]\,[-dF_0(t)]\\
&=\int_{-\infty}^{+\infty}
[1-F_1(t)]\,dF_0(t).
\end{aligned}
$$

Now draw one positive score $$S_1$$ and one negative score $$S_0$$ independently from their respective conditional distributions. Conditional on the negative score being $$t$$,

$$
\Pr(S_1>S_0\mid S_0=t)=1-F_1(t).
$$

Averaging over the negative score gives

$$
\begin{aligned}
\Pr(S_1>S_0)
&=\int \Pr(S_1>t)\,dF_0(t)\\
&=\int [1-F_1(t)]\,dF_0(t)\\
&=\operatorname{AUROC}.
\end{aligned}
$$

Thus, for continuous scores,

$$
\boxed{\operatorname{AUROC}=\Pr(S_1>S_0).}
$$

For discrete scores or finite datasets, ties require a convention. The usual convention awards half credit to a tied positive-negative pair:

$$
\boxed{
\operatorname{AUROC}
=
\Pr(S_1>S_0)
+\frac12\Pr(S_1=S_0).
}
$$

This is equivalent to breaking each tied pair at random. It also corresponds to the usual trapezoidal ROC area when a threshold passes through a group of equal scores.

AUROC is therefore a pairwise ordering probability. It is not the probability that an individual prediction is correct.

### 3. Derive the Mann–Whitney equivalence

Suppose the evaluation set contains $$n_1$$ positive cases and $$n_0$$ negative cases. Define

$$
U=
\sum_{i=1}^{n_1}
\sum_{j=1}^{n_0}
\left[
\mathbf 1\{s_i^+>s_j^-\}
+\frac12\mathbf 1\{s_i^+=s_j^-\}
\right].
$$

There are $$n_1n_0$$ positive-negative pairs, so

$$
\widehat{\operatorname{AUROC}}
=
\frac{U}{n_1n_0}.
$$

To connect this with ranks, pool all scores and rank them in ascending order, using average ranks for ties. Let $$R_+$$ be the sum of the positive cases' ranks.

A case's rank can be written as one plus the number of lower-scoring cases, with half credit for other cases tied with it. When these contributions are summed over all positive cases:

1. Each positive contributes its initial one, giving $$n_1$$.
2. Each unordered pair of positives contributes exactly one in total. If their scores differ, the higher one counts the lower one; if tied, each contributes one half. This gives $$n_1(n_1-1)/2$$.
3. Comparisons with negative cases contribute exactly $$U$$.

Therefore,

$$
\begin{aligned}
R_+
&=n_1+\frac{n_1(n_1-1)}{2}+U\\
&=\frac{n_1(n_1+1)}{2}+U,
\end{aligned}
$$

and hence

$$
\boxed{
U=R_+-\frac{n_1(n_1+1)}{2}
}
$$

and

$$
\boxed{
\widehat{\operatorname{AUROC}}
=
\frac{
R_+-n_1(n_1+1)/2
}{
n_1n_0
}.
}
$$

This is the Mann–Whitney statistic in the orientation that counts positive scores exceeding negative scores.

The equivalence explains why strictly increasing transformations preserve AUROC. They preserve every ordering and tie, so they preserve every term in $$U$$. Such transformations can nevertheless change the meaning of a numerical score as a probability.

### 4. Why AUROC is prevalence-independent, and what that statement assumes

The population definition contains only

$$
P(S\mid Y=1)
\quad\text{and}\quad
P(S\mid Y=0).
$$

It does not contain $$\pi$$. If prevalence changes while these two conditional distributions remain fixed, AUROC remains fixed.

This is a conditional statement. In an actual transfer, prevalence may change together with disease severity, competing diagnoses, acquisition, or referral selection. These changes can alter the conditional score distributions and therefore alter AUROC.

Under the stated fixed-conditionals assumption, prevalence independence is useful for comparing ranking across different class proportions. It is also precisely why AUROC cannot report the consequences of a prevalence-dependent decision.

By the multiplication rule, the population fractions in the four confusion-matrix cells are

$$
\begin{aligned}
\Pr(TP)&=\pi r,\\
\Pr(FN)&=\pi(1-r),\\
\Pr(FP)&=(1-\pi)f,\\
\Pr(TN)&=(1-\pi)(1-f).
\end{aligned}
$$

For example, accuracy is

$$
\Pr(\text{correct})
=
\pi r+(1-\pi)(1-f),
$$

and the fraction of patients receiving a positive result is

$$
q=\pi r+(1-\pi)f.
$$

The same ROC operating point can therefore produce very different workloads.

### 5. Derive predictive values and the prevalence dependence of the PR curve

Precision, or positive predictive value, conditions on the test result rather than the disease state:

$$
\begin{aligned}
\operatorname{PPV}
&=\Pr(Y=1\mid S\geq t)\\
&=\frac{\Pr(Y=1,S\geq t)}{\Pr(S\geq t)}\\
&=\boxed{\frac{\pi r}{\pi r+(1-\pi)f}}.
\end{aligned}
$$

Similarly,

$$
\operatorname{NPV}
=
\frac{(1-\pi)(1-f)}
{(1-\pi)(1-f)+\pi(1-r)}.
$$

These formulas require nonzero denominators. If a rule predicts no positives, its empirical precision is undefined; a plotting convention does not create an observed predictive value.

A precision-recall curve plots precision against recall, where recall is $$r$$. At a fixed threshold, hold $$r$$ and $$f$$ constant and write

$$
D(\pi)=\pi r+(1-\pi)f.
$$

Then

$$
\begin{aligned}
\frac{\partial \operatorname{PPV}}{\partial \pi}
&=\frac{rD(\pi)-\pi r(r-f)}{D(\pi)^2}\\
&=\frac{
r[\pi r+(1-\pi)f]-\pi r(r-f)
}{
D(\pi)^2
}\\
&=\boxed{\frac{rf}{D(\pi)^2}}.
\end{aligned}
$$

When $$r>0$$ and $$f>0$$, precision increases with prevalence. Recall does not change under this particular shift, because the positive-class score distribution was held fixed. The PR curve therefore moves even though the ROC curve does not.

Two useful limiting cases follow directly:

- If $$f=0$$ and positives are selected, precision is one.
- If scores are independent of outcome, then $$r=f>0$$ and

$$
\operatorname{PPV}
=
\frac{\pi r}{\pi r+(1-\pi)r}
=
\pi.
$$

The population no-information precision baseline is prevalence.

### 6. A fully constructed prevalence example

Construct three hypothetical cohorts, each containing 1,000 patients. In every cohort, set sensitivity to $$4/5$$ and false-positive rate to $$1/10$$.

These are chosen arithmetic examples, not estimates of any clinical test.

| Prevalence | Positive patients | Negative patients | True positives | False positives | Precision | Positive-result fraction |
|---|---:|---:|---:|---:|---|---|
| $$1/2$$ | 500 | 500 | 400 | 50 | $$400/450=8/9$$ | $$450/1000=9/20$$ |
| $$1/10$$ | 100 | 900 | 80 | 90 | $$80/170=8/17$$ | $$170/1000=17/100$$ |
| $$1/100$$ | 10 | 990 | 8 | 99 | $$8/107$$ | $$107/1000$$ |

Every row has the same sensitivity and specificity. If the entire class-conditional score distributions are also held fixed, every row has the same ROC curve and AUROC.

Yet the fraction of positive results representing disease changes sharply. In a referral workflow, this changes the composition of the queue and the amount of unnecessary investigation per true case found.

An enriched evaluation dataset can estimate class-conditional performance under suitable sampling assumptions. Its raw precision does not automatically estimate precision in routine care.

### 7. Equal AUROC can conceal different clinical value

Consider the following six hypothetical patients. Scores are arbitrary ranking values, not probabilities.

| Patient | Outcome | Model A score | Model B score |
|---|---:|---:|---:|
| P1 | 1 | 6 | 6 |
| P2 | 1 | 5 | 4 |
| P3 | 1 | 2 | 3 |
| N1 | 0 | 4 | 5 |
| N2 | 0 | 3 | 2 |
| N3 | 0 | 1 | 1 |

There are nine positive-negative pairs.

For Model A:

- P1 beats all three negatives.
- P2 beats all three negatives.
- P3 beats only N3.

Thus,

$$
U_A=3+3+1=7.
$$

For Model B:

- P1 beats all three negatives.
- P2 beats N2 and N3.
- P3 beats N2 and N3.

Thus,

$$
U_B=3+2+2=7.
$$

Therefore,

$$
\operatorname{AUROC}_A
=
\operatorname{AUROC}_B
=
\frac79.
$$

The rank-sum calculation gives the same answer. Positive ranks sum to 13 for both models, so

$$
U=13-\frac{3(3+1)}{2}=13-6=7.
$$

Now specify a decision: only the two highest-scoring patients can receive an additional review.

| Model | Two reviewed patients | True positives found | False-positive reviews |
|---|---|---:|---:|
| A | P1, P2 | 2 | 0 |
| B | P1, N1 | 1 | 1 |

If finding a positive patient produces incremental benefit $$b>0$$ and a false-positive review produces harm or cost $$h>0$$, then

$$
U_A^{\text{decision}}=2b,
$$

whereas

$$
U_B^{\text{decision}}=b-h.
$$

The difference is

$$
U_A^{\text{decision}}-U_B^{\text{decision}}
=
b+h>0.
$$

This is a decision-model calculation under stipulated consequences. It is not evidence of observed clinical benefit.

The ordering also depends on capacity. If four patients can be reviewed, A selects two positives and two negatives, whereas B selects three positives and one negative. Equal total ROC area can conceal crossing curves and different preferred models at different operating regions.

### 8. Average precision answers another ranking question

For distinct scores sorted from highest to lowest, one common definition of average precision is

$$
\operatorname{AP}
=
\sum_k
(\operatorname{Recall}_k-\operatorname{Recall}_{k-1})
\operatorname{Precision}_k.
$$

Recall changes only when a positive case is encountered. Each positive increases recall by $$1/n_1$$, so

$$
\operatorname{AP}
=
\frac1{n_1}
\sum_{\text{positive ranks }k}
\operatorname{Precision}_k.
$$

In the constructed example, A places positives at ranks one, two, and five:

$$
\operatorname{AP}_A
=
\frac{1+1+3/5}{3}
=
\frac{13}{15}.
$$

B places positives at ranks one, three, and four:

$$
\operatorname{AP}_B
=
\frac{1+2/3+3/4}{3}
=
\frac{29}{36}.
$$

Average precision distinguishes these rankings, but it still does not encode a particular service's benefits, harms, or capacity. It is also not generally identical to a trapezoidal area under a plotted PR curve. An evaluation should state its interpolation and averaging convention.

### 9. Derive how consequences select an ROC operating point

Suppose a true-positive action gives incremental benefit $$B>0$$ and a false-positive action gives incremental harm $$H>0$$, both measured relative to taking no action.

Expected incremental utility per patient is

$$
\mathcal U(t)
=
B\pi r(t)-H(1-\pi)f(t).
$$

Holding utility constant and rearranging gives

$$
r
=
\frac{\mathcal U}{B\pi}
+
\frac{H(1-\pi)}{B\pi}f.
$$

An equal-utility line in ROC space therefore has slope

$$
\frac{H(1-\pi)}{B\pi}.
$$

Prevalence and the consequence ratio determine which part of the ROC curve matters. Neither appears in the AUROC ordering probability.

If a smooth ROC curve has an interior utility-maximizing point, its local slope equals this consequence-dependent slope. If the curve is discrete, has corners, or is constrained by workload, the decision must be made directly among feasible operating points.

A partial ROC area over a prespecified false-positive range can focus attention:

$$
\operatorname{pAUC}(\alpha)
=
\int_0^\alpha \operatorname{TPR}(u)\,du.
$$

But the acceptable limit $$\alpha$$ must come from the intended use. Partial area still averages over thresholds and does not replace evaluation of the actual deployed rule.

### 10. What an evaluation should preserve

The evaluation unit must match the action. A model may score individual frames, while a clinician refers an examination or patient. Aggregation changes both errors and workload; frame-level performance does not determine patient-level performance without an aggregation rule.

The threshold and aggregation rule belong to development. After they are fixed, evaluation should report:

- Patient counts and the four confusion-matrix cells.
- Sensitivity and specificity at the intended rule.
- Predictive values in an appropriate population.
- Calibration if outputs are interpreted as risks.
- Review or referral workload.
- Uncertainty that respects patient and examination clustering.
- Performance in the clinically relevant operating range and subgroups.
- Comparison with the actual alternative workflow.

The $$n_1n_0$$ pair comparisons in AUROC are not $$n_1n_0$$ independent observations: many pairs share the same patient. Confidence intervals must respect that dependence. Resampling individual frames also fails to represent patient-level uncertainty when frames share a patient.

Finally, a reliable estimate against an inadequate reference remains inadequate evidence for the intended clinical claim. Ranking a management label is not automatically ranking disease, and performance among verified cases may not represent patients whose outcomes were never established.

### 11. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| What is AUROC? | A positive-negative ordering probability, with half credit for ties |
| Why does rank sum give AUROC? | Within-positive rank contributions sum to $$n_1(n_1+1)/2$$; the remainder counts cross-class wins |
| When is AUROC prevalence-independent? | When the fixed score's two class-conditional distributions remain unchanged |
| Why does precision change? | Bayes' rule introduces prevalence into the positive-result denominator |
| What moves in a PR curve under pure prevalence change? | Precision changes at each threshold while recall remains fixed |
| Can equal AUROC imply unequal value? | Yes; the constructed models differ at a fixed review capacity |
| Does AP solve the decision problem? | No; its ranking weights do not specify clinical consequences |
| What selects an operating point? | Benefits, harms, prevalence, and feasible workload |
| What is the independent evaluation unit? | The unit supporting the intended claim, usually requiring patient-level separation |
| What does a favorable decision calculation establish? | Modeled value under stated assumptions, not observed improvement in care |

In the ontology, an evaluation metric assesses a particular property. The clinical target sets requirements for the metric and decision rule. Discrimination does not establish calibration, clinical evidence reliance, or clinical utility.

## Why it matters for my work

For gallbladder ultrasound AI, I need to identify the action before choosing the headline metric. Additional image acquisition, specialist review, and intervention have different consequences and operating ranges. Clinical faithfulness auditing can explain why a prediction may be fragile; evaluation at the intended decision rule establishes what that fragility costs.

## What I have not resolved

- Which gallbladder workflow provides a defensible operating range and comparator?
- How should examination-level aggregation account for incomplete or unevenly sampled views?
- Which consequences can be estimated retrospectively, and which require evaluation of actual use?

---

Sources: Independent study; the probability identities, rank-statistic equivalence, and decision calculations are developed explicitly above. All numerical examples are constructed for verification and are not clinical performance estimates. These are study notes for research purposes, not clinical guidance.
