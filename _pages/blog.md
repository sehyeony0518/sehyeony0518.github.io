---
layout: default
permalink: /diary/
title: diary
nav: true
nav_order: 6
pagination:
  enabled: true
  collection: posts
  permalink: /page/:num/
  per_page: 20
  sort_field: date
  sort_reverse: true
  trail:
    before: 1 # The number of links before the current page
    after: 3 # The number of links after the current page
---

<div class="post">

{% assign blog_name_size = site.blog_name | size %}
{% assign blog_description_size = site.blog_description | size %}

{% if blog_name_size > 0 or blog_description_size > 0 %}

  <div class="header-bar">
    <h1>{{ site.blog_name }}</h1>
    <h2>{{ site.blog_description }}</h2>
  </div>
  {% endif %}

<!-- Diary navigation: by sector (tag) and by year -->
<style>
  .diary-nav { margin: 0 0 1.5rem; }
  .diary-nav .nav-label {
    font-size: .72rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase;
    opacity: .55; margin: 0 0 .35rem;
  }
  .diary-nav .nav-row { display: flex; flex-wrap: wrap; gap: .4rem; margin-bottom: .9rem; }
  .diary-nav .nav-chip {
    display: inline-block; padding: .18rem .6rem; border-radius: 999px;
    border: 1px solid rgba(128,128,128,.35); font-size: .82rem; text-decoration: none;
    color: inherit; white-space: nowrap; transition: all .15s ease;
  }
  .diary-nav .nav-chip:hover { border-color: var(--global-theme-color); color: var(--global-theme-color); }
  .diary-nav .nav-chip .cnt { opacity: .5; font-size: .72rem; margin-left: .2rem; }
  /* Stats bar */
  .diary-stats {
    display: flex; flex-wrap: wrap; gap: 1.4rem; align-items: baseline;
    padding: .9rem 1.1rem; margin: 0 0 1.4rem; border-radius: 10px;
    border: 1px solid rgba(128,128,128,.2); background: rgba(128,128,128,.05);
  }
  .diary-stats .stat { display: flex; flex-direction: column; }
  .diary-stats .stat .num { font-size: 1.5rem; font-weight: 700; line-height: 1.1; color: var(--global-theme-color); }
  .diary-stats .stat .lbl { font-size: .72rem; letter-spacing: .05em; text-transform: uppercase; opacity: .55; margin-top: .1rem; }
  /* Compact post list */
  .post .post-list { margin-top: .5rem; }
  .post .post-list > li { margin-bottom: 1.1rem; padding-bottom: 1.1rem; border-bottom: 1px solid rgba(128,128,128,.15); }
  .post .post-list > li h3 { margin-bottom: .1rem; line-height: 1.35; }
  .post .post-list > li .post-meta, .post .post-list > li .post-tags { margin: .1rem 0 0; font-size: .8rem; }
  .post .post-list > li p { margin: .15rem 0 0; }
</style>

{% assign sorted_posts = site.posts | sort: 'date' %}
{% assign first_post = sorted_posts | first %}
{% assign last_post = sorted_posts | last %}
{% assign year_groups_all = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% assign meditation_ct = 0 %}
{% for post in site.posts %}{% if post.tags contains "묵상" %}{% assign meditation_ct = meditation_ct | plus: 1 %}{% endif %}{% endfor %}
<div class="diary-stats">
  <div class="stat"><span class="num">{{ site.posts | size }}</span><span class="lbl">기록</span></div>
  <div class="stat"><span class="num">{{ meditation_ct }}</span><span class="lbl">묵상</span></div>
  <div class="stat"><span class="num">{{ year_groups_all | size }}</span><span class="lbl">해</span></div>
  <div class="stat"><span class="num" style="font-size:1rem; font-weight:600;">{{ first_post.date | date: '%Y.%m' }} – {{ last_post.date | date: '%Y.%m' }}</span><span class="lbl">기간</span></div>
</div>

<div class="diary-nav">
  <p class="nav-label">섹터별</p>
  <div class="nav-row">
    {% assign all_tags = site.posts | map: "tags" | join: ',' | replace: ' ,', ',' | split: ',' %}
    {% assign tag_names = all_tags | uniq | sort %}
    {% for tag in tag_names %}
      {% if tag != "" %}
        {% assign tag_count = 0 %}
        {% for post in site.posts %}{% if post.tags contains tag %}{% assign tag_count = tag_count | plus: 1 %}{% endif %}{% endfor %}
        <a class="nav-chip" href="{{ tag | slugify: 'raw' | prepend: '/diary/tag/' | relative_url }}"># {{ tag }}<span class="cnt">{{ tag_count }}</span></a>
      {% endif %}
    {% endfor %}
  </div>

  <p class="nav-label">연도별</p>
  <div class="nav-row">
    {% assign year_groups = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
    {% for yg in year_groups %}
      <a class="nav-chip" href="{{ yg.name | prepend: '/diary/' | append: '/' | relative_url }}">{{ yg.name }}<span class="cnt">{{ yg.items | size }}</span></a>
    {% endfor %}
  </div>
</div>

{% assign featured_posts = site.posts | where: "featured", "true" %}
{% if featured_posts.size > 0 %}
<br>

<div class="container featured-posts">
{% assign is_even = featured_posts.size | modulo: 2 %}
<div class="row row-cols-{% if featured_posts.size <= 2 or is_even == 0 %}2{% else %}3{% endif %}">
{% for post in featured_posts %}
<div class="col mb-4">
<a href="{{ post.url | relative_url }}">
<div class="card hoverable">
<div class="row g-0">
<div class="col-md-12">
<div class="card-body">
<div class="float-right">
<i class="fa-solid fa-thumbtack fa-xs"></i>
</div>
<h3 class="card-title text-lowercase">{{ post.title }}</h3>
<p class="card-text">{{ post.description }}</p>

                    {% if post.external_source == blank %}
                      {% assign read_time = post.content | number_of_words | divided_by: 180 | plus: 1 %}
                    {% else %}
                      {% assign read_time = post.feed_content | strip_html | number_of_words | divided_by: 180 | plus: 1 %}
                    {% endif %}
                    {% assign year = post.date | date: "%Y" %}

                    <p class="post-meta">
                      {{ read_time }} min read &nbsp; &middot; &nbsp;
                      <a href="{{ year | prepend: '/diary/' | relative_url }}">
                        <i class="fa-solid fa-calendar fa-sm"></i> {{ year }} </a>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </a>
        </div>
      {% endfor %}
      </div>
    </div>
    <hr>

{% endif %}

  <ul class="post-list">

    {% if page.pagination.enabled %}
      {% assign postlist = paginator.posts %}
    {% else %}
      {% assign postlist = site.posts %}
    {% endif %}

    {% for post in postlist %}

    {% if post.external_source == blank %}
      {% assign read_time = post.content | number_of_words | divided_by: 180 | plus: 1 %}
    {% else %}
      {% assign read_time = post.feed_content | strip_html | number_of_words | divided_by: 180 | plus: 1 %}
    {% endif %}
    {% assign year = post.date | date: "%Y" %}
    {% assign tags = post.tags | join: "" %}
    {% assign categories = post.categories | join: "" %}

    <li>

{% if post.thumbnail %}

<div class="row">
          <div class="col-sm-9">
{% endif %}
        <h3>
        {% if post.redirect == blank %}
          <a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a>
        {% elsif post.redirect contains '://' %}
          <a class="post-title" href="{{ post.redirect }}" target="_blank">{{ post.title }}</a>
          <svg width="2rem" height="2rem" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
            <path d="M17 13.5v6H5v-12h6m3-3h6v6m0-6-9 9" class="icon_svg-stroke" stroke="#999" stroke-width="1.5" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"></path>
          </svg>
        {% else %}
          <a class="post-title" href="{{ post.redirect | relative_url }}">{{ post.title }}</a>
        {% endif %}
      </h3>
      <p>{{ post.description }}</p>
      <p class="post-meta">
        {{ read_time }} min read &nbsp; &middot; &nbsp;
        {{ post.date | date: '%B %d, %Y' }}
        {% if post.external_source %}
        &nbsp; &middot; &nbsp; {{ post.external_source }}
        {% endif %}
      </p>
      <p class="post-tags">
        <a href="{{ year | prepend: '/diary/' | relative_url }}">
          <i class="fa-solid fa-calendar fa-sm"></i> {{ year }} </a>

          {% if tags != "" %}
          &nbsp; &middot; &nbsp;
            {% for tag in post.tags %}
            <a href="{{ tag | slugify | prepend: '/diary/tag/' | relative_url }}">
              <i class="fa-solid fa-hashtag fa-sm"></i> {{ tag }}</a>
              {% unless forloop.last %}
                &nbsp;
              {% endunless %}
              {% endfor %}
          {% endif %}

          {% if categories != "" %}
          &nbsp; &middot; &nbsp;
            {% for category in post.categories %}
            <a href="{{ category | slugify | prepend: '/diary/category/' | relative_url }}">
              <i class="fa-solid fa-tag fa-sm"></i> {{ category }}</a>
              {% unless forloop.last %}
                &nbsp;
              {% endunless %}
              {% endfor %}
          {% endif %}
    </p>

{% if post.thumbnail %}

</div>

  <div class="col-sm-3">
    <img class="card-img" src="{{ post.thumbnail | relative_url }}" style="object-fit: cover; height: 90%" alt="image">
  </div>
</div>
{% endif %}
    </li>

    {% endfor %}

  </ul>

{% if page.pagination.enabled %}
{% include pagination.liquid %}
{% endif %}

</div>
