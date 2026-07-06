---
layout: default
title: feed
permalink: /rss/
---


{% assign news = site.docs | where_exp: "d", "d.path contains '_docs/news/'" | sort: "title" %}

{% for doc in news %}

## [{{ doc.title }}]({{ doc.url | relative_url }})

{% include_relative news/{{ doc.basename }}.md %}

---

{% endfor %}