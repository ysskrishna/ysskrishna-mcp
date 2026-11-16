# Claude Code

## Install

```text
/plugin marketplace add ysskrishna/ysskrishna-mcp
/plugin install ysskrishna-mcp@ysskrishna-mcp
```

From a terminal:

```bash
claude plugin marketplace add ysskrishna/ysskrishna-mcp
claude plugin install ysskrishna-mcp@ysskrishna-mcp
```

## Connect the MCP server

After the skill is installed, ask the agent to use `connect-ysskrishna-mcp`, or run:

```bash
claude mcp list
claude mcp add --transport http --scope user ysskrishna https://www.ysskrishna.space/mcp
```

For a project or local scope, use the applicable documented `--scope` value. Check `/mcp` in a session for connection and tools.

## Update and remove

```text
/plugin marketplace update ysskrishna-mcp
/plugin uninstall ysskrishna-mcp@ysskrishna-mcp
```

If `marketplace add owner/repo` fails with `Permission denied (publickey)`, run `git config --global url."https://github.com/".insteadOf git@github.com:` once.