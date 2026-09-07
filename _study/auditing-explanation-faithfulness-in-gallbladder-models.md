---
layout: study_note
title: "Auditing Explanation Faithfulness in Gallbladder Models"
description: "Testing whether a model's evidence tracks independent clinical factors, without retraining."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "hepatobiliary"
category_title: "Hepatobiliary Medicine & Imaging"
subgroup: "Clinical-to-AI Connections"
order: 19
source: "Independent study"
written: true
updated: "2026-09-08"
---

An explanation audit asks whether a gallbladder model's reported evidence reflects its prediction process and aligns with independently assessed clinical findings. Anatomical plausibility, computational faithfulness, and clinical relevance are separate properties.

## Clinical overview

A heatmap over the gallbladder may look reasonable while highlighting a measurement marker or a broad organ boundary. Conversely, a clinically relevant posterior shadow extends beyond the lesion itself. I therefore would not define a successful explanation as one that simply stays inside an organ or lesion mask.

The clinical task determines the evidence expected. Stone detection, characterization of wall thickening, and estimation of malignant likelihood need different findings. [Liu and colleagues](https://pubmed.ncbi.nlm.nih.gov/35396183/) frame medical algorithmic auditing around the clinical task, potential errors, and their consequences. I take that framework as a starting point, not as a validated gallbladder-specific faithfulness test.

## Anatomy and pathophysiology

Clinical evidence can occupy several compartments: intraluminal material, the gallbladder wall, adjacent tissue, and posterior acoustic effects. It can also depend on dynamics, such as mobility, that a still image does not contain. A feature's anatomical location is therefore only one part of what makes it relevant.

The same broad appearance can arise from different processes. Wall thickening can accompany inflammation, edema, benign remodeling, or malignancy. An explanation concentrating on a thick wall does not establish that the model distinguished those causes. I would ask which more specific findings are visible and what diagnostic claim they can support.

## Diagnostic workflow and imaging findings

### Define clinical factors independently

Before inspecting model explanations, readers should define and assess factors such as lesion attachment, margin irregularity, intramural cysts, shadowing, and focal versus diffuse wall change. Feature presence and visibility need separate records. When feasible, readers assessing morphology should be blinded to model outputs and final diagnosis. Independent here means that the reference was not constructed from the explanation being evaluated; it does not make the annotation error-free.

### Match each factor to its actual evidence

Annotations should identify supporting frames or regions and distinguish image findings from examination-level observations. A mobility label requires relevant temporal evidence. A posterior-shadow annotation should include the acoustic effect and its relationship to the suspected source. I would retain uncertain and unassessable cases, since excluding them could make the audit easier than the intended clinical setting.

### Review competing explanations for the finding

A highlighted region may contain anatomy, an overlay, and an acquisition artifact together. A broad response to wall thickness could reflect physiological contraction rather than disease-specific morphology. Clinical review should therefore record plausible alternatives before assigning meaning to the attribution. This step establishes what the image supports; it does not reveal the model's internal computation.

### Define clinically interpretable comparisons

I would plan comparisons that preserve the relevant question: the same frame with a removable overlay, adequate views of the same finding, or cases with comparable morphology but different acquisition settings. These are proposed audit contrasts. Different patients are not interchangeable counterfactuals, and a synthetic edit is not a clinical intervention unless the affected evidence and unintended changes have been carefully assessed.

## Differential diagnosis and management context

An explanation does not resolve an indeterminate lesion or replace the usual diagnostic workup. When clinical findings and model evidence disagree, the possibilities include model error, explanation failure, inadequate imaging, and imperfect annotation. The discrepancy should trigger case review rather than an automatic judgment that either the clinician or the model is correct.

## Implications for medical AI

I would freeze model weights, preprocessing, and the output being explained. For a reviewed transformation T, the paired score change Δ = s(T(x)) − s(x) measures sensitivity to that edit. I would compare it with the explanation's predicted importance and with control edits of similar extent. [Yeh and colleagues](https://papers.nips.cc/paper_files/paper/2019/hash/a7471fdc77b3435276507cc8f2dc2569-Abstract.html) formalize relationships between explanations and perturbation-induced output changes. The result remains conditional on the perturbation design; masking tissue can create unrealistic inputs.

Separately, I would test whether predefined attribution summaries, such as absolute attribution within an annotated region, track independently annotated clinical factors, accounting for region size, visibility, and acquisition differences. I would estimate uncertainty at the patient level and prespecify primary comparisons. Such associations support alignment, not causal reliance. Shuffled-factor and simple spatial baselines can reveal trivial agreement. [Adebayo and colleagues](https://papers.nips.cc/paper_files/paper/2018/hash/294a8ed24b1ad22ec2e7efea049b8737-Abstract.html) show why visually convincing saliency requires sanity checks. My aim is converging evidence from clinical annotation, prediction changes, and explanation behavior without retraining. Remaining failures should be reported by clinical factor and case type, rather than compressed into one faithfulness score.

## References

- Liu et al., [The medical algorithmic audit](https://pubmed.ncbi.nlm.nih.gov/35396183/), The Lancet Digital Health 2022.
- Yeh et al., [On the (In)fidelity and Sensitivity of Explanations](https://papers.nips.cc/paper_files/paper/2019/hash/a7471fdc77b3435276507cc8f2dc2569-Abstract.html), NeurIPS 2019.
- Adebayo et al., [Sanity Checks for Saliency Maps](https://papers.nips.cc/paper_files/paper/2018/hash/294a8ed24b1ad22ec2e7efea049b8737-Abstract.html), NeurIPS 2018.
