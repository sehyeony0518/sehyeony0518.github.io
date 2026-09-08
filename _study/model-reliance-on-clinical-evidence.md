---
layout: study_note
title: "Model Reliance on Clinical Evidence"
description: "Moving from an alignment claim to a dependence claim, and what that step requires."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "auditing"
category_title: "Evidence Auditing"
order: 1
source: "Independent study"
written: true
featured: true
updated: "2026-09-08"
papers:
  - "2025-10-28-degrave-covid-shortcut"
---

A dependence claim needs a comparison: which information changes, which model stays fixed, and which output is measured. I would reserve “the model relies on this clinical evidence” for results that specify all three.

## Core question and definition

Let $$X$$ denote the model input, $$Y$$ the clinical reference label, and $$f$$ the frozen predictor, including its prescribed preprocessing. A transformation $$T$$ changes specified input information. For a scalar target score $$s_f$$, the paired response is

$$
\Delta_T(x)=s_f(T(x))-s_f(x).
$$

This quantity describes the model's response to $$T$$. If $$T$$ removes a marker, it measures marker-edit sensitivity. If it blurs a wall, it measures sensitivity to that blurring operation. Calling the latter “reliance on wall irregularity” requires evidence that irregularity changed while other relevant information remained sufficiently controlled.

The target is computational dependence, not disease causation. An imaging sign can be useful because disease produces it. Editing the sign in an image does not alter the patient's disease, and a score response does not establish that the sign is causally responsible for the clinical outcome.

## Key concepts

### Output dependence and useful dependence differ

For a label-preserving transformation, I can define a population loss difference:

$$
R_T(f)=\mathbb{E}_{(X,Y),T}\left[\ell(f(T(X)),Y)-\ell(f(X),Y)\right].
$$

The expectation includes transformation randomness when applicable. The loss $$\ell$$, sampling population, and transformation distribution are part of the definition. Positive $$R_T(f)$$ means that the transformation worsens expected performance against the retained labels. It does not necessarily mean that the removed information was clinically appropriate.

For binary probabilities $$p$$, log loss is $$\ell(p,y)=-y\log p-(1-y)\log(1-p)$$. I would document numerical handling near zero and one. A shortcut may reduce loss in the source population because it predicts that population's labels, yet fail when its association with disease changes.

[Fisher, Rudin, and Dominici](https://jmlr.org/papers/v20/18-760.html) formalize model reliance through feature scrambling and extend the analysis to similarly performing models. My transformation-based loss difference is a related operational choice, not a claim that every intervention is their scrambling estimator. Its value can be negative if removing misleading information improves predictions.

### Marginal and conditional disruption answer different questions

For structured factors $$C$$ and remaining variables $$Z$$, marginal permutation replaces $$C$$ with a draw from its marginal distribution. It breaks associations between $$C$$ and both $$Z$$ and the outcome. If lesion size and morphology are closely related, this can create combinations unlike those observed clinically.

Conditional resampling instead draws a replacement $$C'$$ from $$P(C\mid Z)$$, independently of the case's outcome given $$Z$$. It asks how much predictive information the original $$C$$ contributes beyond $$Z$$ under that resampling design. Estimating this conditional distribution is itself a modeling task, and near-deterministic relationships leave little variation to test.

For images, neither operation is implemented merely by shuffling factor labels in an audit spreadsheet. The classifier receives pixels. A valid input intervention needs a defensible way to express the replacement finding in those pixels, or the analysis must remain a study of structured annotations rather than image-model reliance.

### Local responses can disappear in an average

Signed score changes can cancel: marker removal might lower scores in some malignant cases and raise them in benign cases. I would report the distribution of $$\Delta_T$$, its absolute magnitude, and its direction within reference-label groups. Absolute magnitude measures sensitivity but discards whether the change helps.

A fixed decision threshold $$\tau$$ permits a separate measure:

$$
F_T=\Pr\left(\mathbf{1}\{s_f(T(X))\geq\tau\}\neq
\mathbf{1}\{s_f(X)\geq\tau\}\right).
$$

Here $$\mathbf{1}$$ is the indicator function, and $$F_T$$ is the decision-flip probability. It depends strongly on how many original scores lie near $$\tau$$. I would separate beneficial and harmful flips against the reference label rather than report flips as failures by definition.

Probability saturation also matters. A substantial logit change near an extreme probability can produce a small probability difference. Where accessible, logits help characterize response magnitude; probabilities and decisions retain their relevance to the clinical interface.

### Redundancy limits claims of necessity

A classifier may use both lesion morphology and an acquisition correlate. Removing one can leave its decision unchanged because the other remains informative. Conversely, deleting both can create a large response that neither individual edit predicts.

For compatible transformations $$T_A$$ and $$T_B$$, I would examine an interaction contrast:

$$
I_{A,B}(x)=s_f(T_{AB}(x))-s_f(T_A(x))-s_f(T_B(x))+s_f(x).
$$

Here $$T_{AB}$$ is a separately validated joint edit. Nonzero $$I_{A,B}$$ indicates nonadditivity on the selected score scale, not a unique diagnosis of redundancy. Nonlinear output transformations and edit interactions can also produce it.

## Worked examples in medical AI

### Source labels that become disease cues

[DeGrave, Janizek, and Lee](https://doi.org/10.1038/s42256-021-00338-7) studied chest-radiograph COVID-19 classifiers trained from sources whose membership was strongly associated with COVID-19 status. Source-specific image characteristics could therefore predict the label without requiring the intended pulmonary pathology.

Their investigation combined external evaluation with saliency and generative analyses. A particularly relevant conclusion was that external performance alone could miss shortcut use when the shortcut also transferred. I read this as a reason to challenge the proposed dependency directly, rather than interpret successful transport as proof of appropriate evidence.

The ultrasound analogue is a hypothesis, not an established result: if malignant gallbladder cases mainly come from a referral service and benign cases from routine examinations, device appearance or documentation style could encode the collection pathway.

### Irregular morphology, calipers, and zoom

In my proposed gallbladder study, readers would score wall irregularity without seeing model outputs. Suppose malignancy scores rise with that factor. I would first cross-tabulate irregularity with calipers, zoom, acquisition site, and reference-standard type to determine whether informative comparisons actually exist.

Identical frozen images exported with and without calipers permit a comparatively clean test of annotation dependence. If removing calipers changes the score while tissue pixels are preserved, I can attribute the computational response to the changed annotation layer under that pipeline. I still cannot conclude that morphology contributes nothing.

Zoom is harder. Cropping and resizing simultaneously change field of view, lesion scale, interpolation, and context. A score drop after a tight crop cannot isolate “background reliance.” I would compare crop variants that preserve lesion scale where possible, retain the full-image baseline, and describe the remaining differences explicitly.

To investigate morphology beyond markers, I would examine unmarked cases spanning reader-rated irregularity within acquisition groups. If no realistic morphology intervention exists, this supplies supporting alignment evidence, not a completed dependence test.

## Evaluation methods and limitations

### Match the estimand to the label

Marker removal normally preserves the patient's reference diagnosis. Its effect on diagnostic loss is therefore interpretable as a performance change under altered documentation.

Removing visible evidence has a different implication from changing disease. If a stone and its shadow are obscured, the patient still has the original reference diagnosis, but the edited image may no longer support it. Loss against the unchanged label measures performance after information removal. It does not establish that a lower disease score is clinically irrational.

A synthetic edit intended to change the diagnosis needs a justified counterfactual target. Reader acceptance of appearance alone does not supply pathology for that synthetic patient.

### Require controls and adequate coverage

The primary transformation and output have to be fixed in advance, all eligible patients retained, and uncertainty estimated at the patient level. Matched control edits should challenge explanations based on edit area, boundary artifacts, or global normalization. Multiple replacement methods provide sensitivity analyses rather than extra independent patients.

Natural matched comparisons need overlap. If every malignant case has calipers and no benign case does, statistical adjustment cannot recover an unobserved combination without extrapolation. I would report that limitation directly and seek additional data.

A null response supports only a bounded conclusion: no detectable effect under the tested edit and precision. Redundancy, incomplete removal, insensitive outputs, and sparse samples remain distinct explanations that require different follow-up tests.

## Research connections and open questions

I would begin by estimating caliper-edit responses separately for benign and malignant gallbladder cases, with score changes and harmful flips reported together. This tests whether documentation dependence is concentrated in a clinically consequential subgroup.

A second question is whether marker sensitivity persists when the visible wall finding is well assessed. Comparing predefined visibility strata can distinguish a broad dependence from one concentrated in difficult images, although visibility-related selection still needs review.

Finally, I would test whether joint removal of two independently editable documentation elements produces nonadditive responses. If calipers and peripheral text can be separated without modifying anatomy, that experiment can investigate redundancy more credibly than a joint edit of tightly coupled disease signs.

## References

- Fisher, Rudin, and Dominici, [All Models are Wrong, but Many are Useful: Learning a Variable's Importance by Studying an Entire Class of Prediction Models Simultaneously](https://jmlr.org/papers/v20/18-760.html), Journal of Machine Learning Research 2019.
- DeGrave, Janizek, and Lee, [AI for radiographic COVID-19 detection selects shortcuts over signal](https://doi.org/10.1038/s42256-021-00338-7), Nature Machine Intelligence 2021.
