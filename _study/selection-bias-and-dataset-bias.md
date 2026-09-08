---
layout: study_note
title: "Selection Bias and Dataset Bias"
description: "How the assembly of a medical dataset, through who was scanned, labeled, and recorded, writes itself into the model."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "causality"
category_title: "Causality, Bias & Shortcuts"
order: 3
source: "Independent study"
written: true
updated: "2026-09-08"
---

The patients missing from a gallbladder dataset can determine what its performance estimate means. I want to reconstruct the decisions between an eligible examination and an analyzed, labelled image.

## Core question and definition

Let $$S=1$$ indicate inclusion in the analyzed dataset, $$X$$ the model input, and $$Y$$ the target label. The observed distribution is $$P(X,Y\mid S=1)$$. My intended clinical claim may concern a different distribution, such as all eligible examinations at the point where the system would be used.

Selection is not automatically bias. A surgical cohort can validly support a question about surgical patients. Bias arises when the selection process distorts the quantity being estimated or when a result is interpreted for a population the design does not support.

I use “dataset bias” as an umbrella description, then name the mechanism: selective referral, selective verification, restricted disease spectrum, differential measurement, or documentation-dependent missingness. Patient leakage is another mechanism. It can inflate evaluation through shared information, but fixing leakage does not repair the cohort's clinical coverage.

## Key concepts

### There are several denominators before the final image count

I would distinguish patients eligible for the intended application, patients referred for imaging, completed examinations, retrievable examinations, examinations with usable references, and retained inputs. These denominators describe different losses.

For ultrasound, the saved archive also represents an operator's selection from a larger examination. A still-image collection cannot reveal every view that was attempted or every finding that was difficult to visualize. A model evaluated on retained diagnostic frames therefore inherits an upstream human selection step.

The annotation dataset introduces another filter. If readers label clinical features only when the lesion is clearly visible, an evidence-alignment analysis can exclude precisely the inputs where assessability is uncertain. I would report this annotation denominator separately from the diagnostic test denominator.

### Selection can create an association

Suppose clinical concern $$K$$ and surgical fitness $$F$$ both influence surgery $$S$$:

$$
K\rightarrow S\leftarrow F.
$$

Conditioning on surgery can associate concern and fitness, even without their being associated in the source population. [Hernán, Hernández-Díaz, and Robins](https://pubmed.ncbi.nlm.nih.gov/15308962/) explain selection bias through conditioning on common effects.

In a proposed gallbladder study, this matters if fitness also relates to image quality, treatment options, or other patient characteristics. The operated cohort can contain relationships created by the route to verification.

This mechanism differs from merely having too few patients from a subgroup. Recruiting additional patients through the same restrictive pathway can improve precision while preserving the selection-induced relationship.

### Verification changes which labels become available

Partial verification occurs when only some evaluated patients receive the reference procedure. Differential verification occurs when different reference procedures are used across patients. Both need attention when surgery supplies histology for some lesions while others are classified through follow-up or clinical records.

[Begg and Greenes](https://pubmed.ncbi.nlm.nih.gov/6871349/) describe how restricting diagnostic-test assessment to verified cases can bias sensitivity and specificity, and why correction requires assumptions about verification.

I would not treat “no cancer recorded” as equivalent to a benign specimen. Follow-up length, attendance, subsequent testing, and the outcome definition determine what a negative record supports.

Incorporation bias is another distinction: if the index test being evaluated contributes to the reference diagnosis, agreement can become partly circular. The reference-building process must therefore identify which imaging assessments were available to adjudicators.

### Spectrum and prevalence affect different performance properties

A dataset of obvious masses and uncomplicated benign findings omits the indeterminate lesions that may dominate the intended characterization task. This is a spectrum issue: the distributions of findings within diagnostic classes have changed.

Case-control enrichment has a narrower mathematical consequence when sampling changes only class proportions. At a fixed threshold, positive predictive value is

$$
\mathrm{PPV}
=
\frac{\mathrm{Se}\,\pi}
{\mathrm{Se}\,\pi+(1-\mathrm{Sp})(1-\pi)},
$$

where $$\mathrm{Se}$$ is sensitivity, $$\mathrm{Sp}$$ specificity, and $$\pi=P(Y=1)$$ disease prevalence in the target population.

Changing prevalence changes PPV even if sensitivity and specificity remain fixed. However, selecting advanced cancers and easy benign controls can also change sensitivity, specificity, and AUROC through disease spectrum. I would not describe AUROC as immune to dataset assembly merely because it is not directly determined by prevalence.

## Worked examples in medical AI

### A pathology-only gallbladder lesion cohort

Consider a hypothetical classifier developed from resected gallbladder lesions. Histology provides direct information about the removed tissue, but reaching surgery may depend on imaging concern, symptoms, patient fitness, preferences, and local practice.

The evaluated question is discrimination among included, operated lesions. It does not automatically become discrimination among all incidentally detected lesions. Small, reassuring findings managed without surgery may be absent, while selected benign lesions may be unusually suspicious.

I would preserve the index examination date, decision-to-operate information where available, specimen linkage, and interval to surgery. These records help establish that the reference belongs to the imaged lesion and clarify whether intervening events changed the target.

For the unoperated population, I would define a separate follow-up-based outcome and report its evidence limitations. Combining those labels without identifying their sources would conceal differential verification.

### Curated frames and an invisible failure mode

Suppose reviewers choose one clear frame per lesion, exclude poorly visualized walls, and remove cases where they disagree about the finding. The model may perform well because every tested input already satisfies a demanding human quality screen.

For a tool intended to accept routine saved frames, those exclusions remove part of its actual task. For a tool explicitly designed to classify reader-approved views, the screen may be legitimate, but its workload and rejection rate belong in evaluation.

I would compare the full eligible examination list with the retained set, then inspect excluded cases for recurring acquisition conditions and diagnostic groups. If cine clips exist, I could measure how sensitive results are to a predefined frame-selection rule. If only curated stills remain, I cannot reconstruct performance on unsaved views.

## Evaluation methods and limitations

### Reconstruct the flow and reference process

I would create a cohort flow that counts patients and examinations at each stage, records exclusion reasons, and distinguishes unavailable images from unavailable labels. The dates and reasons matter more than a single final sample-size statement.

[STARD 2015](https://www.bmj.com/content/351/bmj.h5527) provides reporting items for diagnostic accuracy studies, including participant selection, reference standards, missing or indeterminate results, and participant flow. I would use those items to make the study reconstructable, rather than treat checklist completion as evidence that selection bias is absent.

Where source records permit, I would compare included and excluded examinations by indication, age, acquisition setting, clinical concern, and follow-up availability. These comparisons reveal measured differences; they cannot establish similarity on unrecorded findings.

### Weighting requires information about those not selected

Let $$W$$ denote covariates available for the eligible population and $$\pi(W)=P(S=1\mid W)$$ the inclusion probability. For loss $$\ell(f(X),Y)$$ of a fixed predictor $$f$$, a weighted estimate is

$$
\widehat R
=
\frac{\sum_{i:S_i=1}w_i\,\ell(f(X_i),Y_i)}
{\sum_{i:S_i=1}w_i},
\qquad
w_i=\frac{1}{\hat\pi(W_i)}.
$$

This targets the eligible-population risk only under an adequate selection model, positive inclusion probabilities, and assumptions making selected observations representative within $$W$$. In particular, outcome-related selection unexplained by $$W$$ remains a problem.

I would inspect weight concentration and compare weighted and unweighted results. A group with no chance of inclusion cannot be recovered by assigning larger weights to other groups. Nor does weighting convert a follow-up label into histology.

### Preserve uncertainty about missing outcomes

When verification depends on unrecorded concern, I would use sensitivity analyses that vary assumptions about disease among unverified patients. The result should show how conclusions depend on those assumptions.

I would also report performance separately by reference source, without interpreting differences as model failure alone. They may reflect different populations, label errors, or outcome definitions.

Patient-level splits and clustered uncertainty remain necessary. They address dependence between records; they do not make selectively labelled records representative of all scanned patients.

## Research connections and open questions

My first feasible project would link the audit sample back to an examination registry and quantify which exclusions occur before clinical-feature annotation. This would establish the population for which faithfulness can currently be evaluated.

Second, I would compare patients with and without histological verification using information recorded at the index scan. The immediate output would be an overlap assessment and a list of missing verification predictors, rather than a claim that weighting has removed bias.

Third, I would test a predefined frame-selection policy on examinations with multiple saved views. Reporting diagnostic performance, clinical-factor assessability, and the fraction of examinations rejected by that policy would make the interaction between image selection and evidence auditing measurable.

## References

- Hernán, Hernández-Díaz, and Robins, [A structural approach to selection bias](https://pubmed.ncbi.nlm.nih.gov/15308962/), Epidemiology 2004.
- Begg and Greenes, [Assessment of diagnostic tests when disease verification is subject to selection bias](https://pubmed.ncbi.nlm.nih.gov/6871349/), Biometrics 1983.
- Bossuyt et al., [STARD 2015: an updated list of essential items for reporting diagnostic accuracy studies](https://www.bmj.com/content/351/bmj.h5527), BMJ 2015.
