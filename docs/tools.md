# ysskrishna MCP tools

The server at `https://www.ysskrishna.space/mcp` uses Streamable HTTP, needs no API key and is read-only. It exposes two tools, `search` and `fetch`, over the public products, blog posts and tools on ysskrishna.space. Searches go to the remote server, so do not send sensitive information.

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

Search or browse public products, blog posts and tools. Each page has up to 12 results, and every response includes `pagination`.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `query` | string, max 200 chars | Yes | Text to search. Use an empty string to browse everything. |
| `type` | `all` \| `product` \| `blog` \| `tool` | No | Content type filter. Omit it or use `all` for every type. |
| `tags` | array of up to 10 strings | No | Exact lowercase kebab-case tag ids, for example `markdown-and-docs`. Display names such as `Markdown` do not match. Several tags match any of them. |
| `featured` | boolean | No | When `true`, only featured items. |
| `sort` | `auto` \| `updated` \| `created` \| `az` | No | `auto` ranks by relevance when `query` is not empty, otherwise newest updated first. `updated` and `created` are newest first. `az` is A to Z by title. |
| `page` | integer, 1 to 1000 | No | 1-based page number. |

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
    { "id": "tool:markdown-to-outlook", "title": "Markdown to Outlook Converter", "url": "https://www.ysskrishna.space/tools/markdown-to-outlook" },
    { "id": "tool:markdown-editor-preview", "title": "Markdown Editor With Live Preview", "url": "https://www.ysskrishna.space/tools/markdown-editor-preview" }
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

## fetch

Read the full public content of one search result.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string, max 200 chars | Yes | An id returned by `search`: `product:<number>`, `blog:<slug>` or `tool:<slug>`. |

```json
{
  "name": "fetch",
  "arguments": { "id": "tool:markdown-to-slack" }
}
```

The structured result has `id`, `title`, `text` (the page content as Markdown), `url` and `metadata` (`type`, `tags`, `createdAt`):

```json
{
  "id": "tool:markdown-to-slack",
  "title": "Markdown to Slack Converter",
  "text": "Preview Markdown in a Slack-style layout, then copy rich HTML to paste into Slack from your browser. ...",
  "url": "https://www.ysskrishna.space/tools/markdown-to-slack",
  "metadata": {
    "type": "tool",
    "tags": ["content-and-writing", "markdown-and-docs", "text-and-data-conversion"],
    "createdAt": "2026-10-02"
  }
}
```

A bare slug or a URL is not an id. `{"id": "markdown-to-slack"}` returns a tool error: `Content not found. Use an id returned by search, for example product:61, blog:<slug>, or tool:<slug>.`
