#!/usr/bin/env python3
"""Bump version fields across repository manifests."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from validate_repo import PLUGIN_NAME, VERSIONED_MANIFESTS  # noqa: E402

ROOT = _SCRIPTS.parent
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")


def parse_version_arg(argv: list[str]) -> str | None:
    if len(argv) != 2:
        return None
    version = argv[1]
    if not VERSION_RE.match(version):
        return None
    return version


def dumps_pretty(data: object) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def set_versions_in_dict(data: dict, version: str, rel: str) -> bool:
    changed = False
    if data.get("version") != version:
        data["version"] = version
        changed = True
    return changed


def bump_claude_marketplace(path: Path, version: str) -> bool:
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("marketplace root must be object")
    changed = False
    meta = data.get("metadata")
    if isinstance(meta, dict) and meta.get("version") != version:
        meta["version"] = version
        changed = True
    plugins = data.get("plugins")
    if isinstance(plugins, list):
        for entry in plugins:
            if isinstance(entry, dict) and entry.get("name") == PLUGIN_NAME:
                if entry.get("version") != version:
                    entry["version"] = version
                    changed = True
    if not changed:
        return False
    new_text = dumps_pretty(data)
    if new_text == text:
        return False
    path.write_text(new_text, encoding="utf-8")
    return True


def bump_manifest(path: Path, rel: str, version: str) -> bool:
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError(f"{rel}: root must be object")
    changed = set_versions_in_dict(data, version, rel)
    if not changed:
        return False
    new_text = dumps_pretty(data)
    if new_text == text:
        return False
    path.write_text(new_text, encoding="utf-8")
    return True


def main(argv: list[str]) -> int:
    version = parse_version_arg(argv)
    if version is None:
        print("usage: python3 scripts/bump_version.py MAJOR.MINOR.PATCH", file=sys.stderr)
        return 2

    updated: list[str] = []
    for rel in VERSIONED_MANIFESTS:
        path = ROOT / rel
        if bump_manifest(path, rel, version):
            updated.append(rel)

    marketplace = ROOT / ".claude-plugin" / "marketplace.json"
    if bump_claude_marketplace(marketplace, version):
        updated.append(".claude-plugin/marketplace.json")

    # unchanged files are left as-is to preserve formatting
    if updated:
        print("updated:", ", ".join(updated))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))