---
layout: post
title: "BI-RADS for Sonography: Positive and Negative Predictive Values of Sonographic Features"
date: 2025-11-17 12:00:00 +0900
venue: "AJR"
authors: "Hong et al. (2005)"
description: "An empirical look at how well individual BI-RADS sonographic descriptors actually predict malignancy, the kind of per-feature grounding that a BI-RADS-based concept bottleneck for breast ultrasound is implicitly relying on."
related_posts: false
---

**Paper.** *BI-RADS for Sonography: Positive and Negative Predictive Values of Sonographic Features*. [Authors' abstract](https://pubmed.ncbi.nlm.nih.gov/15788607/).

Clinical concepts need more than familiar names. If a breast-ultrasound model exposes shape, margin, and orientation, the reader should understand why those observations are relevant and what diagnostic information they actually provide. Hong and colleagues evaluated descriptors from the sonographic BI-RADS lexicon against histology. The question was whether the standardized vocabulary separated benign and malignant solid masses in an examined cohort, rather than whether the vocabulary itself could replace a complete diagnostic assessment.

The study analyzed 403 solid lesions with known histological diagnoses. Each lesion was assessed by one of three dedicated breast radiologists and described using the lexicon. This is different from saying that all three radiologists independently evaluated every lesion. The descriptors were related to biopsy results, and the authors calculated feature-level predictive values. The study did not fit a multivariable model that established independent contributions for every descriptor.

Of the 403 masses, 141 were malignant, giving a malignancy prevalence of 35%. Spiculated margin had a reported positive predictive value of 86% (19/22), irregular shape 62% (102/164), and nonparallel orientation 69% (75/109). For benign-associated appearances, circumscribed margin had a negative predictive value of 90% (160/178), oval shape 84% (200/237), and parallel orientation 78% (228/294). The evaluated descriptor distributions differed between benign and malignant masses.

The denominators make these results more useful than an ordered list of percentages. The estimate for spiculated margin came from far fewer masses than the estimate for oval shape. A high predictive value based on a small feature-positive group should not be treated as more precisely established merely because its percentage is larger. The counts also make clear that neither a suspicious descriptor nor a benign-associated descriptor determined histology without exceptions.

The primary conclusion is that these descriptors carried diagnostic information in the sampled solid masses. The findings support their use as meaningful observations and motivate their inclusion in structured models. They do not establish universal numerical risks attached to the words, nor do they establish that a feature is necessary or sufficient for malignancy. A concept can be clinically useful while remaining an imperfect and context-dependent indicator.

Predictive values condition in the direction relevant to this interpretation. A feature's positive predictive value asks about malignancy among masses assigned that feature. It does not tell us the proportion of all malignancies that show the feature. A rare but highly suspicious appearance can have high positive predictive value while identifying only a minority of malignant masses. That is why these numbers should not be repurposed as feature sensitivities or used to rank which concepts a model must always detect.

The cohort's 35% malignancy prevalence is also part of the result. Predictive values in a biopsy-confirmed collection need not match those in screening or in a different referral setting. Changing prevalence alone can change predictive values, and changing the clinical spectrum can alter the underlying feature distributions as well. Simple numerical recalibration is therefore not guaranteed to transport the results. A new setting should examine how cases were selected and which lesions reach verification.

A careful reader would focus on selection for histology. Biopsy provides a strong reference for the sampled lesion, but the decision to biopsy is itself related to clinical suspicion and imaging appearance. Masses that were not selected for biopsy may have a different distribution of descriptors and outcomes. The study can describe associations in its verified cohort without identifying the same quantities for every mass encountered in practice.

Descriptors also occur together. An irregular shape, noncircumscribed margin, and nonparallel orientation may describe overlapping aspects of a lesion. Their separate predictive values cannot be multiplied as though they were independent evidence, and the study does not estimate causal weights for a concept-based classifier. A downstream model must learn or specify how combinations are interpreted, then be evaluated on combinations that are uncommon or clinically discordant.

This is particularly relevant to concept intervention. Changing a model's margin label while leaving shape and orientation unchanged can create a combination rarely encountered during training. Even if the corrected descriptor is accurate, the downstream model may respond poorly to that combination or to the numerical confidence used for the correction. Hong's associations motivate which findings to inspect, but they do not validate a specific intervention interface. That requires separate experiments such as those considered in BUS-CBM.

Measurement quality remains another boundary. Because each lesion was read by one of the three radiologists, the design as described does not provide a complete three-reader agreement experiment on all masses. Feature–histology association and reproducibility are distinct properties. Before using the descriptors as supervision, I would want to know how often readers disagree, which categories are difficult, and when the available image does not permit a judgment.

The publication also concerns the lexicon and population examined at that time. Its results should not silently be presented as a validation of every later implementation, category grouping, or clinical management rule bearing the BI-RADS name. A model that collapses multiple descriptor categories into one binary concept changes the measurement. The historical feature-level evidence remains relevant, but the new grouping needs its own assessment of meaning and predictive behavior.

[Clinical Concepts and Concept-Based Interpretability]({{ '/study/clinical-concepts-and-concept-based-interpretability/' | relative_url }}) gains an empirical foundation from this paper: named concepts can relate to pathology in ways that are worth testing computationally. The paper also complicates any assumption that the concept name supplies a universal diagnostic coefficient. [Dataset Design, Ground Truth, and Reference Standards]({{ '/study/dataset-design-ground-truth-and-reference-standards/' | relative_url }}) explains why lesion verification and selection must be interpreted together.

[Evaluation Beyond AUROC]({{ '/study/evaluation-beyond-auroc/' | relative_url }}) clarifies the prevalence dependence of predictive values and their relationship to a decision. For my work, the useful lesson is to preserve three questions separately: can a model measure the descriptor, does its diagnosis respond appropriately to it, and does that response improve decisions in the intended population? This paper grounds the first connection between vocabulary and disease, while leaving the model and deployment questions open.
