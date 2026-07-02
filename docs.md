---
layout: default
title: eBooks
permalink: /docs/
---

# eBooks

Browse articles and ebooks below.

Docs count: {{ site.docs | size }}

{% assign docs = site.docs | sort: "path" %}
{% assign current = "" %}

{% for doc in docs %}
  {% assign parts = doc.path | remove_first: "_docs/" | split: "/" %}
  {% assign folder = parts | slice: 0, parts.size | pop | join: "/" %}

  {% if folder != current %}
    {% assign current = folder %}

{% if folder == "" %}
## Main
{% else %}
## {{ folder }}
{% endif %}

  {% endif %}

  {% assign ebook = doc.path | remove_first: "_docs/" | remove: ".md" %}

- [{{ doc.title }}]({{ doc.url | relative_url }})
  ([PDF]({{ "/ebooks/" | append: ebook | append: ".pdf" | relative_url }}) |
   [EPUB]({{ "/ebooks/" | append: ebook | append: ".epub" | relative_url }}))
{% endfor %}
