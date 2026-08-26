---
layout: post
title: "From Lab to Lives: Chris McIntosh on Making Medical AI Part of Routine Care"
date: 2026-02-20 12:00:00 +0900
description: Notes from Prof. Chris McIntosh's lecture on automated radiotherapy planning, treatment-specific patient matching, prospective deployment, and the gap between an AI plan being clinically acceptable and clinicians actually using it.
tag: "McIntosh Lab"
related_posts: false
---

This post summarizes a Toronto Machine Learning Series lecture by Prof. Chris McIntosh titled *An ML System for Radiotherapy Cancer Care — From Lab to Lives*. It is a particularly valuable case study because the work did not stop at retrospective validation. The system moved through blinded clinical comparison, prospective deployment, regulatory approval, commercialization, and direct use in patient care.

McIntosh is now a Senior Scientist at University Health Network's Peter Munk Cardiac Centre Research Institute and an Associate Professor in the University of Toronto's Department of Medical Biophysics, with additional appointments in Computer Science and Medical Imaging. His lab describes its central objective as advancing medical AI "from bench to bedside," and its official profile states that the radiotherapy technology discussed here is now used in patient care internationally. ([Medical Biophysics][1])

What makes the lecture memorable is not simply that the model performed well. It is that McIntosh followed the model far enough to observe what happens after technical performance is no longer the only variable.

## Part 1 — Radiotherapy planning is not a single prediction task

Radiotherapy seeks to deliver a high dose of radiation to a tumor while minimizing exposure to surrounding healthy tissue.

For a relatively simple case, a radiation beam may approach the tumor from an angle that avoids a nearby organ. Prostate cancer planning is considerably more complex. The beam rotates around the patient, while many small components inside the linear accelerator continuously shape it. The final treatment must cover the target while sparing organs at risk such as the bladder and rectum.

A clinician therefore does not merely choose a label or mark a lesion. The clinical team must construct a three-dimensional dose distribution that satisfies several competing objectives and can actually be delivered by the treatment machine.

The conventional process is iterative. Clinicians inspect the target coverage and organ doses, add or modify optimization objectives, generate another plan, and repeat the process until an acceptable balance is reached. The work may require hours of active planning and considerably more elapsed time once clinical queues and handoffs are included. It also depends heavily on experience.

This turns variation in expertise into a patient-care problem. Two patients with similar disease may receive different-quality plans because they entered different clinical environments or were treated by teams with different levels of experience.

McIntosh's central idea was therefore not merely to automate a manual optimization procedure. It was to make high-quality institutional experience reproducible.

Imagine a database containing treatments from highly experienced cancer centers. For each new patient, the system could identify the historical patients who are most relevant from a treatment perspective, learn from the plans that worked well for them, and transfer that knowledge into a personalized plan.

The goal is not to reproduce the average plan. It is to make the best available experience accessible for every patient.

## Part 2 — Similarity should be defined by the treatment, not appearance alone

The first challenge is representing a patient in a way that is relevant to radiation dose.

The system combines information from the CT image with the geometry of delineated structures. Image features indicate boundaries, tissue characteristics, and anatomical position, while distance-based features describe where each voxel lies relative to the tumor and surrounding organs.

Each previously treated patient then becomes an **atlas**.

An atlas regression forest learns how that particular patient's image and anatomical features relate to the dose that was delivered. It can therefore estimate, voxel by voxel, the probability that a similar anatomical location should receive a particular amount of radiation.

But having a collection of atlases is not enough. The system must determine which historical patients are useful for planning a new one.

To learn this, the researchers applied each atlas to the other patients in the training database and evaluated the quality of the resulting plans. A second machine-learning model then learned which feature relationships predicted whether a given atlas would work well for a given patient.

This produces a **treatment-specific similarity metric** rather than a generic image-similarity measure. Two CT images can look globally similar while differing in the anatomical relationships that determine whether an organ can be spared. Conversely, visually different patients may still support similar treatment strategies.

The relationship can also be asymmetric.

Suppose patient C has an additional organ near the treatment field and the atlas learned from C knows how to protect it. That atlas may still produce a good plan for patient A, who does not present the same constraint. An atlas learned from A, however, may fail on C because it has never learned how to handle that organ.

Patient C can therefore be useful for planning A even when A is not equally useful for planning C. This is an important distinction from the usual assumption that similarity must be symmetric.

For a new patient, the system selects the most relevant atlases, combines their probabilistic dose estimates, and determines the most likely spatial dose distribution. A conditional random field helps enforce spatial consistency, after which dose mimicking converts the prediction into a treatment plan that the physical machine can deliver. The published method thus connects patient-specific retrieval, voxel-level dose prediction, spatial optimization, and physical deliverability in one pipeline. ([arXiv][2])

Another useful property emerges from this design. A poorly planned historical case tends to perform badly when applied to other patients and consequently receives a low atlas-selection score. The system is therefore biased toward the more transferable plans in the database rather than blindly reproducing every historical decision.

In effect, it learns not only from prior experience, but also **which experience deserves to be trusted**.

## Part 3 — Clinical AI needs an evidence ladder

The project progressed through several levels of evaluation.

The early stage used conventional technical metrics across more than 500 retrospective cases and nine treatment sites. The researchers asked whether predicted and clinical dose distributions were sufficiently similar and estimated how many training patients were needed for each model.

They then moved to clinical dose criteria. Rather than judging only voxel-wise agreement, they compared target coverage and the protection of individual organs. Some criteria favored the automated plan, others favored the human plan, and some involved clinically meaningful trade-offs that could not be resolved without considering the patient's wider condition.

The next stage introduced blinded expert review. In an early set of 17 retrospective prostate cases, the automated plan was judged better in 12 cases, equivalent in three, and worse in two.

The decisive step, however, was prospective deployment.

The final clinical study compared machine-learning and human-generated plans in two phases: a retrospective simulation phase with 50 patients and a prospective clinical deployment phase with another 50. Physicians reviewed the two plans blindly using predefined criteria. In the deployment phase, the selected plan proceeded through the hospital's normal peer-review and quality-assurance process and was then used to treat the patient. ([PubMed][3])

Across both phases, 89% of machine-generated plans were considered clinically acceptable, and 72% were selected over the human-generated alternative. The median duration of the overall planning process fell from 118 hours to 47 hours, a reduction of 60.1%. ([PubMed][3])

These results alone would make the study noteworthy. Yet its most revealing result was the difference between simulation and deployment.

Clinical acceptability remained relatively stable: 92% in simulation and 86% during deployment. The proportion of machine-learning plans actually selected, however, fell from 83% to 61%. ([PubMed][3])

The model had not suddenly become much worse. The context in which people judged it had changed.

## Part 4 — The deployment gap was partly a human-behavior gap

In the simulated phase, clinicians could compare the plans without direct consequences for a patient. During prospective deployment, their decision determined which plan would actually be delivered.

That additional responsibility changed their behavior.

McIntosh's team investigated several possible explanations. Quantitative comparisons suggested that the relative quality of the automated plans remained similar across the two phases. The clinicians' ability to distinguish automated from manual plans also remained broadly stable.

What changed was their willingness to select a plan they believed had been generated by machine learning.

In some cases, physicians selected the machine-generated plan while believing it was the human-generated one. The output itself was acceptable; the perceived identity of its author affected the level of confidence placed in it.

This should not be reduced to a simple story of irrational resistance. Greater caution when a patient will actually receive the treatment is an understandable part of clinical responsibility. Some degree of skepticism is necessary for safety.

But it reveals a limitation in the usual evaluation pipeline.

A model can perform well on a held-out dataset, satisfy clinical criteria, and even win a blinded retrospective comparison, yet still behave differently as part of a live care system. The difference may arise not from a change in the image distribution but from a change in the **decision environment**.

The same model is now embedded within accountability, professional norms, uncertainty, workflow constraints, and potential harm.

I think of this as a form of socio-technical distribution shift. The input pixels may not have changed dramatically, but the surrounding system has. A retrospective experiment cannot fully reproduce how clinicians behave when their decision becomes irreversible and personally consequential.

The study therefore measured at least three distinct things:

1. whether the model could generate a clinically acceptable plan;
2. whether its plan compared favorably with the existing standard;
3. whether clinicians were willing to act on it in real practice.

These are related, but they are not interchangeable.

## Part 5 — Workflow improvement is more than reducing computation time

The reported time saving also carries an important operational lesson.

A manual plan may require only a few hours of active work, but the appropriate staff member may not be available immediately. Contours may be completed in the morning while planning begins late in the afternoon or on the following day. A case can move repeatedly between members of the clinical team.

The AI system becomes available as soon as the required imaging and contours are ready. Its contribution is therefore not simply the replacement of several hours of human computation. It removes waiting time and coordination delays from the full clinical pathway.

Following the deployment, McIntosh explained that machine-learning planning became the default prostate-cancer workflow at Princess Margaret Cancer Centre: an automated plan was generated first, and a manual alternative was requested when the physician did not accept it.

That is more significant than adding an AI button to an existing interface.

The workflow itself was inverted. Instead of asking whether AI should occasionally assist a manual process, the clinical team began with the automated plan and reserved scarce human planning effort for exceptions.

The technology was also licensed to RaySearch Laboratories and integrated into RayStation. RaySearch describes the collaboration with Princess Margaret as producing the world's first machine-learning treatment-plan generation module and reports that its platform can now generate personalized plans in minutes. Its 2026 release continues to expand machine-learning planning across additional treatment settings. ([RaySearch Laboratories][4])

## Part 6 — The frozen-model paradox

A question from the audience exposed another difficulty that appears only after successful deployment: why not retrain the model using the new, high-quality plans produced during the clinical study?

Conceptually, that would be the natural next step. Deployment produces new cases, clinicians identify which plans they prefer, and this feedback could be used to build a better model.

McIntosh explained that the approved system could not simply be updated in that manner. The regulatory authorization applied to a particular trained model. Adding another patient and retraining it would produce a new model that required another regulatory process.

The exact regulatory pathways continue to evolve, but the underlying lifecycle problem remains important.

A deployed medical model generates the very evidence that could improve it, while safety regulation appropriately discourages uncontrolled changes to an approved system. Medical AI therefore needs more than a training pipeline. It needs version control, change documentation, monitoring, predefined update policies, and efficient pathways for revalidation.

The challenge is not merely building a model that learns. It is building a system in which learning can continue without making clinical behavior untraceable.

## A researcher's takeaway

The number that stayed with me was not only the 89% clinical acceptability rate. It was the fall in selection from 83% during simulation to 61% during live deployment.

That gap contains much of what medical AI research tends to leave out.

A radiotherapy model can be assessed at the voxel level, at the level of target coverage and organ sparing, at the level of physical deliverability, in blinded physician comparison, in prospective workflow, and eventually through patient outcomes. Success at one level does not guarantee success at the next.

The design also raises valuable questions for trustworthy AI. Which historical atlases most strongly influence a particular plan? Are they selected because of clinically relevant anatomical relationships? What happens when a new patient is unlike all available atlases? Can the system recognize that no reliable precedent exists? Does its evidence remain valid after transfer to another institution, scanner, protocol, or patient population?

These questions are closely related to why I am interested in clinical evidence auditing. A high-quality output is necessary, but it is not sufficient. We also need to know whether the model arrived there through evidence that remains meaningful across patients and environments — and whether the surrounding workflow can recognize when that evidence is no longer trustworthy.

McIntosh's work shows what "bench to bedside" actually requires. It is not a single leap from a paper to a hospital. It is a sequence of increasingly difficult tests: technical accuracy, clinical validity, physical feasibility, human acceptance, workflow integration, regulatory maintenance, and real patient care.

Medical AI earns the right to become routine care only after it remains credible beyond the benchmark.

[1]: https://medbio.utoronto.ca/faculty/mcintosh "Chris McIntosh | Medical Biophysics"
[2]: https://arxiv.org/abs/1609.00740 "Fully Automated Treatment Planning for Head and Neck Radiotherapy using a Voxel-Based Dose Prediction and Dose Mimicking Method"
[3]: https://pubmed.ncbi.nlm.nih.gov/34083812/ "Clinical integration of machine learning for curative-intent radiation treatment of patients with prostate cancer - PubMed"
[4]: https://www.raysearchlabs.com/machine-learning-in-raystation/ "Machine Learning in RayStation | RaySearch Laboratories"
