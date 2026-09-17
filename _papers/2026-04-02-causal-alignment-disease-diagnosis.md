---
layout: post
title: "Learning Causal Alignment for Reliable Disease Diagnosis"
date: 2026-04-02 12:00:00 +0900
venue: "ICLR 2025"
authors: "Mingzhou Liu, Ching-Wen Lee, Xinwei Sun, Xueqing Yu, Qiao Yu, Yizhou Wang (2025)"
description: "A causal framing of the shortcut-learning problem in disease diagnosis, trying to explicitly align a model's learned representation with the causal structure of disease, not just penalize known spurious features after the fact."
og_image: "https://sehyeony0518.github.io/assets/img/og/2026-04-02-causal-alignment-disease-diagnosis.png"
related_posts: false
---

**Paper.** *Learning Causal Alignment for Reliable Disease Diagnosis*. [ICLR conference paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ce9d51dded7dac82b3b4d3dbb1d73bc-Paper-Conference.pdf)

The front-matter author field says “Qiao Yu”; the conference paper lists “Yu Qiao.”

## What kind of alignment is being sought?

A diagnostic model can predict an expert's label without following the expert's reasoning. Even a model whose heatmap overlaps a lesion might depend on a marker, background texture, or acquisition convention. The open question is how to make expert evidence constrain the decision process itself.

The paper approaches this through counterfactual changes: which modifications would make the model change its answer, and do those modifications concern the evidence experts identify? This gives alignment a behavioral motivation. It is more specific than asking whether a visualization looks clinically plausible.

For my work, the important distinction is between explaining a trained classifier's response and identifying the biological causes of disease. The paper's counterfactuals primarily address the former. Its diagnostic hierarchy is a model of how image evidence supports a decision, which should not be confused with the direction in which disease generates anatomy.

## What the method does

The basic alignment loss penalizes counterfactual image changes outside expert-annotated regions. The hierarchical version predicts attributes from images and diagnoses from those attributes, applying alignment at both stages. Counterfactuals are obtained through optimization, and implicit differentiation allows the alignment objective to influence training.

Experiments use LIDC-IDRI lung nodules and CBIS-DDSM breast masses. Artificial plus/minus symbols agree with labels during training and are randomized during validation and testing. The LIDC task derives its binary target from radiologist malignancy scores, grouping scores 1–3 together and 4–5 together. [Study design](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ce9d51dded7dac82b3b4d3dbb1d73bc-Paper-Conference.pdf)

The two-stage structure matters. Attribute prediction is on the diagnostic path, rather than merely displayed beside an unrestricted diagnosis head. That gives the model an inspectable intermediate interface.

It also creates two separate obligations. The image-to-attribute model must recognize the intended findings, and the attribute-to-diagnosis model must combine them appropriately. Accurate diagnosis cannot establish either obligation by itself.

## What the results establish

The reported CAM precision is 0.751 on LIDC and 0.805 on DDSM, with classification accuracies of 0.722 and 0.656. Ablations improve when alignment is introduced and improve further with the hierarchical procedure. These are results under the paper's labels, annotations, architecture, and shortcut design. [Results and ablations](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ce9d51dded7dac82b3b4d3dbb1d73bc-Paper-Conference.pdf)

The artificial-symbol experiment is valuable because the training rule is deliberately made unreliable at evaluation. A model cannot maintain performance simply by continuing to trust the symbol-label association.

However, the result should not be described as a direct demonstration of pathology-based lung-cancer diagnosis. In the stated LIDC task, the target is a thresholded expert suspicion score. Agreement with that target evaluates reproduction of a particular annotation convention, including its handling of intermediate scores.

The ablation also evaluates a training procedure. It does not show that the same individual prediction would change appropriately after correcting a particular attribute. That requires a separate intervention on the fitted system.

## The causal assumptions deserve close reading

The hierarchical causal attribution depends on assumptions about the attribute-to-label relationship, including absence of confounding and monotonicity in the specified attribute coding. Those assumptions are part of the model, not findings established by the reported accuracy.

A clinical descriptor may have different implications depending on accompanying findings, visibility, or population. If a binary attribute is expected always to increase suspicion while other attributes remain fixed, that is a stronger proposition than observing a positive association in the dataset.

Completeness is equally consequential. An expert may use information omitted from the annotated attribute vocabulary. A model forced through an incomplete interface could lose valid evidence or encode additional information in continuous attribute scores.

The latter possibility is particularly relevant to auditability. A displayed attribute category can look correct while its underlying numerical value carries other information. A transparent label on an intermediate variable does not guarantee that all variation in that variable has the advertised meaning.

## Counterfactual validity is the central weakness

An optimized image that flips a prediction establishes that the implemented optimization found a successful change. To interpret the change as clinical evidence, I need to know whether it selectively altered the named finding and preserved relevant alternatives.

Visual realism is insufficient. A realistic counterfactual might change lesion texture and background processing together. Conversely, a small modification might exploit a classifier sensitivity that has no plausible clinical counterpart.

Restricting changes to an expert region helps constrain location, but location does not determine semantics. A lesion region contains disease morphology, noise, reconstruction effects, and potentially annotation artifacts. A counterfactual can remain inside the region while using the wrong kind of information.

CAM precision leaves another gap. Concentrating attribution inside an annotated area measures localization. It does not establish complete coverage of useful evidence, correct attribute recognition, or an appropriate response to a clinically meaningful edit.

I therefore read the results as evidence for supervised computational alignment under explicit assumptions. The stronger clinical interpretation remains something to test.

## Connections to the study notes

[Clinical Alignment and Knowledge as Supervision](/study/clinical-alignment-and-knowledge-as-supervision/) distinguishes auxiliary supervision, architectural restrictions, and behavioral constraints. This paper combines several of them. It supports using knowledge during training, while illustrating why improved localization and improved diagnosis should be evaluated separately.

[Causal Inference for Medical AI](/study/causal-inference-for-medical-ai/) distinguishes interventions on software inputs from interventions on patients or acquisition processes. The counterfactual generator changes the model's evidence representation. Extending that result to clinical causation requires additional assumptions about the generated changes.

[Clinical Concepts and Concept-Based Interpretability](/study/clinical-concepts-and-concept-based-interpretability/) emphasizes the meaning and intervention behavior of concept outputs. The hierarchy creates a useful testing interface, but its concept values still require independent validation.

## How I would extend the evaluation

For a gallbladder application, I would begin with a small, independently annotated attribute set whose assessability is recorded explicitly. I would compare diagnosis performance, attribute accuracy, and controlled nuisance sensitivity, rather than combine them into one alignment score.

I would then correct individual predicted attributes in a frozen model and examine whether diagnostic changes follow the intended clinical relationship. Separately, readers would assess generated image edits for both target changes and unintended changes.

Finally, I would test naturally occurring acquisition variation. Success against an inserted symbol is a useful control; diffuse changes in speckle, view selection, and lesion visibility demand their own evidence.
