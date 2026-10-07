#!/usr/bin/env python3
"""Build index.html from the chapter summaries in content/.

Usage:  pip install markdown && python3 build.py
"""
import html
import json
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
TEMPLATE = ROOT / "template.html"
OUT = ROOT / "index.html"

PARTS = [
    ("Futures, forwards & swaps", range(1, 9)),
    ("Options", range(9, 18)),
    ("Risk management", range(18, 23)),
    ("Credit", range(23, 25)),
    ("Advanced models", range(25, 28)),
    ("Interest rate derivatives", range(28, 33)),
    ("Applications & lessons", range(33, 36)),
]


def slugify(text):
    text = re.sub(r"<[^>]+>", "", text).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "section"


def build_chapter(path):
    num = int(path.name[:2])
    src = path.read_text(encoding="utf-8")
    first, body = src.split("\n", 1)
    title = re.sub(r"^# Ch \d+ — ", "", first.strip())
    tldr_match = re.search(r"\*\*TL;DR:\*\*\s*(.+)", body)
    tldr_md = tldr_match.group(1).strip() if tldr_match else ""
    if tldr_match:
        body = body.replace(tldr_match.group(0), "", 1)

    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
    body_html = md.convert(body)
    tldr_html = markdown.markdown(tldr_md)[3:-4]  # strip <p></p>

    cid = f"ch-{num:02d}"
    sections = []

    def add_anchor(m):
        heading = m.group(1)
        sid = f"{cid}--{slugify(heading)}"
        sections.append({"id": sid, "title": re.sub(r"<[^>]+>", "", heading)})
        return (
            f'<h2 id="{sid}" class="sec">{heading}'
            f'<button class="sec-mark" data-target="{sid}" aria-label="Bookmark this section" title="Bookmark this section">'
            f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h12v18l-6-4-6 4z"/></svg></button></h2>'
        )

    body_html = re.sub(r"<h2>(.*?)</h2>", add_anchor, body_html)
    body_html = re.sub(r"<table>", '<div class="table-wrap"><table>', body_html)
    body_html = body_html.replace("</table>", "</table></div>")

    words = len(re.sub(r"<[^>]+>", " ", body_html).split())
    minutes = max(1, round(words / 120))

    return {
        "num": num,
        "id": cid,
        "title": title,
        "tldr": tldr_html,
        "html": body_html,
        "sections": sections,
        "minutes": minutes,
    }


def main():
    chapters = [build_chapter(p) for p in sorted(CONTENT.glob("[0-9][0-9]-*.md"))]
    by_num = {c["num"]: c for c in chapters}

    nav = []
    for part, nums in PARTS:
        items = []
        for n in nums:
            c = by_num.get(n)
            if not c:
                continue
            items.append(
                f'<li><a href="#{c["id"]}" data-ch="{c["id"]}" data-search="{html.escape((c["title"] + " " + " ".join(s["title"] for s in c["sections"])).lower())}">'
                f'<span class="num">{n:02d}</span><span class="t">{html.escape(c["title"])}</span>'
                f'<span class="dot" aria-hidden="true"></span></a></li>'
            )
        nav.append(f'<div class="part"><h3>{html.escape(part)}</h3><ul>{"".join(items)}</ul></div>')

    articles = []
    for i, c in enumerate(chapters):
        prev_c = chapters[i - 1] if i > 0 else None
        next_c = chapters[i + 1] if i < len(chapters) - 1 else None
        toc = "".join(f'<li><a href="#{s["id"]}">{html.escape(s["title"])}</a></li>' for s in c["sections"])
        pager = '<nav class="pager">'
        pager += (
            f'<a class="prev" href="#{prev_c["id"]}"><small>← Previous</small><span>{prev_c["num"]:02d} · {html.escape(prev_c["title"])}</span></a>'
            if prev_c else "<span></span>"
        )
        pager += (
            f'<a class="next" href="#{next_c["id"]}"><small>Next →</small><span>{next_c["num"]:02d} · {html.escape(next_c["title"])}</span></a>'
            if next_c else "<span></span>"
        )
        pager += "</nav>"
        articles.append(
            f'''<article class="chapter" id="{c["id"]}" data-title="{html.escape(c["title"])}" hidden>
  <header class="ch-head">
    <p class="eyebrow">Chapter {c["num"]} · {c["minutes"]} min read</p>
    <h1>{html.escape(c["title"])}</h1>
    <p class="tldr"><span>TL;DR</span>{c["tldr"]}</p>
    <div class="ch-actions">
      <button class="btn bm-btn" data-target="{c["id"]}" aria-pressed="false">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h12v18l-6-4-6 4z"/></svg><span>Bookmark</span></button>
      <button class="btn done-btn" data-target="{c["id"]}" aria-pressed="false">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5"/></svg><span>Mark as read</span></button>
      <button class="btn link-btn" data-target="{c["id"]}">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/></svg><span>Copy link</span></button>
    </div>
    <details class="toc"><summary>On this page</summary><ul>{toc}</ul></details>
  </header>
  <div class="prose">{c["html"]}</div>
  {pager}
</article>'''
        )

    meta = {c["id"]: {"num": c["num"], "title": c["title"],
                      "sections": {s["id"]: s["title"] for s in c["sections"]}} for c in chapters}

    page = TEMPLATE.read_text(encoding="utf-8")
    page = page.replace("{{NAV}}", "\n".join(nav))
    page = page.replace("{{ARTICLES}}", "\n".join(articles))
    page = page.replace("{{META}}", json.dumps(meta, ensure_ascii=False))
    page = page.replace("{{COUNT}}", str(len(chapters)))
    OUT.write_text(page, encoding="utf-8")
    print(f"Wrote {OUT} ({len(chapters)} chapters, {OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
