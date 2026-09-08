---
layout: study_note
title: "Confounding in Medical AI"
description: "A third factor driving both the image and the label, and what it does to a performance estimate."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "causality"
category_title: "Causality, Bias & Shortcuts"
order: 1
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-10-02-zech-variable-generalization"
---

A scanner-associated pattern can predict a diagnosis without measuring the abnormality I want the classifier to recognize. I need to identify the pathway producing that association before interpreting performance or clinical-feature alignment.

## Core question and definition

Confounding concerns a particular relationship and causal question. In the simple structure $$A\leftarrow Z\rightarrow Y$$, a common cause $$Z$$ creates an association between $$A$$ and $$Y$$ that does not require an effect of $$A$$ on $$Y$$. A variable does not become a confounder merely because it predicts the label.

In medical AI, “confounded performance” often refers more loosely to a predictor exploiting population or acquisition differences. I would make the distinction explicit. An AUROC can correctly describe discrimination in a sampled hospital mixture while providing weak evidence that the model recognizes disease morphology.

My immediate audit question is usually whether an observed relationship between a model readout and a clinical factor has an alternative explanation. That is different from estimating the biological effect of the factor, and different again from estimating the effect of editing the classifier's input.

## Key concepts

### Replace hospital identity with the mechanisms it summarizes

A hospital identifier may stand for referral patterns, scanner allocation, image processing, reporting conventions, and verification practices. These mechanisms have different positions in a causal account.

For example, a specialist referral service might receive more suspicious gallbladder lesions and use a particular machine. The resulting machine texture can correlate with malignancy because patient routing connects disease prevalence and equipment exposure. Alternatively, a reporting service might use a different label-extraction rule, connecting hospital identity to the recorded label even when underlying disease frequencies are similar.

I would distinguish underlying disease $$D$$ from recorded diagnosis $$Y$$. A pathway into $$Y$$ through report language or reference-standard choice is not equivalent to a pathway into $$D$$. Adding “hospital” to a regression does not explain which process was operating.

### Pooled associations contain a composition term

For nuisance cue $$N$$, outcome $$Y$$, and a discrete grouping variable $$Z$$,

$$
P(Y=1\mid N=n)
=
\sum_z P(Y=1\mid N=n,Z=z)P(Z=z\mid N=n).
$$

Even if $$N$$ adds no information within every group, its pooled association with disease can arise because the groups have different disease frequencies and $$N$$ identifies group membership.

The corresponding issue for an evidence readout can be written using the law of total covariance:

$$
\operatorname{Cov}(A,C)
=
E[\operatorname{Cov}(A,C\mid Z)]
+
\operatorname{Cov}(E[A\mid Z],E[C\mid Z]).
$$

Here, $$A$$ is a scalar model readout and $$C$$ a numerical clinical descriptor. The first term averages within-group covariance. The second measures how their group means move together. A pooled alignment result can therefore be driven by group composition even when within-group alignment is weak.

I would inspect both terms conceptually before assigning clinical meaning to a single correlation coefficient.

### Common causes and downstream decisions are different

Suppose visible irregularity prompts the operator to increase zoom and add calipers. Those acquisition decisions occur downstream of the observed finding. They can become shortcuts, but calling them common-cause confounders of every image-label relationship would obscure their timing.

The appropriate adjustment set depends on the relationship being estimated. [Pearl's overview](https://doi.org/10.1214/09-SS057) explains why causal structure, rather than predictive association alone, determines adjustment.

For my audit, protocol adjustment might ask whether a readout tracks irregularity among similarly acquired images. It would not estimate what the readout would have been if the same lesion had been scanned differently. That stronger claim requires additional assumptions or a paired acquisition design.

### Overlap is a property of the available comparisons

If all suspicious masses were scanned using one protocol and all benign lesions using another, protocol and diagnosis cannot be separated credibly from those observations alone. A regression still returns coefficients, but their interpretation may depend on extrapolation into combinations absent from the data.

I would inspect distributions of lesion morphology, size, visibility, and acquisition settings jointly. “Both machines are represented” is insufficient if comparable clinical presentations are missing from one machine.

Restricting analysis to shared support can improve comparability, but changes the population. I would report which patients were excluded and avoid extending the resulting estimate to presentations removed by that restriction.

## Worked examples in medical AI

### Pneumonia discrimination through hospital recognition

[Zech and colleagues](https://doi.org/10.1371/journal.pmed.1002683) evaluated pneumonia classification using chest radiographs from the NIH Clinical Center, Mount Sinai, and Indiana University. Their experiments connected hospital-identifying information and differences in pneumonia prevalence to variable external generalization.

The important mechanism is not simply that hospitals produce different images. Hospital recognition becomes useful for the diagnostic objective when hospital membership predicts the label. Their engineered prevalence comparisons helped examine that dependency.

I read this as a warning about pooled AUROC. A score that primarily orders hospitals by disease prevalence can correctly rank many positive-negative pairs drawn from different hospitals while offering little discrimination between patients within the same hospital.

For a score $$s$$, AUROC equals the probability that an independently drawn positive receives a higher score than a negative, plus half the probability of a tie. That definition contains no requirement that the ordering use pathology.

### Gallbladder morphology and targeted acquisition

Consider a proposed audit of model attention to an irregular gallbladder wall. Suspicious cases might have targeted, enlarged views, whereas other cases have broad survey images. A readout measuring attribution inside the wall can then increase because the wall occupies more pixels, because image detail changes, or because irregularity itself influences the model.

I would independently annotate irregularity, wall-region area, and assessability, then recover zoom or acquisition information where available. Comparing similarly visible lesions within acquisition groups would challenge the simplest protocol explanation.

The clinical comparison also needs benign structural alternatives. Adenomyomatosis can produce a thickened wall containing intramural cystic spaces, as described by [Bonatti and colleagues](https://pubmed.ncbi.nlm.nih.gov/28127678/). I would include such cases to distinguish generic sensitivity to wall abnormality from sensitivity to the finding relevant to the stated differential.

This remains a proposed observational audit. A residual association after adjustment would not establish which pixels causally drive the prediction.

## Evaluation methods and limitations

### Specify the estimand and adjustment rationale

Before fitting a model, I would write whether the target is overall clinical-factor alignment, alignment within diagnosis, or alignment among comparable acquisition conditions. Those are different estimands.

Conditioning on diagnostic class removes between-class variation. This can reveal whether a readout distinguishes degrees of irregularity within malignant lesions, but it may also discard the variation that made the factor diagnostically useful. I would report the pooled and conditional questions separately.

For confounding analyses, I would draw plausible arrows and justify included covariates. I would also state which variables were unavailable, such as prior clinical suspicion or the reason for selecting a particular transducer.

### Use balancing methods with diagnostics

Matching, stratification, outcome regression, and inverse-probability weighting can support adjusted comparisons. None supplies the missing causal assumptions. Weighting particularly requires attention to overlap and model specification, discussed by [Cole and Hernán](https://pubmed.ncbi.nlm.nih.gov/18682488/).

I would inspect covariate balance after matching or weighting, not assume that applying the method achieved it. For weights $$w_i$$ over $$n$$ observations, a useful concentration diagnostic is

$$
n_{\mathrm{eff}}=\frac{(\sum_{i=1}^{n}w_i)^2}{\sum_{i=1}^{n}w_i^2}.
$$

This effective sample size decreases when a few observations dominate. It is not a replacement for patient-level uncertainty estimation or a correction for unmeasured confounding.

If trimming extreme weights changes the conclusion, I would report the sensitivity and the associated change in the comparison population.

### Separate predictive opportunity from model reliance

A classifier trained only on machine, service, or acquisition metadata measures how much label information those variables contain. A successful metadata baseline does not establish that an image model uses the same information.

Such a result is worth connecting to behaviour on the model itself: performance within acquisition groups, performance when cue and label associations weaken, and controlled edits to a visible cue. An external performance drop alone remains ambiguous because label definitions, disease spectrum, and image quality may change together.

Uncertainty intervals should preserve patient clustering. More frames from the same suspicious lesion do not provide the same independent evidence as more patients with comparable lesions.

## Research connections and open questions

My first question is whether attribution-clinical-factor associations survive adjustment for region area and independently rated visibility within acquisition groups. This requires a modest, blinded annotation study rather than new model training.

Second, I would test whether frame count, caliper presence, or zoom predicts diagnosis beyond machine identity. If so, reconstructing the examination workflow may explain more than a device-level label.

Third, I would map missing combinations explicitly: benign irregular walls on each machine, unmarked suspicious lesions, and marked benign lesions. That map could guide targeted data collection. When overlap is absent, the useful research result is a precise statement of which dependence cannot yet be distinguished, followed by a plan to acquire the missing comparison.

## References

- Pearl, [Causal inference in statistics: An overview](https://doi.org/10.1214/09-SS057), Statistics Surveys 2009.
- Zech et al., [Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs: A cross-sectional study](https://doi.org/10.1371/journal.pmed.1002683), PLOS Medicine 2018.
- Cole and Hernán, [Constructing inverse probability weights for marginal structural models](https://pubmed.ncbi.nlm.nih.gov/18682488/), American Journal of Epidemiology 2008.
- Bonatti et al., [Gallbladder adenomyomatosis: imaging findings, tricks and pitfalls](https://pubmed.ncbi.nlm.nih.gov/28127678/), Insights into Imaging 2017.
