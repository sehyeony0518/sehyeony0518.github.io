---
layout: study_note
title: "Clinical Workflow and Task Definition for Gallbladder AI"
description: "Deciding which decision a model supports, and letting that decide the label, the metric, and the design."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "hepatobiliary"
category_title: "Hepatobiliary Medicine & Imaging"
subgroup: "Clinical-to-AI Connections"
order: 13
source: "Independent study"
written: true
updated: "2026-09-08"
---

“Gallbladder AI” is not a sufficiently defined task. I would specify the decision, the information available when it is made, and the consequence of an incorrect output before selecting a model or label.

## Clinical overview

A sonographer deciding whether to acquire another view, a radiologist characterizing a mural lesion, and a clinician deciding on referral occupy different points in the same pathway. Their inputs and responsibilities differ even when they see images from the same examination.

I would write an intended-use statement with a patient population, setting, user, prediction time, and proposed action. One feasible example is assisting radiologists with escalation of indeterminate gallbladder wall lesions after a completed ultrasound examination. That task excludes claims about autonomous cancer screening or choosing surgery.

The alternatives also need definition. “Refer” might mean specialist review, targeted repeat ultrasound, or cross-sectional imaging. Those actions have different costs and clinical thresholds. A model cannot be evaluated for referral utility until the action its score is meant to support is explicit.

## Anatomy and pathophysiology

Gallbladder findings represent processes at different levels. Stones are intraluminal material; cystic duct obstruction impairs emptying; acute inflammation produces a clinical syndrome; adenomyomatosis alters wall architecture; carcinoma involves neoplastic tissue growth. Several can coexist.

Consequently, a multiclass label that forces a patient into either “stone” or “cholecystitis” imposes an artificial exclusivity. A stone can be incidental, while cholecystitis can occur without a demonstrated stone. Wall thickening can reflect contraction, edema, fibrosis, inflammation, or neoplasia.

Time links these processes to acquisition. Feeding changes distension, positioning can move luminal material, and treatment can change inflammatory findings. I would attach timestamps to both observations and interventions. A diagnosis established after surgery should not be interpreted as proof that its defining morphology was visible in every earlier frame.

## Diagnostic workflow and imaging findings

### Decide whether the required evidence was acquired

The [AIUM practice parameter](https://doi.org/10.1002/jum.15874) describes long-axis and transverse gallbladder assessment, suitable positioning, and evaluation of relevant biliary findings. Completeness is a property of the examination, while sharpness is a property of particular images.

For a proposed acquisition aid, I would define missing evidence concretely: an unseen neck, absent orthogonal confirmation of a lesion, or no recorded maneuver when mobility is unresolved. The desired output could then request a particular additional view.

A model that receives only selected still images may be unable to determine whether the operator examined a region but did not save it. I would separate acquisition completeness from archive completeness when constructing the reference.

### Annotate findings before interpreting the syndrome

For each target, I would preserve location, size, attachment, mobility, shadowing, adjacent wall architecture, and whether internal flow was assessable. Reader labels should distinguish absent, present, and unassessable findings. This is my proposed scheme for retaining uncertainty.

A hypothetical echogenic gallbladder focus without a visible shadow is not yet a polyp. A second view may show its attachment, while repositioning may demonstrate mobility. Assigning a disease label from the first frame alone would conceal the evidence that resolved the differential.

Measurement tasks also need a physical definition. Wall thickness measured obliquely or including adjacent liver is not the same quantity as thickness measured perpendicular to the local wall. Pixel agreement cannot compensate for inconsistent anatomical endpoints.

### Identify what the clinical diagnosis adds

The [Tokyo Guidelines 2018](https://pubmed.ncbi.nlm.nih.gov/29032636/) organize acute cholecystitis diagnosis around local inflammatory signs, systemic inflammation, and characteristic imaging. A suspected diagnosis uses local and systemic findings; characteristic imaging contributes to a definite diagnosis.

For example, a shadowing neck stone with wall thickening may be visible on ultrasound, while fever, inflammatory laboratory results, and focal tenderness establish additional clinical context. A still-image classifier does not directly observe those measurements.

I would therefore distinguish a model detecting cholecystitis-associated imaging findings from a multimodal model estimating the clinical diagnosis. Comparing them against the same outcome can be useful, provided the different information sets are stated.

### Fix the prediction time and next action

For an escalation aid, the index time might be completion of the first ultrasound, before CT, MRI, surgery, or pathology. Only information available then should enter the predictor.

The reference can use later evidence, but it must answer the intended question. Pathology can establish malignancy; an expert panel can judge whether further characterization was warranted. Those labels can disagree without either being erroneous: a benign lesion may reasonably require additional investigation because its initial appearance was indeterminate.

## Differential diagnosis and management context

The relevant negative cases are not only normal gallbladders. Sludge, folds, adenomyomatosis, inflammatory thickening, and xanthogranulomatous cholecystitis test whether a model can handle plausible malignant mimics. Including these cases changes the difficulty and clinical meaning of specificity.

For incidental polyps and wall thickening, the [2025 KSAR recommendations](https://doi.org/10.3348/kjr.2024.0914) tie workup to imaging features and context. I would record the guideline version if recommendations become part of the study reference.

Actual surgery is influenced by symptoms, concern for malignancy, operative fitness, preferences, and access. It is therefore an outcome of decision-making, not a pure tissue label. Training a model to reproduce surgery decisions can reproduce these influences even if the stated purpose is cancer detection.

Absence of surgery also leaves some diagnoses unresolved. I would define acceptable follow-up and adjudication before analysis, keeping patients with insufficient verification visible in the participant flow rather than silently labeling them benign.

## Implications for medical AI

### Match the reference to the output

I would separate three initial studies. An acquisition aid would use reader assessment of missing views or unassessable features. A measurement aid would use a standardized measurement protocol and repeated reader measurements. A malignancy aid would use a documented diagnostic reference at the patient or matched-lesion level.

For wall measurements, mean error captures systematic overmeasurement or undermeasurement, while [Bland-Altman analysis](https://pubmed.ncbi.nlm.nih.gov/2868172/) can describe agreement across the measurement range. Correlation alone is insufficient because a model can correlate closely with readers while consistently overestimating thickness.

For malignancy assessment, I would prespecify aggregation across frames and lesions. Choosing the most suspicious frame after seeing pathology would allow information unavailable in the intended workflow to determine the test input.

### Define the operating point in clinical units

For a fixed threshold, let $$TP$$, $$FP$$, $$TN$$, and $$FN$$ denote patient counts against a binary malignancy reference. Then sensitivity is $$TP/(TP+FN)$$, specificity is $$TN/(TN+FP)$$, and positive predictive value is $$TP/(TP+FP)$$.

Sensitivity measures detected malignancies; positive predictive value describes the proportion of positive predictions confirmed malignant. False positives per 100 examined patients are $$100FP/N$$, where $$N=TP+FP+TN+FN$$. That workload measure differs from the false-positive rate $$FP/(FP+TN)$$.

A benign patient escalated appropriately because of unresolved imaging is still a false positive against a malignancy endpoint. I would not automatically call that an unnecessary referral. Clinical appropriateness needs its own assessment.

A probability model also needs calibration in the intended population. A case-control sample enriched for cancer cannot directly establish the positive predictive value expected in routine practice.

### Evaluate a decision rather than only ranking

For a binary escalation decision tied to a specified disease endpoint, [Vickers and Elkin's decision curve analysis](https://doi.org/10.1177/0272989X06295361) defines net benefit at threshold probability $$p_t$$ as

$$
NB(p_t)=\frac{TP(p_t)}{N}-\frac{FP(p_t)}{N}\frac{p_t}{1-p_t}.
$$

Here $$0<p_t<1$$, and $$p_t/(1-p_t)$$ represents the relative weight assigned to a false-positive action. Counts change as the threshold changes. I would compare the model with escalating everyone, escalating no one, and the existing pathway where measurable.

The threshold range must reflect the actual action. Further ultrasound and surgery do not share one harm tradeoff. Net benefit against malignancy also does not capture every legitimate reason for referral or establish observed patient benefit.

### Audit workflow cues and human use

Suspicious lesions may receive calipers, magnification, additional Doppler views, and more saved frames. These features can encode the operator's prior concern. I would test whether they predict labels and whether performance persists within comparable documentation groups.

All examinations from one patient should remain in one data partition. Confidence intervals should account for patient clustering instead of treating correlated frames as independent observations.

My first study question would be whether a model adds useful discrimination among lesions already considered indeterminate by readers. A second would test whether showing feature-specific uncertainty improves escalation decisions compared with displaying a probability alone.

The [DECIDE-AI guideline](https://doi.org/10.1038/s41591-022-01772-9) addresses early clinical evaluation, including human interaction. I would examine accepted and overridden suggestions, missed actionable findings, additional investigations, and user errors. Retrospective accuracy cannot show whether the interface helps clinicians recognize the model's limitations.

## References

- AIUM, [The AIUM Practice Parameter for the Performance of an Ultrasound Examination of the Abdomen and/or Retroperitoneum](https://doi.org/10.1002/jum.15874), Journal of Ultrasound in Medicine 2022.
- Yokoe et al., [Tokyo Guidelines 2018: diagnostic criteria and severity grading of acute cholecystitis (with videos)](https://pubmed.ncbi.nlm.nih.gov/29032636/), Journal of Hepato-Biliary-Pancreatic Sciences 2018.
- Vasey et al., [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9), Nature Medicine 2022.
- Chang et al., [Interpretation, Reporting, Imaging-Based Workups, and Surveillance of Incidentally Detected Gallbladder Polyps and Gallbladder Wall Thickening: 2025 Recommendations From the Korean Society of Abdominal Radiology](https://doi.org/10.3348/kjr.2024.0914), Korean Journal of Radiology 2025.
- Vickers and Elkin, [Decision curve analysis: a novel method for evaluating prediction models](https://doi.org/10.1177/0272989X06295361), Medical Decision Making 2006.
- Bland and Altman, [Statistical methods for assessing agreement between two methods of clinical measurement](https://pubmed.ncbi.nlm.nih.gov/2868172/), Lancet 1986.
