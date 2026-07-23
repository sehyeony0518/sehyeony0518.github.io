---
layout: page
permalink: /team/
title: team
description: Mission2035 self-supporting (tentmaking) mission team.
nav: true
nav_order: 1
---

<style>
  .team-intro { opacity: .8; line-height: 1.75; margin: 0 0 1.6rem; max-width: 660px; }
  .team-cta {
    opacity: .82; line-height: 1.75; max-width: 660px;
    margin: 2.2rem 0 0; padding-top: 1.4rem;
    border-top: 1px solid rgba(128,128,128,.2);
  }
  .team-cta a { color: var(--global-theme-color); text-decoration: none; }
  .team-cta a:hover { text-decoration: underline; }
  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 210px));
    gap: 1.7rem; justify-content: start; margin: 1.6rem 0;
  }
  .member-card { text-align: center; }
  .member-card .m-photo {
    width: 100%; aspect-ratio: 1 / 1; object-fit: cover;
    border-radius: 14px; background: rgba(128,128,128,.1); display: block;
  }
  .member-card .m-role {
    margin-top: .65rem; font-size: .7rem; font-weight: 800; letter-spacing: .07em;
    text-transform: uppercase; color: var(--global-theme-color);
  }
  .member-card .m-name { font-weight: 700; font-size: 1.02rem; margin-top: .05rem; line-height: 1.3; }
  .member-card .m-name span { font-weight: 400; opacity: .5; font-size: .82em; margin-left: .2rem; }
  .member-card .m-desc { font-size: .82rem; opacity: .68; margin-top: .25rem; }
  .member-card .m-links { font-size: .8rem; margin-top: .4rem; }
  .member-card .m-links a { color: var(--global-theme-color); text-decoration: none; }
  .member-card .m-links a:hover { text-decoration: underline; }
</style>

<p class="team-intro">
A self-supporting (tentmaking) mission team — each member serving in their own field of expertise.
</p>

<div class="team-grid">

  <div class="member-card">
    <img class="m-photo" src="/assets/img/team/sehyeon-hwang.jpg" alt="Se-Hyeon Hwang" loading="lazy">
    <div class="m-role">Leader</div>
    <div class="m-name">Se-Hyeon Hwang <span>황세현</span></div>
    <div class="m-desc">M.S. Student, Ajou University</div>
    <div class="m-links"><a href="/research/">research</a> · <a href="/cv/">cv</a></div>
  </div>

  <div class="member-card">
    <img class="m-photo" src="/assets/img/team/jincheol-jeong.jpg" alt="Jin-Cheol Jeong" loading="lazy">
    <div class="m-role">Member</div>
    <div class="m-name">Jin-Cheol Jeong <span>정진철</span></div>
    <div class="m-desc">M.S. Student, Ajou University</div>
  </div>

</div>

<p class="team-cta">
If this calling resonates with you, we would love to <a href="{{ '/' | relative_url }}">hear from you</a>. And even if you cannot walk with us directly, we would be deeply grateful for your partnership in prayer.
</p>
