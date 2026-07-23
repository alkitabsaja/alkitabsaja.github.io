---
layout: default
title: Search
permalink: /search/
---

# Search

<div id="searchbox"></div>

<h2>Articles</h2>
<div id="docs-hits"></div>

<h2>Ebooks</h2>
<div id="news-hits"></div>

<h2>Alkitabiah.org</h2>
<div id="ebooks-hits"></div>

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
    indexName: "ghpost_articles",
    searchClient
});

search.addWidgets([

    instantsearch.widgets.searchBox({
        container: "#searchbox",
        placeholder: "Search..."
    }),

    instantsearch.widgets.configure({
        hitsPerPage: 10
    }),

    instantsearch.widgets.hits({
        container: "#docs-hits",
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
            }
        }
    }),

    instantsearch.widgets.index({
        indexName: "ghdocs_articles"
    }).addWidgets([
        instantsearch.widgets.configure({
            hitsPerPage: 10
        }),
        instantsearch.widgets.hits({
            container: "#news-hits",
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
                }
            }
        })
    ]),

    instantsearch.widgets.index({
        indexName: "alkitabiah_searchable_posts"
    }).addWidgets([
        instantsearch.widgets.configure({
            hitsPerPage: 10
        }),
        instantsearch.widgets.hits({
            container: "#ebooks-hits",
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
                }
            }
        })
    ])

]);

search.start();
</script>