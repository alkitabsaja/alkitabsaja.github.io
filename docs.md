---
layout: default
title: Documentation
permalink: /docs/
---

# Documentation

Browse guides and references below.

<div class="docs-list" markdown="1">
{% for doc in site.docs %}
[{{ doc.title }}]({{ doc.url | relative_url }})
{% endfor %}
</div>

<hr>

Can't find what you need? <a href="https://wa.me/6281234567890"><i class="bi bi-whatsapp"></i> Contact me on WhatsApp</a>
