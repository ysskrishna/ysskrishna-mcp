# GitHub Copilot CLI

## Install

```bash
copilot plugin marketplace add ysskrishna/ysskrishna-mcp
copilot plugin install ysskrishna-mcp@ysskrishna-mcp
```

Through GitHub CLI instead:

```bash
gh skill install ysskrishna/ysskrishna-mcp --agent github-copilot
```

## Connect the MCP server

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

## Update and remove

```bash
copilot plugin update ysskrishna-mcp
copilot plugin uninstall ysskrishna-mcp
```

Do not use `copilot plugin install ysskrishna/ysskrishna-mcp`. Direct installs still work but are deprecated.