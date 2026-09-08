---
layout: post
title: "Su-In Lee on SHAP Consistency, Clinician Decisions, and Auditing Image Models"
date: 2026-09-10 12:00:00 +0900
description: "Notes on SHAP’s axioms, image ablation, and the Prescience clinician study, with implications for evaluating clinical faithfulness audits of medical image classifiers."
tag: "AIMS Lab"
related_posts: false
---

An attribution method can assign less importance to an image feature even when that feature’s contribution to the model increases. Su-In Lee’s earlier technical talk makes the consistency requirement behind SHAP concrete, then presents a clinician study in which an explained prediction tool improved human judgments but still performed better alone. Both results bear directly on how I would audit a medical image classifier.

[My notes on her later podcast conversation](/blog/2026-09-08-suin-lee-explainable-ai-biology-medicine/) cover the broader applications; this post focuses on the attribution framework, its evaluation, and the implications for my image-auditing work.

## MERGE puts prior knowledge into coefficient uncertainty

### Biological knowledge guides how strongly coefficients are regularized

MERGE is the talk’s biological illustration of a general modeling choice: prior knowledge can change how strongly an association is regularized without excluding unfamiliar features before learning.

Using notation for Lee’s Gaussian construction, the association coefficient between gene $$g$$ and drug $$d$$ has prior

$$
w_{gd}\mid\tau_g^2\sim\mathcal{N}(0,\tau_g^2).
$$

The mean remains zero. Prior knowledge does not specify the association’s direction. Instead, gene-level evidence controls the variance: a larger variance permits a larger coefficient in either direction, while a smaller variance encourages stronger shrinkage toward zero.

MERGE learns shared weights over biological properties to construct a gene’s marker-potential score. Lee describes jointly learning those weights and the gene-drug associations. Thus, the prior’s usefulness is learned from data rather than assumed equally for every kind of biological evidence. The published workflow subsequently prioritizes genes using the learned scores; the distinction is that it does not begin with a fixed biological whitelist. ([MERGE paper](https://doi.org/10.1038/s41467-017-02465-5))

### The variance is not the penalty strength

For fixed variances, the coefficient-dependent Gaussian penalty is

$$
\frac{1}{2}\sum_{g,d}\frac{w_{gd}^{2}}{\tau_g^{2}}.
$$

Regularization strength is proportional to inverse variance. Learning the variances also requires the Gaussian normalization terms; this expression alone is not the complete optimization objective.

I read this as a useful principle for image models that incorporate clinical knowledge. An existing vocabulary of findings can guide learning without being treated as an exhaustive account of useful evidence. The conceptual connection to pathway-informed architectures is the same: knowledge shapes the model while leaving room for what that knowledge misses. This does not establish that a particular soft constraint improves an ultrasound classifier. That would require comparison with alternatives and examination of what the constraint suppresses.

## SHAP derives an allocation from explicit requirements

### An image explanation starts by defining its features and reference

For an image classifier, the features being explained might be pixels, patches, segmented regions, or image-derived descriptors. Those choices define different explanatory tasks. A region attribution does not automatically identify the clinical finding within that region.

Let $$N$$ be the chosen feature set and $$v_x(S)$$ the model output associated with retaining information from subset $$S$$ for image $$x$$. The original SHAP formulation uses conditional expectations:

$$
v_x(S)=\mathbb{E}[f(X)\mid X_S=x_S].
$$

Here, $$v_x(\varnothing)$$ is the baseline and $$v_x(N)=f(x)$$. For images, computing or approximating this expectation is already a substantial modeling decision. Replacing an omitted patch with black pixels generally does not implement conditioning on the visible image.

An additive explanation assigns a contribution $$\phi_i$$ to each feature. Local accuracy requires

$$
f(x)=\phi_0+\sum_{i\in N}\phi_i,
\qquad
\phi_0=v_x(\varnothing).
$$

For a gallbladder classifier, the contributions must reconstruct the selected output relative to the selected reference. Contributions explaining a logit cannot be read directly as probability-point changes.

Local accuracy concerns the explanation’s accounting. It does not establish that the predicted diagnosis is correct or that highlighted tissue is clinically relevant. Nor does reconstructing one prediction demonstrate that a simple additive model approximates the classifier everywhere around the image.

### Consistency requires the attribution to follow increased contribution

Define feature $$i$$’s marginal contribution when other available features are $$S$$ as

$$
\Delta_i v_x(S)=v_x(S\cup\{i\})-v_x(S).
$$

Consistency compares two model games while holding the explanatory setup fixed:

$$
\Delta_i v'_x(S)\geq\Delta_i v_x(S)
\quad\text{for every }S\subseteq N\setminus\{i\}
\quad\Longrightarrow\quad
\phi_i(v'_x)\geq\phi_i(v_x).
$$

Suppose an image region contributes at least as much to the selected class score in a revised classifier, regardless of which other regions are available. A consistent explanation must not assign that region a smaller signed contribution.

The qualification “for every subset” is essential. A larger score change after one occlusion does not meet the premise. Nor does increased anatomical overlap or a brighter heatmap establish increased marginal contribution. The comparison concerns the defined model behavior across coalitions.

Lee emphasizes the practical failure permitted by an inconsistent method: a feature’s actual contribution can rise while its assigned importance falls. “Actual” here concerns the specified model game, not the feature’s causal role in disease.

Although the condition compares models, its failure also undermines feature comparison within one model. A clinician or researcher reading an attribution map expects its values to provide a coherent allocation of contribution. If the method can respond to uniformly stronger contributions by reducing assigned credit, the numerical ordering lacks that justification. Comparing a lesion region with surrounding tissue is then vulnerable to the allocation rule itself.

This is more specific than explanation instability. Two explanations may differ because their references differ. Consistency instead constrains the direction of attribution change when marginal contributions have changed in a defined direction. It does not guarantee the same rankings across different region partitions, baselines, or missing-information rules.

### The uniqueness result fixes the allocation within a specified game

The talk emphasizes local accuracy and consistency. The published theorem also includes missingness: a feature absent from the simplified input representation receives zero attribution. Within the paper’s additive framework and fixed input mapping, these requirements identify Shapley values uniquely. ([Lundberg and Lee, 2017](https://proceedings.neurips.cc/paper_files/paper/2017/file/8a20a8621978632d76c43dfd28b67767-Paper.pdf))

The resulting allocation is

$$
\phi_i=
\sum_{S\subseteq N\setminus\{i\}}
\frac{|S|!\,(M-|S|-1)!}{M!}
\left[v_x(S\cup\{i\})-v_x(S)\right],
\qquad M=|N|.
$$

The weights average the feature’s marginal contribution across every possible ordering in which features could be revealed. Along each ordering, the successive changes sum from the baseline to the final prediction. Averaging preserves that sum and, because the weights are nonnegative, preserves the ordering required by consistency.

For an image, revealing a lesion patch after its surrounding anatomy may contribute differently from revealing the same patch first. Averaging prevents one arbitrarily selected reveal order from determining its credit. The uniqueness result is stronger than showing that this average is convenient: within the stated framework, the requirements leave no alternative allocation.

The theorem does not identify the appropriate image reference or ensure that an approximate implementation satisfies the properties exactly. Those remain separate parts of evaluating the explanation.

### Image deletion requires a defined replacement

This is where the axioms meet my [intervention-based auditing notes](/study/intervention-based-auditing/). Removing an image region is not a clean removal of one column of information. Zeroing creates boundaries, blurring changes texture, and inpainting introduces estimated content. The edit can move the input away from the classifier’s training distribution.

A steep deletion curve can therefore reflect destruction of useful evidence, creation of unfamiliar inputs, or both. It is evidence about the implemented replacement procedure before it is evidence about a named clinical dependency.

I would specify what the edit changes and preserves, compare suitable control edits, and inspect validity independently of prediction changes. A faithful allocation under one removal game need not predict the response to a different ablation procedure. Disagreement becomes interpretable only after those experimental definitions are aligned.

## Prescience improved clinicians’ predictions but did not improve on the model

### The crossover design avoided repeated cases

Prescience predicts hypoxemia risk from patient information and intraoperative measurements, with explanations showing features that raise or lower the estimate. The user study tested whether anesthesiologists made better risk judgments when given this assistance.

Five practicing anesthesiologists reviewed recorded cases through an interface. Cases and clinicians were divided into groups, with assistance assigned in a crossover arrangement: clinicians aided on one case set worked unaided on the other, while the other clinician group received the reverse assignment. No clinician assessed the same prediction task twice. ([Prescience study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6467492/))

This matters because reassessing a familiar case could create an apparent benefit unrelated to the explanation. The complementary assignments avoided that direct memory effect, although differences between readers and cases still contribute uncertainty.

The published intraoperative comparison reports AUROC of 0.66 for unaided anesthesiologists, 0.78 with Prescience assistance, and 0.81 for the model alone. These figures measure discrimination in the reader experiment. They are not percentages of complications prevented. ([Published comparison, Figure 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC6467492/))

### The negative comparison changes how I read the positive result

Clinicians improved with the tool, but their assisted judgments remained slightly worse than its predictions alone. This finding deserves the same visibility as the improvement over unaided performance.

In the supplied transcript, Lee interprets the gap as indicating that clinicians’ adjustments away from the model were more often wrong than right. She also says she omits this comparison when presenting to clinicians. I retain that as her account, rather than treating the explanation as an unqualified success because readers improved.

The performance ordering is reported in the paper. The explanation of the gap requires additional care: aggregate AUROC does not itself count beneficial and harmful overrides. Establishing that mechanism would require examining individual revisions against outcomes under a defined measure of improvement.

Still, the result directly challenges an assumption I could otherwise bring to image auditing. Giving a clinician access to model evidence does not ensure that their disagreement with the model becomes more accurate. An explanation may improve overall use while also enabling some harmful departures from correct predictions.

This does not show that clinicians should always defer. A reader of recorded data may lack information available during care, and risk ranking is only part of clinical work. The supported conclusion concerns the evaluated task: the combined judgment did not outperform the model.

### The explanation’s incremental benefit remains separate

The comparison evaluated an explained prediction tool against unaided assessment. It did not isolate the explanation from the prediction score.

For an image classifier, I would therefore distinguish a reader receiving a model probability from a reader receiving that probability plus a heatmap or audit report. A gain over unaided interpretation could arise from the score, the display, or their combination.

Prescience makes both comparisons necessary. Assistance should be compared with usual judgment to establish whether it helps readers, and the resulting judgments should also be compared with the model’s output. Otherwise, a study can report improvement while leaving the effect of human revisions unexplored.

Retrospective reader performance also remains distinct from patient benefit. Better risk estimates create an opportunity for better decisions, but the study does not establish that the resulting actions prevented hypoxemia.

## The CKD plots retain variation between patients

### Summary and dependence plots answer different questions

The chronic kidney disease example illustrates visualizations that also apply to image-derived feature sets. A SHAP summary plot places one dot per person and feature, with horizontal position indicating attribution and color indicating feature value. Stacking reveals density while preserving uncommon, large contributions that an average ranking could conceal.

A dependence plot instead places feature value on the horizontal axis and its attribution on the vertical axis. Vertical dispersion shows that similar measurements can receive different contributions. Coloring by another feature helps investigate interactions, although dependence assumptions and approximation error also need consideration.

For an image-derived descriptor, this could show whether its contribution varies with other measured findings. It would explain the model operating on those descriptors; it would not automatically explain the underlying pixels.

### The inflection points provide external comparisons

Lee relates a blood-pressure inflection to SPRINT’s intensive-treatment target, emphasizing that the model was not given the trial result. SPRINT compared systolic targets below 120 and below 140 mmHg, finding lower cardiovascular-event and mortality rates with intensive treatment in its eligible population, alongside increases in some adverse events. ([SPRINT trial](https://pubmed.ncbi.nlm.nih.gov/26551272/))

The later tree-explanation paper reports the CKD inflection at 125 mmHg. I preserve that published value separately from the talk’s approximate comparison. Agreement with a treatment threshold is useful external context, but an observational prediction pattern does not reproduce a randomized treatment effect. ([Lundberg and colleagues, Figure 4](https://pmc.ncbi.nlm.nih.gov/articles/PMC7326367/))

Lee also describes a urinary-albumin inflection matching the definition of microalbuminuria. I retain this qualitatively because the plotted measure and units remain unverified. Together, the examples show how explanation plots can support comparison with independent evidence without supplying that evidence themselves.

## My image audits still need evaluation of their effect on readers

### Faithfulness does not establish beneficial reliance

My work on clinical faithfulness auditing examines whether readouts describe a medical image classifier’s behavior and align with independently assessed clinical factors. In hepatobiliary ultrasound, that includes distinguishing responses to morphology from possible reliance on acquisition characteristics or documentation.

The SHAP derivation helps specify an attribution’s computational obligations. Intervention tests then examine selected dependencies under explicit edits. Neither establishes that a clinician reading the resulting audit will make a better decision.

Prescience exposes an unresolved part of my work. A faithful audit could identify a dependency that a clinician finds unfamiliar or unconvincing. If that report makes the clinician distrust a correct model and revise toward an incorrect decision, the audit has done harm through its use.

Faithfulness is necessary for claiming that a readout describes model behavior, but it is insufficient evidence of clinical benefit. A report that accurately exposes a shortcut and one that merely looks unusual could both reduce confidence. Their implications for a particular prediction need not be the same.

### I would evaluate what readers change

My current work has not demonstrated that audit outputs improve clinicians’ ability to distinguish correct image predictions from incorrect ones. I should not infer that benefit from localization, model sensitivity, or clinical-factor agreement.

A subsequent study would compare unaided interpretation, interpretation with model predictions, and interpretation with predictions plus audit information. Case assignments should prevent repeated exposure from confounding the comparisons. The analysis should retain both corrections of model errors and revisions that turn correct predictions into errors.

I would record confidence separately from decision quality and examine disagreements by finding, image quality, and acquisition setting. Patient-level grouping and reader variation would need to remain visible in the uncertainty estimates.

For the present study, I can report the readout’s target, the dependencies supported by controlled comparisons, and the edits whose validity failed. Whether showing those findings improves clinical use of the image classifier requires a separate reader evaluation.
