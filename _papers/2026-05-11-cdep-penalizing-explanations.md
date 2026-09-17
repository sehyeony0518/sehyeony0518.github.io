---
layout: post
title: "Interpretations Are Useful: Penalizing Explanations to Align Neural Networks with Prior Knowledge"
date: 2026-05-11 12:00:00 +0900
venue: "ICML 2020"
authors: "Laura Rieger, Chandan Singh, W. James Murdoch, Bin Yu (2020)"
description: "CDEP, penalizing a model's contextual-decomposition-based explanation directly during training, so an explanation isn't just a diagnostic afterward but an actionable lever to fix the model."
og_image: "https://sehyeony0518.github.io/assets/img/og/2026-05-11-cdep-penalizing-explanations.png"
related_posts: false
---

**Paper.** *Interpretations are Useful: Penalizing Explanations to Align Neural Networks with Prior Knowledge*. [Published ICML paper](https://proceedings.mlr.press/v119/rieger20a/rieger20a.pdf)

## The question explanations should help answer

An explanation can identify a suspicious model behavior without providing a way to change it. This paper asks whether prior knowledge about appropriate evidence can be incorporated directly into training by penalizing an explanation.

The question is not merely whether a heatmap can be made more attractive. A useful correction should change the predictor's behavior when the unwanted relationship breaks.

That distinction matters in medical imaging. If a skin-lesion classifier exploits a calibration patch, showing the patch in an explanation is only the first step. Removing all affected training images may discard useful examples, while leaving them untouched preserves the opportunity for shortcut learning.

CDEP proposes another option: retain the examples while discouraging the specified contribution to the prediction.

## What contextual decomposition contributes

Contextual Decomposition Explanation Penalization adds a penalty on contextual-decomposition contributions to the prediction objective. The practitioner specifies features or groups whose contributions should follow a prior.

The skin-lesion experiment penalizes patch contributions. ColorMNIST instead penalizes contributions of isolated pixels to encourage dependence on spatial combinations associated with digit shape. DecoyMNIST tests class-correlated corner patches. These are different priors, expressed through the same general approach. [Method and experiments](https://proceedings.mlr.press/v119/rieger20a/rieger20a.pdf)

The feature grouping is therefore part of the scientific claim. A penalty on a whole region asks a different question from penalties on individual pixels. Interactions can make the group's contribution differ from the sum of intuitive pixel-level effects.

Contextual decomposition also differs from a raw input gradient. A gradient describes local response to an infinitesimal change. A decomposition assigns contributions according to a particular rule for propagating selected and remaining information through the network.

Neither description is automatically equivalent to a clinical intervention. The advantage is that the decomposition creates an actionable training quantity whose relationship to desired behavior can be tested.

## What the published results actually say

On ColorMNIST, CDEP reaches 31.0% accuracy under the altered color relationship; vanilla and RRR results are about 0.2%, while random prediction is 10%. On DecoyMNIST, CDEP reaches 97.2%, versus 99.0% for RRR.

The published ICML ISIC table reports no-patch AUC 0.95 for CDEP and 0.93 for the vanilla model. The earlier review's 0.89 versus 0.87 comparison does not match that table. [Tables 1 and 2](https://proceedings.mlr.press/v119/rieger20a/rieger20a.pdf)

The ColorMNIST result is meaningful but incomplete. Recovering above-chance performance shows that the penalty changed the learned solution under this construction. Accuracy of 31% does not establish that color dependence has been eliminated.

The DecoyMNIST comparison also prevents a blanket conclusion that contextual-decomposition penalties dominate gradient penalties. Different unwanted rules, groupings, and optimization conditions can favor different approaches.

The ISIC no-patch result evaluates images where patches are absent. It is not, by itself, a paired removal experiment in which the identical lesion image is tested before and after patch removal. That distinction affects how directly the result measures patch reliance.

## What is held fixed, and what changes

The basic comparison changes the training objective while retaining the diagnostic task. This estimates the consequence of training with the specified prior, including any resulting change in representation and optimization.

It does not isolate the contribution of a single feature within one already-fitted network. Retraining can alter many aspects of the learned rule.

This matters when interpreting a successful ablation. Better counter-shortcut performance could arise because the model suppresses the named cue, strengthens another valid cue, or changes its decision boundary more broadly. Those possibilities are compatible with a useful training method, but they are different mechanistic explanations.

For a strong comparison, annotation access and tuning resources should also be considered. A method supplied with reliable artifact masks has information unavailable to a baseline trained only on diagnostic labels. That can be entirely appropriate, provided the comparison is described as the value of that complete procedure.

## The weakness I would raise

The method depends on the prior being correct and operationally precise. A region designated irrelevant might contain useful anatomy, an acoustic effect, or evidence about whether the image is interpretable.

For ultrasound, a simple “outside the lesion is irrelevant” rule would be especially questionable. Context may be necessary to interpret a finding, and posterior acoustic effects occur outside the apparent lesion boundary.

The explanation itself is another dependency. Training can improve agreement with the chosen decomposition target without establishing invariance under every meaningful change to the targeted feature. A model may retain redundant or interacting routes that the penalty does not adequately constrain.

There is also a practical comparison limitation in the paper's ISIC experiment: the authors describe memory and optimization constraints on RRR. That does not invalidate the result, but it limits an interpretation that attributes all performance differences solely to the conceptual superiority of one explanation family.

I would therefore treat CDEP as a method for injecting a specified prior, with behavioral effectiveness evaluated independently. It is not a guarantee that the remaining reasoning is clinically correct.

## Connections to the study notes

[Clinical Alignment and Knowledge as Supervision](/study/clinical-alignment-and-knowledge-as-supervision/) distinguishes the object optimized by a knowledge term from the behavior one hopes to obtain. CDEP is a concrete example: the immediate target is a decomposition-based contribution, while the desired endpoint is reduced dependence on inappropriate evidence.

[Explanation Faithfulness versus Plausibility](/study/explanation-faithfulness-versus-plausibility/) explains why a preferred explanation is not sufficient validation. An explanation used as a training constraint should be supplemented with tests that do not merely reward the same representation of importance.

[Intervention-Based Auditing](/study/intervention-based-auditing/) provides those tests. A frozen corrected model can be evaluated under valid cue removal, cue insertion, and changed cue-label association, with controls for the editing procedure.

The Reveal2Revise review extends this idea operationally by connecting discovery, annotation, correction, and another audit. CDEP supplies one important part of that larger process.

## How I would use it

I would begin with a prior that is narrow enough to defend, such as independence from a separately removable documentation overlay. I would compare ordinary training, a simple data-level correction, and explanation regularization under matched development conditions.

Evaluation would include paired overlay changes, a correlation-shift test, and checks that independently annotated clinical findings remain recognized. Penalty strength would be chosen without consulting the final audit set.

The paper's lasting contribution is that explanations can participate in model revision. The standard for success should remain the resulting behavior under a clearly specified test, with preservation of useful evidence evaluated alongside removal of the unwanted dependence.
