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

I keep encountering breast-ultrasound CAD papers reporting numbers on datasets I can't fully verify — unclear how many scanners, whether malignancy status is biopsy-confirmed, or whether the train/test split is standardized enough to compare across papers. BUS-BRA is explicitly a dataset paper built to fix that, so I wanted to know exactly what it standardizes.

## What the paper claims

BUS-BRA provides 1,875 anonymized breast ultrasound images from 1,064 patients at Rio de Janeiro's National Institute of Cancer, acquired across four different ultrasound scanners, with 722 benign and 342 malignant cases confirmed by biopsy. Each image carries a BI-RADS category (2–5) assigned by a senior sonographer, a manual lesion segmentation, and — critically — standardized 5-fold and 10-fold cross-validation partitions released with the dataset so different papers' reported numbers are directly comparable.

## What convinced me

Multi-scanner acquisition combined with biopsy-confirmed labels and a senior sonographer's BI-RADS assignment is a stronger foundation than many single-scanner, single-reader breast-US datasets I've read papers built on. And releasing fixed CV partitions is a small but disproportionately useful contribution — it removes one common source of inflated, incomparable benchmark numbers across papers that each roll their own random split.

## What it leaves open

Multi-scanner acquisition helps but doesn't fully solve generalization — four scanners at one institution is still a narrow slice of the equipment and patient-population diversity a deployed CAD system would face. The paper doesn't report how much performance varies by scanner within the dataset itself, which would be useful for gauging expected external-site drop-off.

## What I take from it

Standardized splits and biopsy-confirmed, multi-scanner labels are exactly the dataset-hygiene details I now check for before trusting a breast-ultrasound benchmark comparison across papers. When two CAD papers report different AUCs on "the same dataset," the first thing I check is whether they actually used the same partition — and a paper like this, that ships the partition itself, removes that ambiguity for anyone using it going forward.
