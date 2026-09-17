---
layout: post
title: "EyePACS Digital Retinal Image Grading Protocol"
date: 2025-12-19 12:00:00 +0900
venue: "EyePACS Grading Protocol"
authors: "EyePACS"
description: "The internal grading manual behind the EyePACS diabetic-retinopathy dataset, the lesion-by-lesion rulebook that every EyePACS-trained DR model's labels ultimately trace back to."
og_image: "https://sehyeony0518.github.io/assets/img/og/2025-12-19-eyepacs-grading-protocol.png"
related_posts: false
---

**Document.** *EyePACS Digital Retinal Image Grading Protocol Narrative.*

This document addresses a question that benchmark tables often hide: how does a reader turn imperfect retinal photographs into disease labels? The answer matters before model training begins. A classifier evaluated against an overall diabetic-retinopathy grade is evaluated against a particular observation and aggregation procedure. Without understanding that procedure, it is difficult to distinguish a model error from a difference in available evidence, reader judgment, or the definition of the target.

The protocol is an operational manual, rather than a diagnostic-accuracy experiment. It specifies how readers assess lesions and how those assessments contribute to summary grades. There is no intervention group, randomized comparison, or single performance result to extract from it. Its contribution is to make the label-generating process inspectable. That is especially valuable when a downloaded dataset contains only images and an integer severity category.

Readers assess lesions including microaneurysms, hemorrhages, cotton-wool spots, intraretinal microvascular abnormalities, venous beading, neovascularization, and hard exudates. The website's algorithm combines lesion assessments into retinopathy and macular-edema summary grades. The described examination uses three photographic fields. Lesion certainty and the amount of visible retinal area therefore affect what can be recorded, rather than merely affecting the aesthetic quality of an image.

Several rules deserve precise reading. A suspected lesion is marked present when the reader is at least 50% certain. When more than half of the retinal area covered by the three fields is missing or obscured, the general rule is cannot grade. When less than half is unavailable, the reader assumes that the unseen portion resembles the visible portion. There is an important exception: specified high-risk lesions are graded when visible regardless of how much area is missing. Macular-edema grading uses hard exudates as a surrogate for thickening.

These rules expose several different forms of uncertainty. A reader may be unsure whether a visible object is a lesion. The relevant region may not be visible at all. Alternatively, an observed lesion may support only an indirect inference about the clinical condition. Collapsing these situations into one confidence value would discard information. They call for different responses: adjudication of an ambiguous observation, additional imaging of an unavailable region, or a reference examination that measures the target more directly.

The 50% certainty convention should not be interpreted as a calibrated probability statement. It instructs readers how to convert their judgment into a recorded answer. It does not demonstrate that lesions assigned that degree of certainty are present half the time, and it does not establish an optimal threshold for an automated detector. A model trained on those answers learns the resulting annotation target, including the consequences of the convention.

The coverage rule is similarly substantive. Inferring that an unseen region resembles a visible one is an assumption used to make grading possible under incomplete observation. It is not evidence that pathology is distributed uniformly. This creates a useful distinction between a grade supported by adequate coverage and one partly supported by an assumption about missing retina. If these cases are merged in evaluation, a model's apparent errors can be difficult to interpret.

The high-risk-lesion exception also prevents a simplistic implementation of gradability. An examination can contain actionable positive evidence despite being inadequate for confidently excluding other findings. Thus, “ungradable” should not automatically erase every lesion observation. For an AI dataset, I would want lesion presence and lesion assessability represented separately, with an examination-level rule specifying how those observations affect the final output. That is a proposed representation derived from the protocol, not a claim that every EyePACS release already provides it.

The main weakness of using the manual as evidence is that a written procedure does not demonstrate how consistently it was followed. It does not, on its own, quantify interreader agreement, establish the completeness of a particular dataset export, or prove that all datasets distributed under the EyePACS name used identical versions and adjudication procedures. Before asserting provenance for a benchmark, I would check its release documentation. The protocol provides a candidate specification to trace, not a universal guarantee about every downstream label.

The hard-exudate surrogate is particularly relevant to model interpretation. Success at predicting a photographic edema-risk label does not establish that a system measures retinal thickening or supports every clinical decision associated with diabetic macular edema. The input, reference, and intended claim must align. Conversely, a model may disagree with the surrogate label for reasons that cannot be resolved using the same photograph. More careful labeling does not eliminate the information limits of the modality.

This document strongly supports [Label Quality and Interobserver Variability]({{ '/study/label-quality-and-interobserver-variability/' | relative_url }}), which treats an annotation as a judgment made under a definition, information set, and reading procedure. It also gives operational content to [Clinical Feature Annotation and Multi-Task Learning]({{ '/study/clinical-feature-annotation-and-multi-task-learning/' | relative_url }}). Lesion-level supervision can make training and auditing more specific, but only if absence, uncertainty, missingness, and inability to assess are not silently treated as equivalent.

The connection to [Dataset Design, Ground Truth, and Reference Standards]({{ '/study/dataset-design-ground-truth-and-reference-standards/' | relative_url }}) is equally direct. A summary grade is the output of a reference process, and a photographic surrogate is a different target from a direct clinical measurement. Together with the CANet review, this manual makes me ask whether a model predicts the disease construct named in its title or the narrower construct actually encoded in its labels.

For my own annotation work, I would use the protocol as an example of the detail needed before asking experts to label images. Each finding needs an anatomical unit, an assessability rule, an uncertainty policy, and an explicit path into the final target. I would retain disagreements near these boundaries for separate review. The practical value of this document is that it moves label quality from a vague aspiration into decisions that can be examined, reproduced, and challenged.
