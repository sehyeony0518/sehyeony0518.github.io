---
layout: study_note
title: "Reproducibility, Benchmarks, and Translational Study Design"
description: "Designing studies whose results survive contact with another site and another team."
og_image: "https://sehyeony0518.github.io/assets/img/og/reproducibility-benchmarks-and-translational-study-design.png"
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "evaluation"
category_title: "Evaluation, Generalization & Reliability"
subgroup: "Failure Analysis & Clinical Translation"
order: 15
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-02-09-underspecification-credibility-ml"
  - "2026-01-08-busbra-breast-ultrasound-dataset"
---

## Core question and definition

**What has been established when another run produces the same number, and what further evidence is needed for a finding to survive independent investigation and clinical use?**

Computational reproducibility concerns recovering a specified result from the stated data and computational procedure. Replication concerns whether independent investigation supports the substantive finding. Generalization concerns performance or conclusions beyond the conditions originally studied.

Terminology varies between fields. A useful report states what was repeated and what changed: data, implementation, training, investigators, population, acquisition, reference, or workflow.

These achievements are related but distinct. A biased analysis can be perfectly reproducible. A reproducible model can fail in a different population. An independently replicated prediction advantage can still lack clinical utility.

## Key concepts

### Reproducing a number can mean several things

| Repeated activity | What agreement supports | What remains untested |
|---|---|---|
| Run the same checkpoint on the same inputs | Inference and scoring reproducibility | Training reproducibility and new-patient performance |
| Retrain with the specified procedure | Recoverability of the training result or result distribution | Transport to a different clinical setting |
| Reimplement the method independently | Robustness to implementation details | Validity of the original sample and reference |
| Collect new data for the same substantive question | Replication under the new collection conditions | All other populations and workflows |
| Evaluate a different intended setting | Generalization to that specified setting | Universal generalization or patient benefit |

Numerically identical results can occur because the same inputs and errors were preserved. Conversely, small numerical differences can be unimportant when the substantive conclusion and relevant uncertainty remain unchanged.

The tolerance for reproduction should match the claim. Exact predictions from a checkpoint, a distribution of results across training runs, and a clinical comparison need different standards.

### The experiment is larger than the architecture

A result depends on cohort definition, exclusions, labels, patient grouping, acquisition, preprocessing, training data, initialization, optimization, model selection, and scoring.

For generative systems, prompts, retrieved context, decoding, selection, and evaluator versions also matter. For tool-using systems, tool behavior and external state can affect the trajectory.

An architecture diagram does not specify these choices. A reproducible description needs the information necessary to recover the evaluated procedure and its scope.

Data access is a separate issue from transparency. When patient data cannot be released, precise definitions, controlled access where possible, and executable evaluation instructions can still make assumptions inspectable. Synthetic examples can verify implementation behavior without reproducing the clinical population.

### Distinguish sources of variability

Let $$D$$ represent the evaluation data and $$A$$ the randomness in the specified development procedure. Let $$\widehat R$$ be its reported performance estimate.

Write

$$
\widehat R-\mathbb E[\widehat R]
=
\bigl(\widehat R-\mathbb E[\widehat R\mid D]\bigr)
+
\bigl(\mathbb E[\widehat R\mid D]-\mathbb E[\widehat R]\bigr).
$$

The first term has conditional mean zero given $$D$$. Therefore its expected cross-product with the second term is zero.

Squaring and taking expectations gives

$$
\operatorname{Var}(\widehat R)
=
\mathbb E_D\!\left[\operatorname{Var}(\widehat R\mid D)\right]
+
\operatorname{Var}_D\!\left(\mathbb E[\widehat R\mid D]\right).
$$

Repeated training runs on one fixed evaluation collection examine conditional variability for that collection. They do not, by themselves, establish variability across new patient samples or sites.

Likewise, a confidence interval based on one checkpoint's evaluated cases does not automatically include uncertainty from all development and selection choices.

### A benchmark defines a measurement, not the entire clinical task

A benchmark fixes a sample, input format, target, reference, split, and scoring rule. Its value is that it makes a particular comparison tractable.

Its limitations follow from those choices. A lesion-classification benchmark may assume that someone has already found and cropped the lesion. A report benchmark may supply context unavailable at the intended decision time. A diagnostic label may reflect a coding rule rather than independent clinical adjudication.

Thus the benchmark is a measurement instrument with a defined domain. A higher score is evidence about that instrument's task, not automatically about every clinical capability suggested by its name.

Comparison conditions also matter. Additional pretraining data, different information access, or a larger selection budget can change the result without isolating the contribution of the proposed method.

### Why selecting the best score creates optimism

Construct $$M$$ candidate methods with identical true performance $$\mu$$. Their evaluation estimates are

$$
\widehat\mu_j=\mu+\varepsilon_j,
$$

where each error independently equals $$+d$$ or $$-d$$ with equal probability.

Every candidate is unbiased before selection:

$$
\mathbb E[\widehat\mu_j]=\mu.
$$

Select the candidate with the highest observed estimate. Its score is

$$
\max_j\widehat\mu_j=\mu+\max_j\varepsilon_j.
$$

The maximum error is $$-d$$ only when all errors are negative, an event with probability $$2^{-M}$$. Otherwise it is $$+d$$.

Therefore

$$
\begin{aligned}
\mathbb E[\max_j\varepsilon_j]
&=
d(1-2^{-M})-d\,2^{-M}\\
&=
d(1-2^{1-M}),
\end{aligned}
$$

and

$$
\mathbb E[\max_j\widehat\mu_j]
=
\mu+d(1-2^{1-M}).
$$

The winner looks better even though all candidates have the same true performance.

This construction isolates selection bias. Its two-point independent errors are illustrative assumptions, not a literal model of all benchmark results.

### Worked example: a gain produced entirely by selection

Choose

$$
\mu=\frac45,\qquad d=\frac1{20},\qquad M=4.
$$

Each candidate's observed score is either

$$
\mu-d=\frac34
$$

or

$$
\mu+d=\frac{17}{20}.
$$

All four estimates are low with probability $$1/16$$. Otherwise the selected estimate is high. Hence

$$
\begin{aligned}
\mathbb E[\text{selected score}]
&=
\frac1{16}\frac34
+
\frac{15}{16}\frac{17}{20}\\
&=
\frac{27}{32}
=
0.84375.
\end{aligned}
$$

The selected model's true performance remains

$$
\frac45=0.8.
$$

The expected optimism is

$$
\frac{27}{32}-\frac45
=
\frac7{160}
=
0.04375.
$$

All numbers follow from the construction. There is no genuine performance improvement.

Actual candidates often have correlated errors. Correlation changes the size of selection bias; perfectly shared errors need not create this particular gain. It does not justify treating a repeatedly consulted test collection as independent confirmation.

### Benchmark reuse creates an information channel

A test set can influence development through published scores, error examples, leaderboard feedback, or informal inspection. Later methods may be selected because they fit those known weaknesses.

This can happen without directly inserting test labels into the training loss. The broader research process can adapt to the collection.

Repeated evaluation is not inherently invalid. A genuinely prespecified evaluation does not become biased merely because a computer runs it twice. The issue is whether feedback affects subsequent choices while the same data continue to be described as untouched confirmation.

Direct inclusion of benchmark material in pretraining is a different problem: contamination of the input or target knowledge. When provenance is unknown, that uncertainty limits how confidently benchmark performance can be interpreted as evidence of new-task transfer.

### Saturation can conceal unresolved clinical failures

A nearly saturated benchmark may have little remaining ability to discriminate methods. Differences can depend on a few cases, disputed labels, or scoring conventions.

Saturation can also indicate that the benchmark's task is narrow. It may omit difficult acquisition, rare but important findings, incomplete information, or the consequences of actions.

Neither saturation nor high accuracy establishes that all clinically relevant problems have been solved. It establishes performance against the benchmark's represented cases and rules.

The appropriate extension depends on the unresolved claim. More difficult cases can probe robustness, while a representative clinical population estimates routine performance. A deliberately difficult challenge collection should not be assigned the interpretation of a prevalence-representative sample.

### Replication should target the substantive conclusion

A claim might concern superiority to a comparator, recognition of a clinical finding, or an improvement in decision quality. Replication should specify which claim is being reconsidered.

Another team using the same data can expose implementation dependence. Another dataset can expose sampling or acquisition dependence. A new clinical setting can expose workflow dependence.

A failure to reproduce the exact original number does not necessarily refute the substantive finding. Conversely, reproducing the number does not rescue a conclusion that relied on an inappropriate reference or comparator.

Independent confirmation is strongest when the choices that could favor the original conclusion are clearly separated from the confirming evidence.

### What prospective observation adds

Prospective evaluation specifies relevant procedures before the incoming cases and outcomes are fully known. It can directly observe whether the pipeline receives the expected inputs, operates within real timing constraints, and handles missing or ambiguous information as patients arrive.

Retrospective studies can address many of these questions when detailed time-stamped records exist. Prospective collection is not automatically unbiased, externally valid, or causal.

Its distinctive contribution is direct evidence about the system under the actual conditions being observed. A retrospective archive cannot reveal clinician responses to a system that was never used, nor actions and failures that were never recorded.

The useful distinction is therefore what new process is observed, not merely whether the calendar date is later.

### Separate silent, live, and comparative evaluation

| Evaluation | What it can add | What it cannot establish alone |
|---|---|---|
| Retrospective analysis | Performance on recorded cases and defined references | Actual interaction with an undeployed system |
| Prospective silent operation | Input availability, timing, integration, and prediction behavior on incoming cases | Effects of showing the output to clinicians |
| Early live use | Interpretation, usability, correction, and operational failure modes | An unbiased estimate of comparative patient benefit |
| Comparative clinical evaluation | Differences in decisions or outcomes under specified use | Transport to every future setting |

Silent operation does not test automation bias because users do not act on the hidden output. Live use can reveal that clinicians ignore useful alerts or overinterpret misleading ones.

A change in behavior is not necessarily an improvement. The clinical outcome and burdens need their own evaluation.

### Why a prospective comparison is not automatically causal

Suppose assisted care is used mainly for unusually difficult patients. Worse outcomes in that group could reflect case complexity rather than harm from assistance. Better outcomes could reflect extra attention or access to specialists.

Calendar order can also confound a before–after comparison if practice, staffing, or referral changes over time.

Random assignment can address confounding of assignment under appropriate conditions. Let $$A$$ indicate assignment, and let $$Y(1)$$ and $$Y(0)$$ be outcomes under the two assigned pathways.

With random assignment independent of these potential outcomes and with consistency,

$$
\begin{aligned}
\mathbb E[Y\mid A=1]-\mathbb E[Y\mid A=0]
&=
\mathbb E[Y(1)\mid A=1]
-
\mathbb E[Y(0)\mid A=0]\\
&=
\mathbb E[Y(1)]-\mathbb E[Y(0)].
\end{aligned}
$$

The first equality uses the connection between assignment and observed outcome. The second uses independence from random assignment.

The interpretation still depends on follow-up, outcome measurement, interference between groups, and the actual assignment scheme. Randomization does not repair a clinically irrelevant endpoint.

### The intervention includes the surrounding workflow

The evaluated intervention includes the model version, interface, instructions, users, escalation, handling of unavailable outputs, and downstream actions.

Changing one of these can change the intervention. A model shown as an optional suggestion differs from the same model used to trigger an automatic action.

Human learning can also spread across groups, especially in shared workflows. The unit of allocation and analysis needs to account for such dependence rather than assuming every encounter is isolated.

An analysis based only on cases where a prediction was successfully produced can omit precisely the patients for whom the pipeline is least reliable. Failures to produce an answer should be handled according to the prespecified clinical question, not quietly removed.

### Worked reasoning: a reproducible system that does not yet translate

Consider a hypothetical image model reproduced by a second team using the original checkpoint and inputs. The predictions match.

Independent retraining then supports the same substantive comparison, but a new hospital has different acquisition and reference practices. Performance changes there. That does not make the original inference code irreproducible; it limits the transport claim.

During silent operation, the service finds that a required expert annotation is unavailable at the intended decision time. The retrospective task was therefore easier than the deployment task.

During live use, clinicians may still find the output confusing or may take actions that add burden without benefit.

Each stage exposes a different assumption. Repeating the original benchmark number cannot settle them.

### Documentation supports scrutiny rather than certifying correctness

Useful records include versioned eligibility definitions, references, split membership, preprocessing, model and software versions, randomization or sampling procedures where applicable, selection decisions, and scoring code.

For clinical evaluation, the comparator, outcomes, follow-up, unavailable predictions, deviations, and model updates also need to be clear.

Reporting guidelines help readers see these choices. They do not establish that the choices were appropriate, the reference was valid, or the study had enough information to support its conclusion.

The aim is an inspectable chain from the stated question to the evidence, including failures and limitations.

### Revision checklist

| Question | Answer to retain |
|---|---|
| Does repeating a number validate the conclusion? | No; the same bias can be reproduced. |
| What should reproducibility terminology specify? | Exactly which data, implementation, procedure, and setting were repeated. |
| Do repeated seeds measure new-population uncertainty? | No; they examine variability conditional on the evaluated data. |
| Why is the best observed score optimistic? | Selection preferentially retains favorable estimation errors. |
| Is repeated test execution itself the problem? | No; adaptive use of its feedback compromises independent confirmation. |
| Does saturation establish clinical completeness? | No; the benchmark may omit important conditions and outcomes. |
| What does prospective silent use add? | Direct observation of pipeline behavior on incoming cases. |
| Does silent use establish clinician–AI benefit? | No; users are not acting on the output. |
| Does prospective mean randomized? | No; assignment and confounding remain separate design questions. |
| What is the clinical intervention? | The complete system and workflow as delivered. |

## Why it matters for my work

Reproducibility makes an evidence claim inspectable. Replication examines whether the finding survives independent investigation. External validation and prospective evaluation extend different parts of the claim, while Clinical utility still requires evidence about the consequences of use. None can replace the others.

## What I have not resolved

- Which development choices have already been informed by the nominal test evidence?
- What new uncertainty would another study actually resolve?
- Is the claimed improvement computational, predictive, operational, or clinical?

---

Sources: Standard probability and study-design principles; published work on adaptive data analysis and holdout reuse; medical-imaging AI reporting guidance; and the established reporting frameworks for early live AI evaluation and comparative AI trials. The selection-bias example is a mathematical construction, not an empirical benchmark result. These are study notes for research purposes, not clinical guidance.
