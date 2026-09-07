---
layout: study_note
title: "Adenomyomatosis and Gallbladder Wall Thickening"
description: "The benign causes of a thick gallbladder wall, the comet-tail artifact, and the differential it opens."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "hepatobiliary"
category_title: "Hepatobiliary Medicine & Imaging"
subgroup: "Gallbladder Disease"
order: 6
source: "Independent study"
written: true
updated: "2026-09-08"
---

Adenomyomatosis is a benign gallbladder wall alteration characterized by mucosal outpouchings into the wall. Wall thickening is the broader imaging finding, with causes ranging from physiological contraction and systemic edema to inflammation and malignancy.

## Clinical overview

Adenomyomatosis is often found incidentally, although it can coexist with stones or symptoms that prompt examination. Its importance lies partly in its resemblance to other mural abnormalities. I distinguish recognizing a characteristic benign pattern from explaining the patient's pain: the imaging diagnosis does not automatically identify the symptomatic process.

## Anatomy and pathophysiology

Mucosal invaginations form intramural spaces called Rokitansky-Aschoff sinuses. These may contain bile, concentrated material, cholesterol crystals, or calcification. Adenomyomatosis can involve the fundus, a segment of the gallbladder, or the wall diffusely. Segmental involvement can narrow the lumen into an hourglass configuration. [Bonatti and colleagues](https://doi.org/10.1007/s13244-017-0544-7) describe these anatomical patterns and their imaging correlates.

Wall thickening outside adenomyomatosis has several mechanisms. Inflammation can cause edema and hyperemia; chronic injury can produce fibrosis; neoplasia can infiltrate and disrupt wall architecture. Hepatitis, venous congestion, renal disease, and low serum albumin can accompany diffuse gallbladder edema without primary gallbladder inflammation. These intrinsic and extrinsic causes are organized in the approach by [Gupta and colleagues](https://doi.org/10.3748/wjg.v26.i40.6163).

## Diagnostic workflow and imaging findings

### Confirm that thickening is real

Preparation and distension should be reviewed before interpreting a thick wall. A contracted gallbladder after eating can create apparent thickening. The wall should be examined perpendicular to the beam across multiple planes, with focal and diffuse involvement distinguished. A single oblique measurement cannot describe the process adequately. I would record whether the abnormality is reproducible and whether the lumen was sufficiently distended for assessment.

### Search within the wall

Small intramural cystic spaces are a central clue to adenomyomatosis. A higher-frequency transducer, appropriate focus, and additional views can help resolve them when the wall is accessible. The inner and outer contours should also be inspected. An echogenic focus merely adjacent to the wall is less informative than one demonstrably contained within it. Luminal stones and wall lesions can overlap in projection.

### Interpret comet-tail and twinkling artifacts

Closely spaced repeated echoes behind reflective material can form a tapering comet-tail artifact. In adenomyomatosis, this can arise from material within Rokitansky-Aschoff sinuses. Color Doppler may show twinkling behind reflective interfaces; this is an artifact rather than proof of blood flow. These findings support the diagnosis in the appropriate mural pattern, but they should not substitute for examining the entire abnormality.

### Look for findings that challenge a benign interpretation

Irregular asymmetric thickening, disrupted wall layering, an associated solid mass, or apparent extension into adjacent tissue warrants further assessment. Conversely, preserved layering and intramural cysts favor some benign processes but do not guarantee that every part of the gallbladder is benign. Acute symptoms, surrounding fluid, stones, and generalized edema help place the wall finding in context. Severe inflammation can also look infiltrative.

### Use further imaging to answer the remaining question

MRI can demonstrate fluid-containing intramural spaces, sometimes producing the T2-bright “pearl necklace” appearance. This sign may be inconspicuous when the spaces are small or contain concentrated material. For inconclusive ultrasound, limited visualization, or suspected malignancy, the [2025 KSAR recommendations](https://doi.org/10.3348/kjr.2024.0914) support considering CT or MRI. I would choose further imaging to answer the unresolved question.

## Differential diagnosis and management context

The differential includes acute and chronic cholecystitis, systemic edema, xanthogranulomatous cholecystitis, and gallbladder cancer. Xanthogranulomatous inflammation can be particularly difficult to distinguish from malignancy. For incidentally detected adenomyomatosis with typical imaging features, KSAR does not recommend routine follow-up. That recommendation should not be extended to an indeterminate lesion or used to dismiss coexisting suspicious findings. Symptoms and diagnostic uncertainty may lead to surgical assessment.

## Implications for medical AI

I read this differential as a reason to separate “wall thickening” from its proposed cause. A model can detect thickness while failing to distinguish edema, intramural cysts, and infiltrative tissue. Those are different clinical tasks and require different reference labels.

For my gallbladder ultrasound auditing, I would annotate the location of cystic spaces and artifacts, wall architecture, distension, and competing inflammatory findings. This suggests a specific faithfulness question: does the model use comet-tail evidence in its anatomical context, or has it learned that any bright trailing pattern means benign disease? Cases containing both characteristic benign findings and a separate suspicious lesion would be especially informative.

## References

- Bonatti et al., [Gallbladder adenomyomatosis: imaging findings, tricks and pitfalls](https://doi.org/10.1007/s13244-017-0544-7), Insights into Imaging 2017.
- Gupta et al., [Imaging-based algorithmic approach to gallbladder wall thickening](https://doi.org/10.3748/wjg.v26.i40.6163), World Journal of Gastroenterology 2020.
- Chang et al., [Interpretation, Reporting, Imaging-Based Workups, and Surveillance of Incidentally Detected Gallbladder Polyps and Gallbladder Wall Thickening: 2025 Recommendations From the Korean Society of Abdominal Radiology](https://doi.org/10.3348/kjr.2024.0914), Korean Journal of Radiology 2025.
