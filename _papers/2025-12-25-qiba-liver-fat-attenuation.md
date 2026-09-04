---
layout: post
title: "US Attenuation for Liver Fat Quantification: An AIUM-RSNA QIBA Pulse-Echo Quantitative Ultrasound Initiative"
date: 2025-12-25 12:00:00 +0900
venue: "Radiology"
authors: "Giovanna Ferraioli, Viksit Kumar, Arinc Ozturk, Kibo Nam, Chris L. de Korte, Richard G. Barr (2022)"
description: "A standards-body review on turning ultrasound attenuation and backscatter into a quantitative, reproducible liver-fat biomarker, the standardization work that any AI liver-steatosis model eventually has to sit on top of."
related_posts: false
---

**Paper.** *US Attenuation for Liver Fat Quantification: An AIUM-RSNA QIBA Pulse-Echo Quantitative Ultrasound Initiative*. [Radiology (2022)](https://doi.org/10.1148/radiol.210736)

## Why I read it

A learned ultrasound model is only as portable as the measurement process that produced its inputs. I read this QIBA review because it treats acquisition protocol, confounding factors, repeatability, and cross-vendor standardization as part of the biomarker, not as technical details outside the model.

## What the paper claims

The initiative reviews attenuation imaging for liver-fat quantification and places it alongside backscatter coefficient and speed of sound as quantitative ultrasound candidates. It summarizes the physics, acquisition recommendations, reference standards, reported diagnostic performance, and unresolved sources of variability that must be addressed before attenuation can function as a standardized biomarker.

## What convinced me

Across the reviewed studies, attenuation methods often achieved strong discrimination for steatosis, with representative AUC around 0.91, and repeatability estimates were generally high, with reported ICCs roughly in the 0.81–0.98 range. At the same time, results and thresholds varied by system, protocol, region-of-interest placement, and reference standard. That combination, promising accuracy but incomplete interchangeability, is exactly why a technical profile is needed.

## What it leaves open

The paper is a review and expert statement, not a single prospective multicenter validation. Different implementations of attenuation are not automatically comparable, and biopsy and MRI-based references have different limitations. Vendor-specific cutoffs, body habitus, depth, and coexisting fibrosis can affect estimates.

## What I take from it

For quantitative ultrasound AI, the acquisition pipeline belongs inside the validation claim. I would report device and protocol, repeat scans, operator effects, calibration or phantom procedures, and external reproducibility. A model cannot be clinically faithful to a biomarker whose own measurement conditions are undefined.
