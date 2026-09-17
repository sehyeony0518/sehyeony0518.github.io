---
layout: post
title: "Auditing the Inference Processes of Medical-Image Classifiers by Leveraging Generative AI and the Expertise of Physicians"
date: 2026-07-28 12:00:00 +0900
venue: "Nature Biomedical Engineering"
authors: "Alex J. DeGrave, Zhuo Ran Cai, Joseph D. Janizek, Roxana Daneshjou, Su-In Lee (2025)"
description: "Generative counterfactuals read by two blinded dermatologists across five academic and consumer skin-lesion classifiers, the closest published template I have found for the audit I want to run on ultrasound models."
og_image: "https://sehyeony0518.github.io/assets/img/og/2026-07-28-auditing-inference-processes-generative-counterfactuals.png"
related_posts: false
---

**Paper.** *Auditing the inference processes of medical-image classifiers by leveraging generative AI and the expertise of physicians*. [Nature Biomedical Engineering (2025)](https://doi.org/10.1038/s41551-023-01160-9)

This paper asks what image evidence medical classifiers use, expressed in terms that specialists can assess. A conventional performance comparison cannot answer that question. Two classifiers may reach similar accuracy through different dependencies, and a highlighted image region may contain several clinically distinct attributes. I read the paper because it connects model behavior to named observations without assuming that a heatmap already provides a clinical explanation.

The framework combines generative counterfactual images with expert interpretation. For a reference image and a fixed classifier, a generator produces related images that move the classifier toward benign and malignant predictions. The comparison creates a visible question for a reader: which attributes differ between the outputs associated with those predictions? The task for the dermatologist is therefore more specific than deciding whether a colorful explanation looks reasonable.

The authors examine five classifiers: DeepDerm, ModelDerm 2018, Scanoma, SSCD, and a SIIM-ISIC competition-style model. Two board-certified dermatologists assess counterfactual pairs after screening and randomization. The generation procedure builds on Explanation by Progressive Exaggeration and is designed to tie generated changes more closely to classifier behavior. That design reduces a concern about arbitrary generative drift, but it should not be interpreted as a guarantee that every visible change independently causes the prediction change.

The resulting attribute profiles contain both clinically recognizable and undesirable dependencies. Lesional pigmentation is prominent, while background texture, hair, and color balance also appear. This mixed picture is useful. An audit should be able to discover appropriate reliance as well as suspicious reliance. Otherwise, the procedure risks becoming a search for failure examples whose existence says little about how the model behaves across its intended population.

The strongest validation is the follow-up color experiment. The authors programmatically changed chromaticity in CIELUV space across 20,260 ISIC images and compared predictions from the same classifiers. The direction of response agreed with the counterfactual observations, including classifier-specific differences: pinker images moved DeepDerm toward benign predictions and Scanoma toward malignant predictions. This gives a controlled test of a dependency suggested by the expert readings.

The two stages establish different things. Expert annotation associates named attributes with the changes generated to alter a classifier output. The programmatic transformation directly measures the fixed classifier's response to a specified color operation. Agreement between them strengthens the interpretation because the second procedure does not depend on the generator producing the same edit. It is still a claim about the implemented transformation, not a universal causal statement about redness or skin disease.

A careful reader should also notice that changing an image's chromaticity can affect both lesion and background appearance. The result supports sensitivity to color balance under that operation. Attributing the entire effect specifically to background skin requires a more selective intervention or further evidence. This is the kind of distinction I want an audit to preserve: the clinical phrase describing a suspected factor and the actual image operation testing it need not have exactly the same scope.

The main weakness of the generative stage is that multiple attributes can change together. A darker lesion, altered surrounding skin, and modified texture might all accompany the same prediction shift. The reader can name those differences, but cannot infer their separate effect sizes merely by observing the pair. A generator may also prefer some changes over others because of its training and architecture. Failure to generate a size change, for example, is not evidence that the classifier ignores size.

Screening introduces another scope condition. Results concern pairs that could be generated and judged sufficiently usable for annotation. Difficult images or rare presentations may be underrepresented among those pairs. For reuse, I would want the audit to retain counts and reasons for generation failure, quality rejection, and unassessable attributes. The ability to produce a valid counterfactual is itself a property that can vary across patient groups and image conditions.

Annotation frequency should consequently be interpreted as frequency under the audit procedure. It is not the percentage of a prediction explained by an attribute, and it is not an effect size directly comparable across classifiers. Reader vocabulary and agreement also shape what becomes visible in the results. Features that lack a familiar name, or interactions between several features, can remain poorly described even when the image pairs clearly alter model behavior.

For gallbladder ultrasound, transferring the procedure would require particular care about image formation. A change to echogenicity can alter apparent tissue relationships, while a change to shadowing can remove evidence relevant to the finding itself. A realistic-looking edit could therefore be clinically invalid. I would begin with a narrow dependency hypothesis, ask readers to assess target change and preservation of other findings independently of prediction movement, and test the selected attribute using a separate intervention where possible.

I would also keep the diagnostic model fixed throughout the audit and retain every generated pair, transformation parameter, and output score. Repeated edits of one patient would characterize intervention variability without becoming additional independent patients. An independent set of cases would be useful for confirming hypotheses discovered during expert review. These design choices make it easier to distinguish a reproducible model dependency from an artifact of selection or interpretation.

This paper supports [Intervention-Based Auditing](/study/intervention-based-auditing/) by demonstrating the value of moving from an observed counterfactual pattern to a specified follow-up intervention. It also sharpens [Explanation Faithfulness Versus Plausibility](/study/explanation-faithfulness-versus-plausibility/): physicians can establish that a change is clinically interpretable, while a behavioral experiment is needed to establish the model response attributed to it.

The connection to [Auditing and Evaluating Generative Medical AI](/study/auditing-and-evaluating-generative-medical-ai/) concerns the generator as part of the measurement process. Visual realism does not establish preservation of clinical evidence, and a convincing edit does not reveal every dependency. For my work, the reusable contribution is the sequence of generation, blinded interpretation, and independent testing, with each stage allowed to fail and each conclusion limited to what that stage actually measures.
