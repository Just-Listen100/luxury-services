#!/usr/bin/env python3
"""Site checks for the Luxury Services one-page site.

Run on every push. Fails the build if the site drifts from the brand rules:
wrong name, images anywhere, old brand strings, or a broken structure.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "index.html"

REQUIRED_STRINGS = [
    "Luxury Services",
    "systems that never call home",
    "mailto:lamisonj19@gmail.com",
    "github.com/Just-Listen100/luxury-services",
]
FORBIDDEN_STRINGS = [
    "AetherGuard",          # retired brand name, must never reappear
    "<img",                  # typography only, no images of any kind
    "<img ",                 # guard against spacing variants
]
VOID_TAGS = {"meta", "link", "br", "img", "hr", "input"}


class StructureCheck(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID_TAGS:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack:
            self.errors.append(f"closing tag </{tag}> with nothing open")
        elif self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.errors.append(
                f"</{tag}> closes while <{self.stack[-1]}> is open"
            )

    def handle_data(self, data):
        self.text.append(data)


def main() -> int:
    failures = []

    if not PAGE.exists():
        print(f"FAIL: {PAGE.name} not found")
        return 1
    html = PAGE.read_text(encoding="utf-8")

    parser = StructureCheck()
    parser.feed(html)
    if parser.errors:
        failures.append("broken HTML structure: " + "; ".join(parser.errors[:5]))
    if parser.stack:
        failures.append(f"unclosed tags: {parser.stack}")

    text = " ".join(parser.text)
    for needle in REQUIRED_STRINGS:
        if needle not in html:
            failures.append(f"missing required string: {needle!r}")
    for needle in FORBIDDEN_STRINGS:
        if needle.lower() in html.lower():
            failures.append(f"forbidden string present: {needle!r}")

    links = re.findall(r'href="([^"]+)"', html)
    bad_links = [h for h in links if not (h.startswith("mailto:") or h.startswith("#") or h.startswith("https://"))]
    if bad_links:
        failures.append(f"links must be mailto, anchor, or https: {bad_links}")

    if failures:
        print(f"FAILED: {len(failures)} problem(s)")
        for f in failures:
            print(f"  - {f}")
        return 1

    print(f"OK: {PAGE.name} clean. brand name present, no images, structure valid, {len(links)} links checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
