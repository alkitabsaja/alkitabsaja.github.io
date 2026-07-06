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

# Generate one markdown file per feed
for name, url in FEEDS.items():

    feed = feedparser.parse(url)

    title = html.unescape(feed.feed.get("title", name)).strip()

    md = [
        "---",
        f'title: "{title}"',
        "layout: default",
        "---",
        "",
        f"# {title}",
        "",
    ]

    for entry in feed.entries:

        entry_title = html.unescape(
            entry.get("title", "Untitled")
        ).strip()

        summary = html.unescape(
            entry.get("summary", "")
        ).strip()

        summary = " ".join(summary.split())

        link = entry.get("link", "")

        md.extend([
            f"## {entry_title}",
            "",
            summary,
            "",
            f"[Read more]({link})",
            "",
            "---",
            "",
        ])

    (OUT / f"{name}.md").write_text(
        "\n".join(md),
        encoding="utf-8",
    )

# Generate combined News page
index = [
    "---",
    'title: "News"',
    "layout: default",
    "permalink: /news/",
    "---",
    "",
    "# News",
    "",
]

for file in sorted(OUT.glob("*.md")):
    index.extend([
        f"{{% include_relative news/{file.name} %}}",
        "",
    ])

Path("_docs/news.md").write_text(
    "\n".join(index),
    encoding="utf-8",
)

from datetime import datetime, timezone
from email.utils import format_datetime
from urllib.parse import quote
from xml.sax.saxutils import escape
import calendar

# -----------------------------------------------------------------------------
# Generate combined RSS feed
# -----------------------------------------------------------------------------

SITE_TITLE = "News"
SITE_LINK = "https://your-domain.com/news/"
SITE_DESCRIPTION = "Aggregated news feed"

items = []

for name, url in FEEDS.items():

    feed = feedparser.parse(url)

    source = html.unescape(feed.feed.get("title", name)).strip()

    for entry in feed.entries:

        title = html.unescape(
            entry.get("title", "Untitled")
        ).strip()

        summary = html.unescape(
            entry.get("summary", "")
        ).strip()

        summary = " ".join(summary.split())

        link = entry.get("link", "")

        if hasattr(entry, "published_parsed") and entry.published_parsed:
            dt = datetime.fromtimestamp(
                calendar.timegm(entry.published_parsed),
                tz=timezone.utc,
            )
        else:
            dt = datetime.now(timezone.utc)

        guid = quote(link, safe="")

        items.append({
            "title": title,
            "summary": summary,
            "link": link,
            "date": dt,
            "guid": guid,
            "source": source,
        })

items.sort(
    key=lambda x: x["date"],
    reverse=True,
)

rss = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<rss version="2.0">',
    "<channel>",
    f"<title>{escape(SITE_TITLE)}</title>",
    f"<link>{escape(SITE_LINK)}</link>",
    f"<description>{escape(SITE_DESCRIPTION)}</description>",
    f"<lastBuildDate>{format_datetime(datetime.now(timezone.utc))}</lastBuildDate>",
]

for item in items:

    rss.extend([
        "<item>",
        f"<title>{escape(item['title'])}</title>",
        f"<link>{escape(item['link'])}</link>",
        f"<guid>{item['guid']}</guid>",
        f"<pubDate>{format_datetime(item['date'])}</pubDate>",
        "<description><![CDATA[",
        item["summary"],
        f'<p><a href="{item["link"]}">Read more</a></p>',
        f"<p><em>{item['source']}</em></p>",
        "]]></description>",
        "</item>",
    ])

rss.extend([
    "</channel>",
    "</rss>",
])

Path("feed.xml").write_text(
    "\n".join(rss),
    encoding="utf-8",
)