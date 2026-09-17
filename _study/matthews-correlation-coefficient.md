---
layout: study_note
title: "Matthews Correlation Coefficient: A Metric That Fails Loudly"
description: "Why accuracy moves with prevalence and F1 ignores a whole cell of the confusion matrix, and how MCC falls out of a chi-squared test of independence between prediction and truth."
og_image: "https://sehyeony0518.github.io/assets/img/og/matthews-correlation-coefficient.png"
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
subgroup: "Validation Design & Performance Measures"
order: 8
source: "Independent study"
written: true
updated: "2026-09-15"
---

Choosing a metric is not a lookup. It requires having already decided what makes one classifier better than another, and if you cannot say that, no table of formulas will tell you. Even distance is like this: the straight line between two points is the right answer until you are driving, at which point it is the road network. There is no context-free best.

What can be argued is narrower and still useful: that some metrics report high numbers in situations everyone agrees are bad. That is a defect nobody has to negotiate over.

## Core question and definition

Accuracy has that defect. Take a classifier that gets 90% of dogs right and 25% of cats right, and vary only how many of each are in the test set:

| dogs | cats | accuracy |
|---|---|---|
| 20 | 4 | 79.2% |
| 300 | 100 | 73.8% |
| 380 | 20 | 86.8% |

The classifier never changed. Its per-class behaviour is identical in all three rows: the macro-average is 57.5% throughout. Accuracy moved thirteen points because the *test set* changed. A number that depends this strongly on something other than the thing being measured is reporting the wrong thing.

The sharper case. Take 95 positives and 5 negatives, and a classifier that has some bug and predicts "positive" for everything, which happens more often than it sounds, since nothing about a training loop announces that its output collapsed.

$$
\text{accuracy} = 0.950, \qquad \text{precision} = 0.950, \qquad \text{recall} = 1.000, \qquad F_1 = 0.974 .
$$

An F1 of 97.4% for a model that has learned nothing whatsoever. Anyone reading a summary table would conclude it worked.

**MCC on that table is 0.000.**

## Key concepts

### F1 leaves out a cell

$$
F_1 = \frac{2\,\text{TP}}{2\,\text{TP} + \text{FP} + \text{FN}} .
$$

There is no TN in that expression. F1 is therefore not symmetric under relabelling which class is "positive," and it is blind to everything the model does on negatives. In the degenerate example above, TN $$= 0$$, the model got every single negative wrong, and F1 cannot see it.

Precision and recall have to be read together, and the trade-off between them is real rather than a knob. Predict all 100 exam questions and you will certainly include the 10 that appear: recall 100%, precision 10%. Predict 5 and get 5 right: precision 100%, recall 50%. Neither dominates, and which you want depends on the cost of being wrong in each direction.

### MCC is the chi-squared test on the confusion matrix

The derivation is what justifies the formula, and it starts from a question about the *worst* case rather than the best: what does it mean for a classifier to be worthless?

It means the prediction is **independent** of the truth. Random guessing, in the precise sense that knowing the label tells you nothing about the output. And independence in a contingency table is exactly what [Pearson's chi-squared test](/study/hypothesis-testing-and-sampling-distributions/) measures. Writing the confusion matrix as $$a,b,c,d$$ (TP, FP, FN, TN), the expected count in each cell under independence is the row total times the column total over $$n$$, and grinding through the algebra collapses all four terms onto a single numerator:

$$
\chi^2 = \frac{n\,(ad - bc)^2}{(a+b)(c+d)(a+c)(b+d)} .
$$

Take $$\sqrt{\chi^2/n}$$, restore the sign of $$ad-bc$$, and that is MCC:

$$
\text{MCC} = \frac{ad - bc}{\sqrt{(a+b)(c+d)(a+c)(b+d)}}, \qquad \text{MCC}^2 = \frac{\chi^2}{n}.
$$

(Checked numerically across several tables: the two sides agree to machine precision.)

So MCC is not an arbitrary combination chosen because it behaves well. It is the association between prediction and truth, measured by the standard test for exactly that, rescaled to $$[-1,+1]$$[^matthews][^chicco]. It is also the Pearson correlation of the two binary vectors: `np.corrcoef` on the 0/1 labels and predictions returns the MCC formula's value exactly. Each of these readings explains **0 means random guessing**, which is the property the whole construction was aimed at.

The degenerate classifier above scores 0 because $$ad-bc = 0$$: it produced no association at all. The denominator also vanishes there, and the convention is to report 0: arguably a division by zero being papered over, but the value it is papered over with is the right one.

### ROC and PR curves under imbalance

A network emits a score, not a decision, so there is a confusion matrix for every threshold, and picking the threshold is a decision **you** must make. The training loss does not make it for you, and 0.5 is a default rather than an answer.

Sweeping the threshold traces a curve. ROC plots recall against $$\text{FPR} = \text{FP}/(\text{FP}+\text{TN})$$; the precision–recall curve plots precision against recall and contains no TN.

That difference decides which is informative when negatives dominate. In detection, sliding-window face detection was the classic case, thousands of candidate windows per image and a handful of faces, TN is enormous. FPR stays tiny no matter how many false positives there are, the ROC curve is pinned to the top-left, and AUROC sits near 1 while the operationally interesting region is compressed into a sliver at the left edge. The PR curve drops TN and spreads that region out.[^saito][^davis]

Worth keeping the hedge: this is a strong argument for preferring PR curves under heavy imbalance, not a proof that ROC is wrong. AUROC remains a reasonable single number for model selection during training, and PR-derived summaries have their own instabilities: the numbers can become very sensitive to a handful of samples, which is its own way of being misleading.

## Why it matters for my work

The property I actually want from a metric is that it **fails loudly**. A metric that reports 0.5 when a model is broken is more valuable than one that reports 0.97, even if the 0.97 is defensible under its own definition, because the failure mode of a summary number is not being wrong: it is being plausible.

Medical datasets are almost never balanced, and the minority class is almost always the one that matters. In that setting accuracy and F1 both drift upward with prevalence rather than with quality, and both can be high while a model does nothing for the cases the system exists to catch. MCC and a balanced-accuracy figure at least move in the right direction, and reporting them alongside the [operating point](/study/evaluation-beyond-auroc/) costs nothing.

Two limits I want recorded rather than glossed. MCC is a *correlation*, and association is not clinical utility: a model can have respectable MCC and still be useless at the threshold a clinic would run it at, because MCC integrates over the whole table rather than the region of it anyone will use. [Decision-curve analysis](/study/evaluation-beyond-auroc/) answers a question MCC does not.

And collapsing four numbers into one always discards something. The right default is to publish the confusion matrix. A single summary should accompany it, never replace it: every failure in this note is a case of four numbers becoming one and the one being read as though it were the four.

---

[^saito]: Saito, T., & Rehmsmeier, M. (2015). The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. *PLoS ONE*, 10(3), e0118432. [10.1371/journal.pone.0118432](https://doi.org/10.1371/journal.pone.0118432)

[^davis]: Davis, J., & Goadrich, M. (2006). The relationship between precision-recall and ROC curves. *ICML 2006*, 233–240. [10.1145/1143844.1143874](https://doi.org/10.1145/1143844.1143874)

[^chicco]: Chicco, D., & Jurman, G. (2020). The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation. *BMC Genomics*, 21, 6. [10.1186/s12864-019-6413-7](https://doi.org/10.1186/s12864-019-6413-7)

[^matthews]: Matthews, B. W. (1975). Comparison of the predicted and observed secondary structure of T4 phage lysozyme. *Biochimica et Biophysica Acta*, 405(2), 442–451. [10.1016/0005-2795%2875%2990109-9](https://doi.org/10.1016/0005-2795%2875%2990109-9)
