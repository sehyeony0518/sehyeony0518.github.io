---
layout: study_note
title: "The Combinatorial Explosion, and Why Pruning Alone Is Not Enough"
description: "Exponential search trees, learned pruning, policy proposals, and value functions: deriving computation costs and the decision errors caused by omitted actions and approximate leaf evaluation."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "decision-and-control"
category_title: "Decision Making & Reinforcement Learning"
subgroup: "Tree Search & Learned Pruning"
order: 3
source: "Independent study"
written: true
updated: "2026-09-15"
---

A search problem becomes combinatorial when choices multiply across decision stages. Learning can help by proposing useful actions, evaluating incomplete solutions, or identifying reusable structure. It does not change the arithmetic of exhaustive enumeration.

Two corrections are necessary. Modern planning systems still search. Learned guidance changes where they search and how they evaluate the frontier. Also, separate policy and value networks are not mathematically required: one network can provide both outputs, and useful search can use neither.

The important question is what each approximation saves and which possibilities or guarantees it removes. Width restriction, depth truncation, adaptive sampling, and state merging have different computational effects and different failure modes.

## Counting a complete search tree

Construct a tree in which every nonterminal node has the same branching factor and every path has the same depth.

There is one root. At depth one there are as many nodes as actions. Each additional level multiplies the count again. Thus the number of leaves is

$$
L_D=b^D.
$$

The total number of nodes, including the root, is

$$
S_D=1+b+b^2+\cdots+b^D.
$$

Multiply by the branching factor:

$$
bS_D=b+b^2+\cdots+b^{D+1}.
$$

Subtract the original sum:

$$
(b-1)S_D=b^{D+1}-1.
$$

Therefore, for a branching factor different from one,

$$
S_D=\frac{b^{D+1}-1}{b-1}.
$$

When the branching factor is one, the tree is a single path with one more node than its depth.

These are counts for a constructed regular tree. Real planning problems have changing action sets, early termination, repeated states, and impossible action sequences. Substituting an informal average branching factor can be a rough estimate, but it is not an exact count of legal trajectories.

The distinction matters because an impressive exponent can obscure the assumptions that produced it.

## Width, depth, and an explicit computation budget

Consider four entirely constructed trees:

| Branching factor | Depth | Leaves | Total nodes |
|---|---|---|---|
| $$20$$ | $$10$$ | $$10{,}240{,}000{,}000{,}000$$ | $$10{,}778{,}947{,}368{,}421$$ |
| $$6$$ | $$20$$ | $$3{,}656{,}158{,}440{,}062{,}976$$ | $$4{,}387{,}390{,}128{,}075{,}571$$ |
| $$6$$ | $$10$$ | $$60{,}466{,}176$$ | $$72{,}559{,}411$$ |
| $$5$$ | $$8$$ | $$390{,}625$$ | $$488{,}281$$ |

None of these rows is intrinsically tractable or intractable. Feasibility depends on the cost of generating states, evaluating leaves, storing nodes, and communicating with the environment.

For illustration, assume each leaf evaluation costs exactly ten microseconds and ignore every other cost. The evaluation rate is then

$$
10^5\ \text{leaves per second}.
$$

The depth-ten tree with six children per node requires

$$
\frac{60{,}466{,}176}{10^5}
=
604.66176\ \text{seconds}.
$$

The depth-eight tree with five children per node requires

$$
\frac{390{,}625}{10^5}
=
3.90625\ \text{seconds}.
$$

These are arithmetic consequences of an assumed cost, not measured timings.

Memory can impose a different limit. A method that stores every node pays for the total-node count, while depth-first enumeration can reuse memory along a path. Reducing memory does not eliminate the number of leaves evaluated.

A useful budget model is therefore

$$
C
\approx
c_{\mathrm{expand}}N_{\mathrm{expanded}}
+
c_{\mathrm{evaluate}}N_{\mathrm{evaluated}},
$$

with a separate memory constraint. Comparing algorithms only through leaf counts can miss an expensive learned evaluator or a costly simulator reset.

## Why faster hardware buys additive depth

Suppose exhaustive leaf evaluation dominates cost and hardware provides a speedup factor. The extra affordable depth satisfies

$$
b^{D+\Delta D}\leq F b^D.
$$

Canceling the original leaf count gives

$$
b^{\Delta D}\leq F,
$$

so

$$
\Delta D\leq\frac{\log F}{\log b}.
$$

The gain in searchable depth is logarithmic in the speedup.

With a branching factor of twenty, one additional full level requires a twenty-fold speedup. Expressed in doublings, that is

$$
\log_2 20\approx4.3219.
$$

No calendar assumption is needed. Converting this to years would require an explicit hardware-progress model, which is not a law of the search problem.

The comparison also changes when faster hardware makes a different algorithm possible. Training a useful proposal function is not equivalent to running the same exhaustive tree faster. It changes the computations performed.

This is why compute can be decisive in practice without making the exponential enumeration itself disappear.

## Histories are not always distinct states

A search tree distinguishes action histories. Dynamic programming can merge histories that reach the same sufficient state with the same remaining horizon.

Construct a layered deterministic problem with eight decisions, five actions per state, and at most three distinct states at every layer after the root. The number of action sequences is still

$$
5^8=390{,}625.
$$

But the number of distinct state-time pairs is at most

$$
1+3(8)=25.
$$

Only the root and the first seven subsequent layers have outgoing actions, so at most

$$
5\bigl(1+3(7)\bigr)=110
$$

state-action transitions need evaluation in a backward dynamic program.

This saving is possible because the continuation value depends on the merged state and remaining time, not on the path used to reach it.

If an omitted history variable changes future feasibility or reward, the merge is invalid. Examples include remaining fuel, a previously visited location that cannot be revisited, or a rule triggered by repeated positions.

For a finite-horizon deterministic model with a bounded number of states and actions per layer, backward evaluation scales with the number of state-action pairs. If every action has a distribution over many successors, summing those successor values adds another cost.

The exponential number of histories is therefore not itself a proof that every solution method must take exponential time. The problem may have reusable structure.

## Separability can remove enumeration entirely

Consider a score that adds independent contributions from each decision:

$$
F(a_1,\ldots,a_D)
=
\sum_{t=1}^{D}f_t(a_t).
$$

For any joint choice,

$$
\sum_t f_t(a_t)
\leq
\sum_t\max_a f_t(a).
$$

Now choose, independently at each stage, an action achieving that stage's maximum. This joint choice attains the right-hand side. Hence

$$
\max_{a_1,\ldots,a_D}
\sum_t f_t(a_t)
=
\sum_t\max_a f_t(a).
$$

The apparent search over exponentially many combinations becomes a collection of independent maximizations.

The equality fails when constraints couple decisions. A total resource budget, for example, can make the individually best choices jointly infeasible. Dynamic programming may still help by including the remaining budget in the state.

This distinction is useful when reading claims about combinatorial difficulty. Before learning a pruning rule, ask whether factorization, symmetry, dynamic programming, or an exact bound already removes much of the search.

A learned method should be compared with the structured problem, rather than only with naive enumeration.

## Four different ways to spend less search

Hard pruning removes actions from consideration. A top-ranked candidate set defines a restricted action space at every visited state.

Soft guidance assigns different priorities or sampling probabilities while retaining actions as possibilities. Under a finite budget, a very small probability can still make an action effectively absent.

Depth truncation replaces unresolved continuations with an evaluation function. The method saves future expansion by estimating its result.

Adaptive allocation, as in [Monte Carlo tree search](/study/monte-carlo-tree-search/), expands some branches more deeply or more often than others. Its tree is generally asymmetric.

These mechanisms can be combined, but their guarantees should not be exchanged. A positive prior is not an admissible bound. A value estimate is not proof that an omitted branch is poor. A larger visit count is not proof that a candidate generator included the best action.

A policy function and a value function are useful conceptual roles. They may be two heads of a shared model, separate models, hand-designed functions, or outcomes of additional search. The mathematics does not require a particular network count.

## Measuring what hard pruning discards

Let the original legal-action set be

$$
\mathcal A(s),
$$

and the retained nonempty set be

$$
K(s)\subseteq\mathcal A(s).
$$

Suppose the original problem has optimal value and action-value functions. Define the one-step omission loss by

$$
\delta(s)
=
\max_{a\in\mathcal A(s)}Q^*(s,a)
-
\max_{a\in K(s)}Q^*(s,a).
$$

This is not the probability mass removed by a policy model. It measures the value of the best action made unavailable.

The distinction can be large. Construct a one-step problem with two actions. A proposal model assigns probability almost one to an action worth one, and a very small probability to an action worth one thousand. Removing the second action discards very little proposal mass but loses

$$
1000-1=999
$$

units of achievable value.

A probability distribution trained to imitate frequent choices does not automatically assign mass in proportion to decision value. Low-frequency actions can matter greatly.

Evaluating omission loss directly requires information about excluded actions, which defeats some of the purpose of pruning. This does not make the definition useless. It identifies what a surrogate metric is trying to control and where its assumptions enter.

## A bound on repeated pruning loss

Let the restricted optimal value be

$$
V^K,
$$

and define the restricted Bellman operator

$$
(T_KV)(s)
=
\max_{a\in K(s)}
\left[
R(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V(s')
\right].
$$

Assume the one-step omission loss is uniformly bounded:

$$
0\leq\delta(s)\leq\varepsilon_p.
$$

Because the restricted operator evaluates the original optimal continuation,

$$
V^*(s)-(T_KV^*)(s)=\delta(s).
$$

Insert this intermediate value:

$$
V^*-V^K
=
V^*-T_KV^*
+
T_KV^*-T_KV^K.
$$

The same maximum-and-expectation argument used for the ordinary Bellman operator gives

$$
\lVert T_KV-T_KW\rVert_\infty
\leq
\gamma\lVert V-W\rVert_\infty.
$$

Therefore,

$$
\lVert V^*-V^K\rVert_\infty
\leq
\varepsilon_p
+
\gamma\lVert V^*-V^K\rVert_\infty,
$$

and

$$
\lVert V^*-V^K\rVert_\infty
\leq
\frac{\varepsilon_p}{1-\gamma}.
$$

Small local omissions can accumulate over repeated decisions.

The bound can be attained. Construct a single-state problem in which both actions return to the same state. One pays one per step, the other pays nine-tenths. Set the discount factor to nine-tenths and retain only the second action.

Then

$$
V^*=\frac1{1-0.9}=10,
$$

$$
V^K=\frac{0.9}{1-0.9}=9.
$$

Under the original optimal continuation, the retained action has value

$$
Q^*(s,\text{retained})=0.9+0.9(10)=9.9.
$$

Thus the local omission loss is one-tenth, while total loss is one:

$$
V^*-V^K
=
1
=
\frac{0.1}{1-0.9}.
$$

This example distinguishes a small per-decision error from a small total policy error.

## Candidate recall and path survival

For a task where the final answer must be selected from a generated candidate set, success requires that the correct answer enter that set. The probability factorization is

$$
\Pr(\text{correct final answer})
=
\Pr(\text{correct answer included})
\Pr(\text{correct final answer}\mid\text{included}).
$$

Construct one hundred cases. The correct answer appears in eighty candidate sets. The downstream selector succeeds in sixty of those eighty cases.

Then candidate inclusion is four-fifths, conditional selection accuracy is three-quarters, and total accuracy is

$$
\frac{80}{100}\frac{60}{80}
=
\frac{60}{100}.
$$

Reporting only the conditional selector score hides the twenty cases that were impossible to solve after candidate generation.

Sequential pruning has an analogous multiplication. Let the conditional probability that a designated good path survives the next pruning decision be

$$
c_t
=
\Pr(\text{survive step }t
\mid
\text{survived all earlier steps}).
$$

The chain rule gives

$$
\Pr(\text{path survives all }D\text{ steps})
=
\prod_{t=1}^{D}c_t.
$$

No independence assumption is needed because these are conditional probabilities.

If each conditional survival probability is constructed to be ninety-five percent, then survival over twenty decisions is

$$
0.95^{20}\approx0.3585.
$$

If each is ninety-nine percent over one hundred decisions, survival is

$$
0.99^{100}\approx0.3660.
$$

These calculations concern one designated path. A problem may have many acceptable paths, so losing one does not necessarily imply failure. The relevant event is losing all sufficiently good alternatives.

## What a leaf-value error does to the root decision

Now assume exact dynamics and exact maximization over a fixed legal-action set. Let the leaf evaluator approximate the desired continuation value uniformly:

$$
\lVert\widehat V-V\rVert_\infty\leq\varepsilon.
$$

Each Bellman backup shrinks maximum error by the discount factor. After a specified number of transitions,

$$
\lVert T^H\widehat V-T^H V\rVert_\infty
\leq
\gamma^H\varepsilon.
$$

This follows by applying the one-step contraction repeatedly. It is the formal reason deeper exact search can reduce the effect of bounded leaf error.

Suppose each estimated root action value has error at most

$$
\eta.
$$

Let the true best action be

$$
a^*,
$$

and let the action maximizing the estimates be

$$
\widehat a.
$$

Insert the two estimates between the true values:

$$
\begin{aligned}
Q(a^*)-Q(\widehat a)
&=
Q(a^*)-\widehat Q(a^*)\\
&\quad+
\widehat Q(a^*)-\widehat Q(\widehat a)\\
&\quad+
\widehat Q(\widehat a)-Q(\widehat a).
\end{aligned}
$$

The middle term is nonpositive because the selected action maximizes the estimate. Each remaining term is at most the error bound, giving

$$
Q(a^*)-Q(\widehat a)\leq2\eta.
$$

For a numerical construction, let two true values be

$$
5,\qquad4.7,
$$

and their estimates be

$$
4.8,\qquad4.9.
$$

Both errors have magnitude two-tenths. The wrong action is selected, losing three-tenths, which respects the bound of four-tenths.

A true action gap strictly larger than twice the error bound cannot be reversed. A small value error can therefore be harmless at a large-gap decision and decisive near a tie.

## Combining candidate and evaluation errors

The previous bounds control different losses. Pruning changes the best achievable policy. Evaluation error can then cause mistakes within the retained action set.

Suppose estimated restricted action values satisfy

$$
\lVert\widehat Q-Q^K\rVert_\infty\leq\eta,
$$

and a policy greedily selects among retained actions using those estimates.

At every state, its selected action loses at most twice the estimation bound relative to the restricted optimum. If it repeats such selections, the value difference satisfies

$$
\lVert V^K-V^{\widehat\pi}\rVert_\infty
\leq
2\eta
+
\gamma\lVert V^K-V^{\widehat\pi}\rVert_\infty.
$$

Thus,

$$
\lVert V^K-V^{\widehat\pi}\rVert_\infty
\leq
\frac{2\eta}{1-\gamma}.
$$

Combining with the pruning bound yields

$$
\lVert V^*-V^{\widehat\pi}\rVert_\infty
\leq
\frac{\varepsilon_p+2\eta}{1-\gamma}.
$$

The assumptions are demanding: uniform errors, correct dynamics, and action values targeting the restricted optimal continuation. An approximate finite-budget search does not acquire this guarantee merely because it uses a policy and a value network.

Still, the decomposition is useful. Better leaf evaluation cannot recover an action that has been removed. Better candidate recall cannot repair systematically wrong comparisons among the retained actions.

## Certified pruning and beam-search counterexamples

Pruning can preserve optimality when it uses valid bounds. For a maximization problem, suppose a completed feasible solution gives a lower bound on the optimum,

$$
L,
$$

and every completion of a branch has value at most

$$
U.
$$

If

$$
U\leq L,
$$

the branch cannot improve the incumbent and may be discarded.

Construct a branch with accumulated reward three and a certified maximum remaining reward four. Its upper bound is seven. If a completed solution already achieves eight, pruning this branch is safe.

A learned prediction that the branch is worth six is not the same certificate. The distinction is whether the estimate bounds every feasible continuation.

Beam search gives a simple example of unsafe prefix pruning. Suppose first-step token probabilities are

$$
P(A)=0.6,\qquad P(B)=0.4.
$$

The best second-token conditional probabilities are

$$
\max_x P(x\mid A)=0.5,
$$

$$
\max_x P(x\mid B)=0.9.
$$

A beam of width one retains A. But the best complete sequence under A has probability

$$
0.6(0.5)=0.3,
$$

while the best sequence under B has probability

$$
0.4(0.9)=0.36.
$$

A better prefix score did not imply a better completed sequence.

The computational saving is real. The lost guarantee is also real. A study of learned pruning should quantify both.

## Revision checklist

| Check | What I should be able to reconstruct |
|---|---|
| Enumeration | Derive both the leaf count and total-node geometric sum. |
| Cost assumptions | Convert node or leaf counts into time only after specifying a cost model. |
| Hardware scaling | Derive the logarithmic gain in affordable depth. |
| State merging | Explain when many histories share one valid continuation value. |
| Separability | Prove when independent maximization replaces enumeration. |
| Pruning loss | Define omission through action value rather than removed proposal mass. |
| Accumulation | Recover the bound $$\varepsilon_p/(1-\gamma)$$ and its one-state equality example. |
| Candidate evaluation | Factor total success into inclusion and conditional selection. |
| Path survival | Use conditional probabilities without assuming independence. |
| Leaf evaluation | Derive root action loss bounded by twice the value-estimation error. |
| Repeated decisions | Explain the additional horizon factor when approximate choices recur. |
| Safe pruning | Distinguish a certified upper bound from a learned point estimate. |

## Why it matters for my work

A diagnostic shortlist or retrieval stage limits what a downstream system can recover. I should evaluate candidate inclusion separately from ranking quality and inspect cases that disappear before the final decision.

The useful lesson is to account for information lost at each stage. Calling the overall system accurate does not identify whether its weakest part is proposal generation, evaluation, or decision selection.

## What I have not resolved

I have not established which candidate-generation errors matter most under the intended downstream costs. Inclusion of one reference answer may be an inadequate target when several alternatives remain clinically plausible.

Define acceptable candidate sets and measure inclusion, conditional selection, and total task performance on the same held-out cases.
