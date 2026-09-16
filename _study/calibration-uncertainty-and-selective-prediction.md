---
layout: study_note
title: "Calibration, Uncertainty, and Selective Prediction"
description: "Whether a stated probability means what it says, and when a model should abstain."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
subgroup: "Calibration & Generalization"
order: 10
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-01-27-guo-calibration"
  - "2026-09-05-auditing-pointwise-reliability-after-learning"
---

A probability estimate should have a defensible interpretation, and withholding an automated prediction should have a defined consequence. Calibration, uncertainty estimation, and selective prediction address different parts of these requirements.

## Core question and definition

Let $$Y\in\{0,1\}$$ be an outcome and

$$
Q=\widehat p(X)\in[0,1]
$$

be a fixed model's predicted probability.

Three questions must be distinguished:

1. **Calibration:** among cases receiving a particular probability, does the outcome occur at that frequency?
2. **Uncertainty:** what remains unknown given the available information and the fitted model?
3. **Selective prediction:** which cases receive an automated answer, and what happens to the others?

Perfect calibration does not imply accurate individual classification. A selection policy does not become useful merely because it rejects many cases. Both statements follow from the definitions developed below.

## Key concepts

### 1. Define perfect calibration as a conditional expectation

Write

$$
\eta(q)=\mathbb E[Y\mid Q=q].
$$

Perfect calibration means

$$
\boxed{\mathbb E[Y\mid Q]=Q\quad\text{almost surely}.}
$$

Equivalently, wherever the conditional probability is defined,

$$
\Pr(Y=1\mid Q=q)=q.
$$

For continuously distributed predictions, an exact score value may have probability zero. The conditional-expectation formulation avoids treating an empty collection of exact matches as an empirical frequency.

Calibration is a property of the joint distribution of predictions and outcomes. It does not mean that an individual patient is partly diseased.

It is also relative to a population. The same model can be calibrated in one referral population and miscalibrated in another.

### 2. Calibration does not imply information or subgroup calibration

A constant forecast

$$
Q=\pi,
\qquad
\pi=\Pr(Y=1),
$$

is perfectly calibrated:

$$
\mathbb E[Y\mid Q=\pi]=\mathbb E[Y]=\pi.
$$

It provides no ranking among patients.

Marginal calibration also need not hold within clinically relevant groups. Construct two equally common groups, A and B, with

$$
\Pr(Y=1\mid A)=\frac34,
\qquad
\Pr(Y=1\mid B)=\frac14.
$$

Give every patient the forecast $$Q=1/2$$. Overall,

$$
\Pr(Y=1)
=
\frac12\cdot\frac34
+
\frac12\cdot\frac14
=
\frac12,
$$

so the model is calibrated in the combined population. Within A it underpredicts risk; within B it overpredicts risk.

Group-conditional calibration would require

$$
\mathbb E[Y\mid Q,G]=Q,
$$

where $$G$$ identifies the group. This is a stronger condition than marginal calibration.

No finite evaluation can establish calibration for every possible subgroup or every exact probability. The grouping, sample size, and uncertainty of the assessment must remain visible.

### 3. Derive why the Brier score is a proper scoring rule

The Brier loss for a binary outcome is

$$
\ell_B(q,y)=(q-y)^2.
$$

Suppose the true event probability in the condition being considered is $$\eta$$. The expected loss from reporting $$q$$ is

$$
\begin{aligned}
\mathbb E[\ell_B(q,Y)]
&=\eta(1-q)^2+(1-\eta)q^2\\
&=\eta(1-2q+q^2)+q^2-\eta q^2\\
&=\eta-2\eta q+q^2\\
&=\eta-\eta^2+(q^2-2\eta q+\eta^2)\\
&=\boxed{\eta(1-\eta)+(q-\eta)^2}.
\end{aligned}
$$

The first term does not depend on the reported probability. The second is nonnegative and equals zero only when $$q=\eta$$.

Therefore truthful reporting uniquely minimizes expected loss. This is the meaning of a strictly proper scoring rule.

The result concerns expected performance. A wrong but lucky forecast can score better on one realized patient.

### 4. Derive calibration and refinement in the Brier score

Condition the previous calculation on the model forecast $$Q$$. The relevant true frequency is now $$\eta(Q)=\mathbb E[Y\mid Q]$$:

$$
\mathbb E[(Y-Q)^2\mid Q]
=
\eta(Q)[1-\eta(Q)]
+
[Q-\eta(Q)]^2.
$$

Taking expectations gives

$$
\boxed{
\operatorname{BS}
=
\underbrace{\mathbb E[Q-\eta(Q)]^2}_{\text{calibration error}}
+
\underbrace{\mathbb E\{\eta(Q)[1-\eta(Q)]\}}_{\text{refinement term}}.
}
$$

The refinement term is the remaining outcome variability after knowing the forecast. Smaller values mean that forecast-defined groups have outcome frequencies closer to zero or one.

It is not necessarily irreducible uncertainty given all available clinical information. A weak score may discard information contained in its inputs.

To obtain the uncertainty-resolution form, let

$$
\pi=\mathbb E[Y]=\mathbb E[\eta(Q)].
$$

Then

$$
\begin{aligned}
\mathbb E\{\eta(Q)[1-\eta(Q)]\}
&=\pi-\mathbb E[\eta(Q)^2]\\
&=\pi-\left(\operatorname{Var}[\eta(Q)]+\pi^2\right)\\
&=\pi(1-\pi)-\operatorname{Var}[\eta(Q)].
\end{aligned}
$$

Consequently,

$$
\boxed{
\operatorname{BS}
=
\underbrace{\pi(1-\pi)}_{\text{uncertainty}}
-
\underbrace{\operatorname{Var}[\eta(Q)]}_{\text{resolution}}
+
\underbrace{\mathbb E[Q-\eta(Q)]^2}_{\text{reliability error}}.
}
$$

Resolution concerns variation in actual conditional outcome frequencies. Merely spreading predictions toward zero and one does not create resolution. If those probabilities are unsupported, the reliability penalty can increase.

### 5. A constructed example of calibration without refinement

Consider a population with prevalence $$1/2$$.

A constant calibrated model reports $$Q=1/2$$ for everyone. Its calibration error is zero, but

$$
\operatorname{BS}_{\text{constant}}
=
\frac12\left(1-\frac12\right)
=
\frac14.
$$

Now construct another calibrated forecast that takes values $$1/4$$ and $$3/4$$ equally often, with the actual event rate matching each forecast.

Its Brier score is

$$
\begin{aligned}
\operatorname{BS}_{\text{informative}}
&=
\frac12\left(\frac14\cdot\frac34\right)
+
\frac12\left(\frac34\cdot\frac14\right)\\
&=\frac{3}{16}.
\end{aligned}
$$

Both models are perfectly calibrated. Their difference is resolution:

$$
\operatorname{Var}[\eta(Q)]
=
\frac12\left(\frac14-\frac12\right)^2
+
\frac12\left(\frac34-\frac12\right)^2
=
\frac1{16}.
$$

Thus,

$$
\frac14-\frac1{16}=\frac3{16}.
$$

A calibration assessment should therefore accompany, rather than replace, an assessment of predictive information.

### 6. The corresponding decomposition for log loss

For probabilities strictly between zero and one, binary log loss is

$$
\ell_{\log}(q,y)
=
-y\log q-(1-y)\log(1-q).
$$

Given event probability $$\eta$$,

$$
\mathbb E[\ell_{\log}(q,Y)]
=
-\eta\log q-(1-\eta)\log(1-q).
$$

Add and subtract the same entropy terms:

$$
\begin{aligned}
\mathbb E[\ell_{\log}(q,Y)]
&=
-\eta\log\eta-(1-\eta)\log(1-\eta)\\
&\quad+
\eta\log\frac{\eta}{q}
+
(1-\eta)\log\frac{1-\eta}{1-q}.
\end{aligned}
$$

Define binary entropy

$$
H(\eta)
=
-\eta\log\eta-(1-\eta)\log(1-\eta).
$$

The remaining expression is the divergence between the true and reported Bernoulli distributions:

$$
D(\eta\Vert q)
=
\eta\log\frac{\eta}{q}
+
(1-\eta)\log\frac{1-\eta}{1-q}.
$$

Its nonnegativity follows from $$\log u\leq u-1$$:

$$
\begin{aligned}
D(\eta\Vert q)
&=
-\eta\log\frac q\eta
-(1-\eta)\log\frac{1-q}{1-\eta}\\
&\geq
-\eta\left(\frac q\eta-1\right)
-(1-\eta)\left(\frac{1-q}{1-\eta}-1\right)\\
&=-(q-\eta)-[(1-q)-(1-\eta)]\\
&=0.
\end{aligned}
$$

Equality holds when $$q=\eta$$. Boundary cases follow by limits; assigning probability zero to an outcome that occurs gives infinite log loss.

Conditioning on $$Q$$ yields

$$
\boxed{
\mathbb E[\ell_{\log}(Q,Y)]
=
\mathbb E[H(\eta(Q))]
+
\mathbb E[D(\eta(Q)\Vert Q)].
}
$$

Again there is a refinement term and a calibration penalty. Proper scores assess both. They are not pure measures of calibration.

### 7. Uncertainty depends on which information is supplied

Let $$X$$ contain a fuller set of observations and let $$Z=g(X)$$ retain only part of that information.

The conditional variance decomposition gives

$$
\operatorname{Var}(Y\mid Z)
=
\mathbb E[\operatorname{Var}(Y\mid X)\mid Z]
+
\operatorname{Var}(\mathbb E[Y\mid X]\mid Z).
$$

Averaging over $$Z$$,

$$
\boxed{
\mathbb E[\operatorname{Var}(Y\mid Z)]
=
\mathbb E[\operatorname{Var}(Y\mid X)]
+
\mathbb E[\operatorname{Var}(\mathbb E[Y\mid X]\mid Z)].
}
$$

The final term is nonnegative. Discarding information cannot reduce the optimal expected squared prediction error.

This gives a precise interpretation of ambiguity in a single ultrasound frame. Additional views may reveal distinctions that are unavailable in that frame. Uncertainty conditional on one image is not necessarily uncertainty conditional on the entire examination.

Aleatoric uncertainty refers to variability remaining conditional on the supplied information. Epistemic uncertainty concerns incomplete knowledge of the predictive relationship. The distinction depends on what information and model class are being considered.

An ensemble can disagree because its members learned different relationships. Agreement does not prove that the shared relationship is correct: every member may rely on the same acquisition cue.

### 8. ECE is a binned estimator, not a direct observation of calibration

For binary probability calibration, partition the forecast range into bins $$B_1,\ldots,B_M$$. In bin $$m$$, let

$$
n_m=\#\{i:Q_i\in B_m\},
$$

$$
\overline Q_m
=
\frac1{n_m}\sum_{i:Q_i\in B_m}Q_i,
\qquad
\overline Y_m
=
\frac1{n_m}\sum_{i:Q_i\in B_m}Y_i.
$$

A common expected calibration error estimator is

$$
\widehat{\operatorname{ECE}}
=
\sum_{m:n_m>0}
\frac{n_m}{n}
\left|\overline Y_m-\overline Q_m\right|.
$$

For a fixed partition, its population counterpart is

$$
\operatorname{ECE}_{\mathcal B}
=
\sum_m
\Pr(Q\in B_m)
\left|
\mathbb E[\eta(Q)-Q\mid Q\in B_m]
\right|.
$$

An unbinned absolute calibration error would instead be

$$
\operatorname{CE}_1
=
\mathbb E|\eta(Q)-Q|.
$$

These are different quantities.

By the triangle inequality for expectations,

$$
\left|\mathbb E[\eta(Q)-Q\mid B_m]\right|
\leq
\mathbb E[|\eta(Q)-Q|\mid B_m].
$$

Weighting and summing gives

$$
\boxed{
\operatorname{ECE}_{\mathcal B}
\leq
\operatorname{CE}_1.
}
$$

Opposing errors inside a bin can cancel.

### 9. Derive binning bias and sampling noise separately

Construct a forecast taking values $$1/4$$ and $$3/4$$ equally often, but let the true event frequency be $$1/2$$ at both forecast values.

The errors are

$$
\eta(1/4)-1/4=\frac14,
$$

and

$$
\eta(3/4)-3/4=-\frac14.
$$

With one bin containing both values,

$$
\operatorname{ECE}_{\mathcal B}
=
\left|\frac12\cdot\frac14+\frac12\cdot\left(-\frac14\right)\right|
=
0.
$$

With separate bins,

$$
\operatorname{ECE}_{\mathcal B}
=
\frac12\cdot\frac14+\frac12\cdot\frac14
=
\frac14.
$$

The forecast has not changed. Only the measurement procedure has changed.

Its Brier score still exposes the unsupported probabilities:

$$
\operatorname{BS}
=
\underbrace{\frac1{16}}_{\text{calibration penalty}}
+
\underbrace{\frac14}_{\text{refinement term}}
=
\frac5{16}.
$$

For nested partitions, refining population bins cannot increase cancellation: the weighted absolute value of a merged mean is no larger than the sum of the separate weighted absolute values.

Finite samples introduce another effect. Suppose calibration is perfect and patients are independent. Conditional on the forecasts in a bin, define

$$
D_m=\frac1{n_m}\sum_{i:Q_i\in B_m}(Y_i-Q_i).
$$

Then

$$
\mathbb E[D_m\mid Q_1,\ldots,Q_n]=0,
$$

but

$$
\operatorname{Var}(D_m\mid Q_1,\ldots,Q_n)
=
\frac1{n_m^2}
\sum_{i:Q_i\in B_m}Q_i(1-Q_i).
$$

Unless this variance vanishes, taking an absolute value produces a positive expected empirical discrepancy.

For an exact example, let every forecast equal $$1/2$$ and let outcomes be independent fair Bernoulli draws.

With one observation,

$$
\widehat{\operatorname{ECE}}
=
|Y-1/2|
=
\frac12
$$

regardless of the outcome.

With two observations in one bin, the observed event fraction is zero, one half, or one, with probabilities $$1/4$$, $$1/2$$, and $$1/4$$. Therefore,

$$
\mathbb E[\widehat{\operatorname{ECE}}]
=
\frac14\cdot\frac12
+
\frac12\cdot0
+
\frac14\cdot\frac12
=
\frac14.
$$

True calibration error is zero in both cases.

Coarser bins can conceal population errors; smaller bins increase sampling noise. The total bias relative to an unbinned target therefore has no universal direction. Equal-width bins, equal-count bins, and data-dependent partitions need not produce comparable estimates.

A calibration report should show the binning rule, counts, probability distribution, and uncertainty. A multiclass top-label ECE also answers a different question from calibration of every class probability.

### 10. What recalibration can and cannot change

For a binary logit $$z$$, temperature scaling produces

$$
Q_T=\frac1{1+\exp(-z/T)},
\qquad T>0.
$$

Division by a positive constant preserves the ordering of logits, and the logistic function is strictly increasing. Therefore binary ranking and AUROC are unchanged.

Also,

$$
Q_T\geq\frac12
\quad\Longleftrightarrow\quad
z/T\geq0
\quad\Longleftrightarrow\quad
z\geq0.
$$

The classification at probability threshold one half is unchanged.

A fitted temperature can change the numerical probability mapping. It cannot create missing clinical information, change an incorrect ranking, or guarantee calibration in a new population. Other recalibration methods may alter rankings, so this invariance should not be generalized to every method.

The recalibration parameters belong to development. Their performance must be assessed on independent outcomes.

### 11. Derive selective risk and coverage

Let $$a(X)\in[0,1]$$ be the probability of accepting an automated prediction. Values strictly between zero and one allow randomized selection, for example at a tied boundary.

Coverage is

$$
c=\mathbb E[a(X)].
$$

For a specified loss $$\ell(f(X),Y)$$ and $$c>0$$, selective risk is

$$
\boxed{
R_{\mathrm{sel}}
=
\frac{\mathbb E[a(X)\ell(f(X),Y)]}{c}.
}
$$

For deterministic acceptance, this is simply

$$
R_{\mathrm{sel}}
=
\mathbb E[\ell(f(X),Y)\mid a(X)=1].
$$

Define conditional risk

$$
r(X)=\mathbb E[\ell(f(X),Y)\mid X].
$$

By iterated expectation,

$$
\mathbb E[a(X)\ell(f(X),Y)]
=
\mathbb E[a(X)r(X)].
$$

Thus the best selection rule for a fixed predictor and fixed coverage accepts cases with the lowest conditional risk.

To see why, suppose a rule accepts a small mass of cases with risk $$r_{\mathrm{high}}$$ while rejecting the same mass with risk $$r_{\mathrm{low}}<r_{\mathrm{high}}$$. Exchanging them preserves coverage and reduces the numerator by

$$
\delta(r_{\mathrm{high}}-r_{\mathrm{low}})>0.
$$

A rule permitting such an exchange cannot be optimal.

### 12. Derive the optimal risk-coverage trade-off

Let $$q_r(u)$$ be the ascending quantile function of conditional risk. Accepting the lowest-risk fraction $$c$$ gives

$$
R^*(c)=\frac1c\int_0^c q_r(u)\,du,
$$

with randomization at ties when needed.

Where differentiable,

$$
\begin{aligned}
\frac{dR^*(c)}{dc}
&=
\frac{c\,q_r(c)-\int_0^c q_r(u)\,du}{c^2}\\
&=
\boxed{\frac{q_r(c)-R^*(c)}{c}}.
\end{aligned}
$$

Because $$q_r(c)$$ is at least the average risk among the cases already included,

$$
\frac{dR^*(c)}{dc}\geq0.
$$

This proves the monotone trade-off for correct risk ordering. It does not prove that every confidence score produces a monotone empirical or population curve.

Construct two equally common groups with model error probabilities $$1/10$$ and $$2/5$$. Full-coverage risk is

$$
\frac12\cdot\frac1{10}
+
\frac12\cdot\frac25
=
\frac14.
$$

At coverage one half:

- Accepting the easier group gives risk $$1/10$$.
- Accepting the harder group gives risk $$2/5$$.

Lower coverage can worsen retained risk if selection orders cases incorrectly. At zero coverage, selective risk is undefined.

For binary classification using the true posterior $$\eta(X)$$, the Bayes decision predicts the more probable class, with conditional error

$$
r(X)=\min\{\eta(X),1-\eta(X)\}.
$$

This follows because predicting one has error $$1-\eta(X)$$ and predicting zero has error $$\eta(X)$$. In this special case, confidence orders error correctly. An arbitrary neural-network confidence score need not have that property.

### 13. Rejected cases remain part of the clinical system

Suppose rejected cases receive human review with loss $$L_{\mathrm{review}}$$ and additional review cost $$k$$. Overall workflow loss is

$$
\mathbb E[
aL_{\mathrm{model}}
+
(1-a)(L_{\mathrm{review}}+k)
].
$$

Equivalently,

$$
cR_{\mathrm{accepted}}
+
(1-c)R_{\mathrm{reviewed}}
+
k(1-c),
$$

where both conditional risks refer to the populations routed to those branches.

Human review is not assumed perfect. Its difficulty may increase precisely because the model rejects the hardest cases.

Class-specific coverage also matters. For deterministic acceptance,

$$
\Pr(a=1,f=1\mid Y=1)
=
\Pr(a=1\mid Y=1)
\Pr(f=1\mid Y=1,a=1).
$$

High sensitivity among accepted positive patients can coexist with low coverage of positive patients. A retained-case metric alone hides that loss of assistance.

An evaluation should report risk and coverage together, alongside subgroup coverage, rejection reasons, workload, and the outcomes of the review pathway.

### 14. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| What is perfect calibration? | $$\mathbb E[Y\mid Q]=Q$$ almost surely |
| Can an uninformative forecast be calibrated? | Yes; the constant prevalence forecast is calibrated |
| Why is Brier loss proper? | Expected loss equals $$\eta(1-\eta)+(q-\eta)^2$$ |
| What does Brier score combine? | Calibration error and refinement; equivalently uncertainty minus resolution plus reliability error |
| What does log loss combine? | Conditional entropy and divergence from the true forecast-group frequency |
| Why does information availability matter? | Conditional variance decomposes into remaining uncertainty and information discarded |
| Why can ECE miss errors? | Opposing errors cancel within bins |
| Why can ECE be positive for a calibrated model? | Sampling noise survives the absolute value |
| When does abstention improve retained risk? | When selection usefully orders conditional loss |
| What is missing from a risk-coverage curve? | The consequences and costs of handling rejected cases |

Calibration, robustness, and clinical utility are distinct ontology properties. A selection method must be evaluated against the requirements of the clinical target, including what happens when automation is withheld.

## Why it matters for my work

For gallbladder models, evidence availability may help explain uncertainty more directly than confidence alone. I would examine whether rejection tracks incomplete views or clinically ambiguous findings, while separately testing whether confident predictions rely on acquisition shortcuts. Any resulting selection policy still needs independent validation.

## What I have not resolved

- Which evidence-availability annotations can support selection without introducing new subjectivity or leakage?
- How should the review pathway handle confident predictions with suspicious evidence reliance?
- Which patient groups lose assistance as coverage decreases?

---

Sources: Independent study; the scoring-rule decompositions, binning examples, and selection arguments are derived above. Numerical examples describe constructed probability models, not clinical performance. These are study notes for research purposes, not clinical guidance.
