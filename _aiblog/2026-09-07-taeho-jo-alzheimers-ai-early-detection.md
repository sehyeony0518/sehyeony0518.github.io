---
layout: post
title: "Before Symptoms Appear: Taeho Jo on Using AI to Find Earlier Signals of Alzheimer's Disease"
date: 2026-09-07 12:00:00 +0900
tag: "Indiana University"
description: "Notes from Prof. Taeho Jo on using AI across tau PET, whole-genome sequencing, metabolomics, rare variants, and uncertainty estimation to search for earlier and more trustworthy signals of Alzheimer's disease."
related_posts: false
---

Alzheimer's disease creates an unusual challenge for artificial intelligence.

By the time dementia becomes clinically obvious, much of the biological process that produced it has already been unfolding for years. A model that recognizes advanced disease accurately may therefore solve an easier computational problem while arriving too late to address the more important medical one.

The harder question is:

> Can we detect the biological signals of Alzheimer's disease before severe cognitive symptoms appear?

This post is based on an interview with Prof. Taeho Jo, an Assistant Professor in the Department of Radiology and Imaging Sciences at Indiana University School of Medicine. His research develops AI and deep-learning methods for Alzheimer's disease using neuroimaging, whole-genome sequencing, metabolomics, proteomics, and other large-scale biomedical data.

What I found most interesting was not one particular architecture.

It was the progression of questions.

Can deep learning recognize Alzheimer's disease from brain images?

If it can, what part of the brain is it using?

If brain imaging already captures relatively advanced biological changes, can we move earlier and examine the genome?

If the genome is too large to analyze conventionally, can AI scan it differently?

Can the same idea be extended to blood-based metabolic signals?

And even if the model becomes accurate, how do we know when its prediction should be trusted?

The technology changes from project to project.

The deeper research program remains the same: use AI not merely to classify disease, but to search through biological information that is too large and complex for a human researcher to inspect exhaustively.

## Part 1. Alzheimer's detection is a problem of timing

Alzheimer's disease and dementia are related but not identical concepts.

Alzheimer's disease is a biological disease process. Dementia describes the cognitive and functional impairment that can eventually result from that process.

This distinction matters because the clinically visible symptoms occur relatively late.

If the research goal is simply to distinguish patients with established Alzheimer's dementia from healthy controls, neuroimaging already contains substantial information. But early detection requires moving upstream toward signals that exist before severe cognitive decline.

Jo's research therefore spans several layers of biological information:

$$
\text{genome}
\rightarrow
\text{molecular changes}
\rightarrow
\text{brain pathology}
\rightarrow
\text{cognitive symptoms}.
$$

Each layer offers a different trade-off.

Brain imaging provides rich information about what is happening inside the brain, but imaging is relatively expensive and may often be obtained after a clinical concern has already emerged.

Blood-based metabolomic or proteomic markers may be easier to collect repeatedly.

Genetic information exists from birth and therefore provides an even earlier window into inherited risk, although Alzheimer's genetics is highly complex and genetic susceptibility is not equivalent to a future diagnosis.

The objective is not to find one magical data source.

It is to identify which combinations of biological signals can reveal risk or disease progression early enough to become useful.

## Part 2. First, can AI see Alzheimer's pathology in the brain?

One of Jo's earlier projects applied deep learning to tau PET imaging.

Tau is a protein strongly associated with Alzheimer's pathology. Its abnormal accumulation follows characteristic spatial patterns as the disease progresses.

A conventional analysis can compare tau deposition statistically across predefined brain regions.

Deep learning offers another possibility.

Instead of telling the algorithm in advance which anatomical regions should matter, researchers can give the model a three-dimensional PET image and ask it to distinguish Alzheimer's disease from cognitively normal controls.

A 3D convolutional neural network can learn directly from the spatial image.

But classification accuracy creates another question:

> What did the model actually use to make the decision?

This is where Jo's group added Layer-wise Relevance Propagation, or LRP.

After the classifier produced a prediction, LRP traced the decision backward through the network to estimate which regions of the image contributed most strongly to that output.

The resulting relevance maps highlighted areas including the hippocampus, parahippocampus, thalamus, fusiform region, and temporal structures.

Importantly, these regions overlapped substantially with established patterns of Alzheimer's-related tau pathology.

This makes the result more interesting than a high classification score alone.

If a model performs well but focuses on irrelevant image borders, scanner artifacts, or acquisition-specific features, its accuracy may reveal very little about Alzheimer's biology.

If its influential regions correspond to known disease processes, the model becomes more useful as a scientific probe.

It can potentially do two things at once:

$$
\text{predict disease}
+
\text{suggest where informative biological signal exists}.
$$

That second role is particularly important for biomedical discovery.

## Part 3. Interpretability can turn prediction into a research hypothesis

Explainability is often discussed as a way to reassure clinicians.

Jo's imaging work suggests another use.

An explanation can generate a biological hypothesis.

Suppose a deep-learning model repeatedly highlights a particular region when identifying Alzheimer's disease. There are then at least two possibilities.

The region may already be known to be involved in the disease. In that case, the model provides a form of consistency check: it appears to have rediscovered information already supported by neuroscience.

More interestingly, the model may consistently highlight a region that has received less attention.

That does not establish a new biomarker.

A saliency or relevance map is not biological proof. It can be affected by model architecture, preprocessing, correlated regions, and the explanation algorithm itself.

But it can identify a candidate worth studying.

The workflow becomes:

$$
\text{AI pattern}
\rightarrow
\text{candidate region}
\rightarrow
\text{statistical and biological validation}
\rightarrow
\text{possible new hypothesis}.
$$

This is a different conception of medical AI from automated diagnosis.

The model is not replacing the scientist.

It is narrowing a search space that would otherwise be extremely difficult to inspect.

## Part 4. But brain imaging may already be too late

A highly accurate imaging model still leaves a fundamental problem.

When clear pathological changes are visible in the brain, the disease process may already be well underway.

Jo therefore asks a more upstream question:

> If we want to move earlier, why not look at the genome?

Genetic information has an obvious temporal advantage.

It is present long before the first symptom.

The difficulty is scale.

Human genomic data contain enormous numbers of variants. Whole-genome sequencing can contain millions of positions for a single individual. With conventional statistical approaches, researchers often test associations between individual variants and a phenotype such as Alzheimer's disease.

Genome-wide association studies have been extraordinarily valuable, including the identification and characterization of well-known Alzheimer's risk regions such as APOE.

But conventional variant-by-variant testing does not naturally capture every nonlinear interaction or local relationship among neighboring variants.

Deep learning offers another question:

> Can the genome itself be treated as structured input rather than as millions of isolated statistical tests?

## Part 5. Turning the genome into something an AI can scan

One of Jo's approaches is SWAT-CNN: the Sliding Window Association Test combined with convolutional neural networks.

The intuition is easier to understand if we imagine an enormous chromosome as a very long document.

Reading every possible interaction in the entire document simultaneously is computationally difficult.

Instead, the algorithm examines manageable local sections.

Conceptually:

$$
\text{whole genome}
\rightarrow
\text{candidate regions}
\rightarrow
\text{overlapping windows}
\rightarrow
\text{variant influence}
\rightarrow
\text{disease-associated loci}.
$$

The method first divides the genome into regions and identifies portions containing potentially useful signals.

A sliding window then moves across selected regions, allowing the model to evaluate a variant together with its local neighborhood rather than always considering each position in complete isolation.

The system calculates a phenotype influence score for variants and uses the resulting candidates for Alzheimer's classification.

When applied to Alzheimer's data, the method identified the well-established APOE region as its strongest genetic locus.

That result is important for the same reason that known tau regions matter in the imaging study.

A method claiming to discover Alzheimer's genetic signals should first be able to rediscover something biology already knows.

Only after that does a newly highlighted region become especially interesting.

## Part 6. From fixed variants to genetic context

The next conceptual step is to stop treating neighboring genetic variants as completely independent units.

Variants located near one another can be inherited together.

This phenomenon is captured by linkage disequilibrium, or LD.

Instead of dividing an enormous genome using an arbitrary number of positions, LD-informed approaches can use biologically meaningful genomic blocks.

The analogy to modern language models is useful, although imperfect.

A language model does not interpret a document as one indivisible object. It divides information into manageable units and learns relationships among them.

Similarly, a genomic model requires a representation through which millions of variants can be organized into units that preserve useful context.

Jo's later work uses LD-informed blocks and transformer-based architectures to model these relationships over much larger genomic regions.

The significance is not that a genome literally behaves like human language.

It is that both problems involve large structured sequences in which local context and interactions matter.

This changes the question from:

> Which single variant is associated with Alzheimer's disease?

toward:

> Which patterns of variants, local relationships, and genomic regions collectively contain information about Alzheimer's risk?

That is a much harder problem, but it is also closer to the biological complexity of the disease.

## Part 7. AI as a genome-scale research assistant

During the interview, Jo uses the emerging language of AI agents to describe the intuition behind this work.

Imagine assigning a narrow task to a computational agent:

> Move across this enormous genomic space. Examine each local region. Compare it with its neighbors. Flag patterns that deserve further investigation.

A human researcher cannot manually inspect millions of combinations around the clock.

A machine can.

This does not mean that the AI independently discovers the cause of Alzheimer's disease.

A statistical or model-derived signal still has a long path before becoming accepted biology.

It must survive:

- replication;
- multiple-testing concerns;
- population differences;
- functional interpretation;
- biological experiments;
- and comparison with existing genetic knowledge.

The model accelerates candidate discovery.

It does not remove the burden of scientific validation.

That distinction is crucial throughout Jo's work.

AI can make the search broader.

Science still determines whether what it finds is real.

## Part 8. From the genome to the blood

Genomic data provide early information, but whole-genome sequencing remains expensive and analytically demanding.

That leads naturally to another question:

> Can related computational ideas be applied to biomarkers that are easier to obtain?

Metabolomics measures small molecules generated through the body's metabolic processes.

Unlike a genome arranged naturally along chromosomes, metabolomic variables do not come with the same simple linear order.

A traditional sliding window therefore cannot simply move from the beginning of a chromosome to the end.

Jo and collaborators developed Circular-SWAT to address this problem.

The basic idea is to reorganize the features so that a window can repeatedly circulate through them and examine local combinations from different positions.

The metaphor used in the interview is a Korean children's game in which an object is passed around a circle.

Instead of a window reaching the end of a linear table and stopping, it continues around the feature space.

This allows an AI model to examine metabolic variables in overlapping contexts and search for combinations associated with Alzheimer's disease.

Again, the broader pattern of the research is visible.

A useful computational idea is not tied permanently to one modality.

The sliding-window principle begins in genomics and is adapted when the structure of the next biological dataset changes.

The algorithm follows the scientific question rather than forcing every dataset into exactly the same architecture.

## Part 9. Common variants may not explain every patient

Most large genetic association studies naturally concentrate on variants that occur often enough to support statistical analysis.

But Alzheimer's disease is heterogeneous.

Two people can arrive at a similar clinical phenotype through partly different biological pathways.

This creates another question:

> What if important information exists in rare variants that appear in only a small number of individuals?

Rare variants are difficult precisely because they are rare.

A weak signal from a small group can disappear among millions of genomic comparisons.

Recent work from Jo's group therefore extends the search toward rare variants and AI-based prediction of their possible regulatory effects.

The goal here should be interpreted carefully.

Finding an unusual variant in a patient does not establish that the variant caused Alzheimer's disease.

Computational tools can prioritize variants that appear biologically consequential or are enriched in particular groups.

Those candidates still need independent validation.

AI again functions as a filter across an otherwise overwhelming search space.

It tells researchers where closer inspection may be worthwhile.

## Part 10. These are discovery tools, not personal Alzheimer's fortune tellers

At this point, it would be easy to misunderstand the research.

If a neural network can analyze a genome, a PET image, or a blood metabolomic profile, can an individual simply submit their data and receive an answer about whether they will develop dementia?

Not from these studies.

Jo explicitly distinguishes research-oriented prediction and biomarker discovery from a clinically validated individual diagnostic service.

A genomic classifier can demonstrate that a dataset contains disease-associated information without being sufficiently accurate, calibrated, externally validated, or clinically actionable for individual prediction.

A candidate genetic locus can improve our understanding of Alzheimer's biology without being ready for genetic counseling.

A metabolomic pattern can motivate future biomarker studies without functioning as a clinical blood test.

This distinction is essential because AI makes prototype prediction deceptively easy.

Producing a probability is technically straightforward.

Establishing what that probability means for a real patient is a much more demanding scientific and clinical problem.

The research pipeline is closer to:

$$
\text{large biomedical data}
\rightarrow
\text{AI-discovered pattern}
\rightarrow
\text{replication}
\rightarrow
\text{biological interpretation}
\rightarrow
\text{clinical validation}
\rightarrow
\text{possible future clinical use}.
$$

Most interesting academic discoveries are still somewhere in the middle of that chain.

## Part 11. From accurate AI to trustworthy AI

The later part of the interview introduces perhaps the most important shift in Jo's current research.

Suppose two patients receive the same predicted probability of Alzheimer's disease.

Should a clinician trust both predictions equally?

Not necessarily.

One patient may resemble cases the model has seen repeatedly. Another may sit near an ambiguous region of the learned decision boundary. A single probability can hide that difference.

This motivates uncertainty-aware AI.

Instead of asking only

> What does the model predict?

the system also asks

> How stable is that prediction?

Jo's recent work uses methods such as Monte Carlo dropout.

Dropout is normally used during training by randomly suppressing parts of a neural network. With Monte Carlo dropout, this stochastic process remains active during inference.

The same patient is evaluated repeatedly.

If the predictions remain very similar, the model exhibits relatively low predictive variance.

If they fluctuate substantially, the case can be flagged as uncertain.

Conceptually:

$$
x
\rightarrow
\begin{cases}
p_1(y\mid x) \\
p_2(y\mid x) \\
\vdots \\
p_T(y\mid x)
\end{cases}
\rightarrow
\text{prediction}
+
\text{uncertainty}.
$$

This enables selective prediction.

Rather than forcing the AI to make an equally authoritative decision for every patient, uncertain cases can be deferred for additional human review.

That is a very different philosophy from conventional automation.

The goal is not:

> AI should classify every case.

It is:

> AI should know which cases it can classify more reliably and which cases deserve additional scrutiny.

## Part 12. Confidence can improve a human–AI system without improving every prediction

Recent work from Jo's group illustrates the idea with tau PET.

A model can produce predictions for all cases and achieve one overall level of accuracy.

If the system identifies its most uncertain cases and sends those cases for additional review, accuracy among the automatically retained cases can increase substantially.

This should not be misread as free performance.

The model has not suddenly learned to classify every patient better.

It has changed the operating policy.

Instead of demanding 100% automation coverage, the system exchanges coverage for reliability:

$$
\text{greater automation}
\quad\leftrightarrow\quad
\text{greater certainty on retained cases}.
$$

This is often called selective prediction or a reject option.

The clinically meaningful question becomes:

> At what uncertainty threshold should the machine defer?

A useful evaluation therefore needs more than ordinary AUROC or accuracy.

It should examine:

- calibration;
- accuracy at different coverage levels;
- risk–coverage curves;
- the kinds of patients being deferred;
- subgroup differences in deferral;
- and what happens after the human receives the case.

An uncertainty estimator becomes clinically useful only when it changes the decision pathway appropriately.

## Part 13. Uncertainty is not the same as knowing that the model is right

There is an important limit to this idea.

A confident model can still be wrong.

If the training dataset contains a stable shortcut, the model may repeatedly exploit it with extremely high confidence.

For example, imagine that a particular scanner, hospital, or acquisition protocol is strongly correlated with Alzheimer's cases in the training data.

The model could learn that correlation.

Repeated stochastic predictions may all agree.

Its uncertainty would be low.

Its reasoning could still be clinically inappropriate.

This creates a distinction between two questions.

Uncertainty asks:

> How stable is the model's belief?

Clinical evidence auditing asks:

> What evidence produced that belief?

A trustworthy system ultimately needs both.

The ideal situation is not merely

$$
\text{high confidence},
$$

but something closer to

$$
\text{high confidence}
+
\text{clinically meaningful evidence}
+
\text{external stability}.
$$

A model should know when it is uncertain.

Researchers should still investigate what it is certain about.

## Part 14. The common thread is not an architecture but a question

One of the strongest ideas in the interview appears when Jo reflects on the sequence of his research.

Each project began with a question.

Why does the image classifier think this patient has Alzheimer's disease?

Can we move earlier than brain imaging?

Can a deep-learning model scan a whole genome?

How can a sliding-window idea work when the data are not arranged linearly?

Could rare variants contain information missed by common-variant studies?

How can a model communicate when its own prediction is unreliable?

Different questions produced different tools.

$$
\text{question}
\rightarrow
\text{method}
\rightarrow
\text{experiment}
\rightarrow
\text{result}
\rightarrow
\text{new question}.
$$

This is a useful correction to the current conversation around AI.

The competitive advantage of a researcher is becoming less about merely knowing how to call the newest model.

Powerful architectures are increasingly accessible.

What remains difficult is identifying a scientifically meaningful question, defining the right data representation, designing a credible experiment, and determining whether the result answers the original question.

AI can search enormous spaces.

Someone still has to decide which space is worth searching.

## Part 15. AI has not replaced radiologists; it has changed what they can do

The interview ends by returning to a prediction that has followed medical AI for a decade.

In 2016, Geoffrey Hinton famously suggested that training radiologists would soon become unnecessary because deep learning would transform image interpretation.

A decade later, radiologists have not disappeared.

The opposite problem is increasingly visible: healthcare systems have more imaging, more elderly patients, more data, and more work than clinicians can manually process.

AI is entering that environment primarily as an amplifier.

It can:

- prioritize examinations;
- automate repetitive measurements;
- summarize records;
- search enormous datasets;
- flag unusual cases;
- and reduce time spent on routine documentation.

The strongest deployments are often not those that remove a physician from the system.

They are those that allow one clinician to process more information without giving up the parts of medicine that require expert judgment.

This pattern also changes across countries.

In a well-resourced hospital, AI may assist a specialist who already exists.

In a region with severe physician shortages, the same technology may provide a capability that was previously unavailable altogether.

In neither case is the practical question simply:

> Will AI replace the doctor?

A better question is:

> Which bottleneck in care can AI reduce, and which decisions should remain under human responsibility?

## Part 16. Technical capability alone does not determine what gets used

Jo also points to a practical reality visible across American hospitals.

The AI systems adopted most rapidly are not necessarily the ones performing the most intellectually impressive diagnostic tasks.

Tools that reduce administrative burden can have an immediate economic and workflow benefit.

Ambient documentation systems, for example, can convert a clinician–patient conversation into a structured clinical note. The value proposition is straightforward: less time typing means more time available for patients and potentially more clinical capacity.

A fully autonomous diagnostic system faces a more difficult path.

It needs strong validation, regulatory authorization, reimbursement, workflow integration, liability rules, and clinician trust.

A technically impressive algorithm therefore does not automatically become a widely used medical product.

The observation connects this interview with a recurring theme across medical AI:

$$
\text{technical performance}
\neq
\text{clinical adoption}.
$$

Deployment is shaped by safety, workflow, economics, regulation, reimbursement, and the availability of someone who can act on the output.

## Part 17. Access may become as important as capability

The discussion also moves beyond high-income academic hospitals.

A large fraction of the world's population still has limited access not only to AI but to physicians, reliable internet, computing infrastructure, and digital health systems.

That changes the replacement debate.

Where there are already highly trained specialists, AI may primarily augment them.

Where specialists are absent, AI may help provide a basic level of screening, triage, education, or decision support that was previously unavailable.

But this possibility creates another layer of responsibility.

Deploying a model in a lower-resource environment requires asking whether:

- the target population was represented during development;
- the necessary hardware exists;
- connectivity is reliable;
- outputs can be understood locally;
- there is a pathway for referral;
- and the system remains useful when specialist confirmation is difficult.

An AI model does not democratize healthcare merely because its software can be copied.

Access requires an entire delivery system.

## A researcher's takeaway

What stands out from Jo's work is the movement across levels of evidence.

The research begins with visible disease patterns in the brain.

It then moves backward toward inherited genomic risk.

It expands sideways toward metabolomics and rare variants.

And finally it adds another dimension: uncertainty about the model's own conclusion.

The progression can be summarized as:

$$
\text{What does the model predict?}
$$

$$
\downarrow
$$

$$
\text{What evidence did it use?}
$$

$$
\downarrow
$$

$$
\text{Can we find that evidence earlier?}
$$

$$
\downarrow
$$

$$
\text{Can AI discover signals humans cannot search exhaustively?}
$$

$$
\downarrow
$$

$$
\text{How much should we trust each prediction?}
$$

For trustworthy medical AI, each of these questions matters.

High accuracy without understanding the source of the prediction can conceal shortcuts.

Interpretability without external validation can provide a plausible explanation for a model that does not generalize.

Genetic association without biological validation can turn correlation into an overstated mechanism.

Uncertainty estimation without calibration can create confidence scores whose clinical meaning is unclear.

And even a technically excellent system can fail if there is no viable workflow in which its output changes care.

The most compelling direction is therefore not one universal Alzheimer's model.

It is a layered evidence system in which genomics provides inherited risk, blood biomarkers provide accessible molecular information, imaging reveals in-vivo brain pathology, and uncertainty tells us when the machine itself requires help.

Eventually, those sources may be integrated:

$$
\text{genomics}
+
\text{multi-omics}
+
\text{neuroimaging}
+
\text{clinical history}
\rightarrow
\text{individualized risk and progression modeling}.
$$

But multimodal scale alone will not make that system trustworthy.

The final model will still need to answer three different questions:

1. Is the prediction accurate?
2. Is the evidence clinically meaningful?
3. Does the system know when those two conditions may not hold?

The interview also offers a broader lesson about research with AI.

AI is extraordinarily good at searching spaces too large for a person to inspect: millions of genomic variants, thousands of imaging features, years of longitudinal biomarkers, or enormous collections of scientific observations.

But the machine does not decide which unexplained phenomenon is worth pursuing.

That begins with a researcher asking a good question.

In that sense, the most interesting part of Jo's work is not that AI provides answers about Alzheimer's disease.

It is that each answer creates a better next question.

And for a disease whose earliest biological changes may begin years before dementia becomes visible, asking the next question earlier may be exactly what matters.
