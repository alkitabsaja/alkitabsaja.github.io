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

{% assign name = folder | remove_first: "_docs/" %}

{% if name == "_docs" or name == "" %}
## Main
{% else %}
## {{ name }}
{% endif %}

{% assign docs = site.docs | where: "dir", folder | sort: "title" %}

{% for doc in docs %}
{% assign ebook = doc.path | remove_first: "_docs/" | remove: ".md" %}

- [{{ doc.title }}]({{ doc.url | relative_url }})
  ([PDF]({{ "/ebooks/" | append: ebook | append: ".pdf" | relative_url }}) |
   [EPUB]({{ "/ebooks/" | append: ebook | append: ".epub" | relative_url }}))
{% endfor %}

{% endfor %}
