---
layout: default
title: Search
permalink: /search/
---

# Search

<div id="searchbox"></div>

<div id="hits"></div>

<div id="pagination"></div>

<link rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/instantsearch.css@8/themes/satellite-min.css">

<script src="https://cdn.jsdelivr.net/npm/algoliasearch@4/dist/algoliasearch-lite.umd.js"></script>
<script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4"></script>

<script>
const searchClient = algoliasearch(
    "KHDI0XM5QR",
    "00a411dad4bfb54b2592536cc436db32"
);

const search = instantsearch({
    indexName: "YOUR_INDEX_NAME",
    searchClient,
});

search.addWidgets([

    instantsearch.widgets.searchBox({
        container: "#searchbox",
        placeholder: "Search articles, books and news...",
    }),

    instantsearch.widgets.hits({
        container: "#hits",

        templates: {
            item(hit) {
                return `
                <article class="docs-list">
                    <a href="${hit.url}">
                        <strong>${instantsearch.highlight({
                            attribute: "title",
                            hit
                        })}</strong>
                    </a>

                    <p>${instantsearch.snippet({
                        attribute: "content",
                        hit
                    })}</p>
                </article>`;
            },

            empty(results) {
                return `No results for "<strong>${results.query}</strong>".`;
            }
        }
    }),

    instantsearch.widgets.pagination({
        container: "#pagination"
    })

]);

search.start();
</script>

<div id="pagination"></div>