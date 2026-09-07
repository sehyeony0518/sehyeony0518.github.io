---
layout: study_note
title: "Clinical Alignment and Knowledge as Supervision"
description: "Using clinical knowledge to shape what a model learns, rather than only to judge it afterwards."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "alignment"
category_title: "Clinical Alignment & Interpretability"
order: 1
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-11-29-concept-bottleneck-models"
  - "2026-02-03-right-for-the-right-reasons"
---

Clinical alignment uses clinical knowledge to shape a model's learning objective, representation, or decision pathway. The question is whether the resulting behavior reflects the intended evidence, not merely whether its outputs agree with diagnostic labels.

## Core question and definition

I use alignment here in a task-specific sense. For a gallbladder classifier, the relevant knowledge might concern lesion attachment, wall architecture, posterior acoustics, and examination limitations. Alignment means meeting explicitly stated expectations about those factors. It does not mean agreement with every clinician, and it is not established by an anatomically plausible heatmap.

Knowledge becomes supervision when it changes training rather than serving only as an evaluation reference. That change can involve feature labels, anatomical regions, consistency constraints, or restrictions on how predictions are formed. Each choice turns a clinical assumption into a modeling assumption that needs examination.

## Key concepts

### Supervision has several forms

A diagnosis supplies an outcome target; a segmentation supplies spatial information; a clinical feature supplies a semantic target. These are different kinds of evidence. A possible multi-task objective is $$L = L_{\text{diagnosis}} + \sum_j \lambda_j L_{\text{feature},j}$$. The weights $$\lambda_j$$ control optimization tradeoffs, not clinical importance by definition. Unassessable features require explicit handling rather than being coded as absent.

### Constraints can target model behavior

Knowledge can specify where sensitivity should be discouraged or which changes should leave a prediction stable. [Ross and colleagues](https://doi.org/10.24963/ijcai.2017/371) regularized input gradients using explanatory annotations. I read this as a concrete mechanism for influencing local sensitivity, with a limited guarantee: a small gradient in a prohibited region does not establish invariance to every finite change there.

### Architecture can make supervision consequential

In a concept bottleneck, predicted concepts feed the final decision: $$x \rightarrow \hat{c} \rightarrow \hat{y}$$. [Koh and colleagues](https://proceedings.mlr.press/v119/koh20a.html) study this explicit pathway. An auxiliary concept head attached to a shared representation does not impose the same dependency. Even a bottleneck requires scrutiny, because inaccurate or overly expressive concept values may convey information beyond their intended clinical meaning.

### Clinical knowledge is incomplete and contextual

The same feature can support different interpretations depending on anatomy, preparation, and competing findings. Knowledge supervision should distinguish a descriptive observation from a diagnostic rule. I would preserve uncertainty and disagreement rather than make the model learn an artificial consensus. Constraints that fit common cases may suppress rare but clinically important exceptions.

## Worked examples in medical AI

Koh and colleagues included radiographic osteoarthritis grading using clinical concepts such as bone spurs. This provides a published example of predicting interpretable findings before the outcome. It does not establish that the same concept vocabulary or architecture will work for gallbladder ultrasound, where visibility and acquisition dependence require separate study.

In a hypothetical gallbladder model, I would supervise lesion location, attachment, and wall findings alongside diagnosis. A shadow could be clinically informative outside the lesion mask, so a rule penalizing all extralesional attention would encode the wrong expectation. The supervision would need to describe the acoustic relationship, not merely the organ boundary. Cases with benign remodeling and a separate suspicious lesion would test whether the learned prior is too restrictive.

## Evaluation methods and limitations

I would compare knowledge-guided training with an otherwise comparable baseline, accounting for the extra annotation and tuning effort. Evaluation should include diagnosis, feature recognition, calibration, and performance across acquisition settings. Better diagnostic accuracy alone cannot identify which part of the added supervision helped.

Independent feature assessment and targeted intervention tests are needed to examine reliance. Training labels should not also function as an unquestioned audit reference. Ablating a supervision term can show its contribution to a training procedure, but does not directly reveal the mechanism of one fitted model. Annotation error, missingness, and disagreement can propagate through every stage.

## Research connections and open questions

For my clinical faithfulness work, knowledge supervision is a proposed way to make the intended evidence explicit before training. I would still audit the resulting gallbladder model independently, because alignment is a claim to test rather than a property conferred by a clinical vocabulary.

- Which gallbladder features are sufficiently observable and reproducible to supervise without manufacturing certainty?
- How should a model represent clinically relevant evidence that lies outside a lesion mask or requires multiple views?
- When do knowledge constraints improve reliance, and when do they merely make a familiar explanation easier to display?

## References

- Ross, Hughes, and Doshi-Velez, [Right for the Right Reasons: Training Differentiable Models by Constraining their Explanations](https://doi.org/10.24963/ijcai.2017/371), IJCAI 2017.
- Koh et al., [Concept Bottleneck Models](https://proceedings.mlr.press/v119/koh20a.html), ICML 2020.
