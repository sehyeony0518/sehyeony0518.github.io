---
layout: study_note
title: "Robustness, Subgroup Performance, and External Validation"
description: "Robustness to acquisition variability, subgroup analysis, and multi-center validation as tests of generalizability."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
order: 10
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-12-13-seyyed-kalantari-underdiagnosis"
  - "2025-10-02-zech-variable-generalization"
---

Robustness concerns whether a model maintains useful behavior under specified changes in its inputs or setting. Subgroup analysis and external validation test different parts of that claim: for whom the model works, and where its performance carries over.

## Core question and definition

I would ask which changes a model should tolerate without losing the clinical information needed for its task. A different scanner preset, a subtle lesion subtype, and a new referral population are not interchangeable perturbations. Each can change the relationship between images, labels, and decisions in a different way.

Generalizability is therefore a claim about particular target settings, not a property established once for a model. A convincing evaluation identifies those settings and makes the remaining gaps visible.

## Key concepts

### Robustness requires a clinically valid change

For a transformation T that preserves the relevant evidence, I may expect f(T(x)) to remain close to f(x). That expectation fails if T removes a lesion, obscures its margin, or changes diagnostically meaningful contrast. In ultrasound, synthetic brightness changes are only partial approximations to acquisition variability. A perturbation test needs a reason to believe that the intended answer should remain stable.

### Averages depend on the mixture of patients

For a loss ℓ and mutually exclusive groups G, overall risk equals Σ_g P(G = g) E[ℓ | G = g]. A large, easier group can dominate this average. I would examine clinically important subtypes alongside demographic and acquisition groups. Similar AUROC across groups also does not establish similar sensitivity at the deployed threshold, calibration, or consequences of error.

### External validation has a defined scope

External testing evaluates a model in data separated from development by a meaningful source boundary. A study involving several hospitals is not automatically an external validation if every hospital contributes to training and testing. I would distinguish pooled patient splits from held-out institutions and later time periods, while documenting differences in eligibility, reference standards, and acquisition.

### Stable performance does not establish stable evidence use

A model might perform consistently because the same shortcut persists across the evaluated sites. Conversely, a clinically grounded model may struggle when image quality genuinely limits visibility. Robustness and clinical faithfulness therefore need related but separate tests. An unchanged score cannot tell me which evidence supported individual predictions.

## Worked examples in medical AI

[Zech and colleagues](https://doi.org/10.1371/journal.pmed.1002683) evaluated pneumonia classification across hospital systems and showed that site-associated information could support prediction when disease prevalence differed between sources. Their findings make pooled multicenter accuracy difficult to interpret without examining performance within and outside those sources.

[Seyyed-Kalantari and colleagues](https://doi.org/10.1038/s41591-021-01595-0) reported underdiagnosis disparities across patient groups in chest-radiograph models. I read this as a reason to inspect conditional errors rather than rely on aggregate performance. The observed disparity still needs interpretation in light of labels, case mix, and clinical workflow; a subgroup difference alone does not identify its causal mechanism.

## Evaluation methods and limitations

For a hypothetical gallbladder study, I would prespecify relevant groups such as scanner family, examination quality, lesion presentation, and referral setting. Patient-level confidence intervals, group sample sizes, and malignant-case counts would accompany the metrics. Intersectional analysis may reveal failures hidden within broad categories, but sparse groups and many comparisons limit certainty. Exploratory findings need confirmation.

External evaluation should first assess the frozen pipeline, including preprocessing, calibration, and thresholds. Any local adaptation should be reported as a separate evaluation stage. Real acquisition variation and controlled perturbations offer complementary evidence, but neither supplies an exhaustive stress test. A collection of similar hospitals can still leave the intended deployment population poorly represented.

## Research connections and open questions

For gallbladder ultrasound, I want to examine whether clinical evidence reliance remains stable across devices and patient groups, alongside diagnostic performance. That would help distinguish tolerance of nuisance variation from continued success through an acquisition correlate.

- Which acquisition changes preserve the sonographic findings my model is expected to use?
- Which clinically important subgroups are absent from the labels currently available to me?
- How many genuinely different external settings are needed to support the scope of my intended claim?

## References

- Zech et al., [Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs: A cross-sectional study](https://doi.org/10.1371/journal.pmed.1002683), PLOS Medicine 2018.
- Seyyed-Kalantari et al., [Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations](https://doi.org/10.1038/s41591-021-01595-0), Nature Medicine 2021.
