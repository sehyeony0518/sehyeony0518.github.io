---
layout: post
title: Beyond AUROC — What VUNO's DeepCARS Teaches Us About Making Medical AI Work
date: 2025-11-14 12:00:00 +0900
description: Notes from an interview with VUNO founder and CEO Ye Ha Lee on DeepCARS, clinical evidence, reimbursement, and what it takes to move medical AI from a model into routine care.
featured: true
related_posts: false
---

How does a promising predictive model become something hospitals can integrate, clinicians can act on, and a healthcare system can pay for? Most medical-AI stories end at the benchmark; this one is about everything that comes after.

The case is VUNO, one of Korea's earliest medical-AI companies, and its flagship inpatient risk-prediction product, VUNO Med®-DeepCARS®. These are my notes from a public interview series in which VUNO founder and CEO Dr. Ye Ha Lee spoke with Dr. Yoon Sup Choi about the company's beginnings, the clinical design of DeepCARS, Korea's reimbursement system, and VUNO's global strategy. Any errors of interpretation are mine.

The original conversation also covered revenue, investment, and corporate performance. I have mostly left those parts aside to focus on what seems more durable: the path from a promising algorithm to a clinical service that is actually used.

## Part 1 — From early deep learning to medical AI

VUNO was founded in December 2014, after Lee had worked on deep learning at the Samsung Advanced Institute of Technology. At the time, deep learning was still unfamiliar outside a relatively small research community, so the technology itself was the company's initial advantage. The harder question was where that technology could create meaningful value.

Lee recalled an early pilot with clinicians at Asan Medical Center. In roughly a month, the team produced a result that surpassed what the clinical group had achieved after years of encoding medical knowledge into conventional methods. The lesson was not that clinical expertise had become unnecessary. It was that medicine contained large amounts of carefully preserved data whose patterns were difficult to express as hand-written rules.

Medical imaging was a natural starting point. Korean hospitals already had extensive PACS infrastructure, medical images were stored in standardized DICOM formats, and radiologists were accustomed to digital workflows. VUNO began with image-based projects and, in May 2018, VUNO Med-BoneAge became Korea's first AI-powered medical device approved by the MFDS. The company also participated in building some of the regulatory guidance that did not yet exist for AI-based software devices.

DeepCARS represented a different direction. Rather than interpreting an image after a test had been ordered, it asked whether routinely collected data could warn clinicians before a patient deteriorated.

## Part 2 — DeepCARS: designing for the ward, not the benchmark

The clinical problem begins with a gap in observation. Intensive-care patients are continuously monitored, but patients in general wards may have their vital signs checked only three or four times a day. A patient can worsen substantially between those measurements, and by the time the change becomes obvious, the opportunity for early intervention may already be narrowing.

VUNO began developing DeepCARS with clinicians at Bucheon Sejong Hospital around 2016. The system analyzes four routinely measured vital-sign categories — blood pressure, heart rate, respiratory rate, and body temperature — and estimates the risk of cardiac arrest within the next 24 hours. Instead of treating each measurement as an isolated snapshot, it analyzes the trajectory accumulated from admission onward.

The limited input set was deliberate. Adding laboratory tests and other EHR variables might increase performance in a particular institution, but it would also introduce missingness, hospital-specific testing patterns, and a much larger integration burden. Every hospital measures the four basic vital signs. Using them made the system easier to transfer across institutions of different sizes and levels of care.

This is an important design lesson: maximizing the number of inputs is not always the same as maximizing clinical usefulness. A somewhat simpler model that can run reliably in many hospitals may be more valuable than a richer model that depends on one institution's data environment.

At the time of regulatory approval, Lee recalled an AUROC of roughly 0.89 and an average warning time of about 16 hours before cardiac arrest. But the more consequential feature was the reduction in false alarms compared with conventional early-warning scores such as MEWS or NEWS.

In a real hospital, sensitivity alone is not enough. If a system produces too many alerts, clinicians begin to ignore or disable it. DeepCARS therefore had to identify high-risk patients while keeping the alert burden low enough for rapid-response teams and ward staff to act on.

The risk score also became a shared language. Instead of a nurse having to call a physician and say that a patient simply "looks unusual," the team could communicate that the DeepCARS score had risen beyond a particular level. The model's output was not replacing clinical judgment; it was making escalation more timely and more concrete.

By the time of the interview, Lee said DeepCARS was being used in roughly 150 hospitals and more than 50,000 beds, including a substantial share of Korea's tertiary hospitals. Adoption by itself does not prove clinical benefit, but it does show that the product had crossed an operational barrier that many medical-AI systems never reach.

## Part 3 — Accuracy and clinical effectiveness are different claims

One of the clearest points in the interview was the distinction between the performance of a medical device and the clinical effectiveness of a medical technology.

A model may predict an event accurately without improving patient outcomes. The prediction may arrive too late, clinicians may have no effective response, the alert may not fit the workflow, or the necessary staff may not be available. Even a technically perfect detector has limited value if its output cannot lead to a useful intervention.

VUNO therefore moved beyond retrospective accuracy studies and began building evidence around what happened after hospitals acted on DeepCARS alerts. Lee highlighted a one-year prospective study at Inha University Hospital in which appropriate responses to DeepCARS alerts were associated with statistically significant reductions in in-hospital cardiac arrest and mortality, on the order of 30–40%, along with shorter hospital stays.

The company was also preparing evidence from three hospitals without dedicated rapid-response teams and conducting a multicenter randomized controlled trial across four university hospitals. These studies address different questions: whether the model generalizes, whether it works outside highly resourced tertiary centers, and whether introducing it into care changes patient outcomes.

The results still need careful interpretation. An early-warning system is not a pill administered in isolation. Its effect depends on staffing, escalation protocols, response time, clinician adherence, and the treatments available after an alert. An observed improvement therefore cannot automatically be attributed to the model alone.

But that is precisely the point. Deployed medical AI is a sociotechnical intervention. Evaluating only the model while ignoring the care pathway around it gives an incomplete account of whether the system works.

## Part 4 — Reimbursement is part of the evidence pipeline

Korea presents another translation problem: receiving medical-device clearance does not automatically allow a hospital to charge for using the device.

To create a new billable medical service, a technology must pass additional assessment. This produces a familiar paradox. Hospitals are reluctant to adopt a product without reimbursement, but a company cannot accumulate strong real-world clinical evidence unless hospitals adopt it.

DeepCARS became the first AI medical device to enter Korea's market through the deferred new health technology assessment pathway. Beginning in 2022, hospitals could offer it as a non-covered service after receiving patient consent. The hospital charged the patient and shared part of the revenue with VUNO.

That arrangement aligned several incentives at once. Clinicians gained a potentially more useful warning system. Patients received additional monitoring. Hospitals could improve patient safety while creating a new revenue stream. VUNO, in turn, earned revenue that could be reinvested in further clinical studies.

The arrangement was conditional, however. The deferral period existed so that the company could build evidence before undergoing the full new health technology assessment. The eventual question was not simply whether DeepCARS generated an accurate risk score, but whether using the technology produced sufficient clinical value to justify continued inclusion in the healthcare system.

This makes clinical evidence more than an academic output or a post-market formality. It becomes part of the product's infrastructure and, in DeepCARS's case, part of the company's ability to continue operating the service.

## Part 5 — Global expansion begins with payment, not approval

VUNO carried the same lesson into its international strategy. According to Lee, the company began its preparation for the United States not by studying FDA clearance alone, but by studying the American reimbursement system.

Regulatory approval gives a company permission to sell a medical device. It does not necessarily give a hospital an economic reason to buy it. Hospitals must pay for integration, training, maintenance, and clinical operation. Without a reimbursement route or a sufficiently strong cost-saving case, even an FDA-cleared product may remain a pilot.

DeepCARS received FDA Breakthrough Device Designation, and VUNO pursued U.S. clearance alongside a potential pathway through the New Technology Add-on Payment program. The broader principle was to coordinate regulation, clinical evidence, and reimbursement rather than treating them as separate stages.

Lee also discussed existing U.S. deterioration-risk systems such as eCART and the Rothman Index. In his account, comparable products often face two practical barriers: they require a broad range of input variables that are difficult to integrate consistently, and hospitals lack a dedicated reimbursement mechanism for using them. VUNO sees DeepCARS's small routine input set and its experience with reimbursement in Korea as potential advantages.

The company's Global Patient Safety Summit reflected another part of that strategy. Researchers who had developed major early-warning systems, rapid-response frameworks, and patient-safety concepts were invited to Seoul. Lee described the experience personally: people whose papers and diagrams he had studied while developing DeepCARS were now visiting VUNO to discuss how the product was being used in practice.

Beyond DeepCARS, VUNO is developing systems for more specific causes or forms of deterioration, including respiratory failure, sepsis, and acute kidney injury, as well as versions for intensive-care and emergency settings. Its DeepECG line aims to identify conditions such as left ventricular systolic dysfunction and acute myocardial infarction from ECG data.

The deeper asset may therefore be more than one successful model. It may be the accumulated ability to connect routine clinical data, a focused prediction task, workflow integration, prospective evidence, regulation, and reimbursement.

## A researcher's takeaway

The interview suggested four layers by which a deployed medical-AI system should be judged:

1. **Predictive validity:** Does the model discriminate and calibrate risk accurately?
2. **Operational validity:** Are its inputs routinely available, and can it be integrated without excessive missingness, latency, or alarm burden?
3. **Clinical effectiveness:** Does acting on its output improve patient care or outcomes?
4. **Institutional viability:** Can the system fit governance, regulation, reimbursement, and the economics of the hospital using it?

Failure at any one of these layers can prevent an otherwise impressive model from having clinical impact.

Trustworthy medical-AI research often concentrates on the first layer: model performance, robustness, calibration, interpretability, or the evidence used by the prediction. Those questions remain essential. DeepCARS's story, however, shows that trust also emerges at the boundary between the model and the surrounding care system.

At the same time, a positive clinical outcome study does not automatically prove that the model relies on clinically valid evidence. A model could still exploit institution-specific correlations or behave inconsistently in particular subgroups, while a strong downstream response protocol partially compensates for those weaknesses. Conversely, a clinically well-aligned model may still fail as a product if it cannot be integrated, acted upon, or reimbursed.

Model auditing and clinical evaluation are therefore complements, not substitutes.

The previous two posts described the policy incentives and technical capabilities behind Korea's medical-AI strategy. VUNO's experience adds the translation layer. A medical-AI model begins to matter when it closes the full loop: from routine data to risk, from risk to action, from action to patient outcomes, and from those outcomes back to evidence and sustainable deployment.
