---
layout: post
title: "Transparency Is Infrastructure, Not a Safety Warranty: Ricardo Gonzales on Making Medical AI Evidence Computable"
date: 2026-07-17 12:00:00 +0900
description: Notes from Ricardo Gonzales's RISE-MICCAI talk on ROADMAP, RSNA ATLAS, machine-readable performance metrics, LLM-assisted documentation, and why transparency can expose, but not eliminate, gaps in medical AI evidence.
tag: "RSNA"
related_posts: false
---

Medical AI does not suffer from a complete absence of documentation.

Its evidence is already everywhere: in the main paper, supplementary material, code repository, dataset page, challenge website, leaderboard, model card, vendor document, or regulatory summary. The problem is that these sources describe similar things using different terms, structures, and levels of detail.

The information may be rich enough for a careful reader to reconstruct one study. It is rarely structured well enough to compare hundreds of studies reliably.

This post is based on Ricardo A. Gonzales's presentation, *Making AI Models and Datasets More Transparent*, delivered at the RISE-MICCAI Journal Club on July 11, 2026. Gonzales is a postdoctoral researcher at Harvard Medical School and Massachusetts General Hospital whose work spans trustworthy medical imaging, reproducible biomarkers, analysis tools, and reusable research infrastructure. ([MICCAI Society][1])

The talk brought together three connected components:

1. **ROADMAP**, a shared ontology for describing medical-AI models, datasets, and projects;
2. **ATLAS**, a public library in which that vocabulary becomes searchable model and dataset cards;
3. **LLM-assisted extraction**, which pre-fills those cards from published papers before human review.

Together, they attempt to move medical-AI evidence from distributed prose into structured, searchable, and reusable metadata. ([Radiology: AI][2])

The most important point, however, is also the most cautious one: structuring evidence makes missing information visible. It does not, by itself, make a model valid, fair, reproducible, or safe.

Any errors of interpretation are mine.

## Part 1. The evidence exists, but it is not computable

Gonzales begins with a question that sounds simple:

> Which published MRI models for a particular task were evaluated on an external test set, and what performance did they report?

Answering that question should not require days of manual review. Yet the relevant details may be divided across several documents.

The model architecture may appear in the methods section. The exact train–validation–test split may be hidden in a supplement. The external dataset may be described only in a challenge page. The operating threshold may be missing from the paper but present in a code repository. Regulatory status may exist in a separate public summary. Limitations may be discussed narratively without any standardized label.

Even when two papers report the same concept, they may describe it differently. One paper may say "external validation," another "independent testing," and another "evaluation at a separate institution." A human reader may understand that these expressions are related, but a database cannot safely assume that they are equivalent.

The result is a literature that is information-rich but difficult to aggregate.

Traditional search engines are good at finding documents containing particular words. They are much less reliable at answering structured questions involving several conditions at once:

* the model used MRI;
* it addressed a specific clinical task;
* the test data came from an external institution;
* the operating threshold was reported;
* subgroup performance was evaluated;
* and calibration was assessed.

The purpose of this project is therefore not to create more documentation for its own sake. It is to make the documentation that already exists computationally usable.

The shift is from **distributed documentation** to **curatable metadata**.

## Part 2. ROADMAP gives medical AI a shared language

ROADMAP stands for the **Radiology Ontology of AI Datasets, Models and Projects**.

An ontology is more than a list of recommended terms. It formally defines concepts, their relationships, their parent classes, and the values that may be assigned to them. ROADMAP expresses these relationships using the Web Ontology Language, or OWL, so that both people and machines can interpret them.

This is the essential difference between free text and computable metadata.

In an ordinary methods section, an author may describe external validation according to the conventions of a particular lab or journal. In an ontology, the corresponding field has a defined meaning and an explicit relationship to other concepts. A machine can then search it, validate it, and reason across it.

Gonzales identifies four main benefits.

First, a shared vocabulary reduces ambiguity across papers and institutions. Second, it enables semantic interoperability between heterogeneous sources. Third, its logical relationships support machine-based validation, inference, and search. Fourth, because an ontology is versioned and extensible, it can evolve without requiring every existing record to be discarded.

ROADMAP's top-level entity is divided into three major subclasses:

* **model**;
* **dataset**;
* **project**.

The three-way structure is important. Existing documentation schemes often describe either a model or a dataset. Model cards explain models, while datasheets or nutrition labels explain datasets. ROADMAP attempts to describe both within one system and adds the project level through which models, datasets, publications, regulatory information, and longer-term maintenance can be connected.

Its descriptors extend beyond architecture and benchmark performance. They include intended use, excluded or out-of-scope use, intended user, model inputs and outputs, data provenance, limitations, operating thresholds, regulatory status, sustainability, and relevant social determinants of health.

Dataset descriptors include the role of the data in development, internal versus external evaluation, patient and site counts, sampling methods, missingness, subsets, imaging modality, acquisition characteristics, annotations, and preprocessing.

This matters because real clinical risk often lies in details that are not captured by the headline performance number.

A model may have an impressive AUROC but an undocumented operating threshold. A dataset may contain thousands of images but only a small number of patients or institutions. A study may report an external test set without clearly describing how that test population differs from the development data. A product may be described as clinically useful without identifying who is expected to use it or which uses are explicitly excluded.

ROADMAP attempts to give each of these details a defined place.

At the time of publication, the ontology contained 514 classes, including 343 with definitions, 20 object properties, one data property, 717 class–subclass relationships, and 773 logical axioms. ([Radiology: AI][2])

Those numbers indicate the scale of the human curation required to build the vocabulary. They should not be treated as a permanent endpoint. The ontology continues to evolve as medical AI introduces new model types, data modalities, evaluation practices, and regulatory concerns.

That strength immediately creates a governance question: when the vocabulary changes, what exactly does a card created under an earlier version mean?

A living standard requires not only technical extensibility but also long-term maintenance, version discipline, and a clearly responsible community.

## Part 3. A standard should connect existing vocabularies, not create another island

A new standard can easily become another silo.

ROADMAP tries to avoid this by reusing terminologies that already organize clinical and imaging knowledge, including RadLex, SNOMED CT, LOINC, and RSNA content codes.

This allows a resource to be indexed using stable concepts rather than free-text words alone.

Gonzales illustrates this with the RSNA Abdominal Traumatic Injury CT dataset. The resource can be associated with the free-text keyword "trauma," but its anatomy can also be represented using the RadLex code for the liver. The clinical condition can be represented using a SNOMED CT code for blunt abdominal injury, while CT and emergency radiology can be assigned through standardized content codes.

To a human, "hepatic" and "liver" may obviously refer to the same organ. A database does not necessarily know that unless their shared meaning is explicitly encoded.

Once that semantic connection exists, a user can ask for every emergency-radiology CT resource involving the liver without predicting all the different phrases that individual authors might have used.

This is what semantic interoperability changes.

The value of the ontology is not merely that everyone is encouraged to write the same word. The value is that different descriptions can be connected to a stable concept with a defined meaning.

For medical AI, that connection is particularly important because the relevant evidence crosses multiple domains. A single resource may need to connect imaging terminology, disease concepts, laboratory measurements, model architecture, demographic attributes, evaluation design, and regulatory status.

A private vocabulary invented for one database would reproduce the fragmentation that the project is attempting to solve. Reusing existing clinical standards makes the metadata more likely to remain interpretable across institutions and systems.

## Part 4. Performance metrics need semantics too

Model and dataset descriptions are only half of the problem. Performance metrics also suffer from inconsistent terminology.

Sensitivity, recall, true-positive rate, and hit rate may refer to the same underlying quantity. A human reader can often recognize that equivalence from context. A database comparing studies may interpret them as four unrelated variables unless their relationship is explicitly represented.

The opposite problem can also occur: similarly named metrics may encode meaningfully different quantities.

Metrics also come in different forms. A confusion matrix is not the same kind of object as a scalar accuracy value. An ROC curve is not identical to the area under that curve. A Kaplan–Meier estimator cannot be stored or interpreted in the same way as a single concordance index.

ROADMAP's companion metrics taxonomy addresses this problem by defining 207 performance metrics across 18 performance criteria.

The metrics are divided into three broad forms:

* 11 graphical metrics;
* three matrix metrics;
* 193 scalar metrics.

The performance criteria include areas such as classification, calibration, image segmentation, fairness, and text analysis. This distinction matters because two models may appear strong under one criterion while behaving poorly under another.

Discrimination does not guarantee calibration. Segmentation overlap does not capture every clinically relevant boundary error. Aggregate accuracy does not establish subgroup fairness. A language model's textual similarity score does not necessarily represent factual reliability.

For each metric, the ontology can record a preferred name, alternate labels, definition, formula, numerical bounds, parent class, performance criterion, and authoritative references.

The entry for true-positive rate provides a concrete example. "True-positive rate" is stored as the preferred label, while sensitivity, recall, and TPR are retained as alternatives. Its formula is explicitly represented as TP / (TP + FN), and its valid numerical range is recorded as zero to one.

This supports more than consistent naming. A reported true-positive rate of 1.4 could be flagged automatically because it violates the defined bounds. A search for sensitivity could also retrieve studies that used the term recall. A confusion matrix could be connected to the scalar metrics derived from it rather than being stored as an isolated object.

The taxonomy does **not** decide which metric a researcher should use.

That task belongs to metric-selection frameworks and methodological guidance. ROADMAP instead describes which metrics exist, what they mean, how they relate, and what values were reported. It supplies the semantic substrate on which more consistent evaluation can be built.

This distinction is important. Standardizing the meaning of AUROC does not make AUROC sufficient for a clinical study. It simply makes it possible to determine, at scale, who reported it, what they compared it with, and which other aspects of performance were omitted.

## Part 5. ATLAS turns the ontology into public infrastructure

A vocabulary becomes useful only when people use it to describe actual resources.

The **RSNA Annotated Library of AI Systems**, or ATLAS, is where ROADMAP moves from an abstract ontology into a public repository.

An ATLAS card is a structured JSON document describing a model or dataset according to a schema derived from ROADMAP. Researchers do not need to write the JSON manually. The platform provides tools to create, edit, and validate cards.

The cards can then be indexed, searched, compared, reviewed, and accessed programmatically.

The process includes schema validation, checks of referenced resources, expert review, and ontology-based indexing. Concepts such as project name, model name, dataset name, anatomy, modality, and imaging subspecialty can therefore become searchable fields rather than phrases buried inside a paper.

A card may contain three broad families of information.

The **model** section can describe intended and excluded uses, intended users, architecture, inputs, outputs, operating threshold, limitations, and regulatory status.

The **dataset** section can document its development or evaluation role, whether it is internal or external, the population and subsets represented, sampling, missingness, patient and image counts, sites, modalities, acquisition characteristics, and preprocessing.

The **evaluation** section can connect reported results to formally defined metrics, performance criteria, formulas, bounds, and related graphical or matrix objects.

The card is not intended to replace the paper.

It is not merely a shorter summary, either. It is a structured companion that places important evidence into named fields. The paper remains necessary for methodology, argument, interpretation, and nuance. The card makes selected evidence queryable and allows missing information to be detected systematically.

This distinction protects against a common misunderstanding of structured reporting. The goal is not to reduce a complex study to a few boxes. It is to prevent essential details from becoming impossible to retrieve across studies.

ATLAS also lowers the barrier to participation because it is publicly accessible and supports card creation without requiring a proprietary platform. That openness is valuable for research groups across institutions and countries.

Yet submission remains voluntary.

A voluntary repository reflects the people, institutions, journals, and subspecialties that choose to participate. A large collection should therefore not automatically be interpreted as a representative census of medical AI.

The repository can be transparent about its contents while still being selective in its coverage.

## Part 6. LLMs reduce documentation labor, but humans remain responsible

Standards often fail because completing them is burdensome.

A schema with dozens of fields may be methodologically impressive, but few authors will manually enter every detail for every paper. The problem becomes even larger when attempting to structure decades of literature that were published before the standard existed.

The project therefore uses large language models to pre-fill ROADMAP-compatible cards.

The initial pipeline divided the task into two stages.

In the first stage, a language model summarized a scientific article using ROADMAP's field definitions and example entries. In the second, another model converted that summary into a schema-constrained model card and dataset card.

The separation was deliberate.

Understanding a scientific paper and conforming to a rigid output schema are different tasks. Asking one prompt to do both can reduce reliability. The first stage concentrates on evidence extraction; the second concentrates on structural compliance.

In an initial evaluation involving 54 articles from *Radiology: Artificial Intelligence*, researchers manually scored the extracted subfields.

Approximately 82% were correct as written. Around 16% were substantially correct but incomplete, while about 3% were incorrect. Model and dataset fields performed similarly, and extraction quality did not appear to decline with paper length.

The processing cost and time were low enough that economics were not the main barrier. The more important question was whether the generated metadata could be trusted without review.

The answer was no.

A 3% outright error rate may sound small, but an incomplete or incorrect field can alter how a model is discovered, compared, or judged. More importantly, roughly one in five extracted fields still required some human completion.

The appropriate interpretation is therefore that the LLM functions as a strong documentation assistant, not an autonomous curator.

A later comparison evaluated GPT-5, Claude, and Gemini on a smaller set of papers using dozens of model and dataset properties. GPT-5 produced the highest overall score, but the differences among the frontier models were only around two percentage points.

Gonzales interprets this result cautiously. The ranking could plausibly change with a different prompt, sample of papers, or model update. The more durable result is that pipeline engineering mattered more than selecting one apparently winning frontier model.

The two-stage decomposition, formal field definitions, constrained output schema, and human review were more important than the brand name of the model placed inside the pipeline.

The best-performing configuration was then applied to a corpus of 311 papers and public challenge resources, producing 283 model cards and 282 dataset cards.

This is the practical role of generative AI in the project.

The LLM provides scale. The ontology provides meaning. Human curators provide accountability.

None of the three is sufficient alone.

## Part 7. Once literature is structured, literature itself becomes data

The most interesting consequence of ATLAS may not be the description of one model.

It is the ability to interrogate the research literature as a dataset.

Once hundreds of papers are represented through common fields, researchers can ask questions that would otherwise require extensive manual review:

* Which modalities and clinical tasks dominate the literature?
* How often is a truly external test set used?
* Which studies report calibration in addition to discrimination?
* How frequently are subgroup results provided?
* Which patient characteristics are systematically omitted?
* How often are operating thresholds or excluded uses documented?
* Who are the intended users of the systems being developed?

The structured corpus discussed in the presentation found that AUC was the most commonly reported metric, MRI was the most prevalent modality, detection and diagnosis were the most frequent use cases, and radiologists were the most common intended users.

These findings require careful interpretation.

The corpus largely consisted of papers from a radiology-focused journal and selected public challenges. It was not a census of all medical AI. Finding many radiologist-facing models in a radiology corpus is informative about that corpus, not necessarily about the entire field.

This caveat illustrates why structured metadata still requires scientific reasoning. A query can return a precise result from an unrepresentative sample.

The more important capability may be the measurement of systematic absence.

Researchers often discuss poor demographic reporting, missing external validation, or limited calibration analysis through individual examples. Structured metadata can turn those concerns into measurable patterns.

For example, the absence of subgroup attributes across hundreds of cards can be counted. Missing descriptions of labeling procedures can be compared across tasks. The proportion of studies without external evaluation can be estimated. Fields related to social determinants of health can reveal whether the literature is actually documenting the populations for whom the systems are intended.

Missingness becomes a result.

That does not explain why the information is absent or prove that a model is inequitable. It establishes, at scale, what the published record does not allow us to evaluate.

## Part 8. Transparency is not mitigation

The strongest caution in the talk is simple:

**Reporting is not mitigation.**

A completely documented model can still be biased. A perfectly structured dataset card can accurately describe data that are unrepresentative. A model can report every required metric and still be clinically useless. A transparent system can remain unsafe.

ROADMAP and ATLAS can expose gaps, inconsistencies, and potential sources of concern. They do not enforce a valid study design, representative sampling, appropriate metric selection, external validation, or effective bias mitigation.

Completeness and quality are different properties.

A field may be filled without being supported by strong evidence. A limitation section may exist while understating the true limitation. An external dataset may be recorded even though it differs little from the development environment. A fairness metric may be reported using subgroups too small to support a reliable conclusion.

There is also a risk that standardized documentation becomes performative. Authors may complete required fields as an administrative exercise rather than using them to reconsider their study design.

That risk is not an argument against structure. It is a reason to preserve expert review and distinguish machine-checkable completeness from scientific validity.

The automation results reinforce the same point. Schema-conformant output is not necessarily accurate output. An LLM can populate every field while misunderstanding the paper. Structural correctness is therefore only one layer of quality assurance.

ROADMAP also faces the challenge of a rapidly changing field.

Its present structure was developed primarily around identifiable models, datasets, and evaluation procedures. Foundation models and agentic systems introduce additional objects that may not fit neatly into fixed fields: pretraining corpora, instruction data, retrieval sources, prompt templates, guardrails, tool access, model-provider updates, multi-step behavior, and interactions between components.

A schema that remains unchanged while the technology changes can create an illusion of completeness.

The ontology must therefore evolve, but evolution creates versioning and governance challenges. A field defined today may be revised tomorrow. Two cards produced under different versions may not be directly equivalent. Long-term transparency requires the vocabulary itself to remain traceable.

The infrastructure must document not only models and datasets, but also its own changes.

## Part 9. Adoption will determine whether the standard survives

The technical system is already operational. The harder question is whether the research community will adopt it.

During the discussion, Gonzales describes several possible routes.

Journals could incorporate structured cards into the publication process, beginning with RSNA journals and later extending to organizations such as MICCAI. Authors of accepted papers could be invited, or eventually required, to review an automatically generated card before publication.

Researchers could also upload an existing manuscript to ATLAS, allow the LLM pipeline to pre-fill its metadata, correct the result, and publish the reviewed card.

The incentive for authors is not only compliance. Structured metadata can make their work easier to discover.

A researcher looking for a model trained on a particular modality, tested externally, and evaluated with specific metrics may find an ATLAS card more efficiently than the original paper through keyword search alone. Documentation can therefore increase the visibility and reuse of a study.

Participation does not necessarily require every model or dataset to be openly downloadable.

A card can record whether the resource is open, restricted, commercially licensed, or unavailable. It can provide a location for further information and make access conditions explicit. Transparency about availability is different from unrestricted access.

The Q&A also raises the possibility of using the schema before publication.

An author could pass a draft through the ROADMAP structure and identify fields that remain unsupported or absent. The system could reveal that the intended user was never defined, the operating threshold was omitted, the test set was not clearly identified as internal or external, or subgroup information was not reported.

Used this way, the ontology becomes more than an archive. It becomes a design and reporting checklist.

It should still complement rather than replace established guidance such as CLAIM, TRIPOD-AI, and other domain-specific standards. Reporting guidelines explain what a high-quality study should report. Metric-selection tools help researchers choose appropriate evaluations. ROADMAP supplies a machine-readable structure in which that information can be represented and retrieved.

The long-term challenge is coordination.

A standard supported by only one journal, institution, or professional society may become another local convention. A sustainable system needs alignment among authors, editors, reviewers, repositories, regulators, developers, and clinical implementers.

The success of the project will therefore depend less on whether the ontology is technically elegant than on whether the community considers it worth maintaining and using.

A beautiful standard that nobody completes is still a dead standard.

## A researcher's takeaway

The talk reveals a sequence of distinctions that should remain separate:

1. **Readable evidence is not necessarily computable evidence.**
2. **Computable evidence is not necessarily complete evidence.**
3. **Complete evidence is not necessarily valid evidence.**
4. **Transparent evidence is not necessarily safe AI.**

Each layer solves a different problem.

Narrative papers remain essential because science requires explanation and interpretation. Structured metadata adds another layer by making selected claims searchable, comparable, and machine-checkable. Human review remains necessary because neither an ontology nor an LLM can determine the validity of every scientific claim automatically.

For trustworthy medical-AI research, this infrastructure suggests a broader meaning of evidence auditing.

Model-level auditing asks what evidence a trained system uses to produce its prediction. Does it rely on clinically meaningful anatomy, pathology, or temporal patterns? Does that evidence remain stable across institutions, patient groups, and acquisition environments?

ROADMAP and ATLAS operate one level above the model. They ask what evidence the research community has preserved about the model, where that evidence is located, whether different studies describe it consistently, and which information is missing.

The objects of the two audits are different, but their logic is similar.

A claim should be connected to inspectable evidence. The terms used to describe that evidence should be explicit. Missing support should not be silently interpreted as support. And a high-level conclusion should not be trusted merely because the underlying information is difficult to retrieve.

This also changes how missing reporting should be understood.

An undocumented operating threshold is not just an incomplete table entry. It may prevent reproduction of the claimed clinical performance. An unspecified test population may prevent assessment of generalizability. Missing subgroup data may make fairness impossible to examine. An absent out-of-scope statement may encourage a model to be used beyond the environment in which it was evaluated.

The missing field identifies the missing claim that cannot be audited.

At the same time, researchers should resist treating metadata infrastructure as a certification system. ROADMAP can tell us that external validation was reported. It cannot, by itself, determine whether that validation was rigorous. ATLAS can show which fairness metrics appear in a card. It cannot guarantee equitable care. An LLM can extract a limitation from a paper. It cannot ensure that the authors recognized every relevant limitation.

Transparency is therefore not the final property of a trustworthy system.

It is the infrastructure that allows stronger questions to be asked.

A medical-AI model does not become trustworthy because it has a detailed card. But without structured and traceable documentation, many of the claims required to evaluate trustworthiness remain scattered, incomparable, or invisible.

Documentation is not the end of auditing.

It is what makes auditing possible.

[1]: https://miccai.org/2026/06/30/next-rise-miccai-journal-club-july-11-2026/ "Next RISE-MICCAI Journal Club - July 11, 2026 - MICCAI Society"
[2]: https://pubs.rsna.org/doi/full/10.1148/ryai.260069 "ROADMAP: An Ontology of Medical AI Models and Datasets | Radiology: Artificial Intelligence"
