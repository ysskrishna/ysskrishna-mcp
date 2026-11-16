# Kimi Code

## Install

Inside Kimi Code:

```text
/plugins install https://github.com/ysskrishna/ysskrishna-mcp
```

Choose **Trust and install**, then run `/reload` or start a new session.

Without a plugin, Kimi reads `~/.agents/skills` and `.agents/skills`, so `npx skills add ysskrishna/ysskrishna-mcp` also works.

## Connect the MCP server

Ask the agent to use `connect-ysskrishna-mcp`; if the skill does not know the client, add Streamable HTTP name `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.