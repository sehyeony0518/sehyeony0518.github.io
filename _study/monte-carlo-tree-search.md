---
layout: study_note
title: "Monte Carlo Tree Search: Exploration, Exploitation, and the Cost of Never Looking"
description: "Why randomness earns a place inside a search algorithm, what the UCT formula is actually balancing, and the sense in which a fixed test suite is a policy that stopped exploring."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "decision-and-control"
category_title: "Decision Making & Reinforcement Learning"
order: 2
source: "Independent study"
written: true
updated: "2026-09-15"
---

"Monte Carlo" is not the name of one algorithm. It names a family, and the family resemblance is that randomness is doing load-bearing work rather than sitting at the edges as noise. Monte Carlo tree search is the member of that family that plans: it decides what to do next in a game or a sequential decision problem by playing out random continuations and letting the results accumulate into a tree.

## Core question and definition

The problem a board game poses is that the tree of possible futures is too large to enumerate. Classical search handles this by cutting the tree off at a fixed depth and calling in a hand-written evaluation function to score the leaves. That works only as well as the evaluation function, and for Go nobody could write one.

MCTS replaces the evaluation function with sampling. It grows an **asymmetric** tree — deep where the promising lines are, shallow elsewhere — by repeating four phases:

1. **Selection.** From the root, walk down the existing tree by a **tree policy**, choosing a child at each step until reaching a node that is not fully expanded.
2. **Expansion.** Add one new child for an untried move.
3. **Simulation (rollout).** From that new node, play to the end of the game using a cheap **default policy** — in the simplest version, uniformly random moves — and record who won.
4. **Backpropagation.** Walk back up the path just taken, incrementing each node's visit count and adding the result to its win total.

Run this thousands of times and the root's children carry visit counts and win rates that reflect a great deal of sampled play. The name reuses a word from [backprop](/study/backpropagation/) for something entirely different: no gradients, just counters being updated along a path. The four-phase template, and the many variants built on it, are catalogued in the standard survey.[^survey]

## Key concepts

### Exploration and exploitation are a genuine trade-off, not a tuning knob

The tree policy faces the question that defines the **multi-armed bandit** problem. You have several slot machines with unknown payout rates and a finite number of pulls. Every pull spent measuring a machine you will not end up using is wasted; every pull spent on your current favourite is a pull that could have revealed a better one.

The everyday version: a new restaurant opens in your neighbourhood. You have a place you already like. Going to the new one might find something better, or might waste the evening. Never going means you will never know — and crucially, *the cost of never knowing does not show up anywhere in your record of past evenings*. Your observed average stays high. It is the counterfactual that is missing.

### The UCT formula makes the trade-off explicit

Upper Confidence bounds applied to Trees scores each child as

$$
\text{UCT}(i) = \underbrace{\frac{w_i}{n_i}}_{\text{exploit}} + \underbrace{C\sqrt{\frac{\ln N}{n_i}}}_{\text{explore}},
$$

where $$w_i$$ is the child's accumulated wins, $$n_i$$ its visit count, $$N$$ the parent's, and $$C$$ a constant. The first term is the observed win rate — what the evidence so far says. The second is large when $$n_i$$ is small relative to how much the parent has been visited, and it shrinks as $$\sqrt{\ln N / n_i}$$ once the child has been sampled. A child that looks mediocre keeps getting revisited for a while, because the explore term says the estimate is not yet trustworthy; a child that has been sampled many times is judged almost entirely on its record.

This form is inherited from UCB1 for bandits, where it comes with a regret bound, and carried into trees by Kocsis and Szepesvári.[^uct][^ucb] The bound is what makes the second term a principled quantity rather than a heuristic: it is an upper confidence bound on the true value, and acting on optimism-under-uncertainty is what keeps the total shortfall growing only logarithmically.

### The final move is not chosen by win rate

After the search budget is spent, the obvious answer is to play the child with the best win rate. It is also common — and defensible — to play the **most-visited** child instead. A high win rate over four visits is a weaker claim than a slightly lower one over four thousand. Visit count is the tree's own record of how much it has checked, and preferring the well-checked child is a robustness choice: it refuses to act on an estimate the search itself has not stress-tested.

AlphaGo kept this structure and replaced both policies with learned networks — a policy network to bias selection and expansion, a value network to shortcut or supplement the rollout.[^alphago] The four phases survived intact; what changed was the quality of the guesses feeding them.

## Why it matters for my work

The structure that makes exploration necessary is the same structure that makes a fixed evaluation suite insufficient.

A benchmark is a tree policy with the explore term set to zero. It samples exactly the situations someone thought to include, accumulates a win rate over them, and reports it. The situations nobody enumerated contribute nothing to the number — not a low score, *no score at all*. This is exactly the restaurant you never tried: the absence is invisible in the statistic, so a model can pass while relying on a shortcut the suite never probed, and the reported accuracy is perfectly consistent with that.

Two consequences carry into [auditing](/study/shortcut-learning-in-medical-imaging/) directly. First, the visit-count preference is the right instinct for evaluation reporting too: a subgroup result over twelve cases and one over twelve hundred should not be presented as commensurable, and reporting the denominator alongside the estimate is the minimum. Second, an audit needs its own explore term — a deliberate budget spent on conditions that look unpromising, precisely because "unpromising" is a judgement made from the same evidence that might be incomplete. Adversarial and stress testing are that budget. Without it, [external validation](/study/robustness-subgroup-performance-and-external-validation/) is measuring how well the model does on the neighbourhood restaurant it already knows.

The honest limitation: bandit theory gives regret bounds because the reward is observed after every pull. An audit has no such luxury — it usually cannot observe the outcome of the deployment path it did not take, which is why exploration in evaluation stays a design discipline rather than an algorithm with a guarantee attached.

---

[^ucb]: Auer, P., Cesa-Bianchi, N., & Fischer, P. (2002). Finite-time analysis of the multiarmed bandit problem. *Machine Learning*, 47, 235–256. [10.1023/A:1013689704352](https://doi.org/10.1023/A:1013689704352)

[^uct]: Kocsis, L., & Szepesvári, C. (2006). Bandit based Monte-Carlo planning. *ECML 2006*, 282–293. [10.1007/11871842_29](https://doi.org/10.1007/11871842_29)

[^survey]: Browne, C. B., et al. (2012). A survey of Monte Carlo tree search methods. *IEEE Transactions on Computational Intelligence and AI in Games*, 4(1), 1–43. [10.1109/TCIAIG.2012.2186810](https://doi.org/10.1109/TCIAIG.2012.2186810)

[^alphago]: Silver, D., et al. (2016). Mastering the game of Go with deep neural networks and tree search. *Nature*, 529, 484–489. [10.1038/nature16961](https://doi.org/10.1038/nature16961)
