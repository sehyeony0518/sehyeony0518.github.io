---
layout: study_note
title: "Gastric Cancer"
description: "Endoscopic detection, screening programs, and reader variability in a real-time diagnostic setting."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "oncology"
category_title: "Oncology"
subgroup: "Detection & Screening"
order: 2
source: "Lecture"
written: true
updated: "2026-09-08"
---

## Core question and definition

What can an endoscopic image reveal about gastric cancer, and what remains unknown until tissue sampling, staging or follow-up?

Gastric cancer usually refers to adenocarcinoma arising from the stomach’s epithelial lining. Other malignant processes can involve the stomach, so “gastric lesion” and “gastric adenocarcinoma” are not interchangeable labels.

Endoscopy observes the mucosal surface. Histology examines sampled tissue. Endoscopic ultrasound and cross-sectional imaging assess different aspects of depth and extent.

The diagnostic process therefore crosses several observation scales:

| Task | Main object being assessed |
| --- | --- |
| Examination quality | Whether relevant mucosa was adequately exposed and recorded |
| Lesion detection | Whether an abnormal area was brought to attention |
| Optical characterisation | Whether visible morphology supports a particular interpretation |
| Tissue diagnosis | What the sampled cells and tissue establish |
| Depth and extent assessment | How far disease may extend through the wall or beyond it |
| Treatment planning | Whether a particular intervention is appropriate in the full clinical context |

A model operating on a selected still image begins after someone has already exposed, recognised and often centred the lesion. It has not demonstrated the ability to find that lesion during an uninterrupted examination.

Similarly, a model estimating histology from surface appearance has not directly observed every microscopic feature that determines treatment.

The core question is: **which consequences of the disease process reach the visible surface, under what acquisition conditions, and with what diagnostic specificity?**

## Key concepts

### The stomach wall explains the difference between surface detection and depth

The stomach’s inner mucosa contains epithelium, glands and supporting tissue. Beneath it lie the submucosa, muscular layers and outer covering.

An ordinary endoscopic image records reflected light from the exposed surface. It can show colour, relief, ulcers, folds and visible vascular or glandular patterns. It does not directly display all deeper wall layers.

This matters because depth of invasion changes the clinical problem. Extension into deeper layers can increase concern about spread through lymphatic and other pathways.

**Early gastric cancer is defined by confinement to the mucosa or submucosa, regardless of lymph-node status.** The word “early” is therefore a depth-based classification, not a guarantee of absent nodal disease or a synonym for every favourable treatment category.

A lesion that looks small on the surface may extend more deeply than expected. Conversely, a broad superficial lesion may have a different pattern of risk from a compact deeply invasive one.

The image, histological depth and overall stage must remain separate labels.

For AI, a surface crop cannot be treated as a complete observation of a wall or nodal state merely because those states were later recorded for the patient.

### Chronic injury can create a background in which cancer develops

Chronic Helicobacter pylori infection is an established contributor to gastric carcinogenesis, particularly in relevant noncardia disease pathways.

Persistent inflammation can be associated with loss of normal glands, atrophic change and intestinal metaplasia. Intestinal metaplasia means replacement by an epithelial phenotype resembling intestinal tissue; it is not itself the same diagnosis as invasive cancer.

Dysplasia describes neoplastic epithelial abnormality with disturbed cellular and architectural organisation. Progression to invasive disease introduces a further distinction: tumour cells extend beyond their original epithelial compartment into surrounding tissue.

This sequence is an important organising pathway, but not every infected person develops cancer and not every gastric cancer follows an identical route.

Other biological and inherited factors also contribute. The clinical history therefore informs risk without replacing examination of a particular lesion.

For imaging research, background atrophy or metaplasia can be legitimate information about patient risk. It does not establish that a specific focal abnormality is malignant.

A model that recognises a high-risk mucosal background may be useful for risk stratification while still failing at the separate task of local cancer detection.

### Why epithelial disorganisation changes the visible surface

Normal mucosa has an organised surface architecture supplied by a corresponding vascular network.

Neoplastic growth can disturb gland arrangement, surface relief and microvascular organisation. These changes can produce a focal alteration in colour, an irregular surface, an elevation or depression, or a boundary between the lesion and surrounding mucosa.

Ulceration removes or disrupts the surface. Bleeding, exudate and tissue repair can then obscure the underlying architecture.

The causal chain is useful but not specific:

- Neoplasia can disrupt surface organisation.
- Inflammation and repair can also disrupt surface organisation.
- Both can alter vascular prominence and colour.
- The acquisition may enhance, obscure or distort the difference.

A red or depressed area is therefore a finding, not a histological diagnosis.

The clinician examines the complete pattern and compares the suspicious area with its surroundings. The question is whether the combination, persistence and context support neoplasia more strongly than alternatives.

For AI, visual saliency within an abnormal area is only an initial plausibility check. It does not establish that the model interpreted the discriminating structure rather than a nonspecific colour change.

### Infiltrative growth can be extensive beneath an unimpressive surface

Some gastric adenocarcinomas grow as poorly cohesive cells infiltrating the wall rather than forming a sharply defined protruding mass.

Infiltration and the associated tissue response can thicken and stiffen the wall. Distensibility may decrease, and folds may become abnormal.

This helps explain why the apparent surface lesion can underestimate the extent of disease. The camera mainly observes the mucosa and the stomach’s behaviour during insufflation and movement. It does not directly inspect the full infiltrated wall.

A limited superficial biopsy can also miss relevant deeper disease if the sampled material does not represent the process.

The reasoning is therefore different from identifying a clearly demarcated mucosal tumour. A negative or uninformative superficial sample must be interpreted alongside the examination and other evidence.

For a learning system, the lesson is not that every subtle fold abnormality implies infiltrative cancer. It is that absence of a conspicuous surface mass is not equivalent to absence of clinically important disease.

### Symptoms and examination indication change the prior

Early disease can produce few specific symptoms. Other patients undergo investigation because of bleeding, anaemia, weight loss or persistent upper gastrointestinal complaints.

Those symptoms have competing explanations, but they change why the examination is being performed and what must be resolved.

A population screening examination differs from investigation of an already suspicious lesion. Surveillance after a previous gastric neoplasm differs again.

Their prevalence, lesion spectrum and available prior information can vary. A model developed from selected resection cases should not be assumed to retain its probability calibration in routine screening.

The background mucosa and clinical history also matter. Prior treatment, documented metaplasia or a known lesion can change the assessment context.

These factors should be recorded as part of the study population and input definition. They should not enter indirectly through filenames, procedure annotations or selection of unusually clear images while remaining absent from the stated model description.

### Acquisition is an active part of diagnosis

The endoscopist changes the observation by cleaning the mucosa, adjusting distension, varying the angle, moving closer and inspecting around folds.

A lesion behind mucus or a fold may not be visible until the acquisition changes. This is not merely a classification failure on a fixed image.

Adequate examination also requires anatomical coverage. The stomach is a three-dimensional cavity whose walls and folds cannot be fully represented by a few attractive stills.

Several distinct failures are possible:

| Failure | What went wrong |
| --- | --- |
| Unseen lesion | The relevant mucosa was not adequately exposed or recorded |
| Unrecognised lesion | The abnormality was visible but did not attract attention |
| Mischaracterised lesion | The area was recognised but interpreted incorrectly |
| Inadequately sampled lesion | Tissue acquisition did not represent the relevant abnormality |
| Incorrectly mapped reference | The tissue result was assigned to the wrong location or image |

An AI system can help with some failures without solving all of them.

A detector cannot establish visual evidence from an unrecorded surface. It may prompt additional inspection from indirect cues, but that is a different capability from recognising the hidden lesion itself.

### White-light endoscopy: what colour and shape can support

White-light examination can reveal focal discoloration, depression, elevation, ulceration, irregular surface structure and abnormal fold convergence.

These appearances are affected by illumination, viewing angle, distance, mucus, blood and image processing. A colour difference must therefore be interpreted in the actual acquisition context.

Fold convergence can reflect traction and tissue alteration around a lesion, but inflammation and scarring can produce related appearances. Ulceration can accompany malignancy or benign injury.

The clinician considers the lesion’s boundaries, location, shape and relation to surrounding mucosa. They also assess whether cleaning or changing the view alters the apparent finding.

A model using a single still image loses part of this dynamic assessment. It cannot know whether an apparent pale area remained after washing unless that information is present in the input.

A well-designed dataset should distinguish stable lesion characteristics from transient obscuration and recording artefact.

### Enhanced imaging changes the information available at the surface

Narrow-band imaging alters illumination to emphasise aspects of superficial vascular and mucosal structure. Magnification can make fine patterns more assessable when focus and viewing conditions are adequate.

The resulting image does not directly become histology. It remains an optical observation whose appearance depends on tissue and acquisition.

Structured approaches such as MESDA-G examine the boundary of a suspicious area and irregularity in its microvascular or microsurface pattern.

The diagnostic logic is that a neoplastic region may have an organised difference from surrounding mucosa together with abnormal internal architecture. Neither a boundary alone nor arbitrary irregularity is an unrestricted cancer rule.

The method also addresses a lesion already brought into view. Performance in optical characterisation does not establish complete detection throughout the stomach.

A non-assessable fine pattern must not be recorded as a normal fine pattern. Poor focus, insufficient magnification or obscuring material can prevent the relevant observation.

For AI, training labels should therefore distinguish the availability of the required pattern from the final tissue diagnosis.

### The same appearance can arise from different lesions

| Differential | Why it can resemble adenocarcinoma | What helps distinguish it |
| --- | --- | --- |
| Gastritis and reactive change | Redness, surface irregularity and altered vascular appearance | Distribution, clinical context, optical assessment and appropriate tissue |
| Erosion or benign ulcer | A depression, exudate, bleeding and converging folds may be present | Complete morphology, sampling adequacy and subsequent clinical assessment |
| Adenoma or dysplasia | Neoplastic epithelial change can produce an abnormal surface | Histological assessment of grade and invasion |
| Gastric lymphoma | Wall or mucosal abnormalities can overlap with epithelial cancer | Tissue classification and assessment of extent |
| Subepithelial lesion | A bulge or ulcerated prominence may be visible | Layer of origin and representative sampling |
| Adenocarcinoma | Disrupted architecture, ulceration or infiltrative changes may occur | Integrated optical, histological and staging evidence |

A subepithelial lesion illustrates the observation boundary particularly well. The visible mucosa may be draped over an abnormality arising below it. Sampling only the surface can fail to identify the underlying lesion.

Likewise, an ulcerated lesion can yield necrotic or inflammatory material rather than representative tumour.

The differential is not resolved by declaring every abnormal surface “positive.” It requires asking what mechanism could produce the finding and which additional observation discriminates the alternatives.

### Biopsy provides a local tissue reference

A targeted biopsy samples a particular location and depth. Histology can establish whether the material contains malignancy and help classify the tissue.

The strength of the result depends on correspondence. The sample must come from the relevant lesion, and the image must represent that lesion at a meaningful time.

A patient with cancer can have many images of normal mucosa. A positive biopsy from one site does not make every image from the examination a positive lesion example.

Negative findings also require interpretation. A specific benign diagnosis in an adequate, representative sample differs from a sample containing only nonspecific inflammation or insufficient tissue.

The pathology report should retain uncertainty where present. Forcing all indeterminate or nondiagnostic samples into a benign class creates an artificial reference.

A research dataset should record the sampling site, lesion identity, adequacy and the relationship between the biopsy and subsequent specimens.

“Histology confirmed” is valuable information, but it is not a substitute for this mapping.

### Resection reveals information that surface imaging and biopsy may miss

A resection specimen can permit more complete assessment of lesion architecture, depth, margins and lymphovascular involvement.

This can revise the interpretation formed from a limited biopsy. The revision may reflect additional tissue rather than an inexplicable disagreement between observers.

Treatment planning also depends on information beyond surface appearance, including the likelihood of nodal disease and the patient’s clinical circumstances.

A lesion may be technically removable through an endoscopic approach without satisfying every requirement for that removal to constitute adequate cancer treatment.

This distinction is essential for AI claims about “resection eligibility.” Such a label can incorporate histology, depth, ulceration, extent and patient factors unavailable in a single image.

A model may estimate that label, but it must be clear which determinants are observed, which are inferred and which are missing.

A pathological reference obtained after resection is appropriate for some preoperative prediction tasks. Postoperative information must remain part of the reference rather than leaking into the model input.

### Endoscopic ultrasound and CT answer different extent questions

Endoscopic ultrasound uses acoustic information to assess the wall and nearby structures. It can contribute to questions about layers and depth.

Its interpretation can be affected by inflammation, fibrosis, lesion geometry and examination quality. It does not directly reproduce a microscopic section.

CT evaluates a wider anatomical field, including wall abnormalities, regional nodes and possible distant disease. A subtle superficial cancer may have little conspicuous CT abnormality.

Suspicious nodes on imaging are not equivalent to histologically proven metastases. Conversely, absence of enlarged or conspicuous nodes does not exclude microscopic involvement.

Other staging procedures may provide additional evidence in selected circumstances. The relevant point for a study note is that extent is assembled from several observations.

A model seeing only the mucosal surface cannot claim that it directly assessed every component of local, nodal and distant disease.

Its intended target must therefore distinguish visible morphology, estimated invasion and complete clinical stage.

### Where each label comes from

| Label | Appropriate evidence source | Main limitation |
| --- | --- | --- |
| Visible lesion | Review of the actual frame or video interval | The lesion may not be assessable throughout the examination |
| Optical suspicion | Reader interpretation using a specified modality | Depends on technique, experience and available views |
| Histological diagnosis | Adequate tissue from the corresponding lesion | Sampling and classification uncertainty |
| Pathological depth | Examination of an appropriate specimen | Often unavailable outside a selected treated group |
| Clinical stage | Integrated staging investigations | Some disease may remain microscopic or unobserved |
| Resection suitability | Defined multidisciplinary or clinical assessment | Includes information beyond image appearance |
| Missed cancer | Subsequent adjudication of an earlier examination | Requires determining whether disease was present and visible then |

These labels should not be collapsed into a generic “gastric cancer image” category.

The distinction is especially important for video. A frame may belong to a patient with cancer while displaying no lesion. Another may show only a partial boundary. Another may be diagnostically useful only when compared with preceding views.

Temporal annotation should identify when the lesion becomes visible and when it becomes adequately characterisable.

### Selected still images and real-time detection are different experiments

A still-image dataset often contains centred, cleaned and well-focused lesions. The endoscopist’s earlier recognition has already influenced the data.

A real-time detector faces movement, defocus, folds, bubbles, normal anatomical variation and changing illumination. It must help identify an abnormality before someone has selected its best view.

A classifier can therefore perform well on lesion crops while contributing little to examination-level detection.

Evaluation should include uninterrupted or appropriately sampled examinations, not only selected positive and negative stills.

The unit of success also matters. Repeatedly identifying the same obvious lesion across adjacent frames does not equal detecting multiple independent cancers. Conversely, one useful prompt during a brief adequate view may have clinical value even if many obscured frames remain negative.

Metrics need to distinguish frame-level behaviour, lesion-level detection and examination-level outcome.

False prompts should be evaluated as events and interruptions, not only as a fraction of a very large number of normal frames.

### Shortcuts can reveal what happened after recognition

Biopsy forceps, marking devices, bleeding after sampling and annotations may be associated with a suspicious lesion.

A model can exploit those cues while failing to recognise the lesion before the endoscopist did.

This is a temporal leakage problem. A system intended to assist initial detection should be evaluated on images available before lesion-directed actions.

The same issue occurs with image selection. Cancer cases may have more close-up enhanced images because the endoscopist was already concerned. Recognising the imaging mode or examination style may partly reproduce that prior decision.

These cues are not universally illegitimate. A model summarising an already completed examination may appropriately use a broader record. The problem arises when the input contains information unavailable at the claimed decision point.

The task specification must define that boundary explicitly.

### Consequences of error change across the pathway

Missing a clinically important early lesion can delay diagnosis and reduce the opportunity for appropriate treatment.

A false detection prompt can interrupt inspection and increase unnecessary sampling or repeat assessment. Its harm depends on how the clinician responds and how often the system distracts from the examination.

Mischaracterising a recognised lesion can produce inappropriate reassurance or excessive concern. Misjudging depth or suitability for local treatment can have more consequential effects than a transient false prompt.

These errors should not share an unexplained universal operating point.

For a detector, sensitivity during adequately visible intervals and the burden of false prompts are central. For a characterisation model, discrimination among plausible lesions and calibrated uncertainty matter. For treatment-support claims, the full reference and consequences of the decision are required.

A system that declines to classify an obscured surface may be behaving appropriately. However, its coverage must be reported: excluding the hardest examinations from evaluation can make clinical performance appear stronger than it is.

### Worked reasoning examples

**A lesion is hidden behind a fold in the sampled video.** Later pathology confirms cancer. The patient-level diagnosis is valid, but the sampled interval contains no direct view of the lesion. The failure concerns coverage or sampling before it concerns optical classification.

**A suspicious ulcer has an uninformative biopsy.** The sample contains inflammation and necrotic material. This is different from a representative specimen establishing a specific benign explanation. A training pipeline should not automatically convert both outcomes into the same negative label.

**A surface lesion appears suitable for limited treatment, but the resection specimen reveals additional invasion.** The later reference can establish that the earlier estimate was incomplete. It does not prove that every decisive microscopic feature was visible in the original still image.

**A classifier performs well on images containing biopsy forceps.** The result may reflect recognition of the endoscopist’s action. Testing the same model before any lesion-directed action asks whether it can support the intended earlier decision.

These hypothetical examples identify evidential boundaries rather than prescribe clinical management.

### Designing an examination-level study

A defensible study should specify:

- Screening, symptomatic investigation or surveillance setting.
- White-light, enhanced or combined imaging inputs.
- Whether the task is detection, characterisation, depth estimation or decision support.
- Lesion and patient correspondence with pathology.
- The interval during which a lesion is visible and assessable.
- Whether images precede biopsy, marking or other lesion-directed actions.
- How multiple lesions and repeated examinations are grouped.
- How uninformative samples and unresolved outcomes are represented.

Patient-level separation is necessary because adjacent frames and repeat examinations can be highly similar.

External evaluation should include different equipment, examination practices, lesion spectra and reference processes. A model may survive a device change while failing in a population with more inflammation or less selected lesions.

Clinical evaluation should examine whether prompts lead to useful additional inspection, whether missed lesions decrease and whether unnecessary procedures or distraction increase.

A technically accurate frame classifier becomes clinically useful only through this interaction with the examination.

### Revision checklist

| Question | What I should be able to explain |
| --- | --- |
| What does ordinary endoscopy observe? | The exposed mucosal surface and its appearance during examination |
| Why does wall anatomy matter? | Surface appearance does not directly measure depth or nodal involvement |
| What defines early gastric cancer? | Confinement to mucosa or submucosa, regardless of nodal status |
| Why can chronic inflammation matter? | It can contribute to a carcinogenic background without making every lesion malignant |
| Why is surface irregularity nonspecific? | Neoplasia, inflammation and repair can overlap |
| Why can infiltrative disease be underestimated? | Important disease may extend beneath a relatively unimpressive surface |
| What does enhanced imaging add? | Assessability of specified superficial patterns |
| Why is optical characterisation not complete detection? | The lesion must first be exposed and brought into view |
| What limits a biopsy label? | Site, depth, adequacy and lesion correspondence |
| Why does resection sometimes revise the diagnosis? | It supplies more complete tissue information |
| Why are adjacent frames not independent examples? | They share the same lesion, patient and acquisition episode |
| What makes an alert useful? | It improves appropriate inspection or action without excessive burden |

### Connecting the clinical reasoning to the ontology

Neoplastic growth can manifest as surface disorganisation, ulceration or wall changes, but competing mechanisms can produce similar findings.

`Malignancy & staging` `setsRequirementsFor` `Reference standard adjudication`: a tissue result must be linked to the correct lesion, depth question and examination time.

`Clinical assessability` limits `Clinical evidence reliance`. A model cannot establish reliance on a microvascular pattern that its input never resolved. It may make an indirect prediction, but that is a different claim.

Finally, acquisition and human action form part of the system. Improved image classification does not establish `Clinical utility` without evidence about examination coverage, recognition, sampling and downstream care.

## Why it matters for my work

Gastric endoscopy makes acquisition an active component of diagnosis. In my own imaging studies, I need to distinguish findings that were never exposed from findings that were visible but misinterpreted, and keep both separate from failures of tissue reference or lesion correspondence.

## What I have not resolved

- How should a dataset represent the interval between first visibility and sufficient visibility for characterisation?
- What is the best reference for lesions with persistent suspicion but incomplete tissue confirmation?
- How can a prospective audit measure useful prompts while detecting distraction and unnecessary sampling?

---

Sources: Existing lecture notes; National Cancer Institute resources on stomach cancer, diagnosis, prevention and treatment; National Institute of Diabetes and Digestive and Kidney Diseases resources on gastritis and gastropathy; Muto and colleagues, Magnifying endoscopy simple diagnostic algorithm for early gastric cancer (MESDA-G), and the associated vessel-and-surface interpretation framework. The hypothetical examples and AI study-design deductions are explanatory applications. These are study notes for research purposes and are not clinical guidance.
