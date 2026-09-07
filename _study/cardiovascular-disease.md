---
layout: study_note
title: "Cardiovascular Disease"
description: "Risk prediction over long horizons, calibration, and decision thresholds tied to treatment."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "cardiovascular"
category_title: "Cardiovascular Medicine"
order: 1
source: "Lecture"
written: true
updated: "2026-09-08"
---

Cardiovascular disease includes disorders of the heart and blood vessels. I focus here on atherosclerotic cardiovascular disease and primary prevention, where a risk estimate can guide treatment before a first clinical event.

## Clinical overview

Hypertension, dyslipidemia, smoking, diabetes, kidney disease, and family history contribute to cardiovascular risk. A person can have substantial atherosclerotic burden without symptoms. Conversely, new chest discomfort or breathlessness requires assessment of a current problem rather than interpretation solely through a long-term prevention score.

The first distinction is whether the patient already has established disease, such as a previous myocardial infarction, ischemic stroke, or peripheral arterial disease. Primary prevention and prevention of recurrent events use different clinical frameworks. I would establish that distinction before interpreting any estimated probability.

## Anatomy and pathophysiology

Atherosclerosis involves lipid accumulation, inflammation, and remodeling within arterial walls. Plaque can narrow the lumen, but an acute event can also follow plaque disruption and thrombosis. The most severe visible narrowing is therefore not a complete description of future event risk.

Cardiovascular disease also includes heart failure, arrhythmias, and valvular disorders, which overlap with but are not identical to atherosclerosis. A composite outcome that includes heart failure differs from one restricted to atherosclerotic events. I read this as a clinical reason to inspect a risk model’s endpoint rather than treat every “cardiovascular risk” estimate as interchangeable.

## Diagnostic workflow and imaging findings

### Establish the risk-factor profile

Assessment includes medical and family history, smoking, medication use, properly measured blood pressure, lipids, and relevant metabolic and kidney measures. A single unusual measurement may need confirmation. The values used in a risk equation should correspond to its definitions and the patient’s current treatment state, rather than whichever numbers are easiest to retrieve.

### Separate acute diagnosis from prevention

For suspected acute coronary disease, ECG findings and serial cardiac troponin measurements contribute to an urgent diagnostic pathway. Neither an isolated normal ECG nor a favorable prevention score excludes an acute problem. The [2021 chest-pain guideline](https://doi.org/10.1161/CIR.0000000000001029) organizes testing around symptoms, clinical assessment, and the likelihood of current disease.

### Estimate a defined outcome over a defined horizon

The [PREVENT equations](https://doi.org/10.1161/CIRCULATIONAHA.123.067626) estimate cardiovascular outcomes over specified horizons, including 10-year and, in applicable populations, 30-year risk. Outcome-specific estimates matter. The [2026 dyslipidemia guideline](https://doi.org/10.1161/CIR.0000000000001423) uses PREVENT-ASCVD for relevant primary-prevention lipid decisions. A result should retain the equation, endpoint, horizon, and population assumptions that produced it.

### Use imaging when it can resolve a clinical question

Coronary artery calcium scoring measures calcified plaque on noncontrast CT and can refine selected prevention decisions. It does not directly measure stenosis, and absent calcium does not exclude noncalcified plaque. Coronary CT angiography assesses plaque and lumen anatomy in appropriate diagnostic settings. Stress imaging evaluates inducible ischemia, while echocardiography examines cardiac structure and function. These tests answer different questions and are not interchangeable screening measures.

## Differential diagnosis and management context

Chest symptoms can arise from coronary ischemia, pulmonary disease, gastrointestinal conditions, musculoskeletal causes, or other disorders. Breathlessness can reflect heart failure, pulmonary disease, anemia, or deconditioning. The clinical setting determines whether the task is urgent diagnosis, investigation of stable symptoms, or prevention in an asymptomatic person.

Preventive management combines lifestyle measures, control of modifiable risk factors, and medication when indicated. Some conditions justify treatment without relying on a general-population risk threshold. For risk-based decisions, the threshold must match the equation and intended intervention. The 2026 guideline combines estimated risk with additional clinical information and selective calcium scoring when appropriate. A threshold is a decision rule, not a boundary between healthy and diseased arteries.

## Implications for medical AI

I would evaluate long-horizon prediction using a clearly defined baseline, follow-up period, and event reference. Loss to follow-up, death from other causes, and treatment initiated during follow-up affect interpretation. A model trained on outcomes under observed care does not directly estimate what would happen without treatment.

This suggests to me that calibration and decision benefit need separate evidence from discrimination. An imaging model might detect clinically relevant plaque yet misestimate absolute risk in another population. As in my gallbladder work, I would audit evidence reliance while also asking whether the output changes management appropriately. Predicting an event and predicting who benefits from an intervention remain different tasks.

## References

- Gulati et al., [2021 AHA/ACC/ASE/CHEST/SAEM/SCCT/SCMR Guideline for the Evaluation and Diagnosis of Chest Pain: A Report of the American College of Cardiology/American Heart Association Joint Committee on Clinical Practice Guidelines](https://doi.org/10.1161/CIR.0000000000001029), Circulation 2021.
- Khan et al., [Development and Validation of the American Heart Association’s PREVENT Equations](https://doi.org/10.1161/CIRCULATIONAHA.123.067626), Circulation 2024.
- Blumenthal et al., [2026 ACC/AHA/AACVPR/ABC/ACPM/ADA/AGS/APhA/ASPC/NLA/PCNA Guideline on the Management of Dyslipidemia: A Report of the American College of Cardiology/American Heart Association Joint Committee on Clinical Practice Guidelines](https://doi.org/10.1161/CIR.0000000000001423), Circulation 2026.
