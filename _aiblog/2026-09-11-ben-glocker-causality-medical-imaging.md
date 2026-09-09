---
layout: post
title: "Ben Glocker on Causal Direction, Scanner Effects, and What Breaks at Deployment"
date: 2026-09-11 12:00:00 +0900
description: "Notes on whether the image causes the label or the label causes the image, how that framing bears on data scarcity and dataset shift, and an experiment in which site information survives a full neuroimaging pipeline."
tag: "Imperial College London"
related_posts: false
---

Two failures we usually treat as one problem — not enough labels, and a model that stops working at another hospital — look different once you ask which direction the data was generated in: does the image cause the label, or does the label cause the image? Ben Glocker's lecture argues that the answer differs between skin lesion classification and tumour segmentation, and that the difference bears on which remedies can be expected to help.

The talk accompanies [Castro, Walker and Glocker's *Causality matters in medical imaging*](https://doi.org/10.1038/s41467-020-17478-w) (*Nature Communications*, 2020). It is unusually candid about its own footing: Glocker introduces it as work outside his group's usual territory, begun after reading Pearl and Mackenzie's *The Book of Why* with students, and repeats that they are not experts on causality.

## The assumed direction between image and label is not always the same

### Prediction always runs the same way; the assumed generating direction does not

Whatever the application, the quantity being fitted is the same conditional — given an image $$X$$, how likely is the label $$Y$$:

$$
P(Y \mid X).
$$

What changes between applications is the assumed data-generating direction. If the image generates the label, that conditional *is* the causal mechanism, and the task is predicting an effect from its cause. If the label's underlying state generates the image, the same conditional runs against the assumed arrow, and the task is predicting a cause from its effect. Glocker calls the second case **anti-causal**.

### Three models Glocker proposes, one of them undecidable

**Skin lesion classification is anti-causal.** The label comes from a biopsy — a separate, non-imaging test. The disease state is what makes the dermoscopic image look the way it does, so the arrow runs from disease to image, even though the recorded label is produced afterwards.

**Tumour segmentation is causal.** An expert sits down in front of the scan and draws the contour. The annotation is an effect of the image.

**Chest X-ray labels extracted from radiology reports are undetermined** from the information usually available. The diagnosis in the report might be driven mostly by the image, or the image might be a visual confirmation of a blood test that actually produced the diagnosis. Glocker's point is not that one answer is right but that without the metadata you cannot tell — which is his argument for collecting it, and for asking clinical collaborators how labels were derived.

## The direction bears on which fix for data scarcity should help

### Why the causal case complicates the usual argument for semi-supervision

The independence of cause and mechanism says the distribution of the cause carries no information about the mechanism turning it into the effect. Unlabelled data tells you about $$P(X)$$. In the causal case $$P(X)$$ is the distribution of the cause and $$P(Y \mid X)$$ is the mechanism, so under that principle the unlabelled images would be uninformative about exactly what you are trying to learn. [Schölkopf and colleagues](https://arxiv.org/abs/1206.6471) drew this out in 2012: semi-supervised learning should be futile in the causal direction.

Segmentation is the causal case, and a large literature does semi-supervised segmentation anyway — Glocker's group included. He is careful about how far to take this. His words are that they "not concluded but thought" the implication follows, that it holds "if this is true," and that he is "not saying this is true." He treats it as a question worth putting, not a demonstrated impossibility.

His scepticism runs on the other side too: the cluster and low-density-separation assumptions are always illustrated with two-dimensional half-moons, and in a high-dimensional space holding a thousand examples, every region is low density. The value he claims for causal reasoning here is that it makes an assumption explicit enough to argue with.

### Augmentation is not blocked by the same principle

Augmentation constructs additional image–label pairs using perturbations assumed to be realistic, rather than borrowing information from the marginal, so the independence principle does not stand in its way. Glocker offers this as a possible explanation for why augmentation helps in both settings. It also suggests a direction: use unlabelled data to learn which perturbations are realistic, rather than to place decision boundaries.

Asked whether augmentation is doing anything principled, his answer is deflationary — regularization by wiggling real examples, working mostly because deep networks are data-hungry. On [mixup](https://arxiv.org/abs/1710.09412)-style interpolation toward the boundary he is explicitly non-committal, calling the argument hand-wavy.

## Naming the shift narrows the search for a fix

Drawing the domain's influence through an unobserved true anatomy $$Z$$ separates shifts that look alike from the outside. These come from different diagrams rather than one universal one:

- **Population shift** — the domain changes $$P(Z)$$: a different patient population.
- **Acquisition shift** — the domain changes $$P(X \mid Z)$$: same patients, different scanner or protocol.
- **Prevalence shift** — a curated retrospective set carries disease rates the deployment site does not.
- **Manifestation shift** — the disease expresses differently in the anatomy across domains. Glocker calls this very difficult to do anything about from the machine learning side.
- **Annotation shift** — sites grade or annotate under different protocols. Often the fix is re-annotation, not an algorithm.

In the causal annotation setting, where the image generates the label, a population shift alone need not disturb $$P(Y \mid X)$$, since the mechanism is independent of the distribution of its cause. Limited training coverage can still cause failure: a model fitted only on young subjects will fail on old ones whether or not the mechanism held. The taxonomy is useful because once you know which distribution moved, you can look up whether a method exists for that one.

## Site information survives a state-of-the-art pipeline

This is the part of the talk with numbers, from [*Machine Learning with Multi-Site Imaging Data*](https://arxiv.org/abs/1910.04597) (Glocker, Robinson, Castro and colleagues, 2019). It builds a deliberately favourable case: 592 T1-weighted brain MRIs, 296 from each of [Cam-CAN](https://doi.org/10.1186/s12883-014-0204-1) and [UK Biobank](https://doi.org/10.1038/nn.4393), age- and sex-matched, both 3T Siemens, similar protocols, then run through standard neuroimaging preprocessing — skull stripping, bias field correction, linear registration to MNI, intensity normalization — and tissue segmentation. Glocker is explicit that matching healthy subjects on age and sex removes those confounders and not others.

**A classifier still recovers which study a scan came from.** On SPM12 grey matter probability maps — probability maps rather than raw MRI intensities — site is recoverable at **80.2%** after rigid alignment and **96.6%** after SPM12's non-linear normalization to MNI space. Accuracy *rises* with the degrees of freedom of the registration, the opposite of what harmonization is meant to do. Glocker suspects interpolation is responsible: resampling may amplify a difference such as SNR into a site signature. He offers that as a belief, not a demonstration.

**The differences were not obvious in the displayed examples.** He allows that a trained radiologist might see them, and notes UK Biobank may have slightly higher contrast.

**The downstream effect depends on which features survive preprocessing.** For sex classification on rigidly aligned scans, pooled multi-site accuracy is 82.6% and within-site 81.4% and 84.5%, with cross-site transfer at 81.4% and 78.0%. Overall brain volume — the single most discriminative feature for this task — is preserved under rigid alignment. Remove it by aligning affinely and within-site accuracy holds at 77.7% and 81.1%, while cross-site falls to 73.7% and **62.2%**.

So transfer was conditional on which features were available: it held while brain volume was there, and the remaining features transferred considerably worse once it was not. The paper's conclusion is that current harmonization does not remove scanner-specific bias, and that it produces overly optimistic performance estimates.

There is a second trap worth naming: if the class split correlates with site — patients from one hospital, controls from the other — accuracy goes up, because the classifier can read site instead of the label.

## Two ways to survive the shift

**Adaptation, when you have unlabelled target data.** [Kamnitsas and colleagues](https://doi.org/10.1007/978-3-319-59050-9_47) attach a domain discriminator to intermediate layers of a segmentation network and train adversarially, so the objective discourages site-discriminative features in the representation feeding the task. The clinical case is concrete: a traumatic brain injury lesion segmenter trained when the protocol included gradient echo, then deployed after the site replaced it with susceptibility weighted imaging — clinically equivalent, a substantial shift for the model. Dropping the changed sequence improves things considerably but misses the microbleeds that motivated it; adaptation recovers them without target labels, reaching Dice close to what training on the target domain would give. The cost is retraining per site, and adversarial training that needs watching: Glocker describes discriminator accuracy sitting high, then ideally falling toward chance while segmentation accuracy climbs, and advises not giving up too early.

**Generalization, when you do not — but with labelled data from at least two source domains.** [Dou, Castro, Kamnitsas and Glocker](https://arxiv.org/abs/1910.13580) (NeurIPS 2019) simulate the shift during training, splitting each episode into meta-train and meta-test domains and adding two losses. **Global class alignment** takes each domain's class-mean feature vector, passes it through the task network, and aligns the resulting soft class distributions across domains — so the same confusions are made either side, preserving inter-class relationships. **Local sample clustering** pulls same-class features from different domains together and pushes different classes apart. Evaluated on [PACS](https://doi.org/10.1109/iccv.2017.591) and [VLCS](https://doi.org/10.1109/iccv.2013.208).

On brain data it gave only a small improvement over the pooled baseline. Training on three sites while ignoring that they are different sites, then evaluating on an unseen fourth, is already strong: the shift between imaging sites is far more subtle than photo-to-sketch.

## What I take from this

Three things bear on auditing whether a model's accuracy rests on clinically valid evidence.

**The direction question belongs in the setup, not the discussion.** For the classifiers I care about — a disease label the image is evidence *for* — the assumed relationship is anti-causal, and the evidence a faithful model should use is what the disease did to the image. That is a sharper statement of what an audit looks for than "clinically plausible features."

**Scanner signature survives everything I would have trusted to remove it.** If site is recoverable at 96.6% from grey matter maps after non-linear normalization, an audit that treats a preprocessed, harmonized dataset as clean is checking the wrong thing. The sex-classification result sharpens it: a model's apparent transfer can rest on one feature, and how much of it survives depends on which features preprocessing leaves standing. Whether removing candidate evidence one at a time is a sound audit is my own inference, not something this experiment establishes — the conditions here differ in preprocessing, not in a controlled ablation on one fixed model.

**Causal diagrams are a reporting instrument.** Glocker's closing recommendation is that studies state their assumptions as a diagram: how data was collected, how labels were derived, what mismatch is expected after deployment — and specifically whether inclusion in the dataset was random, image-dependent (a quality-control step), label-dependent, or both, since each gives a different bias. His group offers a reusable scaffold for drawing one. A diagram showing that a lesion dataset was assembled only from cases suspicious enough to biopsy communicates that selection bias in one picture, at the cost of drawing it. I see this as a useful complement to reporting checklists such as [CLAIM](https://doi.org/10.1148/ryai.2020200029); Glocker argues for supplementing reporting guidelines generally, without naming one.
