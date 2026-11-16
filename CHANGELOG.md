# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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