# OpenCode

## Install

From npm:

```bash
opencode plugin @ysskrishna/ysskrishna-mcp --global
```

OpenCode 1.x, in `opencode.json`:

```json
{
  "plugin": ["@ysskrishna/ysskrishna-mcp"]
}
```

```json
{
  "plugin": ["ysskrishna-mcp@git+https://github.com/ysskrishna/ysskrishna-mcp.git"]
}
```

OpenCode 2.0.4 or later uses the key `plugins`:

```json
{
  "plugins": ["@ysskrishna/ysskrishna-mcp"]
}
```

Restart OpenCode.

Without a plugin, OpenCode also reads `.agents/skills`, so this works:

```bash
npx skills add ysskrishna/ysskrishna-mcp
```

## Connect the MCP server

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.