#!/usr/bin/env python3
"""Validate README local links, in-page anchors, placeholders, and SVG assets."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
HTML_SRC_RE = re.compile(r"""(?:src|href)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
PLACEHOLDER_PATTERNS = (
    "yourusername",
    "your_username",
    "your-deployed-instance",
    "YOUR_USERNAME",
    'href="#"',
    "](#)",
)


def heading_slug(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = text.lower().strip()
    text = re.sub(r"[^\w\- ]", "", text)
    return re.sub(r"\s+", "-", text)


def collect_anchors(markdown: str) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for match in HEADING_RE.finditer(markdown):
        base = heading_slug(match.group(1))
        count = counts.get(base, 0)
        counts[base] = count + 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


def main() -> int:
    if not README.is_file():
        print("ERROR: README.md is missing.")
        return 1

    markdown = README.read_text(encoding="utf-8")
    failures: list[str] = []
    anchors = collect_anchors(markdown)

    for placeholder in PLACEHOLDER_PATTERNS:
        if placeholder in markdown:
            failures.append(f"Placeholder detected: {placeholder}")

    targets = MARKDOWN_LINK_RE.findall(markdown)
    targets.extend(HTML_SRC_RE.findall(markdown))

    checked_local = 0
    checked_anchors = 0
    svg_files: set[Path] = set()

    for raw_target in targets:
        target = unquote(raw_target.strip())
        if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
            continue
        if target.startswith("#"):
            anchor = target[1:]
            checked_anchors += 1
            if anchor not in anchors:
                failures.append(f"Broken in-page anchor: #{anchor}")
            continue

        parsed = urlparse(target)
        if parsed.scheme or parsed.netloc:
            continue

        path_part = parsed.path
        if not path_part:
            continue
        local_path = (ROOT / path_part).resolve()
        try:
            local_path.relative_to(ROOT.resolve())
        except ValueError:
            failures.append(f"Local path escapes repository: {target}")
            continue

        checked_local += 1
        if not local_path.exists():
            failures.append(f"Missing local target: {target}")
        elif local_path.suffix.lower() == ".svg":
            svg_files.add(local_path)

    for svg_path in svg_files:
        try:
            ET.parse(svg_path)
        except ET.ParseError as exc:
            failures.append(f"Invalid SVG XML: {svg_path.relative_to(ROOT)} ({exc})")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1

    print(
        "Profile validation passed: "
        f"{checked_local} local targets, "
        f"{checked_anchors} in-page anchors, "
        f"{len(svg_files)} SVG asset(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
