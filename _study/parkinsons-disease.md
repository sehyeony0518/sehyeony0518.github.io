---
layout: study_note
title: "Parkinson's Disease"
description: "Movement disorder assessment, rating scales as noisy ground truth, and longitudinal measurement."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "neurology"
category_title: "Neurology"
order: 3
source: "Lecture"
written: true
updated: "2026-09-08"
---

Parkinson’s disease is a progressive neurological disorder diagnosed primarily through its clinical pattern. Movement assessment, treatment response, and change over time contribute different evidence, while imaging usually answers a narrower differential-diagnosis question.

## Clinical overview

Motor symptoms include slowness, rigidity, and often rest tremor, with gait and balance problems developing variably. Nonmotor symptoms can include sleep disturbance, constipation, mood changes, autonomic dysfunction, and cognitive impairment. Their burden may be substantial even when a short motor examination appears relatively reassuring.

Parkinsonism is a syndrome, not a synonym for Parkinson’s disease. In the [Movement Disorder Society criteria](https://doi.org/10.1002/mds.26424), its motor definition requires bradykinesia together with rest tremor or rigidity. Determining the cause then requires supportive features, exclusions, and attention to findings that suggest another disorder.

## Anatomy and pathophysiology

Loss of dopaminergic neurons in the substantia nigra disrupts basal ganglia circuits involved in movement. Parkinson’s disease also involves wider neural systems, which helps explain why replacing dopamine does not address every symptom. Alpha-synuclein pathology is characteristic, but routine clinical diagnosis is not equivalent to pathological confirmation.

Motor performance varies with medication effects, fatigue, stress, and the task being performed. I read this as a reason to distinguish disease progression from the patient’s state during a particular examination. A better movement score after treatment need not mean that the underlying disease has reversed.

## Diagnostic workflow and imaging findings

### Observe bradykinesia and the motor pattern

Examination includes repetitive finger, hand, and foot movements, assessing slowness and decrement in amplitude or speed. The clinician also examines rigidity, rest tremor, posture, arm swing, gait, turning, and balance. Asymmetry can support the pattern. Tremor alone does not establish Parkinson’s disease, and its absence does not exclude it.

### Assess history, response, and atypical features

Medication exposure can reveal drug-induced parkinsonism. The course, nonmotor history, and sustained response to dopaminergic treatment provide additional evidence. Early prominent falls, severe autonomic dysfunction, or abnormal eye movements can raise concern for atypical parkinsonian disorders. The MDS framework treats diagnostic confidence as a synthesis of findings, rather than a single positive sign.

### Use imaging for the question it can answer

Structural MRI can identify vascular injury or other explanations but does not independently diagnose Parkinson’s disease. Dopamine-transporter SPECT can support presynaptic dopaminergic deficit when the distinction from essential tremor remains uncertain, as described in [NICE guidance](https://www.nice.org.uk/guidance/ng71/chapter/Recommendations). Reduced striatal uptake is not specific to Parkinson’s disease among degenerative parkinsonian syndromes.

### Record severity under defined conditions

The [MDS-UPDRS](https://doi.org/10.1002/mds.22340) assesses nonmotor experiences, motor experiences of daily living, motor examination, and motor complications. These parts are not interchangeable measurements. The examination should record medication timing and relevant treatment state. Reader technique and interpretation can affect scores, so repeated measurements need comparable conditions before a change is interpreted as progression.

## Differential diagnosis and management context

Alternatives include essential tremor, drug-induced and vascular parkinsonism, multiple system atrophy, progressive supranuclear palsy, and other neurodegenerative syndromes. Diagnostic reassessment over time can clarify a pattern that was initially incomplete. A supportive imaging result cannot erase clinical features that argue for another cause.

Treatment aims to improve function and quality of life through medication, exercise, rehabilitation, and management of nonmotor symptoms. Selected patients may benefit from advanced therapies, including deep brain stimulation. Choice depends on the pattern of disability, treatment response, cognition, and other clinical factors. A rating-scale total alone does not determine the appropriate intervention.

## Implications for medical AI

I would define whether a model detects parkinsonism, estimates an examination item, measures movement continuously, or predicts future disability. A video system cannot directly observe every component of a clinical examination, such as resistance to passive movement. Agreement with a total score may therefore reflect correlated visible features rather than measurement of each underlying sign.

For longitudinal models, I would retain medication state, recording conditions, reader identity, and repeated patient measurements. The connection to my gallbladder audits is the distinction between an observable feature and a clinical label inferred from wider evidence. I would test whether a model tracks movement changes or instead recognizes the recording setup, clinic, or treatment-associated cues.

## References

- Postuma et al., [MDS clinical diagnostic criteria for Parkinson’s disease](https://doi.org/10.1002/mds.26424), Movement Disorders 2015.
- Goetz et al., [Movement Disorder Society-sponsored revision of the Unified Parkinson’s Disease Rating Scale (MDS-UPDRS): Scale presentation and clinimetric testing results](https://doi.org/10.1002/mds.22340), Movement Disorders 2008.
- NICE, [Parkinson’s disease in adults](https://www.nice.org.uk/guidance/ng71/chapter/Recommendations), NG71 2017.
