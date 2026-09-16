---
layout: study_note
title: "MDPs and the Simulator Problem: Every RL Paper Starts After the Hard Part"
description: "The Markov decision process five-tuple, Bellman equations, plans versus policies, and how simulator error and off-policy coverage affect reinforcement learning."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "decision-and-control"
category_title: "Decision Making & Reinforcement Learning"
subgroup: "Environments & Policies"
order: 1
source: "Independent study"
written: true
updated: "2026-09-15"
---

An MDP specifies a sequential decision problem. It does not imply that the learner knows the transition probabilities, possesses a simulator, or must estimate a complete transition model before learning.

That distinction corrects an overstatement suggested by this note's title. Reinforcement learning can use direct interaction with a physical system, a simulator, or previously collected trajectories. Each interface supplies different information and permits different experiments. A simulator is especially useful because it can make repeated, counterfactual interaction affordable. Its availability and fidelity are assumptions to examine, rather than requirements built into the definition of RL.

The mathematical task is to connect four objects: a state representation, a policy, its expected return, and the evidence available for estimating that return.

## What the five-tuple specifies

For a finite discounted problem, write

$$
\mathcal M=(\mathcal S,\mathcal A,P,R,\gamma),
\qquad 0\leq\gamma<1.
$$

The state and action spaces describe what the decision-maker can distinguish and choose. The transition kernel specifies

$$
P(s'\mid s,a)
=
\Pr(S_{t+1}=s'\mid S_t=s,A_t=a).
$$

Here the reward function denotes an expected immediate reward:

$$
R(s,a)
=
\mathbb E[R_{t+1}\mid S_t=s,A_t=a].
$$

A more complete specification gives the joint distribution of next state and reward,

$$
p(s',r\mid s,a),
$$

from which both quantities follow by marginalization. This matters when reward and next state are correlated. Replacing the reward distribution with its mean preserves expected-return calculations, but it does not preserve the full distribution of returns or every risk-sensitive objective.

An initial-state distribution is also needed to define an overall performance number. For a policy with state values, the evaluation target is

$$
J(\pi)
=
\mathbb E_{S_0\sim\rho_0}[V^\pi(S_0)].
$$

Two evaluations can use the same MDP and policy but report different performance because they start from different states.

The Markov assumption is a statement about information:

$$
\Pr(S_{t+1},R_{t+1}\mid H_t,A_t)
=
\Pr(S_{t+1},R_{t+1}\mid S_t,A_t),
$$

where the history contains all previous observations, actions, and rewards. The chosen state must retain everything from that history that affects the next-step distribution under an action.

Calling a vector a state does not establish this property. A cart's position alone is insufficient if velocity affects its next position. Two carts at the same position but moving in opposite directions have different next-state distributions under the same force.

Finite-horizon problems introduce another subtlety. The best action with one decision remaining can differ from the best action with many decisions remaining. Either index the policy by time or include remaining time in the state. A stationary policy over an incomplete state description can otherwise hide a time dependence.

## Observations, hidden states, and beliefs

An observation need not be a Markov state. Suppose a machine displays the same temperature when its internal component is healthy or damaged. Under heavy use, a healthy component survives and a damaged component fails. Temperature alone cannot determine the next-state distribution.

One remedy is to maintain a probability distribution over hidden states. Let

$$
b_t(s)=\Pr(S_t=s\mid H_t).
$$

After choosing an action, first predict the next hidden state:

$$
\widetilde b_{t+1}(s')
=
\sum_s P(s'\mid s,a_t)b_t(s).
$$

Then incorporate the new observation using its likelihood:

$$
b_{t+1}(s')
=
\frac{
O(o_{t+1}\mid s',a_t)\widetilde b_{t+1}(s')
}{
\sum_z O(o_{t+1}\mid z,a_t)\widetilde b_{t+1}(z)
}.
$$

The first step is the law of total probability. The second is Bayes' rule. The denominator makes the probabilities sum to one.

Under a correctly specified partially observed model, this belief is a sufficient summary of the history for future decisions. That does not make the problem cheap. A distribution over hidden states can be much larger than the original observation, and updating it requires a model.

The practical question is therefore not simply whether an algorithm accepts a state vector. It is whether the available representation preserves the distinctions on which useful decisions depend.

## Plans, policies, and objectives

An open-loop plan is a sequence of actions chosen before the intervening outcomes are observed. A Markov policy specifies an action distribution conditional on the current state:

$$
\pi(a\mid s).
$$

A contingent plan can itself represent a policy over a finite horizon. The useful distinction is between committing to actions regardless of observations and conditioning later decisions on what actually happens.

A policy being defined at every state also does not make it reliable at every state. A neural policy may return an action for an unfamiliar input while having no evidence that the action is useful.

To compare policies, define the return

$$
G_t
=
\sum_{k=0}^{\infty}\gamma^k R_{t+k+1}.
$$

If rewards satisfy

$$
\lvert R_{t+1}\rvert\leq R_{\max},
$$

then

$$
\lvert G_t\rvert
\leq
R_{\max}\sum_{k=0}^{\infty}\gamma^k
=
\frac{R_{\max}}{1-\gamma}.
$$

Discounting therefore ensures a finite bound even when interaction continues indefinitely.

There is also a probabilistic interpretation. Imagine that continuation after each reward occurs independently with probability equal to the discount factor. The probability of reaching the reward at offset equal to an integer is the corresponding power of that factor. Expected undiscounted reward before this random termination equals discounted return. This explains the geometric weights, but it does not establish that a particular application's true objective should use them.

Expected return also encodes a risk preference. Construct a one-step decision with two actions. A safe action gives a reward of four. A risky action gives ten with probability three-fifths and negative ten otherwise:

$$
\mathbb E[R\mid\text{risky}]
=
\frac35(10)+\frac25(-10)
=
2.
$$

Expected-return maximization chooses the safe action. If the success probability changes to four-fifths, the risky action's expectation becomes six and the ranking reverses. Whether that choice is acceptable depends on the objective, not on the MDP formalism alone.

## Deriving the Bellman expectation equation

Define the state value as

$$
V^\pi(s)
=
\mathbb E_\pi[G_t\mid S_t=s].
$$

Split the first reward from the return:

$$
\begin{aligned}
G_t
&=
R_{t+1}
+
\sum_{k=1}^{\infty}\gamma^k R_{t+k+1}\\
&=
R_{t+1}
+
\gamma
\sum_{j=0}^{\infty}\gamma^j R_{t+j+2}\\
&=
R_{t+1}+\gamma G_{t+1}.
\end{aligned}
$$

The reindexing in the second line is the step that makes a whole future expressible through one next-state value.

Condition first on the selected action and then on the next state:

$$
V^\pi(s)
=
\sum_a\pi(a\mid s)
\left[
R(s,a)
+
\gamma\sum_{s'}P(s'\mid s,a)V^\pi(s')
\right].
$$

The Markov property and stationary policy let the conditional expectation of the remaining return become the same value function evaluated at the next state.

Similarly, define the value of committing to an action once and following the policy afterward:

$$
Q^\pi(s,a)
=
R(s,a)
+
\gamma\sum_{s'}P(s'\mid s,a)V^\pi(s').
$$

Consequently,

$$
V^\pi(s)=\sum_a\pi(a\mid s)Q^\pi(s,a).
$$

These are expectation identities. They do not require that the learner know the quantities on their right-hand sides.

For a finite state space, collect policy-averaged rewards and transitions into a vector and matrix:

$$
r_\pi(s)=\sum_a\pi(a\mid s)R(s,a),
$$

$$
P_\pi(s,s')
=
\sum_a\pi(a\mid s)P(s'\mid s,a).
$$

Then policy evaluation becomes

$$
V^\pi=r_\pi+\gamma P_\pi V^\pi,
$$

and hence

$$
V^\pi=(I-\gamma P_\pi)^{-1}r_\pi.
$$

The inverse has a useful expansion:

$$
(I-\gamma P_\pi)^{-1}
=
\sum_{k=0}^{\infty}\gamma^kP_\pi^k.
$$

To check it, multiply a finite partial sum by the matrix on the left. Every intermediate term cancels, leaving

$$
I-\gamma^{n+1}P_\pi^{n+1}.
$$

The final term vanishes as the number of terms grows because a stochastic matrix does not increase the maximum absolute component and the discount powers approach zero.

The inverse therefore sums expected rewards after zero, one, two, and all subsequent transitions. It is an algebraic representation of the original return.

## A two-state MDP solved completely

Construct a machine with two states: free and congested. All probabilities and rewards below are definitions of this example.

| State | Action | Immediate reward | Next state |
|---|---|---|---|
| Free | Serve | $$2$$ | Free with probability $$1/2$$, congested otherwise |
| Free | Idle | $$0$$ | Free |
| Congested | Repair | $$-1$$ | Free |
| Congested | Wait | $$0$$ | Congested |

Set

$$
\gamma=\frac9{10}.
$$

Consider the policy that serves when free and repairs when congested. Abbreviate its two values by subscripts indicating the state:

$$
V_F
=
2+\frac9{20}V_F+\frac9{20}V_C,
$$

$$
V_C=-1+\frac9{10}V_F.
$$

Substitution gives

$$
\begin{aligned}
V_F
&=
2+\frac9{20}V_F
+\frac9{20}\left(-1+\frac9{10}V_F\right)\\
&=
\frac{31}{20}+\frac{171}{200}V_F.
\end{aligned}
$$

Therefore,

$$
V_F
=
\frac{310}{29}
\approx10.6897,
\qquad
V_C
=
\frac{250}{29}
\approx8.6207.
$$

To check whether the policy is optimal, evaluate the alternative action in each state while following the candidate policy afterward:

$$
Q^\pi(F,\text{idle})
=
\frac9{10}\frac{310}{29}
=
\frac{279}{29}
<
\frac{310}{29},
$$

$$
Q^\pi(C,\text{wait})
=
\frac9{10}\frac{250}{29}
=
\frac{225}{29}
<
\frac{250}{29}.
$$

Neither one-step deviation improves the value.

The initially unattractive repair action is essential. A policy that maximizes immediate reward waits forever when congested, giving that state value zero. Its free-state value satisfies

$$
V_F=2+\frac9{20}V_F,
$$

so

$$
V_F=\frac{40}{11}\approx3.6364.
$$

The cost of repairing is visible immediately. Its benefit appears through future opportunities to serve. The Bellman equation makes that trade explicit.

## Why value iteration converges

Define the optimality operator

$$
(TV)(s)
=
\max_a
\left[
R(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V(s')
\right].
$$

For any two collections of numbers,

$$
\left\lvert\max_a x_a-\max_a y_a\right\rvert
\leq
\max_a\lvert x_a-y_a\rvert.
$$

To see why, take an action maximizing the first collection. Its advantage over the maximum of the second collection cannot exceed its advantage over the second collection's value at that same action. Reverse the collections to obtain the absolute-value bound.

Applying this fact gives

$$
\begin{aligned}
\lVert TV-TW\rVert_\infty
&\leq
\gamma
\max_{s,a}
\sum_{s'}P(s'\mid s,a)
\lvert V(s')-W(s')\rvert\\
&\leq
\gamma\lVert V-W\rVert_\infty.
\end{aligned}
$$

Thus each update shrinks the maximum discrepancy by at least the discount factor. Iterating from any bounded initial vector converges to a unique fixed point.

In the constructed machine, starting from zero gives

$$
(V_F^{(1)},V_C^{(1)})=(2,0),
$$

$$
(V_F^{(2)},V_C^{(2)})=(2.9,0.8),
$$

$$
(V_F^{(3)},V_C^{(3)})=(3.665,1.61).
$$

The repair action becomes attractive only after value has propagated backward from the free state.

A computable stopping certificate follows from the same inequality:

$$
\begin{aligned}
\lVert V-V^*\rVert_\infty
&\leq
\lVert V-TV\rVert_\infty
+
\lVert TV-TV^*\rVert_\infty\\
&\leq
\lVert V-TV\rVert_\infty
+
\gamma\lVert V-V^*\rVert_\infty.
\end{aligned}
$$

Rearranging,

$$
\lVert V-V^*\rVert_\infty
\leq
\frac{\lVert V-TV\rVert_\infty}{1-\gamma}.
$$

A small change in an algorithm's parameters is not this certificate. The relevant residual measures violation of the Bellman equation.

## What access to an environment actually means

An explicit model allows summation over possible successors. A generative simulator instead returns a sampled reward and next state for a requested state-action pair. A physical interaction stream usually reveals only the successor of the current state. A logged dataset permits no new queries.

These distinctions explain why two algorithms described as model-free may have very different data requirements. Model-free means that the algorithm need not explicitly estimate transition dynamics. It does not mean that its training data appeared without an environment.

Likewise, numerical simulation does not require linearizing a nonlinear physical model. One can integrate the nonlinear equations directly. Linearization is useful for local analysis and controller design, with its own approximation error, as derived in the [pendulum note](/study/linearization-and-the-inverted-pendulum/).

A faithful simulator also need not be computationally free. Search quality depends on how many useful queries fit within the available time, and on whether the simulator can be reset to the states the search requests.

## How transition error becomes value error

Compare a true model with an approximate model under the same policy. Assume uniform bounds

$$
\lvert R(s,a)-\widehat R(s,a)\rvert\leq\varepsilon_r,
$$

$$
\sum_{s'}
\lvert P(s'\mid s,a)-\widehat P(s'\mid s,a)\rvert
\leq\varepsilon_p.
$$

The transition bound uses the full sum of absolute differences, rather than half that sum.

Let the maximum absolute value discrepancy be

$$
\Delta=\lVert V^\pi-\widehat V^\pi\rVert_\infty.
$$

Subtract the Bellman equations and insert an intermediate term using the true transition matrix and approximate value:

$$
V^\pi-\widehat V^\pi
=
r_\pi-\widehat r_\pi
+
\gamma P_\pi(V^\pi-\widehat V^\pi)
+
\gamma(P_\pi-\widehat P_\pi)\widehat V^\pi.
$$

If both models have rewards bounded in magnitude by the same reward limit, then

$$
\Delta
\leq
\varepsilon_r
+
\gamma\Delta
+
\gamma\varepsilon_p\frac{R_{\max}}{1-\gamma}.
$$

Therefore,

$$
\Delta
\leq
\frac{\varepsilon_r}{1-\gamma}
+
\frac{\gamma\varepsilon_pR_{\max}}{(1-\gamma)^2}.
$$

One factor accounts for the amount of future reward exposed to a wrong transition. Another accounts for repeatedly encountering transition errors over time.

For a constructed bound with exact rewards,

$$
\gamma=0.9,\qquad
R_{\max}=2,\qquad
\varepsilon_p=0.01,
$$

the value-error bound is

$$
\Delta\leq\frac{0.9(0.01)(2)}{0.1^2}=1.8.
$$

This is a worst-case guarantee under uniform assumptions, not a prediction that the actual error will equal that number.

Suppose the same bound holds for every policy, and a policy is optimized in the approximate model. Its loss in the true model is at most twice the uniform value-error bound. Insert approximate-model values between the true optimal and selected-policy values. The approximate optimizer's comparison contributes a nonpositive term, leaving at most one model-error term for each policy.

Accurate simulation is therefore a decision-relevant requirement. Small average prediction error on frequently observed transitions does not automatically establish the uniform conditions used above.

## Logged data, coverage, and importance weights

For a finite trajectory, the probability under a policy factors into an initial-state probability, action probabilities, and environment transition-reward probabilities.

When target and behavior policies interact with the same environment, the environment factors cancel in their trajectory probability ratio:

$$
W(\tau)
=
\frac{p_\pi(\tau)}{p_\mu(\tau)}
=
\prod_{t=0}^{H-1}
\frac{\pi(a_t\mid s_t)}{\mu(a_t\mid s_t)}.
$$

Multiplying a behavior-policy expectation by this ratio gives

$$
\mathbb E_\mu[W(\tau)G(\tau)]
=
\sum_\tau p_\pi(\tau)G(\tau)
=
\mathbb E_\pi[G(\tau)].
$$

This requires coverage: every trajectory with positive target probability must have positive behavior probability.

A constructed four-step example shows the variance problem. The target always chooses a particular action. The behavior policy chooses that action with probability one-tenth at each step. Reward is a terminal success indicator, equal to one only if all four selected actions match the target.

The all-target trajectory has behavior probability

$$
(0.1)^4=10^{-4}
$$

and importance weight

$$
10^4.
$$

The weighted return is therefore ten thousand with probability one ten-thousandth and zero otherwise:

$$
\mathbb E_\mu[WG]=1,
$$

$$
\operatorname{Var}_\mu(WG)
=
10^{-4}(10^4)^2-1
=
9999.
$$

The estimator is unbiased and still extremely noisy. More sophisticated estimators can change this trade-off, but no estimator can recover unsupported action outcomes without additional assumptions.

Finally, observational action assignment may depend on hidden variables. The transition distribution conditional on a recorded action can then differ from the distribution caused by intervening to select that action. An MDP notation alone does not resolve that identification problem. Nor does every off-policy estimator require an explicit transition model.

## Revision checklist

| Check | What I should be able to reconstruct |
|---|---|
| State sufficiency | Explain why identical observations can conceal different next-state distributions. |
| Belief update | Perform prediction by total probability, then normalization by Bayes' rule. |
| Return recursion | Reindex the discounted sum to obtain the one-step Bellman equation. |
| Policy evaluation | Derive the matrix inverse and its geometric-series interpretation. |
| Worked MDP | Recover the values $$310/29$$ and $$250/29$$ and check both alternative actions. |
| Optimality | Derive the contraction inequality and Bellman-residual certificate. |
| Environment access | Distinguish a transition table, a generative simulator, interaction, and logs. |
| Simulator error | Recover both factors of the effective horizon in the transition-error bound. |
| Off-policy evaluation | Derive trajectory weights and the constructed variance of $$9999$$. |
| Causal interpretation | State the coverage and identification assumptions needed before comparing interventions. |

## Why it matters for my work

For decision support, the first question is what evidence makes alternative actions comparable. State sufficiency, action coverage, outcome definition, and observation timing come before selecting an RL algorithm.

I also want to separate a policy's mathematical definition from evidence about its behavior. Returning an action on every input is easy. Establishing useful behavior outside the observed states is a different task.

## What I have not resolved

For a concrete application, I have not established which history variables are needed for state sufficiency or which actions have adequate observational support.

Specify the proposed state, decision interval, reward horizon, behavior-policy coverage, and assumptions identifying action effects.
