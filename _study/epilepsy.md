---
layout: study_note
title: "Epilepsy"
description: "Seizure classification, EEG interpretation, and diagnosis built from intermittent evidence."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "neurology"
category_title: "Neurology"
order: 4
source: "Lecture"
written: true
updated: "2026-09-08"
---

Epilepsy is a disorder involving an enduring predisposition to epileptic seizures. Diagnosis combines the history of intermittent events with examination, EEG, and imaging, none of which is expected to capture every relevant abnormality at every visit.

## Clinical overview

A seizure is a transient event caused by abnormal neuronal activity; epilepsy is the underlying disorder. The [ILAE practical definition](https://pubmed.ncbi.nlm.nih.gov/24730690/) includes recurrent unprovoked or reflex seizures, a single such seizure with sufficiently high recurrence risk, or an identified epilepsy syndrome. An acute symptomatic seizure during a metabolic disturbance does not automatically establish epilepsy.

Seizures can affect movement, sensation, cognition, autonomic function, or consciousness. Convulsions are only one presentation. I find the distinction between the event, seizure type, epilepsy syndrome, and cause important because each requires a different level of evidence.

## Anatomy and pathophysiology

Focal seizures arise within networks limited to one hemisphere, while generalized seizures involve bilaterally distributed networks. Observable symptoms reflect the networks recruited and how activity spreads. Structural, genetic, infectious, metabolic, immune, and unknown causes can contribute to epilepsy.

An interictal recording samples the brain between seizures. Epileptiform activity may be intermittent, and a scalp recording has limited sensitivity to some sources. Conversely, artifacts and benign variants can resemble abnormal discharges. I read this as a problem of incomplete observation rather than a simple conflict between a patient’s history and a machine signal.

## Diagnostic workflow and imaging findings

### Reconstruct the event before classifying it

History should establish the circumstances, initial symptoms, sequence, duration, recovery, and possible provoking factors. Witness descriptions and available videos can be valuable. Examination, glucose or other relevant laboratory testing, and ECG may identify alternatives or precipitants. The diagnosis depends on the whole event, not merely the most dramatic movement.

### Apply a defined seizure classification

The [2025 ILAE classification](https://doi.org/10.1111/epi.18338) retains focal, generalized, unknown whether focal or generalized, and unclassified categories. It uses consciousness, operationalized through awareness and responsiveness, where applicable. Classification should reflect available evidence; forcing an uncertain event into a familiar category introduces false precision. Historical labels need their classification version recorded.

### Interpret EEG in clinical context

Routine EEG may show focal spikes, sharp waves, or generalized spike-wave discharges that support classification. An evolving ictal pattern can support identification of a recorded seizure. [NICE guidance](https://www.nice.org.uk/guidance/ng217/chapter/1-Diagnosis-and-assessment-of-epilepsy) explicitly advises against using EEG to exclude epilepsy. Sleep-deprived, ambulatory, or video-EEG assessment may be appropriate when uncertainty remains. A waveform must be interpreted with its spatial field, evolution, artifacts, and clinical context.

### Search for a structural cause with appropriate MRI

Epilepsy-protocol MRI can reveal hippocampal sclerosis, cortical malformations, tumors, or previous injury. Hippocampal atrophy with abnormal T2/FLAIR signal can support sclerosis; cortical thickening and blurred gray-white distinction can suggest focal cortical dysplasia. The [ILAE imaging consensus](https://doi.org/10.1111/epi.15612) emphasizes suitable acquisition and expert interpretation. A normal MRI means no lesion was demonstrated by that examination, not that epilepsy is absent.

## Differential diagnosis and management context

Syncope, functional seizures, sleep disorders, migraine phenomena, and metabolic events can resemble epileptic seizures. Some syncopal events include jerking. Functional seizures should not be diagnosed solely because a routine EEG is normal or an event lacks a clear scalp correlate. Capturing a typical event with synchronized video and EEG can help resolve uncertainty when interpreted by experienced clinicians.

Management depends on seizure type, syndrome, cause, recurrence risk, and the person’s circumstances. Antiseizure medication choice and counseling require this classification. Persistent seizures despite appropriate treatment can prompt specialist assessment, including consideration of surgery in suitable cases. An ongoing prolonged seizure requires emergency management rather than completion of an elective diagnostic workup.

## Implications for medical AI

I would distinguish detection of an EEG discharge, detection of a seizure episode, classification of an event, and diagnosis of epilepsy. They have different references and error costs. Evaluation should include continuous recordings, realistic event frequency, artifacts, and false alarms over recording time, rather than only selected abnormal and normal clips.

The connection to my clinical faithfulness work is the need to interpret absent evidence carefully. A short recording and a selected ultrasound frame can both omit the decisive finding. I would preserve patient-level separation and test whether predictions depend on physiological patterns or on electrode artifacts, recording systems, and annotation conventions.

## References

- Fisher et al., [ILAE official report: a practical clinical definition of epilepsy](https://pubmed.ncbi.nlm.nih.gov/24730690/), Epilepsia 2014.
- Beniczky et al., [Updated classification of epileptic seizures: Position paper of the International League Against Epilepsy](https://doi.org/10.1111/epi.18338), Epilepsia 2025.
- Bernasconi et al., [Recommendations for the use of structural magnetic resonance imaging in the care of patients with epilepsy: A consensus report from the International League Against Epilepsy Neuroimaging Task Force](https://doi.org/10.1111/epi.15612), Epilepsia 2019.
- NICE, [Epilepsies in children, young people and adults](https://www.nice.org.uk/guidance/ng217/chapter/1-Diagnosis-and-assessment-of-epilepsy), NG217 2022.
