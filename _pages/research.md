---
layout: page
permalink: /research/
title: research
description: 사람과 임상을 섬기는 신뢰할 수 있는 의료 AI
nav: true
nav_order: 3
toc:
  sidebar: left
---

> 나의 연구는 Mission2035와 분리된 개인적 성취의 영역이 아니라, 의료와 교육을 통해 사람을 섬기고 장차 대학 캠퍼스에 머물기 위해 하나님께서 맡기신 학문적 소명이다.

**Research Interests** &nbsp;·&nbsp; 신뢰가능·해석가능 의료 AI &nbsp;·&nbsp; 임상 충실성(clinical faithfulness)과 지름길(shortcut) 학습 분석 &nbsp;·&nbsp; 초음파 진단 AI &nbsp;·&nbsp; 모델 신뢰성 모니터링

## Research Mission

의료 AI가 실제 진료 현장에서 신뢰받으려면 높은 성능만으로는 충분하지 않습니다. 모델이 무엇을 근거로 판단했는지, 그 근거가 임상적으로 타당한지까지 검증되어야 합니다. 저는 성능과 임상적 신뢰 사이의 간극을 좁히는 연구를 합니다.

## Clinical Faithfulness

**모델은 실제로 임상적으로 타당한 근거를 사용하는가?** 저는 초음파 진단 모델의 설명이 비의도적인 지름길 단서가 아니라, 실제 임상 중증도와 판독 요인에 충실한지를 검증하는 방법을 연구합니다. 높은 정확도를 보이는 모델이라도 임상적으로 잘못된 근거에 의존할 수 있다는 문제를 다룹니다.

## Ultrasound AI

초음파 영상의 물리적, 임상적 특성을 반영하는 모델을 연구합니다. 주파수 대역(DWT) 분석과 어텐션 기반 표현 분석으로 CNN, 트랜스포머, 그래프, 웨이블릿 기반 분류기의 판단 근거를 비교합니다. 에코 발생도, 질감, 병변 경계, 벽 소견 같은 구조화된 임상 소견을 도메인 사전지식으로 활용합니다.

## Interpretability & Reliability

설명(attribution) 분석과 shortcut 학습 분석, 배포된 모델의 신뢰성 모니터링을 연구합니다. 스마트팩토리 예지보전 과제에서는 국제 신뢰성 표준에 기반한 모니터링 소프트웨어를 설계했습니다.

## Selected Projects

<style>
  .proj-grid { display: grid; grid-template-columns: 1fr; gap: 1rem; margin: 1rem 0 0.5rem; }
  @media (min-width: 640px) { .proj-grid { grid-template-columns: 1fr 1fr; } }
  .proj-card {
    display: flex; flex-direction: column;
    border: 1px solid rgba(128,128,128,.2); border-radius: 12px;
    padding: 1.1rem 1.2rem; background: rgba(128,128,128,.035);
    transition: border-color .15s ease, box-shadow .15s ease;
  }
  .proj-card:hover { border-color: var(--global-theme-color); box-shadow: 0 4px 18px rgba(0,0,0,.06); }
  .proj-card .pc-top { display: flex; flex-wrap: wrap; align-items: center; gap: .45rem; margin-bottom: .5rem; }
  .proj-card .pc-period { font-size: .72rem; opacity: .55; font-variant-numeric: tabular-nums; }
  .proj-card .pc-badge {
    font-size: .66rem; font-weight: 700; letter-spacing: .03em;
    padding: .1rem .5rem; border-radius: 999px;
    border: 1px solid var(--global-theme-color); color: var(--global-theme-color);
  }
  .proj-card h3 { font-size: 1.02rem; margin: 0 0 .4rem; line-height: 1.35; }
  .proj-card .pc-desc { font-size: .88rem; line-height: 1.6; opacity: .82; margin: 0 0 .7rem; flex-grow: 1; }
  .proj-card .pc-tags { display: flex; flex-wrap: wrap; gap: .35rem; }
  .proj-card .pc-tag {
    font-size: .7rem; padding: .12rem .5rem; border-radius: 6px;
    background: rgba(128,128,128,.12); opacity: .85;
  }
  .proj-card .pc-link { margin-top: .6rem; font-size: .8rem; text-decoration: none; color: var(--global-theme-color); }
  .proj-card .pc-link:hover { text-decoration: underline; }
</style>

<div class="proj-grid">

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">M.S. Thesis</span><span class="pc-period">2025 – 현재</span></div>
    <h3>담낭 초음파 진단 AI의 신뢰성</h3>
    <p class="pc-desc">ITRC(IITP) 3년 과제로, 아주대학교병원과 협력하여 담낭 질환의 초음파 AI 진단을 연구합니다. 데이터·모델의 신뢰성 요구분석과 악성 병변 검출 개선을 다루었고, 지금은 진단 모델의 설명이 임상적으로 충실한지 검증하는 석사 논문 연구로 이어지고 있습니다.</p>
    <div class="pc-tags"><span class="pc-tag">Ultrasound AI</span><span class="pc-tag">Clinical Faithfulness</span><span class="pc-tag">아주대병원 협력</span></div>
    <a class="pc-link" href="/publications/">→ ACK 2025 (제1저자)</a>
  </div>

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">Industry</span><span class="pc-period">2025 – 2026</span></div>
    <h3>스마트팩토리 예지보전 모니터링</h3>
    <p class="pc-desc">삼성중공업 과제로, 설비 고장 예측과 상태 모니터링을 위한 머신러닝 모델을 개발하고, 국제 신뢰성 표준에 기반한 모니터링 소프트웨어를 설계했습니다.</p>
    <div class="pc-tags"><span class="pc-tag">Predictive Maintenance</span><span class="pc-tag">Reliability</span><span class="pc-tag">Monitoring SW</span></div>
    <a class="pc-link" href="/publications/">→ KCSE 2026 (제1저자)</a>
  </div>

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">Software</span><span class="pc-period">등록 SW</span></div>
    <h3>의료영상 진단 마커 제거 도구</h3>
    <p class="pc-desc">의료영상 속 진단 마커는 지름길(shortcut) 학습의 원인이 됩니다. 이 마커를 제거하고 영상을 복원하여 진단 활용성을 보존하는 소프트웨어를 개발했습니다 (등록 번호 ASSET_0013931).</p>
    <div class="pc-tags"><span class="pc-tag">Shortcut 제거</span><span class="pc-tag">이미지 복원</span><span class="pc-tag">SW 등록</span></div>
  </div>

  <div class="proj-card">
    <div class="pc-top"><span class="pc-badge">Clinical Research</span><span class="pc-period">2024</span></div>
    <h3>계산정신의학 연구 인턴</h3>
    <p class="pc-desc">아주대학교병원 정신건강의학과의 정부지원 계산정신의학 과제에 참여하여, IRB 기반 임상연구 절차와 임상 데이터 처리, 임상의–AI 협력 연구를 경험했습니다.</p>
    <div class="pc-tags"><span class="pc-tag">Computational Psychiatry</span><span class="pc-tag">IRB 임상연구</span></div>
  </div>

</div>

발표 논문과 준비 중인 원고는 [publications](/publications/)에 있습니다.
