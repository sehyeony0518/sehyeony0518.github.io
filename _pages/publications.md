---
layout: page
permalink: /publications/
title: publications
description: peer-reviewed publications and research in progress.
nav: true
nav_order: 4
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

## Research in Progress

<div class="publications">

{% bibliography --query @unpublished %}

</div>

## Peer-Reviewed Publications

<div class="publications">

{% bibliography --query @inproceedings %}

</div>
