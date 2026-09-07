---
layout: study_note
title: "Allergy and Clinical Immunology"
description: "Diagnostic testing with imperfect specificity, and the role of clinical history in interpreting a result."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "rheum-immunology"
category_title: "Rheumatology & Clinical Immunology"
order: 2
source: "Lecture"
written: true
updated: "2026-09-08"
---

Allergy is an immune-mediated hypersensitivity that produces clinically relevant symptoms after exposure. I focus on IgE-mediated allergy, particularly food allergy, where a positive sensitization test and a demonstrated clinical reaction are different findings.

## Clinical overview

Allergic disease can involve the skin, airways, gastrointestinal tract, or circulation. A history of hives after a particular food raises a different question from chronic nasal symptoms or recurrent infections. Clinical immunology also includes immune deficiency and immune dysregulation, which require different diagnostic pathways.

The practical starting point is what happened, after which exposure, and under what circumstances. The [EAACI diagnostic guideline](https://doi.org/10.1111/all.15902) places an allergy-focused history before targeted sensitization testing. I read this ordering as essential: testing is meant to investigate a clinical hypothesis, not generate an unrestricted list of substances to avoid.

## Anatomy and pathophysiology

In IgE-mediated reactions, allergen recognition can activate mast cells and basophils, releasing mediators that affect blood vessels, smooth muscle, and mucosal tissues. The resulting manifestations depend on the organs involved. Sensitization means that an immune response to an allergen can be demonstrated; symptoms on exposure are a separate requirement for clinical allergy.

Other immune mechanisms can produce delayed reactions, and nonimmune intolerance can resemble allergy. The [NIAID-sponsored food-allergy guideline](https://pubmed.ncbi.nlm.nih.gov/21134576/) distinguishes these categories. A test designed to detect specific IgE cannot settle every adverse reaction to food or medication.

## Diagnostic workflow and imaging findings

### Reconstruct the exposure and reaction

History should document the suspected trigger, timing, reproducibility, amount and preparation where relevant, symptoms, treatment, and recovery. Exercise, alcohol, intercurrent illness, and medications can modify some reactions. Prior tolerance and subsequent exposure also matter. The absence of symptoms during one exposure needs interpretation in that context.

### Match examination to the organ system

Examination may show wheals, angioedema, eczema, nasal inflammation, or respiratory findings, but it can be normal between episodes. Photographs can document transient skin changes, although they cannot establish the trigger or mechanism. Imaging is not a routine confirmation test for IgE-mediated food allergy; it is reserved for a separate anatomical or differential-diagnosis question.

### Interpret sensitization tests with appropriate controls

Skin-prick testing assesses an immediate skin response, while serum testing measures allergen-specific IgE. Skin-test interpretation requires positive and negative controls and attention to factors such as antihistamine use. Broad testing in someone with little supporting history increases the chance of clinically irrelevant positive results. Wheal size or IgE concentration does not independently predict the severity of the next reaction.

### Resolve uncertainty with the appropriate reference

Component-specific IgE testing can clarify selected sensitization patterns, including cross-reactivity, but remains part of a clinical interpretation. EAACI identifies a medically supervised oral food challenge as the reference standard when food-allergy diagnosis remains uncertain. A challenge requires specialist assessment of suitability and safety. An open challenge is often sufficient clinically; blinded procedures can address equivocal outcomes or research questions.

## Differential diagnosis and management context

Food intolerance, infection, toxic reactions, chronic spontaneous urticaria, and other conditions can resemble allergy. Angioedema also has mechanisms that are not IgE-mediated. An allergy label should retain the implicated exposure and supporting evidence, rather than turn every adverse event into the same diagnosis.

Anaphylaxis is a clinical emergency. Skin signs may be absent, and treatment should not wait for laboratory confirmation. The [World Allergy Organization guidance](https://doi.org/10.1016/j.waojou.2020.100472) identifies intramuscular epinephrine as first-line treatment. Subsequent care includes assessment of the trigger, recurrence prevention, and an individualized emergency plan. Long-term management should avoid unnecessary restrictions as well as dangerous re-exposure.

## Implications for medical AI

I would distinguish prediction of sensitization, challenge-confirmed allergy, a documented reaction, and future severe reactions. These labels are not interchangeable. Patients selected for challenge differ from those diagnosed from a convincing history, so a challenge-based dataset may not represent the entire clinic population.

This suggests to me a useful parallel with clinical faithfulness auditing: a model can predict a positive test without identifying the evidence that makes it clinically meaningful. I would preserve exposure history, testing indication, reference method, and unresolved cases. As in gallbladder ultrasound, a plausible visible finding needs its relationship to the clinical decision demonstrated separately.

## References

- Santos et al., [EAACI guidelines on the diagnosis of IgE-mediated food allergy](https://doi.org/10.1111/all.15902), Allergy 2023.
- NIAID-Sponsored Expert Panel, Boyce et al., [Guidelines for the diagnosis and management of food allergy in the United States: report of the NIAID-sponsored expert panel](https://pubmed.ncbi.nlm.nih.gov/21134576/), Journal of Allergy and Clinical Immunology 2010.
- Cardona et al., [World allergy organization anaphylaxis guidance 2020](https://doi.org/10.1016/j.waojou.2020.100472), World Allergy Organization Journal 2020.
