---
layout: study_note
title: "Feedback Control: Open Loop, Feedforward, and Why More Feedback Can Be Worse"
description: "The three ways to make a system do what you want, the shower that scalds you because the thermostat is by the door, and what that says about a model retraining on data its own deployment produced."
tab: "ai-foundations"
tab_title: "Theory"
category: "feedback-control"
category_title: "Feedback Control & Classical Design"
order: 1
source: "Independent study"
written: true
updated: "2026-09-15"
---

Unpacking the phrase *feedback control of dynamic systems* one word at a time turns out to be a good way into the whole subject, because each word is doing real work.

A **system** is anything with an input and an output. Not a computer or a satellite — those are examples, and reaching for them first is like answering "what is an area?" with an integral rather than a rectangle. A resistor with a voltage across it is a system: voltage in, current out.

**Control** means making the output what you want it to be. You name a target; the job is to hit it.

**Dynamic** means the input–output relation is a differential equation. Output does not depend on input alone but on the system's accumulated state — which is what makes this harder than solving for a number.

**Feedback** means measuring the output and using that measurement to decide the input.

## Core question and definition

Why is the last word needed at all? Because of **disturbances**.

Set a car's throttle to a fixed position and the speed still varies: hills, wind, load. Set an air conditioner to a fixed power and the room temperature still varies: sun, occupancy, doors. The input–output relation you modelled is real, but it is not the only thing acting on the output.

That gives three strategies, and the distinction between them is the useful part:

- **Open loop.** Compute an input you believe will produce the target and apply it. No sensor. The throttle held at a fixed angle — fine on the flat, wrong on every hill.
- **Feedforward.** Sense the *disturbance* and compensate in advance. See the hill coming, press harder before the car slows. Requires anticipating which disturbances matter and modelling how each affects the output.
- **Feedback.** Sense the *output* and correct the error. Watch the speedometer, adjust. It needs no model of the disturbance at all, which is why it handles disturbances nobody anticipated — the reason it is the default.

## Key concepts

### Feedback is not automatically good

Here is the example worth remembering, because it makes the failure physical.

The temperature control is by the bathroom door; your friend is in the shower. You set it, they say *too cold*, you turn it up hard. A few seconds later: *too hot!* You turn it down hard. *Too cold!* The temperature oscillates, growing worse rather than settling.

Everything about that loop is textbook correct — sense the output, correct the error. The system is unstable anyway, and two properties of the loop are why: a **delay** between acting and observing the result, and a **gain** high enough that by the time you see the error, your correction has already overshot.

The same loop with a smaller gain — nudging instead of wrenching — converges. This is the central fact of control theory: **feedback is a design problem, not a switch.** Adding it to an unstable configuration makes things worse, and "we added monitoring" is not the same as "we made it stable."

### The dynamic part is where the mathematics goes

Modelling comes before controlling. A car reduces to $$m\dot v + bv = u$$ — mass times acceleration equals applied force minus a drag proportional to speed. A suspension becomes a mass, a spring, and a damper, and yields a second-order equation.

Second-order linear ODEs then supply the whole toolkit. Their homogeneous solutions form a vector space: any linear combination of solutions is a solution, and once you have found two independent ones, *every* solution is a combination of those two. So solving becomes finding two independent solutions by any means available — which is why guessing $$e^{\lambda t}$$ and solving the characteristic equation works, and is legitimate rather than a trick.

The [Laplace transform](/study/all-pass-systems-and-group-delay/) then converts the differential equation into an algebraic one whose poles and zeros are visible at a glance. Same information, rearranged so the stability question can be read off instead of solved for.

## Why it matters for my work

A deployed model is a control system, and classifying which kind it is clarifies a great deal.

**Most deployed medical AI is open loop.** It produces outputs; nobody measures whether they were right. Performance is assumed to persist because it held during validation — which is exactly assuming the disturbance is zero. It is not: case mix drifts, scanners are replaced, protocols change, referral patterns shift.[^shift]

**Input monitoring is feedforward.** Watching for distribution shift compensates for disturbances *you thought to instrument*, which is both its strength — you can act before anything goes wrong — and its limit, since an unanticipated shift passes unnoticed.

**Outcome monitoring is feedback**, and it is the only one that catches disturbances nobody predicted. It is also the hardest, because clinical outcomes arrive months later, which means **long delay** — and long delay is precisely the condition under which feedback destabilises.

That is not an analogy. It is the same mechanism. Consider a model whose predictions influence care, whose outcomes are then recorded, and which is retrained on that record. The model now appears in its own training distribution, with a delay set by how long outcomes take to mature, and a gain set by how strongly clinicians act on its output. A model that under-flags a subgroup produces fewer confirmed cases in that subgroup, which trains a model that under-flags it further. The loop can run away, and it runs away *quietly*, because every metric computed on the model's own downstream data agrees with it.[^perf][^runaway]

The shower has a solution and so does this one: **reduce the gain, or reduce the delay.** Keep a prospective evaluation stream that does not depend on the model's own outputs, recruit the way a trial would, and accept that it is slower and more expensive than reusing the operational data. There is no version where you retrain on your own footprint and stay calibrated by luck.

The last thing I want to keep is the framing itself. Treating the model as the system and the clinic as an environment acting on it is a modelling choice, and a poor one — the clinicians, the workflow and the model together are the system, which is where the loop actually closes.[^selbst] Drawing the boundary too tightly around the model makes the loop invisible, and an invisible loop is exactly the one nobody tunes.

---

[^shift]: Finlayson, S. G., et al. (2021). The clinician and dataset shift in artificial intelligence. *New England Journal of Medicine*, 385(3), 283–286. [10.1056/NEJMc2104626](https://doi.org/10.1056/NEJMc2104626)

[^perf]: Perdomo, J. C., Zrnic, T., Mendler-Dünner, C., & Hardt, M. (2020). Performative prediction. *ICML 2020*. [arXiv:2002.06673](https://arxiv.org/abs/2002.06673)

[^runaway]: Ensign, D., Friedler, S. A., Neville, S., Scheidegger, C., & Venkatasubramanian, S. (2018). Runaway feedback loops in predictive policing. *FAT\* 2018*, PMLR 81, 160–171. [arXiv:1706.09847](https://arxiv.org/abs/1706.09847)

[^selbst]: Selbst, A. D., Boyd, D., Friedler, S. A., Venkatasubramanian, S., & Vertesi, J. (2019). Fairness and abstraction in sociotechnical systems. *FAT\* 2019*, 59–68. [10.1145/3287560.3287598](https://doi.org/10.1145/3287560.3287598)
