---
layout: default
title: eBooks
permalink: /docs/
---

# eBooks

Browse articles and ebooks below.

Docs count: {{ site.docs | size }}

{% assign folders = site.docs | map: "dir" | uniq | sort %}

{% for folder in folders %}

{% if folder == "_docs" %}
## Main
{% else %}
## {{ folder | remove: "_docs/" | replace: "-", " " | capitalize }}
{% endif %}

{% assign docs = site.docs | where: "dir", folder | sort: "title" %}

{% for doc in docs %}
- [{{ doc.title }}]({{ doc.url | relative_url }})
  ([PDF]({{ '/ebooks/' | append: doc.slug | append: '.pdf' | relative_url }}) |
  [EPUB]({{ '/ebooks/' | append: doc.slug | append: '.epub' | relative_url }}))
{% endfor %}

{% endfor %}
