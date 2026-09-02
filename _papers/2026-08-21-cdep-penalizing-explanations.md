---
layout: post
title: "Interpretations Are Useful: Penalizing Explanations to Align Neural Networks with Prior Knowledge"
date: 2026-08-21 12:00:00 +0900
venue: "ICML 2020"
authors: "Laura Rieger, Chandan Singh, W. James Murdoch, Bin Yu (2020)"
description: "CDEP — penalizing a model's contextual-decomposition-based explanation directly during training, so an explanation isn't just a diagnostic afterward but an actionable lever to fix the model."
related_posts: false
---

**Paper.** *Interpretations are Useful: Penalizing Explanations to Align Neural Networks with Prior Knowledge* — [ICML 2020](https://arxiv.org/abs/1909.13584)

## Why I read it

Most explanation methods stop after showing a model's behavior. CDEP is important because it treats an explanation as something that can be acted on during training: if a known region or feature should not influence the prediction, penalize its contextual contribution.

## What the paper claims

Contextual Decomposition Explanation Penalization uses group-level contextual decomposition scores as a regularizer. This differs from penalizing a raw input gradient: the method can target the contribution of a meaningful group of pixels or features, including interactions that simple first-order saliency may miss. Prior knowledge is therefore written as a constraint on the model's reasoning, not only on its output.

## What convinced me

The comparison with gradient-based Right for the Right Reasons is especially informative. On ColorMNIST, where the unwanted rule depends on a higher-order color interaction, CDEP reached about 31% accuracy while vanilla and RRR models remained near chance; on DecoyMNIST it reached 97.2%. In the ISIC patch experiment, CDEP also preserved no-patch performance better than the unregularized model, with AUC 0.89 versus 0.87. These experiments show that the form of the explanation being penalized matters.

## What it leaves open

The method requires the practitioner to name the undesirable evidence in advance and specify it at an appropriate granularity. Incorrect or incomplete priors may suppress useful signal or simply redirect the network to another unmeasured shortcut. Better performance after regularization does not prove that the remaining features are clinically causal.

## What I take from it

Explanation regularization is strongest when it is paired with a falsifiable behavior test: remove the targeted shortcut, reverse its correlation, and verify that performance no longer depends on it. CDEP is a foundational example of explanations functioning as training constraints rather than decorative visualizations.
