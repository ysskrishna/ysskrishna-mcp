# Pi

## Install

```bash
pi install npm:@ysskrishna/ysskrishna-mcp
```

```bash
pi install git:github.com/ysskrishna/ysskrishna-mcp
```

Add `-l` to install for the current project only.

## Connect the MCP server

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.

## Update and remove

```bash
pi update
pi remove npm:@ysskrishna/ysskrishna-mcp
pi remove git:github.com/ysskrishna/ysskrishna-mcp
```