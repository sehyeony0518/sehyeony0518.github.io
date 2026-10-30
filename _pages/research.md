---
layout: page
permalink: /research/
title: research
og_image: "https://sehyeony0518.github.io/assets/img/og/page-research.png"
description: "Clinically grounded interpretability and evaluation of medical imaging AI, with ultrasound as the main application, toward human-centered clinical decision support."
nav: true
nav_order: 7
---
<a href="/assets/pdf/cv-hwang.pdf" target="_blank" rel="noopener" style="display:inline-block; margin:.2rem 0 .8rem; padding:.4rem 1rem; border:1px solid var(--global-theme-color); border-radius:999px; color:var(--global-theme-color); text-decoration:none; font-size:.85rem; font-weight:600;">⬇ Download CV (PDF)</a>

I study whether medical imaging models use the clinical concepts an expert would name, with ultrasound as the main application. The broader goal is **human-centered medical AI**: clinical models whose learned behavior corresponds to clinical concepts and values, supporting rather than displacing the person who has to decide.

This is how I situate the work rather than a settled taxonomy of the field, since interpretable machine learning, human-centered AI, alignment and clinical informatics overlap heavily. **Human-centered AI** asks that systems be designed and judged by human values, autonomy, understandability and control ([Shneiderman, 2020](https://doi.org/10.1080/10447318.2020.1741118)). **Human-AI interaction** asks how a person and a model actually work together ([Amershi et al., CHI 2019](https://doi.org/10.1145/3290605.3300233)). **Clinical decision support** is where I ask those questions: imaging diagnosis, clinical decision making, mental health, and the working relationship between a clinician and a model.

### Accuracy is not the whole question

Suppose a radiologist is handed a lung nodule flagged by a model that detects cancer at 95 percent accuracy. Several things can still be wrong, and the headline accuracy hides all of them.

- The model may have learned a burned-in marker or a property of the scanner rather than the lesion.
- The radiologist may not be able to tell why it decided what it decided.
- The radiologist may defer to it where their own reading was better.
- The radiologist may see something the model missed, with no way to give that back.

These problems span model behavior, explanation quality and how a person uses what they are shown. My current work is on the first of those: whether the model uses the clinical concepts it is credited with.

## Current work and where it is going

### 1. Concept-based interpretability

Does a model actually use the clinical concepts an expert would name?

Saliency maps give spatial attribution. They do not establish which clinical concepts a model uses, and a clinician wants to know something else: whether the lesion border is irregular, whether the tissue architecture is abnormal, whether a particular pattern is present, and how much each of those contributed to the diagnosis. The question is whether a link can be built between concepts a person holds and the representations a model computes, and what has to hold before such a link counts as evidence rather than a plausible picture. The lineage runs through [TCAV](https://proceedings.mlr.press/v80/kim18d.html) (Kim et al., ICML 2018) and [concept bottleneck models](https://proceedings.mlr.press/v119/koh20a.html) (Koh et al., ICML 2020), which have branched rather than been superseded.

This is where my M.S. work sits. An explanation that looks anatomically reasonable is not thereby faithful to the computation, and a readout that correlates with a clinical factor has not thereby been shown to drive the prediction. Making those distinctions measurable is the problem.

### 2. Clinical objectives and evaluation

What makes a medical model good, if not accuracy?

A false negative and a false positive are not the same event in a clinic. Missing a cancer and sending a healthy patient for an unnecessary workup carry different costs, borne by different people, and the balance between them changes with the disease, the setting and the stage of care. So the question is whether what a model optimizes corresponds to what the clinical task is actually for: which operating point, measured against which cost, for which population. My ACK 2025 requirements study is a first step, making malignant-class sensitivity the metric the requirements answer to. Extending that to error costs and populations is work I have not done. The fuller sense of value alignment, whose values a system should serve, is a normative question I am not yet addressing ([Gabriel, 2020](https://doi.org/10.1007/s11023-020-09539-2)).

### 3. Bidirectional human-AI alignment  <span class="rq-status">future direction</span>

Alignment has usually meant moving the model toward the person. The harder version runs both ways, and also covers how people adapt to the system ([Shen et al., NeurIPS 2025 position paper](https://arxiv.org/abs/2406.09264)): the clinician's knowledge, criteria and reasons should reach the model, and the model's uncertainty, grounds and failure modes should reach the clinician.

The aim is not a clinician who agrees with the model. It is a clinician who knows accurately what it is good at and what it is not, and who can therefore rely on it or override it in the right places. That is the older problem of appropriate reliance ([Lee and See, 2004](https://doi.org/10.1518/hfes.46.1.50_30392)). I have not built or studied such a system.

### 4. Human-AI interaction in clinical decision making  <span class="rq-status">future direction</span>

This one is answered by reader study, not by a benchmark alone. Compare unaided interpretation, interpretation with the model's output, and interpretation with its output plus concept-level grounds, and measure not only diagnostic accuracy but confidence, over-reliance and how judgments change. A claim of better joint performance also has to be checked against the model working alone. The clinical onboarding problem here is already a literature ([Cai et al., CSCW 2019](https://doi.org/10.1145/3359206)).

The uncomfortable possibility is the interesting one. Explanations may raise accuracy, or they may simply raise trust, including where trust is not warranted. Which of those happens is an empirical question about a workflow, not a property of an algorithm. I have not run such a study: as I put it in my own [notes on Su-In Lee's lecture](/blog/2026-09-09-suin-lee-iscb-innovator-lecture/), an audit can expose a dependency without helping a clinician recognize an incorrect prediction, and I have not yet demonstrated that an audit changes what a clinician does.

### 5. Human-centered mental health AI

Mental health assessment raises its own version of these questions, because the evidence is the patient's language, affect, context and subjective experience, and classification alone does not reach it.

For an LLM-administered assessment the questions are concrete. Does it extract the clinically significant content from what the patient said? Does its next question follow from the answer it was given? Where do its judgments agree with a clinician's and where do they diverge? Can the patient understand what it is asking and say what they mean? And does it ever hold a wrong conclusion confidently enough to lead a patient toward it? I built a [research prototype inspired by SCID-5 Module J](https://github.com/sehyeony0518/scid5-module-j-agent) to explore structured interviewing. It has not been evaluated for clinician agreement, patient usability or clinical benefit, and its uncertainty category is model-generated rather than calibrated.

## Clinical knowledge shapes the research question

None of the five questions has content without the medicine. "Clinically valid evidence" and "clinical value" are empty phrases until someone knows what a radiologist reads and in what order, which findings are interpreted together, what a reference standard does and does not establish, and how patients who receive one workup differ from those who receive another.

So I study hepatobiliary medicine, sonographic findings, examination protocols and ultrasound physics directly, because they determine what an image can support and which clinical concepts a model should be evaluated against. Acquisition is part of that: operator, machine and preset variation enters the image alongside the patient, and separating the two is a prerequisite for calling anything a shortcut. My [study notes](/study/) cover this alongside the computational side, and my [publications](/publications/) list the work that has appeared.

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
  /* Marks a research question as a direction rather than work already done. */
  .rq-status {
    font-size: .62rem; font-weight: 700; letter-spacing: .06em; text-transform: uppercase;
    vertical-align: .28em; margin-left: .5rem; padding: .1rem .45rem;
    border: 1px solid var(--global-divider-color); border-radius: 999px;
    color: var(--global-text-color-light); opacity: .75;
  }
</style>

<div class="proj-grid">

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">M.S. Thesis</span><span class="pc-period">2025 – Present</span></div>
    <h3>Clinical Faithfulness Auditing for Medical Image Classifiers</h3>
    <p class="pc-desc">M.S. thesis research on whether interpretable readouts from medical image classifiers correspond to clinically valid evidence, and on how that correspondence can be evaluated.</p>
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
  Contributed to an MSIT-funded project on AI-based gallbladder ultrasound diagnosis in collaboration with Ajou University Hospital; the work continued into my M.S. research. First-authored a reliability requirements study reporting malignant-class sensitivity of **0.452 before and 0.600 after** applying the requirements, a relative increase of about 33 percent on the study's internal evaluation (C1). Developed clinical-knowledge-guided modeling strategies using echogenicity, texture, lesion margin, wall features, and anatomical context. Presented center research at the ITRC Talent Development Fair in 2025 and 2026.

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

## Public Research Repositories

Selected repositories on [GitHub](https://github.com/sehyeony0518):

<div class="proj-grid">

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">ACK 2025 · C1</span></div>
    <h3>ultrasound-ai-reliability-requirements</h3>
    <p class="pc-desc">Paper explainer for the ACK 2025 ultrasound reliability requirements study: its framework, experimental setup and reported results. Implementation code is not included.</p>
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
    <p class="pc-desc">Research prototype inspired by SCID-5 Module J, with paraphrased criteria as a decision tree and follow-up questions when an answer is unclear. Clinician agreement and patient usability are unevaluated.</p>
    <a class="pc-link" href="https://github.com/sehyeony0518/scid5-module-j-agent" target="_blank" rel="noopener">→ github.com/sehyeony0518/scid5-module-j-agent</a>
  </div>

</div>

Published papers and manuscripts in preparation are listed on the [publications](/publications/) page.
