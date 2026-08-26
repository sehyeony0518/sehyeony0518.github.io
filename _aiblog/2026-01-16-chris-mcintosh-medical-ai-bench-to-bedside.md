---
layout: post
title: "The Paper Is 10% of the Work: Chris McIntosh on Taking Medical AI from Bench to Bedside"
date: 2026-01-16 12:00:00 +0900
description: Notes from an interview with Prof. Chris McIntosh on clinical collaboration, radiotherapy deployment, transfer learning, explainability, fairness, wearables, and the long path from a paper to patient care.
featured: true
pinned: true
tag: "McIntosh Lab"
related_posts: false
---

Most discussions of medical AI begin with the model: the architecture, the training data, and the benchmark score. This conversation begins somewhere else — with the clinical problem, the people who will use the system, and the years of work required after a technically successful paper.

This post is based on the [EMJ Podcast episode *AI at the Heart of Medicine*](https://www.emjreviews.com/radiology/podcasts/ai-at-the-heart-of-medicine/), featuring Prof. Chris McIntosh of the University of Toronto and University Health Network. His lab works on artificial intelligence in medicine with an explicit bench-to-bedside orientation. The interview covered his entry into medical AI, clinical collaboration, radiation therapy, transfer learning, explainability, fairness, wearable monitoring, and the future relationship between physicians and AI.

I have focused on the ideas that seem most useful for understanding how medical AI becomes clinical technology. Any errors of interpretation are mine.

## Part 1 — Begin with the clinical problem, not the method

McIntosh originally entered computer science intending to develop video games. As he learned more about that industry, however, he became less convinced that it was where he wanted to direct his career. An undergraduate research internship introduced him to machine learning in healthcare and showed him that his interests in computing and medicine did not have to remain separate.

That origin is reflected in how he describes his lab today. The method is not the starting point. The problem is.

Every student in the lab works closely with at least one clinical collaborator. The purpose is not merely to obtain medical data, confirm labels, or ask a physician to review the final model. It is to understand the workflow from the inside: where care is delayed, what information clinicians lack, which decisions are difficult, and what would actually change if an AI system produced a prediction.

Without that collaboration, it is easy for researchers to build a technically sophisticated tool and then search for somewhere to use it. McIntosh argues for the reverse process. Researchers should first understand the clinical need and then ask what combination of machine learning, imaging, sensing, and software could realistically address it.

This changes the questions asked at the beginning of a project. Who will see the model's output? At what point in the workflow? What action becomes possible because of it? What happens when the model is wrong? How much additional work does it create for the clinical team?

A model can be highly accurate while answering a question that nobody in the hospital urgently needs answered. Clinical collaboration is therefore not an auxiliary step in medical AI. It determines whether the research problem itself is valid.

## Part 2 — A paper is not a deployment

McIntosh's clearest example of bench-to-bedside research comes from radiation therapy.

Radiation treatment planning requires clinicians to determine where radiation should be delivered, how much should reach the tumour, and how surrounding healthy organs should be protected. Both the time required to create a plan and the quality of that plan can affect patient care. Once radiation has been delivered, it cannot simply be taken back, so quality assurance is inseparable from automation.

McIntosh and his collaborators began developing machine-learning methods that could use patient imaging to generate radiation treatment plans. But producing a promising retrospective result was only the beginning. The work moved through theoretical development, retrospective testing, safety evaluation, workflow integration, prospective clinical deployment, regulatory processes, licensing, and eventual use in patient care.

Their [prospective prostate-cancer radiotherapy study](https://www.nature.com/articles/s41591-021-01359-w) illustrates why those stages matter. The system was evaluated not only in simulation but inside the real clinical workflow, where physicians reviewed machine- and human-generated plans and selected the plan that would actually be delivered. The study showed that performance measured in a retrospective setting did not perfectly predict acceptance when real patient care was at stake.

In the interview, McIntosh noted that early versions of the technology were developed around 2013 and 2014, while the first patient was treated in 2019. That gap of roughly five or six years is not evidence that the research failed to move quickly. It is evidence of how much work clinical translation requires.

His blunt estimate was that the paper may represent only 10% of the work, while the remaining 90% lies in deployment.

That remaining work includes software integration, data interfaces, quality assurance, regulatory evidence, edge-case handling, clinician training, prospective validation, maintenance, accountability, and the study of how people behave when an algorithm's output affects an actual patient. None of these tasks is visible in a leaderboard result, but any one of them can determine whether a model reaches clinical care.

The statement does not diminish the importance of papers. A paper isolates and tests a scientific claim. But patient care depends on the entire system surrounding that claim.

## Part 3 — Learning when medical data are limited

A recurring obstacle in medical AI is the mismatch between the amount of data modern deep learning often expects and the amount of data available for a particular clinical problem.

A clinician may approach the lab with several hundred patients from a rare disease or a specialized procedure. Training a large model entirely from scratch would be similar, in McIntosh's analogy, to asking someone with no prior education to immediately learn a medical specialty.

Transfer learning changes that process. A model first acquires broad knowledge from a larger and more general dataset, then progressively specializes toward a narrower medical domain and finally toward the particular clinical task. It resembles moving from general education to medical training and then to a specialty, rather than beginning again from infancy for every new problem.

The practical value is not merely computational efficiency. Transfer learning makes it possible to study conditions for which tens of thousands of labeled examples may never exist. It expands the range of diseases and clinical settings that can realistically benefit from AI.

McIntosh also identified meta-learning as part of his lab's methodology, although the interview's detailed explanation focused mainly on transfer learning. Both reflect the same broader concern: medical AI must learn efficiently across related tasks because healthcare data are fragmented across diseases, institutions, modalities, and patient populations.

There is, however, an important trustworthiness question beneath this efficiency. A transferred representation can carry useful general knowledge, but it can also carry biases, shortcuts, and assumptions inherited from its original data. Learning from less task-specific data does not automatically mean learning the clinically correct evidence.

Transfer learning helps answer whether a useful model can be built with limited data. It does not by itself answer whether the resulting model will generalize safely or rely on the right reasons.

## Part 4 — Explainability, safety, bias, and fairness are different questions

McIntosh takes a deliberately careful position on explainable AI: explainability and safety should not be treated as synonyms.

An AI system does not necessarily have to provide a complete human-readable account of its internal reasoning in order to be safe. Humans themselves cannot always explain how they arrived at a complex judgment, and medical experts often show both inter-observer and intra-observer variability. A model may still be validated for a clearly defined clinical use even when its internal mechanism is not fully interpretable.

At the same time, this is not an argument against explainability.

McIntosh sees its strongest value in human–computer interaction. A model that returns only a binary answer leaves little room for a clinician to examine, question, or contextualize its output. A system that reveals relevant evidence, uncertainty, or contributing factors can support a more meaningful division of labour.

The machine can process large quantities of data, identify patterns across long records, and maintain consistency. The clinician contributes contextual knowledge, communication, ethical judgment, compassion, and an understanding of the individual patient. Explainability can help those capabilities work together.

The distinction is important. An explanation can make a system easier to interrogate without proving that it is safe. Conversely, strong prospective validation can support a safety claim without making every internal computation understandable. Explanation, validation, calibration, monitoring, and workflow design each answer different questions.

McIntosh makes a similar distinction between bias and fairness. Fairness concerns whether performance and benefit are distributed equitably across patient groups. Bias refers more broadly to systematic influences in the model or data that may change performance, whether visibly or invisibly.

Many of those biases enter before training begins.

He referred to examples from experimental science in which seemingly irrelevant factors — even differences in who handled different groups of laboratory animals — produced confounding effects. Medical datasets contain analogous pathways. Different patient groups may be examined in different departments, on different scanners, with different protocols, or after different referral decisions. A model may learn those acquisition patterns instead of the underlying disease.

His lab's work on [shortcut learning and data-acquisition bias](https://www.nature.com/articles/s41746-024-01118-4) formalizes this problem: models can achieve high internal accuracy by exploiting signals tied to how and where data were collected, only to lose performance when transferred to another institution.

The practical lesson is that fairness cannot be added after training with a single metric. It begins with study design, data collection, subgroup representation, acquisition pathways, labels, and the choice of objective function.

Balanced group counts are important, but they are not sufficient. Two groups can be numerically balanced while differing systematically in disease severity, equipment, missingness, access to care, or labeling quality. Good intentions do not make a dataset neutral. Those assumptions must be examined empirically.

## Part 5 — From clinical snapshots to patient trajectories

McIntosh sees wearable technology as one of the most promising directions in cardiovascular care because it changes the temporal scale of medicine.

Traditional care is often based on snapshots. A clinician sees a chest X-ray, echocardiogram, ECG, laboratory result, or brief clinic visit and may then be asked to estimate what will happen months or years later. Even when each snapshot is accurate, large parts of the patient's life remain invisible.

Wearables offer a longitudinal view. They can provide information about activity, sleep, functional capacity, recovery, and how a patient's condition changes from day to day outside the hospital.

The problem is that continuous monitoring produces far more data than clinicians could review manually. This is where AI becomes essential: not simply to collect more information, but to compress it into a clinically meaningful signal.

McIntosh described a collaboration involving Apple Watch data and patients with heart failure. The goal was to estimate peak oxygen uptake — ordinarily measured through a resource-intensive cardiopulmonary exercise test — from everyday biometric data. At the time of the interview, enrollment had been completed and analysis was underway.

The larger idea extends beyond one measurement. Instead of asking a model to make a long-term prediction from a brief hospital encounter, longitudinal AI could identify a patient's baseline, detect meaningful decline, and alert the care team when intervention may be needed.

But more data do not automatically create better care. A wearable-derived signal must still be reliable, clinically interpretable, connected to an actionable response, and integrated without overwhelming either patients or clinicians. Continuous prediction without a clear care pathway could simply create continuous alarm.

The future McIntosh describes is therefore collaborative rather than autonomous. AI should not remove physicians from care. It should reduce repetitive work, extend specialist knowledge, and give clinicians more time to interact with patients.

The desired endpoint is not a consultation in which the patient speaks only to a screen. It is a clinical encounter in which the technology handles what machines do well and gives human professionals more room to practice the parts of medicine that require humanity.

## A researcher's takeaway

The most useful idea in the interview is that bench-to-bedside translation is not the final stage of a medical-AI project. It is an organizing principle that should shape the project from the first question.

A model intended for deployment should not be designed first and contextualized later. Its intended user, decision point, failure cost, data pathway, and intervention must influence the dataset, target, architecture, validation plan, and reported endpoint from the beginning.

The interview also clarifies why model-level trust and system-level benefit must be evaluated separately.

A model may use clinically meaningful and generalizable evidence yet fail because it does not fit the workflow, produces information too late, or creates more work than the clinical team can absorb. Conversely, a deployed system may appear to improve efficiency while still relying on fragile shortcuts that could fail at another hospital or in an underrepresented group.

Prospective clinical evaluation and model auditing are therefore complements, not substitutes. One asks whether the system improves care in a particular clinical environment. The other asks what the model has learned, whether its evidence is stable, and whether the same reasoning is likely to survive a change in setting.

The same distinction applies to explainability. Showing where a model looked does not prove that its decision was clinically faithful. But refusing to investigate the model because a black box can sometimes be validated safely would also leave important failure modes undiscovered.

"The paper is 10% of the work" is ultimately a correction to how success is measured. In academic machine learning, the model is often treated as the finished product. In medicine, the relevant unit is closer to a model embedded in a care pathway: connected to real data, interpreted by real people, followed by a possible action, and evaluated against patient outcomes.

Medical AI earns trust not merely when it can produce an accurate answer, but when that answer can be examined, acted upon, and shown to remain useful where patient care actually happens.
