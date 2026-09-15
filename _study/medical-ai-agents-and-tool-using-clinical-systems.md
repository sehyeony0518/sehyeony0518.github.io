---
layout: study_note
title: "Medical AI Agents and Tool-Using Clinical Systems"
description: "Observe, reason, act: the loop underneath agent systems, and the verification and recovery problems it creates."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "systems"
category_title: "Medical AI Systems & Deployment"
order: 5
source: "Independent study"
written: true
updated: "2026-09-08"
---

## Core question and definition

**What changes when a medical AI system selects actions, and why must its evaluation follow the entire trajectory?**

A tool-using system can retrieve information, invoke another model, perform a calculation, prepare a document, or initiate an authorized action. Later choices depend on what earlier steps returned.

This creates more than an answer-quality problem. The system can reach a correct conclusion through an unsafe action, operate on the wrong patient, or mistake an unavailable result for a negative finding.

“Agent” describes a pattern of sequential interaction, not a level of clinical authority. The permitted actions, intended user, stopping conditions, and role of human review must be specified separately.

## Key concepts

### The system acts on observations, not the complete clinical state

Let $$o_t$$ denote the observation available after step $$t$$ and $$a_t$$ an action. A history can contain prior observations and actions:

$$
h_t=(o_0,a_1,o_1,\ldots,a_t,o_t).
$$

A policy selects the next action from that history:

$$
a_{t+1}\sim\pi(\,\cdot\mid h_t).
$$

The clinical state is only partly observed. A record can be incomplete, a tool can return an outdated result, and a patient can change while the system is working.

An action can reveal information or change the environment. Retrieving a report and placing an order therefore have different consequences, even when both are represented as tool calls.

A written reasoning trace records what the system says about its process. It is not proof that the text faithfully exposes the computation that selected each action.

### Why the trajectory is the evaluation unit

A trajectory contains the sequence of observations, actions, results, and termination:

$$
\tau=(o_0,a_1,o_1,\ldots,a_T,o_T).
$$

The final answer is only one component.

A complete evaluation can ask whether the system used the correct patient record, selected an appropriate tool, supplied valid arguments, interpreted the result correctly, recovered from failures, and stopped without unnecessary or unauthorized actions.

Different trajectories can yield identical final text. One may retrieve the correct evidence; another may obtain the answer by chance after using the wrong record. Final-answer grading cannot distinguish them.

Conversely, a trajectory that recognizes insufficient information and stops may be appropriate even though it does not produce the requested clinical conclusion.

### Tool validity has several layers

| Layer | Example question | Why passing an earlier layer is insufficient |
|---|---|---|
| Syntax | Is the request in the accepted format? | A valid request can name the wrong examination. |
| Identity | Does the information belong to the intended patient and encounter? | Correct identity does not establish temporal relevance. |
| Semantics | Are units, anatomical sites, and variable meanings correct? | Correctly interpreted data can still be clinically inapplicable. |
| Applicability | Is this tool suitable for this population and input? | A technically successful calculation can be used outside its scope. |
| Execution | Did the requested operation actually occur? | An acknowledgment may not establish completion. |
| Clinical consequence | Was the action appropriate and useful? | Successful execution is not the same as beneficial care. |

A numeric return value proves neither that the calculation used appropriate inputs nor that its result should influence the intended decision.

The tool contract must therefore include clinical context, not only a machine-readable schema.

### Derive how reliability compounds

Consider a trajectory with a fixed number $$T$$ of required stages. Let $$A_t$$ be the event that stage $$t$$ meets its specified acceptability requirement, and define

$$
S_t=A_1\cap\cdots\cap A_t.
$$

Repeated application of conditional probability gives

$$
\begin{aligned}
P(S_T)
&=P(S_{T-1})P(A_T\mid S_{T-1})\\
&=P(A_1)\prod_{t=2}^{T}P(A_t\mid S_{t-1}).
\end{aligned}
$$

Define

$$
q_1=P(A_1),
\qquad
q_t=P(A_t\mid S_{t-1})\quad(t>1).
$$

Then

$$
P(S_T)=\prod_{t=1}^{T}q_t.
$$

This identity does **not** require independent stages. The probabilities are conditional on the preceding stages having been acceptable.

If every conditional probability equals $$q$$, then

$$
P(S_T)=q^T.
$$

Independent stages with identical marginal reliability are one setting in which this applies. A pooled average of isolated tool accuracies is not enough to justify it.

### Worked example: reliable stages, less reliable completion

Construct a system in which every required stage has conditional reliability

$$
q=\frac{99}{100}.
$$

The resulting probabilities that all stages are acceptable are:

| Required stages | Calculation | All-stage acceptability |
|---|---|---|
| One | $$q$$ | $$0.99$$ |
| Two | $$q^2$$ | $$0.9801$$ |
| Five | $$q^5$$ | $$0.9509900499$$ |
| Ten | $$q^{10}$$ | $$0.90438207500880449001$$ |

These values follow from the construction. They are not measured reliability figures for a medical agent.

The calculation concerns an all-stages requirement. It is not automatically the probability of patient benefit or even final task success. Those outcomes depend on whether the chosen stages were sufficient and whether failures can be recovered.

### Derive a per-stage error requirement

Suppose all conditional stage reliabilities equal $$1-\varepsilon$$, and the allowed probability of any unacceptable stage is at most $$\delta$$.

The requirement is

$$
(1-\varepsilon)^T\ge 1-\delta.
$$

Taking the positive $$T$$th root gives

$$
1-\varepsilon\ge(1-\delta)^{1/T},
$$

so

$$
\varepsilon\le 1-(1-\delta)^{1/T}.
$$

For a constructed target of at least $$0.95$$ all-stage acceptability over ten stages,

$$
q\ge 0.95^{1/10}
\approx 0.9948838031,
$$

and therefore

$$
\varepsilon\lesssim 0.0051161969.
$$

The decimals are evaluations of the displayed expressions, not proposed clinical acceptance thresholds.

For small $$\delta$$, the logarithmic expansion gives

$$
(1-\delta)^{1/T}
=
\exp\!\left(\frac{\log(1-\delta)}{T}\right)
\approx
1-\frac{\delta}{T}.
$$

Hence the required stage error is approximately

$$
\varepsilon\lesssim\frac{\delta}{T}.
$$

A longer chain can require much smaller errors at each essential stage than an isolated benchmark might suggest.

### What dependence changes

Identical marginal accuracies do not identify the joint probability of success.

Construct two stages, each with marginal reliability $$9/10$$.

- If failures always occur together, both stages pass with probability $$9/10$$.
- If failures are independent, both pass with probability $$81/100$$.
- If their failure events are disjoint, both pass with probability $$8/10$$.

The same per-stage marginal reliability therefore permits different trajectory reliability.

The conditional formula remains correct. In the first construction, passing the first stage guarantees passing the second. In the disjoint-failure construction, the second-stage reliability conditional on first-stage success is $$8/9$$.

Shared patient-identification errors, misleading records, and common tool assumptions can create dependence in real systems. Stage scores measured separately can miss these common causes.

### A dependence-free sufficient bound

Let $$F_t$$ denote failure at stage $$t$$ in a fixed-stage specification. The union bound gives

$$
P\!\left(\bigcup_{t=1}^{T}F_t\right)
\le
\sum_{t=1}^{T}P(F_t).
$$

If each marginal stage failure probability is at most $$\varepsilon$$, then

$$
P(\text{any stage fails})\le T\varepsilon.
$$

Thus

$$
\varepsilon\le\frac{\delta}{T}
$$

is a sufficient condition for an overall failure bound of $$\delta$$, without assuming independence.

This can be conservative. It is also only as meaningful as the failure definitions and the populations on which the stage probabilities are assessed.

Unobserved stages after an early termination cannot simply be counted as successful observations.

### Recovery changes the success event

A failed retrieval followed by correct recognition, a successful retry, and an appropriate final response need not be an unsuccessful task.

Conversely, an apparently successful sequence can be unsafe if it completes an inappropriate action. All calls returning normally is a weak success definition.

Recovery introduces additional states: uncertainty about execution, verification, retry, escalation, and termination. Evaluation should distinguish an initially successful path from a recovered path and from an unresolved failure.

Adding steps can improve the system when those steps provide effective verification or recovery. The product calculation does not imply that the shortest trajectory is always best; changing the policy changes both the stages and their conditional probabilities.

### Error attribution is not the same as causal credit

An incorrect tool result followed by an incorrect answer is evidence of a failure sequence. It does not by itself quantify how much that step caused the final error.

The case may already have been difficult, an earlier action may have selected the wrong input, or a later step may have ignored contradictory evidence. Multiple steps can be jointly sufficient for the failure.

Changing one step can also change all later observations and choices. Treating the rest of the trajectory as unaffected can describe a sequence the system would never actually follow.

The distinction is between locating an observed failure, identifying a plausible mechanism, and establishing a causal contribution. Trace inspection is useful for the first two without automatically settling the third.

A correct final answer likewise does not absolve an unsafe intermediate action.

### Retrieval provides evidence with provenance

Retrieved information needs the correct patient, encounter, date, source, and scope. An older normal report may be accurately retrieved but irrelevant to the current clinical question.

Conflicting sources require interpretation. A copied problem list, preliminary report, and finalized interpretation do not have identical evidential status.

A citation confirms provenance only when it points to the actual source. The source must still support the statement, and the statement must remain applicable to the current task.

Instructions embedded in retrieved material are document content. They do not confer authority to change the system's objective or perform additional actions.

### Read actions and write actions need different failure handling

Retrieving a document usually changes what the system knows. Sending a message, placing an order, or modifying a record changes the environment and can affect care.

A timeout after a write creates uncertainty: the action may have occurred even though its confirmation was lost. Retrying without checking can duplicate an action.

Recovery therefore needs an account of execution state, acknowledgments, duplicate prevention, and responsibility for unresolved actions. A tool-call log alone may not establish what happened in the clinical system.

Permissions and review should correspond to the action's consequences. A nominal human approval step is not sufficient if the reviewer cannot see the evidence, intended action, and uncertainty.

### Worked reasoning: correct arithmetic, wrong comparison

Consider a hypothetical assistant that retrieves a current examination and a prior report, extracts lesion measurements, computes a change, and drafts a summary.

Suppose the prior measurement refers to a different lesion.

The retrieval can succeed technically. The numbers can be transcribed correctly. The arithmetic can be exact. The resulting growth claim is still wrong because anatomical correspondence failed.

The actionable category is not “bad at subtraction.” It is failure to establish that the quantities refer to the same clinical object under a meaningful comparison.

If the system recognizes that correspondence is unresolved and withholds the growth claim, that is appropriate handling of uncertainty, not a failed calculation.

This illustrates why semantic checks and trajectory context belong beside final-answer scoring.

### What trajectory evaluation should retain

| Aspect | Evidence to retain | Misleading shortcut |
|---|---|---|
| Task completion | Whether the intended task was completed appropriately | Counting any final answer as success |
| Action validity | Correct tool, inputs, identity, and clinical applicability | Counting syntactically valid calls |
| Safety | Inappropriate, unauthorized, or harmful actions | Ignoring intermediate actions when the answer is correct |
| Evidence use | Source support, timing, and contradictions | Treating a citation as verification |
| Recovery | Detection, correction, escalation, and stopping | Excluding tool failures from evaluation |
| Burden | Time, calls, review, and unnecessary work | Reporting only inference speed |
| Human interaction | What users saw and how they responded | Assuming review catches every error |

Trajectory distributions also matter. Different runs can take different paths, and rare branches can contain important failures. Real systems can also have variable path lengths. Substituting the average length into a fixed-length reliability formula is not generally valid: difficulty, stopping, and stage reliability can be related.

Simulations can expose these branches and provide controlled environments. Their tools, patients, and outcome rules remain approximations. Success in simulation does not establish clinical utility in a hospital.

### Revision checklist

| Question | Answer to retain |
|---|---|
| What is the main evaluation unit? | The trajectory, including actions, evidence, recovery, and termination. |
| Does the probability chain require independence? | No; it uses conditional stage probabilities. |
| When is the simple power expression justified? | When the required conditional reliabilities are equal, including the independent identical-stage case. |
| Do equal marginal stage accuracies determine completion reliability? | No; dependence changes the joint outcome. |
| What does the union bound provide? | A sufficient overall bound without independence. |
| Does any failed call imply task failure? | No; recovery and the definition of success matter. |
| Does correct final text certify safe actions? | No; intermediate actions can be inappropriate or harmful. |
| Is a valid schema clinically sufficient? | No; identity, semantics, timing, and applicability remain. |
| Why is step-level causal credit difficult? | Earlier choices, shared causes, and downstream adaptation interact. |
| Does simulation success establish clinical benefit? | No; real workflows and consequences need their own evidence. |

## Why it matters for my work

Tool use connects prediction to action. The clinical target therefore sets requirements for evidence provenance, permitted actions, and trajectory-level evaluation. Reliability of isolated components does not establish reliability or Clinical utility of the complete system.

## What I have not resolved

- Which intermediate failures are recoverable, and which make the trajectory unacceptable?
- What evidence is needed to verify execution rather than merely a successful-looking return value?
- Which clinical judgments remain unresolved even when every computational operation is correct?

---

Sources: Published tool-using language-model concepts, including Yao and colleagues on interleaving reasoning and acting; standard conditional probability and union-bound arguments; and established clinical workflow-evaluation principles. All reliability figures are calculated from explicitly constructed assumptions. These are study notes for research purposes, not clinical guidance.
