---
layout: page
title: "Optimization for Machine Learning"
description: "Gradients, regularization, and constrained optimization, viewed as the assumptions a training procedure quietly imposes on the solution."
section: "F"
section_title: "Mathematical and Statistical Foundations"
branch: "Branch 01"
order: 4
written: true
---

Training minimizes an objective through a sequence of updates, and both the objective and the update rule influence the solution. I study optimization to understand which preferences enter a medical AI model before anyone evaluates its clinical evidence.

## Why it matters here

Diagnostic labels usually specify the desired output without specifying every acceptable way to obtain it. A training objective can therefore reward predictions supported by clinical findings and predictions supported by acquisition cues. Successful optimization establishes that the procedure reduced its chosen loss, leaving the validity of the evidence as a separate question.

For my work, this connects model development with post-hoc auditing. If I want clinically grounded gallbladder representations, I need to describe how the training procedure encourages them. If I audit an existing classifier, its loss, sampling scheme, and model selection rule help explain which behaviors were rewarded, even when I cannot retrain it.

## The core ideas

### The objective defines what the procedure rewards

Empirical risk averages a loss over training observations. That average assigns influence through the sampling unit and any weights: a patient contributing many frames may matter more than a patient contributing one. Class weighting changes the relative cost of errors and can change the probability interpretation of the learned score. I would therefore read the loss together with the data sampler. The named loss function alone does not fully specify the problem being optimized.

### Gradients describe local change

A gradient collects derivatives of the loss with respect to parameters. In ordinary gradient descent, a step in the negative gradient direction seeks a local decrease, with the learning rate controlling its size. A minibatch gradient estimates that direction from a subset of observations. Large or poorly scaled steps can behave differently from the local approximation. I also need to distinguish parameter gradients used for learning from input gradients used in explanations; neither is automatically a causal description of clinical evidence.

### Regularization imposes a preference among solutions

An explicit penalty trades fit against a chosen property, such as small parameter norms. Data augmentation introduces another preference by training the model to maintain a target across transformed inputs. For ultrasound, that preference needs clinical justification because an intensity or texture transformation may alter useful evidence. Implementation matters too: [Loshchilov and Hutter](https://arxiv.org/abs/1711.05101) show that an L2 penalty and decoupled weight decay are not equivalent for adaptive optimizers such as Adam. “Regularized” is therefore an incomplete description.

### Constraints make a requirement explicit but conditional

Constrained optimization minimizes an objective while requiring specified quantities to remain within permitted values. A penalty formulation instead charges for violating a requirement, with its weight determining a tradeoff. The formulations are not automatically interchangeable, particularly in nonconvex problems solved approximately. If I constrain average attribution outside an anatomical region, I have constrained that measured readout. I have not established that the model uses a clinically valid feature inside the region, or that every patient's prediction satisfies the intended requirement.

### The optimization path also selects the model

Neural network objectives are generally nonconvex, and different initializations, batch orders, learning-rate schedules, or stopping points can produce different solutions. Similar predictive performance does not imply similar representations or evidence use. Early stopping and validation-based checkpoint selection add further preferences, even without an explicit penalty. I would document the selection criterion and inspect variation across training runs when making a claim about a method, rather than presenting one favorable checkpoint as the procedure's typical behavior.

## Where it touches my work

For gallbladder ultrasound AI, I would compare clinically motivated training changes against the same clinical faithfulness and shortcut audits used for a baseline. If augmentation is intended to reduce acquisition reliance, I would test whether it preserves clinically relevant distinctions and whether the output becomes less sensitive to the targeted nuisance. An improved training loss or a satisfied attribution penalty would be intermediate evidence. The intended result is a reproducible change in how the classifier supports its diagnosis on held-out patients.

## What I have not resolved

- Which ultrasound transformations preserve the clinical target closely enough to justify training for invariance?
- How should I select a model when predictive performance, calibration, and evidence-alignment measurements disagree?
- Can a constraint on an interpretable readout improve actual clinical reliance without teaching the model to satisfy the readout while retaining a shortcut?
