# Other agents

## skills.sh

```bash
npx skills add ysskrishna/ysskrishna-mcp
npx skills add ysskrishna/ysskrishna-mcp --list
npx skills add ysskrishna/ysskrishna-mcp --skill connect-ysskrishna-mcp --agent cursor
```

The [skills CLI](https://github.com/vercel-labs/skills) copies each skill into the folder your agent reads.

```bash
npx skills remove connect-ysskrishna-mcp
```

See `npx skills remove --help` for global scope and per-agent options.

Set `DISABLE_TELEMETRY=1` to turn off install telemetry.

## GitHub CLI

Requires GitHub CLI v2.90.0 or later and `gh auth login`.

```bash
gh skill install ysskrishna/ysskrishna-mcp
gh skill install ysskrishna/ysskrishna-mcp connect-ysskrishna-mcp
gh skill install ysskrishna/ysskrishna-mcp connect-ysskrishna-mcp --agent codex --scope user
```

Run `gh skill install --help` for the full agent list. `gh skill` has install, list, preview, publish, search, and update — no remove or uninstall. Delete the skill directory the install step created.

## Any agent that reads SKILL.md

Copy `skills/connect-ysskrishna-mcp/` into the folder your agent reads, or point your agent at this repo. The file follows the [Agent Skills](https://agentskills.io/) standard.

Ask the agent to use `connect-ysskrishna-mcp`. If the skill does not know the client, add a Streamable HTTP server named `ysskrishna` at `https://www.ysskrishna.space/mcp` with no API key, using that client's own docs.