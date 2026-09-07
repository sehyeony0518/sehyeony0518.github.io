---
layout: study_note
title: "Stroke"
description: "Time-critical diagnosis and imaging triage, and why decision latency is itself a clinical outcome."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "neurology"
category_title: "Neurology"
order: 1
source: "Lecture"
written: true
updated: "2026-09-08"
---

Stroke is acute neurological injury caused by vascular ischemia or hemorrhage. I focus here on the initial recognition and imaging of ischemic stroke and spontaneous intracerebral hemorrhage, where diagnostic delay can change the available treatment.

## Clinical overview

Stroke can cause sudden weakness, sensory loss, speech disturbance, visual loss, or impaired coordination. Posterior circulation events may present with combinations of dizziness, diplopia, ataxia, and altered consciousness that are less easily captured by familiar anterior-circulation patterns. Risk increases with vascular disease, but younger age does not exclude the diagnosis.

The immediate task is to recognize a possible stroke, establish the timing, and distinguish ischemia from hemorrhage while assessing treatment eligibility. Symptom severity alone cannot reliably make that distinction. The [2026 AHA/ASA guideline](https://doi.org/10.1161/STR.0000000000000513) places rapid evaluation within an organized system of acute stroke care.

## Anatomy and pathophysiology

Ischemic stroke follows inadequate blood supply to brain tissue, often from arterial occlusion. The affected territory and collateral circulation influence the deficit and evolution of injury. Tissue with severe injury and surrounding hypoperfused but potentially salvageable tissue do not evolve at a uniform rate. I read this as the reason that elapsed time and imaging findings must be interpreted together.

Intracerebral hemorrhage causes direct tissue injury and can produce mass effect, ventricular extension, and hydrocephalus. Its treatment priorities differ from restoring flow through an occluded artery. The [AHA/ASA intracerebral hemorrhage guideline](https://doi.org/10.1161/STR.0000000000000407) addresses this separate pathway, including stabilization and management of complications.

## Diagnostic workflow and imaging findings

### Establish onset, examination findings, and immediate alternatives

The team documents symptom onset or last-known-well time, assesses neurological deficits, and checks glucose because hypoglycemia can mimic stroke. Medication history, particularly anticoagulant exposure, affects treatment assessment. A structured neurological scale supports communication, but should not replace evaluation of a disabling deficit or a suspected posterior circulation event.

### Obtain rapid brain imaging

Noncontrast CT is commonly used first because it rapidly identifies acute hemorrhage. Early ischemic findings can include loss of gray-white differentiation, insular ribbon obscuration, and sulcal effacement. A hyperdense artery may suggest thrombus. An initially unremarkable CT does not exclude ischemic stroke. [Wintermark and colleagues](https://doi.org/10.3174/ajnr.A3690) describe the diagnostic roles of CT and MRI.

### Identify an occluded vessel and treatment-relevant anatomy

CT angiography of the head and neck can identify a large-vessel occlusion and relevant vascular anatomy. Vascular imaging helps determine whether thrombectomy assessment is needed and supports transfer planning. CT perfusion or MR-based assessment may contribute in selected pathways, particularly when onset is uncertain or presentation is later. Additional imaging should answer a treatment question without unnecessarily delaying an already indicated intervention.

### Use MRI to clarify tissue injury when appropriate

Acute ischemia often produces high signal on diffusion-weighted imaging with reduced apparent diffusion coefficient. FLAIR and susceptibility-sensitive sequences provide complementary information about tissue changes and blood products. Small or early infarcts can remain difficult to detect. Perfusion abnormalities and automated core estimates are measurements with technical limitations, not direct histological truth; motion, timing, and processing require review.

## Differential diagnosis and management context

Important mimics include hypoglycemia, seizure-related deficits, migraine, and functional neurological symptoms. These possibilities are considered during urgent assessment rather than inferred from a negative early CT alone. For eligible patients with disabling ischemic deficits, the [2026 guideline](https://doi.org/10.1161/STR.0000000000000513) supports intravenous thrombolysis within the standard 4.5-hour window and selected extended-window treatment using additional criteria. Selected vessel occlusions warrant thrombectomy evaluation.

Intracerebral hemorrhage instead requires its own pathway, including appropriate blood-pressure management, reversal of anticoagulation when indicated, and assessment for neurosurgical or neurocritical care needs. Treatment eligibility depends on the full clinical and imaging picture. I use current guidance for treatment eligibility.

## Implications for medical AI

I would define separate tasks for hemorrhage detection, vessel-occlusion triage, tissue assessment, and workflow prioritization. Their references, inputs, and harmful errors differ. Evaluation should include acquisition-to-result time, failed studies, missed alerts, and whether an alert actually advances clinical review or treatment.

This suggests to me a connection with gallbladder auditing: clinically meaningful evidence must support the output, but it must also arrive in a usable workflow. Decision latency is a clinically consequential endpoint; a faster algorithm is not proof of better patient outcomes. I would evaluate treatment timing, disability, and safety alongside technical accuracy.

## References

- Prabhakaran et al., [2026 Guideline for the Early Management of Patients With Acute Ischemic Stroke: A Guideline From the American Heart Association/American Stroke Association](https://doi.org/10.1161/STR.0000000000000513), Stroke 2026.
- Greenberg et al., [2022 Guideline for the Management of Patients With Spontaneous Intracerebral Hemorrhage: A Guideline From the American Heart Association/American Stroke Association](https://doi.org/10.1161/STR.0000000000000407), Stroke 2022.
- Wintermark et al., [Imaging Recommendations for Acute Stroke and Transient Ischemic Attack Patients: A Joint Statement by the American Society of Neuroradiology, the American College of Radiology, and the Society of NeuroInterventional Surgery](https://doi.org/10.3174/ajnr.A3690), AJNR 2013.
