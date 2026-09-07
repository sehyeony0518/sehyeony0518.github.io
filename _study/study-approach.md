---
layout: page
title: "Study Approach"
description: "How I decide what to study, where the time goes, and what I deliberately leave alone."
source: "Independent study"
written: true
updated: "2026-09-08"
---

<style>
  .st-claim { border-left: 3px solid var(--global-theme-color); padding: .1rem 0 .1rem 1.1rem;
    margin: 1.4rem 0 1.7rem; font-size: 1.05rem; line-height: 1.7; font-weight: 500; }
  .st-claim .st-claim-sub { display: block; margin-top: .5rem; font-size: .85rem; font-weight: 400; opacity: .6; }
  .st-qs { list-style: none; padding: 0; margin: .9rem 0 2rem; display: grid; grid-template-columns: 1fr; }
  @media (min-width: 820px) { .st-qs { grid-template-columns: 1fr 1fr; column-gap: 2.2rem; } }
  .st-qs li { padding: .48rem 0; border-bottom: 1px solid var(--global-divider-color);
    font-size: .92rem; line-height: 1.55; display: flex; gap: .7rem; align-items: baseline; }
  .st-qs li .st-qn { font-size: .71rem; font-weight: 800; font-variant-numeric: tabular-nums;
    color: var(--global-theme-color); opacity: .8; min-width: 1.1rem; }
  .st-alloc { margin: 1.1rem 0 .5rem; }
  .st-alloc-row { display: grid; grid-template-columns: 3.1rem 1fr; gap: .8rem; align-items: center; margin-bottom: .8rem; }
  .st-alloc-pct { font-size: .84rem; font-weight: 700; font-variant-numeric: tabular-nums; text-align: right; opacity: .8; }
  .st-alloc-body .st-alloc-label { font-size: .88rem; line-height: 1.45; margin-bottom: .28rem; }
  .st-alloc-bar { height: 6px; border-radius: 999px; background: rgba(128,128,128,.16); overflow: hidden; }
  .st-alloc-bar span { display: block; height: 100%; border-radius: 999px; background: var(--global-theme-color); opacity: .8; }
  .st-not { border: 1px dashed var(--global-divider-color); border-radius: 12px; padding: 1.05rem 1.25rem; margin: 1.1rem 0; }
  .st-not ul { margin: .5rem 0 .7rem 1.1rem; padding: 0; }
  .st-not li { font-size: .89rem; line-height: 1.6; margin-bottom: .28rem; opacity: .85; }
  .st-not p { font-size: .89rem; line-height: 1.7; margin: 0; opacity: .85; }
  .st-link-row { padding: .8rem 0; border-top: 1px solid var(--global-divider-color); }
  .st-link-row:last-child { border-bottom: 1px solid var(--global-divider-color); }
  .st-link-from { font-size: .71rem; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; color: var(--global-theme-color); }
  .st-link-to { font-size: .94rem; line-height: 1.6; margin-top: .16rem; }
</style>

Writing code, implementing models, summarizing papers, and running experiments all keep getting cheaper and faster. Judging whether a result deserves to be believed does not. That gap is what I have organized my studying around, and I expect it to widen rather than close.

<div class="st-claim">
  I study how we can know whether medical AI models are relying on clinically meaningful evidence, and how to make that reliance measurable and auditable.
  <span class="st-claim-sub">When models were weak, the research question was whether the AI gets it right. As models get strong, the question moves to whether we should believe it.</span>
</div>

## The questions I am studying toward

Everything in these notes exists to make me better at answering seven questions. They are the ones that stay hard even after implementation becomes free.

<ol class="st-qs">
  <li><span class="st-qn">01</span><span>Which problem actually needs to be solved?</span></li>
  <li><span class="st-qn">02</span><span>Can this data answer that question at all?</span></li>
  <li><span class="st-qn">03</span><span>Why did the model reach this decision?</span></li>
  <li><span class="st-qn">04</span><span>Is the performance gain clinically meaningful?</span></li>
  <li><span class="st-qn">05</span><span>Has the model learned a shortcut instead?</span></li>
  <li><span class="st-qn">06</span><span>Does it stay reliable when the distribution changes?</span></li>
  <li><span class="st-qn">07</span><span>Is there enough evidence to use this on a patient?</span></li>
</ol>

## Where my time goes

Roughly how the study time divides in the year leading up to doctoral applications. The proportions matter more than the exact numbers, and the first two rows are deliberately the largest.

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
    <li>Memorizing a hundred CNN architectures</li>
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

The notes themselves are in [Trustworthy AI](/study/#trustworthy-ai) and [Clinical Medicine](/study/#clinical-medicine).
