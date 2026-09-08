---
layout: page
permalink: /blog/
title: insights
description: Insights related to my research, the trustworthiness of medical AI models.
nav: true
nav_order: 10
---

{% include entry_list.liquid %}

{% assign posts_sorted = site.aiblog | sort: "date" | reverse %}

{%- assign tags = "" | split: "," -%}
{%- for post in posts_sorted -%}
  {%- assign t = post.tag | default: "Other" | strip -%}
  {%- unless tags contains t -%}{%- assign one = t | split: "," -%}{%- assign tags = tags | concat: one -%}{%- endunless -%}
{%- endfor -%}
{%- assign tags = tags | sort -%}

<div class="el-cats" id="ab-filter">
  <button type="button" class="el-cat active" data-k="all">All <span class="el-cnt">{{ posts_sorted | size }}</span></button>
  {%- for t in tags %}
  {%- assign n = posts_sorted | where: "tag", t | size %}
  <button type="button" class="el-cat" data-k="{{ t | slugify }}">{{ t }} <span class="el-cnt">{{ n }}</span></button>
  {%- endfor %}
</div>

<div class="el-list" id="ab-list">
  {% for post in posts_sorted %}
    {% assign t = post.tag | default: "Other" | strip %}
    <a class="el-row" data-k="{{ t | slugify }}" href="{{ post.url | relative_url }}">
      <div class="el-title">{{ post.title }}</div>
      {% if post.description %}<div class="el-sum">{{ post.description }}</div>{% endif %}
      <div class="el-foot">
        <span class="el-tag">{{ t }}</span>
        <span class="el-date">{{ post.date | date: '%B %-d, %Y' }}</span>
        <span class="el-read">Read &rarr;</span>
      </div>
    </a>
  {% endfor %}
</div>

{% if site.aiblog.size == 0 %}<p class="el-empty">Posts are being added, the first ones will appear here soon.</p>{% endif %}

<script>
  (function () {
    var f = document.getElementById('ab-filter');
    if (!f) return;
    var chips = f.querySelectorAll('.el-cat');
    var rows = document.querySelectorAll('#ab-list .el-row');
    f.addEventListener('click', function (e) {
      var c = e.target.closest('.el-cat');
      if (!c) return;
      chips.forEach(function (x) { x.classList.remove('active'); });
      c.classList.add('active');
      var k = c.getAttribute('data-k');
      rows.forEach(function (r) {
        r.classList.toggle('el-hidden', k !== 'all' && r.getAttribute('data-k') !== k);
      });
    });
  })();
</script>
