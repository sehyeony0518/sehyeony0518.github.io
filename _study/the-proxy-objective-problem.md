---
layout: study_note
title: "The Proxy Objective: Training on One Thing, Being Judged on Another"
description: "Cross-entropy is not what anyone wants. The metric that matters is usually non-differentiable, unaffordable, or lives in a person's head, so we optimise a stand-in and hope. The gap is structural, not sloppiness."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalisation & Reliability"
subgroup: "Task Definition & Ground Truth"
order: 2
source: "Independent study"
written: true
updated: "2026-09-15"
papers:
  - "2026-02-03-right-for-the-right-reasons"
  - "2026-05-11-cdep-penalizing-explanations"
  - "2026-02-09-underspecification-credibility-ml"
---

In the ideal case the quantity you optimise and the quantity you are judged by are the same function, and everyone is happy. Linear regression evaluated by mean squared error is that case. Almost nothing else is.

## Core question and definition

Four reasons the evaluation metric usually cannot be the training loss:

1. **It is not differentiable.** Precision, recall, AP, IoU above a threshold, word error rate: all involve counting, thresholding, or ranking. Gradient descent has nothing to work with.
2. **It is unaffordable.** Some metrics require running a procedure per example. An occlusion-based faithfulness measure deletes regions one at a time and re-runs the model; embedding that in a training loop multiplies cost by the number of regions.
3. **It requires a person.** Speech naturalness, image quality, whether a generated report reads correctly: these are measured by mean opinion score, a panel of humans, and nobody has found a way around it for the cases that matter.
4. **There are many right answers.** In translation or report generation, one reference is one valid output among many, and penalising distance from it penalises correct alternatives.

So the loss is a **proxy**: a stand-in chosen because it is differentiable, cheap, and correlated with what is wanted. Training then optimises the proxy and reports the metric, and the entire enterprise rests on a correlation nobody measures.

The clearest instance: a defect detector is judged on precision and recall, and trained on cross-entropy. Cross-entropy is minimised very effectively by predicting "normal" everywhere when 99% of cases are normal. **The proxy's optimum and the metric's optimum are in different places, and the optimiser goes where the proxy points.** Class weighting is the standard patch, but weighting is an attempt, and whether it worked is answered by the metric afterward, not by the loss.

## Key concepts

### The statistician computes the probability; you make the decision

I can distinguish two English vowel sounds, or I cannot. I get 5 of 8 right. Can a statistician tell you whether I can hear the difference?

No, and being clear about what they *can* tell you is the whole point. Under the null hypothesis that I am guessing, $$P(\ge 5 \text{ of } 8) = 93/256 = 0.363$$. That is the entire statistical contribution. Roughly one guesser in three does at least this well, so the result is unremarkable. Where the cut-off sits is not a statistical question:

| score | $$P$$ under guessing |
|---|---|
| ≥ 5 | 0.363 |
| ≥ 6 | 0.145 |
| ≥ 7 | **0.035** |
| 8 of 8 | **0.0039** |

At the conventional $$\alpha=0.05$$, 7 of 8 clears the bar and 6 does not. Nothing in the mathematics chose 0.05. Hiring someone to teach pronunciation might warrant 0.001; a casual check might accept 0.1.

The consequence is arithmetic and uncomfortable. At $$\alpha=0.05$$, **one in twenty tests of a true null yields a "significant" result by luck alone**, which is the seed of the replication argument.[^ioannidis] The mitigating fact is that publication is not the end of the process: findings are contested, re-derived, and fail to replicate, and the field's self-correction is what the raw arithmetic omits.

There is a sharper version of this that I keep returning to: whether a model is good enough is not a machine learning question. The developer produces a number; the person who will rely on it decides what the number has to be. An AUROC of 0.95 may be unusable for one task and a landmark for another, and no threshold is universal.

### Accuracy, once more, and what the alternatives cost

Ten thousand people, one hundred sick. Predict "healthy" for everyone: **accuracy 0.9900**, sensitivity 0, precision undefined, F1 0, MCC 0. Accuracy is the one metric that does not notice.

Three real detectors at the same 1% prevalence make the trade-offs concrete:

| | acc | sens | spec | prec | NPV | F1 | MCC |
|---|---|---|---|---|---|---|---|
| high recall | 0.9095 | 0.950 | 0.909 | 0.096 | 0.9994 | 0.174 | 0.286 |
| balanced | 0.9900 | 0.800 | 0.992 | 0.500 | 0.9980 | 0.615 | 0.628 |
| high precision | **0.9936** | 0.400 | 0.9996 | 0.909 | 0.9940 | 0.556 | 0.601 |

The detector with the **best accuracy finds 40% of the sick.** The high-recall detector finds 95% and is wrong about nine of every ten it flags, which is correct behaviour for a triage filter feeding human review and wrong for an autonomous decision.

F1's harmonic mean is a guard against exactly the cheap win. With precision 1.0 and recall 0.01, the arithmetic mean is 0.505 and F1 is **0.0198**. The arithmetic mean rewards maximising one at the other's expense; the harmonic mean refuses to.

And note the two vocabularies for the same numbers. Information retrieval says precision and recall; medicine says sensitivity and specificity. Recall and sensitivity are identical, but precision is not specificity, and quoting either one alone is a signal that something is being hidden. They come in pairs because one of each pair is trivially maximised alone.

### The curve, the summary, and what AP actually is

Every threshold produces a different confusion matrix, so a classifier is a *family* of operating points. The ROC curve traces sensitivity against $$1-\text{specificity}$$ across all of them; the PR curve traces precision against recall. AUROC and average precision collapse each curve into one number.

Once that is clear, **mAP stops being detection jargon**: AP is the area under the precision-recall curve, averaged over pre-set recall levels, and the "m" averages across object classes. It stands to the PR curve exactly as AUROC stands to the ROC curve.[^davis] Under heavy class imbalance the PR curve is the more informative of the two, because specificity's denominator is dominated by the abundant negatives and large changes in false-positive count barely move it.[^saito]

Summarising a curve is useful for ranking systems and useless for deploying one. **No system runs on a curve**: deployment picks a point, and the point is chosen from the cost of each error, not from the plot.

### What "better than doctors" did and did not show

Gulshan et al. put a retinopathy detector's ROC curve against individual ophthalmologists' operating points; several sit below the curve.[^gulshan] Within the frame of the study, the model outperformed those readers.

The frame is the thing to hold onto. Each reader was answering one binary question about one disease from one image, with the reference standard built by adjudication panel. Nobody attends an eye clinic to have that question answered. A clinician is deciding what is wrong across an open set of possibilities, with history and examination, and "is there diabetic retinopathy in this photograph" is one bounded sub-task extracted from that. Beating readers on it is a real result about the sub-task and not a result about the job.

The clinicians' own use case points the same way: the value is in screening volume, where most images are normal and the hard part is sustained attention rather than difficulty, and as a check that something obvious was not missed.

## Why it matters for my work

This is the frame for most of what I do. If a model's reliance on valid evidence is the thing worth measuring, it is a textbook proxy problem: **every faithfulness measure I would want is non-differentiable, expensive, or requires an expert**, hitting three of the four reasons at once. Occlusion-based measures re-run the model per region; expert agreement needs experts; anything defined on a thresholded attribution map has no gradient.

So the honest description of the work is not "optimise faithfulness." It is: choose a proxy, then measure the gap between the proxy and the thing, and treat that gap as a quantity to report rather than an embarrassment to omit. A [shortcut](/study/shortcut-learning-in-medical-imaging/) is exactly a solution that scores well on the proxy and badly on the thing, which means shortcut learning is not a separate pathology. It is what proxy optimisation does when the correlation between proxy and target breaks, and the correlation is most likely to break off the training distribution, which is where deployment is.

The second thing I take from this is about who sets thresholds. A developer who picks the operating point has made a clinical decision without clinical authority, and the [decision-curve framing](/study/evaluation-beyond-auroc/) is the tool for handing it back: state the cost ratio at which each choice becomes preferable, and let the people who bear the costs choose. Reporting AUROC alone is not neutrality. It is declining to state the question.

## What I have not resolved

Whether the proxy-target gap can be measured cheaply enough to monitor during training rather than only at the end. Evaluating the expensive metric on a small held-out subset each epoch is the obvious approach; I do not know whether the correlation is stable enough over the course of training for that to be informative, or whether it drifts in exactly the regime where it matters.

---

[^ioannidis]: Ioannidis, J. P. A. (2005). Why most published research findings are false. *PLoS Medicine*, 2(8), e124. [10.1371/journal.pmed.0020124](https://doi.org/10.1371/journal.pmed.0020124)

[^davis]: Davis, J., & Goadrich, M. (2006). The relationship between Precision-Recall and ROC curves. *ICML*. [10.1145/1143844.1143874](https://doi.org/10.1145/1143844.1143874)

[^saito]: Saito, T., & Rehmsmeier, M. (2015). The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. *PLoS ONE*, 10(3), e0118432. [10.1371/journal.pone.0118432](https://doi.org/10.1371/journal.pone.0118432)

[^gulshan]: Gulshan, V., et al. (2016). Development and validation of a deep learning algorithm for detection of diabetic retinopathy in retinal fundus photographs. *JAMA*, 316(22), 2402–2410. [10.1001/jama.2016.17216](https://doi.org/10.1001/jama.2016.17216)
