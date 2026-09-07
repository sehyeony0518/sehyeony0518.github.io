---
layout: page
title: "Clinical Validity and Clinical Utility"
description: "The difference between a model that measures something real and a model that changes a decision, and why the second does not follow from the first."
section: "I"
section_title: "Trustworthy Medical AI"
branch: "Branch 01"
order: 1
written: true
---

Clinical validity concerns whether a model's output supports its intended clinical interpretation in the intended population. Clinical utility concerns whether using that output improves care or its delivery compared with a relevant alternative.

## Why it matters here

A model can identify something real without changing an actionable decision. It can also change decisions in ways that add unnecessary investigations, delay care, or redistribute workload. I therefore need to trace a claim from the output being evaluated to the action it supports and the consequences of taking that action.

My clinical faithfulness work addresses one part of that sequence: whether a prediction is supported by clinically meaningful evidence. Gallbladder ultrasound AI makes the next part concrete. Even a well-supported prediction needs a defined role in assessment, surveillance, or referral before I can explain what benefit its use is expected to provide.

## The core ideas

### Validity starts with an intended interpretation

Technical accuracy, clinical association, and clinical validation answer related but distinct questions. Software might measure a lesion consistently while the derived score has an uncertain relationship to the intended diagnosis. The IMDRF Software as a Medical Device clinical evaluation framework, adopted by the FDA, distinguishes these layers. For my purposes, validity requires an explicit target, reference standard, population, and use. Agreement with management labels supports a different interpretation from agreement with pathology, even when both are described as diagnostic accuracy.

### Predictive performance does not specify a decision

Discrimination concerns whether the model orders patients appropriately; calibration concerns agreement between predicted risks and observed outcomes. Neither tells me which action should follow a score. That depends on the available actions, their consequences, and the information already used in care. A model could improve ranking without changing decisions near the relevant operating range. I would ask what it adds to the existing clinical assessment, rather than comparing it only with an uninformed baseline.

### Decision analysis connects predictions to consequences

Decision curve analysis evaluates net benefit across threshold probabilities, using each threshold to express a tradeoff between false-positive and false-negative consequences. The method introduced by [Vickers and Elkin](https://pubmed.ncbi.nlm.nih.gov/17099194/) makes that tradeoff explicit when comparing prediction strategies. Its usefulness depends on credible thresholds, appropriate data, and a clearly defined action. An apparently favorable curve estimates potential value under those assumptions. It does not demonstrate that clinicians followed the strategy or that patients experienced better outcomes.

### Clinical use changes what must be evaluated

When clinicians see a model output, their interpretation, timing, and response become part of the intervention. A retrospective analysis cannot observe those interactions. Early live evaluation can examine workflow, safety, and user behavior, while a suitable comparative study is needed to estimate effects attributable to introducing the system. [DECIDE-AI](https://www.bmj.com/content/377/bmj-2022-070904) supports reporting of early clinical evaluation, including human factors. I read it as a framework for making that evidence inspectable, not as proof that a reported system is effective.

### Faithfulness and utility support different claims

A model could improve decisions in a particular workflow while relying partly on an acquisition shortcut. Conversely, a model could use clinically meaningful evidence without adding value to an experienced clinician's assessment. These possibilities are why I would evaluate evidence use and clinical consequences separately. A successful utility study would not resolve every concern about transfer to another hospital. An encouraging faithfulness audit would not establish that deploying the model improves care.

## Where it touches my work

For a gallbladder ultrasound model, I would first specify a proposed action, such as prioritizing examinations for additional clinician review. I would then compare that pathway with current practice, measuring appropriate review, missed important findings, additional work, and consequences for patients. Clinical faithfulness auditing would accompany this evaluation by checking whether the output remains connected to the intended evidence across devices and patient groups. This would let me identify whether a problem arises in the prediction, its supporting evidence, or the clinical response.

## What I have not resolved

- Which gallbladder decision has enough unresolved uncertainty for a model to add useful information beyond the existing assessment?
- What outcomes and follow-up would capture benefit without overlooking unnecessary procedures or delayed diagnoses?
- How should evidence from a successful local workflow influence confidence in another hospital with different readers, referral practices, and resources?
