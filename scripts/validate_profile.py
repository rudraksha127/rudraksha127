#!/usr/bin/env python3
"""Validate README local links, anchors, placeholders, and SVG assets."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

from defusedxml import ElementTree as ET
from defusedxml.common import DefusedXmlException

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
HTML_SRC_RE = re.compile(r"""(?:src|href)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
FENCE_OPEN_RE = re.compile(r"^\s{0,3}(\x60{3,}|~{3,})")
FENCE_CLOSE_RE = re.compile(r"^\s{0,3}(\x60+|~+)\s*$")
PLACEHOLDER_PATTERNS = (
    re.compile(r"\b(?:TODO|FIXME|TBD|PLACEHOLDER)\b", re.IGNORECASE),
    re.compile(r"\[(?:your\s+name|your\s+email|your\s+url|your\s+username|project\s+name|insert\s+[^]]+)\]", re.IGNORECASE),
    re.compile(r"https?://(?:www\.)?example\.(?:com|org|net)(?:[/\w?&=.#%-]*)?", re.IGNORECASE),
    re.compile(r"\bYOUR_[A-Z0-9_]+\b"),
    re.compile(r"\b(?:yourusername|your_username|your-deployed-instance)\b", re.IGNORECASE),
    re.compile(r"""(?:href|src)\s*=\s*["']#?["']""", re.IGNORECASE),
    re.compile(r"\]\(#\)"),
)
SVG_ROOT = "{http://www.w3.org/2000/svg}svg"


def strip_fenced_code(markdown: str) -> str:
    """Remove fenced code blocks so examples cannot create links or headings."""
    output: list[str] = []
    fence_char: str | None = None
    fence_size = 0

    for line in markdown.splitlines():
        if fence_char is None:
            opening = FENCE_OPEN_RE.match(line)
            if opening:
                token = opening.group(1)
                fence_char = token[0]
                fence_size = len(token)
                continue
            output.append(line)
            continue

        closing = FENCE_CLOSE_RE.match(line)
        if closing:
            token = closing.group(1)
            if token[0] == fence_char and len(token) >= fence_size:
                fence_char = None
                fence_size = 0

    return "\n".join(output)


def heading_slug(text: str) -> str:
    """Approximate GitHub's generated heading slug for visible heading text."""
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\x60([^\x60]*)\x60", r"\1", text)
    text = text.lower().strip()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def collect_anchors(markdown: str) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    visible_markdown = strip_fenced_code(markdown)

    for match in HEADING_RE.finditer(visible_markdown):
        base = heading_slug(match.group(1))
        count = counts.get(base, 0)
        counts[base] = count + 1
        anchors.add(base if count == 0 else f"{base}-{count}")

    return anchors


def find_placeholders(markdown: str) -> list[str]:
    """Return common unfinished placeholders outside fenced examples."""
    visible_markdown = strip_fenced_code(markdown)
    found = {
        match.group(0)
        for pattern in PLACEHOLDER_PATTERNS
        for match in pattern.finditer(visible_markdown)
    }
    return sorted(found, key=str.casefold)


def validate_svg(svg_path: Path) -> None:
    """Parse a safe XML document and require the actual SVG root element."""
    root = ET.parse(svg_path).getroot()
    if root.tag != SVG_ROOT:
        raise ValueError(f"root element must be {SVG_ROOT!r}, got {root.tag!r}")


def main() -> int:
    if not README.is_file():
        print("ERROR: README.md is missing.")
        return 1

    markdown = README.read_text(encoding="utf-8")
    visible_markdown = strip_fenced_code(markdown)
    failures: list[str] = []
    anchors = collect_anchors(markdown)

    for placeholder in find_placeholders(markdown):
        failures.append(f"Placeholder detected: {placeholder}")

    targets = MARKDOWN_LINK_RE.findall(visible_markdown)
    targets.extend(HTML_SRC_RE.findall(visible_markdown))

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
            validate_svg(svg_path)
        except (ET.ParseError, DefusedXmlException, ValueError, OSError) as exc:
            failures.append(f"Invalid or unsafe SVG asset: {svg_path.relative_to(ROOT)} ({exc})")

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
