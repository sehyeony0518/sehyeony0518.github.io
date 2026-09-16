---
layout: study_note
title: "Perception as Inference: Illusions Are Not Failures, and the Easy Problems Were the Hard Ones"
description: "Perception as Bayesian inference: retinal-image ambiguity, illumination and reflectance, Gaussian cue integration, decision costs, active sensing, and Moravec's paradox."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "neural-networks"
category_title: "Learning Models & Representation"
subgroup: "Learning & Representation Foundations"
order: 1
source: "Independent study"
written: true
updated: "2026-09-15"
---

Perception estimates hidden properties of the world from measurements that do not uniquely specify them. The task therefore requires assumptions, additional observations, or a willingness to retain uncertainty.

An illusion can reveal those assumptions while still being an error relative to the actual scene. Calling an interpretation rational under a model does not make it physically correct. Nor does the Bayesian formulation prove that the brain performs exact Bayesian calculations.

Moravec's paradox adds a different warning: subjective ease for a human is not a reliable measure of the difficulty of constructing an artificial system. It is a qualitative observation, not a formula relating evolutionary age to computational complexity.

## Forward models explain why perception is an inverse problem

A forward model maps hidden scene properties to observations:

$$
y=f(z)+\epsilon.
$$

Here $$z$$ represents hidden quantities, $$f$$ the measurement process, and $$\epsilon$$ noise or unmodeled variation.

Perception attempts to infer $$z$$ from $$y$$. Even with zero noise, the inverse may not be unique.

A simplified grayscale surface model is

$$
y=\rho\ell,
$$

where reflectance is $$\rho$$ and effective illumination is $$\ell$$. The scalar model assumes away spectral variation, viewing geometry, and other effects so that one ambiguity can be studied clearly.

An observed intensity of 0.2 is consistent with

$$
\rho=0.2,\qquad \ell=1,
$$

and with

$$
\rho=0.4,\qquad \ell=0.5.
$$

Both products equal 0.2. More generally, rescaling one factor and inversely rescaling the other preserves the measurement:

$$
(\rho,\ell)
\longmapsto
(a\rho,\ell/a).
$$

Physical constraints may limit the allowable scale, but do not necessarily identify one solution.

For positive values, taking logarithms gives

$$
\log y=\log\rho+\log\ell.
$$

One observed sum still does not determine its two components. Transforming the equation changes its form, not the amount of information available.

Real color formation involves wavelength-dependent illumination, reflectance, and sensor sensitivity. The simplified product is useful precisely because its assumptions are stated; it should not be mistaken for a complete model of color perception.

## Projection loses depth information

In a pinhole camera, similar triangles give

$$
u=f\frac{X}{Z},
\qquad
v=f\frac{Y}{Z}.
$$

Here $$f$$ is focal length in the chosen image units, and the coordinates are measured relative to the camera.

Multiplying all three spatial coordinates by the same positive factor leaves the image coordinates unchanged:

$$
f\frac{aX}{aZ}=f\frac XZ.
$$

For focal length 100, the points

$$
(1,2,4)
$$

and

$$
(2,4,8)
$$

both project to

$$
(u,v)=(25,50).
$$

A single pixel location specifies a ray, not a unique depth.

A second calibrated viewpoint can add a constraint. For horizontally aligned cameras separated by baseline $$b$$,

$$
u_L=f\frac XZ,
\qquad
u_R=f\frac{X-b}{Z}.
$$

Subtracting gives disparity

$$
d=u_L-u_R=\frac{fb}{Z},
$$

so

$$
Z=\frac{fb}{d}.
$$

The missing step is the cancellation of the unknown horizontal coordinate. Depth becomes identifiable from disparity under the assumed geometry and a correct correspondence.

For

$$
f=100,\qquad b=0.1,\qquad d=5,
$$

the depth is two distance units. Disparities four and six instead produce depths 2.5 and approximately 1.6667.

The sensitivity is

$$
\frac{dZ}{dd}=-\frac{fb}{d^2}.
$$

At disparity five it is negative 0.4 distance units per disparity unit. Small disparity does not merely indicate large depth; it also makes depth more sensitive to disparity error.

More observations can reduce ambiguity while introducing their own calibration and correspondence requirements.

## Deriving Bayes' rule and posterior odds

The joint probability can be factored in two ways:

$$
p(z,y)=p(y\mid z)p(z)=p(z\mid y)p(y).
$$

Dividing by the observation probability gives

$$
p(z\mid y)=\frac{p(y\mid z)p(z)}{p(y)}.
$$

The denominator normalizes the posterior. For discrete hypotheses,

$$
p(y)=\sum_zp(y\mid z)p(z).
$$

For two hypotheses, posterior odds are

$$
\frac{p(z_1\mid y)}{p(z_2\mid y)}
=
\frac{p(y\mid z_1)}{p(y\mid z_2)}
\frac{p(z_1)}{p(z_2)}.
$$

The first factor is the likelihood ratio. It tells us how strongly the observation distinguishes the hypotheses. The second is the prior odds.

If two scene explanations generate the same measurement distribution, their likelihood ratio is one. The observation cannot change their relative odds. A posterior preference then comes from the prior, not from discriminating information in that observation.

That is the mathematical sense in which an underdetermined percept requires assumptions. It does not imply that every confident error can be traced to one simple, human-readable prior.

## A numerical update with an additional cue

Return to two explanations of intensity 0.2:

- A: a dark surface under stronger illumination.
- B: a brighter surface under weaker illumination.

Assume the intensity itself is equally likely under both explanations. Give them prior probabilities

$$
p(A)=0.6,\qquad p(B)=0.4.
$$

Now observe a contextual cue $$C$$ whose specified likelihoods are

$$
p(C\mid A)=0.25,
\qquad
p(C\mid B)=0.75.
$$

The unnormalized posterior masses are

$$
0.6\cdot0.25=0.15,
$$

and

$$
0.4\cdot0.75=0.30.
$$

The normalizing probability is

$$
p(C)=0.15+0.30=0.45.
$$

Thus

$$
p(A\mid C)=\frac13,
\qquad
p(B\mid C)=\frac23.
$$

The same calculation in odds form is

$$
\frac{p(B\mid C)}{p(A\mid C)}
=
\frac{0.75}{0.25}\frac{0.4}{0.6}
=
3\cdot\frac23
=
2.
$$

This is a constructed model, not a measured account of an illusion.

Two observers with different priors can produce different posteriors from the same ambiguous evidence. Their reasoning may be internally consistent while one or both interpretations are wrong about the physical scene. Consistency, accuracy, and calibration are distinct claims.

## Gaussian likelihoods turn inference into regularized optimization

Suppose observations follow a linear model:

$$
y=Az+\epsilon,
\qquad
\epsilon\sim\mathcal N(0,\sigma^2I).
$$

The likelihood is proportional to

$$
\exp\left(
-\frac{\lVert y-Az\rVert_2^2}{2\sigma^2}
\right).
$$

Choose a zero-mean Gaussian prior:

$$
z\sim\mathcal N(0,\tau^2I).
$$

Its density is proportional to

$$
\exp\left(
-\frac{\lVert z\rVert_2^2}{2\tau^2}
\right).
$$

Multiplying likelihood and prior, then taking the negative logarithm, gives the MAP objective

$$
\frac{\lVert y-Az\rVert_2^2}{2\sigma^2}
+
\frac{\lVert z\rVert_2^2}{2\tau^2}.
$$

Terms constant in $$z$$ do not affect the minimizer. Multiplying by $$2\sigma^2$$ yields

$$
\hat z_{\mathrm{MAP}}
=
\arg\min_z
\left[
\lVert y-Az\rVert_2^2
+
\lambda\lVert z\rVert_2^2
\right],
$$

where

$$
\lambda=\frac{\sigma^2}{\tau^2}.
$$

Regularization strength is therefore a relative uncertainty statement under this model: noisier measurements or a tighter prior increase shrinkage.

Differentiate:

$$
2A^{\mathsf T}(Az-y)+2\lambda z=0.
$$

Rearranging produces

$$
(A^{\mathsf T}A+\lambda I)\hat z=A^{\mathsf T}y.
$$

For positive regularization, the matrix is positive definite because for any nonzero vector $$v$$,

$$
v^{\mathsf T}(A^{\mathsf T}A+\lambda I)v
=
\lVert Av\rVert_2^2+\lambda\lVert v\rVert_2^2>0.
$$

The prior can make the optimization solution unique even when the observations alone do not. Uniqueness of the selected estimate is not the same as identifiability from data.

## A regularization example that exposes the bias

Let the observation be

$$
y=z_1+z_2=2.
$$

Without a prior, every pair satisfying the sum is an exact solution.

Among exact solutions, the minimum-norm pair is

$$
(z_1,z_2)=(1,1).
$$

To see this, write

$$
z_2=2-z_1
$$

and minimize

$$
z_1^2+(2-z_1)^2.
$$

Its derivative is

$$
4z_1-4,
$$

which vanishes at one.

Now allow measurement error and use regularization strength one:

$$
L=(2-z_1-z_2)^2+z_1^2+z_2^2.
$$

The normal equations are

$$
\begin{bmatrix}
2&1\\
1&2
\end{bmatrix}
\begin{bmatrix}
z_1\\z_2
\end{bmatrix}
=
\begin{bmatrix}
2\\2
\end{bmatrix}.
$$

By symmetry and substitution,

$$
z_1=z_2=\frac23.
$$

The predicted measurement is four thirds, not two.

The model deliberately accepts a data residual to obtain a smaller latent vector. This is the bias introduced by the prior. It may reduce error under the assumed population, but it does not preserve every observed measurement exactly.

The example separates three ideas often conflated in reconstruction: fitting the measurements, selecting among exact solutions, and balancing approximate fit against a prior.

## Deriving reliability-weighted cue integration

Suppose two independent measurements observe the same scalar quantity:

$$
x_1=z+\epsilon_1,
\qquad
x_2=z+\epsilon_2,
$$

with zero-mean Gaussian noise variances $$s_1^2$$ and $$s_2^2$$.

Under a flat prior, the posterior exponent is

$$
-\frac12
\left[
\frac{(x_1-z)^2}{s_1^2}
+
\frac{(x_2-z)^2}{s_2^2}
\right].
$$

Expanding the squares and collecting terms in $$z$$ gives a quadratic whose precision is

$$
\frac1{s_1^2}+\frac1{s_2^2}.
$$

Completing the square gives posterior variance

$$
v=
\left(
\frac1{s_1^2}+\frac1{s_2^2}
\right)^{-1},
$$

and mean

$$
m=
\frac{
x_1/s_1^2+x_2/s_2^2
}{
1/s_1^2+1/s_2^2
}.
$$

The weights are inverse variances because the Gaussian log-likelihood penalizes a fixed residual more strongly when the cue is more precise.

Choose

$$
x_1=10,\quad s_1^2=4,
\qquad
x_2=14,\quad s_2^2=1.
$$

Then

$$
m=\frac{10/4+14}{1/4+1}=13.2,
$$

and

$$
v=\frac1{1.25}=0.8.
$$

The more precise second cue receives four times the weight of the first.

Add a Gaussian prior with mean 12 and variance four. Its precision adds in the same way:

$$
m_{\mathrm{post}}
=
\frac{10/4+14+12/4}{1/4+1+1/4}
=
13,
$$

$$
v_{\mathrm{post}}=\frac23.
$$

These are consequences of the model assumptions, not universal measurements of human cue integration.

## Correlated errors can create false confidence

Independent evidence accumulates differently from repeated evidence with shared error.

For $$n$$ measurements with equal noise variance $$s^2$$ and pairwise correlation $$\rho$$, the variance of their average is

$$
\operatorname{Var}\left(\frac1n\sum_i\epsilon_i\right)
=
\frac1{n^2}
\sum_{i,j}\operatorname{Cov}(\epsilon_i,\epsilon_j).
$$

There are $$n$$ variance terms and $$n(n-1)$$ off-diagonal covariance terms. Therefore

$$
\operatorname{Var}(\bar\epsilon)
=
\frac{s^2}{n}
\left[1+(n-1)\rho\right].
$$

For two unit-variance measurements with correlation 0.8,

$$
\operatorname{Var}(\bar\epsilon)=0.9.
$$

Assuming independence would incorrectly give 0.5.

Repeated agreement can therefore provide less information than it appears to. Shared acquisition artifacts, common training data, or a common measurement bias can make several outputs fail together.

A posterior can be narrow under a misspecified likelihood. Confidence is conditional on the model used to compute it.

Calibration does not establish complete perceptual understanding either. In a population with positive-label probability one fifth, a constant prediction of one fifth is calibrated but cannot distinguish individual positives from negatives. Reliability and discrimination answer different questions.

## Perception becomes a decision only after costs are specified

A posterior describes beliefs. An action additionally requires a loss function.

For binary state probability

$$
p=P(Y=1\mid x),
$$

suppose a positive action incurs false-positive cost $$c_{FP}$$ and a negative action incurs false-negative cost $$c_{FN}$$. Correct decisions have zero cost.

The expected risks are

$$
R(+)=c_{FP}(1-p),
$$

$$
R(-)=c_{FN}p.
$$

Choose the positive action when

$$
c_{FP}(1-p)<c_{FN}p.
$$

Rearranging gives

$$
p>\frac{c_{FP}}{c_{FP}+c_{FN}}.
$$

A probability threshold of one half is optimal only for equal error costs under these assumptions.

For a constructed alarm problem, let the costs be one and nine. The threshold is 0.1. At posterior probability 0.2, the positive action has risk 0.8 and the negative action has risk 1.8.

The most probable state is still negative. The optimal action differs from the MAP state estimate because the losses are asymmetric.

This is why “infer the most likely explanation” is not a complete account of perception for control. An agent must act under uncertainty, and the consequences of different mistakes matter.

## Active sensing and the value of another observation

Suppose two states are equally likely and an incorrect guess costs one. Without another observation, the minimum expected error is 0.5.

A perfect measurement costing 0.1 reduces the remaining decision error to zero, for total expected cost 0.1.

A noisy measurement that identifies the state correctly with probability 0.8, under a symmetric specified model, leaves expected classification error 0.2. Including the same measurement cost gives total expected cost 0.3.

Both measurements are useful in this construction, but their values differ.

More generally, let a future observation be $$o$$. Before paying a measurement cost, the expected optimized posterior risk satisfies

$$
\sum_o p(o)\min_a R(a\mid o)
\le
\min_a\sum_o p(o)R(a\mid o).
$$

The left side can choose a different action after each observation. The right side must commit to one action for every possible observation.

Under the correct probabilistic model, information cannot increase the minimum expected decision risk when it can be ignored. Acquisition costs, delays, and effects on the world must then be added separately.

An observation need not reduce uncertainty for every realized outcome. Its value is assessed over possible outcomes and in relation to the available actions.

## Moravec's paradox as a problem of hidden state and control

Sensorimotor tasks combine uncertain observation, changing state, action, and feedback. A formal representation is a belief distribution over hidden states.

Given previous belief $$b_{t-1}$$ and action $$a_{t-1}$$, first predict:

$$
\bar b_t(s)
=
\sum_{s'}
p(s\mid s',a_{t-1})b_{t-1}(s').
$$

Then incorporate the new observation:

$$
b_t(s)
=
\eta\,p(o_t\mid s)\bar b_t(s),
$$

where $$\eta$$ normalizes the probabilities.

The first step marginalizes over possible previous states. The second applies Bayes' rule. This is the basic structure of a belief update in a partially observed decision process.

For a constructed two-state environment, suppose the probability that a passage is clear is 0.8. Let the next-step clear probability be 0.9 if previously clear and 0.2 if previously blocked.

The predicted clear probability is

$$
0.8(0.9)+0.2(0.2)=0.76.
$$

A red sensor signal has likelihood 0.1 when clear and 0.8 when blocked. The unnormalized posterior masses are

$$
0.76(0.1)=0.076,
$$

and

$$
0.24(0.8)=0.192.
$$

Thus the posterior probability of blockage is

$$
\frac{0.192}{0.076+0.192}
=
\frac{48}{67}
\approx0.7164.
$$

Choosing whether to proceed now requires action costs and transition consequences, not merely the sensor classification.

This formalization helps explain why an apparently ordinary physical task can hide substantial computation. It does not prove that every sensorimotor task is harder than every symbolic task. Evolutionary familiarity is a plausible part of the historical explanation, not a numerical complexity bound.

## Behavior, mechanisms, and the limits of finite tests

A functional definition of AI and a demand for trustworthy mechanisms are not logical opposites. One can classify a system by its capabilities while separately requiring evidence about reliability, process, and failure modes.

Finite behavioral agreement cannot determine behavior everywhere. Consider two functions:

$$
f(x)=0,
$$

$$
g(x)=x(x-1).
$$

They agree at test inputs zero and one. At one half,

$$
f(1/2)=0,
\qquad
g(1/2)=-\frac14.
$$

Multiplying the second function by an arbitrary constant preserves agreement on the tested points while changing the discrepancy elsewhere.

This construction does not imply that testing is useless. It shows why a claim about generalization requires assumptions connecting tested and untested conditions.

Mechanistic evidence can supply some of those assumptions, but knowing a model's structure does not automatically prove its reliability either. The relevant question is which claim each form of evidence supports.

Perception as inference makes this limitation explicit: conclusions depend on a measurement model, prior information, and a decision objective. Studying failures means examining all three rather than assigning every error to an undifferentiated lack of intelligence.

## Revision checklist

| Can I do this without looking? | Check |
|---|---|
| Construct two scenes with the same scalar intensity. | Explain the reflectance–illumination ambiguity. |
| Derive pinhole projection and depth scaling ambiguity. | Reproduce the two points with identical projections. |
| Derive stereo depth from disparity. | Calculate its sensitivity to disparity error. |
| Derive Bayes' rule from the joint distribution. | Express the update as likelihood ratio times prior odds. |
| Normalize the two-hypothesis cue example. | Obtain posterior probabilities one third and two thirds. |
| Derive MAP as regularized least squares. | Identify the variance ratio controlling regularization. |
| Explain why a unique estimate need not be data-identified. | Reproduce the shrinkage example. |
| Derive Gaussian cue weights. | Obtain means 13.2 and 13 with and without the prior. |
| Calculate the effect of correlated noise. | Explain why two agreeing cues need not halve variance. |
| Derive the cost-sensitive decision threshold. | Distinguish MAP state estimation from action selection. |
| Explain expected value of information. | Include measurement costs and the option to ignore data. |
| Execute a belief-state update. | Obtain blockage probability forty-eight sixty-sevenths. |
| State Moravec's paradox without invented evolutionary arithmetic. | Separate historical explanation from mathematical proof. |

## Why it matters for my work

Medical models also infer hidden states from incomplete measurements. I should separate the measurement model, learned assumptions, probability calibration, and decision costs. A plausible reconstruction or confident classification does not establish that the underlying ambiguity has disappeared.

## What I have not resolved

Identify which characteristic failures in my data follow from measurement ambiguity, which from distribution shift, and which from the chosen loss or decision threshold.
