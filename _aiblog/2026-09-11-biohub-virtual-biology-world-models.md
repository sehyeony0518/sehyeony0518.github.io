---
layout: post
title: "Biohub on Frontier Biology, Emergent Protein Design, and Reading a Model's Representations"
date: 2026-09-11 14:00:00 +0900
description: "Notes on why biology's bottleneck is data that does not exist yet, what it means that protein design arrived without antibody-specific model development, and the argument that interpretability could yield biological knowledge."
tag: "No Priors"
related_posts: false
---

The usual argument for interpretability is defensive: open the model so you can trust it. Alexander Rives, on this episode with Mark Zuckerberg and Priscilla Chan, makes a second argument alongside it. Protein language models are trained on sequences whose biology is largely unknown, and the representations they build nonetheless link proteins nobody understands to proteins that are well characterised. If that structure can be read, interpretability could yield biological knowledge and not only reassurance.

## The bottleneck is data that does not exist yet

Language models had an internet; biology does not. Datasets exist from decades of academic work, but much of what these models need has never been recorded — which is why the effort funds imaging to see things not previously visible, cellular engineering to record what happens inside the body, and instruments in Chicago to measure inflammation.

Zuckerberg's phrase for this is *frontier biology* coupled to *frontier AI*: there is no factory that sells the data, so the methods that produce it have to be invented. He notes these models are smaller than language models, and that the reason is the amount of data, not the ambition.

The consequence is structural. Because the wet lab and the model are run as one effort, experiments can be chosen for what they bridge — transcriptomics located within a cell, translucent zebrafish watched through development, sensors for cell-to-cell communication — so that there is connective tissue between the layers being modelled.

### Building upward rather than modelling everything at once

The stated approach goes proteins, then cells, then systems. Zuckerberg's reasoning is that you cannot understand how cells work without the protein interactions underneath, nor the immune system without cells; a high level of abstraction might simulate a system, but hierarchical simulation is what he argues gives a basis for understanding how it works.

Asked what a virtual cell takes in and returns, Rives describes a requirement rather than a product: model the proteomic, genetic and transcriptomic layers, connect them to phenotype, and carry enough generality to answer a question about an intervention in a context never trained on. Generalisation of that kind is the gap he names for the field, and closing it needs an enormous data effort.

## Design arrived without antibody-specific development

The concrete result is the new ESM release. Rives reports predicting structures for over 1.1 billion proteins, with features connecting them identified through mechanistic interpretability.

His emphasis is not the count. They did not build a model for antibodies, or to bind a particular target; they built one to understand proteins, and protein design came out as an emergent property of searching the space of that model. The design procedure itself was deliberate: hundreds of thousands of computational trajectories, roughly ninety-six candidates selected and synthesised in a single well plate, and nanomolar binders — which Rives describes as the level for therapeutic activity.

The lineage: [ESMFold](https://doi.org/10.1126/science.ade2574) (*Science*, 2023) showed that scaling a protein language model to 15 billion parameters made an atomic-resolution picture of structure emerge in the learned representations, without the multiple sequence alignments [AlphaFold](https://doi.org/10.1038/s41586-021-03819-2) used; [ESM3](https://doi.org/10.1126/science.ads0018) (*Science*, 2025) extended that to generation. Rives is senior author on both. The 1.1 billion figure and the binder results are from the talk, not from those papers.

Chan adds the confirmation step: designed proteins for several therapeutically relevant targets were characterised in their structural biology centre with cryo-EM, so binding interfaces could be seen at atomic resolution.

## Interpretability that could return knowledge

Rives describes applying mechanistic interpretability — developed to ask what a language model's representation space contains and how it computes — to protein language models.

The setup differs from the language case. A model trained on billions of protein sequences has been trained on both known and unknown biology, and anything it learns about structure and function is emergent from token prediction. When its representations turn out to correspond to the reductive picture of biology built up over centuries, that gives a link: an underlying structure or grammar in representation space connecting proteins we know nothing about to proteins we do.

A host suggests this might eventually reveal systems in the body we did not understand, or a treatment's mechanism of action, by interrogating the representation. Rives agrees, and states it as a hope — to learn the underlying basis for how the model makes its predictions, and so see the biology it is representing.

Chan's version of the same move is toxicity. Off-target effects often surface only in humans: a kidney cell also expressed the receptor, and renal toxicity appears in trial. With a single-cell atlas covering cell types — some not predicted before they were modelled — you can ask which cells carry receptors for the target you believed you were hitting, before the trial rather than during it. She grounds this in a lineage the organisation built: funding methods for single-cell sequencing, then the [Human Cell Atlas](https://doi.org/10.7554/eLife.27041), then CELLxGENE as an annotation tool, around which a community accumulated a corpus that transcriptomic models are now trained on.

## Why open, and what that buys

The nonprofit choice is argued from reach. Zuckerberg says it is not clear they could not run it as a business, and that the reason not to is getting the tools into more hands faster. He is explicit that curing diseases is not the theory; accelerating the whole field is.

Chan's argument is the long tail. Under common headings — heart disease, cancer, neurodegeneration — sit many subcategories, and past those, rare diseases that get orphaned when effort is allocated by expected impact. Decentralising the tools means the person who cares about spinal muscular atrophy can make progress on it, and understanding that disease may in turn reveal something general.

Both point to patient-organised research: registries, natural history registries, biobanks and trials assembled by patient groups themselves. Chan recalls one disease group moving a gene therapy forward over roughly three to five years rather than decades, and is careful that this is a recollection.

Separately, she cites baby KJ as an example of choosing an application where delivery was tractable: the [CHOP team's patient-specific CRISPR therapeutic](https://doi.org/10.1056/NEJMoa2504747) (*NEJM*, 2025) targeted liver cells, and the disease was selected on that basis. Zuckerberg's qualification is worth keeping: enabling people who want to be at the frontier does not mean the general population should get less vetting than it has had.

## What I take from this

**A capability that arrives without being built for is a reason to ask what supports it.** They built a model to understand proteins and got protein design out of it — no antibody-specific development, though the search itself was deliberate. For my work this raises a related question: when a model succeeds beyond the objective it was trained on, what evidence supports that success? In imaging the same question has a sharper edge, because accuracy can arrive from a cue the task never intended.

**Decodability is not reliance, and the two need different evidence.** Rives's claim is that the representation links unknown proteins to characterised ones. That is a claim about what the representation contains. Whether a prediction depends on that content is separate, and a linear probe cannot settle it — a distinction I keep returning to. Their laboratory work tests whether the designs behave as predicted; it does not by itself establish which representations the model relied on. Establishing reliance needs a test that changes the proposed evidence and measures what the prediction does.

**The off-target argument is a limited analogy to an evidence audit.** Chan proposes checking, before the trial, which cell types carry the receptor the drug is meant to hit. Both that and auditing a diagnostic model look for failure modes before deployment, but one examines where a drug may act biologically and the other examines what a prediction depends on. They do share a failure mode: the atlas can only speak to cell types it covers, exactly as an audit can only rule out shortcuts it thought to test.

**Data you cannot buy is the constraint, and it recurs downward.** These models are smaller than language models because the data had to be invented. In my auditing work the missing resource is often a dataset linking independently annotated findings, matched outcomes and acquisition metadata — the evidence needed to check what a model is using is not a by-product of clinical work. Assembling it is itself a substantial research task.
