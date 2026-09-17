---
layout: post
title: "Noninvasive Quantitative Estimation of Hepatic Steatosis by Ultrasound: A Comparison of the Hepato-Renal Index and Ultrasound Attenuation Index"
date: 2026-01-14 12:00:00 +0900
venue: "Medical Ultrasonography"
authors: "Heon-Ju Kwon, Kyoung Won Kim, Jin-Hee Jung, Sang Hyun Choi, Woo Kyoung Jeong, Bohyun Kim, Gi-Won Song, Sung-Gyu Lee (2016)"
description: "A head-to-head comparison of two classical ultrasound-based liver-fat indices in living liver-donor candidates, against biopsy, the pair of legible baselines that any liver-steatosis deep model is implicitly competing with."
og_image: "https://sehyeony0518.github.io/assets/img/og/2026-01-14-hepatorenal-index-attenuation-index.png"
related_posts: false
---

**Paper.** *Noninvasive quantitative estimation of hepatic steatosis by ultrasound: a comparison of the hepato-renal index and ultrasound attenuation index.*

The paper asks whether two explicit ultrasound measurements can estimate hepatic steatosis and distinguish clinically defined levels of fat on biopsy. The comparison is useful because the measurements describe different aspects of the image. The hepatorenal index uses relative echogenicity between liver and kidney, whereas the attenuation index uses depth-dependent signal loss. Both provide an interpretable alternative to simply asking a reader or network for a categorical impression.

The question was open because a plausible physical or anatomical relationship does not establish diagnostic performance. A liver can appear bright for reasons involving tissue, acquisition, and display. Likewise, a depth-dependent intensity pattern may contain both tissue information and system effects. A quantitative index needs evaluation against an independent reference, and comparison within the same patients is more informative than comparing headline results from unrelated cohorts.

The study evaluates 224 potential living liver donors who underwent ultrasound and subsequent ultrasound-guided biopsy. The attenuation index was calculated from images acquired with an 8 MHz transducer. HRI was measured on sagittal images showing both liver and kidney. The authors compare the indices against histological steatosis thresholds of at least 5% and at least 30%, and assess interobserver agreement.

For the 5% threshold, the reported AUCs are 0.856 for HRI and 0.820 for the attenuation index. For the 30% threshold, they are 0.937 and 0.909. The differences are not statistically significant. Interobserver ICCs are 0.973 for HRI and 0.931 for attenuation. The paper also reports Bland–Altman assessment of differences between readers. These are results under this cohort and measurement procedure, not universal performance characteristics of either index.

The paired comparison is an important strength. Both methods are assessed in the same clinical population against the same type of reference, reducing the ambiguity that would arise from comparing separate publications. The numerical ordering favors HRI in this experiment. Nevertheless, the evidence does not establish a definitive superiority claim simply because one point estimate is larger. Equally, failure to find a statistically significant difference does not establish equivalence.

The two thresholds answer different classification questions. A result for detecting at least 30% steatosis cannot be used as the accuracy for detecting any steatosis. The distribution of cases around a threshold also matters. Separating markedly fatty from clearly nonfatty livers can be easier than distinguishing patients near a low cutoff. A usable review should therefore preserve the target threshold alongside each performance estimate.

Correlation, discrimination, and quantitative agreement also need to remain separate. A measurement can increase consistently with histological fat while still giving biased numerical estimates. It can rank patients well but make clinically relevant errors near a decision boundary. If the intended use is to estimate a fat percentage, evaluating only AUC would leave the magnitude and direction of estimation error unresolved.

The agreement results are encouraging, but their scope is narrower than complete reproducibility. Reader agreement in extracting measurements from available images does not automatically include variation from repeating the scan, changing the operator, selecting a new view, or using another scanner. The existing review does not establish how fully the study separated acquisition variability from subsequent measurement variability. I would not describe the ICCs as evidence covering all of those stages.

An ICC also depends on the spread of the measured population. When patients differ substantially from one another, measurements can preserve their ordering despite differences that matter near a cutoff. Absolute reader differences therefore provide information that an ICC alone cannot. This is why the paper's agreement analysis is relevant to a reader considering implementation, rather than simply adding another high number to the abstract.

The donor population is the most consequential external-validity limitation. Potential living donors are selected through a clinical process that differs from routine evaluation of patients with suspected chronic liver disease. The prevalence and spectrum of steatosis, accompanying disease, and technically difficult examinations may differ. The study supports considering these indices in comparable patients; it does not establish their accuracy throughout every hepatology or screening population.

HRI also relies on a reference tissue within the image. Using a ratio may reduce some common intensity effects, but it cannot be assumed to cancel all acquisition differences. Liver and kidney must be visualized and measured appropriately, and the meaning of the denominator must remain suitable. Similarly, an attenuation index calculated from displayed images should not automatically be equated with every later quantitative attenuation implementation. The measurement definition is part of the method.

The connection to [Abdominal Ultrasound Physics and Image Formation]({{ '/study/abdominal-ultrasound-physics-and-image-formation/' | relative_url }}) is direct: brightness and depth-dependent signal are produced jointly by tissue and the acquisition pipeline. The study supplies clinically legible measurements, while the note explains why their apparent simplicity does not remove the need to control imaging conditions.

[Label Quality and Interobserver Variability]({{ '/study/label-quality-and-interobserver-variability/' | relative_url }}) helps interpret the agreement analysis, especially its distinction between association and agreement. [Evaluation Beyond AUROC]({{ '/study/evaluation-beyond-auroc/' | relative_url }}) adds the missing decision perspective: a proposed donor-assessment use would need a threshold, error consequences, and an account of what happens after a positive or uncertain result.

For a learned liver-steatosis model, I would use HRI and the attenuation index as serious baselines on the same evaluation patients. If manual regions are supplied to the classical methods, that annotation assistance should be disclosed. I would ask whether the network adds discrimination, reduces measurement burden, handles more examinations, or improves repeatability, rather than treating any increase in complexity as progress.

Read alongside the QIBA review, this paper establishes a useful division of labor. The comparative study provides evidence within a defined cohort. The standardization review asks what is needed to transport a measurement across conditions. A trustworthy AI comparison needs both: a fair local benchmark and a clear account of which parts of its performance remain untested elsewhere.
