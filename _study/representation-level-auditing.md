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

A representation can contain a clinical finding without the diagnostic head using it. I use internal audits to separate information that is accessible, geometry that is shared, and sensitivity that reaches the final prediction.

## Core question and definition

For a chosen layer, I write the model as $$f(x)=g(h(x))$$. The representation $$h(x)$$ is the activation at that layer, and $$g$$ contains the remaining computation. Depending on the architecture, $$h(x)$$ may be a spatial feature map, a sequence of tokens, or a pooled vector.

My questions are distinct: can an independent annotation be predicted from $$h(x)$$, how does $$h(x)$$ change across acquisitions or model versions, and do those changes influence $$g$$? A probe addresses the first, representation comparison the second, and score or activation interventions the third.

I would record the exact layer, pooling operation, normalization, and inference settings. Comparing a spatial map with a pooled embedding without acknowledging the lost spatial information can turn an architectural difference into an apparent clinical finding.

## Key concepts

### Probes measure accessibility under a learning procedure

A linear probe predicts an annotation from frozen features, for example $$q(h)=\sigma(w^\top h+b)$$ for a binary factor, where $$\sigma$$ is the logistic function. Training the probe changes $$w$$ and $$b$$, not the audited encoder or diagnostic head.

Held-out performance measures whether that factor is recoverable through the specified probe. A nonlinear probe has greater capacity to reconstruct relationships the original head may never use. Even a linear probe can exploit an acquisition correlate if concept labels and machine identity align.

[Hewitt and Liang](https://aclanthology.org/D19-1275/) show why probe evaluation needs control tasks to distinguish representation information from probe learning capacity. Their experiments concern linguistic representations. I would adapt that principle with patient-respecting label controls and matched image baselines, rather than claim their language-specific control construction transfers unchanged.

For a gallbladder audit, I would compare the same probe family across trained features, random-network features, and simple image summaries. A positive result only on the trained representation is stronger than success on all three, but remains evidence of accessibility rather than reliance.

### Concept vectors connect accessibility to local sensitivity

In TCAV, a separator learned from concept and comparison examples defines a concept activation vector $$v_C$$. At a selected layer, directional sensitivity of class score $$g_k$$ is

$$
S_{C,k}(x)=\nabla_h g_k(h(x))^\top v_C.
$$

With $$v_C$$ oriented toward the concept, positive sensitivity means that an infinitesimal move in that direction increases the class score. For a specified evaluation set $$\mathcal{X}_k$$,

$$
\mathrm{TCAV}_{C,k}=
\frac{1}{|\mathcal{X}_k|}
\sum_{x\in\mathcal{X}_k}\mathbf{1}\{S_{C,k}(x)>0\}.
$$

This is a fraction of positive directional derivatives, not the proportion of predictions caused by the concept. [Kim and colleagues](https://proceedings.mlr.press/v80/kim18d.html) introduced TCAV to test class sensitivity to user-defined concepts.

I would repeat concept-set sampling and comparisons with random concepts. A “wall irregularity” vector learned from zoomed, marked positives and unmarked survey-view negatives may represent that entire contrast. Its clinical name does not establish semantic purity, and an activation-space move need not correspond to a realizable ultrasound image.

### Representation similarity requires matched examples

For column-centered matrices $$H\in\mathbb{R}^{n\times p}$$ and $$G\in\mathbb{R}^{n\times q}$$, with rows representing the same $$n$$ examples, linear centered kernel alignment is

$$
\mathrm{CKA}(H,G)=
\frac{\|H^\top G\|_F^2}
{\|H^\top H\|_F\,\|G^\top G\|_F}.
$$

The Frobenius norm $$\|\cdot\|_F$$ is the square root of the sum of squared matrix entries. CKA is undefined if either denominator factor is zero. [Kornblith and colleagues](https://proceedings.mlr.press/v97/kornblith19a.html) develop this framework for comparing neural representations.

Linear CKA is invariant to orthogonal transformations and uniform nonzero scaling of either representation. High similarity can therefore coexist with different coordinate systems. More importantly for my audit, shared variation can dominate the comparison while a smaller diagnostically consequential subspace differs.

I would compare matched patient inputs and report score disagreement beside CKA. Similarity alone cannot identify which model uses more appropriate evidence.

### Frequency needs spatial meaning

A Fourier transform over a B-mode image describes spatial intensity variation, not the transmitted ultrasound frequency in megahertz. A transform over arbitrarily ordered embedding channels has no defensible spatial-frequency interpretation.

For a two-dimensional image or spatial activation map, spectral power can be written $$P(u,v)=|\mathcal{F}\{x\}(u,v)|^2$$, with $$u,v$$ indexing spatial frequencies. I would specify mean removal, windowing, sampling resolution, and normalization before comparing spectra. Image borders and annotation edges can otherwise dominate the result.

[Yin and colleagues](https://papers.nips.cc/paper_files/paper/2019/hash/b05b57f6add810d3b7490866d74c0053-Abstract.html) investigate frequency-dependent robustness trade-offs in vision models. Their work motivates frequency-specific tests, but high-frequency dependence is not intrinsically a shortcut: fine anatomical boundaries and small findings can also occupy those bands.

## Worked examples in medical AI

### Wall findings and machine identity in the same embedding

In a proposed gallbladder malignancy audit, I would train separate probes for reader-assessed wall irregularity, visible intramural cystic spaces, caliper presence, and machine identity. Concept labels would be collected independently of the embeddings and diagnostic scores.

Suppose both irregularity and machine identity are readily decoded. This does not show that the classifier chooses machine information over morphology. Nor does strong irregularity decoding establish that its malignancy head uses irregularity.

I would examine concept-probe performance within machine groups and on a held-out machine where feasible. If a morphology probe fails when acquisition changes, I would investigate whether its learned separator captured machine appearance or whether the clinical finding became less visible. These alternatives require image review.

A useful follow-up uses identical marked and unmarked frames. If a clinical probe changes its output when only calipers change, its purported morphology measure is contaminated under that comparison. If the original diagnostic score also changes, the two responses supply related evidence, but still do not prove that the probe direction mediates the classifier's effect.

### Spectral changes after resizing a diagnostic view

Consider the same unmarked gallbladder frame processed through two resize settings. A tiny wall feature may occupy different numbers of pixels, while interpolation changes both its boundary and surrounding speckle. Spectral differences therefore mix anatomy, sampling, and processing.

I would first compare outputs at the original physical field of view, then inspect registered wall regions and corresponding activation maps. Where reliable ultrasound-region calibration is available, spatial frequency can be expressed in cycles per millimeter. Otherwise, I would retain cycles per pixel and avoid interpreting a spectral shift as a physical tissue difference.

For feature maps, stride changes the sampling grid and receptive field, so input-image frequencies do not transfer directly to every layer. A low-pass perturbation that changes malignancy scores could remove fine clinical evidence, marker edges, or both. Clinical-factor annotations and overlay-free comparisons are needed to distinguish these hypotheses.

## Evaluation methods and limitations

### Keep the probe evaluation independent

I would split all probe training, tuning, and testing by patient, including repeat examinations. Standardization and dimensionality reduction must be fitted on probe-training data alone. Fitting them on the complete dataset introduces information from the audit test distribution into the procedure.

Probe capacity and regularization should be selected using the training and validation partitions. When feature dimension is large relative to patient count, I would report learning curves and capacity-matched controls rather than rely on one favorable test score.

Binary clinical concepts need prevalence-aware evaluation, including precision-recall performance and class counts. Machine probes need per-machine results, not only aggregate accuracy. Failure to decode a feature limits the tested probe and sample; it does not prove that the feature is absent from the representation.

### Relate internal changes to the original head carefully

For a binary affine logit head $$z=w^\top h+b$$, an activation change $$\delta h$$ produces the exact logit change $$\Delta z=w^\top\delta h$$. For a nonlinear remaining network, the gradient gives only a local approximation unless the actual edited activation is passed through the network.

This provides a useful bridge from representation change to output response. It does not establish that a chosen activation displacement corresponds to isolated clinical evidence. Projecting out a concept direction may also remove correlated information and move the activation outside the distribution seen during training.

I would report layerwise probe results, similarity, and head response separately, with prespecified primary layers and concepts. Searching many layers and retaining the strongest association would make the apparent mechanism difficult to reproduce.

## Research connections and open questions

My first question is whether independently annotated wall findings remain linearly decodable across machines after caliper and visibility differences are examined. The needed experiment is a patient-separated probe study with explicit acquisition holdouts.

Second, does the representation change produced by authentic overlay removal align with the diagnostic head's sensitive directions? For an affine final head, I can quantify its contribution to the logit exactly and compare it with total embedding change.

Third, which layerwise spectral changes accompany loss of reader-assessed feature visibility under resizing? That experiment could distinguish a processing-induced loss of clinical information from a generic claim that ultrasound models use “too much texture.”

## References

- Hewitt and Liang, [Designing and Interpreting Probes with Control Tasks](https://aclanthology.org/D19-1275/), EMNLP-IJCNLP 2019.
- Kim et al., [Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV)](https://proceedings.mlr.press/v80/kim18d.html), ICML 2018.
- Yin et al., [A Fourier Perspective on Model Robustness in Computer Vision](https://papers.nips.cc/paper_files/paper/2019/hash/b05b57f6add810d3b7490866d74c0053-Abstract.html), NeurIPS 2019.
- Kornblith et al., [Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html), ICML 2019.
