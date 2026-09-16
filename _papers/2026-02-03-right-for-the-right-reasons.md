---
layout: post
title: "Right for the Right Reasons: Training Differentiable Models by Constraining Their Explanations"
date: 2026-02-03 12:00:00 +0900
venue: "IJCAI 2017"
authors: "Andrew Slavin Ross, Michael C. Hughes, Finale Doshi-Velez (2017)"
description: "A clinical asthma-and-pneumonia case study opens this paper: a model that learned asthma predicts lower readmission risk, backwards from reality, because of how the training data was collected, and a method to penalize a model for explaining itself that way."
related_posts: false
---

**Paper.** *Right for the Right Reasons: Training Differentiable Models by Constraining their Explanations.*

The paper asks whether knowledge about an invalid predictive feature can change how a model is trained, rather than merely help a reader criticize it afterward. Prediction labels alone may leave several rules equally compatible with the training data. If one rule depends on an accidental correlation, more examples from the same distribution may continue to reward it. The open question is how to express additional knowledge about which dependencies should be discouraged.

The clinical example in the introduction motivates that ambiguity. Outcomes observed under a particular care process can reflect both illness and treatment decisions. A model can reproduce the observed association while supporting an inappropriate decision if its use changes the surrounding process. The example is motivation for the method, not a clinical trial showing that the proposed regularizer repairs a deployed pneumonia model.

The method adds a penalty on input gradients at features marked irrelevant for particular examples. The original objective combines classification loss, parameter regularization, and a squared penalty on the masked gradient of the sum of class log probabilities. The masks can vary by example, and annotations need not be available for every input. The authors also explore sequentially training models with different gradient explanations when expert annotations are unavailable.

A particularly clear experiment is Decoy MNIST. Training images contain a small corner patch whose intensity is related to the digit class, whereas its intensity is randomized at test time. The unconstrained network attains high training accuracy but approximately 55% test accuracy. Penalizing sensitivity in the decoy region recovers performance close to the architecture's ordinary MNIST baseline. Other experiments include constructed feature confounding and text classification.

The decoy experiment is persuasive because it separates two candidate predictive rules. The digit itself remains the intended evidence, while the added patch loses its training relationship with the label. Test performance therefore challenges whether the model learned a rule that survives that specific change. Keeping the architecture and task comparable helps make the explanation constraint's contribution interpretable.

The result licenses a conditional claim: correctly specified gradient constraints can improve generalization when the unwanted dependence is represented by the annotated features and the tested shift breaks that dependence. It does not establish that explanation supervision always outperforms additional data, nor that a small annotation budget will suffice for every medical task. The artificial decoy is unusually clear compared with many real acquisition and treatment-related signals.

The choice to penalize irrelevant gradients rather than force relevant gradients to be large is also sensible. A correct model can be locally insensitive to a relevant feature on an easy example, especially far from a decision boundary. Requiring a large derivative everywhere would impose a stronger and potentially inappropriate behavior. The method instead expresses a preference that selected inputs should not locally influence the output.

The main weakness lies in the word “locally.” A derivative describes infinitesimal sensitivity at the evaluated input. A model can have a small derivative at that point while changing substantially over a larger alteration. Saturation, nonlinear interactions, and dependencies spread over several features can complicate the relationship between the penalty and actual reliance. A low explanation loss therefore does not establish invariance to every meaningful change in the forbidden feature.

There is also a difference between shrinking one mathematical quantity and improving the intended clinical behavior. The penalty uses a particular function of the outputs. Its value depends on that choice and on input scaling. Two implementations described casually as gradient regularization may therefore impose different constraints. Reproducing the method requires specifying the differentiated quantity, mask meaning, preprocessing, and relative loss weight.

Annotation quality is a second substantive limitation. An expert may correctly identify an obvious text marker yet miss a correlated acquisition pattern elsewhere. Alternatively, a broad irrelevant-region mask may include clinically useful context. In ultrasound, posterior shadowing or enhancement can be evidence even when it lies outside a lesion contour. A rule that treats everything outside the lesion as irrelevant would need a clinical justification rather than an attractive spatial interpretation.

The unannotated search for alternative explanations is useful for a different reason. It exposes that multiple accurate solutions may exist, but it does not identify which solution is clinically correct. Diverse gradients provide candidates for inspection. They can also represent different mixtures of valid and invalid features. Selection among those candidates still needs information beyond their training accuracy and visual difference.

This paper directly supports [Clinical Alignment and Knowledge as Supervision]({{ '/study/clinical-alignment-and-knowledge-as-supervision/' | relative_url }}). It turns an expectation about evidence use into a trainable objective. The same study note places the necessary limit on that move: a clinically motivated loss changes optimization, but its name does not certify that the intended behavior has been achieved.

The connection to [Explanation Faithfulness versus Plausibility]({{ '/study/explanation-faithfulness-versus-plausibility/' | relative_url }}) is especially important after training. Once a model is explicitly optimized to produce an acceptable explanation, evaluating it only with that explanation risks circularity. [Intervention-Based Auditing]({{ '/study/intervention-based-auditing/' | relative_url }}) suggests the stronger follow-up: manipulate the suspected cue under controlled conditions and measure the frozen model's response.

For a medical application, I would compare the constrained model with an unconstrained model, a relevant ordinary-regularization baseline, and, where feasible, a baseline that removes the cue directly. I would keep annotation effort visible and evaluate both the original distribution and a prespecified change in the cue. These are proposed controls for my use of the idea, not experiments claimed for every setting in the paper.

The final audit would ask whether reliance disappeared, moved to another feature, or became harder to see with the chosen gradient measure. I would also test whether clinically useful evidence was damaged by the constraint. The paper establishes an influential and practical principle: knowledge about reasons can enter training. Its medical value depends on making that knowledge explicit and testing the resulting behavior independently.
