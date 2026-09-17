---
layout: post
title: "Evaluating Shortcut Utilization in Deep Learning Disease Classification Through Counterfactual Analysis"
date: 2026-06-13 12:00:00 +0900
venue: "MIDL 2025"
authors: "Vibujithan Vigneshwaran, Emma A.M. Stanley, Raissa Souza, Erik Ohara, Matthias Wilms, Nils D. Forkert (2025)"
description: "A counterfactual-generation approach to quantifying shortcut reliance in disease classifiers, in the same spirit as RoentMod but framed as a general evaluation method rather than a modality-specific tool."
og_image: "https://sehyeony0518.github.io/assets/img/og/2026-06-13-counterfactual-shortcut-utilization.png"
related_posts: false
---

**Paper.** *Evaluating Shortcut Utilization in Deep Learning Disease Classification through Counterfactual Analysis*. [MIDL manuscript](https://openreview.net/pdf?id=vxSo5TJxlB)

## The distinction that motivates the paper

A probe can recover acquisition site or sex from a neural representation even when the diagnostic head does not use that information. Conversely, a model can exploit a complex attribute representation that a particular probe fails to recover.

The paper asks the more consequential question: how much does diagnostic performance change when information associated with a specified attribute is counterfactually removed?

That moves the audit from representation availability toward computational reliance. It also introduces a new difficulty. In real clinical data, an otherwise identical patient observed at every site is generally unavailable. A method must construct the missing comparison or use a more limited observational design.

The authors construct it in activation space. That avoids generating a complete MRI, but it does not remove the need to validate what the intervention preserves.

## What the authors actually did

The study uses T1-weighted MRI from 835 subjects at nine sites, including 426 people with Parkinson's disease and 409 healthy subjects. A disease classifier supplies penultimate-layer activations.

MACAW, a causal generative model using masked normalizing flows, models those activations under a specified graph. For an attribute such as site, the method generates counterfactual activations for its possible values and averages them. The resulting representation is passed to the disease prediction layer.

The data are split within the multisite collection, stratified by site and sex; this is not a leave-one-site-out external test. [Methods and study design](https://openreview.net/pdf?id=vxSo5TJxlB)

Averaging counterfactual activations is an important detail. “Removal” is the name given to a particular standardization operation. It is not direct observation of a representation from which a physically separable site component has been extracted.

## What the reported contrast shows

After the site intervention, disease AUROC falls from approximately 0.74 to 0.65. The sex intervention changes AUROC by about 0.004. Attribute probes and representation visualizations are used to assess the intervention's effect. [Results](https://openreview.net/pdf?id=vxSo5TJxlB)

The 0.09 change is an absolute AUROC difference. It should not be described as nine percent of the model's decisions or nine percent of its information coming from site.

The site-versus-sex contrast is useful because representation accessibility alone would not establish this difference in task consequence. Under the implemented intervention, site-related changes matter much more to aggregate discrimination.

However, the result is conditional on the generator and graph. It is evidence that the classifier's performance changes under the generated activation transformation. Interpreting the entire change as shortcut utilization requires confidence that valid disease information was preserved.

The method also evaluates dependence, not successful mitigation. Lower performance after removing a predictive cue can reveal a vulnerability without providing a replacement diagnostic rule.

## The causal graph does substantive work

A graph determines which relationships the generator is allowed to represent and which variables are held fixed during counterfactual construction.

This is particularly consequential for site. Site can summarize scanner characteristics, recruitment, disease severity, demographic composition, and processing conventions. A single site variable can therefore mix several mechanisms.

If the graph treats disease-related variation as separable from site-related variation, the counterfactual inherits that assumption. It does not establish separability from the observed data alone.

The same issue applies to sex. Whether an attribute is an inappropriate shortcut depends on the clinical question and its relationships with anatomy and disease. Removing a named demographic variable is not automatically equivalent to removing only unjustified evidence.

I would therefore want the graph translated into plain clinical statements: which differences are supposed to disappear, which should remain, and which relationships are deliberately excluded? Those statements are more informative than the word “causal” by itself.

## The central weakness is preservation

The authors acknowledge that distortion by the generative model is an alternative explanation for a performance drop. This is the limitation I would examine first.

An attribute probe becoming unsuccessful shows that the tested probe can no longer recover the attribute effectively. It does not establish that every form of attribute information has disappeared, or that unrelated disease information remains intact.

The small disease-performance change under sex removal is a useful comparison, but it does not fully validate site removal. Different attributes can require counterfactuals of different difficulty and affect different parts of the activation distribution.

Averaging also deserves attention. The average of several plausible representations need not itself represent a plausible individual image. The prediction layer can still process it, but the resulting score describes the chosen computational construction.

A useful control would reconstruct activations without changing the attribute and measure the diagnostic effect. Additional controls could examine whether independently assessed disease features remain recoverable and whether conclusions persist under defensible alternative graphs.

These tests would not eliminate every identification problem. They would make the main alternative explanations more constrained and visible.

## Why a small aggregate effect is limited evidence

The sex result should not be generalized into a claim that sex is irrelevant to every prediction or that the model is fair.

AUROC summarizes ordering across positive-negative pairs. Individual scores or threshold decisions could change while overall AUROC changes little. Opposing effects across subgroups can also cancel in an aggregate comparison.

I would inspect paired score changes, harmful decision flips at a fixed threshold, and results within sufficiently represented subgroups. Those outcomes answer questions that a single AUROC difference cannot.

Similarly, an intervention that lowers pooled AUROC could improve some sites while worsening others. The distribution of effects matters for understanding which patients were supported by the original site association.

## Connections to the study notes

[Representation-Level Auditing](/study/representation-level-auditing/) separates decodability from downstream use. This paper directly operationalizes the next step by combining representation changes with the response of the diagnostic head.

[Causal Inference for Medical AI](/study/causal-inference-for-medical-ai/) emphasizes that counterfactuals require a specified intervention and preserved background conditions. The graph and averaging procedure are therefore central parts of the estimand, not implementation details that can be omitted from a review.

[Intervention-Based Auditing](/study/intervention-based-auditing/) provides the preservation and sham-control logic needed to evaluate the generated comparison.

[Evaluation Beyond AUROC](/study/evaluation-beyond-auroc/) explains why the aggregate performance difference should be supplemented with threshold behavior and subgroup consequences.

The paper also complements Boland's layer-localization study. Locating an accessible shortcut representation and measuring the effect of a specified activation intervention answer related but distinct questions.

## How I would use the approach

I would begin with an attribute whose intervention has a defensible interpretation and sufficient overlap in the observed data. For ultrasound, an overlay with paired marked and unmarked frames could provide a useful check against an activation-space estimate.

I would freeze the original diagnostic model, validate reconstruction and preservation controls, and report the paired response distribution alongside performance changes.

External acquisition tests would then provide another comparison. Agreement between activation interventions, valid input interventions, and transfer behavior would strengthen the reliance interpretation. Disagreement would identify an assumption worth investigating rather than a result to average away.
