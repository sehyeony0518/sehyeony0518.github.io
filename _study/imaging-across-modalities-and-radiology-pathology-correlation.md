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

Imaging across modalities combines different measurements of the same anatomy. Radiology-pathology correlation asks how those appearances relate to tissue findings, while accounting for differences in sampling, scale, and timing.

## Clinical overview

A hepatobiliary workup often begins with ultrasound and proceeds to CT, MRI, MRCP, or tissue assessment because a specific question remains unresolved. The next examination may seek a stone, characterize a lesion, or assess spread. I would state the unresolved question before choosing another modality.

Pathology can establish diagnoses that imaging cannot, but the comparison needs a clearly matched target. A biopsy samples part of a lesion; a resection specimen provides more extensive tissue; neither automatically explains every abnormality in the original examination.

## Anatomy and pathophysiology

Ultrasound reflects acoustic interfaces and scattering. CT measures X-ray attenuation, with contrast enhancement adding information about perfusion and contrast distribution. MRI signal depends on tissue properties and the sequence used. MRCP emphasizes relatively stationary fluid in the ducts. The same lesion can therefore appear different across modalities.

Tissue mechanisms help connect them. Edema can thicken a wall without neoplasia; fibrosis can alter enhancement; necrosis can create nonenhancing regions within a tumor. In adenomyomatosis, Rokitansky-Aschoff sinuses may appear as intramural cystic spaces or generate artifacts when they contain reflective material. [Bonatti and colleagues](https://doi.org/10.1007/s13244-017-0544-7) show how this pathological substrate produces characteristic ultrasound and MRI findings.

## Diagnostic workflow and imaging findings

### Preserve what ultrasound establishes dynamically

Ultrasound can test movement with repositioning, assess focal tenderness, and inspect a finding across changing planes. Stones, sludge, and wall lesions should be described using attachment, mobility, shadowing, vascularity, and mural architecture. CT or still images cannot always recover these observations. I would carry them into the next diagnostic step rather than replace them with the later modality's interpretation.

### Use CT for the unresolved anatomical extent

CT can evaluate adjacent organs, inflammatory collections, vascular involvement, and disease beyond the immediate ultrasound field. Contrast timing matters when assessing an enhancing lesion. A stone conspicuous on ultrasound may be poorly conspicuous on CT, while a complication obscured by gas on ultrasound may be clear on CT. The modalities therefore have complementary strengths. [Yu and colleagues](https://doi.org/10.3748/wjg.v26.i22.2967) illustrate this across benign gallbladder diseases and malignant mimics.

### Separate MRCP from tissue characterization

MRCP provides a ductal map using heavily T2-weighted sequences; it is not synonymous with a complete contrast-enhanced liver MRI. A filling defect describes interrupted fluid signal and needs interpretation for stone, air, debris, or artifact. Source images matter because projection images can conceal detail. [Griffin and colleagues](https://pubmed.ncbi.nlm.nih.gov/22695995/) describe these technical pitfalls. Other MRI sequences can assess enhancement, diffusion, fat, and fluid characteristics that the ductal map alone does not provide.

### Match imaging to the sampled tissue

Correlation should identify the same lesion, location, and relevant wall surface or liver segment. The interval between examinations, intervening treatment, specimen orientation, and sampled region affect interpretation. Fixation and sectioning change tissue geometry. A small biopsy may miss heterogeneous components. I would examine target matching and sampling before interpreting disagreement as a failed imaging-pathology relationship.

## Differential diagnosis and management context

Sludge can resemble a mass, inflammation can resemble invasion, and benign intramural change can resemble neoplastic thickening. Additional imaging should address management-relevant uncertainty. Persisting suspicion may require specialist review or tissue assessment, while a characteristic benign pattern may make invasive investigation unnecessary. For indeterminate gallbladder wall findings, the [KSAR recommendations](https://doi.org/10.3348/kjr.2024.0914) support choosing further imaging according to visibility and concern for malignancy.

A discordant result should be reconciled rather than resolved by automatically ranking modalities. A negative sample may be inadequate, a suspicious scan may reflect inflammation, or the disease may have changed between assessments.

## Implications for medical AI

I read radiology-pathology correlation as a requirement to document how a label was established. For gallbladder AI, “pathology confirmed” should identify the matched lesion and procedure, not merely indicate that some tissue was examined.

This suggests keeping image findings, pathological diagnosis, and management outcomes as linked but separate records. In clinical faithfulness auditing, I would ask whether a model's apparent evidence corresponds to the imaged tissue process and whether that feature was assessable in the supplied view. Cross-modality agreement can strengthen an interpretation, but agreement alone cannot establish that the model used the same evidence.

## References

- Bonatti et al., [Gallbladder adenomyomatosis: imaging findings, tricks and pitfalls](https://doi.org/10.1007/s13244-017-0544-7), Insights into Imaging 2017.
- Yu et al., [Benign gallbladder diseases: Imaging techniques and tips for differentiating with malignant gallbladder diseases](https://doi.org/10.3748/wjg.v26.i22.2967), World Journal of Gastroenterology 2020.
- Griffin, Charles-Edwards, and Grant, [Magnetic resonance cholangiopancreatography: the ABC of MRCP](https://pubmed.ncbi.nlm.nih.gov/22695995/), Insights into Imaging 2012.
- Chang et al., [Interpretation, Reporting, Imaging-Based Workups, and Surveillance of Incidentally Detected Gallbladder Polyps and Gallbladder Wall Thickening: 2025 Recommendations From the Korean Society of Abdominal Radiology](https://doi.org/10.3348/kjr.2024.0914), Korean Journal of Radiology 2025.
