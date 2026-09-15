---
layout: study_note
title: "Recommender Systems: Embeddings, Interactions, and a Field That Audited Itself"
description: "Why recommendation is a ranking problem over extremely sparse categorical features, how embeddings and feature interactions address that, and the reproducibility study that found most of the progress was not there."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "learning-principles"
category_title: "Learning Principles"
order: 13
source: "Independent study"
written: true
updated: "2026-09-15"
---

Recommendation is, at bottom, a **ranking problem**: given what is known about a user, sort the available items by how much that user is likely to want each one. What makes it its own subfield is not the ranking. It is the shape of the input.

## Core question and definition

Most machine learning operates on dense features — pixel intensities, lab values, measurements where every entry carries information and arithmetic on them means something. Recommendation operates on **extremely sparse categorical features**.

A user's history among a hundred thousand videos is a hundred-thousand-dimensional vector with maybe fifty non-zero entries. Browsing history over the web is worse, and gets worse still once you distinguish sections within a site. These are identifiers, not quantities: video #1300 is not larger than video #1299, and averaging them produces nothing.

So the central technical problem is **how to represent identifiers so that arithmetic on them means something** — which is the problem embeddings exist to solve.

## Key concepts

### Embedding turns identifiers into geometry

An embedding maps a discrete category into a continuous vector space, with two properties that matter: the dimension drops enormously (fifty thousand words to a few hundred dimensions), and distances and differences in the target space *mean* something.

The postcode analogy makes the point cleanly. Subtracting two postcodes is meaningless. Map each to the median income of its area, or to a latitude–longitude pair, and now differences, distances and interpolation are all interpretable. Embeddings are learned versions of that map, trained by making the representation serve some task — word embeddings from predicting context, item embeddings from predicting interactions — so that the geometry ends up encoding whatever the task required.

### Before neural networks: filtering and factorisation

**Collaborative filtering** needs no content understanding at all. Find users whose past judgements resemble this user's, and predict from theirs. The item could be anything; the method only sees the pattern of agreement.

**Matrix factorisation** makes that explicit. Represent every user and every item as a vector, and model the rating as the inner product:

$$
\hat{r}_{ui} = \mathbf{p}_u^{\mathsf T}\mathbf{q}_i,
$$

fitting $$\mathbf{p}$$ and $$\mathbf{q}$$ so the predictions match the observed entries. The inner product is a [similarity measure](/study/the-kernel-trick/), so this is asking which users and items point in the same direction.

The same structure covers educational recommendation, where the goal is to serve a problem the learner will find *appropriately* difficult — too easy teaches nothing, too hard teaches nothing. Represent a student by proficiency across skills and a problem by the skills it demands, and the inner product predicts the score. Those vectors can be learned from data or written down by a domain expert, and the expert version is interpretable in a way the learned one is not.

### Interactions carry information that averages destroy

Suppose someone watched *Inception*, and also an old Leonardo DiCaprio film. Averaging those two signals gives a mush of genre. The **conjunction** — both of these, together — points at the actor, and is a far better recommendation signal than either alone. Had the second film been *Interstellar* instead, the same first item would imply something different.

The obstacle is combinatorial: fifty thousand features give two and a half billion pairs, essentially all of which are zero in any given dataset, and a statistical method cannot learn from a table that is almost entirely empty. **Factorisation machines** resolve this by computing interactions between *embeddings* rather than between raw identifiers — the pair is a few hundred dimensions wide instead of billions, and dense instead of empty.[^fm]

Wide & Deep runs both paths at once: a deep tower over embedded features for generalisation, and a wide linear part over explicit conjunctions for memorisation.[^wd] DLRM makes the interaction stage the centrepiece, taking pairwise dot products among embedding vectors before the final network.[^dlrm]

### Two stages, and why the embedding tables are enormous

At production scale, ranking every item is out of the question, so the pipeline splits: **candidate generation** narrows millions of items to hundreds using coarse signals, then **ranking** scores those hundreds with a richer model and more features.[^yt] What feeds the ranker is largely the user's own history — the embedded videos they watched, their search tokens, context — because *what someone watched* describes their taste better than any label attached to them.

The consequence is that these are among the largest models deployed anywhere, and the size is nearly all embedding table: one row per item per category, tens of millions of rows. The compute is trivial by comparison; the memory and lookup traffic dominate, which is why recommendation is a standard hardware benchmark and why serving typically splits embedding lookup onto CPU and the dense layers onto accelerators.

### Graphs, and the cold-start problem

A fixed user–item embedding table breaks when a new user or item arrives: there is no row for them, and there will not be one until something retrains. Yet a new user who watches three videos should get sensible recommendations immediately. Using *context* — what they just watched — rather than an identity lookup is what makes that possible.

Users, items, groups and friendships form a graph naturally, so [graph neural networks](/study/spectral-filtering-and-graph-convolution/) fit the data's actual shape. Recommendation becomes **link prediction**: should an edge exist between this user and this item? Node embeddings are refined by repeatedly aggregating neighbours, so after several steps each node's representation reflects structure well beyond its immediate connections, and the representation depends on the graph rather than only on an identifier.[^pin]

## Why it matters for my work

The part of this I most want to keep is not a method. It is that **this field ran the audit and published the result.**

A 2019 study attempted to reproduce eighteen neural recommendation methods from top venues. Seven could be reproduced with reasonable effort. Of those seven, six were outperformed by simple, long-established baselines — nearest-neighbour methods and basic heuristics — that had been properly tuned.[^dacrema] The reported progress of several years largely failed to survive contact with a fair comparison.

The mechanism is worth naming precisely, because it generalises. Recommendation is genuinely hard to evaluate: offline metrics correlate imperfectly with online behaviour, dataset splits and negative sampling are unstandardised, and the baselines are rarely tuned with the care the proposed method receives. None of that requires misconduct. It requires only that every small choice be made, independently and in good faith, in the direction that favours the new method — and the field's reward structure supplies that pressure without anyone intending it.

Every one of those conditions holds in medical AI, and several hold harder. Evaluation is [contested and proxy-laden](/study/evaluation-beyond-auroc/), splits are non-standard, baselines are frequently a citation rather than a tuned implementation, and the published record is filtered by what worked. The honest conclusion I take is not that medical AI results are wrong. It is that **an equivalent reproducibility study has largely not been run**, so the field does not know what its own answer would be — and "we have not checked" is a different epistemic state from "we checked and it held," even though the literature reads the same either way.

The technical lesson underneath is the sparsity one, and it also transfers. Rare presentations are the medical analogue of long-tail items: the categories that matter most are the ones with the fewest examples, and a method optimised on aggregate performance will be optimised for the head. That is the same structural problem [MCC exists to expose](/study/matthews-correlation-coefficient/), arriving from a different direction.

---

[^fm]: Rendle, S. (2010). Factorization machines. *ICDM 2010*, 995–1000. [10.1109/ICDM.2010.127](https://doi.org/10.1109/ICDM.2010.127)

[^wd]: Cheng, H.-T., et al. (2016). Wide & deep learning for recommender systems. *DLRS 2016*, 7–10. [10.1145/2988450.2988454](https://doi.org/10.1145/2988450.2988454)

[^dlrm]: Naumov, M., et al. (2019). Deep learning recommendation model for personalization and recommendation systems. [arXiv:1906.00091](https://arxiv.org/abs/1906.00091)

[^yt]: Covington, P., Adams, J., & Sargin, E. (2016). Deep neural networks for YouTube recommendations. *RecSys 2016*, 191–198. [10.1145/2959100.2959190](https://doi.org/10.1145/2959100.2959190)

[^pin]: Ying, R., et al. (2018). Graph convolutional neural networks for web-scale recommender systems. *KDD 2018*, 974–983. [10.1145/3219819.3219890](https://doi.org/10.1145/3219819.3219890)

[^dacrema]: Ferrari Dacrema, M., Cremonesi, P., & Jannach, D. (2019). Are we really making much progress? A worrying analysis of recent neural recommendation approaches. *RecSys 2019*, 101–109. [10.1145/3298689.3347058](https://doi.org/10.1145/3298689.3347058)
