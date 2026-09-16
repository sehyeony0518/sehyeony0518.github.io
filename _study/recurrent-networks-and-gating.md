---
layout: study_note
title: "Recurrent Networks and Gating"
description: "State carried across time, why gradients through it vanish or explode, and what a gate is actually doing about it."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Learning Models & Representation"
subgroup: "Sequence Models & Attention"
order: 8
source: "Independent study"
written: true
updated: "2026-09-15"
---

A recurrent network carries a state from one time step to the next. Training must determine both what to write into that state and how an earlier write affects a later loss.

Unrolling the recurrence produces an ordinary computational graph with repeated uses of the same parameters. Backpropagation through time is reverse-mode differentiation of that graph. Its distinctive difficulty is a product of state-transition Jacobians.

Gating changes that product by introducing a direct, additive route for state. It does not remove every multiplicative factor or guarantee that all long-range gradients remain useful.

## The recurrent computation and its shapes

Consider a recurrent model with an element-wise hyperbolic tangent:

$$
a_t=Uh_{t-1}+Wx_t+b,
\qquad
h_t=\tanh(a_t),
$$

$$
o_t=Vh_t+c.
$$

Choose dimensions

$$
x_t\in\mathbb R^{m\times1},
\qquad
h_t,a_t,b\in\mathbb R^{d\times1},
$$

$$
U\in\mathbb R^{d\times d},
\qquad
W\in\mathbb R^{d\times m},
\qquad
V\in\mathbb R^{k\times d},
$$

$$
o_t,c\in\mathbb R^{k\times1}.
$$

The recurrence uses the same matrices at every step. For a sequence loss,

$$
L=\sum_{t=1}^{T}\ell_t(o_t,y_t).
$$

A final-output task is included by making all earlier loss terms zero. A per-frame task instead supplies a loss at each observed step.

Unrolling creates separate intermediate states but shared parameter nodes. The first state depends on the initial state and first input; the next depends on that result; the final loss can consequently depend on every earlier input.

Parameter sharing allows the same computation to run for different sequence lengths. It does not guarantee that a model trained on short sequences performs well on longer ones. The distribution of states, number of gradient factors, and opportunity for accumulated error all change with the sequence.

The hidden state is also a summary, not a literal copy of the complete history. Which distinctions survive is determined by the recurrence and its training objective.

## Deriving backpropagation through time

Let the local output-loss gradient be

$$
q_t=\nabla_{o_t}\ell_t.
$$

There are two routes from the hidden state to the total loss: its current output and the next recurrent computation. Reverse accumulation therefore gives

$$
\bar h_t
=
V^\top q_t+U^\top\bar a_{t+1},
$$

where the future contribution is zero after the final step.

The activation derivative follows from

$$
\tanh(a)=\frac{e^{2a}-1}{e^{2a}+1}.
$$

Differentiating the quotient gives

$$
\frac{\mathrm d}{\mathrm da}\tanh(a)
=
\frac{4e^{2a}}{(e^{2a}+1)^2}
=
1-\tanh^2(a).
$$

Thus,

$$
\bar a_t
=
\bar h_t\odot(1-h_t\odot h_t).
$$

Define the diagonal activation Jacobian

$$
D_t=\operatorname{diag}(1-h_t\odot h_t).
$$

The one-step state Jacobian is

$$
J_t
=
\frac{\partial h_t}{\partial h_{t-1}}
=
D_tU.
$$

The hidden-state backward recursion can equivalently be written as

$$
\boxed{
\bar h_t=V^\top q_t+J_{t+1}^\top\bar h_{t+1}
}.
$$

Expanding this recursion reveals the long paths:

$$
\bar h_s
=
\sum_{t=s}^{T}
\left(J_tJ_{t-1}\cdots J_{s+1}\right)^\top
V^\top q_t.
$$

For the term with matching time indices, the empty product is the identity matrix. The formula separates the contribution of each loss from the transition product that transports it backwards.

The matrices are ordered. In general, matrix multiplication is not commutative, so their order cannot be rearranged.

For the shared recurrent weights, the differential at one step contains

$$
\mathrm da_t=(\mathrm dU)h_{t-1}+\cdots.
$$

Matching coefficients and summing all uses gives

$$
\boxed{
\nabla_UL
=
\sum_{t=1}^{T}\bar a_t h_{t-1}^\top
}.
$$

Likewise,

$$
\nabla_WL
=
\sum_t\bar a_t x_t^\top,
\qquad
\nabla_bL=\sum_t\bar a_t,
$$

$$
\nabla_VL
=
\sum_tq_t h_t^\top,
\qquad
\nabla_cL=\sum_tq_t.
$$

The input gradient at each step is

$$
\nabla_{x_t}L=W^\top\bar a_t.
$$

These are ordinary dense-layer backward rules applied repeatedly. The recurrent part is the dependency between successive states; parameter sharing requires the final sum across time.

## A three-step example with an independently checkable answer

Use a scalar linear recurrence to isolate the effect of sharing:

$$
h_t=wh_{t-1}+x_t.
$$

Set

$$
h_0=0,
\qquad
(x_1,x_2,x_3)=(1,0,0),
\qquad
w=\frac12,
$$

and place a loss only at the final step:

$$
L=\frac12(h_3-1)^2.
$$

The forward states are

$$
h_1=1,
\qquad
h_2=\frac12,
\qquad
h_3=\frac14.
$$

The loss is

$$
L
=
\frac12\left(-\frac34\right)^2
=
\frac9{32}
=
0.28125.
$$

The final state gradient is

$$
\bar h_3=h_3-1=-\frac34.
$$

Each previous state receives multiplication by the shared scalar weight:

$$
\bar h_2
=
w\bar h_3
=
-\frac38,
$$

$$
\bar h_1
=
w\bar h_2
=
-\frac3{16}.
$$

The weight gradient must include every use:

| Step | Previous state | Incoming state gradient | Contribution to the shared weight |
| --- | --- | --- | --- |
| First | $$0$$ | $$-3/16$$ | $$0$$ |
| Second | $$1$$ | $$-3/8$$ | $$-3/8$$ |
| Third | $$1/2$$ | $$-3/4$$ | $$-3/8$$ |

Therefore,

$$
\frac{\partial L}{\partial w}
=
-\frac38-\frac38
=
-\frac34.
$$

There is a direct symbolic check. The constructed inputs imply

$$
h_3=w^2,
\qquad
L=\frac12(w^2-1)^2.
$$

Differentiating gives

$$
\frac{\partial L}{\partial w}
=
2w(w^2-1).
$$

At the selected weight, this is again negative three quarters.

If the state after the second step is detached, its forward value remains one half, but its dependence on earlier weight uses is removed from the backward graph. Only the third-step contribution remains:

$$
\frac{\partial L}{\partial w}\bigg|_{\mathrm{detached}}
=
-\frac38.
$$

This is the essential effect of truncated backpropagation through time. The numerical state can carry earlier information even when the gradient no longer assigns credit through the full history.

## Where vanishing and exploding gradients arise

For a final-time loss, the dependence on an earlier state includes

$$
\frac{\partial h_T}{\partial h_s}
=
J_TJ_{T-1}\cdots J_{s+1}.
$$

In a scalar linear recurrence, each factor is the same weight:

$$
\frac{\partial h_T}{\partial h_s}
=
w^{T-s}.
$$

With ten transitions,

$$
\left(\frac12\right)^{10}
=
0.0009765625,
$$

whereas

$$
2^{10}=1024.
$$

These numbers are consequences of the chosen recurrences. They locate the mechanism: small repeated sensitivities contract a distant contribution, while large repeated sensitivities amplify it.

For a tanh recurrence, the scalar factor is instead

$$
J_t=w(1-h_t^2).
$$

A large recurrent weight does not by itself establish an expanding path. If the weight is two and the state at a step is nine tenths, the local factor is

$$
2(1-0.9^2)=0.38.
$$

Saturation has made that transition contractive.

The converse is also important. With zero inputs, zero initial state, and recurrent weight two, all tanh states remain zero. Nevertheless, the derivative at each step is two, so sensitivity to an initial-state perturbation grows exponentially. **Bounded state values do not imply bounded derivatives.**

For matrices, the operator norm gives

$$
\left\lVert
J_T\cdots J_{s+1}
\right\rVert_2
\le
\prod_{t=s+1}^{T}\lVert J_t\rVert_2.
$$

If every factor is bounded above by the same value below one, long products vanish. This is a sufficient condition. Having some factors with norm above one is not sufficient to prove explosion: the propagated direction might enter contracting subspaces.

The transition matrices also depend on the trajectory through the activation derivatives. Looking only at the recurrent weight matrix misses those factors. [Pascanu, Mikolov, and Bengio analyse this gradient-product difficulty](https://proceedings.mlr.press/v28/pascanu13.pdf).

Even eigenvalues of a fixed matrix can miss finite-time amplification. For example,

$$
U=
\begin{bmatrix}
1&10\\
0&1
\end{bmatrix}
=
I+N,
\qquad
N^2=0.
$$

The binomial expansion terminates:

$$
U^r=I+rN=
\begin{bmatrix}
1&10r\\
0&1
\end{bmatrix}.
$$

Both eigenvalues are one, yet some directions undergo substantial amplification. Singular values and the actual ordered product are more directly relevant to gradient magnitudes.

## Constructing an additive gated memory path

A general memory update can retain an old value and add a new write:

$$
c_t=f_t\odot c_{t-1}+i_t\odot g_t.
$$

The forget gate controls retention, the input gate controls writing, and the candidate supplies the proposed content.

A standard LSTM without direct cell-to-gate connections uses

$$
f_t=\sigma(W_fx_t+U_fh_{t-1}+b_f),
$$

$$
i_t=\sigma(W_ix_t+U_ih_{t-1}+b_i),
$$

$$
g_t=\tanh(W_gx_t+U_gh_{t-1}+b_g),
$$

$$
o_t=\sigma(W_ox_t+U_oh_{t-1}+b_o),
$$

$$
c_t=f_t\odot c_{t-1}+i_t\odot g_t,
\qquad
h_t=o_t\odot\tanh(c_t).
$$

All state and gate vectors here have the same hidden dimension. These equations correspond to the ordinary unprojected form documented in the [LSTM reference](https://docs.pytorch.org/docs/2.14/generated/torch.nn.LSTM.html).

The sigmoid maps real gate preactivations to values strictly between zero and one:

$$
\sigma(a)=\frac1{1+e^{-a}}.
$$

Differentiating gives

$$
\sigma'(a)
=
\frac{e^{-a}}{(1+e^{-a})^2}
=
\sigma(a)\bigl(1-\sigma(a)\bigr).
$$

The bounded gate provides a smooth interpolation between retention and erasure. Values exactly zero or one are useful limiting descriptions, rather than ordinary sigmoid outputs at finite preactivations.

Along the direct cell-to-cell edge, holding the other state input fixed,

$$
\frac{\partial c_t}{\partial c_{t-1}}
=
\operatorname{diag}(f_t).
$$

Following only these edges through time gives

$$
\operatorname{diag}(f_T)
\cdots
\operatorname{diag}(f_{s+1})
=
\operatorname{diag}
\left(
\prod_{t=s+1}^{T}f_t
\right),
$$

where the product inside the diagonal is element-wise.

This path avoids repeated multiplication by a dense recurrent matrix and avoids a tanh derivative at every cell transition. Retention can be learned separately for each coordinate and time step. That is the mathematical advantage of the additive gated path.

## The full LSTM Jacobian includes the gates

The direct path is only one route through the recurrent computation. Gates depend on the previous hidden state, which itself participates in the earlier graph.

Treat the complete recurrent state as the pair

$$
(c_{t-1},h_{t-1}).
$$

Define gate derivative matrices

$$
D_f=\operatorname{diag}(f_t\odot(1-f_t)),
\qquad
D_i=\operatorname{diag}(i_t\odot(1-i_t)),
$$

$$
D_g=\operatorname{diag}(1-g_t\odot g_t),
\qquad
D_o=\operatorname{diag}(o_t\odot(1-o_t)).
$$

The cell differential is

$$
\mathrm dc_t
=
F_t\,\mathrm dc_{t-1}
+
B_t\,\mathrm dh_{t-1},
$$

with

$$
F_t=\operatorname{diag}(f_t)
$$

and

$$
B_t
=
\operatorname{diag}(c_{t-1})D_fU_f
+
\operatorname{diag}(g_t)D_iU_i
+
\operatorname{diag}(i_t)D_gU_g.
$$

Each term comes from differentiating one factor in the cell update. The first changes retention, the second changes the amount written, and the third changes the candidate content.

For the hidden output, define

$$
R_t=
\operatorname{diag}
\left(
o_t\odot[1-\tanh^2(c_t)]
\right),
$$

$$
Q_t=
\operatorname{diag}(\tanh(c_t))D_oU_o.
$$

Then

$$
\mathrm dh_t
=
R_t\,\mathrm dc_t
+
Q_t\,\mathrm dh_{t-1}.
$$

Substituting the cell differential gives the full state-transition Jacobian:

$$
\boxed{
\frac{\partial(c_t,h_t)}
{\partial(c_{t-1},h_{t-1})}
=
\begin{bmatrix}
F_t&B_t\\
R_tF_t&R_tB_t+Q_t
\end{bmatrix}
}.
$$

Long-range derivatives multiply these block matrices. The forget-gate product describes a favourable route within that full product; it is not the entire derivative.

The backward rules also show how gates learn. If the total incoming cell sensitivity has been accumulated, the local contributions are

$$
\bar f_t=\bar c_t\odot c_{t-1},
\qquad
\bar i_t=\bar c_t\odot g_t,
\qquad
\bar g_t=\bar c_t\odot i_t.
$$

The gate preactivations then receive the corresponding sigmoid or tanh derivative. A saturated gate can preserve a value effectively while learning to change that gate remains slow.

## Quantifying retention and its limitations

If one cell coordinate has a constant forget gate and we inspect its direct path over a given number of transitions, the multiplier is a power:

$$
f^r.
$$

For constructed gate values,

$$
0.9^{20}\approx0.121577,
$$

$$
0.99^{100}\approx0.366032.
$$

A gate close to one lengthens the useful retention scale, but a fixed gate below one still produces eventual decay.

Define the gradient half-life by solving

$$
f^r=\frac12.
$$

Taking logarithms gives

$$
r=\frac{\log(1/2)}{\log f}.
$$

The corresponding half-lives are approximately

$$
6.58
\quad\text{and}\quad
68.97
$$

transitions for the two gate values above. These are mathematical properties of the selected constants, not typical measured memory lengths.

Candidate boundedness does not confine the cell to the candidate's range. For example,

$$
c_t=0.99c_{t-1}+0.25,
\qquad
c_0=0,
$$

has the solution

$$
c_t
=
0.25\sum_{j=0}^{t-1}0.99^j
=
25(1-0.99^t).
$$

The cell can grow far beyond one even though every write is bounded. A large cell value can also saturate the output tanh, making the stored value difficult to expose through the current hidden output.

Preserving a direct derivative is therefore only part of learning a useful memory. The model must write relevant information, retain it, expose it, and receive an objective that rewards those operations.

## Deriving the GRU's direct path

A GRU combines retention and updating in one state. Use the convention that a large update gate means retaining the old state:

$$
z_t=\sigma(W_zx_t+U_zh_{t-1}+b_z),
$$

$$
r_t=\sigma(W_rx_t+U_rh_{t-1}+b_r),
$$

$$
n_t=
\tanh\left(
W_nx_t+U_n(r_t\odot h_{t-1})+b_n
\right),
$$

$$
h_t=z_t\odot h_{t-1}+(1-z_t)\odot n_t.
$$

Some presentations reverse the update-gate convention. Implementations can also place the reset multiplication differently; the [GRU documentation explains one such difference](https://docs.pytorch.org/docs/2.14/generated/torch.nn.GRU.html). The equations must be fixed before comparing derivatives.

Differentiate the state update:

$$
\mathrm dh_t
=
\operatorname{diag}(z_t)\,\mathrm dh_{t-1}
+
\operatorname{diag}(h_{t-1}-n_t)\,\mathrm dz_t
+
\operatorname{diag}(1-z_t)\,\mathrm dn_t.
$$

Therefore,

$$
\boxed{
J_t
=
\operatorname{diag}(z_t)
+
\operatorname{diag}(h_{t-1}-n_t)J_{z,t}
+
\operatorname{diag}(1-z_t)J_{n,t}
}.
$$

For the chosen reset convention,

$$
J_{z,t}
=
\operatorname{diag}(z_t\odot(1-z_t))U_z,
$$

$$
J_{r,t}
=
\operatorname{diag}(r_t\odot(1-r_t))U_r,
$$

$$
J_{n,t}
=
\operatorname{diag}(1-n_t\odot n_t)
U_n
\left[
\operatorname{diag}(r_t)
+
\operatorname{diag}(h_{t-1})J_{r,t}
\right].
$$

The first term is the direct retention route. Following those edges yields an element-wise product of update gates. The other terms capture changes to the gate and candidate.

If the gate is fixed and the candidate does not depend on the old state, the direct term is the entire Jacobian. In a learned GRU, that simplification generally does not hold.

## Clipping, truncation, and sequential computation

Global gradient clipping replaces a gradient by

$$
g_{\mathrm{clip}}
=
g\min\left(1,\frac{\gamma}{\lVert g\rVert_2}\right),
$$

with the zero gradient left unchanged. This keeps its norm at or below the chosen threshold. For ordinary gradient descent, it also bounds the update norm by the learning rate times that threshold.

Clipping addresses excessively large computed gradients. It cannot restore an earlier contribution that has already contracted almost to zero. Truncation addresses memory and computation by removing long backward paths, so it changes which dependencies receive credit.

A general nonlinear recurrence has a dependency from each state to the next. Input projections and computations within a step can still be parallelised, as can different sequences in a batch. Special recurrence structures can permit additional parallel algorithms. “Recurrent” does not mean that every operation must execute serially, but the state dependency is a real constraint.

Finally, vanishing gradients describe a learning difficulty, not proof that a trained model uses no distant information. A model can retain an earlier value while a particular loss supplies little gradient through that history. State retention, gradient transport, and demonstrated predictive use require separate checks.

## Revision checklist

| Question | What I should be able to reconstruct |
| --- | --- |
| What is backpropagation through time? | Reverse-mode differentiation of an unrolled graph with shared parameters. |
| Why are recurrent parameter gradients summed? | The same parameter participates in several local operations. |
| What is the basic state Jacobian? | The activation derivative multiplied by the recurrent weight matrix. |
| Where do distant sensitivities arise? | Ordered products of transition Jacobians. |
| What is a sufficient condition for vanishing? | A uniform operator-norm bound below one along the path. |
| Do bounded states prevent exploding derivatives? | No; the zero-state tanh example gives a counterexample. |
| What does the LSTM add? | A direct cell path with forget-gate factors. |
| Is the forget-gate product the full derivative? | No; the full state Jacobian includes gate and output routes. |
| What does the GRU retention term contribute? | An additive diagonal term within its full transition Jacobian. |
| What does truncation remove? | Backward dependencies across the detach boundary, while forward state values can persist. |
| What can clipping repair? | Excessive gradient magnitude, not missing long-range credit. |

## Why it matters for my work

A sequence model can base an ultrasound prediction on evidence written into its state several frames earlier. An audit should therefore distinguish the current frame, the retained history, and the gradients through that history. Looking only at the prediction frame can miss the input that supplied the relevant information.

## What I have not resolved

Which sequence interventions would distinguish useful anatomical context from acquisition-specific state, while preserving enough temporal structure to make the intervention interpretable?
