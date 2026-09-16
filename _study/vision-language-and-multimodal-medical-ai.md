---
layout: study_note
title: "Vision-Language and Multimodal Medical AI"
description: "Image-text alignment, report grounding, and the failure modes of models that read images and language together."
tab: "trustworthy-ai"
tab_title: "Trustworthy AI"
category: "systems"
category_title: "Medical AI Systems & Deployment"
order: 2
source: "Independent study"
written: true
updated: "2026-09-08"
papers:
  - "2026-07-15-clear-auditable-foundation-model-radiology"
  - "2026-08-30-monet-transparent-medical-image-ai"
---

An image-report pair supplies correspondence between two observations produced during a clinical process. It does not automatically supply a complete diagnosis label, a localization for every sentence, or proof that a generated statement is supported by the current image.

## Core question and definition

The central question is:

> What information does each modality provide, what does the training objective supervise, and what evidence supports each output claim?

Vision-language and multimodal systems can perform several distinct tasks:

| Task | Output | Main evaluation question |
|---|---|---|
| Retrieval | A ranked image or text candidate list | Are relevant items retrieved under the candidate-set definition? |
| Classification | A label or probability | Is the clinical target predicted validly? |
| Localization | A region linked to a finding or phrase | Does the region support the specified claim? |
| Multimodal fusion | A prediction using several inputs | What does each input contribute at the intended time? |
| Report generation | A sequence of clinical statements | Are statements supported, complete enough, and appropriately qualified? |

Success on one task does not establish success on another.

## Key concepts

### 1. A report is produced from more than the supplied image

Let:

- $$I$$ be the image supplied to the model.
- $$V$$ be other views or prior examinations.
- $$C$$ be clinical context.
- $$S$$ be reporting style and workflow.
- $$R$$ be the report.

The observed report distribution can be written as

$$
P(R\mid I)
=
\int
P(R\mid I,V,C,S)
\,dP(V,C,S\mid I).
$$

A model trained only on $$I,R$$ sees the marginal result of those additional variables.

The report may include:

- Findings visible in another view.
- Clinical history or referral information.
- Comparisons with prior examinations.
- Negative statements selected for the clinical question.
- Uncertainty and alternative interpretations.
- Recommendations based on more than image appearance.
- Template language or copied text.

Therefore, predicting the report from one image does not mean every predicted sentence is visually supported by that image.

### 2. Derive why a report mention is an indirect label

Let $$D=1$$ indicate that a finding is present, and $$M=1$$ indicate that the report affirmatively mentions it.

Define

$$
\eta(I)=\Pr(D=1\mid I),
$$

$$
u(I)=\Pr(M=1\mid D=1,I),
$$

$$
v(I)=\Pr(M=1\mid D=0,I).
$$

By total probability,

$$
\begin{aligned}
\Pr(M=1\mid I)
&=u(I)\eta(I)+v(I)[1-\eta(I)]\\
&=\boxed{v(I)+[u(I)-v(I)]\eta(I)}.
\end{aligned}
$$

A mention predictor estimates this reporting probability. It equals the finding probability only under additional conditions.

The mechanisms include omission, false mention, uncertainty parsing, and access to information beyond the supplied image.

### 3. A constructed omission example

Construct 100 images:

- The finding is present in 80.
- Reports mention it in 40 of those 80.
- Reports never falsely mention it in the remaining 20.

| Finding status | Mentioned | Not mentioned | Total |
|---|---:|---:|---:|
| Present | 40 | 40 | 80 |
| Absent | 0 | 20 | 20 |
| Total | 40 | 60 | 100 |

The finding prevalence is

$$
\frac{80}{100}=\frac45.
$$

The mention frequency is

$$
\frac{40}{100}=\frac25.
$$

Among reports without a mention,

$$
\Pr(D=1\mid M=0)
=
\frac{40}{60}
=
\frac23.
$$

Coding every unmentioned finding as absent would label many present findings negative in this construction.

The example does not claim a clinical omission rate. It shows why “not mentioned,” “explicitly absent,” “uncertain,” and “not assessable” need separate treatment.

### 4. Derive the image-text matching objective

Let image and text encoders produce normalized vectors

$$
u_i=\frac{\phi(I_i)}{\|\phi(I_i)\|},
\qquad
v_j=\frac{\psi(R_j)}{\|\psi(R_j)\|}.
$$

For temperature $$\tau>0$$, define similarity logits

$$
s_{ij}=\frac{u_i^\top v_j}{\tau}.
$$

In a batch of paired observations, a common training task asks which report belongs to image $$i$$:

$$
q(j\mid I_i,\{R_k\})
=
\frac{e^{s_{ij}}}{\sum_ke^{s_{ik}}}.
$$

If the recorded match is report $$i$$, its loss is

$$
\begin{aligned}
L_i^{I\to R}
&=-\log q(i\mid I_i,\{R_k\})\\
&=\boxed{-s_{ii}+\log\sum_ke^{s_{ik}}}.
\end{aligned}
$$

A reverse loss asks which image belongs to a report. Averaging the two directions creates a bidirectional objective, as used for paired medical image-text representation learning in ConVIRT. [Contrastive Learning of Medical Visual Representations from Paired Images and Text](https://proceedings.mlr.press/v182/zhang22a.html).

Differentiate the image-to-report loss with respect to one logit:

$$
\boxed{
\frac{\partial L_i}{\partial s_{ij}}
=
q(j\mid I_i,\{R_k\})-\mathbf1\{j=i\}.
}
$$

The objective increases the matched score relative to candidate alternatives. The supervised event is pair identity under the sampling scheme.

### 5. Derive the correspondence learned under an ideal negative-sampling model

Suppose one candidate report is drawn from $$p(R\mid I)$$ and the other candidates are independently drawn from the report marginal $$p(R)$$. Let the matched index $$J$$ be uniformly selected.

Conditional on $$J=j$$, the candidate likelihood is proportional to

$$
p(R_j\mid I)\prod_{k\neq j}p(R_k).
$$

Factor out the product over all candidates:

$$
p(R_j\mid I)\prod_{k\neq j}p(R_k)
=
\frac{p(R_j\mid I)}{p(R_j)}
\prod_kp(R_k).
$$

The common product cancels when normalizing over $$j$$. Therefore,

$$
\boxed{
\Pr(J=j\mid I,R_{1:N})
=
\frac{p(R_j\mid I)/p(R_j)}
{\sum_kp(R_k\mid I)/p(R_k)}.
}
$$

Under this idealized sampling model, the optimal matching score represents an image-report density ratio.

That ratio concerns how strongly the image changes the plausibility of a report relative to its background frequency. It is not automatically a disease probability.

Different negative-sampling procedures change the comparison distribution and therefore the matching task.

### 6. A model can solve retrieval through a nonclinical cue

Construct two image-report pairs:

- Pair 1 shares acquisition or template cue A.
- Pair 2 shares cue B.
- The clinical finding is the same in both pairs.

Suppose both encoders retain only the cue:

$$
u_1=v_1=(1,0),
$$

$$
u_2=v_2=(0,1).
$$

Matched cosine similarities are one and unmatched similarities are zero.

Choose

$$
\tau=\frac1{\log3}.
$$

Then matched logits are $$\log3$$ and unmatched logits are zero. The matched probability is

$$
\frac{e^{\log3}}{e^{\log3}+e^0}
=
\frac34.
$$

The loss is

$$
-\log\frac34=\log\frac43.
$$

Top-ranked retrieval is correct for both pairs. As temperature decreases, the matched probability approaches one in this construction.

No clinical distinction was required. The objective can be satisfied through a shared nuisance cue when that cue identifies pairs in the evaluated candidate set.

This is why provenance, within-source evaluation, and clinically controlled retrieval tasks matter.

### 7. Candidate-set confidence is not a disease probability

In the preceding construction, a matched logit $$\log3$$ and one alternative logit zero give probability $$3/4$$.

Add another candidate with logit zero. The same image and matched report now receive

$$
\frac3{3+1+1}
=
\frac35.
$$

The clinical evidence has not changed. The candidate set has.

A retrieval softmax is normalized over the supplied alternatives. Its numerical value cannot be interpreted as a calibrated disease probability without a task definition and validation that support that interpretation.

Candidate descriptions, synonyms, and duplicate reports can also change the normalization.

### 8. Some negative pairs are clinically compatible

Suppose two different patients have reports with the same clinically relevant meaning. If their text embeddings are identical, their similarities to an image are identical.

For a batch containing those two reports, the recorded matched report cannot receive more than half the probability when no other information distinguishes them:

$$
q(\text{recorded match})\leq\frac12.
$$

Thus,

$$
L\geq\log2.
$$

The training loss can remain positive even when the model recognizes the shared clinical meaning perfectly.

Instance-level matching and clinical equivalence are different relations. Treating every unmatched patient as a semantic negative can encourage distinctions based on style, acquisition, or irrelevant detail.

Multiple-positive objectives or clinically informed sampling can address parts of this mismatch, but their grouping information also requires validation.

### 9. Global alignment does not imply grounded localization

Suppose an image representation is the mean of patch features:

$$
\phi(I)=\frac1m\sum_{j=1}^m h_j.
$$

For any permutation $$\pi$$ of patch positions,

$$
\frac1m\sum_jh_{\pi(j)}
=
\frac1m\sum_jh_j.
$$

A globally pooled matching objective can therefore be unchanged when the feature's spatial location changes.

Construct two images with two scalar patch features:

$$
I_{\mathrm{left}}=(1,0),
$$

$$
I_{\mathrm{right}}=(0,1).
$$

Their pooled representation is identical:

$$
\phi(I_{\mathrm{left}})
=
\phi(I_{\mathrm{right}})
=
\frac12.
$$

A localization head receiving only this representation must give the same output for both. If left and right are equally likely, it cannot localize both correctly.

The finding can be globally detectable while its location is lost.

Architectures retaining spatial tokens may preserve localization information. The argument is that a global image-report objective alone does not establish sentence-region grounding.

### 10. Define grounding at the level of a claim

A clinical statement can be represented by components such as

$$
c=
(\text{finding},
\text{anatomy},
\text{location},
\text{polarity},
\text{uncertainty},
\text{time},
\text{evidence source}).
$$

Grounding asks whether the appropriate supplied evidence supports these components.

The evidence source may be:

- The current image.
- Another supplied view.
- A prior examination.
- Clinical history.
- A laboratory result.
- An explicitly qualified inference.

A history statement should not be localized to an image merely because it appears in the report. Conversely, a current-image finding needs support in the supplied image or examination.

Attention weights and text-image similarity are not themselves independent verification of that support. Localization annotations, clinical review, and controlled dependence tests address complementary parts of grounding.

### 11. Derive how complementary modalities can combine evidence

Let two observations be $$I$$ and $$C$$. If they are conditionally independent given disease,

$$
p(I,C\mid D)=p(I\mid D)p(C\mid D).
$$

Bayes' rule gives posterior odds

$$
\begin{aligned}
\frac{\Pr(D=1\mid I,C)}{\Pr(D=0\mid I,C)}
&=
\frac{p(I,C\mid D=1)}{p(I,C\mid D=0)}
\frac{\pi}{1-\pi}\\
&=
\boxed{
\frac{p(I\mid1)}{p(I\mid0)}
\frac{p(C\mid1)}{p(C\mid0)}
\frac{\pi}{1-\pi}
}.
\end{aligned}
$$

Independent evidence multiplies likelihood ratios, not necessarily probabilities.

Construct a prior of $$1/2$$ and two binary observations. Each is positive with probability $$3/4$$ in disease and $$1/4$$ without disease.

One positive observation gives posterior odds three and probability

$$
\frac3{1+3}=\frac34.
$$

If the observations are conditionally independent, two positives give odds nine:

$$
\Pr(D=1\mid I=1,C=1)=\frac9{10}.
$$

Equivalently, the positive-pair likelihoods are $$9/16$$ and $$1/16$$, whose ratio is nine.

### 12. Repeated information must not be counted as independent evidence

Now suppose the second observation simply copies the first:

$$
C=I.
$$

The probability of both being positive is then $$3/4$$ in disease and $$1/4$$ without disease. The joint likelihood ratio remains three.

The correct posterior is

$$
\frac34,
$$

not $$9/10$$.

Treating the copied observation as independent would overstate the evidence.

An image and its report often share information because the report was written from the image. Additional clinical context may contribute new evidence, but that contribution cannot be assumed independent.

Fusion should therefore be evaluated as a learned conditional relationship, not justified merely by counting modalities.

### 13. More information can help an ideal predictor without helping a fitted system

Under squared probability loss, the best predictor from $$I$$ is

$$
\mathbb E[Y\mid I],
$$

with Bayes risk

$$
R_I^*=\mathbb E[\operatorname{Var}(Y\mid I)].
$$

Using both modalities gives

$$
R_{I,C}^*
=
\mathbb E[\operatorname{Var}(Y\mid I,C)].
$$

The conditional variance identity yields

$$
\boxed{
R_I^*-R_{I,C}^*
=
\mathbb E[
\operatorname{Var}(\mathbb E[Y\mid I,C]\mid I)
]
\geq0.
}
$$

An ideal predictor can ignore unhelpful additional information, so adding genuine information cannot worsen the optimum under this loss.

A fitted model can still become worse because of limited data, optimization, shortcut learning, temporal leakage, or changed modality relationships.

To investigate contribution, compare image-only, other-modality-only, and combined procedures under comparable development conditions. Removing a modality from an already trained model answers a different question from retraining without it; the removal may itself create an unfamiliar input pattern.

### 14. Missingness and timing are part of the multimodal task

Let $$M_C$$ indicate whether the additional modality is available. A complete-case evaluation estimates performance conditional on

$$
M_C=1.
$$

That population may differ from patients receiving routine care because the decision to obtain another test can depend on clinical suspicion, resources, or earlier findings.

The system should specify behavior when modalities are:

- Missing.
- Stale.
- Anatomically mismatched.
- From different clinical episodes.
- In conflict.
- Available only after the intended prediction moment.

A referral note containing a suspected diagnosis can be legitimate input for a consultation aid. It does not establish image recognition. A report written after the target decision cannot be used to claim prediction at the earlier time.

Patient identity, anatomical correspondence, and timestamps are therefore part of the model's evidence specification.

### 15. Derive what report-generation likelihood optimizes

For report tokens $$R=(r_1,\ldots,r_L)$$, an autoregressive generator models

$$
p_\theta(R\mid I,C)
=
\prod_{t=1}^L
p_\theta(r_t\mid r_{<t},I,C).
$$

Negative log likelihood is

$$
\boxed{
-\log p_\theta(R\mid I,C)
=
-\sum_{t=1}^L
\log p_\theta(r_t\mid r_{<t},I,C).
}
$$

At a fixed input, let $$P$$ be the true training distribution over reports and $$Q$$ the model distribution. Then

$$
\begin{aligned}
\mathbb E_P[-\log Q(R)]
&=
-\sum_RP(R)\log P(R)
+
\sum_RP(R)\log\frac{P(R)}{Q(R)}\\
&=
H(P)+D_{\mathrm{KL}}(P\Vert Q).
\end{aligned}
$$

The optimum reproduces the training report distribution when the model class permits it.

That distribution includes reporting style, omissions, and dependence on context not always supplied to the model. Minimizing token loss does not convert the reports into a complete clinical reference.

At generation time, the model also conditions on its own earlier tokens. An unsupported early statement can change the context for later statements.

### 16. Word overlap can miss a decisive factual reversal

Consider two constructed sentences:

- Reference: “No focal lesion is seen.”
- Generated: “A focal lesion is seen.”

After removing punctuation, each has five tokens. Four tokens match in position and as shared unigrams:

$$
\frac45.
$$

Yet the finding's polarity is reversed.

A word-overlap score can therefore be high while the clinically decisive claim is wrong. This example concerns a defined token comparison, not the exact value of every report-generation metric.

The reverse problem also occurs: two clinically equivalent statements can use different wording. Linguistic similarity and clinical agreement require separate evaluation.

### 17. Evaluate generated claims against adequate evidence

A report evaluation should distinguish:

- Unsupported positive findings.
- Incorrect negative statements.
- Omitted clinically required findings.
- Wrong anatomy or location.
- Wrong temporal comparison.
- Inappropriate certainty.
- Recommendations unsupported by the supplied information.
- Correct statements derived from the wrong evidence source.

If a required fact set is adequately established, claim precision and recall can be defined as

$$
\operatorname{Precision}
=
\frac{\text{supported generated claims}}
{\text{all evaluated generated claims}},
$$

$$
\operatorname{Recall}
=
\frac{\text{required claims correctly expressed}}
{\text{all required claims}}.
$$

The reference must be sufficiently complete for this interpretation. A statement absent from the original report is not automatically false, and a statement in the report may concern information unavailable in the supplied image.

An empty or uniformly noncommittal report can avoid unsupported assertions while omitting necessary findings. Precision alone cannot evaluate usefulness.

### 18. Statement-level quality does not determine report-level reliability

Suppose a constructed report contains three required statements, each independently incorrect with probability $$1/10$$.

The probability that all are correct is

$$
\left(\frac9{10}\right)^3.
$$

Thus,

$$
\boxed{
\Pr(\text{at least one error})
=
1-\left(\frac9{10}\right)^3
=
\frac{271}{1000}.
}
$$

This is an illustrative independence model, not an empirical report-error rate.

Without independence, the union bound still gives

$$
\Pr(\text{any error})
\leq
\sum_j\Pr(\text{error in statement }j).
$$

Report-level evaluation should therefore include the presence and severity of any consequential error, alongside statement-level summaries.

Errors also differ in importance. A severity-weighted report loss can be defined as

$$
L_{\mathrm{report}}
=
\sum_{j\in\mathcal C}w_jE_j,
$$

where $$\mathcal C$$ includes the relevant generated and required claims, $$E_j$$ records a defined error, and $$w_j$$ expresses its consequence.

Weights should be justified or examined through sensitivity analysis. They should not be presented as measured patient harm without the necessary outcome evidence.

### 19. Match the evaluation to the intended use

For retrieval, define candidate sets and relevance beyond exact patient identity.

For classification, evaluate the clinical target, calibration, and operating point.

For localization, use independent region-level evidence and assess whether the claim is actually visible.

For generation, review factual content, omissions, uncertainty, and evidence source. If clinicians edit or approve the text, evaluate the assisted reporting workflow as well as the generator.

Useful stress tests include:

- Missing modalities.
- Conflicting but individually plausible evidence.
- Report templates from another institution.
- Cases where text is weakly informative but images are decisive.
- Cases where the image is limited and uncertainty should be retained.
- Matched changes to image evidence while other context is held fixed.

An arbitrary image-report mismatch is a stress test, not automatically a realistic clinical intervention. Its interpretation should remain tied to what was changed.

### 20. Revision checklist

| Question | What I should be able to derive or explain |
|---|---|
| What does an image-report pair directly supervise? | Correspondence under the data and pairing process |
| Why is a report an indirect label? | Mention probability combines finding prevalence with reporting behavior |
| What does contrastive matching optimize? | Relative identification of paired candidates |
| Why is matching confidence not disease probability? | It depends on the candidate set and matching task |
| Can retrieval succeed without clinical understanding? | Yes; the cue-only construction retrieves both pairs correctly |
| Why is global alignment insufficient for localization? | Pooling can preserve presence while discarding position |
| When do modality likelihood ratios multiply? | Under conditional independence given the target |
| Why can image and report evidence be double-counted? | The report may repeat information derived from the image |
| What does generation likelihood learn? | The conditional distribution of observed report text |
| Why are word metrics insufficient? | Small wording changes can reverse a clinical fact |
| What should generated-text evaluation include? | Supported claims, omissions, localization, uncertainty, timing, and consequence |

In the ontology, retrieval alignment, clinical validity, and grounded evidence reliance are different properties. Clinical assessability limits which claims can be supported by a particular image, while the clinical target determines the required output and evaluation.

## Why it matters for my work

For gallbladder AI, language can help specify the findings an audit should examine. I need to preserve whether each statement comes from the ultrasound, another observation, or clinical context, and test image reliance when text already predicts the diagnosis.

## What I have not resolved

- Which report statements are assessable in the actual model inputs?
- How can image contribution be evaluated when text is already strongly predictive?
- What output should express unresolved conflict between credible modalities?

---

Sources: Independent study; paired contrastive pretraining is connected to the verified ConVIRT paper linked above. All numerical examples, probability calculations, and counterexamples are constructed and derived explicitly. These are study notes for research purposes, not clinical guidance.
