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

Critical care supports patients with life-threatening organ dysfunction while clinicians identify its cause and assess its reversibility. The measurements describe a patient under active treatment. Their meaning depends on the support being delivered, the measurement process, and the preceding trajectory.

## Core question and definition

A critical-care model may predict physiological deterioration, a treatment action, a syndrome, or an outcome. These are different targets.

Low blood pressure is an observation. Shock is a clinical syndrome involving inadequate perfusion and cellular oxygen availability or use relative to need. Vasopressor initiation is an action. A shock diagnosis code is a documented classification. Death is an outcome influenced by illness, treatment, and other circumstances.

A model trained on one of these labels should not silently claim another.

The central interpretive problem is dynamic: disease changes physiology, clinicians respond, treatment changes subsequent physiology, and those changes influence further observation and action. A time series that removes the treatment context can misrepresent what the patient is experiencing.

## Key concepts

### Oxygen delivery explains why one normal measurement is insufficient

Systemic oxygen delivery depends on blood flow and the oxygen carried in that blood.

A useful physiological identity is

$$
D_{O_2}
=
Q\,C_{aO_2},
$$

where:

- $$D_{O_2}$$ is oxygen delivered per unit time.
- $$Q$$ is cardiac output.
- $$C_{aO_2}$$ is arterial oxygen content.

The units explain the multiplication: blood volume per time multiplied by oxygen per blood volume gives oxygen per time.

Arterial oxygen content depends mainly on hemoglobin and its oxygen saturation. A normal saturation does not establish adequate oxygen delivery if hemoglobin or blood flow is low.

Cardiac output can be decomposed as

$$
Q
=
\text{heart rate}\times\text{stroke volume}.
$$

A compensatory rise in heart rate does not establish adequate flow if the volume ejected with each beat is falling.

Likewise, pressure and flow are different quantities. In a simplified mean-flow description,

$$
\text{mean arterial pressure}
-
\text{central venous pressure}
=
Q\times\text{systemic vascular resistance}.
$$

Different combinations of flow and resistance can produce similar pressures. Raising resistance can improve a pressure measurement without proving that every tissue has adequate perfusion.

These relationships explain why clinicians combine pressure, perfusion findings, gas exchange, hemoglobin, organ function, and the response to support. No single monitor channel measures the entire physiological state.

### Shock is a family of mechanisms

| Mechanism | Physiological problem | Findings that can follow | Why interpretation remains contextual |
|---|---|---|---|
| Hypovolemic | Insufficient effective circulating volume reduces filling and stroke volume | Reduced flow, compensatory tachycardia and vasoconstriction, evidence of blood or fluid loss | Pressure can initially be maintained; the source and type of loss matter |
| Cardiogenic | The heart cannot provide adequate forward flow | Congestion, impaired ventricular function, poor perfusion | Different ventricular or valvular problems can produce different patterns |
| Distributive | Abnormal vascular tone and distribution of flow, sometimes with capillary leak | Low vascular resistance, altered peripheral perfusion, variable cardiac output | Preserved or increased total flow does not ensure effective tissue oxygen use |
| Obstructive | A mechanical impediment limits filling or forward flow | Features of impaired filling or outflow, sometimes right-heart strain | Pulmonary vascular obstruction, pericardial constraint, and intrathoracic pressure problems require different explanations |

These mechanisms can coexist. Infection can impair myocardial function as well as vascular tone. Hemorrhage can occur in a person with poor cardiac reserve. Positive-pressure ventilation can alter venous return and ventricular loading.

A model that recognizes hypotension has detected a shared downstream feature. It has not necessarily distinguished the causes that determine the appropriate response.

The stage also matters. Compensatory responses can preserve some measurements before overt collapse. Conversely, organ injury can persist after a pressure or oxygenation measurement improves.

### Why organ dysfunction produces particular observations

Reduced effective perfusion and inflammatory injury can affect several organs, but their observable consequences occur on different time scales.

**Kidney dysfunction.** Reduced urine output can accompany impaired perfusion or kidney injury, but also obstruction and other processes. Creatinine is an indirect, delayed indicator influenced by production, distribution, and clearance. Fluid administration can change its measured concentration. A apparently reassuring value does not always establish preserved kidney function at that moment.

**Brain dysfunction.** Altered attention, consciousness, or behavior can reflect cerebral dysfunction, metabolic disturbance, medication, or a combination. Sedation changes the examination itself. A neurological label requires distinguishing illness-related impairment from the intended effects of treatment.

**Respiratory dysfunction.** Impaired gas exchange can follow alveolar filling, collapse, edema, infection, or pulmonary vascular disease. Oxygen saturation does not directly measure carbon dioxide clearance. An acceptable saturation while receiving substantial respiratory support is not equivalent to the same saturation without support.

**Circulatory dysfunction.** Cold extremities, delayed peripheral perfusion, altered mental state, and reduced urine output can support concern about inadequate perfusion, but none is specific to one shock mechanism.

**Lactate elevation.** Lactate can rise when production increases or clearance falls. Impaired oxygen delivery is one mechanism, but stress-related metabolism and impaired clearance can also contribute. A high lactate is not a direct label for sepsis or a unique indication of volume depletion.

The observations need to be interpreted as a joint physiological pattern. Their temporal relationships often matter more than whether each crosses an isolated threshold.

### Sepsis connects infection to organ dysfunction

Sepsis involves life-threatening organ dysfunction arising from a dysregulated response to infection.

The mechanism includes interacting inflammatory, endothelial, circulatory, and metabolic changes. Vascular tone can fall, barrier function can become abnormal, and microvascular flow can become heterogeneous. Organ dysfunction is therefore not simply the presence of a pathogen in the blood.

Several diagnostic distinctions follow:

- Infection can exist without sepsis.
- A positive culture can represent infection, colonization, or contamination, depending on the sample and context.
- Negative cultures do not exclude a clinically important infection.
- Fever and hypotension can have noninfectious causes.
- Organ-dysfunction scores summarize observations but do not independently determine their cause.

The clinician must connect a plausible infection to new or worsening organ dysfunction while continuing to examine alternative explanations.

A retrospective sepsis label often operationalizes this clinical reasoning through a rule involving suspected infection and selected physiological variables. The rule is a reproducible research target, but it is not a direct measurement of the complete underlying biological state.

### Bedside reasoning starts by verifying the observation

A monitor alarm should prompt interpretation of both the patient and the measurement system.

An arterial waveform can be altered by damping, resonance, transducer positioning, and line problems. Pulse-oximetry readings can be affected by poor perfusion, motion, and other measurement conditions. Device performance can also vary with skin pigmentation.

A sudden change may represent:

- A real physiological event.
- A procedure or repositioning.
- A treatment adjustment.
- A disconnected or disturbed sensor.
- A change in the device or signal-processing pipeline.

The time series should retain quality indicators where available. Removing all artifacts automatically can also remove real transient events if artifact detection is based only on unusual values.

Verification does not imply waiting for every uncertainty to be resolved before support begins. In critical illness, assessment and treatment often proceed together. The resulting data consequently include observations obtained before, during, and after intervention.

### Imaging narrows the mechanism but does not replace physiology

| Modality | Useful observations | Limits relevant to AI |
|---|---|---|
| Focused echocardiography | Ventricular function, chamber relationships, pericardial fluid, selected loading and flow information | Image quality and operator access vary; a finding needs clinical interpretation |
| Lung ultrasound | Pleural fluid, peripheral consolidation, altered peripheral lung aeration, pneumothorax-related signs | Similar patterns can arise through different mechanisms; inaccessible regions remain unassessed |
| Chest radiography | Lung opacities, devices, selected structural changes | Portable acquisition and projection affect appearance; overlapping causes of opacity remain |
| CT | Detailed anatomical assessment of selected causes and complications | Requires a suitable clinical question and feasible transport; acquisition is strongly selected by clinical circumstances |
| Vascular ultrasound | Selected thrombotic or flow findings | Coverage, compressibility, and technical access determine what is assessed |

B-lines are ultrasound artifacts associated with several conditions affecting peripheral lung aeration. They can accompany pulmonary edema but do not by themselves establish a cardiogenic cause. Consolidation can reflect infection, collapse, or other processes.

A chest image obtained after intubation can also reveal the care pathway through tubes, lines, and projection. Those features may predict severity or an outcome without demonstrating recognition of the disease mechanism.

The image time must therefore be linked to support, procedures, and the intended prediction time.

### The same value can describe different clinical states

Consider two patients with similar observed blood pressure.

One maintains that pressure without circulatory support and has improving organ function. The other maintains it only while receiving escalating support and has deteriorating perfusion findings.

A model that receives pressure alone can treat the measurements as equivalent. Clinically, they represent different states.

The same applies to oxygenation. An acceptable oxygen saturation on minimal support and the same saturation during intensive respiratory support do not establish equal respiratory function.

| Observed variable | Additional context needed |
|---|---|
| Blood pressure | Circulatory support, recent changes, waveform quality, perfusion findings |
| Oxygen saturation | Oxygen delivery system, ventilatory support, signal quality, hemoglobin and flow context |
| Consciousness | Sedation, analgesia, neurological baseline, metabolic state |
| Urine output | Collection interval, catheter status, fluid balance, medications, obstruction |
| Laboratory result | Collection time, result availability, treatment before sampling, baseline function |
| Heart rate | Rhythm, temperature, pain, medications, stroke-volume context |

This is why treatment variables cannot simply be discarded as “shortcuts.” They may be necessary to interpret the observed physiology. Their appropriate role depends on the target.

### Critical-care data are generated by a feedback system

A schematic description is

$$
X_{t+1}
=
f(X_t,A_t,U_t),
$$

where $$X_t$$ is the physiological state, $$A_t$$ the intervention, and $$U_t$$ other influences.

The recorded observation is

$$
O_t
=
g(X_t,A_t,M_t)+\varepsilon_t,
$$

where $$M_t$$ represents measurement conditions and $$\varepsilon_t$$ measurement error.

Clinical action depends on the information available so far:

$$
A_t
=
\pi(O_{\leq t},A_{<t},\text{clinical context}).
$$

These equations are a conceptual model, not a claim that the ICU follows a known simple dynamical law. They make the dependency explicit: the care policy helps generate the future data.

Measurement is also adaptive. A clinician may order more tests when concerned, place an invasive monitor after deterioration, or stop recording a variable after improvement. Missingness and sampling density therefore contain information about clinical decisions.

A model may exploit that information successfully under the original workflow. Transport to a different hospital then tests both physiological relationships and the stability of the observation and treatment policies.

### Confounding by indication: treatment can predict a poor outcome without causing it

The phrase “treatment is a confounder” is incomplete. Its role depends on the question.

When estimating the effect of a treatment, underlying severity can confound the treatment-outcome association:

$$
\text{severity}\rightarrow\text{treatment},
$$

$$
\text{severity}\rightarrow\text{outcome},
$$

while treatment may also affect the outcome.

Clinicians often treat patients because their underlying risk is greater. Treated patients can consequently have worse observed outcomes even when treatment is beneficial within comparable clinical states.

The mixture can be written as

$$
P(Y=1\mid A=a)
=
\sum_u
P(Y=1\mid A=a,U=u)
P(U=u\mid A=a),
$$

where $$U$$ indexes severity.

The weights

$$
P(U=u\mid A=a)
$$

can differ between treated and untreated groups. A crude comparison therefore combines treatment effects with differences in who received treatment.

The association is not guaranteed to have one direction. Contraindications, treatment limitations, access, and goals of care can produce other selection patterns.

In longitudinal care, the problem becomes more complex: earlier treatment changes later physiology, which influences later treatment and outcome. Whether a variable is a confounder, mediator, or legitimate predictive input must be specified relative to the causal or predictive question.

A mortality predictor using treatment information does not thereby estimate the effect of administering or withholding that treatment.

### Treatment response is informative but not a unique diagnosis

Clinicians reassess after intervention because the response supplies information about physiology and whether the current strategy is achieving its purpose.

But an improvement does not uniquely identify the original mechanism. Different causes can respond to the same supportive action. A variable can also improve while another aspect of organ function worsens.

Similarly, the ability of flow to increase after a change in filling conditions is not the whole decision about further fluid administration. Congestion, respiratory effects, and the broader physiological state remain relevant.

For AI, a response-prediction task needs to define:

- The intervention and clinical context.
- The response variable.
- The response interval.
- Concurrent interventions.
- The benefit or harm that the response is intended to represent.

Predicting a short-term pressure change is not equivalent to predicting improved organ function or survival.

### Where the labels come from

| Label | What it actually records | Main limitation |
|---|---|---|
| Physiological measurement | A value from a specified measurement process | Artifact, timing, support dependence, and incomplete physiological coverage |
| Clinician-adjudicated syndrome | Integrated clinical reasoning against an operational definition | Disagreement, incomplete records, and uncertainty about cause |
| Rule-derived organ dysfunction | Selected variables satisfying a rule | Can omit context and incorporate treatment effects |
| Intubation or vasopressor initiation | A clinical action | Reflects physiology, anticipation, practice, resources, and patient goals |
| Diagnosis or registry code | A documented classification | May be delayed, administratively shaped, or insufficiently specific |
| Mortality | A death within a specified setting or horizon | Influenced by care, competing illness, treatment limitations, and follow-up |
| Discharge or transfer | A change in location or care | Does not establish physiological recovery or complete subsequent outcome capture |

Intubation is not a unique label for respiratory failure. It can be performed for airway protection, a procedure, or other reasons. Similarly, a treatment order does not necessarily identify the exact onset of the physiological state that motivated it.

A high-quality dataset preserves the distinction between these labels rather than collapsing them into “deterioration.”

### Timing determines whether a warning is actually early

Clinical event time, sample collection time, result availability, order time, treatment administration, and documentation time are different.

Consider a patient whose clinicians recognize deterioration, obtain cultures, and begin treatment. A diagnosis code is added later. A model that alerts between treatment initiation and coding has preceded the code, but it has not necessarily anticipated clinical recognition.

Retrospective onset definitions can also use information collected after the nominal onset. Such definitions may be legitimate for adjudicating an outcome. They become problematic if future information is included among the model's supposed real-time inputs.

An early-warning evaluation should state:

- What event is being anticipated.
- How its time is established.
- When each predictor became available.
- Whether clinicians had already recognized or acted on the problem.
- What action remained possible after the alert.
- How repeated alerts around one episode are counted.

A short inference time does not establish useful clinical lead time.

### Differential diagnosis remains active during support

Infection, hemorrhage, myocardial dysfunction, pulmonary vascular obstruction, medication effects, and noninfectious inflammatory illness can produce overlapping instability.

The differential is narrowed through the history, examination, trajectory, laboratory evidence, imaging, and response to support. Several mechanisms can remain present together.

The practical question is often not merely “Which label is correct?” but “Which explanation accounts for the current pattern, which alternative remains consequential, and what evidence would discriminate them?”

A model that provides a confident syndrome label without exposing uncertainty about mechanism can encourage premature closure. A model that reports only generic severity can miss the distinction between different actionable causes.

This is a reason to evaluate both recognition and the clinical interpretation encouraged by the output.

### Error costs include the effects of repeated alerts

Missing deterioration can delay assessment and treatment. False alerts can produce unnecessary tests, medications, invasive procedures, or inappropriate escalation. Repeated low-value alerts can also divert attention from other patients.

The unit of evaluation matters. A model that is correct on many stable time windows may still miss the clinically decisive transition. A model that detects every episode by repeatedly alerting throughout a stay may impose an unacceptable burden.

Useful evaluation includes:

- Missed episodes and clinically meaningful detection delay.
- Alert burden per patient and unit of time.
- Repeated alerts belonging to the same event.
- False escalation and downstream consequences.
- Performance under different treatment and measurement policies.
- The human team's response to the system.

Mortality risk should not be equated with futility. A high-risk patient can still benefit from treatment. Predictions also do not determine the person's preferences or goals of care.

If a model changes treatment, it changes the future outcomes on which it will be evaluated. That feedback must be considered when interpreting apparent false alerts, prevented deterioration, and calibration after deployment.

### Revision checklist

| Question | What I should be able to explain |
|---|---|
| What is the target? | Physiology, syndrome, action, code, or outcome |
| Why is saturation not oxygen delivery? | Delivery also depends on hemoglobin and blood flow |
| Why is pressure not perfusion? | Similar pressure can arise from different flow-resistance combinations |
| What distinguishes shock mechanisms? | Problems of circulating volume, pump function, vascular distribution, or mechanical obstruction |
| Why is lactate not a sepsis label? | Production and clearance have several causes |
| What does treatment context add? | It changes the interpretation of otherwise similar measurements |
| Why is missingness informative? | Clinicians choose when and what to measure |
| What is confounding by indication? | Severity influences both treatment allocation and outcome |
| Why is treatment prediction not treatment-effect estimation? | Observed actions are selected, not interchangeable alternatives |
| What makes a warning early? | It precedes a defined event with usable information and actionable time |
| What is the reference standard? | A specified measurement, adjudication, action, or recording process |
| What are the relevant error costs? | Missed deterioration, unnecessary escalation, alert burden, and effects on the team |

## Why it matters for my work

Critical care connects the ontology's feedback and measurement ideas directly to clinical evidence. A model observes physiology through a care process that changes that physiology. Clinical assessability is therefore time- and support-dependent, and Clinical evidence reliance requires distinguishing disease information from recognition of clinicians' existing concern.

## What I have not resolved

- How can an audit preserve treatment information needed to interpret physiology while identifying overdependence on local care practices?
- How should a warning system be evaluated when its successful use prevents the event used as its original label?

---

Sources: General critical-care physiology; consensus publications on circulatory shock and sepsis; FDA information on pulse-oximetry limitations. The dynamical and causal expressions clarify the task rather than prescribe treatment. These are study notes for research purposes, not clinical guidance.
