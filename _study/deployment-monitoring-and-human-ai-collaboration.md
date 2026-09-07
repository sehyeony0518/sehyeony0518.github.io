---
layout: study_note
title: "Deployment, Monitoring, and Human-AI Collaboration"
description: "Drift after deployment, safety monitoring, automation bias, and what changes with a clinician in the loop."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "systems"
category_title: "Medical AI Systems & Deployment"
order: 8
source: "Independent study"
written: true
updated: "2026-09-08"
---

Deployment places a model inside a changing clinical workflow. Monitoring and human-AI collaboration concern whether that complete system continues to perform acceptably, including how people respond when predictions are useful, misleading, or unavailable.

## Core question and definition

A deployed system includes data interfaces, preprocessing, model versions, thresholds, displays, users, and escalation procedures. Retrospective accuracy measures only part of this arrangement. I would define the clinical responsibility of the system and the person receiving its output before interpreting performance in use.

The question is not whether a clinician remains nominally responsible. It is whether the combined workflow detects and manages errors under realistic time pressure, workload, and information constraints. Human involvement changes the behavior that must be evaluated.

## Key concepts

### Drift is a warning signal, not a diagnosis

Input distributions can change because of new scanners, referral patterns, or software. Outcome frequencies and the relationship between inputs and labels can also change. A detected shift does not necessarily imply harmful performance loss, while stable input summaries do not guarantee safety. I would connect drift indicators to subsequent clinical performance rather than interpret them as substitutes for outcome monitoring.

### Monitoring needs process and outcome measures

Process measures include missing inputs, failed predictions, latency, and alert delivery. Outcome-linked measures include diagnostic errors, calibration, and downstream actions once reliable labels become available. Labels may arrive late or only for selected patients. A dashboard showing stable prediction frequencies can therefore miss deteriorating performance, particularly if the reference process itself changes.

### Human review can introduce as well as correct errors

Automation bias describes inappropriate reliance on automated advice, including accepting an incorrect recommendation or failing to act without a prompt. Expertise, presentation, and workload can affect how advice is used. I would evaluate whether users detect incorrect outputs, not assume that displaying an explanation or adding an approval button makes review effective.

### Updates require an identifiable intervention

Changing a threshold, preprocessing step, or interface can alter clinical behavior even when model weights remain fixed. I would version the whole pipeline, record when changes take effect, and define evaluation and rollback procedures. Monitoring an unspecified mixture of versions makes it difficult to attribute a failure or determine whether a correction worked.

## Worked examples in medical AI

[Gaube and colleagues](https://doi.org/10.1038/s41746-021-00385-9) studied physicians interpreting chest radiographs with diagnostic advice, some of it incorrect. The advice was produced by human experts but attributed to either an AI system or a radiologist. Incorrect advice reduced diagnostic accuracy regardless of its stated source. This is evidence about susceptibility to advice, not a trial demonstrating the behavior of a deployed diagnostic model.

In a hypothetical gallbladder workflow, an AI alert could encourage closer review of a subtle wall abnormality. It could also draw attention away from an unflagged region or create enough false alarms that users stop responding. The same standalone model performance could therefore produce different clinical results depending on display design and how findings enter the reporting process.

## Evaluation methods and limitations

I would compare unaided clinicians, the model alone, and assisted clinicians where those comparisons fit the intended task. Relevant outcomes include error patterns, reading time, appropriate escalation, and consequences for patients. Case order, reader experience, and familiarity with the interface need attention. [DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9) provides reporting guidance for early live evaluation of AI decision support, including human interaction and workflow.

After deployment, I would combine automated checks with case review and a route for users to report unexpected behavior. Investigations should link model outputs to the actual examination, software version, and available reference. Alert limits and review responsibilities should be prespecified. Delayed or selectively observed outcomes constrain what monitoring can establish, and a quiet reporting channel does not demonstrate an absence of failures.

## Research connections and open questions

For gallbladder clinical faithfulness, I would monitor whether changes in acquisition or updates alter the evidence supporting predictions. Such audits could help explain a performance change, but their findings would still need connection to the actions clinicians take.

- Which signals can identify meaningful deterioration before enough verified outcomes accumulate?
- What explanation helps clinicians detect an error rather than simply increasing their trust?
- Who reviews a monitoring alert, and what evidence should trigger restriction, rollback, or reevaluation?

## References

- Gaube et al., [Do as AI say: susceptibility in deployment of clinical decision-aids](https://doi.org/10.1038/s41746-021-00385-9), npj Digital Medicine 2021.
- Vasey et al., [Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9), Nature Medicine 2022.
