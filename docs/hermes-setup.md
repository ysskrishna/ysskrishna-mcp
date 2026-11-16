# Hermes Agent

## Install (recommended: skills tap)

```bash
hermes skills tap add ysskrishna/ysskrishna-mcp
hermes skills install ysskrishna/ysskrishna-mcp/connect-ysskrishna-mcp
```

## Connect the MCP server

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

## Update and remove

```bash
hermes skills update
hermes skills uninstall connect-ysskrishna-mcp
hermes skills tap remove ysskrishna/ysskrishna-mcp
```

Plugin route (`hermes plugins install ysskrishna/ysskrishna-mcp --enable`) also works, but Hermes does not advertise plugin skills to the model; prefer the tap.