---
layout: post
title: "Why audit medical AI? — opening this blog"
date: 2026-08-18 12:00:00+0900
description: A short note on why "accurate" is not the same as "trustworthy" in medical AI, and what this blog will be about.
related_posts: false
---

Welcome! This blog is where I will post occasional notes on **medical AI and digital healthcare** — paper readings, lessons from building diagnostic models, and thoughts on what it takes for AI to be genuinely trustworthy in clinical settings.

A question drives most of my research: **when a medical AI model is accurate, is it accurate for clinically valid reasons?** High benchmark scores do not guarantee that a model relies on evidence a clinician would recognize as meaningful. Models can exploit shortcut cues — acquisition artifacts, frequency signatures, dataset biases — that have nothing to do with disease. A model that is right for the wrong reasons can fail silently exactly when it matters.

That is why I work on *auditing*: methods that examine what evidence a trained model actually uses, without retraining it, and model designs whose evidence pathways can be inspected directly.

Posts here will be informal — notes rather than papers. If any of this resonates, feel free to reach out.
