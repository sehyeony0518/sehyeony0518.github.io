---
layout: study_note
title: "Imaging Across Modalities and Radiology-Pathology Correlation"
description: "When ultrasound leads to CT, MRI, or MRCP, and how imaging appearances map back to pathology."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "hepatobiliary"
category_title: "Hepatobiliary Medicine & Imaging"
subgroup: "Biliary Disease"
order: 12
source: "Independent study"
written: true
updated: "2026-09-08"
---

A sonographic shadow, a CT enhancement pattern, and a microscopic tissue section are different measurements of a lesion. I use radiology-pathology correlation to ask which tissue process could generate each observation and whether the observations actually refer to the same target.

## Clinical overview

Additional imaging is most useful when it resolves a named uncertainty. After ultrasound, that might be whether a luminal focus moves, whether thickened wall contains intramural cysts, whether a duct is obstructed, or whether a mass extends into liver. “Further characterization” should identify which of these questions remains open.

A later examination is not automatically a better measurement of every feature. Ultrasound provides dynamic observations; CT surveys anatomical extent; MRI samples several tissue properties; pathology examines tissue directly but only where material was obtained and sectioned.

I would record the clinical question at each step. Otherwise, an investigation ordered for staging can be misread as having independently verified a subtle finding that its protocol was never designed to evaluate.

## Anatomy and pathophysiology

### Translate appearances through tissue mechanisms

On ultrasound, echo strength depends on acoustic interfaces and scattering, while posterior shadowing reflects reduced transmission beyond an attenuating or strongly reflecting structure. CT attenuation depends on tissue composition and acquisition conditions; contrast enhancement adds information about vascular delivery and extracellular distribution. MRI signal changes with sequence, relaxation properties, diffusion weighting, and contrast administration.

These measurements can support a common interpretation without matching visually. Edematous wall can be thick and relatively low in CT attenuation, while fluid-sensitive MRI highlights its water content. Fibrosis can alter delayed enhancement. Necrosis produces nonviable regions whose appearance differs from the viable tissue around them.

I would avoid translating “bright” across modalities without specifying the measurement. A bright ultrasound focus and a bright T2-weighted focus do not imply the same material.

### Adenomyomatosis supplies a structural correspondence

Rokitansky-Aschoff sinuses are epithelial invaginations into the gallbladder wall. Fluid-containing sinuses can appear as intramural cystic spaces; concentrated reflective contents can generate comet-tail artifacts. On MRI, fluid-filled sinuses can create the pearl-necklace appearance. [Bonatti and colleagues](https://doi.org/10.1007/s13244-017-0544-7) connect these imaging findings to the underlying wall alteration.

The correspondence is between an intramural structure and its measurements. The comet tail itself is an acoustic effect, not a microscopic object that pathology should reproduce. I read this as a useful constraint on claims that an image explanation “matches histology.”

## Diagnostic workflow and imaging findings

### Preserve dynamic ultrasound evidence

A suspected stone should be assessed for mobility and posterior shadowing across views. Sludge may layer or change configuration, while an attached mural lesion remains related to the wall. Some impacted stones do not move, and tumefactive sludge may initially resemble a fixed mass. Dynamic behavior must therefore be interpreted with attachment and other findings.

In a hypothetical examination, a nonshadowing echogenic focus appears polypoid in the supine view but changes shape and moves after repositioning. The resolving evidence is the maneuver. A single saved image cannot establish that movement, even if the final report correctly calls sludge.

I would retain clips or paired views documenting the maneuver, along with the report. The distinction between “movement observed” and “report says mobile” matters when evaluating what evidence an image model actually received.

### Use CT to investigate extent and complications

Contrast CT can assess pericholecystic inflammation, collections, adjacent liver, vessels, and disease elsewhere in the abdomen. Multiplanar reconstructions help establish whether an apparent wall defect or liver interface abnormality persists outside one slice.

A cholesterol-rich stone can be poorly conspicuous against bile on CT despite being evident on ultrasound. Conversely, CT may show an inflammatory complication beyond the ultrasound window. [Yu and colleagues](https://doi.org/10.3748/wjg.v26.i22.2967) illustrate these complementary strengths.

I would compare acquisition details before calling this disagreement. A noncontrast CT obtained for another indication and a targeted ultrasound are not interchangeable lesion-characterization tests. Slice thickness can also average a tiny intramural space with surrounding wall, removing a feature that higher-resolution imaging displays.

### Separate the MRCP ductal map from MRI tissue assessment

MRCP uses heavily T2-weighted sequences to emphasize relatively stationary fluid. A dark filling defect interrupts bright duct contents, but stones, gas, debris, and flow-related signal loss can produce competing explanations.

Thick slabs and maximum-intensity projections compress depth information. Small defects can disappear behind bright overlapping fluid, and respiratory motion can distort a duct's apparent continuity. I would inspect thin source images and other planes before diagnosing a stricture from a projection alone. These pitfalls are described by [Griffin, Charles-Edwards, and Grant](https://pubmed.ncbi.nlm.nih.gov/22695995/).

A complete MRI can additionally assess enhancement, fat, diffusion, and mural architecture. Diffusion restriction can accompany cellular tumor or inflammatory material, so it should not be treated as a histological label. MRCP alone does not provide all of this tissue information.

### Match the imaging target to the specimen

For a focal gallbladder lesion, I would link the imaged location to the fundus, body, or neck and, where feasible, to the hepatic or peritoneal surface. Gross photographs, orientation markers, and a block map can make the link more defensible.

An ultrasound plane samples a finite volume through a distended organ. A histological section samples a thin cut through tissue that may have collapsed, been opened, fixed, and deformed. Exact pixel correspondence cannot be assumed from matching organ names.

Suppose ultrasound shows an irregular fundal lesion, while the pathology report describes chronic cholecystitis and a small adenoma at the neck. “Benign pathology” is a patient-level summary, but it has not yet explained the fundal target. I would request target reconciliation before assigning the fundal image an adenoma label.

## Differential diagnosis and management context

Inflammation can thicken the wall and obscure the liver interface, producing an appearance that resembles invasion. Xanthogranulomatous cholecystitis can be particularly mass-like. Conversely, finding a benign wall alteration does not explain a separate suspicious solid component elsewhere in the organ.

The [2025 KSAR recommendations](https://doi.org/10.3348/kjr.2024.0914) support further assessment when gallbladder wall findings remain indeterminate or ultrasound visibility is limited. I would specify whether the next examination should resolve internal wall architecture or assess suspected malignant extension.

Discordance needs an explanation, not an automatic ranking of modalities. A biopsy may miss viable tumor; a scan may depict inflammation; a stone may pass before MRCP or ERCP; antibiotics may reduce inflammatory changes before surgery. The interval and intervening events determine which explanations are plausible.

I would distinguish confirmation of disease from confirmation of an individual image sign. Surgical pathology can establish carcinoma without proving that every blurred wall boundary on the earlier ultrasound represented tumor infiltration.

## Implications for medical AI

### Keep diagnosis, visible feature, and specimen finding separate

I would build linked records for the patient diagnosis, each imaging target, reader-assessed features, and the specimen region. “Pathology confirmed” would identify the procedure, date, target, and diagnosis, rather than act as a universal quality flag.

A carcinoma diagnosis is appropriate supervision for a patient-level disease task. It is not automatically a positive label for every frame from that patient. Frames may show uninvolved wall, stones, or liver alone. Multiple-instance learning can aggregate an examination's frames, but patient-level supervision still does not identify which frame contains diagnostic evidence.

The [STARD 2015 guidance](https://pubmed.ncbi.nlm.nih.gov/26511519/) emphasizes reporting reference standards, timing, and participant flow. I would use those requirements to expose how surgical verification and follow-up differ between cases.

### Make correspondence uncertainty part of the audit

For an initial gallbladder study, I would classify image-specimen matches as confident, approximate, or unresolved using prespecified anatomical criteria. This is my proposed annotation scheme, not an established clinical grading system.

I could then test whether errors attributed to “pathology disagreement” concentrate in unresolved matches. A separate analysis could restrict evaluation to confidently matched lesions while reporting how many patients that excludes. Improvement after restriction would indicate sensitivity to correspondence quality, not prove that the excluded predictions were correct.

For adenomyomatosis, an especially concrete question is whether ultrasound-visible intramural spaces correspond to sinuses documented in the matched specimen region. I would distinguish sinuses present but acoustically unresolved from cases where target matching is inadequate.

### Audit information supplied by the later workup

An MRI report available only after suspicious ultrasound is part of the diagnostic process. Using its text as input to a model intended for the first scan would leak future evidence. Using it as a reference can also introduce dependence if the MRI reader knew the original ultrasound conclusion.

Cross-modality agreement is therefore useful but not automatically independent corroboration. I would record reader access to earlier reports and compare image-only annotations with annotations made after the full workup.

My immediate research question is whether a gallbladder classifier's errors track missing visible features, incorrect lesion correspondence, or true overlap between benign and malignant tissue appearances. A focused review of discordant cases with ultrasound, subsequent imaging, and specimen maps could separate these mechanisms more effectively than one aggregate pathology-confirmed accuracy.

## References

- Bonatti et al., [Gallbladder adenomyomatosis: imaging findings, tricks and pitfalls](https://doi.org/10.1007/s13244-017-0544-7), Insights into Imaging 2017.
- Yu et al., [Benign gallbladder diseases: Imaging techniques and tips for differentiating with malignant gallbladder diseases](https://doi.org/10.3748/wjg.v26.i22.2967), World Journal of Gastroenterology 2020.
- Griffin, Charles-Edwards, and Grant, [Magnetic resonance cholangiopancreatography: the ABC of MRCP](https://pubmed.ncbi.nlm.nih.gov/22695995/), Insights into Imaging 2012.
- Chang et al., [Interpretation, Reporting, Imaging-Based Workups, and Surveillance of Incidentally Detected Gallbladder Polyps and Gallbladder Wall Thickening: 2025 Recommendations From the Korean Society of Abdominal Radiology](https://doi.org/10.3348/kjr.2024.0914), Korean Journal of Radiology 2025.
- Bossuyt et al., [STARD 2015: an updated list of essential items for reporting diagnostic accuracy studies](https://pubmed.ncbi.nlm.nih.gov/26511519/), BMJ 2015.
