---
layout: post
title: "Assessing the Trustworthiness of Saliency Maps for Localizing Abnormalities in Medical Imaging"
date: 2026-03-13 12:00:00 +0900
venue: "Radiology: Artificial Intelligence"
authors: "Arun, Gaw, Singh, Chang, Aggarwal, Chen, Hoebel, Gupta, Patel, Gidwani, Adebayo, Li, Kalpathy-Cramer (2021)"
description: "Radiology-specific saliency evaluation: sanity checks and human-alignment tests applied directly to chest radiograph localization tasks."
related_posts: false
---

**Paper.** *Assessing the Trustworthiness of Saliency Maps for Localizing Abnormalities in Medical Imaging.*

The paper asks whether saliency maps are dependable enough to be used for abnormality localization in medical images. This is a practical question because classification studies often display a heatmap over a lesion and interpret the overlap as evidence that the network found the abnormality. Selected illustrations cannot establish how reliably that behavior occurs, or whether the map meaningfully depends on the learned model.

The question was open partly because “trustworthy explanation” combines several different properties. A map can overlap an abnormality yet change substantially when the classifier is retrained. It can look stable while being insensitive to learned weights. It can also be model-dependent without localizing the clinical target well. The authors make these properties separately testable.

They evaluate eight saliency methods using the SIIM-ACR pneumothorax segmentation dataset and the RSNA pneumonia detection dataset. The criteria cover localization utility, sensitivity to weight randomization, repeatability across models trained with the same architecture, and reproducibility across different architectures. Comparators include an average reference mask and dedicated localization networks, U-Net for segmentation and RetinaNet for detection.

Every evaluated saliency method fails at least one criterion. Reported localization AUPRC ranges are 0.024 to 0.224 for pneumothorax, compared with 0.404 for U-Net, and 0.160 to 0.519 for pneumonia, compared with 0.596 for RetinaNet. These are localization evaluations. They should not be confused with patient-level diagnostic AUPRC or compared directly across the two tasks as if their annotation units were identical.

The average-mask baseline is an especially useful design choice. Medical anatomy and dataset curation can make some locations more likely to contain abnormalities than others. A map can therefore achieve nontrivial overlap without responding meaningfully to the individual examination. Comparing with a simple spatial prior asks whether the explanation adds localization information beyond that background structure.

The dedicated localization models answer a different but equally useful question: how well can the task be performed when localization is explicitly supervised? Their advantage does not show that a classifier-trained explanation had access to the same supervision and failed a perfectly matched learning contest. It shows the practical gap between using an explanatory map as a localizer and training a model for localization.

That distinction makes the comparison fair for the paper's intended-use question. If a researcher wants to present a map as a lesion-localization tool, the user cares about its performance relative to suitable alternatives. If the narrower question is whether the map faithfully describes a classifier's computation, localization overlap alone is incomplete. A classifier might genuinely rely on context outside the annotated abnormality, appropriately or inappropriately, and a faithful explanation could reveal that.

Weight randomization addresses dependence on learned parameters. If the map changes little when the learned predictor is replaced by randomized weights, its visual structure may be driven substantially by the image or explanation procedure. Such a result challenges the claim that the map explains the trained model. Passing that check, however, does not establish clinical correctness; it only closes one particular gap.

Repeatability and reproducibility also need careful interpretation. They concern explanations from separately trained predictors, not merely whether a deterministic plotting function returns the same array twice. If two models have comparable diagnostic performance but produce different maps, several explanations remain possible. The attribution procedure may be unstable, the models may actually use different evidence, or both may be true.

This is where the underspecification paper becomes relevant. Similar predictive performance does not require identical internal solutions. Disagreement between saliency maps is therefore evidence that a proposed stable localization claim needs investigation, but it is not automatically proof that every differing map is mathematically unfaithful. The explanatory quantity and the intended clinical use determine what kind of consistency should be expected.

The strongest limitation is the scope of the evaluated methods, models, and tasks. Pneumothorax segmentation and pneumonia localization are important examples, but they do not exhaust medical imaging or all possible uses of attribution. The study does not establish that explanations can never help generate a hypothesis, expose a gross artifact, or support a carefully specified model comparison.

Annotation and metric choices also influence the localization result. A segmentation mask and a bounding box express different spatial references. Converting a continuous saliency map into a localization evaluation introduces choices about scaling, thresholding, and how background is handled. These choices should be specified before comparing methods. A visually sharper display is not necessarily a better localizer under an independently defined metric.

The paper directly strengthens [Explanation Faithfulness versus Plausibility]({{ '/study/explanation-faithfulness-versus-plausibility/' | relative_url }}). Anatomical agreement, model dependence, and stable behavior are distinct claims. It also gives an empirical counterpart to [Attribution, Attention, and Counterfactual Explanations]({{ '/study/attribution-attention-and-counterfactual-explanations/' | relative_url }}), which asks readers to identify the quantity computed before interpreting its visualization.

[Intervention-Based Auditing]({{ '/study/intervention-based-auditing/' | relative_url }}) identifies what remains when the desired claim concerns reliance on clinical evidence. A localization benchmark tells me where a map lies relative to an annotation. A controlled intervention asks how the prediction changes when a specified piece of evidence is altered. Neither question subsumes the other, and interventions themselves need controls for artifacts and unintended information loss.

For my ultrasound work, I would first decide whether a displayed map is intended as a locator, an explanation of a score, or a tool for forming audit hypotheses. A localization claim would require independent annotations and appropriate spatial baselines. A reliance claim would require tests tied to named findings, with attention to whether those findings are assessable in the selected views.

I would also report a representative set of cases, including failures, rather than treating a gallery of successful overlays as validation. Where maps differ across seeds or architectures, I would investigate whether prediction behavior changes under the same controlled edits. The paper's lasting contribution is a set of questions that makes explanation use accountable: useful for which task, dependent on which model, stable under which changes, and supported by which reference?
