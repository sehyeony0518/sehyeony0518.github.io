---
layout: study_note
title: "MDPs and the Simulator Problem: Every RL Paper Starts After the Hard Part"
description: "The five-tuple that defines an environment, why a plan is not a policy, and the reason reinforcement learning works on games and struggles everywhere the simulator has to be built."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "decision-and-control"
category_title: "Decision Making & Reinforcement Learning"
order: 1
source: "Independent study"
written: true
updated: "2026-09-15"
---

Reinforcement learning formalises the environment as a **Markov decision process**: the five-tuple $$(\mathcal{S}, \mathcal{A}, R, P, \gamma)$$: states, actions, a reward function, transition probabilities $$P(s'\mid s,a)$$, and a discount factor.

Every textbook and every paper begins by assuming you have one. That assumption is doing an enormous amount of work, and this note is mostly about it.

## Core question and definition

Three axes locate a learning problem, and they make clear what RL is up against.

**Sequential or one-shot.** Classifying a photograph is one-shot: what you answered three images ago has no bearing on this one. Navigating a maze is sequential: the move three steps back constrains everything available now.

**Evaluative or instructive feedback.** Supervised learning is instructive: it tells you the correct answer. RL is evaluative: it hands you a *score* and no indication of what you should have done. Getting 3 out of 10 does not tell you which answer was wrong, and whether 3 is good depends on what everyone else scored, which you also do not see.

**Sampled or exhaustive.** If you could enumerate every state and every action you would not need to generalise. You cannot, so you generalise from a sample.

Supervised image classification sits at the easy end of all three; RL on a game sits at the hard end of all three. That is the whole reason RL is a separate subject, and the reason deep networks were necessary before deep RL was possible: the sampling problem had to be solved first.

## Key concepts

### A plan is not a policy

For a robot crossing an icy grid toward a goal, "right, right, down" is a **plan**. It is not a policy, and the difference is the whole game: it says nothing about what to do after slipping. One unexpected transition and there is no next instruction.

A **policy** $$\pi(a\mid s)$$ specifies an action for *every* state, including states you never intended to visit. That is a much stronger object, and it is why the robust choice on ice can be the one that moves away from the goal: if a slip near a hole has a one-in-three chance of falling in, the action that cannot possibly reach the hole beats the action that heads straight for the target.

Which raises the question that organises everything downstream: *which policy is better?* You cannot search for a good policy without a way to score one, and the score is the **value function**: the expected return from following $$\pi$$ onward. Value and policy are mutually defined, and the four families of RL method are four choices about which to attack: **value-based**, **policy-based**, **model-based** (learn $$P$$ and $$R$$, then derive a policy), and **actor–critic** (maintain both).

### AlphaGo as an assembly of these parts

Go's search tree is far too large to enumerate, so Monte Carlo tree search explores it selectively, and two learned networks make that selection affordable.

The **policy network** narrows *breadth*: of ~250 legal moves, most are not worth a thought, and a CNN trained on 30 million human positions to predict the expert's move (57% top-1 accuracy over 361 classes) prunes them. The **value network** reduces *depth*: given a board, estimate the eventual result, so the search need not play to the end. A third, deliberately tiny **rollout network** plays games out fast: far weaker, but callable millions of times, and AlphaGo averages its verdict with the value network's.[^ago]

One detail is worth more than the architecture. The policy network used inside the tree search is the **supervised** one, not the stronger RL-refined version: even though the RL version beats it head-to-head. Search does not want the single best move; it wants a well-spread distribution over plausible moves, because its job is to decide *where to look*. A sharper policy explores worse. That is the [exploration–exploitation](/study/monte-carlo-tree-search/) trade-off appearing as a concrete engineering choice, and it would be easy to get backwards by reasoning about strength alone.

### The part the textbooks skip

Now the assumption. Given an MDP, RL has a large toolkit. **But who gives you the MDP?**

For the cart-pole, the standard toy problem, writing the simulator means deriving the coupled nonlinear equations of motion: force balances in two directions, a torque balance, projection onto a rotating frame, elimination of internal reaction forces. Pages of work, several sign errors, and the result is not analytically solvable, so it is [linearised](/study/linearization-and-the-inverted-pendulum/) with the attendant validity limits. And that is the *easy* environment, the one in every tutorial.

So the honest summary of the field's situation: **RL flourishes where simulation is cheap and faithful.** Board games and video games have exact, free, unlimited simulators: the rules *are* the transition function. Everywhere else, someone has to build the simulator, and building a faithful one is typically harder than the RL that follows.

That is a selection effect, not evidence about where RL is useful. Reading the literature as though the impressive game results indicate readiness elsewhere is reading past the assumption in the first line of every paper.

## Why it matters for my work

The simulator problem is exactly why RL for treatment decisions is hard in a way that the published successes can obscure.

An MDP for clinical decision-making requires $$P(s' \mid s, a)$$: **the probability that a patient in this state moves to that state given this treatment.** That is not a modelling convenience: it is a complete causal model of treatment response, which is the thing medicine does not have and spends enormous effort trying to estimate one narrow slice at a time.

The workaround is off-policy learning from retrospective records, and its failure modes are documented rather than hypothetical. Coverage: the data contain only actions clinicians actually chose, so the value of an unchosen action is an extrapolation with nothing to anchor it. Confounding: treatment assignment responded to patient state, including state not recorded, so apparent treatment effects absorb indication bias. Evaluation: off-policy estimators have variance that grows with how far the learned policy departs from the observed one, and a policy that *agrees* with clinicians is not worth deploying, so the regime of interest is exactly the regime where the estimate is least trustworthy.[^guide]

None of this makes the work illegitimate; the sepsis work and its successors are serious.[^sepsis] What it makes illegitimate is treating a reported improvement in estimated value as comparable evidence to a trial result. The number is conditional on a transition model nobody validated, and "we assumed an MDP" is not a caveat in the discussion section: it is the load-bearing assumption in the first equation.

The smaller lesson I want to keep is the plan-versus-policy one, because it applies to deployment generally. A validated model is a plan: it specifies behaviour on the distribution it was tested against. A policy specifies behaviour **everywhere**, including states nobody intended to reach: the unusual presentation, the corrupted study, the patient outside the inclusion criteria. Most deployed systems have a plan and are asked to function as a policy, and the states where that gap matters are precisely the ones the validation set did not contain.

---

[^ago]: Silver, D., et al. (2016). Mastering the game of Go with deep neural networks and tree search. *Nature*, 529, 484–489. [10.1038/nature16961](https://doi.org/10.1038/nature16961)

[^guide]: Gottesman, O., et al. (2019). Guidelines for reinforcement learning in healthcare. *Nature Medicine*, 25, 16–18. [10.1038/s41591-018-0310-5](https://doi.org/10.1038/s41591-018-0310-5)

[^sepsis]: Komorowski, M., Celi, L. A., Badawi, O., Gordon, A. C., & Faisal, A. A. (2018). The Artificial Intelligence Clinician learns optimal treatment strategies for sepsis in intensive care. *Nature Medicine*, 24, 1716–1720. [10.1038/s41591-018-0213-5](https://doi.org/10.1038/s41591-018-0213-5)
