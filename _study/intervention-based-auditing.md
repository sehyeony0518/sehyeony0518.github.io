---
layout: study_note
title: "Intervention-Based Auditing"
description: "Ablation, masking, and controlled edits as tests of what a prediction actually depends on."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "auditing"
category_title: "Evidence Auditing"
order: 3
source: "Independent study"
written: true
updated: "2026-09-08"
---

The difficult part of an intervention audit is knowing what the edit changed. I want each experiment to test a named dependency while measuring the artifacts and information loss introduced by the test itself.

## Core question and definition

An intervention-based audit changes an input or internal computation and measures the response of a fixed predictor. For a scalar score $$s_f$$ and an edit $$T$$,

$$
\Delta_T(x)=s_f(T(x))-s_f(x).
$$

The sign describes movement in the selected score, not whether the response is desirable. Removing a diagnostic finding can appropriately reduce a disease score; removing peripheral documentation should usually preserve the clinical information available to an image-only task.

I would specify the edit's target, replacement procedure, affected region, expected preserved information, and validity checks before inference. “Remove the lesion” is inadequate because masking, blurring, and synthesizing tissue produce different inputs. The resulting claim concerns the implemented intervention, and expands to a clinical feature only if the edit isolates that feature credibly.

## Key concepts

### Replacement defines the experiment

Zeroing pixels introduces a constant patch and an artificial boundary. Mean filling removes local texture but also creates an unusually homogeneous region. Blurring suppresses fine structure while retaining coarse intensity patterns. Inpainting estimates missing content from surrounding information and its training distribution.

These operations can yield different responses even when their masks are identical. For gallbladder ultrasound, a blurred wall may lose both a clinical feature and speckle structure. An inpainted marker may be replaced by an invented wall contour. I would retain the edited images and record the exact replacement method, parameters, masks, and random seeds.

The position of the edit within the pipeline matters. If the clinical application normalizes after decoding, an edit before normalization can propagate beyond the mask. I would distinguish a test of the complete application from a tensor-level test designed to hold already-normalized surrounding pixels fixed.

### There is a hierarchy of evidence preservation

Removing a separately stored overlay from the identical frozen image is generally a stronger comparison than estimating tissue hidden beneath burned-in pixels. Two neighboring cine frames preserve the patient but may differ in probe angle, breathing phase, and visible morphology. Images from different patients introduce additional biological differences.

I would not collapse these comparisons into a single category of “counterfactual images.” Their strengths differ because the unedited information is controlled differently. An authentic unmarked export still needs verification that dimensions, compression, grayscale mapping, and tissue content match.

Editing anatomy is more demanding. Clinical findings often occur together because they arise from one process. A visually smooth replacement wall may remove irregularity, change thickness, and eliminate small cystic spaces simultaneously. Reader agreement that an image looks realistic is necessary evidence for some edits, but does not establish feature isolation.

### Controls challenge alternative explanations

I would include sham processing, in which the image passes through the editing and export pipeline without changing the target. A control region should be chosen for the suspected artifact: similar area and boundary length for mask-edge effects, or comparable depth and texture for ultrasound appearance changes.

For target edit $$T$$ and control edit $$C$$, a paired contrast is

$$
D(x)=\left[s_f(T(x))-s_f(x)\right]
-\left[s_f(C(x))-s_f(x)\right].
$$

This contrast removes a shared baseline algebraically. It isolates target-specific sensitivity only insofar as the control reproduces relevant nonspecific effects. A same-size patch in a different acoustic compartment may be a poor control despite matching pixel count.

I would compare several defensible replacements when possible. Agreement across them makes one particular editing artifact less plausible, but shared destruction of contextual evidence can still explain the result.

### Retraining answers a different question

[Hooker and colleagues](https://papers.nips.cc/paper_files/paper/2019/hash/fe4b8556000d0f0cae99daa5c5c5a410-Abstract.html) introduced ROAR, Remove And Retrain, to evaluate feature-importance rankings after removing ranked information and retraining models on modified data. Retraining addresses the distribution mismatch created when only test images are corrupted.

For my purpose, that changes the object of inference. A newly trained model can discover alternative cues that the original classifier did not use. ROAR evaluates the usefulness of information under a new learning procedure; a frozen-model audit evaluates the current predictor's response. I would report these experiments separately if both are available.

## Worked examples in medical AI

### Clinical annotations in fetal ultrasound

[Lin and colleagues](https://papers.miccai.org/miccai-2024/695-Paper0423.html) investigated calipers and text as shortcuts in fetal ultrasound segmentation. Clinical annotations correlate with the anatomical planes being documented, and segmentation can fail when a system trained with those cues encounters images without them.

The acquisition sequence explains why the problem matters: annotations are added during documentation, while a live segmentation application may need to operate before they exist. Precise-looking segmentation on stored images therefore does not establish independence from the documentation process.

I take this as motivation for a gallbladder experiment, not evidence that my classifier has the same dependency. I would first inventory which annotations survive export and determine when they become available relative to the intended prediction.

### Caliper removal with a known underlying image

My preferred proposed experiment uses an unmarked frozen gallbladder frame and the same frame with measurement calipers. The target is the annotation layer, not the measured lesion.

I would compare tissue pixels outside the overlay, run both through the deployed pipeline, and record score changes. If source files permit faithful reconstruction, adding the authentic overlay to the unmarked frame gives a complementary insertion test. I would also test sham re-export to detect encoding changes.

If only burned-in calipers exist, I would use more than one reconstruction and ask blinded readers whether the lesion boundary, wall thickness, and attachment remain assessable. Cases where the marker obscures the feature of interest would retain an explicit limitation: the original hidden tissue is unknown.

### Suppressing a stone's posterior shadow

A stone's echogenic appearance and posterior acoustic shadow are related evidence, described in the gallbladder ultrasound review by [Lucius and colleagues](https://pubmed.ncbi.nlm.nih.gov/40566593/). The shadow occupies tissue distal to the suspected stone, so an organ-only mask can exclude part of the relevant image evidence.

In a proposed shadow audit, replacing the distal dark region with surrounding texture does more than erase a dark patch: it invents information that was not visible through the original acoustic path. I would preserve the visible stone boundary, annotate the shadow's origin and extent, and compare edits in nearby regions with similar depth.

A score response would establish sensitivity to the reviewed shadow-suppression operation. I would not call the edited image a stone-free counterfactual, because the visible stone and the patient's reference diagnosis remain unchanged.

## Evaluation methods and limitations

### Evaluate edit validity before selecting model results

Readers assessing edits should be blinded to prediction changes. I would record target modification, preservation of other findings, boundary artifacts, and overall assessability separately. Accepting only edits that produce the expected score change would make the experiment circular.

The report should show the proportion of eligible cases for which an acceptable edit was possible, with rejection reasons. Effects among editable cases may not generalize to small lesions, heavy annotation overlap, or poorly visualized walls. Invalid-edit responses can remain a separate stress test, without supporting the clinical dependence estimate.

Stochastic inpainting requires repeated realizations to characterize reconstruction variability. Those realizations are nested within images and patients. They increase knowledge about edit uncertainty, not the number of independent clinical observations.

### Connect attribution rankings to actual responses

Deletion tests progressively replace highly ranked regions; insertion tests progressively restore them from a specified reference. I would define whether progression is measured by pixels, patches, or anatomical regions and compare with random and simple spatial rankings.

A steep deletion curve can reflect effective destruction of evidence or effective creation of unfamiliar inputs. [Yeh and colleagues](https://papers.nips.cc/paper_files/paper/2019/hash/a7471fdc77b3435276507cc8f2dc2569-Abstract.html) formalize explanation infidelity through disagreement between attribution-predicted effects and perturbation-induced score changes. That framework reinforces my need to specify the perturbation distribution; changing it changes what fidelity means.

I would report paired probability changes, logits where accessible, and decision changes at a fixed threshold. Patient-level resampling should preserve all associated edits. A small average response needs inspection for cancellation, output saturation, incomplete removal, and redundant evidence before receiving a “no reliance” interpretation.

## Research connections and open questions

The first practical question is how often authentic marked and unmarked gallbladder pairs can be recovered. Their availability determines whether the cleanest documentation experiment covers routine cases or only a selected subset.

Second, which inpainting method best preserves reader-assessed wall morphology beneath sparse calipers? I would choose the method using blinded preservation assessments on recoverable examples, then evaluate model effects on separate cases.

Third, does shadow-edit sensitivity exceed sensitivity to comparable distal texture edits, and is that difference concentrated in frames where readers agree the shadow is assessable? This provides a feasible test of a named acoustic-evidence hypothesis while exposing the limits of synthetic reconstruction.

## References

- Hooker et al., [A Benchmark for Interpretability Methods in Deep Neural Networks](https://papers.nips.cc/paper_files/paper/2019/hash/fe4b8556000d0f0cae99daa5c5c5a410-Abstract.html), NeurIPS 2019.
- Lin et al., [Shortcut Learning in Medical Image Segmentation](https://papers.miccai.org/miccai-2024/695-Paper0423.html), MICCAI 2024.
- Lucius et al., [Ultrasound of the Gallbladder: An Update on Measurements, Reference Values, Variants and Frequent Pathologies: A Scoping Review](https://pubmed.ncbi.nlm.nih.gov/40566593/), Life 2025.
- Yeh et al., [On the (In)fidelity and Sensitivity of Explanations](https://papers.nips.cc/paper_files/paper/2019/hash/a7471fdc77b3435276507cc8f2dc2569-Abstract.html), NeurIPS 2019.
