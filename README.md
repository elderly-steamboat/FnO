# F&O Notes

Concise theory summaries of all 35 chapters of John C. Hull's *Options, Futures, and Other Derivatives* (8th ed.), published as a single reading website.

**Read online:** https://elderly-steamboat.github.io/FnO/

## Features
- One chapter per page view with previous/next navigation; every chapter and section has its own URL, so browser bookmarks work.
- In-page bookmarks for chapters or individual sections, a "mark as read" progress tracker, and "continue reading" that returns you to where you stopped. All of this is saved in your browser.
- Chapter filter, dark mode, mobile layout, keyboard shortcuts (`←`/`→`, `b`, `m`, `/`, `h`).

## Editing
Summaries live in `content/*.md`. After editing, rebuild the page:

```bash
pip install markdown
python3 build.py      # writes index.html from content/ + template.html
```
