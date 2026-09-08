---
layout: study_note
title: "Shortcut Learning in Medical Imaging"
description: "The failure mode where a model reaches the right answer through a cue nobody intended it to use."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "causality"
category_title: "Causality, Bias & Shortcuts"
order: 5
source: "Independent study"
written: true
featured: true
updated: "2026-09-08"
papers:
  - "2025-09-06-geirhos-shortcut-learning"
  - "2025-10-28-degrave-covid-shortcut"
  - "2025-10-02-zech-variable-generalization"
---

A classifier can identify the correct diagnosis while relying on evidence that would become misleading under a different acquisition or referral process. I want to identify that dependence before a favorable test score makes it difficult to question.

## Core question and definition

I follow [Geirhos and colleagues](https://doi.org/10.1038/s42256-020-00257-z): shortcut learning produces decision rules that succeed under familiar evaluation conditions but fail when the test demands the intended competence. In medical imaging, the intended competence needs specification. Detecting visible pneumonia, predicting a microbiological diagnosis, and reproducing a radiology report are different tasks.

I distinguish three claims: a candidate cue is associated with the label, the model encodes that cue, and the diagnostic output depends on it. Only the third establishes reliance. A scanner-label association creates an opportunity for shortcut learning; a scanner probe establishes decodability; neither alone demonstrates that changing scanner information changes the diagnosis.

“Unintended” also requires a clinical argument. Posterior shadowing is an acquisition-dependent phenomenon but legitimate evidence for a gallstone. A measurement cross is documentation added after an operator identified something worth measuring.

## Key concepts

### The training objective does not specify acceptable evidence

For training examples $$D=\{(x_i,y_i)\}_{i=1}^{n}$$, empirical risk is

$$
\widehat{R}(f)=\frac{1}{n}\sum_{i=1}^{n}\ell(f(x_i),y_i),
$$

where $$f$$ is the predictor and $$\ell$$ is its loss. Two predictors can achieve similar risk through different features. Ordinary supervised training does not require the feature that reduces loss to be clinically meaningful.

The observation unit matters. If suspicious examinations contribute many close-up frames while normal examinations contribute one overview, frame-level sampling gives suspicious examinations greater weight. A patient-level split prevents shared patients across partitions, but it does not remove this imbalance or the acquisition-label relationship.

### Trace the cue through the data-generating process

For a gallbladder dataset, I would write down a concrete pathway: suspicious morphology prompts additional zoom, calipers, Doppler images, and referral; referral influences whether pathology becomes available; pathology availability influences inclusion in the dataset. Documentation can consequently predict diagnosis without directly depicting tissue biology.

Another pathway begins with institutional equipment. A surgical referral center may use one scanner family and contribute more cancers, while a screening center supplies mostly benign cases from another vendor. Sector geometry, grayscale processing, annotation fonts, and export compression can identify source. Removing a hospital name leaves these other pathways available.

These are hypotheses about a particular dataset. I would verify them using acquisition metadata, inclusion criteria, and image review before calling them observed mechanisms.

### Learning, encoding, and dependence are different

A linear probe trained on a frozen representation can test whether scanner identity is accessible to that probe. High probe accuracy does not establish that the diagnostic head uses scanner information. Conversely, a weak linear probe does not exclude information accessible through a nonlinear readout.

The same distinction applies to explanations. A heatmap over a lesion may highlight calipers that overlap the lesion. Before interpreting the map, I would check whether it changes when learned parameters are randomized. [Adebayo and colleagues](https://papers.nips.cc/paper_files/paper/2018/hash/294a8ed24b1ad22ec2e7efea049b8737-Abstract.html) showed why visually recognizable maps can fail such checks.

### Clinical and shortcut features can substitute for one another

A classifier may use wall irregularity in clear images and documentation cues in difficult images. Removing one overlay can have little effect because zoom or another marker provides redundant information. A null intervention therefore means no detected effect under that comparison, not proof that the cue is irrelevant in every context.

I also avoid equating texture dependence with shortcut learning. Ultrasound texture reflects scattering, interference, and processing. The question is whether a particular texture feature tracks clinically relevant structure or a machine-specific representation of it.

## Worked examples in medical AI

### Disease labels coupled to image repositories

[DeGrave, Janizek, and Lee](https://doi.org/10.1038/s42256-021-00338-7) studied COVID-19 classification using chest radiographs assembled from different sources. One construction combined positive images from an online COVID-19 collection with negative images from NIH ChestX-ray14. Another used PadChest and BIMCV-COVID-19+.

This creates a specific alternative to recognizing pulmonary abnormalities: identify the repository through acquisition and processing differences. Their explanation and image-modification experiments supported reliance on source-associated information. External evaluation did not necessarily eliminate the problem because related shortcuts could remain available across datasets.

I read this as a warning about assembling disease classes separately. A balanced number of positive and negative images does not balance the process that produced them.

### Hospital identity as a pneumonia predictor

[Zech and colleagues](https://doi.org/10.1371/journal.pmed.1002683) investigated pneumonia detection across chest-radiograph datasets and manipulated hospital-specific disease prevalence. Their experiments connected source recognition with diagnostic prediction when hospital identity became informative about pneumonia.

The failure mechanism is more specific than “domain shift.” A predictor can assign a higher score to images from a high-prevalence hospital, improving pooled ranking even when its ability to distinguish patients within that hospital is weaker. I would therefore examine within-source discrimination alongside pooled AUROC.

### Calipers on an irregular gallbladder lesion

Consider a hypothetical malignancy classifier evaluated on a frozen ultrasound image of focal irregular wall thickening. The operator saves an unmarked image, places calipers, and saves the same image again. If tissue pixels and preprocessing are identical, the pair isolates the annotation layer unusually well.

I would compare scores before looking at saliency. A higher malignancy score in the marked export supports sensitivity to that overlay. A second frame from a cine loop is a weaker control because probe position, respiration, and speckle also change.

The clinical finding remains irregular thickening. The tested alternative is the operator’s measurement action, not an invented biological transformation.

## Evaluation methods and limitations

### Define a behavioral quantity

For matched unmarked and marked inputs $$x_i^{(0)}$$ and $$x_i^{(1)}$$, let $$s(x)$$ denote a fixed model score, such as the malignancy logit. I would report

$$
\Delta_i=s(x_i^{(1)})-s(x_i^{(0)}).
$$

The signed mean describes directional influence; the mean absolute difference describes sensitivity that may cancel in the signed average. I would also report threshold crossings at a decision threshold fixed before the audit. A logit difference is not a probability difference, and neither automatically describes clinical harm.

Pairs from one patient remain dependent. Confidence intervals should resample patients with their associated pairs. For a training-method claim, variation across independently trained models also matters.

### Challenge the cue-label relationship

An overlay-only or border-only baseline tests whether the restricted input predicts diagnosis. It establishes available information, not reliance by the full-image model. A complementary challenge evaluates that model where the suspected association weakens: marked benign cases, unmarked malignant cases, or both diagnoses acquired on each scanner.

Those groups need comparable reference standards and sufficient clinical overlap. Comparing tiny benign polyps from screening with advanced cancers from surgery confounds acquisition with disease severity. I would examine performance within relevant size and morphology ranges and report where the data provide no overlap.

Subgroup sensitivity, specificity, calibration, and patient counts answer different questions. Pooled AUROC can hide a poorly served subgroup; subgroup AUROC can become unstable when there are few positive cases.

### Interpret interventions and mitigation together

Black rectangles and inpainting can introduce unfamiliar edges or erase tissue. I would prefer native paired exports, then compare several editing strategies with matched control edits. Similar responses across plausible interventions strengthen the overlay hypothesis without making any edit a perfect counterfactual.

Mitigation should follow the mechanism. Removing burned-in text addresses text; balancing diagnosis within scanner addresses a recorded source association; collecting standardized views addresses acquisition selection. None guarantees removal of other proxies.

I would reserve independent patients for checking both shortcut sensitivity and clinical performance after mitigation. Reduced marker dependence accompanied by reduced sensitivity to subtle wall lesions is not an unqualified improvement.

## Research connections and open questions

My first feasible question is whether paired overlay sensitivity is larger when the underlying lesion is poorly visualized. Readers could rate wall-margin assessability without seeing model scores, and I could compare patient-level intervention effects across those ratings.

Second, does a classifier retain discrimination between benign and malignant lesions within overlapping size ranges and scanner groups? This would test whether apparently strong aggregate performance depends on source or size distributions.

Third, after removing overlays during training, does prediction align more closely with independently annotated sessility, wall irregularity, and intramural cystic spaces? I would evaluate those factors separately because removing an inappropriate cue does not identify its replacement.

Finally, I would examine whether a multi-frame prediction is less sensitive to the operator’s selected still image. Cine loops could support that comparison, provided the aggregation method and included views are fixed before examining outcomes.

## References

- Geirhos et al., [Shortcut learning in deep neural networks](https://doi.org/10.1038/s42256-020-00257-z), Nature Machine Intelligence 2020.
- DeGrave, Janizek, and Lee, [AI for radiographic COVID-19 detection selects shortcuts over signal](https://doi.org/10.1038/s42256-021-00338-7), Nature Machine Intelligence 2021.
- Zech et al., [Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs: A cross-sectional study](https://doi.org/10.1371/journal.pmed.1002683), PLOS Medicine 2018.
- Adebayo et al., [Sanity Checks for Saliency Maps](https://papers.nips.cc/paper_files/paper/2018/hash/294a8ed24b1ad22ec2e7efea049b8737-Abstract.html), NeurIPS 2018.
