---
layout: study_note
title: "Calibration, Uncertainty, and Selective Prediction"
description: "Whether a stated probability means what it says, and when a model should abstain."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
order: 8
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-01-27-guo-calibration"
---

A probability estimate should correspond to observed risk, and an uncertain prediction should have a defined route for review. Calibration, uncertainty estimation, and selective prediction address these requirements, but none alone establishes that a model is safe.

## Core question and definition

Calibration concerns agreement between predicted probabilities and observed outcome frequencies in a specified population. Uncertainty estimation concerns limitations in a prediction arising from available evidence and model knowledge. Selective prediction adds a policy for withholding an automated answer when a selection criterion is not satisfied.

I keep these questions separate. A calibrated model can still make many mistakes, and a confident prediction can be wrong. An abstention policy only helps a clinical system if rejected cases receive appropriate handling and the retained predictions remain useful.

## Key concepts

### Calibration is a population property

For a binary outcome, ideal calibration satisfies $$P(Y = 1 \mid \hat{p} = p) = p$$. It concerns outcome frequencies among comparable predictions, not whether an individual patient is partly diseased. [Van Calster and colleagues](https://doi.org/10.1186/s12916-019-1466-7) explain why calibration matters beyond discrimination. Agreement overall can conceal miscalibration in subgroups, and calibration established in one setting need not persist elsewhere.

### Uncertainty depends on the information available

Aleatoric uncertainty refers to variability remaining conditional on the supplied information; epistemic uncertainty concerns limitations in model knowledge. [Kendall and Gal](https://papers.nips.cc/paper_files/paper/2017/hash/2650d6089a6d640c5e85b2b88265dc2b-Abstract.html) develop this distinction for vision models. Additional ultrasound views can reduce ambiguity that was unavoidable in a single frame. Ensemble disagreement may indicate model uncertainty, but agreement does not prove reliability when every member has learned the same shortcut.

### Recalibration changes the probability mapping

Temperature scaling divides logits by a positive parameter fitted on held-out development data, as studied by [Guo and colleagues](https://proceedings.mlr.press/v70/guo17a.html). It changes confidence without changing the highest-logit class. This can improve calibration under the evaluated conditions, but cannot repair missing clinical information or guarantee calibration after a population shift. Fitting and assessing the mapping on the same cases would overstate its demonstrated performance.

### Abstention trades coverage for retained-case risk

Let a(X) equal one when a prediction is accepted and zero otherwise. Coverage is $$E[a(X)]$$, and selective risk is $$E[a(X)\,\ell(f(X), Y)] / E[a(X)]$$ for a specified loss $$\ell$$ and nonzero coverage. [Geifman and El-Yaniv](https://papers.neurips.cc/paper_files/paper/2017/hash/4a8423d5e91fda00bb7e46540e2b0cf1-Abstract.html) study selective classification for deep networks. Lower risk among accepted cases is meaningful only alongside coverage and the consequences for rejected cases.

## Worked examples in medical AI

In a hypothetical gallbladder classifier, predictions from a new scanner remain confident even when performance deteriorates. A familiar confidence distribution would not establish calibration at that site. I would examine observed outcomes and acquisition conditions rather than treat confidence itself as evidence that transfer succeeded.

Another hypothetical examination contains a poorly visualized wall abnormality. Abstention might prompt review of additional views, but this requires a workflow capable of obtaining them. A policy that excludes difficult examinations can improve retained-case metrics while increasing workload or disproportionately withholding assistance from particular patient groups. The complete pathway matters.

## Evaluation methods and limitations

I would examine calibration plots with uncertainty and the distribution of predicted probabilities, including relevant subgroups. A single binned calibration error depends on binning and sample composition. Sparse malignant outcomes limit what a smooth-looking plot can establish. Recalibration should be evaluated on data independent of its fitting.

For selective prediction, I would report risk-coverage curves, class-specific errors, subgroup coverage, and referral workload. The selection score and threshold belong to development. Testing should examine clinically relevant shifts and the handling of rejected cases. A low observed selective risk does not justify an unconditional guarantee about future patients or institutions.

## Research connections and open questions

My clinical faithfulness audits could help explain confident failures in gallbladder models. I would investigate whether rejection reflects limited clinical evidence or sensitivity to acquisition artifacts. Audit findings might inform a selection policy, but that policy would still need independent validation.

- Can clinically annotated evidence availability improve abstention beyond confidence scores alone?
- How should the system handle confident predictions supported by a suspected shortcut?
- Which patients lose access to assistance as coverage decreases, and what happens to their care?

## References

- Van Calster et al., [Calibration: the Achilles heel of predictive analytics](https://doi.org/10.1186/s12916-019-1466-7), BMC Medicine 2019.
- Kendall and Gal, [What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?](https://papers.nips.cc/paper_files/paper/2017/hash/2650d6089a6d640c5e85b2b88265dc2b-Abstract.html), NeurIPS 2017.
- Guo et al., [On Calibration of Modern Neural Networks](https://proceedings.mlr.press/v70/guo17a.html), ICML 2017.
- Geifman and El-Yaniv, [Selective Classification for Deep Neural Networks](https://papers.neurips.cc/paper_files/paper/2017/hash/4a8423d5e91fda00bb7e46540e2b0cf1-Abstract.html), NeurIPS 2017.
