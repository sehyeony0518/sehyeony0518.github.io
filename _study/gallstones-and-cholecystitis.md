---
layout: study_note
title: "Gallstones and Cholecystitis"
description: "Cholelithiasis, acute and chronic cholecystitis, and the findings that separate them."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "hepatobiliary"
category_title: "Hepatobiliary Medicine & Imaging"
subgroup: "Gallbladder Disease"
order: 5
source: "Independent study"
written: true
updated: "2026-09-08"
---

Cholelithiasis means gallstones are present; cholecystitis means the gallbladder is inflamed. The diagnostic task is to establish whether stones are incidental, causing transient obstruction, or associated with active inflammation and its complications.

## Clinical overview

Gallstones may remain asymptomatic or cause episodes of biliary pain. Acute cholecystitis more often presents with persistent upper abdominal pain and evidence of inflammation, while chronic cholecystitis reflects longstanding inflammatory and fibrotic change. I distinguish stone detection from explaining the current illness.

## Anatomy and pathophysiology

In acute calculous cholecystitis, obstruction at the gallbladder neck or cystic duct promotes distension, inflammation, and potentially impaired perfusion. Infection may contribute, but inflammation is not simply synonymous with bacterial infection. Complications include necrosis, perforation, and localized collections.

Acute acalculous cholecystitis occurs without an obstructing stone and is particularly important in critically ill patients, where stasis and ischemic injury can contribute. Chronic inflammation can produce fibrosis and a contracted, thick-walled gallbladder. Acute inflammation can develop over chronic structural change.

## Diagnostic workflow and imaging findings

### Establish the clinical inflammatory context

The [Tokyo Guidelines 2018](https://pubmed.ncbi.nlm.nih.gov/29032636/) combine local inflammatory signs, systemic inflammatory findings, and characteristic imaging for a definite diagnosis of acute cholecystitis. Local findings include right upper quadrant tenderness or a Murphy sign; systemic evidence includes fever or inflammatory laboratory abnormalities. I read this as a reminder that neither an isolated thick wall nor pain alone establishes the diagnosis.

### Identify stones and assess obstruction

Typical gallstones are echogenic intraluminal foci with posterior acoustic shadowing and movement on repositioning. Very small stones may not produce a clear shadow, and impacted neck stones may remain fixed. A stone-filled gallbladder can produce a wall-echo-shadow complex, obscuring the lumen behind strong interfaces. Sludge more often forms dependent low-level echoes without clean shadowing. These appearances are described by [Yu and colleagues](https://doi.org/10.3748/wjg.v26.i22.2967). The neck and visible bile ducts require attention even when stones are obvious elsewhere.

### Look for a constellation of acute findings

Supportive findings include gallbladder distension, mural thickening or edema, increased mural Doppler flow, pericholecystic fluid, and focal tenderness under the transducer. No single feature is sufficiently specific in isolation. Analgesia, altered consciousness, or advanced wall injury can make tenderness less informative. Fluid and wall edema can also occur with systemic illness. A negative or equivocal ultrasound therefore does not settle every clinically suspected case.

### Separate chronic change and search for complications

Chronic cholecystitis may show a contracted gallbladder containing stones and a fibrotic thickened wall, without the surrounding inflammatory changes expected in an acute episode. Recent eating can also cause contraction. Irregular wall disruption, intraluminal membranes, adjacent collections, or gas raise concern for complicated inflammation. Gas may produce reverberation and dirty shadowing rather than a stone's cleaner shadow. Ultrasound can suggest these complications, but further imaging may be needed to define their extent.

### Resolve uncertainty with the appropriate next test

When acute cholecystitis remains suspected after inconclusive ultrasound, hepatobiliary scintigraphy can assess cystic duct obstruction in a suitable clinical setting. CT is useful for complications and alternative diagnoses; MRI or MRCP can help assess biliary obstruction. Test selection depends on urgency and the unresolved question. The [WSES guidelines](https://doi.org/10.1186/s13017-020-00336-x) discuss additional imaging and emphasize that diagnosis integrates clinical, laboratory, and imaging information.

## Differential diagnosis and management context

Differentials include uncomplicated biliary colic, pancreatitis, hepatitis, peptic disease, and systemic causes of gallbladder edema. Common bile duct obstruction and cholangitis require separate assessment. In suitable patients with acute calculous cholecystitis, WSES supports early laparoscopic cholecystectomy, alongside supportive care and appropriately selected antimicrobials. Patients unsuitable for surgery may need a different strategy, including drainage.

## Implications for medical AI

I read this clinical distinction as a labeling requirement: “stone present,” “acute inflammation,” and “complicated cholecystitis” should not be collapsed into one category. Tenderness, inflammatory blood tests, and disease timing are not fully represented by the image. A model trained on the final clinical diagnosis may therefore be judged against information it never received.

For gallbladder ultrasound auditing, I would examine whether predictions track the relevant constellation rather than stones alone. Device settings influence hyperemia and shadow visibility, while analgesia and clinical documentation affect the reference. This suggests to me that disagreement between an image model and a clinical diagnosis needs case review before being attributed solely to model error.

## References

- Yokoe et al., [Tokyo Guidelines 2018: diagnostic criteria and severity grading of acute cholecystitis (with videos)](https://pubmed.ncbi.nlm.nih.gov/29032636/), Journal of Hepato-Biliary-Pancreatic Sciences 2018.
- Yu et al., [Benign gallbladder diseases: Imaging techniques and tips for differentiating with malignant gallbladder diseases](https://doi.org/10.3748/wjg.v26.i22.2967), World Journal of Gastroenterology 2020.
- Pisano et al., [2020 World Society of Emergency Surgery updated guidelines for the diagnosis and treatment of acute calculus cholecystitis](https://doi.org/10.1186/s13017-020-00336-x), World Journal of Emergency Surgery 2020.
