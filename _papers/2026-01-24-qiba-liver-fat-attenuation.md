---
layout: post
title: "US Attenuation for Liver Fat Quantification: An AIUM-RSNA QIBA Pulse-Echo Quantitative Ultrasound Initiative"
date: 2026-01-24 12:00:00 +0900
venue: "Radiology"
authors: "Giovanna Ferraioli, Viksit Kumar, Arinc Ozturk, Kibo Nam, Chris L. de Korte, Richard G. Barr (2022)"
description: "A standards-body review on turning ultrasound attenuation and backscatter into a quantitative, reproducible liver-fat biomarker — the standardization work that any AI liver-steatosis model eventually has to sit on top of."
related_posts: false
---

**Paper.** *US Attenuation for Liver Fat Quantification: An AIUM-RSNA QIBA Pulse-Echo Quantitative Ultrasound Initiative* — [Radiology (2022)](https://doi.org/10.1148/radiol.210736)

## Why I read it

Most of the AI papers I've read on ultrasound-based liver-fat grading treat attenuation and backscatter as if they were already standardized, reliable inputs. This QIBA review is the actual standardization effort behind that assumption, and I wanted to understand how far along it really is and what confounders it's still contending with.

## What the paper claims

The Quantitative Imaging Biomarkers Alliance (QIBA) Pulse-Echo Quantitative Ultrasound (PEQUS) initiative reviews the state of standardizing attenuation coefficient, backscatter coefficient, and speed of sound as reproducible, cross-vendor quantitative biomarkers for hepatic steatosis, addressing sources of variability such as depth, probe pressure, and patient body habitus. It frames the clinical stakes: NAFLD affects roughly 30% of the general population and 55–80% of people with type 2 diabetes, with NASH incidence estimated at 12–26 per 1,000 person-years.

## What convinced me

The paper is explicit about which confounders (operator technique, machine settings, patient factors) still limit cross-site reproducibility of these quantitative US biomarkers, rather than presenting them as solved. That candor is useful, because it means a downstream AI model trained on attenuation measurements from one QIBA-participating site is not automatically getting a fully standardized input — the review itself documents the standardization is still in progress.

## What it leaves open

As a review and initiative-status paper rather than a validation study, it doesn't provide a single number for how reproducible attenuation measurement currently is across vendors and sites in practice — that evidence lives in the individual studies it surveys, not in this synthesis.

## What I take from it

Any AI paper using ultrasound attenuation or backscatter as a "quantitative" feature is implicitly relying on the QIBA standardization effort holding up across the specific machines and sites in its dataset — and per this review, that's a live, only-partially-solved problem, not settled infrastructure. It's a reminder to check, in any liver-US AI paper, how many scanners and sites the training data actually spans before trusting that the model's attenuation-based features generalize.
