---
layout: page
permalink: /papers/
title: paper reviews
description: Papers I have studied closely — what they claim, how they show it, and what I take from them.
nav: true
nav_order: 10
---

<style>
  .venue-filter { display: flex; flex-wrap: wrap; gap: .45rem; margin: .3rem 0 1.3rem; }
  .venue-filter .vf-chip {
    display: inline-block; padding: .22rem .7rem; border-radius: 999px;
    border: 1px solid rgba(128,128,128,.35); font-size: .8rem; font-weight: 600;
    background: none; color: inherit; cursor: pointer; transition: all .15s ease;
  }
  .venue-filter .vf-chip:hover { border-color: var(--global-theme-color); color: var(--global-theme-color); }
  .venue-filter .vf-chip.active {
    background: var(--global-theme-color); border-color: var(--global-theme-color); color: #fff;
  }
  .venue-filter .vf-chip .vf-cnt { opacity: .75; font-size: .72rem; margin-left: .15rem; }

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
  .paper-list .pr-item.pr-hidden { display: none; }
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

{% comment %} Venues with only one review get folded into a single "Other" chip, so the filter row stays short as the library grows. {% endcomment %}
{% assign main_groups = "" | split: "," %}
{% assign other_count = 0 %}
{% for v in venue_groups %}
  {% assign vcount = 0 %}
  {% for r in reviews %}
    {% capture vg %}{% include venue_group.liquid venue=r.venue %}{% endcapture %}
    {% assign vg = vg | strip %}
    {% if vg == v %}{% assign vcount = vcount | plus: 1 %}{% endif %}
  {% endfor %}
  {% if vcount >= 2 %}
    {% assign one_item = v | split: "," %}
    {% assign main_groups = main_groups | concat: one_item %}
  {% else %}
    {% assign other_count = other_count | plus: 1 %}
  {% endif %}
{% endfor %}

{% if reviews.size > 0 %}
<div class="venue-filter" id="venue-filter">
  <button type="button" class="vf-chip active" data-venue="all">All <span class="vf-cnt">{{ reviews.size }}</span></button>
  {% for v in main_groups %}
    {% assign v = v | strip %}
    {% if v != "" %}
      {% assign vcount = 0 %}
      {% for r in reviews %}
        {% capture vg %}{% include venue_group.liquid venue=r.venue %}{% endcapture %}
        {% assign vg = vg | strip %}
        {% if vg == v %}{% assign vcount = vcount | plus: 1 %}{% endif %}
      {% endfor %}
      <button type="button" class="vf-chip" data-venue="{{ v | slugify }}">{{ v }} <span class="vf-cnt">{{ vcount }}</span></button>
    {% endif %}
  {% endfor %}
  {% if other_count > 0 %}
    <button type="button" class="vf-chip" data-venue="other">Other <span class="vf-cnt">{{ other_count }}</span></button>
  {% endif %}
</div>
{% endif %}

<div class="paper-list" id="paper-list">
  {% for r in reviews %}
    {% capture vg %}{% include venue_group.liquid venue=r.venue %}{% endcapture %}
    {% assign vg = vg | strip %}
    {% if main_groups contains vg %}
      {% assign item_venue = vg | slugify %}
    {% else %}
      {% assign item_venue = "other" %}
    {% endif %}
    <a class="pr-item" data-venue="{{ item_venue }}" href="{{ r.url | relative_url }}">
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

<script>
  (function () {
    var filter = document.getElementById('venue-filter');
    if (!filter) return;
    var chips = filter.querySelectorAll('.vf-chip');
    var items = document.querySelectorAll('#paper-list .pr-item');
    filter.addEventListener('click', function (e) {
      var chip = e.target.closest('.vf-chip');
      if (!chip) return;
      chips.forEach(function (c) { c.classList.remove('active'); });
      chip.classList.add('active');
      var v = chip.getAttribute('data-venue');
      items.forEach(function (item) {
        var show = (v === 'all') || (item.getAttribute('data-venue') === v);
        item.classList.toggle('pr-hidden', !show);
      });
    });
  })();
</script>
