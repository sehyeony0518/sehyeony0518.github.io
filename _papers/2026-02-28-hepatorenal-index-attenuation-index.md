---
layout: post
title: "Noninvasive Quantitative Estimation of Hepatic Steatosis: Hepatorenal Index vs. Attenuation Index"
date: 2026-02-28 12:00:00 +0900
venue: "Medical Ultrasonography"
authors: "Heon-Ju Kwon, Kyoung Won Kim, Jin-Hee Jung, Sang Hyun Choi, Woo Kyoung Jeong, Bohyun Kim, Gi-Won Song, Sung-Gyu Lee (2016)"
description: "A head-to-head comparison of two classical ultrasound-based liver-fat indices in living liver-donor candidates, against biopsy — the pair of legible baselines that any liver-steatosis deep model is implicitly competing with."
related_posts: false
---

**Paper.** *Noninvasive quantitative estimation of hepatic steatosis by ultrasound: a comparison of the hepatorenal index and ultrasound attenuation index* — [Medical Ultrasonography (2016)](https://doi.org/10.11152/mu-868)

## Why I read it

The hepatorenal index (HRI) and ultrasound attenuation index (USAI) recur as baselines across nearly every liver-steatosis AI paper I've read. This paper compares the two directly against biopsy in a well-defined population — potential living liver-donor candidates, who by necessity get both imaging and histology — so I wanted the actual comparative numbers rather than each index's isolated validation study.

## What the paper claims

In 224 potential living hepatic donors who underwent both ultrasound and liver biopsy, the authors compare the diagnostic accuracy of HRI (liver-to-kidney echogenicity ratio) against USAI (attenuation-based) for detecting hepatic steatosis, using biopsy as the reference standard.

## What convinced me

Using a living-donor cohort is a methodologically clean choice for this specific comparison: donor candidates get biopsied essentially as a matter of course, independent of clinical suspicion of liver disease, which avoids the referral bias that affects steatosis studies drawing on patients biopsied because disease was already suspected.

## What it leaves open

A donor-candidate population is healthier and has a narrower range of steatosis severity than a general NAFLD clinical population, which limits how far the reported accuracy generalizes to patients being screened for suspected fatty liver disease rather than pre-transplant clearance. The paper also doesn't test whether combining HRI and USAI outperforms either alone.

## What I take from it

Both HRI and USAI are simple, single-number, fully legible quantities computed directly from standard ultrasound images — exactly the kind of baseline a "the AI model beat classical ultrasound indices" claim should be benchmarked against, and exactly the comparison I look for (and am often disappointed not to find) in newer deep-learning liver-steatosis papers. A model's real contribution should be measured against this pair, in the same population, not against a vaguer "clinical assessment" baseline.
