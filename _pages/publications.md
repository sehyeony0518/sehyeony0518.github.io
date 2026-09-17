---
layout: page
permalink: /publications/
title: publications
og_image: "https://sehyeony0518.github.io/assets/img/og/page-publications.png"
description: peer-reviewed publications and manuscripts in preparation.
nav: true
nav_order: 8
---

<!-- _pages/publications.md -->

**Peer-reviewed publications and manuscripts in preparation.** (\* denotes first author)

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

## Manuscripts in Preparation

<div class="publications">

{% bibliography --query @unpublished %}

</div>

## Peer-Reviewed Publications

<div class="publications">

{% bibliography --query @inproceedings %}

</div>
