---
layout: study_note
title: "Domain Adaptation, Domain Generalization, and Test-Time Adaptation"
description: "Three answers to the same problem of a model meeting data it was not trained on, and what each assumes."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "systems"
category_title: "Medical AI Systems & Deployment"
subgroup: "Adaptation Across Sites & Time"
order: 3
source: "Independent study"
written: true
updated: "2026-09-08"
---

Domain adaptation, domain generalization, and test-time adaptation differ primarily in what target information is available and when the system may change. Their names do not supply the assumptions connecting source evidence to target performance.

## Core question and definition

Let source and target distributions be

$$
P_s(X,Y),
\qquad
P_t(X,Y).
$$

For a fixed predictor,

$$
R_t(f)=\mathbb E_t[\ell(f(X),Y)]
$$

is target risk.

The central question is:

> Which data may the procedure use, which relationships are assumed stable, and what complete procedure is being evaluated?

A labeled target development set, an unlabeled target collection, and an incoming target batch define different information-access regimes.

These categories can overlap. A model trained for domain generalization can later undergo test-time adaptation. The combined procedure then needs evaluation under that combined access pattern.

## Key concepts

### 1. Separate the settings by permitted information

Write labeled source data as

$$
\mathcal D_s^L=\{(x_i^s,y_i^s)\},
$$

and unlabeled target data as

$$
\mathcal U_t=\{x_j^t\}.
$$

| Setting | Development information | Target information used for adaptation | What is evaluated |
|---|---|---|---|
| Unsupervised domain adaptation | Labeled source data and an unlabeled target collection | Target inputs available before final evaluation | The adapted predictor or declared transductive procedure |
| Domain generalization | Often several labeled source environments | No target collection during development or selection | Transfer to a previously unavailable target |
| Test-time adaptation | A pretrained model and a specified update rule | Incoming target inputs at inference time | A stateful or batch-dependent prediction procedure |
| Supervised target adaptation | Source knowledge and labeled target development cases | Target labels as well as inputs | A locally adapted model on independent target cases |

“Unsupervised” here refers to target-label access. Source labels can still be used.

Source-free adaptation is another access restriction: the procedure receives a source-trained model but not the original source records.

Target labels used to choose prompts, checkpoints, or hyperparameters still constitute target-label access even if they never appear in a gradient calculation.

### 2. Reconnect each method to the shift factorization

The joint distribution can be written as

$$
p(x,y)=p(x)p(y\mid x)=p(y)p(x\mid y).
$$

Under covariate shift,

$$
p_t(x,y)=p_t(x)p_s(y\mid x).
$$

Under label shift,

$$
p_t(x,y)=p_t(y)p_s(x\mid y).
$$

Under conditional or concept shift,

$$
p_t(y\mid x)\neq p_s(y\mid x)
$$

on a relevant region. A pure conditional shift keeps $$p_t(x)=p_s(x)$$.

The categories are not fully exclusive. Label shift generally changes posterior probabilities, while covariate shift can change overall prevalence.

The useful question is which conditional relationship remains invariant. A method needs that relationship, or another justified structure, to infer target behavior from unlabeled target inputs.

### 3. Derive what covariate-shift adaptation can identify

Assume

$$
p_t(y\mid x)=p_s(y\mid x)
$$

and target support is contained in source support, apart from null sets.

Define

$$
w(x)=\frac{p_t(x)}{p_s(x)}.
$$

Then

$$
\begin{aligned}
R_t(f)
&=\int\sum_y\ell(f(x),y)p_t(x)p_s(y\mid x)\,dx\\
&=\int\sum_y\ell(f(x),y)
\frac{p_t(x)}{p_s(x)}
p_s(x,y)\,dx\\
&=\boxed{\mathbb E_s[w(X)\ell(f(X),Y)]}.
\end{aligned}
$$

Unlabeled target inputs can help estimate the input-density ratio. Source labels supply outcomes conditional on those inputs.

The identity does not guarantee that estimated weights are accurate, optimization succeeds, or the adapted model improves. It establishes the quantity that weighting targets under the assumptions.

If a target region has no source support, weighting cannot create its missing outcomes. If the conditional relationship changes, input weighting leaves that change uncorrected.

### 4. Label shift requires a different correction

Let source and target prevalence be $$\pi_s$$ and $$\pi_t$$. Under stable class-conditional input distributions,

$$
\frac{p_t(x\mid Y=1)}{p_t(x\mid Y=0)}
=
\frac{p_s(x\mid Y=1)}{p_s(x\mid Y=0)}.
$$

Bayes' rule gives

$$
\frac{\eta_t(x)}{1-\eta_t(x)}
=
\frac{p_s(x\mid1)}{p_s(x\mid0)}
\frac{\pi_t}{1-\pi_t},
$$

and

$$
\frac{\eta_s(x)}{1-\eta_s(x)}
=
\frac{p_s(x\mid1)}{p_s(x\mid0)}
\frac{\pi_s}{1-\pi_s}.
$$

Dividing,

$$
\boxed{
\frac{\eta_t(x)}{1-\eta_t(x)}
=
\frac{\pi_t/(1-\pi_t)}{\pi_s/(1-\pi_s)}
\frac{\eta_s(x)}{1-\eta_s(x)}.
}
$$

The correction concerns prior odds. It is not generally achieved by making the target image distribution resemble the source.

Indeed, when disease prevalence changes, a clinically useful representation should often have a different marginal distribution because different disease states occur at different frequencies. Forcing identical representation marginals can oppose that legitimate change.

### 5. Matching feature distributions does not identify the target labels

Suppose an encoder is trained to make source and target features difficult to distinguish:

$$
P_s(\phi(X))\approx P_t(\phi(X)).
$$

This is a statement about feature marginals. Target prediction requires information about

$$
P_t(Y\mid\phi(X)).
$$

One does not determine the other.

Construct a source distribution:

| Input | Source label | Probability |
|---|---:|---|
| $$-1$$ | 0 | $$1/2$$ |
| $$1$$ | 1 | $$1/2$$ |

The source classifier predicts positive for input one.

Now consider two possible target worlds with exactly the same input distribution:

| Input | Target label in world A | Target label in world B |
|---|---:|---:|
| $$-1$$ | 0 | 1 |
| $$1$$ | 1 | 0 |

Source and target input marginals match perfectly in both worlds. The source classifier has target accuracy one in A and zero in B.

Unlabeled target observations cannot distinguish the worlds. Perfect domain confusion therefore does not establish correct target classification.

The construction violates conditional invariance in world B. That is precisely why an explicit shift assumption matters.

Compression adds another complication. Even if $$P(Y\mid X)$$ is stable, $$P(Y\mid\phi(X))$$ can change when the encoder merges inputs whose mixture changes across domains.

### 6. Domain generalization needs a family of target distributions

Domain generalization often uses several source environments:

$$
P_1,\ldots,P_K.
$$

Multiple environments can expose correlations that vary across sources. They do not prove that every remaining correlation will persist in an unseen target.

A simple positive result follows if the target is assumed to be a mixture of the source distributions:

$$
P_t=\sum_{k=1}^K\alpha_kP_k,
\qquad
\alpha_k\geq0,
\quad
\sum_k\alpha_k=1.
$$

Then, for a fixed predictor,

$$
\begin{aligned}
R_t(f)
&=\mathbb E_t[\ell]\\
&=\sum_k\alpha_k\mathbb E_k[\ell]\\
&=\sum_k\alpha_kR_k(f)\\
&\leq\boxed{\max_kR_k(f)}.
\end{aligned}
$$

This gives a reason to care about the worst source-domain risk under that particular target-family assumption.

Construct source risks

$$
R_1=\frac1{10},
\qquad
R_2=\frac3{10},
$$

and target mixture weights $$1/4$$ and $$3/4$$. Then

$$
R_t
=
\frac14\frac1{10}
+
\frac34\frac3{10}
=
\frac14,
$$

which is below the largest source risk $$3/10$$.

The guarantee concerns population risks and membership in the assumed mixture family. Estimated source risks have uncertainty, and a new acquisition or labeling relationship need not belong to that family.

### 7. Model selection is part of the domain-generalization claim

A domain-generalization experiment needs a selection procedure that does not use the target.

Possible development information includes:

- Held-out patients within source environments.
- Held-out source environments.
- Prespecified robustness objectives.
- Source-only validation of augmentation and regularization choices.

Choosing the best model after inspecting target accuracy changes the experiment. The final reported model has benefited from target information.

Similarly, evaluating many unseen sites and reporting only favorable ones changes the target population represented by the result.

The appropriate claim is about the complete training and selection procedure under its declared source and target access.

### 8. Define test-time adaptation as a state update

Let $$\theta_0$$ be the initial model state and $$B_t$$ the incoming unlabeled batch.

An update-before-prediction protocol is

$$
\theta_t=U(\theta_{t-1},B_t),
$$

$$
\widehat Y_{t,i}=f_{\theta_t}(X_{t,i}).
$$

A predict-then-update protocol instead uses

$$
\widehat Y_{t,i}=f_{\theta_{t-1}}(X_{t,i})
$$

before applying the update.

The distinction changes which information affects the current prediction.

The state can include more than weights:

- Normalization means and variances.
- Optimizer momentum.
- Pseudo-label memory.
- Adaptation buffers.
- Calibration parameters.
- A teacher model or running ensemble.

An episodic procedure resets to $$\theta_0$$ for each episode. A continual procedure carries state forward. These are different algorithms.

### 9. A single batch can change the answer for the same patient

Consider a scalar input and a batch-dependent normalization rule:

$$
z_i=x_i-\overline x_B,
$$

with a positive prediction when $$z_i>0$$.

The patient input is fixed at $$x=1$$.

| Batch containing the patient | Batch mean | Patient's normalized value | Prediction |
|---|---:|---:|---|
| $$[1,3]$$ | 2 | -1 | Negative |
| $$[-3,1]$$ | -1 | 2 | Positive |

The patient's input has not changed. The surrounding batch has.

This is a constructed normalization example, not a claim about a particular clinical model. It demonstrates why adapting statistics on a test batch changes the evaluated mapping from

$$
x\mapsto f(x)
$$

to something like

$$
(x,B)\mapsto f_B(x).
$$

No gradient update is required for this dependence.

If the intended deployment predicts one patient at a time, evaluation using a large curated batch may provide information and behavior unavailable in practice.

### 10. Derive why entropy minimization can reinforce a mistake

Entropy minimization is one test-time adaptation approach; Tent uses this signal while updating specified normalization-related components. [Tent: Fully Test-time Adaptation by Entropy Minimization](https://arxiv.org/abs/2006.10726).

For a binary probability $$q$$,

$$
H(q)=-q\log q-(1-q)\log(1-q).
$$

Differentiate:

$$
\begin{aligned}
\frac{dH}{dq}
&=-(\log q+1)+(\log(1-q)+1)\\
&=\log\frac{1-q}{q}.
\end{aligned}
$$

Let $$q=\sigma(a)$$, where $$a$$ is a logit. Then

$$
\frac{dq}{da}=q(1-q),
$$

and

$$
\log\frac{q}{1-q}=a.
$$

Therefore,

$$
\boxed{
\frac{dH}{da}=-a\,q(1-q).
}
$$

A gradient-descent step on this single free logit gives

$$
a'
=
a-\eta\frac{dH}{da}
=
\boxed{a+\eta a q(1-q)}.
$$

A positive logit becomes more positive; a negative logit becomes more negative. The update uses no outcome information.

In a network with shared parameters, updates interact across cases. This scalar calculation isolates why the entropy objective itself rewards confidence rather than correctness.

### 11. Carry the entropy example through

Construct an incorrect prediction with

$$
Y=0,
\qquad
q=\frac45,
\qquad
a=\log4.
$$

Choose a step size of one for the scalar example. Since

$$
q(1-q)=\frac45\frac15=\frac4{25},
$$

the updated logit is

$$
a'
=
\left(1+\frac4{25}\right)\log4
=
\frac{29}{25}\log4.
$$

Thus,

$$
q'
=
\frac{4^{29/25}}{1+4^{29/25}}
>
\frac45.
$$

Entropy decreases because $$q$$ moves farther above one half.

But the log loss for the true outcome zero is initially

$$
-\log(1-q)=\log5.
$$

After the update,

$$
-\log(1-q')
=
\log(1+4^{29/25})
>
\log5.
$$

The adaptation objective improves while the prediction becomes more confidently wrong.

This does not imply that entropy adaptation always fails. It shows that lower entropy alone cannot certify an improvement.

### 12. Derive order dependence in a running update

Consider a running mean

$$
m_t=(1-\lambda)m_{t-1}+\lambda x_t.
$$

After two inputs,

$$
m_2
=
(1-\lambda)^2m_0
+
\lambda(1-\lambda)x_1
+
\lambda x_2.
$$

Reversing the inputs gives

$$
m_2^{\mathrm{rev}}
=
(1-\lambda)^2m_0
+
\lambda(1-\lambda)x_2
+
\lambda x_1.
$$

Subtracting,

$$
\boxed{
m_2-m_2^{\mathrm{rev}}
=
\lambda^2(x_2-x_1).
}
$$

Construct $$m_0=0$$ and $$\lambda=1/2$$.

| Input order | First updated mean | Second updated mean |
|---|---:|---:|
| $$-2,2$$ | -1 | $$1/2$$ |
| $$2,-2$$ | 1 | $$-1/2$$ |

A later input zero, scored as $$x-m_2$$, receives opposite signs under the two histories.

Randomly shuffling a deployment stream can therefore change the adaptive model being tested. A sequence dominated by one clinical population may affect later cases even when those later inputs are identical.

### 13. The evaluation target is now a procedure over sequences

For a frozen model, risk is a function of one fixed predictor and a case distribution.

For adaptive inference, a more appropriate target is

$$
\boxed{
R_U
=
\mathbb E\left[
\frac1T\sum_{t=1}^T
\ell(f_{\theta_t}(X_t),Y_t)
\right],
}
$$

where the expectation includes the declared sequence or batch process and $$\theta_t$$ follows the update rule.

The risk depends on:

- Initial state.
- Case order and batch composition.
- Update-before or update-after prediction.
- Reset policy.
- Learning rates and updated components.
- Availability of source data.
- The duration and type of shift.

Using unlabeled evaluation inputs can be legitimate in a declared transductive or test-time adaptation experiment. It is not ordinary frozen-model external validation.

Losses can also become dependent because one patient's input changes another patient's predictor. A naive fixed-prediction bootstrap does not evaluate uncertainty in the complete adaptation procedure. Resampling should preserve or reconstruct the relevant episodes and updates.

If adaptation is completed on a separate target collection and the result is then frozen, independent future cases can again evaluate that fixed adapted model.

### 14. Negative transfer and harmful updates need explicit comparators

Define negative transfer relative to the same frozen source model:

$$
R_t(f_{\mathrm{adapted}})
>
R_t(f_{\mathrm{frozen}}).
$$

An adaptive method should therefore retain that comparator under the same target cases and information constraints.

For an online procedure, compare complete trajectories, including:

- Initial performance.
- Performance during adaptation.
- Retention after case-mix changes.
- Behavior after reset.
- Recovery after harmful updates.
- Calibration and subgroup effects.
- Computational and workflow costs.

When target labels are absent, a lower adaptation loss is only a proxy. The entropy example demonstrates why it cannot establish the sign of the true risk change.

Versioned states and a defined fallback make later outcomes attributable to the system that produced each prediction.

### 15. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| What separates adaptation, DG, and TTA? | Target-data access, timing, and whether state changes |
| What identifies target risk under covariate shift? | Conditional invariance plus support overlap and density weighting |
| What changes under label shift? | Prior odds and posterior probabilities despite fixed class-conditionals |
| Does feature matching establish class alignment? | No; the reversed-label construction has identical marginals |
| What can multiple source domains guarantee? | Only results conditional on a specified target family or other assumptions |
| Why does target-informed selection matter? | It changes the claimed unseen-domain protocol |
| Can one batch alter a patient's prediction? | Yes; adaptation can make output depend on other batch members |
| Why can entropy minimization worsen a prediction? | It rewards increased confidence without observing correctness |
| Why does order matter? | State updates generally assign different weights to earlier and later inputs |
| What should TTA evaluation estimate? | Performance of the complete update-and-predict procedure |
| What is negative transfer? | Worse target risk than the declared nonadapted comparator |

In the ontology, adaptation is a method whose claims are limited by support, identifiability, and shift assumptions. Target performance and clinical evidence reliance require reassessment after the model state changes.

## Why it matters for my work

For gallbladder ultrasound, I need to distinguish acquisition changes from changes in referral populations and reference standards. An adaptation method should be evaluated for both target prediction quality and whether its updated state continues to rely on assessable clinical evidence.

## What I have not resolved

- Which target changes satisfy an invariant relationship that adaptation can use?
- Which batch and sequence patterns resemble actual use?
- How can harmful updates be identified when verified outcomes arrive late?

---

Sources: Independent study; the entropy-adaptation example is connected to the verified Tent paper linked above. All numerical examples, counterexamples, and risk identities are constructed and derived here. These are study notes for research purposes, not clinical guidance.
