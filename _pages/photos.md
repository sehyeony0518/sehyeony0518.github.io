---
layout: page
permalink: /photos/
title: photos
description: 부르심의 여정을 함께한 순간들 — 캠퍼스 선교, 공동체, 사역, 그리고 일상.
nav: true
nav_order: 7
---

<style>
  .photo-gallery {
    column-count: 2;
    column-gap: 0.7rem;
    margin-top: 0.8rem;
  }
  @media (min-width: 640px) { .photo-gallery { column-count: 3; } }
  @media (min-width: 1000px) { .photo-gallery { column-count: 4; } }
  .photo-gallery figure {
    break-inside: avoid;
    margin: 0 0 0.7rem;
    position: relative;
    border-radius: 8px;
    overflow: hidden;
    background: rgba(128,128,128,.08);
  }
  .photo-gallery img {
    width: 100%;
    display: block;
    border-radius: 8px;
    transition: transform 0.35s ease;
  }
  .photo-gallery figure:hover img { transform: scale(1.04); }
  .photo-gallery figcaption {
    position: absolute;
    left: 0; right: 0; bottom: 0;
    padding: 1.2rem 0.7rem 0.5rem;
    font-size: 0.74rem;
    color: #fff;
    background: linear-gradient(180deg, transparent, rgba(0,0,0,.6));
    opacity: 0;
    transition: opacity 0.2s ease;
  }
  .photo-gallery figure:hover figcaption { opacity: 1; }
</style>

<div class="photo-gallery">
  {% assign photos = "g07,캠퍼스 선교 — JDM 수원지구 부스|g14,서로를 위한 기도 (마 28:19)|g12,겨울집회 찬양 — Rejoice in the Lord|g06,캠퍼스 전도|g26,아주대학교 졸업|g08,함께 기도하며|g03,카페에서 제자훈련 나눔|g15,수련회 찬양|g27,24 TTS 졸업식|g24,기도 사역|g09,수련회 기도의 시간|g18,연구실에서|g13,겨울 캠퍼스 전도|g05,리더로 섬기며|g16,졸업을 축하하며|g10,목장 모임|g22,전도 물품을 나누며|g11,수련회에서|g23,집회를 섬기며|g25,수련회의 즐거움|g17,캠퍼스에서|g04,지체들과 함께|g01,공동체와 함께|g02,일상의 자리에서" | split: "|" %}
  {% for p in photos %}
    {% assign parts = p | split: "," %}
    <figure>
      <img loading="lazy" src="{{ '/assets/img/gallery/' | append: parts[0] | append: '.jpg' | relative_url }}" alt="{{ parts[1] }}">
      <figcaption>{{ parts[1] }}</figcaption>
    </figure>
  {% endfor %}
</div>
