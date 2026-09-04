#!/usr/bin/env python3
"""Fail on high-confidence accidental disclosure patterns in the public tree.

This validator intentionally uses generic patterns. It must never contain a
denylist copied from private repositories, machines, projects, or runtime state.
"""

from __future__ import annotations

import argparse
import ipaddress
import re
from dataclasses import dataclass
from pathlib import Path

MAX_TEXT_BYTES = 2 * 1024 * 1024
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules"}
PLACEHOLDER_VALUES = {
    "changeme",
    "example",
    "example-value",
    "placeholder",
    "redacted",
    "replace-me",
    "sample",
    "secret",
    "token",
    "your-token-here",
}

HIGH_CONFIDENCE_PATTERNS = (
    (
        "private-key",
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ),
    (
        "github-token",
        re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    ),
    (
        "aws-access-key",
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    ),
    (
        "slack-token",
        re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    ),
    (
        "bearer-token",
        re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{20,}\b"),
    ),
    (
        "credentialed-url",
        re.compile(r"https?://[^/\s:@]+:[^/\s@]+@[^/\s]+"),
    ),
    (
        "unix-user-path",
        re.compile(r"(?<![A-Za-z0-9_])/(?:Users|home)/[A-Za-z0-9._-]+/"),
    ),
    (
        "root-user-path",
        re.compile(r"(?<![A-Za-z0-9_])/" + "root" + r"/"),
    ),
    (
        "windows-user-path",
        re.compile(r"(?i)\b[A-Z]:\\Users\\[^\\\r\n]+\\"),
    ),
)

CREDENTIAL_ASSIGNMENT = re.compile(
    r"""(?ix)
    \b(password|passwd|secret|token|api[_-]?key|credential)
    \b\s*[:=]\s*
    ["']?([A-Za-z0-9._~+/=-]{8,})["']?
    """
)

IPV4_CANDIDATE = re.compile(
    r"(?<![0-9])(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![0-9])"
)


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    category: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    return parser.parse_args()


def iter_text_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        try:
            if path.stat().st_size > MAX_TEXT_BYTES:
                continue
            raw = path.read_bytes()
        except OSError:
            continue
        if b"\x00" in raw:
            continue
        try:
            yield path, raw.decode("utf-8")
        except UnicodeDecodeError:
            continue


def is_placeholder(value: str) -> bool:
    normalized = value.strip("\"'").lower()
    return (
        normalized in PLACEHOLDER_VALUES
        or normalized.startswith(("example-", "sample-", "placeholder-", "redacted-"))
        or normalized.endswith(("-example", "-sample", "-placeholder"))
    )


def is_private_network_literal(token: str) -> bool:
    try:
        ip = ipaddress.ip_address(token)
    except ValueError:
        return False
    if ip.version != 4:
        return False
    first, second, _, _ = (int(part) for part in token.split("."))
    return (
        first == 10
        or (first == 172 and 16 <= second <= 31)
        or (first == 192 and second == 168)
        or (first == 169 and second == 254)
    )


def scan_text(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []

    for line_no, line in enumerate(text.splitlines(), start=1):
        for category, pattern in HIGH_CONFIDENCE_PATTERNS:
            if pattern.search(line):
                findings.append(Finding(path, line_no, category))

        match = CREDENTIAL_ASSIGNMENT.search(line)
        if match and not is_placeholder(match.group(2)):
            findings.append(Finding(path, line_no, "credential-assignment"))

        for match in IPV4_CANDIDATE.finditer(line):
            if is_private_network_literal(match.group(0)):
                findings.append(Finding(path, line_no, "private-network-address"))

    return findings


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    findings: list[Finding] = []

    for path, text in iter_text_files(root):
        findings.extend(scan_text(path, text))

    if findings:
        print("Public-safety validation failed.")
        print("Matched values are intentionally not echoed.")
        for finding in findings:
            relative = finding.path.resolve().relative_to(root)
            print(f"- {relative}:{finding.line}: {finding.category}")
        print(
            "\nDo not add private values to a validator denylist. "
            "Remove/generalize the content or improve the generic rule."
        )
        return 1

    print("Public-safety validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
