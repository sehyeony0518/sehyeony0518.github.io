---
layout: study_note
title: "Medical AI Agents and Tool-Using Clinical Systems"
description: "Observe, reason, act: the loop underneath agent systems, and the verification and recovery problems it creates."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "systems"
category_title: "Medical AI Systems & Deployment"
order: 6
source: "Independent study"
written: true
updated: "2026-09-08"
---

A tool-using medical AI system can gather information, select an action, inspect its result, and decide what to do next. Its reliability depends on the entire sequence, including whether actions were appropriate and whether their outcomes were verified.

## Core question and definition

I use “agent” for a system that selects successive actions based on observations and a task objective. Those actions might retrieve records, call an image-analysis model, calculate a score, or prepare a report. The degree of autonomy varies, so the term alone says little about clinical authority.

The question is whether this sequence reliably supports a defined clinical decision. A correct final answer can conceal an inappropriate test request, a mistaken patient match, or a failed tool call that the system silently treated as successful.

## Key concepts

### The loop operates on incomplete observations

The system sees a representation of the clinical situation, not the situation itself. Each action can reveal additional information or alter what happens next. [ReAct](https://arxiv.org/abs/2210.03629) explores interleaving language-based reasoning and actions. I read the resulting trace as a record to inspect, not proof that the written rationale faithfully describes the model's internal computation.

### Tools need explicit input and output contracts

A valid call requires the correct patient, examination, modality, units, and time context. A tool may return a technically valid result for an inappropriate input. I would separate schema validation from clinical applicability: confirming that a value is numeric does not establish that it belongs to the current patient or supports the intended decision.

### Retrieval supplies evidence, not authority

Retrieved notes can be incomplete, outdated, or contradictory. A citation establishes where text came from only if the source is correctly linked; it does not establish that the source supports the generated claim. I would also treat instructions embedded in retrieved material as document content, not permission for the agent to change its task or access additional systems.

### Recovery is part of the intended behavior

A timeout leaves uncertainty about whether an action occurred. Retrying a retrieval is different from repeating an order or message. I would define bounded retries, stopping conditions, escalation, and checks for duplicate actions. The system should distinguish an observed negative result from unavailable information and should preserve that distinction in its final output.

## Worked examples in medical AI

[AgentClinic](https://arxiv.org/abs/2405.07960) evaluates agents in simulated clinical environments involving patient interaction, information gathering, and tools. Such simulations can expose failures that a single question-answer benchmark misses. Their patients, tools, and outcome rules remain approximations, so success does not establish that an agent can safely perform the corresponding activity in a hospital.

Consider a hypothetical gallbladder review assistant. It retrieves the current ultrasound examination, calls a quality-assessment tool, compares a lesion measurement with a prior study, and drafts a summary. If the prior measurement belongs to a different lesion, the arithmetic can be correct while the growth claim is wrong. The relevant test is whether the system verifies anatomical correspondence before making that comparison.

## Evaluation methods and limitations

I would evaluate complete trajectories as well as final answers: appropriate information gathering, tool selection, argument accuracy, evidence support, recovery, and unnecessary actions. Repeated runs matter because stochastic choices can produce different paths. Time and resource use should be measured alongside clinical correctness, especially when further calls add little useful evidence.

Tests should include missing records, ambiguous identifiers, conflicting findings, failed tools, and misleading retrieved content. A system that performs well only when every component succeeds has not demonstrated recovery. Human review should be evaluated as an actual workflow, including what the reviewer can inspect and how often they detect problems. A nominal approval step cannot compensate for an opaque or misleading action history.

## Research connections and open questions

For my clinical faithfulness work, an agent could organize existing image models and evidence audits without retraining them. I would want its conclusion to remain traceable to the ultrasound, independent clinical factors, and verified tool results, rather than to an internally coherent narrative.

- Which actions require clinical judgment that cannot be reduced to a tool's input schema?
- How can I test whether retrieved evidence changes a conclusion for the right reason?
- What information must a clinician see to recognize and recover from an incorrect action sequence?

## References

- Yao et al., [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629), ICLR 2023.
- Schmidgall et al., [AgentClinic: a multimodal agent benchmark to evaluate AI in simulated clinical environments](https://arxiv.org/abs/2405.07960), arXiv 2024.
