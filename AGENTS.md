# Maintainer guide

This repository ships one agent skill (`skills/connect-ysskrishna-mcp`), host-specific plugin manifests, and a root `index.js` for OpenCode. The skill tells agents how to connect to the hosted MCP; manifests declare the plugin for each host.

## Layout

| Piece | Role |
| ----- | ---- |
| `skills/connect-ysskrishna-mcp/` | The skill (endpoint and usage) |
| `plugin.json`, `package.json`, `.*-plugin/`, `gemini-extension.json` | Host manifests and metadata |
| `index.js` | OpenCode: registers skills from `skills/` only — no MCP server, no extra tools |

## Endpoint URL

Keep **`https://www.ysskrishna.space/mcp`** in the skill and human-readable docs. Do **not** put that URL in JSON manifest files.

## Version bumps (1.0.0 scope)

Use a single release version everywhere:

`plugin.json`, `package.json`, `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `.kimi-plugin/plugin.json`, `gemini-extension.json`, and both version fields in `.claude-plugin/marketplace.json`.

1. Run `python3 scripts/bump_version.py X.Y.Z`.
2. Update `CHANGELOG.md` manually for the release.
3. Run `bash validate-skills.sh` before you consider the change done.

## Host notes

- **Cursor**: `.cursor-plugin/plugin.json` author is name only (no email required in the manifest).
- **Claude marketplace**: one entry for this skill — do not add a duplicate marketplace listing.

## Out of scope for 1.0.0

No ClawHub, `openclaw.plugin.json`, evals, or logo assets in this release.