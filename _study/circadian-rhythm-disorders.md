---
layout: study_note
title: "Circadian Rhythm Disorders"
description: "Wearable and continuous data, and what changes when the signal is a long time series."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "neurology"
category_title: "Neurology & Sleep Medicine"
subgroup: "Sleep & Circadian Regulation"
order: 5
source: "Lecture"
written: true
updated: "2026-09-08"
---

Circadian rhythm sleep-wake disorders concern the organization and timing of sleep in relation to internal biological rhythms and the environment. The relevant evidence is longitudinal: when sleep occurs, whether the pattern is stable or drifting, and how it affects function under the person's actual schedule.

## Core question and definition

A late bedtime, an unusual work schedule, and a circadian disorder are not equivalent.

The clinical assessment distinguishes:

- Internal circadian phase.
- The rhythm's relationship to the environmental day.
- Actual sleep and wake behavior.
- Opportunity and preference for sleep.
- Required work, school, and social timing.
- Insomnia, sleepiness, and functional impairment.

A person can have a late preferred schedule without a disorder. Conversely, substantial impairment can arise when sleep timing conflicts with required activity.

The social context is therefore part of the diagnosis, but the disorder is not merely deviation from a socially preferred bedtime. Some disorders involve failure to remain entrained to the daily cycle or poor consolidation of the sleep-wake rhythm. Biological organization, symptoms, and context must be assessed together.

For AI, sleep-wake estimation, phase estimation, period estimation, disorder classification, and impairment prediction are separate tasks.

## Key concepts

### Circadian timing and sleep pressure are different processes

The suprachiasmatic nucleus coordinates circadian timing. Retinal light input helps align this system with the environment, and downstream pathways influence rhythms in alertness, melatonin secretion, temperature, and other physiology.

This system provides a time-dependent tendency toward sleep or wakefulness. It does not simply count how long a person has been awake.

Homeostatic sleep pressure, by contrast, generally accumulates during wakefulness and dissipates during sleep.

The two processes interact. Someone can be tired after prolonged wakefulness yet have difficulty initiating sleep at a circadian phase that promotes wakefulness. A person required to wake during their biological night can remain sleepy even when the alarm occurs at an ordinary social time.

This explains why the same sleep opportunity can have different effects at different internal phases. It also explains why total time in bed does not fully describe circadian alignment.

A wearable that recognizes inactivity has observed behavior influenced by both processes and by external constraints. It has not separately measured each mechanism.

### Entrainment links the internal oscillator to the environment

An endogenous rhythm has a tendency to continue cycling. Environmental cues help align its timing with the external day.

Light is a major cue for the central circadian system. Its effect depends on timing relative to internal phase, as well as the characteristics of exposure. Other scheduled activities can also help organize behavior and peripheral rhythms.

Two effects should be distinguished.

**Phase shifting** changes the timing of the rhythm.

**Masking** changes the observed output without necessarily indicating a corresponding shift of the internal clock. Work demands, activity, sleep deprivation, and medication can alter observed sleep or activity directly.

A night worker can remain active during biological night because the job requires it. That activity pattern does not prove that the internal clock has fully shifted to the work schedule.

Similarly, a person can lie still at a required bedtime while their internal sleep tendency remains delayed.

### Phase, period, amplitude, and regularity are different quantities

A simple periodic signal can be represented schematically as

$$
r(t)
=
b+a\cos\left(\frac{2\pi t}{\tau}-\phi\right),
$$

where:

- $$b$$ is a baseline.
- $$a$$ describes amplitude.
- $$\tau$$ is the period.
- $$\phi$$ describes phase.

This is a teaching model, not an assertion that actigraphy or melatonin follows a perfect sinusoid.

Changing phase moves a feature of the rhythm to a different time without necessarily changing the interval between cycles. Changing period alters the interval between repeated features.

A stable late phase is therefore different from a rhythm that progressively shifts relative to clock time.

Amplitude and regularity add further distinctions. A weak day-night activity contrast can reflect fragmented behavior, immobility, environmental disruption, or other causes. It does not automatically establish a weak endogenous oscillator.

The observed period can also reflect external forcing. A daily work schedule can generate a strong daily activity pattern even when the internal rhythm is misaligned.

### Why a drifting rhythm requires a long enough record

Consider an idealized unforced rhythm with marker times

$$
t_k=t_0+k\tau,
$$

where $$\tau$$ is the interval between successive cycles.

Let the environmental day have duration $$T_{\mathrm{day}}$$. Comparing the marker with the corresponding environmental cycles gives

$$
t_k-kT_{\mathrm{day}}
=
t_0+k(\tau-T_{\mathrm{day}}).
$$

The relative timing changes by

$$
\tau-T_{\mathrm{day}}
$$

per cycle.

This shows the distinction between a fixed phase offset and progressive drift. A short record can make a slowly drifting rhythm look like a stable delay or advance.

Real sleep timing is also affected by entrainment, naps, obligations, and masking. The expression therefore explains a principle rather than supplying a diagnostic rule from observed bedtimes.

Estimating endogenous period requires more than finding a peak in an activity spectrum. The measurement conditions must allow separation of the rhythm from imposed schedules and other periodic influences.

### The main clinical patterns

| Pattern | Longitudinal observation | Clinical distinction |
|---|---|---|
| Delayed sleep-wake phase | Sleep onset and waking remain later than desired or required | Sleep can be more satisfactory on a compatible schedule; impairment and differential diagnosis still matter |
| Advanced sleep-wake phase | Sleep tendency and waking occur earlier than desired or required | Early timing alone is not a disorder without the relevant clinical problem |
| Non-24-hour sleep-wake rhythm | Sleep timing does not remain aligned with the environmental day | A drifting pattern can produce alternating periods of better and worse alignment |
| Irregular sleep-wake rhythm | Sleep is poorly consolidated into a stable main episode | Multiple sleep periods and weak organization differ from a simple fixed phase shift |
| Shift-work-related disorder | Insomnia or sleepiness is related to a work schedule that conflicts with usual sleep timing | Working nights alone does not establish the disorder |
| Jet-lag-related disorder | Symptoms follow rapid displacement relative to a new local schedule | The recent change in environmental timing is central to interpretation |

Loss of effective light entrainment is one mechanism relevant to non-24-hour rhythms, including in some people with profound visual impairment. A visual-impairment label does not by itself establish the state of the circadian system, and nonentrained patterns can also occur in sighted people.

Irregular sleep-wake organization can occur in neurological and other clinical contexts. It should not be inferred solely from one fragmented night.

These conditions can coexist with other sleep disorders. Classification should not force every complaint into a mutually exclusive circadian category.

### What actigraphy actually measures

Actigraphy records movement and uses an algorithm to infer rest and sleep-related intervals.

It is useful because it can observe patterns across many days in the person's ordinary environment. It can complement a sleep diary and help identify stable timing, variability, naps, or drift.

Its main limitation follows from the measurement itself:

- Quiet wakefulness can be classified as sleep.
- Movement during sleep can be classified as wake.
- Device removal can resemble prolonged inactivity.
- Physical impairment can change movement independently of sleep.
- The algorithm and device placement affect inferred intervals.

Actigraphy does not directly measure the circadian pacemaker or the electrophysiological features used to score sleep stages.

Additional wearable sensors can supply useful information, but an inferred sleep label remains a model output. It should not automatically become the reference standard for another model claiming to measure sleep or circadian phase.

A daily pattern in wrist movement is evidence about daily behavior. Its relationship to internal phase requires validation.

### Diaries supply information that movement cannot

A sleep diary can record:

- Intended bedtime and attempted sleep.
- Perceived sleep onset and waking.
- Time out of bed.
- Naps.
- Work and school obligations.
- Symptoms and perceived sleep quality.
- Relevant exposure and treatment changes.

These distinctions matter. Time in bed is not the same as time asleep. A person may attempt sleep early but remain awake, or voluntarily delay going to bed despite being able to sleep.

Diaries have recall and reporting limitations. Agreement between a diary and actigraphy is useful, but disagreement can also be informative. It can reveal quiet wakefulness, nonwear, misunderstanding of the diary, or a mismatch between perceived and inferred sleep.

The objective is not to declare one source universally correct. It is to understand what each recorded and why their accounts differ.

### A circadian biomarker has its own sampling conditions

Dim-light melatonin onset is a marker used to estimate circadian phase from the rise in melatonin under specified conditions.

Its interpretation requires more than obtaining a melatonin value:

- Samples must cover the relevant part of the profile.
- Their timing must be known.
- Light conditions must be controlled appropriately.
- The assay and onset definition must be stated.
- Medication and exogenous melatonin exposure can affect interpretation.
- A profile that does not capture the rise cannot automatically establish absent secretion.

A single low concentration can occur before a rise, after a decline, or under conditions that suppress or alter the measurement. It is not a unique phase estimate.

The onset rule may use a concentration crossing or another declared method. Different procedures are not automatically interchangeable labels.

A measured onset estimates phase at that assessment. It does not, by itself, establish the intrinsic period, the person's habitual sleep opportunity, or the presence of clinically significant impairment.

The interval between a phase marker and sleep timing also contains information. Two people with similar bedtimes can have different relationships between sleep and internal phase.

### What other modalities contribute

| Observation or modality | What it can support | What it cannot establish alone |
|---|---|---|
| Clinical history | Symptoms, obligations, opportunity, exposures, and longitudinal context | Objective timing of every sleep episode |
| Sleep diary | Intended and perceived sleep-wake behavior | Direct electrophysiological sleep or an endogenous phase marker |
| Actigraphy | Movement-derived rest and activity patterns across days | Direct circadian phase or complete sleep physiology |
| Melatonin profile under a defined protocol | A circadian phase marker | The full disorder diagnosis or intrinsic period from one assessment |
| Polysomnography | Sleep physiology and evidence for selected competing sleep disorders | Habitual circadian organization from a single night |
| Temperature or other physiological rhythms | Additional timing information in suitable settings | A context-free measure unaffected by activity, posture, illness, or measurement conditions |
| Brain imaging | Investigation of selected neurological questions | Routine confirmation of a circadian rhythm sleep-wake disorder |

The test should follow the uncertainty. Suspected sleep apnea requires a different assessment from a suspected progressive phase drift.

Routine structural brain imaging does not supply the longitudinal behavioral and phase evidence needed to diagnose a circadian sleep-wake disorder.

### Clinical reasoning reconstructs the schedule before assigning a label

The clinician asks when the person sleeps, when they can sleep, when they are required to sleep or wake, and what happens when those constraints change.

The history includes workdays and free days, naps, light exposure, recent travel, rotating shifts, medication, caffeine and other relevant substances, mood, and neurological conditions.

A useful sequence is:

1. Establish the main complaint: difficulty initiating sleep, early waking, daytime sleepiness, irregular timing, or another problem.
2. Determine whether adequate sleep opportunity exists.
3. Reconstruct the pattern across relevant days and schedules.
4. Compare reported timing with longitudinal measurements where appropriate.
5. Examine whether symptoms track misalignment.
6. Assess competing and coexisting explanations.
7. Use phase measurements or other tests when they answer a defined uncertainty.

Improvement on free days supports a schedule-related explanation, but is not specific to a circadian disorder. Someone with insufficient sleep during workdays can also improve when allowed to sleep longer.

The assessment must distinguish recovery from sleep restriction from improved alignment of sleep with biological timing.

### Differential diagnosis: the same complaint can have different mechanisms

| Alternative or coexisting condition | Why it can resemble a circadian disorder | What helps distinguish it |
|---|---|---|
| Insomnia disorder | Difficulty sleeping at the desired time | Whether difficulty persists across compatible schedules, together with the broader clinical assessment |
| Insufficient sleep opportunity | Daytime sleepiness and recovery sleep on free days | Actual opportunity, obligations, and sleep duration across the schedule |
| Sleep apnea | Fragmented sleep and daytime impairment | Relevant symptoms and appropriate physiological testing |
| Restless legs symptoms | Difficulty settling to sleep, often in the evening | The characteristic subjective experience and clinical history |
| Mood disorder | Altered sleep timing, duration, or perceived need | Mood symptoms, course, and the relationship between sleep and the broader condition |
| Medication or substance effects | Delayed sleep, sedation, or fragmented sleep | Timing of exposure and the temporal relationship to symptoms |
| Neurological disease | Fragmented or irregular sleep-wake organization | Neurological context, function, and longitudinal assessment |
| Environmental disruption | Poor or irregular sleep | Noise, light, caregiving, work, and other external constraints |

These are not always competing labels. Circadian misalignment and insomnia can coexist. Sleep apnea can complicate an already delayed schedule. A model trained with one label per record can hide this clinical overlap.

Actigraphy alone cannot resolve all of these alternatives because many produce similar movement patterns.

### Worked reasoning: late timing is not the diagnosis

Consider someone whose sleep occurs late and remains stable. They sleep adequately on their preferred schedule, function well, and do not report a relevant conflict or impairment.

The timing describes a late pattern. It does not, by itself, establish a disorder.

Now consider someone with a similarly late pattern who repeatedly cannot initiate sleep at a required earlier time, must wake before obtaining adequate sleep, and experiences persistent impairment.

The schedule conflict is clinically important, but the assessment still asks whether the pattern reflects circadian timing, insufficient opportunity, insomnia, medication, or another condition. A phase marker can add evidence about internal timing when appropriately obtained.

Finally, consider a night worker whose actigraphy shows daytime rest. That behavior may be imposed by employment. It does not prove that the internal rhythm has shifted to the same degree.

The same visible rest interval can therefore represent preference, symptomatic misalignment, or imposed behavior with incomplete physiological adaptation.

A model that recognizes an employer's roster may predict schedule-related complaints. It should not claim to have measured endogenous phase without a corresponding validation.

### Where the diagnostic label comes from

The disorder label is usually a clinical synthesis of timing, symptoms, functional consequences, context, and exclusion or recognition of alternatives.

Different datasets can instead provide narrower references.

| Dataset label | What it supports | What should not be inferred automatically |
|---|---|---|
| Clinician-assigned disorder | Reproduction or prediction of a clinical assessment | A direct biological measurement independent of the assessment process |
| Diary-defined timing category | A reported behavioral pattern | Endogenous phase or clinical impairment |
| Actigraphy-derived sleep interval | An algorithm's estimate from movement | An independent physiological sleep standard |
| Melatonin-derived phase | Phase under the recorded sampling protocol | A complete disorder diagnosis |
| Work schedule | Exposure to a timing constraint | Presence of a symptomatic disorder |
| Daytime impairment questionnaire | Reported functional burden | Its unique physiological cause |
| Registry diagnosis | A recorded clinical classification | Complete diagnostic criteria or precise onset |

If the clinical reference incorporates the same actigraphy used by the model, agreement can show successful reproduction of the assessment pathway. It does not provide independent validation of an additional claim about endogenous phase.

The source of the label should therefore remain visible. A model can perform well at predicting a recorded diagnosis while relying on schedule, access to specialist assessment, or device-specific processing.

### Timing errors can become apparent biological effects

Long recordings introduce technical problems that resemble rhythm changes:

- Device clock drift.
- Time-zone changes.
- Daylight-saving transitions.
- Travel.
- Nonwear and charging.
- Changes in device or software.
- Missing diary entries.
- Changes in work schedule.
- Treatment or light-exposure changes.

Absolute time and local clock time serve different purposes. Absolute time helps preserve elapsed intervals. Local time is needed to interpret the relationship to the environment and obligations.

A time-zone correction can shift recorded bedtime without changing the underlying biological event. Failing to preserve that distinction can create a false phase shift.

Clock phase is also circular. Times immediately before and after midnight are close, although a naive linear difference can make them appear far apart. Period estimation, by contrast, needs the elapsed time between successive cycles rather than repeatedly folding everything into one clock day.

The preprocessing must follow the target being estimated.

### What a medical AI system should be evaluated against

A sleep-wake estimator needs a reference for sleep and wake under the relevant conditions.

A phase estimator needs an appropriately obtained phase reference.

A period estimator needs a recording and protocol capable of identifying the relevant recurrence rather than merely the imposed schedule.

A disorder classifier needs symptoms, context, and clinical assessment.

An impairment predictor needs a functional outcome.

These tasks should not share a generic claim of “circadian accuracy.”

Evaluation should also separate people and relevant episodes appropriately. Adjacent windows from the same person's recording can share routines, device characteristics, and environmental patterns. Splitting them across training and testing can overstate performance on new people.

Transport should examine changes in schedules, devices, mobility, age groups, clinical conditions, and exposure patterns relevant to the intended use.

Schedule information can be a legitimate predictor when the target is schedule-related impairment. It becomes an unsupported substitute when the claim is that the model independently measured the internal clock.

### Treatment timing explains the consequences of phase error

Management can involve changes to sleep scheduling, light exposure, and appropriately timed interventions in selected disorders. The timing relative to internal phase is part of the mechanism.

The same type of exposure can have different phase effects at different biological times. An intervention intended to improve alignment can therefore be poorly matched if the phase estimate is wrong.

This is not a reason to prescribe one timing rule for everyone with a late bedtime. The disorder, phase, desired schedule, sleep opportunity, and other conditions all matter.

An improvement in daytime function can also occur because a schedule becomes more compatible with the person, without proving that the endogenous clock changed. Conversely, a phase marker can shift without resolving the functional problem.

Physiological change and clinical utility need separate outcomes.

### Error costs include pathologizing normal variation

A false-positive disorder label can pathologize a compatible early or late schedule, create unnecessary treatment burden, or encourage a schedule that reduces sleep opportunity.

A false-negative label can leave persistent misalignment and impairment unrecognized. It can also encourage explanations based solely on motivation or adherence when the timing problem has not been adequately assessed.

A wrong phase estimate has a directional consequence: an intervention intended to move timing toward the desired schedule can move it away instead.

Misattributing sleepiness to a circadian problem can delay assessment of sleep apnea, medication effects, or another condition. Conversely, treating every complaint as insomnia can miss a timing pattern that needs a different approach.

The appropriate error analysis therefore separates:

- Sleep-wake estimation error.
- Phase and period estimation error.
- Disorder misclassification.
- Failure to recognize insufficient evidence.
- Missed alternative diagnoses.
- Functional consequences under the proposed use.

### Revision checklist

| Question | What I should be able to explain |
|---|---|
| What makes the pattern a clinical disorder? | Relevant symptoms and impairment interpreted with timing, opportunity, and context |
| How do circadian timing and sleep pressure differ? | One organizes time-dependent propensity; the other reflects prior wake and sleep |
| What is entrainment? | Alignment of the internal rhythm with environmental timing |
| What is masking? | A change in observed behavior or physiology that need not represent a phase shift |
| How do phase and period differ? | Timing within a cycle versus the interval between cycles |
| Why can a short record miss nonentrainment? | Slow drift can resemble a stable phase offset |
| What does actigraphy measure? | Movement from which sleep-related intervals are inferred |
| What does a melatonin onset provide? | A phase marker under a specified sampling and assay protocol |
| Why does a biomarker not establish the whole disorder? | Symptoms, schedule, opportunity, and alternatives remain necessary |
| What defines the label? | Clinical assessment, behavior, biomarker, schedule, impairment, or a code |
| Why preserve clock metadata? | Technical time changes can mimic biological phase changes |
| What determines clinical value? | Improved function and appropriate decisions, not timing accuracy alone |

## Why it matters for my work

Circadian medicine makes the ontology's measurement limits temporal. Clinical assessability depends on recording duration, sampling conditions, and the relation between behavior and internal phase. Clinical evidence reliance requires showing that a model uses the signal relevant to its claim, rather than substituting a device pattern or social schedule for a physiological measurement.

## What I have not resolved

- Which combinations of longitudinal behavior and phase measurements can distinguish internal timing from imposed routine in realistic data?
- How should a model represent uncertainty when the recording supports a behavioral pattern but not a complete clinical diagnosis?

---

Sources: NHLBI material on circadian rhythm disorders and sleep-wake regulation; Smith and colleagues on actigraphy assessment; Benloucif and colleagues, Measuring Melatonin in Humans. The periodic-signal expressions are teaching constructions and do not supply diagnostic cut-offs or treatment schedules. These are study notes for research purposes, not clinical guidance.
