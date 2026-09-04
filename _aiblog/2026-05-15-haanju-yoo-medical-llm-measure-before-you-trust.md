---
layout: post
title: "Measure Before You Trust: Haanju Yoo on Medical LLMs, Hallucination, and Clinical Workflow"
date: 2026-05-15 12:00:00 +0900
description: "Notes from NAVER Cloud's Haanju Yoo on medical LLMs, hallucination, self-consistency, regulation, and why the path to useful healthcare AI begins with defining what can actually be measured."
tag: "NAVER"
featured: true
related_posts: false
---

Large language models are impressive partly because they can answer questions we never explicitly trained them to answer. In medicine, that is also exactly what makes them difficult to trust: as the capability expands, so does the space of possible failure.

That tension was at the center of a 2023 interview with **Dr. Haanju Yoo**, then head of NAVER Cloud's Digital Healthcare Lab, conducted by Dr. Yoon Sup Choi. ([Yoon Sup Choi][1]) What I found most interesting was that Yoo did not frame the central challenge as building a larger or more medically knowledgeable model. The deeper problem was **evaluation**: if we cannot specify where a medical LLM fails, how often, and which failures matter clinically, we cannot systematically improve it, or trust it.

Any errors of interpretation are mine.

## Part 1. Why language models fit medicine, and why they fail there

Foundation models change where development begins: instead of training each clinical task from scratch, a model pretrained on broad data is adapted to many downstream tasks. Yoo emphasized that the defining feature is not parameter count but **generality**, and was appropriately cautious about "emergent" abilities, some of which depend on how performance is measured.

Medicine is unusually well matched to language models because it is document-heavy (knowledge lives in text, and care itself generates text) and because clinicians must recall and synthesize more information than attention comfortably allows.

But the same mechanism that produces fluent answers produces the core weakness. A language model is trained to generate a *plausible continuation*, not a *guaranteed truth*. Faced with a rare or ambiguous case, it still has to generate something, and it may add a medication never prescribed or a diagnosis unsupported by the record, in prose polished enough to make the error harder to catch. Hallucination is therefore not a cosmetic bug. It is a **faithfulness problem**: distinguishing what the current evidence supports from what merely resembles what is usually said.

## Part 2. Confidence, consistency, and retrieval are signals, not guarantees

Three tempting fixes each move the problem rather than solving it.

**Token probability** describes linguistic continuation, not factual correctness, a conventional sentence can be confidently false, and a rare but correct term can look "uncertain."

**Self-consistency**, asking the model the same question several times and checking agreement, provides a useful uncertainty signal, but ten generations can confidently repeat the same misconception. It measures agreement with oneself, not with reality, and every extra generation has a serving cost.

**Retrieval-augmented generation** anchors answers to external evidence, which is valuable for patient-specific questions: but it moves trust upstream: was the right document retrieved, fully, interpreted correctly, and actually applicable to this patient? Grounding helps only if the grounding process is itself evaluated.

## Part 3. The hardest problem is deciding what to measure

Yoo's remark that stayed with me: *to improve hallucination, we first need a way to measure where it happens.*

For classifiers the framework is clear: labels, ground truth, sensitivity, AUROC. For a medical LLM, a record summary, a question answered, and a patient-education text each require a **different failure taxonomy**: omissions, inventions, temporal confusion, reversed negations, wrong attributions. "Medical LLM accuracy" is too broad to be a measurement target; the useful unit is the **clinical use case**: *for this workflow, on this population, given this source information, which clinically relevant errors occur and how often?*

The licensing-exam results deserve the same caution. A human physician's competence can be established with a finite exam because of what we assume about human generalization and supervision. A model could answer millions of questions well and still fail bizarrely in a rare region of the input space. The regulatory question is not whether the model *knows medicine* but whether it *behaves predictably enough for a specified use*.

## Part 4. Regulation through intended use, and the case for smaller descendants

Should ChatGPT be a medical device because someone can ask it a medical question? Yoo was skeptical: regulating every possible misuse of a general model is conceptually incoherent. The situation changes when a system is deliberately built for a clinical function: optimized on healthcare data, embedded in a defined workflow, aimed at specific users. Then there is a concrete configuration to evaluate. A general model becomes clinically testable only after its role becomes less general.

The same logic argues against using the largest model everywhere. A hospital-documentation model does not need every capability of a consumer assistant. Specialized descendants of a foundation model are cheaper, faster: and, because their output space is narrower, **easier to validate**. The process that reduces cost also improves auditability.

## Part 5. NAVER started from workflow, not diagnosis

NAVER's healthcare projects were consistently placed where information is lost or attention is overloaded, rather than where a diagnosis could be automated: pre-visit questionnaires (Smart Survey), automatic documentation from consultations (Voice EMR: which could not simply translate an American product, given Korean documentation style and workflow), longitudinal coaching, conversational check-ins for older adults living alone (CareCall), and screening-result summaries for clinicians.

Revisiting the interview, that philosophy visibly became a product line. By 2025–2026, NAVER Cloud was operating **CLOVA Voice EMR** and a **CLOVA Nursing Agent**, and presenting a HyperCLOVA X-based medical foundation model alongside CLOVA Smart Care. ([CLOVA][3], [KRnet][2]) Not "an LLM for healthcare": an LLM for documenting a consultation, supporting a screening visit, organizing ward requests. **The technology became useful as the use cases became narrower.**

## Part 6. Reliability is a property of the whole system

Hallucination will be partly reduced at the model level. But clinical reliability also depends on the source information, retrieval, prompt, population, interface, reviewing clinician, escalation policy, and post-deployment error measurement. A medical LLM can become safer with the foundation model unchanged: restrict the intended use, ground on patient-specific evidence, require citations, detect unsupported claims, add human review, monitor failure categories. The model matters; the surrounding control system matters just as much.

## A researcher's takeaway

The principle beneath the whole conversation: **what we cannot measure, we cannot systematically improve.**

For generative medical AI, the usual research order may need to be reversed: define the clinical task precisely enough to know what failure means, build the test around that definition, and only then optimize. A plausible answer is not enough; a confident answer is not enough; even a consistently repeated answer is not enough. The question is whether the conclusion is supported by the evidence that should matter for this patient and this task, the same question clinical evidence auditing asks of imaging models, extended to language.

The future of medical LLMs may depend less on proving that a model knows everything about medicine, and more on knowing, with increasing precision, **where it can be trusted, and where it cannot.**

[1]: https://www.yoonsupchoi.com/2023/10/28/haanjuyoo-interview/ "유한주 박사 인터뷰: 최윤섭의 디지털 헬스케어"
[2]: https://krnet.or.kr/board/board.php?category=1568&db=dprogram&no=2970&page=6&pageID=ID13249498101&task=view "KRnet 2026, NAVER Cloud Digital Healthcare Lab"
[3]: https://clova.ai/tech-blog/네이버-ai-의료진의-시간을-되찾다-healthcare-ai팀의-이야기 "NAVER CLOVA Healthcare AI 팀 이야기"
