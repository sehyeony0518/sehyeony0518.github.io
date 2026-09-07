---
layout: study_note
title: "Lung Cancer"
description: "Screening programs, overdiagnosis, and what a screening context does to the meaning of a positive result."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "oncology"
category_title: "Oncology"
order: 1
source: "Lecture"
written: true
updated: "2026-09-08"
---

Lung cancer includes malignant tumors with different histologies, growth patterns, and treatment responses. Screening seeks to reduce deaths by detecting clinically important disease earlier, while also exposing people without cancer to further investigation.

## Clinical overview

Smoking is a major risk factor, but lung cancer also occurs in people who have never smoked. A symptomatic patient with hemoptysis or other concerning findings follows a diagnostic pathway; an asymptomatic person invited to low-dose CT follows a screening pathway. Their starting probabilities and reasons for testing differ.

The [National Lung Screening Trial](https://doi.org/10.1056/NEJMoa1102873) demonstrated reduced lung-cancer mortality with low-dose CT compared with chest radiography in its high-risk study population. I read this as evidence for a defined screening intervention, not a claim that detecting more nodules always improves outcomes.

## Anatomy and pathophysiology

Lung cancers include non-small-cell and small-cell carcinomas. Histology and molecular features influence treatment, while the tumor’s location and spread influence symptoms and staging. A peripheral nodule, central airway lesion, or infiltrative abnormality can therefore represent different diagnostic problems.

Some adenocarcinomas present as subsolid nodules, with ground-glass and solid components reflecting different patterns of tissue involvement. Appearance does not determine histology by itself. Benign inflammatory lesions can resemble cancer, and the rate of progression varies enough that a screening program can preferentially detect slower-growing disease.

## Diagnostic workflow and imaging findings

### Establish eligibility and the purpose of CT

A screening program defines eligibility, repeat testing, shared decision-making, and follow-up. The [USPSTF recommendation](https://doi.org/10.1001/jama.2021.1117) bases eligibility on age and smoking history and also considers whether health status permits meaningful benefit from screening and treatment. Eligibility rules vary across organizations. A screening result should be interpreted within the program that generated it.

### Characterize findings on thin-section images

The reader assesses whether a nodule is solid, part-solid, or ground-glass, together with size, contour, location, and associated findings. Spiculation or an enlarging solid component can increase concern. Certain calcification patterns, fat, or typical perifissural morphology may favor benignity, but assessment requires the complete appearance. Slice thickness and reconstruction affect apparent boundaries and measurements.

### Compare with prior examinations

Persistence, new appearance, and growth influence management. A nodule may change because of infection or technical differences, so growth assessment requires comparable examinations. [Lung-RADS v2022](https://doi.org/10.1016/j.chest.2023.10.028) provides screening-specific assessment categories and management recommendations. A category expresses a recommended pathway; it is not a histological diagnosis or a universal rule for incidental nodules.

### Escalate according to the level of suspicion

Further assessment may include interval CT, diagnostic imaging, PET/CT, or tissue sampling. PET uptake can occur in inflammation, and some small or less metabolically active tumors are not strongly avid. Bronchoscopic or percutaneous sampling depends on lesion location and the clinical question. Confirmed cancer then requires histological characterization and staging before treatment planning.

## Differential diagnosis and management context

The differential includes granulomas, infection, scars, benign nodules, primary lung cancer, and metastases. An abnormal screening examination does not automatically warrant an invasive procedure. Follow-up seeks to identify consequential malignancy while limiting avoidable biopsies, complications, anxiety, and radiation exposure.

Overdiagnosis means detecting a cancer that would not have caused symptoms or death during the person’s lifetime. It differs from a false positive, where the suspected cancer is absent. Earlier diagnosis can also lengthen measured survival without postponing death, creating lead-time bias. This is why screening benefit cannot be established from detection rate or survival after diagnosis alone; the USPSTF explicitly considers benefits and harms together.

## Implications for medical AI

I would evaluate a screening model in the intended eligible population, including benign findings and complete follow-up pathways. A malignancy-enriched collection of selected nodules cannot directly estimate positive predictive value or referral burden in screening. Nodule detection, malignancy assessment, and management recommendation should remain separate targets.

This suggests to me that clinical faithfulness must be paired with consequences of use. A model can correctly detect a subtle lesion without establishing that acting on it benefits the patient. I would examine interval cancers, unnecessary workup, calibration, and workflow effects alongside sensitivity, while auditing reliance on acquisition or screening-center cues.

## References

- National Lung Screening Trial Research Team, [Reduced Lung-Cancer Mortality with Low-Dose Computed Tomographic Screening](https://doi.org/10.1056/NEJMoa1102873), New England Journal of Medicine 2011.
- US Preventive Services Task Force, [Screening for Lung Cancer: US Preventive Services Task Force Recommendation Statement](https://doi.org/10.1001/jama.2021.1117), JAMA 2021.
- Christensen et al., [ACR Lung-RADS v2022: Assessment Categories and Management Recommendations](https://doi.org/10.1016/j.chest.2023.10.028), CHEST 2024.
