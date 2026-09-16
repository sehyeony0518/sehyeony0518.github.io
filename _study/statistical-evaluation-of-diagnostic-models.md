---
layout: study_note
title: "Statistical Evaluation of Diagnostic Models"
description: "Confidence intervals, bootstrapping, power, and the pitfalls that recur in diagnostic accuracy papers."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
subgroup: "Validation Design & Performance Measures"
order: 9
source: "Independent study"
written: true
updated: "2026-09-08"
---

A performance estimate is a calculation from particular cases. Statistical inference describes how that calculation varies under a specified sampling process. It does not automatically account for biased enrollment, an inadequate reference, or a hospital missing from the study.

## Core question and definition

Before choosing an interval or test, define the **estimand**: the quantity the analysis intends to estimate.

Examples include:

- Sensitivity at a fixed threshold among eligible disease-positive patients.
- Specificity among the relevant alternative diagnoses.
- The paired difference between two models on the same patients.
- Performance averaged over a specified mixture of institutions.
- A clinically weighted difference in decisions.

These require different denominators and assumptions.

A frequentist confidence procedure with coverage $$1-\alpha$$ contains the fixed target parameter in that proportion of repeated samples under its assumptions. After one interval has been observed, the coverage statement does not assign a probability to the fixed parameter.

Precision is therefore conditional on the sampling model. A narrow interval around a biased estimand remains a narrow interval around the wrong quantity.

## Key concepts

### 1. Derive uncertainty for a proportion

Suppose a fixed rule is evaluated on $$n$$ independent, identically distributed patients. Let

$$
Z_i=
\begin{cases}
1,&\text{success},\\
0,&\text{failure},
\end{cases}
$$

with

$$
\Pr(Z_i=1)=p.
$$

Then

$$
K=\sum_{i=1}^n Z_i
$$

has binomial probability

$$
\Pr(K=k)=\binom nk p^k(1-p)^{n-k}.
$$

The sample proportion is

$$
\widehat p=\frac Kn.
$$

Because

$$
\mathbb E[Z_i]=p,
\qquad
\operatorname{Var}(Z_i)=p(1-p),
$$

independence gives

$$
\mathbb E[\widehat p]=p,
$$

and

$$
\boxed{
\operatorname{Var}(\widehat p)=\frac{p(1-p)}{n}.
}
$$

For sensitivity, $$n$$ is the number of disease-positive patients. For specificity, it is the number of disease-negative patients.

The total image count is not the appropriate denominator when multiple images share a patient.

### 2. Derive the Wald interval and its boundary failure

A normal approximation treats

$$
\frac{\widehat p-p}{\sqrt{p(1-p)/n}}
$$

as approximately standard normal.

Let

$$
z=\Phi^{-1}(1-\alpha/2),
$$

where $$\Phi$$ is the standard normal distribution function.

Replacing the unknown variance by its estimate gives the Wald interval:

$$
\boxed{
\widehat p
\pm
z\sqrt{\frac{\widehat p(1-\widehat p)}{n}}.
}
$$

At $$\widehat p=0$$ or $$\widehat p=1$$, the estimated variance is zero. The interval collapses to a single point regardless of sample size.

If a model detects all ten positive patients,

$$
\widehat p=1,
$$

and the Wald interval is

$$
[1,1].
$$

But under any true sensitivity $$0<p<1$$, observing ten successes has probability

$$
p^{10}>0.
$$

The data do not prove sensitivity one.

Near a boundary, the symmetric interval can also extend outside the parameter space. With one success in 20 trials and the illustrative choice $$z=2$$,

$$
\widehat p=\frac1{20},
$$

and the half-width is

$$
2\sqrt{\frac{(1/20)(19/20)}{20}}
=
\frac{\sqrt{95}}{100}.
$$

The lower endpoint is

$$
\frac{5-\sqrt{95}}{100}<0.
$$

Truncating it at zero removes an impossible endpoint but does not repair the interval's underlying coverage behavior.

### 3. Derive Wilson's interval by testing candidate proportions

Wilson's interval evaluates each candidate value of $$p$$ using the variance implied by that candidate, rather than substituting the observed proportion before inversion. This is the score-test inversion described in the NIST handbook. [NIST explanation of proportion confidence intervals](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm).

Retain candidate values satisfying

$$
\left|
\frac{\widehat p-p}{\sqrt{p(1-p)/n}}
\right|
\leq z.
$$

Squaring and rearranging,

$$
n(\widehat p-p)^2\leq z^2p(1-p),
$$

$$
n\widehat p^2-2n\widehat pp+np^2
\leq z^2p-z^2p^2,
$$

so

$$
\boxed{
(n+z^2)p^2-(2n\widehat p+z^2)p+n\widehat p^2\leq0.
}
$$

The admissible values lie between the quadratic's roots.

Its discriminant is

$$
\begin{aligned}
\Delta
&=(2n\widehat p+z^2)^2
-4(n+z^2)n\widehat p^2\\
&=4nz^2\widehat p(1-\widehat p)+z^4.
\end{aligned}
$$

Applying the quadratic formula and dividing numerator and denominator by $$2n$$ gives

$$
\boxed{
p_{\pm}
=
\frac{
\widehat p+\frac{z^2}{2n}
\pm
z\sqrt{
\frac{\widehat p(1-\widehat p)}{n}
+
\frac{z^2}{4n^2}
}
}{
1+\frac{z^2}{n}
}.
}
$$

This interval remains within the probability range and does not collapse after zero observed failures.

The algebra is exact for the inverted score inequality. Its nominal coverage still comes from a normal-reference approximation; it is not an exact binomial coverage guarantee for every sample size and parameter.

### 4. Carry Wilson's interval through a concrete example

Use $$z=2$$ to keep the arithmetic exact. Its nominal normal-reference confidence level is $$2\Phi(2)-1$$.

Suppose 12 of 16 positive patients are detected:

$$
\widehat p=\frac{12}{16}=\frac34.
$$

The denominator is

$$
1+\frac4{16}=\frac54.
$$

The numerator's center is

$$
\frac34+\frac4{32}=\frac78.
$$

Inside the square root,

$$
\begin{aligned}
\frac{(3/4)(1/4)}{16}+\frac4{4(16)^2}
&=\frac3{256}+\frac1{256}\\
&=\frac1{64}.
\end{aligned}
$$

Thus the numerator's half-width is

$$
2\sqrt{\frac1{64}}=\frac14.
$$

The interval is

$$
\begin{aligned}
\left[
\frac{7/8-1/4}{5/4},
\frac{7/8+1/4}{5/4}
\right]
&=
\left[
\frac{5/8}{5/4},
\frac{9/8}{5/4}
\right]\\
&=\boxed{\left[\frac12,\frac9{10}\right]}.
\end{aligned}
$$

The point estimate is three quarters, but the interval reveals how little precision 16 positive patients provide.

At the all-success boundary, substituting $$\widehat p=1$$ gives

$$
\boxed{
\left[\frac{n}{n+z^2},1\right].
}
$$

At the all-failure boundary,

$$
\boxed{
\left[0,\frac{z^2}{n+z^2}\right].
}
$$

For the same illustrative $$z=2$$:

| Observed successes | Point estimate | Wilson interval |
|---|---|---|
| 10 of 10 | $$1$$ | $$[5/7,1]$$ |
| 100 of 100 | $$1$$ | $$[25/26,1]$$ |
| 0 of 20 | $$0$$ | $$[0,1/6]$$ |

“No observed failures” becomes more informative as the number of independent cases increases.

### 5. Exact binomial reasoning gives another boundary check

If all $$n$$ trials succeed, their probability under candidate success probability $$p$$ is

$$
p^n.
$$

A one-sided lower bound obtained by exact tail inversion solves

$$
p_L^n=\alpha,
$$

so

$$
\boxed{p_L=\alpha^{1/n}.}
$$

Equivalently, with zero failures and failure probability $$q=1-p$$, the corresponding upper bound is

$$
\boxed{q_U=1-\alpha^{1/n}.}
$$

An absence of failures therefore leaves a nonzero upper bound on the failure rate.

Exact binomial procedures account for the discrete sampling distribution. Their coverage can be conservative because the available tail probabilities do not vary continuously with the observed count.

Neither an exact interval nor Wilson's interval corrects reference error, patient selection, or clustering. Those problems change the sampling or target model.

### 6. Derive the advantage of paired model comparisons

Suppose models A and B are evaluated on the same $$n$$ patients. Let

$$
A_i=\mathbf1\{\text{A correct on patient }i\},
$$

$$
B_i=\mathbf1\{\text{B correct on patient }i\}.
$$

The estimated accuracy difference is

$$
\widehat\Delta=\frac1n\sum_i(A_i-B_i).
$$

For independent patient pairs,

$$
\boxed{
\operatorname{Var}(\widehat\Delta)
=
\frac{
\operatorname{Var}(A_i)+\operatorname{Var}(B_i)
-2\operatorname{Cov}(A_i,B_i)
}{n}.
}
$$

An unpaired analysis drops the covariance term. When the models tend to succeed and fail on the same patients, covariance is positive, and ignoring pairing overstates the variance of their difference.

Positive covariance is not guaranteed. Ignoring pairing is generally a mismatch to the design; its direction depends on the joint results.

Separate confidence intervals for A and B do not reveal this covariance. Their overlap is not a test of the paired difference.

### 7. Derive McNemar's test from discordant cases

Use the paired correctness table:

| | B correct | B wrong |
|---|---:|---:|
| A correct | $$a$$ | $$b$$ |
| A wrong | $$c$$ | $$d$$ |

The accuracy difference is

$$
\begin{aligned}
\widehat\Delta
&=\frac{a+b}{n}-\frac{a+c}{n}\\
&=\boxed{\frac{b-c}{n}}.
\end{aligned}
$$

Cases where both models agree on correctness cancel.

Let the population probabilities of the two discordant outcomes be $$p_b$$ and $$p_c$$. Equal marginal accuracy means

$$
p_b=p_c.
$$

Conditional on a patient being discordant,

$$
\Pr(\text{A alone correct}\mid\text{discordant})
=
\frac{p_b}{p_b+p_c}
=
\frac12.
$$

For independent, identically distributed patient pairs, conditional on the total number of discordant cases

$$
m=b+c,
$$

the null distribution is

$$
\boxed{b\mid m\sim\operatorname{Binomial}(m,1/2).}
$$

This gives an exact conditional test.

A common two-sided tail convention is

$$
\boxed{
p_{\mathrm{exact}}
=
\min\left\{
1,\;
2\sum_{j=0}^{\min(b,c)}
\binom mj2^{-m}
\right\}.
}
$$

For sufficiently many discordant cases, standardizing the binomial count gives

$$
\frac{b-m/2}{\sqrt{m/4}}
=
\frac{b-c}{\sqrt{b+c}}.
$$

Squaring yields the uncorrected large-sample McNemar statistic:

$$
\boxed{
\chi^2_{\mathrm{McN}}
=
\frac{(b-c)^2}{b+c},
}
$$

with an approximate chi-square reference distribution with one degree of freedom.

The relevant count for this approximation is discordance, not total dataset size.

### 8. Identical accuracies can produce different paired evidence

Construct two possible 100-patient comparisons:

| Comparison | Both correct | A alone correct | B alone correct | Both wrong |
|---|---:|---:|---:|---:|
| I | 80 | 12 | 4 | 4 |
| II | 84 | 8 | 0 | 8 |

In both comparisons,

$$
\operatorname{Accuracy}_A=\frac{92}{100},
$$

$$
\operatorname{Accuracy}_B=\frac{84}{100},
$$

and

$$
\widehat\Delta=\frac8{100}.
$$

For comparison I, there are 16 discordant patients:

$$
\begin{aligned}
p_{\mathrm{exact}}
&=
2\frac{
\binom{16}{0}+\binom{16}{1}+\binom{16}{2}
+\binom{16}{3}+\binom{16}{4}
}{2^{16}}\\
&=
2\frac{1+16+120+560+1820}{65536}\\
&=\boxed{\frac{2517}{32768}}.
\end{aligned}
$$

For comparison II, all eight discordant patients favor A:

$$
p_{\mathrm{exact}}
=
2\frac{\binom80}{2^8}
=
\boxed{\frac1{128}}.
$$

The marginal accuracies are identical, but the paired evidence differs. In comparison I, gains and losses oppose each other more often. In comparison II, every observed difference favors A.

At an illustrative significance level $$1/20$$, the first exact value exceeds the level and the second falls below it. This is a statement about the constructed statistical comparison, not about clinical importance.

### 9. Derive the paired difference's variance directly

Let

$$
D_i=A_i-B_i.
$$

Then $$D_i$$ is one for A-only successes, minus one for B-only successes, and zero otherwise.

Therefore,

$$
\mathbb E[D_i]=p_b-p_c,
$$

and

$$
\mathbb E[D_i^2]=p_b+p_c.
$$

Thus,

$$
\boxed{
\operatorname{Var}(\widehat\Delta)
=
\frac{p_b+p_c-(p_b-p_c)^2}{n}.
}
$$

This expression explains why the marginal accuracies alone cannot determine uncertainty in their difference.

For sensitivity comparisons, construct the paired table only among reference-positive patients. For specificity, use reference-negative patients. Comparing overall correctness can conceal opposing changes in these two clinically distinct errors.

McNemar's test also does not compare AUROC or probability calibration. Those require methods appropriate to the metric while preserving the paired patient structure.

### 10. Multiplicity changes the chance of an apparently positive result

Suppose $$M$$ hypotheses are all null and each independent test has false-positive probability $$\alpha$$.

The probability that none falsely rejects is

$$
(1-\alpha)^M.
$$

Therefore,

$$
\boxed{
\Pr(\text{at least one false rejection})
=
1-(1-\alpha)^M.
}
$$

With 20 independent null tests at level $$1/20$$,

$$
1-\left(\frac{19}{20}\right)^{20}
\approx0.6415.
$$

This number follows from the constructed testing setup; it is not an empirical rate for a particular research field.

Independence is unnecessary for the expected number of false rejections. If each test has exact false-positive probability $$\alpha$$,

$$
\mathbb E[\text{false rejections}]
=
\sum_{j=1}^M\Pr(\text{false rejection }j)
=
M\alpha.
$$

For valid tests bounded by $$\alpha$$, this becomes an upper bound.

Testing many subgroups, layers, thresholds, masking strategies, and outcome definitions creates a family of opportunities for selection, even if only the most favorable result is eventually reported.

### 11. Derive a simple familywise correction

By the union bound,

$$
\Pr\left(\bigcup_{j=1}^M\{\text{false rejection }j\}\right)
\leq
\sum_{j=1}^M
\Pr(\text{false rejection }j).
$$

If each test uses level $$\alpha/M$$,

$$
\Pr(\text{any false rejection})
\leq M\frac{\alpha}{M}
=\alpha.
$$

This is the Bonferroni principle. It does not require independent tests.

For simultaneous two-sided intervals, a corresponding normal critical value is

$$
z_M=\Phi^{-1}\left(1-\frac{\alpha}{2M}\right).
$$

It exceeds the single-comparison critical value and produces wider intervals.

The family should follow the scientific claim. Confirmatory comparisons need prespecification. Exploratory subgroup discoveries remain useful, but their discovery process and need for confirmation should be explicit.

### 12. Statistical significance does not establish clinical importance

For an estimated effect $$\widehat\Delta$$ with standard error approximately $$\tau/\sqrt n$$, the standardized statistic is

$$
Z\approx\frac{\widehat\Delta\sqrt n}{\tau}.
$$

A small nonzero effect can become statistically distinguishable from zero as the sample grows.

Clinical importance instead depends on whether the effect changes worthwhile decisions. Let $$\Delta_{\mathrm{clin}}>0$$ be a prespecified minimum useful improvement.

Evidence against

$$
\Delta=0
$$

does not by itself establish

$$
\Delta>\Delta_{\mathrm{clin}}.
$$

For a constructed illustration, suppose an appropriately obtained interval for improvement is

$$
\left[\frac1{1000},\frac3{1000}\right],
$$

while the minimum useful improvement is

$$
\Delta_{\mathrm{clin}}=\frac1{100}.
$$

The interval excludes zero but lies entirely below the specified useful effect.

The margin must be justified by the workflow and consequences. Small effects can be valuable in some settings; their value cannot be decided from a significance label alone.

Likewise, a nonsignificant result is not evidence of equivalence. Equivalence requires sufficiently precise evidence relative to a prespecified acceptable range. Noninferiority requires an appropriate bound relative to a justified loss margin.

### 13. Plan for precision and power separately

For a proportion away from boundaries, an approximate interval half-width is

$$
h\approx z\sqrt{\frac{p(1-p)}{n}}.
$$

Solving for sample size,

$$
\boxed{
n\approx\frac{z^2p(1-p)}{h^2}.
}
$$

Since

$$
p(1-p)=\frac14-\left(p-\frac12\right)^2\leq\frac14,
$$

a conservative variance-based planning expression is

$$
n\approx\frac{z^2}{4h^2}.
$$

These are planning approximations, not exact finite-sample guarantees.

For sensitivity, the required observations are disease-positive patients. If a consecutive cohort has prevalence $$\pi$$, its expected number of positives is

$$
\mathbb E[N_+]=N\pi.
$$

Meeting an expected count does not guarantee that count in the realized sample.

Power concerns the probability of rejecting a specified null under a specified alternative. It depends on effect size, variability, significance level, design, and multiplicity. Precision concerns the width of estimation uncertainty. The two should not be substituted for each other.

### 14. Bootstrap the unit and preserve the comparison

For a frozen model evaluated on repeated observations:

- Resample independent patients.
- Retain their associated examinations or frames.
- Keep both models' predictions together in paired comparisons.
- Reapply the prespecified aggregation and metric.
- Record resamples where the metric is undefined.

Resampling individual frames treats within-patient variation as independent patient information.

A bootstrap of fixed predictions estimates uncertainty from the evaluation sample. It does not include variation from retraining the model. Repeated training runs address another component, and neither automatically captures transfer to an unobserved institution.

Bootstrap methods also do not manufacture missing information. If every observed positive case was detected, resampling those cases produces no failures and can yield a degenerate interval. That does not prove zero population error.

### 15. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| What is the denominator for sensitivity uncertainty? | Independent disease-positive cases |
| Why does Wald fail at a boundary? | Its plug-in variance becomes zero |
| What does Wilson do differently? | It inverts a score inequality using each candidate proportion's variance |
| Does perfect observed sensitivity imply certainty? | No; both Wilson and exact-tail reasoning leave uncertainty |
| Why preserve pairing? | The variance of a difference contains the covariance between models |
| Which cases determine McNemar's test? | Patients on whom model correctness differs |
| Can identical accuracies yield different paired results? | Yes; the discordance table determines the evidence |
| Why does multiplicity matter? | Several valid tests can have a large combined false-positive probability |
| What does a significant result establish? | Evidence against a statistical null under the design assumptions |
| What does clinical importance require? | A consequence-based interpretation and appropriate effect size |
| What can a test-set bootstrap estimate? | Sampling uncertainty conditional on the evaluated fitted pipeline |

In the ontology, statistical evaluation assesses uncertainty in a specified metric. It does not establish reference validity, clinical utility, or transportability. The clinical target sets the endpoint, operating point, and meaningful comparison.

## Why it matters for my work

Faithfulness audits generate many candidate effects across features, interventions, and model components. I need patient-level uncertainty, paired comparisons, and a defined family of claims so that an appealing audit result is not merely the winner of an unreported search.

## What I have not resolved

- What audit effect would change my interpretation of clinical evidence reliance?
- How many independent positive cases are needed for the intended precision?
- Which subgroup and intervention comparisons are confirmatory?

---

Sources: Independent study, with Wilson score inversion checked against the NIST methodological page linked above. All worked counts, intervals, paired comparisons, and multiplicity calculations are constructed and explicitly derived. These are study notes for research purposes, not clinical guidance.
