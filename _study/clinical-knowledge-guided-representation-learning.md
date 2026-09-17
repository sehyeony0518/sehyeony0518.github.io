---
layout: study_note
title: "Clinical Knowledge-Guided Representation Learning"
description: "Using echogenicity, texture, margin, wall features, and anatomical context as domain priors."
og_image: "https://sehyeony0518.github.io/assets/img/og/clinical-knowledge-guided-representation-learning.png"
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "gallbladder-ai"
category_title: "Gallbladder AI: Applied Research"
subgroup: "Task Definition & Clinical Supervision"
order: 3
source: "Independent study"
written: true
updated: "2026-09-08"
featured: true
papers:
  - "2025-11-29-concept-bottleneck-models"
  - "2026-04-02-causal-alignment-disease-diagnosis"
  - "2026-07-09-birads-net-explainable-breast-us"
---

## Core question and definition

**What clinical knowledge can reasonably shape a gallbladder representation, and what does incorporating that knowledge actually guarantee?**

A representation is the information about an input that a model makes available to later computation. Clinical knowledge can influence that information through annotation, additional prediction tasks, anatomical constraints, explicit concepts, or training preferences.

The clinical prior should describe how findings arise and under what conditions they are observable. It should not reduce the differential to an inflexible list such as “thick wall means cancer” or “comet-tail means every part of the gallbladder is benign.”

Knowledge can improve the structure of a learning problem without proving that the resulting prediction is clinically valid. The route by which knowledge enters determines the strength and limits of the claim.

## Key concepts

### Start with anatomical compartments

The gallbladder lumen, wall, and surrounding tissues are distinct compartments. A bright structure means different things depending on where it lies and how it relates to the boundaries.

Luminal material may include stones or sludge. A wall-attached projection may represent several forms of polypoid pathology or a mimic. An intramural space differs from a fluid-filled lumen and from fluid outside the organ.

An anatomical representation is useful because it preserves these relationships. “Bright focus” is an incomplete description. “Bright intraluminal focus with a related posterior shadow” specifies a more informative relationship between structure and sound propagation.

Anatomical localization remains conditional on acquisition. A partial or poorly penetrated view may not support a confident compartment assignment. A model should not be encouraged to express a complete anatomical account when the input depicts only a fragment.

### Wall architecture links mechanism to appearance

Inflammation can produce edema and alter wall thickness and echogenicity. Systemic congestion or other fluid disturbances can produce similar enlargement without primary gallbladder inflammation.

Benign remodelling in adenomyomatosis includes thickened muscle and mucosal invaginations into the wall. These intramural sinuses can contain fluid or reflective material, creating different sonographic appearances according to their contents and visibility.

Neoplastic infiltration can distort the normal tissue arrangement, producing mural thickening, a polypoid growth, or a mass. The image appearance overlaps with benign disease, particularly when only broad thickening or irregularity is depicted.

This is a many-to-many relationship: a mechanism can produce several findings, and a finding can have several causes. Clinical knowledge helps organize that relationship; it does not make it one-to-one.

### Sonographic layers are not a histology bottleneck

Ultrasound bands arise from tissue interfaces and acoustic properties under finite resolution. They do not provide a direct enumeration of microscopic wall layers.

A model trained to describe mural layering should therefore predict an imaging observation. It should not silently convert that observation into microscopic invasion depth.

A poorly resolved interface can resemble a disrupted one. A preserved visible segment does not establish that the entire wall is intact. Local appearance, whole-lesion extent, and pathological stage are distinct levels of description.

This matters for architectural constraints. A rigid requirement that every image contain a complete sequence of clean wall bands could encode an idealized drawing rather than the range of valid examinations.

### Echogenicity is relative and acquisition-dependent

Anechoic, hypoechoic, and hyperechoic describe displayed echoes, sometimes relative to another structure. They are not absolute material identities.

Brightness depends on gain, attenuation, depth, beam orientation, and processing. The liver can supply a useful anatomical reference, but background liver disease can alter that reference.

Consequently, a feature label needs to specify what is being compared and whether the comparison is technically meaningful. A dark patch could represent fluid, low-return tissue, attenuation, or a display limitation. Its location and surrounding structure determine the differential.

A representation that preserves relative relationships can be clinically sensible. A representation that treats every identical gray value as the same biological property is not.

### Texture combines tissue and image formation

Ultrasound speckle results from interference among echoes from scatterers. Apparent texture also depends on resolution, processing, compression, and the scale of observation.

True tissue heterogeneity can affect the image, but image heterogeneity does not uniquely identify heterogeneous histology. The distinction is especially important when different machines use different processing conventions.

Clinical texture terms should remain descriptions of what is observed. A claim that a texture feature identifies fibrosis, inflammation, or malignancy requires evidence beyond naming the feature.

The useful prior is that texture must be interpreted with compartment, architecture, and acquisition. It is not that texture is worthless or that all machine-dependent variation can be discarded safely.

### Margins require a named interface

“Margin irregularity” can refer to the lumen-facing surface, the lesion's attachment, the outer gallbladder boundary, or the interface with adjacent liver.

These are different observations. An irregular luminal contour does not establish extension into liver. A blurred outer boundary can reflect limited visibility or inflammation as well as tumor.

Similarly, “focal” and “diffuse” describe distribution, while “smooth” and “irregular” describe shape. Combining them into one vague abnormality label loses information about the clinical reasoning.

An adequate representation should keep the object of the description clear. The model cannot be assessed meaningfully against an annotation whose interface is unspecified.

### Acoustic effects can be useful knowledge

Posterior shadowing, enhancement, and reverberation are consequences of sound interacting with structures. They may contain information about the source even though they are not tissue boundaries themselves.

A shadow should be related to its source and beam direction. A rib shadow crossing the gallbladder differs from a shadow originating behind a luminal focus. A comet-tail appearance is more informative when linked to an appropriate intramural finding than when treated as a free-floating texture.

This creates a limit on region restriction. A tight lesion crop can remove attachment, a reference tissue, or posterior acoustics. Restricting the field of view is a modeling choice whose clinical adequacy depends on the target.

Likewise, making representations invariant to every acoustic artifact would not be a universally valid objective. Some variation changes clinically relevant evidence.

### What each supervision route buys

| Route | How clinical knowledge enters | What it can support | What it does not guarantee |
|---|---|---|---|
| Diagnostic annotation | A case or lesion receives a diagnostic target | Learning agreement with that reference | Recognition of a specified image finding |
| Feature annotation | Observable morphology receives explicit labels | Assessment and learning of those features | Completeness or correctness of the diagnosis |
| Auxiliary prediction task | Features are predicted alongside diagnosis | Pressure to make feature information available | Use of those features by the diagnostic head |
| Anatomical constraint | Computation is organized around regions or relationships | A restriction on represented structure or accessible context | Correct anatomy or adequate retained evidence |
| Concept bottleneck | Diagnosis receives explicit predicted concepts | Dependence on the supplied concept variables | That each variable has only its intended clinical meaning |
| Evidence-related regularization | Training favors specified spatial or conceptual agreement | Better agreement under the chosen objective | A faithful account of all predictive computation |

These routes are not interchangeable. A claim about one should not be inferred from success with another.

### Why an auxiliary task does not force diagnostic use

Consider an ordinary shared representation with a feature head and a diagnosis head.

The representation can contain both morphology and acquisition information. The feature head can read morphology accurately, while the diagnosis head reads a correlated acquisition pattern. Both training objectives can be satisfied even though the diagnosis does not depend on the feature information in the intended way.

This possibility follows from the available computational paths. The feature head's success shows that information is accessible to that head. It does not constrain every other head to use the same information.

Similarly, a successful probe in a representation shows decodability under the probe's conditions. Decodability is weaker than a claim that the diagnostic computation uses the probed concept.

An improvement in classification performance does not close that logical gap.

### What a concept bottleneck changes

In a strict concept bottleneck, the diagnostic component receives the predicted concepts rather than unrestricted image features. This removes a direct route from the image representation to the final prediction.

The restriction is meaningful, but its semantics need examination.

A variable called “wall irregularity” may be predicted incorrectly, may reflect acquisition quality, or may encode additional information through a continuous output. Concept variables can also have relationships that differ across populations.

A bypass containing unconstrained image features weakens the claim that the decision passes exclusively through concepts. Even without a bypass, a restricted interface is not proof that the variables correspond faithfully to clinical findings.

Finally, the chosen vocabulary may omit useful evidence. Restricting diagnosis to incomplete concepts can sacrifice information necessary to resolve a difficult differential.

### Knowledge can be descriptive, uncertain, or decision-dependent

A descriptive concept states what is depicted: an intramural space, a shadow, or a visible attachment.

An etiological concept states a cause: inflammation, benign remodelling, or invasion.

A decision concept states an action or level of concern: further characterization, surveillance, or specialist assessment.

These should not be treated as equivalent supervision. A reader may confidently describe focal thickening while remaining uncertain about cause. A management recommendation can vary with patient factors even when morphology is unchanged.

Preserving these levels lets a model express a well-supported observation without pretending that the observation settles the clinical decision.

### Missingness and uncertainty are part of the prior

Some concepts require inputs that are absent. Mobility requires temporal or positional evidence; tenderness requires examination context; vascularity requires an appropriate Doppler acquisition.

A concept system needs room for insufficient evidence. Forcing every concept into present or absent can create apparently complete but false clinical descriptions.

Uncertainty also has different sources. An image may be adequate but the finding borderline, or the finding may be unassessable because the needed interface is obscured. These situations should not be conflated.

Acquisition quality is itself clinically relevant information. It can inform the limits of an answer without becoming a surrogate disease label.

### Why familiar patterns must allow exceptions

A characteristic benign pattern can support an explanation for one region without resolving every abnormality in the examination. Stones, inflammation, benign remodelling, and neoplasia are not mutually exclusive categories in all patients.

A hard rule that one reassuring feature excludes every concerning diagnosis can therefore be clinically unsound. A prior can also become harmful when its expected feature is not visible: failure to resolve a small intramural space is not proof that no such space exists.

The appropriate use of knowledge is to structure possible explanations and their evidential requirements. It should preserve unresolved distinctions when the acquisition cannot settle them.

### Worked reasoning: thickening with an intramural finding

Consider a hypothetical examination in which a segment of thickened wall contains visible small cystic spaces and associated reverberation. Another part of the wall is poorly seen.

A clinically organized description can state that the depicted segment has findings supporting benign remodelling. It can identify which observations support that interpretation.

It cannot infer that the poorly seen segment has the same architecture. Nor can it infer that all possible disease has been excluded throughout the gallbladder.

Now consider three learning objectives.

- A diagnosis label alone encourages agreement with the final case category but does not specify the observations supporting it.
- Feature supervision adds explicit targets for the depicted morphology, provided the annotations retain the visibility limitation.
- A concept-restricted diagnosis can use those feature variables, but its conclusion remains limited by concept accuracy, missing information, and the adequacy of the concept set.

This example explains the additional structure that clinical knowledge provides without assuming a guaranteed gain in accuracy or interpretability.

### How to read evidence for a knowledge-guided model

Several claims need separate support: the features are defined meaningfully, the model predicts them adequately, the diagnostic computation has the stated access to them, and performance remains acceptable in the intended clinical population.

External performance adds evidence about transport. It does not prove that a learned representation has become invariant to every irrelevant acquisition factor.

A plausible feature display adds inspectability. It does not, by itself, make the diagnostic output clinically valid or useful.

Errors should also be interpreted by consequence. A knowledge constraint that suppresses atypical malignancy can create false reassurance; an overly broad irregularity concept can turn benign inflammation into repeated alerts. Better agreement with a feature vocabulary is not an adequate endpoint if the vocabulary misrepresents the clinical problem.

### Revision checklist

| Question | Answer to retain |
|---|---|
| What makes a useful gallbladder prior? | Anatomy, mechanism, acoustic relationships, and conditions of observability. |
| Is wall thickening a unique disease signature? | No; several mechanisms produce it. |
| Are displayed wall bands microscopic layers? | No; they are resolution-dependent acoustic appearances. |
| What reference does echogenicity need? | A defined comparison and adequate acquisition. |
| Should all acoustic artifacts be removed? | No; some carry relevant evidence about their source. |
| Does feature prediction prove diagnostic use? | No; separate heads can use different information. |
| What does a strict bottleneck restrict? | The variables available to its diagnostic component. |
| What can remain wrong in a bottleneck? | Concept semantics, accuracy, completeness, and downstream interpretation. |
| Why preserve unassessable concepts? | The input may not contain the observation needed to assign them. |
| Can a benign finding settle the whole case? | No; incomplete coverage and coexisting disease remain possible. |

## Why it matters for my work

Mechanism → canManifestAs → Finding describes why clinical concepts need anatomical and physical meaning. Clinical knowledge can shape supervision, but making concepts inspectable does not by itself establish Clinical evidence reliance. Clinical assessability limits the concept claims that an individual image can support.

## What I have not resolved

- Which concepts retain a consistent observable meaning across views and machines?
- Which parts of the clinical differential cannot be represented adequately by the chosen vocabulary?
- When does an anatomical constraint preserve useful context, and when does it remove necessary evidence?

---

Sources: General gallbladder ultrasound teaching; Bonatti and colleagues on adenomyomatosis; Feldman, Katyal, and Blackwood on US artifacts; and Koh and colleagues on concept bottleneck models. The architectural comparisons describe general learning principles, not demonstrated benefits for a particular gallbladder system. These are study notes for research purposes, not clinical guidance.
