---
layout: post
title: "Concept Gradients: Concept-Based Interpretation Without Linear Assumption"
date: 2026-08-10 12:00:00 +0900
venue: "ICLR 2023"
authors: "Andrew Bai, Chih-Kuan Yeh, Neil Y. C. Lin, Pradeep Ravikumar, Cho-Jui Hsieh (2023)"
description: "TCAV assumes a concept occupies a linear direction in activation space. Concept Gradients drops that assumption and, in a medical case study, tracks concept importance scores against mortality-risk descriptions already published in the clinical literature."
related_posts: false
---

**Paper.** *Concept Gradients: Concept-Based Interpretation Without Linear Assumption*. [ICLR paper](https://openreview.net/forum?id=_01dDd3f78). [Author implementation](https://github.com/jybai/concept-gradients).

Concept Gradients asks what happens when a clinically meaningful concept cannot be represented adequately by one linear direction. Concept Activation Vectors make interpretation tractable by fitting a linear separator to concept examples. That separator can be useful, but the clinical meaning of its direction depends on the geometry of the chosen representation. I read this paper because a weak linear approximation can become an unexamined assumption underneath an apparently precise concept-importance score.

The proposal replaces a fixed linear concept direction with a differentiable concept function. A target predictor supplies the output to explain, and a concept model estimates the concept from the same input or an appropriate representation. Their gradients are combined using a pseudoinverse. The concept direction can consequently change with the example. The diagnostic predictor remains the object being explained; training a concept model does not itself make the diagnostic model concept-based.

For one scalar concept $$g$$ and scalar target output $$f$$, the local expression has the form

$$
\operatorname{CG}(x)
=
\frac{\nabla g(x)^\top \nabla f(x)}
{\|\nabla g(x)\|^2},
$$

when the denominator is nonzero. This expression relates movement in the target output to movement along the locally defined concept direction. It recovers an ordinary derivative under suitable compositional assumptions, such as the target depending on the input entirely through that concept. For a general predictor, its interpretation needs the specified local construction.

The medical case study uses a myocardial-infarction complications dataset with 1,700 patient records, 112 input fields, and 11 complication targets. The target model predicts lethal outcome, while concept models predict complications. The authors compare aggregated importance scores with mortality-risk descriptions from medical literature. The comparison is largely clinically consistent, with some differences between CG and the linear alternative. It provides a domain-specific plausibility check rather than a measured causal effect of a complication.

That distinction is essential. Literature can describe how a complication relates to mortality in a clinical population. A model explanation describes the behavior of a fitted function under an explanatory construction. These quantities can disagree for several reasons, including confounding, redundancy between inputs, a poor predictor, or an inaccurate explanation. Agreement is encouraging, but it does not identify which of those possibilities has been excluded.

A faithful explanation of an inappropriate model could even disagree with clinical knowledge. If a model relies on an acquisition or documentation cue, an explanation method should reveal that dependence rather than produce the ranking a clinician expects. Consequently, literature agreement should complement tests of the explanation's mathematical and behavioral claims. It should not become the sole definition of explanation quality.

The paper's broader experiments and derivations help address the geometric motivation. They examine situations in which nonlinear concept models represent concepts better than linear alternatives. For use in medical AI, I would still keep concept prediction quality separate from importance estimation. A more flexible concept model can improve measurement while also learning new unwanted correlations. Its greater expressive capacity does not remove the need to validate what its output represents.

Locality is another important boundary. A derivative concerns small changes around the evaluated point. It does not automatically predict the effect of changing a complication from absent to present or replacing one imaging finding with another. A finite edit can move into a region where the concept gradient changes substantially. If the intended application is concept correction, the correction magnitude and the distribution of edited examples need their own evaluation.

Concept units also matter. In the scalar expression, multiplying the concept function by a positive constant divides the corresponding CG value by that constant. This is a mathematical consequence of the definition, not an empirical weakness discovered in the medical experiment. It means that importance magnitudes cannot be compared casually across concept models with different output scales. A probability, logit, and standardized continuous measurement define different numerical changes.

Multiple concepts add an identifiability issue. If two concept functions vary together, their local Jacobian can be poorly conditioned, and a pseudoinverse must resolve overlapping directions. The result is a specified geometric allocation of sensitivity, not necessarily a unique clinical decomposition. I would examine sensitivity to concept selection, model fitting, layer choice, and numerical conditioning before interpreting small differences in rankings.

The medical setting also requires attention to time. A complication label can be useful for retrospective interpretation even if the complication was not available at the prediction time. That does not make it a valid prospective input or prove that the model observed its defining evidence. For any reproduction, I would document when each input and concept reference was measured. The distinction between predicting a future complication and recognizing a currently visible finding should remain explicit.

For a gallbladder application, I would first validate a small set of concept predictors against independent annotations. The audit would record whether each finding was assessable, not merely whether a label was supplied. I would then compare local scores with finite, clinically reviewed changes and include nuisance concepts as controls. A method that only recovers expected clinical rankings would leave me uncertain about its ability to expose an inappropriate dependency.

This paper extends [Clinical Concepts and Concept-Based Interpretability](/study/clinical-concepts-and-concept-based-interpretability/) by relaxing the assumption that one linear direction adequately represents a concept. It also reinforces [Geometry of Representation Spaces](/study/geometry-of-representation-spaces/): local directions, scaling, and coordinate choices shape what a sensitivity means. Nonlinearity increases flexibility while preserving the need to specify the geometry.

The connection to [Explanation Faithfulness Versus Plausibility](/study/explanation-faithfulness-versus-plausibility/) is the most valuable correction to my reading. The mortality comparison tests compatibility with outside clinical knowledge. It does not independently establish that the scores isolate the model's use of each clinical factor. For my work, CG is a candidate measurement of local concept sensitivity whose concept model, numerical definition, and clinical interpretation all need to be evaluated explicitly.
