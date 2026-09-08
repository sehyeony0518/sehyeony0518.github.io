---
layout: study_note
title: "Clinical Knowledge-Guided Representation Learning"
description: "Using echogenicity, texture, margin, wall features, and anatomical context as domain priors."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "hepatobiliary"
category_title: "Hepatobiliary Medicine & Imaging"
subgroup: "Clinical-to-AI Connections"
order: 17
source: "Independent study"
written: true
updated: "2026-09-08"
featured: true
papers:
  - "2025-11-29-concept-bottleneck-models"
---

Clinical knowledge-guided representation learning uses domain knowledge to influence what a model encodes. In gallbladder ultrasound, the relevant knowledge concerns tissue appearance, acoustic behavior, wall architecture, and the anatomical relationships that make a finding interpretable.

## Clinical overview

Clinicians do not interpret echogenicity, texture, or margin in isolation. A bright focus within the lumen, within the wall, or outside the gallbladder creates different possibilities. I understand a useful domain prior as a constraint or preference grounded in these relationships, rather than a list of appearances that must always predict one diagnosis.

The clinical vocabulary also has limits. A finding may be subtle, incompletely visible, or dependent on acquisition. Knowledge-guided learning should therefore preserve the possibility that the available image does not support a confident feature assignment. Encoding certainty where the examination is uncertain would misrepresent the clinical evidence.

## Anatomy and pathophysiology

The gallbladder lumen contains bile, while its wall and surrounding tissues provide distinct anatomical compartments. Luminal stones and sludge, intramural changes, and solid mural lesions differ partly through their relationship to those compartments. Adjacent liver supplies context, but its appearance can itself change with background disease and acquisition.

Adenomyomatosis provides a concrete link between structure and appearance: intramural Rokitansky-Aschoff sinuses may contain fluid or reflective material and produce characteristic findings. [Bonatti and colleagues](https://doi.org/10.1007/s13244-017-0544-7) describe these relationships. I take this as support for learning where a feature occurs and what accompanies it, rather than treating a comet-tail artifact anywhere in the image as equivalent evidence.

## Diagnostic workflow and imaging findings

### Interpret echogenicity relative to a reference

Anechoic, hypoechoic, and hyperechoic describe appearance under an acquisition and, where relevant, relative to another structure. A dark lesion and a fluid lumen are not interchangeable findings. Gain and attenuation influence displayed brightness, so comparison should use appropriate nearby tissue and suitable settings. I would preserve that reference explicitly when turning a clinical term into an annotation or computational target.

### Separate tissue texture from image formation

Speckle, resolution, compression, and postprocessing influence apparent texture. Heterogeneous tissue may contain genuine internal differences, but a heterogeneous image need not imply heterogeneous pathology. The artifact mechanisms described by [Feldman and colleagues](https://doi.org/10.1148/rg.294085199) help explain this limitation. A texture description becomes more persuasive when it persists across adequate views and is interpreted alongside the lesion's structure.

### Define margin and wall architecture

Margin assessment should identify the relevant interface: lumen to lesion, lesion to wall, or gallbladder to adjacent liver. Smoothness, attachment, focal versus diffuse thickening, and preservation of layering describe different properties. A clearly depicted segment should not stand in for an obscured circumference. I would also distinguish apparent boundary disruption from an established claim of invasion, which may require additional imaging or pathology.

### Keep posterior acoustics and anatomical context

Shadowing, enhancement, and comet-tail artifacts contribute information about acoustic interactions. Their spatial relationship to the suspected source matters. A shadow behind a luminal focus differs from one cast by a rib overlying the region. The gallbladder neck, lumen, wall, and adjacent tissues should remain distinguishable across views. Cropping tightly around a lesion may remove the context needed to interpret its attachment or posterior effect.

## Differential diagnosis and management context

Benign remodeling, inflammation, and malignancy can share wall thickening or heterogeneous appearance. A characteristic combination can support a diagnosis, but the absence of one expected feature does not automatically exclude it. Further characterization is appropriate when the unresolved distinction changes management. I regard clinical knowledge as a way to organize evidence and uncertainty, not as an infallible rulebook for every image.

## Implications for medical AI

My proposed approach would combine anatomical localization with supervision for observable features, while retaining relevant surrounding tissue. Domain knowledge could guide region selection, feature losses, or which paired images should have similar representations. For example, two adequate views of the same lesion may support consistency in its clinical description, but they need not have identical pixels or reveal identical features. I would test these choices against an otherwise comparable model on held-out patients and acquisition settings.

A concept bottleneck, as studied by [Koh and colleagues](https://proceedings.mlr.press/v119/koh20a.html), offers one way to route prediction through explicit features. Other approaches merely encourage a representation to contain them. That distinction matters: feature decodability does not establish diagnostic reliance. For my clinical faithfulness work, I would assess feature recognition, robustness, and reliance separately, including cases where a familiar benign pattern coexists with a suspicious lesion. A prior that suppresses such exceptions could make a model more interpretable while making its clinical reasoning less adequate.

## References

- Bonatti et al., [Gallbladder adenomyomatosis: imaging findings, tricks and pitfalls](https://doi.org/10.1007/s13244-017-0544-7), Insights into Imaging 2017.
- Feldman, Katyal, and Blackwood, [US Artifacts](https://doi.org/10.1148/rg.294085199), RadioGraphics 2009.
- Koh et al., [Concept Bottleneck Models](https://proceedings.mlr.press/v119/koh20a.html), ICML 2020.
