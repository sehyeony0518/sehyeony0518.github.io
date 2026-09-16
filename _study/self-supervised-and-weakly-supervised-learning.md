---
layout: study_note
title: "Self-Supervised and Weakly Supervised Learning"
description: "Learning from medical data whose labels are scarce, noisy, or only available at the study level."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Learning Models & Representation"
subgroup: "Learning & Representation Foundations"
order: 4
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-03-01-canet-cross-disease-attention"
  - "2026-08-30-monet-transparent-medical-image-ai"
---

Self-supervised learning constructs targets from the data. Weakly supervised learning uses external supervision that is incomplete, coarse, or unreliable relative to the intended task.

Neither removes the need to define what a correct training response means. A masked-pixel target supervises a prediction of hidden content. A contrastive target supervises identification of a related view. An examination label supervises an examination-level response. None of these automatically supplies a correct lesion label for every frame.

The useful starting question is therefore: **what random variable is the model actually being trained to predict?**

## Separating the observed data, the training target, and the intended task

Let an observation be a random variable and let the eventual task label be another:

$$
X,
\qquad
Y.
$$

A self-supervised procedure constructs a visible input and a target using a random transformation or sampling decision:

$$
V=a(X,A),
\qquad
T=b(X,A).
$$

An encoder and a prediction head are trained through

$$
h=f_\theta(V),
\qquad
\hat T=q_\phi(h),
$$

$$
\min_{\theta,\phi}
\mathbb E\left[
\ell\bigl(q_\phi(f_\theta(V)),T\bigr)
\right].
$$

The supervised variable in this objective is the constructed target. The desired downstream label need not appear anywhere in the loss.

For masked prediction, the target is hidden content. For transformation prediction, it is a selected transformation. For contrastive learning, it is the index of a related candidate. Calling these tasks self-supervised describes where the target comes from, not the absence of supervision.

The visible input must not trivially contain the answer. If a reconstruction target remains available through a skip connection or unmasked channel, a system can solve the objective by copying. The resulting loss would provide little reason for the encoder to learn the intended structure.

Transfer requires an additional relationship: distinctions useful for predicting the constructed target must also help predict the downstream label. That is an assumption to investigate. It is not a consequence of using more unlabeled observations.

## What squared-error reconstruction actually supervises

Suppose a masked scalar target is predicted from the visible input. For a fixed visible value, the conditional risk of predicting a number is

$$
R(a\mid v)
=
\mathbb E[(T-a)^2\mid V=v].
$$

Let the conditional target mean be

$$
\mu(v)=\mathbb E[T\mid V=v].
$$

Add and subtract this mean inside the square:

$$
T-a=(T-\mu)+(\mu-a).
$$

After expansion,

$$
R(a\mid v)
=
\mathbb E[(T-\mu)^2\mid v]
+
2(\mu-a)\mathbb E[T-\mu\mid v]
+
(\mu-a)^2.
$$

The middle term vanishes because the conditional deviation has mean zero. Hence,

$$
R(a\mid v)
=
\operatorname{Var}(T\mid V=v)
+
(\mu(v)-a)^2.
$$

The minimum occurs at

$$
\boxed{
a^\ast(v)=\mathbb E[T\mid V=v]
}.
$$

Squared-error reconstruction therefore rewards the conditional mean of the missing content. It does not necessarily reward one plausible complete realization.

For a constructed example, suppose the visible input gives no information about a masked bit, which is equally likely to be zero or one. Predicting one half gives risk

$$
\frac12(0-0.5)^2+\frac12(1-0.5)^2
=
0.25.
$$

Predicting zero gives

$$
\frac12(0-0)^2+\frac12(1-0)^2
=
0.5.
$$

The optimal prediction is an average even though that average is never the actual target. This explains how an optimal squared-error prediction can smooth over uncertainty.

For an image, an unweighted pixel loss also gives each predicted pixel an equal place in the sum. A large region can contribute more total error than a small region because it contains more terms. Whether this weighting serves a diagnostic task is a separate design question.

The example does not show that reconstruction is useless. It shows exactly what its optimum means. Reconstruction quality and diagnostic information are different quantities, and the connection between them must be checked downstream.

## Constructing the contrastive prediction problem

A contrastive procedure forms related views of one source observation:

$$
v_i^{(1)}=t_i^{(1)}(x_i),
\qquad
v_i^{(2)}=t_i^{(2)}(x_i).
$$

An encoder produces representations, optionally followed by a projection head:

$$
h_i=f_\theta(v_i),
\qquad
z_i=g_\phi(h_i).
$$

A normalized embedding is

$$
u_i=\frac{z_i}{\lVert z_i\rVert_2},
$$

assuming the vector is nonzero. Dot products between these unit vectors are cosine similarities. Normalization removes the possibility of increasing a dot product solely by increasing both vector magnitudes.

In the two-view batch construction used by [SimCLR](https://proceedings.mlr.press/v119/chen20j.html), each anchor's other view is its positive. Views of other source observations serve as negatives. The anchor itself is excluded from its candidate set.

This target means “identify the paired view.” It does not mean “identify another image with the same diagnosis.” Another patient with the same diagnosis can be a negative under this construction.

The augmentation distribution consequently defines an invariance assumption. If two transformations are treated as interchangeable, the objective rewards preserving what helps identify their shared source and discounting some differences between them.

That does not establish that every discarded difference is clinically irrelevant. A crop can remove the structure the downstream task needs, while shared acquisition markings can remain available in both views. The model is rewarded for solving the constructed matching problem by whatever accessible distinctions achieve it.

## Deriving InfoNCE as classification over candidates

Take one anchor and a set of candidate embeddings:

$$
q,
\qquad
k_1,\ldots,k_N.
$$

Exactly one candidate index is designated positive:

$$
J\in\{1,\ldots,N\}.
$$

Define compatibility scores and logits:

$$
s_j=\operatorname{sim}(q,k_j),
\qquad
a_j=\frac{s_j}{\tau},
\qquad
\tau>0.
$$

We need a probability distribution over the candidate index. Exponentiation gives positive weights, and division by their sum normalizes them:

$$
\pi_j
=
P_\theta(J=j\mid q,k_{1:N})
=
\frac{\exp(a_j)}
{\sum_{r=1}^{N}\exp(a_r)}.
$$

The negative log-likelihood of the known positive index is

$$
\ell
=
-\log\pi_J.
$$

Substituting the softmax gives the InfoNCE form:

$$
\boxed{
\ell
=
-\log
\frac{\exp(s_J/\tau)}
{\sum_{r=1}^{N}\exp(s_r/\tau)}
}.
$$

Equivalently,

$$
\ell
=
-\frac{s_J}{\tau}
+
\log\sum_{r=1}^{N}\exp(s_r/\tau).
$$

The positive belongs in the denominator because it is one possible outcome of the classification problem. Omitting it would no longer produce the negative logarithm of this normalized candidate probability.

Differentiate with respect to a logit:

$$
\frac{\partial\ell}{\partial a_j}
=
-\mathbf1[j=J]
+
\frac{\exp(a_j)}{\sum_r\exp(a_r)}.
$$

Therefore,

$$
\boxed{
\frac{\partial\ell}{\partial s_j}
=
\frac{\pi_j-\mathbf1[j=J]}{\tau}
}.
$$

The positive receives a negative score derivative, so gradient descent tends to increase its compatibility. Negatives receive positive score derivatives, so their compatibility tends to decrease. A negative already assigned negligible probability receives little pressure.

These are derivatives with respect to scores. The embedding and encoder gradients also include the derivatives of the similarity function and normalization. Scores cannot necessarily move independently when constrained embeddings share parameters.

## Why the negative distribution changes the learned distinction

The classification interpretation can be derived from a sampling model. Suppose the positive index is selected uniformly. Conditional on the anchor, that candidate is drawn from a related-view distribution, while the remaining candidates are drawn independently from a reference distribution:

$$
k_J\sim p(k\mid q),
\qquad
k_r\sim r(k)\quad\text{for }r\ne J.
$$

Assume the reference distribution has positive mass wherever the relevant conditional distribution does. Bayes' rule gives

$$
P(J=j\mid q,k_{1:N})
=
\frac{
p(k_j\mid q)\prod_{r\ne j}r(k_r)
}{
\sum_{\ell=1}^{N}
p(k_\ell\mid q)\prod_{r\ne\ell}r(k_r)
}.
$$

Divide every numerator and denominator term by the common product of reference probabilities:

$$
\boxed{
P(J=j\mid q,k_{1:N})
=
\frac{p(k_j\mid q)/r(k_j)}
{\sum_{\ell=1}^{N}p(k_\ell\mid q)/r(k_\ell)}
}.
$$

The ideal compatibility is therefore a density ratio: how much more plausible is this candidate given the anchor than under the reference sampling process?

If the reference is the marginal candidate distribution, the ratio compares conditional and marginal probabilities. This classification derivation appears in [Contrastive Predictive Coding](https://arxiv.org/html/1807.03748v2).

Changing the negative sampling distribution changes the denominator of that ratio. Negatives sampled from the same patient, device, or temporal neighbourhood pose a different discrimination problem from negatives sampled across an entire dataset.

This is why negatives are part of the supervision design. They specify the alternatives against which a positive must be identified. A contrastive loss value by itself is not a measurement of diagnostic information, and its interpretation depends on how candidate sets were produced.

## A contrastive loss computed from explicit vectors

Choose an anchor and four unit-length candidates:

$$
q=(1,0)^\top,
$$

$$
k_1=(1,0)^\top,
\quad
k_2=(0,1)^\top,
\quad
k_3=(0,-1)^\top,
\quad
k_4=(-1,0)^\top.
$$

Designate the first candidate as positive and use dot-product similarity. The scores are

$$
(s_1,s_2,s_3,s_4)=(1,0,0,-1).
$$

Choose the temperature so that

$$
\tau=\frac1{\log2}.
$$

Then the exponentiated logits are exactly

$$
\left(
e^{s_1/\tau},
e^{s_2/\tau},
e^{s_3/\tau},
e^{s_4/\tau}
\right)
=
\left(2,1,1,\frac12\right).
$$

Their sum is nine halves, giving

$$
(\pi_1,\pi_2,\pi_3,\pi_4)
=
\left(
\frac49,\frac29,\frac29,\frac19
\right).
$$

The loss is

$$
\ell
=
-\log\frac49
=
\log\frac94
\approx0.810930.
$$

The logit derivatives are

$$
\left(
-\frac59,\frac29,\frac29,\frac19
\right).
$$

The most dissimilar negative receives the smallest gradient contribution because its probability is already smaller.

Now halve the temperature while leaving every vector fixed. The exponentiated logits become

$$
\left(4,1,1,\frac14\right).
$$

The positive probability and loss become

$$
\pi_1=\frac{16}{25},
\qquad
\ell=\log\frac{25}{16}\approx0.446287.
$$

The representation has not changed, but its loss has. Temperature controls the sharpness of the classification distribution and the scaling of score gradients. Losses obtained under different temperatures are therefore not directly interchangeable measures of representation quality.

## Why negatives matter, and what they do not guarantee

If there is only the positive candidate, its probability is one:

$$
\ell
=
-\log
\frac{\exp(s_1/\tau)}
{\exp(s_1/\tau)}
=
0.
$$

The gradient is zero regardless of the embedding. Within this objective, no discrimination can be learned without alternatives.

Pure pairwise agreement has another trivial solution. If the loss only penalizes differences between positive embeddings, assigning the same constant vector to every observation makes all such differences zero.

With multiple candidates, a fully collapsed representation gives equal scores and hence

$$
\pi_j=\frac1N,
\qquad
\ell=\log N.
$$

When the data and model permit the positive to be distinguished, lower loss is possible. Negatives create an incentive for discrimination.

This does not prove that optimization cannot stall at a collapsed or otherwise poor representation. Parameter sharing and normalization can produce stationary configurations even when the score-space derivatives suggest improvement. Nor does discrimination guarantee that the learned distinctions are the desired clinical ones.

A false negative is a candidate treated as unrelated by the training construction despite sharing a factor that should be preserved downstream. Instance discrimination can push two observations apart even if their diagnostic content is similar.

Larger candidate sets add comparisons, but they can also add false negatives or make acquisition identity an easier discriminator. Repeated frames from one examination are also not independent new patients.

Finally, explicit negatives are a requirement of the classification objective derived here, not a universal requirement of self-supervised learning. Reconstruction already supplies a different target. Agreement-based methods can impose additional asymmetry or distributional constraints. Each method needs its own explanation of why its trivial solutions are excluded or disfavoured.

## Weak labels change the probability being estimated

Let the intended binary label and the recorded weak label be

$$
Y,
\qquad
\widetilde Y.
$$

Suppose the underlying task probability is

$$
\eta(x)=P(Y=1\mid X=x).
$$

For a simple class-conditional noise model, define

$$
\alpha=P(\widetilde Y=1\mid Y=0),
$$

$$
\beta=P(\widetilde Y=0\mid Y=1),
$$

and assume these rates do not depend further on the input.

The law of total probability gives

$$
P(\widetilde Y=1\mid x)
=
\alpha[1-\eta(x)]
+
(1-\beta)\eta(x).
$$

Therefore,

$$
\boxed{
P(\widetilde Y=1\mid x)
=
\alpha+(1-\alpha-\beta)\eta(x)
}.
$$

Training ordinary cross-entropy against recorded labels targets this noisy probability.

To see the optimum directly, let the recorded positive probability at an input be a fixed number:

$$
\widetilde\eta.
$$

The expected binary cross-entropy for prediction probability is

$$
R(q)
=
-\widetilde\eta\log q
-
(1-\widetilde\eta)\log(1-q).
$$

Its derivative is

$$
R'(q)
=
-\frac{\widetilde\eta}{q}
+
\frac{1-\widetilde\eta}{1-q}.
$$

Setting the derivative to zero yields

$$
q^\ast=\widetilde\eta.
$$

The loss does not know that this target differs from the intended label probability.

For a constructed group of one hundred cases, let eighty be truly positive. Flip sixteen of those to negative, and flip two of the twenty true negatives to positive. The recorded labels contain sixty-six positives:

$$
\eta=0.8,
\quad
\alpha=0.1,
\quad
\beta=0.2,
$$

$$
\widetilde\eta
=
0.1+0.7(0.8)
=
0.66.
$$

If the noise rates are known and their coefficient is nonzero, inversion gives

$$
\eta
=
\frac{\widetilde\eta-\alpha}{1-\alpha-\beta}.
$$

In this example, the correction recovers eight tenths. If the noise rates are unknown, the observed probability alone cannot identify the truth: a clean population with positive probability sixty-six hundredths gives the same recorded-label probability.

More weakly labelled data can estimate the recorded distribution more precisely without resolving this ambiguity.

## Multiple-instance learning and the missing instance labels

A bag contains several instances:

$$
B=\{x_1,\ldots,x_m\}.
$$

Under a classical binary multiple-instance assumption, the bag is positive exactly when at least one latent instance label is positive:

$$
Y_B=\mathbf1\left[\sum_{j=1}^{m}Z_j\ge1\right].
$$

This is a modelling assumption, not a consequence of having an examination-level diagnosis. A positive diagnosis does not logically imply that every selected image, or even one selected image, visibly contains the relevant finding.

Suppose instance labels are conditionally independent given the bag and that each instance probability is modelled from its image:

$$
p_j=P(Z_j=1\mid x_j).
$$

The probability of an all-negative bag is then

$$
P(Y_B=0\mid B)=\prod_j(1-p_j).
$$

Taking the complement gives noisy-OR pooling:

$$
\boxed{
q_B=P(Y_B=1\mid B)
=
1-\prod_j(1-p_j)
}.
$$

For the constructed probabilities

$$
(p_1,p_2,p_3)=(0.2,0.3,0.5),
$$

the positive bag probability is

$$
q_B=1-(0.8)(0.7)(0.5)=0.72.
$$

A positive bag has loss

$$
-\log0.72\approx0.328504.
$$

The first instance receives a derivative through

$$
\frac{\partial q_B}{\partial p_1}
=
(1-p_2)(1-p_3)=0.35,
$$

so

$$
\frac{\partial(-\log q_B)}{\partial p_1}
=
-\frac{0.35}{0.72}
\approx-0.486111.
$$

The bag loss therefore supplies instance gradients despite the missing instance labels.

But the instance probabilities are not uniquely determined by that bag probability. The alternative assignment

$$
(p_1,p_2,p_3)=(0.72,0,0)
$$

produces exactly the same bag prediction and loss. One bag-level observation cannot determine which instance supplied the evidence.

Closely related frames also challenge the conditional independence assumption behind the product. Other pooling rules encode other assumptions; changing the pooling operation does not create missing instance annotations.

## Evaluation must address the supervision gap

Self-supervised evaluation should separate at least three questions: whether the pretext objective was solved, whether the representation supports the downstream task, and whether it preserves the evidence the task is meant to use.

A frozen-encoder probe tests what a specified readout can extract without changing the representation. Fine-tuning tests what supervised adaptation can achieve from that starting point. Neither alone establishes why a prediction succeeds.

Weak-supervision evaluation also needs information that the training labels do not supply. An independently reviewed subset can examine recorded-label errors, selected-frame coverage, and instance-level behaviour. Reusing the same weak labels to train and validate a localization claim leaves the original ambiguity intact.

Missing labels introduce a further selection issue. If label availability depends on both the input and true outcome, the labelled subset represents

$$
P(Y\mid X,\text{label observed}),
$$

which need not equal the intended population conditional distribution. “Unmentioned” should therefore not be silently converted into a negative target without an explicit observation model.

Pseudo-labels inherit a teacher's decision process. Confidence filtering can select confident mistakes as well as correct predictions. Attention weights identify a model's pooling mechanism; a bag label alone does not certify those weights as lesion locations or causal evidence.

Patient separation must also be considered during pretraining. Using unlabeled evaluation cases changes what information was available during learning. The experimental description should make that access explicit rather than treating the absence of manual labels as the absence of evaluation-data exposure.

## Revision checklist

| Question | What I should be able to reconstruct |
| --- | --- |
| What supervises a pretext task? | A target explicitly constructed from observations and sampling decisions. |
| What does squared-error reconstruction estimate? | The conditional mean of the hidden target. |
| What is the contrastive class label? | The index of the designated positive candidate. |
| Why is the positive included in the denominator? | The denominator normalizes probabilities over all candidate classes. |
| What is the InfoNCE score derivative? | Predicted candidate probability minus its indicator, divided by temperature. |
| Why does negative sampling matter? | It defines the reference distribution and therefore the discrimination problem. |
| What does collapse cost? | Equal candidate probabilities give a loss of the logarithm of candidate count. |
| What does cross-entropy on noisy labels estimate? | The recorded-label conditional probability. |
| When can simple noise correction work? | When its assumptions and noise rates are known and the mapping is invertible. |
| What does a positive bag establish? | Only the stated bag-level target, subject to the bag construction and model. |
| Why are instance explanations underdetermined? | Different instance assignments can produce identical bag predictions. |

## Why it matters for my work

For gallbladder ultrasound, I need to inspect the target-generation rule as closely as the network architecture. Pair selection, masking, report extraction, and bag construction each determine what the model is rewarded for learning. Independent feature annotations remain valuable for checking the gap between that reward and the intended evidence.

## What I have not resolved

Which view-pairing and bag-construction rules preserve the relevant clinical distinctions, and what independently reviewed data would be sufficient to reveal their most consequential failures?
