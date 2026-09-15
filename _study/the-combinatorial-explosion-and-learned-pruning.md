---
layout: study_note
title: "The Combinatorial Explosion, and Why Pruning Alone Is Not Enough"
description: "Lighthill's 1973 case against AI was arithmetically correct and is still correct. What changed is that nobody searches the tree any more — and working the numbers shows that pruning the branches only solves half of it."
tab: "ai-foundations"
tab_title: "Theory"
category: "decision-and-control"
category_title: "Decision Making & Reinforcement Learning"
order: 3
source: "Independent study"
written: true
updated: "2026-09-15"
---

The most useful thing about the argument that shut down British AI funding in 1973 is that it was right.[^lighthill] It is usually recounted as a failure of imagination. It was not. It was an arithmetic claim, the arithmetic was correct, and the arithmetic has not changed.

## Core question and definition

Lighthill's case rests on a growth-rate comparison.

The number of interpretations of a sentence grows **exponentially in its length**. "Spirit" has perhaps five dictionary senses — mind, courage, ghost, essence, and liquor. Over a three-word span with five senses each, that is $$5^3 = 125$$ readings; over five words, $$3125$$. And "take" carries something closer to fifty senses, so two occurrences alone admit $$50^2 = 2500$$ combinations. Add a word, multiply again.

Computing power grows by doubling: 64K, 128K, 256K. Fast, but the base is 2 and the exponent is *time*, whereas the problem's exponent is *input size*. One extra word of context outruns years of hardware progress.

The famous illustration is a machine-translation demo where "the spirit is willing but the flesh is weak," round-tripped through Russian, allegedly returned as "the vodka is good but the meat is rotten." The anecdote is almost certainly apocryphal — it circulated for years without a documented source — but it illustrates the real failure exactly, which is why it survived: every word choice was defensible in isolation, and the sentence could only be resolved by knowing which combination made sense.

## Key concepts

### The numbers, and the hardware that cannot catch them

Go has roughly 200 legal moves per position and games run about 150 moves, giving on the order of $$200^{150} = 10^{345}$$ sequences. Chess, at roughly 40 moves over 80 plies, gives $$40^{80} = 10^{128}$$.

The observable universe contains about $$10^{80}$$ atoms. Chess exceeds it by 48 orders of magnitude; Go by 265.

The comparison that makes Lighthill's point precise: under Moore's law, buying the compute to search **one additional ply of Go** — a factor of 200 — takes $$\log_2(200)\times 2 \approx 15.3$$ years. Fifteen years of hardware progress for one move of lookahead. Exhaustive search was never going to arrive, and no plausible extrapolation makes it arrive.

### What actually changed

Not the arithmetic. The refusal to search.

AlphaGo does not evaluate $$10^{345}$$ sequences. A policy network proposes a handful of plausible moves at each position and the search explores only those — the network's job is not to play well, it is to **shrink the branching factor from 200 to 5**. Human players do the same thing, which is why a strong player can look further ahead than a beginner despite thinking no faster.

Here is where working the numbers changed my understanding of the story. Pruning to 6 candidates gives $$6^{150} = 10^{117}$$ — still 37 orders of magnitude beyond the atom count. **Pruning the width alone does not make Go tractable.** The depth must be truncated too:

| candidates | depth | leaves | tractable |
|---|---|---|---|
| 6 | 150 | $$10^{117}$$ | no |
| 6 | 20 | $$3.7\times10^{15}$$ | no |
| 6 | 10 | $$6.0\times10^{7}$$ | yes |
| 5 | 8 | $$3.9\times10^{5}$$ | yes |

So two learned functions are required, not one. The policy network cuts the width; a **value network** cuts the depth, by estimating a position's worth without playing to the end. Either alone leaves the problem intractable. That the two are separate networks in AlphaGo is not an implementation detail — it is the two halves of the answer to Lighthill.

[Monte Carlo tree search](/study/monte-carlo-tree-search/) is what allocates the remaining budget among the surviving branches, spending more on promising lines. It is the third piece, and it presupposes that the first two already reduced the problem to a size where allocation is meaningful.

### The same shape in language

Word-sense disambiguation was Lighthill's example, and it was solved the same way. A transformer does not enumerate sense combinations; it produces a representation in which context has already collapsed the possibilities, so that "take a bus" and "take a pill" resolve without the $$50^2$$ grid ever being constructed.

The lecturer's observation, from having supervised a dictionary application built on this: the word-sense component was tractable, and **the year of work went into collecting and cleaning data.** That inversion — the mathematically frightening part turning out to be the easy part — is worth remembering, and not only for this example.

## Why it matters for my work

The structural lesson is the one I keep wanting to state precisely: **a learned model's contribution is often not to solve the problem but to make a classical method's search space small enough that the classical method works.** The neural network is the proposal distribution; the guarantees, where there are any, come from the procedure it feeds.

That reframes what to audit. If a policy network proposes five candidates and the search picks among them, then anything never proposed is unreachable regardless of how good the search is. **The pruning step is where the possibilities are eliminated, and it is the step with no guarantees.** For a diagnostic system built the same way — a model that narrows to a shortlist for a clinician or a downstream procedure — the failure that matters is not a wrong ranking within the shortlist. It is a correct diagnosis that never entered it, and the evaluation metrics computed over the shortlist cannot see that by construction.

There is also a cleaner way to say what hardware did. It is often said that deep learning worked because GPUs arrived. The more exact statement is that **the mathematics was mostly in place decades earlier, and what changed was data and compute** — which is why Lighthill's argument survives rather than being refuted. Compute did not catch the exponential. It made it affordable to *learn the function that avoids* the exponential. Those are different claims, and only the second one is true.

## What I have not resolved

Whether the pruning-plus-truncation structure has an analogue in diagnosis that is worth building deliberately rather than describing after the fact. The differential diagnosis is a shortlist, generated by something and then narrowed by testing — which is the same two-stage shape. Whether a value-function equivalent exists there, something that scores a partial diagnostic state without running it to conclusion, I genuinely do not know.

---

[^lighthill]: Lighthill, J. (1973). Artificial Intelligence: A General Survey. In *Artificial Intelligence: a paper symposium*. Science Research Council, London.
