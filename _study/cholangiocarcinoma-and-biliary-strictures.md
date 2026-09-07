---
layout: study_note
title: "Cholangiocarcinoma and Biliary Strictures"
description: "Distinguishing benign from malignant strictures, and what each modality can contribute."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "hepatobiliary"
category_title: "Hepatobiliary Medicine & Imaging"
subgroup: "Biliary Disease"
order: 10
source: "Independent study"
written: true
updated: "2026-09-08"
---

A biliary stricture is an abnormal narrowing of a bile duct; cholangiocarcinoma is a malignancy arising from biliary epithelium. A stricture can be malignant or benign, and its appearance alone often cannot settle the distinction.

## Clinical overview

Extrahepatic and perihilar tumors frequently present through impaired drainage, with jaundice, pruritus, or cholangitis. Intrahepatic cholangiocarcinoma may instead appear as a liver mass without early jaundice. Primary sclerosing cholangitis and some chronic biliary disorders increase risk, but cancer can occur without a recognized predisposing condition. I keep the subtype explicit because it changes the diagnostic route.

The [ACG stricture guideline](https://pubmed.ncbi.nlm.nih.gov/36863037/) separates two goals: establishing the cause and restoring bile flow when needed. Successful drainage does not establish benignity. Likewise, unresolved pathology does not remove the need to treat clinically significant obstruction.

## Anatomy and pathophysiology

Cholangiocarcinoma is classified as intrahepatic, perihilar, or distal according to its origin. Growth may form a mass, infiltrate along the duct wall, or project into the lumen. Fibrous tumor stroma can contribute to delayed contrast enhancement, while longitudinal microscopic spread may extend beyond the apparent imaging abnormality.

Benign narrowing can result from surgical injury, ischemia, chronic pancreatitis, or inflammatory cholangiopathies, including IgG4-related disease. Fibrosis and inflammation can thicken and enhance the duct wall, creating overlap with malignancy. I understand this overlap as a shared tissue response, which explains why a technically excellent image may still leave the diagnosis uncertain.

## Diagnostic workflow and imaging findings

### Establish the location and relevant history

Ultrasound can reveal upstream duct dilatation, an associated mass, or an abrupt transition, but may not depict the stricture itself. Previous surgery, transplantation, pancreatitis, stenting, and known cholangiopathy should be reviewed. The report should identify which ducts are affected and whether the distal duct is visible. “Biliary obstruction” is an incomplete description when treatment depends on the level and distribution of narrowing.

### Map the lesion with contrast imaging and MRCP

Contrast-enhanced CT assesses the mass, vascular relationships, nodes, and distant disease. MRI with MRCP is particularly useful for mapping perihilar or intrahepatic duct involvement. Irregular asymmetric narrowing, shouldering, enhancing tissue, and an associated mass increase concern; smooth tapering may favor benign disease but cannot establish it. The [BSG guideline](https://doi.org/10.1136/gutjnl-2023-330029) recommends obtaining staging imaging before biliary intervention where clinically feasible, because instrumentation can alter appearances.

### Interpret tissue results as samples

ERCP permits ductal imaging, drainage, brush cytology, and intraductal biopsy. Negative brush cytology does not reliably exclude cancer because the sample may contain few diagnostic cells. The [ASGE guideline](https://pubmed.ncbi.nlm.nih.gov/37307900/) supports adding fluoroscopic biopsy to brush sampling and using cholangioscopy or EUS in selected settings. “Nondiagnostic” and “benign” should remain separate conclusions. Further sampling depends on location and the unresolved question.

### Plan sampling around potential treatment

EUS can assess distal lesions and suspicious nodes, but the target and needle route matter. A potentially operable or transplant-eligible perihilar lesion should undergo specialist discussion before direct needle sampling because seeding concerns can affect treatment options. This does not prohibit all tissue acquisition. The BSG pathway distinguishes sampling of a primary hilar lesion from appropriately selected nodal or metastatic targets.

## Differential diagnosis and management context

The differential includes postoperative strictures, primary sclerosing cholangitis, IgG4-related cholangitis, chronic pancreatitis, and external compression from pancreatic or other tumors. Serum CA 19-9 is an adjunct: obstruction and inflammation can elevate it, and it cannot independently diagnose cholangiocarcinoma. Histology, imaging, serology, and the clinical course may need to be reconciled together.

Management depends on location, extent, patient fitness, and the possibility of complete resection. Drainage planning is especially consequential at the hilum, where separate liver segments may remain obstructed. Resection, selected transplant pathways, and oncological treatment require multidisciplinary decisions. I would not reduce an indeterminate stricture to indefinite observation merely because one sampling procedure was negative.

## Implications for medical AI

I read this workflow as a challenge to simple binary labels. A stricture may have suspicious imaging, negative cytology, and later surgical confirmation of malignancy without any of those records being internally inconsistent. The reference needs to state its method, timing, and adequacy.

For clinical faithfulness auditing, I would separate models that detect narrowing, estimate malignant likelihood, and map disease extent. I would also examine reliance on stents or postprocedural changes. This suggests that apparent diagnostic accuracy may partly reflect whether the model recognizes who has already entered a cancer workup, rather than the untreated lesion's morphology.

## References

- Elmunzer et al., [ACG Clinical Guideline: Diagnosis and Management of Biliary Strictures](https://pubmed.ncbi.nlm.nih.gov/36863037/), American Journal of Gastroenterology 2023.
- Rushbrook et al., [British Society of Gastroenterology guidelines for the diagnosis and management of cholangiocarcinoma](https://doi.org/10.1136/gutjnl-2023-330029), Gut 2024.
- Fujii-Lau et al., [American Society for Gastrointestinal Endoscopy guideline on the role of endoscopy in the diagnosis of malignancy in biliary strictures of undetermined etiology: summary and recommendations](https://pubmed.ncbi.nlm.nih.gov/37307900/), Gastrointestinal Endoscopy 2023.
