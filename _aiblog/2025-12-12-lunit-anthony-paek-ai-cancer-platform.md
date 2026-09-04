---
layout: post
title: "Beyond Point Solutions: Lunit's Vision for an AI-Native Cancer Platform"
date: 2025-12-12 12:00:00 +0900
description: Notes from Lunit co-founder Anthony Seungwook Paek on Volpara, foundation models, autonomous AI, and the shift from accurate algorithms to an integrated cancer-care platform.
featured: true
tag: "Lunit"
related_posts: false
---

This post summarizes a long-form conversation between Dr. Yoon Sup Choi and Anthony Seungwook Paek, co-founder and Executive Chairman of Lunit. Recorded near the end of 2023 and released in early 2024, the interview took place just after Lunit announced its plan to acquire Volpara Health Technologies. It should therefore be read as a snapshot of Lunit's strategy at that point, rather than as a current product catalogue. ([YouTube][2])

> **Update.** Lunit completed the Volpara acquisition in 2024. In November 2025, the company announced that Volpara would operate under the Lunit brand as part of a unified global organization. ([Lunit][3])

## Part 1. Accuracy is only the entry ticket

Lunit was founded in 2013 with an unusually direct mission: **conquer cancer through AI**.

At the time of the interview, Paek described the company through two major product groups. The Cancer Screening Group developed Lunit INSIGHT, which analyzes medical images such as chest X-rays and mammograms to identify suspicious findings. The Oncology Group developed Lunit SCOPE, which analyzes pathology images and seeks to predict whether a patient is likely to respond to a particular cancer treatment.

The more important point, however, was that Lunit's growth equation was changing.

In the early years of medical AI, a highly accurate algorithm was itself enough to attract attention. A company could build a model, demonstrate strong performance, obtain regulatory clearance, and enter the market through partnerships. As the field matured, that became insufficient. Hospitals did not simply want another accurate model; they wanted a product that solved a recognizable operational or clinical problem.

This is the transition from an **AI-centered product** to a **customer-centered system**. The question is no longer only whether the model can detect cancer. It is whether the software fits into the hospital's infrastructure, supports the clinician's workflow, reduces unnecessary work, and ultimately changes the patient pathway.

In that sense, benchmark accuracy is not the finished product. It is the entry ticket.

## Part 2. Volpara: acquiring workflow, distribution, and a data flywheel

This shift explains why Volpara was strategically attractive.

Volpara was founded in 2009, before the modern deep-learning boom. It began with software for measuring breast density, relying more heavily on mathematics and imaging physics than on contemporary AI. It later expanded through acquisitions into breast-cancer risk assessment and patient-centered screening workflow management.

By the time Lunit approached the company, Volpara possessed many of the capabilities Lunit lacked in the US breast-screening market: an established customer base, subscription-based software revenue, workflow infrastructure, breast-density and risk-assessment tools, image-quality management, and long-standing relationships with screening centers.

Lunit, by contrast, brought advanced cancer-detection AI.

The proposed combination was therefore not simply a matter of placing two algorithms next to each other. Paek described an integrated environment in which a breast-imaging center could receive density, risk, image-quality, and cancer-detection results through a unified interface. Instead of purchasing several disconnected point solutions, the customer could use a broader software suite built around the full screening process.

The acquisition also addressed distribution. Lunit had strong technology, but its US market presence had been limited by regulatory scope and the difficulty of understanding local clinical operations from Korea. Volpara offered an installed customer network and an organization already accustomed to selling subscription software in the United States.

A third component was data. Paek argued that medical AI cannot remain sustainable if a company must begin a new, expensive data-acquisition project whenever it wants to improve a model. The more durable structure is a feedback loop:

**product deployment → newly generated data → model improvement → better products → wider deployment**

Volpara had already built part of the contractual and operational infrastructure required for such a cycle. Paek was careful to distinguish permission to use data from ownership of the data itself, but the strategic value was clear: continuous access is more powerful than a one-time dataset.

The final consideration was culture. Paek saw both companies as science-oriented organizations from countries outside the conventional center of the global technology industry, yet determined to compete in the largest markets. He also emphasized their shared preference for evidence-based decisions, ambitious goals, and interpersonal respect. Lunit continues to express the latter through the unusually explicit value, **"Respect one another, with love."** ([Lunit][1])

The broader lesson is that post-merger integration depends on more than a spreadsheet of product synergies. When two organizations must combine teams across countries, languages, and professional backgrounds, culture becomes part of the technical infrastructure.

## Part 3. From detection models to autonomous cancer workflows

Paek used autonomous driving as an analogy for the future of medical AI.

A fully autonomous vehicle did not appear in a single step, and fully autonomous medicine will not either. The more realistic path is gradual: software takes responsibility for a growing number of bounded tasks while clinicians retain authority over the overall process.

A radiologist does much more than decide whether an image contains cancer. In breast screening, the work may include assessing image quality, estimating breast density, evaluating future risk, interpreting suspicious findings, producing a report, and recommending follow-up examinations.

A model that performs only one of these functions may be highly accurate and still represent only a small fraction of the workflow. Combining Lunit's detection technology with Volpara's density, risk, quality, and patient-management capabilities moves the system closer to supporting the complete work of a screening program.

The same logic appeared in Paek's discussion of foundation models.

Traditional supervised image classifiers are built to answer a predefined question. A model trained to detect a particular set of abnormalities usually cannot step outside that task. Supporting a new clinical request therefore requires another labeled dataset and another development cycle.

Foundation models change that development process. Rather than training each task from the beginning, a company can first train a large model on broad collections of medical images and reports, then adapt that shared representation to downstream applications.

Paek described an internal chest X-ray foundation-model project that Lunit had begun several years earlier. According to the interview, the model could respond to previously unspecified questions about abnormalities, generate radiology-style reports, and explain an image in language intended for a patient. Lunit had demonstrated some of these capabilities internally and at professional events, although Paek acknowledged that the commercialization and regulatory pathways were still unclear.

The strategic importance is not merely that one large model can perform more tasks. It is that the entire product-development process becomes more flexible. New clinical requests no longer have to begin from an empty model.

At the same time, this flexibility makes validation harder. A system capable of answering many questions also has many more ways to fail.

## Part 4. The patient is also part of the platform

Another revealing part of the interview concerned Lunit Care.

Before its spin-off, Lunit Care began as a new-business team under Paek. He gave the team a deliberately non-technical mission: create something that genuinely helps people with cancer and their families. AI did not have to be the center of the product.

The team concluded that patients often need the most help immediately after receiving a cancer diagnosis. At that moment, they must suddenly understand hospitals, physicians, treatment pathways, insurance, medical terminology, and a large volume of online information of uneven quality.

At the time of the interview, Lunit Care offered a free information service through which patients could ask questions and receive responses from physicians or nurses. It did not provide diagnoses or prescriptions. Its role was to help patients navigate trustworthy information and understand the next steps in their care.

This may appear far removed from radiology AI, but Paek presented it as part of the same long-term strategy.

Patients influence which technologies hospitals adopt. They are also central stakeholders in decisions about how their medical data may be used. A company seeking to build a sustainable cancer-data ecosystem cannot regard patients merely as the final recipients of a diagnostic result.

The larger ambition is therefore not to become a vendor of isolated AI algorithms. Paek described a future in which Lunit participates across the cancer journey: screening, diagnosis, treatment selection, pharmaceutical development, clinical workflow, and patient support.

Rather than integrating every part of healthcare, Lunit hopes to integrate the fragmented ecosystem surrounding one disease category. Cancer is broad enough to support an enormous platform, but focused enough to provide a coherent mission.

That ambition also explains the kind of people Paek said Lunit wanted to recruit. The company looks for people who are motivated by large problems and comfortable operating without an existing reference model. When the goal itself has little precedent, the organization must repeatedly decide what the next step should be rather than simply copy a known playbook.

## A researcher's takeaway

The interview suggests that medical AI has at least three nested problems.

The first is the **prediction problem**: can the model accurately detect disease or estimate treatment response?

The second is the **workflow problem**: can the prediction be delivered at the right moment, in the right interface, with enough context to help a clinician or patient act?

The third is the **system problem**: can the technology improve care while remaining sustainable, governable, and trusted across hospitals, regulators, developers, and patients?

Most academic benchmarks concentrate on the first problem. Lunit's strategy reflects the reality that clinical and commercial impact depends heavily on the other two.

But integration also increases the burden of trust. A point model can be evaluated around a relatively narrow output. A foundation model embedded in an end-to-end workflow raises much broader questions: what evidence produced the answer, whether the training and operational data are representative, how performance changes across institutions, when the system should defer, how its behavior drifts over time, and who remains responsible for the resulting action.

The closer medical AI moves from being a diagnostic tool to becoming an active participant in care, the less sufficient a single AUROC or external-validation result becomes.

The most important lesson I took from Paek's vision is therefore not simply that medical AI companies must build larger platforms. It is that **auditability must scale with capability and autonomy**. The winning system will not be the one that merely performs best on a benchmark. It will be the one that earns the right to operate inside real clinical care.

[1]: https://www.lunit.io/en/our-team/ "Our Team"
[2]: https://www.youtube.com/watch?v=vUvFfSxwArw "[통합본] 루닛 백승욱 의장님 인터뷰 | 최윤섭 박사의 디지털 헬스케어"
[3]: https://www.lunit.io/en/media-hub/volpara-now-operates-under-lunit-brand-advancing-a-unified-vision-for-ai-cancer-intelligence/ "Volpara Now Operates Under Lunit Brand"
