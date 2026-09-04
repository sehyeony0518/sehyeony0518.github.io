---
layout: post
title: "Who Does Medical AI Work For?: Why Average Accuracy Is Not Enough"
date: 2025-08-15 12:00:00 +0900
description: "High average accuracy does not mean medical AI works equally well for every patient. A look at hidden bias, data representation, subgroup performance, and why trustworthy AI must ask who benefits, and who bears the errors."
tag: "Fairness"
related_posts: false
---

Artificial intelligence is often presented as an objective alternative to human judgment.

A machine applies the same mathematical rules to every patient. It does not become tired, distracted, or consciously prejudiced. This creates an appealing expectation: if everyone is evaluated by the same algorithm, everyone should be treated fairly.

But equal computation does not necessarily produce equal care.

A medical AI system can achieve excellent average performance while providing very different levels of benefit across patient populations. The reason is that healthcare data contain more than biological signals of disease. They also contain traces of who had access to care, who received diagnostic testing, how clinicians made decisions, which measurements were collected, and how those decisions were documented.

Existing inequalities in the healthcare system can therefore become embedded in the data used to train AI.

The ethical question is not simply whether AI should be restricted. A more important question is:

**Who receives the benefits of medical AI, and who absorbs its errors?**

## AI does not learn disease alone

Hospital data are not a perfect sample of the general population. They represent people who reached the healthcare system, underwent particular examinations, received certain diagnoses, and had those events recorded.

Two people with the same disease may enter the healthcare system very differently. Income, geography, occupation, insurance, transportation, caregiving responsibilities, and access to specialists can all affect when someone seeks care and which tests they receive. A patient who rarely appears in the healthcare system may consequently be poorly represented in the data used to train an AI model.

From the model's perspective, that patient population may barely exist.

A striking example was published in *Science* in 2019. Researchers examined a widely used algorithm designed to identify patients who would benefit from additional healthcare management. The algorithm did not explicitly use race as an input, yet it systematically underestimated the health needs of Black patients.[1]

The problem was not an explicit racial rule. It was the target the algorithm had been asked to predict. Instead of directly estimating illness burden, the system used previous healthcare spending as a proxy for medical need.

That sounds reasonable until we remember that healthcare spending reflects more than health. If one population historically receives less healthcare because of barriers to access, lower spending does not mean that population is healthier. But an algorithm trained on cost may interpret exactly that.

The same mathematical rule is applied to everyone, yet the result reinforces an existing inequality. AI can therefore reproduce inequity without ever being given a variable called "race."

## AI can discover demographic signals humans cannot see

Removing sensitive attributes from a dataset does not guarantee fairness. Race, socioeconomic status, or other characteristics can remain indirectly encoded in apparently unrelated variables such as insurance type, residential location, healthcare utilization, testing frequency, or institutional patterns.

Even medical images may contain demographic information that clinicians themselves cannot readily identify. A 2022 study in *The Lancet Digital Health* showed that deep learning models could predict a patient's self-reported race from chest X-rays, CT scans, and mammograms with unexpectedly high performance.[2] Human experts generally cannot perform this task reliably from the images alone.

The important question is not simply that AI can infer race. The deeper concern is that a diagnostic model may unintentionally use these hidden signals when making predictions about disease. If disease prevalence, healthcare utilization, scanner type, institutional practice, or labeling patterns are correlated with a demographic group, the model may exploit those relationships rather than relying only on clinically meaningful evidence.

This means fairness cannot be evaluated merely by inspecting which variables were explicitly supplied to the model. We need to examine its actual behavior. Does sensitivity differ across populations? Does specificity? Are false negatives concentrated in one group? Is calibration equally reliable? Does the model fail differently across hospitals, devices, or demographic subgroups?

The relevant question is not only **what information entered the model**, but **how the model behaves for different patients**.

## Patients missing from the data may also be missing from the benefits

Representation matters particularly clearly in dermatology.

Many historically used dermatology image datasets have disproportionately included lighter skin tones. A model trained primarily on those images may perform very well on a conventional benchmark while behaving differently when deployed in a more diverse population. Research using the Diverse Dermatology Images dataset found that several dermatology AI systems showed substantial performance degradation when tested on more diverse patients, with particularly notable problems involving darker skin tones and less common diseases.[3]

A model that performs well on light skin does not automatically perform equally well on dark skin.

This illustrates why "more data" is not sufficient as a goal. A dataset can contain millions of examples and still omit clinically important parts of the population. Medical AI datasets must represent the kinds of variation that affect real-world performance: age, sex, skin tone, disease severity, rare conditions, geographic region, hospital environment, scanner manufacturer, acquisition protocol, and many other sources of clinical heterogeneity.

Researchers should also report who was included and who was not. Subgroup performance and external validation should not be treated as optional supplementary analyses.

Data representation is not merely a statistical question. It determines which patients are more likely to bear the cost when the model is wrong.

## AI can inherit the bias of medical devices

Bias does not always originate in the algorithm. It can already exist in the instruments used to produce the model's inputs or labels.

Pulse oximetry provides an important example. Pulse oximeters estimate arterial oxygen saturation noninvasively using light transmitted through tissue. These measurements are widely used in clinical care and may also serve as inputs or reference measurements for predictive models.

A 2020 study in *The New England Journal of Medicine* found that occult hypoxemia, dangerously low arterial oxygen saturation despite apparently reassuring pulse-oximeter readings, occurred more frequently among Black patients than White patients.[4]

If an AI system treats such measurements as objective ground truth, it may learn and reproduce the measurement error. The bias is then no longer limited to the original device. It can propagate through the AI system and potentially affect decisions at much larger scale.

Evaluating medical AI therefore requires examining the entire measurement chain. What device produced the input? Is that device equally accurate across patient groups? Were the labels themselves affected by measurement bias? Do diagnostic thresholds have the same clinical meaning across populations?

An algorithm cannot automatically correct a biased measurement simply because its computation is mathematically consistent. The US Food and Drug Administration's 2025 draft guidance for medical-purpose pulse oximeters reflects this concern, proposing stronger expectations for diversity in clinical studies and evaluation across different skin pigmentation levels.[5]

The reliability of AI depends on the reliability of what it learns from.

## High average accuracy can hide unequal harm

Consider a hypothetical medical AI system evaluated on 1,000 patients, achieving an overall accuracy of 91.5%. That sounds excellent.

But imagine that 900 patients belong to a majority population in which accuracy is 95%, while the remaining 100 patients belong to a minority population in which accuracy is only 60%. The overall number still looks impressive because the larger population dominates the average. Yet the burden of error is concentrated in the smaller group.

This is why the following statements are fundamentally different:

**The model performs well on average.**

and

**The model performs fairly across patients.**

Overall accuracy and AUROC cannot answer the second question by themselves. Medical AI should be evaluated across clinically relevant subgroups using measures such as sensitivity, specificity, false-positive rate, false-negative rate, predictive value, and calibration.

And fairness does not necessarily mean forcing every metric to become numerically identical across every group. Different errors have different consequences. In cancer screening, a false negative may delay diagnosis and create far greater harm than a false positive. In a model determining eligibility for an invasive procedure, excessive false positives may expose patients to unnecessary risk.

The question of which error matters most cannot be answered by mathematics alone. It requires clinical judgment and social values. Patients, clinicians, researchers, health systems, and regulators all have a role in deciding which risks are acceptable and how they should be distributed.

## Fairness begins before the model is trained

Medical AI ethics should not appear only as a paragraph in the limitations section of a finished paper.

Fairness begins at study design. Researchers should first define the population for whom the technology is intended, ask which groups might be underrepresented, and consider which sources of inequality might already exist in the underlying healthcare process. During data collection, they should examine not only who was included but also who was excluded and why. During model development and validation, subgroup performance and external validity should be tested explicitly.

And deployment is not the end of evaluation. Once a system enters clinical practice, performance should continue to be monitored to determine whether errors increase for particular populations, institutions, devices, or changing patient distributions. This lifecycle perspective is consistent with international guidance emphasizing inclusiveness, equity, transparency, human oversight, and continuous monitoring in healthcare AI.[6]

Fairness is not a one-time property certified before deployment. It is something that must continue to be observed.

## Equal rules are not always equitable rules

There is an intuitive appeal to treating every person identically. But healthcare does not begin from identical conditions. Patients differ in their biology, access to care, social circumstances, previous treatment, exposure to diagnostic testing, and representation in historical datasets.

Applying exactly the same algorithm to everyone may therefore preserve inequalities that already existed before the algorithm was introduced. A fair medical AI system is not necessarily one that applies a mathematically identical process and then stops asking questions. It is one whose performance and failures are examined across the people it is intended to serve.

This distinction becomes increasingly important as AI moves from retrospective studies into screening programs, emergency departments, hospitals, and population-scale healthcare systems. At small scale, a biased decision may affect one patient. At algorithmic scale, the same pattern can be reproduced thousands or millions of times.

Automation increases consistency. If the underlying system is unfair, it can also increase the consistency of unfairness.

## A researcher's takeaway

Medical AI is often evaluated by asking: **How accurate is the model?**

That question is necessary. It is no longer sufficient. We also need to ask: **Accurate for whom?**

A model can achieve state-of-the-art average performance while failing patients who were poorly represented in its training data. It can avoid explicitly using race while reconstructing demographic information through hidden proxies. It can learn bias from healthcare utilization, clinical documentation, or the medical devices used to generate its labels. And it can make those historical patterns appear objective because they are expressed through numbers.

This is why fairness belongs to the broader problem of trustworthy medical AI. The goal is not to force every population to produce identical statistics. The goal is to identify where performance diverges, understand why it diverges, determine whether those differences create clinically meaningful harm, and redesign the system when risk becomes concentrated in particular patients.

Medical AI will not be trustworthy simply because its average performance becomes high enough. It will be trustworthy when we understand **where that performance holds, where it breaks, and who pays the price when it breaks**.

The next question for medical AI is therefore not only how accurate it can become. It is whether that accuracy remains valid for the people who need it most.

## References

1. Obermeyer Z, Powers B, Vogeli C, Mullainathan S. *Dissecting racial bias in an algorithm used to manage the health of populations.* Science. 2019;366:447–453. doi:10.1126/science.aax2342.
2. Gichoya JW, Banerjee I, Bhimireddy AR, et al. *AI recognition of patient race in medical imaging: a modelling study.* The Lancet Digital Health. 2022;4:e406–e414. doi:10.1016/S2589-7500(22)00063-2.
3. Daneshjou R, Vodrahalli K, Novoa RA, et al. *Disparities in dermatology AI performance on a diverse, curated clinical image set.* Science Advances. 2022;8. doi:10.1126/sciadv.abq6147.
4. Sjoding MW, Dickson RP, Iwashyna TJ, Gay SE, Valley TS. *Racial Bias in Pulse Oximetry Measurement.* New England Journal of Medicine. 2020;383:2477–2478. doi:10.1056/NEJMc2029240.
5. U.S. Food and Drug Administration. *Pulse Oximeters for Medical Purposes: Draft Guidance.* 2025.
6. World Health Organization. *Ethics and Governance of Artificial Intelligence for Health.* 2021.
