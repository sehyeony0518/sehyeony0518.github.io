---
layout: study_note
title: "Monte Carlo Tree Search: Exploration, Exploitation, and the Cost of Never Looking"
description: "Why randomness earns a place inside a search algorithm, what the UCT formula is actually balancing, and the sense in which a fixed test suite is a policy that stopped exploring."
og_image: "https://sehyeony0518.github.io/assets/img/og/monte-carlo-tree-search.png"
tab: "ai-foundations"
tab_title: "AI Theory"
category: "decision-and-control"
category_title: "Decision Making & Reinforcement Learning"
subgroup: "Tree Search & Learned Pruning"
order: 2
source: "Independent study"
written: true
updated: "2026-09-15"
---

Monte Carlo tree search allocates a limited computation budget among possible future decisions. It builds a tree selectively, using previous simulation results to decide where the next simulation should go.

The central difficulty is that the search must estimate action quality while also choosing which action values to estimate. A branch with a poor sample mean might be bad, or it might simply be poorly measured. Spending every simulation on the current favorite prevents the algorithm from distinguishing those possibilities.

MCTS is a family of procedures, not a requirement to use uniformly random terminal rollouts. A leaf can be evaluated by a rollout, a learned value function, a domain-specific evaluator, or a combination. The mathematical interpretation depends on which of these supplies the evidence.

## The quantity stored on an edge

At a state-action edge, maintain a visit count and accumulated return:

$$
N(s,a),
\qquad
W(s,a).
$$

The estimated action value is

$$
Q(s,a)=\frac{W(s,a)}{N(s,a)}
$$

when the count is positive.

Why use a mean? If repeated simulations from an edge produce independent returns with a fixed common expectation, then

$$
\mathbb E\left[\frac1n\sum_{j=1}^n G_j\right]
=
\mathbb E[G_1].
$$

If their common variance is finite, independence gives

$$
\begin{aligned}
\operatorname{Var}\left(\frac1n\sum_{j=1}^nG_j\right)
&=
\frac1{n^2}
\sum_{j=1}^n\operatorname{Var}(G_j)\\
&=
\frac{\sigma^2}{n}.
\end{aligned}
$$

The standard deviation therefore decreases with the square root of the number of samples.

An actual tree search complicates this simple interpretation. Its policy below an edge changes as the tree expands. Early rollouts may follow a weak default policy, while later simulations use deeper search. Their returns need not be independent samples from one fixed distribution.

The sample mean remains a useful statistic, but a confidence interval justified for independent, stationary observations cannot be attached to it automatically.

For the bandit derivations below, assume returns are scaled to the interval

$$
[0,1].
$$

A win indicator satisfies this convention. A discounted sum of many rewards may not. Changing the reward scale requires changing the exploration scale as well.

## One simulation through the tree

A common MCTS iteration has four stages:

1. Select actions through the existing tree using a tree policy.
2. Expand an unrepresented action or successor.
3. Evaluate the resulting leaf.
4. Back up the resulting returns along the traversed path.

Implementations differ in whether they add one node, several nodes, or a collection of successors. The invariant is that the new evidence updates the decisions responsible for reaching it.

For a discounted problem, backup is a return recursion. Starting with a leaf estimate,

$$
G_H=\widehat V(s_H),
$$

work backward:

$$
G_t=r_{t+1}+\gamma G_{t+1}.
$$

Update the edge taken at each time with its own remaining return:

$$
N(s_t,a_t)\leftarrow N(s_t,a_t)+1,
$$

$$
W(s_t,a_t)\leftarrow W(s_t,a_t)+G_t.
$$

A constructed path makes the indexing visible. Let the three rewards be

$$
1,\quad -2,\quad 4,
$$

with discount factor one-half and zero value after the final reward. The backed-up returns are

$$
G_2=4,
$$

$$
G_1=-2+\frac12(4)=0,
$$

$$
G_0=1+\frac12(0)=1.
$$

Adding the same terminal total to every edge would be wrong here. Each edge sees a different remaining reward sequence.

In an undiscounted game with no intermediate rewards, copying a terminal result can be correct, provided its player perspective is handled consistently.

This backup has no derivatives. Its resemblance to neural-network backpropagation is that information travels backward along a computation path.

## Deriving the exploration bonus

First consider a simpler problem: a fixed bandit arm producing independent rewards in the unit interval. Let its mean be

$$
\mu,
$$

and its sample mean after a specified number of observations be

$$
\widehat\mu_n=\frac1n\sum_{j=1}^nX_j.
$$

The relevant question is how far the sample mean might underestimate the true mean.

A concentration bound can be derived through exponential moments. For a bounded random variable, define

$$
f(\lambda)=\log\mathbb E[e^{\lambda X}].
$$

Differentiating shows that the first derivative is a mean under exponentially reweighted probabilities, and the second derivative is a variance under those probabilities.

Any distribution supported on the unit interval has variance at most one-quarter. One way to check this is

$$
\operatorname{Var}(X)
=
\min_c\mathbb E[(X-c)^2]
\leq
\mathbb E[(X-\tfrac12)^2]
\leq
\frac14.
$$

The same support bound holds after exponential reweighting. Consequently,

$$
f''(\lambda)\leq\frac14.
$$

Since the value and derivative at zero are

$$
f(0)=0,
\qquad
f'(0)=\mu,
$$

integrating the second-derivative bound gives

$$
\log\mathbb E[e^{\lambda(X-\mu)}]
\leq
\frac{\lambda^2}{8}.
$$

Apply Markov's inequality to the exponential of the negative centered sum. For any positive parameter,

$$
\Pr(\mu-\widehat\mu_n\geq\varepsilon)
\leq
\exp\left(
-\lambda n\varepsilon+\frac{n\lambda^2}{8}
\right).
$$

Minimizing the exponent gives

$$
\lambda=4\varepsilon,
$$

and hence

$$
\Pr(\mu-\widehat\mu_n\geq\varepsilon)
\leq
e^{-2n\varepsilon^2}.
$$

To make this upper bound equal to a chosen failure probability, solve

$$
e^{-2n\varepsilon^2}=\delta.
$$

The resulting radius is

$$
\varepsilon
=
\sqrt{\frac{\log(1/\delta)}{2n}}.
$$

This explains both the square root and the inverse dependence on sample count.

If the confidence level becomes stricter as the total number of decisions grows, one possible choice is

$$
\delta=N^{-4}.
$$

Substitution produces

$$
\varepsilon
=
\sqrt{\frac{2\log N}{n}}.
$$

The logarithm is therefore not an arbitrary aesthetic choice. It comes from asking for increasingly reliable decisions while allowing the accumulated probabilities of bad estimation events to remain controlled.

## From UCB to UCT

The corresponding optimistic action score has the form

$$
U_i
=
\widehat\mu_i
+
c\sqrt{\frac{\log N}{n_i}}.
$$

The first term favors actions with high observed return. The second favors actions whose values remain uncertain.

UCT applies this pattern separately at nodes of a search tree:

$$
\operatorname{UCT}(s,a)
=
Q(s,a)
+
c\sqrt{\frac{\log N(s)}{N(s,a)}}.
$$

An unvisited action needs an explicit convention, commonly mandatory initial exploration or an infinite selection score. Direct substitution would divide by zero.

The constant depends on reward scaling and on which theoretical or practical variant is intended. The preceding stationary-bandit construction yields the familiar square-root-of-two coefficient. A tuned tree-search coefficient is not necessarily a literal confidence level.

There is also a limit to the derivation. Descendant policies change during tree search, so returns at a parent are generally nonstationary. The stationary concentration argument motivates the score's form. It does not, by itself, establish a finite-budget guarantee for an arbitrary MCTS implementation.

An exploration score can exceed one even when all returns lie between zero and one. It is a selection index, not a predicted win probability.

## A fully specified UCT calculation

Construct a parent with two actions. Action A has returned six ones and two zeros. Action B has returned one one and one zero.

Thus,

$$
N=10,
$$

$$
n_A=8,\quad W_A=6,\quad Q_A=0.75,
$$

$$
n_B=2,\quad W_B=1,\quad Q_B=0.5.
$$

Use an exploration coefficient of one for this illustrative update. The scores are

$$
U_A
=
0.75+\sqrt{\frac{\log10}{8}}
\approx1.2865,
$$

$$
U_B
=
0.5+\sqrt{\frac{\log10}{2}}
\approx1.5730.
$$

The search chooses B despite its lower sample mean.

Now construct the next simulation to return zero. After backup,

$$
N=11,\qquad n_B=3,\qquad W_B=1.
$$

Recomputing both scores gives

$$
U_A
=
0.75+\sqrt{\frac{\log11}{8}}
\approx1.2975,
$$

$$
U_B
=
\frac13+\sqrt{\frac{\log11}{3}}
\approx1.2274.
$$

The next selection switches to A.

Two effects occurred simultaneously. B's sample mean decreased, and its exploration bonus shrank because its count increased. A's bonus increased slightly because the parent acquired another visit while A did not.

This last behavior prevents a neglected child from becoming permanently invisible in ordinary UCT, provided its parent keeps receiving visits and the algorithm continues to consider that child.

## What the bandit regret calculation does and does not say

For a stationary bandit, define an arm's gap from the best mean as

$$
\Delta_i=\mu_*-\mu_i.
$$

The expected cumulative regret after a fixed number of pulls is

$$
\mathbb E[R_T]
=
\sum_i\Delta_i\,\mathbb E[n_i(T)].
$$

Each pull of a suboptimal arm contributes its mean gap, so collecting pulls by arm yields this expression.

The logarithmic intuition can be derived on events where all relevant confidence bounds hold. An optimistic score for the best arm is at least its true mean. A suboptimal arm's score is at most its true mean plus twice its confidence radius. Therefore, selecting the suboptimal arm requires

$$
\Delta_i
\leq
2\sqrt{\frac{2\log T}{n_i}}.
$$

Rearrangement gives

$$
n_i
\leq
\frac{8\log T}{\Delta_i^2}.
$$

This is the central counting argument. A complete regret proof must also account for initialization and failed confidence events.

The planning objective is different. Search simulations usually do not earn the reward that matters operationally. The real objective is the quality of the single action selected after search.

For a recommended action, simple regret is

$$
r_{\mathrm{simple}}
=
\mu_*-\mu_{\widehat a}.
$$

Low cumulative regret while gathering samples and low simple regret at the final recommendation are related but distinct goals. This is one reason to separate the tree's exploratory selection rule from its final action rule.

## Choosing the action after search

Common final rules choose the highest estimated value or the largest visit count. Neither should retain the exploration bonus unchanged: a large bonus means that an action is insufficiently measured, which is a reason to investigate it during search, not necessarily to execute it.

The most-visited rule uses the search's allocation history. It often favors an action that remained competitive across many iterations. It is not a universal guarantee that the most-visited action has the best true value.

For example, a poor prior, biased leaf evaluator, or misleading rollout policy can cause a bad action to receive many visits. Counts record computational attention. They do not independently certify correctness.

Similarly, a high sample mean based on very few visits is weak evidence. The relevant reporting habit is to retain the estimate, count, return scale, and evaluation procedure together.

A deterministic tie-breaking rule can also matter when budgets are very small. An implementation should specify it rather than allowing iteration order to act as an undocumented policy.

## Opponent decisions are not chance events

A search tree may contain different kinds of nodes.

At a chance node, successor outcomes are sampled or averaged according to their probabilities. Choosing the most favorable stochastic outcome would solve an imaginary problem in which the planner controls chance.

At an opponent node in a two-player zero-sum game, the opponent chooses an action. If values are measured from the root player's perspective, a fully solved opponent node takes a minimum.

An alternative convention stores values from the perspective of the player making each decision. Then the backup must reverse perspective when moving between players.

For outcomes represented as win probabilities, the reversal is

$$
z_{\mathrm{parent}}=1-z_{\mathrm{child}},
$$

with a draw represented by one-half. For signed outcomes, the reversal is negation.

Without this correction, every player in the tree may appear to cooperate with the root player.

Consider a constructed root decision. Action A guarantees a utility of six-tenths. Action B lets the opponent choose among ten replies: nine give the root player utility one, and one gives utility zero.

A uniformly random opponent rollout estimates

$$
V_{\mathrm{rollout}}(B)
=
\frac9{10}(1)+\frac1{10}(0)
=
0.9.
$$

An adversarial opponent instead gives

$$
V_{\mathrm{adversarial}}(B)=0.
$$

The safe action is better against that opponent, even though random rollouts favor B.

If independent uniform rollouts sample opponent replies, the probability of missing the refutation in every one of ten rollouts is

$$
(0.9)^{10}\approx0.3487.
$$

To reduce this miss probability below five percent requires

$$
(0.9)^n\leq0.05,
$$

so

$$
n
\geq
\frac{\log0.05}{\log0.9}.
$$

The smallest integer satisfying the condition is twenty-nine. This calculation applies to this constructed sampling rule. It is not a universal MCTS sample requirement.

## Learned priors and leaf evaluation

A learned policy can influence where the search spends simulations. One common prior-weighted index is

$$
Q(s,a)
+
c\,P_\theta(a\mid s)
\frac{\sqrt{N(s)}}{1+N(s,a)}.
$$

This is often called a PUCT-style rule. It differs mathematically from the logarithmic UCT bonus. A prior probability is not a posterior confidence interval for an action value.

An action with zero prior receives no bonus from this expression. Unless initialization, noise, or another mechanism forces exploration, the prior can make a useful action effectively unreachable within the budget.

A value function can replace a long continuation. For a depth-limited simulation,

$$
\widehat G_0
=
\sum_{t=0}^{H-1}\gamma^t r_{t+1}
+
\gamma^H\widehat V(s_H).
$$

Suppose the dynamics are correct and the leaf estimate approximates the same continuation policy's true value uniformly:

$$
\lvert\widehat V(s)-V(s)\rvert\leq\varepsilon.
$$

Then, conditional on the simulated prefix,

$$
\lvert\widehat G_0-G_0^{\mathrm{bootstrapped}}\rvert
\leq
\gamma^H\varepsilon.
$$

The return-prefix terms cancel, leaving only discounted leaf error.

This bound does not say that the continuation policy is optimal. Nor does increasing the number of simulations eliminate a systematic leaf-evaluation bias. More samples can estimate the biased target more precisely.

A mixture of rollout and learned evaluation should likewise be understood as a new estimator. If

$$
\widehat V_{\mathrm{mix}}
=
\alpha\widehat V_{\mathrm{network}}
+
(1-\alpha)\widehat V_{\mathrm{rollout}},
$$

its bias is the same weighted combination of the component biases. Its variance also includes their covariance. Combining two estimates is not automatically an improvement.

## Implementation checks that change the mathematics

Several apparently minor choices determine which problem the search solves.

A terminal state must use its actual terminal return, rather than an ordinary value-network prediction. A finite horizon must be counted consistently so that rewards are not omitted or discounted twice. Legal-action masks must be applied before selection and expansion.

A repeated physical state is not necessarily the same search state. Remaining time, player to move, repetition rules, or accumulated resources may change its future value. Sharing statistics across such states requires a valid state representation.

For stochastic environments, one action may have several successors. Edge statistics must average over the environment's outcome distribution. A tree that stores only the first observed successor as though it were deterministic introduces a model error.

Finally, reusing a tree after executing an action is useful only if the new root corresponds to the actual observed state. Retaining statistics from an incompatible simulated successor can silently turn saved computation into biased evidence.

These checks are part of the algorithm's definition. They cannot be repaired merely by increasing the simulation budget.

## Revision checklist

| Check | What I should be able to reconstruct |
|---|---|
| Edge statistics | Explain the meanings of visit count, accumulated return, and sample mean. |
| Discounted backup | Recover the path returns $$4$$, $$0$$, and $$1$$ in the constructed example. |
| Concentration | Derive the exponential tail bound from bounded exponential moments. |
| UCT shape | Explain the logarithm, square root, visit denominator, and unvisited-action convention. |
| Numerical selection | Reproduce the switch from B to A after the additional zero return. |
| Regret | Distinguish cumulative sampling regret from final-action simple regret. |
| Player perspective | Apply minimization or sign reversal consistently at opponent nodes. |
| Rollout bias | Explain why nine favorable replies do not neutralize one adversarial refutation. |
| Learned guidance | Distinguish prior-weighted allocation from a confidence bound. |
| Leaf error | Derive the discounted evaluation-error term and state its assumptions. |
| Implementation | Check terminal handling, horizon, chance outcomes, and state identity. |

## Why it matters for my work

The useful connection to model auditing is allocation of limited evaluation effort. Repeatedly testing familiar conditions can leave important alternatives unmeasured. Counts and sampling rules should accompany reported performance.

A benchmark is not literally a bandit policy with its exploration coefficient removed. The transferable principle is narrower: evidence depends on where measurement effort was allocated, including which conditions received none.

## What I have not resolved

I have not established when adaptive search for failure cases improves the final audit under a fixed budget, especially when candidate tests have different costs or dependent outcomes.

Compare audit allocation rules using a predefined evaluation budget, independent final assessment, and recorded discovery costs.
