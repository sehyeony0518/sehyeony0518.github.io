---
layout: study_note
title: "Model Reliance on Clinical Evidence"
description: "Moving from an alignment claim to a dependence claim, and what that step requires."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "auditing"
category_title: "Evidence Auditing"
order: 1
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-10-28-degrave-covid-shortcut"
---

A model relies on clinical evidence when its predictions depend on that evidence under a specified comparison. Moving from alignment to reliance requires testing a dependency, rather than showing that a feature and a prediction occur together.

## Core question and definition

The question I want to answer is concrete: if the relevant evidence were changed or unavailable, while other relevant conditions were controlled, how would this model behave? The answer depends on the model, output, patient population, and intervention. “The model uses the wall” leaves each of these unspecified.

Reliance concerns the prediction mechanism. It does not establish that an image feature causes disease, or that a clinician should act on the prediction. A disease can produce an imaging sign that is diagnostically useful even though changing the displayed sign would not change the patient's underlying condition.

## Key concepts

### Association is weaker than dependence

A score may correlate with an independently annotated feature because both track diagnosis, acquisition, or another factor. A representation may also encode the feature without the diagnostic head using it. These observations support alignment or information availability. I would reserve a reliance claim for evidence connecting a controlled change in information to a change in model behavior.

### Reliance needs an operational definition

One possible quantity is R_T(f) = E[ℓ(f(T(X)), Y) − ℓ(f(X), Y)], where T disrupts specified evidence and ℓ measures prediction loss against a fixed reference. Its interpretation depends on whether retaining Y is appropriate for the comparison. [Fisher, Rudin, and Dominici](https://jmlr.org/papers/v20/18-760.html) formalize related reliance measures through feature scrambling. Different transformations define different questions, not interchangeable estimates of one intrinsic importance.

### Local and population reliance differ

A feature can matter strongly for a subset of cases while having little average effect. Score changes can also cancel when averaged with signs intact. I would distinguish effects on individual predictions, changes in classification, and changes in population performance. The output being studied matters: a logit, probability, and thresholded decision can respond differently to the same intervention.

### Redundancy complicates necessity and sufficiency

Removing one useful feature may have little effect when another supplies similar information. Keeping a region while removing the rest may preserve a prediction, but the model may be reacting to the artificial background. Marginal scrambling can create implausible combinations; conditional scrambling asks about information beyond what other features already provide. Neither a null ablation nor apparent sufficiency warrants an unrestricted conclusion.

## Worked examples in medical AI

[DeGrave and colleagues](https://doi.org/10.1038/s42256-021-00338-7) investigated shortcut use in chest-radiograph models for COVID-19 detection. Their study combined several analyses rather than treating accurate classification or a convincing saliency map as evidence of clinically appropriate reasoning. I take this as a methodological example, without assuming that every cue they identified transfers to ultrasound.

In a hypothetical gallbladder audit, a malignancy score might increase with independently rated wall irregularity. That association could reflect useful morphology, or irregular cases might also have more calipers and tighter zoom. Reviewed comparisons with altered overlays would address one candidate dependency. Comparisons that alter wall evidence would address another, but would require much stronger checks that the intended change is isolated.

## Evaluation methods and limitations

I would define primary features and comparisons before examining the results, preserve the deployed preprocessing, and estimate uncertainty at the patient level. Both harmful and clinically appropriate dependencies should be assessed. Robustness to every change is not desirable if some changes remove the evidence needed for diagnosis.

A reliance claim becomes more persuasive when clinical annotation, controlled input changes, and internal analyses agree. These methods can still share errors. A synthetic edit may alter several features; a concept probe may capture a correlate; an explanation may misrepresent the computation. Unchanged predictions may reflect redundancy, saturation, or an ineffective intervention rather than absence of use.

## Research connections and open questions

My central research question is whether gallbladder models depend on independently justified clinical evidence. I would report the scope of each dependency test explicitly, including the cases, perturbations, and outputs for which it supports a conclusion.

- Which interventions can vary a gallbladder feature without changing acquisition quality or related diagnostic evidence?
- How can I distinguish genuine redundancy from a model's failure to use an expected feature?
- What combination of evidence would justify a reliance claim when no realistic isolated intervention is available?

## References

- Fisher, Rudin, and Dominici, [All Models are Wrong, but Many are Useful: Learning a Variable's Importance by Studying an Entire Class of Prediction Models Simultaneously](https://jmlr.org/papers/v20/18-760.html), Journal of Machine Learning Research 2019.
- DeGrave, Janizek, and Lee, [AI for radiographic COVID-19 detection selects shortcuts over signal](https://doi.org/10.1038/s42256-021-00338-7), Nature Machine Intelligence 2021.
