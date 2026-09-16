---
layout: study_note
title: "Label Quality and Interobserver Variability"
description: "Evaluating against labels that expert readers themselves disagree about."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
subgroup: "Task Definition & Ground Truth"
order: 4
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-10-15-kellgren-lawrence-classification"
  - "2025-09-12-oarsi-atlas-radiographic-features"
  - "2025-12-19-eyepacs-grading-protocol"
---

An annotation is a judgment made under a definition, an information set, and a reading procedure. Agreement measures reproducibility under those conditions. It does not establish that the shared judgment is clinically correct.

## Core question and definition

The central question is:

> What does disagreement tell me about the target, the available evidence, and the reference used to train or evaluate a model?

Disagreement can arise because readers:

- Apply different definitions.
- See different images or clinical information.
- Choose different measurement locations.
- Interpret a borderline finding differently.
- Cannot assess the relevant feature.
- Make avoidable mistakes.
- Share or differ in systematic biases.

These mechanisms require different responses. A clearer annotation guide can address a definitional mismatch. It cannot reveal anatomy missing from the supplied image.

I distinguish:

1. **Validity:** whether the label represents the intended target.
2. **Interobserver agreement:** reproducibility across readers.
3. **Intraobserver agreement:** reproducibility across repeated readings by the same reader.
4. **Assessability:** whether the supplied evidence permits the requested judgment.

## Key concepts

### 1. Start with the complete reader table

For two readers assigning a binary category, use the following counts:

| | Reader B positive | Reader B negative | Total |
|---|---:|---:|---:|
| Reader A positive | $$a$$ | $$b$$ | $$a+b$$ |
| Reader A negative | $$c$$ | $$d$$ | $$c+d$$ |
| Total | $$a+c$$ | $$b+d$$ | $$n$$ |

Observed agreement is

$$
p_o=\frac{a+d}{n}.
$$

The positive-label frequencies are

$$
p_A=\frac{a+b}{n},
\qquad
p_B=\frac{a+c}{n}.
$$

These marginals describe the readers' use of categories. They are not independently established disease prevalence.

Raw agreement alone does not reveal whether agreement is mostly on positives or negatives. The full table preserves that distinction.

### 2. Derive Cohen's kappa from its reference agreement

Construct a reference calculation in which the readers' labels are paired independently while preserving their marginal category frequencies.

Under that calculation, the probability of both labels being positive is

$$
p_Ap_B.
$$

The probability of both being negative is

$$
(1-p_A)(1-p_B).
$$

Expected agreement under this independence reference is therefore

$$
p_e=p_Ap_B+(1-p_A)(1-p_B).
$$

The observed agreement beyond that reference is

$$
p_o-p_e.
$$

The maximum possible increase from the reference to perfect agreement is

$$
1-p_e.
$$

Normalizing the first quantity by the second defines Cohen's kappa:

$$
\boxed{
\kappa=\frac{p_o-p_e}{1-p_e}.
}
$$

Equivalently,

$$
\begin{aligned}
\kappa
&=\frac{(1-p_e)-(1-p_o)}{1-p_e}\\
&=\boxed{1-\frac{1-p_o}{1-p_e}}.
\end{aligned}
$$

Kappa compares observed disagreement with disagreement under its marginal-independence reference.

This construction does not establish how often either reader actually guesses. “Chance-corrected agreement” refers to the specified mathematical reference, not an observed mental process.

### 3. Interpret the boundary cases carefully

When $$p_e<1$$:

- Perfect agreement gives $$\kappa=1$$.
- Agreement equal to the independence reference gives $$\kappa=0$$.
- Agreement below that reference gives negative kappa.

If both readers assign the same single category to every case, then

$$
p_o=p_e=1.
$$

Kappa becomes

$$
\frac00,
$$

so it is undefined.

Raw agreement is perfect, but the sample provides no information about whether the readers can distinguish the absent category. An undefined kappa should not be silently converted into proof of excellent clinical annotation.

Likewise, no universal verbal category for a kappa value establishes that a finding is reliable enough for a particular clinical or research use.

### 4. Construct high agreement with low kappa

Consider 100 cases:

| | B positive | B negative | Total |
|---|---:|---:|---:|
| A positive | 1 | 4 | 5 |
| A negative | 4 | 91 | 95 |
| Total | 5 | 95 | 100 |

Observed agreement is

$$
p_o=\frac{1+91}{100}=\frac{23}{25}.
$$

Each reader labels only $$1/20$$ of cases positive. Therefore,

$$
\begin{aligned}
p_e
&=\left(\frac1{20}\right)^2+\left(\frac{19}{20}\right)^2\\
&=\frac{1+361}{400}\\
&=\frac{181}{200}.
\end{aligned}
$$

Since

$$
p_o=\frac{184}{200},
$$

kappa is

$$
\begin{aligned}
\kappa
&=\frac{184/200-181/200}{1-181/200}\\
&=\frac{3/200}{19/200}\\
&=\boxed{\frac3{19}}.
\end{aligned}
$$

The readers agree on 92 of 100 cases, yet kappa is low because its reference agreement is already high when both readers rarely use the positive category.

This is not a contradiction. The metrics answer different questions.

### 5. Keep raw agreement fixed and change the marginals

Now construct another 100-case table:

| | B positive | B negative | Total |
|---|---:|---:|---:|
| A positive | 46 | 4 | 50 |
| A negative | 4 | 46 | 50 |
| Total | 50 | 50 | 100 |

Observed agreement remains

$$
p_o=\frac{92}{100}=\frac{23}{25}.
$$

But now

$$
p_e=\left(\frac12\right)^2+\left(\frac12\right)^2=\frac12.
$$

Therefore,

$$
\kappa
=
\frac{23/25-1/2}{1/2}
=
\boxed{\frac{21}{25}}.
$$

| Construction | Raw agreement | Each reader's positive frequency | Kappa |
|---|---|---|---|
| Mostly negative labels | $$23/25$$ | $$1/20$$ | $$3/19$$ |
| Balanced labels | $$23/25$$ | $$1/2$$ | $$21/25$$ |

The number of disagreements is identical. Their context within the category frequencies differs.

This is the central prevalence-related paradox: a high raw agreement can coexist with low kappa when one category dominates. The relevant “prevalence” here is the marginal frequency of assigned categories; without a separate reference, it should not be equated automatically with true disease prevalence.

### 6. Derive kappa's dependence on marginal imbalance

Expand the expected disagreement:

$$
\begin{aligned}
1-p_e
&=1-[p_Ap_B+(1-p_A)(1-p_B)]\\
&=p_A+p_B-2p_Ap_B.
\end{aligned}
$$

Let

$$
m=\frac{p_A+p_B}{2},
\qquad
\delta=\frac{p_A-p_B}{2}.
$$

Then

$$
p_A=m+\delta,
\qquad
p_B=m-\delta,
$$

and

$$
p_Ap_B=m^2-\delta^2.
$$

Substitution gives

$$
\begin{aligned}
1-p_e
&=2m-2(m^2-\delta^2)\\
&=\boxed{2m(1-m)+2\delta^2}.
\end{aligned}
$$

Let observed disagreement be

$$
q=\frac{b+c}{n}=1-p_o.
$$

Then

$$
\boxed{
\kappa
=
1-\frac{q}{2m(1-m)+2\delta^2}.
}
$$

This equation displays two effects:

- With equal reader marginals, moving the common positive rate toward zero or one reduces the denominator.
- At fixed average positive rate and observed disagreement, increasing the difference between reader marginals increases the denominator and can increase kappa.

The feasible values are constrained by the contingency table. In particular, the difference between positive-label frequencies cannot exceed total disagreement.

### 7. Construct the marginal-bias paradox

Compare these two 100-case tables:

| Construction | $$a$$ | $$b$$ | $$c$$ | $$d$$ | $$p_A$$ | $$p_B$$ |
|---|---:|---:|---:|---:|---|---|
| Equal marginals | 40 | 10 | 10 | 40 | $$1/2$$ | $$1/2$$ |
| Different marginals | 40 | 20 | 0 | 40 | $$3/5$$ | $$2/5$$ |

Both have observed agreement

$$
p_o=\frac45,
$$

and the same average positive-label frequency.

For equal marginals,

$$
p_e=\frac12,
$$

so

$$
\kappa=\frac{4/5-1/2}{1/2}=\frac35.
$$

For different marginals,

$$
p_e
=
\frac35\frac25+\frac25\frac35
=
\frac{12}{25},
$$

so

$$
\begin{aligned}
\kappa
&=\frac{4/5-12/25}{1-12/25}\\
&=\frac{8/25}{13/25}\\
&=\boxed{\frac8{13}}.
\end{aligned}
$$

The second table has a larger kappa even though all disagreements point in one direction: A labels positive where B labels negative.

This does not establish which reader is clinically biased. Without a disease reference, the table describes a difference in category use. It shows why a higher kappa alone does not establish a better annotation process.

### 8. Report category-specific agreement alongside kappa

The first high-agreement example contains only one jointly positive case. Its overall agreement is dominated by jointly negative cases.

Symmetric positive agreement can be defined as

$$
A_+
=
\frac{2a}{2a+b+c}.
$$

The denominator counts all positive labels contributed by either reader. Jointly positive cases contribute two agreeing positive labels.

Likewise, negative agreement is

$$
A_-
=
\frac{2d}{2d+b+c}.
$$

For the mostly negative table,

$$
A_+
=
\frac{2}{2+4+4}
=
\frac15,
$$

whereas

$$
A_-
=
\frac{182}{182+4+4}
=
\frac{91}{95}.
$$

These quantities make the imbalance visible. They are agreement measures, not sensitivity and specificity against disease, because neither reader has been declared correct.

A useful report includes the complete table, raw agreement, marginals, kappa, and uncertainty. The intended clinical use determines which disagreements are consequential.

### 9. Derive a label-noise ceiling under explicit assumptions

Let $$D$$ be the true binary target and $$R$$ a recorded label. Suppose the reference independently flips the true target with probability

$$
0\leq\varepsilon<\frac12.
$$

Let

$$
\eta(x)=\Pr(D=1\mid X=x).
$$

Then

$$
\begin{aligned}
\Pr(R=1\mid X=x)
&=\Pr(R=1\mid D=1,X=x)\eta(x)\\
&\quad+\Pr(R=1\mid D=0,X=x)[1-\eta(x)]\\
&=(1-\varepsilon)\eta(x)+\varepsilon[1-\eta(x)]\\
&=\boxed{\varepsilon+(1-2\varepsilon)\eta(x)}.
\end{aligned}
$$

For a binary label with probability $$q(x)$$ of being one, predicting zero has error $$q(x)$$ and predicting one has error $$1-q(x)$$. The best conditional error is therefore

$$
\min\{q(x),1-q(x)\}.
$$

Because $$1-2\varepsilon>0$$,

$$
\min\{q(x),1-q(x)\}
=
\varepsilon+(1-2\varepsilon)\min\{\eta(x),1-\eta(x)\}.
$$

Average over inputs. If $$R_D^*$$ is the smallest achievable disease-classification error using $$X$$, then the smallest error against a fresh noisy reference is

$$
\boxed{
R_R^*
=
\varepsilon+(1-2\varepsilon)R_D^*.
}
$$

In accuracy form,

$$
\boxed{
A_R^*
=
\varepsilon+(1-2\varepsilon)A_D^*.
}
$$

If disease is fully determined by the available inputs, $$A_D^*=1$$, giving

$$
A_R^*=1-\varepsilon.
$$

Even a perfect disease predictor cannot predict independent random errors in a fresh reference.

### 10. Human-human agreement is not the model's performance ceiling

Construct a setting where disease is fully recoverable from the model's inputs. Two readers independently flip the true label with probability $$1/10$$.

They agree when both are correct or both are wrong:

$$
\begin{aligned}
\Pr(R_1=R_2)
&=\left(\frac9{10}\right)^2+\left(\frac1{10}\right)^2\\
&=\frac{81+1}{100}\\
&=\frac{41}{50}.
\end{aligned}
$$

A model that predicts the true disease state agrees with either reader with probability

$$
\frac9{10}.
$$

Thus model-reader agreement can exceed reader-reader agreement:

$$
\frac9{10}>\frac{41}{50}.
$$

The relevant ceiling depends on the target reference, the available information, and the noise mechanism. It is not obtained by copying a human agreement statistic.

The ceiling derived above also does not apply unchanged when:

- Reference errors are predictable from the image.
- The model receives reader-specific information.
- The reference aggregates more information than the individual reader.
- Training and evaluation share memorized cases.
- Labels are revised through model-informed adjudication.

Observed interobserver disagreement alone does not identify $$\varepsilon$$.

### 11. Asymmetric noise can change the learned decision boundary

Let

$$
\alpha=\Pr(R=1\mid D=0)
$$

be the reference false-positive probability and

$$
\beta=\Pr(R=0\mid D=1)
$$

its false-negative probability. Assume these probabilities do not otherwise depend on $$X$$.

Then

$$
\begin{aligned}
q(x)
&=\Pr(R=1\mid X=x)\\
&=(1-\beta)\eta(x)+\alpha[1-\eta(x)]\\
&=\boxed{\alpha+(1-\alpha-\beta)\eta(x)}.
\end{aligned}
$$

When $$\alpha+\beta<1$$, a classifier optimized for reference-label accuracy predicts positive if

$$
q(x)\geq\frac12,
$$

which is equivalent to

$$
\boxed{
\eta(x)\geq
\frac{1/2-\alpha}{1-\alpha-\beta}.
}
$$

This need not be the disease-accuracy threshold $$1/2$$.

For squared probability loss, conditioning on the input gives

$$
\mathbb E[(R-p)^2\mid X]
=
q(X)[1-q(X)]+[p-q(X)]^2.
$$

Its optimum is $$p=q(X)$$. Training faithfully on noisy labels can therefore learn the reference process rather than the intended disease probability.

Correcting this relationship requires information about the noise process. An agreement table alone generally does not identify the required disease-error probabilities.

### 12. Consensus and soft labels change the target

Adjudication can resolve overlooked evidence or inconsistent definitions. It can also suppress an informative minority interpretation.

Preserve:

- Independent initial readings.
- Information available to each reader.
- Confidence and assessability.
- The disagreement being resolved.
- The reason for the final decision.

If three readers assign labels positive, positive, and negative, the fraction

$$
\frac23
$$

describes those votes. It is not automatically the probability that the patient has disease.

A model trained on vote fractions may learn the distribution of reader judgments under that protocol. That can be a useful target, but it differs from predicting pathology or future outcomes.

“Not assessable” should also remain distinct from negative. If the relevant interface is obscured, forcing a morphology label mixes absence of evidence with evidence of absence.

### 13. Continuous measurements require agreement, not just correlation

Suppose one reader measures

$$
A=(1,2,3)
$$

in arbitrary units and another measures

$$
B=(3,4,5)=A+2.
$$

The measurements are perfectly linearly associated, but differ by two units in every case.

More generally, if $$B=A+c$$ and $$\operatorname{Var}(A)>0$$,

$$
\operatorname{Cov}(A,B)=\operatorname{Var}(A),
$$

and

$$
\operatorname{Var}(B)=\operatorname{Var}(A).
$$

Therefore,

$$
\operatorname{Corr}(A,B)=1.
$$

The paired differences are nevertheless

$$
B-A=c.
$$

A measurement comparison should inspect the mean difference, variation of differences, and whether differences change with measurement size.

For segmentation, a high overlap score can similarly conceal a disagreement at a small but clinically important boundary. The metric must reflect the feature's use, not merely its geometric size.

### 14. Design the reading study around the uncertainty of interest

A reproducibility study should specify:

- The exact annotation question.
- The unit: patient, lesion, examination, or frame.
- Which views and clinical context readers receive.
- Whether readers see diagnosis or model output.
- How indeterminate and unassessable cases are recorded.
- How cases and readers were sampled.
- Which cases receive repeated readings.
- How adjudication is performed.

Repeated images from a patient do not create independent evidence about agreement. Likewise, a study of a fixed small reader panel does not automatically estimate variability across all future readers.

Initial clinical assessment should be independent of model explanations where feasible. Otherwise an explanation can shape the annotation later treated as independent evidence that the explanation is correct.

### 15. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| What does raw agreement measure? | The fraction of matching labels |
| Where does kappa's expected agreement come from? | Independent pairing of labels with the observed marginals |
| Why can high agreement produce low kappa? | Dominant category frequencies make the reference agreement high |
| Why can marginal imbalance increase kappa? | It changes the expected-disagreement denominator |
| Does kappa identify clinical correctness? | No; it compares readers without establishing truth |
| What is a label-noise ceiling? | A bound conditional on a specified noise process and available information |
| Is human-human agreement a universal model ceiling? | No; the independent-reader construction disproves that claim |
| What does asymmetric noise change? | The learned probability and potentially the decision boundary |
| Are vote fractions disease probabilities? | Only with additional justification connecting reader judgments to disease |
| Why inspect measurement differences? | Perfect correlation can coexist with systematic disagreement |

In the ontology, clinical assessability limits how strongly an annotation can support a claim about clinical evidence reliance. Label agreement supports reproducibility; reference validity and clinical meaning require additional evidence.

## Why it matters for my work

Gallbladder finding annotations are part of the measurement apparatus of a faithfulness audit. I need to establish which features readers can assess consistently before treating disagreement with those features as evidence of inappropriate model reliance.

## What I have not resolved

- Which disagreements are reducible through clearer definitions, and which arise from missing image evidence?
- How should reader uncertainty be represented separately from disease probability?
- What reliability is sufficient for a feature to support the intended audit claim?

---

Sources: Independent study; the agreement statistics, marginal effects, noise bounds, and numerical examples are derived explicitly above. Constructed reader tables are not empirical estimates of clinical agreement. These are study notes for research purposes, not clinical guidance.
