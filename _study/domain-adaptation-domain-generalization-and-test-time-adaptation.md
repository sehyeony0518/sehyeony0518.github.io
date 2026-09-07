---
layout: study_note
title: "Domain Adaptation, Domain Generalization, and Test-Time Adaptation"
description: "Three answers to the same problem of a model meeting data it was not trained on, and what each assumes."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "systems"
category_title: "Medical AI Systems & Deployment"
order: 4
source: "Independent study"
written: true
updated: "2026-09-08"
---

Domain adaptation, domain generalization, and test-time adaptation address performance when a model encounters a different data distribution. Their main distinction is what target information is available, when it is available, and whether the model changes after deployment.

## Core question and definition

I would describe the source distribution P_s(X, Y), the target distribution P_t(X, Y), and the permitted access to each before naming an algorithm. Labeled target cases, an unlabeled target collection, and a stream of individual incoming examinations create different learning problems.

These categories can overlap. Test-time adaptation is a form of adaptation performed during inference, while a model trained for domain generalization may later be adapted locally. The method's name does not replace a clear account of data access and update rules.

## Key concepts

### Domain adaptation uses information from the target

Adaptation uses target-domain information to improve performance there. Unsupervised domain adaptation typically combines labeled source data with unlabeled target data; other settings permit target labels. [Ganin and colleagues](https://jmlr.org/papers/v17/15-239.html) train representations to support the source task while making domains harder to distinguish. Matching feature distributions is not sufficient if it merges clinically different classes or removes useful disease information.

### Domain generalization prepares for unseen domains

Domain generalization aims to perform on target domains unavailable during development, often using multiple source environments. Augmentation and representation constraints attempt to discourage reliance on source-specific regularities. [Gulrajani and Lopez-Paz](https://arxiv.org/abs/2007.01434) show why controlled comparisons and model-selection rules matter. A model chosen using target labels no longer demonstrates the same unseen-domain claim, even if those labels never enter gradient updates.

### Test-time adaptation updates from incoming inputs

Test-time adaptation modifies parameters or model state using test inputs, often without their labels. [Tent](https://arxiv.org/abs/2006.10726) updates normalization-related components through prediction-entropy minimization. Entropy is H(p) = −Σ_c p_c log p_c; reducing it encourages confidence, not necessarily correctness. Unlike averaging predictions over transformed inputs, this procedure changes the model, so batch composition, case order, and reset rules can affect later outputs.

### The type of shift constrains what can work

Under idealized covariate shift, P_s(X) differs from P_t(X) while P_s(Y | X) = P_t(Y | X). Other shifts change disease prevalence, label definitions, or the conditional relationship itself. A scanner change and a different pathology-verification policy may coexist. I would not assume that making images look source-like resolves every change, especially when target cases fall outside source support.

## Worked examples in medical AI

Consider a hypothetical gallbladder classifier transferred to a hospital using a different ultrasound preset. With a separate unlabeled local collection, I could investigate domain adaptation before evaluation. If no target data were available, training across source hospitals and selecting on held-out source environments would instead support a domain-generalization experiment.

A second hypothetical system updates continuously on incoming examinations. A sequence dominated by routine benign studies could influence its state before a rare malignant case arrives. Confidence-based updates might reinforce an existing mistake. Tent's published experiments establish a technical approach on computer-vision benchmarks; they do not establish that this clinical adaptation pathway is beneficial.

## Evaluation methods and limitations

I would compare every adaptive method with the same frozen source model and, where permitted, a clearly labeled supervised local baseline. The protocol should specify target-label access, source-data access, adaptation data, update frequency, and model selection. Using unlabeled evaluation inputs may be legitimate in a declared transductive setting, but that result should not be presented as ordinary frozen external validation.

For online adaptation, evaluation must reproduce realistic ordering and availability of cases. I would test resets, sustained shifts, changing case mixtures, and recovery after harmful updates. Diagnostic performance, calibration, subgroup effects, and update cost all matter. Negative transfer means adaptation worsens target performance; detecting it without timely outcome labels remains difficult. Retaining a frozen comparator and versioned update history would make this behavior easier to audit.

## Research connections and open questions

For gallbladder clinical faithfulness, adaptation raises a temporal question: does the model continue using the same clinical evidence after its state changes? I would audit before and after adaptation, rather than assume that improved target accuracy reflects better clinical reliance.

- Which shifts in my data concern acquisition, and which concern patient selection or reference standards?
- What adaptation signal can distinguish unfamiliar but valid clinical evidence from a nuisance change?
- How can harmful updates be detected when malignant outcomes are sparse and labels arrive late?

## References

- Ganin et al., [Domain-Adversarial Training of Neural Networks](https://jmlr.org/papers/v17/15-239.html), JMLR 2016.
- Gulrajani and Lopez-Paz, [In Search of Lost Domain Generalization](https://arxiv.org/abs/2007.01434), ICLR 2021.
- Wang et al., [Tent: Fully Test-Time Adaptation by Entropy Minimization](https://arxiv.org/abs/2006.10726), ICLR 2021.
