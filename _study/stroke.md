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

## Core question and definition

What does each acute stroke image reveal about a vessel, brain tissue and a possible clinical action?

Stroke is acute neurological injury caused by vascular ischemia or hemorrhage. This note focuses on arterial ischemic stroke and spontaneous intracerebral hemorrhage. Other vascular disorders can require related but distinct reasoning.

Ischemic stroke results from inadequate blood supply to brain tissue. Intracerebral hemorrhage results from bleeding into brain tissue. Their initial symptoms can overlap, while their immediate treatment priorities differ.

The central imaging questions must therefore remain separate:

| Question | Example of the target |
| --- | --- |
| Is blood present? | Acute intracranial hemorrhage |
| Is a vessel obstructed? | An arterial occlusion at a specified location |
| Is tissue injured? | A visible ischemic lesion or diffusion abnormality |
| How is blood reaching tissue? | Perfusion and collateral-flow patterns |
| What clinical action is appropriate? | A decision integrating symptoms, timing, imaging and other information |
| Does a tool improve care? | More timely appropriate action with acceptable harms |

A model that detects an occluded vessel has not independently determined treatment eligibility. A model that segments a diffusion lesion has not directly measured every irreversibly injured cell. A model that processes an image quickly has not demonstrated faster treatment.

Stroke is especially useful for studying these distinctions because the patient, tissue and available evidence can all change between observations.

## Key concepts

### Vascular anatomy explains why location matters more than lesion size alone

Brain function is organised through networks supplied by particular arterial territories. Interruption of flow therefore produces deficits related to which structures are affected.

A cortical lesion can disturb language, spatial attention or vision. Injury to a compact motor pathway can produce substantial weakness despite a relatively small lesion. Brainstem and cerebellar injury can affect coordination, eye movements, balance, swallowing or consciousness.

This is why lesion volume is not a complete measure of clinical severity. A small strategically located injury can be highly disabling, while a larger lesion elsewhere may produce a different pattern of impairment.

Symptoms also help test whether an imaging finding is relevant. An old infarct may be conspicuous on CT yet fail to explain the new deficit. A subtle lesion matching the current neurological pattern may be more important.

For AI, segmentation quality should therefore be evaluated alongside localisation and clinical context. An overlap metric that rewards large lesions can conceal missed small lesions in consequential locations.

The disease label belongs to the patient and episode. The image finding belongs to a particular structure and acquisition time. They need to be linked explicitly.

### Ischemia: from loss of supply to cellular dysfunction

Brain tissue depends on a continuing supply of oxygen and metabolic substrate. When blood flow becomes inadequate, energy production falls.

Energy-dependent ion regulation becomes impaired. Cells lose normal control of ionic gradients, and water shifts into cellular compartments. Membrane dysfunction and excitatory signalling can further injure tissue.

These processes help explain several observations:

- Neurological function can fail before a large structural lesion becomes visible.
- Altered cellular water distribution can produce diffusion abnormalities.
- Increasing tissue water can later reduce CT attenuation.
- Tissue swelling can compress sulci and contribute to mass effect.

The chain is not a universal clock. The degree and duration of flow reduction, collateral circulation and other physiological conditions influence how quickly injury develops.

An arterial occlusion therefore does not imply that every downstream region is equally damaged. Some tissue may receive collateral supply, while other tissue is more severely deprived.

A single image captures one stage of this evolving process. Its interpretation depends on when it was obtained and what happened before and after it.

### Core and penumbra describe tissue states, not directly visible colours

The ischemic core refers to tissue considered severely and irreversibly injured in the relevant physiological context. The penumbra refers to threatened tissue that may remain viable if adequate perfusion is restored.

Clinical imaging attempts to estimate these states through observable signals. It does not directly inspect every cell’s future recoverability.

A perfusion map labelled “core” is therefore an inference produced by a measurement and processing method. Its colour is not histological proof.

The penumbra is also not necessarily a uniform ring surrounding a central lesion. Vascular territories and collateral routes create heterogeneous patterns.

This distinction matters when training a model. If a commercial processing output is used as the label, the model may learn to reproduce that software’s estimate. It has not automatically acquired a stronger biological reference than the original method.

Nor is later infarction a simple substitute for pretreatment core. Tissue outcome depends on whether and when reperfusion occurs, as well as subsequent events.

The reference must state whether the target is a contemporaneous imaging estimate, a later lesion or a proposed counterfactual tissue outcome.

### Hemorrhage produces injury through several mechanisms

A ruptured vessel releases blood into tissue. The hematoma can directly disrupt local structures and displace surrounding tissue.

Blood and its breakdown products also contribute to secondary injury and surrounding edema. If blood enters the ventricular system or obstructs cerebrospinal-fluid pathways, hydrocephalus may occur.

The resulting clinical state depends on location, extent, mass effect and evolution. It cannot be summarised by the presence of any bright region on CT.

Underlying causes also differ. Hypertensive small-vessel disease, vascular malformations, anticoagulant-associated bleeding and other conditions can enter the assessment.

Imaging may reveal clues to cause, but a hemorrhage detector does not independently perform the complete etiological investigation.

For a learning task, acute hematoma, chronic blood products, hemorrhagic transformation of an infarct and other intracranial bleeding patterns should not be silently merged. Their appearance, reference and consequences can differ.

Even the phrase “hemorrhage negative” needs a scope: which types of hemorrhage, on which acquisition, at what time?

### Clinical reasoning starts before image interpretation

The team establishes the neurological pattern and the timing of symptoms. When the exact onset is unknown, last-known-well time records the latest time the person was known to be at their previous baseline. It is not necessarily the moment the vessel became occluded.

The assessment also considers glucose, medication exposure, prior neurological deficits and relevant medical history. These observations can affect the differential and the interpretation of treatment risk.

A structured neurological scale supports communication and repeated assessment. Its total does not replace attention to a disabling deficit or a suspected posterior circulation event.

The clinical and imaging examinations constrain each other. A visible lesion should plausibly relate to the symptoms, while a negative early image should not erase a convincing acute neurological syndrome.

For AI, these are distinct sources of information. A model using only an image cannot truthfully claim to have considered an unknown onset time or an unrecorded anticoagulant history.

If such variables are incorporated, their availability at the decision time must be documented.

### Noncontrast CT: blood, water and the early visibility problem

Noncontrast CT is widely used in acute assessment because it can be acquired rapidly and is useful for detecting acute hemorrhage.

Acute clotted blood often appears more attenuating than surrounding brain. Ischemic tissue, however, can initially look close to normal.

As ischemic injury develops, increased tissue water can reduce attenuation and blur normal anatomical contrast. Early findings may include loss of grey-white differentiation, obscuration of the insular ribbon and sulcal effacement.

The reason these signs are subtle is that the reader is often detecting a small change in contrast or geometry rather than an obvious new mass.

A hyperdense artery can suggest intraluminal thrombus. It is a sign requiring interpretation, not a complete vascular study. Calcification, technical factors and other sources of density can complicate the appearance.

The crucial negative statement is: **an initially unremarkable CT does not exclude ischemic stroke.**

For a model, a patient-level ischemic stroke label does not guarantee that the baseline CT contains a confidently visible lesion. Visibility should be assessed separately from the later diagnosis.

### CT angiography: contrast shows the vessel lumen, not the entire tissue outcome

CT angiography uses intravascular contrast to depict arterial anatomy and contrast passage.

An abrupt termination or filling defect can support an occlusion diagnosis. The reader also considers the vessel’s course, downstream filling, collateral pathways and the adequacy of the acquisition.

Several technical conditions can complicate interpretation. Poor bolus timing, motion, incomplete coverage or slow flow can make a vessel segment difficult to assess. An apparent absence of contrast is not always equivalent to a fixed anatomical obstruction.

Even a well-established occlusion leaves further questions. Which tissue is affected? How severe are the symptoms? Has the vessel reopened between examinations? What additional clinical information determines an appropriate action?

A model should therefore specify whether it detects any occlusion, a particular vessel group or an occlusion relevant to a defined triage pathway.

An evaluation that includes only conspicuous proximal occlusions cannot establish performance for all arterial locations.

Later angiography can provide valuable reference information, but it is obtained selectively and at a later time. A difference between scans may represent a real vascular change rather than an error in the earlier image.

### Diffusion MRI: why bright signal needs interpretation

Diffusion-weighted imaging is sensitive to the movement of water molecules. Acute ischemic cellular dysfunction commonly produces restricted diffusion, seen as increased diffusion-weighted signal with reduced apparent diffusion coefficient.

The apparent diffusion coefficient, or ADC, helps distinguish true diffusion restriction from high signal contributed by other image properties, including T2 effects.

This is a measurement of water behaviour. It is not a direct stain for dead neurons.

Diffusion abnormalities can also occur in conditions other than arterial infarction. Distribution, accompanying sequences and clinical context remain important.

Small or very early ischemic lesions can be difficult to detect, particularly when anatomical location and acquisition limitations reduce conspicuity. A negative early diffusion study is therefore not an unconditional exclusion of ischemic stroke.

For AI, a lesion label needs the sequence and time attached. A mask drawn on diffusion imaging cannot be transferred to another sequence without considering registration, distortion and differences in visibility.

A model may predict a lesion from a less sensitive modality, but that is a cross-modal inference. It should not be described as though the target signal were directly present with equal clarity in every input.

### Other MRI sequences supply complementary evidence

FLAIR suppresses cerebrospinal-fluid signal and helps display abnormalities in brain tissue. Its appearance can contribute information about lesion evolution, but it is not an exact clock applicable to every patient.

Susceptibility-sensitive sequences can demonstrate blood products and related effects. They answer a different question from diffusion imaging.

Anatomical sequences help assess location, pre-existing lesions, structural alternatives and the context of an abnormality.

The combination matters because a single bright or dark region is rarely self-interpreting. The reader asks which physical contrast produced it and whether the other sequences support the same explanation.

For a dataset, “MRI-positive stroke” should identify how positivity was established. A report-based label may summarise several sequences and clinical information. An individual slice may contain only part of that evidence.

Sequence availability can also encode the care pathway. Patients selected for an extensive MRI investigation may differ from patients assessed only with emergency CT. A model can exploit that selection unless the intended population is clearly defined.

### Perfusion maps are estimates built from a measurement model

Perfusion imaging tracks the passage of a signal through tissue, commonly using contrast dynamics. Processing methods estimate quantities related to flow, blood volume and transit or arrival behaviour.

The estimate depends on the recorded time course, arterial input, acquisition coverage, movement correction and the assumptions of the processing method.

Delayed arrival can reflect collateral pathways as well as critically inadequate tissue flow. Technical errors can also distort the curves.

A colourful map can therefore look precise while remaining uncertain about biological tissue state. Thresholding the map creates a categorical label from a continuous, model-dependent estimate.

For machine learning, the distinction between an imaging-derived label and an independently adjudicated clinical target is essential. Reproducing a thresholded map may be useful for automation, but it validates agreement with that pipeline.

It does not independently demonstrate irreversible injury, salvageability or benefit from a particular intervention.

The appropriate evaluation asks whether the method remains reliable across acquisition conditions and whether its output supports the intended clinical decision.

### The modality-to-question map

| Modality or observation | Principal question | Important non-entailment |
| --- | --- | --- |
| Neurological examination | What function changed, and where might the lesion be? | Symptoms alone do not reliably distinguish ischemia from hemorrhage |
| Noncontrast CT | Is there hemorrhage or visible structural injury? | A negative early CT does not exclude ischemia |
| CT or MR angiography | What vessels are patent, narrowed or occluded? | Occlusion alone does not determine tissue viability or treatment eligibility |
| Diffusion MRI and ADC | Is there a pattern of altered water diffusion? | Restriction is not uniquely arterial stroke or direct proof of irreversible injury |
| Perfusion imaging | How does blood or tracer passage through tissue appear? | A processed map is not histological ground truth |
| Follow-up imaging | What tissue abnormality is visible later? | Later injury is not an unchanged copy of the pretreatment state |

This map prevents a broad “stroke detection” label from concealing several incompatible tasks.

### Differential diagnosis and mismatched findings

Important alternatives include seizure-related deficits, migraine, hypoglycemia, functional neurological symptoms and other structural or systemic conditions.

Their consideration depends on history, examination and investigations. A negative early CT does not independently establish a mimic.

Seizure can produce focal neurological deficits and imaging changes. Migraine can produce neurological symptoms with a different temporal pattern. Glucose disturbance can produce acute dysfunction without the same vascular mechanism.

Old stroke deficits may also become more apparent during systemic stress. The presence of an old lesion does not automatically explain a newly reported event in the same way as a new infarct.

The study lesson is that imaging findings must be matched to the current episode. A model that recognises any prior infarction may achieve apparent “stroke” accuracy while missing the task of identifying an acute event.

Reference construction should distinguish acute injury, chronic injury, uncertain findings and nonvascular alternatives.

### A different reference standard is needed for each target

| Target | Possible reference | Main qualification |
| --- | --- | --- |
| Acute hemorrhage | Expert interpretation of appropriate imaging, with additional evidence where needed | Blood type, location and acquisition context must be specified |
| Arterial occlusion | Adjudicated vascular imaging or angiography | Vessel status can change between examinations |
| Visible ischemic lesion | Expert annotation on specified sequences | Visibility and boundaries depend on modality and time |
| Final infarct | Follow-up imaging with defined timing | Treatment, edema and lesion evolution affect the result |
| Clinical ischemic stroke | Integrated clinical assessment and investigations | A visible lesion may be absent on an early study |
| Treatment eligibility | A defined clinical decision framework using all required information | An image alone may omit essential variables |
| Functional outcome | Follow-up assessment of specified function | Baseline disability, care and missing follow-up matter |

A report extracted from the record may be a practical reference, but its information content must be understood. It may describe a preliminary interpretation, incorporate later information or summarise several modalities.

Consensus review improves reproducibility without making uncertainty disappear. Borderline findings, incomplete studies and disagreement should remain visible in the data.

### Treatment changes the meaning of the later label

Consider a baseline perfusion abnormality followed by successful restoration of blood flow and a small later infarct.

It would be incorrect to conclude automatically that the baseline abnormality was false. Some threatened tissue may have survived because the patient was treated.

The reverse problem also occurs. A later infarct may extend beyond an early visible lesion because the vascular problem persisted or new events occurred.

The later image is therefore an outcome under the care actually received. It is not direct observation of what would have happened without treatment.

This is where causal inference enters the imaging task. Predicting observed infarct or disability differs from predicting treatment benefit or untreated outcome.

A supervised label derived from a clinical decision has a similar limitation. It can encode clinician judgement, local resources and access to treatment. Learning that decision is not automatically learning the causal effect of the treatment.

These distinctions should be made before choosing a model architecture.

### Error costs are tied to the action

Missing hemorrhage can delay the appropriate pathway and may contribute to unsafe interpretation of an ischemic treatment question. Falsely labelling hemorrhage can also delay or divert care.

Missing an arterial occlusion can delay specialist review or transfer. A false alert can consume attention, trigger unnecessary escalation and interfere with prioritisation.

Overestimating severely injured tissue can support an overly pessimistic interpretation. Underestimating it can also distort risk assessment. Neither error is captured fully by a generic image-level accuracy score.

The operating point should therefore be defined for the system’s role. A triage prompt, a measurement aid and an autonomous eligibility decision have different consequences.

Performance should include failed acquisitions and cases in which the system cannot produce a result. Excluding motion-degraded or clinically difficult studies can conceal the very failures likely to occur in emergency practice.

### Worked reasoning examples

**Acute focal deficit with an unremarkable initial CT.** The scan may adequately exclude conspicuous hemorrhage while providing limited evidence about early ischemia. A later clinical stroke diagnosis does not mean that a clear infarct was necessarily visible in the original image.

**A vessel appears occluded on one study and patent on another.** Before declaring one interpretation wrong, establish the sequence of acquisitions and intervening treatment. The vessel may genuinely have reopened. The reference must preserve time.

**A small lesion receives a poor segmentation score.** The numerical overlap may be low because the lesion is small, yet its location may make the miss clinically consequential. Conversely, an excellent average score dominated by large lesions can conceal that failure.

**A baseline tissue-at-risk estimate exceeds the later infarct.** Treatment and natural evolution lie between the observations. The discrepancy cannot be interpreted as pure measurement error without considering those processes.

These are hypothetical examples of target and reference reasoning, not estimates of treatment effect.

### Evaluating a stroke AI system as part of a workflow

The relevant timeline includes acquisition, data availability, processing, notification, review and action.

A reduction in computation time affects only one segment. If a result arrives in an unattended queue or duplicates information already acted upon, technical speed may have little clinical value.

Evaluation should therefore distinguish:

- Time until a usable result exists.
- Time until an appropriate clinician reviews it.
- Whether the result changes prioritisation or action.
- Missed cases and false alerts.
- Transfer or treatment delays.
- Safety and functional outcomes.

A comparison of workflows must also address differences in staffing, patient mix and resources. An association between tool availability and better outcomes is not automatically its causal effect.

Patient-level data separation remains necessary, with particular care when multiple series, reconstructions and follow-up studies belong to the same episode.

The model should be evaluated on the acquisitions available at its intended decision point, not on a retrospectively enriched collection.

### Revision checklist

| Question | What I should be able to explain |
| --- | --- |
| Why do location and volume differ in importance? | Compact or specialised networks can be damaged by small lesions |
| Why can symptoms precede CT changes? | Dysfunction can occur before conspicuous structural alteration |
| Why does ischemia alter diffusion? | Energy failure changes cellular ion and water regulation |
| Why inspect ADC with diffusion-weighted signal? | Bright signal can have contributions other than restriction |
| What does CTA observe? | Contrast passage and vessel anatomy |
| Why is a perfusion label model-dependent? | Acquisition and processing turn time courses into estimates |
| Why is a negative early image limited? | Visibility depends on time, location and technique |
| Why can later angiography disagree legitimately? | Vessel status may have changed |
| Why is final infarct not pretreatment core truth? | Care and lesion evolution intervene |
| Why is eligibility not an image-only label? | Timing, examination and other clinical variables matter |
| Why can average overlap mislead? | Large lesions dominate while small consequential lesions are missed |
| Why is speed not sufficient utility evidence? | The whole route to appropriate action determines benefit |

### Connecting the clinical reasoning to the ontology

Vascular injury provides a mechanism-to-finding example: ischemic cellular dysfunction can manifest as diffusion restriction or evolving loss of tissue contrast, depending on the acquisition and time.

`Acute stroke triage` `setsRequirementsFor` `Evaluation metrics` and `Comparative workflow evaluation`. A relevant metric must account for missed urgent cases and the timing of usable action.

`Clinical assessability` limits `Clinical evidence reliance`: a claim that a model used visible early ischemic change requires evidence that the change was assessable in its actual input.

Treatment-dependent follow-up also connects to `Causal inference`. Observed outcome, untreated outcome and treatment benefit are separate targets.

## Why it matters for my work

Stroke shows that reference validity is inseparable from time and care. I need to identify what was observable at the decision point, what changed before the reference was obtained, and whether a model’s technical success advances the intended clinical action.

## What I have not resolved

- How should an audit distinguish an image-invisible clinical event from a missed subtle finding?
- What reference best supports tissue-state prediction when treatment changes the later image?
- How can workflow evaluation separate a model’s contribution from differences in staffing, transfer systems and local resources?

---

Sources: Existing lecture notes; National Institute of Neurological Disorders and Stroke resources on stroke; American Society of Neuroradiology, American College of Radiology and Society of NeuroInterventional Surgery imaging recommendations; RadiologyInfo, Stroke; established neuroradiological descriptions of early CT findings, diffusion imaging and perfusion assessment. The hypothetical examples address research interpretation rather than treatment eligibility. These are study notes for research purposes and are not clinical guidance.
