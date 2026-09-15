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

Cardiovascular disease includes disorders of the heart and blood vessels. This note focuses on atherosclerotic disease and prevention, where the main prediction target is often a future clinical event rather than an abnormality that can be confirmed in the current image.

## Core question and definition

A cardiovascular risk model asks whether a specified event will occur within a specified time after an eligible baseline assessment. That is different from asking whether an artery currently contains plaque, whether a stenosis limits blood flow, or whether a patient is having an acute myocardial infarction.

These questions can be related without being interchangeable.

| Question | Target | Evidence needed |
|---|---|---|
| Is atherosclerosis present? | Current arterial-wall disease | Appropriate anatomical assessment |
| Is coronary flow insufficient under the tested conditions? | Functional significance | Clinical assessment and suitable physiological or stress testing |
| Is an acute myocardial injury ischemic? | Current clinical event and its mechanism | Symptoms, ECG, serial biomarkers, and other relevant findings |
| Will a cardiovascular event occur? | Future outcome over a horizon | Baseline information linked to longitudinal outcome ascertainment |
| Would an intervention improve this patient's outcome? | Benefit relative to an alternative action | Evidence about treatment effects, harms, and the intended decision |

A risk estimate is therefore incomplete without its population, endpoint, horizon, baseline, and care context.

Primary prevention concerns people without established atherosclerotic cardiovascular disease. Prevention of recurrent events concerns a different population, with existing disease and different management considerations. A model developed for one should not silently be interpreted as a model for the other.

## Key concepts

### How arterial-wall disease develops

Atherosclerosis develops within the arterial wall. Retention of cholesterol-containing particles, inflammatory-cell recruitment, and altered vascular-cell behavior contribute to plaque formation. Macrophages accumulate lipid, and smooth-muscle cells and extracellular matrix contribute to a fibrous covering over lipid-rich and damaged tissue.

The resulting lesion is more than a deposit protruding into a pipe. It has a composition, a relationship to the vessel wall, and a biological history.

Several consequences follow.

**Wall disease can precede marked luminal narrowing.** The vessel can remodel outward as plaque accumulates. An artery may therefore contain substantial wall disease before the residual lumen looks severely narrowed.

**Fixed narrowing can limit flow reserve.** A vessel may supply sufficient blood at rest but fail to meet increased myocardial demand. The clinical finding then depends on the circumstances under which the circulation is tested.

**An acute event can follow plaque disruption.** Rupture or erosion can expose thrombogenic material, activate platelets and coagulation, and produce an obstructing thrombus. The lesion responsible for an event need not previously have been the most conspicuous fixed narrowing.

**Calcification records one aspect of plaque biology.** Detectable calcium is a marker of calcified plaque burden. It does not describe every component of plaque or directly identify when a particular lesion will cause an event.

These mechanisms explain why plaque burden, stenosis, ischemia, and future infarction are related but distinct targets.

### Risk factors describe exposure and susceptibility

Blood pressure, lipid abnormalities, smoking, diabetes, kidney disease, age, and family history contribute information about cardiovascular risk through different pathways.

Raised blood pressure increases mechanical stress and the workload imposed on the heart. Lipid abnormalities influence arterial-wall lipid accumulation. Smoking affects vascular injury, inflammation, and thrombosis. Diabetes and kidney disease alter vascular and metabolic conditions in ways that extend beyond a single image-visible lesion.

Age can summarize accumulated exposure and changing physiological reserve. Family history can reflect inherited susceptibility and shared environments. Neither variable identifies a particular plaque in an image.

The measured value also has a context:

- Blood pressure depends on measurement technique, immediate circumstances, and treatment.
- Lipid measurements must be interpreted with medication status and relevant clinical context.
- An acute deterioration in kidney function is not interchangeable with a stable baseline measure.
- A value recorded after treatment began does not necessarily represent the untreated state.

A model can make a legitimate prognostic use of these variables without providing a mechanistic explanation of an individual future event. The distinction matters when an imaging model claims to have discovered disease-specific evidence rather than a correlated risk profile.

### Cardiovascular disease is broader than atherosclerosis

Not every cardiovascular outcome arises from plaque disruption.

Heart failure can reflect ischemic injury, chronic pressure overload, valvular disease, or other myocardial processes. Ventricular filling can be abnormal even when the fraction of blood ejected from the ventricle is preserved.

Arrhythmias concern electrical activation and rhythm. An intermittent arrhythmia may be absent from a brief recording. Some arrhythmias also change thromboembolic risk without being measurements of atherosclerotic burden.

Valvular disease alters flow and imposes pressure or volume loads. Its anatomical and functional assessment differs from coronary plaque assessment.

This heterogeneity affects outcome labels. A composite that includes heart failure is not the same target as one restricted to atherosclerotic events. A composite that includes revascularization also incorporates a treatment decision influenced by testing and local practice.

The label “cardiovascular event” must consequently be unpacked before interpreting model performance.

### What is observable, and at what stage?

| Modality or observation | What it can support | Important limitation |
|---|---|---|
| History and examination | Symptoms, exposures, previous disease, functional change | Recall and documentation are incomplete; symptoms are not specific to one mechanism |
| Blood pressure and laboratory measurements | Risk factors and aspects of current physiology | Technique, acute illness, treatment, and timing affect interpretation |
| ECG | Electrical activity during the recording | A normal tracing does not exclude every acute or intermittent cardiac process |
| Serial cardiac troponin | Evidence and evolution of myocardial injury | Injury is not, by itself, proof of a coronary thrombotic mechanism |
| Noncontrast coronary calcium CT | Location and burden of detectable calcified coronary plaque | Does not directly measure stenosis or exclude noncalcified plaque |
| Coronary CT angiography | Coronary lumen and plaque anatomy | Motion, calcification, and acquisition quality can limit assessment; anatomy alone does not fully establish physiological significance |
| Stress imaging | Evidence of inducible ischemia under the tested conditions | Results depend on the test and clinical setting; they are not a direct forecast of every future event |
| Echocardiography | Cardiac structure, motion, valve function, and hemodynamic information | Structural measurements require clinical interpretation; normal appearance does not exclude all disease |
| Cardiac MRI | Selected aspects of function, tissue injury, and scar | The acquired sequences determine what can be assessed |

A negative result should be expressed in the language of the test. “No coronary calcium detected” is narrower than “no coronary atherosclerosis” and much narrower than “no future cardiovascular event.”

Likewise, finding plaque establishes current anatomical evidence. It does not supply an individual event date or prove that preventive treatment will benefit every person with that appearance to the same extent.

### Diagnostic reasoning begins by separating the present from the future

The first clinical distinction is whether the person is being assessed for prevention or for a current symptom.

New chest discomfort may arise from myocardial ischemia, pulmonary disease, gastrointestinal disease, musculoskeletal causes, or another process. Breathlessness may reflect heart failure, pulmonary disease, anemia, or several conditions together.

A prevention score does not adjudicate this differential. It summarizes a different question over a different time scale.

For suspected acute coronary disease, the clinician integrates the presentation with ECG findings, serial biomarkers, and other relevant tests. Troponin identifies myocardial injury, but the mechanism still needs interpretation. Myocardial injury can occur in settings other than an acute coronary plaque event.

For stable symptoms, the question may instead concern obstructive coronary anatomy, inducible ischemia, valve disease, or ventricular dysfunction. Selecting a test requires deciding which uncertainty it is intended to resolve.

For asymptomatic prevention, the emphasis is on baseline risk factors, established disease status, and whether additional information would change a decision.

An AI system that mixes these settings can achieve apparent accuracy by recognizing which pathway the patient entered. That is not equivalent to recognizing the same disease state in an unselected population.

### Defining a future-event target

Let the baseline be the time when the model is intended to make its prediction. Let $$\tau$$ denote the chosen follow-up horizon.

A risk target can be written as

$$
p_\tau(x)
=
P(\text{target event by }\tau
\mid X_{\mathrm{baseline}}=x).
$$

This notation leaves an important clinical question to be specified: under what care?

Observed outcomes occur while people receive prevention, investigations, and treatment. A model trained on those outcomes ordinarily predicts risk under the care patterns represented in its data. It does not automatically estimate risk if all treatment were withheld.

The endpoint also needs an operational definition:

- Which events qualify?
- Is the target a first event or a recurrent event?
- Are fatal and nonfatal events combined?
- Are treatment decisions included?
- How are event dates assigned?
- How are uncertain causes of death handled?
- Does an event outside the original hospital system remain observable?

Changing any of these can change the meaning of the probability, even if the model inputs remain the same.

### Why incomplete follow-up is not a negative label

First consider a simple setting without competing events. Let

- $$T$$ be time to the target event.
- $$C$$ be time until follow-up ends.
- $$U=\min(T,C)$$ be the observed time.
- $$\Delta=\mathbf 1\{T\leq C\}$$ indicate that the event was observed.

The horizon-specific outcome is

$$
Y_\tau=\mathbf 1\{T\leq\tau\}.
$$

A person observed without an event until before $$\tau$$ does not yet have an observed negative horizon label.

| Follow-up record | What is known about the horizon outcome? |
|---|---|
| Target event observed before the horizon | Positive |
| Follow-up reaches the horizon without the target event | Negative for that horizon |
| Follow-up ends early without an observed event | Unknown beyond the last observation |
| Target event occurs after the horizon | Negative for the shorter horizon, potentially positive for a longer one |

Coding every early loss to follow-up as event-free assumes that no unobserved events occurred afterward. That can understate risk. Excluding incomplete records can also bias results if retention is related to health, care access, or other predictors.

Survival methods and censoring-aware evaluation address this problem under assumptions about the follow-up process. They do not make missing outcomes harmless. The assumptions need to be credible for the measured covariates and care setting.

The distinction is particularly important when linking imaging archives to hospital records. Absence of a subsequent event code in that hospital can mean event-free survival, care elsewhere, loss of contact, or an unrecorded death.

### Competing death changes the probability being estimated

For a nonfatal cardiovascular endpoint, death from another cause can prevent a later target event.

This is a competing event, rather than an ordinary interruption of observation in a person who remains at risk.

Let $$T$$ now represent time to the first occurrence of either the target event or a competing death, and let $$J$$ identify which occurred. The observed-world cumulative incidence of the target is

$$
P(T\leq\tau,\ J=\text{target}\mid X=x).
$$

A person who dies from another cause before the horizon cannot subsequently experience that first target event. Their record should preserve the competing outcome.

Treating competing death as ordinary censoring can answer a different question from the actual probability of experiencing the target before death. The distinction becomes clinically consequential when competing mortality differs across populations.

This also explains why “no target event” is not a single biological state. It can include healthy event-free survival, survival with other illness, or death from a competing cause. A label must retain enough detail to support the intended interpretation.

### The reference standard is an outcome-ascertainment process

A future event cannot usually be established by a baseline biopsy or image. Its reference comes from follow-up.

Event adjudication may combine clinical records, serial tests, imaging, procedure reports, death information, and predefined endpoint rules. This can be more reliable than an isolated code, but it still has limitations.

| Label source | What it contributes | What requires scrutiny |
|---|---|---|
| Adjudicated clinical event | An integrated assessment against an endpoint definition | Completeness of source records and uncertainty in event timing or mechanism |
| Hospital diagnosis code | A documented clinical or administrative classification | Coding practices, specificity, and whether the event is new |
| Procedure record | Evidence that an intervention occurred | The action reflects decision-making as well as disease |
| Death registry | Vital status and an assigned cause | Cause-of-death uncertainty and linkage quality |
| Patient report | Events that may occur outside linked systems | Recall, interpretation, and need for corroboration |
| No subsequent record | Absence of an observed record | Does not establish event-free follow-up |

There is no observed “true probability” for an individual. There is an event history, observed with varying completeness. Calibration evaluates whether probabilities agree with event frequencies across appropriate groups and time horizons.

### Calibration is essential for absolute-risk decisions

Discrimination asks whether people who experience an event tend to receive higher scores than those who do not. Calibration asks whether a stated probability agrees with the corresponding event frequency.

For a horizon outcome, perfect calibration can be expressed as

$$
P(Y_\tau=1\mid \widehat p_\tau=p)=p.
$$

The observed event frequency used to assess this relation must account appropriately for censoring and competing events.

A simple construction shows why ranking cannot replace calibration. Suppose $$p$$ is calibrated, and transform every prediction to

$$
q=p^2.
$$

Squaring preserves the ordering of probabilities, so the ranking is unchanged. But because $$p=\sqrt q$$,

$$
P(Y_\tau=1\mid q)
=
\sqrt q,
$$

which differs from $$q$$ for interior probabilities.

The model can retain its discrimination while understating absolute risk.

The reverse limitation also exists. A model that gives everyone the population event probability can be calibrated while providing no individual risk stratification.

Thus calibration is indispensable when decisions depend on absolute risk, but it is not universally “more important” than discrimination. Neither replaces the other, and neither alone establishes clinical utility. Their importance follows from the intended decision.

### Prediction under treatment is not prediction of treatment benefit

Suppose people judged to be at greater risk receive more intensive prevention. Their subsequent outcomes reflect both their underlying susceptibility and the treatment they received.

An event-free outcome after treatment does not establish that the original risk estimate was wrong. It also does not prove that treatment prevented an event in that individual; the untreated counterfactual was not observed.

The same issue arises after deployment. If a model changes who receives preventive care, future outcomes may differ from those generated under the previous policy. A model can appear to overpredict because care improved, because its calibration deteriorated, or because outcome ascertainment changed. Those possibilities require different explanations.

Prediction of benefit requires comparing outcomes under alternative actions. A model of observed event risk supplies only part of that decision.

The expected harms, treatment burden, competing illness, and patient preferences also matter. A probability threshold is a decision rule, not a boundary between healthy and diseased arteries.

### Worked clinical reasoning: the same image can support different claims

Consider an asymptomatic person with coronary calcification on an appropriate CT.

The image supports the presence of calcified coronary plaque. It may contribute to preventive risk assessment when used in the intended context.

It does not, by itself, establish:

- That a particular vessel has a flow-limiting stenosis.
- That the person is currently having an acute coronary event.
- That an event will occur within the model's horizon.
- That every observed calcification belongs to the coronary arteries.
- That a particular intervention has a favorable individual benefit-harm balance.

Now consider someone with new concerning symptoms and no detected coronary calcium. The negative calcium finding remains a statement about detectable calcified plaque. It should not be substituted for assessment of the acute presentation.

For an AI model, these cases distinguish detecting an image feature, estimating prognosis, and supporting a current clinical decision. A single output labeled “cardiovascular disease” conceals those differences.

### Error consequences depend on the decision

Underestimating preventive risk can withhold an opportunity to reduce future events. Overestimating it can expose people to unnecessary treatment burden, adverse effects, testing, expense, and anxiety.

These errors are not symmetric, but neither is every positive risk classification followed by no event a clinically meaningful false alarm. Risk is probabilistic, and subsequent care can change outcomes.

For current disease assessment, the consequences differ. Missing an acute event can delay urgent care, while an incorrect acute diagnosis can trigger unnecessary invasive evaluation or treatment. Those costs should not be represented by the same operating point used for long-term prevention.

Evaluation should therefore report:

- Horizon- and endpoint-specific calibration.
- Discrimination appropriate to the event-time setting.
- Censoring and competing-event handling.
- Performance in clinically relevant populations.
- Consequences at the proposed decision rule.
- Effects of using the model compared with the existing pathway.

An imaging model can recognize genuine plaque features and still provide poorly calibrated risk in another population. Conversely, a prognostic model can use useful age-related or systemic information without having demonstrated plaque-specific evidence reliance.

### Revision checklist

| Question | What I should be able to explain |
|---|---|
| What is being predicted? | Current anatomy, current physiology, an acute event, a future event, or treatment benefit |
| Why can plaque exist without severe stenosis? | Arterial-wall disease and remodeling can precede marked luminal narrowing |
| Why is stenosis not the whole risk story? | Acute thrombosis and other mechanisms are not summarized by fixed narrowing alone |
| What does calcium CT measure? | Detectable calcified plaque, with limits for noncalcified disease and stenosis |
| Which cardiovascular endpoint is used? | The exact event components and whether actions are included |
| What defines the baseline? | Eligibility, available inputs, established disease, and treatment state |
| Why is early loss to follow-up not negative? | The horizon outcome remains unobserved |
| Why preserve competing death? | It changes the probability of experiencing the target event |
| What is the outcome reference? | A specified ascertainment and adjudication process |
| Why is AUROC insufficient for risk-based decisions? | Ranking does not establish correct absolute probabilities |
| Why is calibration insufficient alone? | A calibrated model may provide little useful stratification |
| Why is event risk not treatment benefit? | Outcomes under alternative actions are different targets |

## Why it matters for my work

Cardiovascular prediction makes the distinction between an image finding and a clinical claim especially clear. In the ontology, Cardiovascular risk sets requirements for Bayesian decision analysis and longitudinal evaluation. Clinical assessability limits claims about visible plaque, while future risk also depends on exposures, care, competing events, and outcome ascertainment.

## What I have not resolved

- How should an imaging-based risk model be audited when useful prognostic information extends beyond the named anatomical feature?
- How can recalibration distinguish a changed patient population from changed prevention and incomplete event capture?

---

Sources: General cardiovascular teaching cross-checked against NHLBI resources on atherosclerosis and cardiac testing, and ACR/RSNA information on coronary calcium imaging. The probability examples are symbolic constructions, not empirical clinical estimates. These are study notes for research purposes, not clinical guidance.
