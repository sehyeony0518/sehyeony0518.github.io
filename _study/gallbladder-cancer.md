---
layout: study_note
title: "Gallbladder Cancer"
description: "Features that raise concern for malignancy, the risk factors that shift pretest probability, and where imaging alone cannot settle it."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "hepatobiliary"
category_title: "Hepatobiliary Medicine & Imaging"
subgroup: "Gallbladder Disease"
order: 7
source: "Independent study"
written: true
updated: "2026-09-08"
---

Gallbladder cancer is a malignant tumor arising in the gallbladder, most commonly adenocarcinoma. Imaging can identify concerning morphology and disease extent, but it cannot reliably settle the histology of every early or inflammatory-appearing lesion.

## Clinical overview

Early disease may produce no distinctive symptoms and can be discovered incidentally after cholecystectomy performed for presumed benign disease. More advanced disease may present with abdominal pain, weight loss, or jaundice. I separate the question of whether cancer is plausible from whether imaging has provided enough evidence to plan its management.

Risk rises with age and varies geographically. Gallstones and longstanding inflammation are established associations, and anomalous pancreaticobiliary junction anatomy is another recognized risk factor. Most people with gallstones do not develop gallbladder cancer. [Rawla and colleagues](https://doi.org/10.5114/ceh.2019.85166) review these epidemiological relationships. I treat them as modifiers of pretest probability, not substitutes for examining a lesion.

## Anatomy and pathophysiology

The gallbladder's close attachment to the liver and connections to the biliary and lymphatic systems shape how disease spreads. Tumor can extend into adjacent liver, involve regional lymph nodes, obstruct bile ducts, or disseminate beyond the local site. The route and extent of spread affect whether a complete surgical resection is feasible.

Cancer can grow as a mass replacing the gallbladder, a polypoid intraluminal lesion, or an infiltrating wall abnormality. Small mural lesions may resemble benign thickening; destructive masses are more conspicuous. [Ramachandran and colleagues](https://doi.org/10.1259/bjr.20200726) describe these presentations.

## Diagnostic workflow and imaging findings

### Establish the clinical and imaging context

The assessment starts with symptoms, previous imaging, relevant risk factors, and laboratory evidence of inflammation or biliary obstruction. Prior studies may clarify whether a finding is persistent or changing, although acquisition differences can mimic change. Jaundice requires assessment of the biliary tree rather than attention to the gallbladder alone. An earlier benign interpretation should not end reassessment of an atypical finding.

### Characterize the lesion on ultrasound

Concerning appearances include an irregular solid mass, asymmetric mural thickening, loss of normal wall layering, and disruption of the interface with adjacent liver. A polypoid lesion should be assessed for attachment, associated wall change, and detectable internal vascularity. Mobility and posterior acoustic behavior help evaluate luminal mimics. No isolated feature establishes malignancy, and failure to detect Doppler flow does not exclude a tumor.

### Assess extent beyond the gallbladder

Ultrasound should look for adjacent hepatic abnormalities, duct dilatation, suspicious nodes, and ascites, while documenting limited regions. Contrast-enhanced CT is central to assessing local extension and metastatic disease; MRI can help characterize liver involvement and biliary anatomy. Their assessment of microscopic invasion and small metastatic deposits remains imperfect, so imaging stage is an estimate rather than a complete pathological map.

### Plan tissue confirmation within the treatment pathway

Histopathology establishes the definitive diagnosis. Tissue may come from a cholecystectomy specimen or planned sampling, depending on presentation and treatment intent. The timing and route of biopsy should be decided with the treating team. Resectable and advanced disease may require different diagnostic sequences. The [ESMO guideline](https://pubmed.ncbi.nlm.nih.gov/36372281/) places diagnosis and staging within this multidisciplinary pathway.

## Differential diagnosis and management context

Adenomyomatosis, chronic cholecystitis, xanthogranulomatous inflammation, benign polyps, and adherent sludge can resemble cancer. Inflammatory disease may obscure normal tissue planes, so apparent invasion alone is not histological proof. Conversely, an inflammatory presentation does not exclude an underlying tumor. Unresolved overlap warrants further characterization and specialist review.

Localized disease may be managed with surgery, with the operation determined by extent and patient suitability. An incidental cancer diagnosis requires review of the specimen, margins, and stage before deciding whether additional surgery is appropriate. Unresectable or metastatic disease follows an oncological pathway; the [ESMO interim update](https://pubmed.ncbi.nlm.nih.gov/39864891/) addresses systemic treatment and molecular profiling.

## Implications for medical AI

I read this workflow as a warning about what a cancer classifier may actually learn. A dataset dominated by bulky tumors can reward recognition of advanced structural destruction while providing little evidence about subtle, potentially actionable disease. Surgical cohorts also select which benign and malignant findings receive pathological labels.

For clinical faithfulness auditing, I would examine performance by morphological presentation and reference standard, including difficult inflammatory mimics. I would also test whether predictions depend on the lesion's wall architecture or on stones, referral patterns, and acquisition choices. This suggests that cancer detection, differential diagnosis, and staging should remain distinct evaluation targets, even when one model contributes to all three.

## References

- Rawla et al., [Epidemiology of gallbladder cancer](https://doi.org/10.5114/ceh.2019.85166), Clinical and Experimental Hepatology 2019.
- Ramachandran, Srivastava, and Madhusudhan, [Gallbladder cancer revisited: the evolving role of a radiologist](https://doi.org/10.1259/bjr.20200726), British Journal of Radiology 2021.
- Vogel et al., [Biliary tract cancer: ESMO Clinical Practice Guideline for diagnosis, treatment and follow-up](https://pubmed.ncbi.nlm.nih.gov/36372281/), Annals of Oncology 2023.
- Vogel and Ducreux, [ESMO Clinical Practice Guideline interim update on the management of biliary tract cancer](https://pubmed.ncbi.nlm.nih.gov/39864891/), ESMO Open 2025.
