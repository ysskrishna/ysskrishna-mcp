# Codex CLI and App

Needs Codex CLI v0.122 or later.

## Install

```bash
codex plugin marketplace add ysskrishna/ysskrishna-mcp
codex plugin add ysskrishna-mcp@ysskrishna-mcp
```

Start a new session afterwards. Codex loads plugin skills only in new sessions.

## Connect the MCP server

After the skill is installed:

```bash
codex mcp list
codex mcp add ysskrishna --url https://www.ysskrishna.space/mcp
```

The installed Codex CLI accepts `codex mcp add ysskrishna --url https://www.ysskrishna.space/mcp`; a throwaway `CODEX_HOME` add/list/get on 2026-11-16 stored transport `streamable_http` and left the real config unchanged.

## Update and remove

```bash
codex plugin marketplace upgrade ysskrishna-mcp
codex plugin remove ysskrishna-mcp@ysskrishna-mcp
```

The Codex IDE extension has no plugin support.