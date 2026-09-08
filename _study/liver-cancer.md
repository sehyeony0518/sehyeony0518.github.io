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

A liver lesion's meaning depends on the liver in which it appears and the question that prompted imaging. I separate surveillance for hepatocellular carcinoma from characterization of an incidental mass and staging of a known extrahepatic cancer.

## Clinical overview

Hepatocellular carcinoma (HCC) arises from hepatocytes. Cirrhosis provides an important risk background, although HCC can develop without cirrhosis, particularly in chronic hepatitis B. Surveillance eligibility therefore requires clinical information that cannot be recovered reliably from a selected liver image.

The [AASLD guidance](https://pmc.ncbi.nlm.nih.gov/articles/PMC10663390/) recommends ultrasound with alpha-fetoprotein (AFP) approximately every six months for eligible patients. Surveillance aims to find disease early enough for useful treatment. It is neither population-wide screening nor a diagnostic declaration that every detected nodule is malignant.

Hepatic metastases originate outside the liver. Their evaluation may determine whether an extrahepatic cancer remains amenable to local treatment, whether liver-directed treatment is possible, or whether systemic therapy is working. I would preserve the known primary cancer and treatment history rather than group all hepatic malignancy into one clinical task.

## Anatomy and pathophysiology

### Arterialization has a tissue basis

The liver receives portal venous and hepatic arterial blood. During hepatocarcinogenesis, nodules can lose normal portal supply while developing abnormal arterial vessels. [Ueda and colleagues](https://pubmed.ncbi.nlm.nih.gov/1317345/) demonstrated differences in arterial and portal vascular structures across hepatocellular nodules in a morphometric study.

This helps explain why progressed HCC can enhance more strongly than surrounding liver during the arterial phase. Early lesions do not necessarily display the complete vascular pattern. I read this as a reason to distinguish absence of a classic sign from absence of cancer, especially when discussing small nodules.

“Washout” is a temporal change in enhancement relative to liver, not simply a dark lesion on one image. Background liver enhancement contributes to that comparison. The contrast agent and phase therefore affect what the observation means.

### Metastatic tissue does not have one appearance

Portal venous drainage provides a route from gastrointestinal primaries to the liver. Colorectal metastases are commonly hypovascular, whereas neuroendocrine and renal cell cancer metastases can be hypervascular. Necrosis, mucin, hemorrhage, and treatment can further alter signal and enhancement.

On MRI, metastases generally lack functioning hepatocytes that take up hepatobiliary contrast. Their resulting hypointensity can improve conspicuity, but this property is shared with other lesions. [Maino and colleagues](https://pubmed.ncbi.nlm.nih.gov/37901445/) describe this variability. Neither multiplicity nor one echogenicity pattern supplies a sufficient diagnosis.

## Diagnostic workflow and imaging findings

### Report surveillance findings and visibility independently

US LI-RADS separates the surveillance examination category from visualization. US-1 is negative, US-2 denotes a subthreshold observation, and US-3 is positive. The visualization scores A, B, and C describe increasing limitations. These are examination-level statements, not histological grades. The [2024 update](https://pubmed.ncbi.nlm.nih.gov/39625378/) aligns the surveillance framework with AASLD guidance.

Attenuation from steatosis or body habitus can obscure deeper liver, while heterogeneous parenchyma can conceal a focal lesion. I would record which regions were inadequately seen. A negative study with an obscured hepatic dome cannot provide the same reassurance as a complete examination.

AASLD recommends short-interval ultrasound and AFP follow-up, generally in three to six months, for a subcentimeter observation. A suspicious lesion at least 1 cm prompts multiphasic CT or MRI; concerning AFP findings can also trigger diagnostic evaluation. These are recall decisions within an eligible surveillance population.

### Verify the phases before applying diagnostic criteria

Multiphasic imaging tests how enhancement evolves. Nonrim arterial-phase hyperenhancement, nonperipheral washout, enhancing capsule appearance, size, and growth contribute to CT/MRI LI-RADS assessment. An arterial acquisition obtained too early can miss hyperenhancement, and motion can make an apparent boundary unreliable.

For gadoxetate MRI, washout is assessed in the portal venous phase. Transitional or hepatobiliary hypointensity cannot substitute because hepatocyte uptake increasingly brightens the background liver. The [ACR definitions](https://radssupport.acr.org/support/solutions/articles/11000079469) explain this distinction. I would document the actual phase supporting a feature instead of storing an unqualified “washout present” label.

A technically missing feature and a confidently absent feature should remain distinct. If the arterial phase is unusable, a later dark observation cannot reconstruct the enhancement behavior that was not measured.

### Interpret LI-RADS within its intended population

CT/MRI LI-RADS applies to defined patients at high risk for HCC, with eligibility and exclusions that should be checked before categorization. LR-5 denotes definite HCC within that framework. LR-M indicates probable or definite malignancy without HCC-specific features; it can include cholangiocarcinoma, metastasis, or atypical HCC.

For a concrete hypothetical example, a 15-mm observation in an eligible patient with cirrhosis shows nonrim arterial hyperenhancement and nonperipheral portal venous washout. That combination supports LR-5 under [LI-RADS version 2018](https://doi.org/10.1148/radiol.2018181494). The same pair of descriptive findings in a patient outside the target population does not automatically authorize the same diagnostic conclusion.

I would preserve the category, its supporting features, and the eligibility information together. A category detached from those conditions becomes difficult to audit.

### Stage metastases with lesion correspondence

Contrast CT surveys extrahepatic disease; MRI can clarify small or indeterminate liver findings. Diffusion-weighted imaging should be read with apparent diffusion coefficient maps because high diffusion-weighted signal can reflect T2 shine-through. Restricted diffusion is also not unique to cancer.

In a hypothetical colorectal cancer workup, MRI reveals a small deposit in the opposite lobe from the dominant lesion seen on CT. The additional lesion matters through its location and the planned treatment, not merely because the lesion count increased. I would link each reported observation across examinations rather than assume that similarly sized lesions are the same target.

## Differential diagnosis and management context

Cysts, hemangiomas, focal fat, regenerative nodules, abscesses, and other primary tumors can mimic hepatic malignancy. Focal fat near the gallbladder fossa is particularly relevant to my ultrasound work: altered echogenicity without a true expansile mass can be mistaken for a lesion. MRI chemical-shift imaging can help establish fat-related signal behavior.

AASLD permits noninvasive HCC diagnosis under appropriate imaging and risk conditions. Outside those conditions, or when findings suggest another malignancy, pathology may be needed. AFP alone is not a diagnostic reference.

The [Barcelona Clinic Liver Cancer strategy](https://pubmed.ncbi.nlm.nih.gov/34801630/) combines tumor burden, liver function, and performance status to inform prognosis and treatment. A small tumor in a patient with impaired hepatic reserve creates a different treatment problem from the same tumor in a well-compensated liver. LI-RADS is a diagnostic framework, not a substitute for this staging assessment.

Treatment response is another separate task. [RECIST 1.1](https://pubmed.ncbi.nlm.nih.gov/19097774/) evaluates selected target lesions alongside nontarget disease and new lesions. A response label therefore cannot be reconstructed from one shrinking liver mass while ignoring new disease elsewhere. I would also record the response framework used when therapies alter viable enhancement without proportionate size change.

## Implications for medical AI

### Separate detection from characterization

A classifier evaluated on expertly cropped masses starts after lesion detection has succeeded. It does not measure surveillance performance on complete examinations, including normal studies, unseen regions, and subtle lesions the operator did not select.

For detection, I would evaluate patient-level sensitivity and false-positive findings per examination, with a prespecified rule linking detections to reference lesions. Lesion-level sensitivity answers a different question: finding one of several deposits may count as a patient-level success while leaving clinically relevant disease unmapped.

I would also retain how HCC was established. A pathology-only cohort excludes many patients diagnosed through accepted imaging criteria and can alter the spectrum of disease represented.

### Audit the background without assuming it is irrelevant

A model might recognize cirrhotic texture, a nodular contour, ascites, or a cancer-specific acquisition protocol. Background liver disease is legitimate information for risk estimation, but strong use of it does not establish lesion characterization.

The gallbladder analogue is a malignancy classifier using adjacent liver abnormalities or biliary dilatation. I could compare models supplied with the lesion, surrounding liver, and the full field, while controlling lesion scale where possible. These are information comparisons, not pure causal interventions: cropping changes context and may remove true invasion.

### Ask questions the available gallbladder data can answer

I would first annotate background steatosis, cirrhotic appearance, liver lesions, and visualization limitations in existing gallbladder examinations. Do false malignancy predictions cluster in cases with abnormal liver background despite benign gallbladder pathology?

A second audit would compare wall-confined lesions with cases showing liver involvement, separating visible direct extension from unrelated hepatic lesions. If performance depends mainly on advanced extension, the model's apparent success may not support early lesion discrimination.

Finally, I would review whether cancer cases received more targeted views or higher-resolution examinations than benign controls. Testing within acquisition groups would help distinguish a lesion-associated signal from recognition of who received an intensified cancer workup.

## References

- Singal et al., [AASLD Practice Guidance on prevention, diagnosis, and treatment of hepatocellular carcinoma](https://pmc.ncbi.nlm.nih.gov/articles/PMC10663390/), Hepatology 2023.
- Kamaya et al., [LI-RADS US Surveillance Version 2024 for Surveillance of Hepatocellular Carcinoma: An Update to the American College of Radiology US LI-RADS](https://pubmed.ncbi.nlm.nih.gov/39625378/), Radiology 2024.
- Chernyak et al., [Liver Imaging Reporting and Data System (LI-RADS) Version 2018: Imaging of Hepatocellular Carcinoma in At-Risk Patients](https://doi.org/10.1148/radiol.2018181494), Radiology 2018.
- Maino et al., [Liver metastases: The role of magnetic resonance imaging](https://pubmed.ncbi.nlm.nih.gov/37901445/), World Journal of Gastroenterology 2023.
- Ueda et al., [Vascular supply in adenomatous hyperplasia of the liver and hepatocellular carcinoma: a morphometric study](https://pubmed.ncbi.nlm.nih.gov/1317345/), Human Pathology 1992.
- American College of Radiology, [LI-RADS imaging features: frequently asked questions](https://radssupport.acr.org/support/solutions/articles/11000079469).
- Reig et al., [BCLC strategy for prognosis prediction and treatment recommendation: The 2022 update](https://pubmed.ncbi.nlm.nih.gov/34801630/), Journal of Hepatology 2022.
- Eisenhauer et al., [New response evaluation criteria in solid tumours: revised RECIST guideline (version 1.1)](https://pubmed.ncbi.nlm.nih.gov/19097774/), European Journal of Cancer 2009.
