---
layout: study_note
title: "Evaluation Beyond AUROC"
description: "Sensitivity and specificity at the operating point that matters, decision curves, and clinical utility."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
order: 6
source: "Independent study"
written: true
updated: "2026-09-08"
---

AUROC measures how well a model ranks cases across thresholds. Evaluation beyond AUROC asks what happens at the operating point used in care, including missed disease, unnecessary action, and the consequences of both.

## Core question and definition

A model can rank patients well without providing useful probabilities or supporting a worthwhile clinical decision. I therefore separate discrimination, threshold-specific accuracy, calibration, and clinical utility. These are related properties, but one cannot stand in for all the others.

The central question is which consequences follow when a particular output triggers a particular action. A threshold for requesting another view is not interchangeable with a threshold for specialist referral. The evaluation must name the action before deciding what counts as an acceptable error.

## Key concepts

### Ranking leaves the operating point unspecified

AUROC summarizes sensitivity against the false-positive rate across thresholds. It can hide differences within the narrow range relevant to a clinical task. Two models with similar AUROC may have different sensitivity at the specificity required by a service. I would examine that region directly rather than assume that the model with the larger overall area is preferable.

### Sensitivity and specificity describe conditional errors

At a fixed threshold, sensitivity = TP/(TP + FN) and specificity = TN/(TN + FP). They describe detection among patients with disease and exclusion among those without it. The threshold should be selected using development data and clinical requirements, then evaluated independently. Neither quantity is universally constant across populations, because disease severity and the range of alternative diagnoses can change.

### Predictive values connect results to the tested population

Precision, or positive predictive value, is TP/(TP + FP); recall is sensitivity. Predictive values depend on disease prevalence as well as test performance. [Saito and Rehmsmeier](https://pubmed.ncbi.nlm.nih.gov/25738806/) examine precision-recall plots for imbalanced classification. Such plots help describe positive predictions, but they also change with prevalence. I would use them alongside ROC analysis, rather than treat either curve as a complete account of clinical usefulness.

### Decision curves make the tradeoff explicit

In [Vickers and Elkin's decision curve analysis](https://doi.org/10.1177/0272989X06295361), $$\text{net benefit} = \frac{TP}{n} - \frac{FP}{n} \times \frac{p_t}{1 - p_t}$$. Here $$p_t$$ is the threshold probability at which the modeled action becomes worthwhile, and its odds encode the relative weight of false-positive harm against true-positive benefit. This threshold expresses a decision preference; it is not simply the cutoff that maximizes a statistical index. Relevant comparisons include acting on everyone, acting on no one, and existing practice.

## Worked examples in medical AI

Consider a hypothetical gallbladder triage system that recommends specialist review. A highly sensitive threshold may identify more malignant findings while also referring many benign abnormalities. Its value depends on review capacity, delays, and the consequences of missed disease. A favorable AUROC does not reveal whether that referral burden is workable.

A different hypothetical model supports further characterization of an already selected lesion. The disease frequency and competing diagnoses may differ from those in general ultrasound screening. Even with similar sensitivity and specificity, its positive predictive value can differ. A dataset deliberately enriched with malignancy would not directly estimate the number of unnecessary referrals in routine practice.

## Evaluation methods and limitations

I would report sensitivity, specificity, predictive values, and uncertainty at prespecified operating points, together with the underlying patient counts. Examination-level referral burden matters when many frames receive predictions. For enriched datasets, population-level quantities require an appropriate sampling design or justified adjustment to the target population.

Decision curves should cover clinically defensible thresholds and relevant alternatives. Their net benefit is a modeled tradeoff, not observed improvement in patient outcomes. It also depends on valid outcome ascertainment and representative data. Prospective evaluation is needed to learn how clinicians respond, whether recommended actions occur, and whether the complete workflow improves care.

## Research connections and open questions

For my gallbladder work, I would evaluate clinical faithfulness alongside the decision a model supports. Evidence reliance can explain fragility or inappropriate reasoning, but it cannot replace measurement of missed disease, unnecessary follow-up, and performance where the model will actually operate.

- Which operating range reflects a real gallbladder workflow rather than a convenient point on a curve?
- How should patient preferences and service capacity enter the choice of an action threshold?
- Can improved clinical evidence reliance reduce harmful decisions even when overall AUROC changes little?

## References

- Saito and Rehmsmeier, [The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets](https://pubmed.ncbi.nlm.nih.gov/25738806/), PLOS ONE 2015.
- Vickers and Elkin, [Decision Curve Analysis: A Novel Method for Evaluating Prediction Models](https://doi.org/10.1177/0272989X06295361), Medical Decision Making 2006.
