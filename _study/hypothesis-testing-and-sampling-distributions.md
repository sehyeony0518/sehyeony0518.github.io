---
layout: study_note
title: "Hypothesis Testing and Sampling Distributions: What a p-Value Can and Cannot Say"
description: "The conditional form of every test, why 'at least as extreme' is the operative phrase, and the t and chi-squared distributions that make the calculation possible at all."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "probability-and-inference"
category_title: "Probability & Statistical Inference"
order: 6
source: "Independent study"
written: true
updated: "2026-09-15"
---

Toss a coin 15 times and get 10 heads. Is the coin fair?

**You cannot know.** That is not a hedge; it is the correct and complete answer to the question as asked. What you can compute is something narrower and conditional, and the whole apparatus of hypothesis testing is built to compute exactly that one thing.

## Core question and definition

The move is to assume the claim and see how strange the data becomes:

> *If* the coin were fair, what is the probability of an outcome **at least as extreme** as the one observed?

For 15 fair tosses, $$P(\text{exactly }10) = 0.0916$$, but that is not the quantity wanted. Had 11 or 12 heads come up you would have been at least as suspicious, so the tail belongs in the count; and 5 heads would have been equally suspicious in the other direction, so the far tail belongs too. The two-sided figure is

$$
P(X \ge 10) + P(X \le 5) = 0.3018 .
$$

Thirty percent. A fair coin produces something this lopsided or worse in roughly one experiment in three, so 10 of 15 is no evidence of anything. Push to 12 heads and the same calculation gives $$0.0352$$: now the observation is awkward for the fair-coin hypothesis, though where to draw the line is a human decision, not a fact the data supplies.

Note what was and was not concluded. Not "the coin is biased." Only: *under the assumption of fairness, what happened had probability 0.035*. Every p-value has that conditional shape, and essentially every misreading of one comes from dropping the condition.[^asa]

## Key concepts

### The test is impossible without a distribution for the statistic

The calculation above worked only because the count of heads under a fair coin is known to be binomial. That is the binding constraint on the whole enterprise: **you must know what distribution your statistic follows when the null hypothesis is true.** Without it there is no "how extreme," and the argument cannot start.

Consider testing whether a Gaussian has mean $$\mu_0$$ when the variance is unknown. One sample is useless: it cannot say whether a deviation is large, because "large" has no scale yet. Draw $$n$$ samples, estimate the spread, and form

$$
t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}},
\qquad s^2 = \frac{1}{n-1}\sum_i (x_i-\bar{x})^2 ,
$$

and this quantity follows Student's $$t$$ with $$n-1$$ degrees of freedom, regardless of the true $$\sigma$$.[^student] That independence from $$\sigma$$ is the entire point: an unknown nuisance parameter has been eliminated, and a computable test remains.

Simulation confirms it directly: draw 200,000 sets of 5 samples from $$\mathcal{N}(3, 7^2)$$, compute $$t$$ each time, and the histogram matches $$t_4$$ to a KS statistic of 0.0014.

**A trap worth naming.** NumPy's `std` defaults to `ddof=0`, the population formula dividing by $$n$$; the $$t$$ statistic needs `ddof=1`. Using the default in the same simulation moves the KS statistic from 0.0014 to 0.0244: a seventeen-fold degradation, and one that produces a plot which still looks roughly bell-shaped. With $$n=5$$ the two differ by a factor of $$\sqrt{5/4}$$, which is enough to shift a p-value but not enough to look obviously wrong.

Student's $$t$$ is heavy-tailed at low degrees of freedom, with few samples the estimated spread is itself unreliable, and the distribution widens to absorb that, and converges to the normal as the count grows.

### Chi-squared, and the goodness-of-fit test

The sum of squares of $$k$$ independent standard normals follows the **chi-squared** distribution with $$k$$ degrees of freedom. (Simulation: 200,000 sums of 3 squared normals against $$\chi^2_3$$ gives a KS statistic of 0.0032.)

Its use here is Pearson's goodness-of-fit test.[^pearson] With observed counts $$O_i$$ and expected counts $$E_i$$ under the null,

$$
\chi^2 = \sum_i \frac{(O_i - E_i)^2}{E_i}
$$

approximately follows $$\chi^2$$ with $$k-1$$ degrees of freedom.

Roll a die 204 times and observe $$22, 24, 38, 30, 46, 44$$. A fair die expects $$34$$ of each, so

$$
\chi^2 = \frac{144+100+16+16+144+100}{34} = 15.294,
$$

which on 5 degrees of freedom gives $$p = 0.0092$$. Under fairness, a table this uneven or worse arises about once in a hundred experiments.

The honest caveat, which the derivation does not supply: the connection between "sum of squared normals" and "sum of squared *count* deviations scaled by expected counts" is not obvious, and the approximation is asymptotic. It is a proved result being used, not one being re-derived, and it degrades when expected counts are small.

### Plotting a histogram against a density

A smaller point, but one that silently breaks plots. Draw $$N$$ samples and histogram them with bin width $$\Delta$$. The count in a bin centred at $$x$$ is approximately $$N \cdot f(x)\cdot\Delta$$, so to overlay the density you must divide the counts by $$N\Delta$$, not by $$N$$ alone. Get it wrong and the curve and the bars miss each other by a constant factor, which looks like a modelling error and is arithmetic.

## Why it matters for my work

Almost every claim of improvement in a paper is a hypothesis test, whether or not one is reported, and the conditional form is what gets lost.

The most consequential loss is the direction of the inference. A p-value says *P(data this extreme | null true)*. What a reader wants is *P(null true | data)*, and these are not the same quantity: converting between them requires a prior, which the test does not have and does not use. A large p-value is not evidence of no effect; it is failure to accumulate evidence against no effect, and in a small [validation cohort](/study/statistical-inference-for-diagnostic-studies/) those are very different situations with identical outputs.

Second, the requirement that you know the null distribution is where most applied testing quietly breaks. The standard tests assume independent samples. Medical imaging data routinely is not: multiple slices per study, multiple studies per patient, multiple patients per site. Treating slices as independent samples inflates $$n$$, shrinks the standard error, and manufactures significance out of nothing but repeated measurement of the same person. The test will not complain, it has no way to know, which is why [study design](/study/dataset-design-ground-truth-and-reference-standards/) has to settle the unit of analysis before any test is run.

The `ddof` detail is the small lesson standing in for a large one: a statistical result can be wrong by a factor that leaves the output looking entirely reasonable. Verifying a sampling distribution by simulation before trusting a p-value built on it costs a few lines and is one of the few checks that actually catches this class of error.

This machinery is also what justifies a specific evaluation metric: see [MCC](/study/matthews-correlation-coefficient/), which is a chi-squared test of independence on a confusion matrix, rescaled.

---

[^student]: Student (1908). The probable error of a mean. *Biometrika*, 6(1), 1–25. [10.2307/2331554](https://doi.org/10.2307/2331554)

[^pearson]: Pearson, K. (1900). On the criterion that a given system of deviations from the probable in the case of a correlated system of variables is such that it can be reasonably supposed to have arisen from random sampling. *Philosophical Magazine*, 50(302), 157–175. [10.1080/14786440009463897](https://doi.org/10.1080/14786440009463897)

[^asa]: Wasserstein, R. L., & Lazar, N. A. (2016). The ASA statement on p-values: context, process, and purpose. *The American Statistician*, 70(2), 129–133. [10.1080/00031305.2016.1154108](https://doi.org/10.1080/00031305.2016.1154108)
