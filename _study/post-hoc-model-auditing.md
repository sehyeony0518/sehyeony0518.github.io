---
layout: study_note
title: "Post-hoc Model Auditing"
description: "Auditing a model as it stands, and what a structured audit of a deployed system contains."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "auditing"
category_title: "Evidence Auditing"
order: 2
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-08-04-medical-algorithmic-audit"
  - "2025-10-02-zech-variable-generalization"
---

An audit starts with a system version and a clinical claim that could be wrong. I want its output to identify reproducible failure conditions, their consequences, and the evidence needed to decide what happens next.

## Core question and definition

Post-hoc auditing examines an existing model and its surrounding workflow after development. It can occur before deployment, during a silent prospective evaluation, or after clinicians begin using the output. “Post-hoc” does not restrict the audit to explanation methods.

I would define the audited object as the whole prediction pathway: input eligibility, image selection, preprocessing, checkpoint, aggregation across frames, threshold, displayed result, and handling of missing or rejected inputs. A checkpoint can behave as expected while the application selects the wrong series or converts a failed inference into an apparently negative result.

[Liu and colleagues](https://pubmed.ncbi.nlm.nih.gov/35396183/) organize the medical algorithmic audit around possible errors, contributing system components, and clinical consequences. I use that framework to connect measurements to failure hypotheses, rather than to produce a checklist whose completion implies certification.

## Key concepts

### Translate intended use into observable requirements

“Detect gallbladder malignancy” leaves the population and decision unresolved. A system that scores clinician-selected lesion images addresses a different task from one that searches an entire examination. Its validation denominator must reflect that distinction.

For a hypothetical lesion-characterization system, I would specify who selects the images, whether measurements already exist, which presentations are eligible, and how a score influences further review. I would then translate the claim into requirements: correct patient linkage, defined behavior for inadequate visualization, patient-level discrimination, interpretable probability estimates, and traceable handling of technical failures.

An audit also needs access boundaries. Output-only access permits performance and paired-input tests. Internal access adds representation and parameter checks. Training records permit leakage and provenance investigations. Missing access limits particular conclusions; it does not make every other test impossible.

### Freeze the pathway, including apparently minor transformations

I would record checkpoint and code identifiers, image decoding, grayscale conversion, resizing, normalization, crop rules, and patient-level aggregation. Reproducing a result requires knowing whether the score is the maximum, mean, or another function of frame outputs.

That distinction can create a concrete failure mechanism. A maximum-score rule gives examinations with more frames more opportunities to exceed a threshold. If suspicious lesions also receive more saved images, frame count and disease can become entangled. I would test the actual aggregation rule and examine performance by frame count.

Preprocessing can also mediate an intervention. Removing a bright marker may change image-wide normalization statistics, altering every normalized tissue pixel. I would retain intermediate images to determine whether an apparent marker effect occurs through local content, global preprocessing, or both.

### Separate the deployment denominator from an enriched audit set

A consecutively sampled cohort estimates behavior across the intended stream of examinations. A deliberately enriched challenge set investigates uncommon but important failures. I would maintain both when feasible, but not estimate deployment prevalence or predictive values from an unweighted challenge set.

The data flow should retain counts of eligible patients, exclusions, missing images, rejected inputs, successful predictions, and available reference outcomes. Reporting accuracy only for successfully processed, definitively labeled cases can conceal failures at both ends of the pathway.

Reference ascertainment needs its own map. Pathology may be available mainly after surgery; other cases may rely on follow-up or imaging review. If concerning predictions influence who receives definitive verification, observed performance can become entangled with the system's clinical use.

### Findings need evidence and a retest condition

For each finding, I would record the affected version, triggering condition, observed behavior, comparator, patient count, uncertainty, plausible mechanism, and unresolved alternatives. The proposed response should follow the demonstrated failure.

For example, unexplained score changes after export would motivate examination of decoding and preprocessing. Poor calibration after referral-pattern changes would motivate a separately evaluated recalibration proposal. Neither observation alone proves that retraining will solve the problem.

I would assign follow-up ownership and define what evidence would close the finding. Any mitigation creates a new evaluated version. Keeping the original cases permits regression testing, while fresh cases are needed to assess generalization after repeated fixes.

## Worked examples in medical AI

### Hospital identity masquerading as pneumonia evidence

[Zech and colleagues](https://doi.org/10.1371/journal.pmed.1002683) evaluated pneumonia classifiers using chest radiographs from NIH, Mount Sinai, and Indiana University. Disease prevalence differed across sources, and networks could identify hospital-related information. Their controlled changes to source-specific prevalence helped investigate why pooled internal performance could overstate transportability.

The mechanism is more specific than “external data are different.” A model can infer the source and assign a higher disease score to images from a source with higher label prevalence. It can thereby improve ranking across the pooled dataset without equivalent improvement within each source.

I read this as a model for audit reasoning: locate a performance discrepancy, formulate a source-related hypothesis, then design a comparison that changes the hypothesized association. The external AUROC identifies a problem; it does not by itself explain it.

### A gallbladder system receiving the wrong clinical input stream

Consider a proposed malignancy model developed from selected lesion frames but connected to a service that forwards all gallbladder images. Routine views, inadequately visualized walls, and images from acute inflammatory presentations may now enter the classifier.

The mismatch begins before inference. I would reconstruct which images actually arrived, compare them with the development eligibility rules, and review false positives and false negatives by presentation and visibility. A good result on a retrospectively curated lesion set would not resolve this input-selection failure.

Clinical review must also distinguish the image task from the complete diagnosis. The [Tokyo Guidelines 2018](https://pubmed.ncbi.nlm.nih.gov/29032636/) assess acute cholecystitis through local inflammatory signs, systemic inflammation, and imaging. I read this as a reminder that an image-only model does not receive every component supporting an examination-level clinical label.

My audit would preserve that distinction when reviewing an inflammatory case called suspicious by the model. The error could involve unsupported extrapolation, overlapping visible morphology, missing clinical context, or an unsuitable target label. A heatmap cannot choose among these explanations.

## Evaluation methods and limitations

### Measure decisions as well as ranking

I would report AUROC alongside precision-recall performance and threshold-specific sensitivity, specificity, and predictive values. Precision-recall results and predictive values depend on prevalence, so cohort construction belongs beside the metrics.

For patient probabilities $$p_i$$ and binary outcomes $$y_i$$, the Brier score is

$$
\mathrm{BS}=\frac{1}{n}\sum_{i=1}^{n}(p_i-y_i)^2.
$$

Here $$n$$ is the number of evaluated patients. This is an overall probability-error measure, not a pure calibration statistic. I would supplement it with a calibration curve and, where sample size permits, calibration intercept and slope. Any threshold should be fixed before evaluating the audit cohort.

Confidence intervals should preserve patient clustering. Subgroup tables need event counts, technical-failure counts, and uncertainty, including groups too sparse for stable estimates. A favorable point estimate from a small machine subgroup is an evidence gap, not demonstrated equivalence.

### Use error review to generate testable mechanisms

I would sample correct predictions as well as errors, with reviewers initially blinded to the model result where practical. Otherwise, correct predictions may escape scrutiny even when they depend on a fragile cue.

A predefined review form would capture finding visibility, competing diagnoses, overlays, field of view, acquisition group, and reference-standard uncertainty. Exploratory clusters could then motivate controlled edits or additional sampling. I would distinguish these generated hypotheses from the prespecified primary analyses.

### Evaluate the interaction once outputs are visible

Silent prospective evaluation can test the live input stream while withholding model outputs from clinical decisions. It cannot measure how clinicians respond to those outputs.

Once the system is used, I would examine overrides, additional review, time demands, and decisions following discordant model and clinician assessments. [DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9) provides reporting guidance for early live evaluation, including human factors and clinical context. It is not evidence that a system improves outcomes merely because those items are reported.

Monitoring also faces delayed and selective labels. Changes in score distributions can trigger investigation, but cannot distinguish prevalence change, acquisition change, and performance deterioration without additional information.

## Research connections and open questions

My first audit question is whether the actual gallbladder input stream matches the claimed lesion-characterization task. I can compare export logs, saved series, and blinded image review before interpreting any explanation.

Second, does patient-level error vary with frame count under the deployed aggregation rule? Subsampling existing examinations under a prespecified protocol could reveal sensitivity to documentation intensity, while preserving the full-examination analysis as primary.

Third, which reference outcomes are missing, and does missingness align with score, presentation, or management pathway? Mapping those patterns would identify where additional follow-up is needed. It would also prevent an apparently favorable audit from resting mainly on the subset selected for definitive verification.

## References

- Liu et al., [The medical algorithmic audit](https://pubmed.ncbi.nlm.nih.gov/35396183/), The Lancet Digital Health 2022.
- Zech et al., [Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs: A cross-sectional study](https://doi.org/10.1371/journal.pmed.1002683), PLOS Medicine 2018.
- Vasey et al., [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9), Nature Medicine 2022.
- Yokoe et al., [Tokyo Guidelines 2018: diagnostic criteria and severity grading of acute cholecystitis (with videos)](https://pubmed.ncbi.nlm.nih.gov/29032636/), Journal of Hepato-Biliary-Pancreatic Sciences 2018.
