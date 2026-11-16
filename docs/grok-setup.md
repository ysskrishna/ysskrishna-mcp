# Grok Build

## Install

```bash
grok plugin install ysskrishna/ysskrishna-mcp --trust
```

Without `--trust`, Grok prints a warning and stops.

## Connect the MCP server

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

## Update and remove

```bash
grok plugin update ysskrishna-mcp
grok plugin uninstall ysskrishna-mcp
```

Install directly. Do not use `grok plugin marketplace add` with this repo.