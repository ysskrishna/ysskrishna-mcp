# Muse

Set `MUSE_EXPERIMENTAL_PLUGINS=1` before plugin commands.

## Install

```bash
git clone https://github.com/ysskrishna/ysskrishna-mcp.git
export MUSE_EXPERIMENTAL_PLUGINS=1
muse plugins install ./ysskrishna-mcp --scope user
muse plugins approve ysskrishna-mcp
```

## Connect the MCP server

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

## Update and remove

```bash
muse plugins update ysskrishna-mcp
muse plugins remove ysskrishna-mcp
```