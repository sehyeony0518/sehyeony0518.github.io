---
layout: study_note
title: "Gallbladder Polyps and Their Malignant Potential"
description: "Cholesterol versus adenomatous polyps, the size thresholds that drive management, and why the distinction is hard on ultrasound."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "hepatobiliary"
category_title: "Hepatobiliary Medicine & Imaging"
subgroup: "Gallbladder Disease"
order: 4
source: "Independent study"
written: true
updated: "2026-09-08"
featured: true
---

Gallbladder polyps are projections from the gallbladder wall into its lumen, but the imaging label includes lesions with different biological meanings. Most are benign; the clinical problem is identifying those that warrant closer assessment or surgery without treating every polyp as a cancer precursor. [SRU consensus](https://pubs.rsna.org/doi/10.1148/radiol.213079)

## Why it matters here

For trustworthy medical AI, the target definition matters before model design begins. Detecting a polyp, distinguishing neoplastic from non-neoplastic lesions, identifying existing malignancy, and predicting future malignant transformation are different tasks. Evidence supporting one does not automatically validate the others.

In my gallbladder ultrasound work, I need to understand what a diagnostic label actually represents. A pathology diagnosis, an ultrasound impression, and a decision to operate contain different information. If I merge them into a single target, a model could appear clinically meaningful while reproducing the selection process that determined which patients received surgery.

## The core ideas

### Cholesterol polyps and adenomatous lesions differ biologically

Cholesterol polyps are non-neoplastic pseudopolyps associated with cholesterol deposition. They are not regarded as precancerous lesions. Adenomas are epithelial neoplasms with malignant potential, but an adenoma diagnosis does not mean invasive cancer is present or inevitable. Older studies also use “adenomatous polyp” more broadly than newer pathological classifications. I need to preserve that terminology when comparing datasets, rather than assuming every historical category maps directly onto a current one. [SRU pathological distinctions](https://pubs.rsna.org/doi/10.1148/radiol.213079)

### Ultrasound shows morphology, with overlapping appearances

Conventional ultrasound can describe a lesion's size, attachment, echogenicity, and surrounding wall. Cholesterol polyps often appear echogenic, but echogenicity is affected by imaging conditions and does not reliably establish histology. Adherent sludge and adenomyomatosis can also complicate identification of a polypoid lesion. I take these limitations to mean that a confident image classification needs a clearly defined reference standard. A plausible appearance alone cannot establish whether a lesion is neoplastic. [SRU imaging assessment](https://pubs.rsna.org/doi/10.1148/radiol.213079)

### Size thresholds belong to specific management frameworks

The [2022 European joint guideline](https://pubmed.ncbi.nlm.nih.gov/34918177/) recommends cholecystectomy for polyps measuring at least 10 mm when the patient is fit for and accepts surgery. The [2025 Korean recommendations](https://doi.org/10.3348/kjr.2024.0914) recommend surgery in surgically fit patients at 15 mm or above, or at 10-14 mm with concerning features such as sessility, adjacent wall thickening, or significant growth. Without those features, surgery or surveillance is an option at 10-14 mm. I understand these as decision thresholds balancing risks, not points where benign tissue becomes malignant.

### Growth requires attention to measurement

A change in recorded diameter may reflect biological growth, measurement variability, or differences between examinations. The Korean recommendations call for assessment across multiple views to identify the longest diameter and acknowledge that growth itself does not establish malignancy. [KSAR measurement and growth guidance](https://doi.org/10.3348/kjr.2024.0914) For an AI study, I would retain the measurement method and examination timing. Otherwise, apparent precision in a growth label could conceal uncertainty in how the underlying images were obtained and compared.

### Pathology answers a different question from management

Histopathology can establish the nature of a removed lesion, but operated patients are a selected population. For my purposes, this creates a distinction between predicting pathology among surgical cases and estimating risk among incidentally detected polyps. A model trained on “surgery versus follow-up” would instead learn a management outcome. I would want to know whether it reproduces size-based decisions, adds information beyond them, or captures local referral practices before interpreting its output as malignant potential.

## Where it touches my work

This topic gives clinical faithfulness auditing a concrete constraint: the evidence must match the claimed target. For a gallbladder ultrasound classifier, I would examine reliance on lesion morphology and size while checking alternatives such as caliper overlays, image selection, and acquisition settings. Size can be valid clinical evidence, yet reproducing a size rule does not demonstrate additional histological discrimination. I would compare against a size-based baseline and preserve the distinction between pathology-confirmed lesions and lesions assessed through surveillance.

## What I have not resolved

- How can I evaluate malignant potential when pathology is selectively available and surveillance does not provide equivalent histological confirmation?
- Which ultrasound descriptors are reproducible enough across readers and devices to serve as clinical audit references?
- How should a model communicate uncertainty near a management threshold when repeated measurements could change the category?

## References

- Kamaya et al., [Management of Incidentally Detected Gallbladder Polyps: Society of Radiologists in Ultrasound Consensus Conference Recommendations](https://pubs.rsna.org/doi/10.1148/radiol.213079), Radiology, 2022.
- Foley et al., [Management and follow-up of gallbladder polyps: updated joint guidelines between the ESGAR, EAES, EFISDS and ESGE](https://pubmed.ncbi.nlm.nih.gov/34918177/), European radiology, 2022.
- Chang et al., [Interpretation, Reporting, Imaging-Based Workups, and Surveillance of Incidentally Detected Gallbladder Polyps and Gallbladder Wall Thickening: 2025 Recommendations From the Korean Society of Abdominal Radiology](https://doi.org/10.3348/kjr.2024.0914), Korean Journal of Radiology, 2025.
