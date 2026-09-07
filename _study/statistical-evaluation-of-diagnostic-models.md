---
layout: study_note
title: "Statistical Evaluation of Diagnostic Models"
description: "Confidence intervals, bootstrapping, power, and the pitfalls that recur in diagnostic accuracy papers."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
order: 5
source: "Independent study"
written: true
updated: "2026-09-08"
---

Statistical evaluation asks how precisely a diagnostic model's performance has been estimated and whether an observed difference supports the claim being made. I treat the sampling unit, target population, and comparison as part of the statistical question.

## Core question and definition

A reported sensitivity or AUROC is an estimate from particular patients, labels, and evaluation conditions. Statistical inference describes uncertainty under assumptions about that process. It does not automatically account for selection bias, a flawed reference standard, or a hospital absent from the study.

Before choosing a test, I would specify the estimand: the quantity I want to estimate. Patient-level sensitivity at a fixed threshold, the paired difference in AUROC between two models, and performance averaged across hospitals require different analyses.

## Key concepts

### Count independent information

Several frames from one patient do not provide the same information as several independent patients. Treating them as independent can make intervals too narrow. If the decision is examination-level, I would first apply the prespecified aggregation rule and evaluate examinations, while accounting for patients with repeated studies. The analysis should preserve the structure that generated the observations.

### Interpret confidence intervals carefully

A frequentist 95% confidence procedure has 95% coverage under its assumptions across repeated samples. After observing one interval, this does not assign a 95% probability to a fixed parameter lying inside it. A narrow interval indicates sampling precision under the analysis, not freedom from systematic error.

### Bootstrap the relevant units

The bootstrap approximates sampling variation through resampling observed data, as developed by [Efron](https://doi.org/10.1214/aos/1176344552). In an examination-based study with repeated observations, I would resample patients and retain their associated records. For paired model comparisons, both models' predictions must travel together. Bootstrapping fixed test predictions measures uncertainty from the test sample; it does not capture variation from retraining the model.

### Plan for precision and meaningful differences

Power concerns the probability of detecting a specified effect under an alternative hypothesis. Precision concerns the expected uncertainty around an estimate. Both require planning before inspecting results. [Buderer](https://pubmed.ncbi.nlm.nih.gov/8870764/) describes how disease prevalence enters sample-size calculations for sensitivity and specificity. The number of disease-positive patients limits sensitivity estimation; additional benign frames cannot compensate for very few malignant cases.

### Match comparisons to the claim

Models evaluated on the same patients produce correlated estimates. [DeLong and colleagues](https://pubmed.ncbi.nlm.nih.gov/3203132/) developed a nonparametric comparison of correlated AUROCs. That method does not by itself resolve clustering from multiple images per patient. A nonsignificant difference does not demonstrate equivalence, and testing many endpoints or subgroups increases opportunities for chance findings. Primary comparisons and any noninferiority margin need prior justification.

## Worked examples in medical AI

Consider a hypothetical gallbladder model that misses no malignant cases in a small test cohort. Its observed sensitivity is perfect, but the estimate remains uncertain. The appropriate conclusion depends on the number and range of malignant cases, the reference process, and the confidence interval, rather than the absence of observed errors alone.

Suppose two models are evaluated on those same patients. I would estimate their paired performance difference directly. Overlap between their separate confidence intervals is not a substitute for that comparison. If the clinical question concerns missed malignancy at a fixed referral burden, a test of overall AUROC answers only part of it.

## Evaluation methods and limitations

I would prespecify the endpoint, operating threshold, comparison, clustering structure, and handling of missing or indeterminate results. Bootstrap resamples with no disease-positive cases can make some metrics undefined when events are sparse. Reporting the resampling method and such failures matters; resampling cannot manufacture information absent from the cohort.

Repeated training runs can assess optimization variability, while resampling the development process addresses a broader source of uncertainty. Neither establishes generalization to unseen institutions without relevant data. I would keep sampling uncertainty, training variability, and uncertainty about applicability separate in the report.

## Research connections and open questions

My clinical faithfulness audits also produce estimates, such as changes after an intervention or associations with annotated findings. These need patient-level uncertainty and prespecified comparisons, particularly when many features, layers, or masking choices are examined.

- Which audit effect would be large enough to change my interpretation of a model's evidence?
- How many independent malignant cases are needed for the precision my intended claim requires?
- Which subgroup analyses are confirmatory, and which should remain explicitly exploratory?

## References

- Efron, [Bootstrap Methods: Another Look at the Jackknife](https://doi.org/10.1214/aos/1176344552), The Annals of Statistics 1979.
- Buderer, [Statistical methodology: I. Incorporating the prevalence of disease into the sample size calculation for sensitivity and specificity](https://pubmed.ncbi.nlm.nih.gov/8870764/), Academic Emergency Medicine 1996.
- DeLong, DeLong, and Clarke-Pearson, [Comparing the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach](https://pubmed.ncbi.nlm.nih.gov/3203132/), Biometrics 1988.
