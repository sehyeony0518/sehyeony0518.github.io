---
layout: study_note
title: "Perception as Inference: Illusions Are Not Failures, and the Easy Problems Were the Hard Ones"
description: "Why the retinal image cannot determine what you see, why walking took a billion years and calculus took a hundred thousand, and where the functional definition of AI runs out."
tab: "ai-foundations"
tab_title: "AI Foundations"
category: "learning-principles"
category_title: "Learning Principles"
order: 16
source: "Independent study"
written: true
updated: "2026-09-15"
---

Eyes evolved independently at least seven times. That is not a curiosity — it is a measure of how useful vision is, and of how hard the problem it solves must be that evolution kept re-solving it: trilobites with calcite lenses, the four-eyed *Anableps*, the pinhole camera of the nautilus.

## Core question and definition

The problem vision solves is worth stating precisely, because it is **not** the one it appears to solve.

What reaches the retina at a point is illumination multiplied by surface reflectance. You observe the product. From a single number you are asked to recover one of two factors, and **there is no answer** — red light on a white surface and white light on a red surface are the same measurement. The same holds for depth: a 2-D projection does not determine a 3-D scene.

So the visual system is not a light meter. It is an **inference engine**, committing to the most plausible interpretation under a prior about how the world tends to be. And it is not optional: an animal that reported "the 3-D structure is not determined by my input" would be eaten by something whose visual system guessed.

This reframes illusions entirely. The dress that some people see as white-and-gold and others as blue-and-black is not a malfunction — it is two observers applying different priors about the illuminant, **both reasoning correctly** from insufficient data. The checker-shadow illusion, where two patches of identical pixel value look obviously different, is the visual system correctly inferring that a patch in shadow must have higher reflectance to produce the same measurement.

Illusions are not where perception fails. They are where the prior becomes visible — and the fact that it is normally invisible is the measure of how well it usually works.[^land]

## Key concepts

### Moravec's paradox

Which is harder: computing a comet's perihelion, or recognising a face?

Early AI researchers had a clear answer, and were wrong by a margin that reorganised the field. Orbital mechanics is a few hundred lines. Face recognition, walking across a room, understanding a spoken sentence — these were assigned to graduate students as summer projects and remained unsolved for fifty years, while the moon landing happened in the middle of that span.

The explanation is evolutionary timekeeping. Sensorimotor skill has been under optimisation for roughly a billion years, under selection pressure that kills you for being slow. Abstract symbolic reasoning has perhaps a hundred thousand. **We find calculus hard and seeing easy because seeing has been optimised a ten-thousand-fold longer**, not because seeing is simpler — the subjective difficulty ordering is exactly inverted from the computational one.[^moravec]

The DARPA Robotics Challenge footage is the demonstration: machines falling over doorways, defeated by a task any toddler manages. That looks like comedy and is better read as data.

And the paradox has a corollary about intelligence itself. A bee hovers in gusting wind with two million neurons. Crows bend hooks into tools and teach the technique to crows in other places. Chimpanzees beat humans at rapid numeric-sequence recall. Restricting "intelligence" to what school examinations measure discards most of it, and most of what we would most like to build.

### The functional definition, and what it buys

Artificial flavouring is judged by whether it tastes right. Nobody asks whether it was synthesised the way a plant does it.

The dominant working definition of AI is the same: **the only question is what the system can do.** Not whether it thinks like a human, not how it was built. Turing made this behavioural criterion explicit — the test replaces "can machines think" with a question that can actually be adjudicated.[^turing]

The definition is deliberately permissive about method, and that permissiveness is what made the field's history possible. An expert system that classifies with hand-written rules is AI under it. So is a linear classifier separating salmon from sea bass by width and brightness — which, written out, is a weighted sum passed through a nonlinearity, i.e. a neuron. That single unit can only draw a straight line, which is why XOR defeats it, which is why layers, which is why depth. The whole architectural history follows from asking what the previous thing could not represent.

## Why it matters for my work

Two things, and the second is the one I keep returning to.

**First: a model's errors are its priors made visible.** If perception is inference under a prior, then the analogue of an illusion is not a bug report — it is the most informative output the system produces. A [shortcut](/study/shortcut-learning-in-medical-imaging/) is precisely a prior that holds on the training distribution and is wrong off it, and it is invisible exactly while it is working. This argues for treating characteristic failures as the primary object of study rather than as residue to be minimised: the cases where a model is confidently wrong tell you what it assumed, and nothing else does.

It also sets a limit worth being honest about. The inverse problem is underdetermined for a model in the same way it is for an eye. An ultrasound image does not determine the tissue; a radiograph does not determine the pathology. **A model that appears well calibrated is not one that escaped the ambiguity — it is one whose prior happens to match the test distribution**, and that is a statement about the test set, not about the model.

**Second, and sharper: the functional definition is exactly what trustworthy AI declines to accept.** "Only what it does matters, never how" is a fine criterion for flavouring and an unacceptable one for a system that participates in a diagnosis. The whole case for [faithful explanation](/study/explanation-faithfulness-versus-plausibility/), for auditability, for [interpretable models in high-stakes settings](/study/auditable-by-design-medical-ai/), is a rejection of it — the argument that mechanism is part of the claim, not an implementation detail behind it.[^rudin]

That tension does not resolve cleanly, and I would rather hold it than paper over it. The functional definition is how the field escaped decades of arguing about whether machines really think, and it is the reason there is anything to audit. It is also the reason the thing that got built is opaque, because nothing in the definition ever asked for anything else. Reliability research is the bill arriving for a simplification that was genuinely productive — which is a different and more uncomfortable thing than a mistake.

---

[^land]: Land, E. H., & McCann, J. J. (1971). Lightness and retinex theory. *Journal of the Optical Society of America*, 61(1), 1–11. [10.1364/JOSA.61.000001](https://doi.org/10.1364/JOSA.61.000001)

[^moravec]: Moravec, H. (1988). *Mind Children: The Future of Robot and Human Intelligence*. Harvard University Press.

[^turing]: Turing, A. M. (1950). Computing machinery and intelligence. *Mind*, LIX(236), 433–460. [10.1093/mind/LIX.236.433](https://doi.org/10.1093/mind/LIX.236.433)

[^rudin]: Rudin, C. (2019). Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nature Machine Intelligence*, 1, 206–215. [10.1038/s42256-019-0048-x](https://doi.org/10.1038/s42256-019-0048-x)
