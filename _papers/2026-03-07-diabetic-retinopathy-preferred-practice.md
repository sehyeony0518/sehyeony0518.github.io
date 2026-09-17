---
layout: post
title: "Diabetic Retinopathy Preferred Practice Pattern"
date: 2026-03-07 12:00:00 +0900
venue: "American Academy of Ophthalmology"
authors: "American Academy of Ophthalmology, Retina/Vitreous PPP Panel (2024)"
description: "The clinical practice guideline that defines how diabetic retinopathy is actually meant to be screened, staged, and managed, the standard any AI screening tool is ultimately deployed to support, not replace."
og_image: "https://sehyeony0518.github.io/assets/img/og/2026-03-07-diabetic-retinopathy-preferred-practice.png"
related_posts: false
---

**Guideline.** *Diabetic Retinopathy Preferred Practice Pattern*, the version approved by the American Academy of Ophthalmology on September 13, 2024, published in [Ophthalmology 132(4), P75-P162 (2025)](https://doi.org/10.1016/j.ophtha.2024.12.020).

The question I bring to this guideline is what a diabetic-retinopathy prediction is supposed to accomplish in care. A benchmark asks whether a model agrees with a reference category. A clinical pathway must also decide whether the examination is adequate, whether further assessment is needed, how urgently the patient should be seen, and which information remains unavailable. Those decisions give the classification task its meaning.

This is a guideline rather than a single diagnostic experiment. It synthesizes evidence and expert recommendations for detection, assessment, follow-up, treatment, and counseling. There is no single study population, model comparison, or effect size that summarizes its contribution. Reading it as if it were one cohort study would miss its purpose: organizing clinical decisions across different patient circumstances.

The document distinguishes retinopathy severity from macular edema and places ocular findings within a broader assessment that includes symptoms, treatment history, and systemic context. It also discusses screening approaches, including image-based and automated systems. These elements help identify where an AI component might fit, but the guideline does not validate a particular research model merely because that model predicts a familiar disease category.

The open problem for an AI developer is the translation from this clinical framework into an observable task. Screening for a referral-relevant finding, reproducing an image grade, predicting progression, and recommending management are different tasks. They require different inputs and references. A system trained for one should not silently acquire the claims of the others when it is described as a diabetic-retinopathy model.

The first practical distinction is between the patient and the available photograph. A disease diagnosis concerns the patient or eye. A model may receive only one selected image. That image can support some observations while leaving other regions or properties unavailable. A correct label attached at the patient level does not guarantee that every selected image contains sufficient evidence for it.

Gradability therefore belongs in the pathway itself. Excluding poor-quality examinations from a retrospective test can be appropriate for a narrow image-classification study, but it removes a class of cases that a screening service still has to handle. A usable system needs a specified response when it cannot make an adequate assessment. The response might involve further acquisition or clinical review, and its consequences should be included in evaluation.

The EyePACS grading protocol provides a complementary perspective. It makes particular photographic observation rules explicit, including how visible lesions and incomplete coverage affect grading. The Preferred Practice Pattern places such observations in a larger clinical context. The two documents should not be merged into a claim that reproducing one photographic protocol is equivalent to satisfying the entire clinical guideline.

Macular edema is a good example of why the distinction matters. A photographic surrogate label, an assessment of retinal thickening, and a management decision are related but different targets. A model can be evaluated accurately against the first without establishing the latter two. The CANet review therefore needs this guideline as a boundary on the interpretation of joint DR and DME grading.

The strongest value of the guideline for research is its ability to expose missing parts of a proposed workflow. A paper may report excellent five-class accuracy while saying little about failed acquisition, prior treatment, symptoms outside the image, or the next action after a positive result. These omissions are not automatically flaws in a narrowly framed algorithm experiment. They become flaws when the paper makes a broader clinical-use claim.

A careful reader should also distinguish the authority of a guideline from certainty about every implementation choice. Recommendations synthesize evidence for specified circumstances, and applying them locally requires decisions about the population, available equipment, staff, and follow-up resources. The guideline is not a complete machine-readable ontology or a ready-made loss function. Turning its prose into labels necessarily adds operational choices that should be documented.

That translation can create errors even when the underlying model is statistically sound. If a service defines the referral target differently from the training dataset, apparent model disagreement may partly be target mismatch. If an output is presented as a management recommendation while the model observes only a photograph, the missing information may be structural rather than a problem that more training can solve.

This document strongly supports [From Clinical Problem to Machine Learning Task]({{ '/study/from-clinical-problem-to-machine-learning-task/' | relative_url }}). That note requires a decision, target, prediction unit, population, input boundary, reference, and operating rule. The guideline supplies clinical context for making those choices. It also prevents a convenient public label from defining the research question by default.

[Clinical Validity and Clinical Utility]({{ '/study/clinical-validity-and-clinical-utility/' | relative_url }}) explains the next distinction. Agreement with a suitable reference can establish a form of validity, but utility concerns what happens when the output changes care. A screening system can be accurate yet fail to improve outcomes if positive patients do not receive follow-up, if ungradable cases disappear from the workflow, or if the added review burden overwhelms available capacity.

[Calibration, Uncertainty, and Selective Prediction]({{ '/study/calibration-uncertainty-and-selective-prediction/' | relative_url }}) is relevant to any proposed confidence-based referral or abstention rule. Rejected cases remain part of the clinical system. Their outcomes and workload cannot be omitted simply because the automated component declined to classify them. A selective system should be evaluated together with the process receiving those cases.

For a retinal AI study, I would use the guideline to write a task specification before choosing the headline metric. I would state which decision the system supports, what it observes, which patients are eligible, and what happens after each possible output. Evaluation would include the complete denominator of eligible examinations, with separate reporting for inadequate inputs and unresolved assessments.

The broader lesson transfers to my ultrasound work. Clinical guidance is most useful when it constrains the research claim and reveals missing information. It can help define an appropriate task and comparison, but it cannot substitute for evidence that a particular AI-supported pathway works. The benchmark label is one part of that pathway, and the clinical question determines how much more must be evaluated.
