---
layout: study_note
title: "Lung Cancer"
description: "Screening programs, overdiagnosis, and what a screening context does to the meaning of a positive result."
og_image: "https://sehyeony0518.github.io/assets/img/og/lung-cancer.png"
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "oncology"
category_title: "Oncology"
subgroup: "Detection & Screening"
order: 1
source: "Lecture"
written: true
updated: "2026-09-08"
---

## Core question and definition

What can a lung image establish about a lesion, and when does detecting that lesion help the patient?

Lung cancer comprises malignant tumours with different cellular origins, growth patterns, molecular features and clinical behaviour. The familiar distinction between non-small-cell and small-cell carcinomas is clinically important, but an imaging appearance is not a substitute for histological classification.

The first distinction for medical AI is between **screening** and **diagnostic investigation**.

Screening examines people without symptoms of the target disease within a defined programme. Diagnostic investigation addresses a symptom, suspicious finding or other clinical concern. The populations, starting probabilities and acceptable follow-up burdens differ.

Several tasks can occur within either pathway:

| Task | What success establishes |
| --- | --- |
| Nodule detection | A specified image finding was located |
| Nodule characterization | Features such as attenuation, contour and change were assessed |
| Malignancy estimation | The finding’s probability of being malignant was estimated in a defined population |
| Histological or molecular prediction | An imaging association with a tissue-defined target was estimated |
| Staging support | Evidence about local, nodal or distant extent was assessed |
| Screening evaluation | The programme’s benefits and harms were evaluated |
| Clinical utility assessment | Using the system improved a relevant decision or outcome |

These claims are not interchangeable. A true cancer can be overdiagnosed in a screening context. A correctly detected nodule can still lead to unnecessary investigation. A model can recognize advanced disease without demonstrating early detection.

## Key concepts

### Airways, alveoli and tissue replacement explain the main appearances

The lung contains branching airways ending in gas-exchanging alveolar structures. Much of its normal volume is air, with thin supporting tissue, vessels and airway walls.

On CT, the image reflects the mixture of air and tissue within each reconstructed region. A disease process becomes visible when it changes that mixture, distorts normal structures or introduces a focal abnormality.

A tumour growing as a compact mass replaces or displaces aerated lung and can produce a solid opacity. A tumour involving an airway can narrow or obstruct it. A tumour growing along alveolar surfaces may leave some air-containing architecture intact and produce a different appearance.

This is the mechanism behind an important principle: image attenuation is not a direct cell-type label. Several processes can increase tissue content or reduce air, including tumour, inflammation, fluid, haemorrhage and fibrosis.

A bright pulmonary focus is therefore an observation requiring explanation. The clinician considers its morphology, location, persistence, change and the patient’s context.

For AI, a model must learn a distinction among plausible causes of an opacity, not merely the difference between aerated lung and additional tissue.

### Histological families have overlapping imaging presentations

Non-small-cell lung cancers include adenocarcinoma, squamous cell carcinoma and other categories. Small-cell carcinoma has a distinct biological and clinical context, including a tendency toward aggressive growth and dissemination.

Adenocarcinoma can occur peripherally and may have solid, part-solid or ground-glass components. Squamous carcinoma can involve central airways, although location is not an absolute classifier. Small-cell carcinoma can present with central disease and nodal involvement, but an image alone cannot reliably assign the histological category.

The same broad appearance can arise from primary lung cancer, a metastasis or a benign process.

Histology matters because treatment depends on more than gross anatomy. Molecular testing can add information about tumour biology that is not directly visible as a unique CT feature.

An imaging model may estimate associations with histology or molecular status. Such an estimate requires tissue-defined validation and appropriate uncertainty. It should not be described as directly reading a mutation from an image.

The biological label and the visible phenotype are linked, but they are not identical observations.

### Solid, ground-glass and part-solid are imaging descriptions

A solid nodule has soft-tissue attenuation that obscures the underlying structures within the affected region.

Ground-glass opacity increases attenuation while allowing underlying vessels and airway structures to remain visible. This can occur when air is only partly displaced or when abnormalities are below the image’s spatial resolution.

A part-solid nodule combines ground-glass and solid components.

In some adenocarcinomas, growth along alveolar walls helps explain a ground-glass component. This growth pattern is termed lepidic. More invasive growth, stromal reaction or collapse can contribute to a denser component.

However, the correspondence is not exact enough to make CT a histological section. Inflammation and other benign processes can also produce ground-glass or part-solid appearances.

A new ground-glass focus and a persistent focal ground-glass nodule are therefore different evidential situations. Persistence and evolution add information that a single image cannot provide.

The image category should also not be confused with disease stage. A small or faint lesion is not automatically biologically harmless, while a conspicuous solid lesion is not automatically a particular histological subtype.

### Contour and associated findings suggest mechanisms, not certainty

Spiculation describes radiating strands at a lesion’s margin. Tumour infiltration and a fibrotic stromal response can produce such distortion, but scarring and inflammatory processes can also create irregular margins.

Lobulation can reflect uneven growth, yet it is not unique to malignancy. Cavitation can occur when material within a lesion breaks down or communicates with an airway; infection and malignancy can both produce cavities.

Some calcification patterns, visible fat or a typical perifissural configuration can favour a benign interpretation. The complete pattern matters. The mere presence of any calcium is not an unconditional exclusion of cancer.

Associated findings can also be informative. Airway obstruction can lead to distal collapse or retained secretions. A central tumour may therefore be partly hidden within atelectatic or inflamed lung.

A model confined to a neatly cropped nodule may miss these relationships. Conversely, a whole-scan model may rely on associated disease or care-related features rather than the nominated lesion.

The audit question is whether the information used is appropriate for the stated task, not whether it lies inside an arbitrary bounding box.

### Symptoms can arise from local effects or disease beyond the visible lesion

A lesion affecting an airway can produce cough, bleeding or recurrent obstruction-related infection. Involvement of nearby structures or distant sites can produce other symptoms.

A peripheral lesion may produce few symptoms while still being biologically important. The absence of respiratory complaints therefore does not imply absence of cancer.

Likewise, symptoms are not specific. Haemoptysis, weight loss or a persistent cough can have several causes. They change the clinical question and prior probability without identifying the pathology alone.

Smoking history is an important risk factor, but lung cancer also occurs in people who have never smoked. A dataset restricted to a familiar risk profile should not silently become a universal disease detector.

For a model, risk-related context can be legitimate when estimating patient-level risk. It is less adequate as an explanation that the model characterized a particular lesion’s malignant morphology.

The intended claim determines whether a contextual association is useful prior information or a substitute for the evidence the model claims to inspect.

### What each modality contributes

| Modality or procedure | What it can contribute | Important limit |
| --- | --- | --- |
| Chest radiography | Larger opacities, collapse and other thoracic abnormalities | Superimposed anatomy and limited visibility of subtle lesions |
| Thin-section CT | Nodule detection, morphology, distribution and anatomical relationships | Appearance does not uniquely determine histology |
| Serial CT | Persistence and change under comparable acquisition | Apparent change can include technical and physiological variation |
| PET/CT | Metabolic information and assessment of possible disease elsewhere | Inflammation can be avid; small or less avid cancers can be inconspicuous |
| Bronchoscopy or image-guided sampling | Tissue or cellular material from a selected site | Sampling may miss tumour or fail to represent its full heterogeneity |
| Resection specimen | More complete assessment of the removed lesion and relevant pathology | Available only in a selected group; not a reference for every other nodule |
| Clinical follow-up | Subsequent behaviour and outcomes | Requires adequate duration, ascertainment and lesion correspondence |

A negative result has meaning only relative to the procedure. A lesion not seen on a radiograph may be visible on CT. A non-avid lesion on PET is not equivalent to benign histology. A nondiagnostic biopsy is not a demonstrated absence of tumour.

### CT acquisition changes what is measurable

Slice thickness, reconstruction method, motion, dose-related noise, inspiratory level and display choices affect lesion visibility and measurement.

A small structure can occupy only part of a reconstructed voxel. Its apparent attenuation then reflects an average with surrounding air or tissue. Changing reconstruction can alter the appearance of the margin or a small solid component.

Inspiratory differences can also change the relationship between a lesion and surrounding lung. A measurement difference between examinations may therefore contain both biological change and acquisition variation.

This does not make serial imaging useless. It explains why comparable studies and careful review are needed.

For AI, acquisition metadata and quality should be retained. A model trained on one reconstruction style may fail when edges, texture or noise change.

Downsampling deserves particular attention. It may preserve the existence of a nodule while erasing a small internal component that changes its interpretation. Preserving a patient-level cancer label is not proof that preprocessing preserved the diagnostic evidence.

### Diagnostic reasoning begins by defining the setting

The clinician first establishes why the image was obtained.

An asymptomatic screening participant, a patient with a known extrathoracic malignancy and a patient with an acute respiratory illness can present with superficially similar nodules but different differentials.

The assessment then considers prior imaging, lesion type, location, morphology, associated abnormalities and the person’s clinical context.

Previous examinations are especially informative. A finding may be new, persistent, resolving or changing. Each description adds temporal evidence.

The next question is what additional information would change management. Depending on context, this may involve observation over time, additional imaging or tissue sampling.

The reasoning is not “suspicious image equals immediate biopsy.” The value of obtaining tissue depends on the probability of disease, whether the result will affect care and the risks of the procedure.

A model intended to recommend an action therefore needs a richer target than whether a selected nodule was eventually malignant.

### Differential diagnosis of a pulmonary nodule

| Possibility | Why the image can resemble cancer | Discriminating evidence |
| --- | --- | --- |
| Granuloma or previous infection | A persistent focal nodule can remain after inflammation | Pattern, prior imaging, relevant history and, when needed, tissue |
| Active infection or inflammation | Irregular, solid or ground-glass abnormalities can occur | Clinical context and evolution; metabolic activity is not decisive alone |
| Scar or focal fibrosis | Distortion and spiculation can resemble infiltrative growth | Stability, anatomical pattern and complete imaging assessment |
| Benign neoplasm or intrapulmonary lymph node | A discrete nodule is present | Characteristic morphology or composition, with appropriate context |
| Primary lung cancer | Tumour growth produces a focal abnormality | Integrated imaging, temporal and pathological evidence |
| Metastasis | A malignant nodule may originate outside the lung | Cancer history, distribution and tissue correspondence |

No single feature in the table supplies a universal diagnosis.

Multiplicity also needs interpretation. Several nodules do not automatically mean metastatic disease, and one proven cancer does not make every other nodule malignant.

This creates a reference-standard problem: patient-level malignancy cannot be propagated indiscriminately to every lesion.

### Tissue diagnosis is strong evidence with a sampling boundary

Histology and cytology assess cells and tissue obtained from a particular site.

A positive sample can establish malignancy in that sampled material and support classification. A limited sample may not reveal every histological component or provide sufficient material for all molecular tests.

A negative sample has to be interpreted in relation to adequacy and targeting. Normal tissue, necrosis or nonspecific inflammation may indicate that the relevant portion of the lesion was not represented.

The pathology report should therefore distinguish a specific benign diagnosis from an uninformative or nondiagnostic sample.

Resection provides a more complete specimen, but it introduces selection. Patients who undergo surgery differ from those observed, treated through another pathway or considered unable to tolerate an operation.

An image model evaluated only on resected lesions may consequently learn a case spectrum unlike routine screening.

The phrase “pathology-proven dataset” describes the reference source. It does not, by itself, establish representativeness or eliminate selection and verification bias.

### Staging requires a map of extent beyond the primary lesion

Cancer staging concerns local extent, regional lymph nodes and distant spread.

CT can show anatomical relationships and suspicious lesions. PET can add metabolic evidence. Selected tissue sampling can establish whether a particular site contains tumour.

These observations remain imperfect. Enlarged lymph nodes can be reactive, while normal-sized nodes can contain microscopic disease. Metabolic activity can occur in inflammation, and lack of conspicuous uptake does not universally exclude malignancy.

The primary tumour’s appearance therefore cannot independently establish the complete stage.

Clinical stage and pathological stage also arise from different evidence. Imaging and preoperative assessment produce one estimate; examination of resected tissue can provide additional information.

For supervised learning, the dataset must identify which stage is the target and how it was established. It should not mix clinical and pathological categories without recording their provenance.

A postoperative label can legitimately serve as a reference for a preoperative prediction, but postoperative images, reports or treatment indicators must not leak into the model’s inputs.

### Screening benefit is not established by finding more abnormalities

Screening aims to improve outcomes by identifying clinically important disease earlier. Detecting more lesions is an intermediate observation.

Several biases explain why detection and survival statistics can mislead.

**Lead-time bias:** diagnosis occurs earlier, so the measured interval from diagnosis to death becomes longer even if death occurs at the same time.

**Length bias:** a periodic screen has more opportunity to detect a slowly evolving disease during its longer detectable phase. Screen-detected cases can therefore differ biologically from cases presenting between screens.

**Overdiagnosis:** screening detects a genuine cancer that would not have caused symptoms or death during the person’s lifetime.

Overdiagnosis differs from a false positive. In a false positive, the target cancer is absent. In overdiagnosis, the cancer is present, but detecting it does not create the intended benefit.

These distinctions mean that pathology confirmation is not sufficient to establish the value of every screen-detected cancer. The relevant outcome concerns the whole screening strategy and its consequences.

Evidence supporting low-dose CT screening in defined populations should be understood as evidence about that intervention and population, not a guarantee that every additional detection is beneficial.

### Prevalence changes the meaning of a positive model result

A selected collection containing many cancers can be useful for studying image features. It does not directly estimate the positive predictive value or referral burden of screening.

When disease is less common, a substantial share of positive results can arise from people without the target cancer even if conditional test characteristics are unchanged.

In practice, conditional performance may also change because screening includes smaller, subtler and more varied findings than a diagnostic referral collection.

The study therefore needs the intended population, not merely a convenient case-control balance.

A model’s probability calibration should be evaluated in that population. An output interpreted as malignancy probability cannot be assumed to retain its meaning after a change in referral pathway or recruitment.

Recalibrating probabilities may address some differences, but it does not automatically repair a model that learned the wrong features or was never tested on relevant benign alternatives.

### Error costs depend on whether the action is review, surveillance or intervention

A missed clinically consequential cancer can delay diagnosis and reduce the opportunity for appropriate treatment.

A false positive can lead to additional imaging, invasive sampling, complications, anxiety and resource use. The magnitude of harm depends on what follows the alert.

A low-confidence prompt for image review has a different consequence from a recommendation for an invasive procedure. A false negative during nodule detection differs from an incorrect reassurance after a known nodule has already been identified.

Overdiagnosis adds a harm not captured by ordinary cancer-versus-benign classification. A system can correctly identify malignant tissue while increasing treatment of disease that would not have become clinically consequential.

The operating point must therefore be chosen within a defined pathway. It cannot be justified solely by a preferred sensitivity-specificity balance on an enriched test set.

Evaluation should report the downstream workload and the patients for whom the system fails, abstains or produces repeated unresolved alerts.

### Worked reasoning examples

**A persistent part-solid lesion has little conspicuous PET uptake.** The PET result is one observation with sensitivity limitations related to lesion properties and resolution. It does not erase the CT pattern or temporal evidence. A model trained to use PET negativity as a universal benign label would be learning an invalid rule.

**A spiculated, metabolically active lesion occurs in an inflammatory context.** The appearance raises concern, but both morphology and uptake have competing explanations. Tissue or subsequent evolution may change the interpretation. A heatmap on the lesion can be spatially plausible without establishing that the model distinguished these mechanisms.

**A surgical specimen confirms cancer in one nodule.** Other nodules in the same scan require their own correspondence and evidence. Assigning the patient’s cancer label to every crop introduces lesion-level label error.

**A model detects more cancers during screening.** The result is promising for detection. It does not alone establish reduced mortality, less morbidity or a favourable balance of investigation and treatment.

These examples are hypothetical and contain no invented performance estimates.

### Building an evaluation that matches the clinical claim

For nodule detection, the evaluation needs full examinations, lesion-level references and a definition of which findings count as targets.

For malignancy estimation, it needs lesion-specific outcomes and transparent handling of pathology, surveillance and incomplete verification.

For a management-support system, it also needs the clinical setting, available prior examinations and the action associated with the recommendation.

Patient separation must include all nodules, scans and follow-up studies from that patient. Temporal information must respect the intended decision point.

Useful subgroup analyses include lesion type, location, conspicuity, acquisition quality and the presence of clinically plausible benign alternatives. Failures on a small solid component may matter more than a similar numerical error elsewhere.

External validation should examine both acquisition changes and clinical selection. A model may transport between scanners while failing when prevalence, referral or follow-up practice changes.

Finally, a prospective workflow comparison is needed to establish what clinicians do with the output and what consequences follow.

### Revision checklist

| Question | What I should be able to explain |
| --- | --- |
| What makes a nodule visible on CT? | A change in the local mixture or organization of air and tissue |
| What is ground-glass opacity? | Increased attenuation with retained visibility of underlying structures |
| Why can lepidic growth appear ground-glass? | Growth along alveolar walls may preserve some air-containing architecture |
| Why is spiculation not a diagnosis? | Tumour and benign fibrotic processes can both distort margins |
| Why compare prior scans? | Persistence and change add evidence unavailable in a single examination |
| Why is a negative biopsy limited? | Adequacy and lesion targeting determine what was sampled |
| Why is PET uptake not cancer-specific? | Inflammatory processes can also be metabolically active |
| Why is stage not a property of one crop? | Extent includes regional and distant sites |
| What separates overdiagnosis from a false positive? | Cancer is genuinely present in overdiagnosis |
| Why can longer survival after diagnosis mislead? | Earlier diagnosis can lengthen the measured interval without delaying death |
| Why does an enriched dataset misstate screening burden? | The target prevalence and case spectrum differ |
| What establishes utility? | Evidence about the outcomes and harms of using the system |

### Connecting the clinical reasoning to the ontology

Tumour growth, inflammation and fibrosis provide different mechanisms that can manifest as overlapping pulmonary findings. Acquisition then determines whether their discriminating details are assessable.

`Malignancy & staging` `setsRequirementsFor` `Reference standard adjudication`: the reference must match the lesion, tissue sample, time and extent being predicted.

`Pretest probability` limits interpretation of `Predictive values`, particularly when transferring from selected diagnostic cases to screening.

`Clinical assessability` limits `Clinical evidence reliance` when reconstruction or downsampling removes a subtle component. Even valid lesion detection remains distinct from `Clinical utility`, because the benefit of acting on it depends on the complete screening or diagnostic pathway.

## Why it matters for my work

Lung cancer makes lesion truth, patient truth and intervention benefit visibly different. I need to keep pathology correspondence precise while evaluating the population and workflow in which a model’s output will acquire clinical meaning.

## What I have not resolved

- How should malignancy models combine pathology and longitudinal references without hiding their different verification processes?
- How can lesion-level audits distinguish legitimate risk context from substitution for local diagnostic evidence?
- What evaluation best detects an increase in unnecessary workup when image-level performance improves?

---

Sources: Existing lecture notes; National Cancer Institute PDQ summaries on lung cancer and screening; Fleischner Society, Glossary of Terms for Thoracic Imaging; American Thoracic Society, What Is a Lung Nodule?; RadiologyInfo resources on lung cancer imaging and diagnosis. The hypothetical cases and AI evaluation proposals are explanatory applications. These are study notes for research purposes and are not clinical guidance.
