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

A gallstone explains an echogenic focus more readily than it explains a patient's current illness. I separate stone formation, transient obstruction, acute inflammation, and chronic structural damage because each requires different evidence.

## Clinical overview

Cholelithiasis means stones are present in the gallbladder. Many are incidental. Symptomatic stones can produce biliary pain when gallbladder emptying encounters an obstructed outlet, while acute cholecystitis involves sustained inflammation. Despite the term “biliary colic,” the pain can be steady during an episode. Persistent pain, focal tenderness, fever, and inflammatory laboratory abnormalities change the diagnostic question from stone detection to an inflammatory syndrome.

Chronic cholecystitis describes longstanding inflammatory and fibrotic changes, often associated with stones. It is not established merely by a history of recurrent pain, nor does its presence exclude a superimposed acute episode. I would retain the distinction between a clinical presentation, an imaging impression, and a pathological diagnosis when reading a case or constructing its label.

## Anatomy and pathophysiology

### Stone formation and outlet obstruction are different mechanisms

Cholesterol stone formation involves cholesterol supersaturation of bile, crystal nucleation, and retention promoted by impaired gallbladder emptying. Pigment stones have different compositional pathways: black pigment stones are associated with conditions including chronic hemolysis, while brown pigment stones are associated with biliary infection and stasis. These mechanisms explain predisposition, but ultrasound appearance alone does not reliably establish stone composition. The [EASL gallstone guideline](https://doi.org/10.1016/j.jhep.2016.03.005) reviews these distinctions.

A stone lodged at the neck or cystic duct impedes gallbladder drainage. Continued secretion and distension increase intraluminal pressure, while inflammation and edema can compromise mural perfusion. Secondary bacterial infection may contribute, but the initiating injury is not necessarily infectious. Progression can produce gangrene, perforation, or a pericholecystic abscess.

The obstruction's location matters. Isolated cystic duct obstruction need not dilate the common bile duct. A stone that has migrated into the common bile duct creates a separate problem, potentially producing jaundice, pancreatitis, or cholangitis.

### Acalculous and chronic disease complicate the expected pattern

Acute acalculous cholecystitis occurs without an obstructing stone, particularly during critical illness. Gallbladder stasis and ischemic injury can contribute. The same patients may also have fasting-related distension, sludge, ascites, and systemic edema, so several supportive ultrasound findings have competing explanations.

Chronic injury can leave a fibrotic, contracted gallbladder containing stones. However, physiological contraction after eating also reduces the lumen and makes the wall appear thicker. I read this overlap as a requirement to establish preparation and distension before interpreting contraction as disease.

## Diagnostic workflow and imaging findings

### Establish the inflammatory syndrome

The [Tokyo Guidelines 2018](https://pubmed.ncbi.nlm.nih.gov/29032636/) organize acute cholecystitis diagnosis into local inflammatory findings, systemic inflammatory findings, and characteristic imaging. Local findings include right upper quadrant tenderness or a Murphy sign; systemic findings include fever, elevated C-reactive protein, or an abnormal white blood cell count. Local plus systemic evidence supports a suspected diagnosis, with characteristic imaging required for a definite diagnosis under this framework.

I would preserve the timing of these observations. An examination after analgesia or treatment does not represent the same clinical state as the initial assessment. Likewise, a pathology report describing chronic inflammation cannot retrospectively establish whether systemic inflammation was present when an ultrasound frame was acquired.

### Demonstrate the stone and its acoustic behavior

Typical stones are echogenic intraluminal structures with posterior acoustic shadowing. Strong reflection and attenuation reduce the returning signal behind the stone. Repositioning helps demonstrate movement, but an impacted neck stone can remain fixed. Small stones may produce an inconspicuous shadow, particularly when acquisition settings or beam geometry are unfavorable.

The wall-echo-shadow complex occurs when a stone-filled gallbladder presents closely spaced reflective interfaces followed by shadowing. The apparent absence of a visible fluid-filled lumen should not automatically be interpreted as failure to find the organ. Sludge generally produces dependent low-level echoes without a clean shadow, although compact sludge can appear mass-like. [Yu and colleagues](https://doi.org/10.3748/wjg.v26.i22.2967) illustrate these patterns and their mimics.

I would inspect the neck separately from the body. A conspicuous mobile fundal stone can attract attention while an impacted stone at the outlet remains hidden by bowel gas or an incomplete sweep.

### Evaluate inflammation as a constellation

Relevant findings include distension, mural edema, wall thickening, mural hyperemia, pericholecystic fluid, and focal tenderness directly over the imaged gallbladder. The sonographic Murphy sign requires transducer localization and patient interaction. A grayscale frame cannot establish it.

Each finding needs a competing explanation. Ascites can account for surrounding fluid; venous congestion can thicken the wall; recent food intake can alter its apparent thickness. Doppler hyperemia depends on gain, velocity scale, wall filtering, and motion. “No increased flow detected” is therefore different from demonstrating normal perfusion.

In a hypothetical ultrasound examination, a patient has a mobile shadowing stone, a well-distended gallbladder with a thin wall, and no surrounding inflammatory change. The image supports cholelithiasis. If pain has resolved and inflammatory findings are absent, uncomplicated biliary pain remains plausible. Calling this acute cholecystitis from the stone alone would omit the evidence that distinguishes the diagnoses.

### Search for complications and resolve uncertainty

Irregular wall defects, sloughed intraluminal membranes, adjacent collections, and gas raise concern for complicated inflammation. Gas may produce reverberation and dirty shadowing. Advanced wall injury can make the expected tenderness response less dependable. These findings require assessment beyond a simple stone count.

When ultrasound is inconclusive, the next test should address the unresolved mechanism. Hepatobiliary scintigraphy follows hepatocyte uptake and biliary excretion of a radiotracer. Persistent gallbladder nonvisualization under an appropriate protocol supports cystic duct obstruction. Prolonged fasting, severe illness, and hepatocellular dysfunction can complicate interpretation, as described in the [SNM practice guideline](https://pubmed.ncbi.nlm.nih.gov/21078782/).

CT can assess perforation, collections, gas, and alternative abdominal diagnoses. MRI or MRCP can investigate associated duct disease. I would not treat these examinations as interchangeable confirmations of the same image feature.

## Differential diagnosis and management context

The differential includes uncomplicated biliary pain, pancreatitis, hepatitis, peptic disease, and systemic gallbladder edema. Marked jaundice or duct dilatation requires a separate assessment for extrahepatic obstruction. An inflammatory gallbladder appearance also does not exclude an underlying tumor, particularly when a focal irregular abnormality persists.

The [2020 WSES guideline](https://doi.org/10.1186/s13017-020-00336-x) supports early laparoscopic cholecystectomy for suitable patients with acute calculous cholecystitis. Supportive care and antimicrobial decisions accompany source management. Being medically high risk is not identical to being unsuitable for surgery; drainage is an option for selected patients who cannot undergo an operation.

For study purposes, I distinguish treatment choice from disease severity. Drainage may reflect comorbidity, physiological instability, or local expertise. It should not automatically become a label for more severe image morphology.

## Implications for medical AI

### Test whether the model separates stones from inflammation

I would construct separate references for stone presence, acute clinical cholecystitis, and complications. For the acute diagnosis, adjudication would include contemporaneous symptoms, laboratory findings, and imaging. For frame-level features, readers would independently annotate visible stones, wall edema, surrounding fluid, and assessability.

A feasible audit would compare four groups: stones with acute inflammation, stones without acute inflammation, acalculous inflammation, and neither finding. This exposes a classifier that succeeds mainly by recognizing shadowing stones. Performance in an unstratified cohort could conceal that failure.

For a fixed decision threshold $$t$$ and score $$s_i$$, sensitivity among patients in subgroup $$G$$ is

$$
\mathrm{Sensitivity}_G(t)=
\frac{\sum_{i\in G}\mathbf{1}(y_i=1)\mathbf{1}(s_i\geq t)}
{\sum_{i\in G}\mathbf{1}(y_i=1)}.
$$

Here, $$y_i=1$$ denotes the adjudicated acute diagnosis, and $$\mathbf{1}$$ is the indicator function. The quantity is undefined if the subgroup contains no positive cases. I would choose the threshold before examining subgroup results and calculate uncertainty at the patient level.

### Audit acquisition and documentation pathways

A specific shortcut hypothesis is that suspected inflammation prompts wall measurements and Doppler acquisition, whereas routine stone examinations contribute mainly grayscale images. Calipers, color boxes, or a bedside scanner's export layout could therefore predict the diagnosis through clinical workflow.

I would first measure these associations, then test paired marked and unmarked exports where identical tissue pixels are available. Removing an overlay from a different frame would also change anatomy and speckle, weakening the interpretation.

Another attackable question is whether errors concentrate in stone-positive cases with systemic edema. Readers could annotate the inflammatory constellation while blinded to model scores. I read this as a test of whether the classifier distinguishes local inflammatory evidence from a thick wall that has another plausible cause.

## References

- Yokoe et al., [Tokyo Guidelines 2018: diagnostic criteria and severity grading of acute cholecystitis (with videos)](https://pubmed.ncbi.nlm.nih.gov/29032636/), Journal of Hepato-Biliary-Pancreatic Sciences 2018.
- Yu et al., [Benign gallbladder diseases: Imaging techniques and tips for differentiating with malignant gallbladder diseases](https://doi.org/10.3748/wjg.v26.i22.2967), World Journal of Gastroenterology 2020.
- Pisano et al., [2020 World Society of Emergency Surgery updated guidelines for the diagnosis and treatment of acute calculus cholecystitis](https://doi.org/10.1186/s13017-020-00336-x), World Journal of Emergency Surgery 2020.
- EASL, [EASL Clinical Practice Guidelines on the prevention, diagnosis and treatment of gallstones](https://doi.org/10.1016/j.jhep.2016.03.005), Journal of Hepatology 2016.
- Tulchinsky et al., [SNM practice guideline for hepatobiliary scintigraphy 4.0](https://pubmed.ncbi.nlm.nih.gov/21078782/), Journal of Nuclear Medicine Technology 2010.
