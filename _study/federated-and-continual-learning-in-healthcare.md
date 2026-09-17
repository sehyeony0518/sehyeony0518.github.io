---
layout: study_note
title: "Federated and Continual Learning in Healthcare"
description: "Training across institutions that cannot share data, and updating a model without losing what it knew."
og_image: "https://sehyeony0518.github.io/assets/img/og/federated-and-continual-learning-in-healthcare.png"
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "systems"
category_title: "Medical AI Systems & Deployment"
subgroup: "Adaptation Across Sites & Time"
order: 4
source: "Independent study"
written: true
updated: "2026-09-08"
---

Federated learning distributes training across data holders. Continual learning updates capabilities over time. Their central difficulties concern different boundaries: institutional access in one case, retention across updates in the other.

## Core question and definition

The central question is:

> Which objective does collaboration optimize, what information leaves each institution, and which earlier capabilities must remain after an update?

A federated model can be trained once and frozen. A continually updated model can learn within one institution. Combining the two adds interactions between client participation, data heterogeneity, and temporal change.

Neither local data storage nor continued training establishes clinical validity, privacy, or useful retention. Each needs a specified target and evaluation.

## Key concepts

### 1. Derive the pooled objective represented by a federation

Suppose client $$k$$ holds $$n_k$$ training records and has empirical loss

$$
F_k(\theta)
=
\frac1{n_k}\sum_{i=1}^{n_k}
\ell(\theta;x_{ki},y_{ki}).
$$

Let

$$
n=\sum_kn_k.
$$

The loss on the pooled records is

$$
\begin{aligned}
F_{\mathrm{pool}}(\theta)
&=
\frac1n\sum_k\sum_i
\ell(\theta;x_{ki},y_{ki})\\
&=
\sum_k\frac{n_k}{n}
\left[
\frac1{n_k}\sum_i\ell(\theta;x_{ki},y_{ki})
\right]\\
&=
\boxed{\sum_kw_kF_k(\theta)},
\end{aligned}
$$

where

$$
w_k=\frac{n_k}{n}.
$$

Thus sample-count weighting defines the same empirical objective as pooling those records.

Equal client weighting,

$$
F_{\mathrm{site}}(\theta)=\frac1K\sum_kF_k(\theta),
$$

defines another objective. It gives each institution equal influence regardless of record count.

Neither weighting automatically represents clinical importance. If records are frames, sample-count weighting can also give patients with more frames more influence.

### 2. Define Federated Averaging precisely

In a basic full-participation round, the server distributes common parameters $$\theta_t$$.

Each client initializes

$$
\theta_{k,0}=\theta_t
$$

and performs $$E$$ local steps:

$$
\theta_{k,e+1}
=
\theta_{k,e}-\eta\nabla F_k(\theta_{k,e}).
$$

The server averages the resulting parameters:

$$
\boxed{
\theta_{t+1}
=
\sum_kw_k\theta_{k,E}.
}
$$

This is the central model-averaging structure of Federated Averaging. [Communication-Efficient Learning of Deep Networks from Decentralized Data](https://proceedings.mlr.press/v54/mcmahan17a.html).

Real protocols can use minibatches, partial participation, different local step counts, and additional state. Those choices are part of the algorithm.

Having the same nominal objective as pooled training does not imply following the same optimization trajectory.

### 3. One synchronized gradient step can equal pooled training

Set $$E=1$$ and use full local gradients from the common starting point:

$$
\theta_{k,1}
=
\theta_t-\eta\nabla F_k(\theta_t).
$$

Averaging,

$$
\begin{aligned}
\theta_{t+1}
&=
\sum_kw_k[
\theta_t-\eta\nabla F_k(\theta_t)
]\\
&=
\theta_t-\eta\sum_kw_k\nabla F_k(\theta_t)\\
&=
\boxed{
\theta_t-\eta\nabla F_{\mathrm{pool}}(\theta_t).
}
\end{aligned}
$$

This equality holds even when client distributions differ.

Therefore, “non-IID data make federation unequal to pooled training” is too broad. The usual difference arises because multiple local steps evaluate gradients at different client-specific parameter values.

With stochastic gradients, analogous equality can hold in expectation under appropriate sampling. Individual random trajectories need not coincide.

### 4. Derive where multiple local steps diverge

At a common starting point $$\theta$$, write

$$
g_k=\nabla F_k(\theta),
\qquad
H_k=\nabla^2F_k(\theta).
$$

For sufficiently smooth objectives and small step size, after one local step,

$$
\theta_{k,1}=\theta-\eta g_k.
$$

Taylor expansion gives

$$
\nabla F_k(\theta_{k,1})
=
g_k-\eta H_kg_k+O(\eta^2).
$$

A second local step therefore yields

$$
\begin{aligned}
\theta_{k,2}
&=
\theta-\eta g_k
-\eta[g_k-\eta H_kg_k+O(\eta^2)]\\
&=
\theta-2\eta g_k+\eta^2H_kg_k+O(\eta^3).
\end{aligned}
$$

Define

$$
\overline g=\sum_kw_kg_k,
\qquad
\overline H=\sum_kw_kH_k.
$$

Averaging the two-step local models gives

$$
\theta_{\mathrm{Fed}}
=
\theta-2\eta\overline g
+\eta^2\sum_kw_kH_kg_k
+O(\eta^3).
$$

Two pooled gradient steps instead give

$$
\theta_{\mathrm{pool}}
=
\theta-2\eta\overline g
+\eta^2\overline H\,\overline g
+O(\eta^3).
$$

Hence,

$$
\boxed{
\theta_{\mathrm{Fed}}-\theta_{\mathrm{pool}}
=
\eta^2
\left[
\sum_kw_kH_kg_k-\overline H\,\overline g
\right]
+O(\eta^3).
}
$$

The bracket equals

$$
\sum_kw_k(H_k-\overline H)(g_k-\overline g).
$$

Client-specific gradients and curvature determine the divergence. Heterogeneous data can create both, but inequality is not inevitable in every special case.

### 5. Carry a two-client example through every update

Construct scalar objectives

$$
F_1(\theta)=\frac12(\theta-1)^2,
$$

$$
F_2(\theta)=\frac32(\theta+1)^2,
$$

with equal client weights.

Their gradients are

$$
g_1(\theta)=\theta-1,
\qquad
g_2(\theta)=3(\theta+1).
$$

Start from

$$
\theta_0=0,
\qquad
\eta=\frac14.
$$

Client 1:

$$
\theta_{1,1}
=
0-\frac14(-1)
=
\frac14,
$$

$$
\theta_{1,2}
=
\frac14-\frac14\left(\frac14-1\right)
=
\frac14+\frac3{16}
=
\frac7{16}.
$$

Client 2:

$$
\theta_{2,1}
=
0-\frac14(3)
=
-\frac34,
$$

$$
\theta_{2,2}
=
-\frac34-\frac14\left[3\left(-\frac34+1\right)\right]
=
-\frac34-\frac3{16}
=
-\frac{15}{16}.
$$

Federated averaging gives

$$
\boxed{
\theta_{\mathrm{Fed}}
=
\frac12\left(\frac7{16}-\frac{15}{16}\right)
=
-\frac14.
}
$$

The pooled objective is

$$
\begin{aligned}
F(\theta)
&=\frac12F_1(\theta)+\frac12F_2(\theta)\\
&=\theta^2+\theta+1,
\end{aligned}
$$

with gradient

$$
g(\theta)=2\theta+1.
$$

The first pooled step is

$$
\theta_{\mathrm{pool},1}=-\frac14.
$$

The second is

$$
\begin{aligned}
\theta_{\mathrm{pool},2}
&=
-\frac14-\frac14\left(2\left(-\frac14\right)+1\right)\\
&=
-\frac14-\frac18\\
&=\boxed{-\frac38}.
\end{aligned}
$$

| Procedure | After one local or pooled step | After two steps and aggregation |
|---|---|---|
| Client 1 | $$1/4$$ | $$7/16$$ |
| Client 2 | $$-3/4$$ | $$-15/16$$ |
| Federated average | $$-1/4$$ | $$-1/4$$ |
| Pooled training | $$-1/4$$ | $$-3/8$$ |

The initial equality disappears after the clients move to different points.

The pooled objective values are

$$
F(-1/4)=\frac{13}{16},
$$

and

$$
F(-3/8)=\frac{49}{64}.
$$

They are different even though both procedures began with the same model and nominal objective.

### 6. The difference can persist across rounds

For the same quadratic example, two local steps from an arbitrary $$\theta$$ give

$$
\theta_{1,2}=\frac9{16}\theta+\frac7{16},
$$

$$
\theta_{2,2}=\frac1{16}\theta-\frac{15}{16}.
$$

Averaging produces the round update

$$
\theta_{t+1}
=
\frac5{16}\theta_t-\frac14.
$$

Its fixed point satisfies

$$
\theta^*=\frac5{16}\theta^*-\frac14,
$$

so

$$
\boxed{\theta^*_{\mathrm{Fed}}=-\frac4{11}}.
$$

The pooled objective's minimizer instead solves

$$
2\theta+1=0,
$$

giving

$$
\boxed{\theta^*_{\mathrm{pool}}=-\frac12}.
$$

This construction uses fixed local step size and two local steps per round. It demonstrates a persistent optimization difference, not a universal convergence claim about every federated algorithm.

### 7. Participation and weighting determine whose objective is learned

Suppose one client is selected per round, with probability $$p_k$$, and performs one gradient step.

The expected update is

$$
\mathbb E[\theta_{t+1}-\theta_t]
=
-\eta\sum_kp_k\nabla F_k(\theta_t).
$$

This matches the declared weighted objective only if the selection and correction scheme supplies the intended weights.

If client availability depends on institution, workload, or resources, the training process can emphasize the institutions that participate more often.

Other differences also matter:

- Local epoch counts can imply different numbers of updates.
- Class reweighting changes each local objective.
- Inconsistent target definitions can make losses clinically incompatible.
- Local normalization and preprocessing can change the input meaning.
- Shared average performance can conceal poor performance at a small client.

A federation is a data-access arrangement. It does not automatically harmonize clinical targets or create a representative deployment population.

### 8. Derive a simple example of information leakage through gradients

Keeping raw records local does not imply that updates contain no information about them.

Consider one training example with input vector $$x$$, target $$y$$, and linear prediction

$$
\widehat y=w^\top x+b.
$$

Use squared loss

$$
L=\frac12(\widehat y-y)^2.
$$

Let the residual be

$$
r=w^\top x+b-y.
$$

The gradients are

$$
\nabla_wL=rx,
$$

$$
\frac{\partial L}{\partial b}=r.
$$

If the bias gradient is nonzero,

$$
\boxed{
x=
\frac{\nabla_wL}{\partial L/\partial b}.
}
$$

With known parameters, the target can also be recovered:

$$
\boxed{
y=w^\top x+b-\frac{\partial L}{\partial b}.
}
$$

Construct

$$
x=(2,-1),
\qquad
y=1,
\qquad
w=(0,0),
\qquad
b=0.
$$

Then

$$
r=-1,
$$

$$
\nabla_wL=(-2,1),
\qquad
\frac{\partial L}{\partial b}=-1.
$$

Dividing recovers $$x=(2,-1)$$, and the residual recovers $$y=1$$.

This is a deliberately simple single-example setting. Aggregation, larger batches, clipping, noise, and restricted access change the attack. The example is sufficient to disprove the blanket claim that shared gradients are anonymized merely because raw inputs were not transferred.

### 9. Separate storage, aggregation, and privacy guarantees

| Property | What it addresses | What it does not establish by itself |
|---|---|---|
| Local raw-data storage | Avoids routine central collection of original records | Privacy of updates or final models |
| Access control and encrypted transport | Restricts who can inspect communication | What an authorized recipient can infer |
| Secure aggregation | Can hide individual updates while revealing an aggregate under its protocol assumptions | Privacy of the aggregate or released model |
| Differential privacy | Bounds changes in output distributions caused by a specified data-unit change | Clinical validity or zero information disclosure |
| Audit and governance records | Make access and changes accountable | A mathematical privacy guarantee |

The threat model must identify the observer: server, other clients, an external model user, or colluding participants. It must also specify what that observer receives.

Patient-level and image-level privacy are different when one patient contributes many records.

### 10. State a formal privacy guarantee and its composition

For neighboring datasets differing by one protected unit, a randomized mechanism $$M$$ is $$(\varepsilon,\delta)$$-differentially private if, for every measurable output event $$A$$,

$$
\boxed{
\Pr(M(D)\in A)
\leq
e^\varepsilon\Pr(M(D')\in A)+\delta.
}
$$

The neighboring unit must be specified, such as an entire patient's contribution. [The Algorithmic Foundations of Differential Privacy](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf).

Repeated data-dependent releases require accounting. For pure privacy guarantees, suppose each release has a conditional likelihood-ratio bound $$e^{\varepsilon_t}$$ given the preceding transcript. Then

$$
\begin{aligned}
\frac{p(o_{1:T}\mid D)}{p(o_{1:T}\mid D')}
&=
\prod_t
\frac{p(o_t\mid o_{<t},D)}
{p(o_t\mid o_{<t},D')}\\
&\leq
\prod_te^{\varepsilon_t}\\
&=
e^{\sum_t\varepsilon_t}.
\end{aligned}
$$

This gives a basic composition bound. More refined accounting can improve bounds for particular mechanisms.

Reusing an already private output through postprocessing is different from making another query to protected data. Federation alone supplies neither this definition nor its accounting.

### 11. Define continual learning and forgetting against fixed targets

Let $$\theta_t$$ be the model after update stage $$t$$. Let $$P_j$$ represent an earlier evaluation population with a fixed target definition.

Write

$$
R_{t,j}
=
\mathbb E_{P_j}[\ell(f_{\theta_t}(X),Y)].
$$

Forgetting means deterioration on an earlier capability that remains required. An immediate risk increase is

$$
R_{t,j}-R_{t-1,j}>0.
$$

For a higher-is-better score $$a_{t,j}$$, one possible nonnegative forgetting measure is

$$
\boxed{
F_{t,j}
=
\left[
\max_{u=j,\ldots,t-1}a_{u,j}
-
a_{t,j}
\right]_+.
}
$$

The definition compares current performance with the best earlier measured performance. Other baselines answer different questions, so the full performance matrix should accompany a summary.

“Catastrophic” describes a substantial loss of required capability; it has no universal numerical cutoff.

A decline on a new population is not automatically forgetting. To isolate model-induced retention loss, compare versions on the same target distribution and reference definition.

### 12. Derive the stability-plasticity conflict from gradients

Let

$$
g_{\mathrm{new}}=\nabla R_{\mathrm{new}}(\theta)
$$

and update

$$
\theta'=\theta-\eta g_{\mathrm{new}}.
$$

A Taylor expansion of old-task risk gives

$$
R_{\mathrm{old}}(\theta')
=
R_{\mathrm{old}}(\theta)
-
\eta\nabla R_{\mathrm{old}}(\theta)^\top g_{\mathrm{new}}
+
O(\eta^2).
$$

If the gradients have a negative inner product, the new-task step increases old-task loss to first order.

At an old-task optimum, its gradient can be zero. The second-order term then matters:

$$
R_{\mathrm{old}}(\theta')
-
R_{\mathrm{old}}(\theta)
\approx
\frac{\eta^2}{2}
g_{\mathrm{new}}^\top
H_{\mathrm{old}}
g_{\mathrm{new}}.
$$

Near a local minimum with positive curvature, movement needed for the new task can increase old-task loss.

This is a conflict between objectives under the available representation and parameters. It is not a theorem that every update must trade away old performance. Compatible tasks or additional informative context can permit improvement on both.

### 13. Carry a retention-regularization example through

Construct

$$
R_{\mathrm{old}}(\theta)=\frac12\theta^2,
$$

$$
R_{\mathrm{new}}(\theta)=\frac12(\theta-2)^2.
$$

The old optimum is zero; the new optimum is two.

Training only on the new objective moves from old loss zero to old loss two.

Now minimize

$$
J(\theta)
=
R_{\mathrm{new}}(\theta)
+
\lambda R_{\mathrm{old}}(\theta),
\qquad
\lambda\geq0.
$$

Differentiating,

$$
J'(\theta)
=
(\theta-2)+\lambda\theta.
$$

Setting the derivative to zero gives

$$
\boxed{\theta^*=\frac2{1+\lambda}}.
$$

The two losses become

$$
\boxed{
R_{\mathrm{old}}(\theta^*)
=
\frac2{(1+\lambda)^2},
}
$$

$$
\boxed{
R_{\mathrm{new}}(\theta^*)
=
\frac{2\lambda^2}{(1+\lambda)^2}.
}
$$

| Retention weight | Updated parameter | Old loss | New loss |
|---|---|---|---|
| $$0$$ | $$2$$ | $$2$$ | $$0$$ |
| $$1$$ | $$1$$ | $$1/2$$ | $$1/2$$ |
| $$3$$ | $$1/2$$ | $$1/8$$ | $$9/8$$ |
| Limit as $$\lambda\to\infty$$ | $$0$$ | $$0$$ | $$2$$ |

The table makes stability and plasticity explicit for this constructed conflict.

A parameter penalty is useful only insofar as it preserves the capabilities that matter. Preventing all change can preserve obsolete label conventions or known mistakes.

### 14. Replay, regularization, and versioning answer different needs

Replay approximates an old-data objective while training on new data:

$$
J(\theta)
=
(1-\beta)R_{\mathrm{new}}(\theta)
+
\beta\widehat R_{\mathrm{replay}}(\theta).
$$

Its effectiveness depends on what the replay set represents. A small memory can omit rare but important earlier conditions. Generated substitutes introduce their own approximation.

Regularization can discourage changes to parameters or outputs considered important. Such importance is estimated under a previous distribution; it is not a universal guarantee of retained clinical behavior.

Evaluation should include:

- Fixed earlier reference cohorts.
- New cases from the updated setting.
- Participating and unseen institutions.
- Clinically important subgroups.
- Corrected-label analyses when definitions change.
- The complete update and participation history.

Repeatedly selecting updates on the same historical cohort makes that cohort part of development. Fresh evaluation remains necessary.

### 15. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| When does a federated objective equal pooled empirical loss? | Under sample-count weighting of the same records |
| Does one local step necessarily differ from pooled training? | No; synchronized full-gradient averaging is exactly equal |
| Why do multiple local steps diverge? | Gradients are evaluated at different client-specific parameters |
| Can the difference persist? | Yes; the quadratic example has a different federated fixed point |
| Why does participation matter? | It changes the expected contribution of client objectives |
| Does local storage imply anonymization? | No; the gradient example reconstructs its input |
| What must a privacy claim specify? | Protected unit, observer, mechanism, releases, and accounting |
| What is forgetting? | Deterioration of an earlier required capability under a fixed evaluation target |
| Why can new learning harm old performance? | Objectives can have conflicting gradients or curvature |
| What do replay and penalties preserve? | Approximations to selected earlier behavior, requiring evaluation |

In the ontology, federation and continual learning are methods with distinct requirements. Privacy, robustness, retention, and clinical evidence reliance remain separate properties. Institutional collaboration does not substitute for external validation.

## Why it matters for my work

A gallbladder federation could share useful representations while inheriting different reference practices and acquisition cues. I would examine both site-level performance and how updates change reliance on clinical findings, especially when participation shifts toward one patient population.

## What I have not resolved

- Which institutional weighting represents the intended clinical population?
- Which earlier capabilities and label definitions should persist?
- What patient-level privacy and audit guarantees are feasible for the actual communication protocol?

---

Sources: Independent study; Federated Averaging and differential privacy are linked to verified primary sources above. The optimization, gradient-disclosure, and retention examples are constructed and derived explicitly. These are study notes for research purposes, not clinical guidance.
