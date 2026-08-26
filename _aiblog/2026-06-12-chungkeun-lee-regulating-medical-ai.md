---
layout: post
title: "The Industry Cannot Outgrow Its Regulation: Chungkeun Lee on Governing Medical AI"
date: 2026-06-12 12:00:00 +0900
description: Notes from former MFDS reviewer Dr. Chungkeun Lee on how Korea moved early in medical-AI regulation, why model changes matter as much as initial accuracy, and how generative AI is pushing regulation from one-time approval toward continuous oversight.
related_posts: false
---

Regulation is often described as the final obstacle standing between an innovative medical-AI model and the patient.

This interview presents almost the opposite view.

Dr. Yoon Sup Choi opens the conversation with a phrase he often uses: the level of a country's medical industry ultimately converges toward the level of its regulation. An industry may complain about regulation or try to move faster than it, but it cannot permanently grow beyond the ceiling that regulation creates.

The previous posts on [VUNO's DeepCARS](/blog/2025-11-14-vuno-deepcars-beyond-auroc/) and [Chris McIntosh's bench-to-bedside research](/blog/2026-01-16-chris-mcintosh-medical-ai-bench-to-bedside/) examined what happens when a model meets clinical workflow, evidence generation, reimbursement, and real patient care. This post turns to another layer of the same problem: who defines the conditions under which that model may enter healthcare, change after approval, and remain trustworthy over time?

These are my notes from a two-part interview with Dr. Chungkeun Lee, formerly a medical-device reviewer at Korea's Ministry of Food and Drug Safety and now a research professor at the Medical Device Research and Development Center of Seoul National University Bundang Hospital. The first part focused on [how Korea became an early mover in digital-health regulation](https://www.youtube.com/watch?v=XYLCLmTlt6k), while the second examined [the regulatory problems created by generative medical AI](https://www.youtube.com/watch?v=ktiCjLEMq0k).

The conversation was recorded while Korea's generative-AI medical-device guidance was still being developed. The MFDS subsequently issued its final guidance in January 2025, describing it as the world's first dedicated approval and review guideline for generative-AI medical devices. In April 2026, it also authorized Korea's first generative-AI-based digital medical device. The interview should therefore be read both as an account of how the guidance was formed and as an explanation of the unresolved lifecycle problems that remain after the first products enter the market.

Any errors of interpretation are mine.

## Part 1 — A regulator with an engineering view of the problem

Lee entered regulation through biomedical engineering rather than through policy alone.

During his master's training, he worked on analog front-end circuits for measuring electrical signals from nerve bundles. His doctoral research moved to photoplethysmography, or PPG, the optical pulse-sensing technology now commonly found in devices such as the Apple Watch and Galaxy Watch. After completing postdoctoral research, he joined the MFDS and spent approximately ten years reviewing medical devices.

His early work covered cardiovascular and imaging equipment, including X-ray systems, ventilators, ventricular assist devices, and other life-support technologies. He later worked on advanced medical devices and eventually joined the division responsible for digital-health regulatory support, where he dealt with artificial-intelligence medical devices and digital therapeutics.

That career path matters because medical-AI regulation is not merely a legal question.

A regulator must understand what a system measures, how its software is trained, which components may change, where failure can enter, how clinicians will use the output, and what evidence can reasonably demonstrate safety and effectiveness. In that sense, regulation is another form of system engineering — one conducted under uncertainty and with patient safety as its constraint.

Lee's current position at a hospital-based medical-device research center places him on the other side of the same boundary. Instead of reviewing products only when they reach the regulator, he now works closer to the point at which technologies are developed, clinically evaluated, and prepared for market entry.

The two roles reveal the same underlying problem from different directions: a promising technology needs a path into medicine, but that path must make its risks inspectable.

## Part 2 — Korea moved early because industry and regulation moved together

Korea was unusually early in producing guidance for emerging categories such as medical AI, virtual reality, three-dimensional printing, and digital therapeutics.

Lee does not describe this as a case of regulators predicting the future in isolation. The industry played an equally important role.

When a new technological wave reaches medicine, the people riding it often come from outside the traditional medical-device sector. They may understand machine learning, software, gaming technology, or data platforms, but have little experience with medical-device classification, quality systems, clinical validation, or approval procedures.

Their technologies do not fit comfortably within categories designed for conventional hardware.

A regulator can respond in two ways. It can wait until the technology becomes mature enough to resemble an existing product, or it can begin defining a pathway while the category is still taking shape. According to Lee, the MFDS increasingly chose the second approach.

The agency did not create its early guidance through imagination alone. It looked for products that were already approaching a usable form and examined them from multiple regulatory perspectives. Expert committees brought together medical-AI companies, hospital clinicians, academic researchers, and reviewers. Companies such as Lunit and VUNO participated at a time when even the terminology surrounding medical AI was not yet settled.

The resulting process was iterative.

Companies brought concrete questions and near-market products. Regulators identified safety and performance issues that existing rules did not address. Clinicians clarified how the systems would be used. The answers became guidance, and the guidance lowered uncertainty for the next group of developers.

This produced a positive feedback loop:

1. a new technology approached the healthcare market;
2. developers engaged the regulator rather than avoiding it;
3. the regulator learned from actual products;
4. guidance made the route to approval more predictable;
5. more companies could enter with a clearer understanding of the evidence required.

Lee joked that the MFDS had experienced the unusual reward of being praised. Regulatory agencies are more often criticized for delaying products than thanked for enabling them. The favorable response to the early AI guidance reinforced the agency's willingness to continue moving proactively.

Korea also carried this experience into international discussions. The MFDS shared English versions of its guidance at meetings of the International Medical Device Regulators Forum, which brings together major regulatory authorities to promote international convergence.

Lee recalled showing Korea's AI guidance to then-FDA Center for Devices and Radiological Health Director Jeff Shuren. Shuren's immediate question was whether it was guidance for machine learning in general or specifically for deep learning.

The anecdote captures how early the field still was. Regulators were not merely debating evaluation thresholds. They were still deciding which technological distinctions mattered enough to appear in a regulatory document.

Korea's advantage was therefore not that it had discovered a perfect regulatory answer. It was that it began turning technical ambiguity into a shared language earlier than many other jurisdictions.

## Part 3 — The central AI-regulation problem is change

The most difficult issue in early medical-AI regulation was not simply how to measure the first model's accuracy.

It was how to manage what happened afterward.

A conventional medical device is generally expected to retain the characteristics for which it was approved. Its performance specifications are defined, its components are controlled, and a significant modification may require another regulatory review.

An AI model is different because its behavior depends on data.

The data used for training cannot represent every patient, scanner, institution, protocol, demographic group, or future clinical environment. A model may perform well at the development hospital and deteriorate after transfer. It may be retrained using new data and improve overall while losing a capability that it previously possessed. Even when the software itself is unchanged, the distribution of the data entering it can change over time.

The relevant object of regulation is therefore not only a frozen model. It is also the process through which the model is transferred, monitored, modified, and revalidated.

Lee described an early Korean approach that replaced the expectation of one exact, permanently fixed performance value with a minimum acceptable performance boundary. Certain limited changes could be managed within the manufacturer's quality-management system, provided that the model remained within the approved range. If performance fell below the specified threshold or the change exceeded the permitted scope, a formal change review would be required.

This gave manufacturers some room to maintain an AI product without treating every small adjustment as an entirely new device.

The autonomy was also proportional to risk. Many early medical-AI products did not directly deliver treatment or operate without supervision. They produced information that a trained healthcare professional would interpret. That clinical oversight made it possible to consider a more flexible change-management approach than would be appropriate for a high-risk autonomous device.

The US concept of a Predetermined Change Control Plan, or PCCP, addresses a related problem.

A PCCP does not mean that a company may change an approved model in any way it wishes. It asks the developer to specify in advance:

* what kinds of changes are expected;
* why those changes may become necessary;
* how the modified model will be developed;
* what evidence will be used to validate it;
* and which performance limits must continue to be satisfied.

The Korean quality-system approach described by Lee and the FDA's PCCP framework are not identical. They nevertheless reflect the same regulatory insight: change should not be treated as an unexpected exception when change is an inherent property of the technology.

A sophisticated regulatory system does not merely approve a model. It defines the conditions under which that model may change without becoming a different and untraceable clinical product.

## Part 4 — Generative AI makes the boundary of the device unclear

Generative AI intensifies nearly every one of these difficulties.

A conventional medical-AI developer often builds and controls the model embedded in its product. A generative-AI application may instead depend on a foundation model supplied by another company. The application developer may add prompts, retrieval, fine-tuning, safety filters, or a user interface without controlling the underlying model.

The foundation-model provider may then update that model.

A newer version may perform better on average, but there is no guarantee of backward compatibility. A capability that previously worked well may deteriorate. The downstream medical application may therefore change even when its own developer has not deliberately modified its code.

This immediately raises a scope problem.

What exactly is the regulated medical device?

Is it the foundation model? The fine-tuned model? The prompt template? The retrieval database? The safety layer? The user interface? The complete system? If the foundation model is supplied by an external company, how much control and documentation should the medical-device manufacturer be required to maintain over it?

The problem becomes more difficult because generative models are broadly capable.

Medical-device regulation ordinarily begins with an intended use. A product is evaluated for a defined purpose, population, user, input, and clinical setting. A general-purpose language model, however, can respond to an enormous range of prompts and produce many different forms of output.

Testing everything that it could possibly say is not feasible.

Lee therefore expects the practical scope of regulated generative-AI medical devices to be considerably narrower than the apparent scope of the underlying technology. A general-purpose model may be capable of answering almost any medical question, but a regulated product will likely need to limit that capability to a specific clinical task.

A system that summarizes a record, explains medical terminology to a patient, drafts a report, proposes a differential diagnosis, recommends treatment, or conducts a psychiatric conversation may use similar underlying technology. Whether each function becomes a medical device depends on its intended purpose, claims, clinical risk, and role in decision-making.

The model's open-ended capability is not itself the intended use. The regulated use must still be bounded.

Generative AI also introduces risks that cannot be reduced to hallucination or dataset bias alone.

A fluent response may cause users to trust the system more than its actual accuracy warrants. A clinician may give insufficient attention to a case because reviewing the model's long output creates additional workload. A novice and an experienced specialist may use the same recommendation differently. The system may behave differently across languages, cultural settings, prompt styles, or documentation conventions.

Safety therefore depends partly on the user's relationship with the model.

The product is not only generating information. It is shaping attention, confidence, workload, and clinical behavior.

## Part 5 — Approval is becoming a site-specific lifecycle problem

In the FDA discussions described in the interview, three broad questions organized the debate around generative-AI medical devices:

1. What evidence should be submitted before authorization?
2. How should the risks be identified and controlled?
3. How should the product be monitored after deployment?

The third question is becoming increasingly difficult to separate from the first two.

One idea that repeatedly appeared was site-specific evaluation.

A model may satisfy a minimum performance standard during centralized testing but behave differently after deployment at a particular hospital. The local patient population may differ. Prompts may be written differently. Clinicians may use the output in another workflow. Documentation may follow different conventions. The model may operate in another language or cultural context.

The same foundation model can therefore become a meaningfully different clinical system at each site.

This is related to the familiar problem of external validation, but generative AI adds another layer. The relevant distribution includes not only patient data but also prompts, users, workflows, local retrieval sources, software integrations, and institutional policies.

A model's context is partly created by the people and organization using it.

Continuous monitoring is an obvious response, but it introduces an unresolved governance question: who is capable of doing it?

The manufacturer cannot directly supervise every local implementation in every hospital. Hospitals may not have the personnel, infrastructure, reference labels, or regulatory expertise needed to evaluate a changing model continuously. A system can therefore fall into a gap in which everyone agrees that ongoing monitoring is necessary, but no participant can perform the full task alone.

This is why the total product lifecycle, or TPLC, has become central to AI regulation.

A meaningful lifecycle approach would need more than a general instruction to "monitor performance." It would require operational answers to questions such as:

* Which model version is currently active at each hospital?
* How is local baseline performance established?
* Which signals indicate data or performance drift?
* How are failures and near misses reported?
* What triggers retraining or recalibration?
* How is an updated model tested before replacement?
* Can a hospital roll back to an earlier version?
* Which changes require regulatory notification or review?
* Who is accountable when the foundation-model provider changes the system?

At the time of the interview, Korea's draft guidance was primarily concerned with the evidence required for approval and review. The FDA discussion covered a broader lifecycle because it was still asking what the regulator's role should be across development, deployment, and post-market use.

These approaches reflect differences in institutional scope as much as differences in philosophy. A premarket-review division cannot by itself define every post-market responsibility held by other regulatory units, hospitals, developers, and health systems.

The larger direction, however, is shared.

Medical-AI authorization can no longer be understood as one strong evaluation conducted at one moment. Approval is becoming the entry point into a continuing process of performance maintenance.

## Part 6 — The choice is not simply locked or continuously learning

Regulators have historically preferred locked algorithms because they are easier to identify and evaluate.

The model reviewed before authorization is the same model delivered to the hospital. Its behavior may still vary across data, but its parameters do not silently change. When a failure occurs, investigators can at least determine which version produced the output.

Continuous learning promises a different advantage.

A model could incorporate new clinical experience, respond to a changing population, and remain current instead of gradually becoming obsolete. Hospitals and developers naturally want a successful system to improve using the data and feedback generated after deployment.

But an unrestricted continuously learning model creates a traceability problem.

If the system changes every day, what exactly has been approved? When did a new failure mode enter? Which patients were affected? Can the previous model be reconstructed? Was the new behavior caused by a data shift, a training decision, a foundation-model update, or interaction with a local workflow?

At the time of the discussion, Lee emphasized that the regulatory-science methodology needed to manage fully continuous learning had not yet matured.

The realistic path is therefore unlikely to be a simple choice between a permanently frozen model and a model allowed to rewrite itself freely.

A more plausible system would use controlled, periodic, and auditable learning:

* new data are collected under predefined rules;
* candidate updates are developed separately from the deployed model;
* performance is tested in shadow mode;
* regressions are examined across tasks, sites, and subgroups;
* updates are released only after specified criteria are met;
* every version remains identifiable and reversible.

Learning may continue, but not invisibly.

The central requirement is not that a medical model must never change. It is that every clinically meaningful change must have an identity, a rationale, and evidence.

Since the interview, Korea's final generative-AI guidance and its first authorization of a generative-AI-based digital medical device have moved this debate from a hypothetical problem toward an operational one. The first approvals do not resolve the lifecycle question. They make resolving it more urgent.

## Part 7 — Should generative AI be governed more like a professional?

The interview ends with a more radical regulatory idea.

Bakul Patel, who previously led digital-health regulation at the FDA and later joined Google, has argued with David Blumenthal that clinical generative AI may eventually need to be treated not simply as another medical device, but as a novel form of intelligence.

The proposal uses the oversight of human clinicians as an analogy.

A physician is not approved once and then assumed to remain permanently competent. Physicians undergo education, supervised training, examinations, certification, continuing professional development, and ongoing oversight. They are fallible, their performance can change, and their work is shaped by experience, fatigue, environment, and supervision.

Generative AI shares some of those characteristics.

It can perform multiple tasks, respond differently across contexts, change over time, make errors, and exhibit behavior that cannot be completely predicted from a single premarket test. Trying to enumerate and authorize every possible output may eventually become less realistic than evaluating its continuing competence within a defined scope.

This should not be interpreted literally as declaring an AI system to be a physician.

The analogy instead shifts the regulatory question.

Rather than asking only whether one software version satisfies one specification, an oversight system might ask whether the AI has demonstrated competence for a defined role, completed supervised evaluation in actual clinical environments, remains within that role, and continues to meet performance requirements over time.

Lee sees a relevant insight in this proposal because AI performance cannot be separated from the person using it.

Studies of medical-AI systems often show different outcomes when the same tool is used by experienced clinicians and less experienced users. An expert may recognize when a recommendation is implausible, while a novice may accept it. One user may treat the model as a source of evidence, while another treats it as an answer.

Digital literacy, user training, interface design, and usability are therefore safety variables.

The effective clinical unit is not the AI alone. It is the AI, its user, the local institution, and the rules governing their interaction.

A professional-style oversight model would still leave difficult questions. Who defines the AI's permitted scope? Who supervises it? How often must it be reassessed? Who is responsible when a model and clinician jointly produce an error? Which organization has authority to suspend its use?

Yet the proposal captures a limitation of conventional device regulation.

The more AI behaves like a broad, changing, and interactive source of clinical judgment, the less sufficient it becomes to regulate only a static package of software.

## A researcher's takeaway

This interview changes the way trustworthy medical AI should be framed.

Trust is often treated as a property of the model at the end of training. We evaluate accuracy, calibration, robustness, subgroup performance, interpretability, or clinical alignment and then describe the resulting system as trustworthy or untrustworthy.

Regulation forces a more difficult question: trustworthy when, where, in which version, and under whose use?

Four principles stand out.

1. **A model is not stable merely because its code is locked.**
   The patient population, scanner, protocol, language, workflow, and user behavior can all change around it.

2. **A model update is not necessarily a monotonic improvement.**
   Better average performance can conceal regression in an earlier capability, subgroup, institution, or clinical context.

3. **Change control is part of model performance.**
   A clinically strong model with an untraceable update process is not a well-controlled medical system.

4. **Human interaction is part of safety.**
   Overreliance, workload, user expertise, and institutional response can determine whether the same output helps or harms.

These principles also expand the meaning of clinical evidence auditing.

It is not enough to ask whether the initial model relied on clinically meaningful evidence. We also need to ask whether that evidence remains stable after transfer, recalibration, retraining, or a foundation-model update. An audit should identify not only what evidence the model uses, but whether the healthcare system can detect when that evidence changes.

This suggests that trustworthy medical-AI evaluation should become lifecycle-aware.

The relevant unit is not simply a checkpoint. It is a checkpoint with a version history, deployment environment, update policy, monitoring process, user population, and rollback mechanism.

Korea's early regulatory advantage did not come from removing regulation. It came from treating regulation as something that could be developed alongside the technology rather than years after it.

That may be the most durable lesson from Lee's account.

The goal is not to approve medical AI as quickly as possible. It is to create a system in which useful models are allowed to enter care, adapt to reality, and improve — without ever becoming impossible to identify, evaluate, or hold accountable.

Medical AI should be allowed to learn, but never invisibly.
