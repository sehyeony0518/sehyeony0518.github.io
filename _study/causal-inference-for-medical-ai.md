---
layout: study_note
title: "Causal Inference for Medical AI"
description: "Causal graphs, mediators and colliders, counterfactuals, and intervention as a language for asking why a feature predicts an outcome."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "causality"
category_title: "Causality, Bias & Shortcuts"
order: 2
source: "Independent study"
written: true
updated: "2026-09-08"
---

Removing a caliper can change a classifier without changing the patient's disease. I use causal inference to keep that computational effect separate from claims about acquisition, diagnosis, and biological mechanisms.

## Core question and definition

A causal question specifies what changes, what outcome is measured, and which population the comparison concerns. “Does this feature cause the prediction?” remains incomplete until the feature and intervention are operationally defined.

For a fixed classifier, I can manipulate an input overlay and observe the resulting score. For a patient, I cannot obtain a second untreated history merely by generating another image. These experiments differ in their units, mechanisms, and identifiable quantities.

Diagnostic evidence also need not cause disease. An imaging finding can be useful because disease produces it. The relevant question for clinical faithfulness is whether the predictor uses evidence appropriate to its diagnostic role, rather than whether every predictive feature lies upstream of pathology.

## Key concepts

### A graph separates processes that the image merges

A directed acyclic graph represents assumed causal relationships. Its arrows specify possible direct effects relative to the included variables; missing arrows assert their absence. D-separation determines which paths are blocked under conditioning. These graphical ideas are developed for epidemiological research by [Greenland, Pearl, and Robins](https://pubmed.ncbi.nlm.nih.gov/9888278/).

For a proposed ultrasound audit, I would distinguish pathology $$D$$, morphology $$M$$, prior clinical concern $$K$$, acquisition settings $$A$$, overlay $$O$$, stored image $$X$$, and model score $$R$$. Candidate pathways include

$$
D\rightarrow M\rightarrow X\rightarrow R,
\qquad
M\rightarrow K\rightarrow O\rightarrow X\rightarrow R.
$$

The second pathway represents documentation responding to a finding. It is a local hypothesis, not a discovered graph.

I would represent verification and the recorded label separately. Pathology exists before a specimen is obtained; whether I observe a pathological diagnosis depends on subsequent clinical decisions.

### Confounders, mediators, and colliders depend on the question

If patient characteristics influence both acquisition choice and the model-visible anatomy, they can confound an acquisition-score comparison. If acquisition changes feature visibility, which changes the score, visibility mediates part of that acquisition effect.

A collider has two incoming arrows on a path. Suppose clinical concern and surgical fitness both influence surgery:

$$
K\rightarrow S\leftarrow F,
$$

where $$S$$ denotes surgery and $$F$$ fitness. Restricting to operated patients can associate concern and fitness through selection. If fitness also influences image quality or case mix, the selected cohort can contain additional associations relevant to the audit.

I would therefore avoid a universal list of “variables to control.” A variable's role changes with the exposure, outcome, and graph. In particular, a measure of visibility may be a mediator in one analysis and a comparability variable in another.

### Observation is not intervention

$$P(R\mid O=o)$$ describes scores among images observed with overlay state $$o$$. $$P(R\mid do(O=o))$$ describes scores under an intervention replacing the usual overlay-generating mechanism. [Pearl](https://doi.org/10.1214/09-SS057) formalizes this distinction.

Observed marked and unmarked images can differ in lesion severity because operators selectively measure suspicious findings. Setting the overlay state for an otherwise fixed input addresses a narrower question that does not inherit all those between-patient differences.

Changing an exported machine logo is likewise an intervention on pixels, not an intervention on the physical scanner. It leaves beam formation, acquisition settings, and patient routing untouched.

### Identification precedes estimation

Let $$A$$ be a well-defined acquisition intervention, $$R(a)$$ the score that would result under setting $$a$$, and $$L$$ measured pre-intervention covariates. Under consistency, conditional exchangeability, and positivity,

$$
E[R(a)]
=
\sum_l E[R\mid A=a,L=l]P(L=l).
$$

Consistency connects an observed score to its corresponding potential outcome. Conditional exchangeability requires $$R(a)\perp A\mid L$$. Positivity requires the acquisition setting to occur with nonzero probability in the relevant covariate strata. For continuous covariates, the sum becomes an integral. [Hernán and Robins](https://miguelhernan.org/whatifbook) develop these identification conditions.

In my setting, “use another machine” may be insufficiently specified if it also changes operator, probe, preset, and saved-view policy. A precise intervention would state which components change and which remain fixed.

### Counterfactual images require preserved background conditions

A structural causal model describes each variable as a function of its causes and background factors. Counterfactual reasoning uses observed evidence to constrain those background factors, changes a mechanism, and derives the alternative outcome.

For ultrasound, an image generator may change speckle, wall shape, and acquisition appearance together. A generated image that reduces a malignancy score is therefore evidence about the generator-classifier combination. Calling it the same patient's benign counterfactual requires a defensible account of what was preserved and why the altered findings could coexist.

I would reserve stronger counterfactual language for interventions whose unit and preserved information I can explain concretely.

## Worked examples in medical AI

### An overlay intervention with observable paired outcomes

Suppose an archive contains identical frozen gallbladder images exported with and without a separately stored annotation layer. Define $$x_i(1)$$ and $$x_i(0)$$ as the marked and unmarked versions for case $$i$$, and $$s_f$$ as the fixed classifier's scalar score.

The paired computational effect is

$$
\Delta_i=s_f(x_i(1))-s_f(x_i(0)).
$$

Unlike mutually exclusive patient treatments, both software inputs can be evaluated. I would verify identical tissue content, dimensions, compression behavior, and preprocessing, then summarize paired effects with patient-level uncertainty.

A positive effect means the marked version raises the selected score. It does not show that calipers cause malignancy, that all annotations have the same effect, or that operator behavior caused the learned dependency.

If only burned-in markers exist, reconstruction adds another mechanism. The contrast then concerns marker removal plus the chosen replacement of hidden pixels.

### Adjusting away the effect of improved visibility

Consider a hypothetical prospective comparison of two ultrasound acquisition protocols for gallbladder wall characterization. A protocol might improve the visibility of small intramural structures, thereby changing a classifier's score.

If the target is the total protocol effect on the score, adjusting for visibility would remove part of the pathway of interest. If the target is sensitivity to acquisition appearance while holding clinical information comparable, a visibility-restricted analysis asks a different question.

I would first collect paired acquisitions with recorded order and reader-rated feature visibility. Even within a patient, probe motion, breathing, and view selection can change what is shown. Pairing reduces between-patient differences but does not isolate a single physical acquisition parameter.

### Clinical diagnosis can include information outside the image

The Tokyo Guidelines 2018 diagnostic framework for acute cholecystitis combines local inflammatory signs, systemic inflammatory signs, and characteristic imaging findings. A selected still frame does not contain that complete clinical assessment. [Yokoe and colleagues](https://pubmed.ncbi.nlm.nih.gov/29032636/) describe the criteria.

I read this as a reason to separate a clinical diagnosis label from a frame-visible finding. If a model predicts that diagnosis using an emergency-service annotation, the cue may encode clinical context unavailable in tissue pixels. Whether that input is appropriate depends on the intended decision, timing, and information contract.

## Evaluation methods and limitations

I would begin each analysis with a short estimand statement naming the unit, intervention, outcome scale, and target population. For an overlay audit, that might be the mean change in malignancy probability when a specified annotation layer is added to otherwise identical, eligible frozen frames.

Next, I would draw alternative plausible graphs before choosing adjustment variables. If one graph treats zoom as a response to suspicion and another treats it as a fixed service protocol, the same adjusted coefficient may have different interpretations. Records of acquisition timing could resolve more than a more flexible estimator.

Randomized assignment is valuable when the intervention can be controlled. Randomizing annotation presentation to the software can identify an input effect under the implemented rendering procedure. Randomizing acquisition order can reduce systematic order effects, although it cannot make two physical scans identical.

I would include sham export, verify preserved information, and report effects on both scores and decisions at a prespecified threshold. A score change and a threshold crossing answer different questions.

Failure to detect an effect does not prove independence. The cue may be redundant with another input, the tested range may be narrow, or the score may be locally saturated. Conversely, a large response to an unrealistic edit can establish sensitivity without establishing clinically meaningful reliance.

## Research connections and open questions

My first tractable question is whether authentic overlay addition changes gallbladder scores when the underlying frozen image is fixed. That needs paired exports and pipeline checks, without requiring a biological causal model.

Second, I would reconstruct whether zoom, Doppler use, and caliper placement preceded or followed recognition of the target finding. This could distinguish routine acquisition variation from a response to suspicion.

Third, I would compare conclusions under two prespecified visibility analyses: the overall paired acquisition effect and the effect among pairs judged to preserve the same findings. Their difference would help quantify how much the proposed acquisition comparison also changes the clinical information available to the model.

## References

- Pearl, [Causal inference in statistics: An overview](https://doi.org/10.1214/09-SS057), Statistics Surveys 2009.
- Greenland, Pearl, and Robins, [Causal diagrams for epidemiologic research](https://pubmed.ncbi.nlm.nih.gov/9888278/), Epidemiology 1999.
- Hernán and Robins, [Causal Inference: What If](https://miguelhernan.org/whatifbook), Chapman & Hall/CRC 2020.
- Yokoe et al., [Tokyo Guidelines 2018: diagnostic criteria and severity grading of acute cholecystitis (with videos)](https://pubmed.ncbi.nlm.nih.gov/29032636/), Journal of Hepato-Biliary-Pancreatic Sciences 2018.
