---
layout: page
permalink: /research/
title: research
description: Trustworthy medical AI grounded in clinical evidence.
nav: true
nav_order: 7
toc:
  sidebar: left
---

## Trustworthy Medical AI Grounded in Clinical Evidence

My research asks a simple but consequential question:

> **When a medical AI model is accurate, is it accurate for clinically valid reasons?**

High predictive performance alone does not guarantee that a model relies on evidence clinicians would consider meaningful. I study how to audit model reasoning, identify shortcut reliance, and evaluate whether interpretable model readouts remain faithful to independent clinical factors.

## Clinical Faithfulness

My primary research focuses on **clinical faithfulness**: whether a model's interpretable evidence meaningfully aligns with clinical severity, diagnostic factors, or other independent clinical information.

I am particularly interested in post-hoc auditing methods that can evaluate model reasoning without retraining the model or requiring direct faithfulness annotations.

## Ultrasound AI

I study ultrasound AI that reflects clinically and physically meaningful image characteristics — echogenicity, texture, lesion boundaries, anatomical context, and frequency structure.

Rather than treating interpretability as an additional visualization step, I aim to connect computational evidence with the factors clinicians actually use in practice.

## Research Interests

- Clinical faithfulness and model auditing
- Shortcut learning and spurious correlations
- Trustworthy and interpretable medical AI
- Ultrasound image analysis
- Frequency-based and graph-based representations
- Reliability monitoring for deployed AI systems

## Selected Projects

<style>
  .proj-grid { display: grid; grid-template-columns: 1fr; gap: 1rem; margin: 1rem 0 0.5rem; }
  @media (min-width: 640px) { .proj-grid { grid-template-columns: 1fr 1fr; } }
  .proj-card {
    display: flex; flex-direction: column;
    border: 1px solid rgba(128,128,128,.2); border-radius: 12px;
    padding: 1.1rem 1.2rem; background: rgba(128,128,128,.035);
    transition: border-color .15s ease, box-shadow .15s ease;
  }
  .proj-card:hover { border-color: var(--global-theme-color); box-shadow: 0 4px 18px rgba(0,0,0,.06); }
  .proj-card .pc-top { display: flex; flex-wrap: wrap; align-items: center; gap: .45rem; margin-bottom: .5rem; }
  .proj-card .pc-period { font-size: .72rem; opacity: .55; font-variant-numeric: tabular-nums; }
  .proj-card .pc-badge {
    font-size: .66rem; font-weight: 700; letter-spacing: .03em;
    padding: .1rem .5rem; border-radius: 999px;
    border: 1px solid var(--global-theme-color); color: var(--global-theme-color);
  }
  .proj-card h3 { font-size: 1.02rem; margin: 0 0 .4rem; line-height: 1.35; }
  .proj-card .pc-desc { font-size: .88rem; line-height: 1.6; opacity: .82; margin: 0 0 .7rem; flex-grow: 1; }
  .proj-card .pc-tags { display: flex; flex-wrap: wrap; gap: .35rem; }
  .proj-card .pc-tag { font-size: .7rem; padding: .12rem .5rem; border-radius: 6px; background: rgba(128,128,128,.12); opacity: .85; }
  .proj-card .pc-link { margin-top: .6rem; font-size: .8rem; text-decoration: none; color: var(--global-theme-color); }
  .proj-card .pc-link:hover { text-decoration: underline; }
</style>

<div class="proj-grid">

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">M.S. Thesis</span><span class="pc-period">2025 – Present</span></div>
    <h3>Clinical Faithfulness Auditing for Medical Image Classifiers</h3>
    <p class="pc-desc">Developing post-hoc methods to examine whether interpretable model readouts rely on clinically valid evidence rather than shortcut features — without retraining the model or requiring faithfulness annotations.</p>
    <div class="pc-tags"><span class="pc-tag">Clinical Faithfulness</span><span class="pc-tag">Shortcut Analysis</span><span class="pc-tag">Post-hoc Auditing</span></div>
  </div>

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">ITRC · Hospital</span><span class="pc-period">2025 – Present</span></div>
    <h3>Gallbladder Ultrasound AI</h3>
    <p class="pc-desc">Research on trustworthy gallbladder ultrasound classification in collaboration with Ajou University Hospital, including reliability requirements analysis and clinically grounded representation learning.</p>
    <div class="pc-tags"><span class="pc-tag">Ultrasound AI</span><span class="pc-tag">Reliability</span><span class="pc-tag">Ajou Univ. Hospital</span></div>
    <a class="pc-link" href="/publications/">→ ACK 2025 (first author)</a>
  </div>

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">Industry</span><span class="pc-period">2025 – 2026</span></div>
    <h3>Predictive Maintenance Monitoring</h3>
    <p class="pc-desc">Designed fault-prediction models and reliability monitoring software for industrial equipment in a smart-factory research project with Samsung Heavy Industries, grounded in international reliability standards.</p>
    <div class="pc-tags"><span class="pc-tag">Predictive Maintenance</span><span class="pc-tag">Monitoring SW</span></div>
    <a class="pc-link" href="/publications/">→ KCSE 2026 (first author)</a>
  </div>

</div>

## Education

- **M.S., AI Convergence Network**, Ajou University &nbsp;<span style="opacity:.55;">Feb 2026 – Feb 2028 (expected)</span>
  Embedded & Software Lab / MIIDS Research Center. Thesis on clinical faithfulness auditing of ultrasound diagnostic models.
- **B.S., Electrical and Computer Engineering** (Microdegree in Data Science & AI), Ajou University &nbsp;<span style="opacity:.55;">Mar 2020 – Feb 2026</span>

## Research Experience

- **Graduate Researcher**, Embedded & Software Lab, Ajou University &nbsp;<span style="opacity:.55;">2026 – Present</span>
  Clinical faithfulness auditing and shortcut analysis of ultrasound diagnostic models (M.S. thesis).
- **Undergraduate Researcher**, ITRC Gallbladder Ultrasound AI Project (with Ajou University Hospital) &nbsp;<span style="opacity:.55;">2025 – 2026</span>
  Reliability requirements analysis and clinically grounded modeling; first-authored ACK 2025.
- **Research Intern**, Samsung Heavy Industries Project, Embedded & Software Lab &nbsp;<span style="opacity:.55;">2025 – 2026</span>
  Fault-prediction models and reliability monitoring software; first-authored KCSE 2026.
- **Research Intern**, Dept. of Psychiatry, Ajou University Hospital &nbsp;<span style="opacity:.55;">2024</span>
  Government-funded computational psychiatry project; IRB-approved clinical research workflows.

## Teaching

- **Teaching Assistant**, Logic Circuit Experiment (논리회로실험), Dept. of Electrical and Computer Engineering, Ajou University &nbsp;<span style="opacity:.55;">Spring 2026</span>
  Led weekly digital-logic lab sessions and guided students through circuit implementation. Course evaluation **4.77 / 5.0 (95.4%)**.

For a full list of roles, publications, and skills, see the [cv](/cv/) page.

## Open-Source Software

Selected repositories on [GitHub](https://github.com/sehyeony0518):

<div class="proj-grid">

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">ACK 2025 · C1</span></div>
    <h3>ultrasound-ai-reliability-requirements</h3>
    <p class="pc-desc">Requirements framework for reliable ultrasound diagnostic AI — data/model attribute pairs made executable as a gallbladder pipeline (paper explainer).</p>
    <a class="pc-link" href="https://github.com/sehyeony0518/ultrasound-ai-reliability-requirements" target="_blank" rel="noopener">→ github.com/sehyeony0518/ultrasound-ai-reliability-requirements</a>
  </div>

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">KCSE 2026 · C2</span></div>
    <h3>smart-factory-monitoring</h3>
    <p class="pc-desc">Condition-monitoring console for predictive maintenance of industrial robots — five-layer architecture traced to software quality and functional safety standards (reference implementation).</p>
    <a class="pc-link" href="https://github.com/sehyeony0518/smart-factory-monitoring" target="_blank" rel="noopener">→ github.com/sehyeony0518/smart-factory-monitoring</a>
  </div>

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">Software Reg. · S1</span></div>
    <h3>medical-marker-remover</h3>
    <p class="pc-desc">Client-side tool for removing diagnostic markers from medical images and restoring the background (OpenCV.js + WASM, PSNR/MSE). No image leaves the browser.</p>
    <a class="pc-link" href="https://github.com/sehyeony0518/medical-marker-remover" target="_blank" rel="noopener">→ github.com/sehyeony0518/medical-marker-remover</a>
  </div>

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">Research Prototype</span></div>
    <h3>scid5-module-j-agent</h3>
    <p class="pc-desc">LLM-administered SCID-5 Module J (adjustment disorder) interview — DSM-5 criteria as a decision tree, with human-in-the-loop probes on uncertainty.</p>
    <a class="pc-link" href="https://github.com/sehyeony0518/scid5-module-j-agent" target="_blank" rel="noopener">→ github.com/sehyeony0518/scid5-module-j-agent</a>
  </div>

</div>

Published papers and manuscripts in preparation are listed on the [publications](/publications/) page.
