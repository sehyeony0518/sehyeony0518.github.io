---
layout: post
title: "Hidden Stratification Causes Clinically Meaningful Failures in Machine Learning for Medical Imaging"
date: 2025-11-10 12:00:00 +0900
venue: "ACM CHIL"
authors: "Oakden-Rayner, Dunnmon, Carneiro, Ré (2020)"
description: "Within a labeled class there are clinically distinct subsets, and a model can fail on the dangerous ones while the headline number stays high."
og_image: "https://sehyeony0518.github.io/assets/img/og/2025-11-10-oakden-rayner-hidden-stratification.png"
related_posts: false
---

**Paper.** *Hidden Stratification Causes Clinically Meaningful Failures in Machine Learning for Medical Imaging*. [ACM CHIL 2020](https://dl.acm.org/doi/10.1145/3368555.3384468)

The central question is whether a benchmark's label schema is detailed enough to reveal clinically important failures. A class such as “abnormal” or “pneumothorax” can contain cases with different appearances, treatment states, annotation quality, and clinical consequences. If those distinctions are absent from the evaluation schema, a strong aggregate result can conceal poor performance on the subset that motivates deployment. The problem can occur even when patients are correctly held out and the aggregate calculation is accurate.

The paper calls this hidden stratification. The authors examine medical imaging tasks including musculoskeletal abnormality, hip fracture, and pneumothorax detection, using additional subclass descriptions to reassess performance. They discuss three ways to identify the problem: specifying additional labels, reviewing errors, and using algorithmic methods to suggest groups. The key design move is to evaluate a model within clinically meaningful subclasses that were not adequately represented by the original broad target.

The pneumothorax example is especially useful because the hidden distinction concerns treatment. The reported model had an overall AUC of 0.87, compared with 0.94 for pneumothoraces with a chest drain and 0.77 for those without one. A reassuring aggregate score therefore concealed poorer performance in cases lacking a visible treatment-associated cue. The finding matters for a detection claim aimed at patients whose condition has not already prompted that intervention.

In MURA, the reported abnormality AUC was 0.98 for hardware and 0.76 for degenerative disease. The paper also examined variation across hip-fracture presentations. These examples show that hidden strata can arise through different mechanisms, including subtle appearance, rarity, label quality, and correlated features. They should not all be reduced to shortcut learning. Some subtypes may simply be harder to depict or less consistently included in the broad reference label. [Authors' analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC7665161/).

The results license a strong claim about evaluation completeness: an aggregate score does not determine performance on every clinically important subclass. They do not establish that every poorly performing subclass has equal clinical priority. Difficulty detecting a common incidental degenerative finding and difficulty detecting an untreated urgent condition can have very different consequences. The paper's value is in bringing the clinical purpose back into subgroup definition, rather than merely increasing the number of reported metrics.

The chest-drain result also needs a mechanism boundary. Different AUCs in cases with and without drains are consistent with treatment-associated shortcut reliance, but the comparison does not by itself isolate the effect of deleting a drain from an otherwise identical image. The groups can differ in disease appearance and clinical history. A controlled intervention or additional matched analysis would strengthen the specific reliance claim. The subgroup result is already sufficient to challenge a broad performance claim without requiring complete causal identification.

Another subtlety is that a subgroup AUC still requires a negative comparison group. Its value depends on how the subclass cases are compared with negatives and on the clinical spectrum of those negatives. It is not simply the probability that the model detects a patient in the subgroup. For a practical detection system, I would also report sensitivity at the prespecified operating threshold, with the number and characteristics of affected patients retained.

The three proposed discovery approaches have different blind spots. A richer schema can ensure that known important subclasses are evaluated, but depends on the schema designer's knowledge. Error review can discover patterns that were not anticipated, but can miss rare failures or mistake memorable examples for common mechanisms. Clustering can suggest structure without expensive complete annotation, but the resulting groups need not correspond to meaningful clinical categories.

A careful reader should therefore resist interpreting subgroup discovery as subgroup completeness. Finding one dangerous stratum is evidence that the original summary was insufficient; it is not evidence that all remaining strata are safe. A representation used for clustering might also fail to preserve the distinction that matters clinically. Algorithmic discovery is useful as a way to direct attention, while independent clinical assessment is needed to establish the meaning and consequences of the discovered groups.

There is a statistical cost to searching many slices of a fixed test set. Some apparent gaps will be imprecise or selected because they are extreme. I would separate exploratory discovery from confirmation, retain patient counts and uncertainty intervals, and reserve independent cases for evaluating a newly proposed subgroup. This is not an argument against exploratory auditing. It is a way to keep a useful discovery from becoming an overstated estimate of the size of the problem.

For a hypothetical gallbladder model, I would start with clinically motivated strata such as lesion morphology, visibility, treatment status, and the source of diagnostic verification. A model may perform well on large obvious abnormalities but poorly on subtle wall lesions. It may also fail when the saved still image does not depict the evidence needed for the patient-level label. Those possibilities need separate categories because one calls for better recognition, while another concerns the input contract.

I would review successful cases alongside errors. If calipers appear in many false positives, their prevalence among correctly classified cases is needed before attributing failure to them. Similarly, a rare subtype's appearance in an error gallery does not establish a high subtype error rate without the denominator. Once a pattern is confirmed, the remedy should match its mechanism: additional examples, revised labels, better acquisition, or a targeted reliance audit may be appropriate in different cases.

[Error and Clinical Failure Analysis]({{ '/study/error-and-clinical-failure-analysis/' | relative_url }}) develops this paper's central lesson into a process for distinguishing reference disagreement, prediction error, workflow failure, and potential harm. The paper supports that process by showing why the benchmark's existing schema cannot be the only source of failure categories. It also motivates keeping discovery and confirmation separate.

[Robustness, Subgroup Performance, and External Validation]({{ '/study/robustness-subgroup-performance-and-external-validation/' | relative_url }}) explains subgroup performance as a conditional quantity. [Label Quality and Interobserver Variability]({{ '/study/label-quality-and-interobserver-variability/' | relative_url }}) complicates the interpretation when the broad label is less reliable for some subclasses. I take hidden stratification as a requirement to evaluate the clinical cases that justify the system, rather than allowing the easiest or most numerous cases to define success.
