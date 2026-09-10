---
layout: post
title: "Priscilla Chan on the Virtual Cell, Open Datasets, and Patients Who Build the Assets"
date: 2026-09-12 12:00:00 +0900
description: "Notes on why the constraint in cell modelling moved from compute to data format, how an annotation tool accumulated a corpus mostly contributed by others, and what rare-disease groups bring beyond motivation."
tag: "Biohub"
related_posts: false
---

Two years ago the question was whether the models were powerful enough and whether there was enough compute. Priscilla Chan says the key constraint now is data — specifically that most biological data sits in proprietary sets, shaped around the question someone originally went in to answer.

This is the same programme as [my earlier notes on the No Priors episode](/blog/2026-09-11-biohub-virtual-biology-world-models/), approached from what has to exist before a model can usefully be trained.

## The constraint moved from compute to format

There is good data in biology — single cell, spatial, protein. But it is usually proprietary, and usually configured for a specific question, which Chan calls reasonable rather than culpable. What the field lacks, in her account, is foundational datasets that are open, standardised, and available to everyone.

She grounds this in something that happened by accident. CELLxGENE began as an annotation tool rather than a large dataset, built because annotating single-cell data was hard. Because researchers were all using the same tool, they produced the same data format, the data began to compound, and people started giving their data back. CZI paid for and seeded the original data; about three quarters of what is in it now is not something CZI put into the world itself. The [platform paper](https://doi.org/10.1093/nar/gkae1142) (*Nucleic Acids Research*) describes what it became.

The lesson she draws is that no single group builds these datasets, and that standardisation is what makes one useful to everyone else. The stated next step is a **billion cell project**, deliberately spanning species, ancestry, age and disease state, and she is clear the hard part is not the cell count. The techniques exist. The difficulty is getting multiple parties willing to use the same data format.

The earlier work she cites is the Human Cell Atlas and [Tabula Sapiens](https://doi.org/10.1126/science.abl4896) (*Science*, 2022) — a Tabula Sapiens Consortium reference atlas of nearly 500,000 cells across 24 tissues and organs, which Chan describes as built at Stanford.

## What a virtual cell is for

There is no consensus definition, and Chan says so before giving CZI's: a computational model of the biology powering the human cell, one that lets you look at cause and effect quickly and cheaply — disease states, perturbations, how particular genes produce changes that may later cause disease.

The purpose she gives it is de-risking. Basic science currently runs on a clever idea, happy accidents, years of dedicated trial and error. A model that lets a scientist test many ideas — especially riskier ones — and take only the highest-yield few to the bench changes what it costs to be wrong.

Her stated holy grail is a model of an *individual's* biology: given three unusual variants, trace which protein is affected downstream and what process that protein is integral to, then look at risk profile, at treatment, and at predicted natural history for a condition that currently has no name — only a constellation of symptoms and some genes of unknown effect. She sets this against the diagnostic journey as it is, where a whole genome yields three unusual findings and no risk group to put the patient in.

Euan Ashley, interviewing, adds the dimensions that make this hard, and Chan does not soften them: perturbation rather than a quiescent cell, spatial arrangement rather than soup, and time — cells are usually stopped or killed to be measured. Their imaging response is to push toward video rather than static slides, and toward label-free methods for living cells. Chan credits investment in a laser phase plate, in partnership with a Berkeley group, with improving their contrast and resolution, and says they can see a mutation change a protein's conformation. The [2019 paper](https://doi.org/10.1038/s41592-019-0552-2) (*Nature Methods*) demonstrated laser-based phase contrast in transmission electron microscopy; the rest is her account of what it has since enabled.

## Patients bring assets, not only motivation

CZI began seed-funding rare-disease advocacy groups in 2019. Chan says her imagination had not been open to what they would do — she expected patient support and awareness. What happened instead: fifty groups, about twenty thousand researchers now plugged into their research agendas, and the groups converting funding into research programmes for their own disease.

Her word for why the science moved fast is **assets**: disease models, hundreds of cell lines, clinical registries, biobanks, natural history studies. Things without which, she says, the research would not happen — and once they exist, anyone with basic-science skills can contribute.

Her example is a group working on FOXG1 syndrome, a rare neurodevelopmental disorder — [characterised longitudinally in 101 children and adults](https://doi.org/10.1186/s11689-025-09653-1) (*Journal of Neurodevelopmental Disorders*, 2025). Chan says the group received FDA approval for a gene-therapy clinical study, and that the mother who founded it had promised her daughter a study by the time the child was ten; approval came on Amara's tenth birthday.

Ashley's contrast is the sharper one. Reviewers ask where the actionability is in a diagnosis. Rare-disease parents never ask that: the diagnosis ends being on an island and begins a community, and that is where the mission starts.

## Reading cells rather than only looking at them

The New York Biohub work is cellular engineering, described as a platform rather than a product: send a cell to a specific destination, have it read out a state, encode that reading back into its own DNA, then lyse itself so the cell-free DNA can be drawn and sequenced.

Chan's example is coronary plaque burden — inject cells, later draw blood, read what they recorded. She calls it science fiction herself and names the open questions: the inflammation such a thing would trigger, and whether the readout has fidelity. The step she wants after reading is action. They see themselves building a general-purpose technique and depending on physician-scientists to say what it should be used for.

## What I take from this

**Standardisation let contributions accumulate past the seed.** CZI paid for the original CELLxGENE data, and most of what sits there now arrived from elsewhere, because a tool people wanted to use imposed a format. For auditing medical models the useful version is a proposal, not a conclusion: an annotation tool with a shared schema might make independently reviewed findings, matched outcomes and acquisition conditions easier to collect and reuse than commissioning the dataset would.

**Configured-for-one-question is a limit worth testing for downstream.** Chan's objection is that proprietary data was shaped around its collector's question. Whether that propagates into a model — whether collection and evaluation choices preserve a shortcut that lets a diagnostic model perform without relying on clinically valid evidence — is my hypothesis to test, not something her argument establishes.

**De-risking has a direction.** A virtual cell that filters hypotheses before the bench saves effort depending on *which* hypotheses it wrongly rejects. I would want to know whether it systematically filters out promising ideas that lie outside its training experience. The audit I work on has an analogous exposure: it clears what it was designed to test and is silent on the failure mode nobody thought of.

**The infrastructure argument transfers, with a caveat.** Researchers attached themselves to rare-disease agendas where registries, cell lines and natural history studies already existed. Evidence auditing needs its own version — but the distinction that matters is between what clinical work already records and the additional annotation, linkage and validation an audit requires. Assembling that is a research task in itself, and I do not yet have an organised way to do it.
