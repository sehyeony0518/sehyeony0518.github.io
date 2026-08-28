---
layout: page
permalink: /papers/
title: paper reviews
description: Papers I have studied closely — what they claim, how they show it, and what I take from them.
nav: true
nav_order: 10
---

<style>
  .paper-list { margin-top: .5rem; display: grid; grid-template-columns: 1fr; gap: .8rem; }
  @media (min-width: 576px) { .paper-list { grid-template-columns: 1fr 1fr; } }
  .paper-list .pr-item {
    display: block; text-decoration: none; color: inherit;
    padding: 1rem 1.15rem; border-radius: 12px;
    border: 1px solid rgba(128,128,128,.18); background: rgba(128,128,128,.035);
    transition: border-color .15s ease, transform .15s ease, box-shadow .15s ease;
  }
  .paper-list .pr-item:hover {
    border-color: var(--global-theme-color);
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(0,0,0,.07);
  }
  .paper-list .pr-meta { display: flex; align-items: baseline; gap: .55rem; }
  .paper-list .pr-venue {
    font-size: .72rem; font-weight: 800; letter-spacing: .06em; text-transform: uppercase;
    color: var(--global-theme-color); white-space: nowrap;
  }
  .paper-list .pr-date { font-size: .76rem; opacity: .5; font-variant-numeric: tabular-nums; }
  .paper-list .pr-title { font-weight: 700; font-size: 1.08rem; line-height: 1.4; margin-top: .15rem; }
  .paper-list .pr-authors { font-size: .8rem; opacity: .55; margin-top: .15rem; font-style: italic; }
  .paper-list .pr-desc { font-size: .86rem; opacity: .7; margin-top: .25rem; line-height: 1.55; }
  .paper-empty { opacity: .6; line-height: 1.7; margin-top: 1rem; }
</style>

<div class="paper-list">
  {% assign reviews = site.papers | sort: "date" | reverse %}
  {% for r in reviews %}
    <a class="pr-item" href="{{ r.url | relative_url }}">
      <div class="pr-meta">
        {% if r.venue %}<span class="pr-venue">{{ r.venue }}</span>{% endif %}
        <span class="pr-date">{{ r.date | date: '%B %d, %Y' }}</span>
      </div>
      <div class="pr-title">{{ r.title | split: ": " | first }}</div>
      {% if r.authors %}<div class="pr-authors">{{ r.authors }}</div>{% endif %}
      {% if r.description %}<div class="pr-desc">{{ r.description }}</div>{% endif %}
    </a>
  {% endfor %}
</div>

{% if site.papers.size == 0 %}
  <p class="paper-empty">Reviews are being added — the first ones will appear here soon.</p>
{% endif %}
