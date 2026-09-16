---
layout: study_note
title: "The Kernel Trick: Similarity Instead of Coordinates"
description: "Why the SVM dual admits a kernel at all, what a kernel is being asked to encode, and how one-class SVM and SVDD turn the same machinery into novelty detection."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Neural Networks & Representation"
order: 7
source: "Independent study"
written: true
updated: "2026-09-15"
---

Everything up to here handles linearly separable patterns, possibly with some slack. Real data is often not linearly separable in any sense that slack can rescue: two concentric rings, say. The standard fix is to map the data into a space where it *is* separable, and the kernel trick is the observation that you may never need to build that space.

## Core question and definition

Map $$x \mapsto \varphi(x)$$ into some higher-dimensional space and run a linear classifier there. A decision boundary that is linear in $$\varphi$$-space pulls back to a curved boundary in the original space. Concentric rings become separable the moment you add a radius coordinate.

This is structurally what a deep network does: layers of feature transformation with a linear classifier on top. The difference is entirely in how $$\varphi$$ is arrived at: learned by gradient descent there, chosen by the practitioner here.

The obstacle is obvious. If $$\varphi$$ maps into a thousand dimensions, the [primal SVM](/study/support-vector-machines/) has a thousand parameters, and if it maps into infinitely many the primal has no finite solution at all.

## Key concepts

### The dual never touches the coordinates

Look again at the dual objective and the decision rule:

$$
\max_{\alpha}\ \sum_i \alpha_i - \tfrac12\sum_{i,j}\alpha_i\alpha_j y_iy_j \langle x_i,x_j\rangle,
\qquad
f(x) = \sum_i \alpha_i y_i \langle x_i, x\rangle + b .
$$

The samples appear **only inside inner products**. Substituting $$\varphi$$ changes $$\langle x_i,x_j\rangle$$ into $$\langle \varphi(x_i),\varphi(x_j)\rangle$$ and changes nothing else: the number of variables is still $$n$$, one per training sample, regardless of how large the feature space is. Whether $$\varphi$$ lands in three dimensions or a million, the problem you solve is the same size.

So the only thing standing in the way is computing $$\langle\varphi(x_i),\varphi(x_j)\rangle$$. And that is a single number.

### Defining the inner product instead of the map

Skip $$\varphi$$ entirely and define

$$
K(x, y) = \langle \varphi(x), \varphi(y)\rangle
$$

directly, as a function taking two inputs to a scalar. That is the **kernel trick**: never write $$\varphi$$ down, never evaluate it, and assert only that a corresponding $$\varphi$$ exists.

The concrete case makes it unmysterious. In two dimensions take $$K(x,y) = (x^{\mathsf T}y)^2$$. Expanding,

$$
(x_1y_1 + x_2y_2)^2 = x_1^2y_1^2 + 2x_1x_2y_1y_2 + x_2^2y_2^2
= \big\langle (x_1^2,\ \sqrt2\,x_1x_2,\ x_2^2),\ (y_1^2,\ \sqrt2\,y_1y_2,\ y_2^2)\big\rangle .
$$

So this kernel *is* the inner product after the map $$\varphi(x) = (x_1^2, \sqrt2 x_1x_2, x_2^2)$$ into three dimensions, but computing $$K$$ costs one dot product and one squaring, and the three-dimensional vector is never formed. With a Gaussian kernel the corresponding $$\varphi$$ is infinite-dimensional and could not be formed.

Not every two-argument function qualifies. $$K$$ must be symmetric and positive semidefinite: the Gram matrix $$K_{ij} = K(x_i,x_j)$$ must be PSD for every finite sample. Mercer's condition is what guarantees that some $$\varphi$$ exists to be implicit about.[^mercer]

### A kernel is a similarity measure, and that is how to design one

The useful way to think about designing a kernel is not "what feature map do I want" but **"what does it mean for two of these objects to be similar?"** An inner product is one of the most common similarity measures there is, and a kernel generalises it. If you have a defensible notion of similarity between two proteins, two strings, or two graphs, objects with no natural vector representation at all, and it satisfies the PSD condition, you can run a linear classifier in a high-dimensional space you never describe.

In practice two choices cover most usage. The **linear** kernel, which is no kernel at all, and the **Gaussian/RBF** kernel

$$
K(x,y) = \exp\!\left(-\frac{\lVert x-y\rVert^2}{2\sigma^2}\right).
$$

Here $$\sigma$$ controls locality, and it is a complexity knob. Small $$\sigma$$ makes the kernel peaked: only very nearby samples influence the decision at a point, and the boundary becomes intricate and wraps tightly around individual training points: overfitting, in the shape of the boundary itself. Large $$\sigma$$ smooths it out. It interacts with $$C$$, so the two are tuned together and neither alone is the regularisation story.

The honest practical note: for patterns intricate enough to genuinely need a small $$\sigma$$, a neural network is usually the better tool now, and the reason to reach for an SVM is the small-data regime. Try the linear kernel first.

The trick is also not specific to SVMs. Kernel PCA is the same substitution applied to a different problem, and the list goes on.[^kpca]

### The relation to nearest neighbours

Written as $$f(x) = \sum_i \alpha_i y_i K(x_i, x) + b$$, the classifier is comparing a new sample against stored training samples by similarity and voting. That is $$k$$-NN's structure.

The difference is that most $$\alpha_i$$ are zero. $$k$$-NN's standing objection is that it must retain the entire training set; the SVM retains only the support vectors. The [KKT conditions](/study/kkt-conditions-and-shadow-prices/) are what deliver that sparsity: it is not an approximation someone added afterwards, it falls out of the optimality conditions.

### One class, and the smallest enclosing sphere

Drop the second class entirely. **One-class SVM** finds the hyperplane that separates the data from the origin with maximum distance, with slack for outliers; anything falling on the origin side of it is flagged as not belonging.[^oc] **SVDD** poses the sibling problem: the smallest sphere containing the data, again with slack, and anything outside it is an outlier.[^svdd] Both dualise exactly as before and both accept kernels without modification, which is the payoff for having derived the dual properly once.

These are the classical novelty- and [out-of-distribution](/study/distribution-shift-and-out-of-distribution-generalization/) detectors.

## Why it matters for my work

One-class methods are the cleanest available statement of a question a deployed model should be asking: *is this input like the things I was trained on?* An answer to that is what makes [abstention](/study/calibration-uncertainty-and-selective-prediction/) principled rather than a threshold on a softmax.

But the caveat is sharp enough to be the whole point. A one-class model defines "normal" as **resembling the training set under the chosen kernel**. If the training data carries a site signature, one scanner, one protocol, one preprocessing pipeline, then that signature is part of what the detector has learned to call normal. The consequence is a specific and bad failure mode: the detector flags a *different scanner* as anomalous while passing a genuinely novel pathology acquired on the familiar one. It is doing what it was asked; it was asked the wrong question. The same [shortcut](/study/shortcut-learning-in-medical-imaging/) that corrupts a classifier corrupts the detector meant to catch the classifier's blind spots, and it corrupts both in the same direction, so the two failures do not cancel: they agree.

The second point is about where a modelling choice goes when it stops being visible. Choosing a kernel is choosing a similarity measure, with the same epistemic standing as choosing features: a claim about what makes two patients comparable, made by a person, open to being argued with. End-to-end learning did not remove that claim. It moved it into the training data and the architecture, where it is no longer written down anywhere and no longer has an author. Representation-learning audits exist because someone has to go and recover it.

---

[^mercer]: Mercer, J. (1909). Functions of positive and negative type, and their connection with the theory of integral equations. *Philosophical Transactions of the Royal Society A*, 209, 415–446. [10.1098/rsta.1909.0016](https://doi.org/10.1098/rsta.1909.0016)

[^kpca]: Schölkopf, B., Smola, A., & Müller, K.-R. (1998). Nonlinear component analysis as a kernel eigenvalue problem. *Neural Computation*, 10(5), 1299–1319. [10.1162/089976698300017467](https://doi.org/10.1162/089976698300017467)

[^oc]: Schölkopf, B., Platt, J. C., Shawe-Taylor, J., Smola, A. J., & Williamson, R. C. (2001). Estimating the support of a high-dimensional distribution. *Neural Computation*, 13(7), 1443–1471. [10.1162/089976601750264965](https://doi.org/10.1162/089976601750264965)

[^svdd]: Tax, D. M. J., & Duin, R. P. W. (2004). Support vector data description. *Machine Learning*, 54, 45–66. [10.1023/B:MACH.0000008084.60811.49](https://doi.org/10.1023/B:MACH.0000008084.60811.49)
