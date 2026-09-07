---
layout: study_note
title: "Representation-Level Auditing"
description: "Probing, frequency analysis, and representation comparison as evidence about what formed inside the model."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "auditing"
category_title: "Evidence Auditing"
order: 4
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-09-19-tcav-concept-activation-vectors"
---

Representation-level auditing examines the internal features a model produces, including what can be decoded, how representations compare, and which spatial patterns they preserve. These measurements describe internal organization without automatically explaining the final decision.

## Core question and definition

For a model f(x) = g(h(x)), h(x) is a representation and g is the remaining prediction computation. I want to ask what information is accessible in h, how that information changes across layers or conditions, and whether it matters to g. Those are separate questions.

A representation can encode clinical features, machine identity, and patient characteristics simultaneously. Discovering one does not establish that the others are absent. Nor does a visually separated embedding prove that the geometry corresponds to a clinically meaningful distinction.

## Key concepts

### Probes measure accessible information

A probe q is trained to predict an annotation from frozen h(x). Its held-out performance measures accessibility under that probe family and dataset. A flexible probe can learn relationships that the original head never uses. [Hewitt and Liang](https://aclanthology.org/D19-1275/) demonstrate the importance of control tasks in linguistic probing. I would adapt the principle to medical images, without assuming their task-specific controls transfer unchanged.

### Concept directions add a sensitivity question

A concept activation vector is learned from examples representing a concept and comparison examples. [TCAV](https://proceedings.mlr.press/v80/kim18d.html) evaluates directional sensitivity of a class score along that vector. Concept separability and score sensitivity therefore remain distinct measurements. A direction labeled “wall irregularity” may also encode zoom or annotation style, and moving along it need not correspond to a realistic clinical change.

### Frequency analysis needs a meaningful axis

Spatial Fourier analysis can characterize images or spatial feature maps, and frequency-specific perturbations can test model sensitivity. [Yin and colleagues](https://papers.nips.cc/paper_files/paper/2019/hash/b05b57f6add810d3b7490866d74c0053-Abstract.html) study frequency-dependent robustness in vision models. Applying a Fourier transform across arbitrarily ordered embedding channels does not give those channels a physical frequency meaning. Spectral energy also measures what is present, not necessarily what the classifier uses.

### Representation comparison is descriptive

Centered kernel alignment compares relationships among matched examples across representations. For centered feature matrices H and G with matched example rows, linear CKA is ||HᵀG||²_F divided by ||HᵀH||_F ||GᵀG||_F. Here ||·||_F denotes the Frobenius norm. [Kornblith and colleagues](https://proceedings.mlr.press/v97/kornblith19a.html) develop this comparison framework. High similarity does not guarantee equal clinical behavior, and low similarity does not identify which representation is more appropriate. Sample composition and preprocessing affect the comparison.

## Worked examples in medical AI

In a hypothetical gallbladder audit, I would probe several frozen layers for independently annotated wall findings and for machine identity. Strong decoding of both would show that the representation contains accessible information about both. It would not establish whether malignancy predictions depend on either one. Testing the diagnostic head's response would require additional analysis.

A second hypothetical comparison would examine representations of the same lesion across acquisition settings. Spatial spectral differences might reflect altered speckle, resolution, or marker edges. Clinical review would need to establish which findings remain visible. Comparing matched acquisitions is more informative than interpreting different spectra from unrelated patient groups as evidence of a particular learned mechanism.

## Evaluation methods and limitations

I would separate probe training and testing by patient, constrain probe capacity, tune without using the audit test set, and compare appropriate control representations and labels. Multiple layers, concepts, and probes create many opportunities for selective reporting. A negative probe result only limits what was recoverable under the tested setup; it does not prove that the representation lacks the information.

Representation comparisons should use matched examples and disclose centering, normalization, layer selection, and spatial resolution. Frequency analysis should specify pixel or physical units where meaningful. A two-dimensional embedding can hide or exaggerate structure. Most importantly, none of these methods independently establishes clinical reliance: availability, geometry, and predictive use need separate evidence.

## Research connections and open questions

I see representation auditing as a way to locate candidate mechanisms in gallbladder models before making stronger faithfulness claims. It can help identify which layers and concepts deserve targeted tests, while keeping internal feature discovery distinct from proof of diagnostic reasoning.

- Can I construct clinical concept sets that separate morphology from acquisition and annotation habits?
- Which spectral differences remain meaningful after accounting for depth, resolution, and image formation?
- How can I connect a probe result to the original diagnostic head without mistaking probe learning for model reliance?

## References

- Hewitt and Liang, [Designing and Interpreting Probes with Control Tasks](https://aclanthology.org/D19-1275/), EMNLP-IJCNLP 2019.
- Kim et al., [Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV)](https://proceedings.mlr.press/v80/kim18d.html), ICML 2018.
- Yin et al., [A Fourier Perspective on Model Robustness in Computer Vision](https://papers.nips.cc/paper_files/paper/2019/hash/b05b57f6add810d3b7490866d74c0053-Abstract.html), NeurIPS 2019.
- Kornblith et al., [Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html), ICML 2019.
