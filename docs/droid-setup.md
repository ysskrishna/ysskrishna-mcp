# Factory Droid

## Install

```bash
droid plugin marketplace add ysskrishna/ysskrishna-mcp
droid plugin install ysskrishna-mcp@ysskrishna-mcp --scope user
```

Use `--scope project` to limit it to the current repo.

## Connect the MCP server

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

## Update and remove

```bash
droid plugin update ysskrishna-mcp@ysskrishna-mcp
droid plugin uninstall ysskrishna-mcp@ysskrishna-mcp
```