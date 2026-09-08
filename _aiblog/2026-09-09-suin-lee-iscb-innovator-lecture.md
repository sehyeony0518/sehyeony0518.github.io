---
layout: post
title: "AI, Biology, and Clinical Medicine: Su-In Lee’s ISCB Innovator Award Lecture"
date: 2026-09-09 12:00:00 +0900
description: "Notes on Prescience, ENABL Age, Alzheimer’s pathway models, COVID shortcuts, and CoAI, with implications for clinical faithfulness auditing."
tag: "AIMS Lab"
related_posts: false
---

Prescience’s clinician study adds a test that my own medical-image auditing work has not yet performed: whether providing model evidence improves a clinician’s judgment. In Su-In Lee’s ISCB Innovator Award lecture, that study sits alongside biological age estimation, Alzheimer’s research, image-model audits, and prediction under limited clinical resources. The breadth changes how I read the individual projects.

Lee delivered the lecture, *Explainable AI for Biomedical Sciences: Where We Are and How to Move Forward*, at ISMB 2024. These notes follow her account, with published papers used to check methods and findings. My [earlier podcast post](/blog/2026-09-08-suin-lee-explainable-ai-biology-medicine/) covers SHAP, AML drug synergy, counterfactual dermatology auditing, and MONET. Here I concentrate on the other projects and their different forms of validation. ([ISCB conference recap](https://www.iscb.org/about-iscb/society-communications/announcements/july-16-2024-ismb-2024-day-5-highlights-and-recap))

## The ABC framing connects research problems across fields

Lee describes her lab through three fields: AI, biology, and clinical medicine. AI work develops explainability principles and methods. Biology work investigates disease mechanisms and potential treatments. Clinical work develops predictions and audits systems proposed for patient care.

Her argument goes beyond applying a common toolkit to separate datasets. She expects biology and clinical medicine to converge and would like more labs to work across both. In the lecture, students and collaborators move between methodological problems, molecular measurements, and clinical decisions. Explainability supplies shared research problems, while the application determines what an adequate answer requires.

### Shared methods face different validation requirements

I find this organization useful because the projects do not all treat prediction as the final objective. In Prescience, a prediction must arrive while a clinician can still respond. In the Alzheimer’s studies, fitting expression patterns supports an investigation of disease biology. In the COVID audit, a successful classifier becomes the object of scrutiny.

These differences matter for my reading of the ABC claim. A gene attribution, a clinician’s improved risk estimate, and a controlled image modification provide different evidence. Working across these fields does not make those forms of validation interchangeable. It makes their differences harder to overlook.

The convergence Lee proposes also changes problem selection. A model can identify a promising biological target without supporting a treatment recommendation, just as a diagnostic model can achieve useful discrimination without revealing a disease mechanism. Collaboration has to establish which of those objectives the study actually pursues.

## Prescience evaluates clinicians using an explained prediction

Prescience predicts hypoxemia during anesthesia and displays the factors contributing to its risk estimate. Its real-time task concerns events within the next five minutes. In the published study, anesthesiologists improved their predictions when assisted by the system, evaluated using recorded surgical data. ([Lundberg and colleagues, 2018](https://doi.org/10.1038/s41551-018-0304-0))

Lee’s demonstration emphasizes the changing explanation over a procedure. Contributions that increase and decrease predicted risk are displayed over time, allowing the user to inspect both the trend and its attributed inputs. In her example, a decline in tidal volume contributes to rising risk. Because tidal volume is related to ventilator management, the explanation points toward information a clinician could examine.

I would keep the interpretation at that level. The display explains the fitted predictor. It does not establish the effect of changing ventilation for that patient. A potentially adjustable measurement makes the explanation clinically interesting, but does not turn attribution into an intervention recommendation.

### The user study tests an additional outcome

The paper compared five anesthesiologists’ predictions with and without Prescience assistance. For real-time prediction, pooled discrimination improved with assistance, although Prescience alone performed better than the assisted clinicians. This was a study of risk estimation using recorded cases, not a prospective demonstration that the system prevented hypoxemia. ([Study results](https://pubmed.ncbi.nlm.nih.gov/31001455/))

That design is valuable to me because it evaluates what happens after the explanation reaches its intended user. It moves beyond showing that risk factors look reasonable to experts. The clinician has to use the available information to perform a defined task, and the resulting judgment can be compared with the outcome.

The study nevertheless evaluates the assistance package: prediction and explanation together. I would not cite that comparison as isolating the benefit of the explanation itself. Establishing its incremental contribution would require a comparison with the same prediction presented without the explanatory information.

This distinction directly affects how I would describe a future audit interface. Showing that clinicians understand a display, showing that they estimate risk better with it, and showing that they choose a better action are separate results. Prescience provides evidence about the middle step. My own work has not yet established that step for clinical-faithfulness readouts.

## ENABL Age makes the output scale part of the explanation

ENABL Age estimates biological age by first predicting an age-related outcome, such as mortality, and then rescaling that prediction into age. The published framework uses UK Biobank and NHANES data and includes versions suited to laboratory measurements or questionnaire information. It adapts explanation methods to decompose the resulting age into individual contributions. ([Qiu and colleagues, 2023](https://doi.org/10.1016/S2666-7568%2823%2900189-7))

Lee uses this project to explain the practical value of additivity. Contributions can be expressed in years, so the explanation shares the scale of the displayed estimate. Instead of receiving only a ranked list of important variables, the reader can inspect how much each factor contributes to the model’s age estimate relative to its reference.

### An interpretable unit still needs a defined meaning

The conversion is a methodological step. An attribution for mortality risk does not automatically become an attribution in years simply because the display is relabeled. ENABL Age explicitly connects the risk model, the age transformation, and the explanation.

The paper also develops clocks for different mortality causes and examines their associations with genetic variation and health characteristics. These analyses support investigating what the clocks capture beyond their ability to predict mortality. ([ENABL Age paper record](https://pubmed.ncbi.nlm.nih.gov/37944549/))

For me, the useful distinction is between a comprehensible unit and a causal interpretation. A contribution expressed in years is easier to relate to the output than an arbitrary importance score. It does not mean that removing a risk factor would reverse that many years of aging, or that every clock measures the same underlying biological process.

This is relevant to medical-image auditing whenever a familiar label is attached to a numerical readout. Calling a score “wall irregularity” or “clinical alignment” can make it easier to discuss. Its interpretation still depends on the measurement procedure and the evidence connecting it to the named property.

## Alzheimer’s research uses prediction and representation to investigate biology

The first Alzheimer’s project models relationships between brain gene expression and neuropathology. MD-AD jointly predicts six neuropathological phenotypes using a neural network and accommodates samples with incomplete phenotype measurements. A sample can contribute to training through the outcomes available for it, allowing information to be shared across cohorts. ([MD-AD, Nature Communications, 2021](https://doi.org/10.1038/s41467-021-25680-7))

Lee stresses that these are postmortem tissues. The purpose is to investigate relationships between expression and pathology, rather than produce a prediction that could help the person whose tissue was sampled.

### Missing labels and nonlinear relationships shape the method

The methodological choices follow that scientific setting. Requiring every phenotype for every sample would discard usable information. Modeling related outcomes together lets the study use partially overlapping measurements, while attribution examines how gene expression contributes to the fitted relationships.

The published analysis identifies sex-specific relationships between microglial immune response and neuropathology. I would describe this as evidence for more detailed biological associations, without treating the network as having established the causal sequence leading to Alzheimer’s disease. ([MD-AD paper record](https://pubmed.ncbi.nlm.nih.gov/34508095/))

That limitation affects what should happen after model interpretation. An expression pattern in postmortem tissue can motivate an experiment, but its predictive contribution alone cannot distinguish an initiating process from a response to disease. Lee’s next project is interesting because it adds an experimental step.

### Pathway structure supports interpretation without completing it

PAUSE combines attribution with biologically structured autoencoders. The learned representation organizes expression through pathway modules, and attribution helps identify both important latent dimensions and the genes contributing to them. Because representation learning is unsupervised, it can use expression samples without requiring neuropathology labels for training. ([PAUSE, Genome Biology, 2023](https://doi.org/10.1186/s13059-023-02901-4))

I take two methodological points from this combination. First, assigning a pathway name to a module does not establish which genes dominate its learned representation. Second, an unsupervised model needs an explicit definition of importance. A dimension that helps reconstruct expression is not automatically the dimension most useful for distinguishing disease severity.

In the lecture’s discussion, Lee describes prior pathway knowledge as allowing unequal learned contributions from member genes. The published work also makes clear that pathway structure and subsequent attribution perform different jobs. The structure supplies an interpretable organization; attribution examines how the fitted model uses it. This is relevant to my interest in architectures that expose clinical concepts, where naming an intermediate variable is only the beginning of its evaluation.

### The C. elegans experiment tests the biological lead

The Alzheimer’s application highlighted mitochondrial respiratory complex I. In follow-up experiments, reducing expression of complex I genes in a transgenic C. elegans model delayed amyloid-beta-associated paralysis. The measured outcome was therefore a response to gene perturbation in a model organism. ([PAUSE experimental validation](https://link.springer.com/article/10.1186/s13059-023-02901-4))

This gives the biological interpretation evidence beyond another expression association. It supports a role for complex I in the response to amyloid-beta toxicity under the experimental conditions. It does not establish a treatment for human Alzheimer’s disease or resolve every mechanism behind the protective response.

Lee also describes single-cell work separating variation shared across cells from variation associated with treatment. I read its place in the lecture as an extension of the representation problem: dominant differences between cell types can obscure the treatment-related differences being investigated. Across these projects, the lab changes what the model represents and what the explanation targets to match the biological comparison.

## The COVID audit traces shortcuts back to data collection

The COVID chest x-ray study is the closest new material to my own research. Lee describes models that performed well within their development datasets but failed when evaluated using images from other hospitals. Their explanations drew attention to laterality markers and devices such as pacemakers, rather than consistently supporting an interpretation based on pulmonary pathology. The study is [DeGrave, Janizek, and Lee, Nature Machine Intelligence 2021](https://doi.org/10.1038/s42256-021-00338-7).

The underlying study, *AI for radiographic COVID-19 detection selects shortcuts over signal*, examines how dataset construction creates these opportunities. Combining COVID-positive images from newly collected sources with negative images from older repositories makes source identity predictive of the label. Image appearance can then reveal where a radiograph came from. ([DeGrave, Janizek, and Lee, 2021](https://doi.org/10.1038/s42256-021-00338-7))

### The marker is evidence of a collection process

I find the data history more consequential than the conspicuous marker example by itself. Laterality lettering is easy to identify as suspicious when the stated task is recognizing COVID-related pathology. The harder problem is understanding how many other visual differences encode the same source distinction.

The paper combines explanation methods with image-modification experiments and shows that external evaluation can still preserve shortcuts. A model can transfer successfully when a misleading association remains available at the new site. ([Published study](https://doi.org/10.1038/s42256-021-00338-7))

For ultrasound, this means I should investigate how examinations were acquired, selected, annotated, and exported before deciding which variation an external dataset actually challenges. A change of hospital does not necessarily change the documentation practice associated with a diagnosis. Conversely, a performance drop can also reflect differences in clinical spectrum or image quality, so source dependence needs its own evidence.

This COVID study and the dermatology audit discussed in my earlier post are the closest precedents for my clinical-faithfulness work. The former connects suspicious model behavior to data provenance; the latter uses generated comparisons and physician interpretation to characterize visual dependencies. My [MONET review](/papers/2026-08-30-monet-transparent-medical-image-ai/) covers the additional role of concept scoring. I would use these studies to define complementary audit tasks, while keeping their evidentiary limits separate.

## CoAI treats feature acquisition as part of model development

CoAI introduces a practical constraint that is easy to omit when working with an already assembled dataset: obtaining the inputs has a cost. In the lecture, Lee discusses predicting acute traumatic coagulopathy, where clinical information must be gathered under time pressure.

The framework estimates feature importance, combines it with acquisition costs, selects a feature set within a budget, and trains a predictor on that set. The published study evaluates prehospital coagulopathy prediction and mortality prediction in intensive-care and outpatient settings. ([Erion and colleagues, 2022](https://doi.org/10.1038/s41551-022-00872-8))

### Importance informs a constrained choice

For the trauma task, the paper reports that CoAI exceeded the PACT score’s discrimination with a feature-acquisition budget of 50 seconds, compared with eight minutes for PACT. These are model-development comparisons using estimated acquisition costs, not observed reductions in time to treatment from a deployment trial. ([CoAI full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC9537352/))

I find the change in objective more useful than the specific time saving. A feature’s contribution to prediction is evaluated alongside what collecting it requires. The model with access to every recorded variable is only one point of comparison.

This also limits how I would transfer the idea to ultrasound. Several features may come from one view, while acquiring another view may require repositioning, additional examination time, or expertise. Counting features equally would miss those differences.

For my auditing work, a related cost is the effort needed to obtain independent clinical annotations. CoAI does not directly solve that problem, but it encourages me to specify the budget and the intended benefit of additional information. Expanding a clinical vocabulary indefinitely could make the audit less feasible without improving its ability to identify consequential failures.

## My next evaluation needs to include the clinician’s response

My work concerns clinical faithfulness in gallbladder and hepatobiliary ultrasound classifiers. The immediate task is to examine whether model evidence aligns with independently assessed clinical findings and to test selected dependencies. The COVID and dermatology audits provide precedents for investigating misleading evidence use. They do not establish that my own readouts already identify such failures reliably.

Prescience adds a requirement beyond that technical evaluation. An audit can expose a dependency without helping a clinician recognize an incorrect prediction or choose an appropriate response. I have not yet demonstrated that an audit changes what a clinician does.

### A proposed reader study should hold the prediction fixed

A feasible next study would compare the same frozen classifier and source images under different information conditions: prediction alone, and prediction with an audit readout. An unaided condition could help distinguish the overall contribution of the model from the additional contribution of the audit. These are proposed comparisons, not completed experiments.

I would define the reader’s task before choosing the display. For an initial study, it could be identifying cases where the model’s stated evidence is unsupported and deciding whether its prediction needs further review. Outcomes would include correct identification of those cases, unnecessary rejection of useful predictions, and review time.

Confidence would be secondary. A display that makes every prediction more persuasive could increase confidence while reducing appropriate scrutiny. The study therefore needs both useful and misleading model outputs, with independent reference assessments and controls for readers seeing the same cases repeatedly.

Such a reader study would still be preliminary. Its result would concern judgment under the study conditions. Demonstrating changes in actual clinical management would require a subsequent evaluation in the intended workflow. For now, I would keep technical audit validity and clinician benefit as separate claims in my research plan.

## Lee’s closing reflection concerns research responsibility

Lee closes by describing the award as a responsibility associated with receiving a public platform. She acknowledges that many researchers deserve recognition and credits her students for the work presented.

Her advice to trainees is to evaluate research through the knowledge and capabilities it adds, rather than through publication venue alone. She connects those standards with being able to appreciate other researchers’ achievements, and advises trainees to concentrate on what they can control.
