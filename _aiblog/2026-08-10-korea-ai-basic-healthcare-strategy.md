---
layout: post
title: "Korea's 'AI-Basic Healthcare' Strategy: a Potential Game Changer for Medical AI"
date: 2026-08-10 12:00:00+0900
description: "Notes on Korea's new national medical AI strategy: outcome-based reimbursement decided at the hospital level, a public 'AI highway' for inference infrastructure, and sovereign medical AI."
featured: true
tag: "MOHW"
related_posts: false
---

In the summer of 2026, the Korean government announced one of the most consequential policies the medical AI field here has seen: the **AI-Basic Healthcare Strategy** (AI 기본의료 전략), a joint strategy across ministries including the Ministry of Health and Welfare (MOHW), the Presidential AI Strategy Committee, the Ministry of Science and ICT, and the MFDS. It was presented at a presidential event on July 22 and formally adopted at the State Policy Coordination Meeting on August 6 — meaning this is no longer a proposal under discussion, but a fixed national direction now entering the implementation stage.

This post summarizes my notes from a public interview in which **Director Jung-hwan Park** (MOHW, Medical AI and Data Policy Division), one of the strategy's chief architects, explained its design to **Dr. Yoon Sup Choi** of Digital Healthcare Partners. Any errors of interpretation are mine. I found the strategy remarkable enough — especially as someone who studies whether medical AI models actually earn clinical trust — that it seemed worth writing up in three parts.

## Part 1 — What "AI-Basic Healthcare" means

The name follows the government's broader **"AI-Basic Society"** philosophy: just as roads, electricity, and water are provided as universal social infrastructure, AI-based healthcare should become infrastructure that reaches every citizen's life.

The catch, as Director Park noted, is that healthcare is not something a government can deliver directly. Between the state and the patient stand physicians, hospitals, device makers, pharmaceutical companies, and distributors — and all of them must share the vision for AI to actually reach patients. The strategy therefore positions the government as a *primer* (마중물): a vision-level roadmap that sets national direction, with the concrete mechanisms — reimbursement, R&D programs, data guidelines — to be worked out item by item from here.

## Part 2 — The boldest part: outcome-based, hospital-decided reimbursement

Korea's reimbursement system has two existing routes for new technology: the fee-for-service track (the hardest to enter) and the "early market entry" track beneath it — both gated by central pre-evaluation bodies. The strategy adds a **third, ground-floor track** that inverts the usual logic:

- **Hospitals, not the government, decide what to adopt.** A hospital reviews an AI product's clinical scenario, decides "let's try this on 100 cases," and submits its own plan and success metrics. The same product can carry different KPIs at different hospitals.
- **Payment follows demonstrated outcomes.** Evaluation happens *after* real-world use, not before. If the pre-declared clinical indicators improve, the government compensates the institution — and that revenue flows back to the developer. In Director Park's words, the target is **effectiveness** (performance in uncontrolled, real clinical environments), not just efficacy in controlled studies.
- **No patient copay.** Unlike the existing conditional-entry pathways that rely on out-of-pocket payments, this is an institution-level payment under a fiscal cap.
- **Scope includes non-device AI.** Both MFDS-cleared AI medical devices and AI tools classified as non-medical-devices (ambient voice EMR being the recurring example) are eligible.
- **Strings attached: governance.** Higher compensation tiers require in-hospital AI governance — a function that decides which tools to adopt, monitors performance drift, and keeps conflicts of interest transparent.

Funding is still under discussion (health insurance funds via institution-level payments, the general account, and the essential-care special account are all candidates), and pricing is expected to be dynamic: nearly free early on while evidence accumulates, with suppliers gaining pricing power once a scenario proves out and replicates across hospitals — plausible precisely because medical AI's marginal cost is so low.

What struck me most is the incentive realignment. As Director Park put it, the industry has long said "stop optimizing AUROC; change actual clinical outcomes" — and this policy makes that literal: a company's objective function must now be *clinical indicators that practicing physicians find convincing*, or even the ground-floor track is out of reach.

## Part 3 — Infrastructure and sovereignty: the AI highway and Korean models

Two supporting pillars complete the picture.

**The Public Medical AI Highway.** Today, every hospital or vendor procures its own GPUs, and that capital cost gets baked into prices. The strategy proposes government-provided inference infrastructure — initially called an "inference farm" — so that hospitals can switch on AI tools integrated with their EMRs without buying hardware. Director Park's analogy was defragmenting a disk: consolidating scattered GPU fragments across the country so the freed-up resources flow into R&D instead. Pilots begin in the second half of 2026 with regional flagship (national university) hospitals, expanding next year.

**Sovereign medical AI.** The strategy's mention of "independent AI models trained on domestic data" drew misreadings — it does not mean the state will build models that compete with industry. It is R&D support for *Korean companies and hospitals* to develop models (training data included) that keep the healthcare system resilient if foreign licenses or model access were suddenly cut off. Medical foundation-model R&D calls are expected next year, favoring domestically developed open-weight lineages.

There is also a regional-care thread I found meaningful: packaged AI for underserved areas — ambient documentation to reduce administrative load, and decision support tuned to primary care (screening, rule-out, referral-necessity judgments), where a model built for tertiary hospitals could actively mislead.

## A researcher's takeaway

If this framework works, the currency of medical AI in Korea stops being benchmark accuracy and becomes **verified real-world clinical effect** — evaluated where care actually happens, with governance watching for performance drift. That is, in a policy form, the same question my research asks technically: *is this model right for clinically valid reasons, and can we audit that?* Outcome-based reimbursement will need exactly such auditing machinery — for shortcut reliance, for drift, for evidence that survives the move from curated datasets to messy clinics. It is rare to see a national policy and a research agenda point so directly at the same problem.
