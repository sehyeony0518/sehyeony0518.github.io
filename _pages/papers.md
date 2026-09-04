---
layout: page
permalink: /papers/
title: paper reviews
description: "Papers I have studied closely: what they claim, how they show it, and what I take from them."
nav: true
nav_order: 10
---

<style>
  /* Widen just this page's content column so a 4-up card grid has room to breathe */
  .container.mt-5 { max-width: 1400px; }

  .venue-filter { margin: .3rem 0 1.3rem; }
  .venue-filter .vf-row { display: flex; flex-wrap: wrap; align-items: center; gap: .45rem; margin-bottom: .5rem; }
  .venue-filter .vf-row-label {
    display: block; width: 100%;
    font-size: .68rem; font-weight: 800; letter-spacing: .08em; text-transform: uppercase;
    color: var(--global-text-color-light); opacity: .75; margin: .6rem 0 .1rem;
  }
  .venue-filter .vf-row-label:first-child { margin-top: 0; }
  /* Short trailing group sits on one line: label in the first column, chips in the second */
  .venue-filter .vf-row-label.vf-inline { width: auto; margin: 0 .35rem 0 0; }
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
  @media (min-width: 576px) { .paper-list { grid-template-columns: repeat(2, 1fr); } }
  @media (min-width: 900px) { .paper-list { grid-template-columns: repeat(3, 1fr); } }
  @media (min-width: 1200px) { .paper-list { grid-template-columns: repeat(4, 1fr); } }
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

{% comment %}
  Venues are split into three rows: Conference, Journal, and Other (guidelines,
  protocols, preprints — neither). Within Conference and Journal, a venue with
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
    folded venues — a venue with several papers must add its full weight, not 1. {% endcomment %}
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
<div class="venue-filter" id="venue-filter">
  <div class="vf-row">
    <button type="button" class="vf-chip active" data-venue="all">All <span class="vf-cnt">{{ reviews.size }}</span></button>
  </div>

  <div class="vf-row-label">Conference</div>
  <div class="vf-row">
    {% for v in conf_main %}
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
    {% if conf_other_count > 0 %}
      <button type="button" class="vf-chip" data-venue="conference-other">Other <span class="vf-cnt">{{ conf_other_count }}</span></button>
    {% endif %}
  </div>

  <div class="vf-row-label">Journal</div>
  <div class="vf-row">
    {% for v in journal_main %}
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
    {% if journal_other_count > 0 %}
      <button type="button" class="vf-chip" data-venue="journal-other">Other <span class="vf-cnt">{{ journal_other_count }}</span></button>
    {% endif %}
  </div>

  {% if misc_main.size > 0 or misc_other_count > 0 %}
    <div class="vf-row">
      <span class="vf-row-label vf-inline">Other</span>
      {% for v in misc_main %}
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
      {% if misc_other_count > 0 %}
        <button type="button" class="vf-chip" data-venue="other">Other <span class="vf-cnt">{{ misc_other_count }}</span></button>
      {% endif %}
    </div>
  {% endif %}
</div>
{% endif %}

<div class="paper-list" id="paper-list">
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
    <a class="pr-item" data-venue="{{ item_venue }}" href="{{ r.url | relative_url }}">
      <div class="pr-meta">
        {% if r.venue %}<span class="pr-venue">{{ r.venue }}</span>{% endif %}
        <span class="pr-date">{{ r.date | date: '%B %d, %Y' }}</span>
      </div>
      <div class="pr-title">{{ r.title }}</div>
      {% if r.authors %}<div class="pr-authors">{{ r.authors }}</div>{% endif %}
      {% if r.description %}<div class="pr-desc">{{ r.description }}</div>{% endif %}
    </a>
  {% endfor %}
</div>

{% if site.papers.size == 0 %}
  <p class="paper-empty">Reviews are being added, the first ones will appear here soon.</p>
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
