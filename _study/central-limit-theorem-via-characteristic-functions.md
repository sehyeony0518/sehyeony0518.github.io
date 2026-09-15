---
layout: study_note
title: "The Central Limit Theorem, via Characteristic Functions"
description: "Why sums of independent quantities turn Gaussian, shown by the transform that turns convolution into multiplication."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "probability-and-inference"
category_title: "Probability & Statistical Inference"
order: 5
source: "Independent study"
written: true
updated: "2026-09-15"
---

Adding independent random quantities produces something Gaussian almost regardless of what was added. That is the reason Gaussian assumptions are so often defensible, and the cleanest route to it runs through a transform that converts the hard operation into an easy one.

## Core question and definition

The **characteristic function** of a random variable is the expected complex exponential

$$
\varphi_X(\omega) = \mathbb{E}\!\left[e^{i\omega X}\right],
$$

which is the Fourier transform of its density with the sign convention flipped. For a zero-mean Gaussian with variance $$\sigma^2$$, completing the square in the exponent gives

$$
\varphi(\omega) = e^{-\sigma^2\omega^2/2},
$$

so a Gaussian transforms to a Gaussian in $$\omega$$, with the variance inverted in role.

## Key concepts

### Adding variables convolves densities, and convolution becomes a product

If $$X$$ and $$Y$$ are independent and $$Z = X + Y$$, then for $$Z$$ to equal $$z$$, $$Y$$ must supply whatever $$X$$ did not:

$$
p_Z(z) = \int p_X(x)\, p_Y(z-x)\,dx,
$$

which is a convolution. Under the Fourier transform convolution becomes multiplication, so

$$
\varphi_Z(\omega) = \varphi_X(\omega)\,\varphi_Y(\omega).
$$

For $$n$$ independent and identically distributed variables the characteristic function is simply raised to the $$n$$-th power. An operation that was an $$n$$-fold integral becomes an exponent — which is the whole reason for working in this domain.

### A second-order expansion is enough

Take $$X_i$$ with mean zero and variance $$\sigma^2$$, and scale the sum so its variance does not grow:

$$
Z_n = \frac{1}{\sqrt{n}}\sum_{i=1}^n X_i .
$$

Expanding the characteristic function about $$\omega = 0$$, the constant term is $$1$$, the first-order term vanishes because the mean is zero, and the second-order term carries the variance:

$$
\varphi_X(\omega) = 1 - \tfrac{1}{2}\sigma^2\omega^2 + o(\omega^2).
$$

The scaling puts $$\omega/\sqrt{n}$$ into each factor, so

$$
\varphi_{Z_n}(\omega) = \left[\varphi_X\!\left(\tfrac{\omega}{\sqrt n}\right)\right]^n
= \left[1 - \frac{\sigma^2\omega^2}{2n} + o\!\left(\tfrac{1}{n}\right)\right]^n
\;\longrightarrow\; e^{-\sigma^2\omega^2/2}.
$$

The limit on the right is a Gaussian's characteristic function, and therefore $$Z_n$$ is asymptotically Gaussian. [Lindeberg](https://doi.org/10.1007/BF01494395) (1922) gave the derivation in a form close to this.

Two features are worth naming. Nothing beyond the mean and variance of $$X$$ survived the limit — every higher moment sat in the $$o(\omega^2)$$ term and was scaled away. And the argument needed only two derivatives at the origin, which is why the theorem holds for such a wide class of distributions.

### What the theorem does not license

It is a statement about a scaled sum in the limit. It says nothing about how quickly the approximation becomes usable, and convergence is slowest exactly where it usually matters — in the tails. A distribution can be visually Gaussian in its body while its extreme quantiles are badly wrong, and extreme quantiles are what a decision threshold sits on.

It also requires finite variance, and independence. Correlated summands can converge to something else or not converge at all.

## Where this touches my work

This is the licence behind the Gaussian noise assumptions that appear throughout imaging, and it is a real licence: a measurement disturbed by many small independent effects has a good claim to being Gaussian. That claim is what makes the [Wiener filter's](/study/linear-mmse-and-the-wiener-filter/) setup reasonable rather than merely convenient.

The caution I take is about the failure cases rather than the theorem. Ultrasound speckle is not the sum of many independent small effects but interference from scatterers, which is why it is not Gaussian and why filters derived on Gaussian assumptions behave oddly on it. Knowing which conditions produce the theorem is the same as knowing when to distrust it.

The forgetting property has a second use. Since only the first two moments survive, two very different underlying processes can produce the same limit — so an observed Gaussian says little about what generated it. That cuts against reasoning backwards from a distribution's shape to a mechanism.

## What I have not resolved

How badly the independence assumption is violated by the acquisition processes I care about, where consecutive frames share an operator, a machine and a patient, and where whatever is common to them is exactly what an audit wants to detect.

## References

- Lindeberg (1922). [Eine neue Herleitung des Exponentialgesetzes in der Wahrscheinlichkeitsrechnung](https://doi.org/10.1007/BF01494395). *Mathematische Zeitschrift*.
