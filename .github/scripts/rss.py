import calendar
import html
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape

import feedparser

SITE_TITLE = "Berita Keselamatan Kekal"
SITE_LINK = "https://alkitabsaja.surge.sh/news/"
SITE_DESCRIPTION = "Bagaimana Manusia Diselamatkan dari Neraka Kekal"

FEEDS = {
    "Keselamatan": "https://www.slamat.link/ingatmati/feed.xml",
    "Alkitabiah": "https://alkitabiah.org/tag/keselamatan/feed/",
    "Fundamentalis": "https://kristenfundamentalis.wordpress.com/keselamatan/feed",
    "YesusTuhan": "https://yesustuhan.wordpress.com/tag/keselamatan/feed/",
}

INCLUDE_DIR = Path("_includes")
INCLUDE_DIR.mkdir(parents=True, exist_ok=True)

items = []
merged = []

for source_name, url in FEEDS.items():

    feed = feedparser.parse(url)

    source = html.unescape(
        feed.feed.get("title", source_name)
    ).strip()

#    merged.extend([
#        f"## {source}",
#        "",
#    ])

    for entry in feed.entries:

        title = html.unescape(
            entry.get("title", "Untitled")
        ).strip()

        summary = html.unescape(
            entry.get("summary", "")
        ).strip()

        summary = " ".join(summary.split())

        link = entry.get("link", "")

        if getattr(entry, "published_parsed", None):
            dt = datetime.fromtimestamp(
                calendar.timegm(entry.published_parsed),
                tz=timezone.utc,
            )
        else:
            dt = datetime.now(timezone.utc)

        items.append({
            "title": title,
            "summary": summary,
            "link": link,
            "date": dt,
            "source": source,
        })

items.sort(
    key=lambda i: i["date"],
    reverse=True,
)

for item in items:

    merged.extend([
        f"# [{item['title']}]({item['link']})",
        "",
        item["summary"],
        "",
#        f"*Source: {item['source']}*",
#        "",
        "---",
        "",
    ])
    
(INCLUDE_DIR / "news.md").write_text(
    "\n".join(merged),
    encoding="utf-8",
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
        f"<guid>{quote(item['link'], safe='')}</guid>",
        f"<pubDate>{format_datetime(item['date'])}</pubDate>",
        "<description><![CDATA[",
        item["summary"],
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
