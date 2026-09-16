---
layout: study_note
title: "Head and Neck Cancer"
description: "Multimodal staging and the coordination problem between imaging, pathology, and treatment planning."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "oncology"
category_title: "Oncology"
subgroup: "Staging & Treatment Planning"
order: 3
source: "Lecture"
written: true
updated: "2026-09-08"
---

Head and neck cancer occupies an anatomically dense region in which a small extension can change the functional and treatment problem. This note focuses on mucosal squamous cell carcinoma, with particular attention to biological classification, staging, and the meaning of a segmentation boundary.

## Core question and definition

A model may be asked to detect a primary tumor, identify involved lymph nodes, predict invasion, assign stage, or draw treatment-planning contours. These outputs require different reference standards.

A tumor contour is also not a single universal object. A visible tumor boundary, a region at risk of microscopic disease, and a planning margin for geometric uncertainty have different meanings.

The clinical problem is to reconcile:

- The primary anatomical site.
- Histological diagnosis.
- Relevant biological classification.
- Local, nodal, and distant extent.
- Function, including swallowing, speech, and airway protection.
- The observations available before or after treatment.

A correct label or contour must retain this context.

## Key concepts

### Site determines anatomy, spread, and the meaning of the label

The oral cavity and oropharynx are adjacent but distinct. The mobile oral tongue and the tongue base do not belong to the same clinical compartment. The tonsillar region, larynx, and hypopharynx also have different anatomical relationships and presenting problems.

A superficial oral lesion can be accessible to inspection and palpation. A primary within tonsillar tissue or a deeper pharyngeal region can be less conspicuous. A laryngeal lesion may affect voice or vocal-fold movement. A cervical lymph node can be the most evident abnormality even when the primary is small or difficult to identify.

The site also changes:

- The tissue planes available for local extension.
- Regional lymphatic drainage.
- The structures whose invasion matters.
- The appropriate pathological and staging framework.
- The functional consequences of treatment.

A generic “head and neck cancer” class can therefore combine biologically and anatomically different tasks.

Salivary tumors, thyroid malignancies, lymphoma, and other nonmucosal tumors require their own frameworks. They should not inherit assumptions developed for mucosal squamous cell carcinoma solely because they appear in the same image volume.

### From epithelial malignancy to an observable lesion

Squamous cell carcinoma arises from epithelial cells that acquire abnormal growth and invasive behavior.

Disruption of the mucosal surface can produce ulceration or an irregular visible lesion. Invasion into underlying tissue can produce induration, distortion, and loss of normal tissue relationships. Associated vascular and inflammatory changes contribute to enhancement and swelling.

These appearances are not specific to malignancy. Infection and inflammation can also produce mucosal thickening, enhancement, and tissue edema. The diagnostic meaning comes from the pattern, persistence, anatomical context, and tissue assessment.

Once a tumor invades beyond the mucosa, the direction of spread becomes consequential. Extension into a deep compartment can alter resectability or treatment volume even if the visible surface component changes little.

This explains why a model that measures only maximum diameter may omit the feature that changes the clinical decision.

### Routes of spread explain the imaging search

**Direct extension.** Tumor can cross local tissue planes and involve muscle, cartilage, bone, or adjacent spaces. Contact with a structure is not automatically invasion of that structure.

**Lymphatic spread.** Tumor cells can reach regional cervical nodes. The primary site and involved pathways influence which nodal regions require assessment. Nodal size alone does not establish or exclude involvement.

**Perineural spread.** Tumor can extend along nerves beyond the most obvious mass. Changes in nerve appearance, enhancement, or associated foramina may support suspicion, but microscopic involvement can remain below imaging resolution.

**Distant spread.** Disease outside the head and neck changes the staging and treatment problem. A local image cannot establish the absence of distant disease outside its coverage.

**Extranodal extension.** Tumor can extend beyond an involved lymph node into surrounding tissue. Imaging can suggest this through altered margins and adjacent tissue changes, but microscopic confirmation and imaging suspicion are not identical labels.

The search is therefore organized around pathways and interfaces, rather than simply around a bright or enlarged region.

### HPV-associated oropharyngeal disease is a specific biological context

High-risk HPV-associated oropharyngeal squamous cell carcinoma has a different etiological basis from HPV-independent disease.

Viral oncogenic activity disrupts cell-cycle and tumor-suppressor pathways, including pathways involving p53 and the retinoblastoma protein. This differs from treating HPV status as merely another demographic predictor.

HPV-associated oropharyngeal disease also has a distinct prognostic context. Outcomes differ on average from HPV-independent disease, but status does not determine an individual's outcome independently of extent, other exposures, comorbidity, and treatment.

The anatomical qualification is essential. The interpretation used for an oropharyngeal squamous cell carcinoma cannot automatically be transferred to every oral, laryngeal, salivary, or other head and neck tumor.

p16 immunohistochemistry is used as a surrogate marker in appropriate pathological settings. It measures protein expression, not viral nucleic acid directly. The relationship between a p16 result and HPV-associated disease depends on the site, specimen, assay, and testing framework.

The record should preserve:

- The anatomical site.
- The specimen and whether it represents a primary or a metastasis.
- The actual test performed.
- The original result and interpretation.
- Any discordance between surrogate and HPV-specific testing.

An imaging model may estimate the probability of a biomarker classification from associated appearances. That does not establish that it has measured the biomarker itself.

### What each modality can reveal

| Observation or modality | Main contribution | Important limit |
|---|---|---|
| Inspection and palpation | Surface abnormality, ulceration, induration, accessible extent | Deep or obscured disease may remain unassessed |
| Flexible endoscopy | Mucosal assessment and selected functional observations, including movement | Surface visualization does not reveal all deep or microscopic extension |
| Ultrasound | Accessible neck nodes and guidance for sampling | Air, bone, depth, and coverage limit assessment of many primary sites |
| Contrast-enhanced CT | Local anatomy, nodes, cortical bone changes, and selected invasion findings | Dental artifacts, contrast timing, and overlapping inflammation can obscure boundaries |
| MRI | Soft-tissue relationships, marrow abnormalities, and perineural assessment | Motion, distortion, and nonspecific edema can complicate interpretation |
| FDG-PET/CT | Metabolic information, selected occult-primary searches, regional and distant assessment | Uptake is not cancer-specific; small or less conspicuous disease can remain undetected |
| Histopathology | Cellular diagnosis and sampled invasion or margin information | The specimen represents selected tissue, not automatically the complete in-vivo extent |

Modality choice follows the question. A negative surface examination does not resolve a deep-space question. A CT-visible node does not establish its histology. A metabolically active region can represent inflammation or physiological activity.

Combining modalities can improve assessment, but it also introduces registration and timing problems. The tongue, pharynx, and larynx can change position. A contour transferred between acquisitions is an anatomical hypothesis that needs checking, not a guaranteed correspondence.

### Why tumor boundaries are uncertain

A boundary can be uncertain for several different reasons.

**Biological transition.** Microscopic infiltration can extend beyond a conspicuous mass. There may be no sharp image-visible edge corresponding to the outermost malignant cell.

**Reactive change.** Edema and inflammation can extend beyond the tumor and resemble involvement.

**Measurement limitations.** Partial-volume effects, dental artifacts, motion, and contrast differences can change apparent margins.

**Different evidence.** One reader may have endoscopic or pathological information that another does not.

**Different contour purpose.** A diagnostic lesion outline and a treatment volume may intentionally include different tissue.

These sources of disagreement should not all be labeled annotation noise. Some represent missing information, some represent uncertain biology, and some represent different clinical objects.

For AI, the annotation protocol must state what boundary the annotator was asked to draw and which evidence was available.

### Segmentation is sometimes the clinical product

In radiotherapy planning, a contour can influence which tissue is treated and which tissue is spared. Its clinical meaning must therefore be explicit.

| Contour | What it represents | What it does not represent |
|---|---|---|
| Gross tumor volume | Macroscopic disease established from the relevant clinical and imaging evidence | Every microscopic malignant cell |
| Clinical target volume | Tissue intended to cover known disease and relevant risk of microscopic spread | A boundary that must be directly visible in image intensity |
| Planning target volume | A geometric planning construct addressing uncertainties such as positioning and motion | Additional biological tumor inferred solely from the larger volume |
| Organ at risk | A normal structure whose exposure matters for treatment planning | A generic background region interchangeable with all other normal tissue |

After surgery, a clinical target can include a tumor bed and tissue at risk even when no macroscopic tumor remains. A model should not interpret the absence of a visible mass as proof that no target volume is required.

Clinical target volumes can encode knowledge of routes of spread and treatment intent. They are not simply enlarged lesion segmentations with one universally correct margin.

Planning volumes also incorporate the treatment and positioning process. Learning them from an archive can reproduce local planning practice as well as anatomy.

### Why overlap alone cannot validate a clinical contour

A volume-overlap metric treats equally sized errors alike regardless of their location.

Let the reference region be $$R$$. Consider predictions that omit a region $$A$$ entirely within $$R$$:

$$
P=R\setminus A.
$$

If the omitted volume is $$a=|A|$$, then

$$
|P|=|R|-a,
$$

and

$$
|P\cap R|=|R|-a.
$$

The Dice coefficient is therefore

$$
\operatorname{Dice}(P,R)
=
\frac{2(|R|-a)}{2|R|-a}.
$$

This expression depends on the omitted volume, not its location.

Two omissions of equal volume can receive identical Dice values even if one misses a clinically consequential extension and the other differs at a less consequential interface.

The same problem applies to normal structures. A small boundary error near a critical structure can matter despite good overall overlap.

Evaluation can therefore include:

- Boundary errors at relevant interfaces.
- Missed extensions or nodal regions.
- Disconnected or anatomically implausible contours.
- Effects on an appropriately reviewed treatment plan.
- Expert corrections and their clinical significance.
- Performance across acquisition conditions and treatment states.

A favorable overlap score does not by itself establish that a contour is usable for its intended clinical purpose.

### Staging is a structured clinical abstraction

Stage summarizes disease using a defined classification system. It is a model of clinically relevant extent and, in some settings, prognostic grouping.

Here “model” means a rule-based abstraction. It does not necessarily mean a fitted machine-learning predictor.

Schematically,

$$
\text{stage}
=
h(
\text{site},
\text{local extent},
\text{regional nodes},
\text{distant spread},
\text{relevant biology};
\text{classification rules}
).
$$

The classification rules include the applicable system and version. The underlying observations must also retain whether they came from clinical assessment, imaging, biopsy, or resection.

The same broad stage label is not automatically comparable across sites or biological subtypes. A change in classification rules can also change a stage label without changing the patient's anatomy.

This creates several distinct AI tasks:

- Extracting the documented stage.
- Reproducing a stage from known component variables.
- Predicting a stage from incomplete pre-treatment information.
- Estimating an individual component, such as invasion or nodal involvement.
- Predicting an outcome beyond what stage summarizes.

They should not share an undifferentiated claim of “staging accuracy.”

### Clinical and pathological stage are different evidence states

Clinical stage integrates the information available through examination, imaging, and appropriate sampling before treatment.

Pathological stage uses information from resected tissue when that information is available. It can reveal microscopic features that were not visible before surgery.

Post-treatment assessment introduces another state: therapy can change the tumor, tissue architecture, and appearance. The treated specimen or image is not a direct replacement for the original untreated disease record.

A model may legitimately predict later pathological findings from earlier imaging. Its claim is then prediction of a tissue-established outcome. It should not claim that every predicted feature was directly visible.

Surgical selection also matters. Patients with resection-based labels can differ from patients managed without surgery. A pathology-only dataset may therefore test a restricted clinical population.

The reference should retain the component findings, evidence basis, timing, and uncertainty, rather than only a final stage category.

### Histology is strong evidence with a sampling boundary

Biopsy establishes the diagnosis in the sampled tissue. An adequate sample can distinguish squamous carcinoma from lymphoma, salivary disease, inflammatory conditions, and other alternatives.

A nodal sample does not automatically establish the precise primary site. Cystic or necrotic material may also be less informative than representative viable tissue.

Resection provides more extensive information about invasion and margins, but correspondence to preoperative images is not trivial. Orientation, deformation, tissue processing, and specimen sampling affect spatial comparison.

An expert image contour is consequently not equivalent to a voxel-by-voxel map of all malignant cells established by pathology.

The strongest reference for a particular task may combine clinical examination, imaging, pathology, and multidisciplinary adjudication. That combination should be documented so the model's input is not confused with the richer evidence used to establish its label.

### Worked reasoning: a neck mass can lead to a hidden primary

Consider an adult with a persistent cervical mass. Imaging shows a cystic or necrotic nodal abnormality, while the primary mucosal lesion is not obvious.

A cystic appearance does not establish a benign cyst. The differential includes metastatic disease as well as benign and inflammatory explanations.

Clinical reasoning connects several observations:

1. The location and morphology of the node help define the search.
2. Examination and endoscopy assess relevant mucosal sites.
3. Representative tissue establishes what the nodal process is.
4. Biomarker results are interpreted in the specimen and anatomical context.
5. Additional imaging addresses local, regional, or distant uncertainties.

A model that predicts an oropharyngeal origin from the nodal appearance may exploit a real association. It has not replaced tissue classification or demonstrated the precise primary boundary.

A patient-level positive label also should not be copied indiscriminately to every neck structure or image slice.

### Differential diagnosis changes after treatment

Before treatment, infection, inflammatory lesions, benign masses, lymphoma, and other malignancies can resemble mucosal carcinoma or nodal metastasis.

After treatment, edema, mucosal inflammation, fibrosis, altered anatomy, and tissue injury become important alternatives to residual or recurrent tumor.

Enhancement and FDG uptake can persist in nonmalignant tissue because inflammation and repair also alter vascularity and metabolism. A post-treatment abnormality must therefore be interpreted with treatment timing, the previous tumor distribution, serial change, symptoms, and other evidence.

A negative or equivocal sample may also have a sampling limitation. Conversely, an alarming image appearance is not sufficient to establish recurrence.

An AI model trained on untreated tumors should not be assumed to recognize recurrence reliably. The biological and measurement processes generating the images have changed.

### Error consequences depend on the structure and intended use

Underestimating disease extent can omit involved tissue from a treatment target, misrepresent resectability, or fail to identify a consequential extension.

Overestimating extent can expose additional normal tissue, impair function, or support an unnecessarily extensive plan.

Errors in organs at risk have their own consequences. Undercontouring can misrepresent the exposure of sensitive tissue. Overcontouring can unnecessarily constrain a plan and affect target coverage.

A staging error can also propagate through planning even when a tumor mask looks plausible. Misclassifying the site or biological context can make the stage category itself inappropriate.

The relevant error analysis should distinguish:

- Missed macroscopic disease.
- Uncertain microscopic-risk coverage.
- Incorrect normal-structure boundaries.
- Wrong biological or anatomical classification.
- Incorrect use of a staging framework.
- Errors caused by registration or treatment-related change.

Tumor control, speech, swallowing, airway function, and other outcomes cannot be represented adequately by one undifferentiated segmentation score.

### Revision checklist

| Question | What I should be able to explain |
|---|---|
| Which disease is included? | The primary site and histological scope |
| Why does direction of extension matter? | Dense anatomical relationships can change function and treatment |
| What are the routes of spread? | Direct, lymphatic, perineural, and distant extension |
| Where does HPV status have its stated meaning? | The relevant oropharyngeal and specimen context |
| What does p16 measure? | A surrogate protein-expression marker interpreted under appropriate conditions |
| What does each modality contribute? | Surface, functional, anatomical, metabolic, or sampled tissue evidence |
| Why are boundaries uncertain? | Biology, reactive change, measurement, available evidence, and contour purpose |
| What is the segmentation target? | Gross disease, microscopic-risk tissue, planning geometry, or an organ at risk |
| Why is Dice insufficient? | Equal-volume errors can have different clinical consequences |
| What is stage? | A classification derived from specified components and rules |
| Why distinguish clinical and pathological stage? | They use different evidence and may describe different treatment states |
| What is the reference standard's limit? | Sampling, selection, timing, correspondence, and adjudication uncertainty |

## Why it matters for my work

Head and neck cancer makes the ontology's Malignancy & staging target impose concrete requirements on segmentation, reference adjudication, and evaluation. Clinical assessability limits claims about microscopic extension, while treatment contours may intentionally include tissue whose risk is inferred from clinical knowledge rather than directly visible.

## What I have not resolved

- How can contour uncertainty be represented without hiding clinically consequential boundary disagreements?
- How should a model separate image-visible extent from the additional knowledge used to define microscopic-risk and planning volumes?

---

Sources: NCI material on oropharyngeal cancer; CAP guidance on HPV testing in head and neck carcinomas; IAEA teaching material on radiotherapy volume definitions. The overlap example is a symbolic construction illustrating metric limitations. These are study notes for research purposes, not clinical guidance.
