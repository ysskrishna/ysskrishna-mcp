#!/usr/bin/env python3
"""Repository manifest and layout checks for ysskrishna-mcp."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VERSIONED_MANIFESTS = [
    "plugin.json",
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
    ".kimi-plugin/plugin.json",
    "gemini-extension.json",
    "package.json",
]

PLUGIN_NAME = "ysskrishna-mcp"
NPM_PACKAGE_NAME = "@ysskrishna/ysskrishna-mcp"

ROOT_PLUGIN_ALLOWED_KEYS = frozenset(
    {
        "$schema",
        "name",
        "version",
        "description",
        "author",
        "homepage",
        "repository",
        "license",
        "keywords",
        "extensions",
    }
)

REQUIRED_PACKAGE_FILES = frozenset(
    {
        "index.js",
        "skills/",
        ".claude-plugin/",
        ".codex-plugin/",
        ".cursor-plugin/",
        ".kimi-plugin/",
        ".agents/",
        "plugin.json",
        "gemini-extension.json",
        "skills.sh.json",
        "README.md",
        "LICENSE",
        "CHANGELOG.md",
    }
)

README_REQUIRED_SUBSTRINGS = (
    "npx skills add ysskrishna/ysskrishna-mcp",
    "gh skill install ysskrishna/ysskrishna-mcp",
    "@ysskrishna/ysskrishna-mcp",
)

SKILLS_DIR = ROOT / "skills"
CONNECT_SKILL_DIR = "connect-ysskrishna-mcp"


def err(message: str) -> None:
    print(message)


def load_json(path: Path) -> tuple[object | None, str | None]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return None, f"{path.relative_to(ROOT)}: cannot read file ({exc})"
    try:
        return json.loads(text), None
    except json.JSONDecodeError as exc:
        return None, f"{path.relative_to(ROOT)}: invalid JSON ({exc})"


def parse_skill_frontmatter_name(text: str) -> str | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    for line in block.splitlines():
        line = line.strip()
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip()
    return None


def check_versioned_manifests(errors: list[str]) -> str | None:
    versions: list[str] = []
    for rel in VERSIONED_MANIFESTS:
        path = ROOT / rel
        data, parse_err = load_json(path)
        if parse_err:
            errors.append(parse_err)
            continue
        if not isinstance(data, dict):
            errors.append(f"{rel}: root must be a JSON object")
            continue
        expected_name = NPM_PACKAGE_NAME if rel == "package.json" else PLUGIN_NAME
        name = data.get("name")
        if name != expected_name:
            errors.append(f"{rel}: name must be {expected_name!r}, got {name!r}")
        version = data.get("version")
        if not isinstance(version, str) or not version:
            errors.append(f"{rel}: missing or invalid version")
        else:
            versions.append(version)
    if not versions:
        return None
    unique = set(versions)
    if len(unique) != 1:
        errors.append(
            f"version mismatch across manifests: {', '.join(sorted(unique))}"
        )
    return versions[0]


def check_claude_marketplace(errors: list[str], version: str | None) -> None:
    path = ROOT / ".claude-plugin" / "marketplace.json"
    data, parse_err = load_json(path)
    if parse_err:
        errors.append(parse_err)
        return
    if not isinstance(data, dict):
        errors.append(".claude-plugin/marketplace.json: root must be a JSON object")
        return
    meta = data.get("metadata")
    if not isinstance(meta, dict):
        errors.append(".claude-plugin/marketplace.json: metadata must be an object")
    elif version is not None and meta.get("version") != version:
        errors.append(
            ".claude-plugin/marketplace.json: metadata.version must match bundle version"
        )
    plugins = data.get("plugins")
    if not isinstance(plugins, list):
        errors.append(".claude-plugin/marketplace.json: plugins must be a list")
        return
    match = None
    for entry in plugins:
        if isinstance(entry, dict) and entry.get("name") == PLUGIN_NAME:
            match = entry
            break
    if match is None:
        errors.append(
            ".claude-plugin/marketplace.json: missing plugins entry named ysskrishna-mcp"
        )
        return
    if version is not None and match.get("version") != version:
        errors.append(
            ".claude-plugin/marketplace.json: plugin ysskrishna-mcp version must match bundle"
        )


def check_root_plugin_json(errors: list[str]) -> None:
    path = ROOT / "plugin.json"
    data, parse_err = load_json(path)
    if parse_err or not isinstance(data, dict):
        return
    extra = set(data) - ROOT_PLUGIN_ALLOWED_KEYS
    if extra:
        errors.append(
            f"plugin.json: disallowed keys: {', '.join(sorted(extra))}"
        )


def check_platform_plugins(errors: list[str]) -> None:
    for rel in (
        ".cursor-plugin/plugin.json",
        ".codex-plugin/plugin.json",
        ".kimi-plugin/plugin.json",
    ):
        path = ROOT / rel
        data, parse_err = load_json(path)
        if parse_err or not isinstance(data, dict):
            continue
        if data.get("skills") != "./skills/":
            errors.append(f"{rel}: skills must be './skills/'")

    cursor_path = ROOT / ".cursor-plugin" / "plugin.json"
    data, parse_err = load_json(cursor_path)
    if parse_err or not isinstance(data, dict):
        return
    author = data.get("author")
    if not isinstance(author, dict) or set(author) != {"name"}:
        errors.append(
            ".cursor-plugin/plugin.json: author must be an object with exactly key 'name'"
        )


def check_gemini_extension(errors: list[str]) -> None:
    path = ROOT / "gemini-extension.json"
    data, parse_err = load_json(path)
    if parse_err or not isinstance(data, dict):
        return
    if not isinstance(data.get("version"), str) or not data.get("version"):
        errors.append("gemini-extension.json: missing version")
    if not isinstance(data.get("description"), str) or not data.get("description"):
        errors.append("gemini-extension.json: missing description")


def check_agents_marketplace(errors: list[str]) -> None:
    path = ROOT / ".agents" / "plugins" / "marketplace.json"
    data, parse_err = load_json(path)
    if parse_err:
        errors.append(parse_err)
        return
    if not isinstance(data, dict):
        errors.append(".agents/plugins/marketplace.json: root must be a JSON object")
        return
    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        errors.append(
            ".agents/plugins/marketplace.json: plugins must be a non-empty list"
        )
        return
    match = None
    for entry in plugins:
        if isinstance(entry, dict) and entry.get("name") == PLUGIN_NAME:
            match = entry
            break
    if match is None:
        errors.append(
            ".agents/plugins/marketplace.json: missing ysskrishna-mcp plugin entry"
        )
        return
    source = match.get("source")
    if not isinstance(source, dict):
        errors.append(
            ".agents/plugins/marketplace.json: ysskrishna-mcp source must be an object"
        )
    else:
        if source.get("source") != "local":
            errors.append(
                ".agents/plugins/marketplace.json: ysskrishna-mcp source.source must be 'local'"
            )
        if source.get("path") != "./":
            errors.append(
                ".agents/plugins/marketplace.json: ysskrishna-mcp source.path must be './'"
            )
    policy = match.get("policy")
    if not isinstance(policy, dict):
        errors.append(
            ".agents/plugins/marketplace.json: ysskrishna-mcp policy must be an object"
        )
    else:
        if policy.get("installation") != "AVAILABLE":
            errors.append(
                ".agents/plugins/marketplace.json: policy.installation must be 'AVAILABLE'"
            )
        if policy.get("authentication") != "ON_INSTALL":
            errors.append(
                ".agents/plugins/marketplace.json: policy.authentication must be 'ON_INSTALL'"
            )


def check_package_files(errors: list[str]) -> None:
    path = ROOT / "package.json"
    data, parse_err = load_json(path)
    if parse_err or not isinstance(data, dict):
        return
    files = data.get("files")
    if not isinstance(files, list):
        errors.append("package.json: files must be a list")
        return
    as_set = set(files)
    missing = REQUIRED_PACKAGE_FILES - as_set
    for entry in sorted(missing):
        errors.append(f"package.json: files missing required entry {entry!r}")
    if "openclaw.plugin.json" in as_set:
        errors.append("package.json: files must not include openclaw.plugin.json")


def check_readme(errors: list[str]) -> None:
    path = ROOT / "README.md"
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"README.md: cannot read file ({exc})")
        return
    for needle in README_REQUIRED_SUBSTRINGS:
        if needle not in text:
            errors.append(f"README.md: must contain substring {needle!r}")
    if re.search(r"clawhub", text, re.IGNORECASE):
        errors.append("README.md: must not mention clawhub (case-insensitive)")


def check_skills_layout(errors: list[str]) -> None:
    if not SKILLS_DIR.is_dir():
        errors.append("skills/: directory missing")
        return
    children = [p for p in SKILLS_DIR.iterdir() if p.name != ".DS_Store"]
    dirs = [p for p in children if p.is_dir()]
    if len(dirs) != 1 or dirs[0].name != CONNECT_SKILL_DIR:
        names = sorted(p.name for p in dirs)
        errors.append(
            f"skills/: must contain exactly one directory {CONNECT_SKILL_DIR!r}, found {names!r}"
        )
        return
    skill_md = dirs[0] / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"skills/{CONNECT_SKILL_DIR}/SKILL.md: missing")
        return
    try:
        text = skill_md.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"skills/{CONNECT_SKILL_DIR}/SKILL.md: cannot read ({exc})")
        return
    fm_name = parse_skill_frontmatter_name(text)
    if fm_name != CONNECT_SKILL_DIR:
        errors.append(
            f"skills/{CONNECT_SKILL_DIR}/SKILL.md: frontmatter name must be {CONNECT_SKILL_DIR!r}"
        )


def main() -> int:
    errors: list[str] = []
    version = check_versioned_manifests(errors)
    check_claude_marketplace(errors, version)
    check_root_plugin_json(errors)
    check_platform_plugins(errors)
    check_gemini_extension(errors)
    check_agents_marketplace(errors)
    check_package_files(errors)
    check_readme(errors)
    check_skills_layout(errors)
    if errors:
        for message in errors:
            err(message)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())