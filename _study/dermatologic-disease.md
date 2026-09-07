---
layout: study_note
title: "Dermatologic Disease"
description: "Visual diagnosis, dataset bias across skin tones, and the failure modes this field has documented most thoroughly."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "dermatology"
category_title: "Dermatology"
order: 1
source: "Lecture"
written: true
updated: "2026-09-08"
---

Dermatologic diagnosis starts with the appearance and distribution of skin findings, interpreted alongside symptoms and their evolution. I use inflammatory eruptions and suspicious skin lesions to study why a photograph can be informative without containing everything needed for diagnosis.

## Clinical overview

Skin disease includes inflammatory, infectious, autoimmune, vascular, and neoplastic conditions. Similar-looking lesions can arise through different mechanisms, while one disease can look different across body sites, stages, treatment states, and skin tones. A chronic itchy eruption and a changing solitary lesion therefore require different histories and examinations.

Visible extent also does not fully describe burden. Itch, pain, sleep disruption, bleeding, and functional or psychological effects matter. The [atopic dermatitis assessment guideline](https://pubmed.ncbi.nlm.nih.gov/24290431/) treats diagnosis and severity as clinical assessments involving more than appearance. I would keep that distinction when interpreting a photograph-based severity score.

## Anatomy and pathophysiology

The epidermis, dermis, appendages, and subcutaneous tissue can each be the primary site of disease. Surface scale reflects a different process from a deep nodule or a transient wheal. Barrier dysfunction and inflammation contribute to eczema, whereas a melanocytic lesion raises questions about cell proliferation and tissue architecture.

Pigmentation and vascular changes both influence visible color. Inflammation may appear less conspicuously red on more deeply pigmented skin, and residual pigment change can persist after activity subsides. I read this as a reason to assess texture, swelling, symptoms, and change over time alongside color, rather than treat redness as a universal measure of inflammation.

## Diagnostic workflow and imaging findings

### Establish morphology and distribution

The clinician describes primary lesions such as macules, papules, plaques, vesicles, or nodules, then secondary changes such as scale, crust, erosion, or ulceration. Distribution, symmetry, borders, and involvement of nails, scalp, or mucosa narrow the differential. A close crop can preserve surface detail while removing precisely this diagnostic context.

### Add history and direct examination

Onset, progression, itch, pain, exposure, medication, treatment response, and systemic symptoms can change the interpretation. Palpation provides information about induration, tenderness, temperature, and depth that a photograph cannot directly supply. Examination beyond the photographed area may reveal associated lesions or an alternative explanation.

### Use dermoscopy for a specific lesion question

Dermoscopy reveals structures not readily visible to the unaided eye. In melanocytic lesions, asymmetry of structures, atypical pigment networks, irregular dots or globules, and uneven color distribution can raise concern, but no isolated feature establishes melanoma. [NICE guidance](https://www.nice.org.uk/guidance/ng14/chapter/Recommendations) recommends trained dermoscopic assessment of relevant pigmented lesions in specialist care. Clinical photography and dermoscopy should remain distinct input types.

### Obtain tissue or other tests when needed

Biopsy can establish histological features relevant to malignancy or an inflammatory differential. The specimen must represent the lesion and the diagnostic question. Microbiological testing or patch testing may be more appropriate for other presentations. A pathology-confirmed dataset consequently represents lesions selected for biopsy, not an unbiased sample of all skin problems.

## Differential diagnosis and management context

Eczema, psoriasis, fungal infection, and contact dermatitis can overlap in appearance. Pigmented benign lesions can resemble melanoma, while some malignancies lack prominent pigment. Clinical change or discordance between appearance and an initial interpretation can justify reassessment rather than repeated reliance on the same image.

Management follows the diagnosis, severity, location, and patient context. An inflammatory eruption may need barrier care and anti-inflammatory treatment; infection requires a different approach; suspected malignancy may require biopsy and definitive treatment planning. A model output that increases unnecessary procedures carries a different cost from one that delays assessment of a consequential cancer.

## Implications for medical AI

The [DDI study by Daneshjou and colleagues](https://doi.org/10.1126/sciadv.abq6147) documented poorer performance on darker skin for evaluated dermatology AI systems using a diverse, pathology-confirmed image set. It also examined limitations of expert visual labels. I would treat this as evidence about the tested systems and dataset, rather than assume that every dermatology model has an identical disparity.

For my own auditing work, the lesson is to retain skin-tone annotation methods, diagnosis frequency, acquisition conditions, body site, and reference provenance. I would test errors across their combinations and preserve patient-level separation. As in gallbladder ultrasound, attention inside a plausible lesion does not establish reliance on the feature that makes the diagnosis clinically defensible.

## References

- Eichenfield et al., [Guidelines of care for the management of atopic dermatitis: section 1. Diagnosis and assessment of atopic dermatitis](https://pubmed.ncbi.nlm.nih.gov/24290431/), Journal of the American Academy of Dermatology 2014.
- NICE, [Melanoma: assessment and management](https://www.nice.org.uk/guidance/ng14/chapter/Recommendations), NG14 2015.
- Daneshjou et al., [Disparities in dermatology AI performance on a diverse, curated clinical image set](https://doi.org/10.1126/sciadv.abq6147), Science Advances 2022.
