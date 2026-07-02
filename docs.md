---
layout: default
title: eBooks
permalink: /docs/
---

# eBooks

Browse articles and ebooks below.

Docs count: {{ site.docs | size }}

{% for doc in site.docs %}
- [{{ doc.title }}]({{ doc.url | relative_url }})
  ([PDF]({{ '/ebooks/' | append: doc.slug | append: '.pdf' | relative_url }}) |
  [EPUB]({{ '/ebooks/' | append: doc.slug | append: '.epub' | relative_url }}))
{% endfor %}
