---
layout: page
permalink: /ministry/
title: ministry
description: 지금 맡겨진 자리에서의 순종, 그리고 부르심의 여정
nav: true
nav_order: 2
---

<style>
  .mj-bar {
    display: flex; flex-wrap: wrap; align-items: center; gap: .5rem;
    margin: 0 0 1.6rem; padding-bottom: .9rem;
    border-bottom: 1px solid rgba(128,128,128,.18);
  }
  .mj-tab {
    background: none; border: 1px solid rgba(128,128,128,.35); border-radius: 999px;
    font-size: .88rem; font-weight: 600; padding: .3rem .95rem; cursor: pointer;
    color: inherit; transition: all .15s ease;
  }
  .mj-tab:hover { border-color: var(--global-theme-color); color: var(--global-theme-color); }
  .mj-tab.active {
    background: var(--global-theme-color); border-color: var(--global-theme-color); color: #fff;
  }
  .mj-share {
    margin-left: auto; display: inline-flex; align-items: center; gap: .35rem;
    background: none; border: 1px solid rgba(128,128,128,.35); border-radius: 999px;
    font-size: .82rem; font-weight: 600; padding: .28rem .8rem; cursor: pointer;
    color: inherit; transition: all .15s ease;
  }
  .mj-share:hover { border-color: var(--global-theme-color); color: var(--global-theme-color); }
  .mj-panel { display: none; }
  .mj-panel.active { display: block; }
  .mj-toast {
    position: fixed; left: 50%; bottom: 2rem; transform: translateX(-50%) translateY(1rem);
    background: rgba(20,20,20,.92); color: #fff; padding: .6rem 1.1rem; border-radius: 999px;
    font-size: .84rem; opacity: 0; pointer-events: none; transition: all .25s ease; z-index: 4000;
  }
  .mj-toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
</style>

<div class="mj-bar">
  <button class="mj-tab active" type="button" data-tab="ministry">ministry</button>
  <button class="mj-tab" type="button" data-tab="journey">journey</button>
  <button class="mj-share" id="mj-share" type="button" aria-label="이 탭 공유하기"><span aria-hidden="true">🔗</span> 공유하기</button>
</div>

<div class="mj-panel active" id="panel-ministry" markdown="1">
{% include content_ministry.liquid %}
</div>

<div class="mj-panel" id="panel-journey" markdown="1">
{% include content_journey.liquid %}
</div>

<div class="mj-toast" id="mj-toast">링크가 복사되었습니다</div>

<script>
  (function () {
    var tabs = [].slice.call(document.querySelectorAll('.mj-tab'));
    var panels = {
      ministry: document.getElementById('panel-ministry'),
      journey: document.getElementById('panel-journey')
    };
    var toast = document.getElementById('mj-toast');

    function activate(name, updateHash) {
      if (!panels[name]) name = 'ministry';
      Object.keys(panels).forEach(function (k) {
        panels[k].classList.toggle('active', k === name);
      });
      tabs.forEach(function (t) {
        t.classList.toggle('active', t.getAttribute('data-tab') === name);
      });
      if (updateHash && history.replaceState) {
        history.replaceState(null, '', '#' + name);
      }
    }

    tabs.forEach(function (t) {
      t.addEventListener('click', function () {
        activate(t.getAttribute('data-tab'), true);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    });

    activate((window.location.hash || '').replace('#', '') === 'journey' ? 'journey' : 'ministry', false);
    window.addEventListener('hashchange', function () {
      activate((window.location.hash || '').replace('#', '') === 'journey' ? 'journey' : 'ministry', false);
    });

    function showToast(msg) {
      toast.textContent = msg;
      toast.classList.add('show');
      setTimeout(function () { toast.classList.remove('show'); }, 2200);
    }

    var btn = document.getElementById('mj-share');
    btn.addEventListener('click', function () {
      var active = document.querySelector('.mj-tab.active');
      var name = active ? active.getAttribute('data-tab') : 'ministry';
      var url = window.location.origin + window.location.pathname + '#' + name;
      if (navigator.share) {
        navigator.share({ url: url }).catch(function () {});
      } else if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(function () {
          showToast('링크가 복사되었습니다');
        }).catch(function () { showToast(url); });
      } else {
        showToast(url);
      }
    });
  })();
</script>
