---
layout: post
title: "From Diagnostic Tools to Expert Companions: Why Korea Wants Its Own Medical Foundation Model"
date: 2026-08-21 12:00:00+0900
description: "Notes from a lecture by Prof. Joon-Beom Seo, head of the AI-Basic Healthcare Task Force: ten years from AlphaGo, four ways AI can transform care, and the case for a sovereign medical foundation model."
featured: true
related_posts: false
---

This is a follow-up to my [previous post on Korea's AI-Basic Healthcare Strategy](/blog/2026-08-10-korea-ai-basic-healthcare-strategy/). That post covered the policy machinery; this one covers the vision behind it, as laid out in a public lecture at Seoul National University by **Prof. Joon-Beom Seo** — a radiologist who has collaborated with (mostly Korean) engineering teams for some twenty years, and who now chairs the **AI-Basic Healthcare Task Force** under the National AI Strategy Committee. He was careful to note he was speaking personally, not for the TF; the same disclaimer applies doubly to my notes here.

He opened with a wry remark: when generative models first appeared, he argued Korea should build its own healthcare foundation models — and was widely dismissed ("does Korea even have the capacity?"). That the same argument is now national policy says something about how fast this field has moved.

## Part 1 — Ten years from AlphaGo: from narrow experts to expert companions

It has been almost exactly ten years since AlphaGo (February 2016), and Prof. Seo divides the decade sharply in two.

The first wave was **supervised deep learning matching specialists on narrow pattern-recognition tasks**. The landmark was Google's 2016 *JAMA* paper on diabetic retinopathy — shocking at the time, obvious in retrospect — followed by skin cancer, pathology, and the rest. The result today: on the order of a thousand AI medical devices cleared in the US and roughly three hundred in Korea, and a period of "will radiologists be replaced?" rhetoric. But these systems were narrow: expert-level at one supervised task, nothing more. General intelligence was something people projected for 2050.

The last three or four years broke that frame. Transformers and generative models turned the conversation from task-specific tools to **medical foundation models** — his summary: first train something to roughly the level of passing a medical licensing exam, then specialize it with comparatively little extra training, the way a resident specializes. With major labs now releasing medical-specialty models, and consumer-facing health models that aggressively reduce hallucination through expert curation, the field has moved from *assistants for experts* to *expert-level companions*. That reframing is what makes a national strategy thinkable at all.

## Part 2 — Four ways AI can actually transform care

The paradigm shift healthcare has promised since the 2000s — personalized, preventive, patient-centered — stalled, in his view, for a simple reason: it requires far more expert labor than any system can supply. Intelligent agents are what make it feasible. He organizes AI's contribution into four categories:

**1. Productivity and efficiency.** Already happening: diagnostic-assist tools in routine use, and ambient documentation — AI drafting the medical record from the doctor–patient conversation — which is an established market in the US and now being built by multiple Korean companies. The doctor who stared at the computer instead of the patient is the first thing this fixes.

**2. Quality of care.** The more interesting frontier. Earlier clinical decision support failed, he argued, not because the idea was wrong but because it came too early and underestimated medicine. Now evidence-grounded LLM search engines are reshaping practice — reportedly more than half of US clinicians already consult one rather than a general search engine. He also highlighted physician-to-physician **remote consultation** (not telemedicine — doctor-to-doctor) as a key lever for fixing care-delivery structure, though it lacks a revenue model anywhere in the world. And **predictive medicine**: ICU deterioration prediction already deployed; opportunistic screening (e.g., predicting osteoporosis from a chest X-ray — a company he disclosed a COI with); a UK Biobank–trained foundation model predicting ten-year onset across a thousand-plus diseases at the individual level, externally tested on a Danish cohort; and US EHR-scale models predicting complications, medication adherence, even ER-visit probability from a hundred million patients' records.

**3. Accessibility.** Not replacing primary care with AI, but **raising primary care to tertiary-level accuracy** — "1.5th-tier care," as some call it: the clinic near your home, backed by AI decision support and remote specialist consultation. The other half is patients' access to medical knowledge itself — LLMs translating health-check results and clinical language into something patients actually understand, which several Korean companies are building.

**4. Expanding the scope of medicine.** From wellness through chronic-disease management to elder care, connected as one seamless data flow: continuous-glucose-monitoring platforms managing diet, exercise, and complications; and in the US, virtual nursing companions that know a patient's full post-operative context and counsel them at home.

The through-line: in the generative era, AI is not a point solution for one department — it is intelligence embedded across the entire system.

## Part 3 — Why a sovereign medical foundation model

Given all that, his conclusion is blunt: the Korean agents this system needs cannot all be built on foreign proprietary models. He frames a shared, public Korea-specific medical foundation model as a matter of **health rights and medical sovereignty** — the same logic as the government's sovereign-AI policy, applied to medicine. A joint foundation-model initiative announced by Seoul National University Hospital and Naver last November is, in his view, an important starting point.

He closed with where the AI Strategy Committee's action plan stands: of its 99 action items, five concern healthcare, and the three he personally focuses on are **expanding medical data, securing foundation models, and implementing AI-Basic Healthcare** on top of them.

## A researcher's takeaway

Reading this alongside the reimbursement strategy from the previous post, the division of labor becomes clear: the TF supplies the *capability* thesis (foundation models as national infrastructure), the ministry supplies the *incentive* thesis (pay only for verified real-world effect). What sits between them — and what I think is still underdeveloped — is the **verification layer**. Foundation models specialize with little extra training, which is exactly why their failure modes are subtle: shortcut cues, distribution shift, capability that does not transfer from licensing-exam benchmarks to a messy clinic. If expert-level companions are to be embedded across an entire health system, auditing *what evidence these models actually use* stops being an academic question and becomes infrastructure of its own.
