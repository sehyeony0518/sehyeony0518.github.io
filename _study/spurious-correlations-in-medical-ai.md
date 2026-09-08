---
layout: study_note
title: "Spurious Correlations in Medical AI"
description: "Associations that hold in the training distribution and carry no clinical meaning, and how to tell them apart from real signal."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "causality"
category_title: "Causality, Bias & Shortcuts"
order: 4
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-09-06-geirhos-shortcut-learning"
---

A cue-label association tells me what a model could exploit; an intervention tells me something about what the fitted model actually uses. I need both kinds of evidence before calling a gallbladder classifier's success clinically misleading.

## Core question and definition

I use a spurious correlation to mean an association that supports prediction in the observed data but does not support the intended clinical interpretation or expected use. It can arise through documentation, acquisition, selection, label construction, or sampling chance.

The term is relative to the task. A referral code could be appropriate contextual information in a referral-prioritization system while failing to establish image-based recognition of malignancy. Likewise, a disease consequence can be valid diagnostic evidence even though it does not cause disease.

I distinguish three statements: a nuisance predicts the label; the trained model uses that nuisance; and this use causes failure under a relevant change. Each statement requires additional evidence. [Geirhos and colleagues](https://doi.org/10.1038/s42256-020-00257-z) frame shortcut learning around decision rules that succeed under benchmark conditions but fail under more demanding conditions.

## Key concepts

### Trace the cue to a concrete recording step

In ultrasound, a caliper appears because an operator freezes a view, selects a measurement, and exports the annotated image. Its presence can record that something was worth measuring. Its style can identify software or equipment. Its coordinates can also reveal lesion location and approximate extent.

Those are different information channels. Removing a marker tests more than “text dependence” if the marker also supplies localization. I would define whether the intended application receives an already localized lesion and whether measurements exist at prediction time.

Other candidates include a color Doppler box, depth scale, preset text, black borders, compression patterns, and the number of saved frames. Each should be linked to a hypothesized workflow, rather than placed on a generic list of suspicious pixels.

### Conditional association cannot certify clinical meaning

Let $$N$$ denote a suspected nuisance, $$C$$ measured clinical factors, and $$Y$$ the diagnostic target. The condition

$$
P(Y\mid N,C)=P(Y\mid C)
$$

states that $$N$$ adds no label information after conditioning on $$C$$. It does not prove that $$N$$ is meaningless. The nuisance could duplicate a valid finding, while the measured concepts could also be incomplete or noisy.

Conversely, residual predictive information in $$N$$ does not establish clinical validity. A caliper style may still identify a referral service after adjustment for lesion size.

I would use conditional analyses to challenge named explanations. The result needs a description of the factor labels, their measurement error, and the clinical variation retained after conditioning.

### Stability is informative only when environments challenge the mechanism

An acquisition cue can remain predictive across hospitals if all hospitals share the same documentation practice. A leave-one-hospital-out evaluation may therefore preserve the suspected shortcut.

For a caliper hypothesis, useful environments might differ in whether images are exported before measurement, whether overlays remain removable, or whether measurements are applied routinely to benign and suspicious findings. Machine diversity without those differences may be less informative.

An association that changes across environments is a candidate dependency, not automatically a spurious one. Clinical spectrum, feature visibility, and reference definitions can also change. I would ask whether the environments vary the nuisance while preserving a comparable diagnostic task.

### Predictability, representation, and reliance are separate

A metadata-only classifier tests predictive opportunity. A probe trained to recover machine identity from a frozen representation tests whether machine information is accessible to that probe. Neither demonstrates that the diagnostic head uses the information.

A controlled input edit or internal intervention moves closer to reliance, but still inherits the intervention's limitations. Replacing an overlay can introduce edges or reconstruct hidden anatomy. Removing a representation direction can change correlated clinical information.

I would interpret converging results as a sequence of narrower findings: the cue is label-associated, encoded, behaviorally consequential, and harmful under a specified challenge. Skipping those distinctions makes a plausible shortcut story look more complete than the evidence supports.

## Worked examples in medical AI

### Surgical markings in dermoscopy

[Winkler and colleagues](https://pubmed.ncbi.nlm.nih.gov/31411641/) compared dermoscopic images with and without surgical skin markings. Added markings increased melanoma scores for benign nevi and increased false-positive classifications in the evaluated network.

This is concrete evidence of sensitivity to an introduced nonlesional cue. The clinical lesion did not become melanoma because a marking appeared.

I would separate that result from a claim about the exact training mechanism. Marking sensitivity does not reconstruct the network's training distribution or establish which training examples produced the behavior.

For ultrasound, I read this as motivation to seek authentic paired documentation states. It does not establish that calipers have the same effect as skin markings, or that every model responds similarly.

### Caliper style and the missing combinations

Consider a hypothetical gallbladder dataset where suspicious lesions usually have a particular caliper style, while benign findings are often unmarked. A classifier could learn to treat that style as evidence of malignancy.

I would organize an evaluation by diagnosis and cue state: marked benign, unmarked benign, marked malignant, and unmarked malignant cases. The marked benign and unmarked malignant groups challenge the dominant association.

The clinical comparison must remain meaningful. If marked benign lesions are larger and harder to characterize, lower specificity there cannot be attributed entirely to calipers. I would annotate morphology, size, and visibility, then add paired overlay comparisons where source data permit.

Empty groups are especially informative about study design. If no unmarked malignant cases exist, an observational benchmark cannot establish independence from marking through subgroup analysis alone.

### An acoustic artifact with clinical information

The word “artifact” does not make an ultrasound feature spurious. In adenomyomatosis, echogenic material within Rokitansky-Aschoff sinuses can produce comet-tail artifacts, a recognized imaging finding discussed by [Bonatti and colleagues](https://pubmed.ncbi.nlm.nih.gov/28127678/).

I would distinguish that acoustic consequence of tissue structure from a marker added during documentation. Both may look conspicuous, but they enter the image through different mechanisms.

A proposed audit could compare model responses to independently annotated intramural spaces and associated comet-tail artifacts. I would not erase all reverberation and assume clinical information was preserved. That intervention could remove part of the evidence supporting the benign diagnosis.

## Evaluation methods and limitations

### Evaluate where the association breaks

At a fixed diagnostic threshold, I would report error rates for each diagnosis-cue group, with patient counts and uncertainty. A group containing only malignant cases supports a sensitivity estimate, not a within-group AUROC.

More generally, for loss $$\ell$$, fixed model $$f$$, and prespecified groups indexed by $$g$$, define

$$
R_g(f)=E[\ell(f(X),Y)\mid G=g],
\qquad
R_{\mathrm{worst}}(f)=\max_g R_g(f).
$$

Here, $$G$$ assigns each observation to a group. Worst-group risk reveals a failure that average risk can conceal, but depends on which groups were defined and how precisely their risks can be estimated.

Group distributionally robust optimization targets the largest training-group loss. [Sagawa and colleagues](https://arxiv.org/abs/1911.08731) show why regularization matters for worst-group generalization. I would treat this as a possible mitigation after identifying useful groups, not as proof that the resulting model uses clinical evidence.

### Pair additions and removals with controls

For authentic marked and unmarked versions $$x_i(1)$$ and $$x_i(0)$$, the quantity of interest is the paired difference

$$
\Delta_i=s(x_i(1))-s(x_i(0)),
$$

where $$s$$ is a chosen scalar output of the model. What matters is the distribution of those differences, their direction by diagnosis, and whether decisions change at a fixed threshold.

A near-zero mean can conceal large positive and negative effects. I would therefore report absolute changes as well as signed changes, preserving patient clustering.

Sham export tests can reveal compression or grayscale changes. If an overlay must be reconstructed, I would review whether the procedure changes wall boundaries or attachment morphology and compare defensible replacement methods. Agreement across replacements reduces dependence on one editing algorithm, but does not recover tissue that was never recorded.

### Keep discovery separate from confirmation

Searching many crops, metadata fields, and subgroups can produce compelling associations by chance. I would use development data to formulate candidate mechanisms, then freeze the cue definition, intervention, outcome scale, and analysis before confirmatory evaluation.

A repaired model needs a fresh challenge set. Removing the first discovered cue can leave correlated alternatives, such as marker style disappearing while zoom and frame count still encode the same workflow.

Successful nuisance invariance also needs a clinical counterpart. A model insensitive to every input change would pass a simple stability test while being useless. I would jointly evaluate retained diagnostic performance and alignment with independently annotated findings.

## Research connections and open questions

My first experiment would test whether the diagnosis-caliper association differs between routine survey frames and targeted lesion views. Recovering that acquisition context could distinguish documentation practice from a machine-specific visual style.

Second, I would assemble authentic marked and unmarked pairs and ask whether overlay effects are larger when calipers overlap the lesion boundary. This would test whether anatomical localization makes a documentation dependency appear clinically plausible.

Third, after any mitigation, I would evaluate marked benign and unmarked malignant cases alongside clinical-factor alignment. The useful outcome is not simply a smaller overlay effect. It is evidence that the classifier remains responsive to relevant findings when the convenient documentation association is challenged.

## References

- Winkler et al., [Association Between Surgical Skin Markings in Dermoscopic Images and Diagnostic Performance of a Deep Learning Convolutional Neural Network for Melanoma Recognition](https://pubmed.ncbi.nlm.nih.gov/31411641/), JAMA Dermatology 2019.
- Geirhos et al., [Shortcut learning in deep neural networks](https://doi.org/10.1038/s42256-020-00257-z), Nature Machine Intelligence 2020.
- Sagawa et al., [Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization](https://arxiv.org/abs/1911.08731), arXiv 2019, revised 2020.
- Bonatti et al., [Gallbladder adenomyomatosis: imaging findings, tricks and pitfalls](https://pubmed.ncbi.nlm.nih.gov/28127678/), Insights into Imaging 2017.
