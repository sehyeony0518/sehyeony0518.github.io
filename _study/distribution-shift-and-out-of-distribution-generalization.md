---
layout: study_note
title: "Distribution Shift and Out-of-Distribution Generalization"
description: "What breaks when the hospital, scanner, operator, or population changes, and which failures are foreseeable."
og_image: "https://sehyeony0518.github.io/assets/img/og/distribution-shift-and-out-of-distribution-generalization.png"
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
subgroup: "Calibration & Generalization"
order: 11
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-10-02-zech-variable-generalization"
  - "2026-05-18-shortcut-learning-data-acquisition-bias"
  - "2026-08-30-monet-transparent-medical-image-ai"
---

A model is evaluated under one joint distribution of inputs and targets and used under another. Understanding transfer requires stating which parts of that distribution change, which relationships are assumed to remain stable, and whether the target conditions are represented at all.

## Core question and definition

Let

$$
P_s(X,Y)
$$

be the source distribution and

$$
P_t(X,Y)
$$

the target distribution. Subscripts denote source and target, not time indices.

For a fixed predictor $$f$$ and loss $$\ell$$, define

$$
R_s(f)=\mathbb E_s[\ell(f(X),Y)],
$$

and

$$
R_t(f)=\mathbb E_t[\ell(f(X),Y)].
$$

A source evaluation estimates $$R_s$$ under its sampling assumptions. The quantity needed for deployment is $$R_t$$.

The question is not simply whether the target is “different.” It is:

> Which assumptions connect the target risk to observations available from the source and target?

Without such a connection, a favorable source estimate does not identify target performance. Naming a model architecture or an external site does not supply the missing assumption.

## Key concepts

### 1. Start from the two factorizations of the joint distribution

For either domain,

$$
p(x,y)=p(x)p(y\mid x)
$$

and

$$
p(x,y)=p(y)p(x\mid y).
$$

Here $$p$$ can denote a probability mass function or density as appropriate.

These two factorizations lead to different shift assumptions.

| Shift assumption | What changes | What remains fixed |
|---|---|---|
| Covariate shift | $$p(x)$$ | $$p(y\mid x)$$ |
| Label shift | $$p(y)$$ | $$p(x\mid y)$$ |
| Conditional or concept shift | $$p(y\mid x)$$ | No marginal is fixed unless additionally specified |

Under covariate shift,

$$
p_t(x,y)=p_t(x)p_s(y\mid x).
$$

Under label shift,

$$
p_t(x,y)=p_t(y)p_s(x\mid y).
$$

Under conditional shift,

$$
p_t(x,y)=p_t(x)p_t(y\mid x),
$$

with

$$
p_t(y\mid x)\neq p_s(y\mid x)
$$

on a relevant set. A *pure* conditional shift additionally holds $$p_t(x)=p_s(x)$$.

These categories describe mathematical assumptions. “New scanner” and “new hospital” do not identify one of them.

### 2. The categories are not all mutually exclusive

Covariate shift can change prevalence:

$$
\Pr_t(Y=1)
=
\int p_s(Y=1\mid x)p_t(x)\,dx.
$$

Even though the conditional relationship is fixed, changing which inputs are common can change the average event rate.

Label shift generally changes the posterior $$p(y\mid x)$$, because Bayes' rule contains the prior:

$$
p(y\mid x)
=
\frac{p(x\mid y)p(y)}
{\sum_{y'}p(x\mid y')p(y')}.
$$

Thus label shift usually satisfies the broad definition of conditional change as well. Some uses of “concept shift” reserve the term for a narrower change in the underlying relationship; the convention must be stated.

The practical distinction is the invariant relationship being assumed. Covariate weighting needs stable $$p(y\mid x)$$. Prior correction needs stable $$p(x\mid y)$$. Observing a prevalence difference does not establish either one.

### 3. Clinical and acquisition processes can change several factors together

An image can be viewed schematically as the result of

$$
\text{disease and anatomy}
\longrightarrow
\text{physical signal}
\longrightarrow
\text{acquisition and reconstruction}
\longrightarrow
X.
$$

The recorded label may follow another process:

$$
\text{clinical state}
\longrightarrow
\text{investigation and follow-up}
\longrightarrow
\text{reference interpretation}
\longrightarrow
Y.
$$

Changing devices, operators, referral practices, or reference procedures can alter different parts of these processes simultaneously.

For example, a new service might receive a different range of disease severity and use different acquisition protocols. Calling this “covariate shift” would assume that the same observed input still has the same conditional outcome distribution. That assumption needs justification.

A change in recorded labels also need not mean disease biology changed. It may reflect a revised reference definition or ascertainment process. The statistical shift is real for the dataset, but its mechanism matters for any repair.

### 4. Derive importance weighting under covariate shift

Assume:

1. The conditional outcome distribution is invariant:

$$
p_t(y\mid x)=p_s(y\mid x).
$$

2. The target input distribution is absolutely continuous with respect to the source input distribution:

$$
p_t(x)>0\implies p_s(x)>0
$$

apart from sets of probability zero.

Define the importance weight

$$
w(x)=\frac{p_t(x)}{p_s(x)}.
$$

Then

$$
\begin{aligned}
R_t(f)
&=
\int\sum_y
\ell(f(x),y)p_t(x)p_t(y\mid x)\,dx\\
&=
\int\sum_y
\ell(f(x),y)p_t(x)p_s(y\mid x)\,dx\\
&=
\int\sum_y
\ell(f(x),y)
\frac{p_t(x)}{p_s(x)}
p_s(x)p_s(y\mid x)\,dx\\
&=
\boxed{\mathbb E_s[w(X)\ell(f(X),Y)]}.
\end{aligned}
$$

The same change of measure gives

$$
\mathbb E_s[w(X)]
=
\int \frac{p_t(x)}{p_s(x)}p_s(x)\,dx
=
1.
$$

Weighting works because the source supplies the correct conditional outcomes for every target-relevant input region. The weight changes how frequently those regions contribute.

It does not correct a changed conditional relationship.

### 5. A fully constructed covariate-shift example

Let the input take two values, $$a$$ and $$b$$. In both domains, set

$$
\Pr(Y=1\mid X=a)=\frac14,
$$

and

$$
\Pr(Y=1\mid X=b)=\frac34.
$$

Let the source and target input proportions be

| Input | Source probability | Target probability | Event probability in both |
|---|---|---|---|
| $$a$$ | $$3/4$$ | $$1/4$$ | $$1/4$$ |
| $$b$$ | $$1/4$$ | $$3/4$$ | $$3/4$$ |

Use a classifier that always predicts zero. Its zero-one loss is therefore $$Y$$.

Source risk is

$$
\begin{aligned}
R_s
&=\frac34\cdot\frac14+\frac14\cdot\frac34\\
&=\frac3{16}+\frac3{16}\\
&=\frac38.
\end{aligned}
$$

Target risk is

$$
\begin{aligned}
R_t
&=\frac14\cdot\frac14+\frac34\cdot\frac34\\
&=\frac1{16}+\frac9{16}\\
&=\frac58.
\end{aligned}
$$

The conditional relationship has not changed. The model performs worse because the more difficult input state becomes more common.

The weights are

$$
w(a)=\frac{1/4}{3/4}=\frac13,
$$

and

$$
w(b)=\frac{3/4}{1/4}=3.
$$

Construct an exact source sample of 16 cases:

- Twelve have input $$a$$, with three positive outcomes.
- Four have input $$b$$, with three positive outcomes.

The weighted source error is

$$
\frac{3(1/3)+3(3)}{16}
=
\frac{1+9}{16}
=
\frac58,
$$

matching target risk.

The total weight is

$$
12\left(\frac13\right)+4(3)=16.
$$

An exact target construction has four cases at $$a$$ with one positive and twelve at $$b$$ with nine positives, again giving $$10/16=5/8$$.

This example is not label shift. Among positive cases,

$$
\Pr_s(X=b\mid Y=1)=\frac36=\frac12,
$$

whereas

$$
\Pr_t(X=b\mid Y=1)=\frac9{10}.
$$

The class-conditional input distribution changed.

### 6. Support overlap is necessary, but finite-sample stability needs more

For a fixed predictor, known weights, and independent source evaluation cases,

$$
\widehat R_{\mathrm{IW}}
=
\frac1n\sum_{i=1}^n w(X_i)\ell(f(X_i),Y_i)
$$

is unbiased under the covariate-shift assumptions.

Writing $$L=\ell(f(X),Y)$$, its variance is

$$
\boxed{
\operatorname{Var}(\widehat R_{\mathrm{IW}})
=
\frac1n
\left[
\mathbb E_s[w(X)^2L^2]-R_t^2
\right].
}
$$

This follows from the variance of an average of independent copies of $$wL$$.

Even when every target region has positive source probability, rare source regions can receive large weights. The second moment may then be large or fail to be finite.

Support overlap therefore permits identification of target risk; it does not guarantee that the available finite sample estimates it precisely.

A self-normalized estimator is

$$
\widehat R_{\mathrm{SN}}
=
\frac{\sum_i w_iL_i}{\sum_i w_i}.
$$

Under suitable laws of large numbers, its numerator and denominator converge to $$R_t$$ and one after division by $$n$$, so the ratio is consistent. The finite-sample expectation of a ratio is not generally the ratio of expectations, so it is not generally unbiased.

Estimated weights add another source of error. Weight clipping can reduce variance, but changes the weighting identity and usually introduces bias. Neither operation removes the need to state what target population is being estimated.

### 7. Derive what weighting estimates when the conditional relationship changes

Define source and target conditional risks

$$
r_s(x)=\mathbb E_s[L\mid X=x],
$$

and

$$
r_t(x)=\mathbb E_t[L\mid X=x].
$$

With input-density weights and support overlap,

$$
\mathbb E_s[w(X)L]
=
\mathbb E_t[r_s(X)].
$$

Actual target risk is

$$
R_t=\mathbb E_t[r_t(X)].
$$

Subtracting gives

$$
\boxed{
R_t-\mathbb E_s[w(X)L]
=
\mathbb E_t[r_t(X)-r_s(X)].
}
$$

Input weighting corrects the input mixture. It leaves the conditional-risk mismatch untouched.

This is why a density-ratio estimate alone is insufficient evidence that performance has been transported successfully. The invariant conditional relationship is doing essential work.

### 8. Derive label-shift weighting and posterior correction

Under label shift,

$$
p_t(x\mid y)=p_s(x\mid y).
$$

Assume every class present in the target also has positive source probability. Define

$$
w(y)=\frac{p_t(y)}{p_s(y)}.
$$

Then

$$
\begin{aligned}
R_t
&=
\sum_y\int
\ell(f(x),y)p_t(y)p_s(x\mid y)\,dx\\
&=
\sum_y\int
\ell(f(x),y)
\frac{p_t(y)}{p_s(y)}
p_s(y)p_s(x\mid y)\,dx\\
&=
\boxed{\mathbb E_s[w(Y)L]}.
\end{aligned}
$$

For binary outcomes, write

$$
\pi_s=\Pr_s(Y=1),
\qquad
\pi_t=\Pr_t(Y=1),
$$

and

$$
\eta_s(x)=\Pr_s(Y=1\mid X=x).
$$

Bayes' rule gives source posterior odds

$$
\frac{\eta_s(x)}{1-\eta_s(x)}
=
\frac{p_s(x\mid Y=1)}{p_s(x\mid Y=0)}
\frac{\pi_s}{1-\pi_s}.
$$

The corresponding target odds are

$$
\frac{\eta_t(x)}{1-\eta_t(x)}
=
\frac{p_t(x\mid Y=1)}{p_t(x\mid Y=0)}
\frac{\pi_t}{1-\pi_t}.
$$

The likelihood ratios are equal under label shift. Dividing the two equations gives

$$
\frac{\eta_t(x)}{1-\eta_t(x)}
=
\alpha\frac{\eta_s(x)}{1-\eta_s(x)},
$$

where

$$
\alpha
=
\frac{\pi_t/(1-\pi_t)}{\pi_s/(1-\pi_s)}.
$$

Solving explicitly,

$$
\eta_t(1-\eta_s)
=
\alpha\eta_s(1-\eta_t),
$$

$$
\eta_t[1-\eta_s+\alpha\eta_s]
=
\alpha\eta_s,
$$

and hence

$$
\boxed{
\eta_t(x)
=
\frac{\alpha\eta_s(x)}
{1-\eta_s(x)+\alpha\eta_s(x)}.
}
$$

Equivalently, posterior log odds shift by the log prior-odds ratio.

### 9. A constructed prior-correction example

Set source prevalence to $$1/2$$ and target prevalence to $$1/5$$. Then

$$
\alpha
=
\frac{(1/5)/(4/5)}{(1/2)/(1/2)}
=
\frac14.
$$

For an input with source posterior $$3/4$$,

$$
\begin{aligned}
\eta_t
&=
\frac{(1/4)(3/4)}
{1-3/4+(1/4)(3/4)}\\
&=
\frac{3/16}{4/16+3/16}\\
&=\frac37.
\end{aligned}
$$

One compatible construction gives the input a probability of $$3/4$$ among positives and $$1/4$$ among negatives in both domains. Bayes' rule then produces the stated source and target posteriors.

For positive $$\alpha$$, the posterior correction is strictly increasing in the source posterior. It changes probability values while preserving ordering.

More generally, under label shift the distributions of any fixed score conditional on outcome remain fixed. Its ROC curve and AUROC therefore remain fixed. Precision and calibration can change because prevalence enters their definitions.

Applying the correction to an arbitrary model output requires care. The displayed formula uses the true source posterior. If a score is only calibrated in the source, analogous correction concerns risk conditional on that score, not necessarily the full posterior given every input feature.

### 10. When can target prevalence be inferred without target labels?

Suppose a fixed binary classifier has source sensitivity

$$
r=\Pr_s(g(X)=1\mid Y=1)
$$

and false-positive rate

$$
f=\Pr_s(g(X)=1\mid Y=0).
$$

Under label shift, these conditional rates remain the same in the target.

Let the observed fraction of positive predictions in the target be

$$
q=\Pr_t(g(X)=1).
$$

By total probability,

$$
\begin{aligned}
q
&=\pi_t r+(1-\pi_t)f\\
&=f+(r-f)\pi_t.
\end{aligned}
$$

If $$r\neq f$$,

$$
\boxed{
\pi_t=\frac{q-f}{r-f}.
}
$$

If $$r=f$$, this classifier's positive-prediction frequency contains no information about prevalence. If $$r-f$$ is small, estimation errors in $$q$$, $$r$$, or $$f$$ are amplified.

Failure of this summary does not prove that the full input distribution is uninformative. Another score or richer representation may distinguish the class-conditional mixtures.

For multiple classes, let

$$
C_{ij}=\Pr_s(g(X)=i\mid Y=j).
$$

The target predicted-class proportions satisfy

$$
q=C\pi_t.
$$

Recovering unrestricted interior class proportions from this linear summary requires identifiable columns; full column rank provides that condition. An uninformative or nearly singular matrix prevents unique or stable recovery.

The calculation assumes class-conditional invariance. Fitting the target prediction frequency does not independently verify that assumption.

### 11. Derive the failure when support does not overlap

Suppose a set of input conditions $$A$$ has

$$
P_s(X\in A)=0
$$

but

$$
P_t(X\in A)=\delta>0.
$$

Split target risk into

$$
R_t
=
\mathbb E_t[L\mathbf1\{X\notin A\}]
+
\mathbb E_t[L\mathbf1\{X\in A\}].
$$

If loss lies between zero and one, the second term can lie anywhere between zero and $$\delta$$.

Even if the contribution outside $$A$$ is identified,

$$
\boxed{
R_{\mathrm{shared}}
\leq R_t
\leq R_{\mathrm{shared}}+\delta.
}
$$

Source examples cannot determine outcomes in a region that the source never represents. A density ratio cannot assign a finite weight to absent observations and thereby create their labels.

Support is a population concept. It does not require identical pixel arrays in both datasets. In high-dimensional data, meaningful overlap must be reasoned about through acquisition, clinical conditions, and modeling assumptions; the absence of exact duplicate images is not evidence of support failure.

Nominal presence is also insufficient for precise estimation. A clinically important combination may occur so rarely that the available sample effectively provides little information about it.

### 12. A two-world argument for the limit of assumption-free OOD generalization

Construct a source distribution containing only input $$a$$ with outcome zero.

Let the target contain input $$b$$ with probability $$\delta$$ and input $$a$$ otherwise. Consider two possible target worlds:

- World 0: the outcome at $$b$$ is always zero.
- World 1: the outcome at $$b$$ is always one.

Both worlds have exactly the same source observations and the same unlabeled target input distribution.

Any learner using only that information must behave the same way at $$b$$ in both worlds. Suppose it predicts one there with probability $$q$$.

Its target error contribution from $$b$$ is

$$
\delta q
$$

in World 0 and

$$
\delta(1-q)
$$

in World 1.

Therefore,

$$
\begin{aligned}
\max\{\delta q,\delta(1-q)\}
&=\delta\max\{q,1-q\}\\
&\geq\boxed{\frac{\delta}{2}}.
\end{aligned}
$$

For a deterministic prediction, one world gives error contribution $$\delta$$.

More source observations cannot distinguish the worlds because they are identical on the source. Unlabeled target observations cannot distinguish them because their input distributions are identical.

Thus no method can guarantee arbitrarily small target error over unrestricted target relationships. Useful OOD guarantees require assumptions, target labels, restrictions on intended use, or some other information that rules out incompatible worlds.

### 13. Input familiarity cannot detect every harmful shift

Support failure is not the only problem. Consider a target with exactly the same input distribution as the source but a different conditional outcome relationship.

An input-only detector observes the same distribution in both domains. It cannot identify the changed labels from inputs alone.

Conversely, an unfamiliar input need not produce an incorrect prediction. A change in irrelevant background appearance may be easy to detect while leaving the target relationship intact.

Therefore:

- OOD detection estimates a notion of unfamiliarity.
- Error detection estimates whether predictions fail.
- Neither is automatically equivalent to the other.

An abstention policy based on unfamiliarity still needs evaluation of retained errors, coverage, and the consequences for rejected patients.

### 14. Calibration can fail even under covariate shift

If a model outputs the true source posterior,

$$
Q=\eta_s(X)=\Pr_s(Y=1\mid X),
$$

then covariate shift preserves that posterior pointwise:

$$
\eta_t(X)=\eta_s(X).
$$

By iterated expectation,

$$
\mathbb E_t[Y\mid Q]
=
\mathbb E_t[\eta_t(X)\mid Q]
=
Q.
$$

Such a model remains calibrated.

But source calibration alone is weaker than having the true posterior for every input. A forecast can merge distinct input groups whose frequencies later change.

For a separate constructed example, let

$$
\Pr(Y=1\mid a)=\frac14,
\qquad
\Pr(Y=1\mid b)=\frac34
$$

in both domains. In the source, let $$a$$ and $$b$$ be equally common. A constant forecast $$Q=1/2$$ is calibrated.

In the target, let their probabilities become $$1/4$$ and $$3/4$$. The target event rate is

$$
\frac14\cdot\frac14+\frac34\cdot\frac34
=
\frac58.
$$

The constant forecast remains $$1/2$$, so it is no longer calibrated.

The source calibration equality averaged over a particular mixture inside a forecast group. Covariate shift changed that mixture. A marginal calibration result is not a pointwise guarantee.

### 15. Detection, adaptation, and generalization use different information

| Task | Information or action | Claim requiring evaluation |
|---|---|---|
| Shift detection | Compare inputs or outputs with a reference distribution | Whether the monitored change is detected |
| OOD detection | Flag inputs outside a defined familiarity criterion | Whether the flag identifies the intended unfamiliar conditions |
| Adaptation | Use target information to modify the system | Performance after the specified adaptation procedure |
| Recalibration | Change the probability mapping | Probability accuracy in the evaluated target population |
| Domain generalization | Transfer without fitting to the target setting | Performance across the specified family of target conditions |

Using unlabeled target images for adaptation is different from using no target data. Using labeled target cases for tuning is different again. Final evaluation must remain separate from whichever adaptation is claimed.

A generalization method may optimize a worst-case objective such as

$$
\min_f\sup_{Q\in\mathcal U}
\mathbb E_Q[\ell(f(X),Y)].
$$

The uncertainty set $$\mathcal U$$ defines which distributions are protected against. If the actual target belongs to that set, its risk is bounded by the supremum by definition.

The substantive work is justifying the set. If the target lies outside it, the displayed objective supplies no corresponding guarantee. If the set contains every possible labeling relationship, the two-world argument prevents a useful universal low-error guarantee.

### 16. Design evaluation around the transfer being claimed

For medical imaging, record the factors that could change the measurement or target relationship:

- Referral population and disease spectrum.
- Devices, reconstruction, and acquisition settings.
- Operators and view-selection practices.
- Image completeness and quality.
- Reference definitions, verification, and follow-up.
- Clinical workflow and the point at which predictions are used.

A held-out hospital tests the changes present at that hospital. A temporal holdout tests the changes that occurred during that period. Neither establishes performance under every absent combination.

Report discrimination, calibration, and the deployed operating point separately. Stable AUROC can coexist with changed predictive values under label shift. Stable average performance can conceal subgroup deterioration or a change in supporting evidence.

Clinical evidence annotations also have their own measurement process. If an audit changes across sites, possible explanations include changed model reliance, changed clinical composition, and changed annotation reliability. These should be investigated separately.

### 17. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| What defines covariate shift? | Changed $$p(x)$$ with invariant $$p(y\mid x)$$ |
| What defines label shift? | Changed $$p(y)$$ with invariant $$p(x\mid y)$$ |
| Why are the categories not fully exclusive? | Prior change generally changes the posterior; input mixture change can alter prevalence |
| Why does importance weighting work? | Change of measure plus an invariant conditional outcome distribution |
| What does support overlap provide? | Source information for every target-relevant region |
| Why can weighting still be unstable? | Large weights enlarge the second moment and estimation variance |
| How are posterior odds corrected under label shift? | Multiply by the target-to-source prior-odds ratio |
| When is target prevalence identifiable from prediction counts? | When the invariant classifier confusion summary distinguishes classes |
| Why is unrestricted OOD prediction impossible? | Indistinguishable observed data can correspond to incompatible target labels |
| Does source calibration guarantee target calibration? | No; it can depend on the mixture within forecast groups |
| Does unfamiliarity imply error? | No; input shift and prediction failure are different properties |
| What does external validation establish? | Performance under the particular transfer and information-access scheme evaluated |

In the ontology, transportability requires a defensible connection between source and target. Distribution shift warrants reassessment of robustness, calibration, and clinical evidence reliance. Support and identifiability limit which claims weighting or adaptation can establish.

## Why it matters for my work

For gallbladder ultrasound AI, I would define transfer questions around particular changes in acquisition, operators, and referral services. Evaluating predictions and clinical evidence reliance together can reveal whether a stable headline metric hides a change in what the model uses. The audit must also test whether clinical factors remain comparably assessable.

## What I have not resolved

- Which acquisition changes can be represented credibly by simulation, and which require actual target examinations?
- How can an audit distinguish changed evidence reliance from changed annotation reliability?
- Which combinations of clinical findings and acquisition conditions remain outside the available support?

---

Sources: Independent study; the change-of-measure identities, prior correction, calibration example, and impossibility construction are derived above. Numerical examples are explicitly constructed distributions, not empirical transfer results. These are study notes for research purposes, not clinical guidance.
