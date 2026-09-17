---
layout: study_note
title: "Parkinson's Disease"
description: "Movement disorder assessment, rating scales as noisy ground truth, and longitudinal measurement."
og_image: "https://sehyeony0518.github.io/assets/img/og/parkinsons-disease.png"
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "neurology"
category_title: "Neurology & Sleep Medicine"
subgroup: "Neurodegeneration"
order: 5
source: "Lecture"
written: true
updated: "2026-09-08"
papers:
  - "2026-06-13-counterfactual-shortcut-utilization"
---

## Core question and definition

What evidence allows a clinician to infer Parkinson’s disease from a person’s movements, and which parts of that inference could a camera or scan actually support?

Parkinson’s disease is a progressive neurological disease involving degeneration of dopaminergic neurons and dysfunction of wider neural systems. Its clinical expression includes motor and nonmotor problems. The diagnosis ordinarily rests on a pattern assembled from history, examination, treatment response and evolution over time.

**Parkinsonism is a motor syndrome; Parkinson’s disease is one cause of that syndrome.** In the Movement Disorder Society framework, motor parkinsonism requires bradykinesia together with rest tremor or rigidity. Establishing this combination starts the diagnostic reasoning. It does not finish it.

For medical AI, the distinction immediately separates several targets:

| Target | What the output claims |
| --- | --- |
| Movement measurement | A specified movement had a particular speed, amplitude, rhythm or trajectory |
| Motor-sign assessment | The observed task supports a sign such as bradykinesia or tremor |
| Syndrome recognition | The examination supports parkinsonism |
| Disease diagnosis | Parkinson’s disease is the most appropriate explanation of the syndrome |
| Severity assessment | A specified aspect of impairment or daily burden has a particular level |
| Prognosis | A defined future outcome is likely under specified conditions |

A model can succeed at one target without establishing the others. Measuring slow finger movement does not identify its cause. Recognizing parkinsonism does not distinguish every degenerative syndrome. Predicting a clinical rating does not mean that every component of that rating was observed.

The central study question is therefore: **what is the chain from neural dysfunction to observable movement, and where does additional clinical information enter?**

## Key concepts

### Basal ganglia dysfunction: why movement becomes small and difficult to sustain

The substantia nigra contains neurons that supply dopamine to the striatum. The striatum participates in circuits linking cortex, basal ganglia, thalamus and brainstem systems involved in movement.

These circuits help select, scale and organize actions. They do not simply send a command directly to a muscle. A person can retain substantial muscle strength while having difficulty initiating an action, producing an adequate movement amplitude or maintaining a repetitive sequence.

A useful first approximation is that basal ganglia output regulates inhibition of downstream motor pathways. Dopamine modulates the balance of activity through parallel pathways. Loss of normal dopaminergic input disrupts that regulation, making the selection and scaling of voluntary movement less effective.

This helps explain why Parkinsonian slowness differs from weakness. A weak muscle may fail to generate force. A person with bradykinesia may generate force yet perform a sequence slowly, with progressively smaller excursions or interruptions.

The circuit account is an organizing model, not a complete derivation of every symptom. Tremor, postural control and nonmotor dysfunction involve additional network properties. A single scalar measure of “dopamine loss” cannot explain the entire clinical examination.

For imaging research, this also explains an important mismatch of scales. Neural dysfunction can substantially alter movement without creating an obvious abnormality on routine structural MRI. Functional disturbance and macroscopic tissue appearance are different observations.

### Bradykinesia: a sequence contains information that a still image cannot

Bradykinesia is assessed through the performance of movement, particularly repetitive tasks. The clinician considers slowness together with decrement in amplitude or speed, or progressive hesitations and interruptions.

Finger tapping illustrates the reasoning. The clinician does not merely count how many times the fingers meet. They observe whether the fingers open sufficiently, whether the movement becomes smaller, whether rhythm deteriorates and whether the patient pauses.

Different failures can produce a similar average tapping rate:

- A person may move slowly but maintain a regular, full-amplitude sequence.
- Another may begin briskly and then develop progressively smaller movements.
- Another may interrupt the task because of pain.
- Another may misunderstand the instruction or have difficulty maintaining attention.

These are not interchangeable findings. A model trained only on the average rate can erase the pattern that made the examination informative.

A still image cannot establish decrement because decrement is a change across a sequence. Even a video may be insufficient if it begins after the task has already deteriorated, omits the relevant joint or lacks enough spatial detail to measure the movement.

This is a concrete example of clinical assessability: the label may be meaningful at the examination level while being unsupported by a particular extracted frame.

### Rigidity and tremor require different measurements

**Rigidity** is increased resistance encountered when an examiner moves a relaxed limb passively. Its defining evidence includes a mechanical interaction between examiner and patient.

An ordinary video records displacement and appearance. It does not directly record the force needed to produce that displacement. Seeing an examiner bend an elbow therefore does not, by itself, measure rigidity.

A model might predict the examiner’s rigidity rating from correlated visible signs. That could be a useful surrogate if independently validated, but it remains a prediction of an unmeasured component. The distinction matters when the model is described as an automated examination.

**Rest tremor** is an involuntary rhythmic movement that is particularly evident when the affected body part is supported and not performing a voluntary action. It may change with posture, movement, stress and attention. Its absence during a short recording does not establish its absence throughout the day.

Tremor also does not uniquely identify Parkinson’s disease. Essential tremor, medication effects and other disorders can produce shaking, sometimes with overlapping appearances.

The clinical question is consequently richer than “is there oscillation?” It includes when the movement occurs, which body parts are involved, whether other motor signs coexist and how the pattern has evolved.

Video and wearable sensors can characterize oscillation, but recording conditions still matter. A poorly supported hand, camera movement or an unstable sensor attachment can change the observed signal.

### Gait, automatic movement and the limits of a short examination

Reduced arm swing, short steps, difficulty turning and freezing episodes can contribute to the motor picture. Reduced facial expression and changes in speech may also be observable.

These findings follow from dysfunction of movement scaling, automaticity and coordinated motor control. They are not all direct measures of the same process, and they do not necessarily respond equally to treatment.

A person may walk relatively well along an unobstructed corridor but struggle when turning, passing through a doorway or dividing attention between tasks. An examination samples behaviour under particular demands.

This creates a difference between **capacity under instruction** and **performance in everyday life**. A supervised clinic task measures what happened during that task. It does not automatically establish how often freezing occurs at home or how safely the person navigates an unfamiliar environment.

The same distinction applies to negative findings. A recording with no fall, no freezing and no tremor is evidence about the recorded interval. It is not a complete account of the patient’s burden.

For a model, the task protocol is part of the input definition. “Walking video” is too vague unless the route, turns, instructions, assistive devices and visibility are specified.

### Nonmotor disease explains why a motor score is incomplete

Parkinson’s disease affects neural systems beyond the nigrostriatal motor pathway. Sleep disturbance, constipation, autonomic symptoms, mood changes, pain and cognitive difficulties may contribute substantially to disability.

These symptoms are not merely consequences of visibly impaired walking. Some can precede a clear motor syndrome, while others develop during the subsequent course. Their timing and severity vary.

A camera may show facial movement or posture while missing fatigue, urinary symptoms, dream-enactment behaviour, cognitive fluctuation or the effect of symptoms on daily activities.

Nor is every nonmotor symptom specific. Constipation, depression and disturbed sleep have many possible causes. Their presence can contribute to a clinical pattern without functioning as a stand-alone diagnostic test.

For supervised learning, a patient-level disease label may therefore incorporate evidence absent from the model’s modality. That is not automatically an invalid task: prediction from partial information is common. It becomes misleading when predictive agreement is presented as direct observation of the full disease process.

The appropriate claim might be that visible motor behaviour helps estimate a clinical diagnosis. It should not silently become a claim that video has measured all clinically relevant manifestations.

### Disease progression and examination state are different variables

Motor performance depends on more than the underlying disease.

Dopaminergic treatment can improve some motor manifestations. Performance can also vary with fatigue, pain, anxiety, sleep, attention and the demands of the task. Treatment-related involuntary movements can further complicate interpretation.

Consequently, greater movement is not always improvement, and a better examination score does not demonstrate reversal of neurodegeneration.

A useful conceptual measurement model is:

$$
\text{observed performance}
=
f(\text{disease},\text{treatment state},\text{task},\text{context},\text{measurement}).
$$

This is a statement about dependencies, not an assumption that their effects are additive or separable.

Suppose the same person is recorded before and after medication. A change may represent treatment response. Comparing a later treated examination with an earlier untreated examination does not isolate disease progression.

Likewise, a person recorded repeatedly in different rooms may appear to change because the camera angle or movement instructions changed. Longitudinal research needs comparable conditions, or an explicit model of their differences.

The target must state whether it concerns present performance, response to treatment, daily fluctuations or longer-term progression. A dataset mixing these targets under one “severity” label leaves the model’s meaning unclear.

### How the clinical diagnosis is assembled

The clinician first asks whether the motor findings support parkinsonism. They then ask which cause best explains the pattern.

The history establishes onset, progression, initial asymmetry, medication exposure, associated symptoms and functional consequences. The examination assesses the motor syndrome and searches for findings pointing elsewhere.

A sustained response to appropriate dopaminergic treatment can support the diagnosis, but treatment response must be interpreted in context. The recorded dose history, adherence, tolerability and symptoms being assessed affect what an apparent response means.

The clinician also looks for atypical features. Prominent early balance problems, particular eye-movement abnormalities, marked autonomic dysfunction or additional cortical signs may change the differential.

These features are not a checklist that can be interpreted independently of timing. A manifestation that is plausible later in established Parkinson’s disease may be more concerning when it dominates the initial presentation.

Diagnostic confidence can therefore change over follow-up. A diagnosis revised after additional evidence is not necessarily evidence that the earlier clinician ignored an obvious sign. The discriminating pattern may not yet have been present.

A research label should preserve that uncertainty rather than retrospectively making every early examination appear diagnostically obvious.

### Differential diagnosis: similar movement, different explanation

| Alternative | Why it can resemble Parkinson’s disease | Evidence that helps discriminate |
| --- | --- | --- |
| Essential tremor | Visible rhythmic movement can dominate the presentation | Relationship to action and posture, distribution, and whether bradykinesia or rigidity is present |
| Drug-induced parkinsonism | Interference with dopaminergic function can produce a Parkinsonian syndrome | Medication exposure and temporal relationship; underlying degeneration may also coexist |
| Vascular parkinsonism | Vascular injury can affect movement pathways and gait | Clinical course, distribution of deficits and relevant vascular lesions; incidental MRI changes alone are insufficient |
| Progressive supranuclear palsy | Slowness, stiffness and gait impairment overlap | Characteristic eye-movement problems, early falls and the broader clinical pattern |
| Multiple system atrophy | Parkinsonism can accompany degeneration of other systems | Prominent autonomic dysfunction, cerebellar findings and progression |
| Corticobasal syndrome | Asymmetric impaired movement can resemble Parkinsonism | Apraxia, cortical sensory abnormalities and other cortical signs |
| Musculoskeletal or peripheral neurological disease | Pain, restricted joints or weakness can slow movement | Examination of strength, sensation, joint mechanics and the reason the task stops |

The table describes discriminating evidence, not absolute rules. Asymmetry does not prove Parkinson’s disease. A medication exposure does not prove that all symptoms are drug-induced. Vascular changes on MRI do not establish that they caused the movement disorder.

For AI, the important test population contains these alternatives. Distinguishing established Parkinson’s disease from unusually healthy volunteers answers a much easier question than distinguishing causes of slowness in a referral clinic.

### What each modality can and cannot establish

| Observation source | What it can support | What remains outside the observation |
| --- | --- | --- |
| Standardized video | Visible movement amplitude, rhythm, posture, gait and some examination signs | Passive resistance, complete nonmotor burden and the cause of every observed abnormality |
| Wearable motion sensors | Movement trajectories and fluctuations during recorded activities | Clinical interpretation without task context; unrecorded symptoms and events |
| Structural MRI | Vascular lesions, masses, structural alternatives and some patterns relevant to the differential | Independent confirmation of routine Parkinson’s disease |
| Dopamine-transporter SPECT | Evidence concerning presynaptic striatal dopaminergic function | Unique distinction of Parkinson’s disease from all degenerative Parkinsonian syndromes |
| Clinical history and examination | Integration of motor, nonmotor, temporal and treatment evidence | Direct pathological confirmation in the living patient |
| Neuropathological examination | Tissue-level evidence about degeneration and associated pathology | A direct record of every earlier examination state or daily functional experience |

Structural MRI is particularly easy to overinterpret in an AI paper. A normal routine scan does not erase a clinically supported syndrome. Conversely, a classifier finding a statistical difference between diagnostic groups does not establish a visible, disease-specific MRI sign.

Dopamine-transporter imaging answers a narrower biological question. Reduced uptake can support a presynaptic dopaminergic deficit, but such a deficit is shared by several degenerative disorders.

A model trained to reproduce an abnormal scan classification has therefore learned a different target from a model trained to distinguish Parkinson’s disease from those alternatives.

### A rating scale is an organized observation, not a disease assay

The MDS-UPDRS includes distinct domains:

| Domain | Main source of information |
| --- | --- |
| Nonmotor experiences of daily living | Patient and informant report, with clinical assessment |
| Motor experiences of daily living | Reported effects on ordinary activities |
| Motor examination | Performance and signs during a structured examination |
| Motor complications | Treatment-related fluctuations and complications |

A paper reporting an “UPDRS score” must identify the instrument and part used. A motor examination score and a patient’s report of daily difficulty are not interchangeable outcomes.

The items are ordinal clinical judgements. Moving between adjacent categories does not automatically represent an equal physical increment across the whole scale. A numerical regression loss does not change that measurement property.

Reader disagreement can arise from different observations, interpretation of instructions, borderline performance and unavailable information. Replacing all ratings with a single consensus value can conceal this structure.

For model development, it is useful to preserve item-level ratings, reader identity and the conditions under which ratings were made. A video-only reader and an in-person examiner may have access to different evidence.

A missing rigidity assessment must not silently become “no rigidity.” Nor should a whole examination score be attached to every isolated clip as though each clip independently displayed the entire examination.

### Where a Parkinson’s disease label comes from

| Label source | What it establishes most directly | Main limitation |
| --- | --- | --- |
| Specialist clinical diagnosis | An expert interpretation of the available clinical pattern | May change as the disease evolves |
| Documented diagnostic criteria | A reproducible framework for classifying the clinical evidence | Criteria still depend on the quality and completeness of observations |
| Examination-item rating | The severity of a specified sign under recorded conditions | Reader variation and treatment-state dependence |
| Patient-reported outcome | Experienced burden during the report’s reference period | Recall, interpretation and differences from clinic performance |
| Dopaminergic imaging result | A classification of the measured imaging pattern | Does not uniquely identify the disease causing the deficit |
| Registry or billing code | A recorded diagnostic designation | May reflect provisional diagnosis, coding practice or copied history |
| Neuropathology | Tissue-level evidence available after death | Highly selected availability and a different observation time |

There is no single label source that solves all tasks.

If the intended target is current clinical diagnosis, a carefully documented specialist assessment may be appropriate. If the target is a motor item, a disease code is too coarse. If the target is progression, repeated disease codes do not measure change.

A label obtained later can help adjudicate an earlier uncertain diagnosis. However, the dataset must distinguish a retrospective disease classification from what was observable at the earlier visit.

Otherwise, a model may be penalized for failing to recover information that had not yet emerged.

### Consequences of error determine the operating point

A false negative in a referral-support system may delay specialist assessment or recognition of functional problems. A false positive can cause anxiety, inappropriate disease attribution and unnecessary investigation.

Those consequences differ from the errors of a home-monitoring system. Underestimating motor difficulty could conceal deterioration; overestimating it could prompt unnecessary review or distort interpretation of treatment response.

A model that mistakes treatment-related involuntary movement for improved mobility may produce a particularly misleading longitudinal signal.

The action following the output must therefore be specified. A prompt for human review is not equivalent to a diagnosis, and a measurement summary is not a treatment recommendation.

Evaluation should include whether errors cluster in people with pain, atypical Parkinsonism, cognitive difficulty, assistive devices or incomplete recordings. A satisfactory average error can conceal a clinically important failure in one of these groups.

Abstention also has a cost and a purpose. Declining to score an unassessable task can be appropriate, but a system that disproportionately rejects the most impaired patients cannot claim reliable monitoring of the full intended population.

### Worked reasoning examples

**A slow tapping video with a positive disease label.** The patient has a specialist diagnosis, but the clip shows a painful hand with a limited view of finger excursion. The diagnosis may be correct while the clip is a poor reference for bradykinesia. The useful annotation separates disease status, task quality, visible performance and the reason for stopping.

**An abnormal dopaminergic scan with atypical clinical findings.** The scan supports dopaminergic deficit. If the clinical course includes findings pointing to another degenerative syndrome, the scan does not override them. A model reproducing scan abnormality has not demonstrated differential diagnosis of Parkinson’s disease.

**A later recording appears substantially better.** The later session occurs in a different treatment state and uses clearer instructions. The observed improvement may be real performance improvement, but it cannot be attributed entirely to a change in underlying disease. The appropriate comparison depends on whether the study targets treatment response or progression.

These examples are hypothetical reasoning exercises. They contain no measured treatment effects or diagnostic performance estimates.

### Designing a defensible learning task

A study specification should state:

- The clinical question and intended user.
- The body part, task and recording protocol.
- Which findings are directly observable.
- The label source and its observation time.
- Medication and relevant treatment state.
- How incomplete or unassessable examinations are represented.
- Whether evaluation concerns new patients, new visits or change within a patient.
- The action, if any, triggered by the output.

Patient separation is essential when recordings repeat. Otherwise, recognition of identity, voice, clothing or environment can masquerade as generalization to new people.

Temporal evaluation also needs care. A model trained on later visits must not indirectly reveal the future when evaluated on an earlier visit from the same patient.

Useful audits compare behaviour across recording setups and clinically relevant alternatives. Removing every contextual feature is not automatically correct: an assistive device may be relevant to functional assessment. The audit must ask whether the feature is legitimate for the specified claim.

### Revision checklist

| Question | What I should be able to explain |
| --- | --- |
| Parkinsonism or Parkinson’s disease? | A motor syndrome and its cause are different targets |
| Why can movement be slow without weakness? | Basal ganglia dysfunction affects movement selection and scaling |
| Why is a tapping sequence needed? | Decrement and interruptions are temporal findings |
| Why cannot ordinary video directly measure rigidity? | Resistance requires information about applied force |
| Why is absent tremor weak exclusion evidence? | Tremor varies and is not present in every patient |
| Why can a normal MRI coexist with disease? | Routine structural imaging does not directly measure dopaminergic dysfunction |
| What does abnormal transporter imaging establish? | Evidence of dopaminergic deficit, with limited disease specificity |
| What does a rating score measure? | A defined domain, reader judgement and observation condition |
| Why is a missing item not a negative item? | The finding may never have been assessed |
| Why is improved movement not proof of slowed degeneration? | Treatment and context alter performance |
| Which errors matter? | Those linked to the actual referral, monitoring or decision task |
| What is the independent evaluation unit? | Usually the patient, with visits and clips nested within that patient |

### Connecting the clinical reasoning to the ontology

The mechanism-to-finding relationship is conditional: altered motor circuitry can manifest as bradykinesia, but observed slowness has competing explanations.

`Neurological disease` therefore `setsRequirementsFor` `Clinical feature annotation`: an annotation protocol must distinguish disease identity from a visible motor event and from an unmeasured examination component.

`Clinical assessability` limits `Clinical evidence reliance`. A model cannot establish reliance on measured passive resistance when the recording contains no measurement of that resistance. It may estimate rigidity indirectly, but the evidential claim must say so.

Finally, `Clinical validity` does not establish `Clinical utility`. Agreement with specialist labels still leaves the question of whether using the system improves monitoring, referral or care.

## Why it matters for my work

This note makes the difference between predicting a label and measuring its supporting evidence concrete. In my imaging work, I need the same discipline: identify the finding, establish that the acquisition contains it, and distinguish its measurement from a diagnosis assembled from wider information.

## What I have not resolved

- How should disagreement between video ratings and in-person examination be represented without treating either as infallible?
- Which longitudinal changes remain interpretable when treatment state and recording conditions cannot be standardized?
- How can an audit distinguish useful indirect prediction from an unjustified claim of direct clinical measurement?

---

Sources: Existing lecture notes; National Institute of Neurological Disorders and Stroke, Parkinson’s Disease and resources on atypical Parkinsonian disorders; Movement Disorder Society, clinical diagnostic criteria for Parkinson’s disease and MDS-UPDRS documentation; NICE, Parkinson’s disease in adults. The hypothetical examples and AI study-design deductions are explanatory applications. These are study notes for research purposes and are not clinical guidance.
