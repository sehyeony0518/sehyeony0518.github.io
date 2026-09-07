---
layout: study_note
title: "Circadian Rhythm Disorders"
description: "Wearable and continuous data, and what changes when the signal is a long time series."
tab: "clinical-medicine"
tab_title: "Clinical Medicine"
category: "sleep-circadian"
category_title: "Sleep & Circadian Medicine"
order: 1
source: "Lecture"
written: true
updated: "2026-09-08"
---

Circadian rhythm sleep-wake disorders involve persistent or recurrent disruption of sleep timing that causes insomnia, excessive sleepiness, or impaired functioning. The relevant evidence is often a pattern across days rather than an abnormality captured during one night.

## Clinical overview

Delayed and advanced sleep-wake phase disorders involve sleep timing that is persistently later or earlier than desired or required. Non-24-hour sleep-wake rhythm disorder involves a rhythm that fails to remain aligned with the daily cycle. Irregular sleep-wake rhythm disorder involves poorly consolidated sleep distributed across the day and night.

Shift work and travel can also create circadian misalignment. A preference for late sleep is not itself a disorder. I would first ask whether the timing causes impairment and whether sleep improves when the person can follow their preferred schedule.

## Anatomy and pathophysiology

The suprachiasmatic nucleus coordinates circadian timing, with light input from the retina helping align internal rhythms to the environment. Sleep also depends on homeostatic pressure that accumulates during wakefulness. Circadian timing and sleep pressure interact, so similar bedtimes do not necessarily imply similar internal biological phases.

Light exposure and melatonin can shift circadian timing, with effects depending on when they occur relative to internal phase. Treatment timing is part of its mechanism, and I would record it alongside the dose.

## Diagnostic workflow and imaging findings

### Reconstruct the habitual schedule

History should cover sleep onset, waking, work or school obligations, free days, naps, light exposure, medication, caffeine, and symptoms. The clinician distinguishes inability to sleep at a required time from poor sleep across all schedules. Recent travel, rotating shifts, mood symptoms, and neurological conditions can change the interpretation.

### Observe the pattern across multiple days

Sleep diaries document intended and perceived sleep timing. Actigraphy estimates rest and activity from movement and can complement the diary, as recommended for selected evaluations in the [AASM actigraphy guideline](https://doi.org/10.5664/jcsm.7230). One quiet night cannot establish a stable delay, and a short recording may miss a progressively drifting rhythm.

### Distinguish movement-derived sleep from biological phase

Actigraphy does not directly record sleep physiology or the circadian pacemaker. Quiet wakefulness can resemble sleep, and device removal can resemble inactivity. In specialized assessment, dim-light melatonin onset can help estimate circadian phase. [Benloucif and colleagues](https://pubmed.ncbi.nlm.nih.gov/18350967/) describe why controlled light conditions, sampling, and assay interpretation matter. A wearable’s inferred bedtime is not interchangeable with this measurement.

### Order additional testing for a defined alternative

Polysomnography may be indicated when another sleep disorder is suspected, but it is not ordinarily needed simply to demonstrate habitual circadian timing. Brain imaging does not routinely confirm a circadian rhythm disorder. The decisive findings are the longitudinal timing pattern, symptoms, and their relationship to imposed schedules, with additional investigations guided by the differential.

## Differential diagnosis and management context

Insomnia disorder, insufficient sleep, sleep apnea, restless legs symptoms, mood disorders, medication effects, and environmental disruption can overlap with circadian complaints. These conditions may coexist rather than compete as mutually exclusive labels. Improvement on free days is informative but should be interpreted alongside total sleep opportunity and daytime function.

Management can involve scheduled sleep, changes in light exposure, and appropriately timed melatonin in selected disorders. The [2015 AASM treatment guideline](https://pubmed.ncbi.nlm.nih.gov/26414986/) makes recommendations specific to the disorder and patient population, with uneven evidence across interventions. I would not generalize one schedule or treatment timing to every patient who reports sleeping late.

## Implications for medical AI

I would separate sleep-wake estimation, circadian-phase estimation, disorder classification, and prediction of daytime impairment. Each requires a different reference. Long recordings introduce missingness, nonwear, clock errors, travel, seasonal changes, and treatment changes. Splitting adjacent windows from one person across training and testing can make personal routines appear to be generalizable disease evidence.

The connection to my clinical faithfulness work is temporal context. A model may recognize an employer’s shift pattern or a device’s behavior while claiming to measure endogenous rhythm. I would evaluate across people, devices, and schedules, and compare predictions with independent diaries or phase markers where appropriate. An accurate activity pattern is only one part of the clinical explanation.

## References

- Smith et al., [Use of Actigraphy for the Evaluation of Sleep Disorders and Circadian Rhythm Sleep-Wake Disorders: An American Academy of Sleep Medicine Clinical Practice Guideline](https://doi.org/10.5664/jcsm.7230), Journal of Clinical Sleep Medicine 2018.
- Benloucif et al., [Measuring melatonin in humans](https://pubmed.ncbi.nlm.nih.gov/18350967/), Journal of Clinical Sleep Medicine 2008.
- Auger et al., [Clinical Practice Guideline for the Treatment of Intrinsic Circadian Rhythm Sleep-Wake Disorders: Advanced Sleep-Wake Phase Disorder (ASWPD), Delayed Sleep-Wake Phase Disorder (DSWPD), Non-24-Hour Sleep-Wake Rhythm Disorder (N24SWD), and Irregular Sleep-Wake Rhythm Disorder (ISWRD). An Update for 2015: An American Academy of Sleep Medicine Clinical Practice Guideline](https://pubmed.ncbi.nlm.nih.gov/26414986/), Journal of Clinical Sleep Medicine 2015.
