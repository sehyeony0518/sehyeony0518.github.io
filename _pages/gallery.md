---
layout: page
permalink: /gallery/
title: gallery
description: Moments from research — lab, demos, and presentations.
nav: true
nav_order: 10
---

<style>
  .photo-gallery {
    column-count: 2;
    column-gap: 0.7rem;
    margin-top: 0.8rem;
  }
  @media (min-width: 640px) { .photo-gallery { column-count: 3; } }
  .photo-gallery figure {
    break-inside: avoid;
    margin: 0 0 0.7rem;
    position: relative;
    border-radius: 8px;
    overflow: hidden;
    background: rgba(128,128,128,.08);
    cursor: zoom-in;
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

  /* Lightbox */
  .lightbox {
    position: fixed; inset: 0; z-index: 3000;
    display: none; align-items: center; justify-content: center;
    background: rgba(0,0,0,.9); padding: 2.5vh 3vw; cursor: zoom-out;
    opacity: 0; transition: opacity .2s ease;
  }
  .lightbox.open { display: flex; opacity: 1; }
  .lightbox img {
    max-width: 100%; max-height: 88vh; border-radius: 8px;
    box-shadow: 0 10px 50px rgba(0,0,0,.6); object-fit: contain;
  }
  .lightbox .lb-cap {
    position: absolute; left: 0; right: 0; bottom: 2vh; text-align: center;
    color: #fff; font-size: .9rem; opacity: .85; padding: 0 1rem;
    text-shadow: 0 1px 4px rgba(0,0,0,.8);
  }
  .lightbox .lb-close {
    position: absolute; top: 2vh; right: 3vw; color: #fff; font-size: 2rem;
    line-height: 1; opacity: .8; cursor: pointer; background: none; border: 0;
  }
  .lightbox .lb-close:hover { opacity: 1; }
</style>

<div class="photo-gallery">
  {% assign photos = "g41,Demonstrating a gallbladder ultrasound AI diagnostic system|rg01,Presenting at the Lunit Medical FM Hackathon|g42,Presenting ultrasound curriculum-learning work at the lab|rg11,Conference oral presentation|rg06,Poster session — explainable gallbladder ultrasound AI|rg09,MIIDS Research Center booth · ITRC Talent Development Fair|g40,Recognized at the 2025 ECE Industry–Academia Expo|rg10,Social Value Award · 2025 Capstone Design Competition|rg02,Korea Computer Congress (KCC 2026) · Jeju|rg03,Supervising the digital logic laboratory as a TA|g18,At the Embedded & Software Lab|rg05,B.S. commencement · Ajou University|rg04,Commencement day with lab and classmates" | split: "|" %}
  {% for p in photos %}
    {% assign parts = p | split: "," %}
    <figure>
      <img loading="lazy" src="{{ '/assets/img/gallery/' | append: parts[0] | append: '.jpg' | relative_url }}" alt="{{ parts[1] }}">
      <figcaption>{{ parts[1] }}</figcaption>
    </figure>
  {% endfor %}
</div>

<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Enlarged image">
  <button class="lb-close" id="lb-close" aria-label="Close">&times;</button>
  <img id="lb-img" src="" alt="">
  <div class="lb-cap" id="lb-cap"></div>
</div>

<script>
  (function () {
    var lb = document.getElementById('lightbox');
    if (!lb) return;
    var lbImg = document.getElementById('lb-img');
    var lbCap = document.getElementById('lb-cap');
    function open(src, cap) {
      lbImg.setAttribute('src', src);
      lbImg.setAttribute('alt', cap || '');
      lbCap.textContent = cap || '';
      lb.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
    function close() {
      lb.classList.remove('open');
      lbImg.setAttribute('src', '');
      document.body.style.overflow = '';
    }
    document.querySelectorAll('.photo-gallery img').forEach(function (img) {
      img.addEventListener('click', function () {
        open(img.getAttribute('src'), img.getAttribute('alt'));
      });
    });
    lb.addEventListener('click', close);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && lb.classList.contains('open')) close();
    });
  })();
</script>
