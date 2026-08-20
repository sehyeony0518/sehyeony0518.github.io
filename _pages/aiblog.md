---
layout: page
permalink: /blog/
title: blog
description: Notes on medical AI and digital healthcare.
nav: true
nav_order: 9
---

<style>
  .aiblog-list { margin-top: .5rem; }
  .aiblog-list .ab-item {
    display: block; text-decoration: none; color: inherit;
    padding: 1rem 1.15rem; margin-bottom: .8rem; border-radius: 12px;
    border: 1px solid rgba(128,128,128,.18); background: rgba(128,128,128,.035);
    transition: border-color .15s ease, transform .15s ease, box-shadow .15s ease;
  }
  .aiblog-list .ab-item:hover {
    border-color: var(--global-theme-color);
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(0,0,0,.07);
  }
  .aiblog-list .ab-date { font-size: .76rem; opacity: .5; font-variant-numeric: tabular-nums; }
  .aiblog-list .ab-title { font-weight: 700; font-size: 1.08rem; line-height: 1.4; margin-top: .15rem; }
  .aiblog-list .ab-desc { font-size: .86rem; opacity: .7; margin-top: .25rem; line-height: 1.55; }
</style>

<p style="opacity:.75; line-height:1.7; margin:0 0 1.4rem;">
Occasional posts on medical AI and digital healthcare — paper notes, trustworthy-AI perspectives, and things I learn while building diagnostic models.
</p>

<div class="aiblog-list">
  {% assign posts_sorted = site.aiblog | sort: "date" | reverse %}
  {% for post in posts_sorted %}
    <a class="ab-item" href="{{ post.url | relative_url }}">
      <div class="ab-date">{{ post.date | date: '%B %d, %Y' }}</div>
      <div class="ab-title">{{ post.title }}</div>
      {% if post.description %}<div class="ab-desc">{{ post.description }}</div>{% endif %}
    </a>
  {% endfor %}
</div>
