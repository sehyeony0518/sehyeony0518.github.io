---
layout: study_note
title: "Curvature Without the Hessian: Power Iteration, Trace Estimation, and Quantization"
description: "Second-order information about a network that is too large to form, estimated by matrix-vector products, and what it is used to decide."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "algebra-and-optimisation"
category_title: "Linear Algebra & Optimisation"
subgroup: "Losses & Gradient Optimisation"
order: 8
source: "Independent study"
written: true
updated: "2026-09-15"
---

The Hessian describes how a loss gradient changes when parameters move. Forming every Hessian entry can be prohibitively expensive, but many useful questions require only the Hessian's action on selected vectors.

Three operations organize this note: double backward computes a Hessian-vector product; power iteration extracts a dominant eigenpair from repeated products; and Hutchinson's estimator recovers the trace in expectation. Their outputs answer different questions, especially when the Hessian has negative eigenvalues.

## What curvature means before computing it

Let a scalar loss depend on a parameter vector:

$$
L(w),
\qquad
g=\nabla L(w),
\qquad
H=\nabla^2L(w).
$$

Assume the loss is twice continuously differentiable near the point being examined. Define a one-dimensional path through a perturbation:

$$
h(t)=L(w+t\Delta).
$$

The chain rule gives

$$
h'(t)=\nabla L(w+t\Delta)^\top\Delta,
$$

and

$$
h''(t)=\Delta^\top H(w+t\Delta)\Delta.
$$

Integrating the derivative twice yields

$$
L(w+\Delta)
=
L(w)+g^\top\Delta+
\int_0^1(1-t)\Delta^\top H(w+t\Delta)\Delta\,dt.
$$

If the Hessian changes little along the displacement, replace it inside the integral by its value at the starting point. Since the integral of the weight is one-half,

$$
L(w+\Delta)
\approx
L(w)+g^\top\Delta+
\frac12\Delta^\top H\Delta.
$$

The linear term measures slope. The quadratic term measures curvature. A trained checkpoint need not have a negligible full gradient, and a small nonzero linear term can dominate sufficiently small perturbations because it scales with displacement rather than squared displacement.

For a constructed parameter count of one million, a dense Hessian has one trillion entries. At four bytes per entry, that is four trillion bytes before accounting for other memory. The calculation illustrates quadratic storage growth; it is not a measurement of a particular model.

Inability to store the matrix does not make every second-order method impossible. Iterative linear solvers can use Hessian-vector products to approximate damped Newton steps. Matrix storage and linear-system solution are related but distinct obstacles.

## Directional curvature and the meaning of “top”

For a unit vector, directional curvature is the Rayleigh quotient:

$$
\rho(v)=v^\top Hv,
\qquad
\lVert v\rVert_2=1.
$$

Because the Hessian is symmetric under the stated differentiability assumption, expand the vector in an orthonormal eigenbasis:

$$
v=\sum_jc_jq_j,
\qquad
\sum_jc_j^2=1.
$$

Then

$$
v^\top Hv=\sum_j\lambda_jc_j^2.
$$

The quotient is a weighted average of eigenvalues. It lies between the smallest and largest algebraic eigenvalues, with the extremes attained at the corresponding eigenvectors.

For a positive semidefinite Hessian, every directional quadratic contribution is nonnegative. At an indefinite point, some directions decrease the loss to second order while others increase it.

“Top eigenvalue” is therefore ambiguous unless the ordering is specified:

- The largest algebraic eigenvalue identifies the most positive curvature.
- The smallest algebraic eigenvalue identifies the most negative curvature.
- The eigenvalue of largest magnitude identifies the strongest absolute amplification by the matrix.

Ordinary power iteration targets the last of these. It targets the most positive curvature automatically only when the spectrum and dominant magnitude make those quantities coincide.

## Deriving a Hessian-vector product with double backward

Let a probe vector be fixed with respect to the parameters. Form the scalar

$$
s(w)=g(w)^\top v.
$$

Differentiate its coordinate expression:

$$
\frac{\partial s}{\partial w_j}
=
\sum_i
\frac{\partial g_i}{\partial w_j}v_i.
$$

This is the vector-Jacobian product of the gradient, or

$$
\nabla_ws=H^\top v.
$$

Symmetry gives

$$
\nabla_w(g^\top v)=Hv.
$$

The computation consists of a gradient followed by a gradient of a scalar constructed from that gradient. It never needs to assemble the entries of the Hessian.

Holding the probe fixed is essential. If the probe itself depends on the parameters, the product rule gives an extra term:

$$
\nabla_w[g(w)^\top v(w)]
=
Hv+J_v^\top g.
$$

That is not the desired fixed-vector product. Detaching the probe from automatic differentiation prevents the unwanted term.

The first differentiation must retain differentiable operations in its result. A numerical gradient vector with no derivative graph is insufficient for a second differentiation. Retaining an ordinary forward graph and constructing a graph of the derivative are different requirements.

Computational memory still includes the model's derivative graph and saved activations. “No dense Hessian” does not mean “no substantial memory cost.” What is avoided is storing a parameter-by-parameter matrix.

## A double-backward example with an explicit answer

Use the quadratic

$$
L(w_1,w_2)
=
\frac32w_1^2+w_1w_2+\frac32w_2^2.
$$

Its gradient and Hessian are

$$
g=
\begin{bmatrix}
3w_1+w_2\\
w_1+3w_2
\end{bmatrix},
\qquad
H=
\begin{bmatrix}
3&1\\
1&3
\end{bmatrix}.
$$

Choose

$$
v=
\begin{bmatrix}
2\\-1
\end{bmatrix}.
$$

Direct multiplication gives

$$
Hv=
\begin{bmatrix}
5\\-1
\end{bmatrix}.
$$

The double-backward route reaches the same result without matrix construction:

$$
g^\top v
=
2(3w_1+w_2)-(w_1+3w_2)
=
5w_1-w_2.
$$

Differentiating this scalar gives the expected product.

A minimal PyTorch implementation is:

```python
import torch

w = torch.tensor(
    [1.0, -1.0],
    dtype=torch.float64,
    requires_grad=True,
)
v = torch.tensor([2.0, -1.0], dtype=torch.float64)

loss = 1.5 * w[0] ** 2 + w[0] * w[1] + 1.5 * w[1] ** 2

(gradient,) = torch.autograd.grad(loss, w, create_graph=True)
directional_derivative = (gradient * v.detach()).sum()
(hv,) = torch.autograd.grad(directional_derivative, w)

# Algebraically expected: tensor([5., -1.], dtype=torch.float64)
```

For a model with multiple parameter tensors, the scalar directional derivative sums the elementwise products over all corresponding gradient and probe tensors. A completely unused parameter or a locally constant first derivative needs explicit zero handling; not every such case leaves a differentiable tensor for a second call.

Custom operations must support higher derivatives. At nondifferentiable activation boundaries, the classical Hessian may not exist, and the returned automatic-differentiation result must be interpreted according to the implemented derivative rules.

## Checking that the product represents one fixed objective

A finite-difference comparison provides an independent check:

$$
Hv
=
\lim_{h\to0}
\frac{
\nabla L(w+hv)-\nabla L(w-hv)
}{
2h
}.
$$

To see the connection, expand each gradient around the central point. Their first-order changes have opposite signs, so subtraction doubles the Hessian-vector term. For the constructed quadratic, the equality holds for every nonzero step in exact arithmetic because the gradient is linear.

In floating-point computation, an extremely small step can amplify cancellation error. Testing several moderate step sizes is more informative than trusting one arbitrarily tiny value.

Symmetry supplies another check:

$$
u^\top Hv=v^\top Hu.
$$

If this fails substantially on a smooth deterministic example, inspect the graph, parameter ordering, probe handling, and objective evaluation.

Repeated products used by an eigensolver must refer to the same matrix. Changing the minibatch, dropout mask, parameter values, or normalization state between calls changes the operator. Standard power-iteration reasoning no longer applies directly.

Freezing randomness or using evaluation mode must be an explicit objective choice. Evaluation-mode curvature and training-mode curvature need not describe the same function. A reproducible report records the loss reduction, data subset, model mode, regularizer, and parameter subset.

## Why power iteration works

Start with a unit vector and repeatedly compute

$$
w_{k+1}=Hv_k,
\qquad
v_{k+1}=\frac{w_{k+1}}{\lVert w_{k+1}\rVert_2}.
$$

If a product is zero, normalization is impossible. The current vector lies in the nullspace, so a restart may be needed.

Ignoring the intermediate normalizations, the direction after repeated products is

$$
H^kv_0.
$$

Expand the starting vector in eigenvectors, ordering eigenvalues by magnitude:

$$
v_0=\sum_jc_jq_j.
$$

Then

$$
H^kv_0=\sum_jc_j\lambda_j^kq_j.
$$

Factor out the largest-magnitude eigenvalue:

$$
H^kv_0
=
\lambda_1^k
\left[
c_1q_1+
\sum_{j>1}c_j
\left(\frac{\lambda_j}{\lambda_1}\right)^kq_j
\right].
$$

If its magnitude is strictly greater than the others and the initial coefficient is nonzero, the remaining relative contributions vanish geometrically.

The convergence speed is controlled by

$$
\left|\frac{\lambda_2}{\lambda_1}\right|.
$$

A ratio close to one means slow separation. Equal dominant magnitudes can prevent convergence to a unique direction. A negative dominant eigenvalue can cause alternating signs, which do not prevent the Rayleigh quotient from estimating that negative eigenvalue.

After each iteration, estimate the eigenvalue using

$$
\rho_k=v_k^\top Hv_k.
$$

This requires only the same matrix-vector operation.

## Power iteration carried through numerically

For the earlier constructed Hessian,

$$
H=
\begin{bmatrix}
3&1\\
1&3
\end{bmatrix},
$$

the eigenpairs are

$$
\lambda_+=4,
\qquad
q_+=\frac1{\sqrt2}(1,1)^\top,
$$

and

$$
\lambda_-=2,
\qquad
q_-=\frac1{\sqrt2}(1,-1)^\top.
$$

Start from the first coordinate axis. The first product and normalization give

$$
Hv_0=(3,1)^\top,
\qquad
v_1=\frac1{\sqrt{10}}(3,1)^\top.
$$

The Rayleigh quotient is

$$
\rho_1
=
\frac{(3,1)\cdot(10,6)}{10}
=
\frac{18}{5}
=
3.6.
$$

The next normalized direction is

$$
v_2=\frac1{\sqrt{34}}(5,3)^\top.
$$

Its quotient is

$$
\rho_2
=
\frac{(5,3)\cdot(18,14)}{34}
=
\frac{66}{17}
\approx3.88235.
$$

The relative unwanted eigenvector coefficient halves with every multiplication because the eigenvalue ratio is one-half.

A useful stopping diagnostic is the residual:

$$
r_k=Hv_k-\rho_kv_k.
$$

For the second iterate in this example,

$$
\lVert r_2\rVert_2=\frac8{17}.
$$

A stable-looking quotient can therefore still accompany a noticeable residual.

Expanding the residual in the eigenbasis gives

$$
\lVert Hv-\rho v\rVert_2^2
=
\sum_jc_j^2(\lambda_j-\rho)^2.
$$

At least one eigenvalue must lie within the residual norm of the quotient. But a small residual does not establish that the eigenvalue is the largest: an exact non-dominant eigenvector also has zero residual.

## The indefinite-Hessian correction

Consider

$$
H=
\begin{bmatrix}
-5&0\\
0&2
\end{bmatrix}.
$$

A generic power-iteration start converges in direction toward the first axis because negative five has the largest magnitude. The Rayleigh quotient approaches negative five, even though the largest algebraic eigenvalue is two.

Reporting that result as the “largest positive curvature” would be incorrect.

If a valid spectral lower bound is available, shifting the matrix can make its spectrum nonnegative:

$$
\tilde H=H+\alpha I.
$$

Products remain cheap:

$$
\tilde Hv=Hv+\alpha v.
$$

The eigenvectors are unchanged and every eigenvalue shifts by the same amount. With a shift of six in this example, the eigenvalues become one and eight. Power iteration then identifies eight, from which subtracting the shift recovers two.

The shift must be justified. Choosing an arbitrary shift does not guarantee the intended ordering for an unknown indefinite spectrum. Symmetric Krylov methods can estimate multiple spectral extremes using products, but their outputs likewise require convergence diagnostics.

## Hutchinson's estimator from coordinate expectations

The trace is the sum of diagonal entries and also the sum of eigenvalues:

$$
\operatorname{tr}(H)=\sum_iH_{ii}=\sum_j\lambda_j.
$$

Let a random probe satisfy

$$
\mathbb E[zz^\top]=I.
$$

Independent Rademacher coordinates, each equally likely to be positive or negative one, satisfy this condition. Their squared coordinates are one, while distinct-coordinate products have zero expectation.

Expand the quadratic form:

$$
z^\top Hz=\sum_{i,j}H_{ij}z_iz_j.
$$

Taking expectations gives

$$
\mathbb E[z^\top Hz]
=
\sum_{i,j}H_{ij}\mathbb E[z_iz_j]
=
\sum_iH_{ii}
=
\operatorname{tr}(H).
$$

The off-diagonal contributions disappear in expectation. This is the entire unbiasedness argument.

With independent probes, the estimator is

$$
\hat T=\frac1m\sum_{a=1}^m z_a^\top Hz_a.
$$

Each sample requires one Hessian-vector product and one dot product. Averaging preserves unbiasedness and divides the variance by the number of probes.

Normalization needs care. A random unit direction has

$$
\mathbb E[zz^\top]=\frac1P I
$$

in a parameter space of dimension $$P$$. Its quadratic form estimates average eigenvalue, not trace. Multiplying by the dimension restores a trace estimate.

## Deriving the Rademacher estimator's variance

For a symmetric matrix and Rademacher probe,

$$
z^\top Hz
=
\operatorname{tr}(H)+
2\sum_{i<j}H_{ij}z_iz_j.
$$

The diagonal contribution is deterministic because every squared coordinate equals one.

When the centered expression is squared, cross terms between distinct unordered index pairs have zero expectation. At least one independent sign appears to an odd power. The remaining squared pair terms equal one, giving

$$
\operatorname{Var}(z^\top Hz)
=
4\sum_{i<j}H_{ij}^2
=
2\sum_{i\neq j}H_{ij}^2.
$$

Therefore,

$$
\operatorname{Var}(\hat T)
=
\frac4m\sum_{i<j}H_{ij}^2.
$$

This explains a useful special case: for a diagonal matrix in the chosen coordinates, every Rademacher probe gives the exact trace.

For the constructed two-coordinate Hessian,

$$
z^\top Hz=6+2z_1z_2.
$$

The four possible probes produce

$$
8,\quad4,\quad4,\quad8.
$$

Their mean is six, exactly the trace, and their variance is

$$
\frac{(8-6)^2+(4-6)^2+(4-6)^2+(8-6)^2}{4}
=
4.
$$

An average over independent probes has standard deviation

$$
\frac2{\sqrt m}.
$$

This is the exact sampling variability for the constructed matrix.

Rotating this matrix into its eigenbasis gives a diagonal matrix with eigenvalues four and two. Its trace is still six, but Rademacher probes in those coordinates have zero estimator variance. The trace is coordinate-invariant under orthogonal changes; this probe distribution's variance need not be.

## Trace and extreme eigenvalues summarize different risks

For a positive semidefinite Hessian and perturbation budget,

$$
\lVert\Delta\rVert_2\leq r,
$$

the largest quadratic contribution is

$$
\max_{\lVert\Delta\rVert_2\leq r}
\frac12\Delta^\top H\Delta
=
\frac12r^2\lambda_{\max}.
$$

The eigenbasis expansion proves the upper bound, and a perturbation along the leading eigenvector attains it.

The trace instead connects to an average over isotropic perturbations. Let a random perturbation have mean and covariance

$$
m=\mathbb E[\Delta],
\qquad
C=\mathbb E[(\Delta-m)(\Delta-m)^\top].
$$

Write the perturbation as its mean plus a zero-mean remainder. Expanding the quadratic and taking expectations removes the cross terms:

$$
\mathbb E[\Delta^\top H\Delta]
=
m^\top Hm+\operatorname{tr}(HC).
$$

The expected Taylor change is therefore

$$
\mathbb E[L(w+\Delta)-L(w)]
\approx
g^\top m+
\frac12m^\top Hm+
\frac12\operatorname{tr}(HC).
$$

For zero-mean isotropic perturbations,

$$
C=\tau^2I,
$$

this simplifies to

$$
\mathbb E[L(w+\Delta)-L(w)]
\approx
\frac{\tau^2}{2}\operatorname{tr}(H).
$$

Top eigenvalue and trace are consequently answers to different perturbation models. Their usefulness is not resolved by declaring one universally superior.

For example,

$$
H_A=\operatorname{diag}(6,0),
\qquad
H_B=\operatorname{diag}(3,3)
$$

have equal trace. Their average quadratic response to equal isotropic noise is the same, while the worst directional response is twice as large for the first.

For an indefinite Hessian, trace is signed. The matrix

$$
\operatorname{diag}(10,-10)
$$

has zero trace and substantial curvature in both directions. A near-zero trace is not a certificate of flatness.

## Applying the perturbation model to quantization

Quantization replaces weights with nearby representable values. Its error is a parameter perturbation, so the Taylor expression provides a local sensitivity model.

As a deliberately simplified model, suppose each coordinate's rounding error is independent and uniform over an interval of width $$h$$ centered at zero. Its variance is

$$
\mathbb E[\Delta_i^2]
=
\frac1h\int_{-h/2}^{h/2}u^2\,du
=
\frac{h^2}{12}.
$$

Thus,

$$
C=\frac{h^2}{12}I,
$$

and the predicted average quadratic loss change is

$$
\frac{h^2}{24}\operatorname{tr}(H).
$$

For the constructed Hessian with trace six and interval width one-fifth,

$$
\frac{(1/5)^2}{24}\cdot6=0.01.
$$

Because that loss is exactly quadratic, the Taylor calculation is exact under the stipulated random-error model. Actual deterministic rounding does not automatically generate independent uniform errors. Clipping, unequal scales, correlated weights, and biased errors change the relevant covariance and mean.

For a parameter block, the corresponding Hessian block and perturbation covariance determine its local contribution. Cross-block Hessian terms vanish in expectation only when the assumed cross-covariances and means make them vanish. Independently ranking blocks can miss interactions.

Block size also matters. Trace sums curvature over coordinates; average curvature divides by block dimension. Equal per-coordinate noise and equal total perturbation energy imply different comparisons. A sensitivity report should state the perturbation budget before selecting a normalization.

Calibration statistics do not resolve these issues automatically. Matching activation means and variances constrains moments, not a complete distribution. A symmetric two-point variable and a standard Gaussian both have mean zero and variance one, despite different distributions. Such moment matching cannot by itself establish that calibration inputs reproduce clinically relevant cases.

## Keeping curvature measurements comparable

Loss normalization directly scales curvature. If a loss is multiplied by a constant, its gradient, Hessian eigenvalues, and trace all receive that constant. Summed losses and mean losses cannot be compared as if their curvature values shared a scale.

Adding a squared-norm penalty contributes

$$
\lambda I
$$

to the Hessian. Every eigenvalue increases by the penalty coefficient, and the trace increases by that coefficient times the parameter count. Whether the reported Hessian includes regularization must therefore be explicit.

Parameterization matters too. Under a linear change of variables,

$$
w=Aq,
$$

the transformed Hessian is

$$
H_q=A^\top H_wA.
$$

This follows by applying the chain rule twice. A uniform parameter rescaling can therefore change every curvature value even when the represented predictions are unchanged after the corresponding reparameterization.

Finally, the method should match the question. An HVP reveals response to one chosen direction. Power iteration searches for a dominant spectral direction. Trace estimation averages directional information. None of them directly measures clinical reliance on an input structure; they characterize a declared loss with respect to declared parameters.

## Revision checklist

| Question | What I should be able to derive or check |
|---|---|
| What does the quadratic term approximate? | Derive Taylor's expression by integrating along a perturbation path. |
| When can the linear term be neglected? | Check the actual gradient and perturbation scale. |
| Why does double backward produce a product? | Differentiate the gradient–probe inner product coordinatewise. |
| Why must the probe be fixed? | Identify the additional product-rule term. |
| How can the implementation be checked? | Use the explicit quadratic, finite differences, and symmetry. |
| What does power iteration target? | Order eigenvalues by magnitude and state the initial-overlap condition. |
| What controls convergence speed? | Derive the unwanted-to-dominant eigenvalue ratio. |
| What does a residual establish? | Distinguish proximity to an eigenvalue from identification of the desired one. |
| Why is trace estimation unbiased? | Expand coordinate expectations and cancel off-diagonal terms. |
| What controls Rademacher variance? | Derive the sum of squared off-diagonal entries. |
| Can a small trace hide strong curvature? | Reproduce the positive-and-negative diagonal example. |
| Why use trace or a top eigenvalue for quantization? | State the average or worst-direction perturbation model. |
| What must a report specify? | Record objective, data, model mode, parameterization, regularization, and probe procedure. |

## Why it matters for my work

Curvature can help me study the sensitivity of an ultrasound model to weight perturbation or compression. I need to keep that question separate from sensitivity to clinical evidence in an image, while checking whether compression changes the evidence-use behavior I actually care about.

## What I have not resolved

- Which perturbation model best approximates the quantization scheme I would deploy?
- Compare predicted local loss changes with actual quantization changes and patient-separated clinical faithfulness audits.
