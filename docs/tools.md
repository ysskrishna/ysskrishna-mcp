# ysskrishna MCP tools

The server at `https://www.ysskrishna.space/mcp` uses Streamable HTTP, needs no API key and is read-only. It exposes three tools, `search`, `fetch` and `list_tags`, over the public products, blog posts, tools and courses on ysskrishna.space. Searches go to the remote server, so do not send sensitive information.

The server is stateless, so it does not send `notifications/tools/list_changed` (`capabilities.tools.listChanged` is `false`). It accepts requests with no `Origin` header, which is what server-side clients send, and requests from ysskrishna.space itself. Any other `Origin`, for example a browser-based client on another site, gets HTTP 403.

## Connect

Claude Code:

```bash
claude mcp add --transport http --scope user ysskrishna https://www.ysskrishna.space/mcp
```

Codex CLI:

```bash
codex mcp add ysskrishna --url https://www.ysskrishna.space/mcp
```

Gemini CLI:

```bash
gemini mcp add --transport http --scope user ysskrishna https://www.ysskrishna.space/mcp
```

Cursor (`~/.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "ysskrishna": {
      "url": "https://www.ysskrishna.space/mcp"
    }
  }
}
```

Setup guides for other agents are in this `docs/` folder.

## search

Search or browse public products, blog posts, tools and courses. Each page has up to 12 results, and every response includes `pagination`.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `query` | string, max 200 chars | Yes | Text to search. Use an empty string to browse everything. |
| `type` | `all` \| `product` \| `blog` \| `tool` \| `course` | No | Content type filter. Omit it or use `all` for every type. |
| `tags` | array of up to 10 strings | No | Exact lowercase kebab-case tag ids, for example `markdown-and-docs`. Display names such as `Markdown` do not match. Several tags match any of them. Call `list_tags` for the ids. |
| `featured` | boolean | No | When `true`, only featured items. |
| `sort` | `auto` \| `updated` \| `created` \| `az` | No | `auto` ranks by relevance when `query` is not empty, otherwise newest updated first. `updated` and `created` are newest first. `az` is A to Z by title. |
| `page` | integer, 1 to 1000 | No | 1-based page number. |

Each result has:

| Field | Description |
| --- | --- |
| `id` | Pass it to `fetch`. |
| `title` | Page title. |
| `url` | Public page URL. |
| `type` | `product`, `blog`, `tool` or `course`. |
| `summary` | One-line description, at most 200 characters. Left out when the item has none. |
| `tags` | Tag ids, the same ids `tags` and `list_tags` use. |
| `createdAt` | When the item was published. |
| `updatedAt` | When the item was last updated. Left out when the item was never updated; `sort: "updated"` then uses `createdAt`. |

Dates are ISO 8601 in UTC with milliseconds, for example `2026-11-19T00:00:00.000Z`. `fetch` uses the same format.

Browse tools tagged `markdown-and-docs`:

```json
{
  "name": "search",
  "arguments": { "query": "", "type": "tool", "tags": ["markdown-and-docs"] }
}
```

Response (first 2 of 5 results):

```json
{
  "results": [
    {
      "id": "tool:markdown-to-outlook",
      "title": "Markdown to Outlook Converter",
      "url": "https://www.ysskrishna.space/tools/markdown-to-outlook",
      "type": "tool",
      "summary": "Free Markdown to Outlook converter with live preview and one-click rich paste.",
      "tags": ["content-and-writing", "markdown-and-docs", "text-and-data-conversion"],
      "createdAt": "2026-10-09T00:00:00.000Z"
    },
    {
      "id": "tool:markdown-editor-preview",
      "title": "Markdown Editor With Live Preview",
      "url": "https://www.ysskrishna.space/tools/markdown-editor-preview",
      "type": "tool",
      "summary": "Free online Markdown editor with live preview, tables, code highlighting, and Mermaid diagrams.",
      "tags": ["content-and-writing", "markdown-and-docs"],
      "createdAt": "2026-10-02T00:00:00.000Z"
    }
  ],
  "pagination": { "total": 5, "page": 1, "pageCount": 1 }
}
```

Page through blog posts, newest updated first:

```json
{
  "name": "search",
  "arguments": { "query": "", "type": "blog", "sort": "updated", "page": 2 }
}
```

Use `pagination.pageCount` to know when to stop.

An unknown tag returns a tool error that suggests close tag ids. For `{"query": "", "tags": ["markdown"]}`:

```text
Unknown or unavailable tag: markdown. Did you mean: markdown-and-docs? Call list_tags to see every tag id.
```

A page past the end returns `Page is out of range.`

## fetch

Read the full public content of one search result.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string, max 200 chars | Yes | An id returned by `search`: `product:<number>`, `blog:<slug>`, `tool:<slug>` or `course:<slug>`. A course id is the course, not a chapter. |

```json
{
  "name": "fetch",
  "arguments": { "id": "tool:markdown-to-slack" }
}
```

The structured result has `id`, `title`, `text` (the page content as Markdown, with at most one blank line in a row outside code blocks), `url` and `metadata` (`type`, `tags`, `createdAt`, and `updatedAt` when the item was updated):

```json
{
  "id": "tool:markdown-to-slack",
  "title": "Markdown to Slack Converter",
  "text": "Preview Markdown in a Slack-style layout, then copy rich HTML to paste into Slack from your browser. ...",
  "url": "https://www.ysskrishna.space/tools/markdown-to-slack",
  "metadata": {
    "type": "tool",
    "tags": ["content-and-writing", "markdown-and-docs", "text-and-data-conversion"],
    "createdAt": "2026-10-02T00:00:00.000Z"
  }
}
```

A bare slug or a URL is not an id. `{"id": "markdown-to-slack"}` returns a tool error: `Content not found. Use an id returned by search, for example product:61, blog:<slug>, tool:<slug>, or course:<slug>.`

## list_tags

List the tag ids used by public content, for the `search` `tags` filter. It takes no arguments.

```json
{
  "name": "list_tags",
  "arguments": {}
}
```

Each tag has `id`, `name` (display name), `group` and `count` (the number of items with that tag, which equals that tag's `search` total). Tags are sorted by `id`. Counts change as content is added. Response (3 of the tags):

```json
{
  "tags": [
    { "id": "google-sheets", "name": "Google Sheets", "group": "tech", "count": 11 },
    { "id": "markdown-and-docs", "name": "Markdown & Docs", "group": "themes", "count": 11 },
    { "id": "mcp", "name": "MCP", "group": "tech", "count": 2 }
  ]
}
```
