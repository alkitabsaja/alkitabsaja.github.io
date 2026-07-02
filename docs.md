---
layout: default
title: eBooks
permalink: /docs/
---

# eBooks

Browse articles and ebooks below.

Docs count: {{ site.docs | size }}

{% assign grouped_docs = site.docs | group_by: "path" %}

{% for group in grouped_docs %}
  {% assign folder = group.name | split: "/" | first %}
  
  {% if folder == "" %}
    ## Main
  {% else %}
    ## {{ folder | capitalize }}
  {% endif %}
  
  {% for doc in group.items %}
  - [{{ doc.title }}]({{ doc.url | relative_url }})
    ([PDF]({{ '/ebooks/' | append: doc.slug | append: '.pdf' | relative_url }}) |
    [EPUB]({{ '/ebooks/' | append: doc.slug | append: '.epub' | relative_url }}))
  {% endfor %}
{% endfor %}
