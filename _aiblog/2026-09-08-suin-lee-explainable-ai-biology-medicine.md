---
layout: post
title: "Beyond Feature Attribution: Su-In Lee on Explainable AI for Biology and Medicine"
date: 2026-09-08 12:00:00 +0900
description: "Notes from a TWIML conversation on SHAP, biological interpretation, counterfactual clinical audits, and the connection to my research on clinical faithfulness in gallbladder ultrasound AI."
tag: "AIMS Lab"
featured: true
related_posts: false
---

Su-In Lee argues that assigning importance to individual features is insufficient for the biological and clinical problems her lab wants to solve. A gene ranking does not explain how a treatment works, and a pixel attribution does not establish which clinical finding a classifier uses. I found this distinction especially relevant to my work on clinical faithfulness auditing, where anatomical agreement can be much easier to demonstrate than dependence on clinically meaningful evidence.

These notes follow her conversation with Sam Charrington on the TWIML AI Podcast, *Explainable AI for Biology and Medicine*, published on August 14, 2023, around her talk at the ICML Workshop on Computational Biology. Lee is a professor at the University of Washington's Paul G. Allen School of Computer Science and Engineering and leads the AIMS Lab. I use the conversation as the main source, with published papers to clarify particular methods and later developments. ([TWIML episode](https://twimlai.com/podcast/twimlai/explainable-ai-for-biology-and-medicine))

## Research across machine learning, biology, and medicine

Lee describes a research program spanning foundational explainable AI, computational biology, and clinical diagnosis and auditing. Her interest in biomedical problems began during her machine learning training at Stanford, working with high-dimensional data. Gene expression measurements offered a setting where better methods could help identify disease mechanisms and therapeutic targets.

After joining Washington, contact with researchers using electronic health records expanded that work into clinical departments, including anesthesiology, dermatology, and emergency medicine. In her account, these encounters affected the problems the lab chose to study.

Lee expects biology and clinical medicine to become increasingly connected. Selecting a cancer treatment for an individual patient already brings molecular measurements into a clinical decision. Understanding those measurements requires biological knowledge, while deciding what constitutes a useful prediction requires knowledge of the treatment setting.

Her advice to students is to become bilingual or trilingual across computer science, biology, and medicine. I read this as a requirement to understand enough of each field to formulate the research problem responsibly. Collaboration remains necessary, but an ML researcher cannot leave every decision about biological meaning or clinical relevance until after fitting the model.

## Feature attribution leaves part of the scientific problem unresolved

Lee introduces feature attribution through its familiar formulation: a model receives an input, produces a prediction, and an explanation assigns contributions to input features. SHAP draws on cooperative game theory to make that allocation principled. Lundberg and Lee introduced the framework in *A Unified Approach to Interpreting Model Predictions* at NeurIPS 2017. ([Original SHAP paper](https://proceedings.neurips.cc/paper_files/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html))

Her criticism concerns what that allocation accomplishes. In biology, knowing which genes receive large importance scores may leave the relevant scientific problem largely untouched. Researchers want to understand how genes participate in functional processes, how those processes relate to disease, and why they might explain treatment response.

The dermatology example makes the same point in a different modality. A map identifying pixels associated with a melanoma prediction does not necessarily identify the image attributes on which the classifier depends. Lee argues that modifying the image and examining changes that alter the prediction can reveal aspects of model behavior that an attribution map leaves unresolved.

Charrington describes this as moving toward system-level or process-level explanation grounded in the use case, and Lee agrees. I understand that exchange as a demand to connect explanations to the biological process or clinical decision under investigation. It does not mean that one explanation method recovers an entire biological mechanism or clinical workflow.

### The theoretical framework still matters

Lee continues to regard removal-based explanation and cooperative game theory as useful foundations. A feature's contribution is evaluated in the context of other available features, rather than through an isolated score detached from the model's response.

The later paper *Explaining by Removing*, by Covert, Lundberg, and Lee, organizes explanation methods according to how they remove information, which model behavior they explain, and how they summarize influence. Those choices matter when interpreting disagreement between methods. ([JMLR, 2021](https://www.jmlr.org/papers/v22/20-1316.html))

Lee also describes the computational difficulty of evaluating many feature subsets. Her lab's work includes faster estimation and methods adapted to particular model families. Larger models make that practical constraint more severe. She identifies explanation robustness, multimodal attribution, and explanations for foundation models as continuing research directions.

My reading is that the theoretical and applied criticisms are compatible. A well-defined attribution can be useful while answering a narrower question than the scientist or clinician needs answered.

## The AML study moves from explanations to a biological hypothesis

Lee's main biological example concerns predicting drug synergy in acute myeloid leukemia, or AML. She describes the difficulty of selecting combinations from many possible drugs, especially when patients with the same diagnosis can respond differently.

In her formulation, the model uses patient gene expression and information about a pair of drugs to predict their synergy. Explanations should help identify the molecular characteristics associated with a promising combination. The more ambitious objective is to find a principle that explains patterns across combinations and patients.

The corresponding paper is Janizek and colleagues' *Uncovering expression signatures of synergistic drug responses via ensembles of explainable machine-learning models*, published in *Nature Biomedical Engineering* in 2023. ([Paper record](https://pubmed.ncbi.nlm.nih.gov/37127711/))

### Pathway analysis followed model training

Lee emphasizes that the researchers trained with individual genes as features. They did not require the predictor to operate only through predefined pathways. After generating feature attributions, they examined whether influential genes were enriched in biologically defined gene sets, using statistical testing and correction for multiple comparisons.

That order matters. Existing biological knowledge helped interpret the learned associations without specifying every permissible association during training. Lee argues that computational methods need this flexibility because prior knowledge remains incomplete.

In the conversation, she describes a finding involving a hematopoietic stem cell-like expression signature. She interprets the combination principle in terms of complementary activity against less differentiated and more differentiated cancer cells. I take this as a reported biological interpretation of the study, not a general treatment rule or evidence that an attribution score can select a patient's therapy.

Lee also explains that AML was a practical choice because of available samples and drug-response data. She sees broader applicability, but applying the approach elsewhere would still require suitable measurements and validation.

What interests me is the additional analysis between feature importance and biological interpretation. The researchers aggregated explanations, related them to functional categories, and tested the resulting patterns. An individual prediction's explanation became part of a larger investigation.

### Correlated features complicate the interpretation

Lee identifies feature correlation as a problem that foundational explainability work has not adequately resolved for biomedical applications. Genes can vary together, making the allocation of importance among them sensitive to which predictive relationships a fitted model happens to use.

She describes averaging attributions across multiple trained models to obtain more robust explanations. This is particularly relevant when several models predict similarly but distribute importance differently across correlated inputs.

I would keep the distinction between stability and identification explicit. Averaging can reduce variation across fitted models without establishing which gene has a causal biological role. Likewise, a Shapley allocation is well-defined once its underlying game is specified; that does not make the game's treatment of missing or correlated features uniquely appropriate for the scientific question.

For my own work, this makes explanation stability a separate evaluation target. Similar predictive performance across training runs would not establish that those runs use the same evidence.

## Counterfactual images extend the clinical audit

In the clinical part of the conversation, Lee describes auditing dermatology classifiers on separate held-out images and finding concerning behavior. Feature attributions helped investigate the models, but she argues that they showed only part of what needed examination.

Her counterfactual approach changes an image so that the classifier produces a different prediction, then examines the attributes that changed. This creates a comparison between model responses that can be interpreted using clinical knowledge.

The group's published dermatology audit combines generative counterfactuals with physician assessment. It reports reliance on both clinically recognizable features, such as lesional pigmentation patterns, and undesirable features, including background skin texture and colour balance. The article appeared online in December 2023 and in the journal's 2025 volume, so it is a published follow-up to the work discussed as under review in the episode. ([DeGrave and colleagues](https://doi.org/10.1038/s41551-023-01160-9))

### A changed prediction needs an interpretable comparison

I find this approach closer to an audit of evidence use than a heatmap alone because it connects an observable image change to an observable model response. Physician assessment supplies a vocabulary for describing that change.

The strength of the conclusion still depends on the edit. A generated image can cross a decision boundary while changing several attributes together. It can also contain artifacts or altered contextual information. Clinical plausibility helps assess whether the comparison is credible, but it does not establish that exactly one feature changed.

I therefore read a counterfactual as evidence about the model under a particular constructed comparison. A named dependency becomes more convincing when a separate intervention tests that attribute while controlling alternative explanations. This is my methodological reading of Lee's argument, rather than a claim that every counterfactual fully exposes the model's reasoning.

The same distinction separates a model intervention from a biological intervention. Altering an image changes the classifier's input. It does not change the patient's disease, demonstrate a disease mechanism, or establish the effect of a clinical treatment.

## MONET adds a way to describe data and models in clinical terms

I had already reviewed the lab's MONET paper, *Transparent medical image AI via an image-text foundation model grounded in medical literature*. Published in *Nature Medicine* in 2024, it comes after this conversation. MONET learns associations between dermatology images and text, then scores images for named concepts to support data auditing, model auditing, and interpretation. ([Kim and colleagues](https://doi.org/10.1038/s41591-024-02887-x))

Reading the interview alongside that paper helps me understand the continuity in the lab's work. The AML example connects gene-level explanations to biological categories. The dermatology audit connects generated image differences to physician-described attributes. MONET provides a learned way to describe images using concepts that can support systematic analysis.

These approaches have different assumptions and validation requirements. I would not describe MONET's concept scores as interchangeable with counterfactual evidence. Detecting a concept in an image and demonstrating a classifier's reliance on it are separate tasks.

Lee's discussion of future single-cell models raises a related issue. She wants representations whose units support biological interpretation, because an input variable is not automatically the most useful unit of explanation. My reading is that selecting the explanatory vocabulary is itself part of the research problem. A convenient list of features can constrain what an audit is able to discover.

## The connection to my clinical faithfulness work

My research on gallbladder and hepatobiliary ultrasound concerns whether a classifier's evidence aligns with independently assessed clinical factors and whether selected dependencies can be tested. Lee's argument is unusually close to that objective. The overlap is in the problem formulation; it does not establish that my work already provides the capabilities demonstrated by her lab.

I use clinical faithfulness to connect clinical relevance, explanation faithfulness, and model reliance. Clinical relevance concerns whether a finding informs the specified diagnostic task. Explanation faithfulness concerns whether a readout describes the model behavior it claims to describe. Reliance concerns how predictions respond when particular information changes under a defined comparison.

An explanation can faithfully expose a shortcut. Conversely, a map can look anatomically appropriate without identifying the feature the classifier uses. These possibilities are why I need separate evidence for each part of the audit.

### Anatomical overlap does not identify the diagnostic finding

Consider a hypothetical gallbladder image with a suspicious wall finding and measurement calipers placed over it. An attribution map concentrated in that region could reflect tissue appearance, annotation edges, or a combination. Overlap alone cannot distinguish those possibilities.

My first step would be to define the relevant clinical factors independently of the explanation. Readers would assess the original images without seeing model scores or heatmaps. Depending on the task, annotations could describe wall morphology, lesion attachment, or whether a proposed feature is assessable in the available frame.

That independence concerns how the reference was constructed. It does not mean the clinical factor is statistically independent of diagnosis. I would also preserve uncertainty and distinguish a feature that is absent from one that cannot be assessed.

This extends Lee's argument in a direction specific to my project: before interpreting agreement, I need a defensible clinical reference that was not shaped by the model display being evaluated.

### A feasible intervention can support a narrower claim

For the caliper example, I would prefer marked and unmarked exports of the same frozen image, if available. I would verify that tissue content and preprocessing match and include a sham export to detect changes introduced by encoding or processing.

A prediction difference would support sensitivity to the annotation layer under that comparison. It would not establish every dependency of the classifier. If the calipers are burned into the image and must be inpainted, the claim becomes weaker because the underlying tissue has to be estimated.

Editing morphology is harder. Smoothing a wall region might change thickness, contour, texture, and nearby findings together. I would not treat the resulting score change as isolated reliance on wall irregularity without evidence that the edit preserved the other relevant information.

These are proposed experiments, not results I have obtained. The connection to Lee's work helps specify what I would need to demonstrate and where a conclusion should remain limited.

### The audit needs variation across cases and settings

The AML discussion also makes me wary of drawing conclusions from a few persuasive examples. I would examine clinical-factor associations and intervention responses across patients, with uncertainty estimates that preserve the grouping of multiple frames from the same patient.

I would report variation across trained models separately from variation across sampled patients. Acquisition conditions and sites would require their own comparisons. Averaging everything into one clinical-faithfulness score could obscure a failure that matters for a particular finding or setting.

For my immediate study, the most useful consequence of this conversation is a more specific analysis plan: define independent clinical factors, evaluate the relevant model readouts, and test selected dependencies with controlled comparisons. I would report anatomical agreement, clinical-factor alignment, and intervention effects separately, including cases where they disagree.
