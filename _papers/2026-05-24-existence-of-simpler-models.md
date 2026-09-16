---
layout: post
title: "On the Existence of Simpler Machine Learning Models"
date: 2026-05-24 12:00:00 +0900
venue: "ACM FAccT 2022"
authors: "Lesia Semenova, Cynthia Rudin, Ronald Parr (2022)"
description: "The Rashomon-set argument: for a given dataset, there are often many equally accurate models, some far simpler and more interpretable than others, so 'we needed the complex model for accuracy' is a claim that should be checked, not assumed."
related_posts: false
---

**Paper.** *On the Existence of Simpler Machine Learning Models*. [FAccT paper](https://facctconference.org/static/pdfs_2022/facct22-3533232.pdf)

## Why the existence question matters

Finding a complex model with good validation performance is often easier than finding the best small rule list, sparse score, or compact tree. Consequently, a failed quick attempt with a simple baseline can become an unjustified conclusion that complexity is necessary.

The paper asks an earlier question: can the structure of a learning problem indicate that an accurate simpler model is likely to exist before the expensive search for it?

For trustworthy medical AI, that changes the burden of comparison. A complex model's small observed advantage should be assessed against a serious search for alternatives, not only against one untuned linear model.

At the same time, simplicity is not itself clinical validity. A short rule based on hospital identity can be easy to understand and inappropriate. The value of a simpler model is that its behavior may be easier to inspect and constrain, provided the features and task are defensible.

## The Rashomon set and ratio

The Rashomon set contains models whose loss is within a specified tolerance of the best loss in a chosen hypothesis class. The Rashomon ratio measures the size of that set relative to the class. The authors give theoretical conditions connecting a sufficiently rich near-optimal set with accurate models from simpler classes.

Their empirical study uses 38 UCI classification datasets and compares logistic regression, CART, random forests, gradient-boosted trees, and RBF-kernel SVMs. Bounded-depth decision trees serve as a surrogate space for estimating Rashomon-set size. [Theory and experimental design](https://facctconference.org/static/pdfs_2022/facct22-3533232.pdf)

Three choices therefore belong to any interpretation: the dataset, the hypothesis class, and the loss tolerance. “This problem has many good models” is incomplete unless “good” and the space being searched are specified.

The ratio also depends on how size is defined. In a finite class, counting models has an immediate interpretation. In a continuous space, a reference measure is required. It should not be treated as a universal property of a dataset independent of model representation.

## What the empirical pattern suggests

The authors propose similar performance across different learning methods as a practical signal that searching for a simpler model may be worthwhile. The experiments connect this pattern with larger estimated Rashomon sets and the availability of simpler alternatives. [Empirical results](https://arxiv.org/abs/1908.01755)

The sensible use of that signal is to guide additional work. It does not prove that any particular clinical task has an accurate transparent solution.

Several algorithms can tie because the available labels are noisy, the representation is uninformative, the sample is small, or the tuning procedure is weak. They can also tie because the task admits many distinct good solutions. Similar scores alone do not distinguish these explanations.

That ambiguity does not make the heuristic useless. If several well-developed model families generalize similarly, spending the next iteration on interpretability and stability can be more informative than adding architectural complexity.

The relevant comparison must include generalization. Multiple models fitting the training data equally well is a much weaker observation than multiple models performing similarly on appropriately separated evaluation data.

## What the theory licenses

The theoretical contribution is conditional. Under the paper's assumptions about the relationship between model classes, a large near-optimal set can support the existence of a simpler accurate model and associated generalization statements.

It does not establish that large neural-network parameter spaces necessarily contain a clinically interpretable model that an available optimizer will find. Existence, search, and verification are separate problems.

It also does not establish that every member of a near-optimal set is interchangeable. Equal average loss can conceal different predictions for the same patient.

That multiplicity is especially consequential in medical AI. One model may fail mainly on subtle malignant lesions, another on difficult benign mimics. Their overall scores can tie while their clinical consequences differ.

A Rashomon set can therefore be viewed as a space for selecting additional properties, such as calibration, subgroup sensitivity, or restricted evidence use. But each additional property must be measured. It does not follow from membership in the set.

## The weakness I would press

The empirical bridge from an estimated set in a tractable surrogate class to the behavior of a much larger practical model space is the main issue for translation.

The paper's bounded-depth tree calculations are informative for its experimental setting. They do not directly estimate the volume of near-optimal deep image classifiers. The surrogate must be capable of representing the kinds of functions that matter for the target task.

For medical imaging, feature availability is another major complication. A small classifier operating on expert measurements can look competitive with an image network while relying on information that requires substantial manual work at deployment.

The complete systems must be compared. If one model receives manually annotated morphology and another receives raw pixels, the comparison mixes model complexity with information access and annotation effort.

Finally, the tolerance around optimal performance needs a defensible interpretation. Failure to find a statistically significant difference does not establish clinical equivalence. A tolerance should reflect acceptable performance loss and uncertainty, rather than being selected afterward to include a preferred model.

## Connections to the study notes

[Auditable-by-Design Medical AI](/study/auditable-by-design-medical-ai/) asks whether a reviewer can inspect and challenge the evidence pathway. The Rashomon argument supports searching for a model that makes those operations easier when several solutions perform adequately.

[Model Reliance on Clinical Evidence](/study/model-reliance-on-clinical-evidence/) emphasizes that comparable performance does not imply comparable reliance. This paper makes that point a model-selection opportunity: evaluate evidence use across the acceptable candidates rather than explain only the first winner.

[Evaluation Beyond AUROC](/study/evaluation-beyond-auroc/) complicates the meaning of “equally accurate.” Models can tie on ranking while differing at the threshold and workload that matter clinically. The acceptable set should be defined using outcomes appropriate to the intended decision.

[Reproducibility, Benchmarks, and Translational Study Design](/study/reproducibility-benchmarks-and-translational-study-design/) also matters because extensive searching creates selection optimism. Choosing a simpler model from many candidates still requires an independent final evaluation.

## How I would use the argument

I would define a performance tolerance before comparing candidate families and distinguish model simplicity from feature-acquisition burden.

For a clinical concept model, I would evaluate a sparse score, a small tree, and a more flexible predictor on the same available concept inputs. I would separately evaluate errors introduced by the image-to-concept stage.

Among candidates meeting the performance requirements, I would compare calibration, subgroup errors, sensitivity to acquisition cues, and the stability of predictions across resampling.

The result could justify a transparent model, or reveal that the simpler class misses an important interaction. Either outcome is useful. The paper's contribution is a principled reason to conduct that search seriously, with the final choice based on the complete clinical and computational system.
