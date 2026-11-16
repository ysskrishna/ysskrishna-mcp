# Gemini CLI

## Install

As an extension:

```bash
gemini extensions install https://github.com/ysskrishna/ysskrishna-mcp
```

Or install only the skills:

```bash
gemini skills install https://github.com/ysskrishna/ysskrishna-mcp.git --path skills
```

Add `--consent` to skip the confirmation prompt. Add `--scope workspace` to limit skills to the current project.

## Connect the MCP server

After the skill is installed:

```bash
gemini mcp list
gemini mcp add --transport http --scope user ysskrishna https://www.ysskrishna.space/mcp
```

Use `--scope project` when requested. Check `/mcp` for tools.

## Update and remove

```bash
gemini extensions update ysskrishna-mcp
gemini extensions uninstall ysskrishna-mcp
```

The extension install uses the latest GitHub Release, not the default branch.