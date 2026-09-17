---
layout: post
title: "Covariate-Adjusted Spearman's Rank Correlation with Probability-Scale Residuals"
date: 2026-03-20 12:00:00 +0900
venue: "Biometrics"
authors: "Qi Liu, Chun Li, Valentine Wanga, Bryan E. Shepherd (2018)"
description: "A statistics paper on adjusting rank correlation for confounding covariates, read because so many AI-versus-classical-index comparisons in medical imaging report raw Spearman correlation without asking whether a shared confound is inflating it."
og_image: "https://sehyeony0518.github.io/assets/img/og/2026-03-20-covariate-adjusted-spearman-correlation.png"
related_posts: false
---

**Paper.** *Covariate-Adjusted Spearman's Rank Correlation with Probability-Scale Residuals*. [Biometrics (2018)](https://doi.org/10.1111/biom.12812)

## The question behind the method

If a model score correlates with a clinical severity grade, what has been established? Possibly that the model tracks severity. Possibly that both variables differ between hospitals, age groups, or diagnostic classes. A pooled correlation cannot distinguish these explanations.

This matters for my work because an evidence-alignment metric can look convincing while measuring population composition. Suppose more suspicious lesions receive magnified ultrasound views. A model readout sensitive to magnification might correlate with reader-assessed irregularity without measuring irregularity reliably within comparable acquisitions. Adjusting for acquisition asks a more specific question, provided the adjustment itself is appropriate.

The statistical problem is that the familiar partial-correlation formula does not automatically become a principled rank-based estimand when Pearson correlations are replaced with Spearman correlations. The paper supplies a population definition and an estimator that fit together.

## What probability-scale residuals do

The authors model the conditional distributions of two orderable variables, X and Y, given covariates Z. Each observation becomes a probability-scale residual, and the partial Spearman estimate is the correlation between the two residual sets. They also define conditional correlations, which can vary with covariate values, and study semiparametric cumulative probability models that preserve the outcomes' ordering. [Full paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5949238/)

For intuition, a probability-scale residual compares how much fitted probability lies below an observation with how much lies above it:

$$
r_X = P(X^* < X \mid Z) - P(X^* > X \mid Z).
$$

Equivalently, it uses the fitted cumulative probabilities immediately below and at the observation. That distinction handles ties and ordinal categories. A positive residual means that the observation is relatively high compared with its fitted conditional distribution. It is not a residual measured in the original biomarker's units.

The correlation therefore asks whether people who rank relatively high on one variable, given their covariates, also rank relatively high on the other. The authors' later [PResiduals paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11451338/) provides an implementation-oriented explanation of this construction.

Partial and conditional correlation answer different questions. A single adjusted coefficient summarizes an association across the sampled population. A conditional analysis asks whether that association changes, for example, with age. One pooled adjusted number can still conceal clinically important heterogeneity.

## What the empirical examples establish

In the HIV biomarker application, adjustment includes demographic and clinical covariates and study cohort. The IL-6–sCD14 correlation changes from 0.03 to 0.19, with an adjusted 95% confidence interval of 0.04 to 0.33. The leptin–sCD14 estimate changes from −0.20 to +0.13, but the latter interval is −0.01 to 0.27. That sign reversal should therefore not be described as decisive evidence of a positive adjusted association. [Application results](https://pmc.ncbi.nlm.nih.gov/articles/PMC5949238/)

These examples make a useful point: adjustment can reveal an association as well as attenuate one. It would be a mistake to approach covariate adjustment solely as a device for reducing an inflated score. The scientific question determines the adjustment; the desired direction of the answer does not.

The simulations support the estimator under the settings examined. They cannot establish that a particular adjustment set or conditional model is adequate for a new imaging study.

## What the result licenses

An adjusted correlation supports a statement about residual ordering under the specified models and adjustment variables. It does not establish that the model uses the correlated clinical finding. Two readouts can remain associated because of an unmeasured common influence, or because both are downstream consequences of diagnosis.

It also does not measure agreement. A model measurement can rank patients correctly while consistently overestimating the quantity. If the intended output is joint-space width or lesion size, correlation alone cannot establish acceptable measurement error.

Likewise, zero adjusted correlation is a limited negative result. A non-monotonic relationship, a subgroup effect, measurement noise, or restricted variation could produce a small coefficient. The absence of a rank association does not establish that the two variables are unrelated in every useful sense.

For ordinal clinical labels, the ordering is meaningful, but category transitions may not represent equal biological changes. Probability-scale residuals respect that distinction. They do not solve uncertainty about whether the label measures the intended clinical construct.

## The weakness I would press

The main vulnerability is the conditional-distribution modeling step. Calling the result rank-based can make it sound almost assumption-free. Once covariates enter, estimates depend on how their relationships with both outcomes are represented. Missed nonlinearities or interactions can leave structure in the residuals.

The adjustment set is an even earlier decision. Conditioning on diagnosis changes an overall alignment question into a within-diagnosis question. If a finding helps determine diagnosis, that adjustment may remove part of the relationship I wanted to study. Conditioning on selection into surgery could introduce another association rather than remove one.

I would therefore specify the estimand before fitting anything: overall association, within-class association, or association among comparable acquisition conditions. These are complementary analyses, not progressively more correct versions of the same number.

Limited overlap also matters. If one scanner contributes only severe cases, a regression model may manufacture an adjusted comparison through extrapolation. A tidy confidence interval does not demonstrate that the underlying clinical comparison was observed.

## Connections to the study notes

[Confounding in Medical AI](/study/confounding-in-medical-ai/) argues that hospital identity should be unpacked into mechanisms and that the adjustment rationale depends on the question. This paper supplies a useful estimator for those observational comparisons. It does not supply their causal justification.

[Statistical Inference for Diagnostic Studies](/study/statistical-inference-for-diagnostic-studies/) emphasizes the estimand and sampling unit. In an ultrasound audit, I would preserve patient clustering and refit the conditional models during a bootstrap intended to include uncertainty from adjustment. Resampling already-computed residuals would omit that fitting variation.

[Representation-Level Auditing](/study/representation-level-auditing/) separates information accessibility from diagnostic use. A significant adjusted correlation between an internal readout and a clinical annotation remains evidence about association. A controlled intervention on the original predictor addresses the additional reliance question.

## How I would use it

I would report the raw coefficient, adjusted coefficient, confidence interval, covariate definitions, model specifications, and subgroup composition together. I would inspect conditional-model diagnostics and sensitivity to defensible alternative specifications.

The practical benefit is a more precise claim: this readout tracks this annotation after this adjustment in this population. That statement is narrower than clinical faithfulness, but it is testable, reproducible, and useful for deciding which behavioral experiment should follow.
