---
layout: page
permalink: /prayer/
title: prayer
description: Mission2035 기도편지 — 부르심의 여정을 함께 기도해 주세요.
nav: true
nav_order: 5
---

<style>
  .pl-intro { opacity: .78; line-height: 1.75; margin: 0 0 1.6rem; }
  .pl-list { display: flex; flex-direction: column; gap: 1rem; }
  .pl-card {
    display: flex; gap: 1.1rem; align-items: stretch;
    text-decoration: none; color: inherit;
    border: 1px solid rgba(128,128,128,.18); border-radius: 14px;
    overflow: hidden; background: rgba(128,128,128,.03);
    transition: border-color .15s ease, transform .15s ease, box-shadow .15s ease;
  }
  .pl-card:hover {
    border-color: var(--global-theme-color);
    transform: translateY(-2px);
    box-shadow: 0 6px 22px rgba(0,0,0,.07);
  }
  .pl-card .pl-thumb {
    flex: 0 0 34%; max-width: 200px; background: rgba(128,128,128,.1);
    background-size: cover; background-position: center;
  }
  @media (max-width: 520px) { .pl-card { flex-direction: column; } .pl-card .pl-thumb { flex-basis: 150px; max-width: none; height: 150px; } }
  .pl-card .pl-content { padding: 1.1rem 1.2rem; display: flex; flex-direction: column; }
  .pl-card .pl-badge {
    align-self: flex-start; font-size: .68rem; font-weight: 800; letter-spacing: .04em;
    padding: .16rem .55rem; border-radius: 999px;
    background: var(--global-theme-color); color: #fff; margin-bottom: .5rem;
  }
  .pl-card h3 { margin: 0 0 .4rem; font-size: 1.12rem; line-height: 1.35; }
  .pl-card .pl-sum { font-size: .86rem; opacity: .7; line-height: 1.55; margin: 0 0 .6rem; }
  .pl-card .pl-read { font-size: .8rem; color: var(--global-theme-color); margin-top: auto; }
</style>

<p class="pl-intro">
<strong>Mission2035 기도편지</strong>입니다. 하나님께서 이 부르심의 길을 어떻게 인도하시는지, 어떤 훈련과 준비를 거치고 있는지, 그리고 함께 기도해 주셔야 할 내용을 가능할 때마다 나눕니다. 각 편지 안에서 <strong>링크 공유하기</strong> 버튼으로 동역자들과 나눌 수 있습니다.
</p>

<div class="pl-list">
  {% assign letters = site.prayer | sort: 'date' | reverse %}
  {% for letter in letters %}
    <a class="pl-card" href="{{ letter.url | relative_url }}">
      {% if letter.cover %}
        <div class="pl-thumb" style="background-image:url('{{ '/assets/img/gallery/' | append: letter.cover | append: '.jpg' | relative_url }}');"></div>
      {% endif %}
      <div class="pl-content">
        <span class="pl-badge">{{ letter.issue }}</span>
        <h3>{{ letter.title | remove: letter.issue | remove: ' · ' | strip }}</h3>
        {% if letter.summary %}<p class="pl-sum">{{ letter.summary }}</p>{% endif %}
        <span class="pl-read">편지 읽기 &rarr;</span>
      </div>
    </a>
  {% endfor %}
</div>
