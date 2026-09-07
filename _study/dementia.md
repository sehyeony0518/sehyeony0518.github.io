---
layout: study_note
title: "Dementia"
description: "Biomarker-based diagnosis and the difficulty of validating prediction far ahead of an event."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "neurology"
category_title: "Neurology"
order: 2
source: "Lecture"
written: true
updated: "2026-09-08"
---

Dementia is a syndrome of acquired cognitive decline that interferes with independent daily functioning. Alzheimer’s disease is one possible cause, and evidence of Alzheimer pathology is not interchangeable with the presence or severity of dementia.

## Clinical overview

Assessment concerns changes in memory, language, executive function, visuospatial ability, behavior, and everyday activities. A patient may retain basic self-care while losing the ability to manage medication or finances. Mild cognitive impairment generally preserves independence, although tasks may require greater effort or compensatory strategies.

Age increases the likelihood of neurodegenerative disease, but cognitive decline should not be attributed to age alone. The clinical question includes whether a syndrome is present, what contributes to it, and how it affects the person and family. I find this separation useful before interpreting any scan or biomarker.

## Anatomy and pathophysiology

Alzheimer’s disease involves amyloid and tau pathology, while other dementias reflect different or overlapping processes, including vascular injury, Lewy body disease, and frontotemporal degeneration. Mixed pathology is common. Brain reserve, comorbidity, and the distribution of injury help explain why similar biological findings do not produce identical clinical impairment.

Structural atrophy measures tissue loss rather than identifying its cause directly. Molecular biomarkers and cognitive assessments observe different parts of the disease process. The [2024 Alzheimer’s Association criteria](https://doi.org/10.1002/alz.13859) explicitly distinguish biological diagnosis from clinical staging.

## Diagnostic workflow and imaging findings

### Establish change from the person’s baseline

History should include the patient and, where possible, someone who knows their everyday functioning. The clinician assesses onset, progression, medications, mood, sleep, sensory impairment, and delirium. Cognitive testing supports this assessment, but language, education, and testing conditions affect interpretation. [Atri and colleagues’ diagnostic guideline](https://doi.org/10.1002/alz.14333) organizes evaluation around the cognitive syndrome, functional status, and likely causes.

### Look for contributing and alternative conditions

Physical and neurological examination and appropriate laboratory testing assess potentially treatable contributors. Depression, medication effects, metabolic illness, and acute confusion can coexist with neurodegeneration. A brief screening score cannot settle these alternatives. Rapid progression, focal signs, or an atypical presentation may require a more specialized investigation.

### Interpret structural imaging as a pattern

MRI can identify infarcts, white-matter disease, hemorrhagic lesions, masses, and patterns of atrophy; CT is an alternative when MRI is unsuitable. Medial temporal atrophy can support an Alzheimer-pattern interpretation, while frontal or anterior temporal predominance may suggest another syndrome. These patterns overlap. [NICE guidance](https://www.nice.org.uk/guidance/ng97/chapter/recommendations) recommends structural imaging to assess alternative causes and assist subtype diagnosis, with specified exceptions.

### Use biomarkers to answer an etiological question

Amyloid PET, appropriate cerebrospinal-fluid assays, and sufficiently validated blood-based assays can provide evidence of Alzheimer pathology. Under the 2024 criteria, an abnormal qualifying Core 1 biomarker can establish biological Alzheimer’s disease. That does not prove that Alzheimer pathology explains every symptom or predict an exact date of functional decline. The criteria recommend against clinical diagnostic testing of cognitively unimpaired people outside research.

## Differential diagnosis and management context

The differential includes Alzheimer’s disease, vascular cognitive impairment, dementia with Lewy bodies, frontotemporal disorders, and other neurological or systemic causes. Fluctuating attention, hallucinations, parkinsonism, behavioral change, or a stepwise course can guide assessment, but none should be interpreted in isolation. A biomarker-positive patient can still have important copathology.

Management follows the clinical syndrome and cause: addressing contributors, supporting safety and daily function, discussing care needs, and considering appropriate symptomatic or disease-targeted treatment through specialist assessment. Biological confirmation may affect treatment eligibility, but does not replace assessment of benefit, risk, and the patient’s goals.

## Implications for medical AI

I would distinguish prediction of a current clinical syndrome, biomarker status, and future dementia. A model trained to separate established dementia from healthy volunteers has not demonstrated prediction years before functional impairment. Longitudinal evaluation needs a defined starting point, outcome, prediction horizon, and handling of loss to follow-up and death before dementia develops.

This suggests to me a connection with clinical faithfulness auditing: a model may encode relevant atrophy without establishing which pathology caused it or when symptoms will emerge. I would test calibration over the intended horizon and examine whether scanner, recruitment pathway, or follow-up intensity substitutes for biological evidence.

## References

- Jack et al., [Revised criteria for diagnosis and staging of Alzheimer’s disease: Alzheimer’s Association Workgroup](https://doi.org/10.1002/alz.13859), Alzheimer’s & Dementia 2024.
- Atri et al., [Alzheimer’s Association clinical practice guideline for the Diagnostic Evaluation, Testing, Counseling, and Disclosure of Suspected Alzheimer’s Disease and Related Disorders (DETeCD-ADRD): Executive summary of recommendations for primary care](https://doi.org/10.1002/alz.14333), Alzheimer’s & Dementia 2025.
- NICE, [Dementia: assessment, management and support for people living with dementia and their carers](https://www.nice.org.uk/guidance/ng97/chapter/recommendations), NG97 2018.
