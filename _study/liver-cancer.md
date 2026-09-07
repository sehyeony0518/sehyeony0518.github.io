---
layout: study_note
title: "Liver Cancer"
description: "Hepatocellular carcinoma and hepatic metastasis: surveillance, imaging diagnosis, and the reporting systems used."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "hepatobiliary"
category_title: "Hepatobiliary Medicine & Imaging"
subgroup: "Biliary Disease"
order: 11
source: "Independent study"
written: true
updated: "2026-09-08"
---

Hepatocellular carcinoma arises from hepatocytes, while hepatic metastases represent cancer that has spread from another primary site. Their imaging workups share some tools, but surveillance populations, diagnostic criteria, and treatment implications differ.

## Clinical overview

HCC often develops in chronic liver disease, particularly cirrhosis, although it also occurs without cirrhosis. Selected patients with chronic hepatitis B warrant surveillance even without established cirrhosis. Surveillance seeks clinically useful early detection in people who could benefit from treatment; it is not general population screening. The [AASLD guidance](https://pmc.ncbi.nlm.nih.gov/articles/PMC10663390/) recommends ultrasound with alpha-fetoprotein approximately every six months for eligible patients.

Metastases are assessed in relation to an extrahepatic cancer or an unexplained liver lesion. The question may concern staging, resectability, or treatment response. I therefore separate finding a lesion from determining its origin and from measuring its effect on the patient's management.

## Anatomy and pathophysiology

During hepatocarcinogenesis, changes in vascular supply can produce increased arterial enhancement and reduced enhancement relative to the liver on later phases. This pattern is useful but not universal, particularly in small or atypical tumors. Background cirrhosis also creates regenerative and dysplastic nodules that complicate lesion detection.

Metastases reach the liver through circulating tumor cells and vary in vascularity, cellularity, fibrosis, and necrosis according to the primary cancer and treatment history. Some are hypovascular, while others enhance strongly in the arterial phase. Neither lesion number nor echogenicity establishes the diagnosis.

## Diagnostic workflow and imaging findings

### Document surveillance quality and the finding separately

Ultrasound surveillance evaluates the liver systematically for focal abnormalities and relevant vascular findings. HCC may be hypoechoic, hyperechoic, or heterogeneous, so grayscale appearance alone is insufficient. The [2024 US LI-RADS update](https://pubmed.ncbi.nlm.nih.gov/39625378/) separates the examination category from the visualization score. A negative examination with severe visualization limitations is not equivalent to an adequately visualized negative study. Positive surveillance findings prompt diagnostic evaluation rather than automatically becoming an HCC diagnosis.

### Characterize suspected HCC with multiphasic imaging

Diagnostic CT or MRI evaluates arterial enhancement, washout, capsule appearance, size, and growth. Nonrim arterial-phase hyperenhancement and nonperipheral washout are important features, interpreted using the appropriate phases for the contrast agent. The [CT/MRI LI-RADS framework](https://doi.org/10.1148/radiol.2018181494) applies to defined patients at risk for HCC. Its criteria should not be transferred uncritically to incidental lesions in people outside that population.

### Read the category as a specific claim

LR-5 denotes definite HCC within the applicable diagnostic framework. LR-M denotes probable or definite malignancy that is not specific for HCC; it does not simply mean metastasis. Indeterminate categories require context-dependent follow-up or further investigation. I read these as statements of diagnostic confidence, conditional on the patient and examination meeting the system's assumptions. A technically incomplete study may not support confident categorization.

### Evaluate suspected metastases in the oncological context

Contrast-enhanced CT supports staging beyond the liver, while MRI can further characterize lesions and detect small deposits. Diffusion-weighted imaging and hepatobiliary-phase imaging can improve conspicuity, but restricted diffusion or hepatobiliary hypointensity is not specific for metastasis. [Maino and colleagues](https://pubmed.ncbi.nlm.nih.gov/37901445/) describe these patterns and pitfalls. A report should communicate lesion location, distribution, vascular relationships, and changes relevant to treatment, rather than supply only a count.

## Differential diagnosis and management context

Cysts, hemangiomas, focal fat, abscesses, and other primary liver tumors can enter the differential. Appropriate imaging criteria may establish HCC without biopsy in an eligible high-risk patient; outside that setting, or with atypical findings, tissue may be needed. AFP alone does not establish HCC. Metastatic disease likewise requires interpretation alongside the known primary and pathology when indicated.

HCC management depends on tumor extent, liver function, and patient fitness, with treatment selected accordingly. Metastatic disease follows pathways determined by the primary cancer and distribution of disease. I distinguish a diagnostic reporting category from a staging system and from a treatment recommendation.

## Implications for medical AI

I read these pathways as separate tasks: surveillance detection, lesion characterization, staging, and response assessment. A classifier trained on curated masses cannot establish performance in surveillance examinations containing no lesion or poorly visualized tissue.

For my clinical faithfulness work, I would ask whether a model uses lesion-specific evidence or mainly recognizes cirrhosis, treatment changes, and cancer-related acquisition protocols. This suggests evaluating background liver status and visualization alongside pathology, while preserving which diagnostic framework actually justified the label.

## References

- Singal et al., [AASLD Practice Guidance on prevention, diagnosis, and treatment of hepatocellular carcinoma](https://pmc.ncbi.nlm.nih.gov/articles/PMC10663390/), Hepatology 2023.
- Kamaya et al., [LI-RADS US Surveillance Version 2024 for Surveillance of Hepatocellular Carcinoma: An Update to the American College of Radiology US LI-RADS](https://pubmed.ncbi.nlm.nih.gov/39625378/), Radiology 2024.
- Chernyak et al., [Liver Imaging Reporting and Data System (LI-RADS) Version 2018: Imaging of Hepatocellular Carcinoma in At-Risk Patients](https://doi.org/10.1148/radiol.2018181494), Radiology 2018.
- Maino et al., [Liver metastases: The role of magnetic resonance imaging](https://pubmed.ncbi.nlm.nih.gov/37901445/), World Journal of Gastroenterology 2023.
