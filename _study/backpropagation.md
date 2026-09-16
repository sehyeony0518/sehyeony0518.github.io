---
layout: study_note
title: "Backpropagation, in Scalars and in Matrices"
description: "How backpropagation organises the chain rule to compute derivatives for training, with scalar and matrix derivations for a dense layer and a convolution."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Learning Models & Representation"
subgroup: "Learning & Representation Foundations"
order: 2
source: "Independent study"
written: true
updated: "2026-09-15"
---

A loss measures an error at the output of a network. Backpropagation computes how that scalar error changes when each intermediate value, input, or parameter changes. Its central idea is to reuse derivatives of shared intermediate computations.

One correction is necessary at the outset: **backpropagation computes gradients; an optimiser uses those gradients to update parameters.** Differentiation alone does not specify a learning rate, a training objective, or a stopping rule. Understanding that separation makes it easier to distinguish an incorrect derivative from an unsuccessful optimisation process.

The examples below are constructed so that every result can be checked directly.

## The learning problem and the derivative it requires

For training examples and parameters, define

$$
L(\theta)
=
\frac{1}{N}\sum_{i=1}^{N}
\ell\bigl(f_\theta(x_i),y_i\bigr).
$$

Gradient descent uses

$$
\theta_{\mathrm{new}}
=
\theta-\alpha\nabla_\theta L.
$$

Why move in this direction? The first-order expansion for a small displacement is

$$
L(\theta+\Delta\theta)
=
L(\theta)
+
\nabla_\theta L^\top\Delta\theta
+
o(\lVert\Delta\theta\rVert).
$$

Substituting the gradient descent displacement gives

$$
L(\theta-\alpha\nabla_\theta L)
=
L(\theta)
-
\alpha\lVert\nabla_\theta L\rVert_2^2
+
o(\alpha).
$$

At a differentiable point with a nonzero gradient, sufficiently small positive steps therefore decrease the loss. This is a local statement. It does not guarantee that a large step decreases the loss, that training reaches a global minimum, or that a low training loss implies useful predictions.

The computational question is how to obtain all components of the gradient without separately perturbing every parameter. Backpropagation answers this by traversing the operations that produced the loss.

A useful distinction is between a **local derivative**, which treats an operation's arguments as independent, and a **total derivative**, which includes every downstream route through which a value affects the loss.

## The scalar chain rule as accumulation over paths

Start with a chain of scalar operations:

$$
u=f(x),
\qquad
v=g(u),
\qquad
L=h(v).
$$

For a small change in the input,

$$
\mathrm du=f'(x)\,\mathrm dx,
\qquad
\mathrm dv=g'(u)\,\mathrm du,
\qquad
\mathrm dL=h'(v)\,\mathrm dv.
$$

Substitution gives

$$
\frac{\mathrm dL}{\mathrm dx}
=
h'(v)g'(u)f'(x).
$$

The same product can be evaluated in either direction. Forward accumulation begins with an input perturbation and propagates its effect. Reverse accumulation begins with the sensitivity of the loss and propagates that sensitivity backwards.

Define the adjoint of an intermediate scalar by

$$
\bar v=\frac{\partial L}{\partial v}.
$$

The bar means “how sensitive is the final loss to this value?” It does not mean an average. Since changing the loss itself changes the loss by the same amount, the reverse pass starts from

$$
\bar L=1.
$$

For the chain above,

$$
\bar v=h'(v),
\qquad
\bar u=\bar v\,g'(u),
\qquad
\bar x=\bar u\,f'(x).
$$

A network is usually a graph with branches, so multiplication is only half the rule. If a value affects the loss through several children, the contributions add:

$$
\bar u
=
\sum_{v\in\operatorname{children}(u)}
\bar v\,
\frac{\partial v}{\partial u}.
$$

This follows directly from the multivariable differential. Each outgoing route contributes one first-order change to the final loss. Discarding one route discards a genuine dependency; counting a route twice introduces a dependency that the computation does not have.

## A branched scalar example, carried through completely

Consider

$$
u=wx,
\qquad
v=u+x,
\qquad
L=\frac12(v-y)^2.
$$

The input affects the loss through both the multiplication and the direct addition. Set

$$
x=2,\qquad w=3,\qquad y=1.
$$

The forward pass is

$$
u=6,
\qquad
v=8,
\qquad
L=\frac12(8-1)^2=24.5.
$$

The reverse pass starts at the squared error:

$$
\bar v=v-y=7.
$$

Because the addition has derivative one with respect to each argument,

$$
\bar u=7,
\qquad
\bar x_{\mathrm{direct}}=7.
$$

The multiplication contributes

$$
\bar w=\bar u\,x=14,
\qquad
\bar x_{\mathrm{through}\ u}=\bar u\,w=21.
$$

Therefore,

$$
\boxed{\bar x=7+21=28},
\qquad
\boxed{\bar w=14}.
$$

An independent check comes from eliminating the intermediates:

$$
L=\frac12\bigl(x(w+1)-y\bigr)^2.
$$

Direct differentiation gives

$$
\frac{\partial L}{\partial x}
=
\bigl(x(w+1)-y\bigr)(w+1)
=
7\cdot4=28,
$$

$$
\frac{\partial L}{\partial w}
=
\bigl(x(w+1)-y\bigr)x
=
7\cdot2=14.
$$

This is why a backward operation must **add into** an existing gradient accumulator. Assigning a new value to the accumulator would overwrite the contribution from another branch.

Shared parameters obey the same rule. If one weight is used at several locations, its gradient is the sum of the contributions from all those uses. Unrolling a recurrent network later turns this observation into backpropagation through time.

## Why reverse mode is efficient for a scalar output

Let a function have many inputs and one output:

$$
F:\mathbb R^P\longrightarrow\mathbb R.
$$

Forward mode propagates a chosen tangent. Seeding the input tangent with a vector gives

$$
\dot\theta=v,
\qquad
\dot L=\nabla_\theta L^\top v.
$$

This computes one directional derivative. To recover the entire gradient by ordinary forward accumulation, use each coordinate basis vector in turn:

$$
v=e_1,\ldots,e_P.
$$

That requires work proportional to the number of input directions. Propagating all those directions together does not remove the arithmetic: each intermediate now carries a tangent vector with that many components.

Reverse mode instead seeds the single output with one:

$$
\bar L=1.
$$

One reverse traversal then accumulates a sensitivity for every input. The distinction is described in the [survey of automatic differentiation by Baydin and colleagues](https://www.jmlr.org/papers/volume18/17-468/17-468.pdf).

The cost claim needs careful wording. Suppose a scalar computational graph takes arithmetic work proportional to

$$
C
$$

to evaluate. Each elementary operation has a backward rule requiring a bounded amount of work relative to its forward rule. For example, one multiplication produces two derivative contributions. Visiting every operation once backwards therefore also takes work proportional to

$$
C.
$$

Thus a scalar gradient costs one reverse sweep with **the same order of work as the forward computation**. It does not necessarily cost exactly one forward pass in wall-clock time or operation count.

A dense layer illustrates the constant factor. Its forward pass requires a matrix multiplication. Computing both input and weight gradients requires two related matrix multiplications. Memory traffic and implementation details affect the actual runtime.

For a vector-valued function, the distinction generalises:

$$
F:\mathbb R^P\longrightarrow\mathbb R^Q.
$$

Forward mode computes Jacobian-vector products; reverse mode computes transposed-Jacobian-vector products:

$$
J_Fv,
\qquad
J_F^\top u.
$$

Recovering a general full Jacobian requires one forward direction per input or one reverse seed per output. Reverse mode is particularly attractive when the desired output is a scalar loss. Forward mode remains efficient when only a few input directions are needed.

## Matrix backpropagation with shapes tracked

Use column vectors and define one dense block:

$$
x\in\mathbb R^{n\times1},
\quad
W\in\mathbb R^{m\times n},
\quad
b\in\mathbb R^{m\times1},
$$

$$
z=Wx+b\in\mathbb R^{m\times1},
\qquad
a=\phi(z)\in\mathbb R^{m\times1}.
$$

For any vector intermediate, define its gradient through the differential:

$$
\mathrm dL=g_z^\top\mathrm dz.
$$

For a matrix, use the Frobenius inner product:

$$
\mathrm dL
=
\sum_{i,j}(G_W)_{ij}\,\mathrm dW_{ij}
=
\operatorname{tr}(G_W^\top\mathrm dW).
$$

These conventions determine the orientation of every gradient.

First differentiate the affine operation:

$$
\mathrm dz
=
(\mathrm dW)x
+
W\,\mathrm dx
+
\mathrm db.
$$

Substitute this expression into the loss differential:

$$
\mathrm dL
=
g_z^\top(\mathrm dW)x
+
g_z^\top W\,\mathrm dx
+
g_z^\top\mathrm db.
$$

The input term can be rewritten as

$$
g_z^\top W\,\mathrm dx
=
(W^\top g_z)^\top\mathrm dx.
$$

Therefore,

$$
\boxed{\nabla_xL=W^\top g_z}.
$$

For the weight term, expand the indices:

$$
g_z^\top(\mathrm dW)x
=
\sum_{i=1}^{m}\sum_{j=1}^{n}
(g_z)_i x_j\,\mathrm dW_{ij}.
$$

Matching coefficients gives

$$
\boxed{\nabla_WL=g_zx^\top},
\qquad
\boxed{\nabla_bL=g_z}.
$$

The weight gradient is an outer product because one weight connects one input coordinate to one output coordinate. Its effect is the input value multiplied by the sensitivity at the destination.

| Gradient | Product | Resulting shape |
| --- | --- | --- |
| Input | $$W^\top g_z$$ | $$n\times1$$ |
| Weights | $$g_zx^\top$$ | $$m\times n$$ |
| Bias | $$g_z$$ | $$m\times1$$ |

For an element-wise activation,

$$
\mathrm da
=
\operatorname{diag}\bigl(\phi'(z)\bigr)\mathrm dz.
$$

Consequently,

$$
\boxed{g_z=g_a\odot\phi'(z)}.
$$

For ReLU, the derivative is one at positive preactivations and zero at negative preactivations. At zero, the ordinary derivative does not exist, so an implementation uses a specified convention.

The transpose in the input gradient is an instance of a general identity:

$$
\mathrm dv=J\,\mathrm du
\quad\Longrightarrow\quad
\mathrm dL
=
g_v^\top J\,\mathrm du
=
(J^\top g_v)^\top\mathrm du.
$$

Backpropagation applies this identity without constructing the full Jacobian.

## A complete numerical dense-network example

Consider a hidden ReLU layer and a scalar linear output:

$$
z=Wx+b,
\qquad
a=\operatorname{ReLU}(z),
\qquad
\hat y=v^\top a+c,
\qquad
L=\frac12(\hat y-y)^2.
$$

Choose

$$
x=
\begin{bmatrix}1\\2\end{bmatrix},
\quad
W=
\begin{bmatrix}
1&-1\\
2&1
\end{bmatrix},
\quad
b=
\begin{bmatrix}0\\1\end{bmatrix},
$$

$$
v=
\begin{bmatrix}3\\-2\end{bmatrix},
\qquad
c=1,
\qquad
y=-7.
$$

The forward values are

$$
z=
\begin{bmatrix}-1\\5\end{bmatrix},
\qquad
a=
\begin{bmatrix}0\\5\end{bmatrix},
\qquad
\hat y=-9,
\qquad
L=2.
$$

Start the backward pass with the residual:

$$
g_{\hat y}=\hat y-y=-2.
$$

For the output layer,

$$
\nabla_vL
=
g_{\hat y}a
=
\begin{bmatrix}0\\-10\end{bmatrix},
\qquad
\nabla_cL=-2,
$$

$$
g_a
=
v\,g_{\hat y}
=
\begin{bmatrix}-6\\4\end{bmatrix}.
$$

The first hidden unit has negative preactivation. Its ReLU derivative removes its incoming sensitivity:

$$
g_z
=
\begin{bmatrix}-6\\4\end{bmatrix}
\odot
\begin{bmatrix}0\\1\end{bmatrix}
=
\begin{bmatrix}0\\4\end{bmatrix}.
$$

The remaining gradients are

$$
\nabla_WL
=
\begin{bmatrix}
0&0\\
4&8
\end{bmatrix},
\qquad
\nabla_bL=
\begin{bmatrix}0\\4\end{bmatrix},
$$

$$
\nabla_xL
=
W^\top g_z
=
\begin{bmatrix}8\\4\end{bmatrix}.
$$

The input gradient is independently checkable. In the neighbourhood where the activation pattern stays unchanged,

$$
\hat y=-2(2x_1+x_2+1)+1.
$$

Its input derivative is therefore

$$
\nabla_x\hat y=
\begin{bmatrix}-4\\-2\end{bmatrix}.
$$

Multiplying by the residual gives the same loss gradient.

The zero first row of the weight gradient has a precise meaning: for this example and activation pattern, changing those weights slightly does not change the output. It does not mean those weights are irrelevant for every input.

## Batches, broadcasting, and loss reduction

Stack examples as columns:

$$
X\in\mathbb R^{n\times B},
\qquad
Z=WX+b\mathbf1_B^\top
\in\mathbb R^{m\times B}.
$$

Let the incoming gradient have the same shape as the preactivations:

$$
G_Z\in\mathbb R^{m\times B}.
$$

The same differential argument gives

$$
\nabla_XL=W^\top G_Z,
$$

$$
\nabla_WL=G_ZX^\top,
$$

$$
\nabla_bL=G_Z\mathbf1_B.
$$

The weight product sums one outer product per example. The bias gradient sums across the axis on which the bias was broadcast. More generally, the backward operation for broadcasting sums over the replicated uses.

If the loss is a mean over examples, its reciprocal batch-size factor already enters the backward pass through the loss. Dividing the parameter gradients by the batch size again would apply the averaging twice.

Differentiation remains linear when a loss is a sum. However, computing examples independently is not always equivalent to differentiating an actual batch computation. Operations that use batch statistics or compare examples create cross-example dependencies. Backpropagation must follow those dependencies in the graph that was actually evaluated.

## Convolution as a structured linear map

A simple one-dimensional operation makes the indexing visible. Define a valid cross-correlation by

$$
y_i=\sum_{j=0}^{K-1}k_jx_{i+j}.
$$

For fixed kernel values, this is multiplication by a sparse matrix. With a two-element kernel and four-element input,

$$
y=
\begin{bmatrix}
k_0&k_1&0&0\\
0&k_0&k_1&0\\
0&0&k_0&k_1
\end{bmatrix}x.
$$

The input gradient is multiplication by this matrix's transpose. For

$$
x=(1,2,3,4)^\top,
\qquad
k=(2,-1)^\top,
$$

the output and squared loss are

$$
y=(0,1,2)^\top,
\qquad
L=\frac12\lVert y\rVert_2^2=2.5.
$$

The incoming gradient is the output itself. Transposed multiplication gives

$$
\nabla_xL=(0,2,3,-2)^\top.
$$

Kernel sharing requires accumulation across output positions:

$$
\frac{\partial L}{\partial k_j}
=
\sum_i(g_y)_i x_{i+j}.
$$

Thus,

$$
\frac{\partial L}{\partial k_0}
=
0\cdot1+1\cdot2+2\cdot3=8,
$$

$$
\frac{\partial L}{\partial k_1}
=
0\cdot2+1\cdot3+2\cdot4=11.
$$

Stride, padding, and dilation change the indexing, not the principle. If

$$
y_i=\sum_jk_jx_{si-p+dj},
$$

with out-of-range input coordinates treated as zero, then

$$
\frac{\partial L}{\partial x_r}
=
\sum_{i,j:\,r=si-p+dj}(g_y)_i k_j,
$$

$$
\frac{\partial L}{\partial k_j}
=
\sum_i(g_y)_i x_{si-p+dj}.
$$

These formulas say exactly where each contribution is scattered. A flipped-kernel description depends on whether the forward convention is convolution or cross-correlation and on the boundary rules.

The general object is the **adjoint of the forward linear operator**. It is not its inverse. The [PyTorch transposed-convolution documentation](https://docs.pytorch.org/docs/2.14/generated/torch.nn.ConvTranspose1d.html) makes this distinction explicit.

## Saved values and practical derivative checks

A backward rule needs particular forward values. The dense weight gradient needs its input; an activation derivative needs enough information to determine its local slope. Some derivatives can use the output instead of the preactivation.

Consequently, training does not literally require storing every intermediate forever. It requires preserving or recomputing the values needed by backward operations. Checkpointing stores selected values and recomputes others, exchanging additional arithmetic for less retained memory.

Automatic differentiation applies derivative rules to the executed computation. It does not use finite differences internally, and it does not repair a detached dependency or an incorrectly written custom backward rule.

A useful independent check compares a directional derivative with a central difference:

$$
\nabla_\theta L^\top v
\approx
\frac{L(\theta+hv)-L(\theta-hv)}{2h}.
$$

For the dense example, perturb the second weight row in direction

$$
(1,-1).
$$

The analytic directional derivative is

$$
4-8=-4.
$$

The perturbation changes the loss to

$$
L(h)=2-4h+2h^2.
$$

Its central difference is exactly negative four in exact arithmetic. This checks several derivatives together without estimating every coordinate separately.

In general, very large steps introduce approximation error, while very small steps expose floating-point cancellation. Checks near a ReLU boundary also compare different activation branches. A failed numerical check therefore needs interpretation, but a well-chosen small example is a strong way to catch missing sums, incorrect transposes, and wrong reduction factors.

## Revision checklist

| Question | What I should be able to reconstruct |
| --- | --- |
| What does backpropagation compute? | Derivatives of a specified scalar objective; an optimiser supplies the update rule. |
| Why do branches require addition? | The loss differential contains one contribution from every outgoing path. |
| Why seed the loss with one? | Its derivative with respect to itself is one. |
| Why is reverse mode efficient here? | One scalar output seeds one reverse traversal that reaches all inputs. |
| Is backward exactly as expensive as forward? | It has comparable arithmetic order, with operation-dependent constant factors. |
| Where do dense-layer transposes come from? | Matching coefficients in the loss differential. |
| Why is the weight gradient an outer product? | Each weight multiplies one input and affects one preactivation. |
| What happens to broadcast variables? | Their gradients sum across replicated uses. |
| What is a convolution's input backward operation? | The adjoint of the indexed forward operator, including its boundary rules. |
| How can I check a backward implementation? | Compare a hand-derived directional derivative with a central difference away from kinks. |

## Why it matters for my work

For an ultrasound model audit, gradients are useful only when I know which scalar was differentiated, which inputs were treated as variables, and which dependencies were retained. The scalar and matrix derivations give me concrete expectations for checking an attribution pipeline or a custom analysis layer.

## What I have not resolved

For models I audit, which preprocessing and custom operations preserve the intended input dependency, and which introduce discontinuities or detachments that make a reported gradient answer a narrower question?
