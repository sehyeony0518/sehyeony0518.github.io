---
layout: study_note
title: "Auditing and Evaluating Generative Medical AI"
description: "What evaluation means when the output is text or an image rather than a label."
og_image: "https://sehyeony0518.github.io/assets/img/og/auditing-and-evaluating-generative-medical-ai.png"
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "systems"
category_title: "Medical AI Systems & Deployment"
subgroup: "Generative Systems, Agents & Deployment"
order: 5
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2025-12-06-roentmod-counterfactual-cxr"
---

## Core question and definition

**What does a generative evaluation measure, and when does that measurement support a claim of clinical correctness?**

A medical generator can produce reports, answers, summaries, or images. Its output can be fluent, internally coherent, and partly correct while still failing the clinical task.

Evaluation therefore needs a specified input, permitted information, output purpose, and reference. Describing an image, summarizing a record, answering a clinical question, and synthesizing an image are different tasks.

Likelihood, text overlap, and human preference measure different properties. None independently establishes that every clinically important assertion is correct, supported, and complete.

## Key concepts

### Likelihood evaluates a distribution of outputs

For input $$x$$ and output tokens $$y_1,\ldots,y_T$$, the probability chain rule gives

$$
p_\theta(y\mid x)
=
\prod_{t=1}^{T}
p_\theta(y_t\mid y_1,\ldots,y_{t-1},x).
$$

Taking the negative logarithm converts the product into a sum:

$$
-\log p_\theta(y\mid x)
=
-\sum_{t=1}^{T}
\log p_\theta(y_t\mid y_1,\ldots,y_{t-1},x).
$$

This rewards assigning probability to the reference wording. It does not directly assign a clinical cost to a mistaken negation, omitted finding, or incorrect temporal comparison.

Let $$q(y\mid x)$$ denote the distribution of reference documents. At a fixed input, the expected negative log likelihood is

$$
\begin{aligned}
\mathbb E_q[-\log p_\theta(Y\mid x)]
&=
-\sum_y q(y\mid x)\log p_\theta(y\mid x)\\
&=
-\sum_y q(y\mid x)\log q(y\mid x)
+
\sum_y q(y\mid x)
\log\frac{q(y\mid x)}{p_\theta(y\mid x)}\\
&=
H(q)+D_{\mathrm{KL}}(q\Vert p_\theta).
\end{aligned}
$$

The algebra inserts and subtracts the log probability under the reference distribution. With the required support and finite quantities, convexity of the negative logarithm gives

$$
D_{\mathrm{KL}}(q\Vert p_\theta)
=
\mathbb E_q\!\left[-\log\frac{p_\theta(Y\mid x)}{q(Y\mid x)}\right]
\ge
-\log\mathbb E_q\!\left[\frac{p_\theta(Y\mid x)}{q(Y\mid x)}\right]
\ge 0.
$$

The expectation inside the logarithm sums the model's probabilities over the support of the reference distribution, so it is at most one. Equality is attained when the distributions agree.

That is a statement about predicting documents. If the documents omit findings, contain errors, or depend on clinical information missing from the input, matching their distribution does not turn the objective into patient-level factual verification.

### Text probability is not statement probability

The probability of one wording is not the probability that its clinical meaning is true.

A true observation may have many valid phrasings, each receiving only part of the probability mass. A common but inappropriate phrase may receive substantial probability because it is frequent in similar documents.

Token probabilities also condition on previous generated tokens. Once an unsupported premise enters the text, a coherent continuation can be likely under that premise while remaining unsupported by the patient evidence.

Consequently, multiplying token probabilities does not produce a calibrated confidence that the complete report is clinically correct.

### What n-gram overlap measures

An n-gram is a consecutive sequence of tokens. Overlap metrics compare such sequences with those in reference text.

For a single reference, clipped precision at order $$n$$ is

$$
P_n
=
\frac{
\sum_g
\min\{\operatorname{count}_{\mathrm{candidate}}(g),
      \operatorname{count}_{\mathrm{reference}}(g)\}
}{
\sum_g \operatorname{count}_{\mathrm{candidate}}(g)
}.
$$

Clipping prevents repeated candidate phrases from earning unlimited credit from one reference occurrence.

A conventional BLEU score combines these precisions through a geometric mean and a length penalty. For equal-length sentences, with equal weights through order four, the unsmoothed expression is

$$
\mathrm{BLEU}_4
=
(P_1P_2P_3P_4)^{1/4}.
$$

This is a metric definition, not a theorem connecting word overlap to clinical meaning. In particular, a zero high-order overlap can make the unsmoothed sentence score zero.

### Worked example: overlap rewards a negation error

Use lowercase tokens and omit punctuation.

Reference:

> no pleural effusion is present

Incorrect candidate:

> large pleural effusion is present

Correct paraphrase:

> there is no pleural effusion

All contain five tokens. Direct counting gives:

| Candidate | Unigram precision | Bigram precision | Trigram precision | Four-gram precision |
|---|---|---|---|---|
| Incorrect candidate | $$4/5$$ | $$3/4$$ | $$2/3$$ | $$1/2$$ |
| Correct paraphrase | $$4/5$$ | $$1/2$$ | $$1/3$$ | $$0$$ |

For the incorrect candidate,

$$
\mathrm{BLEU}_4
=
\left(
\frac45\frac34\frac23\frac12
\right)^{1/4}
=
\left(\frac15\right)^{1/4}.
$$

For the correct paraphrase, the unsmoothed score is zero because there is no shared four-gram.

The incorrect statement preserves much of the wording while reversing the clinically important claim. The paraphrase preserves the claim while changing word order.

This is a constructed example of the metric's limitation. Smoothing or corpus aggregation changes the numerical behavior, but does not make lexical overlap a definition of factual correctness.

### Human preference measures a specified judgment

A preference assessment asks which output a reader favors under particular instructions and available evidence.

Readers may value readability, brevity, completeness, tone, or usefulness. Those are legitimate properties, but their weighting need not match factual accuracy.

A polished answer can be preferred because it is easier to read or more confident. An appropriate uncertain answer can be less satisfying while being better supported.

Expert review can directly assess clinical correctness when reviewers receive suitable evidence and an explicit task. It is then a clinical assessment with defined criteria and uncertainty, not merely a general preference vote.

The distinction matters when reporting results: preferred wording, fewer factual errors, and better clinical decisions are different endpoints.

### Decompose the output into clinically meaningful claims

A statement needs its subject, finding, location, polarity, certainty, and time context preserved.

“An opacity was present previously” is not equivalent to “an opacity is present now.” “Cannot exclude” is not equivalent to “confirmed.” A correct finding on the wrong side remains an error.

A useful error taxonomy includes:

- Unsupported or contradicted findings.
- Incorrect anatomical location or laterality.
- Incorrect negation.
- Incorrect severity or extent.
- Incorrect comparison with prior evidence.
- Unsupported diagnostic or management conclusions.
- Omitted clinically necessary information.

Claims should not be split so finely that their meaning disappears. Separating a finding from its negation or temporal qualifier can make an incorrect sentence look like several correct fragments.

### Hallucination and calibration are related, not identical

“Hallucination” is used for several failures, including fabricated facts and statements unsupported by the supplied evidence. The definition should be stated.

Truth and grounding can differ. A statement can happen to be true while unsupported by the information the system was allowed to use. Another statement can faithfully summarize an inaccurate source. These require different judgments.

Calibration becomes relevant when the system expresses a probability of correctness or support. Let $$C$$ indicate whether an emitted statement satisfies a specified adjudication rule, and let $$Q$$ be its stated confidence.

Perfect calibration over the defined statement population means

$$
\mathbb E[C\mid Q=p]=p.
$$

Thus statements assigned confidence $$p$$ should satisfy the rule with frequency $$p$$.

Confident unsupported assertions can reveal overconfidence. But an individual false statement does not by itself prove miscalibration: a calibrated system can make errors. Conversely, calibrated probabilities do not make a clinically dangerous error rate acceptable.

Hallucination also involves evidence access, retrieval, generation, and verification failures. It should not be reduced to calibration alone.

### Worked example: statement-level overconfidence

Construct five adjudicable statements, each assigned confidence $$4/5$$. Suppose exactly two satisfy the stated correctness rule.

Their empirical correctness rate is

$$
\widehat p=\frac25,
$$

while their mean confidence is

$$
\overline Q=\frac45.
$$

The observed confidence–accuracy gap is therefore

$$
\overline Q-\widehat p=\frac25.
$$

Their mean Brier loss is

$$
\begin{aligned}
\frac15\sum_{j=1}^{5}(Q_j-C_j)^2
&=
\frac15\left[
2\left(\frac45-1\right)^2
+
3\left(\frac45-0\right)^2
\right]\\
&=
\frac15\left(\frac{2}{25}+\frac{48}{25}\right)
=
\frac25.
\end{aligned}
$$

This small construction makes the accounting explicit. It does not establish population miscalibration from five observations.

Unverifiable statements should remain distinct from statements known to be false. Silently assigning both the same reference value changes the target being calibrated.

### Correctness among emitted claims is not completeness

A generator can emit one safe, correct sentence and omit the finding that matters most.

Statement precision asks how many emitted claims are correct or supported. Completeness asks whether the output contains the information required for its purpose.

The denominator is different. Completeness requires a reference set of clinically necessary information; counting only what the model chose to say cannot reveal all omissions.

Report-level evaluation also matters. Many minor correct statements can coexist with one critical error. Averaging across all statements can give long reports disproportionate influence and dilute the clinically decisive failure.

Error weighting should therefore reflect the task, while retaining the error categories and the uncertainty in their adjudication.

### The reference report is evidence, not infallible truth

A reference report may omit normal findings, compress uncertainty, or reflect information outside the supplied image. Different competent readers can produce different valid reports.

A disagreement with its wording is not necessarily a clinical error. Conversely, copying its wording does not verify every statement against the patient evidence.

Review needs access to the appropriate source material: images, relevant records, prior examinations, or other evidence, depending on the task. The reference must also be matched to the correct patient and time.

A citation deserves a separate check. The source may exist without supporting the statement, and a supported general medical claim may still be inapplicable to the current patient.

### Image generation has a corresponding fidelity problem

A synthetic image can resemble the target modality without preserving the patient's anatomy or disease.

Distribution matching rewards output characteristics seen in the target population. It does not alone enforce correspondence of every clinically important structure in a particular patient. Published medical image-translation work has illustrated this limitation.

Global image similarity can also conceal a small but consequential local change. Conversely, harmless differences in noise or intensity can reduce pixel similarity without changing the clinical interpretation.

Reconstruction, image translation, and generation of new synthetic cases therefore need different fidelity claims. A plausible image is not observational evidence that its generated details existed in the original patient.

### The evaluated system includes generation and selection

Prompts, retrieved context, model version, decoding settings, and output selection all influence what is delivered.

Returning the first sample, selecting among several candidates, and presenting a clinician-edited output are different systems. Reporting only the most convincing sample evaluates neither ordinary output quality nor the full cost of selection.

If a human corrects the text, the correction burden and residual errors belong to the workflow evaluation. If an automated verifier filters outputs, its own errors and failure modes become part of the system.

Consistency is useful but insufficient. Repeatedly generating the same unsupported statement is stable failure.

### What an audit must sample

The sampling frame should reflect the intended claim.

| Dimension | What needs representation | Failure hidden by narrow sampling |
|---|---|---|
| Clinical cases | Common findings, important uncommon findings, mimics, and limited evidence | Good performance confined to easy cases |
| Inputs and context | Missing records, uncertain findings, conflicting sources, relevant prior studies | Dependence on unrealistically complete information |
| Requests | The actual task and meaningful variations in how it is requested | Sensitivity to wording concealed by one prompt |
| Generated outputs | Ordinary outputs, failures, refusals, truncations, and repetitions where relevant | Selection of only successful examples |
| Workflow | Retrieval, verification, selection, editing, and final delivery | Evaluating an intermediate artifact rather than the used system |
| Reference assessment | Defined reviewer evidence, disagreement, and adjudication | Treating uncertain judgments as unquestioned truth |

Representative sampling estimates routine performance under its population assumptions. Deliberately difficult challenge sets probe particular vulnerabilities. Their error frequencies should not be presented as clinical prevalence without a justified sampling model.

Repeated outputs from one clinical case share evidence and difficulty. They are not interchangeable with additional independent patients. Uncertainty summaries should respect that structure.

### Automated judges require their own validation

A model-based evaluator can help organize large audits, but it is another measurement instrument.

It may share the generator's misconceptions, miss subtle negation, favor familiar prose, or accept a confident citation without checking support. High agreement on easy statements does not establish detection of consequential errors.

Its performance should be assessed against the intended error categories and reviewer reference, including ambiguous cases. A judge validated for one modality or task is not automatically valid for another.

Automated scores are most interpretable when their failures and coverage limits remain visible.

### Revision checklist

| Question | Answer to retain |
|---|---|
| What does likelihood optimize? | Probability assigned to reference outputs under the modeled distribution. |
| Is token probability factual confidence? | No; wording probability and statement correctness are different quantities. |
| Why can overlap reward an error? | Small wording changes can reverse clinical meaning while preserving n-grams. |
| What does preference establish? | A judgment under specified instructions, readers, and evidence. |
| Is every false statement a calibration failure? | No; calibration is a population relationship between confidence and correctness. |
| Does statement precision measure completeness? | No; omitted necessary information needs a different denominator. |
| Is a reference report infallible? | No; wording, information access, and reader uncertainty matter. |
| Does image realism establish patient fidelity? | No; plausible structure can be unsupported. |
| What is the evaluated generator? | The complete generation, selection, verification, and editing process. |
| What must an audit retain? | Representative cases, important failure modes, unsuccessful outputs, and reference uncertainty. |

## Why it matters for my work

Generative evaluation makes the distinction between plausible output and supported clinical evidence unavoidable. Clinical assessability limits what the input can justify; the clinical target determines which omissions and false statements matter. Fluency and alignment with expected wording do not establish Clinical validity or Clinical utility.

## What I have not resolved

- Which claims can be adjudicated from the information actually supplied?
- Which errors matter most for the action the generated output supports?
- How much of a favorable result comes from the generator, the selector, the evaluator, or human correction?

---

Sources: Papineni and colleagues on BLEU; Yu and colleagues on radiology report-generation evaluation; Cohen and colleagues on limitations of distribution matching in medical image translation; and standard probability and calibration definitions. All numerical examples are self-contained constructions, not empirical medical performance estimates. These are study notes for research purposes, not clinical guidance.
