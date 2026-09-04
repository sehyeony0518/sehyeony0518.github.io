---
layout: post
title: "The Medical Algorithmic Audit"
date: 2026-08-04 12:00:00 +0900
venue: "Lancet Digital Health"
authors: "Xiaoxuan Liu, Ben Glocker, Melissa M. McCradden, Marzyeh Ghassemi, Alastair K. Denniston, Lauren Oakden-Rayner (2022)"
description: "A viewpoint proposing a structured audit process for deployed medical AI, treating shortcut learning, poor generalizability, and weak explainability as the three named failure modes an auditor should anticipate rather than discover by accident."
related_posts: false
---

**Paper.** *The medical algorithmic audit* — [Lancet Digital Health (2022)](https://doi.org/10.1016/S2589-7500(22)00003-6)

## Why I read it

Most of the papers in this collection are single studies demonstrating one failure mode in one model. This viewpoint asks a more organizational question: what would it look like to audit for these failure modes systematically, as a named process, rather than stumbling onto them one dataset at a time.

## What the paper claims

The authors propose a medical algorithmic audit framework that walks an auditor through a clinical task, the components that could produce errors within it, and the likely consequences of those errors. They name shortcut learning, poor generalizability to new deployment settings, and unreliable explainability as the qualities that make AI systems distinctively prone to errors a conventional medical-device audit would miss. Recommended testing approaches include exploratory error analysis, subgroup testing, and adversarial testing, illustrated with examples from the authors' own prior work. The paper frames safety monitoring as a joint responsibility between developers and users, with feedback loops running in both directions after deployment.

## What convinced me

Naming shortcut learning, generalizability, and explainability as the three qualities that distinguish AI failure modes from conventional device failure modes is a genuinely useful frame, because each of those three maps directly onto a body of technical literature (the shortcut-learning papers, the external-validation papers, the interpretability papers) that otherwise reads as three separate conversations. Positioning the audit as joint developer-user responsibility, with structured feedback after deployment, also treats auditing as an ongoing process rather than a one-time pre-deployment gate.

## What it leaves open

As a viewpoint rather than an empirical study, the paper does not itself run the audit process it proposes on a concrete model, and the framework's individual components (exploratory error analysis, subgroup testing, adversarial testing) are each the subject of extensive separate literatures with their own limitations. The paper also does not specify who has the authority or incentive to demand an audit, or what happens when a developer and a deploying institution disagree about its findings.

## What I take from it

This is a useful organizing scaffold for the rest of my reading: shortcut reliance, generalization failure, and explanation unreliability are not three unrelated concerns but the three named axes of one audit. When I evaluate a new medical-AI paper now, I ask explicitly which of these three axes it addresses and which it leaves for a different study, rather than treating "the model was audited" as a single undifferentiated claim.
