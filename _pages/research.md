---
layout: page
permalink: /research/
title: research
description: Trustworthy medical AI grounded in clinical evidence.
nav: true
nav_order: 7
---
<a href="/assets/pdf/cv-hwang.pdf" target="_blank" rel="noopener" style="display:inline-block; margin:.2rem 0 .8rem; padding:.4rem 1rem; border:1px solid var(--global-theme-color); border-radius:999px; color:var(--global-theme-color); text-decoration:none; font-size:.85rem; font-weight:600;">⬇ Download CV (PDF)</a>

I study the reliability of medical image classifiers, with a focus on ultrasound AI for gallbladder and hepatobiliary diagnosis. My research concerns the relationship between diagnostic performance and the evidence a model uses: whether a correct prediction is supported by clinically meaningful image characteristics, how that reliance can be examined, and where it becomes unstable.

I organize this work around two directions. In reliable medical AI models, I investigate clinical faithfulness auditing and study robustness under distribution shift. In clinical translation, I study the diseases, imaging findings, and diagnostic reasoning needed to define what an audit should check. My M.S. research at Ajou University, advised by Prof. Jung-Won Lee in the Embedded & Software Lab, connects these directions through ultrasound classification.

## Reliable Medical AI Models

### Diagnostic performance and shortcut reliance

A classifier can achieve good diagnostic accuracy while using features whose relationship with disease depends on how images were acquired or selected. Hospital-specific image formatting, measurement markers, and acquisition settings can become predictive when they occur unevenly across diagnostic groups. A random split may preserve these relationships in both training and test data, allowing an apparently successful evaluation to leave the underlying reliance unexamined.

I distinguish a cue's association with the target from the model's reliance on that cue. A marker-only baseline could establish that annotations contain predictive information. It would take additional comparisons, such as controlled marker edits and corresponding changes in classifier outputs, to establish sensitivity to those annotations. Conversely, an unfamiliar image feature is not automatically a shortcut. Its diagnostic relevance needs investigation before it can be classified as clinically inappropriate.

### Clinical faithfulness auditing

My current research focuses on clinical faithfulness: whether interpretable model readouts align with independently defined clinical factors. These factors may describe lesion morphology, diagnostic findings, or clinical severity. I am developing post-hoc approaches that examine trained classifiers without retraining them or requiring direct annotations of whether each explanation is faithful.

This constraint still requires clinical reference information. A diagnosis label alone cannot establish which evidence supports a prediction. I need factors defined independently of the model readout, with their provenance and measurement limitations recorded. Otherwise, an audit risks validating an explanation against information derived from the same model or against a descriptor that merely repeats the target label.

I use frequency-band, attention, and attribution analyses to examine model evidence. Each exposes a different quantity, and each requires a specific interpretation. Attention weights describe an internal weighting operation; attribution methods estimate an input's contribution under particular assumptions. Neither automatically establishes a clinically valid explanation. Frequency-band sensitivity can identify dependence on image structure at particular scales, but a frequency band has no fixed clinical meaning across acquisition conditions.

For an audit, I would specify the readout and clinical factor before measuring their relationship. Candidate measurements include the association between an evidence score and an ordinal clinical descriptor, attribution concentrated within independently delineated regions, and prediction changes following a controlled modification. Comparisons within diagnostic groups can help determine whether apparent alignment is explained mainly by the shared class label. Acquisition-stratified analyses can examine whether it persists under different recording conditions.

These measurements support different conclusions. Spatial overlap establishes localization, while a controlled edit tests sensitivity to the edited information. An edit may also damage relevant tissue or introduce an artifact. I therefore want audits to report agreement and disagreement across checks, with uncertainty estimated at the patient level when multiple images belong to one person. Clinical alignment provides evidence for a bounded claim about model behavior; it does not by itself establish a causal account of the decision.

### Robustness across clinical settings

I study generalisation as part of model reliability. Hospitals can differ in equipment, referral patterns, disease prevalence, image selection, and reference-label procedures. A performance change across sites may reflect several of these mechanisms simultaneously. External validation needs enough information about the evaluation population and acquisition process to investigate those differences.

In future evaluations, I would pair diagnostic performance with evidence audits across hospitals, devices, and patient groups. Relevant outcomes include malignant-class sensitivity at a specified threshold, calibration, and uncertainty within clinically meaningful subgroups. Patient-level separation is necessary to avoid leakage between related images. The model and preprocessing should remain fixed during an external test, with any subsequent adaptation evaluated separately. I would also examine whether stable aggregate performance conceals changes in which clinical findings or acquisition cues drive predictions.

## Clinical Translation

### Gallbladder and hepatobiliary evidence

Gallbladder ultrasound gives this work a concrete clinical setting. My published ACK 2025 paper examines data and model requirements for reliable ultrasound diagnosis. My ongoing work on clinical faithfulness and clinically grounded representation learning is listed as manuscripts in preparation on the [publications page](/publications/).

In my ultrasound work, I have explored clinically guided modeling using echogenicity, texture, lesion margin, wall features, and anatomical context. These descriptors require explicit definitions. Echogenicity needs a reference tissue and an appropriate comparison region. Texture depends on the spatial scale being measured. Margin assessment requires a visible boundary, while wall findings need their location and relationship to the lesion preserved.

Anatomical context determines how such observations should be interpreted. A representation centered tightly on a lesion may exclude its attachment to the wall or its relationship with surrounding liver tissue. A wider field can retain useful context while also admitting unrelated image content. I am interested in making these representation choices explicit enough that their diagnostic contribution can be examined.

### Acquisition variability and on-image markers

Ultrasound appearance depends on acquisition as well as tissue. Gain, imaging depth, probe orientation, and image processing can change brightness, apparent texture, and boundary visibility. Consequently, a numerical feature described as echogenicity or texture may partly measure acquisition conditions. Normalization can reduce some variability, but it may also remove relative contrast that matters clinically.

On-image markers introduce another source of ambiguity. Calipers and annotations may record a clinician's selection or measurement decision. If their presence or style differs across diagnostic groups, a classifier can receive information about the care process alongside the tissue image. Whether that information is appropriate depends on the intended point of use.

I would examine marker presence, location, and overlap with relevant anatomy before interpreting a removal experiment. Removing a marker can erase tissue, while restoration can introduce synthetic structure. A change in prediction therefore needs controls for the editing operation itself. This is especially relevant when auditing texture or frequency sensitivity, since the edit may alter exactly those image properties.

### Clinical knowledge as the audit reference

I study hepatobiliary medicine because clinical factors need a defensible interpretation before they can serve as audit references. Wall thickening, for example, has overlapping inflammatory, neoplastic, and systemic explanations. A familiar descriptor can be measured accurately while remaining insufficient for the diagnostic claim being tested.

My [study notes](/study/) cover anatomy, imaging findings, differential diagnosis, and clinical evaluation alongside machine learning. This study helps me distinguish an absent finding from one that is unassessable in the available view. It also clarifies what a selected still image cannot establish about an examination.

Reference standards need similar attention. Histopathology and longitudinal imaging provide different forms of evidence, and patients receiving surgery may differ systematically from those followed without intervention. I want these distinctions reflected in evaluation design, including how labels are assigned and which patients the resulting claims cover.

## Research Directions

I want to develop a reproducible post-hoc audit protocol that connects model readouts to independent clinical factors and tests plausible acquisition-related alternatives. My next priorities are to specify the scope of each measurement, examine disagreement between audit methods, and assess how conclusions depend on image editing and clinical-factor quality.

Alongside this, I want to investigate ultrasound representations whose clinical descriptors can be evaluated individually. During PhD study, I hope to extend these evaluations across acquisition settings and patient populations, with clearly defined diagnostic tasks and reference standards.

## Knowledge Graph {#graph}

Every study note, the categories above it, and the paper reviews and insights it shares citations with. A line is either the taxonomy or a source two pieces both cite. Hovering isolates a node's connections, dragging rearranges the layout, and clicking opens the piece.

{% include knowledge_graph.liquid full=true height=620 %}

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
