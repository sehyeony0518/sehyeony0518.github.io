---
layout: post
title: "Can You Trust This Prediction? Auditing Pointwise Reliability After Learning"
date: 2026-09-05 12:00:00 +0900
venue: "AISTATS 2019"
authors: "Peter Schulam, Suchi Saria (2019)"
description: "Resampling Uncertainty Estimation asks a narrower, more auditable question than most uncertainty methods: not how confident is the model in general, but how much would this specific prediction have changed if the model had been fit on slightly different training data."
related_posts: false
---

**Paper.** *Can You Trust This Prediction? Auditing Pointwise Reliability After Learning*. [AISTATS 2019](https://proceedings.mlr.press/v89/schulam19a.html)

This paper asks how to assess the reliability of an individual prediction after the predictor has already been trained. Average test error does not identify which future cases are likely to be difficult, while many uncertainty methods require changes during development. Resampling Uncertainty Estimation, or RUE, addresses a specific alternative: approximate how much a prediction would vary if the training observations had received different bootstrap weights.

The attraction for my work is its timing. A model can be audited without repeatedly running the full training procedure from scratch. However, post hoc does not mean black-box or training-data-free. RUE requires access to derivatives of the training loss and the fitted model. That access requirement is central to deciding whether the method can be applied to an existing medical system, particularly one supplied only through an inference interface.

The method uses per-example loss gradients and the Hessian of the training objective. Bootstrap resampling is represented through counts assigned to training observations, and a local approximation converts those count changes into parameter changes. Predictions from the resulting parameter ensemble yield a pointwise uncertainty score. Greater prediction dispersion means greater estimated resampling sensitivity. The score should not be read as a calibrated probability that the individual prediction is wrong.

Schematically, if $$G$$ contains training-example gradients and $$\widetilde H$$ is a damped Hessian, the approximation takes the form

$$
\theta^*
\approx
\hat\theta-\widetilde H^{-1}G(w-\mathbf 1).
$$

Here $$w$$ records bootstrap counts and $$\mathbf 1$$ represents the original weighting. This clarifies what varies: the local influence of observations in the existing training sample. The procedure does not independently explore every architecture, training objective, initialization, or optimization trajectory that could have produced another model.

The main error-detection experiments use eight regression benchmarks, with a fixed network containing one hidden layer of 50 units. The comparison applies different uncertainty estimators to predictions from the same fitted model for each split. RUE is compared with a Laplace approximation, input-density estimation, and a bootstrap-based gradient-step baseline. This controlled setup helps attribute differences to the reliability estimators rather than to different predictive architectures.

The evaluation defines an error through a tolerance on the regression residual and measures how well uncertainty ranks errors above acceptable predictions. Its AUROC is therefore an error-detection AUROC, not a disease-classification AUROC. The paper reports generally favorable results for RUE but also a difficult power-plant benchmark, where the compared error-detection AUCs remain below 0.56. That limitation matters: an uncertainty score with a principled construction can still be a weak detector of actual error.

The contribution is strongest as a precise question about one source of variability. If a prediction changes substantially when the effective training sample changes, that instability can justify closer inspection. But the reverse implication does not hold. A stable prediction can be wrong because the model class is inadequate, labels are systematically biased, or the training sample consistently supports an inappropriate association. Resampling the same evidence does not repair what that evidence omits.

A shortcut provides a concrete example. Suppose a scanner signature is strongly associated with disease throughout the training sample. Most bootstrap resamples will preserve that association. A model can therefore produce a stable prediction through the same clinically invalid dependency across many resampled weightings. Low RUE uncertainty would describe stability relative to the observed training distribution. It would not establish appropriate evidence use or transfer to a scanner where the association changes.

The local approximation is another boundary. It estimates changes around the fitted parameter vector using derivatives and damping. Actual retraining can move into a different region of the loss landscape or follow another optimization trajectory. Consequently, the approximation should be checked against some explicit retraining when feasible, especially after moving to a substantially different model class. “Avoids repeated full fitting” is a computational advantage, but it is not evidence that approximation error is negligible everywhere.

Scaling is a practical limitation for imaging models. Forming and solving with a full Hessian can be expensive, and retaining per-example gradients can also be demanding. The paper discusses alternatives involving Hessian-vector products and approximate calculations, while leaving their large-scale evaluation open. Applying such an approximation to a modern image encoder would create a new method configuration whose numerical behavior and reliability ranking need validation.

The resampling unit matters as well. For an ultrasound dataset with several frames from one examination, resampling frames independently treats correlated observations as separate pieces of evidence. A patient-level or examination-level procedure may better match the uncertainty question. This is a proposed adaptation for my setting, not an experiment reported in the paper. The relevant unit should follow the data-generating process and the level at which the prediction will be used.

A clinical use also needs a decision rule. If RUE triggers review or abstention, evaluation should report retained-case error together with coverage, subgroup coverage, and the outcomes of the review pathway. Rejecting difficult predictions can make the accepted subset look better while shifting workload or risk elsewhere. The threshold for intervention should be selected independently of the final evaluation, and any claim about improved care requires evidence about what happens after the uncertainty score is shown.

This paper supports [Calibration, Uncertainty, and Selective Prediction](/study/calibration-uncertainty-and-selective-prediction/) by giving uncertainty an explicit object: approximate variability under resampling. It also reinforces the note's distinction between a useful ranking of risk and calibrated probabilities. Neither the name “reliability” nor the existence of an ensemble settles that distinction.

[Curvature Without the Hessian: Power Iteration, Trace Estimation, and Quantization](/study/curvature-without-the-hessian/) provides the computational connection, while [Post-Hoc Model Auditing](/study/post-hoc-model-auditing/) supplies the broader scope. RUE can contribute one measurement to an audit of an existing predictor. For my gallbladder work, I would pair it with evidence-reliance tests and external evaluation, so that sensitivity to the training sample, clinical appropriateness of the dependency, and performance in the intended setting remain separately inspectable.
