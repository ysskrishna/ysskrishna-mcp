# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- **Tool docs.** Document the new `list_tags` tool, the richer `search` results (`type`, `summary`, `tags`, `createdAt`, `updatedAt`), ISO 8601 UTC dates, the rule for a missing `updatedAt`, the current not-found and unknown-tag errors, `listChanged: false`, and the `Origin` policy for browser-based clients.

## [1.0.3] - 2026-11-19

### Changed

- **Courses.** `search` accepts `type` `course`. `fetch` accepts `course:<slug>` for a whole course. Skill, tools doc, and Context7 rules match the site catalog.

[1.0.3]: https://github.com/ysskrishna/ysskrishna-mcp/compare/v1.0.2...v1.0.3

## [1.0.2] - 2026-11-16

### Changed

- **Skill and docs.** Document `search` and `fetch` tool arguments and responses, and document MCP removal commands for Claude Code, Codex, and Gemini CLI. Clarify that `gh skill` has no uninstall and how to remove skills installed via `gh skill` or skills.sh.

[1.0.2]: https://github.com/ysskrishna/ysskrishna-mcp/compare/v1.0.1...v1.0.2

## [1.0.1] - 2026-11-16

### Changed

- **Discovery metadata.** Plugin and npm keywords now name the MCP server and the hosts that install this skill. The Cursor plugin category is `developer-tools`, with tags for marketplace filtering. Codex and the agents marketplace stay in `Productivity`.
- **Release steps.** `AGENTS.md` records how to tag `main`, let GitHub create the Release, and publish npm. `docs/contributing/release-state.md` records what is already published.

[1.0.1]: https://github.com/ysskrishna/ysskrishna-mcp/compare/v1.0.0...v1.0.1

## [1.0.0] - 2026-11-16

### Added

- **npm package and OpenCode entry.** Publishes `@ysskrishna/ysskrishna-mcp`; `index.js` registers the skill for OpenCode.
- **Install documentation.** `README.md` and `docs/` describe how to install the plugin or skill per host.
- **skills.sh manifest.** `skills.sh.json` for skills.sh discovery and install.
- **GitHub automation.** Workflows validate manifests and README (`validate-skills`), create GitHub Releases from tags (`release`), and publish to npm with OIDC (`publish-npm`).

### Changed

- **Plugin manifests.** Root and host-specific manifest versions are aligned at `1.0.0` for the first public release.
- **Cursor plugin author.** `.cursor-plugin/plugin.json` author is limited to `name` so it matches Cursor's plugin schema.
- **Codex MCP command.** `codex mcp add ysskrishna --url https://www.ysskrishna.space/mcp` matches the installed Codex CLI help. A throwaway config add did not modify the real Codex config. A Cursor UI session was not run.

[1.0.0]: https://github.com/ysskrishna/ysskrishna-mcp/releases/tag/v1.0.0