---
layout: study_note
title: "Auditing Explanation Faithfulness in Gallbladder Models"
description: "How the evidence a diagnostic model exposes can be checked against clinical information assessed separately from it."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "hepatobiliary"
category_title: "Hepatobiliary Medicine & Imaging"
subgroup: "Clinical-to-AI Connections"
order: 19
source: "Independent study"
written: true
updated: "2026-09-08"
featured: true
papers:
  - "2026-08-04-medical-algorithmic-audit"
---

## Core question and definition

**What does an explanation allow us to claim about a gallbladder model, and what additional clinical evidence is needed?**

An explanation audit examines the meaning and limitations of a model's explanation. Computational faithfulness concerns whether the explanation reflects the model's prediction process. Plausibility concerns whether it fits human expectations. Clinical relevance concerns whether the information described can support the particular clinical claim.

These properties are independent. A plausible account can misdescribe the computation. A faithful account can reveal an inappropriate cue. Even a faithful account of relevant image information does not establish that the diagnosis is correct or that using the system improves care.

The purpose of an audit is therefore to make claims more specific and better supported. A visually persuasive heatmap is not a certificate of clinical reasoning.

## Key concepts

### Begin with the clinical question

The relevant evidence changes with the task.

Stone detection concerns a luminal structure and its acoustic behavior. Characterizing mural thickening concerns wall architecture, distribution, and surrounding anatomy. Assessing possible malignancy requires a differential that includes inflammatory and benign proliferative conditions.

A model output labeled “abnormal” may collapse these questions. An explanation that highlights the gallbladder does not clarify which abnormality was recognized or what action the answer supports.

The explanation's target must also be identified. An explanation of a stone prediction is not an explanation of a malignancy prediction simply because both refer to the same organ. Likewise, a map describing image similarity is not automatically an explanation of a diagnostic decision.

### Keep the properties separate

| Property | Question it answers | What it does not establish |
|---|---|---|
| Anatomical localization | Does the display correspond to an organ or finding? | That those pixels drove the prediction |
| Human plausibility | Does the account fit a reader's expectations? | That it describes the computation |
| Computational faithfulness | Does it represent the specified aspect of model behavior? | That the information used is clinically appropriate |
| Clinical relevance | Can that information support this clinical question? | That the model actually uses it |
| Diagnostic validity | Does the prediction agree with an appropriate reference? | That the explanation is faithful |
| Clinical utility | Does use improve the relevant decision or outcome? | That a particular explanation mechanism is correct |

A successful audit cannot silently substitute one row for another. Each conclusion needs evidence suited to that conclusion.

### Why gallbladder anatomy makes simple overlap inadequate

The evidence occupies several compartments: lumen, wall, surrounding tissue, and the sound path beyond a structure.

For a suspected stone, posterior shadowing may be useful even though it lies beyond the stone boundary. For a mural lesion, the attachment and adjacent wall may matter more than the lesion center. For possible invasion, the interface with the liver matters, but an indistinct interface does not itself prove infiltration.

An organ mask can therefore be too broad for one question and too restrictive for another. A large heatmap may overlap the gallbladder almost automatically. A narrowly localized map may exclude an essential acoustic relationship.

Overlap also ignores the meaning of the highlighted appearance. The same wall region can contain physiological contraction, edema, benign remodelling, or tumor. Correct location does not establish correct interpretation.

### What wall findings can support

Inflammatory edema expands the wall and can alter its layered appearance. Systemic fluid disturbances can produce a similar broad finding without primary gallbladder inflammation.

Adenomyomatosis can produce muscle thickening and intramural sinuses. When resolved, the relationship between cystic spaces, wall location, and characteristic reverberation supports a benign structural explanation.

Neoplastic tissue can disturb architecture and extend beyond expected boundaries. However, early lesions can be subtle, while severe inflammation can appear irregular or infiltrative.

These mechanisms explain why “the model attended to the thick wall” is an incomplete clinical account. The broad finding does not settle the differential. More specific morphology may be helpful, but only if it is depicted and assessed adequately.

### Assessability precedes a claim about visible evidence

A still image does not contain the full examination.

| Clinical factor | Evidence needed to assess it | Limitation of a selected still |
|---|---|---|
| Wall architecture | Adequate resolution, orientation, and visible interfaces | Missing detail can resemble loss of layering. |
| Lesion attachment | Depiction of the relevant lesion–wall interface | A partial view cannot establish the entire attachment. |
| Mobility | Temporal or positional observation | Appearance at one position does not demonstrate movement. |
| Vascularity | Suitable Doppler acquisition and interpretable signal | An uninformative acquisition cannot establish absent flow. |
| Sonographic tenderness | Patient response during examination | It is not a B-mode pixel finding. |
| Extent of disease | Appropriate coverage and sometimes other modalities | A local frame cannot establish whole-patient stage. |

“Not assessable” should remain distinct from “absent.” A confident model answer does not change what was acquired.

There is a further distinction between reader uncertainty and physical absence of information. A model could use subtle measured information that a reader does not readily recognize. That possibility does not justify naming an unseen anatomical feature as its evidence without support.

### Four possible relationships between explanation and expectation

The following are conceptual examples, not observations from a particular system.

| Faithful? | Plausible? | Gallbladder example |
|---|---|---|
| Yes | Yes | A task-relevant explanation correctly describes use of a depicted finding that a reader also considers relevant. |
| Yes | No | An explanation correctly reveals use of an acquisition pattern that the reader does not regard as disease evidence. |
| No | Yes | A familiar-looking wall highlight is shown although the prediction is determined by unrelated information. |
| No | No | The displayed account neither matches the computation nor supplies a clinically sensible explanation. |

The unfaithful but plausible case is particularly deceptive: it can make an inadequately justified prediction look clinically reasoned. The faithful but implausible case is diagnostically useful for auditing because it may reveal a problem rather than conceal it.

Neither statement implies that every unusual explanation is wrong. Human expectations are also incomplete, and a surprising pattern requires investigation rather than automatic rejection.

### What published sanity checks establish

Published saliency work has shown why visual appeal is insufficient. Adebayo and colleagues examined whether explanations respond appropriately when learned model information is changed or destroyed.

If an explanation presented as a description of learned prediction remains largely unchanged despite removal of that learned information, its visual structure may arise from image edges or architectural properties. That weakens the claimed interpretation.

Passing such a check is more limited. It shows that the explanation responds to the tested changes; it does not prove clinical relevance, complete representation of the computation, or correctness on every case.

The result also depends on which part of the model is changed and how explanation similarity is judged. These checks are evidence about a particular explanation property, not a universal ranking of explanation methods.

### What generic perturbation checks establish

Perturbation-based explanation tests ask whether modifying information designated as important affects behavior in a way consistent with the explanation. They examine a specified relationship between an explanation and behavior under those modifications.

The interpretation rests on assumptions:

- The modification actually concerns the purported information.
- It does not unintentionally destroy other relevant evidence.
- The resulting input remains meaningful for the question.
- The model's behavior on modified inputs is relevant to the intended claim.
- The explanation is being judged at a scale appropriate to its definition.

Gallbladder ultrasound makes these assumptions substantive. Altering a bright focus can also alter its posterior acoustic context. Removing surrounding tissue can eliminate the reference needed to judge echogenicity or the interface needed to assess attachment.

A response to an unrealistic input is still model behavior. It is not automatically evidence about the corresponding clinical disease process. Image manipulation is not the same thing as changing a patient's pathology.

### Why a small response does not settle importance

Models can use redundant information. A stone may be recognizable through more than one depicted feature; changing one feature need not abolish the prediction.

Features can also interact. A bright focus is interpreted differently depending on whether it is luminal, intramural, or outside the gallbladder. The meaning of the focus cannot always be assigned independently of its location and surrounding anatomy.

Thus neither a large nor a small response to a generic modification, considered alone, supplies a complete account of clinical reasoning. The evidence remains conditional on what was modified, what remained, and which behavior the explanation claims to describe.

This is a limitation of interpretation, not a reason to abandon behavioral checks.

### What independent clinical annotation contributes

Clinical annotation can describe whether a particular finding is depicted and how certain that assessment is. To serve as a separate reference, it should not be constructed by following the explanation being evaluated.

A wall-architecture annotation and a final diagnosis answer different questions. Knowledge of the diagnosis can help a reader interpret an examination, but it can also encourage labeling an expected feature that is not actually resolved. The information available to the reader therefore affects the meaning of the annotation.

Disagreement may reflect vocabulary, viewing conditions, subtle morphology, or insufficient acquisition. Adjudication produces a documented judgment; it does not turn uncertain image evidence into microscopic truth.

Agreement between an explanation and such annotations supports an alignment claim at the defined level. It does not identify all information used by the diagnostic model.

### A heatmap is a display with choices

An attribution map is converted into a visual object through scaling, thresholding, interpolation, and color mapping. These choices can change its apparent extent and contrast.

A map normalized separately for each image can make weak and strong underlying signals look similarly vivid. A coarse attribution grid can appear anatomically precise after smooth interpolation. A display that suppresses sign can obscure whether information supports or opposes the explained prediction.

Accordingly, “bright red over the lesion” is not a self-contained scientific statement. Interpretation requires the explanation definition and the display convention. Clinical readers should not be asked to infer computational meaning from color alone.

### Reference standards answer different parts of the audit

Histopathology can establish the nature of sampled tissue. It does not directly validate every explanation pixel, nor show that every stored frame depicts the histological finding.

An expert image annotation provides a reference for visible morphology. It may be uncertain or incomplete and can depend on the views supplied.

A clinical diagnosis may incorporate symptoms, laboratory evidence, other imaging, and follow-up. An explanation confined to a selected image cannot account for information that the model never received.

A management decision incorporates risk tolerance, patient factors, and available care. Agreement with that decision is not equivalent to agreement with pathology.

The audit should therefore state whether its reference concerns diagnosis, image evidence, or clinical action. These references are complementary rather than interchangeable.

### Worked reasoning: a reassuring-looking explanation

Imagine a hypothetical model that calls a case concerning and displays a smooth heatmap over a thickened wall.

The image clearly depicts thickening, but the finer mural architecture is unresolved. The clinical record later identifies a benign inflammatory process.

Several conclusions can be separated.

**Localization:** the map corresponds to the wall.

**Clinical plausibility:** wall assessment is relevant, but thickening is not specific for malignancy.

**Faithfulness:** the appearance of the map alone does not show whether it reflects the prediction process.

**Diagnostic error:** the concerning prediction disagrees with the selected benign reference, assuming that reference appropriately corresponds to the case.

**Clinical consequence:** the seriousness of that disagreement depends on whether the output prompts further characterization, urgent referral, or an inappropriate definitive conclusion.

The case does not justify calling the heatmap wholly meaningless or calling the prediction clinically sound. It shows why the conclusions must be stated separately.

### Audit findings should describe failure types

A useful account distinguishes failures of target definition, image assessability, feature recognition, explanation behavior, reference construction, and clinical interpretation.

A correct prediction with an unsupported explanation remains an explanation problem. A faithful explanation of an incorrect prediction can still help identify a model limitation. An unassessable finding is not automatically a failure of feature recognition.

False reassurance can delay appropriate assessment. A plausible explanation can intensify that reassurance by giving the answer an appearance of anatomical justification. Conversely, an explanation that exaggerates nonspecific wall changes can amplify over-referral.

An audit is clinically informative when it makes these failure modes visible without claiming that one summary score certifies the system.

### Revision checklist

| Question | Answer to retain |
|---|---|
| Is plausibility the same as faithfulness? | No; one concerns expectation, the other the computation. |
| Does anatomical overlap show model use? | No; it establishes a spatial relationship. |
| Can useful evidence lie outside a lesion mask? | Yes; posterior acoustics and adjacent interfaces may matter. |
| Can a still frame establish mobility or tenderness? | No; those require different observations. |
| What do sanity checks provide? | Evidence about dependence on learned information under specified tests. |
| What do perturbation checks provide? | Conditional evidence about behavior under particular modifications. |
| Why can an unchanged prediction be ambiguous? | Redundancy, interactions, and inappropriate modifications remain possible. |
| Does pathology validate a heatmap? | No; tissue diagnosis and explanation validity are different references. |
| Which failure is especially deceptive? | A plausible account that does not describe the computation. |

## Why it matters for my work

The ontology separates Faithfulness from Clinical evidence reliance. A faithful explanation can describe inappropriate information, and a clinically sensible explanation can misdescribe the model. Clinical assessability limits what an image-based account can claim; ClinicalTarget → setsRequirementsFor → Method/Metric prevents a generic saliency score from standing in for the clinical question.

## What I have not resolved

- Which clinical factors have sufficiently clear image-level definitions for meaningful assessment?
- Which disagreements arise from the model, the explanation, the reference, or limited acquisition?
- How can audit conclusions communicate those distinctions without implying more certainty than the evidence supports?

---

Sources: Established explanation-audit concepts from Adebayo and colleagues on saliency sanity checks and Liu and colleagues on medical algorithmic auditing, together with general gallbladder ultrasound teaching. The cases are conceptual illustrations, and no universal faithfulness guarantee is claimed. These are study notes for research purposes, not clinical guidance.
