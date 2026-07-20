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
  {% assign photos = "g38,캠퍼스에서 함께 기도하며|g35,부흥하는 캠퍼스, 열매맺는 제자 — JDM 수원지구|g41,담낭 초음파 AI 진단 시연|g57,JDM 디모데 훈련학교 (TTS)|g40,2025 산학협력 박람회 시상식|g07,캠퍼스 선교 — JDM 수원지구 부스|g14,서로를 위한 기도 (마 28:19)|g12,겨울집회 찬양 — Rejoice in the Lord|g06,캠퍼스 전도|g26,아주대학교 졸업|g08,함께 기도하며|g03,카페에서 제자훈련 나눔|g15,수련회 찬양|g27,24 TTS 졸업식|g24,기도 사역|g09,수련회 기도의 시간|g18,연구실에서|g13,겨울 캠퍼스 전도|g05,리더로 섬기며|g16,졸업을 축하하며|g10,목장 모임|g22,전도 물품을 나누며|g11,수련회에서|g23,집회를 섬기며|g25,수련회의 즐거움|g17,캠퍼스에서|g04,지체들과 함께|g01,공동체와 함께|g02,일상의 자리에서|g42,연구 발표|g43,JDM 수원 종교개혁 세미나|g46,2025 JDM 대학여름집회|g47,JDM TTS 졸업식|g50,캠퍼스를 개척하라 — 대학여름집회|g51,캠퍼스 소그룹 모임|g52,캠퍼스 부스에서 함께 기도하며|g53,2025 JDM 수원 겨울수련회 — Rejoice|g58,2024 JDM 청소년 겨울수련회|g36,공동체와 함께한 새해|g28,교회 역사 앞에서|g29,예배당에서|g30,함께 나눈 식탁|g31,교회 앞에서|g32,새 학기 캠퍼스 전도|g33,거리에서 복음을 전하며|g34,수련회에서|g37,축하의 자리|g39,졸업을 축하하며|g44,가을 캠퍼스에서|g48,친구들과 함께|g49,함께 웃으며|g54,함께한 저녁 식탁|g55,찬양을 준비하며|g56,함께 본 뮤지컬" | split: "|" %}
  {% for p in photos %}
    {% assign parts = p | split: "," %}
    <figure>
      <img loading="lazy" src="{{ '/assets/img/gallery/' | append: parts[0] | append: '.jpg' | relative_url }}" alt="{{ parts[1] }}">
      <figcaption>{{ parts[1] }}</figcaption>
    </figure>
  {% endfor %}
</div>

<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="확대 이미지">
  <button class="lb-close" id="lb-close" aria-label="닫기">&times;</button>
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
