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

Gallbladder assessment is a sequence of clinical decisions: whether the examination is adequate, what findings are present, what they mean, and what should happen next. A useful AI task has to identify the particular decision it is intended to support.

## Clinical overview

The same ultrasound appearance can enter different pathways. A stone found during an unrelated examination, a stone in a patient with acute inflammatory symptoms, and a mural lesion found during follow-up do not create the same immediate decision. Symptoms, previous findings, laboratory results, and the reason for referral establish the clinical problem.

I would therefore begin a task definition with the intended patient group, clinical setting, user, and point of use. An acquisition aid used by a sonographer answers a different question from a radiologist's characterization aid or a clinician's referral support. This is my proposed framing for a study.

## Anatomy and pathophysiology

The relevant processes include mobile intraluminal material, cystic duct obstruction, mural inflammation, benign wall remodeling, and neoplastic growth. A thick wall can reflect inflammation, contraction, edema, or tumor; a stone can be incidental or involved in an acute episode. Anatomy and physiological state constrain what an image finding means.

Time also matters. Gallbladder distension changes with feeding, sludge can move, and treatment can change inflammation. A later diagnosis does not establish what was visible at the first scan. I keep disease state, observed finding, and later outcome separate when reconstructing a case.

## Diagnostic workflow and imaging findings

### Establish whether the examination can answer the question

The gallbladder should be assessed across suitable planes, including the neck and fundus, with relevant position changes and documentation of limitations. These principles follow the [AIUM practice parameter](https://doi.org/10.1002/jum.15874). An obscured neck cannot be treated as evidence that no neck stone exists. If a finding requires mobility assessment, the examination must actually include repositioning rather than infer movement from a static frame.

### Record findings before compressing them into a diagnosis

The report should distinguish stones and sludge from attached lesions, describe focal or diffuse wall change, and record relevant posterior acoustics and Doppler findings. A lesion's size, attachment, margins, and adjacent wall should remain available for interpretation. I would preserve uncertainty when a feature is not demonstrable, rather than force every finding into present or absent.

### Combine image evidence with the clinical syndrome

Acute cholecystitis is assessed using local signs, systemic inflammation, and characteristic imaging, as set out in the [Tokyo Guidelines 2018](https://pubmed.ncbi.nlm.nih.gov/29032636/). Focal tenderness under the transducer and inflammatory blood tests contribute evidence beyond grayscale morphology. Conversely, detecting a stone does not establish active inflammation. The clinical diagnosis therefore cannot always serve as a direct claim about what a selected image contains.

### Identify the next decision and its alternatives

Possible next steps include completing a limited examination, comparing prior studies, obtaining further characterization, arranging surveillance, or seeking surgical assessment. The choice depends on the finding and clinical context. I would state the pending decision explicitly, such as whether an indeterminate mural lesion needs further characterization.

## Differential diagnosis and management context

Sludge, folds, adenomyomatosis, inflammatory thickening, and malignancy can overlap in selected views. Management also depends on symptoms, patient suitability, and information obtained elsewhere in the workup. A surgical decision is therefore not a pure pathological label: it incorporates uncertainty, competing risks, and preferences. Similarly, absence of surgery does not establish that a lesion was definitively benign.

## Implications for medical AI

My proposed design would let the decision determine the reference and metric. An acquisition aid needs expert assessment of examination completeness and evaluation of repeat-scan burden. A wall-measurement aid needs a defined measurement protocol and assessment of bias and agreement. A referral aid needs a specified reference outcome, sensitivity for actionable findings, false-referral burden, and calibration at the intended operating point. These are my proposed evaluation choices.

For clinical faithfulness auditing, I would define which evidence is available at prediction time and which findings should support the output. Patient-level data separation, explicit handling of unassessable views, and inclusion of difficult mimics would follow from that definition. Retrospective discrimination would remain insufficient to establish clinical benefit. [DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9) emphasizes evaluating decision support in its actual clinical setting, including human interaction. I would want to know whether the tool changes decisions appropriately and whether its errors remain detectable by the intended user.

## References

- AIUM, [The AIUM Practice Parameter for the Performance of an Ultrasound Examination of the Abdomen and/or Retroperitoneum](https://doi.org/10.1002/jum.15874), Journal of Ultrasound in Medicine 2022.
- Yokoe et al., [Tokyo Guidelines 2018: diagnostic criteria and severity grading of acute cholecystitis (with videos)](https://pubmed.ncbi.nlm.nih.gov/29032636/), Journal of Hepato-Biliary-Pancreatic Sciences 2018.
- Vasey et al., [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9), Nature Medicine 2022.
