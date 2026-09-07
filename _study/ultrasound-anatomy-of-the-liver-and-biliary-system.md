---
layout: study_note
title: "Ultrasound Anatomy of the Liver and Biliary System"
description: "The anatomy a sonographer works through, including the variants that change what a normal study looks like."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "hepatobiliary"
category_title: "Hepatobiliary Medicine & Imaging"
subgroup: "Anatomy & Imaging Foundations"
order: 1
source: "Independent study"
written: true
updated: "2026-09-08"
---

Hepatobiliary ultrasound anatomy is a map of liver tissue, vessels, ducts, and the gallbladder across moving scan planes. Normal variation changes that map without necessarily indicating disease.

## Clinical overview

The examination is commonly used for abdominal pain, jaundice, abnormal liver tests, and suspected hepatobiliary disease. Its anatomical task is to establish which structure is being seen, whether the relevant region has been adequately examined, and how any finding relates to adjacent structures. I organize this topic around recognizable landmarks rather than memorized appearances from isolated images.

## Anatomy and pathophysiology

The liver receives blood through the portal vein and hepatic artery; hepatic veins drain into the inferior vena cava. Portal branches run within functional segments, while major hepatic veins help define boundaries between them. The plane through the middle hepatic vein toward the gallbladder fossa approximates the division between functional right and left liver. Surface lobes and functional segmentation are not identical. [Draghi and colleagues](https://doi.org/10.1016/j.jus.2007.02.002) describe these vascular landmarks.

Bile drains through intrahepatic ducts into the right and left hepatic ducts, which usually form the common hepatic duct. After the cystic duct joins, the channel is called the common bile duct. The gallbladder stores and concentrates bile beneath the liver. Its fundus, body, and neck form a continuous lumen, but their orientation varies. The distal common bile duct passes through or behind the pancreatic head toward the duodenum.

## Diagnostic workflow and imaging findings

### Establish orientation and survey the liver

A systematic survey uses longitudinal, transverse, and oblique views through subcostal and intercostal windows. The diaphragm, right kidney, inferior vena cava, and portal vein provide orientation. The liver should be inspected for contour, parenchymal uniformity, and focal abnormalities, with attention to regions obscured by ribs or bowel gas. The [AIUM practice parameter](https://doi.org/10.1002/jum.15874) emphasizes examination of the hepatic lobes and major vessels. A visible central liver does not establish that the dome and peripheral margins were assessed.

### Distinguish portal vessels from hepatic veins

Portal vein branches generally have conspicuous echogenic walls and can be followed from the porta hepatis into the liver. Hepatic veins converge toward the inferior vena cava and usually have less conspicuous walls. Their appearance also depends on beam orientation. Color and spectral Doppler help establish vascular continuity and flow characteristics; a tubular dark structure should not be called a bile duct merely because color is absent at one setting.

### Follow the biliary pathway

The extrahepatic duct is sought near the portal vein and followed distally where possible. Duct caliber is measured perpendicular to its long axis, with the location documented. Small normal intrahepatic ducts may not be conspicuous. Age, prior cholecystectomy, and measurement location affect interpretation of duct size, as discussed by [Lucius and colleagues](https://doi.org/10.3390/diagnostics15070919). I would interpret apparent dilatation with symptoms, laboratory findings, and the extent of duct visualization, rather than apply one universal number.

### Recognize variants before assigning pathology

A folded fundus, often called a Phrygian cap, can resemble a septum or localized abnormality in one plane. Gallbladder position, shape, and number can vary; these variations are illustrated by [Meilstrup and colleagues](https://pubmed.ncbi.nlm.nih.gov/1950867/). Following the lumen through multiple planes helps distinguish a fold from a discrete lesion. Biliary branching and cystic duct insertion also vary, and routine ultrasound may not define them completely. Unexpected anatomy should be documented rather than forced into a standard diagram.

## Differential diagnosis and management context

Vessels can mimic dilated ducts, folds can mimic masses, and adjacent bowel can complicate gallbladder identification. Failure to visualize the gallbladder is not itself proof of congenital absence. Prior surgery, contraction, unusual position, and technical limitations need consideration. When symptoms or biochemical evidence suggest obstruction despite an incomplete ultrasound assessment, further imaging such as MRCP or endoscopic ultrasound may be appropriate.

## Implications for medical AI

I read this anatomy as a requirement for spatial and examination-level context. A gallbladder classifier trained only on typical longitudinal views may mistake a fold or unusual orientation for pathology. A label of “normal” should distinguish adequate assessment from incomplete visualization.

For my ultrasound and clinical faithfulness work, I would retain view orientation, visible landmarks, anatomical variants, and examination limitations. This suggests to me that an anatomically plausible heatmap is only an initial check: the model may recognize the expected organ location while missing the structural relationship needed to interpret the finding.

## References

- Draghi et al., [Ultrasound examination of the liver: Normal vascular anatomy](https://doi.org/10.1016/j.jus.2007.02.002), Journal of Ultrasound 2007.
- AIUM, [The AIUM Practice Parameter for the Performance of an Ultrasound Examination of the Abdomen and/or Retroperitoneum](https://doi.org/10.1002/jum.15874), Journal of Ultrasound in Medicine 2022.
- Lucius et al., [Ultrasound of Bile Ducts: An Update on Measurements, Reference Values, and Their Influencing Factors](https://doi.org/10.3390/diagnostics15070919), Diagnostics 2025.
- Meilstrup, Hopper, and Thieme, [Imaging of gallbladder variants](https://pubmed.ncbi.nlm.nih.gov/1950867/), AJR 1991.
