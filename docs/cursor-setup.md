# Cursor

## Install

Plugin route:

1. Open **Customize, Plugins, Add, From GitHub Repository**.
2. Enter `github.com/ysskrishna/ysskrishna-mcp`.

In Agent chat you can also run `/add-plugin` and give the repo.

Skills-only route:

```bash
npx skills add ysskrishna/ysskrishna-mcp --agent cursor
```

Cursor reads skills from `.cursor/skills`, `.agents/skills` and `~/.cursor/skills`.

## Connect the MCP server

After the skill is installed, add the endpoint as a remote HTTP server in Cursor's MCP settings for the requested scope.

Cursor's docs use `mcpServers.<name>.url` in `.cursor/mcp.json` (project) or `~/.cursor/mcp.json` (global). This was not added to a live Cursor config.

## Update and remove

Use the plugin's menu in **Customize, Plugins**. For the skills route, run `npx skills add` again to update.