---
name: connect-ysskrishna-mcp
description: Connect an AI client to the public, read-only ysskrishna MCP server. Use when asked to install, configure, verify, or remove this specific MCP connection.
license: MIT
---

# Connect ysskrishna MCP

The remote Streamable HTTP endpoint is `https://www.ysskrishna.space/mcp`. It provides read-only search, fetch and tag listing for public site content (products, blog posts, tools and courses); it does not run the site's tools. Searches go to the remote server, so do not send sensitive information. No API key is needed.

## Setup

1. Identify the client and the intended configuration scope from the request and environment. If either is unclear and would change the files or users affected, ask. Do not configure other clients or scopes without being asked.
2. Inspect the client's existing MCP entries using its documented listing command or settings UI. If `ysskrishna` already points to this endpoint, leave it intact and verify it. If the name points elsewhere, or a different entry already uses the endpoint, explain the conflict and ask before changing anything. Preserve unrelated configuration and tool trust settings.
3. Add only the missing entry using the client's supported command or UI. Examples below are documented client commands, not a guarantee that a particular client version is compatible. Verify installed CLI help and supported scope before running. The user's request to connect authorizes the necessary configuration change within the chosen scope; respect host permission requirements.
4. Check the entry is present, then attempt client-native discovery of the `search`, `fetch` and `list_tags` tools and a small public search when the client permits it. Report configuration and connection status separately. If the server is disabled, unavailable, or blocked by client policy, say so and preserve the configuration. Do not claim success based only on an entry being present. Avoid repeated retries, credentials, automatic trust, proxies, and unrelated installations.

## Tools

The server exposes `search`, `fetch` and `list_tags`.

**`search`** accepts:

- `query` (string, required; an empty string browses)
- `type` (`all` | `product` | `blog` | `tool` | `course`)
- `tags` (exact lowercase kebab-case ids, any-match; for example `markdown-and-docs`; display names such as Markdown do not match; `list_tags` returns the ids, and an unknown tag error suggests close ids)
- `featured` (boolean)
- `sort` (`auto` | `updated` | `created` | `az`)
- `page` (integer, starts at 1)

Every search response includes `results` (up to 12 items with `id`, `title`, `url`, `type`, `summary`, `tags`, `createdAt`, and `updatedAt` when the item was updated) and `pagination` (`total`, `page`, `pageCount`). Dates are ISO 8601 UTC, for example `2026-11-19T00:00:00.000Z`.

Example: search with an empty `query`, `tags` set to `markdown-and-docs`, and `type` `tool`.

**`fetch`** accepts `id`, which must be an id returned by search: `product:<number>`, `blog:<slug>`, `tool:<slug>`, or `course:<slug>`. A course id returns that course, not one chapter. A URL or a bare slug is not an id. It returns `id`, `title`, `text` (Markdown), `url` and `metadata` (`type`, `tags`, `createdAt`, and `updatedAt` when the item was updated).

**`list_tags`** takes no arguments and returns `tags`, each with `id`, `name`, `group` and `count`.

## Client commands

- **Codex:** `codex mcp list`, then `codex mcp add ysskrishna --url https://www.ysskrishna.space/mcp` if missing. Codex CLI and IDE share configuration; this command normally changes user configuration. Inspect the installed version's help for other scopes.
- **Claude Code:** `claude mcp list`, then `claude mcp add --transport http --scope user ysskrishna https://www.ysskrishna.space/mcp` for user scope. For a project or local scope, use the applicable documented `--scope` value. Check `/mcp` in a session for connection and tools.
- **Gemini CLI:** `gemini mcp list`, then `gemini mcp add --transport http --scope user ysskrishna https://www.ysskrishna.space/mcp` for user scope, or `--scope project` when requested. Check `/mcp` for tools.
- **VS Code:** use the MCP server settings UI or `MCP: Add Server`, select HTTP, enter the endpoint and `ysskrishna`, and choose the requested configuration destination. Start the server and inspect its tools.
- **Cursor:** add the endpoint as a remote HTTP server in Cursor's MCP settings for the requested scope. Preserve existing entries and check connection status in the client.
- **Other clients:** consult that client's current official documentation for Streamable HTTP, scopes, configuration and verification. Do not guess a config path or use a stdio bridge unless explicitly requested.

## Removal

Only remove the entry in the requested client and scope. Verify the entry points at `https://www.ysskrishna.space/mcp` before removing it. Leave other servers and this skill in place unless the user also asks to remove those.

- **Claude Code (user scope):** `claude mcp remove ysskrishna -s user`
- **Codex:** `codex mcp remove ysskrishna`
- **Gemini CLI (user scope):** `gemini mcp remove --scope user ysskrishna`
- **VS Code and Cursor:** use that client's MCP settings UI (no documented remove CLI in this skill)

For MCP removal, use the client's command or UI. Removing the skill is separate and depends on how it was installed. `gh skill` has no uninstall; delete the skill directory that install created. For skills.sh, run `npx skills remove connect-ysskrishna-mcp`.
