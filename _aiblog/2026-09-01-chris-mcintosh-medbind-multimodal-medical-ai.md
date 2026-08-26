---
layout: post
title: One Patient, Many Modalities — Chris McIntosh on MEDBind and Cross-Modal Medical AI
date: 2026-09-01 12:00:00 +0900
description: How MEDBind aligns chest X-rays, ECGs, and clinical text to support multimodal prediction, few-shot learning, and cross-modal knowledge transfer.
featured: true
related_posts: false
---

A chest X-ray is not the patient. An electrocardiogram is not the patient. A clinical note is not the patient.

Each is a different observation of the same underlying person.

Most medical AI systems, however, have traditionally treated these observations as separate problems. One model reads chest X-rays. Another analyzes electrocardiograms. A language model processes clinical notes. Even when all three data types come from the same patient, their representations are often developed independently.

In a lecture on multimodal medical AI, Prof. Chris McIntosh introduced a different possibility: what if models trained on different clinical modalities could learn to represent the same patient in a shared language?

The work presented in the talk corresponds to **MEDBind**, developed by Yuan Gao, Sangwook Kim, David E. Austin, and Chris McIntosh and published at MICCAI 2024. MEDBind aligns chest X-rays, electrocardiograms, and medical text within a common embedding space, enabling information retrieval, zero- and few-shot learning, downstream outcome prediction, and even knowledge transfer from one medical modality to another. ([MICCAI][1])

McIntosh is a Senior Scientist at University Health Network's Peter Munk Cardiac Centre Research Institute and an Associate Professor at the University of Toronto, with additional appointments in Computer Science and Medical Imaging. His broader research program focuses on moving medical AI beyond isolated technical demonstrations and toward models that can operate across the heterogeneous data encountered in actual healthcare. ([Medical Biophysics][2])

## Part 1 — Medical AI has usually learned one data type at a time

The simplest form of machine learning begins with one modality.

A chest X-ray enters an image encoder. The encoder transforms the image into a vector — a compact numerical representation — and a classifier converts that representation into probabilities for several possible conditions.

The model might estimate, for example, the probability of pneumonia, cardiomegaly, edema, or another abnormality. This is the familiar single-modality setting: one type of input, one learned representation, and one predefined output task.

Recent vision-language systems expanded this idea by combining images and text. An image encoder converts a picture into visual features, while a language model processes words. A trainable projection or adapter then translates the visual representation into a form that the language component can use.

This is the basic idea behind systems that accept both an image and a written question.

McIntosh used ChatGPT as an intuitive example, but the analogy is more important than the particular product. The central problem is translation: an image model and a language model do not naturally represent information in the same numerical form. Something must connect their internal languages.

Medicine makes this challenge substantially harder because a patient is rarely described by only two modalities.

A single encounter may include a chest X-ray, an ECG, laboratory values, physiological waveforms, clinical notes, diagnostic codes, and prior examinations. Some modalities may be available for one patient but missing for another. Some may have been recorded simultaneously, while others may be separated by hours, days, or months.

The real multimodal problem is therefore not merely attaching an image to a language model. It is learning a representation in which different clinical measurements can be recognized as observations of the same underlying patient state.

## Part 2 — Binding different modalities into a shared space

MEDBind uses a separate encoder for each of its three modalities.

A Swin Transformer encodes chest X-rays. A transformer-based encoder processes 12-lead ECG signals. BioBERT represents medical text. Each encoder initially speaks its own numerical language, so the resulting features are projected and normalized into a shared 256-dimensional embedding space. ([arXiv][3])

The desired outcome is conceptually simple.

When a chest X-ray, an ECG, and a report belong to the same patient encounter, their embeddings should lie close together. Data from unrelated patients should lie farther apart.

The model should therefore learn that:

**this is the patient's chest X-ray,
this is the patient's ECG,
and this is the text describing the same clinical state.**

MEDBind uses text as its central anchor. This is a practical choice because many medical data types are already accompanied by narrative interpretations. Radiologists produce reports for X-rays, while ECG systems or clinicians generate textual interpretations of cardiac signals.

The model first aligns each non-text modality with its corresponding text through **Text-Modality Contrastive Loss**, or TMCL.

Contrastive learning brings matched pairs closer together and pushes unmatched examples apart. MEDBind modifies the conventional formulation to account for repeated clinical descriptions. Two patients may both have the report "normal ECG," for example. Treating those identical reports as unrelated negative examples would teach the model an artificial distinction, so TMCL allows matching texts to act as additional positive relationships.

Text alone, however, does not guarantee that the chest X-ray and ECG representations will be directly compatible.

Two independently trained models might both align reasonably well with text while still placing their image and signal embeddings in different regions of the representation space. MEDBind therefore adds **Edge-Modality Contrastive Loss**, or EMCL, which directly aligns chest X-rays and ECGs recorded from the same patient encounter. ([arXiv][3])

This direct connection is particularly important because not every patient has every modality.

The MIMIC datasets used in the study contained large collections of chest X-rays and ECGs, but only a subset could be linked at the patient and visit level. The researchers created a paired subset by connecting examinations belonging to the same hospital encounter or recorded within 24 hours. EMCL was designed to use these available pairs even when the number of paired chest X-rays and ECGs varied between training batches. ([arXiv][3])

The result is not simply three models placed next to each other. It is a shared coordinate system in which different clinical data types can be compared directly.

## Part 3 — Matching human-interpreted reports without reading them

One of the clearest experiments in the talk concerned 30-day hospital readmission and in-hospital mortality.

A previous text-based approach could use clinical documentation — including the written interpretations of chest X-rays and ECGs — to predict these outcomes. The text contains clinically useful information because radiologists and other clinicians have already examined the raw data and summarized what they found.

MEDBind asks whether those human-written modality reports can be replaced by representations extracted directly from the chest X-ray and ECG.

In the published experiment, the text-only model received relevant clinical text together with clinician-generated chest X-ray and ECG interpretations. The MEDBind version retained the other clinical text but replaced those modality-specific interpretations with embeddings computed directly from the raw X-ray and ECG.

For 30-day readmission, the text-only model achieved 65.0% accuracy, while the fully bound MEDBind model achieved 64.3%. For in-hospital mortality, the scores were 74.5% and 74.8%, respectively. ([arXiv][3])

At first glance, matching rather than exceeding a baseline may seem unremarkable.

But beating the text-only system was not the central point.

The text-only model depended on a clinician or reporting system first interpreting the X-ray and ECG and converting their findings into language. MEDBind recovered almost the same downstream information directly from the original modalities.

The apparent tie therefore represents a change in workflow:

**raw chest X-ray and ECG → multimodal representation → outcome prediction**

rather than:

**raw chest X-ray and ECG → human interpretation → written report → outcome prediction**

This does not mean that MEDBind replaced clinical interpretation or demonstrated readiness for autonomous care. The experiment was retrospective, still included other clinical text, and evaluated two specific prediction tasks.

It does show, however, that the shared representation preserved information that had previously required modality-specific written summaries.

## Part 4 — Zero-shot and few-shot learning reduce the need to start from zero

McIntosh then explained two terms that frequently appear in foundation-model research: **zero-shot** and **few-shot** learning.

Suppose a model has learned a shared representation for chest X-rays and text. We can embed a chest X-ray into that space and also embed written descriptions such as:

> a chest X-ray showing no acute abnormality

and:

> a chest X-ray showing pneumonia

The model can classify the image according to whichever text description lies closer to it.

No new classifier has been trained specifically for that dataset or disease distinction. The model instead uses relationships learned during pretraining. This is the basic zero-shot setting used in vision-language models.

Few-shot learning provides a small number of labeled examples — perhaps one, two, five, or several dozen — and trains only a lightweight classifier on top of the pretrained representation.

The difference is important for medicine.

Conventional supervised learning often requires thousands of labeled cases. That is possible for common conditions at large institutions, but it is far less realistic for rare diseases, uncommon phenotypes, or narrowly defined patient populations.

A useful pretrained representation changes the starting point. Researchers no longer need to teach the model the entire structure of medical images or ECG signals from a small disease-specific cohort. They only need enough examples to define the new task within an already meaningful space.

In the MEDBind experiments, the frozen encoders were tested in zero-shot settings and with 1, 2, 4, 8, and 16 labeled examples. The bound version consistently improved over the version without direct X-ray–ECG binding and remained competitive across both chest X-ray and ECG tasks. ([arXiv][3])

Zero-shot should not be interpreted as learning without prior data.

The model had already undergone extensive multimodal pretraining. "Zero" refers to the absence of task-specific supervised training for the new classification problem, not to an absence of prior knowledge.

## Part 5 — Can one modality borrow a disease concept from another?

The most striking part of the lecture was the cross-modal zero-shot experiment.

Some cardiac findings are conventionally associated more strongly with one modality than another. Hypertrophy is commonly assessed using ECG-related information, while cardiomegaly is commonly evaluated on chest X-rays.

Because MEDBind places both modalities in the same representation space, the researchers asked whether a disease concept defined through one modality could be recognized in the other.

For the first experiment, chest X-rays were used as queries, but the labeled support examples came from ECGs. The model attempted to identify hypertrophy from the chest X-ray by locating it relative to ECG examples representing hypertrophy and other findings.

MEDBind achieved **82.1% balanced accuracy**.

The direction was then reversed. ECGs were used as queries, while the support examples were chest X-rays labeled for cardiomegaly. MEDBind achieved **84.6% balanced accuracy**. In both directions, the directly bound model substantially outperformed combinations of independently trained chest X-ray and ECG encoders. ([arXiv][3])

These experiments do not mean that an X-ray has somehow become an ECG, or that an ECG now contains every detail visible in an X-ray.

The more plausible interpretation is that both modalities contain partially overlapping manifestations of an underlying cardiac state. By aligning them at the patient level, MEDBind learns enough common structure to transfer a disease concept across modalities.

There is also a technical nuance in the term "cross-modal zero-shot."

The model did receive labeled support examples, but those labels were supplied in the other modality. It was "zero-shot" with respect to task-specific training on the query modality. The chest X-ray encoder, for example, was not explicitly trained on chest X-ray hypertrophy labels for this experiment.

This is what makes the result interesting: supervision collected for one clinical measurement may become useful for another.

## Part 6 — The value lies in the relationships between data types

Multimodal learning is often described as a way to increase prediction accuracy by adding more inputs.

That is only one possible benefit.

MEDBind suggests that the relationships between modalities may be as valuable as the modalities themselves.

A shared representation can support retrieval: given one patient's chest X-ray, the system can search for related ECGs or reports.

It can support flexible prediction: when several modalities are available, their representations can be passed to a downstream model together.

It can support low-data adaptation: a disease concept learned from a limited number of labeled examples may be transferred through the pretrained space.

Most importantly, it may allow one modality to act as supervision for another.

This matters because clinical labels are not distributed evenly. Some findings are easy to annotate in one modality but difficult or expensive to acquire in another. Echocardiograms, pathology slides, genomic tests, and specialist interpretations each provide forms of supervision that are valuable but not universally available.

A sufficiently coherent multimodal space could allow accessible modalities to inherit useful knowledge from more expensive ones.

At the end of the talk, McIntosh offered a practical rule of thumb for potential collaborators. For a modality already represented by the system, a preliminary study might be possible with roughly 200 patients and 50 outcome events. Adding an entirely new modality would still require thousands of examples.

These numbers should be understood as collaboration heuristics rather than universal sample-size requirements. The necessary cohort size depends on prevalence, task difficulty, label quality, desired confidence, and the degree of distribution shift.

The broader message is nevertheless clear: multimodal pretraining can reduce the amount of new supervision required, but it does not eliminate the need for representative data.

## Part 7 — Binding modalities also creates new questions of trust

A shared embedding space is powerful precisely because it compresses many kinds of information into a common representation.

That compression is also where the risk lies.

If a chest X-ray and ECG from the same encounter are pulled together, what exactly causes the alignment?

Ideally, the common representation reflects clinically meaningful patient state: cardiac size, ventricular stress, pulmonary congestion, rhythm abnormalities, or other physiological relationships.

But the model could also exploit less meaningful connections. Examinations from the same hospital visit may share institutional workflows, patient demographics, acquisition timing, device characteristics, reporting conventions, or patterns of clinical selection.

A model can therefore learn that two records belong together without necessarily learning the biological reason they belong together.

This makes multimodal alignment an auditing problem as much as a representation-learning problem.

We need to know whether the model transfers disease evidence or merely transfers context.

We also need to examine what happens when modalities disagree. A chest X-ray may appear normal while the ECG is abnormal. One measurement may be technically poor. The examinations may reflect different moments in a rapidly changing clinical course.

A trustworthy multimodal system should not force every modality into artificial agreement. In some cases, disagreement is itself the clinically meaningful signal.

This creates several important evaluation questions. Does the shared representation generalize across hospitals and devices? Does performance remain stable when one modality is missing? Can the model recognize patients unlike those seen during pretraining? Is cross-modal prediction calibrated? Which features are actually responsible for the transferred concept?

One promising extension would be to use multimodal consistency as an audit mechanism. When the X-ray, ECG, and clinical text support compatible conclusions, confidence may increase. When their representations strongly conflict, the system could defer or request additional review.

In this way, multimodality need not only make a model more capable. It could also provide multiple forms of evidence with which to challenge the model's conclusion.

## A researcher's takeaway

The most important idea in this lecture was not simply that three modalities outperform one.

It was that different medical measurements can be treated as different views of a shared patient state.

MEDBind moves from isolated modality-specific models toward a system in which chest X-rays, ECGs, and text can exchange information. The near-equivalence between raw-modality embeddings and clinician-written modality reports shows that this shared space can preserve useful downstream information. The cross-modal experiments go further, suggesting that supervision acquired in one modality may help define a task in another.

For rare diseases and limited clinical datasets, that possibility is particularly compelling.

But a unified representation is not automatically a clinically meaningful one.

As medical AI begins to transfer concepts across modalities, we must audit not only whether the prediction is correct but also what has been transferred. Is it disease biology, patient context, institutional workflow, or an acquisition shortcut?

That distinction will determine whether multimodal medical AI generalizes beyond the dataset in which its modalities were bound.

The next generation of medical AI will not merely read images, signals, and notes separately. It will connect them.

The trustworthy version will also know when those connections should not be trusted.

[1]: https://papers.miccai.org/miccai-2024/497-Paper2333.html "MEDBind: Unifying Language and Multimodal Medical Data Embeddings"
[2]: https://medbio.utoronto.ca/faculty/mcintosh "Chris McIntosh - Medical Biophysics - University of Toronto"
[3]: https://arxiv.org/html/2403.12894v2 "MEDBind: Unifying Language and Multimodal Medical Data Embeddings"
