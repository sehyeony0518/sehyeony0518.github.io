---
layout: study_note
title: "Information Theory"
description: "Entropy, mutual information, and KL divergence as ways to quantify how much a signal carries and how far two distributions have moved."
tab: "ai-foundations"
tab_title: "AI Theory"
category: "probability-and-inference"
category_title: "Probability & Statistical Inference"
subgroup: "Latent Variables & Approximate Inference"
order: 8
source: "Independent study"
written: true
updated: "2026-09-08"
---

Information theory starts by specifying a probability distribution. It then measures uncertainty, predictive mismatch, or statistical dependence relative to that distribution.

These are different questions. Entropy describes uncertainty in one variable. Cross-entropy evaluates predictions under another distribution. KL divergence isolates the mismatch between them. Mutual information compares a joint distribution with the distribution it would have under independence.

The derivations below use finite discrete variables unless stated otherwise. Information quantities use base-two logarithms and are measured in bits. The maximum-likelihood section also uses natural logarithms, with the change of units made explicit.

## Why information is measured with a logarithm

An outcome that occurs with certainty should provide no surprise. A less probable outcome should provide more. Independent events should have additive surprise, because observing both combines two separate pieces of information.

Let the surprise associated with a probability be

$$
s(p).
$$

The independence requirement gives

$$
s(pq)=s(p)+s(q),
\qquad
s(1)=0.
$$

Choose the unit so that an event with probability one half carries one bit:

$$
s(1/2)=1.
$$

For a sequence of independent equally likely binary outcomes,

$$
s(2^{-n})=n.
$$

More generally, the additive equation determines the values at rational powers, and continuity extends the result to all positive probabilities. The resulting function is

$$
\boxed{s(p)=-\log_2p}.
$$

The negative sign ensures that probabilities below one produce positive surprise. The base specifies the unit. Natural logarithms instead produce nats:

$$
-\ln p=(\ln2)(-\log_2p).
$$

This construction measures surprise under a modelled distribution. It does not measure importance, truth, or clinical consequence. A rare irrelevant identifier can carry more statistical surprise than a common clinically important finding.

An outcome assigned zero probability has infinite surprise if it occurs. In sums weighted by the true distribution, an impossible outcome contributes zero through the limiting convention

$$
0\log_2 0=0.
$$

The distinction between an impossible true outcome and an observed outcome that a predictive model incorrectly rules out will matter for cross-entropy.

## Entropy as expected surprise

For a discrete random variable with probabilities

$$
p(x)=P(X=x),
$$

entropy is the expected surprise:

$$
\boxed{
H(X)
=
-\sum_xp(x)\log_2p(x)
}.
$$

The probability weights are essential. Entropy describes uncertainty before drawing an outcome, so it averages over how often each surprise will occur.

If one outcome has probability one, the entropy is zero. Every possible draw is already known. Since every nonzero probability is at most one, each surprise term is nonnegative, so discrete entropy cannot be negative.

Consider a constructed source with three symbols:

$$
P(A)=\frac12,
\qquad
P(B)=P(C)=\frac14.
$$

Their surprises are respectively one, two, and two bits. Hence,

$$
H(X)
=
\frac12(1)+\frac14(2)+\frac14(2)
=
1.5\text{ bits}.
$$

There is an exact prefix code with these lengths:

| Symbol | Probability | Code | Length |
| --- | --- | --- | --- |
| A | $$1/2$$ | `0` | One bit |
| B | $$1/4$$ | `10` | Two bits |
| C | $$1/4$$ | `11` | Two bits |

No codeword is the beginning of another, so a stream can be decoded unambiguously. The expected code length is exactly the entropy.

For general probabilities, negative log probabilities need not be integer lengths, so a one-symbol binary code does not necessarily attain entropy exactly. This example demonstrates the coding interpretation where the lengths fit exactly; it should not be stretched into a claim that every entropy is an immediately achievable one-symbol code length.

Formal definitions and coding connections are developed in the [MIT notes on entropy and divergence](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/2243edffb30f57181ed97dcb77691580_MIT6_441S16_chapter_1.pdf).

## Cross-entropy evaluates a predictive distribution

Suppose outcomes are drawn from one distribution but predictions assign probabilities from another:

$$
X\sim P,
\qquad
Q.
$$

The expected surprise according to the predictor is

$$
\boxed{
H(P,Q)
=
-\sum_xp(x)\log_2q(x)
}.
$$

The expectation is still under the distribution generating the observations. The probabilities inside the logarithm come from the predictor. Keeping these roles separate prevents reversing the meaning of the quantity.

Use the same three-symbol source, but predict

$$
Q(A)=\frac14,
\qquad
Q(B)=\frac14,
\qquad
Q(C)=\frac12.
$$

The predictor assigns surprise two bits to the first two symbols and one bit to the third. Therefore,

$$
H(P,Q)
=
\frac12(2)+\frac14(2)+\frac14(1)
=
1.75\text{ bits}.
$$

The predictor spends too much probability on the third symbol and too little on the first. Its expected surprise exceeds the source entropy by one quarter of a bit.

Predictive entropy is different. Computing the entropy of a model's own output probabilities measures how concentrated those reported probabilities are. A model that places all probability on the wrong class has predictive entropy zero while assigning infinite cross-entropy loss to the true class.

Low predictive entropy therefore does not, by itself, establish accuracy or justified confidence.

## KL divergence isolates the mismatch

Subtract entropy from cross-entropy:

$$
H(P,Q)-H(P)
=
-\sum_xp(x)\log_2q(x)
+
\sum_xp(x)\log_2p(x).
$$

Combining the logarithms gives

$$
\boxed{
D_{\mathrm{KL}}(P\Vert Q)
=
\sum_xp(x)\log_2\frac{p(x)}{q(x)}
}.
$$

Thus,

$$
\boxed{
H(P,Q)=H(P)+D_{\mathrm{KL}}(P\Vert Q)
}.
$$

The mismatch is averaged under the true distribution. This explains both the direction of the divergence and its role in prediction: assigning too little probability to outcomes that actually occur incurs a penalty.

For the three-symbol example,

$$
D_{\mathrm{KL}}(P\Vert Q)
=
\frac12\log_2 2
+
\frac14\log_2 1
+
\frac14\log_2\frac12
=
\frac14.
$$

The decomposition is verified numerically:

$$
1.75=1.5+0.25.
$$

### Proving nonnegativity

For a positive number, define

$$
f(u)=u-1-\ln u.
$$

Its derivative is

$$
f'(u)=1-\frac1u.
$$

The function decreases up to one and increases afterwards, with value zero at one. Therefore,

$$
-\ln u\ge1-u.
$$

Apply this inequality with the ratio of predictive to true probability on the support of the true distribution:

$$
\sum_{x:p(x)>0}
p(x)\ln\frac{p(x)}{q(x)}
\ge
\sum_{x:p(x)>0}p(x)
-
\sum_{x:p(x)>0}q(x).
$$

The first sum is one and the second is at most one. Hence the natural-log divergence is nonnegative. Dividing by the positive constant converting nats to bits proves

$$
D_{\mathrm{KL}}(P\Vert Q)\ge0.
$$

Equality requires matching probabilities on the true support and no extra predictive mass outside it, so equality holds exactly when the distributions match.

If the predictor assigns zero probability where the true distribution assigns positive probability, the divergence is infinite.

### Consequences for entropy and asymmetry

Let the reference distribution be uniform over a finite alphabet of size

$$
K.
$$

Then

$$
D_{\mathrm{KL}}(P\Vert U)
=
\sum_xp(x)\log_2p(x)+\log_2K
=
\log_2K-H(P).
$$

Nonnegativity proves

$$
H(P)\le\log_2K,
$$

with equality exactly for the uniform distribution. This derives the claim that entropy is maximised by a uniform distribution over a fixed finite alphabet.

KL divergence is not symmetric. For example, take

$$
P=(1,0),
\qquad
Q=(1/2,1/2).
$$

Then

$$
D_{\mathrm{KL}}(P\Vert Q)=1,
$$

but

$$
D_{\mathrm{KL}}(Q\Vert P)=\infty.
$$

The reverse direction penalises the zero that the first distribution assigns to an outcome occurring under the second. KL divergence consequently is not a distance metric.

## Why cross-entropy loss is maximum likelihood

Suppose a model supplies conditional class probabilities:

$$
q_\theta(y\mid x).
$$

Under the usual conditional independence factorisation for observed training examples, the likelihood is

$$
\mathcal L(\theta)
=
\prod_{i=1}^{N}q_\theta(y_i\mid x_i).
$$

The logarithm is strictly increasing, so maximising the likelihood is equivalent to maximising its logarithm:

$$
\log\mathcal L(\theta)
=
\sum_{i=1}^{N}\log q_\theta(y_i\mid x_i).
$$

Negating and dividing by the sample count gives

$$
\boxed{
-\frac1N\log\mathcal L(\theta)
=
-\frac1N\sum_{i=1}^{N}
\log q_\theta(y_i\mid x_i)
}.
$$

This is the empirical categorical cross-entropy loss for one-hot labels. The equivalence is exact: the same parameter values maximise likelihood and minimise this loss.

It does not depend on a metaphor about information. It follows from multiplying observation probabilities, taking a logarithm, and changing the sign. Using base-two rather than natural logarithms multiplies the objective by a positive constant and leaves its minimiser unchanged.

For a numerical example, suppose a Bernoulli model predicts the same positive probability for four independent observations, of which three are positive:

$$
\mathcal L(\theta)=\theta^3(1-\theta).
$$

Using natural logarithms, the mean negative log-likelihood is

$$
L(\theta)
=
-\frac14\left[3\ln\theta+\ln(1-\theta)\right].
$$

Differentiate:

$$
L'(\theta)
=
\frac14
\left[
-\frac3\theta+\frac1{1-\theta}
\right].
$$

The stationary point satisfies

$$
\frac3\theta=\frac1{1-\theta},
$$

so

$$
3(1-\theta)=\theta,
\qquad
\boxed{\hat\theta=\frac34}.
$$

The second derivative is positive throughout the interior:

$$
L''(\theta)
=
\frac14
\left[
\frac3{\theta^2}
+
\frac1{(1-\theta)^2}
\right]>0.
$$

The solution is therefore the unique interior minimum. Its likelihood is

$$
\left(\frac34\right)^3\left(\frac14\right)
=
\frac{27}{256},
$$

compared with

$$
\left(\frac12\right)^4=\frac1{16}
$$

for a probability of one half.

The minimum mean loss is

$$
-\frac34\ln\frac34-\frac14\ln\frac14
\approx0.562335\text{ nats},
$$

or

$$
-\frac34\log_2\frac34-\frac14\log_2\frac14
\approx0.811278\text{ bits}.
$$

### The softmax gradient follows from the same likelihood

For class logits and a true class index,

$$
q_j=\frac{e^{z_j}}{\sum_re^{z_r}},
\qquad
y,
$$

the natural-log loss is

$$
\ell
=
-\ln q_y
=
-z_y+\ln\sum_re^{z_r}.
$$

Differentiating each logit gives

$$
\boxed{
\frac{\partial\ell}{\partial z_j}
=
q_j-\mathbf1[j=y]
}.
$$

The familiar “prediction minus target” gradient is therefore a derivative of the categorical log-likelihood.

At the population level, conditional cross-entropy decomposes into

$$
\mathbb E_X H\bigl(P(Y\mid X),Q_\theta(Y\mid X)\bigr)
=
H(Y\mid X)
+
\mathbb E_X
D_{\mathrm{KL}}
\bigl(P(Y\mid X)\Vert Q_\theta(Y\mid X)\bigr).
$$

The first term does not depend on the model. Minimising expected cross-entropy therefore minimises the expected conditional mismatch within the chosen model family.

Regularisation, class weighting, and altered target distributions change the overall estimation problem. They should not be silently described as ordinary unpenalised maximum likelihood for the original observed labels.

## Joint entropy, conditional entropy, and mutual information

For two discrete variables, the joint entropy is

$$
H(X,Y)
=
-\sum_{x,y}p(x,y)\log_2p(x,y).
$$

Factor the joint probability:

$$
p(x,y)=p(x)p(y\mid x).
$$

Substituting this factorisation into the logarithm yields

$$
H(X,Y)
=
-\sum_{x,y}p(x,y)\log_2p(x)
-
\sum_{x,y}p(x,y)\log_2p(y\mid x).
$$

The first term reduces to the entropy of the first variable. Define the second as conditional entropy:

$$
H(Y\mid X)
=
-\sum_{x,y}p(x,y)\log_2p(y\mid x).
$$

Hence the entropy chain rule is

$$
\boxed{
H(X,Y)=H(X)+H(Y\mid X)
}.
$$

Conditional entropy is an average of the uncertainty remaining after each possible observation. It is not the entropy at one selected conditioning value.

Now compare the actual joint distribution with the independent distribution formed from its marginals:

$$
\boxed{
I(X;Y)
=
D_{\mathrm{KL}}(P_{XY}\Vert P_XP_Y)
}.
$$

Expanding gives

$$
I(X;Y)
=
\sum_{x,y}p(x,y)
\log_2\frac{p(x,y)}{p(x)p(y)}.
$$

Collecting terms produces

$$
I(X;Y)
=
H(X)+H(Y)-H(X,Y).
$$

Using the entropy chain rule gives two equivalent expressions:

$$
\boxed{
I(X;Y)
=
H(Y)-H(Y\mid X)
=
H(X)-H(X\mid Y)
}.
$$

Mutual information is therefore the average reduction in uncertainty about one variable after observing the other. It is symmetric because the joint-versus-product expression is symmetric.

Its nonnegativity follows from KL nonnegativity. It is zero exactly when the joint equals the product of the marginals, which is the definition of independence.

For discrete variables, conditional entropy is nonnegative, so

$$
I(X;Y)\le\min\{H(X),H(Y)\}.
$$

## Mutual information from an explicit probability table

Construct a joint distribution from eight equally likely outcomes with the following counts:

|  | $$Y=0$$ | $$Y=1$$ | Row total |
| --- | --- | --- | --- |
| $$X=0$$ | $$3/8$$ | $$1/8$$ | $$1/2$$ |
| $$X=1$$ | $$1/8$$ | $$3/8$$ | $$1/2$$ |
| Column total | $$1/2$$ | $$1/2$$ | $$1$$ |

Both marginals are fair binary variables, so each has entropy one bit.

Given either value of the first variable, the second matches it with probability three quarters. Its conditional entropy is

$$
H(Y\mid X)
=
-\frac34\log_2\frac34
-
\frac14\log_2\frac14
\approx0.811278.
$$

Therefore,

$$
I(X;Y)
=
1-0.811278
\approx0.188722\text{ bits}.
$$

The joint-distribution definition gives an independent check. Under independence every cell would have probability one quarter. The diagonal probability ratios are three halves, while the off-diagonal ratios are one half:

$$
I(X;Y)
=
2\left(\frac38\right)\log_2\frac32
+
2\left(\frac18\right)\log_2\frac12.
$$

Thus,

$$
I(X;Y)
=
\frac34\log_2\frac32-\frac14
\approx0.188722.
$$

An individual log ratio can be negative. Here the off-diagonal outcomes are less likely together than independence would predict. Mutual information remains nonnegative because it averages these pointwise contributions over the actual joint distribution.

The result establishes statistical dependence. It does not establish a causal direction or identify the mechanism producing the dependence.

## Conditional mutual information can increase after conditioning

Define conditional mutual information as an average divergence within conditioning strata:

$$
I(X;Y\mid Z)
=
\sum_zp(z)
D_{\mathrm{KL}}
\left(
P_{XY\mid z}
\Vert
P_{X\mid z}P_{Y\mid z}
\right).
$$

Each divergence is nonnegative, so the average is nonnegative. Expanding the logarithms gives

$$
I(X;Y\mid Z)
=
H(Y\mid Z)-H(Y\mid X,Z).
$$

It is incorrect to assume that adding conditioning always decreases mutual information.

For a constructed counterexample, let two inputs be independent fair bits and define the output by exclusive OR:

$$
Y=X\mathbin{\mathrm{XOR}}Z.
$$

Without knowing the second input, the output is equally likely to be either bit for each value of the first:

$$
I(X;Y)=0.
$$

Once the second input is known, the first input determines the output exactly:

$$
H(Y\mid Z)=1,
\qquad
H(Y\mid X,Z)=0.
$$

Therefore,

$$
I(X;Y\mid Z)=1.
$$

Conditioning exposed a dependency that was absent marginally. In an audit, adding device or site variables is consequently a substantive change to the question, not an automatic improvement or a general guarantee of removing confounding.

## The data processing inequality and its proof

Suppose an observation is processed into a representation without additional target information entering the computation:

$$
Y\longrightarrow X\longrightarrow Z.
$$

The Markov condition means

$$
P(Z\mid X,Y)=P(Z\mid X).
$$

Given the observation, knowing the target supplies no further information about how the representation is produced. A fixed deterministic encoder satisfies this condition, as does a random encoder whose randomness is conditionally independent of the target.

The data processing inequality states

$$
\boxed{
I(Y;Z)\le I(Y;X)
}.
$$

To prove it, first obtain a chain rule for mutual information:

$$
I(Y;X,Z)
=
I(Y;X)+I(Y;Z\mid X).
$$

This follows by writing both terms on the right as entropy differences; the intermediate conditional entropies cancel. Reversing the order gives another expansion:

$$
I(Y;X,Z)
=
I(Y;Z)+I(Y;X\mid Z).
$$

The Markov condition makes the first expansion's conditional information term zero:

$$
I(Y;Z\mid X)=0.
$$

Equating the expansions yields

$$
I(Y;X)
=
I(Y;Z)+I(Y;X\mid Z).
$$

Conditional mutual information is nonnegative, so the inequality follows. This proof and related properties are developed in the [MIT notes on mutual information](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/184197ca5d5418da2415d37e929860b9_MIT6_441S16_chapter_2.pdf).

The equation also identifies the information lost:

$$
I(Y;X)-I(Y;Z)=I(Y;X\mid Z).
$$

Equality holds precisely when the representation leaves no additional target information in the original observation. It can discard irrelevant input details while preserving everything needed for the specified target.

## What processing can preserve, expose, and destroy

Let two independent fair bits form an observation:

$$
X=(A,B),
\qquad
Y=A.
$$

The full observation determines the target, so

$$
I(Y;X)=1.
$$

If the representation keeps the first bit,

$$
Z=A,
$$

then

$$
I(Y;Z)=1.
$$

The representation has reduced the input from two bits to one while retaining all target information.

If it instead keeps the second bit,

$$
Z=B,
$$

then independence gives

$$
I(Y;Z)=0.
$$

No subsequent function of that representation alone can recover target information: applying data processing again leaves its mutual information at zero.

Processing can nevertheless make information easier for a restricted decoder to use. Consider an observation made of two independent signs, with a target indicating whether the signs match. The target is already determined by the pair. The transformed feature

$$
Z=X_1X_2
$$

makes the target directly readable from a single coordinate.

A linear classifier on the original two coordinates cannot separate matching from nonmatching corners: the two class convex hulls intersect at the origin. A threshold on the product can separate them. The transformation improved accessibility for that decoder without creating target information.

With unrestricted decision rules, an observer of the original input could first compute the representation and then apply any representation-based rule. Processing cannot provide an informational advantage over unrestricted access to its own input.

The qualification about extra information is essential for learned encoders. If parameters contain information about the same evaluation targets, the representation depends on more than the test input. For a frozen encoder and fresh evaluation cases, the corresponding inequality can be stated conditional on the learned parameters:

$$
I(Y;Z\mid\Theta)\le I(Y;X\mid\Theta),
$$

provided the conditional Markov assumption holds. Memorisation or side information does not violate data processing; it changes the variables entering the computation.

## Continuous variables and finite-sample estimates need care

Replacing sums with integrals produces differential entropy, but its behaviour differs from discrete entropy.

For a continuous variable with density and a positive scaling,

$$
V=aU,
\qquad
f_V(v)=\frac1a f_U(v/a).
$$

Substituting this density into the differential-entropy integral and changing variables gives

$$
h(V)=h(U)+\log_2a.
$$

A uniform variable on the unit interval has differential entropy zero. Scaling it to an interval of length one half gives differential entropy negative one bit. This is a change of measurement scale, not negative uncertainty in the discrete coding sense.

Mutual information behaves more consistently under invertible transformations. Applying data processing to an invertible mapping gives one inequality; applying it to the inverse gives the reverse inequality. Therefore, the information is unchanged.

Estimation introduces a separate difficulty. Consider random identifiers independent of balanced binary labels. In a finite sample where every identifier is unique, an empirical table assigns exactly one observed label to each identifier. It therefore reports

$$
\widehat H(Y\mid\mathrm{ID})=0.
$$

If the sample labels are balanced, the resulting empirical mutual information is one bit, even though the generating variables are independent.

The apparent dependence comes from fitting the empirical distribution too finely. More representation dimensions or finer bins can create more such opportunities. An information estimate must therefore be interpreted with its estimator, sample size, partitioning, and evaluation design.

Finally, the data processing inequality concerns true information quantities under a specified joint distribution. Two finite-sample estimates can appear to violate it through estimation error or incompatible sampling. Such a comparison should first trigger a check of those assumptions.

## Revision checklist

| Question | What I should be able to reconstruct |
| --- | --- |
| Why use a logarithm for surprise? | Independent probabilities multiply while their information should add. |
| What does entropy average? | Negative log probability under the same distribution that generates outcomes. |
| What changes in cross-entropy? | Outcomes follow the true distribution; log probabilities come from the predictor. |
| How are entropy, cross-entropy, and KL related? | Cross-entropy equals entropy plus the forward KL mismatch. |
| Why is KL nonnegative? | Apply the elementary logarithm inequality and check support conditions. |
| Why is the uniform distribution maximally uncertain? | Its KL divergence from any distribution equals maximum entropy minus actual entropy. |
| Why is cross-entropy maximum likelihood? | Negative log likelihood turns the product of observation probabilities into the cross-entropy sum. |
| What does mutual information compare? | The actual joint distribution with the product of its marginals. |
| Can conditioning increase mutual information? | Yes; the exclusive-OR construction gives an exact example. |
| What assumption supports data processing? | The representation receives no target information beyond the observation. |
| When does processing preserve all target information? | The original observation adds no target information conditional on the representation. |
| Can decoding improve without information increasing? | Yes; a representation can expose existing information to a restricted readout. |
| Why distrust an unqualified empirical information value? | Finite-sample fitting, discretisation, and dimensionality can create misleading estimates. |

## Why it matters for my work

In ultrasound auditing, I need to name the variable, population, and conditioning set before interpreting an information quantity. Dependence between a readout and a clinical descriptor can support a statistical claim, while evidence validity still requires checking what the model uses and how that relationship behaves under meaningful interventions.

## What I have not resolved

Which dependence estimates remain credible with limited independently annotated patients, and which conditioning choices clarify the audit question without introducing a different association?
