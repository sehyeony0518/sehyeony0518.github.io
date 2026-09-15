---
layout: study_note
title: "Marginalisation, Not Optimisation: What Deep Ensembles Are Actually Doing"
description: "The frequentist/Bayesian split is one decision — is the parameter a constant or a random variable — and it propagates all the way to why averaging several trained networks is not a trick."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "probability-and-inference"
category_title: "Probability & Statistical Inference"
order: 13
source: "Independent study"
written: true
updated: "2026-09-15"
---

A coin with a fair bias is flipped, caught, and covered. What is the probability it shows heads?

The answer depends entirely on one prior decision, and the decision is not a matter of evidence.

## Core question and definition

**Frequentist**: the coin has landed. Its state is a fixed constant that I happen not to know. Probability describes the sampling procedure, not my ignorance, so "the probability it is heads" is not a well-formed question about *this* coin.

**Bayesian**: from where I sit nothing has changed. The state is a random variable, and 50% is the right answer.

Neither is wrong. They are different choices about what may be assigned a distribution, and the choice determines which quantity can sit on the left of the conditioning bar:

$$
\underbrace{P(\text{data} \mid \theta)}_{\text{frequentist: } \theta \text{ is a constant}}
\qquad\text{versus}\qquad
\underbrace{P(\theta \mid \text{data})}_{\text{Bayesian: } \theta \text{ is a random variable}}
$$

That swap is small to write and enormous in consequence, because $$P(A\mid B)$$ and $$P(B\mid A)$$ are different numbers answering different questions.

It also clears up a common misreading. A 95% confidence interval does **not** say the parameter lies inside it with probability 0.95 — under the frequentist commitment the parameter is a constant, so it is either in or out. It says that the *procedure*, repeated, produces intervals containing the parameter 95% of the time. The interpretation people actually want is the Bayesian credible interval, and they routinely report the first while meaning the second.

The claim that Bayesian methods are subjective because they require a prior is weaker than it looks: **writing a likelihood is already a modelling commitment.** Choosing a dice model with six equal faces, or a squared-error loss, encodes assumptions as surely as a prior does. The difference is which assumption is written down where, not whether one was made.

## Key concepts

### The marginalisation, and why it is the whole point

Standard training finds one parameter vector and predicts with it:

$$
p(y \mid x, \hat\theta), \qquad \hat\theta = \arg\max_\theta \ p(\mathcal D \mid \theta)\,p(\theta)
$$

The Bayesian predictive distribution instead **integrates over every parameter setting**, weighted by how well each explains the data:

$$
p(y \mid x, \mathcal D) = \int p(y \mid x, \theta)\, p(\theta \mid \mathcal D)\, d\theta
$$

Wilson and Izmailov's argument is that this integral — not the prior — is what Bayesian inference *is*, and that the field mostly discards it.[^wilson] Regularised training with a MAP estimate looks Bayesian (the regulariser is a log prior) and is not, because it collapses the integral to its single tallest point.

That collapse is harmless when the posterior has one sharp mode: the peak and the mean coincide. A deep network's loss surface has enormous numbers of distinct good solutions, so the peak and the integral are not remotely the same object. **Picking the tallest point of a multimodal distribution and calling it the answer discards most of the distribution.**

### Deep ensembles are that integral, approximated

Train the same architecture from several random initialisations and average the predictions. This is normally filed as an engineering trick and compared *against* Bayesian methods.

The reframing is that it is a **Monte Carlo approximation to the marginalisation**:

$$
\int p(y\mid x,\theta)\,p(\theta\mid\mathcal D)\,d\theta \;\approx\; \frac{1}{M}\sum_{m=1}^{M} p(y \mid x, \theta_m)
$$

Different random seeds converge to different modes, so the ensemble members *are* samples from distinct regions of the posterior — which is precisely what an integral over a multimodal posterior needs and what a single Gaussian fitted around one mode cannot provide. Variational inference, the standard "proper" Bayesian method, approximates the posterior with one tractable distribution centred on one mode; the ensemble covers several. **On the criterion that matters — approximating the integral — the ensemble is the more Bayesian method**, which inverts the usual ranking.

Averaging $$M$$ independent estimates cuts variance to $$\sigma^2/M$$: 5 models to a fifth, 10 to a tenth. That is the ordinary statistical gain. The marginalisation reading says something stronger — the ensemble is not reducing noise around a correct answer, it is computing a different and better-posed quantity.

SWAG sits between: run SGD past convergence, fit a Gaussian to the weights it visits, and sample.[^swag] That characterises one basin well and still misses the others, which is why MultiSWAG — several basins, a Gaussian in each — outperforms both.

### The observations this explains

Three results that the bias–variance story cannot accommodate:

**Random labels.** A network with 60 million parameters trained on 1 million images can fit *randomly assigned* labels to zero training error.[^zhang] Its capacity is not the constraint. Yet given real labels the same network generalises well. Capacity alone therefore does not explain generalisation — the question is which of the many fitting solutions the training procedure prefers, and why.

**Double descent.** Test error falls, rises to a peak at the interpolation threshold, and then **falls again** as the model grows past it.[^belkin] The classical U-curve says this is impossible. The Bayesian reading is that a larger model has broader *support* — it can express more functions — while its inductive bias still concentrates mass on the plausible ones, so growth need not cost generalisation.

**Overconfidence.** LeNet-era networks had softmax outputs roughly matching empirical accuracy; modern networks are badly overconfident, and temperature scaling — dividing logits by a fitted constant — largely fixes it on in-distribution data.[^guo] It fixes nothing out of distribution, because the model never saw that region and a single $$\hat\theta$$ has no mechanism for representing that fact.

### Inductive bias is two-dimensional

The thing these share is that **model complexity is not one number.** Wilson's framing separates:

- **support** — the range of datasets the model *can* express, and
- **inductive bias** — how its prior mass is distributed across that range.

An MLP has broad support and flat bias: it can fit anything, prefers nothing. A CNN has narrower support and sharply peaked bias — translating an image should not change its label, and the architecture builds that in. A linear model has support so narrow it cannot express the data at all.

What you want is **broad support with well-placed bias**: able to represent the truth, and preferring it. That is a two-dimensional criterion, and "number of parameters" projects it onto one axis and loses the part that matters.

The Deep Image Prior makes it vivid: an *untrained* convolutional network, fitted to a single noisy image, reconstructs the image before it reconstructs the noise.[^dip] No training data at all. The architecture alone prefers natural images — the inductive bias is in the wiring.

## Why it matters for my work

The honest reason to care is **out-of-distribution behaviour**, which is the central reliability problem in medical AI and which no single-$$\hat\theta$$ model can address in principle.

Feed a chest radiograph to a model trained on MRI and it answers confidently. Not because it is badly calibrated — temperature scaling fixes in-distribution calibration and does nothing here — but because a point estimate has **no representation of the distinction between "I have seen this and I am sure" and "I have never seen this."** Both come out as a softmax vector. Recovering that distinction requires disagreement between plausible parameter settings, and disagreement requires more than one parameter setting.

Which makes the practical conclusion unusually cheap for how much it buys: **train five models with different seeds and look at the spread.** No new theory, no variational machinery, roughly linear cost. Where they agree, the training data constrained the answer. Where they disagree, they are reporting that several very different functions explain the data equally well — which is exactly the [epistemic uncertainty](/study/calibration-uncertainty-and-selective-prediction/) that should trigger abstention.

There is a reporting consequence too, and I think it is underweighted. A paper reporting one trained model reports one sample from a distribution it did not characterise — and I now read single-run results as an estimate with an unreported variance rather than as a measurement. That belongs with the [reproducibility](/study/reproducibility-benchmarks-and-translational-study-design/) concerns rather than beneath notice.

## What I have not resolved

Whether ensemble disagreement is a usable OOD signal in clinical practice or only in benchmarks. Members share an architecture, a training set and a preprocessing pipeline, so they share every bias those impose — and a [shortcut](/study/shortcut-learning-in-medical-imaging/) present in the training data is available to all five. They would agree, confidently, and be wrong together. Ensemble disagreement detects the uncertainty that comes from having insufficient data to pin down the function; it cannot detect the uncertainty that comes from every member having learned the same wrong thing.

---

[^wilson]: Wilson, A. G., & Izmailov, P. (2020). Bayesian deep learning and a probabilistic perspective of generalization. *NeurIPS*. [arXiv:2002.08791](https://arxiv.org/abs/2002.08791)

[^swag]: Maddox, W. J., Garipov, T., Izmailov, P., Vetrov, D., & Wilson, A. G. (2019). A simple baseline for Bayesian uncertainty in deep learning. *NeurIPS*. [arXiv:1902.02476](https://arxiv.org/abs/1902.02476)

[^zhang]: Zhang, C., Bengio, S., Hardt, M., Recht, B., & Vinyals, O. (2021). Understanding deep learning (still) requires rethinking generalization. *Communications of the ACM*, 64(3), 107–115. [10.1145/3446776](https://doi.org/10.1145/3446776)

[^belkin]: Belkin, M., Hsu, D., Ma, S., & Mandal, S. (2019). Reconciling modern machine-learning practice and the classical bias–variance trade-off. *PNAS*, 116(32), 15849–15854. [10.1073/pnas.1903070116](https://doi.org/10.1073/pnas.1903070116)

[^guo]: Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On calibration of modern neural networks. *ICML*. [arXiv:1706.04599](https://arxiv.org/abs/1706.04599)

[^dip]: Ulyanov, D., Vedaldi, A., & Lempitsky, V. (2018). Deep image prior. *CVPR*. [10.1109/CVPR.2018.00984](https://doi.org/10.1109/CVPR.2018.00984)
