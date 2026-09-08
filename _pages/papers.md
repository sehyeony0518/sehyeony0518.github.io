---
layout: page
permalink: /papers/
title: paper reviews
description: "Papers I have studied closely: what they claim, how they show it, and what I take from them."
nav: true
nav_order: 11
---

{% include entry_list.liquid %}

{% assign reviews = site.papers | sort: "date" | reverse %}

{% assign venue_groups = "" | split: "," %}
{% for r in reviews %}
  {% capture vg %}{% include venue_group.liquid venue=r.venue %}{% endcapture %}
  {% assign vg = vg | strip %}
  {% unless venue_groups contains vg %}
    {% assign one_item = vg | split: "," %}
    {% assign venue_groups = venue_groups | concat: one_item %}
  {% endunless %}
{% endfor %}
{% assign venue_groups = venue_groups | sort %}

{% comment %}
  Venues are split into three rows: Conference, Journal, and Other (guidelines,
  protocols, preprints, none of which is either). Within Conference and Journal, a venue with
  only one review folds into that row's own "Other" chip so the row stays short
  as the library grows, except a short pinned list of venues significant enough
  to always keep visible on their own.
{% endcomment %}
{% assign pinned_venues = "IEEE ISBI,IEEE TMI" | split: "," %}
{% assign conf_main = "" | split: "," %}
{% assign journal_main = "" | split: "," %}
{% assign misc_main = "" | split: "," %}
{% assign conf_other_count = 0 %}
{% assign journal_other_count = 0 %}
{% assign misc_other_count = 0 %}
{% for v in venue_groups %}
  {% assign vcount = 0 %}
  {% for r in reviews %}
    {% capture vg %}{% include venue_group.liquid venue=r.venue %}{% endcapture %}
    {% assign vg = vg | strip %}
    {% if vg == v %}{% assign vcount = vcount | plus: 1 %}{% endif %}
  {% endfor %}
  {% capture cat %}{% include venue_category.liquid venue_group=v %}{% endcapture %}
  {% assign cat = cat | strip %}
  {% comment %} Each "Other" chip's count is a sum of papers (vcount), not a count of
    folded venues, because a venue with several papers must add its full weight, not 1. {% endcomment %}
  {% if cat == "conference" %}
    {% if vcount >= 2 or pinned_venues contains v %}
      {% assign one_item = v | split: "," %}
      {% assign conf_main = conf_main | concat: one_item %}
    {% else %}
      {% assign conf_other_count = conf_other_count | plus: vcount %}
    {% endif %}
  {% elsif cat == "journal" %}
    {% if vcount >= 2 or pinned_venues contains v %}
      {% assign one_item = v | split: "," %}
      {% assign journal_main = journal_main | concat: one_item %}
    {% else %}
      {% assign journal_other_count = journal_other_count | plus: vcount %}
    {% endif %}
  {% else %}
    {% if vcount >= 2 %}
      {% assign one_item = v | split: "," %}
      {% assign misc_main = misc_main | concat: one_item %}
    {% else %}
      {% assign misc_other_count = misc_other_count | plus: vcount %}
    {% endif %}
  {% endif %}
{% endfor %}
{% assign own_chip_groups = conf_main | concat: journal_main | concat: misc_main %}

{% if reviews.size > 0 %}
<div class="el-cats" id="venue-filter">
  <button type="button" class="el-cat active" data-venue="all">All <span class="el-cnt">{{ reviews.size }}</span></button>

  <span class="el-row-label">Conference</span>
  {%- for v in conf_main %}
    {%- assign v = v | strip %}
    {%- if v != "" %}
      {%- assign vcount = 0 %}
      {%- for r in reviews %}
        {%- capture vg %}{% include venue_group.liquid venue=r.venue %}{% endcapture %}
        {%- assign vg = vg | strip %}
        {%- if vg == v %}{% assign vcount = vcount | plus: 1 %}{% endif %}
      {%- endfor %}
  <button type="button" class="el-cat" data-venue="{{ v | slugify }}">{{ v }} <span class="el-cnt">{{ vcount }}</span></button>
    {%- endif %}
  {%- endfor %}
  {%- if conf_other_count > 0 %}
  <button type="button" class="el-cat" data-venue="conference-other">Other <span class="el-cnt">{{ conf_other_count }}</span></button>
  {%- endif %}

  <span class="el-row-label">Journal</span>
  {%- for v in journal_main %}
    {%- assign v = v | strip %}
    {%- if v != "" %}
      {%- assign vcount = 0 %}
      {%- for r in reviews %}
        {%- capture vg %}{% include venue_group.liquid venue=r.venue %}{% endcapture %}
        {%- assign vg = vg | strip %}
        {%- if vg == v %}{% assign vcount = vcount | plus: 1 %}{% endif %}
      {%- endfor %}
  <button type="button" class="el-cat" data-venue="{{ v | slugify }}">{{ v }} <span class="el-cnt">{{ vcount }}</span></button>
    {%- endif %}
  {%- endfor %}
  {%- if journal_other_count > 0 %}
  <button type="button" class="el-cat" data-venue="journal-other">Other <span class="el-cnt">{{ journal_other_count }}</span></button>
  {%- endif %}

  {%- if misc_main.size > 0 or misc_other_count > 0 %}
  <span class="el-row-label el-inline">Other</span>
  {%- for v in misc_main %}
    {%- assign v = v | strip %}
    {%- if v != "" %}
      {%- assign vcount = 0 %}
      {%- for r in reviews %}
        {%- capture vg %}{% include venue_group.liquid venue=r.venue %}{% endcapture %}
        {%- assign vg = vg | strip %}
        {%- if vg == v %}{% assign vcount = vcount | plus: 1 %}{% endif %}
      {%- endfor %}
  <button type="button" class="el-cat" data-venue="{{ v | slugify }}">{{ v }} <span class="el-cnt">{{ vcount }}</span></button>
    {%- endif %}
  {%- endfor %}
  {%- if misc_other_count > 0 %}
  <button type="button" class="el-cat" data-venue="other">Other <span class="el-cnt">{{ misc_other_count }}</span></button>
  {%- endif %}
  {%- endif %}
</div>
{% endif %}

<div class="el-list" id="paper-list">
  {% for r in reviews %}
    {% capture vg %}{% include venue_group.liquid venue=r.venue %}{% endcapture %}
    {% assign vg = vg | strip %}
    {% if own_chip_groups contains vg %}
      {% assign item_venue = vg | slugify %}
    {% else %}
      {% capture cat %}{% include venue_category.liquid venue_group=vg %}{% endcapture %}
      {% assign cat = cat | strip %}
      {% if cat == "conference" %}
        {% assign item_venue = "conference-other" %}
      {% elsif cat == "journal" %}
        {% assign item_venue = "journal-other" %}
      {% else %}
        {% assign item_venue = "other" %}
      {% endif %}
    {% endif %}
    <a class="el-row" data-venue="{{ item_venue }}" href="{{ r.url | relative_url }}">
      <div class="el-title">{{ r.title }}</div>
      {% if r.description %}<div class="el-sum">{{ r.description }}</div>{% endif %}
      {% if r.authors %}<div class="el-authors">{{ r.authors }}</div>{% endif %}
      <div class="el-foot">
        {% if r.venue %}<span class="el-tag">{{ r.venue }}</span>{% endif %}
        <span class="el-date">{{ r.date | date: '%B %-d, %Y' }}</span>
        <span class="el-read">Read &rarr;</span>
      </div>
    </a>
  {% endfor %}
</div>

{% if site.papers.size == 0 %}
  <p class="el-empty">Reviews are being added, the first ones will appear here soon.</p>
{% endif %}

<script>
  (function () {
    var filter = document.getElementById('venue-filter');
    if (!filter) return;
    var chips = filter.querySelectorAll('.el-cat');
    var items = document.querySelectorAll('#paper-list .el-row');
    filter.addEventListener('click', function (e) {
      var chip = e.target.closest('.el-cat');
      if (!chip) return;
      chips.forEach(function (c) { c.classList.remove('active'); });
      chip.classList.add('active');
      var v = chip.getAttribute('data-venue');
      items.forEach(function (item) {
        var show = (v === 'all') || (item.getAttribute('data-venue') === v);
        item.classList.toggle('el-hidden', !show);
      });
    });
  })();
</script>
