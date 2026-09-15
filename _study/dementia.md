---
layout: study_note
title: "Dementia"
description: "Biomarker-based diagnosis and the difficulty of validating prediction far ahead of an event."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "neurology"
category_title: "Neurology"
order: 2
source: "Lecture"
written: true
updated: "2026-09-08"
---

## Core question and definition

What does an image of the brain establish about cognitive impairment, its cause and its future course?

Dementia is a syndrome of acquired cognitive decline that interferes with independent everyday functioning. It describes a clinical state. Alzheimer’s disease, vascular injury, Lewy body disease and frontotemporal degeneration are among its possible causes.

The distinction between syndrome and cause is fundamental. A person can have evidence of a disease process without having dementia. A person with dementia can have more than one contributing process. A scan showing tissue loss cannot by itself establish how independently that person manages daily life.

Mild cognitive impairment describes cognitive difficulty with relative preservation of independence. A person may take longer, use reminders or make occasional errors while still managing activities. The boundary with dementia therefore depends on function as well as test performance.

For medical AI, several apparently similar classification tasks make different claims:

| Target | Required meaning of the label |
| --- | --- |
| Cognitive impairment | Performance or reported change in specified cognitive domains |
| Dementia syndrome | Cognitive decline interfering with independent functioning |
| Etiological diagnosis | The disease process or processes judged to explain impairment |
| Biomarker status | A result from a specified biological assay or imaging procedure |
| Future dementia | A defined clinical outcome over a specified follow-up horizon |
| Functional prognosis | Future ability to perform specified activities under observed care |

A model trained to separate established dementia from healthy volunteers has not thereby learned early diagnosis, disease mechanism or future conversion. Those claims require different populations, observations and references.

The study problem is to keep these levels separate while understanding how they are related.

## Key concepts

### Cognitive symptoms follow damage to networks, not a single “memory centre”

Cognition depends on interacting systems supporting attention, memory, language, visuospatial processing, executive control and behaviour.

The hippocampus and adjacent medial temporal structures are important for forming new episodic memories. Frontal systems contribute to planning, inhibition, initiation and flexible organisation. Parietal and other association networks contribute to spatial processing and integration of information.

Damage to different networks therefore produces different patterns of difficulty. A patient may repeatedly forget recent conversations, lose word meaning, become unable to organise a familiar task or misinterpret the spatial arrangement of objects.

These patterns help localise dysfunction, but they do not create a one-to-one map between symptom and pathology. A distributed task can fail when several different parts of its supporting network are disrupted.

For example, poor recall can reflect impaired storage, ineffective retrieval, poor attention during learning, language difficulty or misunderstanding of the task. The clinician considers how the person learned the information, whether cues help and what other domains are affected.

A single screening total compresses these distinctions. Two patients with similar totals may have different patterns, causes and functional consequences.

An image model predicting that total should therefore not be described as having identified one specific cognitive mechanism.

### Alzheimer pathology: why memory and tissue structure can change

Alzheimer’s disease is associated with amyloid plaques, abnormal tau accumulation, synaptic dysfunction and neuronal loss.

Amyloid and tau are biological features of the disease process. They are not directly visible as ordinary structures on routine MRI. Structural imaging principally shows consequences at the scale of tissue organisation, such as regional volume loss.

In a common clinical pattern, dysfunction of medial temporal memory systems contributes to difficulty retaining new information. As additional networks are affected, language, spatial processing, executive function and everyday independence may also deteriorate.

The sequence is not identical in every person. Some presentations are initially dominated by language or visuospatial problems. The absence of a classic memory-led presentation does not make the biological question disappear.

Nor does a visible degree of atrophy uniquely determine symptom severity. The distribution of injury, prior abilities, other diseases and the demands of everyday life all influence how impairment becomes apparent.

This is why an image-to-diagnosis relationship is probabilistic. The same broad structural pattern can occur in people with different functional states, and clinically important impairment can occur before dramatic structural changes are evident.

### Other disease processes can produce overlapping impairment

Vascular disease can damage cognition through large infarcts, strategically placed smaller injuries and diffuse disruption of white-matter connections. The consequence depends on location and network involvement, not merely the total volume of abnormal tissue.

Lewy body disease can affect cognitive, perceptual, motor and sleep-related systems. Fluctuating attention, recurrent visual hallucinations, Parkinsonism and dream-enactment behaviour can contribute to the clinical pattern.

Frontotemporal degeneration can prominently affect behaviour, personality, executive control or language. A person may lose social judgement or word knowledge while performing relatively well on some familiar memory tasks.

These processes can coexist with Alzheimer pathology. Finding one plausible contributor does not establish that all others are absent.

“Mixed pathology” is therefore more than a nuisance category. It challenges the assumption that every patient belongs to a single mutually exclusive biological class.

A classifier forced to choose one diagnosis may be reproducing the coding convention of a clinic rather than the complete disease state. The reference should distinguish a primary clinical diagnosis, documented copathology and uncertainty about causal contribution.

### Reserve and context separate biological burden from observed disability

People begin with different cognitive abilities, learned strategies, occupational demands and support systems. These differences affect when a decline becomes noticeable and when it disrupts independence.

A person who previously managed complex finances may experience meaningful decline while still performing above a population screening threshold. Another person may score poorly because the assessment uses an unfamiliar language or educational format.

Daily function is also contextual. If another household member has always handled a task, the patient’s lack of participation does not establish loss of that ability. Conversely, family members may quietly compensate for errors, making the patient appear more independent than they are.

The clinician therefore asks about change from the person’s own baseline and the reason assistance is needed.

This matters for labels. “Needs help with shopping” could reflect cognitive difficulty, poor mobility, sensory impairment, access to transport or ordinary household roles.

An image cannot directly disambiguate those reasons. A functional label requires clinical interpretation of behaviour in context, even when brain imaging contributes useful evidence about possible causes.

### Establishing the syndrome: change, domains and independence

The diagnostic assessment begins with history from the patient and, where possible, an informant familiar with everyday functioning.

The clinician asks what changed, when it changed and how the change affects activities. They distinguish a persistent pattern from isolated lapses and assess whether problems are progressive, fluctuating, abrupt or associated with an acute illness.

Cognitive examination then samples relevant domains. Interpretation includes language, education, hearing, vision, motor limitations, fatigue and the testing environment.

Functional assessment asks whether the person can safely and reliably carry out activities they previously managed. It is not sufficient to document that a task was completed once under supervision.

The syndrome is assembled from these observations. A screening score supports the assessment but does not replace history or establish cause.

For an AI dataset, the practical consequence is that a “dementia” label should ideally retain its basis: cognitive findings, evidence of decline, functional consequences and the assessment context.

Without this information, disagreement between model and label is hard to interpret. The model may have missed relevant imaging evidence, or the label may depend mainly on information the image cannot contain.

### Delirium and other contributors must remain in the reasoning

Delirium involves an acute disturbance of attention and awareness, often with fluctuation. It can occur in someone with an underlying neurodegenerative disorder and temporarily worsen cognitive performance.

A low test score during acute illness therefore does not automatically measure the patient’s stable cognitive state.

Depression, medication effects, sleep problems, sensory impairment and systemic illness can also contribute to cognitive difficulty. Their presence does not automatically exclude neurodegeneration; several factors may operate together.

The clinical task is to identify contributions and assess the course, not simply place every patient into “degenerative” or “reversible” categories.

Some structural alternatives, such as a mass, subdural collection or hydrocephalus, can also matter. Their imaging appearance must be interpreted with the clinical presentation. Ventricular enlargement, for example, can arise from different mechanisms and does not independently establish a particular treatable syndrome.

An image model that identifies chronic atrophy in an acutely confused patient may be detecting a real background finding while failing to explain the current deterioration.

The target must specify whether it concerns underlying disease, present cognitive state or the cause of an acute change.

### Differential diagnosis as a pattern comparison

| Clinical possibility | Findings that can support consideration | Why the finding is not decisive alone |
| --- | --- | --- |
| Alzheimer-pattern disease | Progressive difficulty retaining new information; compatible regional atrophy or biomarkers | Other disorders can impair memory, and copathology may contribute |
| Vascular cognitive impairment | Relevant vascular injury, focal deficits or executive and processing difficulties | White-matter abnormalities can be incidental or only partly explanatory |
| Lewy body dementia | Cognitive fluctuation, visual hallucinations, Parkinsonism and sleep-related features | Individual features have other causes and may not all be present |
| Frontotemporal disorder | Early behavioural change, language impairment or executive dysfunction | Psychiatric, developmental and other neurological conditions can overlap |
| Delirium | Acute onset, fluctuation and impaired attention in an appropriate context | Underlying dementia may coexist |
| Depression or other contributing conditions | Mood symptoms, sleep disturbance, medication effects or systemic illness | Improvement in a contributor does not prove the absence of degeneration |

A supposedly distinctive course also needs caution. Vascular cognitive impairment need not always follow obvious stepwise declines. Alzheimer-related impairment need not always begin with the same memory complaint.

The useful question is whether the proposed cause explains the timing, affected domains, examination and investigations better than its alternatives.

A model should be tested against clinically plausible alternatives, not only against a healthy-control group selected to have few competing problems.

### Structural MRI: why atrophy is visible and why its cause remains uncertain

Neuronal and synaptic loss can eventually be accompanied by macroscopic tissue loss. On structural imaging, this can appear as reduced regional volume, thinner cortex, widened sulci or enlargement of adjacent cerebrospinal-fluid spaces.

The observation is about anatomy. It does not directly count neurons, identify a protein deposit or measure memory performance.

Regional patterns can nevertheless be informative. Medial temporal atrophy can support a particular interpretation in an appropriate clinical setting. Frontal or anterior temporal predominance can support another pattern.

Several limits follow:

- Regional volumes vary between people before disease.
- Normal ageing and different diseases can produce overlapping changes.
- Early disease may have little conspicuous atrophy.
- Image quality and segmentation methods affect measurements.
- A regional abnormality may be real without being the dominant cause of current symptoms.

A model can exploit subtle distributed associations beyond a human visual rating. That possibility does not make its output a direct assay of pathology.

The claim still requires validation against the target actually being predicted, with careful attention to age, scanner, recruitment and diagnostic reference.

### MRI sequences observe different aspects of injury

| Image or sequence | Main observation relevant here | Important limitation |
| --- | --- | --- |
| Structural anatomical MRI | Regional morphology and tissue volume | Atrophy is not uniquely etiological |
| FLAIR and related imaging | White-matter abnormalities and other changes in tissue water | Hyperintensity is a signal description with several possible causes |
| Diffusion imaging | Changes in water diffusion, including acute tissue injury | Abnormal diffusion is not a general dementia diagnosis |
| Susceptibility-sensitive imaging | Blood products and related susceptibility effects | A microbleed does not by itself quantify its contribution to cognition |
| CT | Gross atrophy, major vascular injury and some structural alternatives | Subtle findings may be less assessable than with an appropriate MRI examination |

A dataset described simply as “brain MRI” can therefore contain materially different inputs.

A model may infer which diagnostic pathway a patient entered from the sequences acquired. If specialist cases receive a different protocol from controls, protocol recognition can become a shortcut.

The presence of an additional sequence is also not equivalent to a positive finding on that sequence. Acquisition choices and measured abnormalities should be represented separately when auditing the model.

### Molecular and functional biomarkers answer narrower questions

Amyloid PET measures the distribution of a tracer related to amyloid pathology. Cerebrospinal-fluid assays measure specified molecular quantities. Other tests may assess tau-related pathology or aspects of brain metabolism.

These measurements can contribute evidence about disease biology. They are not interchangeable with a dementia syndrome or a precise prediction of when independence will be lost.

FDG-PET, for example, concerns glucose metabolism. A regional metabolic pattern can support a diagnostic interpretation, but it is not a direct measure of a person’s daily functioning.

Likewise, an amyloid-positive result does not establish that amyloid-related disease explains every symptom. Vascular injury, Lewy body disease or other contributors may also be present.

An unspecified “biomarker-positive” label is inadequate for research. The dataset should identify the assay or imaging procedure, its interpretation, sample handling where relevant, and the clinical population in which it was obtained.

A model predicting biomarker status from structural MRI is estimating an association between modalities. It is not directly observing the molecule through the MRI image.

That distinction remains necessary even when prediction is useful.

### Where the ground truth comes from

| Reference | What it establishes most directly | Main source of uncertainty |
| --- | --- | --- |
| Clinical consensus | An integrated judgement about syndrome and likely cause | Incomplete information, disagreement and evolving presentation |
| Cognitive test | Performance on specified tasks at an assessment | Language, education, sensory factors and state |
| Functional assessment | Ability and assistance needs in defined activities | Informant knowledge, household roles and noncognitive limitations |
| Molecular biomarker | Evidence about a specified biological process | Assay interpretation, timing and incomplete explanation of symptoms |
| Longitudinal diagnosis | A later clinically recognised outcome | Follow-up intensity, visit timing and diagnostic practice |
| Registry code | A recorded designation | Coding conventions, delayed recording and uncertain diagnostic basis |
| Neuropathology | Tissue-level disease findings | Selection of donors, copathology and the interval from earlier imaging |

Clinical consensus can be an appropriate reference for a clinical syndrome. It should not be described as pathological truth.

Conversely, pathology does not retrospectively make every baseline image diagnostic. Tissue examined much later answers a different temporal question.

If MRI contributed to the consensus diagnosis, evaluating an MRI model against that diagnosis also requires acknowledging incorporation of imaging into the reference. The comparison can still be useful, but it is not an entirely independent demonstration of etiological validity.

The strongest label is the one matched to the claim, with its provenance visible.

### Future dementia requires an explicit time structure

A prognosis study needs an index time, information available at that time, an outcome definition and a prediction horizon.

“Eventually diagnosed with dementia” is insufficient. A person followed briefly and a person followed extensively have different opportunities for an event to be recognised.

The date of a diagnosis code may also differ from the onset of impairment. More frequent visits can produce earlier recorded recognition without changing the biological course.

Loss to follow-up is not automatically a negative outcome. Death before the target event is a competing event whose treatment depends on the question being estimated.

Treatment and support during follow-up can affect observed function and recognition. A prediction of outcomes under actual care should not be reinterpreted as an untreated natural-history forecast.

The model’s inputs also require a time boundary. A report written after the outcome, a later biomarker result or a future diagnostic code cannot become a baseline predictor merely because it appears in the same patient record.

These are failures of target definition and temporal validity, not problems that a larger network can solve.

### Why a patient-level split is necessary but insufficient

Separating patients prevents direct reuse of the same individual across development and evaluation. It does not remove every easy distinction between diagnostic groups.

Patients with established dementia may be recruited through specialist clinics, while controls come from healthy volunteer programmes. The groups can differ in age, comorbidity, scanner protocol, movement during imaging and intensity of assessment.

A model might consequently recognise recruitment pathways as well as disease-related structure.

Restricting all images to a common preprocessing pipeline helps define the input, but does not guarantee that the remaining signal is clinically appropriate.

Useful evaluation examines clinically relevant comparison groups, including people with cognitive complaints who do not meet the target diagnosis. It also records failed scans and incomplete assessments rather than discarding them without explanation.

External validation should specify what changed: institution, recruitment, language, reference procedure, scanner or care pathway. A new site is evidence about a particular transport problem, not a universal test of generalisation.

### Consequences of false positive and false negative claims

A false dementia diagnosis can alter expectations, autonomy and family decisions. It may divert attention from another explanation or lead to unnecessary restrictions and investigations.

A false negative can delay support, safety assessment, planning and evaluation of contributing conditions.

An incorrect etiological label adds another layer. A patient may genuinely have cognitive impairment while the proposed explanation is wrong or incomplete.

Prognostic errors have distinct consequences. An overly certain prediction of decline can create avoidable distress and poor planning. False reassurance can leave a patient and family unprepared.

The operating point therefore depends on whether the model prompts assessment, supports differential diagnosis, estimates risk or communicates a prognosis.

An uncertainty flag should also be meaningful. It may reflect unassessable imaging, ambiguous clinical information or uncertainty about future events. These are different reasons for uncertainty and should not be collapsed into one uninterpretable confidence score.

### Worked reasoning examples

**Marked atrophy with preserved reported independence.** The scan provides evidence about brain structure. The clinician still needs to establish cognitive change, actual task performance and whether support is masking difficulty. Atrophy alone does not settle the syndrome boundary.

**Acute confusion in a person with chronic cognitive decline.** A model identifies an Alzheimer-like structural pattern. That may concern the background disease, while the immediate deterioration reflects an additional acute process. The image classification does not explain the whole presentation.

**A participant with impairment disappears from follow-up.** The database contains no later dementia code. Labelling the participant “non-converter” assumes an outcome that was not observed. The record instead needs a last known assessment and an explicit missing-outcome strategy.

**An MRI model predicts an amyloid result correctly.** This establishes predictive agreement with that biomarker reference in the tested population. It does not establish current dementia, explain every symptom or specify an individual date of future decline.

These hypothetical cases illustrate different evidential questions; they are not clinical outcome estimates.

### A study specification that makes the claim reviewable

Before training, I would write down:

- Whether the target is a syndrome, cause, biomarker or future outcome.
- The intended population and the clinical reason for assessment.
- The index time and permitted input information.
- The role of imaging in constructing the reference.
- How functional independence was assessed.
- How mixed diagnoses and uncertain cases are represented.
- How follow-up, censoring and competing events are handled.
- Which decision the output is intended to support.

Evaluation should then match that specification. A model predicting current clinical categories needs a credible clinical reference. A biomarker surrogate needs the specified assay. A prognosis model needs temporal follow-up and calibration for its stated horizon.

A useful representation audit can ask whether the model encodes atrophy, vascular injury or acquisition characteristics. Showing that a feature is decodable from the representation still does not prove that it caused the diagnostic output.

### Revision checklist

| Question | What I should be able to explain |
| --- | --- |
| What distinguishes dementia from a biomarker result? | Dementia requires a clinical syndrome with functional consequences |
| Why is baseline important? | Impairment concerns acquired change in a particular person |
| Why is a screening score insufficient? | It compresses domains and depends on context |
| Why can similar scans accompany different symptoms? | Injury distribution, prior abilities and copathology differ |
| What does atrophy establish? | A structural pattern, not a unique molecular cause |
| Why can MRI be unremarkable in early disease? | Functional and molecular changes need not produce conspicuous anatomy |
| What does an amyloid result establish? | Evidence concerning a specified pathology |
| Why retain mixed diagnoses? | Multiple processes can contribute to impairment |
| Why is absent follow-up not a negative label? | The outcome may not have been observed |
| Why specify a prediction horizon? | Risk and outcome ascertainment depend on time |
| Why can diagnosis date mislead? | Recognition and coding occur through a care process |
| What demonstrates utility? | Evidence about consequences of using the output in care |

### Connecting the clinical reasoning to the ontology

Different mechanisms can manifest as overlapping cognitive findings. Clinical assessment determines which findings constitute a syndrome and which causes plausibly explain it.

`Reference standard adjudication` is therefore central to `Clinical validity`: a biomarker, functional assessment and later diagnosis are not interchangeable references.

`Clinical assessability` limits `Clinical evidence reliance`. Structural MRI may support an atrophy assessment while providing no direct observation of medication management or financial independence.

`External validation` assesses `Transportability`; it does not establish that predictions improve care. That latter question belongs to `Clinical utility` and an evaluation of the intended workflow.

## Why it matters for my work

Dementia makes the difference between biological evidence, a clinical syndrome and a future outcome especially clear. My imaging studies need to state which of these a label represents and whether the acquisition can support the proposed explanation.

## What I have not resolved

- How should mixed pathology be represented without forcing an artificial single-cause label?
- How can retrospective datasets distinguish biological progression from changes in diagnosis and follow-up intensity?
- What evidence is sufficient to describe a model’s prediction as clinically meaningful when its strongest reference is a biomarker surrogate?

---

Sources: Existing lecture notes; National Institute on Aging, Alzheimer’s Disease Fact Sheet and resources on dementia, Lewy body dementia and frontotemporal disorders; NICE, Dementia: assessment, management and support for people living with dementia and their carers. The hypothetical examples and research-design deductions distinguish observations, diagnoses and prognostic targets. These are study notes for research purposes and are not clinical guidance.
