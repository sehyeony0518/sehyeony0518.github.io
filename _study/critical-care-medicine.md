---
layout: study_note
title: "Critical Care Medicine"
description: "Continuous monitoring data, deterioration prediction, and the ethical weight carried by such a model."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "critical-care"
category_title: "Critical Care Medicine"
order: 1
source: "Lecture"
written: true
updated: "2026-09-08"
---

Critical care medicine supports patients with life-threatening organ dysfunction while clinicians identify and treat its cause. Continuous measurements help track instability, but interpreting them requires knowing what treatment was being delivered at each moment.

## Clinical overview

Patients may need intensive care for respiratory failure, shock, severe neurological injury, major trauma, or complications of surgery and other illness. Similar physiological disturbances can arise through different mechanisms. I focus on shock and infection-related deterioration because they expose the gap between recognizing abnormal measurements and identifying an actionable cause.

Sepsis is infection-associated, life-threatening organ dysfunction arising from a dysregulated host response, as defined in [Sepsis-3](https://doi.org/10.1001/jama.2016.0287). It is not synonymous with a positive culture, fever, or hypotension. Organ-dysfunction scores summarize selected findings but do not independently establish why those findings occurred.

## Anatomy and pathophysiology

Shock involves inadequate tissue perfusion or oxygen utilization relative to need. Hypovolemic, cardiogenic, distributive, and obstructive mechanisms can coexist. Blood pressure is one observation within that process: restoring a measured pressure does not necessarily resolve every aspect of perfusion or organ injury.

Respiratory, circulatory, renal, and neurological dysfunction interact. Sedation changes consciousness, ventilation changes gas exchange, and vasoactive treatment changes circulation. I read these measurements as observations of a patient under active treatment. A trajectory cannot be interpreted reliably if the interventions shaping it have been removed from the record.

## Diagnostic workflow and imaging findings

### Assess immediate instability and verify the signal

Bedside evaluation addresses airway, breathing, circulation, and neurological state while urgent support begins when needed. Clinicians examine the patient and verify monitoring quality. An arterial waveform may be distorted by the measurement system, and pulse oximetry can be unreliable with poor signal conditions. A monitor alarm is a reason to assess, not a complete diagnosis.

### Combine serial findings with laboratory evidence

Blood gases, lactate, blood counts, renal function, cultures, and other tests address specific clinical questions. Trends can matter more than an isolated value, but measurement frequency itself reflects clinical concern. Lactate elevation is not specific to sepsis or simple volume depletion. Sampling time, result availability, and treatment timing should remain distinguishable.

### Use bedside imaging to narrow the mechanism

Focused echocardiography can assess ventricular function, pericardial fluid, and other findings relevant to shock. Lung ultrasound can show pleural fluid, consolidation, or B-lines, which require interpretation in context. The [international lung-ultrasound recommendations](https://pubmed.ncbi.nlm.nih.gov/22392031/) describe syndrome-based uses of these signs. B-lines alone do not distinguish cardiogenic edema from every other interstitial process. CT may answer further questions when transport is appropriate.

### Reassess response and search for the cause

The team repeatedly reviews perfusion, oxygenation, urine output, mental state, and the response to support. In suspected sepsis, identifying the source guides antimicrobial treatment and source control. The [2026 Surviving Sepsis Campaign guideline](https://pubmed.ncbi.nlm.nih.gov/41869847/) emphasizes urgent management and reassessment, including dynamic measures to guide fluid resuscitation where appropriate. Resuscitation is not a single completed action.

## Differential diagnosis and management context

Hemorrhage, myocardial dysfunction, pulmonary embolism, infection, medication effects, and other conditions can produce overlapping instability. Several may occur together. A patient with suspected infection can also have a noninfectious explanation for deterioration, so diagnostic reassessment continues alongside treatment.

Management balances organ support, treatment of the cause, and avoidance of additional harm. Escalation also depends on prognosis, reversibility, and the patient’s values and goals of care. A high estimated mortality risk does not by itself establish that an intervention is futile or that a patient would decline it.

## Implications for medical AI

I would define deterioration by a clinically meaningful event and an actionable prediction horizon. Intubation or vasopressor initiation records a treatment decision as well as physiology. In an external evaluation, [Wong and colleagues](https://doi.org/10.1001/jamainternmed.2021.2626) found important limitations in a widely implemented sepsis model. Deployment elsewhere therefore cannot substitute for local validation of detection and alert burden.

My connection to gallbladder auditing is the distinction between disease evidence and care-process evidence. I would test whether a model recognizes physiology or clinicians’ existing concern through test ordering and treatment. Evaluation should include useful warning time, missed deterioration, unnecessary escalation, and outcomes under use. A risk estimate describes neither treatment benefit nor the person’s preferences.

## References

- Singer et al., [The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3)](https://doi.org/10.1001/jama.2016.0287), JAMA 2016.
- Volpicelli et al., [International evidence-based recommendations for point-of-care lung ultrasound](https://pubmed.ncbi.nlm.nih.gov/22392031/), Intensive Care Medicine 2012.
- Prescott et al., [Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2026](https://pubmed.ncbi.nlm.nih.gov/41869847/), Critical Care Medicine 2026.
- Wong et al., [External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients](https://doi.org/10.1001/jamainternmed.2021.2626), JAMA Internal Medicine 2021.
