---
layout: post
title: "Stress Testing Reveals Gaps in Clinic Readiness of Image-Based Diagnostic Artificial Intelligence Models"
date: 2026-08-16 12:00:00 +0900
venue: "npj Digital Medicine"
authors: "Albert T. Young, Kristen Fernandez, Jacob Pfau, Rasika Reddy, Nhat Anh Cao, Max Y. von Franque, Arjun Johal, Benjamin V. Wu, Rachel R. Wu, Jennifer Y. Chen, Raj P. Fadadu, Juan A. Vasquez, Andrew Tam, Michael J. Keiser, Maria L. Wei (2021)"
description: "A skin-lesion classifier at dermatologist-level AUC gave false positive or negative predictions for up to 22% of lesions under a simple image rotation, a direct test of whether an acceptable benchmark score means the model is ready for a clinic."
og_image: "https://sehyeony0518.github.io/assets/img/og/2026-08-16-stress-testing-clinic-readiness-dermatology.png"
related_posts: false
---

**Paper.** *Stress testing reveals gaps in clinic readiness of image-based diagnostic artificial intelligence models*. [npj Digital Medicine (2021)](https://doi.org/10.1038/s41746-020-00380-6)

This paper asks whether models that perform well in a controlled comparison with dermatologists also satisfy practical requirements for use. The open question concerns the gap between ranking lesions correctly in a benchmark and behaving dependably when images are acquired, selected, and interpreted in a clinic. I read it because that gap is easy to overlook when AUROC becomes the main result and ordinary acquisition variation becomes an optional appendix.

The study is broader than a rotation experiment. The authors develop melanoma-versus-nevus classifiers and examine discrimination, calibration, unfamiliar disease classes, selective prediction, repeated capture, and image transformations. Their evaluation includes seven test datasets spanning curated and less curated settings. This matters because computational stress testing and external evaluation appear together. The paper does not suggest that modifying one fixed test set can replace evaluation on genuinely different clinical data.

The models use a common SE-ResNet-50 architecture with different development-data combinations and ensemble predictions. This provides a way to investigate data composition while retaining a shared architectural basis. The authors also examine standard training and a loss intended to support opting out of difficult predictions. The resulting evidence concerns these development procedures and datasets. It should not be generalized into a statement that every dermatology classifier has the same failure rate.

Across the reported transformation tests, inconsistent predictions produced false positive or negative results for 6.5–22% of lesions. That range should be attributed to the tested transformations and datasets collectively, not exclusively to rotation. The transformations include changes such as brightness, contrast, flipping, and rotation. The result is clinically relevant because these operations can resemble incidental image variation, but it is not an estimate that 22% of patients in routine care would necessarily receive a wrong decision.

Repeated capture is a separate experiment. For the representative model in one teledermatology dataset, 24 of 79 lesions with replicated images crossed the selected decision threshold between captures. This comparison keeps lesion identity fixed while allowing image acquisition to vary. It demonstrates that the image presented can affect the decision. It does not establish that every disagreement is caused by an invalid cue, because different views can reveal different amounts of diagnostic information.

That distinction determines how a stress result should be judged. Rotating an otherwise unchanged image often motivates an invariance expectation. Taking a new view can change visibility, focus, or the part of a lesion represented. A prediction should remain stable when the relevant evidence is preserved, but may reasonably change when better evidence becomes available. A useful audit needs to record which kind of variation the paired images contain.

Threshold crossings also need context. A tiny score change near a decision boundary can alter a binary output, while a larger change far from the boundary can leave the assigned class unchanged. Neither the flip rate nor the mean score difference is sufficient alone. I would examine both, together with the direction of the error and the confidence of the resulting prediction. That would distinguish numerical instability from changes likely to alter the intended clinical action.

The calibration results address another weakness. Calibration on development data did not ensure adequate calibration in the evaluated test settings, and the paper reports remaining overconfidence. This makes the claim stronger than “the scores sometimes move.” A model can give unstable answers while presenting confidence that encourages reliance. Conversely, a stable output can still be miscalibrated. Robustness, calibration, and discrimination are different properties of the same predictor.

The unfamiliar-disease tests also expose a task-definition problem. A classifier trained to distinguish two categories will encounter images outside that distinction if the clinical input stream is broader. A confident output then need not mean that the image belongs to either learned class. Adding a rejection mechanism creates another prediction task: identify cases for which the system should withhold its answer. Its usefulness must be evaluated rather than inferred from the existence of an opt-out option.

The main limitation is that a collection of stress tests cannot reproduce the complete clinical distribution. The selected transformations have specified ranges and frequencies, and those choices shape the observed failures. Stronger perturbations can destroy valid evidence. Real clinical failures can also arise through missing history, unexpected diagnoses, or image selection, none of which is necessarily captured by a digital transformation. The paper supplies concrete failure conditions, not a complete model of deployment risk.

For an ultrasound study, I would separate changes that preserve the finding from changes that reduce its assessability. A brightness change might preserve the lesion outline while weakening a faint acoustic effect; a crop might remove the reference tissue needed to judge echogenicity. Clinicians reviewing the stress conditions should assess these effects before seeing the model response. Otherwise, an appropriate response to missing evidence could be counted as a robustness failure.

I would preserve a prespecified operating rule during the main stress evaluation and report lesion- or patient-level uncertainty. Multiple transformed versions of one image are repeated measurements, not additional independent patients. If a revised threshold or augmentation scheme is proposed after inspecting the failures, its benefit should be assessed on separate data. This keeps discovery of fragility distinct from evidence that the proposed remedy works.

The paper supports [Evaluation Beyond AUROC](/study/evaluation-beyond-auroc/) by demonstrating why acceptable ranking does not settle behavior at a clinical operating point. It also supports [Calibration, Uncertainty, and Selective Prediction](/study/calibration-uncertainty-and-selective-prediction/): confidence and rejection must be evaluated in the population where they will influence decisions.

[Ultrasound Acquisition Variability and Image Quality](/study/ultrasound-acquisition-variability-and-image-quality/) adds the condition needed for transfer to my work. Stability is desirable when the evidence is preserved, while loss of evidence should change confidence or trigger review. I would use this paper to justify a paired acquisition and transformation evaluation alongside external validation, with the preserved clinical information stated for every stress condition.
