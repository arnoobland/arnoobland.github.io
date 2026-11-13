#!/usr/bin/env python3
"""Writes the website's pages in every language of the game.

    python3 _build/pages.py

English is the base: index.html and privacy-policy.html at the top; the
others go in a folder each (ar/, zh/, fr/, ja/, ru/, es/), with their
screenshots in images/<code>/ (taken from the game in that language).
The translations were made with the help of AI. Change the words here,
not in the generated .html files. GitHub Pages does not publish folders
that start with "_", so this one stays private.
"""
import html
import os

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from texts import LANGS, T  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://arnoobland.github.io/"

STYLE = """
    :root {
      --sky: #9fd3e6;
      --hill: #6fa86a;
      --hill-dark: #4e8a55;
      --paper: #fbf5e8;
      --paper-edge: #e3d6bd;
      --ink: #6e503c;
      --gold: #fac83c;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: "Nunito", "Trebuchet MS", "Segoe UI", system-ui, sans-serif;
      color: var(--ink);
      background: linear-gradient(var(--sky) 0, #c8e6ef 380px, var(--hill) 380px, var(--hill-dark) 100%);
      background-attachment: fixed;
      min-height: 100vh;
      line-height: 1.6;
    }
    :lang(ar) body, body:lang(ar) { font-family: "Noto Sans Arabic", "Segoe UI", Tahoma, system-ui, sans-serif; }
    main {
      max-width: 760px;
      margin: 0 auto;
      padding: 20px 16px 48px;
    }
    nav.langs {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 6px;
      margin: 0 0 16px;
    }
    nav.langs a {
      padding: 4px 12px;
      border-radius: 999px;
      background: rgba(251, 245, 232, 0.75);
      color: var(--ink);
      text-decoration: none;
      font-size: 0.95rem;
    }
    nav.langs a[aria-current] {
      background: var(--hill);
      color: #fff;
      font-weight: bold;
    }
    header { text-align: center; }
    header img.logo {
      width: 128px;
      height: 128px;
      filter: drop-shadow(0 6px 10px rgba(40, 60, 40, 0.25));
    }
    h1 {
      margin: 8px 0 0;
      font-size: 2.6rem;
      color: #fffcf0;
      text-shadow: 0 3px 0 #5f8f9e, 0 0 12px rgba(40, 80, 90, 0.35);
    }
    .tagline {
      margin: 4px 0 24px;
      font-size: 1.15rem;
      font-weight: bold;
      color: var(--ink);
    }
    .card {
      background: var(--paper);
      border-radius: 22px;
      box-shadow: 0 5px 0 var(--paper-edge), 0 10px 24px rgba(30, 50, 30, 0.18);
      padding: 24px 24px 20px;
      margin: 0 0 24px;
    }
    .banner {
      display: block;
      width: 100%;
      border-radius: 16px;
      margin-bottom: 18px;
    }
    h2 { margin: 0 0 10px; font-size: 1.35rem; }
    p { margin: 0 0 12px; }
    ul.features { list-style: none; padding: 0; margin: 0; }
    ul.features li {
      position: relative;
      padding: 0 0 10px 0;
      padding-inline-start: 30px;
    }
    ul.features li::before {
      content: "";
      position: absolute;
      inset-inline-start: 4px;
      top: 0.45em;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: var(--gold);
      box-shadow: 0 2px 0 #cd9123;
    }
    .shots {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
    }
    .shots img {
      width: 100%;
      border-radius: 14px;
      box-shadow: 0 4px 10px rgba(30, 50, 30, 0.2);
    }
    .links { text-align: center; }
    .button {
      display: inline-block;
      margin: 6px;
      padding: 12px 26px;
      border-radius: 999px;
      background: var(--hill);
      box-shadow: 0 4px 0 var(--hill-dark);
      color: #fff;
      font-weight: bold;
      text-decoration: none;
    }
    .button:hover { background: #7cb877; }
    .button.light {
      background: var(--paper);
      color: var(--ink);
      box-shadow: 0 4px 0 var(--paper-edge);
      border: 2px solid var(--paper-edge);
    }
    footer {
      text-align: center;
      color: #eef6e6;
      font-size: 0.9rem;
    }
    footer p { margin: 0 0 6px; }
    @media (max-width: 600px) {
      h1 { font-size: 2.1rem; }
      .shots { grid-template-columns: repeat(2, 1fr); }
      .card { padding: 20px 16px 16px; }
    }
"""

POLICY_STYLE = """
    body {
      font-family: Arial, sans-serif;
      max-width: 850px;
      margin: 40px auto;
      padding: 0 20px;
      line-height: 1.7;
      color: #333;
      background: #fff;
    }
    body:lang(ar) { font-family: "Noto Sans Arabic", Tahoma, Arial, sans-serif; }
    h1, h2 { color: #6e503c; }
    a { color: #4e8a55; }
    .home { display: inline-flex; align-items: center; gap: 10px; font-weight: bold; text-decoration: none; }
    .home img { width: 40px; height: 40px; }
    nav.langs { margin: 12px 0 0; display: flex; flex-wrap: wrap; gap: 4px 12px; font-size: 0.95rem; }
    nav.langs a[aria-current] { font-weight: bold; color: #6e503c; text-decoration: none; }
    .note { background: #f6f1e4; border-radius: 8px; padding: 10px 14px; }
    footer {
      margin-top: 40px;
      border-top: 1px solid #ddd;
      padding-top: 20px;
      color: #666;
    }
"""

SHOTS = ["1-farm-market", "2-inventory", "3-oven", "4-crown-jar"]


def e(s):
    return html.escape(s, quote=False)


def a(s):
    return html.escape(s, quote=True)


def prefix(code):
    """The way from a language's folder to the site's root."""
    return "" if code == "en" else "../"


def page_url(code, page):
    return SITE + ("" if code == "en" else code + "/") + ("" if page == "index.html" else page)


def head(code, page, title, desc=None, style=STYLE):
    t, up = T[code], prefix(code)
    out = ['<!DOCTYPE html>',
           '<html lang="%s"%s>' % (code if code != "zh" else "zh-Hans", ' dir="rtl"' if code == "ar" else ""),
           '<head>',
           '  <meta charset="UTF-8">',
           '  <meta name="viewport" content="width=device-width, initial-scale=1.0">',
           '  <title>%s</title>' % e(title)]
    if desc:
        out += ['  <meta name="description" content="%s">' % a(desc),
                '  <meta property="og:title" content="Arnoob Land">',
                '  <meta property="og:description" content="%s">' % a(t["og"]),
                '  <meta property="og:image" content="%simages/feature-graphic.jpg">' % SITE]
    for c in LANGS:
        out.append('  <link rel="alternate" hreflang="%s" href="%s">' % (c if c != "zh" else "zh-Hans", page_url(c, page)))
    out.append('  <link rel="alternate" hreflang="x-default" href="%s">' % page_url("en", page))
    out += ['  <link rel="icon" type="image/png" href="%simages/favicon.png">' % up,
            '  <style>' + style.rstrip(), '  </style>', '</head>']
    return out


def langs_nav(code, page):
    links = []
    for c in LANGS:
        href = prefix(code) + ("" if c == "en" else c + "/") + page
        cur = ' aria-current="page"' if c == code else ""
        links.append('<a href="%s" hreflang="%s" lang="%s"%s>%s</a>' % (href, c, c, cur, e(T[c]["name"])))
    return links


def index(code):
    t, up = T[code], prefix(code)
    img = up + "images/" + ("" if code == "en" else code + "/")
    out = head(code, "index.html", "Arnoob Land", t["desc"])
    out += ['<body>', '  <main>',
            '    <nav class="langs" aria-label="%s">' % a(t["langlabel"])]
    out += ['      ' + l for l in langs_nav(code, "index.html")]
    out += ['    </nav>',
            '    <header>',
            '      <img class="logo" src="%simages/logo.png" alt="%s">' % (up, a(t["logoalt"])),
            '      <h1>Arnoob Land</h1>',
            '      <p class="tagline">%s</p>' % e(t["tagline"]),
            '    </header>',
            '',
            '    <section class="card">',
            '      <img class="banner" src="%simages/feature-graphic.jpg" alt="%s">' % (up, a(t["banneralt"])),
            '      <p>%s</p>' % e(t["intro"]),
            '      <ul class="features">']
    for bold, rest in t["features"]:
        out.append('        <li><strong>%s</strong> %s</li>' % (e(bold), e(rest)))
    out += ['      </ul>', '    </section>', '',
            '    <section class="card">',
            '      <h2>%s</h2>' % e(t["shotstitle"]),
            '      <div class="shots">']
    for name, alt in zip(SHOTS, t["shotalts"]):
        out.append('        <img src="%s%s.jpg" alt="%s" loading="lazy">' % (img, name, a(alt)))
    out += ['      </div>', '    </section>', '',
            '    <section class="card links">',
            '      <h2>%s</h2>' % e(t["parentstitle"]),
            '      <p>%s</p>' % e(t["parents"]),
            '      <a class="button" href="privacy-policy.html">%s</a>' % e(t["privacy"]),
            '      <a class="button light" href="%sapp-ads.txt">app-ads.txt</a>' % up,
            '    </section>', '',
            '    <footer>']
    if code != "en":
        out.append('      <p>%s</p>' % e(t["ainote"]))
    out += ['      <p>&copy; 2026 Arnoob Land</p>', '    </footer>', '  </main>', '</body>', '</html>', '']
    return "\n".join(out)


def policy(code):
    t, up = T[code], prefix(code)
    p = t["policy"]
    out = head(code, "privacy-policy.html", p["title"], style=POLICY_STYLE)
    out += ['<body>', '',
            '<a class="home" href="index.html"><img src="%simages/logo.png" alt="">Arnoob Land</a>' % up,
            '<nav class="langs" aria-label="%s">' % a(t["langlabel"])]
    out += ['  ' + l for l in langs_nav(code, "privacy-policy.html")]
    out += ['</nav>', '', '<h1>%s</h1>' % e(p["h1"]), '']
    if code != "en":
        out += ['<p class="note">%s</p>' % e(p["note"]), '']
    for section in p["sections"]:
        out.append('<h2>%s</h2>' % e(section[0]))
        for block in section[1:]:
            if isinstance(block, list):
                out.append('<ul>')
                out += ['  <li>%s</li>' % e(li) for li in block]
                out.append('</ul>')
            elif block == "@google":
                out.append('<p><a href="https://policies.google.com/privacy">%s</a></p>' % e(p["googlelink"]))
            elif block == "@more":
                out.append('<p>%s <a href="https://policies.google.com/privacy">%s</a>%s</p>' % (e(p["seemore"]), e(p["googlepolicy"]), p.get("end", ".")))
            elif block == "@contact":
                c = p["contact"]
                out += ['<p>',
                        '  <strong>%s</strong> Mohamed Abdelrahman<br>' % e(c[0]),
                        '  <strong>%s</strong> Arnoob Land<br>' % e(c[1]),
                        '  <strong>%s</strong> com.arnoobland<br>' % e(c[2]),
                        '  <strong>%s</strong> <a href="mailto:mabdalrahman@outlook.com">mabdalrahman@outlook.com</a>' % e(c[3]),
                        '</p>']
            else:
                out.append('<p>%s</p>' % e(block))
        out.append('')
    out += ['<footer>', '  &copy; 2026 Arnoob Land', '</footer>', '', '</body>', '</html>', '']
    return "\n".join(out)


def main():
    for code in LANGS:
        d = ROOT if code == "en" else os.path.join(ROOT, code)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(index(code))
        with open(os.path.join(d, "privacy-policy.html"), "w", encoding="utf-8") as f:
            f.write(policy(code))
        print("wrote", os.path.relpath(d, ROOT) or ".")


if __name__ == "__main__":
    main()
