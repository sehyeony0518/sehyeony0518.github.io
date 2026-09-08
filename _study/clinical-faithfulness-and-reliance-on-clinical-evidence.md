---
layout: study_note
title: "Clinical Faithfulness and Reliance on Clinical Evidence"
description: "My own research question: whether a model's evidence aligns with independent clinical factors rather than merely looking anatomically reasonable."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "alignment"
category_title: "Clinical Alignment & Interpretability"
order: 5
source: "Independent study"
written: true
featured: true
pinned: true
updated: "2026-09-08"
papers:
  - "2026-03-13-arun-assessing-saliency"
---

I want to know whether a medical image classifier relies on clinically meaningful evidence, and how to make that reliance measurable and auditable. A heatmap that falls inside the gallbladder is a starting observation, not an answer.

## Core question and definition

I use clinical faithfulness as a research objective connecting three properties: the clinical relevance of evidence, the faithfulness of a model readout, and the predictor's reliance on that evidence. I do not treat it as an established metric with a universal acceptance threshold.

Clinical relevance asks whether a finding informs the specified task. Explanation faithfulness asks whether a readout describes the model behavior it claims to explain. Reliance asks whether changing particular information changes the prediction under a defined comparison. An explanation can faithfully expose reliance on calipers. Conversely, an attractive map over a lesion can be clinically plausible without identifying what the classifier uses.

My immediate objective is narrower than recovering a complete diagnostic reasoning process: evaluate an existing classifier against independently assessed clinical factors, then test selected dependence hypotheses. This can proceed without retraining the classifier, but it still requires annotation, methodological controls, and a clearly bounded claim.

## Key concepts

### Independence is about how the reference was constructed

I would define clinical factors before inspecting explanations: focal versus diffuse wall thickening, attachment morphology, intramural cystic spaces, or posterior shadowing, depending on the target diagnosis. Readers would record presence, absence, uncertainty, and whether the relevant evidence is assessable. “Not visible” must not become “absent.”

Independence means that the factor label was not derived from the explanation being tested. It does not imply statistical independence from diagnosis. A reader tracing a region after seeing the heatmap creates circular validation, even if that reader is clinically experienced. Blinding readers to model scores and, where feasible, final diagnosis reduces separate sources of expectation bias.

I would also distinguish a frame annotation from an examination finding. A still image can show an echogenic focus and its shadow; it cannot establish mobility across patient positions. An examination-level mobility label assigned to every frame would give the audit a reference that some inputs cannot support.

### Anatomical agreement does not identify the feature

For attribution values $$a_j(x)$$ at pixels $$j$$ and an independently annotated region $$M$$, one descriptive measure is the fraction of absolute attribution inside that region:

$$
A_M(x)=\frac{\sum_{j\in M}|a_j(x)|}{\sum_j|a_j(x)|}.
$$

I would leave this undefined when the denominator is zero. Absolute values combine contributions supporting and opposing the explained score, so the measure describes attribution concentration, not positive diagnostic evidence.

A large region can capture much attribution by chance. Comparing $$A_M(x)$$ with the area fraction $$|M|/|\Omega|$$, where $$\Omega$$ is the evaluated image domain, checks one trivial explanation. It does not correct for an organ's habitual position or a method's tendency to emphasize edges. Average anatomical masks and simple edge maps provide additional spatial baselines.

In chest radiography, [Arun and colleagues](https://pubs.rsna.org/doi/10.1148/ryai.2021200267) evaluated saliency on the SIIM-ACR pneumothorax and RSNA pneumonia datasets using localization, weight randomization, repeatability, and reproducibility. I take that separation seriously: localization evaluates where a map falls; the other tests examine different properties.

### The readout determines the explanatory claim

A gradient measures local score sensitivity. Integrated Gradients allocates a score difference relative to a baseline along a chosen path. Its completeness property makes the attributions sum to that difference, subject to numerical approximation. Completeness does not establish that the baseline or path represents a plausible ultrasound comparison. [Sundararajan, Taly, and Yan](https://proceedings.mlr.press/v70/sundararajan17a.html) provide the method's axiomatic formulation.

For my audit, the explained class, output scale, baseline, layer, and normalization must be fixed before comparing patients. Independently rescaling every map to its brightest pixel can make weak and strong responses look equally persuasive. A method that discards negative attribution also cannot answer a question about evidence against malignancy.

### Alignment can arise through competing pathways

Suppose a wall-region readout increases with reader-rated irregularity. One explanation is sensitivity to irregular morphology. Another is that suspicious walls receive tighter zoom and additional measurements, making both the clinical feature and annotation edges more prominent.

I would examine diagnosis, lesion extent, visibility, machine, and overlays as candidate explanations for that association. These variables are not an automatic adjustment list. Zoom can improve visibility, and selection for surgery can depend on suspicious findings. Adjusting without considering those pathways can remove relevant variation or introduce selection bias.

## Worked examples in medical AI

### A thick wall with a benign structural explanation

Adenomyomatosis provides a useful test case because “attention to the thickened wall” leaves the discriminating finding unresolved. Its characteristic structural feature is Rokitansky-Aschoff sinuses, mucosal invaginations that may appear as intramural cystic spaces. Echogenic contents can produce comet-tail artifacts. These are established imaging findings, described by [Bonatti and colleagues](https://pubmed.ncbi.nlm.nih.gov/28127678/), rather than features invented for an explanation benchmark.

In a proposed benign-versus-malignant gallbladder audit, I would separately annotate wall thickening, assessable intramural spaces, and supporting acoustic artifacts. A malignancy heatmap could overlap the wall while responding mainly to its overall thickness. I read this as a reason to test feature specificity within the same anatomical compartment.

I would compare adequately visualized benign wall-thickening cases with and without visible intramural spaces, then examine whether the relationship survives differences in zoom and machine. This remains observational alignment. It does not justify synthetically erasing cystic spaces and declaring the altered image malignant.

### A measurement marker inside the correct region

Consider a hypothetical stored image in which calipers bracket an irregular gallbladder lesion. The operator noticed the lesion, froze a diagnostic view, and added measurements before export. Marker geometry therefore records an action downstream of clinical suspicion.

An attribution map can overlap the lesion precisely because the calipers overlap it. I would seek two exports of the identical frozen image, with and without the overlay, and verify that tissue pixels and preprocessing match. A score change would support sensitivity to the annotation layer. A nearby cine frame would be weaker evidence because breathing, probe movement, and speckle also change.

This example makes anatomical overlap ambiguous in a specific way: tissue morphology and documentation occupy the same region but enter the image through different mechanisms.

## Evaluation methods and limitations

### Test alignment and faithfulness separately

For an ordinal clinical factor, I would prespecify a readout and examine rank association alongside the underlying distributions. I would report results within clinically relevant diagnostic groups where sufficient variation exists. A pooled association could simply separate large malignant lesions from small benign findings.

Factor-label permutations must respect the analysis unit and intended null. Shuffling labels across frames independently would destroy patient structure and create an inappropriate reference distribution. If permutations are restricted within machine or diagnosis groups, I would report that they test a correspondingly narrower association.

Parameter-randomization checks examine whether a readout depends on learned weights. The training-label randomization experiment in [Adebayo and colleagues](https://papers.nips.cc/paper_files/paper/2018/hash/294a8ed24b1ad22ec2e7efea049b8737-Abstract.html) additionally requires training comparison models. For a strictly frozen-model audit, I would state which checks are feasible and avoid implying that a weight check covers both.

### Preserve the limits of the evidence

Reader disagreement should remain visible through reader-specific analyses and adjudication records. A consensus label is useful, but it does not erase uncertainty about a subtle finding. Confidence intervals should resample patients with all their associated frames, rather than count frames as independent observations.

I would report anatomical agreement, clinical-factor alignment, and intervention effects separately. Combining them into one score would require a justified weighting scheme and could hide a decisive failure behind favorable averages. Agreement across methods is persuasive only to the extent that their errors differ.

## Research connections and open questions

My first feasible question is whether attribution concentration in an annotated wall region tracks specific wall findings after accounting for region area and visibility. I can attack this with blinded annotation and predefined spatial baselines, before attempting difficult morphology edits.

Second, among cases with identical marked and unmarked exports, does marker sensitivity explain cases where anatomical overlap looks favorable but clinical-factor alignment is weak? This directly connects an apparently reassuring display to a testable documentation mechanism.

Third, how sensitive are alignment conclusions to reader disagreement about intramural spaces? I would repeat the analysis using each reader's labels, adjudicated labels, and an explicitly assessable subset. Differences would identify which clinical references need better acquisition or annotation before a stronger reliance claim is warranted.

## References

- Arun et al., [Assessing the Trustworthiness of Saliency Maps for Localizing Abnormalities in Medical Imaging](https://pubs.rsna.org/doi/10.1148/ryai.2021200267), Radiology: Artificial Intelligence, 2021.
- Sundararajan, Taly, and Yan, [Axiomatic Attribution for Deep Networks](https://proceedings.mlr.press/v70/sundararajan17a.html), ICML 2017.
- Bonatti et al., [Gallbladder adenomyomatosis: imaging findings, tricks and pitfalls](https://pubmed.ncbi.nlm.nih.gov/28127678/), Insights into Imaging 2017.
- Adebayo et al., [Sanity Checks for Saliency Maps](https://papers.nips.cc/paper_files/paper/2018/hash/294a8ed24b1ad22ec2e7efea049b8737-Abstract.html), NeurIPS 2018.
