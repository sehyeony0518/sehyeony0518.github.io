---
layout: study_note
title: "Head and Neck Cancer"
description: "Multimodal staging and the coordination problem between imaging, pathology, and treatment planning."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "oncology"
category_title: "Oncology"
order: 2
source: "Lecture"
written: true
updated: "2026-09-08"
---

Head and neck cancer comprises tumors arising in anatomically and biologically different sites. I focus here on mucosal squamous cell carcinoma, where examination, imaging, and pathology must be reconciled before a stage can guide treatment.

## Clinical overview

A persistent oral lesion, swallowing difficulty, voice change, or neck mass can initiate assessment. The presenting symptom depends on the site, and a cervical nodal metastasis may be more apparent than the primary tumor. Tobacco and alcohol are important risk factors; HPV-associated oropharyngeal disease represents a distinct clinical context.

An oral-cavity cancer and an oropharyngeal cancer should not be treated as the same problem simply because they occupy neighboring anatomy. The [EHNS-ESMO-ESTRO guideline](https://doi.org/10.1016/j.annonc.2020.07.011) organizes diagnosis and treatment around site, disease extent, and clinical circumstances. Functional outcomes such as swallowing, speech, and airway protection also matter.

## Anatomy and pathophysiology

Tumors can spread across mucosal boundaries, through deep tissue planes, into bone or cartilage, and along nerves. Regional lymphatic drainage determines which cervical nodal groups require attention. Small differences in the location or direction of extension can therefore change the treatment problem more than a small difference in tumor diameter.

HPV-associated oropharyngeal squamous cell carcinoma differs biologically and prognostically from HPV-independent disease. Pathological biomarkers help classify this context, but their meaning depends on anatomical site and specimen type. I read this as a reason to retain the original pathology interpretation rather than reduce every result to a generic “HPV positive” label.

## Diagnostic workflow and imaging findings

### Identify the lesion and obtain representative tissue

Clinical examination and flexible endoscopy assess the visible mucosal surface and functional findings such as vocal-cord mobility. Biopsy establishes histology. A neck mass may be sampled under ultrasound guidance, but a nodal specimen does not by itself establish the exact primary site. Tissue location and the procedure used to obtain it should remain linked to the imaging findings.

### Establish the relevant pathological classification

For newly diagnosed oropharyngeal squamous cell carcinoma, HPV assessment has diagnostic and prognostic importance. The [2025 CAP guideline update](https://doi.org/10.5858/arpa.2024-0388-CP) specifies testing approaches for different specimens and settings. p16 immunohistochemistry is used as a surrogate in appropriate contexts; it is not interchangeable with direct HPV detection in every head and neck tumor.

### Map local and regional extent

Contrast-enhanced CT and MRI provide complementary anatomical information. Readers assess the enhancing lesion, deep-space involvement, bone or cartilage invasion, and suspicious lymph nodes. MRI can help evaluate soft tissue, marrow, and perineural spread; CT depicts cortical bone changes well. Nodal necrosis or cystic change can raise suspicion, while size alone is insufficient. The [ACR staging guidance](https://doi.org/10.1016/j.jacr.2023.08.008) relates modality choice to the clinical scenario.

### Integrate distant assessment and the staging record

Chest imaging and, in appropriate settings, FDG-PET/CT assess additional disease and can assist evaluation of an occult primary. FDG uptake is not cancer-specific. Clinical stage combines available examination, imaging, and biopsy information; pathological stage uses resection findings when available. The record should identify the staging system, version, anatomical site, and whether assessment occurred before or after treatment.

## Differential diagnosis and management context

Inflammatory lesions, infection, benign tumors, lymphoma, and other malignancies can resemble mucosal cancer or nodal metastasis. Post-treatment edema, fibrosis, and inflammation create an additional interpretation problem. Imaging suspicion of invasion or extranodal extension is not identical to microscopic confirmation, and discordant findings require review rather than automatic substitution of one result for another.

Treatment may involve surgery, radiotherapy, systemic therapy, or combinations according to site, extent, biology, and patient factors. Planning must account for resectability and expected function, as well as tumor control. I understand multidisciplinary review as the point where these observations become one clinical plan, with unresolved discrepancies made explicit.

## Implications for medical AI

I would separate primary-tumor detection, nodal assessment, invasion prediction, staging, and treatment-response evaluation. Their references differ. Assigning a final pathological stage to every preoperative image can obscure which component was visible and which was established only after surgery.

This suggests to me a direct connection with gallbladder clinical faithfulness auditing: anatomical plausibility does not establish that a model used the evidence required for a staging claim. I would preserve lesion correspondence, biomarker provenance, treatment timing, and modality availability, and evaluate errors by their effect on the proposed treatment plan.

## References

- Machiels et al., [Squamous cell carcinoma of the oral cavity, larynx, oropharynx and hypopharynx: EHNS-ESMO-ESTRO Clinical Practice Guidelines for diagnosis, treatment and follow-up](https://doi.org/10.1016/j.annonc.2020.07.011), Annals of Oncology 2020.
- Lewis et al., [Human Papillomavirus Testing in Head and Neck Carcinomas: Guideline Update](https://doi.org/10.5858/arpa.2024-0388-CP), Archives of Pathology & Laboratory Medicine 2025.
- Expert Panel on Neurological Imaging et al., [ACR Appropriateness Criteria Staging and Post-Therapy Assessment of Head and Neck Cancer](https://doi.org/10.1016/j.jacr.2023.08.008), Journal of the American College of Radiology 2023.
