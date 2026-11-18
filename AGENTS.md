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

## Version bumps

Use a single release version everywhere:

`plugin.json`, `package.json`, `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `.kimi-plugin/plugin.json`, `gemini-extension.json`, and both version fields in `.claude-plugin/marketplace.json`.

1. Run `python3 scripts/bump_version.py X.Y.Z`.
2. Update `CHANGELOG.md` manually for the release.
3. Run `bash validate-skills.sh` before you consider the change done.

## Host notes

- **Cursor**: `.cursor-plugin/plugin.json` author is name only (no email required in the manifest).
- **Claude marketplace**: one entry for this skill — do not add a duplicate marketplace listing.

## Out of scope

No ClawHub, `openclaw.plugin.json`, evals, or logo assets.

## Releases

What is **already published** lives in [docs/contributing/release-state.md](docs/contributing/release-state.md). When the owner asks to ship a release:

1. Run `python3 scripts/bump_version.py X.Y.Z`. Confirm that version in `plugin.json`, `package.json`, `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `.kimi-plugin/plugin.json`, `gemini-extension.json`, and both version fields in `.claude-plugin/marketplace.json`. Add a `## [X.Y.Z]` section at the top of `CHANGELOG.md` with a footer compare link.
2. Ensure those changes are on `main` (`git pull origin main`).
3. Run `bash validate-skills.sh` and `node --check index.js` on `main`.
4. Create an annotated tag `vX.Y.Z` on that `main` commit and `git push origin vX.Y.Z`. The tag name must match `plugin.json`. [`.github/workflows/release.yml`](.github/workflows/release.yml) uses `ysskrishna/changelog-release-action@v1` to create the GitHub Release from the matching nonempty `CHANGELOG.md` section, titled `Release <tag>`. Missing or empty notes fail; there is no fallback. The same tag runs [`.github/workflows/publish-npm.yml`](.github/workflows/publish-npm.yml), which publishes `@ysskrishna/ysskrishna-mcp`.
5. Confirm the GitHub Release and the npm version, then update `docs/contributing/release-state.md` (version, tag, `main` commit, release URL, npm URL).

GitHub About fields (description, homepage, topics) are repository settings, not files. Keep the description aligned with `package.json`, the homepage at `https://ysskrishna.space/`, and topics that include `gemini-cli-extension` so the Gemini CLI gallery can list the extension. This repo has no custom social preview image. GitHub shows its automatic card. Do not add a preview image unless the owner asks.

Do not create tags or GitHub releases unless the owner asks. This repo does not publish to ClawHub.

## Commits and PRs

- Short imperative subject that says what changed and why.
- No `Co-Authored-By` line and no "Generated with" line.

## Security

Never put tokens or user data in the repo or in examples. Report vulnerabilities through GitHub private reporting, as in [SECURITY.md](SECURITY.md).