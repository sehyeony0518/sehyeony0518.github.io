---
layout: post
title: "Beyond the Benchmark: Ghada Zamzmi and Jean Feng on Building Medical AI That Survives Deployment"
date: 2025-10-24 12:00:00 +0900
description: Notes from a MICCAI webinar on regulatory-driven AI development, clinically meaningful endpoints, data quality, post-market drift, SHIFT, and why diagnosis should come before model retraining.
tag: "MICCAI"
featured: true
related_posts: false
---

A medical-AI model can perform impressively on a benchmark and still fail before reaching a patient.

It may address a problem that clinicians do not urgently need solved. Its endpoint may not correspond to a meaningful clinical benefit. Its development data may omit the population, workflow, or acquisition conditions encountered after deployment. Even after successful implementation, changes in patients, practice patterns, databases, and hospital systems may gradually make the model unreliable.

The benchmark is therefore not the end of medical-AI evaluation. It is one point in a much longer lifecycle.

This post is based on the MICCAI Special Interest Group for Challenges webinar *Beyond the Benchmark Dataset: Real-World Generalizability and Regulatory Challenges in Medical AI*, held on October 10, 2025. ([MICCAI Society][1])

The webinar brought together two complementary perspectives.

Ghada Zamzmi, introduced as a regulatory scientist and AI researcher at HeartFlow, discussed how regulatory science should influence medical-AI development before a model reaches the market. Her central argument was that developers should begin with the intended clinical use, define meaningful endpoints and acceptance criteria, and treat data quality as a core design decision rather than a preliminary technical task.

Jean Feng, an associate professor at the University of California, San Francisco and the UCSF–UC Berkeley Joint Program in Computational Precision Health, focused on what happens after validation. She examined why performance changes across hospitals and over time, why automatic retraining is often the wrong first response, and how the SHIFT framework can identify the subgroups and variables associated with performance decay. ([PMC][2])

Taken together, the two talks describe one continuous process:

**clinical framing → data and model development → validation → deployment → monitoring → diagnosis → corrective action.**

The first talk asks how to prevent foreseeable failures from being designed into the system. The second asks how to understand and repair the failures that emerge despite those precautions.

Any errors of interpretation are mine.

## Part 1. Innovation should begin with the final clinical use

Zamzmi began by acknowledging the extraordinary pace of technical innovation in medical AI.

Medical-imaging conferences are filled with increasingly capable diffusion models, foundation models, multimodal systems, and new architectures. This work is necessary for the field to advance. Her argument was not that theoretical or technical research should stop.

The problem is that many technically sophisticated systems never leave the laboratory.

A major reason is **clinical misalignment**: the model is developed before researchers have clearly defined the clinical problem, deployment conditions, regulatory requirements, or patient-safety implications.

Zamzmi proposes a shift toward **regulatory-driven AI innovation**.

The term does not mean that regulation should suppress scientific creativity. It means that researchers should innovate with the eventual use of the system in mind. Instead of building the most advanced model possible and later searching for an application, development should be organized around the product's intended use and eventual clinical label.

This approach is already familiar in other high-risk industries.

A drug-development program begins with a proposed therapeutic indication and designs its evidence-generation process around that intended label. An aviation system is not designed by optimizing technical performance alone. Developers must also consider the pilot, operating environment, failure conditions, training requirements, and interaction between the human and the machine.

Medical AI should be approached with the same discipline.

Before selecting an architecture, researchers should be able to answer several basic questions:

* What clinical problem is the system intended to solve?
* Who is expected to use it?
* At what point in the workflow will it be used?
* How will the user interact with its output?
* Which patient population is included?
* Which disease spectrum and clinical settings are represented?
* What uses are outside the intended scope?

These questions are not administrative details to be written after development. They determine what data should be collected, which errors matter, how performance should be measured, and what evidence will eventually be required.

A model can be statistically excellent while solving a clinically irrelevant problem. It can also answer a useful question at the wrong time, for the wrong user, or in a form that cannot change care.

The intended use is therefore not merely the wording on an authorization document.

It is the organizing hypothesis of the entire project.

## Part 2. State-of-the-art performance is not the clinical definition of success

Machine-learning research often defines progress through comparison with the current state of the art.

A higher AUROC, Dice score, sensitivity, or F1 score provides a clear and convenient basis for ranking methods. That logic is useful for technical development, but it is insufficient for a medical product.

Zamzmi reframed success around three requirements:

1. performance must be clinically acceptable;
2. the system must be safe;
3. the system must be effective for its intended use.

This leads to four practical questions:

1. **What should be measured?**
2. **What is good enough?**
3. **For whom does the system work?**
4. **How strong is the supporting evidence?**

The first question challenges the assumption that familiar computer-vision metrics should automatically become clinical endpoints.

The appropriate endpoint depends on the task.

For a triage system, the purpose may be to identify the most urgent cases early enough to change the order in which clinicians review them. Sensitivity remains important, but time to notification may be just as consequential. A model that detects every critical case after the clinician has already reviewed it has little triage value.

For a screening system, the aim may be to minimize missed disease while preventing an unmanageable number of unnecessary follow-up examinations. A relevant endpoint could therefore be sensitivity at a prespecified specificity floor, accompanied by an analysis of net clinical benefit and additional workload.

A segmentation system may require another form of evaluation. A geometric error of two millimetres may be inconsequential in one anatomical region and clinically dangerous in another. The numerical size of the error does not determine its clinical cost independently of location and task.

The same principle applies to classification errors.

A model with 99% accuracy may still be unacceptable when the remaining 1% consists of preventable failures in a life-threatening application. False positives and false negatives rarely carry equal costs, and those costs can vary across patients and settings.

Metrics should therefore follow the clinical task.

The clinical task should not be reconstructed after researchers have selected the metric they know how to optimize.

## Part 3. "Good enough" requires a risk-informed boundary

Once the relevant endpoint has been selected, the next question is what level of performance is acceptable.

There is no universal threshold.

The required performance should reflect the risk profile of the device, the role of the user, the availability of clinical oversight, and the consequences of error. A system that autonomously controls a life-sustaining intervention requires a different evidentiary standard from a system that organizes information for review by a trained specialist.

Zamzmi identified several possible sources for defining an acceptance criterion:

* clinical guidelines;
* the existing standard of care;
* measured human performance;
* established clinical outcomes;
* and a formal analysis of risk and benefit.

The target value should be clinically justified, while its uncertainty boundaries should be supported by data.

This distinction matters because a point estimate alone can be misleading. A model may appear to meet a threshold in a small development dataset while its confidence interval extends below the clinically acceptable range.

The choice of data used to establish the boundary is also critical.

Suppose the acceptance criterion is derived from a development cohort with a particular disease prevalence. After deployment, the model encounters a population in which prevalence, severity, referral patterns, or comorbidity structure differs. Metrics such as positive predictive value may then change substantially even if the underlying model has not.

A threshold that looked appropriate in development may no longer support the intended clinical use.

This creates a difficult practical problem. Developers often cannot obtain a perfect representation of the future deployment environment before deployment occurs. Zamzmi suggested that carefully validated synthetic data may sometimes help researchers explore plausible scenarios and broaden relevant coverage.

But synthetic data are not automatically trustworthy.

Her own work found that generative image models could produce anatomically implausible breast images, including incorrect shape and duplicated anatomical structures. Such images may appear visually realistic at a glance while violating clinically important constraints.

Synthetic data may extend a dataset, but only after their intended role and clinical validity have been examined.

Generated diversity should not be mistaken for valid clinical representation.

## Part 4. Equal performance is not the whole meaning of equity

Subgroup analysis is essential, but interpreting it requires more than checking whether every group receives the same numerical score.

Zamzmi described an experience from work on sickle cell disease. Her initial instinct was to seek equal performance across all groups. Clinical collaborators emphasized, however, that the disease burden was not distributed equally and that performance in the population carrying the greatest clinical risk deserved particular attention.

The lesson is not that unequal performance should be accepted casually.

It is that equality on one aggregate metric does not necessarily guarantee equitable clinical value.

A higher-risk subgroup may require greater sensitivity. Another subgroup may experience greater harm from false positives. Differences in disease prevalence can alter predictive values even when sensitivity and specificity remain constant. Access to follow-up care may also determine whether the same model output produces equal benefit.

Fairness must therefore be interpreted in the context of:

* disease burden;
* error cost;
* baseline risk;
* availability of subsequent care;
* and the model's role in the workflow.

A model could report similar average accuracy across groups and still produce unequal outcomes. Conversely, a clinically justified operating policy may intentionally place a stricter sensitivity requirement on a particularly vulnerable population.

The objective should not be superficial numerical symmetry.

It should be an evidence-based account of who benefits, who carries the errors, and whether the system reduces or reproduces existing inequities.

## Part 5. Data quality sets the ceiling

Medical AI is often described as data-hungry, but Zamzmi emphasized that it is also fundamentally **data-driven**.

The model learns the regularities, omissions, errors, and confounders contained in its development data. A sophisticated architecture cannot recover information that was never measured, correct labels that are systematically wrong, or distinguish disease from acquisition bias without sufficient evidence.

Poor data do not simply reduce performance slightly. They can determine the failure modes of the entire system.

Zamzmi discussed several dimensions of data quality:

* representativeness;
* completeness;
* correctness of feature values;
* target and annotation accuracy;
* consistency;
* metadata quality;
* and fitness for the intended purpose.

Experimental work cited in the talk showed performance degradation when training data, evaluation data, or both were corrupted. Incomplete features, incorrect values, poor representation, and unreliable targets all affected downstream models.

The familiar phrase "garbage in, garbage out" is therefore not a cliché in this context. It describes a causal feature of the development process.

Annotation quality deserves particular attention.

Medical labels often contain disagreement because the clinical phenomenon itself is ambiguous, experts apply different criteria, or the reference standard is imperfect. Labels generated from reports, billing codes, or automated rules may introduce additional errors.

If the reference used to evaluate the model is unreliable, model performance becomes difficult to interpret.

Possible responses include the use of multiple annotators, formal consensus procedures, adjudication, and probabilistic approaches that preserve disagreement instead of forcing every case into one apparently certain label.

The central principle is that annotation quality establishes an upper bound on what the model can meaningfully learn and what an evaluation can claim.

A model should not be described as exceeding clinicians when its "ground truth" is itself an unstable or weak approximation of clinical truth.

## Part 6. Confounders should be studied before the trial

Biases in medical data are not limited to age, sex, or race.

They can enter through scanners, acquisition parameters, referral pathways, hospital departments, medication use, site selection, missingness, or differences in how and when tests are ordered. A model may associate one of these variables with the outcome and appear accurate without learning the intended clinical signal.

Zamzmi therefore argued that researchers should investigate the factors driving model performance early in development.

The relevant variables are task- and modality-specific. In one study, demographic characteristics and medication may be central. In another, scanner manufacturer, reconstruction method, imaging protocol, or institution may dominate.

This analysis should occur before a costly clinical trial.

If researchers do not understand the data-generating process, a trial can be built around a model whose apparent performance depends on a hidden shortcut. Once that model is transferred to another setting, the association may disappear.

Causal reasoning can help distinguish the intended clinical relationship from site-specific noise and clarify which variables should be controlled, stratified, or represented in the evaluation.

This does not mean every medical-AI study requires a complete causal model of the healthcare system. It means that researchers should explicitly ask why the input contains information about the outcome and whether that relationship is expected to survive deployment.

A model that predicts well for the wrong reason remains a deployment risk even before any performance decline is observed.

## Part 7. Deployment is not the end of development

The second half of the webinar begins where many benchmark studies end.

The model has been trained. Internal validation has been completed. Perhaps it has even been evaluated on a public benchmark or an external dataset.

What happens next?

Feng separates the post-development lifecycle into deployment, monitoring, diagnosis, and correction.

Each transition introduces new challenges.

Moving from retrospective validation to prospective use can change the database from which features are retrieved, the timing of data availability, the definition of the population, and the way predictions enter the workflow. Moving between hospitals introduces differences in patients, equipment, clinical practice, and documentation.

Even after successful deployment, the environment continues to change.

A new treatment protocol may alter the relationship between inputs and outcomes. A pandemic may change patient behavior and hospital utilization. Software systems may be replaced. Coding practices may evolve. The prevalence of a disease may shift. A model trained on an earlier period can gradually become outdated.

Feng emphasized that post-market monitoring is therefore necessary, but monitoring itself must be evaluated.

The mere existence of a dashboard or drift detector does not prove that clinically meaningful degradation will be found. A monitoring system can have low statistical power, generate excessive false alarms, or focus on changes that do not affect model performance.

In her words, having a monitoring system is not necessarily the same as having a good monitoring system.

Techniques from statistical process control and quality assurance can provide a starting point. These methods have long been used in manufacturing to distinguish routine process variation from meaningful deviation.

Medical AI, however, requires a clinically grounded definition of the process being monitored.

As Zamzmi noted, not every deviation is drift. Some variation reflects the natural course of the disease, seasonal patterns, or expected differences in the clinical population. Developers must understand that baseline variability before defining an alarm.

Otherwise, monitoring may interpret ordinary medicine as model failure, or fail to notice a clinically important change because it is hidden within aggregate stability.

## Part 8. Detection should be followed by diagnosis, not automatic retraining

Once monitoring detects a problem, the intuitive response is to retrain the model.

Collect recent data, fit a new model, and replace the old one.

Feng argues that this should not be the automatic first step.

Retraining has several limitations.

It has non-zero financial, computational, operational, and regulatory costs. The updated model is not guaranteed to outperform the original. A model optimized for the most recent slice of data may become more brittle and lose useful generalizability. Fine-tuning can repair performance in one environment while degrading it elsewhere.

Most importantly, retraining assumes that the model is the source of the problem.

That assumption may be wrong.

The failure may originate in the data pipeline, missing features, an altered definition, an interface, a new subgroup, a prevalence shift, or a local workflow. In such cases, replacing the entire model can conceal the root cause while introducing new uncertainty.

Feng proposes adding a diagnostic step between monitoring and redevelopment:

**detect a problem → diagnose its source → select the smallest justified correction.**

Depending on the diagnosis, the appropriate response might be:

* repairing data extraction;
* restoring a missing variable;
* recalibrating the output;
* adjusting an operating threshold;
* applying a subgroup-specific model;
* adding a wrapper around the existing system;
* retraining only part of the model;
* fully retraining the model;
* or temporarily suspending its use.

The principle resembles clinical medicine itself.

Detection establishes that something is wrong. Diagnosis determines what should be treated.

## Part 9. SHIFT asks where performance changed and why

Diagnosing performance decay is difficult because clinical AI operates in high-dimensional environments.

Feng introduced two broad mechanisms of dataset shift.

A **covariate shift** occurs when the distribution of the model inputs changes across domains. Patients may be older, imaging properties may differ, or laboratory measurements may follow another pattern.

An **outcome shift** occurs when the relationship between the inputs and the target changes. The same clinical characteristics may no longer correspond to the outcome in the same way because treatment, documentation, referral, or practice has changed.

In a high-dimensional model, many variables may differ across two hospitals. Merely demonstrating that the input distribution has changed does not tell us which differences caused the performance loss.

Average performance can also conceal the problem.

A model's overall AUROC or accuracy may remain nearly unchanged while a clinically important subgroup experiences severe deterioration. Monitoring only the average can therefore miss inequitable or localized failure.

Feng's group developed the **Subgroup-scanning Hierarchical Inference Framework for performance drifT**, or **SHIFT**, to make the diagnosis more granular. ([PMC][2])

The framework asks two sequential questions.

First, **where** is performance decay occurring?

It searches for subgroups in which the deterioration attributable to covariate or outcome shift exceeds a prespecified meaningful level.

Second, **how** can that deterioration be explained?

It examines which variables or combinations of variables contribute to the identified shift.

The approach can be understood as a form of variable-importance analysis for performance decay. Rather than asking which variables generally influence a model prediction, it asks which variables explain why performance changed between two domains.

SHIFT does not automatically prove a causal explanation.

A flagged variable identifies a plausible source that should be investigated with domain experts and operational data. The meaningful performance threshold must also be chosen in advance, and an overly sensitive system could create another form of alarm fatigue.

Its value lies in narrowing the search.

Instead of responding to an unexplained decline with a full model replacement, the clinical and technical teams receive a testable account of which population and which data-generating differences deserve attention.

## Part 10. A successful model at Duke did not transfer directly to UCSF

Feng's first case study concerned a model developed by radiation oncologist Julian Hong and collaborators to predict acute-care needs among patients receiving radiation therapy.

The model was a gradient-boosted tree trained on tabular clinical data at Duke.

It had unusually strong clinical evidence behind it. A randomized clinical trial at Duke found that using the model as part of an intervention reduced acute-care utilization from approximately 22% to 12%.

This was not merely a retrospective model with a strong benchmark score. It had already demonstrated value within a real care pathway.

When Hong later moved to UCSF, the natural question was whether the same system could be transferred.

At Duke, the model's positive predictive value was approximately 20%. When tested at UCSF before deployment, the positive predictive value fell to about 9%.

A simple response would have been to discard the original model and retrain it entirely on UCSF data.

But the Duke system had already passed through a randomized trial. Replacing it without understanding the failure would mean abandoning a clinically validated model and introducing a new one with less evidence.

The diagnostic analysis indicated that covariate shift was the dominant issue.

A particular subgroup accounted for only about 3% of the Duke population but approximately 34% of the UCSF population. Further investigation showed that UCSF included substantially more patients with prostate cancer and related conditions. These patients also tended to have lower emergency-department utilization.

The transferred model was therefore not uniformly broken.

It was encountering a much larger subgroup whose clinical characteristics and utilization patterns differed from those represented at Duke.

The team implemented a limited correction.

A wrapper first determined whether a patient belonged to the shifted subgroup. Patients resembling the original Duke population continued to use the original model. Patients in the newly prominent subgroup were directed to a separate model.

This targeted update nearly closed the gap in positive predictive value.

The case illustrates why diagnosis matters.

The original model remained useful for much of the new population. Full retraining would have modified predictions for every patient, including those for whom the original clinically tested system still worked.

The wrapper preserved what was already supported by evidence and changed only the part that the diagnosis identified as deficient.

## Part 11. The acute kidney injury model did not initially need a new model

The second case involved a system for predicting intraoperative acute kidney injury.

During retrospective development, the model achieved a positive predictive value of approximately 40%. In silent prospective deployment, the positive predictive value fell to around 13%.

The size of the drop could easily have been interpreted as model failure.

The diagnostic process highlighted differences in laboratory measurements and vital signs, along with evidence of an outcome-related shift. When the team investigated those variables directly, it found a major missing-data problem.

The retrospective model had been developed using an analytical database. Prospective deployment relied on a live operational database. Features expected by the model were not being retrieved in the same way, leaving many values unavailable.

The primary failure was therefore not that the learned relationship had become obsolete.

The deployed model was receiving a materially different and incomplete input.

The corrective action was correspondingly simple: work with the deployment team to repair how the data were being pulled.

After the data issue was addressed, positive predictive value improved substantially. The original gap was not completely eliminated, and further diagnostic work remained necessary. But the intervention recovered performance without blindly replacing the model.

This case exposes an important ambiguity in the phrase "real-world generalization."

When a model performs poorly prospectively, the cause may be statistical distribution shift. It may also be a software-engineering failure, delayed data availability, inconsistent variable definition, or broken interface.

From the patient's perspective, all of these produce the same result: an unreliable prediction.

From the perspective of corrective action, however, they are entirely different problems.

Model monitoring must therefore be connected to data-pipeline observability and institutional operations. A clinical-AI team cannot maintain performance by studying model weights alone.

## Part 12. PCCP turns anticipated repair into a regulatory plan

A model used in clinical care cannot necessarily be modified whenever a monitoring team detects deterioration.

Regulated medical devices are generally authorized in an identified form. A meaningful change to the model, its inputs, intended use, or performance may require further regulatory review.

The **Predetermined Change Control Plan**, or **PCCP**, provides one way to prepare for foreseeable changes. ([FDA][3])

Under this approach, a developer describes anticipated modifications during the original regulatory submission. The plan explains:

* which changes may become necessary;
* under what conditions they would be triggered;
* how the modified system would be developed;
* how its performance would be validated;
* how the impact of the change would be assessed;
* and what boundaries would continue to apply.

If the regulator accepts the plan and a later change remains within its authorized scope, the manufacturer may implement that change without repeating the full submission process that would otherwise be required.

A population shift could potentially be addressed through a PCCP, but only when the detection mechanism and response have been specified clearly enough in advance.

The developer cannot simply state that the model will be updated whenever performance decreases. The plan must explain how deterioration will be recognized, what type of update will be made, and how the revised system will be shown to remain safe and effective.

Changes outside the plan may still require a new submission.

This connects Feng's diagnostic framework to Zamzmi's regulatory-driven development.

The post-market response should be considered before deployment. If a developer can anticipate meaningful shifts, monitoring signals, and corrective actions, those elements can become part of the product's original lifecycle strategy.

The model may change, but the governance of that change should not be improvised after failure occurs.

## Part 13. Standard benchmarks remain necessary, but they are not sufficient

During the discussion, a participant asked what would be required to create open and trustworthy medical-AI benchmarks.

Both speakers agreed that existing public datasets are valuable for research but often insufficient for product development and regulatory evidence.

A sustainable benchmark would require more than uploading data.

Hospitals, academic groups, regulatory agencies, and industry would need to agree on data quality, intended uses, documentation, governance, privacy, representativeness, and appropriate reference standards. The infrastructure would also require long-term funding.

The goal would not simply be a leaderboard.

A clinically useful benchmark should help determine whether a system meets minimum evidence requirements, behaves consistently across relevant populations, and can be compared with alternatives under conditions that resemble deployment.

Even such a benchmark would remain only one part of the evidence.

No centralized dataset can represent every hospital, future time period, workflow, or patient population. A model that performs well on the strongest available benchmark still requires local validation, post-market monitoring, and a plan for responding to change.

The benchmark can reduce uncertainty before deployment.

It cannot abolish the need to learn from deployment.

## Part 14. Translation requires different academic incentives

The final discussion turned from models to research culture.

A student asked how machine-learning and computer-vision researchers could contribute to these problems from within a laboratory.

Zamzmi's answer was that medical AI needs methods designed for medicine rather than methods imported unchanged from general computer vision.

That includes:

* clinically aligned performance metrics;
* risk-sensitive evaluation frameworks;
* methods for data-quality assessment;
* subgroup analysis;
* robust monitoring;
* drift diagnosis;
* and tools for evaluating intervention and workflow impact.

Feng added that close collaboration is essential.

Her own experience working with regulators changed which theoretical questions appeared practically important. Problems that seemed interesting in abstraction were not always the problems that hospitals and regulatory agencies needed solved.

Clinical translation exposes questions that a benchmark alone cannot reveal.

The discussion also identified a structural obstacle: academia frequently rewards publications and state-of-the-art comparisons more visibly than deployment work.

Translational grants could require deliverables such as validated tools, monitoring systems, or implementation frameworks in addition to papers. Journals and conferences could create more space for rigorous reports of deployment, failure analysis, corrective action, and long-term maintenance.

These studies may not introduce a larger neural network.

They can nevertheless contribute more directly to patient safety than another marginal improvement on an internal benchmark.

The field needs venues in which discovering why a model failed is treated as scientific progress rather than as an embarrassing absence of progress.

## A researcher's takeaway

The two talks correct opposite but related simplifications.

The first simplification is that a strong model can be translated by adding clinical context after development.

Zamzmi shows why this is mistaken. Intended use, user, population, workflow, endpoint, acceptance criterion, data quality, and risk should shape the project before training begins.

The second simplification is that a deployed model can be maintained by monitoring performance and retraining whenever it declines.

Feng shows why this is also mistaken. Monitoring establishes that something may have changed. It does not identify what changed or determine the appropriate intervention.

Together, the talks suggest five principles for trustworthy medical-AI development.

### 1. The clinical claim should precede the model

The intended use is not a description attached to a finished algorithm. It determines the relevant data, errors, endpoints, and evidence.

### 2. Performance must be interpreted through consequence

A higher aggregate score is not automatically a clinically better system. The cost of error, timing of the output, operating threshold, workflow burden, subgroup risk, and available intervention all matter.

### 3. Data quality is part of the model

Missingness, annotation variability, site characteristics, acquisition practices, and feature definitions are not external nuisances. They help determine what the model learns and how it fails.

### 4. Monitoring should lead to diagnosis

A performance alarm should initiate an investigation into subgroups, covariates, outcomes, and infrastructure. Retraining is one possible treatment, not the default diagnosis.

### 5. Change should be anticipated and auditable

Monitoring rules, corrective actions, validation procedures, version control, and regulatory pathways should be designed as part of the product lifecycle rather than invented after deployment.

These principles also matter for research on clinical evidence auditing.

An audit of a trained model may reveal that it relies on a clinically questionable feature, unstable frequency band, acquisition shortcut, or spurious correlate. But the audit itself is also situated within a lifecycle.

The relevant evidence may change when the model is transferred, fine-tuned, recalibrated, wrapped with another model, or connected to a different data pipeline. A correction that improves one subgroup could alter evidence use elsewhere. A model whose parameters are unchanged could behave differently because its inputs are missing or differently distributed.

A trustworthy audit must therefore ask not only:

> What evidence does this model use?

It must also ask:

> Under which population, site, version, pipeline, and clinical context does it use that evidence, and how will we know when the answer changes?

The Duke-to-UCSF case is especially instructive. The original model was not globally invalid. Its performance problem was concentrated in a subgroup that had become far more common at the new institution. The best response preserved the original model where its evidence remained relevant and introduced a limited correction where it did not.

The acute kidney injury case goes further. What appeared to be model degradation was partly a failure of data delivery. No interpretability method applied only to the checkpoint could have repaired a missing feature pipeline.

The unit of trustworthiness is therefore larger than the model.

It includes the data source, intended use, user, workflow, monitoring system, diagnostic process, update policy, and regulatory boundary.

A benchmark tells us what a model did once, on a defined dataset.

A medical-AI lifecycle must tell us what the model is supposed to do, for whom, under which conditions, how we will recognize when those conditions have changed, and what evidence will justify the next action.

Going beyond the benchmark does not mean abandoning technical performance.

It means placing performance inside the system that gives it clinical meaning.

[1]: https://miccai.org/2025/09/03/webinar-beyond-the-benchmark-dataset-october-10-2025/ "Webinar: Beyond the Benchmark Dataset, MICCAI Society"
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12747154/ "SHIFT: Subgroup-scanning Hierarchical Inference Framework for performance drift"
[3]: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence "FDA Guidance: Predetermined Change Control Plans for AI-Enabled Device Software Functions"
