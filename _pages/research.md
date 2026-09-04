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

<a href="/assets/pdf/cv-hwang.pdf" target="_blank" rel="noopener" style="display:inline-block; margin:.2rem 0 .8rem; padding:.4rem 1rem; border:1px solid var(--global-theme-color); border-radius:999px; color:var(--global-theme-color); text-decoration:none; font-size:.85rem; font-weight:600;">⬇ Download CV (PDF)</a>

## Trustworthy Medical AI Grounded in Clinical Evidence

My research asks a simple but consequential question:

> **When a medical AI model is accurate, is it accurate for clinically valid reasons?**

High predictive performance alone does not guarantee that a model relies on evidence clinicians would consider meaningful. I study how to audit model reasoning, identify shortcut reliance, and evaluate whether interpretable model readouts remain faithful to independent clinical factors.

## Clinical Faithfulness

My primary research focuses on **clinical faithfulness**: whether a model's interpretable evidence meaningfully aligns with clinical severity, diagnostic factors, or other independent clinical information.

I am particularly interested in post-hoc auditing methods that can evaluate model reasoning without retraining the model or requiring direct faithfulness annotations.

## Ultrasound AI

I study ultrasound AI that reflects clinically and physically meaningful image characteristics: echogenicity, texture, lesion boundaries, anatomical context, and frequency structure.

Rather than treating interpretability as an additional visualization step, I aim to connect computational evidence with the factors clinicians actually use in practice.

## Research Interests

**Clinical Evidence Auditing**<br>
Whether diagnostic AI models make correct predictions for clinically valid reasons: evidence attribution, shortcut learning and spurious correlations, and auditable model behavior, evaluated without retraining or direct faithfulness annotations.

**Ultrasound AI for Hepatobiliary Diagnosis**<br>
Ultrasound-based AI models for gallbladder and hepatobiliary disease diagnosis, with an emphasis on clinically informed and interpretable representations grounded in echogenicity, texture, and anatomical context.

**Generalizable & Clinically Deployable Medical AI**<br>
Medical AI that remains reliable across hospitals, devices, and patient populations, through external validation, robustness analysis, and clinically grounded evaluation of deployed systems.

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
    <p class="pc-desc">Developing post-hoc methods to examine whether interpretable model readouts rely on clinically valid evidence rather than shortcut features, without retraining the model or requiring faithfulness annotations.</p>
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

- **M.S. in AI Convergence Network**, Ajou University &nbsp;<span style="opacity:.55;">Feb 2026 – Feb 2028 (expected)</span>
  Advisor: Prof. Jung-Won Lee. Embedded & Software Lab / MIIDS Research Center. Thesis on clinical faithfulness auditing of ultrasound diagnostic models.
- **B.S. in Electrical and Computer Engineering** (Microdegree in Data Science & AI), Ajou University &nbsp;<span style="opacity:.55;">Mar 2020 – Feb 2026</span>
  Advisor: Prof. Jung-Won Lee.

## Research Experience

- **Graduate Researcher**, Embedded & Software Lab (ESL) / MIIDS Research Center, Ajou University &nbsp;<span style="opacity:.55;">Feb 2026 – Present</span>
  <span style="opacity:.55;">MSIT-funded University ICT Research Center (ITRC)</span>
  Conducting M.S. research on trustworthy medical AI, including post-hoc auditing of evidence use in trained models and auditable diagnostic model design (M2, M1). Evaluating model evidence using frequency-band, attention, and attribution analyses across CNN, transformer, graph, and wavelet-based classifiers.

- **Undergraduate Researcher**, ITRC Project on Gallbladder Ultrasound AI &nbsp;<span style="opacity:.55;">Jan 2025 – Feb 2026</span>
  <span style="opacity:.55;">MIIDS Research Center, Ajou University</span>
  Contributed to an MSIT-funded project on AI-based gallbladder ultrasound diagnosis in collaboration with Ajou University Hospital; the work continued into my M.S. research. First-authored a reliability requirements study reporting a **~33% improvement in malignant-class detection sensitivity** (C1). Developed clinical-knowledge-guided modeling strategies using echogenicity, texture, lesion margin, wall features, and anatomical context. Presented center research at the ITRC Talent Development Fair in 2025 and 2026.

- **Graduate Researcher**, Diagnostic Prediction via Robotic Motion Anomaly Detection &nbsp;<span style="opacity:.55;">Dec 2025 – Nov 2026</span>
  <span style="opacity:.55;">Embedded & Software Lab (ESL), Ajou University, funded by Samsung Heavy Industries</span>
  Developing machine learning models for robotic motion anomaly detection and equipment fault prediction in smart-factory systems; first-authored a monitoring-software design paper based on international reliability standards (C2).

- **Undergraduate Research Intern**, Dept. of Psychiatry, Ajou University Medical Center &nbsp;<span style="opacity:.55;">May 2024 – Dec 2024</span>
  Participated as an external researcher in a government-funded, IRB-approved computational psychiatry project involving clinical research workflows and clinical data handling. Supervised by Prof. Taewi Kim.

- **Research Assistant**, Energy Center, Ajou University &nbsp;<span style="opacity:.55;">Jan – Dec 2021</span>
  Operated XRD and IR spectroscopy equipment and analyzed samples for university and industry collaborators.

## Teaching Experience

- **Teaching Assistant** (Spring 2026) **→ Head Teaching Assistant** (Fall 2026), Logic Circuit Laboratory (undergraduate), Ajou University &nbsp;<span style="opacity:.55;">Mar 2026 – Dec 2026</span>
  Supervised undergraduate digital logic labs (circuit troubleshooting, team projects, and grading) as TA in Spring 2026, with student evaluation **4.77 / 5.00 (95.4%)**. Served as Head TA in Fall 2026, training and coordinating the course's teaching assistants.

- **Undergraduate Research Mentor**, Convergence Electronics Research, Dept. of ECE, Ajou University &nbsp;<span style="opacity:.55;">Jan – Dec 2026</span>
  Mentored an undergraduate research project on ultrasound image segmentation model design and experiments.

## Selected Projects & Competitions

- **Self-Supervised ECG Anomaly Detection Framework**, ICT Challenge 2026 &nbsp;<span style="opacity:.55;">Jan – Dec 2026</span>
  <span style="opacity:.55;">University ICT Research Center Program</span>
  Designing, training, and optimizing lightweight self-supervised models for ECG anomaly detection.

- **Explainable Diagnostic Framework for Gallbladder Polyp Classification**, ICT Challenge 2025 &nbsp;<span style="opacity:.55;">2025</span>
  <span style="opacity:.55;">Undergraduate capstone project · Team leader · also presented at the Industry–Academia Fair</span>
  Developed a clinically guided ultrasound classifier using lesion margin, contrast, and liver–gallbladder echogenicity difference as explicit model features. Achieved **93% overall accuracy and 0.90 malignant-class F1** on a public dataset.

- **Conquer Health Hackathon**, Medical Science Foundation Models, hosted by Lunit &nbsp;<span style="opacity:.55;">Aug 2026</span>
  <span style="opacity:.55;">Team of 2 · system designer and presenter</span>
  Designed *Control Plane for a Frozen Clinician*: an orchestration harness that controls a frozen medical foundation model (Lunit L2) with risk-adaptive clinical-evidence retrieval and source-cited answers, without retraining. Evaluated on HealthBench-based clinical dialogue tasks; presented at the final session.

## Awards

- **Encouragement Award**, ECE Industry–Academia Fair, Ajou University &nbsp;<span style="opacity:.55;">Dec 2025</span>
  <span style="opacity:.55;">Individual entry · 84 teams competed</span>
- **Social Value Award** (Special Award), 2025 Capstone Design Competition, Ajou University &nbsp;<span style="opacity:.55;">Nov 2025</span>
  <span style="opacity:.55;">Team leader · 1 of 12 awarded teams</span>

## Skills

- **Programming.** Python, PyTorch, PyTorch Geometric, Linux, Git
- **Machine Learning.** CNNs, vision transformers, graph neural networks, self-supervised learning
- **Trustworthy AI.** Shortcut analysis, attribution analysis, frequency-band analysis, model auditing
- **Medical Imaging.** Ultrasound imaging, clinical-factor analysis, superpixel-based image representation
- **Languages.** Korean (native); English (IELTS scheduled)

## Professional Training

- **Digital Healthcare AI Solution Development and Industry Field Experience**, Center for Artificial Intelligence in Healthcare, Seoul National University Bundang Hospital &nbsp;<span style="opacity:.55;">Aug 2024</span>
- **Convergence Security Workforce Training: Smart Healthcare (Basic)**, 21 hours, Korea Information Security Industry Association (KISIA), Ministry of Science and ICT &nbsp;<span style="opacity:.55;">Jul 2024</span>

## Community Service & Military

- **Community Outreach Volunteer**, Sillim-dong, Seoul &nbsp;<span style="opacity:.55;">Mar 2026 – Present</span>
  Participate in regular community outreach, providing practical assistance and ongoing support to local residents.
- **Sergeant, Republic of Korea Air Force**, 15th Special Mission Wing, honorably discharged &nbsp;<span style="opacity:.55;">Mar 2022 – Dec 2023</span>

## Open-Source Software

Selected repositories on [GitHub](https://github.com/sehyeony0518):

<div class="proj-grid">

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">ACK 2025 · C1</span></div>
    <h3>ultrasound-ai-reliability-requirements</h3>
    <p class="pc-desc">Requirements framework for reliable ultrasound diagnostic AI, data/model attribute pairs made executable as a gallbladder pipeline (paper explainer).</p>
    <a class="pc-link" href="https://github.com/sehyeony0518/ultrasound-ai-reliability-requirements" target="_blank" rel="noopener">→ github.com/sehyeony0518/ultrasound-ai-reliability-requirements</a>
  </div>

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">KCSE 2026 · C2</span></div>
    <h3>smart-factory-monitoring</h3>
    <p class="pc-desc">Condition-monitoring console for predictive maintenance of industrial robots, five-layer architecture traced to software quality and functional safety standards (reference implementation).</p>
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
    <p class="pc-desc">LLM-administered SCID-5 Module J (adjustment disorder) interview, DSM-5 criteria as a decision tree, with human-in-the-loop probes on uncertainty.</p>
    <a class="pc-link" href="https://github.com/sehyeony0518/scid5-module-j-agent" target="_blank" rel="noopener">→ github.com/sehyeony0518/scid5-module-j-agent</a>
  </div>

</div>

Published papers and manuscripts in preparation are listed on the [publications](/publications/) page.
