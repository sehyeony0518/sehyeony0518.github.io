---
layout: post
title: "A Bold Number Is Not Evidence: Christodoulou and Colliot on Performance Reporting in Medical Imaging AI"
date: 2025-09-19 12:00:00 +0900
description: "Notes from a MICCAI webinar on performance uncertainty: confidence intervals, false claims of outperformance, data splitting, standard deviation versus standard error, and bootstrap-based reporting."
tag: "MICCAI"
related_posts: false
---

Medical-imaging AI papers often end with a familiar table: methods in the rows, a metric in the columns, and the largest value printed in bold. A difference of 0.01 may be enough for the proposed method to be called state of the art.

The formatting looks decisive. The evidence beneath it often is not.

This post is based on the MICCAI Special Interest Group for Challenges webinar *Performance Reporting in Medical Imaging AI*, presented on June 10, 2025 by Evangelia Christodoulou (German Cancer Research Center) and Olivier Colliot (CNRS, Paris Brain Institute). ([MICCAI Society][1]) The talk combined two studies: *Confidence Intervals Uncovered* (MICCAI 2024), which surveyed how uncertainty was reported in MICCAI 2023 segmentation papers, and *False Promises in Medical Imaging AI?*, which asked whether published outperformance claims were actually supported. ([MICCAI Open Access][2], [arXiv][3])

The question was not which metric to choose — frameworks like Metrics Reloaded cover that — but what happens after: how uncertain is the estimate, and how much evidence does a superiority claim require?

Any errors of interpretation are mine.

## Part 1 — Performance is a sample estimate, not a property of the checkpoint

Evaluate a classifier on 50 cases and it scores 46/50 = 92%. Swap in four harder cases and the same model scores 42/50 = 84%. Nothing about the model changed — only the sample did. Neither number is the model's "true" accuracy; each is an estimate from one finite sample of a larger population.

This is obvious when stated, yet papers routinely present a single point estimate as though the checkpoint possessed that value intrinsically. The point estimate is the center of the result. It is not the whole result.

## Part 2 — The field reports the center and hides the spread

The survey examined all 221 medical-image segmentation papers at MICCAI 2023. **More than half reported no measure of performance variability at all. Exactly one paper — about 0.5% — reported a confidence interval.**

Even where a "±" appeared, its meaning was often undefined: variation across test patients? standard error of the mean? across folds? across seeds? These are different quantities answering different questions. Patient-level standard deviation describes how *heterogeneous* performance is across cases (and does not shrink just because you test more patients); the standard error describes how *precisely the mean was estimated* (and does shrink with sample size); a confidence interval bounds the population-level statistic — not the range where 95% of patients fall. A precisely estimated mean can coexist with wildly inconsistent per-patient performance, and vice versa. One unexplained number cannot carry both facts.

The omission is not just a stylistic lapse: regulatory evaluation of medical devices expects performance estimates with confidence intervals, because a sensitivity of 0.90 with a narrow interval and the same value with a wide one are different evidentiary situations.

## Part 3 — The reconstructed uncertainty was larger than the claimed improvements

Since the surveyed papers rarely published case-level results, the authors approximated the missing uncertainty: using the Medical Segmentation Decathlon, they found an inverted-U relationship between mean Dice and its standard deviation (very poor and near-perfect models both vary little; mid-range models vary most), fitted a regression, and reconstructed approximate 95% confidence intervals from each paper's reported mean and test-set size — validating the approximation on 56 past segmentation challenges.

The result: the **median reconstructed interval width was ~0.03 Dice, while the median gap between the first- and second-ranked methods was ~0.01** — the typical uncertainty was about three times the typical claimed advantage. In over 60% of papers, the runner-up's mean fell inside the winner's interval.

Two caveats matter. Interval overlap is not a formal comparison — predictions from two models on the same patients are correlated, so the right quantity is the *paired difference* and its uncertainty. And the reconstruction is a rescue approximation, least reliable for tiny test sets — the original authors could have computed the real thing from their own predictions. But the scale of the omitted uncertainty was not negligible.

## Part 4 — "False promises": most bold claims were statistically unsupported

The follow-up study covered 347 MICCAI 2023 classification and segmentation papers. Over 80% bolded a top result and claimed outperformance; only ~13% (classification) and ~10% (segmentation) included any statistical analysis. Median winner-vs-runner-up gap: ~0.01 in both tasks. Median test sets: 500 images (classification), 62 (segmentation).

Using a Bayesian estimate of the **probability of a false claim** — how plausible it is that the runner-up is actually as good or better, given the observed values, test size, and empirically estimated congruence between models — the authors found that probability exceeded 5% in an estimated **86% of classification papers and 53% of segmentation papers**.

The term needs care: this is an evidentiary statement under the study's model, not an accusation that most conclusions are false. The field simply spoke with more certainty than its evaluation designs supported. Simulations made the cost concrete: supporting a 0.01 accuracy gain at <5% false-claim probability required a test set roughly **8× larger** than the observed median; a 0.01 Dice gain required roughly **10× larger**. Those multipliers are setting-specific, not universal rules — but the durable message is that the smaller the claimed improvement, the more evaluation data it takes to distinguish it from sampling noise. A reported 0.873 is not known more precisely than 0.87; decimal precision and evidentiary precision are different things.

## Part 5 — Practical machinery: splits, folds, and the bootstrap

Three pieces of practical guidance recurred.

**Splits define what the number means.** Validation performance is optimistically biased (it steered development); the independent test set estimates performance in the target distribution; an external set tests transfer. A "test set" repeatedly examined during development is no longer independent — integrity depends on how a set was used, not what it was called. The splitting unit (patient vs image vs slice) must be explicit.

**Cross-validation folds are not independent experiments.** Fold scores share training data; their standard deviation describes *learning-procedure instability*, not the sampling uncertainty of the final model. Running a t-test across folds, or presenting fold SD as the test-set standard error, mislabels one kind of variability as another. Both are worth reporting — separately and labeled.

**The bootstrap is a practical default — at the patient level.** Resample the *n* test cases with replacement, recompute the metric, repeat ~10,000 times (cheap — no retraining), and take percentile intervals. It estimates sampling uncertainty conditional on the trained model; it cannot manufacture information a small test set lacks. Crucially, the resampling unit must be the independent unit — usually the patient. Resampling correlated images or slices as if independent yields artificially narrow intervals. And for comparing models, **bootstrap the paired difference**: same resampled patients for both models, distribution of Δ = θ_A − θ_B. An interval crossing zero means the ordering is not established — though even a stable difference of 0.001 may be clinically irrelevant, and a clinically meaningful difference may remain uncertain because the study was small. Statistical precision and clinical importance are distinct judgments.

## Part 6 — What a narrow interval cannot fix

A narrow confidence interval means a statistic was estimated precisely under the observed sampling process — nothing more. It can surround a biased answer if patients leaked across splits, correlated images were treated as independent, the test set quietly steered development, labels were unreliable, or a scanner shortcut inflated performance. Precision does not repair bias.

Sample size also cannot be separated from prevalence and subgroups: a 5,000-exam test set with 25 positives estimates sensitivity from 25 cases. Aggregate power can coexist with hopeless imprecision for a sex, site, scanner, or disease subtype. The denominators behind every claim — independent patients, positives, subgroup counts, sites — are part of the result, as is a description of who the test population actually was. When asked for a universal minimum test-set size, the speakers declined: it depends on the metric, target precision, prevalence, and the claim being made — and estimating within 2–3 percentage points often takes thousands of cases, not hundreds.

## Part 7 — A minimum reporting package

Compressing the webinar's recommendations: **(1)** define the estimand (patient-level mean Dice? image-level accuracy? macro-AUROC?); **(2)** describe splits and the independent unit; **(3)** report the point estimate *with* a defined confidence interval from the independent test set, naming the method and resampling unit; **(4)** report patient-level dispersion separately from the standard error; **(5)** report training/seed variability separately from sampling uncertainty; **(6)** support outperformance claims with paired differences, not adjacent bold means; **(7)** give subgroup denominators; **(8)** describe the test population; **(9)** separate statistical evidence from clinical relevance; **(10)** never print an unexplained ±.

The speakers were explicit that the field still lacks a dedicated community guideline for uncertainty reporting in medical-image computing — this is a floor, not a ceiling.

## A researcher's takeaway

Reported performance is not a property of the checkpoint alone. It is the checkpoint evaluated on a particular sample, through a particular metric, at a particular unit of analysis, under a particular splitting and statistical procedure. Change any of those and the conclusion can change.

This applies with full force to evidence auditing. If two models score 0.52 and 0.47 on a clinical-alignment metric, the bold-number instinct says the first is more aligned. But an audit metric is still an empirical statistic: What is the paired interval on the difference? Does the ranking survive training seeds? Is the variability driven by the checkpoint or by the sampled patients? Does it persist at another site? Test-set sampling uncertainty, training-seed variability, and external distribution shift are three different uncertainties — patient-level bootstrap, repeated training, and external cohorts address them respectively, and none substitutes for the others. The same logic protects negative results: a near-zero estimate with a wide interval is not evidence of absence.

A model does not outperform another because its mean is printed in bold. It outperforms when the uncertainty in the paired difference is small enough, the improvement is clinically meaningful enough, and the evaluation is representative enough to support the claim.

The number may be bold. The evidence must be stronger.

[1]: https://miccai.org/2025/05/20/webinar-performance-reporting-in-medical-imaging-ai-june-10-2025/ "Webinar: Performance Reporting in Medical Imaging AI — June 10, 2025 — MICCAI Society"
[2]: https://papers.miccai.org/miccai-2024/152-Paper3400.html "Confidence intervals uncovered: Are we ready for real-world medical imaging AI? (MICCAI 2024)"
[3]: https://arxiv.org/html/2505.04720v1 "False Promises in Medical Imaging AI? Assessing Validity of Outperformance Claims"
