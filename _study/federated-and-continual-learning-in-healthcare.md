---
layout: study_note
title: "Federated and Continual Learning in Healthcare"
description: "Training across institutions that cannot share data, and updating a model without losing what it knew."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "systems"
category_title: "Medical AI Systems & Deployment"
order: 5
source: "Independent study"
written: true
updated: "2026-09-08"
---

Federated learning coordinates training across data holders without routinely pooling their raw records. Continual learning addresses a different problem: updating a model over time while retaining capabilities that remain clinically necessary.

## Core question and definition

The two approaches can be combined, but neither implies the other. A federated model can be trained once and frozen. A continually updated model can learn from one hospital's data. I would first specify whether the main constraint concerns institutional data access, changing clinical conditions, or both.

The question is whether collaboration and updating improve the intended clinical task without hiding losses at particular institutions or in earlier patient populations. Keeping data local and maintaining accuracy over time are separate claims that require separate evidence.

## Key concepts

### Aggregation defines whose data shape the model

In a basic federated objective, F(θ) = Σ_k w_k F_k(θ), where F_k is a site's loss and the weights sum to one. [McMahan and colleagues](https://proceedings.mlr.press/v54/mcmahan17a.html) introduced Federated Averaging, which combines locally trained model parameters. Weighting by sample count gives larger contributors more influence. Equal site weighting answers a different optimization question; neither choice automatically reflects clinical importance or fairness.

### Institutional heterogeneity remains inside the federation

Hospitals may differ in scanners, referral patterns, labels, and disease frequency. Local optimization can move models in competing directions when these distributions differ. Shared preprocessing and label definitions help establish a coherent task, but should not conceal meaningful differences. I would examine whether a shared model, local model, or personalized adaptation best supports each intended setting.

### Local data storage is not a complete privacy guarantee

Model updates can reveal information about training records under some conditions. [Zhu and colleagues](https://proceedings.neurips.cc/paper_files/paper/2019/hash/60a6c4002cc7b29142def8871531281a-Abstract.html) demonstrate reconstruction attacks from shared gradients. This does not mean every federated deployment permits the same attack. It means that privacy claims need an explicit threat model and evaluated protections, rather than relying solely on the absence of raw-image transfer.

### Continual learning balances retention and adaptation

Updating on new data can degrade earlier capabilities, a problem called catastrophic forgetting. Replay revisits earlier examples or substitutes, while regularization can discourage changes to parameters considered important. [Kirkpatrick and colleagues](https://doi.org/10.1073/pnas.1611835114) developed elastic weight consolidation for this purpose. Retention is not always the only goal: obsolete labeling conventions may need correction, so I would define which behavior should persist.

## Worked examples in medical AI

[Sheller and colleagues](https://doi.org/10.1038/s41598-020-69250-1) studied federated learning for medical image segmentation across institutional datasets. Their work provides evidence that collaborative training can be feasible without centralizing the original patient images. It does not establish universal equivalence to pooled training or eliminate the need to evaluate each institution.

In a hypothetical gallbladder federation, a referral center might contribute more malignant cases while another hospital contributes mostly routine examinations. A later update dominated by the second hospital could improve average accuracy while weakening malignant-case sensitivity. That possibility connects institutional weighting with continual retention, even if every participating hospital follows the same software protocol.

## Evaluation methods and limitations

I would compare federated training with local baselines and, where legitimately available, a pooled-data reference. Evaluation should include participating sites, unseen institutions, communication failures, and differences in client participation. A pooled score can hide poor results at a small contributor, while external testing remains necessary because collaboration is not itself validation.

For continual learning, I would evaluate each released version on both retained reference cohorts and later cases. Repeated use of a fixed cohort can turn it into development data, so fresh evaluation is also needed. Update histories, rollback conditions, and the handling of corrected labels should be documented. If old data cannot be retained, the limits of both replay and historical verification need acknowledgment.

## Research connections and open questions

For gallbladder clinical faithfulness, I would examine whether collaboration and updates change reliance on wall features, lesion morphology, or acquisition cues. Stable diagnostic performance could conceal a shift in the evidence supporting it.

- How should institutional contributions be weighted when case counts and clinical priorities differ?
- Which earlier capabilities must remain stable after an update?
- Can evidence reliance be compared across sites without transferring sensitive patient-level audit records?

## References

- McMahan et al., [Communication-Efficient Learning of Deep Networks from Decentralized Data](https://proceedings.mlr.press/v54/mcmahan17a.html), AISTATS 2017.
- Zhu, Liu, and Han, [Deep Leakage from Gradients](https://proceedings.neurips.cc/paper_files/paper/2019/hash/60a6c4002cc7b29142def8871531281a-Abstract.html), NeurIPS 2019.
- Kirkpatrick et al., [Overcoming catastrophic forgetting in neural networks](https://doi.org/10.1073/pnas.1611835114), PNAS 2017.
- Sheller et al., [Federated learning in medicine: facilitating multi-institutional collaborations without sharing patient data](https://doi.org/10.1038/s41598-020-69250-1), Scientific Reports 2020.
