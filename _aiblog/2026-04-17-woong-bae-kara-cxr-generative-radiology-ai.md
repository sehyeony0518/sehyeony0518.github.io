---
layout: post
title: "Beyond Average Accuracy: Woong Bae on KARA-CXR, Hallucination, and Clinical Trust"
date: 2026-04-17 12:00:00 +0900
description: Notes from Woong Bae's interview on why radiology AI should move beyond lesion detection, how KARA-CXR was designed to draft chest X-ray reports, and why rare but absurd errors matter more than a strong average score.
tag: "Kakao Brain"
related_posts: false
---

A medical AI system can perform well on average and still fail the moment that matters most.

That was the idea that stayed with me after listening to an interview with Woong Bae, then Vice President and Chief Healthcare Officer of Kakao Brain. The conversation, conducted by Dr. Yoon Sup Choi and released in March 2024, covered Kakao Brain's chest X-ray report-generation model KARA-CXR, the difficulty of evaluating hallucinations, the regulatory challenges of generative medical AI, workflow integration, medical foundation models, and AI-assisted antibody design. ([Yoon Sup Choi][2])

Bae's background helps explain the practical tone of the interview. Before joining Kakao Brain, he worked at VUNO on medical-imaging AI and physiological-signal products, including the development and regulatory process surrounding DeepCARS. At Kakao Brain, he oversaw both healthcare research and business, including KARA-CXR and an AI-based antibody-design initiative.

The interview was recorded before KARA-CXR became an authorized medical device. That makes it particularly interesting in retrospect.

> **2026 update.** Bae is now co-founder and CEO of Soombit.ai, which was established by members of Kakao Brain's former healthcare team. KARA-CXR was subsequently renamed AIRead-CXR. On April 1, 2026, Korea's Ministry of Food and Drug Safety granted it Class III authorization as the country's first generative AI-based digital medical device. The current product generates preliminary reports from adult frontal chest radiographs for review by qualified physicians; it does not provide an autonomous final diagnosis. ([Soombit.ai][1])

The questions raised in the interview — how to define hallucination, how to evaluate an open-ended report, and how to regulate a model capable of describing many findings — were therefore not abstract questions. They eventually became product, clinical-study, and regulatory-design questions.

## Part 1 — An AI-first company should still begin with a clinical problem

Kakao Brain was founded as an AI-centered research and product company rather than a healthcare company in the conventional sense.

Its healthcare strategy began by asking where advanced AI could create substantial social impact. The team experimented with several healthcare applications before concentrating on medical imaging and antibody design — areas in which the underlying AI capability was expected to be central to solving the problem.

But an AI-first strategy does not mean starting with a large model and searching for somewhere to deploy it.

The clinical problem came first.

Radiology departments face increasing imaging volumes, limited specialist capacity, delayed reporting, and professional burnout. Chest radiography is especially relevant because it is one of the most common examinations in medicine and appears across screening centers, outpatient clinics, emergency departments, hospital wards, and intensive care units.

Bae's team asked whether AI could assist with more than highlighting a small number of abnormalities. Could it reduce the burden of the complete reporting process?

This distinction is important.

A technically impressive capability is not automatically a valuable clinical product. The relevant question is not merely:

**What can this model predict?**

It is:

**Which part of the clinician's work is creating the bottleneck, and what form of assistance would actually change that workflow?**

## Part 2 — From detecting lesions to drafting the report

Bae divided chest X-ray interpretation into four broad stages.

A radiologist first scans the image for abnormalities. The radiologist may then compare it with prior studies, synthesize the available information into a differential interpretation, and finally document the conclusion in a radiology report.

Most early commercial medical-imaging AI systems concentrated on the first stage. They detected or classified a predetermined list of findings and displayed a location, score, or alert.

That can be useful, but it still leaves most of the interpretive and documentation process to the radiologist.

KARA-CXR took a different approach. A user could upload a frontal chest radiograph — either a standard posteroanterior image or the more variable anteroposterior image frequently obtained from seated, supine, or portable examinations — and receive a preliminary written report.

Bae described two output styles. A simple version provided a shorter interpretation, while a longer version followed a more structured reporting format containing findings, an impression, and possible recommendations.

The system was not presented as an autonomous radiologist.

Its intended role was closer to that of a first draft. The AI would write a preliminary report, and the radiologist would review, edit, and approve it — similar in concept to the way a supervising physician may review a report initially prepared by a trainee.

This changes the unit of assistance.

A detection system gives the clinician another piece of information to interpret.

A drafting system attempts to reduce the distance between the image and the completed clinical document.

KARA-CXR did not literally automate every component of radiological reasoning. For example, the interview focused on a single uploaded image rather than a complete longitudinal comparison with prior examinations. But it moved AI assistance further downstream, from locating selected abnormalities toward synthesizing image findings into clinically usable language.

## Part 3 — Test the workflow before training the model

One of the strongest product-development lessons in the interview came before the discussion of model architecture or training data.

The team first tested whether preliminary reports would actually help radiologists — even before the AI existed.

Developing a large medical model requires substantial data, engineering effort, computing resources, clinical collaboration, and regulatory planning. Building the entire system before confirming that its output improves the user's work would therefore be an expensive way to discover that the problem had been framed incorrectly.

Kakao Brain instead ran an MVP in which clinicians received preliminary reports without relying on a completed AI model. The purpose was to test the workflow hypothesis:

Would a useful first draft allow radiologists to report faster while maintaining or improving quality?

The response was sufficiently positive that the team proceeded to collect data, train the model, and release a web-based research demonstration.

This separates two questions that medical-AI development often mixes together.

The first is a **product question**:

> Would this form of assistance be useful if it were sufficiently accurate?

The second is a **model question**:

> Can AI generate that assistance with sufficient accuracy and safety?

Testing the first question independently prevents a team from optimizing a model for an intervention that clinicians never needed.

In medical AI, a high-performing model can still fail because the intervention itself is poorly designed. Pretotyping the workflow makes it possible to reject the intervention before spending years improving the algorithm.

## Part 4 — Scale expands the vocabulary, but not the certainty

Bae said that KARA-CXR had been developed using approximately 16 million chest X-ray images paired with their reports, collected from Korean and international sources covering varied institutions, clinical settings, disease findings, and imaging devices.

This scale was intended to address a major limitation of conventional disease-specific classifiers.

A classifier trained to detect 10 or 15 findings can produce results only for those predefined categories. It cannot easily describe an unexpected device, an uncommon postoperative state, or a finding that was absent from its original label schema.

A generative image-to-text model can, in principle, learn a much broader clinical vocabulary from reports. Bae described cases in which the system mentioned medical devices that were unfamiliar even to some of the clinicians using the demonstration.

But he was also cautious about saying that the model could identify **every** possible finding.

The reason was simple: the team had not evaluated every possible finding.

That distinction matters.

A large and diverse training corpus increases the number of situations the model may have encountered. It does not prove exhaustive coverage, and it does not establish performance for every rare disease, device, image-quality problem, or unusual combination of abnormalities.

Generative models expand both the answer space and the failure space.

A fixed classifier may be unable to mention an unmodeled disease. A generative model may mention it — but may also describe it incorrectly, place it in the wrong location, assign it the wrong severity, or generate a plausible sentence unsupported by the image.

Scale makes broader capability possible. It does not remove the need to specify what has actually been validated.

## Part 5 — Hallucination must be defined clinically

Hallucination is often discussed as though it were one universal phenomenon.

In practice, hallucination depends on the task.

In general-purpose language generation, it may mean inventing a citation, date, event, or fact. In chest radiology, it could include describing a lesion that is not present, placing a real abnormality on the wrong side, misstating the number of nodules, confusing a medical device, or recommending an inappropriate follow-up examination.

Bae acknowledged that KARA-CXR had hallucination problems and that the team was continuing to reduce them. His central point was that the problem becomes more manageable when the intended task is narrowly defined.

It may be impossible to construct a single test that captures every possible hallucination produced by a general-purpose model. But once the task is constrained to generating preliminary reports from frontal chest radiographs, the development team can begin to define clinically meaningful failure categories, construct evaluation metrics, and ask researchers to minimize those errors.

This is a fundamental shift from saying:

**The model sometimes hallucinates.**

to asking:

**Which unsupported statements can the model generate, how frequently do they occur, and how clinically harmful are they?**

A useful hallucination framework for medical reporting cannot rely only on textual similarity to a reference report. Two radiologists may describe the same image with different but equally valid wording. Conversely, a generated report can closely resemble a reference while still containing one clinically important false statement.

Evaluation must therefore operate at several levels:

* whether the major findings are correct;
* whether findings have been omitted or invented;
* whether their locations and quantities are correct;
* whether the impression follows from the findings;
* whether the report can be accepted without revision;
* and whether any error could materially affect patient management.

The goal is not simply to make the generated text sound radiological. It is to ensure that its clinical claims remain anchored to the image.

## Part 6 — The average can hide the error that destroys trust

Bae described what he called the danger of being deceived by averages.

A model may appear superior to a clinician according to an aggregate metric. It may perform well across thousands of common cases. But if it occasionally makes an error that a clinician considers completely unreasonable, users may stop trusting the product altogether.

That loss of trust is not necessarily irrational.

In healthcare, errors are not interchangeable. Missing a subtle chronic finding, generating the wrong follow-up recommendation, and overlooking a tension pneumothorax do not carry the same consequences.

An average score can combine many trivial successes with one catastrophic failure and still look excellent.

Bae therefore argued that a model should not be described as human-level merely because its average result resembles or exceeds the human average. Rare but unacceptable errors must also be minimized. He regarded hallucination as one of the clearest examples of this problem.

This suggests that clinical trust is closer to a **tail-risk problem** than a mean-performance problem.

A convincing safety evaluation should not ask only how often the model is correct. It should also ask:

How severe are its worst errors?

Do the same errors repeat systematically?

Are critical cases represented adequately in the test set?

Does performance change between screening, outpatient, emergency, and intensive-care environments?

Can users identify when the output is unreliable?

Does the model fail cautiously, or does it produce confident and polished language when its evidence is weak?

These questions are not captured by a single AUROC, report-similarity score, or average physician preference.

## Part 7 — What the later studies showed

Several studies published after the interview began to answer the empirical questions Bae had raised.

A 2025 *Radiology* study described the model as a domain-specific multimodal generative system. It first classified abnormalities using an image and transformer encoder and then generated the report through a transformer decoder conditioned on the image features and predicted findings. The researchers initially collected more than 14 million radiograph-report pairs and retained approximately 8.84 million after exclusions for the reported training set. ([Radiology][3])

On a test set of 2,145 radiographs, reports generated by the domain-specific model were accepted without modification in 70.5% of evaluations. Radiologist-written reports were accepted in 73.3%, while GPT-4Vision-generated reports were accepted in 29.6%. The domain-specific model's reports were ranked first among the three report types in 60.0% of comparisons. ([Radiology][3])

The result illustrates the value of domain-specific development. A general model capable of discussing many topics was not automatically competitive with a system trained and evaluated for one clearly specified medical task.

Another 2025 reader study evaluated five radiologists reading 758 chest radiographs. Providing the AI-generated report as a preliminary draft reduced average interpretation time from 34.2 seconds to 19.8 seconds and produced small improvements in reporting agreement and quality. However, the effects varied across individual radiologists. ([PubMed][4])

That study directly tested the workflow hypothesis that Kakao Brain had examined during its early MVP: a draft report can create value even when the AI is not intended to replace the reader.

A later multicohort study involving 1,539 individuals revealed a more nuanced picture. Under a standard criterion allowing either no revision or minor revision, AI-generated and radiologist-written reports had similar acceptability: 88.4% and 89.2%, respectively. Under the stricter requirement of acceptance without any revision, the AI reports performed worse: 66.8% compared with 75.7%. The generated reports showed higher sensitivity but lower specificity for referable abnormalities, and most participating radiologists did not consider them reliable enough to replace radiologist-written reports. ([Radiology][5])

Together, these findings support a more precise conclusion than either "AI has reached radiologist level" or "AI is not ready."

The system appears capable of producing useful preliminary reports, reducing reporting time, and improving sensitivity in some settings. At the same time, it still requires review, revision, and context-dependent evaluation.

That is exactly why the product is framed as a drafting assistant rather than an autonomous reporting system.

## Part 8 — Regulation begins with intended use

At the time of the interview, KARA-CXR had not yet received regulatory authorization.

Bae nevertheless argued that authorization would be necessary because the generated text could influence clinical decisions. The challenge was determining how a generative output should be evaluated.

A conventional chest X-ray classifier may have a fixed list of findings, allowing sensitivity, specificity, or AUROC to be calculated for each one. A report-generating model can potentially produce an enormous variety of findings, descriptions, impressions, and recommendations.

Testing every imaginable sentence is impossible.

Bae favored a more clinical approach. The test set should be sufficiently large and representative of real chest-radiography practice, and multiple radiologists should judge whether the generated report contains a clinical problem, whether it is acceptable, and whether it can be confirmed without editing. Reader studies could also compare radiologists working with and without AI assistance.

The eventual authorization resolved much of this open-endedness by narrowing the intended use.

AIRead-CXR is designed for adult PA and AP chest radiographs. It generates a preliminary report for licensed physicians, who must review and approve the output. The authorized product evaluates 57 core findings and diseases rather than claiming formally validated performance for every possible chest abnormality. ([Soombit.ai][6])

This illustrates a central principle of medical-device regulation:

**A model is not authorized in the abstract. A defined product is authorized for a defined user, input, output, population, and clinical purpose.**

The narrower specification does not diminish the technology. It creates the conditions under which its safety and effectiveness can be tested.

## Part 9 — Workflow integration is part of the medical device

Bae emphasized that even an accurate AI system can make radiologists less efficient if it is difficult to use.

Kakao Brain therefore considered integration with the radiologist's existing environment essential. Rather than forcing the user to move between applications or manually transfer text, the preliminary report should appear directly within the reporting workflow, ideally through integration with the hospital's picture archiving and communication system.

The planned commercial model was software-based rather than tied to a particular X-ray machine, with per-examination or subscription pricing adjusted to reporting volume. The team was also preparing for partnerships with PACS vendors because the interface through which the result reached the physician would determine much of its practical value.

This is more than a sales or user-interface issue.

The same model can produce different clinical effects depending on how it is deployed.

A draft that automatically appears in the reporting window may save time. The identical text displayed in a separate web page may create additional clicks, cognitive switching, and copying errors.

A report presented before the radiologist's independent review may influence attention differently from one displayed afterward.

A system that clearly distinguishes generated text from approved text creates a different accountability structure from one that silently inserts language into the final report.

Workflow is therefore part of the intervention and part of the safety case. It should be evaluated alongside model performance, not treated as packaging added after the model has been validated.

## Part 10 — Foundation models will not eliminate the service layer

The interview also explored whether increasingly general AI systems would eventually absorb specialized healthcare products.

Bae expected the industry to divide, at least temporarily, into two broad groups.

One group would pursue highly general AI or AGI-scale models. The other would develop services that solve specific customer problems. He expected general systems to become increasingly powerful, but argued that specialized service companies would retain an advantage through problem definition, user relationships, workflow knowledge, and trusted brands.

Even if an AGI company eventually provides the underlying intelligence, it may still need to collaborate with a healthcare company that understands how to turn that intelligence into a regulated and trusted clinical service.

This argument is particularly relevant in medicine.

A general model may be capable of interpreting an image. That does not automatically give its developer access to representative clinical data, an appropriate intended-use statement, a validated reporting interface, regulatory documentation, hospital integration, post-market monitoring, or clinician trust.

Bae also questioned whether service companies always need the largest possible model. If the customer's problem is precisely understood, a focused model may create more value than a vastly larger model developed without a clear clinical purpose.

In retrospect, the transition from Kakao Brain's healthcare division to Soombit.ai makes this distinction concrete. The underlying generative-AI capability became the foundation for a company focused specifically on radiology workflow, evidence generation, authorization, and deployment. ([Soombit.ai][1])

The foundation model matters.

But the clinical system built around it determines whether the model becomes more than a demonstration.

## Part 11 — The same philosophy extends beyond radiology

Kakao Brain's healthcare work was not limited to medical imaging.

Bae also described a partnership with Galux, founded by Seoul National University chemistry professor Chaok Seok, to develop AI-based antibody-design technology. The program focused on predicting antibody structures, identifying where an antibody would bind to a target antigen, estimating binding affinity, reducing unintended binding, and experimentally validating the resulting designs.

Kakao Brain had invested in Galux and planned to combine large-scale AI expertise with Galux's protein-modeling and molecular-design technology. The collaboration covered antigen–antibody complex prediction, binding-strength prediction, antibody design, and experimental verification. ([Galux][7])

Although report generation and antibody design appear to be very different problems, they reflect the same strategic logic.

Both involve domains in which expert work is expensive, data and physical constraints matter, and a superficially convincing output is not enough.

A generated radiology report must remain faithful to the image.

A designed antibody must bind the intended target, avoid unintended interactions, and survive experimental validation.

In both cases, AI produces a candidate. Reality provides the final audit.

## A researcher's takeaway

The most memorable part of this interview was not the size of the training dataset.

It was Bae's warning about the deception of the average.

Medical-AI research often compresses model behavior into one number. Yet clinical trust is shaped disproportionately by the failures that appear unreasonable, dangerous, or impossible for the user to anticipate.

This becomes even more important for generative systems. A classifier produces a bounded set of scores. A report-generating model produces a clinical narrative whose findings, locations, certainty, interpretation, and recommendations may each be correct or incorrect in different ways.

The evaluation must expand with the output space.

KARA-CXR's development also shows that trustworthy medical AI requires more than adding a safety test after the model has been trained. Trust begins with defining the problem narrowly, validating that the proposed workflow is useful, specifying the role of the human reviewer, constructing clinically meaningful failure categories, and designing the regulatory indication around what can actually be supported by evidence.

The later evolution into AIRead-CXR is important because it turned those principles into a real product pathway: domain-specific model development, multireader validation, workflow studies, restricted intended use, mandatory physician review, and regulatory authorization.

The central lesson is therefore not that generative AI can write radiology reports.

It is that a fluent report becomes clinically valuable only when its claims are measurable, its failures are bounded, and its place in the workflow is clear.

Average performance may earn attention.

Trust is earned by what happens outside the average.

[1]: https://soombit.ai/about "Soombit.ai — About"
[2]: https://www.yoonsupchoi.com/2024/03/19/kakao-brain-cho-interview/ "Kakao Brain interview — Yoon Sup Choi"
[3]: https://pubs.rsna.org/doi/10.1148/radiol.241476 "Radiology (2025)"
[4]: https://pubmed.ncbi.nlm.nih.gov/40067108/ "Reader study — PubMed"
[5]: https://pubs.rsna.org/doi/10.1148/radiol.250568 "Radiology (2025), multicohort study"
[6]: https://soombit.ai/news/license-2 "Soombit.ai — AIRead-CXR MFDS authorization"
[7]: https://galux.co.kr/ko/sub/newsroom/detail.php?id=1&type=news "Galux — Kakao Brain partnership"
