# ysskrishna MCP setup skill

An Agent Skill that helps an AI agent connect a supported client to the public, read-only ysskrishna MCP server. The server searches and reads public products, blog posts, and tools. It does not execute the website's tools.

The server must be deployed and enabled before connection can work. Client-specific setup and end-to-end compatibility have not yet been verified.

## Install the skill

Install the skill using a compatible skills installer:

```bash
npx skills add ysskrishna/ysskrishna-mcp
```

Choose the agent and scope in the installer. Restart the agent if it does not discover the skill immediately. Installing the skill does not connect the MCP server.

Then ask your agent:

> Use the connect-ysskrishna-mcp skill to connect ysskrishna MCP to my AI tool.

The agent identifies the requested client and scope, checks the existing configuration, adds the server when needed, and verifies the connection where the client supports it. It will not replace a conflicting entry silently. The endpoint is `https://www.ysskrishna.space/mcp`; searches are sent to the remote server, so do not include sensitive information.

The skill contains setup routes for Codex, Claude Code, Gemini CLI, VS Code and Cursor, with a documentation-based fallback for other Streamable HTTP clients. These are setup instructions, not claims that every client or version has been tested. The server may be disabled by its operator.

## Remove

Ask the agent to remove the `ysskrishna` MCP connection in the desired client and scope. Remove the skill separately using the same tool used to install it.

## License

MIT. See [LICENSE](LICENSE).
