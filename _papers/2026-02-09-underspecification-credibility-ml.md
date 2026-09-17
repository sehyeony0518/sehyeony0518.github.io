---
layout: post
title: "Underspecification Presents Challenges for Credibility in Modern Machine Learning"
date: 2026-02-09 12:00:00 +0900
venue: "JMLR"
authors: "Alexander D'Amour, Katherine Heller, Dan Moldovan, Ben Adlam, Babak Alipanahi, Alex Beutel, Christina Chen, Jonathan Deaton, et al. (2020)"
description: "Two models with identical training accuracy, identical architecture, and different random seeds can behave completely differently under distribution shift, a Google-scale audit of just how common this is, including in a dermatology model."
og_image: "https://sehyeony0518.github.io/assets/img/og/2026-02-09-underspecification-credibility-ml.png"
related_posts: false
---

**Paper.** *Underspecification Presents Challenges for Credibility in Modern Machine Learning.* The work circulated as a preprint in 2020; the final JMLR publication is from 2022.

The paper asks why a development pipeline can repeatedly produce models with similarly strong test performance but different behavior on properties that matter after deployment. The issue is not simply that a model encounters unfamiliar data. It is that the training and validation requirements may never have selected a unique, deployment-appropriate behavior among the solutions they admit.

This remained an important gap in ordinary evaluation practice. A held-out set from the development distribution can estimate performance under that distribution, yet it may barely distinguish two models that use different predictive relationships. Choosing the checkpoint with the slightly better aggregate score can then feel scientifically decisive when the difference says little about the intended deployment requirement.

The authors call a pipeline underspecified when it can return distinct predictors with equivalently strong performance under its stated evaluation criteria. Their evidence spans several application areas. The medical imaging examples are particularly relevant here because they make the omitted requirements concrete: performance across retinal camera types and across skin-type strata.

In the retinal experiment, the authors examine ten models differing in random initialization at fine-tuning. They evaluate diabetic-retinopathy prediction on a camera type absent from training and validation. Variation on that camera is larger than suggested by ordinary test performance, and models with similar calibration on familiar cameras can differ on the held-out camera. A dermatology experiment similarly examines ten predictors and subgroup accuracy, with exploratory analysis of how much variability could reflect sample size.

These examples are stronger than merely showing that one model performs poorly externally. They expose variation among outputs of an otherwise shared development procedure. Random initialization is useful here as a way to sample different solutions. It is not itself a clinical cause of failure. The important observation is that the accepted development criteria leave room for consequential differences.

The result also does not require exactly identical training accuracy or identical predictions. “Equivalently strong” means that the ordinary evaluation treats predictors as comparable for the purpose at hand. They can still disagree on particular cases. The paper's argument concerns whether the pipeline's selection criteria adequately specify the behavior being claimed, rather than whether two numerical scores match to every decimal place.

Underspecification and distribution shift are related but distinct. Shift changes the distribution on which a predictor is evaluated. Underspecification concerns the set of predictors the development process can accept. A shift can expose differences within that set, but subgroup tests within an existing dataset may expose them too. This distinction changes the remedy: collecting a larger ordinary test set may improve precision without adding the missing behavioral requirement.

The medical examples also show why calibration cannot be treated as a property established once for a model family. Two runs may look similar on familiar data while assigning probabilities differently after a camera change. The Guo calibration review provides a tool for correcting probabilities under a specified distribution. This paper adds a pipeline-level question: how much does the need for that correction vary among apparently interchangeable development runs?

A careful reader should question how broadly the case studies establish the prevalence of the problem. They demonstrate consequential examples across domains, but they are not a representative survey estimating how often every modern pipeline fails. Likewise, stress-test variation is not automatically clinically important. Its significance depends on the endpoint, operating rule, affected patients, and uncertainty. A small subgroup with few outcomes may support only a limited conclusion.

The dermatology analysis is useful precisely because it considers sampling variability rather than treating every visible difference between runs as a substantive effect. I would preserve that caution when borrowing the paper's message. Repeating training does not eliminate uncertainty in the test population, and subgroup comparisons remain sensitive to the number and composition of available patients.

The larger limitation is that underspecification is easier to diagnose than to eliminate. A finite stress-test panel can constrain the accepted solutions along selected axes, but it cannot cover every future environment. Domain knowledge is needed to decide which requirements matter. Once stress tests are used to select a model, they also become part of development and need independent confirmation.

This paper deepens [Reproducibility, Benchmarks, and Translational Study Design]({{ '/study/reproducibility-benchmarks-and-translational-study-design/' | relative_url }}). Reproducing a benchmark number is useful, but a credible pipeline should also reproduce the behavior supporting its clinical claim. Seed variation is therefore a scientific quantity to investigate when it changes that behavior, rather than an implementation detail to hide behind one selected checkpoint.

It also complements [Distribution Shift and Out-of-Distribution Generalization]({{ '/study/distribution-shift-and-out-of-distribution-generalization/' | relative_url }}) and [Robustness, Subgroup Performance, and External Validation]({{ '/study/robustness-subgroup-performance-and-external-validation/' | relative_url }}). Those notes ask which relationships and populations support a transfer claim. Underspecification adds that different models trained under the same nominal procedure may answer those questions differently.

For my ultrasound work, I would begin by defining requirements before comparing seeds: acceptable behavior across devices, stable performance in difficult presentations, and appropriate responses to changes in clinical evidence. I would then examine the joint distribution of ordinary performance and these additional outcomes across several runs. Selecting only the best ordinary score and auditing that checkpoint afterward would miss information about the reliability of the procedure.

Ensembling could be evaluated as one response, but it should not be assumed to solve the problem. An ensemble can average variable predictions while preserving a shortcut shared by its members. Similarly, adding a clinical loss may narrow the solution set while leaving other behaviors unspecified. Each proposed repair needs evaluation against the requirement it is meant to address.

The practical contribution is a change in the object being assessed. A checkpoint is one output of a development process. Credibility concerns whether that process reliably produces systems satisfying the intended requirements, and whether the available evaluation could distinguish an acceptable solution from a problematic one.
