import html
from pathlib import Path

import feedparser

OUT = Path("_docs/news")
OUT.mkdir(parents=True, exist_ok=True)

FEEDS = {
    "Diselamatkan": "https://www.matikemana.com/web1/feed",
    "Alkitabiah": "https://alkitabiah.org/tag/keselamatan/feed/",
    "Fundamentalis": "https://kristenfundamentalis.wordpress.com/keselamatan/feed",
    "Yesus Tuhan": "https://yesustuhan.wordpress.com/tag/keselamatan/feed/",
}

for name, url in FEEDS.items():

    feed = feedparser.parse(url)

    md = [
        "---",
        f"title: {feed.feed.get('title', name)}",
        "layout: default",
        "---",
        "",
        f"# {feed.feed.get('title', name)}",
        "",
    ]

    for entry in feed.entries:

        title = html.unescape(entry.get("title", "Untitled")).strip()

        summary = html.unescape(entry.get("summary", "")).strip()

        summary = " ".join(summary.split())

        link = entry.get("link", "")

        md += [
            f"## {title}",
            "",
            summary,
            "",
            f"Source: {link}",
            "",
            "---",
            "",
        ]

    (OUT / f"{name}.md").write_text(
        "\n".join(md),
        encoding="utf-8",
    )