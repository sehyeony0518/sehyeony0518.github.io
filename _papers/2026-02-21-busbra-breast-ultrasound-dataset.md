---
layout: post
title: "BUS-BRA: A Breast Ultrasound Dataset for Assessing Computer-Aided Diagnosis Systems"
date: 2026-02-21 12:00:00 +0900
venue: "Medical Physics"
authors: "Wilfrido Gómez-Flores, Maria Julia Gregorio-Calas, Wagner Coelho de Albuquerque Pereira (2024)"
description: "A biopsy-proven, multi-scanner breast ultrasound dataset with standardized cross-validation partitions — the kind of dataset-hygiene paper that makes fair benchmark comparisons possible in the first place."
related_posts: false
---

**Paper.** *BUS-BRA: A breast ultrasound dataset for assessing computer-aided diagnosis systems* — [Medical Physics (2024)](https://doi.org/10.1002/mp.16812)

## Why I read it

Dataset design determines what a breast-ultrasound model can validly claim. I read BUS-BRA not only as a data source, but as an example of how biopsy labels, BI-RADS categories, lesion masks, scanner diversity, and patient-level partitions should be documented for reproducible CAD evaluation.

## What the paper claims

BUS-BRA contains 1,875 breast-ultrasound images from 1,064 women, acquired with four ultrasound systems. The dataset includes biopsy-confirmed benign and malignant diagnoses, BI-RADS categories 2–5, and manual lesion segmentations. The authors also provide standardized patient-level folds for training and evaluation.

## What convinced me

The most valuable contribution is the unit of organization. The 1,875 images correspond to 722 benign and 342 malignant patient cases, so image-level random splitting would allow multiple images from one patient to cross partitions. Publishing fixed five- and ten-fold patient partitions removes a common source of leakage and makes comparisons between methods substantially more credible. The combination of pathology, clinical category, and masks also supports classification, segmentation, and concept-based analysis from the same cases.

## What it leaves open

The data are still from one clinical source, and the reference contours were produced within a limited annotation setting. Four scanners add acquisition variation but do not constitute external multi-institution validation. The class and BI-RADS distributions also reflect local biopsy and referral practice, which can become a shortcut if treated as universally representative.

## What I take from it

A public dataset should ship with its evaluation contract. For BUS-BRA, I would retain patient-wise folds, report scanner-stratified results, and reserve another institution for external testing. Dataset scale matters, but provenance and split discipline determine whether a performance claim is believable.
