---
layout: study_note
title: "Auditable-by-Design Medical AI"
description: "Building models whose evidence can be checked, instead of auditing whatever is left afterwards."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "auditing"
category_title: "Evidence Auditing"
order: 5
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-11-29-concept-bottleneck-models"
---

I want an unexpected prediction to leave enough evidence for someone else to reconstruct it, challenge its intermediate claims, and test a suspected dependency. Auditability begins with deciding which questions the system must remain capable of answering.

## Core question and definition

I use auditable-by-design medical AI to mean a system whose development and operation preserve the information and interfaces needed for predefined audits. This includes input provenance, reproducible computation, independently assessable evidence claims, and controlled access to the prediction pathway.

Auditability is distinct from clinical validity. Reproducing an incorrect malignancy score establishes computational traceability, not diagnostic reliability. Likewise, exposing a concept called “wall irregularity” does not establish that its numerical value measures irregularity.

For a gallbladder classifier, I would specify several claims separately: the score came from these examination frames; this intermediate output represents an assessable finding; this finding influences the diagnostic output; and changing a documentation cue does not materially change the result under a defined test. Each claim requires different evidence. A system becomes easier to audit when those requirements influence data collection and architecture before training.

## Key concepts

### Define the decision before defining the interface

The input contract should identify the patient population, prediction time, unit of analysis, permitted information, and intended output. Characterizing an already identified gallbladder lesion is different from finding lesions during an examination. The former may legitimately receive an operator-selected view; the latter cannot assume that someone has already located and measured the abnormality.

I would record whether the system accepts still frames, cine clips, or an examination assembled from several views. For an examination-level prediction, frame selection and aggregation belong to the model specification. Taking the maximum frame score makes an additional saved frame capable of changing the examination result.

[Model Cards](https://doi.org/10.1145/3287560.3287596) provide a reporting framework for intended uses, evaluation conditions, and limitations. My implementation would connect those statements to actual input checks and retained examples, so that an intended-use description can be tested against what the application accepts.

### Expose a pathway whose semantics can be challenged

A concept bottleneck model separates concept prediction from diagnostic prediction:

$$
\hat{\mathbf c}=h_\theta(x), \qquad \hat p=g_\phi(\hat{\mathbf c}).
$$

Here, $$x$$ is the image input, $$h_\theta$$ predicts a vector of declared concepts, and $$g_\phi$$ maps that vector to a disease probability $$\hat p$$. The parameters $$\theta$$ and $$\phi$$ belong to the two stages. [Koh and colleagues](https://proceedings.mlr.press/v119/koh20a.html) demonstrate this structure and interventions that replace predicted concept values before recomputing the output.

For my task, candidate concepts could include focal wall thickening, attachment morphology, and visible intramural cystic spaces. Their annotation definitions need to specify the relevant view and whether presence can actually be judged. “Not assessable” should remain distinct from “absent.”

An auxiliary concept head is different: if the diagnostic head also receives unrestricted image features, displaying concepts does not make them the complete decision pathway. I would document that bypass explicitly and test its contribution.

### A named bottleneck can still transmit unnamed information

Continuous concept scores have more capacity than their displayed labels suggest. Two images can receive the same displayed category while differing in the underlying numerical outputs used by the diagnostic head. Those differences might encode morphology, acquisition, or another unlabelled property.

[Mahinpei and colleagues](https://arxiv.org/abs/2106.13314) show that learned concept representations can contain information beyond the predefined concepts. I read this as a reason to audit semantics at the actual interface used by the classifier.

I would compare predictions obtained from continuous concept estimates, their declared categorical versions, and independent reader annotations. A performance difference would identify a question about information transmission. It would not, by itself, establish that the extra information is a shortcut: reader annotations may also be coarse or incomplete.

### Preserve the complete computational record

For each audited output, I would retain links to the source examination and analyzed frames, the model checkpoint identifier, preprocessing configuration, frame-selection rule, aggregation rule, and calibration transformation. The reference diagnosis would have its own provenance, including evidence source and timing.

Preprocessing deserves this detail because resizing, cropping, grayscale conversion, and normalization change what reaches the network. A caliper-removal experiment performed before image-wide normalization can change values outside the edited region. Without the pipeline record, an apparent overlay effect could partly reflect this propagation.

Access controls can protect patient information while allowing authorized replay. Auditability requires appropriate access to evidence, rather than unrestricted publication of clinical images.

## Worked examples in medical AI

### A benign wall finding and an incorrect concept prediction

Gallbladder adenomyomatosis can produce wall thickening containing Rokitansky-Aschoff sinuses, seen as intramural cystic spaces. These are established imaging findings described by [Bonatti and colleagues](https://pubmed.ncbi.nlm.nih.gov/28127678/).

In a proposed characterization system, I would expose separate predictions for thickening and visible intramural spaces. Suppose a reader identifies spaces in an adequately visualized wall, but the model reports them absent and assigns a high malignancy score. Replacing that concept estimate with the reader annotation would test the downstream consequence of this particular concept error.

If the malignancy score falls, the diagnostic head uses the corrected information under that intervention. If it barely changes, the next question concerns the head's weighting or competing concepts. Neither result proves that the image encoder recognizes the finding correctly.

I would also retain the original view beside the concept record. Otherwise, a reviewer cannot distinguish a detector error from an annotation attached to a different frame where the spaces were visible.

### A measurement overlay that contaminates a concept

Consider a hypothetical frozen ultrasound frame with calipers bracketing a lesion. A concept detector might interpret high-contrast marker edges as an irregular attachment boundary. The final output could then change through a clinically named intermediate variable, even though the initiating evidence came from documentation.

An identical marked and unmarked export would permit a stronger test than inpainting burned-in markers. I would compare both the concept vector and diagnostic score, checking that tissue pixels and export processing match.

This gives the audit a failure location: overlay sensitivity in the encoder, propagation through a particular concept, and a resulting diagnostic change. A heatmap over the correct anatomical region would not provide that decomposition.

## Evaluation methods and limitations

### Test whether another reviewer can answer the promised questions

I would give an independent reviewer a fixed set of cases and questions: recover the analyzed input, reproduce the output, locate the reference evidence, replace a concept, and rerun a controlled overlay comparison. The audit would record which tasks were completed, what information was missing, and where interpretation required undocumented decisions.

Exact numerical equality may depend on the computational environment. Any permitted numerical tolerance should follow measured reproducibility behavior and the application's output requirements, rather than an invented universal cutoff.

Successful replay would establish that the retained artifacts support those operations. It would leave the validity of the clinical concepts and intervention assumptions to separate evaluations.

### Evaluate concepts at their stated level

For a binary concept with predicted probability $$q_i$$ and reader label $$c_i\in\{0,1\}$$, I could report the Brier score:

$$
\mathrm{BS}_c=\frac{1}{n}\sum_{i=1}^{n}(q_i-c_i)^2.
$$

Here, $$n$$ counts evaluated observations with assessable concept labels. Lower values indicate smaller squared probability errors. I would accompany this with calibration plots, sensitivity and specificity at a prespecified decision rule, and the proportion of inputs on which the concept was assessable.

A favorable average could conceal failure on subtle findings. I would therefore stratify by visibility and relevant acquisition conditions, preserve reader disagreement, and resample patients rather than individual frames for uncertainty estimates.

Concept correction experiments also need an explicit correction policy. Allowing an evaluator to choose the most beneficial correction after seeing the diagnosis overstates what a reader could achieve prospectively.

### Evaluate the human interaction and revision process

An exposed concept can make an incorrect output look coherent. I would test whether readers detect wrong concepts, whether correcting them improves decisions, and how much review time the interface requires. [DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9) addresses reporting of early live clinical evaluation, including system use within a human workflow.

Version changes need equally concrete triggers. A new crop policy should prompt spatial and overlay checks; a revised concept vocabulary should prompt annotation and intervention checks. Reusing the old diagnostic AUROC alone would leave the altered evidence pathway insufficiently examined.

## Research connections and open questions

My first feasible study would compare two interfaces to the same frozen gallbladder classifier: a score with its source frames, and a score with source frames plus independently evaluated evidence readouts. I would measure whether reviewers can identify predefined failure mechanisms more accurately, rather than treating greater confidence as success.

A second question is whether continuous concept values predict machine identity after conditioning on reader concept labels. A successful probe would identify retained acquisition information; paired overlay or export tests would then examine whether the diagnostic head uses it.

Third, I would investigate which concept errors are both frequent and consequential. Combining reader disagreement, detector error, and downstream correction effects could identify where additional annotation would improve auditability most. That is a more actionable target than expanding the concept vocabulary without evidence that the added concepts support reliable review.

## References

- Mitchell et al., [Model Cards for Model Reporting](https://doi.org/10.1145/3287560.3287596), FAT* 2019.
- Koh et al., [Concept Bottleneck Models](https://proceedings.mlr.press/v119/koh20a.html), ICML 2020.
- Vasey et al., [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9), Nature Medicine 2022.
- Mahinpei et al., [Promises and Pitfalls of Black-Box Concept Learning Models](https://arxiv.org/abs/2106.13314), arXiv 2021.
- Bonatti et al., [Gallbladder adenomyomatosis: imaging findings, tricks and pitfalls](https://pubmed.ncbi.nlm.nih.gov/28127678/), Insights into Imaging 2017.
