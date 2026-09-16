---
layout: study_note
title: "Foundation Models for Medical Imaging"
description: "What large pretrained imaging models change about medical AI, and what they do not change about validation."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "systems"
category_title: "Medical AI Systems & Deployment"
subgroup: "Foundation & Multimodal Models"
order: 1
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-07-15-clear-auditable-foundation-model-radiology"
  - "2026-08-30-monet-transparent-medical-image-ai"
---

A foundation model supplies a reusable starting point for multiple downstream tasks. Its clinical meaning comes from the particular inputs, adaptation procedure, output, and evaluation attached to that starting point.

## Core question and definition

The central question is:

> What does pretraining make available, what does downstream adaptation actually use, and what evidence supports the resulting clinical claim?

The foundation-model framing concerns models pretrained on broad data at scale and adapted across downstream uses. It describes a role in a learning pipeline, rather than a certificate of general competence. [On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258).

The term does not, by itself, establish that a model:

- Covers every imaging modality.
- Understands disease mechanisms.
- Produces calibrated probabilities.
- Localizes the evidence behind its output.
- Works without task information or prompting.
- Has an independent evaluation dataset.
- Is clinically valid or useful.

There is no mathematical parameter-count boundary at which these properties follow. A large model trained for a narrow output remains a model trained for that output. A reusable medical encoder may also have a narrower scope than general medical competence.

## Key concepts

### 1. Write down the complete learning pipeline

Let pretraining data be

$$
\mathcal D_{\mathrm{pre}},
$$

and let the pretraining procedure produce parameters

$$
\theta_0=\mathcal P(\mathcal D_{\mathrm{pre}}).
$$

A downstream procedure then uses local development data:

$$
f=\mathcal A(\theta_0,\mathcal D_{\mathrm{dev}};\gamma),
$$

where $$\gamma$$ includes architecture choices, prompts, optimization settings, preprocessing, and model-selection decisions.

The evaluated object is $$f$$ together with its surrounding pipeline. It is not merely the checkpoint $$\theta_0$$.

This separation matters because an improvement may come from:

- The pretrained representation.
- Additional downstream labels.
- A better adaptation procedure.
- Human localization supplied through prompts.
- A different tuning budget.
- Different preprocessing or examination aggregation.

An evaluation should identify which of these contributions changed.

### 2. A pretraining objective specifies what is rewarded

Pretraining usually minimizes an empirical objective:

$$
\widehat L_{\mathrm{pre}}(\theta)
=
\frac1N\sum_{i=1}^N
\ell_{\mathrm{pre}}(\theta;Z_i).
$$

The training example $$Z_i$$ might be an image, a masked image, an image-report pair, or an annotated structure.

| Objective | What directly reduces the loss | What does not follow automatically |
|---|---|---|
| Reconstruction | Recovering withheld image content | Recognition of the clinically decisive feature |
| Contrastive image learning | Distinguishing or matching augmented observations | Invariance appropriate for every clinical task |
| Image-text matching | Identifying paired images and text | Sentence-level image grounding |
| Supervised segmentation | Matching supplied masks under the prompting protocol | Autonomous lesion detection |
| Language generation | Predicting observed report tokens | Factual completeness or correctness for a new patient |

A useful representation may emerge from these objectives. The objective itself does not certify the downstream interpretation.

For squared reconstruction loss over $$P$$ pixels,

$$
L_{\mathrm{rec}}
=
\frac1P\sum_{j=1}^P(\widehat x_j-x_j)^2.
$$

Suppose a clinically important region occupies $$k$$ pixels. Its direct contribution is

$$
\frac1P\sum_{j\in\mathcal R}(\widehat x_j-x_j)^2,
$$

while the remaining $$P-k$$ pixels contribute the rest.

A small region can therefore contribute little to the average despite being decisive for diagnosis. This does not prove that reconstruction discards the region. It explains why low average reconstruction error is insufficient evidence that the region is represented adequately.

### 3. More data estimates the pretraining distribution more precisely

Under suitable sampling assumptions,

$$
\widehat L_{\mathrm{pre}}(\theta)
\longrightarrow
\mathbb E_{P_{\mathrm{pre}}}
[\ell_{\mathrm{pre}}(\theta;Z)].
$$

Increasing the dataset can improve estimation of that objective. It does not change the objective into a clinical one or make the pretraining population equal to the deployment population.

Repeated observations also need to be distinguished from independent information. If every example is copied $$k$$ times,

$$
\begin{aligned}
\widehat L_{\mathrm{repeated}}(\theta)
&=
\frac1{kN}\sum_{i=1}^N\sum_{r=1}^k
\ell_{\mathrm{pre}}(\theta;Z_i)\\
&=
\frac1N\sum_{i=1}^N
\ell_{\mathrm{pre}}(\theta;Z_i).
\end{aligned}
$$

The record count increases, but the objective contains no new observations.

Adjacent frames, repeated examinations, and duplicated reports are less extreme versions of this distinction. A large image count does not identify the number of independent patients, clinical presentations, or acquisition conditions.

### 4. Frozen probes and fine-tuning test different capabilities

For a frozen encoder,

$$
Z=\phi_{\theta_0}(X),
$$

a linear probe learns a restricted predictor such as

$$
\widehat Y
=
\mathbf1\{w^\top Z+b\geq0\}.
$$

A nonlinear head permits a larger class of mappings. Fine-tuning also changes $$\phi_{\theta_0}$$ itself.

These answer different questions:

| Adaptation | Question it most directly addresses |
|---|---|
| Linear probe | Is the target accessible through a linear readout under this protocol? |
| Nonlinear frozen-encoder head | Is the target accessible through the chosen nonlinear readout? |
| Partial fine-tuning | Can selected parameters adapt usefully with the supplied labels? |
| Full fine-tuning | Can the complete initialization support the downstream learning procedure? |
| Prompted use | What can the model do with the supplied prompt information? |

Failure of a linear probe does not prove that the representation contains no target information. Success does not establish that a separately adapted model uses the intended evidence.

### 5. A representation can contain the answer while a linear probe misses it

Construct four equally likely representations:

| $$z_1$$ | $$z_2$$ | Target $$Y$$ |
|---:|---:|---:|
| 1 | 1 | 1 |
| 1 | -1 | 0 |
| -1 | 1 | 0 |
| -1 | -1 | 1 |

The target is exactly recoverable:

$$
\boxed{Y=\frac{1+z_1z_2}{2}.}
$$

Now suppose a linear classifier could classify all four points.

For the two positive points,

$$
w_1+w_2+b\geq0,
$$

$$
-w_1-w_2+b\geq0.
$$

Adding gives

$$
2b\geq0.
$$

For the two negative points,

$$
w_1-w_2+b<0,
$$

$$
-w_1+w_2+b<0.
$$

Adding gives

$$
2b<0.
$$

The requirements contradict each other. No linear classifier can classify all four.

A linear rule predicting positive when

$$
z_1+z_2\geq1
$$

gets three of the four correct, so the best linear accuracy is $$3/4$$. The nonlinear product rule gets all four correct.

The representation contains complete target information. The linear evaluation cannot extract all of it.

This construction separates information availability from accessibility under a particular probe.

### 6. Available clinical information is not necessarily used information

Now construct a representation containing two binary features:

$$
Z=(M,S),
$$

where $$M$$ is the intended clinical feature and $$S$$ is a site-associated cue. Define the true target as

$$
Y=M.
$$

In the source data, suppose

$$
S=M.
$$

Two heads then have identical source accuracy:

$$
h_M(Z)=M,
\qquad
h_S(Z)=S.
$$

In a target setting, let the association reverse:

$$
S=1-M.
$$

| Target case | Clinical feature $$M$$ | Site cue $$S$$ | True target | Clinical head | Site head |
|---|---:|---:|---:|---:|---:|
| A | 0 | 1 | 0 | 0 | 1 |
| B | 1 | 0 | 1 | 1 | 0 |

The clinical head remains correct; the site head is wrong on both cases.

A successful probe for $$M$$ establishes that $$M$$ is recoverable from the representation under that probe. It does not establish that the deployed head uses $$M$$.

This is the distinction between evidence available in a representation and evidence relied on by the prediction.

### 7. Transfer performance and clinical validity are different claims

A transfer comparison might establish

$$
R_t\bigl(\mathcal A(\theta_0,\mathcal D_n)\bigr)
<
R_t\bigl(\mathcal B(\mathcal D_n)\bigr),
$$

where both procedures use a specified downstream sample of size $$n$$ and are evaluated independently in population $$t$$.

That is evidence of an advantage for the tested learning procedure.

Clinical validity additionally requires:

- The correct clinical target.
- An adequate reference standard.
- Appropriate patient, lesion, examination, or frame matching.
- Inputs available at the intended decision time.
- Relevant acquisition and case-mix coverage.
- Acceptable behavior at the intended operating point.

An improvement can remain insufficient for the use. Symbolically,

$$
R_{\mathrm{required}}
<
R_{\mathrm{pretrained}}
<
R_{\mathrm{baseline}}
$$

means pretraining improves the result while the resulting risk remains above the requirement.

Likewise, a strong segmentation result does not establish diagnostic validity, and diagnostic validity does not establish clinical utility.

### 8. Prompts can supply substantial task information

A prompted model predicts

$$
\widehat Y=f(X,P),
$$

where $$P$$ is the prompt.

The relevant information set is therefore $$X,P$$, not $$X$$ alone.

Construct an image-localization problem with four equally likely target locations. Suppose the supplied image contains no information distinguishing them. Without other information, the best localization accuracy is

$$
\frac14.
$$

Now supply the true location as a prompt:

$$
P=J,
$$

where $$J$$ is the target location. A system that simply follows the prompt can localize correctly with probability one.

This is an intentionally extreme construction. It shows why information supplied through prompting must be included in the claim.

A bounding box derived from a reference mask evaluates segmentation conditional on unusually informative localization. A box drawn by a clinician evaluates a human-model procedure whose localization effort and failures matter. Neither is automatically an autonomous detection evaluation.

“Zero-shot” also needs an operational definition. No downstream gradient updates does not imply no downstream information. Category descriptions, prompt selection, reference-derived boxes, and label-informed checkpoint selection can all provide task information.

### 9. Scale changes the independence problem

The usual evaluation boundary separates development from test patients. With broad pretraining, development begins before the local study.

Potential overlap includes:

- The same image or report.
- A transformed or re-exported copy.
- Another frame or examination from the same patient.
- A derivative dataset built from the same source.
- Evaluation questions or labels incorporated into later training.
- Benchmark-driven checkpoint or prompt selection.

Not every overlap has the same effect. Seeing an image without its downstream label differs from seeing the labeled image-report pair. Neither should be silently described as a wholly unseen patient evaluation.

Unlabeled use can be legitimate under a declared transductive protocol. The point is to match the claim to the information actually available.

### 10. Derive how contamination can inflate the reported result

Let $$C=1$$ indicate evaluation cases encountered during development or pretraining, and let

$$
\alpha=\Pr(C=1).
$$

Write accuracy on encountered and novel cases as $$a_{\mathrm{seen}}$$ and $$a_{\mathrm{new}}$$. Overall accuracy is

$$
\boxed{
a_{\mathrm{mix}}
=
\alpha a_{\mathrm{seen}}
+
(1-\alpha)a_{\mathrm{new}}.
}
$$

If the novel subset represents the intended new-case population, the difference from new-case accuracy is

$$
\begin{aligned}
a_{\mathrm{mix}}-a_{\mathrm{new}}
&=
\alpha a_{\mathrm{seen}}
-\alpha a_{\mathrm{new}}\\
&=
\boxed{\alpha(a_{\mathrm{seen}}-a_{\mathrm{new}})}.
\end{aligned}
$$

Overlap produces optimism in this calculation when performance is better on encountered cases. Overlap alone does not prove the direction or magnitude.

Construct 100 evaluation cases:

| Cases | Number | Correct |
|---|---:|---:|
| Encountered during development | 40 | 40 |
| Novel | 60 | 45 |
| Total | 100 | 85 |

Reported accuracy is

$$
\frac{85}{100}=\frac{17}{20}.
$$

Novel-case accuracy is

$$
\frac{45}{60}=\frac34.
$$

The difference is

$$
\frac{17}{20}-\frac34=\frac1{10},
$$

which also follows from

$$
\frac25\left(1-\frac34\right)=\frac1{10}.
$$

These are constructed counts, not a claim about any released checkpoint.

### 11. Unknown overlap prevents a clean interpretation

If $$\alpha<1$$ is known but encountered-case accuracy is unknown,

$$
a_{\mathrm{new}}
=
\frac{a_{\mathrm{mix}}-\alpha a_{\mathrm{seen}}}{1-\alpha}.
$$

Using

$$
0\leq a_{\mathrm{seen}}\leq1
$$

gives

$$
\boxed{
\max\left\{0,\frac{a_{\mathrm{mix}}-\alpha}{1-\alpha}\right\}
\leq a_{\mathrm{new}}
\leq
\min\left\{1,\frac{a_{\mathrm{mix}}}{1-\alpha}\right\}.
}
$$

For the constructed values $$a_{\mathrm{mix}}=17/20$$ and $$\alpha=2/5$$, this yields

$$
\frac34\leq a_{\mathrm{new}}\leq1.
$$

The aggregate alone cannot identify novel-case performance.

These bounds concern the novel subset. Transporting them to another clinical population still requires representativeness. Unknown provenance and unknown case mix are separate uncertainties.

### 12. Pretraining provenance is part of shortcut analysis

Provenance should describe more than the names of datasets.

| Provenance information | Why it matters |
|---|---|
| Patient and institution sources | Identifies overlap and site-associated regularities |
| Acquisition and reconstruction | Reveals which appearance changes were represented |
| Sampling and referral pathways | Describes disease spectrum and selection |
| Report production | Identifies templates, clinical context, and label-generating practices |
| De-identification and preprocessing | May introduce source-specific artifacts |
| Annotation and verification | Determines what supervised targets mean |
| Deduplication unit | Distinguishes file deduplication from patient independence |
| Training and checkpoint history | Establishes which releases may have encountered evaluation material |

A source cue may correlate with disease because of referral policy or labeling practice. More examples from that same process can make the association easier to learn.

Missing provenance is not proof that a model uses a shortcut. It limits the ability to rule out particular inherited dependencies and evaluate independence.

### 13. Evaluate the contribution of pretraining under controlled comparisons

A useful comparison holds the downstream question fixed:

- The same eligible patients and reference definition.
- The same patient-level partitions.
- Comparable local annotation budgets.
- Explicit adaptation and tuning budgets.
- The same examination aggregation and operating point.
- Independent evaluation after model selection.

Learning curves should vary the number of independently labeled patients, not only the number of frames. Frozen probes, partial tuning, and full tuning should be reported separately.

Broad averages across tasks can conceal the clinically relevant result:

$$
R_{\mathrm{average}}=\sum_jw_jR_j.
$$

A low average does not impose a low risk on every task. The target task needs its own estimate, uncertainty, and requirements.

Evaluation should also preserve the exact checkpoint, preprocessing, prompts, and adaptation recipe. An unversioned collection of these components does not identify the system that produced the result.

### 14. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| What does “foundation model” denote? | Broad pretraining and reuse across downstream tasks |
| Does scale establish clinical competence? | No; objectives, coverage, and validation remain separate |
| What does a linear probe test? | Accessibility through a restricted readout |
| Can useful information survive a failed probe? | Yes; the four-point construction contains a perfectly recoverable nonlinear target |
| Does recoverable clinical information prove reliance? | No; a downstream head can use another feature |
| Why do prompts belong in the evaluation? | They change the information available to the predictor |
| How can overlap inflate accuracy? | The evaluation mixes encountered and novel-case performance |
| What does unknown provenance limit? | Claims about independence, coverage, and inherited shortcuts |
| What establishes transfer? | A controlled downstream comparison |
| What establishes clinical validity? | Evidence for the specified clinical interpretation in the intended use |

In the ontology, pretraining is a method that can supply transferable representations. Transfer performance does not establish clinical validity or clinical evidence reliance. The clinical target determines what the adapted system must demonstrate.

## Why it matters for my work

For gallbladder ultrasound, I need to separate morphology available in an encoder from morphology used after adaptation. Prompting, source overlap, and inherited acquisition cues belong in that analysis, alongside the downstream diagnostic evaluation.

## What I have not resolved

- Which pretrained features support ultrasound morphology across acquisition settings?
- How does fine-tuning change clinical evidence reliance?
- What independent evaluation is possible when pretraining provenance is incomplete?

---

Sources: Independent study, with the foundation-model framing checked against the paper linked above. All numerical examples and bounds are constructed and derived explicitly. These are study notes for research purposes, not clinical guidance.
