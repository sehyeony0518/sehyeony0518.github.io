---
layout: study_note
title: "Clinical Feature Annotation and Multi-Task Learning"
description: "Building supervision from structured sonographic findings rather than the diagnosis alone."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "hepatobiliary"
category_title: "Hepatobiliary Medicine & Imaging"
subgroup: "Clinical-to-AI Connections"
order: 16
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-11-29-concept-bottleneck-models"
---

## Core question and definition

**How can structured sonographic findings provide useful supervision without turning uncertain or missing observations into false ground truth?**

A diagnosis summarizes a clinical conclusion. Feature annotation records particular observations: where a lesion lies, whether an interface is depicted, what its internal echoes look like, and what acoustic effects accompany it.

These are different targets. A patient can have a well-established diagnosis while a selected image does not show the defining feature. Conversely, an image can show a clear abnormality whose cause remains uncertain.

Multi-task learning uses several targets during training, often sharing a representation between diagnosis and feature prediction. Its clinical value depends first on whether those targets are meaningful, observable, and attached to the correct unit of evidence.

## Key concepts

### Separate observation, interpretation, and action

A useful feature vocabulary distinguishes three levels.

| Level | Example | Basis of the statement |
|---|---|---|
| Observation | Focal wall thickening is depicted. | An interpretable image finding |
| Interpretation | The appearance supports benign remodelling. | A differential informed by several findings and context |
| Clinical action | Additional characterization is appropriate. | Uncertainty, consequences, patient context, and available care |

Labeling an image “invasion” when it shows an indistinct interface skips from observation to etiology. Labeling it “requires surgery” goes further, into management.

These higher-level statements can be legitimate targets for appropriate tasks. They should not be presented as directly observed morphology. Otherwise the feature dataset imports the diagnostic conclusion that it was intended to help examine.

### Define the anatomical object

The gallbladder lumen, wall, and surrounding tissues produce different findings.

Luminal echoes can represent stones, sludge, or tissue projecting into the lumen. Wall changes can reflect edema, muscle thickening, intramural sinus formation, fibrosis, or neoplastic infiltration. Surrounding fluid and adjacent liver changes provide context but have their own differential.

A feature therefore needs an object. “Irregular” is incomplete without specifying an interface. “Echogenic” is incomplete without identifying a structure and, where appropriate, its comparison tissue.

Even a familiar term such as “wall thickness” depends on boundaries, plane, distension, and whether the relevant segment is adequately seen. Consistency begins with agreeing on the observation, not with computing agreement after ambiguous labels have accumulated.

### Why mechanisms should inform definitions

Inflammatory change can increase tissue water and alter the wall's appearance. Benign remodelling in adenomyomatosis can create intramural sinuses. Infiltrating neoplastic tissue can distort architecture.

These processes explain why the annotation vocabulary should preserve both shared and more discriminating findings. Thickening alone is broad. An intramural cystic space is a more specific structural observation, but its presence still depends on adequate resolution and anatomical localization.

A posterior acoustic effect is another kind of feature: it arises through sound propagation. Its annotation should identify the relationship to the suspected source, rather than treating the dark or bright region as a separate tissue lesion.

Mechanistic knowledge helps readers describe evidence coherently. It must not become a rule that an expected feature is present whenever a diagnosis is known.

### Match the annotation unit to the evidence

| Unit | Suitable examples | Common overreach |
|---|---|---|
| Region or interface | Visible margin segment, intramural space | Certifying unseen parts of the wall |
| Frame | Echogenicity and architecture depicted in that view | Claiming mobility or whole-lesion extent |
| Clip or positional sequence | Demonstrated motion or changing relationship | Treating all motion as lesion mobility |
| Lesion | Findings integrated across relevant views | Assigning its features to every stored image |
| Examination | Coverage, multiple lesions, examination-level observations | Equating an incomplete examination with a normal one |
| Clinical episode | Diagnosis incorporating symptoms, tests, and course | Treating the episode label as a pixel-level reference |

Motion deserves particular care. Movement of the probe or patient can change the image without demonstrating that luminal material moves relative to the gallbladder wall. A mobility annotation needs evidence of the intended relationship.

Repeated frames also do not create independent clinical confirmation. They may reproduce the same view, limitation, or interpretive uncertainty.

### Operational definitions should preserve clinical distinctions

A practical definition specifies what is judged, what evidence is required, and when the judgment cannot be made.

| Feature | Definition must address | Interpretation to avoid |
|---|---|---|
| Wall thickening | Segment, distension, plane, visible boundaries | Treating every broad wall appearance as primary inflammation |
| Wall layering | Which segment and interfaces are resolved | Treating nonvisualization as proven destruction |
| Margin irregularity | Which named interface is irregular | Equating any irregularity with invasion |
| Echogenicity | Structure, comparison, and usable settings | Treating gray value as an absolute tissue property |
| Intramural cystic spaces | Localization within an adequately depicted wall | Calling adjacent fluid an intramural finding |
| Posterior shadowing | Shadow and plausible source along the beam | Assigning rib or bowel-gas shadow to a lesion |
| Vascularity | Acquisition capable of assessing the relevant signal | Calling tissue avascular after an inadequate Doppler examination |

An atlas of examples can clarify these terms, but textbook examples alone are insufficient. Borderline appearances, partial visibility, and common mimics are part of the concept's meaning.

### Keep presence, assessability, uncertainty, and missingness distinct

These are related questions, not interchangeable labels.

**Presence or absence** describes the finding when the evidence supports that judgment.

**Assessability** describes whether the available input permits the observation.

**Uncertainty** describes how securely the finding can be assigned. A structure may be visible but borderline; alternatively, acquisition may be too limited to support a judgment.

**Annotation missingness** describes the record. The feature may never have been requested or reviewed.

A blank field therefore cannot safely be converted into a negative. Nor does “not mentioned in the report” mean “looked for and absent.”

It is often useful to retain assessability separately from the feature assessment. That allows distinctions such as an adequately depicted but equivocal margin, an obscured margin, and a margin that no reader has evaluated.

### A negative finding has evidential requirements

“No flow detected” means that no relevant signal was demonstrated under the acquisition conditions. It does not universally establish absence of blood vessels.

“No mobility” is only meaningful if suitable observation was possible. A single retained image cannot establish it, and a structure that does not move may include an impacted stone or adherent sludge as well as a mural lesion.

“No intramural cystic spaces” is limited by resolution and coverage. Small spaces may be unresolved, and an inadequately seen wall segment cannot be confidently certified negative.

“No invasion” is particularly strong. An apparently preserved interface on ultrasound is an imaging observation; microscopic invasion is a pathological question.

The educational point is that negative annotations require positive evidence of adequate assessment.

### Preserve what readers were allowed to know

A reader assessing morphology from images has a different information set from a clinician interpreting the complete episode.

Knowing a pathological diagnosis may change how a subtle interface is interpreted. Seeing a model explanation may direct attention to a region that would otherwise be overlooked. Necessary clinical context can also improve interpretation.

There is no single information condition appropriate for every annotation task. The record should make the intended condition clear. An independent morphology reference should not be defined by copying the model's display or by inferring features solely from the final diagnosis.

Reader expertise, available views, clinical context, and access to subsequent findings affect the meaning of an annotation. They belong to its provenance.

### Disagreement is information about the task

Readers can disagree because they use different definitions, because the feature is subtle, because different views support different impressions, or because the acquisition is inadequate.

These causes have different remedies. A clearer definition may help semantic disagreement. Additional clinical evidence may resolve an image limitation. A genuinely borderline appearance may remain uncertain despite expert review.

Adjudication produces a documented consensus; it does not erase the original disagreement or establish that the consensus is infallible. Preserving the initial readings and the reason for resolution makes the final label interpretable.

Agreement statistics summarize the recorded decisions. They depend on which cases and feature frequencies are represented. High agreement in an easy, restricted sample does not establish reliability in a population dominated by subtle or unassessable findings.

### The reference for a feature differs from the reference for diagnosis

Histopathology can establish a tissue diagnosis, but specimen handling, sampling, orientation, and correspondence to the imaged lesion matter. A histological feature does not automatically have a visible sonographic counterpart in every frame.

Expert imaging consensus provides a reference for image appearance. It is appropriate for a defined morphological task, while retaining reader uncertainty.

Follow-up can support a conclusion about persistence, change, or resolution. It cannot retrospectively prove every detail of an earlier unclear image.

A registry code describes a recorded clinical category and may combine several forms of evidence. It is a different reference again.

A dataset can therefore contain a strong diagnostic reference and a weak feature reference, or the reverse. Calling both “ground truth” conceals this distinction.

### What a generic multi-task objective expresses

An ordinary multi-task objective can be written as

$$
L_{\mathrm{total}}
=
L_{\mathrm{diagnosis}}
+
\sum_j \lambda_j L_{\mathrm{feature},j}.
$$

Each feature loss is calculated over examples with an appropriate available label for that feature. An unassessed example should not contribute as though its feature were absent.

The coefficients express the relative optimization emphasis. They are not estimates of clinical importance. Loss scales, task frequency, label quality, and how examples are averaged all influence the training signal.

If one feature is annotated mainly in unusually clear examinations, its training term emphasizes that selected subset. Excluding unknown labels avoids inventing negatives, but it does not make the remaining labels representative of all intended inputs.

Thus label masking and clinical validity solve different problems: one controls which targets enter an objective; the other concerns what those targets mean.

### Why additional tasks can help or interfere

Shared tasks can encourage a representation to preserve information useful for several predictions. For example, learning the location of a wall segment may also support a morphological description.

They can also compete. A task dominated by machine-specific appearance may encourage a representation that transports poorly. A noisy or ambiguously defined feature can impose inconsistent supervision. An overly strong auxiliary objective can prioritize agreement with that feature over the diagnostic task.

There is no general theorem that adding clinically named targets improves clinical performance. The names do not determine the compatibility or reliability of their training signals.

The benefit claimed should match the evidence: better feature prediction, better diagnostic agreement, improved inspectability, and successful transfer are separate outcomes.

### Why feature accuracy does not prove diagnostic use

A shared representation can carry multiple kinds of information. The feature head can read anatomy while the diagnostic head uses a different correlated signal.

Accurate feature prediction therefore shows that the relevant information is available to that head under the evaluated conditions. It does not prove that the diagnostic prediction depends on those features.

A strict concept bottleneck changes the computational restriction by supplying concepts to the diagnostic component. It still inherits concept error, incomplete vocabulary, and possible mismatch between a variable's name and the information it carries.

Neither arrangement repairs a feature label that describes an unseen finding.

### Worked annotation example: an apparent mural projection

Consider a hypothetical still image showing a nonshadowing projection near the gallbladder wall. Part of the attachment is unclear. No positional sequence or Doppler acquisition is available. The clinical episode is labeled benign after follow-up.

An appropriate record can distinguish:

- A projection is depicted in the supplied view.
- Its full attachment is not adequately assessed.
- Mobility is not assessable from this input.
- Vascularity is not assessable from this input.
- The episode has a follow-up-based benign reference, whose scope should be stated.

It would be unjustified to convert this into “immobile, avascular benign polyp with a smooth attachment.” Each added adjective claims evidence that was not supplied.

If the clinical question is whether the projection is tissue or adherent sludge, the missing observations matter directly. A richly populated feature vector made from assumptions would be less useful than a shorter, honest description.

### Consequences of annotation errors

A false feature-positive can train the model to associate a common benign appearance with concern. A false feature-negative can suppress recognition of subtle disease. Treating poor visibility as normal can encourage reassurance precisely when additional evidence is needed.

These errors need not affect all patients equally. Depth, acoustic access, examination purpose, and available views influence which features can be assigned. A dataset with more complete labels in easier examinations can teach a different task from the one intended.

Feature annotation is therefore part of the clinical measurement system. Its quality cannot be inferred solely from how well a model fits the resulting labels.

### Revision checklist

| Question | Answer to retain |
|---|---|
| Is a feature label the same as a diagnosis? | No; observation, interpretation, and action are different levels. |
| Why specify the annotation unit? | Evidence may belong to a region, frame, sequence, lesion, or episode. |
| What does “irregular” need? | A named interface and an operational definition. |
| Is an empty field a negative? | No; it may mean unassessed, unassessable, or missing documentation. |
| Does absent Doppler signal prove avascularity? | No; acquisition adequacy limits that interpretation. |
| Does adjudication eliminate uncertainty? | No; it records a reasoned resolution. |
| Can pathology certify every image feature? | No; tissue truth and visible morphology must be distinguished. |
| Do loss weights measure clinical importance? | No; they set optimization emphasis. |
| Does auxiliary feature accuracy prove diagnostic use? | No; the computational paths can differ. |
| What makes a feature label useful? | Clear meaning, appropriate evidence, provenance, and honest uncertainty. |

## Why it matters for my work

Structured findings connect Mechanism → canManifestAs → Finding without making the inverse relationship certain. Clinical assessability limits which feature labels an acquisition can support. In turn, the clinical target sets requirements for supervision and evaluation; adding tasks does not bypass those requirements.

## What I have not resolved

- Which feature disagreements reflect unclear definitions, and which reflect irreducible image limitations?
- How much of the available feature record describes direct observation rather than diagnostic inference?
- Which clinically useful distinctions are lost when supervision requires an oversimplified label?

---

Sources: General clinical annotation and multi-task learning principles; Yu and colleagues on the imaging differential of benign gallbladder disease; and Koh and colleagues on concept bottleneck models. The loss expression is a generic learning objective, and the annotation example is illustrative. These are study notes for research purposes, not clinical guidance.
