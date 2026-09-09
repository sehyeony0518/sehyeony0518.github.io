---
layout: page
permalink: /study/
title: study
description: "Notes on trustworthy AI and the clinical knowledge that informs my research."
nav: true
nav_order: 9
---

<style>

  .sl-intro { font-size: 1rem; line-height: 1.75; margin-bottom: .3rem; }
  .sl-intro a { font-weight: 600; }

  /* Two top-level tabs */
  .sl-tabs { display: flex; gap: .5rem; flex-wrap: wrap; margin: 1.5rem 0 0; }
  .sl-tab {
    flex: 1 1 260px; text-align: left; cursor: pointer;
    padding: .85rem 1.1rem; border-radius: 12px; background: none;
    border: 1px solid var(--global-divider-color); color: inherit;
    transition: border-color .15s ease, background .15s ease;
  }
  .sl-tab:hover { border-color: var(--global-theme-color); }
  .sl-tab.active { border-color: var(--global-theme-color); background: rgba(128,128,128,.06); }
  .sl-tab .sl-tab-name { display: block; font-size: 1.02rem; font-weight: 700; line-height: 1.3; }
  .sl-tab.active .sl-tab-name { color: var(--global-theme-color); }
  .sl-tab .sl-tab-desc { display: block; font-size: .8rem; line-height: 1.5; opacity: .65; margin-top: .2rem; }
  .sl-tab .sl-tab-cnt { font-size: .72rem; font-weight: 700; opacity: .5; font-variant-numeric: tabular-nums; }

  .sl-cats { display: flex; flex-wrap: wrap; gap: .3rem; margin: .9rem 0 .2rem; padding-bottom: .7rem;
             border-bottom: 2px solid var(--global-theme-color); }
  .sl-cat {
    padding: .18rem .6rem; border-radius: 999px; cursor: pointer; white-space: nowrap;
    border: 1px solid rgba(128,128,128,.32); background: none; color: inherit;
    font-size: .755rem; font-weight: 600; transition: all .15s ease;
  }
  .sl-cat:hover { border-color: var(--global-theme-color); color: var(--global-theme-color); }
  .sl-cat.active { background: var(--global-theme-color); border-color: var(--global-theme-color); color: #fff; }
  .sl-cat .sl-cat-cnt { opacity: .7; font-size: .69rem; margin-left: .1rem; font-variant-numeric: tabular-nums; }

  .sl-block { margin: 1.9rem 0 0; }
  .sl-block.sl-hidden, .sl-pane.sl-hidden { display: none; }
  .sl-block h2 {
    font-size: 1.12rem; margin: 0 0 .2rem; padding: 0; border: 0; line-height: 1.35;
  }
  .sl-sub {
    font-size: .68rem; font-weight: 800; letter-spacing: .08em; text-transform: uppercase;
    color: var(--global-text-color-light); opacity: .8; margin: 1.1rem 0 .1rem;
  }

  /* Note rows */
  .sl-note {
    display: block; text-decoration: none; color: inherit;
    padding: .78rem 0; border-bottom: 1px solid var(--global-divider-color);
  }
  a.sl-note:hover .sl-note-title { color: var(--global-theme-color); }
  a.sl-note:hover .sl-read { opacity: 1; }
  .sl-note-title { font-size: .97rem; font-weight: 650; line-height: 1.4; }
  .sl-note-sum { font-size: .845rem; line-height: 1.6; opacity: .68; margin-top: .12rem; max-width: 78ch; }
  .sl-note-foot { display: flex; align-items: baseline; gap: .6rem; flex-wrap: wrap; margin-top: .3rem; }
  .sl-tag {
    font-size: .68rem; font-weight: 700; letter-spacing: .04em;
    color: var(--global-text-color-light); opacity: .75;
  }
  .sl-read { margin-left: auto; font-size: .78rem; font-weight: 600; color: var(--global-theme-color); opacity: .8; white-space: nowrap; }

  /* Planned topics */
  .sl-planned { margin: .9rem 0 0; }
  .sl-planned > summary {
    cursor: pointer; list-style: none; display: inline-flex; align-items: center; gap: .4rem;
    font-size: .78rem; font-weight: 700; letter-spacing: .03em;
    color: var(--global-text-color-light); opacity: .8; padding: .3rem 0;
  }
  .sl-planned > summary::-webkit-details-marker { display: none; }
  .sl-planned > summary::before { content: "+"; font-weight: 800; opacity: .7; }
  .sl-planned[open] > summary::before { content: "\2212"; }
  .sl-planned > summary:hover { color: var(--global-theme-color); opacity: 1; }
  .sl-planned ul { list-style: none; margin: .35rem 0 .3rem; padding: 0; }
  @media (min-width: 760px) { .sl-planned ul { column-count: 2; column-gap: 2.4rem; } }
  .sl-planned li {
    break-inside: avoid; padding: .28rem 0; font-size: .84rem; line-height: 1.45;
    opacity: .62; border-bottom: 1px solid var(--global-divider-color);
  }
  .sl-empty { font-size: .87rem; opacity: .6; padding: .6rem 0; }
</style>

<p class="sl-intro">Notes on trustworthy AI and the clinical knowledge behind my research.</p>

{% assign all_notes = site.study | where_exp: "n", "n.category" %}
{% assign written_notes = all_notes | where: "written", true %}

<div class="sl-tabs" id="sl-tabs">
  {%- for t in site.data.study_sections.tabs %}
  {%- assign t_notes = all_notes | where: "tab", t.id %}
  {%- assign t_written = t_notes | where: "written", true %}
  <button type="button" class="sl-tab{% if forloop.first %} active{% endif %}" data-tab="{{ t.id }}">
    <span class="sl-tab-name">{{ t.title }}</span>
    <span class="sl-tab-desc">{{ t.description }}</span>
    <span class="sl-tab-cnt">{{ t_written | size }} of {{ t_notes | size }} written</span>
  </button>
  {%- endfor %}
</div>

{%- for t in site.data.study_sections.tabs %}
<div class="sl-pane{% unless forloop.first %} sl-hidden{% endunless %}" data-pane="{{ t.id }}">
  {%- assign t_cats = site.data.study_sections.categories | where: "tab", t.id %}
  <div class="sl-cats">
    {%- assign t_written = all_notes | where: "tab", t.id | where: "written", true %}
    <button type="button" class="sl-cat active" data-cat="all">All <span class="sl-cat-cnt">{{ t_written | size }}</span></button>
    {%- for c in t_cats %}
    {%- assign c_written = all_notes | where: "category", c.id | where: "written", true %}
    <button type="button" class="sl-cat" data-cat="{{ c.id }}">{{ c.title }} <span class="sl-cat-cnt">{{ c_written | size }}</span></button>
    {%- endfor %}
  </div>

  {%- for c in t_cats %}
  {%- assign c_notes = all_notes | where: "category", c.id | sort: "order" %}
  {%- assign c_written = c_notes | where: "written", true %}
  {%- assign c_planned = c_notes | where: "written", false %}
  <div class="sl-block" data-cat="{{ c.id }}">
    <h2 id="{{ c.id }}">{{ c.title }}</h2>
    {%- if c_written.size > 0 %}
      {%- assign last_sub = "" %}
      {%- for n in c_written %}
        {%- if n.subgroup and n.subgroup != last_sub %}
    <div class="sl-sub">{{ n.subgroup }}</div>
          {%- assign last_sub = n.subgroup %}
        {%- endif %}
    <a class="sl-note" href="{{ n.url | relative_url }}">
      <div class="sl-note-title">{{ n.title }}</div>
      <div class="sl-note-sum">{{ n.description }}</div>
      <div class="sl-note-foot">
        <span class="sl-tag">{{ c.title }}{% if n.subgroup %} · {{ n.subgroup }}{% endif %}</span>
        <span class="sl-read">Read note &rarr;</span>
      </div>
    </a>
      {%- endfor %}
    {%- else %}
    <p class="sl-empty">No notes written in this category yet.</p>
    {%- endif %}

    {%- if c_planned.size > 0 %}
    <details class="sl-planned">
      <summary>Planned topics ({{ c_planned | size }})</summary>
      <ul>
        {%- for n in c_planned %}
        <li>{{ n.title }}{% if n.subgroup %} <span style="opacity:.7">· {{ n.subgroup }}</span>{% endif %}</li>
        {%- endfor %}
      </ul>
    </details>
    {%- endif %}
  </div>
  {%- endfor %}
</div>
{%- endfor %}

<script>
  (function () {
    var tabsEl = document.getElementById('sl-tabs');
    if (!tabsEl) return;
    var tabs = tabsEl.querySelectorAll('.sl-tab');
    var panes = document.querySelectorAll('.sl-pane');

    function showTab(id, remember) {
      var found = false;
      tabs.forEach(function (b) {
        var on = b.getAttribute('data-tab') === id;
        b.classList.toggle('active', on);
        if (on) found = true;
      });
      if (!found) return false;
      panes.forEach(function (p) { p.classList.toggle('sl-hidden', p.getAttribute('data-pane') !== id); });
      if (remember) {
        try { sessionStorage.setItem('studyTab', id); } catch (e) {}
        if (history.replaceState) history.replaceState(null, '', location.pathname + '#' + id);
      }
      return true;
    }

    function showCat(pane, cat, remember) {
      pane.querySelectorAll('.sl-cat').forEach(function (b) {
        b.classList.toggle('active', b.getAttribute('data-cat') === cat);
      });
      pane.querySelectorAll('.sl-block').forEach(function (bl) {
        bl.classList.toggle('sl-hidden', cat !== 'all' && bl.getAttribute('data-cat') !== cat);
      });
      if (remember) { try { sessionStorage.setItem('studyCat:' + pane.getAttribute('data-pane'), cat); } catch (e) {} }
    }

    tabsEl.addEventListener('click', function (e) {
      var b = e.target.closest('.sl-tab');
      if (b) showTab(b.getAttribute('data-tab'), true);
    });

    panes.forEach(function (pane) {
      pane.addEventListener('click', function (e) {
        var b = e.target.closest('.sl-cat');
        if (b) showCat(pane, b.getAttribute('data-cat'), true);
      });
    });

    // Restore where the reader was: URL hash first, then the last visit
    var hash = (location.hash || '').replace('#', '');
    var stored = null;
    try { stored = sessionStorage.getItem('studyTab'); } catch (e) {}
    if (!hash || !showTab(hash, false)) { if (stored) showTab(stored, false); }
    panes.forEach(function (pane) {
      var c = null;
      try { c = sessionStorage.getItem('studyCat:' + pane.getAttribute('data-pane')); } catch (e) {}
      if (c) showCat(pane, c, false);
    });
  })();
</script>
