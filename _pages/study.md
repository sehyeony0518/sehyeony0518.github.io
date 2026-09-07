---
layout: page
permalink: /study/
title: study
description: "What I study and why: judging when medical AI deserves to be believed, and learning the medicine that makes that judgment possible."
nav: true
nav_order: 9
toc:
  sidebar: left
---

<style>
  .st-lede { font-size: 1.05rem; line-height: 1.8; }

  .st-claim {
    border-left: 3px solid var(--global-theme-color);
    padding: .1rem 0 .1rem 1.1rem; margin: 1.6rem 0 1.8rem;
    font-size: 1.06rem; line-height: 1.7; font-weight: 500;
  }
  .st-claim .st-claim-sub { display: block; margin-top: .5rem; font-size: .86rem; font-weight: 400; opacity: .6; }

  .st-qs { list-style: none; padding: 0; margin: 1rem 0 1.4rem; display: grid; grid-template-columns: 1fr; gap: .1rem; }
  @media (min-width: 800px) { .st-qs { grid-template-columns: 1fr 1fr; gap: .1rem 2rem; } }
  .st-qs li {
    padding: .5rem 0; border-bottom: 1px solid var(--global-divider-color);
    font-size: .93rem; line-height: 1.55; display: flex; gap: .7rem; align-items: baseline;
  }
  .st-qs li .st-qn {
    font-size: .72rem; font-weight: 800; font-variant-numeric: tabular-nums;
    color: var(--global-theme-color); opacity: .8; min-width: 1.1rem;
  }

  .st-branch {
    display: flex; align-items: baseline; gap: .7rem; flex-wrap: wrap;
    margin: 2.6rem 0 .2rem; padding-bottom: .5rem;
    border-bottom: 2px solid var(--global-theme-color);
  }
  .st-branch .st-bnum {
    font-size: .68rem; font-weight: 800; letter-spacing: .1em; text-transform: uppercase;
    padding: .16rem .6rem; border-radius: 999px;
    background: var(--global-theme-color); color: #fff;
  }
  .st-branch h2 { margin: 0 !important; font-size: 1.5rem; border: 0; }
  .st-branch-note { font-size: .92rem; line-height: 1.7; opacity: .75; margin: .9rem 0 0; }

  .st-grid { display: grid; grid-template-columns: 1fr; gap: 1rem; margin: 1.3rem 0 .5rem; }
  @media (min-width: 700px) { .st-grid { grid-template-columns: 1fr 1fr; } }
  .st-card {
    display: flex; flex-direction: column;
    border: 1px solid var(--global-divider-color); border-radius: 12px;
    padding: 1.1rem 1.2rem; background: var(--global-card-bg-color);
    transition: border-color .15s ease, box-shadow .15s ease;
  }
  .st-card:hover { border-color: var(--global-theme-color); box-shadow: 0 4px 18px rgba(0,0,0,.06); }
  .st-card h3 { font-size: 1rem; margin: 0 0 .5rem; line-height: 1.4; }
  .st-card p { font-size: .88rem; line-height: 1.68; opacity: .85; margin: 0 0 .75rem; flex-grow: 1; }
  .st-card .st-tags { display: flex; flex-wrap: wrap; gap: .32rem; }
  .st-card .st-tag {
    font-size: .69rem; padding: .12rem .5rem; border-radius: 6px;
    background: rgba(128,128,128,.13); opacity: .85;
  }

  .st-alloc { margin: 1.1rem 0 .5rem; }
  .st-alloc-row { display: grid; grid-template-columns: 3.1rem 1fr; gap: .8rem; align-items: center; margin-bottom: .8rem; }
  .st-alloc-pct { font-size: .84rem; font-weight: 700; font-variant-numeric: tabular-nums; text-align: right; opacity: .8; }
  .st-alloc-body .st-alloc-label { font-size: .89rem; line-height: 1.45; margin-bottom: .28rem; }
  .st-alloc-bar { height: 6px; border-radius: 999px; background: rgba(128,128,128,.16); overflow: hidden; }
  .st-alloc-bar span { display: block; height: 100%; border-radius: 999px; background: var(--global-theme-color); opacity: .8; }

  .st-not { border: 1px dashed var(--global-divider-color); border-radius: 12px; padding: 1.1rem 1.25rem; margin: 1.1rem 0; }
  .st-not ul { margin: .5rem 0 .7rem 1.1rem; padding: 0; }
  .st-not li { font-size: .9rem; line-height: 1.6; margin-bottom: .3rem; opacity: .85; }
  .st-not p { font-size: .9rem; line-height: 1.7; margin: 0; opacity: .85; }

  .st-link { display: grid; grid-template-columns: 1fr; gap: .1rem; margin: 1.1rem 0 .5rem; }
  .st-link-row { padding: .85rem 0; border-top: 1px solid var(--global-divider-color); }
  .st-link-row:last-child { border-bottom: 1px solid var(--global-divider-color); }
  .st-link-from { font-size: .72rem; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; color: var(--global-theme-color); }
  .st-link-to { font-size: .95rem; line-height: 1.6; margin-top: .18rem; }
</style>

<p class="st-lede">Writing code, implementing models, summarizing papers, and running experiments are all getting cheaper and faster. Judging whether a result deserves to be believed is not. That gap is what I have organized my studying around, and I expect it to widen rather than close.</p>

<div class="st-claim">
  I study how we can know whether medical AI models are relying on clinically meaningful evidence, and how to make that reliance measurable and auditable.
  <span class="st-claim-sub">When models were weak, the research question was whether the AI gets it right. As models get strong, the question moves to whether we should believe it.</span>
</div>

## The questions I am studying toward

Everything below exists to make me better at answering these. They are the questions that stay hard even when implementation becomes free.

<ol class="st-qs">
  <li><span class="st-qn">01</span><span>Which problem actually needs to be solved?</span></li>
  <li><span class="st-qn">02</span><span>Can this data answer that question at all?</span></li>
  <li><span class="st-qn">03</span><span>Why did the model reach this decision?</span></li>
  <li><span class="st-qn">04</span><span>Is the performance gain clinically meaningful?</span></li>
  <li><span class="st-qn">05</span><span>Has the model learned a shortcut instead?</span></li>
  <li><span class="st-qn">06</span><span>Does it stay reliable when the distribution changes?</span></li>
  <li><span class="st-qn">07</span><span>Is there enough evidence to use this on a patient?</span></li>
</ol>

Answering them takes two different kinds of knowledge, so my studying runs in two branches. The first is about the machinery of belief: statistics, evaluation, and interpretability. The second is about the domain that gives the belief its content: the medicine itself, without which "clinically meaningful evidence" is only a phrase.

<div class="st-branch">
  <span class="st-bnum">Branch 01</span>
  <h2 id="trustworthiness-and-reliability-of-ai">Trustworthiness and Reliability of AI</h2>
</div>

<p class="st-branch-note">The skill I want is not building one more architecture. It is being able to say what a piece of AI evidence is worth, and to defend that judgment with numbers. Most of this branch is older than deep learning and will outlive whatever replaces it.</p>

<div class="st-grid">

  <div class="st-card">
    <h3>Statistics, causal inference, and experimental design</h3>
    <p>Even when a model writes its own code, the statistical thinking stays mine to do. I work through hypothesis testing, confidence intervals, effect size, bootstrap, multiple comparisons, calibration, and Bayesian inference, and then into causal inference: confounding, selection bias, and dataset shift. The decisive question in a medical AI paper is rarely how well the model estimates <em>P(Y&thinsp;|&thinsp;X)</em>. It is why <em>X</em> predicts <em>Y</em> in the first place, and which part of that relationship collapses when the environment changes.</p>
    <div class="st-tags"><span class="st-tag">effect size</span><span class="st-tag">bootstrap</span><span class="st-tag">calibration</span><span class="st-tag">confounding</span><span class="st-tag">selection bias</span><span class="st-tag">dataset shift</span></div>
  </div>

  <div class="st-card">
    <h3>Evaluation science, not architecture design</h3>
    <p>An AUROC moving from 0.91 to 0.93 says almost nothing by itself. The questions that follow are the real work: is the difference clinically meaningful, how does the sensitivity and specificity tradeoff sit at the operating point that matters, does the gain hold in subgroups and on external data, what happens when the scanner or hospital or operator changes, is the model calibrated, which cases produce the false negatives, does the model's stated evidence agree with clinical evidence, and does the prediction move when an artifact is removed.</p>
    <div class="st-tags"><span class="st-tag">external validation</span><span class="st-tag">subgroup analysis</span><span class="st-tag">operating points</span><span class="st-tag">failure analysis</span></div>
  </div>

  <div class="st-card">
    <h3>Interpretability past the saliency map</h3>
    <p>Producing one Grad-CAM overlay is becoming a weak answer. I am studying representation probing, concept-based analysis, counterfactual evaluation, intervention and feature ablation, causal attribution, mechanistic interpretability, representation geometry, frequency analysis, and multimodal grounding. The move I care about is from "where did the model look" to "what information formed inside the model, and which part of it the decision actually used."</p>
    <div class="st-tags"><span class="st-tag">probing</span><span class="st-tag">concepts</span><span class="st-tag">counterfactuals</span><span class="st-tag">intervention</span><span class="st-tag">mechanistic</span></div>
  </div>

  <div class="st-card">
    <h3>Representation learning, robustness, and shift</h3>
    <p>What a model encodes decides what it can be trusted for. I study invariance and domain generalization, frequency and texture structure in learned features, the geometry of latent space, multimodal alignment, and how imaging foundation models behave when they leave the distribution they were built on. This is also where my ultrasound work lives, since scanner and operator variation is a distribution shift problem before it is anything else.</p>
    <div class="st-tags"><span class="st-tag">invariance</span><span class="st-tag">domain generalization</span><span class="st-tag">latent geometry</span><span class="st-tag">foundation models</span></div>
  </div>

  <div class="st-card">
    <h3>Agents and LLMs: the principles, not the frameworks</h3>
    <p>New agent frameworks, APIs, and prompting tricks will keep arriving, and following each one has no end. What lasts is the loop underneath, observe then reason then act then observe again, and the problems that loop creates: memory, tool selection, planning, verification, uncertainty, state management, feedback, and failure recovery. Those survive every renaming. At the Lunit hackathon I ended up working on the harness and control plane rather than the model itself, which is the same instinct.</p>
    <div class="st-tags"><span class="st-tag">planning</span><span class="st-tag">verification</span><span class="st-tag">uncertainty</span><span class="st-tag">failure recovery</span></div>
  </div>

  <div class="st-card">
    <h3>Mathematics that outlasts the tooling</h3>
    <p>Linear algebra: eigenvalues, SVD, projection, PCA. Probability: Bayes, expectation, variance, conditional independence. Optimization: gradients, regularization, constrained problems. Information theory: entropy, mutual information, KL divergence. Geometry: cosine similarity, manifolds, metric spaces, representation geometry. For work on representations, the combination of linear algebra, geometry, and statistics turns out to be unusually powerful.</p>
    <div class="st-tags"><span class="st-tag">SVD</span><span class="st-tag">Bayes</span><span class="st-tag">optimization</span><span class="st-tag">information theory</span><span class="st-tag">geometry</span></div>
  </div>

</div>

<div class="st-branch">
  <span class="st-bnum">Branch 02</span>
  <h2 id="medical-knowledge-for-clinical-translation">Medical Knowledge for Clinical Translation</h2>
</div>

<p class="st-branch-note">Machine learning knowledge is becoming less scarce. People who hold machine learning, ultrasound, clinical workflow, and diagnostic reasoning at the same time are still rare. This branch is the harder one for me, and the one that most changes what questions I am able to ask.</p>

<div class="st-grid">

  <div class="st-card">
    <h3>Hepatobiliary anatomy and disease</h3>
    <p>Gallbladder wall layers, biliary anatomy and its common variants, acute and chronic and xanthogranulomatous cholecystitis, adenomyomatosis, cholelithiasis and sludge, polypoid lesions and their malignant potential, gallbladder carcinoma and its staging, and the liver and biliary conditions that present alongside them. Knowing which diseases genuinely compete in a differential is what tells me what a classification label actually means.</p>
    <div class="st-tags"><span class="st-tag">gallbladder</span><span class="st-tag">biliary tract</span><span class="st-tag">differential diagnosis</span></div>
  </div>

  <div class="st-card">
    <h3>Ultrasound physics and image formation</h3>
    <p>Acoustic impedance and attenuation, gain and time gain compensation, the tradeoff between frequency and depth, focal zone, harmonic imaging, and the artifacts: posterior acoustic shadowing, comet tail and ring down, reverberation, side lobe. A great many things a network could learn from an ultrasound image are properties of the machine and the operator rather than of the patient. Telling those apart is a prerequisite for calling anything a shortcut.</p>
    <div class="st-tags"><span class="st-tag">acoustic physics</span><span class="st-tag">artifacts</span><span class="st-tag">acquisition variability</span></div>
  </div>

  <div class="st-card">
    <h3>The vocabulary radiologists actually use</h3>
    <p>Echogenicity and what it implies, wall thickening and whether its layered pattern is preserved, margin and interface, mural nodularity, vascularity on Doppler, whether a lesion moves with the patient, the sonographic Murphy sign, pericholecystic fluid, and the size thresholds that drive polyp management. What matters is not only each sign on its own but which signs are read together, and which combinations change the conclusion.</p>
    <div class="st-tags"><span class="st-tag">echogenicity</span><span class="st-tag">wall thickening</span><span class="st-tag">margin</span><span class="st-tag">Doppler</span></div>
  </div>

  <div class="st-card">
    <h3>Diagnostic reasoning and clinical workflow</h3>
    <p>The order in which findings are gathered, how prior probability from history and laboratory results enters the reading, when ultrasound leads on to CT or MRCP or endoscopic ultrasound, what the report is expected to state, and which decision follows from it. A model that ignores this ordering can be accurate and still be useless at the moment a decision is actually made.</p>
    <div class="st-tags"><span class="st-tag">reading order</span><span class="st-tag">pretest probability</span><span class="st-tag">reporting</span><span class="st-tag">referral pathway</span></div>
  </div>

  <div class="st-card">
    <h3>Clinical evidence standards</h3>
    <p>STARD, TRIPOD+AI, CLAIM, DECIDE-AI, QUADAS-2, and the guideline literature: how a diagnostic accuracy study should be designed and reported, what external and prospective validation actually require, and what level of evidence a claim needs before it is allowed anywhere near a patient. Reading these changed how I read results, including my own.</p>
    <div class="st-tags"><span class="st-tag">STARD</span><span class="st-tag">TRIPOD+AI</span><span class="st-tag">CLAIM</span><span class="st-tag">prospective validation</span></div>
  </div>

  <div class="st-card">
    <h3>Where the two branches meet</h3>
    <p>Once the clinical vocabulary becomes real to me, the research question changes shape. It stops being "the attention map looks reasonable" and becomes "is the model's decision supported by independent clinical evidence, and can that support be measured." That single change is the whole reason this branch exists, and it is the identity I am building my work around.</p>
    <div class="st-tags"><span class="st-tag">clinical faithfulness</span><span class="st-tag">evidence auditing</span></div>
  </div>

</div>

## Where my time goes

Roughly how I am dividing study time in the year leading up to doctoral applications. The proportions matter more than the exact numbers, and the first two rows are deliberately the largest.

<div class="st-alloc">
  <div class="st-alloc-row">
    <div class="st-alloc-pct">30%</div>
    <div class="st-alloc-body">
      <div class="st-alloc-label">Statistics, causal inference, and experimental design</div>
      <div class="st-alloc-bar"><span style="width:100%"></span></div>
    </div>
  </div>
  <div class="st-alloc-row">
    <div class="st-alloc-pct">25%</div>
    <div class="st-alloc-body">
      <div class="st-alloc-label">Trustworthy AI: shortcut learning, robustness, interpretability</div>
      <div class="st-alloc-bar"><span style="width:83%"></span></div>
    </div>
  </div>
  <div class="st-alloc-row">
    <div class="st-alloc-pct">20%</div>
    <div class="st-alloc-body">
      <div class="st-alloc-label">Medical imaging, ultrasound, and clinical diagnostic reasoning</div>
      <div class="st-alloc-bar"><span style="width:67%"></span></div>
    </div>
  </div>
  <div class="st-alloc-row">
    <div class="st-alloc-pct">15%</div>
    <div class="st-alloc-body">
      <div class="st-alloc-label">Representation learning, multimodal, and foundation models</div>
      <div class="st-alloc-bar"><span style="width:50%"></span></div>
    </div>
  </div>
  <div class="st-alloc-row">
    <div class="st-alloc-pct">10%</div>
    <div class="st-alloc-body">
      <div class="st-alloc-label">Agents, large language models, and AI systems</div>
      <div class="st-alloc-bar"><span style="width:33%"></span></div>
    </div>
  </div>
</div>

## What I deliberately do not optimize for

<div class="st-not">
  <ul>
    <li>Memorising a hundred CNN architectures</li>
    <li>Knowing the PyTorch API by heart</li>
    <li>CUDA implementation detail</li>
    <li>Model-specific prompting tricks that expire with the next release</li>
    <li>Every new agent framework as it appears</li>
  </ul>
  <p>Being able to implement something when I need it, with whatever tooling is current, is enough. The value of a researcher is shifting away from whether you can implement it and toward whether you know what should be implemented.</p>
</div>

## Study that turns into research

The rule I hold myself to is that nothing stays as reading. Each topic has to come back as a question about work I am actually doing.

<div class="st-link">
  <div class="st-link-row">
    <div class="st-link-from">Causal inference</div>
    <div class="st-link-to">Can my shortcut audit be expressed as a causal intervention rather than a correlation check?</div>
  </div>
  <div class="st-link-row">
    <div class="st-link-from">Calibration</div>
    <div class="st-link-to">How does the calibration of the current gallbladder classifier change across subgroups?</div>
  </div>
  <div class="st-link-row">
    <div class="st-link-from">Representation geometry</div>
    <div class="st-link-to">Can the geometry of the latent space be compared directly against independent clinical factors?</div>
  </div>
</div>

The reading itself is on the [paper reviews](/papers/) page, where I write up what each paper claims and what it leaves open, and the longer arguments are in [insights](/blog/). What this studying is for is on the [research](/research/) page.
