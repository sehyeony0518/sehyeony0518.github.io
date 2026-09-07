---
layout: study_note
title: "Gastric Cancer"
description: "Endoscopic detection, screening programs, and reader variability in a real-time diagnostic setting."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "oncology"
category_title: "Oncology"
order: 3
source: "Lecture"
written: true
updated: "2026-09-08"
---

Gastric cancer usually refers to adenocarcinoma arising from the stomach’s epithelial lining. Endoscopy detects and characterizes mucosal abnormalities, but histology and assessment of disease extent determine what those appearances mean clinically.

## Clinical overview

Early gastric cancer may produce few specific symptoms. Other patients present with anemia, bleeding, weight loss, or persistent upper gastrointestinal symptoms. A screening examination and an investigation prompted by concerning symptoms therefore begin with different clinical probabilities and purposes.

The [Korean Practice Guidelines for Gastric Cancer 2024](https://doi.org/10.5230/jgc.2025.25.e11), published in 2025, describe a national screening program beginning at age 40 with two-year intervals. That program schedule should not be confused with follow-up for a known lesion or an individual at elevated risk. I find the distinction important when interpreting what an endoscopy was expected to detect.

## Anatomy and pathophysiology

Chronic Helicobacter pylori infection can contribute to atrophic gastritis, intestinal metaplasia, and gastric adenocarcinoma, although not every cancer follows an identical sequence. Family history and other conditions can also alter risk. The [NCI prevention summary](https://www.cancer.gov/types/stomach/hp/stomach-prevention-pdq) distinguishes established risk factors from associations that may remain confounded.

Depth of invasion matters because the mucosa, submucosa, and deeper wall layers differ in their relationship to lymphatic spread. Early gastric cancer is confined to the mucosa or submucosa, regardless of nodal status. Surface appearance can suggest invasion depth, but it does not directly measure every microscopic feature relevant to treatment.

## Diagnostic workflow and imaging findings

### Examine the entire mucosal surface

A high-quality examination requires adequate visualization, distension, and systematic inspection, including areas that are easily hidden by folds or retained material. Cleaning and changes in viewing angle can make a subtle lesion apparent. I read this as part of diagnosis itself: an abnormality cannot be recognized if the relevant mucosa was never adequately seen.

### Recognize and characterize a suspicious area

White-light findings may include a subtle depression or elevation, focal discoloration, an irregular surface, ulceration, or abnormal fold convergence. These appearances overlap with inflammation and benign ulcer disease. Lesion boundaries, size, location, and the surrounding mucosa should be described before assigning a diagnostic category.

### Use enhanced imaging for a defined question

Magnifying narrow-band imaging can display microvascular and microsurface patterns. The [MESDA-G algorithm](https://doi.org/10.1111/den.12638) evaluates a demarcation line and irregular microvascular or microsurface patterns when characterizing suspected early cancer. This is a structured interpretation of a lesion already brought into view, not a guarantee of complete detection throughout the stomach.

### Confirm histology and assess treatment-relevant extent

Targeted biopsy provides tissue diagnosis but samples only part of the lesion. Histological differentiation, estimated invasion depth, ulceration, and possible nodal involvement contribute to planning. CT assesses regional and distant disease; endoscopic ultrasound can help selected depth-assessment questions. A resection specimen may reveal information absent from the original biopsy, including deeper invasion or lymphovascular involvement.

## Differential diagnosis and management context

Gastritis, erosions, benign ulcers, adenomas, lymphoma, and subepithelial lesions can enter the differential. Persistent suspicion despite an uninformative sample requires clinical reassessment of sampling and lesion characteristics. A negative biopsy should not be interpreted independently of whether it adequately represented the abnormality.

Selected early cancers can be managed by endoscopic resection when their features imply an acceptably low risk of lymph-node metastasis. Others require surgery or systemic treatment according to stage and clinical circumstances. The Korean guideline links treatment decisions to pathological and staging information, rather than to endoscopic appearance alone. Eradication of H. pylori, where indicated, does not remove the need for appropriate surveillance in patients who remain at risk.

## Implications for medical AI

I would distinguish real-time lesion detection from characterization of a selected still image and prediction of resection eligibility. A dataset containing clear, centered lesions measures a different task from an uninterrupted screening examination with motion, mucus, folds, and incomplete views. Patient-level separation is necessary because adjacent frames can be nearly identical.

The connection to my gallbladder work is both acquisition dependence and reader-dependent evidence. I would record whether an error arose because a lesion was unseen, unrecognized, mischaracterized, or inadequately sampled. Evaluation should include missed lesions, false prompts, examination time, reader disagreement, and downstream pathology, while checking whether biopsy instruments or annotations become shortcut cues.

## References

- Kim et al., [Korean Practice Guidelines for Gastric Cancer 2024: An Evidence-based, Multidisciplinary Approach (Update of 2022 Guideline)](https://doi.org/10.5230/jgc.2025.25.e11), Journal of Gastric Cancer 2025.
- Muto et al., [Magnifying endoscopy simple diagnostic algorithm for early gastric cancer (MESDA-G)](https://doi.org/10.1111/den.12638), Digestive Endoscopy 2016.
- NCI PDQ Screening and Prevention Editorial Board, [Stomach (Gastric) Cancer Prevention (PDQ)](https://www.cancer.gov/types/stomach/hp/stomach-prevention-pdq), National Cancer Institute, accessed 2026.
