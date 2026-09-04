#!/usr/bin/env python3
"""Validate repository-local links in Markdown files using only stdlib."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

FENCED_BLOCK = re.compile(r"(?ms)^(```|~~~).*?^\1[ \t]*$")
INLINE_CODE = re.compile(r"`[^`\n]*`")
INLINE_LINK = re.compile(r"!?\[[^\]]*]\(([^)\n]+)\)")
REFERENCE_LINK = re.compile(r"(?m)^[ \t]*\[[^\]]+]:[ \t]*(\S+)")
HTML_LINK = re.compile(r'''(?i)\b(?:href|src)=["']([^"']+)["']''')


@dataclass(frozen=True)
class BrokenLink:
    source: Path
    target: str
    reason: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    return parser.parse_args()


def strip_code(text: str) -> str:
    text = FENCED_BLOCK.sub("", text)
    return INLINE_CODE.sub("", text)


def normalize_destination(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        return value[1 : value.index(">")].strip()
    return value.split(maxsplit=1)[0]


def is_external_or_anchor(destination: str) -> bool:
    if not destination or destination.startswith("#") or destination.startswith("//"):
        return True
    parsed = urlsplit(destination)
    return bool(parsed.scheme)


def resolve_target(root: Path, source: Path, destination: str) -> tuple[Path | None, str | None]:
    parsed = urlsplit(destination)
    local_path = unquote(parsed.path)

    if not local_path:
        return None, None

    if local_path.startswith("/"):
        candidate = root / local_path.lstrip("/")
    else:
        candidate = source.parent / local_path

    try:
        candidate = candidate.resolve()
        candidate.relative_to(root)
    except ValueError:
        return None, "target escapes repository root"

    return candidate, None


def destinations(text: str):
    clean = strip_code(text)
    for match in INLINE_LINK.finditer(clean):
        yield normalize_destination(match.group(1))
    for match in REFERENCE_LINK.finditer(clean):
        yield normalize_destination(match.group(1))
    for match in HTML_LINK.finditer(clean):
        yield normalize_destination(match.group(1))


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    broken: list[BrokenLink] = []

    for source in sorted(root.rglob("*.md")):
        if ".git" in source.parts:
            continue
        text = source.read_text(encoding="utf-8")
        for destination in destinations(text):
            if is_external_or_anchor(destination):
                continue
            target, error = resolve_target(root, source.resolve(), destination)
            if error:
                broken.append(BrokenLink(source, destination, error))
                continue
            if target is not None and not target.exists():
                broken.append(BrokenLink(source, destination, "target does not exist"))

    if broken:
        print("Markdown local-link validation failed.")
        for item in broken:
            source = item.source.resolve().relative_to(root)
            print(f"- {source}: {item.target!r}: {item.reason}")
        return 1

    print("Markdown local-link validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
