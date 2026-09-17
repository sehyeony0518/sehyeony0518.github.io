---
layout: study_note
title: "Marginalization, Not Optimization: What Deep Ensembles Are Actually Doing"
description: "The frequentist/Bayesian distinction, posterior marginalization, and deep ensembles: deriving predictive uncertainty while separating model averaging from posterior sampling."
og_image: "https://sehyeony0518.github.io/assets/img/og/bayesian-deep-learning-and-deep-ensembles.png"
tab: "ai-foundations"
tab_title: "AI Theory"
category: "probability-and-inference"
category_title: "Probability & Statistical Inference"
subgroup: "Bayesian Imaging & Model Uncertainty"
order: 13
source: "Independent study"
written: true
updated: "2026-09-15"
papers:
  - "2026-09-05-auditing-pointwise-reliability-after-learning"
  - "2026-02-09-underspecification-credibility-ml"
---

Bayesian prediction averages over a posterior distribution of model parameters. A deep ensemble averages predictions from several fitted models. These operations have the same algebraic shape, but they do not automatically average over the same distribution.

The essential correction is that random initialization followed by optimization does not generally produce posterior samples. The frequency with which an optimizer reaches a solution depends on initialization, optimization dynamics, regularization, and stopping. Bayesian posterior mass depends on the likelihood and prior.

An ensemble can still be useful. Its predictive mixture, disagreement, and variance can all be analyzed directly without claiming that it performs exact Bayesian inference.

The mathematical task is to identify the distribution being averaged, derive what uncertainty the mixture contains, and distinguish uncertainty in a prediction from numerical uncertainty in an estimated average.

## The frequentist/Bayesian distinction

In a conventional frequentist parameter model, the parameter is fixed and unknown. Probability describes the data-generating experiment and the sampling distribution of estimators.

In a Bayesian model, a probability distribution represents uncertainty about that parameter before and after observing data.

This does not mean that frequentists cannot assign a probability to an unobserved coin outcome. A coin outcome is a random observation under either framework. The distinction concerns inference about an unknown parameter, such as the coin's probability of heads, rather than whether an already generated but hidden observation may still be treated probabilistically.

Both approaches require a likelihood model. Bayesian inference additionally requires a prior distribution. A likelihood, a prior, an architecture, and a training procedure can each encode assumptions.

For a confidence procedure, the coverage statement concerns repetitions of the data:

$$
\Pr_\theta\{\theta\in C(\mathcal D)\}=0.95
$$

for an exact ninety-five-percent procedure, or an appropriate inequality for conservative coverage.

A Bayesian credible region instead satisfies a posterior probability statement after conditioning on the observed data:

$$
\Pr\{\theta\in C(\mathcal D)\mid\mathcal D\}=0.95.
$$

These statements place randomness in different objects. Neither interpretation can be substituted for the other merely because the numerical endpoints look similar.

## Bayes' rule and the predictive integral

The joint model factors as

$$
p(\theta,\mathcal D)
=
p(\mathcal D\mid\theta)p(\theta).
$$

Integrating over the parameter gives the marginal likelihood:

$$
p(\mathcal D)
=
\int p(\mathcal D\mid\theta)p(\theta)\,d\theta.
$$

Dividing the joint density by this normalizing constant yields

$$
p(\theta\mid\mathcal D)
=
\frac{p(\mathcal D\mid\theta)p(\theta)}
{p(\mathcal D)}.
$$

For supervised learning, one common assumption is conditional independence of labels given inputs and parameters:

$$
p(\mathcal D\mid\theta)
=
\prod_{i=1}^{n}p(y_i\mid x_i,\theta).
$$

This is a modeling assumption. Correlated observations may require a different factorization.

For a new input, the joint posterior distribution of its output and the parameter is

$$
p(y,\theta\mid x,\mathcal D)
=
p(y\mid x,\theta)p(\theta\mid\mathcal D),
$$

assuming that the parameter makes the new output conditionally independent of the training data.

Marginalizing the parameter gives

$$
p(y\mid x,\mathcal D)
=
\int
p(y\mid x,\theta)
p(\theta\mid\mathcal D)\,d\theta.
$$

Why this definition? The output can occur under many possible parameter settings. The law of total probability requires weighting each conditional output distribution by the current probability of that parameter setting.

A point estimate replaces the parameter distribution by a point mass. It retains one conditional predictor and discards variation among the others.

## MLE, MAP, and regularized training

Maximum likelihood chooses

$$
\widehat\theta_{\mathrm{MLE}}
=
\arg\max_\theta p(\mathcal D\mid\theta).
$$

Maximum a posteriori estimation chooses

$$
\widehat\theta_{\mathrm{MAP}}
=
\arg\max_\theta
p(\mathcal D\mid\theta)p(\theta).
$$

The marginal likelihood does not appear in the optimization because it is constant with respect to the parameter.

Taking negative logarithms transforms products into sums:

$$
\widehat\theta_{\mathrm{MAP}}
=
\arg\min_\theta
\left[
-\sum_{i=1}^{n}\log p(y_i\mid x_i,\theta)
-\log p(\theta)
\right].
$$

For an isotropic Gaussian prior,

$$
p(\theta)\propto
\exp\left(-\frac{\lVert\theta\rVert^2}{2s^2}\right),
$$

the prior contribution is

$$
-\log p(\theta)
=
\frac{\lVert\theta\rVert^2}{2s^2}
+\text{constant}.
$$

This derives quadratic regularization as a MAP objective under a particular prior.

The scale depends on whether the data loss is summed or averaged. Dividing the entire objective by the number of observations gives

$$
\frac1n\sum_i-\log p(y_i\mid x_i,\theta)
+
\frac{\lVert\theta\rVert^2}{2ns^2}.
$$

Keeping the same numerical regularization coefficient while changing between summed and averaged losses changes the implied prior scale.

MAP is a Bayesian point estimator. Calling it “not Bayesian” is too strong. What it does not provide is posterior marginalization.

A sharp unimodal posterior also does not make a plug-in prediction exactly equal to the integral. That approximation is good only when the predictive function varies little across the posterior, or when suitable linearity and concentration conditions make the difference negligible.

## A complete conjugate example

Let the unknown probability of heads be

$$
\theta\in[0,1],
$$

and choose a uniform prior. Observe three heads and one tail in an ordered sequence.

The likelihood is proportional to

$$
\theta^3(1-\theta).
$$

The normalizing integral is

$$
\begin{aligned}
\int_0^1\theta^3(1-\theta)\,d\theta
&=
\int_0^1(\theta^3-\theta^4)\,d\theta\\
&=
\frac14-\frac15\\
&=
\frac1{20}.
\end{aligned}
$$

Thus the posterior density is

$$
p(\theta\mid\mathcal D)
=
20\theta^3(1-\theta).
$$

This is a beta distribution with parameters four and two, but the following calculations do not require memorizing beta-distribution formulas.

The posterior mean is

$$
\begin{aligned}
\mathbb E[\theta\mid\mathcal D]
&=
20\int_0^1(\theta^4-\theta^5)\,d\theta\\
&=
20\left(\frac15-\frac16\right)\\
&=
\frac23.
\end{aligned}
$$

The posterior mode maximizes the log density. Differentiating gives

$$
\frac3\theta-\frac1{1-\theta}=0.
$$

Multiplying through by the positive denominator gives

$$
3(1-\theta)-\theta=0,
$$

so

$$
\theta_{\mathrm{MAP}}=\frac34.
$$

The posterior mean and mode already differ in this small unimodal example.

The posterior predictive probability of another head is

$$
p(H_{\mathrm{next}}\mid\mathcal D)
=
\int_0^1\theta\,p(\theta\mid\mathcal D)\,d\theta
=
\frac23.
$$

A MAP plug-in prediction instead gives three-quarters.

The second posterior moment is

$$
\begin{aligned}
\mathbb E[\theta^2\mid\mathcal D]
&=
20\int_0^1(\theta^5-\theta^6)\,d\theta\\
&=
20\left(\frac16-\frac17\right)\\
&=
\frac{10}{21}.
\end{aligned}
$$

Hence,

$$
\operatorname{Var}(\theta\mid\mathcal D)
=
\frac{10}{21}-\frac49
=
\frac2{63}.
$$

All of these numbers follow from elementary integration of the specified posterior.

## Why future observations become dependent

Given the parameter, two future coin flips are independent. After marginalizing the shared unknown parameter, they are generally dependent.

The probability of two future heads is

$$
p(H_1,H_2\mid\mathcal D)
=
\mathbb E[\theta^2\mid\mathcal D]
=
\frac{10}{21}.
$$

Multiplying the individual predictive probabilities would instead give

$$
p(H_1\mid\mathcal D)p(H_2\mid\mathcal D)
=
\left(\frac23\right)^2
=
\frac49.
$$

Their difference is

$$
\frac{10}{21}-\frac49
=
\frac2{63},
$$

exactly the posterior variance of the parameter.

The dependence has a simple interpretation. If the first future flip is a head, it provides evidence favoring larger head probabilities, which raises the probability of another head.

This is a reason to distinguish a collection of marginal predictions from a joint predictive distribution. Parameter uncertainty couples predictions that share the same model parameters.

In deep learning, independently drawing a new parameter sample for every element of a jointly predicted object can erase this shared uncertainty structure. The intended predictive joint distribution determines how samples should be reused.

## When an ensemble is Monte Carlo integration

If parameter vectors are independent draws from the posterior,

$$
\theta_m\sim p(\theta\mid\mathcal D),
$$

then

$$
\widehat p_M(y\mid x)
=
\frac1M\sum_{m=1}^{M}p(y\mid x,\theta_m)
$$

is an unbiased Monte Carlo estimate of the posterior predictive probability.

Let the conditional predictive quantity being averaged be

$$
f(\theta)=p(y\mid x,\theta).
$$

Independence gives

$$
\operatorname{Var}(\widehat p_M)
=
\frac{\operatorname{Var}_{p(\theta\mid\mathcal D)}[f(\theta)]}{M}.
$$

Now suppose training produces samples from an optimizer-induced distribution,

$$
q(\theta\mid\mathcal D),
$$

instead. The same average estimates

$$
\mathbb E_q[f(\theta)],
$$

not necessarily the posterior expectation.

Its mean squared error relative to the desired posterior prediction decomposes as

$$
\mathbb E[(\widehat p_M-p_*)^2]
=
\frac{\operatorname{Var}_q[f(\theta)]}{M}
+
\left(\mathbb E_q[f(\theta)]-p_*\right)^2.
$$

To derive this, add and subtract the estimator's expectation, square, and observe that the centered random term has mean zero. The cross term vanishes.

More members reduce the Monte Carlo term. They do not remove the distribution-mismatch term.

## A two-region counterexample to posterior sampling

Construct a posterior with two relevant regions. Region A has posterior mass nine-tenths and predicts class-one probability two-tenths. Region B has posterior mass one-tenth and predicts nine-tenths.

The Bayesian predictive probability is

$$
0.9(0.2)+0.1(0.9)=0.27.
$$

Now construct a training procedure that converges to each region with equal probability. An increasingly large ordinary ensemble converges to

$$
0.5(0.2)+0.5(0.9)=0.55.
$$

The ensemble average is a perfectly valid mixture prediction. It is simply a different mixture.

If both the posterior masses and proposal probabilities were known, importance weighting could correct the mismatch. The region weights would be

$$
w_A=\frac{0.9}{0.5}=1.8,
\qquad
w_B=\frac{0.1}{0.5}=0.2.
$$

Then

$$
0.5(1.8)(0.2)+0.5(0.2)(0.9)=0.27.
$$

In a neural network, the optimizer-induced distribution and posterior region masses are usually not available in this simple form. Random seeds do not supply those weights automatically.

Posterior density height also differs from posterior mass. A narrow region with a tall peak can contain less probability than a broad region with a lower peak. Selecting several good optima does not determine how an integral should weight their neighborhoods.

## Variational inference and function diversity

A variational approximation chooses a distribution from a tractable family. It need not be a single Gaussian or be restricted to one mode.

Start with the divergence from an approximation to the posterior:

$$
\operatorname{KL}(q\Vert p(\theta\mid\mathcal D))
=
\mathbb E_q
\left[
\log q(\theta)-\log p(\theta\mid\mathcal D)
\right].
$$

Substitute Bayes' rule:

$$
\operatorname{KL}(q\Vert p(\theta\mid\mathcal D))
=
\mathbb E_q[\log q(\theta)-\log p(\mathcal D,\theta)]
+
\log p(\mathcal D).
$$

Rearranging gives

$$
\log p(\mathcal D)
=
\underbrace{
\mathbb E_q[\log p(\mathcal D,\theta)-\log q(\theta)]
}_{\mathrm{ELBO}}
+
\operatorname{KL}(q\Vert p(\theta\mid\mathcal D)).
$$

Because the divergence is nonnegative, the first term is a lower bound on the log marginal likelihood. Maximizing it is equivalent to minimizing this divergence within the chosen family.

Nonnegativity follows from Jensen's inequality applied to the logarithm:

$$
\mathbb E_q\left[\log\frac{p}{q}\right]
\leq
\log\mathbb E_q\left[\frac pq\right]
\leq0.
$$

Negating gives the divergence inequality, with the usual support qualifications.

A restrictive family can miss important posterior structure. An ensemble can cover functionally different solutions that a particular local approximation misses. Neither observation establishes a universal ranking between all ensembles and all variational methods.

Weight diversity also differs from predictive diversity. In a one-hidden-layer network,

$$
f(x)=\sum_{j=1}^{J}v_j\,\sigma(w_j^\top x+b_j),
$$

permuting hidden units leaves the sum unchanged. Different parameter vectors can therefore represent exactly the same function.

The uncertainty relevant to prediction concerns differences in outputs on relevant inputs, not simply distances between weight vectors or the number of apparently distinct minima.

## Deriving regression predictive variance

Suppose each model predicts a conditional mean and variance:

$$
\mu_\theta(x)=\mathbb E[Y\mid x,\theta],
$$

$$
\sigma_\theta^2(x)=\operatorname{Var}(Y\mid x,\theta).
$$

Let the averaged predictive mean be

$$
\overline\mu=\mathbb E_\theta[\mu_\theta].
$$

Decompose the centered output:

$$
Y-\overline\mu
=
(Y-\mu_\theta)+(\mu_\theta-\overline\mu).
$$

After squaring and averaging, the cross term vanishes because

$$
\mathbb E[Y-\mu_\theta\mid\theta]=0.
$$

Therefore,

$$
\operatorname{Var}(Y\mid x,\mathcal D)
=
\mathbb E_\theta[\sigma_\theta^2(x)]
+
\operatorname{Var}_\theta[\mu_\theta(x)].
$$

The first term is within-model output variation. The second is variation in model means under the averaging distribution.

For an equally weighted finite ensemble,

$$
\overline\mu=\frac1M\sum_m\mu_m,
$$

and

$$
\operatorname{Var}_{\mathrm{mixture}}(Y)
=
\frac1M\sum_m
\left[
\sigma_m^2+(\mu_m-\overline\mu)^2
\right].
$$

Construct three members with means

$$
1,\quad2,\quad3
$$

and variances

$$
1,\quad4,\quad1.
$$

Their mixture mean is two. The average within-model variance is

$$
\frac{1+4+1}{3}=2.
$$

The between-model variance is

$$
\frac{(1-2)^2+(2-2)^2+(3-2)^2}{3}
=
\frac23.
$$

Thus total mixture variance is

$$
2+\frac23=\frac83.
$$

The denominator is the number of mixture components because this is the exact variance of the specified discrete mixture. The alternative sample-variance denominator serves a different purpose: unbiased estimation of a population variance from independent samples.

A Gaussian mixture is generally not Gaussian. Matching its mean and variance with one Gaussian preserves those moments, not its full shape or tail probabilities.

## Classification uncertainty and disagreement

For categorical predictions, define ensemble probabilities by averaging member probabilities:

$$
\overline p_c=\frac1M\sum_m p_{m,c}.
$$

The entropy of the mixture is

$$
H(\overline p)
=
-\sum_c\overline p_c\log\overline p_c.
$$

To isolate disagreement, introduce a random member index chosen uniformly. The mutual information between that index and the output is

$$
I(Y;M)
=
\frac1M\sum_m\sum_c
p_{m,c}
\log\frac{p_{m,c}}{\overline p_c}.
$$

Expanding the logarithm and collecting terms gives

$$
I(Y;M)
=
H(\overline p)
-
\frac1M\sum_mH(p_m).
$$

It is an average divergence from member predictions to their mixture, so it is nonnegative.

Two binary examples distinguish predictive uncertainty from disagreement.

In the first, both members predict one-half. The predictive entropy and each member entropy are

$$
\log2\approx0.6931
$$

nats, and mutual information is zero.

In the second, the members predict one-tenth and nine-tenths. Their average remains one-half, so predictive entropy is unchanged. Each member entropy is

$$
-0.1\log0.1-0.9\log0.9
\approx0.3251.
$$

Consequently,

$$
I(Y;M)
\approx0.6931-0.3251
=
0.3681\ \text{nats}.
$$

The first ensemble has members that are individually uncertain. The second has confident members that disagree.

Under exact posterior averaging, this decomposition has a Bayesian information interpretation about parameters and outcomes. Under an ordinary ensemble, it describes disagreement among the selected predictors. Treating that disagreement as a complete measure of epistemic uncertainty requires additional justification.

## Why averaging probabilities matters

A predictive mixture averages probabilities, not logits.

Construct two binary classifiers with probabilities

$$
0.9,\qquad0.6.
$$

Their probability mixture is

$$
\frac{0.9+0.6}{2}=0.75.
$$

Their logits are

$$
\log9,
\qquad
\log1.5.
$$

Averaging logits and then applying the logistic function gives

$$
\frac{\sqrt{13.5}}{1+\sqrt{13.5}}
\approx0.7861.
$$

This is a different predictor because the logistic function is nonlinear.

For a realized class, convexity of negative logarithm gives

$$
-\log\left(\frac1M\sum_mp_m(y)\right)
\leq
\frac1M\sum_m[-\log p_m(y)].
$$

In the example, if the observed class is one, the mixture's negative log likelihood is

$$
-\log0.75\approx0.2877,
$$

while the average member loss is

$$
-\frac{\log0.9+\log0.6}{2}
\approx0.3081.
$$

The mixture improves on the average member loss for this observation. It does not beat the best member automatically.

The reason log loss targets the correct probability distribution can also be derived. If the true categorical probabilities are represented by another distribution, expected log loss equals its entropy plus its divergence from the prediction:

$$
-\sum_c q_c\log p_c
=
-\sum_cq_c\log q_c
+
\sum_cq_c\log\frac{q_c}{p_c}.
$$

The entropy term is fixed, and the divergence is minimized when prediction matches the true distribution. This is a population property of the scoring rule, not a guarantee of finite-sample calibration or performance under distribution shift.

## Correlation limits variance reduction

Suppose model errors have common variance and common pairwise correlation. The variance of their average is

$$
\begin{aligned}
\operatorname{Var}\left(\frac1M\sum_m e_m\right)
&=
\frac1{M^2}
\left[
M\sigma^2+M(M-1)\rho\sigma^2
\right]\\
&=
\sigma^2
\left[
\rho+\frac{1-\rho}{M}
\right].
\end{aligned}
$$

The independent-error result appears when the correlation is zero.

For a constructed correlation of six-tenths and five members,

$$
\operatorname{Var}(\overline e)
=
\sigma^2\left(0.6+\frac{0.4}{5}\right)
=
0.68\sigma^2.
$$

It is not one-fifth of the individual variance. With increasing ensemble size, the correlated component remains.

Independent random seeds do not imply independent prediction errors across cases. Members share data, labels, architecture choices, and possibly the same shortcut.

Also distinguish variance reduction in estimating a predictive average from the predictive uncertainty itself. More posterior samples make the numerical approximation to the integral more precise. They do not make the posterior distribution collapse. The between-model component of predictive variance can approach a nonzero value as the number of members grows.

Finally, the bias–variance identity does not require a U-shaped test-error curve. With a regression target decomposed into a conditional mean and independent zero-mean noise, expanding squared error gives

$$
\mathbb E[(Y-\widehat f)^2]
=
\operatorname{Var}(\text{noise})
+
\bigl(f^*-\mathbb E[\widehat f]\bigr)^2
+
\operatorname{Var}(\widehat f).
$$

The cross terms vanish by centering. Nothing in this identity says that estimator variance must increase monotonically with parameter count. A nonmonotonic learning curve does not invalidate the decomposition.

## What uncertainty cannot certify

An ensemble can agree confidently because all its members learned the same wrong dependence. Low disagreement therefore does not establish that the input is familiar, that the model is correctly specified, or that the prediction is correct.

Conversely, a single fitted model is not categorically incapable of supporting an out-of-distribution detection method. A separate density model, representation-based score, explicit rejection mechanism, or other construction can supply information beyond a softmax maximum. Such methods still require evaluation against their intended target.

Neither Bayesian averaging nor ensembling guarantees reliable extrapolation under an incorrect model family. Posterior concentration can occur around the best explanation available within a misspecified family.

The useful operational questions are more specific: which uncertainty score is computed, what event it should predict, how a threshold is chosen, and which distribution supports the evaluation. Agreement and disagreement are measurements whose interpretation must be tested.

## Revision checklist

| Check | What I should be able to reconstruct |
|---|---|
| Interpretation | Distinguish random observations from uncertainty about a parameter. |
| Bayesian prediction | Derive posterior normalization and the predictive integral from joint probabilities. |
| Point estimation | Explain MLE, MAP, and the prior scale implied by quadratic regularization. |
| Conjugacy | Recover the normalized density $$20\theta^3(1-\theta)$$ by integration. |
| Predictive calculation | Derive the mean $$2/3$$, mode $$3/4$$, and variance $$2/63$$. |
| Joint prediction | Explain why two future heads have probability $$10/21$$ rather than $$4/9$$. |
| Ensemble interpretation | Identify the optimizer-induced distribution and its possible mismatch with the posterior. |
| Approximate inference | Derive the ELBO identity and distinguish parameter diversity from function diversity. |
| Regression uncertainty | Recover the within-model and between-model variance decomposition. |
| Classification uncertainty | Derive entropy minus average entropy as member-output mutual information. |
| Averaging | Explain why probability averaging and logit averaging produce different predictors. |
| Correlation | Derive the residual variance floor and distinguish it from Monte Carlo integration error. |
| Reliability | Explain why shared bias can produce confident agreement. |

## Why it matters for my work

For medical-image models, an ensemble gives a concrete way to measure variation among fitted predictors. I should describe that variation as ensemble disagreement unless a posterior-sampling interpretation is established.

The practical target is whether the score helps identify a specified error or supports a useful abstention decision. Its name does not establish that connection.

## What I have not resolved

I have not established which sources of variation are represented by changing seeds alone, or whether the resulting disagreement identifies failures under the intended acquisition and population shifts.

Evaluate ensemble log loss, calibration, disagreement, and selective-prediction performance on prespecified held-out conditions, including cases where members share the same error.
