---
layout: study_note
title: "Dermatologic Disease"
description: "Visual diagnosis, dataset bias across skin tones, and the failure modes this field has documented most thoroughly."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "clinical-foundations"
category_title: "Clinical Foundations & Systemic Disease"
subgroup: "Immune & Skin Disease"
order: 6
source: "Lecture"
written: true
updated: "2026-09-08"
papers:
  - "2026-08-16-stress-testing-clinic-readiness-dermatology"
  - "2026-07-28-auditing-inference-processes-generative-counterfactuals"
  - "2026-08-30-monet-transparent-medical-image-ai"
---

Dermatologic diagnosis connects visible morphology to a process in the skin, using distribution, symptoms, palpation, and change over time. A photograph can preserve useful evidence while omitting the information that distinguishes two otherwise similar conditions.

## Core question and definition

Skin disease includes inflammatory, infectious, autoimmune, vascular, and neoplastic processes. This note focuses on inflammatory eruptions and suspicious skin lesions because they expose different limits of image-based diagnosis.

A model may be asked to:

- Describe a visible finding.
- Classify a lesion or eruption.
- Identify cases requiring assessment.
- Estimate severity or change.
- Predict a biopsy result.
- Support a management decision.

These targets have different reference standards. Histology is central for many suspected malignancies, while clinical assessment, targeted testing, or longitudinal follow-up may be more appropriate for other conditions.

The acquisition setting also changes the problem. Specialist photography, dermoscopy, and a phone image taken at home are different measurements collected from differently selected populations.

## Key concepts

### The skin layer and mechanism explain the morphology

The epidermis, dermis, appendages, and subcutaneous tissue produce different observable patterns when affected.

**Epidermal disturbance can produce scale.** Altered maturation and shedding of superficial cells create visible flakes or thickened keratin. Scale is therefore a description of a surface process, not a diagnosis. Inflammatory disease, infection, and some tumors can all produce it.

**Fluid within or beneath the epidermis can produce blisters.** The level and mechanism of separation differ among inflammatory, infectious, and autoimmune processes. A photograph can show a vesicle or bulla without revealing the exact tissue plane or cause.

**Dermal edema can produce a wheal.** Increased vascular permeability raises the skin transiently. The time course of an individual lesion can be more discriminating than its appearance in one photograph.

**Deeper growth or inflammation can produce a nodule.** A nodule's depth, consistency, tenderness, and mobility matter. Those properties are incompletely represented by surface color and contour.

**Surface disruption produces secondary changes.** Scratching, bleeding, infection, or tissue destruction can produce erosion, crust, and ulceration. These can obscure the primary lesion that initiated the process.

Clinical description therefore separates primary morphology from changes caused by evolution, scratching, or treatment.

### Eczema and psoriasis illustrate why mechanism matters

In eczematous inflammation, impaired barrier function and inflammation can reinforce each other. The skin becomes more susceptible to irritants and water loss. Intercellular edema in the epidermis can contribute to small vesicles and weeping.

Itch encourages scratching, which further disrupts the barrier. With chronic rubbing, skin markings can become accentuated and the surface thickened. A chronic lesion may consequently look different from an earlier moist or vesicular phase of the same process.

Psoriasis involves immune-mediated changes that accelerate epidermal proliferation and alter maturation. Accumulated surface scale and thickened plaques follow from that altered turnover.

These mechanisms overlap at the level of a cropped image: both conditions can produce an inflamed, scaly plaque. Distribution, lesion boundaries, other body sites, nail changes, history, and examination help discriminate them.

A model that recognizes scale has measured a relevant finding. It has not necessarily identified which mechanism produced it.

The same caution applies to pustules. A pustule contains inflammatory cells, but its presence does not by itself establish a bacterial cause. Sterile inflammatory processes can also produce pustular lesions.

### Pigment and vascular signals are not interchangeable

Skin color reflects interacting contributions from pigment, blood, tissue structure, and illumination.

Inflammation can change blood flow and vascular appearance. Its visible expression varies with the underlying skin pigmentation and the process involved. Redness may be less conspicuous or appear as a different color pattern on more deeply pigmented skin.

Less visible redness does not establish less inflammation.

Pigment changes can also persist after active inflammation subsides. A photograph may therefore record a residual consequence rather than current disease activity.

Severity assessment needs to distinguish:

- Active inflammation.
- Residual hyperpigmentation or hypopigmentation.
- Thickening or swelling.
- Excoriation and barrier damage.
- Symptoms such as itch and pain.
- Effects on sleep and daily function.

An image-based severity score that relies heavily on redness can miss burden that is expressed through other findings. A score based on residual color can also overstate ongoing inflammatory activity.

### Neoplastic growth creates a different set of questions

Melanocytic lesions are assessed partly through the organization of pigment and structures. Asymmetry, uneven distribution, and change can be informative because abnormal growth can disrupt an otherwise coherent architecture.

No single visible feature establishes melanoma. Benign lesions can be irregular, and some melanomas have little conspicuous pigment.

Keratinocytic cancers can present with scale, crust, ulceration, abnormal vessels, or a raised lesion. These findings can overlap with inflammatory and benign conditions.

The clinical question is not simply whether a lesion is dark or irregular. It includes:

- Whether the lesion has changed.
- How it compares with the person's other lesions.
- Whether the surface pattern matches a recognizable benign process.
- Whether palpation suggests induration or deeper involvement.
- Whether the lesion is adequately represented in the image.
- Whether tissue assessment is needed.

Depth of invasion and other microscopic features cannot be directly measured from an ordinary surface photograph. A model can estimate their probability from associated appearances, but that remains a prediction requiring an appropriate tissue reference.

### Morphology must be connected to distribution and time

| Observation | Clinical contribution | What a close crop can miss |
|---|---|---|
| Primary lesion type | Identifies the kind of tissue response | Depth and tactile properties |
| Scale, crust, or erosion | Describes surface change | Whether it is primary or caused by scratching or treatment |
| Distribution | Supports exposure-related, anatomical, infectious, or inflammatory patterns | Symmetry, extent, and associated sites |
| Borders and arrangement | Can narrow the differential | How the lesion relates to neighboring skin |
| Evolution | Distinguishes persistent, recurrent, migrating, or changing processes | The temporal pattern itself |
| Symptoms | Itch, pain, tenderness, bleeding, or systemic involvement | Subjective and systemic information |
| Palpation | Induration, warmth, texture, mobility, and depth | Properties not directly recorded by pixels |
| Other lesions | Provides within-person comparison and diagnostic context | Findings outside the submitted image |

A transient wheal and a persistent papule can resemble each other at one moment. Their time courses imply different mechanisms.

Similarly, a solitary scaly patch can be interpreted differently when there are matching lesions elsewhere, a relevant exposure distribution, or associated nail findings. Cropping can remove exactly the evidence that makes the diagnosis coherent.

### Clinical photography and dermoscopy are different modalities

Clinical photography records the macroscopic surface appearance under a particular camera and illumination setup.

Dermoscopy reduces some surface optical interference and reveals patterns not readily visible to the unaided eye. It can support assessment of pigment structures, vessels, and other lesion features.

The two input types should not be treated as interchangeable:

- A finding visible in dermoscopy may not be assessable in an ordinary phone photograph.
- Polarization and contact conditions can change which structures are emphasized.
- Contact pressure can alter visible vascular features.
- Magnification does not restore information lost through poor focus or incomplete coverage.

Dermoscopy remains an interpreted measurement. A pattern associated with malignancy is not a histological diagnosis, and a reassuring pattern does not make the history or adequacy of the image irrelevant.

The model's claimed evidence should match the modality it actually receives.

### Unstandardized acquisition changes the measurement before the model sees it

The recorded image depends on the lesion, surrounding skin, illumination, geometry, camera optics, and image processing.

Important changes include:

- Exposure and white balance.
- Flash and shadows.
- Camera distance and angle.
- Focus and motion blur.
- Compression and sharpening.
- Automatic enhancement or cosmetic filters.
- Presence of hair, rulers, ink markings, gel, or dressings.

These factors can alter color, texture, apparent boundaries, and visibility of small structures.

A model can also learn how the image was collected. A ruler, biopsy mark, clinic background, or distinctive dermoscopic device can correlate with the likelihood that the lesion was concerning enough to photograph or sample.

Such information is not always irrelevant. A scale reference can support measurement. But its presence or placement can also encode prior clinical concern. The audit needs to distinguish its intended measurement role from its association with the target label.

Color normalization is not automatically a safe correction. Color can carry clinical evidence, and changing it can remove meaningful contrast. The required invariance is to irrelevant acquisition variation while retaining the differences needed for the clinical task.

### Skin tone needs an operational measurement

Skin tone, race, ethnicity, and sun-response classifications are not interchangeable variables.

A classification based on burning and tanning tendency does not directly measure the color visible in a particular image. Image color is itself affected by illumination and processing.

An evaluation should state:

- How skin tone was assessed.
- Whether assessment was in person or from photographs.
- Which anatomical region was assessed.
- How uncertainty was handled.
- Whether the annotation describes constitutive pigmentation or the appearance under the recorded conditions.

Performance differences across skin tones can reflect several interacting causes: visibility of the finding, representation in training data, disease mix, reference-label quality, and acquisition.

Published evaluations have demonstrated skin-tone-related performance gaps in some dermatology AI systems. That evidence supports testing the relevant model and setting; it does not establish that every system has the same disparity or mechanism.

Subgroup analysis should also consider body site, diagnosis, and acquisition together. A broad average can hide a clinically consequential failure concentrated in a particular combination.

### Diagnostic reasoning compares mechanisms

Consider an itchy, scaly plaque.

Eczema, psoriasis, superficial fungal infection, and other processes can overlap visually. The clinician asks about onset, recurrence, exposure, symptoms, other sites, and treatment already used.

An active border, distribution, associated findings, and the history can make one explanation more plausible, but no isolated feature is universally decisive. Treatment can also change the appearance and obscure a previously recognizable pattern.

If infection is a serious competing explanation, targeted microscopy or microbiological testing may answer a different question from a biopsy. If allergic contact dermatitis is suspected, exposure history and appropriately interpreted testing can matter more than a photograph alone.

A model that classifies the image as “inflammatory” may be correct at a broad descriptive level while failing to distinguish alternatives that lead to different management.

Now consider a changing solitary lesion. Comparison with earlier images and the person's other lesions can be informative. A current close-up alone cannot establish whether the lesion is stable, newly appearing, or evolving.

The diagnostic process is therefore multimodal even when the most visible part of the disease is on the skin.

### Reference standards are condition-specific

| Reference | Appropriate contribution | Important limitation |
|---|---|---|
| Histopathology | Cellular and architectural diagnosis in sampled tissue | Sampling, tissue processing, interpretation, and lesion matching |
| Clinical assessment | Integration of morphology, distribution, symptoms, and examination | Reader disagreement and incomplete information |
| Clinical consensus | A documented shared interpretation | Consensus is not independent proof of the biological mechanism |
| Targeted microbiology or microscopy | Evidence relevant to an infectious differential | Sampling, prior treatment, and the distinction between presence and causation |
| Appropriate allergy or immune testing | Evidence addressing a specific mechanism | The result needs clinical relevance and context |
| Planned follow-up | Stability, evolution, resolution, or later diagnosis | Adequate duration, adherence, and ascertainment are required |
| Image-only expert label | Interpretation of the submitted image | May omit decisive information available in the actual clinical encounter |

Biopsy is a strong reference for many suspicious neoplasms, but it is not an infallible or universal gold standard for all dermatology.

A partial sample can miss the most consequential part of a heterogeneous lesion or fail to capture its deepest extent. The tissue diagnosis must correspond to the lesion shown in the image.

For inflammatory disease, histology may establish a reaction pattern without uniquely identifying its cause. Clinical history and distribution can remain necessary.

Conversely, routine clinical diagnosis can be appropriate for some conditions without biopsy. Requiring tissue confirmation for every label would select a different and less representative population.

### Follow-up is evidence only when follow-up actually occurred

A lesion judged appropriate for observation may receive a reference based on documented stability or evolution. That is different from histological confirmation.

The record should identify:

- What was being observed.
- Whether the same lesion was reassessed.
- The method and adequacy of reassessment.
- Whether treatment occurred.
- Whether the observation period was suitable for the clinical question.
- Whether a later diagnosis was captured.

“No further visit” is not equivalent to “stable benign lesion.” The person may have sought care elsewhere or not returned.

Improvement with treatment also does not always identify a unique diagnosis. Several inflammatory processes can improve under similar treatment, while treatment can temporarily alter the appearance of another process.

Follow-up labels should therefore retain their provenance rather than being made indistinguishable from pathology-confirmed diagnoses.

### Biopsy selection changes the dataset

Lesions are selected for biopsy because of concern, uncertainty, symptoms, accessibility, and other clinical considerations.

A pathology-confirmed dataset consequently estimates performance among selected lesions. It is not an unbiased sample of all skin findings encountered by a phone application or primary-care service.

If suspicious lesions receive tissue confirmation while reassuring lesions receive a visual label or incomplete follow-up, the reference process differs between groups. This is differential verification.

A model can appear accurate partly because:

- The biopsied positive cases are more conspicuous.
- The negative cases have a weaker reference.
- Acquisition differs between biopsied and nonbiopsied lesions.
- The image was obtained after a clinical decision or procedure.
- Uncertain cases were excluded.

The correct response is to document and evaluate the reference process. Calling every label “ground truth” does not remove these differences.

### Prevalence changes the value of a positive result

A specialist lesion clinic and a broadly used phone application draw from different selection processes. A specialist clinic may be enriched for concerning lesions; an app can include normal variants and minor conditions, while also attracting people worried about a changing lesion.

The target prevalence must be measured in the intended setting. It should not be assigned merely from the fact that the input came from a phone.

For a binary target, let:

- $$\pi$$ be prevalence.
- $$Se$$ be sensitivity.
- $$Sp$$ be specificity.

Then

$$
P(\text{target and positive})
=
Se\,\pi,
$$

and

$$
P(\text{positive})
=
Se\,\pi+(1-Sp)(1-\pi).
$$

Therefore,

$$
PPV
=
\frac{Se\,\pi}
{Se\,\pi+(1-Sp)(1-\pi)}.
$$

Even if sensitivity and specificity stayed fixed, a lower prevalence would generally reduce the probability that a positive result represents the target when false positives occur.

In practice, moving from a specialist dataset to phone images can also change sensitivity and specificity because image quality, disease spectrum, and user behavior change.

Prevalence adjustment alone cannot repair those additional shifts.

The implication is practical: a classifier that seems manageable in an enriched lesion clinic can create a large burden of unnecessary assessment in a broader population. Conversely, reassuring aggregate performance can conceal missed malignancy in an underrepresented presentation.

### The action is part of the target

“Benign versus malignant” is not always the most useful immediate output.

A triage system may need to distinguish:

- Images adequate for the intended assessment.
- Cases requiring additional history or examination.
- Findings warranting prompt professional assessment.
- Cases for which a defined observation pathway is appropriate.

These are action-linked targets, but they need their own references. A clinician's decision to biopsy is not identical to a histological malignancy label.

Image inadequacy should not become a negative diagnosis. A blurred or incomplete image can be uninformative rather than reassuring.

The same applies to severity. A photograph may show limited visible extent while itch, pain, sleep disruption, or involvement of a functionally important site creates substantial burden. A visual severity score should retain the scope of what it measured.

### Error consequences are asymmetric and diagnosis-dependent

Missing a consequential malignancy can delay diagnosis and allow further progression. A false-positive cancer classification can lead to unnecessary biopsy, scarring, anxiety, cost, and clinical workload.

Errors among inflammatory and infectious conditions can direct the person toward an inappropriate treatment pathway. The consequences differ from confusing two low-consequence descriptive categories.

A close crop can also omit extensive involvement, mucosal lesions, or systemic features that determine urgency. An image-only model should not claim that it assessed information it never received.

An error analysis should consequently separate:

- Missed malignancy from benign-category confusion.
- Inadequate-image reassurance from an interpretable negative result.
- Misclassification that changes treatment from one that does not.
- Current inflammation from residual pigment change.
- Errors concentrated by skin tone, site, modality, or reference method.
- Failure to recognize that the task exceeds the available information.

The operating point should follow the intended action and its consequences, rather than a universal preference for higher sensitivity or specificity.

### Revision checklist

| Question | What I should be able to explain |
|---|---|
| What process produces the finding? | Epidermal change, dermal inflammation, vascular change, infection, or neoplastic growth |
| Why is morphology not a diagnosis? | Different mechanisms can produce the same visible pattern |
| What does distribution contribute? | Anatomical and exposure context lost in a close crop |
| What is unavailable from a photograph? | Palpation, symptoms, complete extent, and unrecorded evolution |
| How does dermoscopy differ? | It reveals additional optical structures under a different acquisition |
| Why does skin tone affect assessment? | Pigment, vascular signals, disease expression, and acquisition interact |
| What does the skin-tone label mean? | A specified assessment rather than a substitute for race or device-dependent image color |
| When is histology the reference? | When sampled tissue addresses the clinical target |
| What can follow-up establish? | Documented longitudinal behavior under a suitable observation process |
| Why is a biopsy dataset selected? | The decision to sample depends on concern and clinical circumstances |
| Why does clinic-to-app transport change PPV? | The target prevalence and selection process change |
| Which errors matter most? | Those that alter the intended clinical action or conceal insufficient evidence |

## Why it matters for my work

Dermatology makes measurement and reference provenance inseparable from interpretation. A plausible lesion-centered explanation can still depend on acquisition or prior clinical selection. In the ontology, Clinical assessability limits Clinical evidence reliance: an image may support a visible finding while leaving depth, symptoms, and the decisive diagnostic context unmeasured.

## What I have not resolved

- How can acquisition variation be reduced without erasing clinically meaningful color and texture?
- How should mixed pathology, clinical, and follow-up references be evaluated without treating their uncertainties as equivalent?

---

Sources: NIAMS material on atopic dermatitis and psoriasis; NCI material on melanoma assessment; Daneshjou and colleagues, Disparities in dermatology AI performance on a diverse, curated clinical image set. The predictive-value relation is symbolic and does not assign clinical performance figures. These are study notes for research purposes, not clinical guidance.
