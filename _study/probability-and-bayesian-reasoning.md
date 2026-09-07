---
layout: page
title: "Probability and Bayesian Reasoning"
description: "Conditional probability, expectation and variance, conditional independence, and Bayes as the grammar for reasoning about diagnostic evidence."
section: "F"
section_title: "Mathematical and Statistical Foundations"
branch: "Branch 01"
order: 2
written: true
---

The probability of a positive test in someone with disease is different from the probability of disease after a positive test. Bayesian reasoning keeps those directions explicit and describes how evidence changes an existing assessment.

## Why it matters here

A diagnostic model's score only becomes interpretable as risk when its target and conditioning information are clear. The same test result can imply different probabilities in different populations. A study that reports sensitivity and specificity has therefore not yet told me what a positive result means in the intended clinical setting.

In my research, probability also provides a language for evidence auditing. I want to distinguish a readout that varies with a clinical factor from one that adds information after other factors are known. Writing down what is conditioned on helps expose assumptions that a pooled correlation or an unexplained confidence score can hide.

## The core ideas

### Conditioning changes the population under discussion

Conditional probability P(A|B) describes A within the circumstances specified by B. Sensitivity is the probability of a positive result given disease; positive predictive value reverses that conditioning. They answer different questions because their denominators describe different groups. For a gallbladder classifier, conditioning on surgery would create another distinction: the probability of malignancy among operated patients need not match the probability among all patients with an ultrasound finding.

### Bayes combines prior information with a likelihood

Bayes' rule gives P(D|E) = P(E|D)P(D)/P(E), where D denotes disease and E the observed evidence. The prior describes probability before this evidence, while the likelihood describes how compatible the evidence is with disease. In odds form, posterior odds equal prior odds multiplied by the likelihood ratio. This is the diagnostic update described by [Altman and Bland](https://www.bmj.com/content/329/7458/168). It requires estimates appropriate to the patient population and evidence being evaluated, rather than an assumed universal test property.

### Expectation and variance depend on what is averaged

Expectation is a probability-weighted average; variance is the expected squared deviation from that average. Neither identifies the mechanism behind the variation. The law of total expectation lets me average conditional means over groups. The law of total variance separates average variation within groups from variation between their conditional means. For an evidence score, a broad overall spread might therefore reflect device differences even when scores vary little within each device group.

### Conditional independence controls how evidence combines

Two findings are conditionally independent given disease status if knowing one does not change the conditional distribution of the other. Multiplying their individual likelihood ratios requires that factorization under both disease and its absence. Two ultrasound descriptors obtained from the same lesion may share information, so treating them as independent can count similar evidence twice. Conditioning can also introduce associations. If selection for surgery depends on several findings, studying only surgical cases can change how those findings relate.

### A posterior is conditional on a model of the problem

A Bayesian posterior incorporates a prior and a likelihood; it does not remove uncertainty about whether those choices describe the data adequately. Likewise, a neural network's normalized output is not automatically a calibrated probability or a Bayesian posterior over model parameters. Calibration asks whether reported risks agree with observed frequencies in an evaluation population. That population-level agreement still leaves open whether a particular patient's prediction rests on clinically appropriate evidence.

## Where it touches my work

For gallbladder ultrasound AI, I would specify whether the target is existing malignancy, a pathological category, or a management outcome before interpreting any probability. In clinical faithfulness auditing, I would examine how the association between an evidence readout and a clinical factor changes when acquisition conditions or diagnostic categories are considered. I would choose those conditioning variables from a defensible account of how the data arose. Adding more variables does not automatically make the resulting claim more credible.

## What I have not resolved

- Which population provides an appropriate prior when the available labels mainly come from patients selected for surgery?
- How can I identify redundant clinical evidence before combining model outputs with clinician assessments?
- When does conditioning on diagnosis clarify within-class evidence alignment, and when does it remove or distort the clinical relationship I want to study?
