---
layout: study_note
title: "Resampling and Anti-Aliasing: Why Half of a Checkerboard Is Grey"
description: "What downsampling does to a spectrum, why the filter has to come first, and the resize call that has been quietly changing benchmark results for years."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "learning-principles"
category_title: "Learning Principles"
order: 11
source: "Independent study"
written: true
updated: "2026-09-15"
---

Here is the whole problem in one example.

Take a $$512\times512$$ image of a perfect checkerboard, alternating black and white pixel by pixel. Resize it to $$256\times256$$. What should it look like?

Not black. Not white. **Grey** — because each output pixel covers two input pixels, one of each, and their average is grey. Now take every other pixel, which is what downsampling literally means, and the result is uniformly *white*. Every black pixel landed on an odd index and was discarded.

In one dimension: the sequence $$1,-1,1,-1,\dots$$ downsampled by 2 gives $$1,1,1,1,\dots$$, while the true local mean is $$0,0,0,0,\dots$$. The output is not slightly off. It is maximally wrong, it contains no trace of the structure it destroyed, and it looks like a perfectly clean image.

## Core question and definition

Downsampling by $$M$$ keeps $$x_d[n] = x[nM]$$. In the frequency domain this **stretches** the spectrum by $$M$$ and superimposes $$M$$ shifted copies:

$$
X_d(e^{j\omega}) = \frac{1}{M}\sum_{i=0}^{M-1} X\!\left(e^{j(\omega - 2\pi i)/M}\right).
$$

If the original spectrum extends beyond $$\pi/M$$, the stretched copies overlap, and overlapping is irreversible — once two frequency components have been summed there is no operation that separates them again. That is **aliasing**, and high frequencies do not vanish; they reappear masquerading as low ones. The checkerboard is the extreme case: content at exactly $$\pi$$ aliases to exactly $$0$$, and alternating black-and-white becomes flat white.

The fix follows immediately. Everything above $$\pi/M$$ is going to cause damage, so remove it *before* downsampling:

> **Decimation** = lowpass filter with cutoff $$\pi/M$$, **then** downsample by $$M$$.

Running the checkerboard through even a crude 3-tap filter first gives $$0,0,0,\dots$$ — grey, the right answer. The information at $$\pi$$ is still lost, as it must be, but it is lost *honestly* rather than being folded into the output as a fabricated constant.

## Key concepts

### Upsampling is the mirror image

Upsampling by $$L$$ inserts $$L-1$$ zeros between samples. In frequency this **compresses** the spectrum, which means $$L-1$$ unwanted copies — spectral images — now sit inside the band. There is no aliasing to worry about, since nothing overlapped, but the images are artefacts and have to go:

> **Interpolation** = upsample by $$L$$ (insert zeros), **then** lowpass filter with cutoff $$\pi/L$$ and gain $$L$$.

The gain is not cosmetic. Only one in $$L$$ samples is non-zero, so everything has been attenuated by exactly that factor and multiplying it back is restoring what the zero-stuffing removed.

### Rational resampling, and why the order matters

To resample by $$L/M$$ — say 7/16 — do **not** decimate then interpolate. Downsampling first destroys frequency content that the subsequent upsampling cannot recover, and the result is band-limited far more aggressively than the target rate requires.

Upsample first, then downsample. And because the two stages put a lowpass filter back to back, they collapse into one with cutoff $$\min(\pi/L,\ \pi/M)$$ and gain $$L$$ — cheaper and better than doing it in the wrong order.

Concretely, moving audio from 40 kHz to 10 kHz means $$M = 4$$, and it means a lowpass at $$\pi/4$$ before the decimation, not after and not instead.

## Why it matters for my work

This one is not a metaphor. It is a defect that is actually present in machine-learning pipelines, including ones whose results are in print.

**Resize functions disagree about anti-aliasing.** PIL applies a proper filter by default; several deep-learning frameworks' resize operations historically did not, and some still do not unless a flag is set. The resulting images differ, and the difference is large enough to move benchmark numbers on its own — documented in detail for GAN evaluation, where the choice of resize implementation shifts FID scores by amounts comparable to the differences between methods being compared.[^parmar] A pipeline detail nobody wrote down, deciding a published ranking.

**Strided convolution and pooling are downsampling without a filter.** A stride-2 convolution is decimation with no anti-aliasing stage, which is why CNNs are far less shift-invariant than their architecture suggests, and why inserting a blur before each downsampling step measurably improves both stability and accuracy.[^zhang] The architecture diagram does not show this; the aliasing is in the operation itself.

**For medical imaging the consequence is specific and unpleasant.** Resampling to a common voxel spacing is routine preprocessing, and different scanners supply different native spacings, so each source gets a *different resampling ratio*. Without proper anti-aliasing, each ratio produces its own characteristic aliasing pattern — which means the preprocessing stamps a scanner-dependent texture signature onto every image. That is a [shortcut](/study/shortcut-learning-in-medical-imaging/) manufactured by the pipeline rather than present in the data, it correlates perfectly with site, and site correlates with prevalence, population, and outcome. A model can learn it, [external validation across those same sites will not catch it](/study/robustness-subgroup-performance-and-external-validation/), and no attribution method will name it, because the artefact is spread across the whole image rather than localised anywhere an explanation could point.

The checkerboard is worth keeping as the mental image. The failure produced a clean, plausible, entirely uniform result, and the only way to know it was wrong was to know what the answer *should* have been. Aliasing does not look like corruption. It looks like data.

---

[^parmar]: Parmar, G., Zhang, R., & Zhu, J.-Y. (2022). On aliased resizing and surprising subtleties in GAN evaluation. *CVPR 2022*, 11410–11420. [10.1109/CVPR52688.2022.01112](https://doi.org/10.1109/CVPR52688.2022.01112)

[^zhang]: Zhang, R. (2019). Making convolutional networks shift-invariant again. *ICML 2019*. [arXiv:1904.11486](https://arxiv.org/abs/1904.11486)
