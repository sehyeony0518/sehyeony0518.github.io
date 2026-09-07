---
layout: page
permalink: /study/
title: study
description: "What I am studying and why: judging when medical AI deserves to be believed, and learning the medicine that makes that judgment possible."
nav: true
nav_order: 9
---

<style>
  .container.mt-5 { max-width: 1280px; }

  .st-lede { font-size: 1.04rem; line-height: 1.8; }
  .st-claim {
    border-left: 3px solid var(--global-theme-color);
    padding: .1rem 0 .1rem 1.1rem; margin: 1.5rem 0 1.7rem;
    font-size: 1.05rem; line-height: 1.7; font-weight: 500;
  }
  .st-claim .st-claim-sub { display: block; margin-top: .5rem; font-size: .85rem; font-weight: 400; opacity: .6; }

  .st-qs { list-style: none; padding: 0; margin: .9rem 0 2.2rem; display: grid; grid-template-columns: 1fr; }
  @media (min-width: 820px) { .st-qs { grid-template-columns: 1fr 1fr; column-gap: 2.2rem; } }
  .st-qs li {
    padding: .48rem 0; border-bottom: 1px solid var(--global-divider-color);
    font-size: .92rem; line-height: 1.55; display: flex; gap: .7rem; align-items: baseline;
  }
  .st-qs li .st-qn {
    font-size: .71rem; font-weight: 800; font-variant-numeric: tabular-nums;
    color: var(--global-theme-color); opacity: .8; min-width: 1.1rem;
  }

  /* Section picker: label on the left, selectable sections on the right */
  .tp-bar {
    position: sticky; top: 0; z-index: 4;
    display: flex; align-items: baseline; flex-wrap: wrap; gap: .5rem 1rem;
    padding: .7rem 0 .55rem; margin: .4rem 0 0;
    background: var(--global-bg-color);
    border-bottom: 2px solid var(--global-theme-color);
  }
  .tp-bar-title { font-size: 1.02rem; font-weight: 700; line-height: 1.35; }
  .tp-bar-title .tp-bar-branch {
    display: block; font-size: .66rem; font-weight: 800; letter-spacing: .09em;
    text-transform: uppercase; color: var(--global-theme-color); opacity: .85; margin-bottom: .12rem;
  }
  .tp-chips { margin-left: auto; display: flex; flex-wrap: wrap; gap: .32rem; justify-content: flex-end; }
  .tp-chip {
    display: inline-block; padding: .2rem .62rem; border-radius: 999px;
    border: 1px solid rgba(128,128,128,.35); font-size: .76rem; font-weight: 600;
    background: none; color: inherit; cursor: pointer; transition: all .15s ease; white-space: nowrap;
  }
  .tp-chip:hover { border-color: var(--global-theme-color); color: var(--global-theme-color); }
  .tp-chip.active { background: var(--global-theme-color); border-color: var(--global-theme-color); color: #fff; }
  .tp-chip .tp-cnt { opacity: .7; font-size: .69rem; margin-left: .12rem; font-variant-numeric: tabular-nums; }

  .tp-sec { margin: 2rem 0 0; }
  .tp-sec.tp-hidden { display: none; }
  .tp-head { display: flex; align-items: baseline; gap: .6rem; flex-wrap: wrap; }
  .tp-head h3 { font-size: 1.16rem; margin: 0; line-height: 1.35; }
  .tp-branch {
    font-size: .62rem; font-weight: 800; letter-spacing: .09em; text-transform: uppercase;
    padding: .13rem .5rem; border-radius: 999px; white-space: nowrap;
    border: 1px solid var(--global-theme-color); color: var(--global-theme-color);
  }
  .tp-branch.tp-b2 { background: var(--global-theme-color); color: #fff; }
  .tp-note { font-size: .88rem; line-height: 1.7; opacity: .72; margin: .45rem 0 .3rem; max-width: 62ch; }

  .tp-list { margin: .5rem 0 0; padding-left: 1.5rem; }
  @media (min-width: 900px) { .tp-list { column-count: 2; column-gap: 2.6rem; } }
  .tp-list li {
    break-inside: avoid; padding: .5rem 0; line-height: 1.45;
    border-bottom: 1px solid var(--global-divider-color);
  }
  .tp-list li::marker { font-size: .72rem; color: var(--global-text-color-light); font-variant-numeric: tabular-nums; }
  .tp-list .tp-t { display: block; font-size: .9rem; font-weight: 600; line-height: 1.4; }
  .tp-list a.tp-t { color: inherit; text-decoration: none; }
  .tp-list a.tp-t:hover { color: var(--global-theme-color); text-decoration: underline; }
  .tp-list a.tp-t::after { content: " \2192"; opacity: .35; font-weight: 400; }
  .tp-list .tp-todo { color: var(--global-text-color-light); opacity: .72; font-weight: 500; }
  .tp-list .tp-sum { display: block; font-size: .8rem; line-height: 1.55; opacity: .62; margin-top: .12rem; }

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

<p class="st-lede">Writing code, implementing models, summarizing papers, and running experiments all keep getting cheaper and faster. Judging whether a result deserves to be believed does not. That gap is what I have organized my studying around, and I expect it to widen rather than close.</p>

<div class="st-claim">
  I study how we can know whether medical AI models are relying on clinically meaningful evidence, and how to make that reliance measurable and auditable.
  <span class="st-claim-sub">When models were weak, the research question was whether the AI gets it right. As models get strong, the question moves to whether we should believe it.</span>
</div>

<p class="st-lede">Everything below exists to make me better at answering seven questions. They are the ones that stay hard even after implementation becomes free.</p>

<ol class="st-qs">
  <li><span class="st-qn">01</span><span>Which problem actually needs to be solved?</span></li>
  <li><span class="st-qn">02</span><span>Can this data answer that question at all?</span></li>
  <li><span class="st-qn">03</span><span>Why did the model reach this decision?</span></li>
  <li><span class="st-qn">04</span><span>Is the performance gain clinically meaningful?</span></li>
  <li><span class="st-qn">05</span><span>Has the model learned a shortcut instead?</span></li>
  <li><span class="st-qn">06</span><span>Does it stay reliable when the distribution changes?</span></li>
  <li><span class="st-qn">07</span><span>Is there enough evidence to use this on a patient?</span></li>
</ol>

<p class="st-lede">Answering them takes two different kinds of knowledge, so the topics run in two branches. <strong>Branch 01</strong> is the machinery of belief: trustworthiness, the advancing frontier, and research methodology. <strong>Branch 02</strong> is the domain that gives the belief its content, the medicine itself, without which clinically meaningful evidence is only a phrase. Pick a section to read its list.</p>

<div class="tp-bar" id="tp-bar">
  <div class="tp-bar-title" id="tp-title"><span class="tp-bar-branch" id="tp-title-branch">Both branches</span>All topics</div>
  <div class="tp-chips" id="tp-chips">
      <button type="button" class="tp-chip active" data-sec="all">All <span class="tp-cnt">{{ site.study | size }}</span></button>
      {%- for sec in site.data.study_sections %}
      <button type="button" class="tp-chip" data-sec="{{ sec.id }}" data-title="{{ sec.title }}" data-branch="{{ sec.branch }}">{{ sec.id }}. {{ sec.short }} <span class="tp-cnt">{{ sec.count }}</span></button>
      {%- endfor %}
  </div>
</div>

<div id="tp-sections">
{%- for sec in site.data.study_sections %}
  {%- assign items = site.study | where: "section", sec.id | sort: "order" %}
  <section class="tp-sec" data-sec="{{ sec.id }}">
    <div class="tp-head">
      <span class="tp-branch{% if sec.branch == 'Branch 02' %} tp-b2{% endif %}">{{ sec.branch }}</span>
      <h3 id="section-{{ sec.id }}">{{ sec.id }}. {{ sec.title }}</h3>
    </div>
    <p class="tp-note">{{ sec.note }}</p>
    <ol class="tp-list">
      {%- for it in items %}
      <li>
        {%- if it.written %}
        <a class="tp-t" href="{{ it.url | relative_url }}">{{ it.title }}</a>
        {%- else %}
        <span class="tp-t tp-todo">{{ it.title }}</span>
        {%- endif %}
        <span class="tp-sum">{{ it.description }}</span>
      </li>
      {%- endfor %}
    </ol>
  </section>
{%- endfor %}
</div>

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

<script>
  (function () {
    var bar = document.getElementById('tp-bar');
    if (!bar) return;
    var chips = bar.querySelectorAll('.tp-chip');
    var secs = document.querySelectorAll('#tp-sections .tp-sec');
    var title = document.getElementById('tp-title');
    var branch = document.getElementById('tp-title-branch');

    function select(key) {
      chips.forEach(function (c) { c.classList.toggle('active', c.getAttribute('data-sec') === key); });
      secs.forEach(function (s) { s.classList.toggle('tp-hidden', key !== 'all' && s.getAttribute('data-sec') !== key); });
      var chip = bar.querySelector('.tp-chip[data-sec="' + key + '"]');
      if (key === 'all') {
        branch.textContent = 'Both branches';
        title.lastChild.nodeValue = 'All topics';
      } else if (chip) {
        branch.textContent = chip.getAttribute('data-branch');
        title.lastChild.nodeValue = key + '. ' + chip.getAttribute('data-title');
      }
      if (history.replaceState) {
        history.replaceState(null, '', key === 'all' ? location.pathname : location.pathname + '#section-' + key);
      }
    }

    bar.addEventListener('click', function (e) {
      var chip = e.target.closest('.tp-chip');
      if (!chip) return;
      select(chip.getAttribute('data-sec'));
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    var hash = (location.hash || '').replace('#section-', '');
    if (hash && bar.querySelector('.tp-chip[data-sec="' + hash + '"]')) select(hash);
  })();
</script>
