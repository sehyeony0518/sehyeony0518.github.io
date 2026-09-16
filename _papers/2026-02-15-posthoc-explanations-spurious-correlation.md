---
layout: post
title: "Post hoc Explanations May Be Ineffective for Detecting Unknown Spurious Correlation"
date: 2026-02-15 12:00:00 +0900
venue: "ICLR 2022"
authors: "Julius Adebayo, Michael Muelly, Hal Abelson, Been Kim (2022)"
description: "A sobering stress test of the exact interpretability toolkit I lean on elsewhere in this collection (feature attribution, concept activation, and training-point ranking) against spurious signals the practitioner doesn't already know to look for."
related_posts: false
---

**Paper.** *Post hoc Explanations May Be Ineffective for Detecting Unknown Spurious Correlation.*

The paper asks whether an explanation can reveal a shortcut that its user does not already know to investigate. This is a more demanding question than asking whether a method highlights a known artifact. In many successful explanation demonstrations, the audience is effectively told what to see. That setup can establish usefulness for a specified hypothesis while leaving the promise of open-ended discovery untested.

The distinction matters for medical AI because an audit often begins without a complete list of failure mechanisms. A model might depend on an obvious annotation, but it might also exploit image processing, acquisition characteristics, or selection patterns. If a normal-looking explanation is treated as evidence that no such dependence exists, the explanation is being used as a negative diagnostic test for shortcuts. Its ability to miss them then becomes central.

The authors construct semi-synthetic tasks using hand radiographs for bone-age classification, knee radiographs, and dog-breed images. They introduce tags, stripes, or background blur and verify model dependence on these signals. They evaluate feature attribution, TCAV concept analysis, and training-point ranking through influence functions. Their measurements distinguish detection of known signals, concern about unknown signals, and false alarms.

A blinded user study provides an additional comparison: participants are assigned to conditions with or without prior information about the possible spurious signal, and explanation conditions are compared with a prediction-only control. The findings show substantial difficulty with unknown shortcuts, particularly diffuse blur. Feature attributions can also suggest dependence in models that do not rely on the artifact. These results concern the evaluated methods and conditions, not every possible explanation workflow.

The controlled contamination is a strength because the experimenter knows which signal was introduced and can check that the model uses it. In an uncontrolled clinical dataset, merely noticing an artifact in a heatmap would not establish that relationship. Here, explanation performance can be evaluated against a behavioral target rather than against the investigator's preferred visual story.

The false-alarm condition is especially valuable. Many interpretability demonstrations ask only whether the explanation finds a dependency that exists. An audit tool must also avoid confidently naming dependencies that do not exist. Otherwise, investigators can spend time removing harmless features, or infer an incorrect mechanism for a model's performance. A persuasive-looking map can be misleading through either omission or overinterpretation.

The paper also clarifies why concept methods face a discovery problem. A concept test generally needs a concept to be specified and represented by examples. If the user already knows that a particular tag might matter, the test can address that hypothesis. If the user does not know the candidate concept, producing a concept score is not itself a procedure for discovering it. The difficulty has moved into concept selection and data construction.

Training-point rankings have a related limitation. Highly ranked examples may share many properties, and the user still has to identify which commonality explains their relevance to the prediction. A set of images can suggest a useful hypothesis without uniquely identifying the dependency. This is particularly challenging when the distinguishing signal is diffuse or difficult for a person to perceive.

The result licenses skepticism toward explanations as stand-alone detectors of unknown shortcuts. It does not establish that post hoc analysis has no value. A method may be useful for comparing hypotheses, inspecting a known region, or supporting a broader debugging process. The tested discovery task is one use of explanations, and a failure on that task should not be generalized to every mathematical or practical purpose they can serve.

The strongest limitation is the controlled nature of the artifacts and tasks. Synthetic contamination creates a known target, but it does not exhaust the ways acquisition and clinical selection can influence a real dataset. Human performance can also depend on expertise, time, instructions, and the ability to request additional tests. A bounded user study cannot establish the effectiveness of every extended collaboration between a clinician and an engineer.

That limitation cuts in both directions. Real shortcuts may be easier to identify when metadata provide a clear clue, or harder when several correlated signals operate together. The experiment therefore provides counterexamples to a broad guarantee, rather than a universal estimate of shortcut-discovery sensitivity. It is enough to show that a reassuring explanation cannot, by itself, justify concluding that the model is free of problematic dependencies.

This paper complicates the optimistic use of Grad-CAM elsewhere in the corpus. A successful example of a heatmap exposing dataset bias is evidence that such discovery can happen. It is not evidence that the same method will reliably expose an arbitrary unseen dependency. The distinction between demonstrating a capability and measuring its reliability is the central lesson I would retain.

[Post-hoc Model Auditing]({{ '/study/post-hoc-model-auditing/' | relative_url }}) offers a broader structure: freeze the system, state a claim that could be wrong, and combine error review, metadata, operating-point evaluation, and targeted tests. [Explanation Faithfulness versus Plausibility]({{ '/study/explanation-faithfulness-versus-plausibility/' | relative_url }}) explains why a visually convincing account is not an adequate stopping rule. The paper supplies empirical cases where that stopping rule would fail.

[Intervention-Based Auditing]({{ '/study/intervention-based-auditing/' | relative_url }}) supplies the next step once a candidate shortcut is named. I would compare predictions before and after a justified change in the suspected signal, include control edits, and inspect whether the change also damages clinical evidence. An apparent effect of blur, for example, cannot automatically be attributed to an acquisition shortcut if the edit also removes the lesion detail needed for diagnosis.

For my own work, explanation review would be one source of hypotheses alongside scanner metadata, subgroup errors, and repeated examinations. I would evaluate the auditing procedure itself on cases with known dependencies and known nondependencies, including signals that are hard to see. Most importantly, a negative explanation review would be reported as a limited observation. The absence of a visible warning is useful only to the extent that the method has been shown capable of revealing the failure being ruled out.
