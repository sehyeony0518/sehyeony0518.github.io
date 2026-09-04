---
layout: post
title: "Learning Causal Alignment for Reliable Disease Diagnosis"
date: 2026-06-27 12:00:00 +0900
venue: "ICLR 2025"
authors: "Mingzhou Liu, Ching-Wen Lee, Xinwei Sun, Xueqing Yu, Qiao Yu, Yizhou Wang (2025)"
description: "A causal framing of the shortcut-learning problem in disease diagnosis, trying to explicitly align a model's learned representation with the causal structure of disease, not just penalize known spurious features after the fact."
related_posts: false
---

**Paper.** *Learning Causal Alignment for Reliable Disease Diagnosis*. [ICLR 2025](https://arxiv.org/abs/2310.01766)

## Why I read it

The title is close to the question I am pursuing, whether a diagnostic model follows a clinically valid evidence chain rather than merely correlating with the label. I read it to see how the paper operationalizes "causal alignment" and how strong the resulting evidence really is.

## What the paper claims

The method generates counterfactual samples, identifies changes associated with diagnostic attributes, and trains the classifier with a causal-alignment loss and a hierarchical alignment procedure. The objective is to make the model's visual evidence agree with expert-defined disease attributes while maintaining classification performance.

## What convinced me

The study evaluates lung nodules and breast masses, with additional modalities in the appendix, and includes controlled artificial shortcuts. On LIDC and DDSM, CAM precision reached 0.751 and 0.805, while classification accuracy was 0.722 and 0.656. The ablations attribute much of the localization gain to the alignment loss rather than to the backbone alone. The counterfactual component is valuable because it creates a stronger training signal than simply rewarding visually plausible heatmaps.

## What it leaves open

The causal claim depends on the realism of the generator, the chosen attribute hierarchy, and the assumption that those attributes sufficiently describe the diagnostic pathway. Artificial symbols are useful controls but are simpler than diffuse clinical confounding. CAM precision is still a localization proxy; it does not establish that correcting an attribute would change the prediction or improve a clinical decision.

## What I take from it

This paper is best read as clinically supervised representation alignment, with causal motivation rather than complete causal identification. I would strengthen the claim with concept interventions, counter-shortcut external tests, and explicit analysis of cases where the expert attribute set is incomplete.
